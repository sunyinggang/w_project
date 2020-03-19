from flask import render_template, flash, redirect, url_for, session, request

from . import user
from .forms import LoginForm, ExpenseForm
from .. import db
from ..models import Driver, Expense, ExpenseType


@user.route("/")
def index():
    return render_template("user/index.html")

@user.route("/profile/")
def profile():
    return render_template("user/profile.html")

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

@user.route("/order/list/")
def orderList():
    return render_template("user/order_list.html")

@user.route("/expense/add/",methods=["GET","POST"])
def expenseAdd():
    form = ExpenseForm()
    if form.validate_on_submit():
        data = form.data
        expense = Expense(
            user_id=session["driver_id"],
            user_type=1,
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
def expenseList(page=None):
    if page is None:
        page = 1
    expense_list = Expense.query.join(
        ExpenseType
    ).filter(
        Expense.user_type == 1
    ).filter(
        Expense.user_id == session["driver_id"]
    ).filter(
        ExpenseType.id == Expense.type_id
    ).paginate(page=page, per_page=5)
    return render_template("user/expense_list.html",expense_list=expense_list)

@user.route("/leave/add/")
def leaveAdd():
    return render_template("user/leave_add.html")
