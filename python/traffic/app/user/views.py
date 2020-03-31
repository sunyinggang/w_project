from functools import wraps

from flask import render_template, flash, redirect, url_for, session, request
from sqlalchemy import or_

from . import user
from .forms import LoginForm, ExpenseForm, LeaveForm
from .. import db
from ..models import Driver, Expense, ExpenseType, Notice, Leave, Schedule


def admin_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "driver_name" not in session:
            return redirect(url_for("user.login",next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@user.route("/")
@admin_login_req
def index():
    notice = Notice.query.order_by(Notice.add_time.desc()).first()
    schedule = Schedule.query.filter(
        Schedule.driver_id == session["driver_id"]
    ).filter(or_(Schedule.status == 1, Schedule.status == 2)).first()
    print(schedule)
    return render_template("user/index.html",notice=notice,schedule=schedule)

@user.route("/profile/")
@admin_login_req
def profile():
    driver = Driver.query.filter_by(id=session["driver_id"]).first()
    return render_template("user/profile.html",driver=driver)

@user.route("/login/",methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        driver = Driver.query.filter_by(phone=data["phone"]).first()
        if not driver:
            flash("用户不存在！","err")
            return redirect(url_for("user.login"))
        if not driver.check_pwd(data["password"]):
            flash("密码错误！", "err")
            return redirect(url_for("user.login"))
        session["driver_name"] = driver.name
        session["driver_id"] = driver.id
        flash("登录成功！", "ok")
        return redirect(request.args.get("next") or url_for("user.index"))
    return render_template("user/login.html",form=form)

@user.route("/schedule/list/")
@admin_login_req
def scheduleList():
    return render_template("user/schedule_list.html")

@user.route("/schedule/detail/<int:id>/")
@admin_login_req
def scheduleDetail(id=None):
    if id is None:
        id = 1
    schedule = Schedule.query.filter_by(id=id).first()
    return render_template("user/schedule_detail.html",schedule=schedule)

@user.route("/expense/add/",methods=["GET","POST"])
@admin_login_req
def expenseAdd():
    form = ExpenseForm()
    if form.validate_on_submit():
        data = form.data
        expense = Expense(
            user_id=session["driver_id"],
            type_id=data["type_id"],
            content=data["content"],
            money=data["money"],
            add_time=data["add_time"],
            note=data["note"],
            img_url=data["img_url"],
        )
        db.session.add(expense)
        db.session.commit()
        flash("添加成功", "ok")
        return redirect(url_for("user.expenseList",page=1))
    return render_template("user/expense_add.html",form=form)

@user.route("/expense/list/<int:page>/")
@admin_login_req
def expenseList(page=None):
    if page is None:
        page = 1
    expense_list = Expense.query.join(
        ExpenseType
    ).filter(
        Expense.user_id == session["driver_id"]
    ).filter(
        ExpenseType.id == Expense.type_id
    ).paginate(page=page, per_page=5)
    return render_template("user/expense_list.html",expense_list=expense_list)

@user.route("/leave/add/",methods=["GET","POST"])
@admin_login_req
def leaveAdd():
    form = LeaveForm()
    if form.validate_on_submit():
        data = form.data
        leave = Leave(
            driver_id=session["driver_id"],
            content=data["content"],
            start_time=data["start_time"],
            end_time=data["end_time"],
            note=data["note"],
        )
        db.session.add(leave)
        db.session.commit()
        flash("添加成功", "ok")
        return redirect(url_for("user.leaveList", page=1))
    return render_template("user/leave_add.html",form=form)

@user.route("/leave/list/<int:page>/")
@admin_login_req
def leaveList(page=None):
    if page is None:
        page = 1
    leave_list = Leave.query.filter_by(driver_id=session["driver_id"]).paginate(page=page, per_page=5)
    return render_template("user/leave_list.html",leave_list=leave_list)

@user.route("/notice/list/<int:page>/")
@admin_login_req
def noticeList(page=None):
    if page is None:
        page = 1
    notice_list = Notice.query.paginate(page=page, per_page=5)
    return render_template("user/notice_list.html", notice_list=notice_list)