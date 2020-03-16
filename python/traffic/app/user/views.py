from flask import render_template

from . import user


@user.route("/")
def index():
    return render_template("user/index.html")

@user.route("/profile/")
def profile():
    return render_template("user/profile.html")

@user.route("/login/")
def login():
    return render_template("user/login.html")

@user.route("/order/list/")
def orderList():
    return render_template("user/order_list.html")

@user.route("/expense/add/")
def expenseAdd():
    return render_template("user/expense_add.html")

@user.route("/expense/list/")
def expenseList():
    return render_template("user/expense_list.html")

@user.route("/leave/add/")
def leaveAdd():
    return render_template("user/leave_add.html")
