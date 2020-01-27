from flask import flash, redirect, url_for, session, render_template

from . import home
from app.home.forms import LoginForm
from app.models import Admin, Teacher, Student


@home.route("/",methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        if data["usertype"] == 1:
            admin = Admin.query.filter_by(username=data["username"]).first()
            if not admin:
                flash("账号不存在！")
                return redirect(url_for("home.login"))
            if not admin.check_pwd(data["password"]):
                flash("密码错误!")
                return redirect(url_for("home.login"))
            session["username"] = data["username"]
            session["type"] = 1
            session["id"] = admin.id
            return redirect(url_for("admin.index"))
        if data["usertype"] == 2:
            teacher = Teacher.query.filter_by(username=data["username"]).first()
            if not teacher:
                flash("账号不存在！")
                return redirect(url_for("home.login"))
            if not teacher.check_pwd(data["password"]):
                flash("密码错误!")
                return redirect(url_for("home.login"))
            session["username"] = data["username"]
            session["type"] = 2
            session["id"] = teacher.id
            return redirect(url_for("teacher.index"))
        if data["usertype"] == 3:
            student = Student.query.filter_by(username=data["username"]).first()
            if not student:
                flash("账号不存在！")
                return redirect(url_for("home.login"))
            if not student.check_pwd(data["password"]):
                flash("密码错误!")
                return redirect(url_for("home.login"))
            session["username"] = data["username"]
            session["id"] = student.id
            session["type"] = 3
            return redirect(url_for("student.index"))
    return render_template("home/login.html",form=form)

# @home.route("change",methods=["GET","POST"])

@home.route("/logout/")
def logout():
    session.pop("username",None)
    session.pop("type", None)
    session.pop("id", None)
    return redirect(url_for("home.login"))
