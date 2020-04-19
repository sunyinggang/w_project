#coding=utf-8
import calendar
import json
import os
import re
import datetime
from functools import wraps

from dateutil.relativedelta import relativedelta
from flask import render_template, flash, redirect, url_for, session, request, jsonify,abort
from sqlalchemy import or_, func
from werkzeug.security import generate_password_hash

from . import admin
from .forms import LoginForm, ChangeForm, DriverForm, CarForm, NoticeForm, ScheduleForm, ExpenseTypeForm, ExpenseForm, \
    BecauseForm, AuthForm, RoleForm, AdminForm
from .. import db,app
from ..lib.functions import change_filename, curl, geocode_curl, driving_curl
from ..models import Admin, Driver, Car, Notice, ExpenseType, Expense, Schedule, Track, Leave, Auth, Role


def admin_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "id" not in session:
            return redirect(url_for("admin.login",next=request.url))
        return f(*args, **kwargs)
    return decorated_function

#权限控制装饰器
def admin_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        admin = Admin.query.join(
            Role
        ).filter(
            Role.id == Admin.role_id,
            Admin.id == session["id"]
        ).first()
        auths = admin.role.auths
        if auths != '':
            auths = list(map(lambda v: int(v), auths.split(",")))
            auth_list = Auth.query.all()
            urls = [v.url for v in auth_list for val in auths if val == v.id]
            rule = request.url_rule
            if str(rule) not in urls:
                abort(404)
        return f(*args, **kwargs)

    return decorated_function

@admin.route("/login/",methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(phone=data["phone"]).first()
        if not admin:
            flash("用户不存在！","err")
            return redirect(url_for("admin.login"))
        if not admin.check_pwd(data["password"]):
            flash("密码错误！", "err")
            return redirect(url_for("admin.login"))
        session["name"] = admin.name
        session["id"] = admin.id
        session["is_super"] = admin.is_super
        return redirect(request.args.get("next") or url_for("admin.index"))
    return render_template("admin/login.html",form=form)

@admin.route("/changePwd/",methods=["GET","POST"])
@admin_login_req
def changePwd():
    form = ChangeForm()
    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(id=session["id"]).first()
        if not admin.check_pwd(data["password"]):
            flash("旧密码错误！", "err")
            return redirect(url_for("admin.changePwd"))
        rule = re.match("^\S{6,10}$", data["newpassword"])
        if not rule:
            flash("新密码为6~15位！", "err")
            return redirect(url_for("admin.changePwd"))
        if data["newpassword"] != data["newpasswordt"]:
            flash("两次新密码不同！", "err")
            return redirect(url_for("admin.changePwd"))
        admin.password = generate_password_hash(data["newpassword"])
        db.session.add(admin)
        db.session.commit()
        flash("密码修改成功,请重新登录！", "ok")
        return redirect(url_for("admin.logout"))
    return render_template("admin/changepwd.html",form=form)

@admin.route("/logout/")
def logout():
    session.pop("name",None)
    session.pop("id", None)
    session.pop("is_super", None)
    return redirect(url_for("admin.login"))

@admin.route("/")
@admin_login_req
def index():
    # 近6个月的累计排班数据处理
    halfYearSchedules = {
                "labels": [],
                "datasets": [{
                    "label": '次数',
                    "backgroundColor": 'rgb(42, 222, 96)',
                    "borderColor": 'rgb((42, 222, 96)',
                    "data": []
                }]
            }
    time_list, temp = halfYear()
    halfYearSchedules['labels'] = time_list
    count_list = []
    for v in temp:
        count = Schedule.query.filter(Schedule.start_time.between(v[0], v[1])).count()
        count_list.append(count)
    halfYearSchedules['datasets'][0]['data'] = count_list
    # 近6个月累积里程和行驶时长
    travelSummary = {
            "labels": [],
            "datasets": [
                {
                    "label": "里程(公里)",
                    "borderColor": "rgb(43, 144, 255)",#路径颜色
                    "pointBackgroundColor": "rgb(43, 144, 255)",#定点填充色
                    "data": []
                },
                {
                    "label": "时长(小时)",
                    "borderColor": "rgb(255, 174, 0)",#路径颜色
                    "pointBackgroundColor": "rgb(255, 174, 0)",#定点填充色
                    "data": []
                }
            ]
        }
    travelSummary['labels'] = time_list
    travel_list0 = []
    travel_list1 = []
    for v in temp:
        track = Track.query.filter(Track.end_time.between(v[0], v[1])).all()
        sum = 0
        hour = 0
        for i in track:
            sum = sum + int(i.distance)
            hour = hour + int(i.duration)
        travel_list0.append(round(sum*0.001,1))
        travel_list1.append(round(hour/3600,1))
    travelSummary['datasets'][0]['data'] = travel_list0
    travelSummary['datasets'][1]['data'] = travel_list1
    # 近6个月利润、收入、支出
    # 车辆监控
    carMonitorChart = {
                "labels": ['空闲车辆', '行驶车辆', '检修车辆'],
                "datasets": [
                    {
                        "backgroundColor": ["rgb(52,207,104)", "rgb(40,174,219)", "rgb(222,71,29)"],
                        "data": []
                    }
                ]
            }
    car_list = [0,0,0]
    car_count = db.session.query(Car.status,func.count(Car.status)).group_by(Car.status).all()
    for v in car_count:
        car_list[v[0]] = v[1]
    carMonitorChart['datasets'][0]['data'] = car_list
    # 今日排班与明日排班数量统计
    scheduleToday,scheduleTomorrow = scheduleTodayAndTomorrow()
    # 近6个月利润、收入、支出
    financialChart = {
                "labels": [],
                "datasets": [
                    {
                        "label": '利润',
                        "data": [],
                        "backgroundColor": "rgb(255, 142, 100)"
                    },
                    {
                        "label": '收入',
                        "data": [],
                        "backgroundColor": "rgb(38, 247, 206)"
                    },
                    {
                        "label": '支出',
                        "data": [],
                        "backgroundColor": "rgb(1, 168, 250)"
                    }
                ]
            }
    financialChart['labels'] = time_list
    expense_in_list = []
    expense_out_list = []
    expense_profit_list = []
    for v in temp:
        expense = Expense.query.filter(Expense.end_time.between(v[0], v[1])).filter(Expense.status==1).all()
        schedule = Schedule.query.filter(Schedule.end_time.between(v[0], v[1])).filter(Expense.status == 3).all()
        expense_in = 0
        expense_out = 0
        for v in expense:
            if v.expense_type.type == '收入':
                expense_in += int(v.money)
            else:
                expense_out -= int(v.money)
        for i in schedule:
            money = int(i.money) - int(i.driver_money)
            expense_in += money
        expense_in_list.append(expense_in)
        expense_out_list.append(expense_out)
        expense_profit_list.append(expense_in + expense_out)
    financialChart['datasets'][0]['data'] = expense_profit_list
    financialChart['datasets'][1]['data'] = expense_in_list
    financialChart['datasets'][2]['data'] = expense_out_list
    return render_template("admin/index.html",halfYearSchedules=json.dumps(halfYearSchedules,ensure_ascii=False)
                           ,travelSummary=json.dumps(travelSummary,ensure_ascii=False)
                           ,carMonitorChart=json.dumps(carMonitorChart,ensure_ascii=False)
                           ,scheduleToday=scheduleToday,scheduleTomorrow=scheduleTomorrow
                           ,financialChart=json.dumps(financialChart,ensure_ascii=False))

@admin.route("/driver/list/")
@admin_login_req
@admin_auth
def driverList():
    driver_list = Driver.query.all()
    return render_template("admin/driver_list.html",driver_list = driver_list)

@admin.route("/driver/add/",methods=["GET","POST"])
@admin_login_req
@admin_auth
def driverAdd():
    form = DriverForm()
    if form.validate_on_submit():
        data = form.data
        if data['idcardz'] == '' or data['idcardf'] == '' or data['drivercardz'] == '' or data['drivercardf'] == '':
            flash("信息填写不完整",'err')
        driver = Driver(
            name=data["name"],
            phone=data["phone"],
            address=data["address"],
            idcardz=data["idcardz"],
            idcardf=data["idcardz"],
            drivercardz=data["drivercardz"],
            drivercardf=data["drivercardf"],
            content=data["content"]
        )
        db.session.add(driver)
        db.session.commit()
        flash("添加成功", "ok")
        return redirect(url_for("admin.driverList"))
    return render_template("admin/driver_add.html",form=form)

@admin.route("/driver/edit/<int:id>/",methods=["GET","POST"])
@admin_login_req
@admin_auth
def driverEdit(id=None):
    form = DriverForm()
    driver = Driver.query.get_or_404(id)
    if form.validate_on_submit():
        data = form.data
        driver.name = data["name"]
        driver.phone = data["phone"]
        driver.address = data["address"]
        driver.idcardz = data["idcardz"]
        driver.idcardf = data["idcardz"]
        driver.drivercardz = data["drivercardz"]
        driver.drivercardf = data["drivercardf"]
        driver.content = data["content"]
        db.session.add(driver)
        db.session.commit()
        flash("修改成功", "ok")
        return redirect(url_for("admin.driverList"))
    return render_template("admin/driver_edit.html",form=form,driver=driver)

@admin.route("/driver/del/")
@admin_login_req
@admin_auth
def driverDel():
    id = request.args.get("id")
    driver = Driver.query.filter_by(id=id).first_or_404()
    if driver.status != 0:
        flash("司机暂不能删除！", 'err')
        return redirect(url_for("admin.driverList"))
    db.session.delete(driver)
    db.session.commit()
    flash("删除成功！",'ok')
    return redirect(url_for('admin.driverList'))

@admin.route("/car/list/")
@admin_login_req
@admin_auth
def carList():
    car_list = Car.query.all()
    return render_template("admin/car_list.html",car_list = car_list)

@admin.route("/car/add/",methods=["GET","POST"])
@admin_login_req
@admin_auth
def carAdd():
    form = CarForm()
    if form.validate_on_submit():
        data = form.data
        if data['img_url'] == '':
            flash("未上传车辆图片",'err')
        else:
            count = Car.query.filter_by(number=data["number"]).count()
            if count == 1:
                flash("车牌号码已存在", 'err')
            else:
                params = {
                    'name': data["number"]
                }
                response = curl('terminal/add', params, 'POST')
                car = Car(
                    number=data["number"],
                    tid=response['data']['tid'],
                    nickname=data["nickname"],
                    capacity=data["capacity"],
                    model=data["model"],
                    img_url=data["img_url"],
                    content=data["content"]
                )
                db.session.add(car)
                db.session.commit()
                flash("添加成功", "ok")
                return redirect(url_for("admin.carList"))
    return render_template("admin/car_add.html",form=form)

@admin.route("/car/edit/<int:id>/",methods=["GET","POST"])
@admin_login_req
@admin_auth
def carEdit(id=None):
    form = CarForm()
    car = Car.query.get_or_404(id)
    if form.validate_on_submit():
        data = form.data
        if data["number"] != car.number:
            count = Car.query.filter_by(number=data["number"]).count()
            if count == 1:
                flash("车牌号码已存在", 'err')
                return redirect(url_for("admin.carList"))
            else:
                params = {
                    'name': data["number"],
                    'tid': car.tid
                }
                response = curl('terminal/update', params, 'POST')
                print(response)
        car.number = data["number"]
        car.nickname = data["nickname"]
        car.capacity = data["capacity"]
        car.model = data["model"]
        car.img_url = data["img_url"]
        car.content = data["content"]
        db.session.add(car)
        db.session.commit()
        flash("修改成功", "ok")
        return redirect(url_for("admin.carList"))
    return render_template("admin/car_edit.html",form=form,car=car)

@admin.route("/car/del/")
@admin_login_req
@admin_auth
def carDel():
    id = request.args.get("id")
    car = Car.query.filter_by(id=id).first_or_404()
    if car.status != 0:
        flash("车辆暂不能删除！", 'err')
        return redirect(url_for("admin.carList"))
    db.session.delete(car)
    db.session.commit()
    flash("删除成功！",'ok')
    return redirect(url_for('admin.carList'))

@admin.route("/car/status/<int:id>/")
@admin_login_req
@admin_auth
def carStatus(id=None):
    car = Car.query.get_or_404(id)
    if car.status == 0:
        car.status=2
    else:
        car.status=0
    db.session.add(car)
    db.session.commit()
    flash("状态修改成功", "ok")
    return redirect(url_for("admin.carList"))

#添加管理员
@admin.route('/admin/add/', methods=["GET", "POST"])
@admin_login_req
@admin_auth
def adminAdd():
    form = AdminForm()
    from werkzeug.security import generate_password_hash
    if form.validate_on_submit():
        data = form.data
        admin = Admin(
            name=data["name"],
            phone=data["phone"],
            password=generate_password_hash('123456'),
            role_id=data["role_id"],
            is_super=1
        )
        db.session.add(admin)
        db.session.commit()
        flash("添加管理员成功！","ok")
        return redirect(url_for("admin.adminList"))
    return render_template("admin/admin_add.html", form=form)

#管理员列表
@admin.route('/admin/list/', methods=["GET"])
@admin_login_req
@admin_auth
def adminList():
    admin_list = Admin.query.join(
        Role
    ).filter(
        Role.id == Admin.role_id
    ).all()
    return render_template("admin/admin_list.html",admin_list=admin_list)

@admin.route("/admin/del/")
@admin_login_req
@admin_auth
def adminDel():
    id = request.args.get("id")
    auth = Admin.query.filter_by(id=id).first_or_404()
    db.session.delete(auth)
    db.session.commit()
    flash("删除管理员成功！","ok")
    return redirect(url_for('admin.adminList'))

@admin.route("/admin/sta/")
@admin_login_req
@admin_auth
def adminSta():
    id = request.args.get("id")
    admin = Admin.query.filter_by(id=id).first_or_404()
    admin.password = generate_password_hash('123456')
    db.session.add(admin)
    db.session.commit()
    flash("恢复密码成功！","ok")
    return redirect(url_for('admin.adminList'))

@admin.route('/auth/add/', methods=["GET","POST"])
@admin_login_req
@admin_auth
def authAdd():
    form = AuthForm()
    if form.validate_on_submit():
        data = form.data
        auth_count = Auth.query.filter_by(name=data["name"]).count()
        if auth_count == 1:
            flash("权限名称已经存在！", "err")
            return redirect(url_for('admin.authAdd'))
        auth_count = Auth.query.filter_by(url=data["url"]).count()
        if auth_count == 1:
            flash("权限地址已经存在！", "err")
            return redirect(url_for('admin.authAdd'))
        auth = Auth(
            name=data["name"],
            url=data["url"]
        )
        db.session.add(auth)
        db.session.commit()
        flash("添加权限成功！","ok")
        return redirect(url_for('admin.authList'))
    return render_template("admin/auth_add.html",form=form)

@admin.route('/auth/list/')
@admin_login_req
@admin_auth
def authList():
    auth_list = Auth.query.order_by(
        Auth.add_time.desc()
    ).all()
    return render_template("admin/auth_list.html",auth_list=auth_list)

@admin.route("/auth/del/")
@admin_login_req
@admin_auth
def authDel():
    id = request.args.get("id")
    auth = Auth.query.filter_by(id=id).first_or_404()
    db.session.delete(auth)
    db.session.commit()
    flash("删除标签成功！","ok")
    return redirect(url_for('admin.authList'))

@admin.route("/auth/edit/<int:id>/",methods=["GET","POST"])
@admin_login_req
@admin_auth
def authEdit(id=None):
    form = AuthForm()
    auth = Auth.query.filter_by(id=id).first_or_404()
    if form.validate_on_submit():
        data = form.data
        auth_count = Auth.query.filter_by(name=data["name"]).count()
        if auth.name !=data["name"] and auth_count == 1:
            flash("权限名称已经存在！", "err")
            return redirect(url_for('admin.authAdd'))
        auth_count = Auth.query.filter_by(url=data["url"]).count()
        if auth.url !=data["url"] and auth_count == 1:
            flash("权限地址已经存在！", "err")
            return redirect(url_for('admin.authAdd'))
        auth.url = data["url"]
        auth.name = data["name"]
        db.session.add(auth)
        db.session.commit()
        flash("权限修改成功！","ok")
        return redirect(url_for('admin.authList'))
    return render_template("admin/auth_edit.html",form=form,auth=auth)

@admin.route('/role/add/', methods=["GET","POST"])
@admin_login_req
@admin_auth
def roleAdd():
    form = RoleForm()
    if form.validate_on_submit():
        data = form.data
        role = Role(
            name=data["name"],
            auths=",".join(map(lambda v: str(v), data["auths"]))
        )
        db.session.add(role)
        db.session.commit()
        flash("添加角色成功！", "ok")
        return redirect(url_for('admin.roleList'))
    return render_template("admin/role_add.html", form=form)

@admin.route('/role/list/')
@admin_login_req
@admin_auth
def roleList():
    role_list = Role.query.order_by(
        Role.add_time.desc()
    ).all()
    return render_template("admin/role_list.html",role_list=role_list)

@admin.route("/role/del/")
@admin_login_req
@admin_auth
def roleDel():
    id = request.args.get("id")
    role = Role.query.filter_by(id=id).first_or_404()
    db.session.delete(role)
    db.session.commit()
    flash("删除角色成功！","ok")
    return redirect(url_for('admin.roleList'))

@admin.route('/role/edit/<int:id>/',methods=["GET","POST"])
@admin_login_req
@admin_auth
def roleEdit(id=None):
    form = RoleForm()
    role = Role.query.get_or_404(id)
    if request.method == "GET":
        auths = role.auths
        form.auths.data = list(map(lambda  v: int(v),auths.split(",")))
    if form.validate_on_submit():
        data = form.data
        role.name = data["name"]
        role.auths = ",".join(map(lambda v: str(v), data["auths"]))
        db.session.add(role)
        db.session.commit()
        flash("修改角色成功！","ok")
        return redirect(url_for('admin.roleList'))
    return render_template("admin/role_edit.html",form=form,role=role)

@admin.route("/schedule/list/")
@admin_login_req
@admin_auth
def scheduleList():
    schedule_list = Schedule.query.order_by(
        Schedule.start_time.desc()
    ).all()
    return render_template("admin/schedule_list.html",schedule_list = schedule_list)

@admin.route("/schedule/add/",methods=["GET","POST"])
@admin_login_req
@admin_auth
def scheduleAdd():
    form = ScheduleForm()
    driver_list = Driver.query.filter_by(status=0).all()
    car_list = Car.query.filter_by(status=0).all()
    if form.validate_on_submit():
        data = form.data
        origin = geocode_curl(data["start_point"])
        destination = geocode_curl(data["end_point"])
        track_data = driving(origin,destination)
        track = Track(
            origin=origin,
            destination=destination,
            distance=track_data['distance'],
            duration=track_data['duration'],
            steps=json.dumps(track_data['steps']),
            start_time = data["start_time"],
            end_time = data["end_time"]
        )
        db.session.add(track)
        db.session.flush()
        driver_id = request.form.get('driver_id')
        car_id = request.form.get('car_id')
        selectDC = request.form.get('selectDC')
        if selectDC is None or driver_id is None or car_id is None:
            schedule = Schedule(
                unit=data["unit"],
                user=data["user"],
                phone=data["phone"],
                start_point=data["start_point"],
                end_point=data["end_point"],
                start_time=data["start_time"],
                end_time=data["end_time"],
                content=data["content"],
                money=data["money"],
                driver_money=data["driver_money"],
                track_id=track.id
            )
        else:
            driver = Driver.query.get_or_404(driver_id)
            car = Car.query.get_or_404(car_id)
            driver.status = 1
            db.session.add(driver)
            car.status = 1
            db.session.add(car)
            schedule = Schedule(
                unit=data["unit"],
                user=data["user"],
                phone=data["phone"],
                start_point=data["start_point"],
                end_point=data["end_point"],
                start_time=data["start_time"],
                end_time=data["end_time"],
                content=data["content"],
                driver_id=driver_id,
                car_id=car_id,
                money=data["money"],
                driver_money=data["driver_money"],
                status=1,
                track_id=track.id
            )
        db.session.add(schedule)
        db.session.commit()
        flash("添加成功", "ok")
        return redirect(url_for("admin.scheduleList"))
    return render_template("admin/schedule_add.html",form=form,driver_list=driver_list,car_list=car_list)

@admin.route("/schedule/edit/<int:id>/",methods=["GET","POST"])
@admin_login_req
@admin_auth
def scheduleEdit(id=None):
    form = ScheduleForm()
    driver_list = Driver.query.filter_by(status=0).all()
    car_list = Car.query.filter_by(status=0).all()
    schedule = Schedule.query.get_or_404(id)
    if form.validate_on_submit():
        data = form.data
        track = Track.query.filter_by(id=schedule.track_id).first_or_404()
        origin = geocode_curl(data["start_point"])
        destination = geocode_curl(data["end_point"])
        track_data = driving(origin,destination)
        track.origin=origin
        track.destination=destination
        track.distance=track_data['distance']
        track.duration=track_data['duration']
        track.steps=json.dumps(track_data['steps'])
        track.start_time = data["start_time"]
        track.end_time = data["end_time"]
        db.session.add(track)
        db.session.flush()
        driver_id = request.form.get('driver_id')
        car_id = request.form.get('car_id')
        selectDC = request.form.get('selectDC')
        if selectDC is None:
            if driver_id is None or car_id is None:
                schedule.unit=data["unit"]
                schedule.user=data["user"]
                schedule.phone=data["phone"]
                schedule.start_point=data["start_point"]
                schedule.end_point=data["end_point"]
                schedule.start_time=data["start_time"]
                schedule.end_time=data["end_time"]
                schedule.content=data["content"]
                schedule.money=data["money"]
                schedule.driver_money=data["driver_money"]
            else:
                schedule.unit = data["unit"],
                schedule.user = data["user"],
                schedule.phone = data["phone"],
                schedule.start_point = data["start_point"],
                schedule.end_point = data["end_point"],
                schedule.start_time = data["start_time"],
                schedule.end_time = data["end_time"],
                schedule.content = data["content"],
                schedule.driver_id = driver_id,
                schedule.car_id = car_id,
                schedule.money = data["money"],
                schedule.driver_money = data["driver_money"],
                schedule.status = 1,
        db.session.add(schedule)
        db.session.commit()
        flash("修改成功", "ok")
        return redirect(url_for("admin.scheduleList"))
    return render_template("admin/schedule_edit.html",form=form,driver_list=driver_list,car_list=car_list,schedule=schedule)

@admin.route("/schedule/del/")
@admin_login_req
@admin_auth
def scheduleDel():
    id = request.args.get("id")
    schedule = Schedule.query.filter_by(id=id).first_or_404()
    track = Track.query.filter_by(id=schedule.track_id).first_or_404()
    db.session.delete(schedule)
    db.session.delete(track)
    db.session.commit()
    flash("删除成功！",'ok')
    return redirect(url_for('admin.scheduleList'))

@admin.route("/schedule/sta/")
@admin_login_req
@admin_auth
def scheduleSta():
    scheduleByTime = {
        "labels": [],
        "datasets": [{
            "type": 'bar',
            "label": '未分配司机/车辆',
            "backgroundColor": 'rgb(255, 99, 132)',
            "data": []
        }, {
            "type": 'bar',
            "label": '未开始',
            "backgroundColor": 'rgb(75, 192, 192)',
            "data": []
        },  {
            "type": 'bar',
            "label": '已结束',
            "backgroundColor": 'rgb(180,191,192)',
            "data": []
        }]
    }
    type = request.args.get("type")
    count_list_0 = []
    count_list_1 = []
    count_list_3 = []
    start_date = ''
    end_date = ''
    if type is None:
        time_list, temp = halfYear()
        scheduleByTime['labels'] = time_list
        for v in temp:
            count = Schedule.query.filter(Schedule.status==0).filter(Schedule.start_time.between(v[0], v[1])).count()
            count_list_0.append(count)
            count = Schedule.query.filter(Schedule.status == 1).filter(Schedule.start_time.between(v[0], v[1])).count()
            count_list_1.append(count)
            count = Schedule.query.filter(Schedule.status == 3).filter(Schedule.start_time.between(v[0], v[1])).count()
            count_list_3.append(count)
    else:
        start_date = request.args.get("start")
        end_date = request.args.get("end")
        day_list = getBetweenDay(start_date, end_date)
        scheduleByTime['labels'] = day_list
        for v in day_list:
            str = v + ' 00:00:00'
            start = datetime.datetime.strptime(str, "%Y-%m-%d %H:%M:%S")
            end = start + datetime.timedelta(hours=23, minutes=59, seconds=59)
            count = Schedule.query.filter(Schedule.status == 0).filter(Schedule.start_time.between(start, end)).count()
            count_list_0.append(count)
            count = Schedule.query.filter(Schedule.status == 1).filter(Schedule.start_time.between(start, end)).count()
            count_list_1.append(count)
            count = Schedule.query.filter(Schedule.status == 3).filter(Schedule.start_time.between(start, end)).count()
            count_list_3.append(count)
    scheduleByTime['datasets'][0]['data'] = count_list_0
    scheduleByTime['datasets'][1]['data'] = count_list_1
    scheduleByTime['datasets'][2]['data'] = count_list_3
    return render_template("admin/schedule_sta.html", scheduleByTime=json.dumps(scheduleByTime, ensure_ascii=False),
                           start_date=start_date, end_date=end_date)

@admin.route("/monitor/")
def monitor():
    return render_template("admin/monitor.html")

@admin.route("/monitor/detail/")
def monitorDetail():
    params = {
        'tid':246882981,
        'trid':40
    }
    response = curl('terminal/lastpoint',params,'GET')
    print(response)
    return jsonify(response)

@admin.route("/track/list/")
@admin_login_req
@admin_auth
def trackList():
    schedule_list = Schedule.query.filter(Schedule.status==3).order_by(
        Schedule.start_time.desc()
    ).all()
    return render_template("admin/track_list.html",schedule_list = schedule_list)

@admin.route("/track/detail/<int:id>/")
@admin_login_req
@admin_auth
def trackDetail(id=None):
    return render_template("admin/track_detail.html",id=id)

@admin.route("/json/<int:id>/")
def jsonData(id=None):
    schedule = Schedule.query.filter_by(id=id).first_or_404()
    track = Track.query.filter_by(id=schedule.track_id).first_or_404()
    data = []
    str = schedule.start_point + "->" + schedule.end_point
    data.append({"name": str, "path": json.loads(track.steps)})
    return json.dumps(data,ensure_ascii=False)

@admin.route("/expense/list/<int:type>/")
@admin_login_req
@admin_auth
def expenseList(type=None):
    if type is None:
        type = 0
    if type == 0:
        expense_list = Expense.query.filter_by(status=0).all()
    else:
        expense_list = Expense.query.filter(or_(Expense.status == 1, Expense.status == 2)).all()
    return render_template("admin/expense_list.html",expense_list = expense_list,type=type)

@admin.route("/expense/detail/<int:id>/",methods=["GET","POST"])
@admin_login_req
@admin_auth
def expenseDetail(id=None):
    if id is None:
        id = 1
    form = ExpenseForm()
    becauseForm = BecauseForm()
    expense = Expense.query.get_or_404(id)
    if becauseForm.validate_on_submit():
        data = becauseForm.data
        expense.because = data["because"]
        expense.status = 2
        db.session.add(expense)
        db.session.commit()
        flash("提交成功", "ok")
        return redirect(url_for("admin.expenseList",type=1))
    return render_template("admin/expense_detail.html",form=form,expense=expense,becauseForm=becauseForm)

@admin.route("/expense/approval/<int:id>/")
@admin_login_req
@admin_auth
def expenseApproval(id=None):
    if id is None:
       id = 1
    expense = Expense.query.get_or_404(id)
    expense.status = 1
    expense.end_time = datetime.datetime.now()
    db.session.add(expense)
    db.session.commit()
    flash("结算成功", "ok")
    return redirect(url_for("admin.expenseList",type=1))

@admin.route("/expense/del/")
@admin_login_req
@admin_auth
def expenseDel():
    id = request.args.get("id")
    expense = Expense.query.filter_by(id=id).first_or_404()
    db.session.delete(expense)
    db.session.commit()
    flash("删除成功！",'ok')
    return redirect(url_for('admin.expenseList',type=0))

@admin.route("/expense/type/")
@admin_login_req
@admin_auth
def expenseType():
    type_list = ExpenseType.query.all()
    return render_template("admin/expense_type.html",type_list = type_list)

@admin.route("/expense/addType/",methods=["GET","POST"])
@admin_login_req
@admin_auth
def expenseAddType():
    form = ExpenseTypeForm()
    if form.validate_on_submit():
        data = form.data
        expense_type = ExpenseType(
            name=data["name"],
            type=data["type"],
            content=data["content"],
        )
        db.session.add(expense_type)
        db.session.commit()
        flash("添加成功", "ok")
        return redirect(url_for("admin.expenseType"))
    return render_template("admin/expense_addType.html",form=form)

@admin.route("/expense/delType/")
@admin_login_req
@admin_auth
def expenseTypeDel():
    id = request.args.get("id")
    cost_type = ExpenseType.query.filter_by(id=id).first_or_404()
    db.session.delete(cost_type)
    db.session.commit()
    flash("删除成功！",'ok')
    return redirect(url_for('admin.expenseType'))

@admin.route("/expense/schedule/<int:type>/")
@admin_login_req
@admin_auth
def expenseSchedule(type=None):
    if type is None:
        type = 0
    if type == 0:
        expense_list = Expense.query.filter_by(status=0).all()
    else:
        expense_list = Expense.query.filter(or_(Expense.status == 1, Expense.status == 2)).all()
    return render_template("admin/expense_schedule.html",expense_list = expense_list,type=type)

@admin.route("/expense/sta/")
@admin_login_req
def expenseSta():
    expenseByTime = {
        "labels": [],
        "datasets": [{
                "type": 'bar',
                "label": '收入',
                "backgroundColor": 'rgb(255, 99, 132)',
                "data": []
            }, {
                "type": 'bar',
                "label": '支出',
                "backgroundColor": 'rgb(75, 192, 192)',
                "data": []
            },{
                "type": 'line',
                "label": '利润',
                "borderColor": 'rgb(54, 162, 235)',
                "data": []
            }]
    }
    type = request.args.get("type")
    expense_in_list = []
    expense_out_list = []
    expense_profit_list = []
    start_date=''
    end_date=''
    if type is None:
        time_list, temp = halfYear()
        expenseByTime['labels'] = time_list
        for v in temp:
            expense = Expense.query.filter(Expense.end_time.between(v[0], v[1])).filter(Expense.status == 1).all()
            schedule = Schedule.query.filter(Schedule.end_time.between(v[0], v[1])).filter(Expense.status == 3).all()
            expense_in = 0
            expense_out = 0
            for v in expense:
                if v.expense_type.type == '收入':
                    expense_in += int(v.money)
                else:
                    expense_out -= int(v.money)
            for i in schedule:
                money = int(i.money) - int(i.driver_money)
                expense_in += money
            expense_in_list.append(expense_in)
            expense_out_list.append(expense_out)
            expense_profit_list.append(expense_in + expense_out)
    else:
        start_date = request.args.get("start")
        end_date = request.args.get("end")
        day_list = getBetweenDay(start_date,end_date)
        expenseByTime['labels'] = day_list
        for v in day_list:
            str = v + ' 00:00:00'
            start = datetime.datetime.strptime(str, "%Y-%m-%d %H:%M:%S")
            end = start + datetime.timedelta(hours=23, minutes=59, seconds=59)
            expense = Expense.query.filter(Expense.end_time.between(start, end)).filter(Expense.status == 1).all()
            schedule = Schedule.query.filter(Schedule.end_time.between(start, end)).filter(Expense.status == 3).all()
            expense_in = 0
            expense_out = 0
            for t in expense:
                if t.expense_type.type == '收入':
                    expense_in += int(t.money)
                else:
                    expense_out -= int(t.money)
            for i in schedule:
                money = int(i.money) - int(i.driver_money)
                expense_in += money
            expense_in_list.append(expense_in)
            expense_out_list.append(expense_out)
            expense_profit_list.append(expense_in + expense_out)
    expenseByTime['datasets'][0]['data'] = expense_in_list
    expenseByTime['datasets'][1]['data'] = expense_out_list
    expenseByTime['datasets'][2]['data'] = expense_profit_list
    return render_template("admin/expense_sta.html",expenseByTime=json.dumps(expenseByTime,ensure_ascii=False),start_date=start_date,end_date=end_date)

@admin.route("/leave/list/<int:type>/")
@admin_login_req
@admin_auth
def leaveList(type=None):
    if type is None:
        type = 0
    if type == 0:
        leave_list = Leave.query.filter_by(status=0).all()
    elif type == 1:
        leave_list = Leave.query.filter(or_(Leave.status == 1, Leave.status == 2)).all()
    else:
        leave_list = Leave.query.all()
    return render_template("admin/leave_list.html",leave_list=leave_list,type=type)

@admin.route("/leave/status/")
@admin_login_req
@admin_auth
def leaveStatus():
    id = request.args.get("id")
    status = request.args.get("status")
    leave = Leave.query.filter_by(id=id).first_or_404()
    leave.status = status
    db.session.add(leave)
    db.session.commit()
    flash("操作成功！",'ok')
    return redirect(url_for('admin.leaveList',type=0))

@admin.route("/leave/del/")
@admin_login_req
@admin_auth
def leaveDel():
    id = request.args.get("id")
    leave = Leave.query.filter_by(id=id).first_or_404()
    db.session.delete(leave)
    db.session.commit()
    flash("删除成功！",'ok')
    return redirect(url_for('admin.leaveList',type=0))

@admin.route("/leave/sta/")
@admin_login_req
@admin_auth
def leaveSta():
    type = request.args.get("type")
    if not type is None:
        if int(type) == 1:
            content = request.args.get("content")
            driver = Driver.query.filter(
                or_(Driver.name.ilike('%' + content + '%'), Driver.phone.ilike('%' + content + '%'))).first()
            if not driver is None:
                leave_list = Leave.query.filter(Leave.driver_id == driver.id).all()
            else:
                leave_list = ''
            return render_template("admin/leave_sta.html", leave_list=leave_list, content=content)
        elif int(type) == 2:
            time = request.args.get("time")
            now = datetime.datetime.now()
            if int(time) == 1:
                start = request.args.get("start")
                end = request.args.get("end")
            elif int(time) == 2:
                yesterday = now - datetime.timedelta(days=1)
                start = yesterday - datetime.timedelta(hours=yesterday.hour, minutes=yesterday.minute,
                                                       seconds=yesterday.second,
                                                       microseconds=yesterday.microsecond)
                end = start + datetime.timedelta(hours=23, minutes=59, seconds=59)
            elif int(time) == 3:
                start = now - datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second,
                                                 microseconds=now.microsecond)
                end = start + datetime.timedelta(hours=23, minutes=59, seconds=59)
            else:
                tomorrow = now + datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second,
                                                    microseconds=now.microsecond)
                start = tomorrow - datetime.timedelta(hours=tomorrow.hour, minutes=tomorrow.minute,
                                                      seconds=tomorrow.second,
                                                      microseconds=tomorrow.microsecond)
                end = start + datetime.timedelta(hours=23, minutes=59, seconds=59)
            leave_list = Leave.query.filter(Leave.start_time.between(start, end)).all()
            return render_template("admin/leave_sta.html", leave_list=leave_list, start=start, end=end, content='')
    else:
        leave_list = Leave.query.filter(Leave.status!=0).all()
        return render_template("admin/leave_sta.html", leave_list=leave_list)

@admin.route("/notice/list/")
@admin_login_req
@admin_auth
def noticeList():
    notice_list = Notice.query.all()
    return render_template("admin/notice_list.html",notice_list = notice_list)

@admin.route("/notice/add/",methods=["GET","POST"])
@admin_login_req
@admin_auth
def noticeAdd():
    form = NoticeForm()
    if form.validate_on_submit():
        data = form.data
        notice = Notice(
            content=data["content"],
        )
        db.session.add(notice)
        db.session.commit()
        flash("添加成功", "ok")
        return redirect(url_for("admin.noticeList"))
    return render_template("admin/notice_add.html",form=form)

@admin.route("/notice/del/")
@admin_login_req
@admin_auth
def noticeDel():
    id = request.args.get("id")
    notice = Notice.query.filter_by(id=id).first_or_404()
    db.session.delete(notice)
    db.session.commit()
    flash("删除成功！",'ok')
    return redirect(url_for('admin.noticeList'))

@admin.route('/upload/',methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files.get('img')
        if not os.path.exists(app.config['UPLOADED_PATH']):
            os.makedirs(app.config['UPLOADED_PATH'])
            os.chmod(app.config['UPLOADED_PATH'],"rw")
        f_new_name = change_filename(f.filename)
        f.save(os.path.join(app.config['UPLOADED_PATH'], f_new_name))
        d = {
            'path' : f_new_name
        }
        return json.dumps(d)

@admin.route("/content/search/")
def contentSearch():
    type = request.args.get("type")
    if int(type) == 1:
        sel = request.args.get("sel")
        if int(sel) == 4:
            schedule_list = Schedule.query.all()
        else:
            schedule_list = Schedule.query.filter_by(status=sel).all()
        return render_template("admin/schedule_list.html",schedule_list=schedule_list,sel=sel)
    elif int(type) == 2:
        content = request.args.get("content")
        driver = Driver.query.filter_by(name=content).first()
        car = Car.query.filter_by(number=content).first()
        if not driver is None:
            schedule_list = Schedule.query.filter(
                or_(Schedule.unit.ilike('%' + content + '%'), Schedule.user.ilike('%' + content + '%'), Schedule.driver_id==driver.id)).all()
        elif not car is None:
            schedule_list = Schedule.query.filter(
                or_(Schedule.unit.ilike('%' + content + '%'), Schedule.user.ilike('%' + content + '%'),Schedule.car_id == car.id)).all()
        else:
            schedule_list = Schedule.query.filter(
                or_(Schedule.unit.ilike('%' + content + '%'), Schedule.user.ilike('%' + content + '%'))).all()
        return render_template("admin/schedule_list.html", schedule_list=schedule_list, content=content,sel=4)
    elif int(type) == 3:
        time = request.args.get("time")
        now = datetime.datetime.now()
        if int(time) == 1:
            start = request.args.get("start")
            end = request.args.get("end")
        elif int(time) == 2:
            yesterday = now - datetime.timedelta(days=1)
            start = yesterday - datetime.timedelta(hours=yesterday.hour, minutes=yesterday.minute,
                                                          seconds=yesterday.second,
                                                          microseconds=yesterday.microsecond)
            end = start + datetime.timedelta(hours=23, minutes=59, seconds=59)
        elif int(time) == 3:
            start = now - datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second,
                                                  microseconds=now.microsecond)
            end = start + datetime.timedelta(hours=23, minutes=59, seconds=59)
        else:
            tomorrow = now + datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second,
                                                microseconds=now.microsecond)
            start = tomorrow - datetime.timedelta(hours=tomorrow.hour, minutes=tomorrow.minute,
                                                          seconds=tomorrow.second,
                                                          microseconds=tomorrow.microsecond)
            end = start + datetime.timedelta(hours=23, minutes=59, seconds=59)
        schedule_list = Schedule.query.filter(Schedule.start_time.between(start, end)).all()
        return render_template("admin/schedule_list.html", schedule_list=schedule_list, start=start,end=end,sel=4,content='')

def driving(origin,destination):
    params = {
        'origin': origin,
        'destination': destination
    }
    driving = driving_curl(params)
    k = driving['route']['paths'][0]['steps']
    paths = [origin.split(',')]
    for m in k:
        pp = m['polyline'].split(';')[0].split(',')
        paths.append(pp)
    paths.append(destination.split(','))
    data = {}
    data['distance'] = driving['route']['paths'][0]['distance']
    data['duration'] = driving['route']['paths'][0]['duration']
    data['steps'] = paths
    return data

def halfYear():
    start = datetime.date.today() - relativedelta(months=5)
    end = datetime.datetime.now()
    month_num = 12 * (end.year - start.year) + end.month - start.month
    time_list = []
    year = start.year
    month = start.month
    # 遍历月份数+1,之所以加1是因为即使是本月注册的博主，月份差为0，他的页面也要显示一个月，即本月
    temp = []
    for m in range(month_num + 1):
        # 把年月的小列表追加进大列表
        time_list.append(str(month) + '月')
        temp.append(LF(year, month))
        # 月份加1
        month += 1
        # 当月份达到13的时候，需要再从1月开始数，而且这代表跨年了，所以年份加1
        if month == 13:
            month = 1
            year += 1
    return time_list,temp

def LF(year,month):
    FL = []
    firstDayWeekDay, monthRange = calendar.monthrange(year, month)
    firstDay = datetime.date(year=year, month=month, day=1)
    lastDay = datetime.date(year=year, month=month, day=monthRange)
    FL.append(firstDay)
    FL.append(lastDay)
    return FL

def TodayAndTomorrow():
    now = datetime.datetime.now()
    zero_today = now - datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second,
                                          microseconds=now.microsecond)
    last_today = zero_today + datetime.timedelta(hours=23, minutes=59, seconds=59)

    tomorrow = now + datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second,
                                 microseconds=now.microsecond)
    zero_tomorrow = tomorrow - datetime.timedelta(hours=tomorrow.hour, minutes=tomorrow.minute, seconds=tomorrow.second,
                                        microseconds=tomorrow.microsecond)
    last_tomorrow = zero_tomorrow + datetime.timedelta(hours=23, minutes=59, seconds=59)
    return zero_today,last_today,zero_tomorrow,last_tomorrow

def scheduleTodayAndTomorrow():
    zero_today, last_today, zero_tomorrow, last_tomorrow = TodayAndTomorrow()
    scheduleToday = []
    scheduleToday.append(Schedule.query.filter(Schedule.start_time.between(zero_today, last_today)).count())
    scheduleToday.append(
        Schedule.query.filter(Schedule.start_time.between(zero_today, last_today)).filter(Schedule.status == 0).count())
    scheduleToday.append(
        Schedule.query.filter(Schedule.start_time.between(zero_today, last_today)).filter(Schedule.status == 1).count())
    scheduleToday.append(
        Schedule.query.filter(Schedule.start_time.between(zero_today, last_today)).filter(Schedule.status == 2).count())
    scheduleToday.append(
        Schedule.query.filter(Schedule.end_time.between(zero_today, last_today)).filter(Schedule.status == 3).count())
    scheduleTomorrow = []
    scheduleTomorrow.append(Schedule.query.filter(Schedule.start_time.between(zero_tomorrow, last_tomorrow)).count())
    scheduleTomorrow.append(
        Schedule.query.filter(Schedule.start_time.between(zero_tomorrow, last_tomorrow)).filter(
            Schedule.status == 0).count())
    scheduleTomorrow.append(
        Schedule.query.filter(Schedule.start_time.between(zero_tomorrow, last_tomorrow)).filter(
            Schedule.status == 1).count())
    scheduleTomorrow.append(
        Schedule.query.filter(Schedule.start_time.between(zero_tomorrow, last_tomorrow)).filter(
            Schedule.status == 2).count())
    scheduleTomorrow.append(
        Schedule.query.filter(Schedule.end_time.between(zero_tomorrow, last_tomorrow)).filter(
            Schedule.status == 3).count())
    return scheduleToday,scheduleTomorrow

#获取指定日期区间日期列表
def getBetweenDay(start_date,end_date):
  date_list = []
  begin_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
  end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
  while begin_date <= end_date:
    date_str = begin_date.strftime("%Y-%m-%d")
    date_list.append(date_str)
    begin_date += datetime.timedelta(days=1)
  return date_list



@admin.route("/test/map/")
def testMap():
  return render_template("admin/t.html")