import json
import os
import re
from functools import wraps

from flask import render_template, flash, redirect, url_for, session, request
from werkzeug.security import generate_password_hash

from . import admin
from .forms import LoginForm, ChangeForm, DriverForm, CarForm, NoticeForm, ScheduleForm, ExpenseTypeForm, ExpenseForm
from .. import db,app
from ..lib.functions import change_filename,curl
from ..models import Admin, Driver, Car, Notice, ExpenseType, Expense, Schedule


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

@admin.route("/schedule/list/")
@admin_login_req
def scheduleList():
    schedule_list = Schedule.query.all()
    return render_template("admin/schedule_list.html",schedule_list = schedule_list)

@admin.route("/schedule/add/",methods=["GET","POST"])
@admin_login_req
def scheduleAdd():
    form = ScheduleForm()
    driver_list = Driver.query.filter_by(status=0).all()
    car_list = Car.query.filter_by(status=0).all()
    if form.validate_on_submit():
        data = form.data
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
                driver_money=data["driver_money"]
            )
        else:
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
                driver_money=data["driver_money"]
            )
        db.session.add(schedule)
        db.session.commit()
        flash("添加成功", "ok")
        return redirect(url_for("admin.scheduleList"))
    return render_template("admin/schedule_add.html",form=form,driver_list=driver_list,car_list=car_list)

@admin.route("/expense/list/")
@admin_login_req
def expenseList():
    expense_list = Expense.query.all()
    return render_template("admin/expense_list.html",expense_list = expense_list)

@admin.route("/expense/add/",methods=["GET","POST"])
@admin_login_req
def expenseAdd():
    form = ExpenseForm()
    if form.validate_on_submit():
        data = form.data
        expense = Expense(
            user_id=session["id"],
            user_type=0,
            expense_type=data["expense_type"],
            content=data["content"],
            money=data["money"],
            add_time=data["add_time"],
            note=data["note"],
            img_url=data["img_url"],
        )
        db.session.add(expense)
        db.session.commit()
        flash("添加成功", "ok")
        return redirect(url_for("admin.expenseList"))
    return render_template("admin/expense_add.html",form = form)

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