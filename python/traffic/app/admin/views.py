import json
import os
import re
from datetime import datetime
from functools import wraps

from flask import render_template, flash, redirect, url_for, session, request
from sqlalchemy import or_
from werkzeug.security import generate_password_hash

from . import admin
from .forms import LoginForm, ChangeForm, DriverForm, CarForm, NoticeForm, ScheduleForm, ExpenseTypeForm, ExpenseForm, \
    BecauseForm
from .. import db,app
from ..lib.functions import change_filename, curl, geocode_curl, driving_curl
from ..models import Admin, Driver, Car, Notice, ExpenseType, Expense, Schedule, Track, Leave


def admin_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "admin" not in session:
            return redirect(url_for("admin.login",next=request.url))
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
        session["admin"] = admin.name
        session["id"] = admin.id
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
    session.pop("admin",None)
    session.pop("id", None)
    return redirect(url_for("admin.login"))

@admin.route("/")
@admin_login_req
def index():
    return render_template("admin/index.html")

@admin.route("/driver/list/")
@admin_login_req
def driverList():
    driver_list = Driver.query.all()
    print(driver_list)
    return render_template("admin/driver_list.html",driver_list = driver_list)

@admin.route("/driver/add/",methods=["GET","POST"])
@admin_login_req
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
def carList():
    car_list = Car.query.all()
    return render_template("admin/car_list.html",car_list = car_list)

@admin.route("/car/add/",methods=["GET","POST"])
@admin_login_req
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

@admin.route("/schedule/list/")
@admin_login_req
def scheduleList():
    schedule_list = Schedule.query.order_by(
        Schedule.start_time.desc()
    ).all()
    return render_template("admin/schedule_list.html",schedule_list = schedule_list)

@admin.route("/schedule/add/",methods=["GET","POST"])
@admin_login_req
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
        print(selectDC)
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
def scheduleDel():
    id = request.args.get("id")
    schedule = Schedule.query.filter_by(id=id).first_or_404()
    db.session.delete(schedule)
    db.session.commit()
    flash("删除成功！",'ok')
    return redirect(url_for('admin.scheduleList'))

@admin.route("/expense/list/<int:type>/")
@admin_login_req
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
def expenseApproval(id=None):
    if id is None:
       id = 1
    expense = Expense.query.get_or_404(id)
    expense.status = 1
    expense.end_time = datetime.now()
    db.session.add(expense)
    db.session.commit()
    flash("结算成功", "ok")
    return redirect(url_for("admin.expenseList",type=1))

@admin.route("/expense/del/")
@admin_login_req
def expenseDel():
    id = request.args.get("id")
    expense = Expense.query.filter_by(id=id).first_or_404()
    db.session.delete(expense)
    db.session.commit()
    flash("删除成功！",'ok')
    return redirect(url_for('admin.expenseList',type=0))

@admin.route("/expense/type/")
@admin_login_req
def expenseType():
    type_list = ExpenseType.query.all()
    return render_template("admin/expense_type.html",type_list = type_list)

@admin.route("/expense/addType/",methods=["GET","POST"])
@admin_login_req
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
def expenseTypeDel():
    id = request.args.get("id")
    cost_type = ExpenseType.query.filter_by(id=id).first_or_404()
    db.session.delete(cost_type)
    db.session.commit()
    flash("删除成功！",'ok')
    return redirect(url_for('admin.expenseType'))

@admin.route("/leave/list/<int:type>/")
@admin_login_req
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
def leaveDel():
    id = request.args.get("id")
    leave = Leave.query.filter_by(id=id).first_or_404()
    db.session.delete(leave)
    db.session.commit()
    flash("删除成功！",'ok')
    return redirect(url_for('admin.leaveList',type=0))

@admin.route("/notice/list/")
@admin_login_req
def noticeList():
    notice_list = Notice.query.all()
    return render_template("admin/notice_list.html",notice_list = notice_list)

@admin.route("/notice/add/",methods=["GET","POST"])
@admin_login_req
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
def noticeDel():
    id = request.args.get("id")
    print(id)
    notice = Notice.query.filter_by(id=id).first_or_404()
    db.session.delete(notice)
    db.session.commit()
    flash("删除成功！",'ok')
    return redirect(url_for('admin.noticeList'))

@admin.route("/monitor/")
@admin_login_req
def monitor():
    return render_template("admin/monitor.html")

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

@admin.route("/test/")
def test():
    params = {}
    response = curl('service/list',params,'GET')
    return response

def driving(origin,destination):
    params = {
        'origin': origin,
        'destination': destination
    }
    driving = driving_curl(params)
    k = driving['route']['paths'][0]['steps']
    paths = [['116.964624', '36.614668']]
    for m in k:
        pp = m['polyline'].split(';')[0].split(',')
        paths.append(pp)
    paths.append(['116.48303839', '39.990633'])
    data = {}
    data['distance'] = driving['route']['paths'][0]['distance']
    data['duration'] = driving['route']['paths'][0]['duration']
    data['steps'] = paths
    return data
