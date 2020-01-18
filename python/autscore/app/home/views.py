from flask import flash, redirect, url_for, session, render_template

from . import home
from app.home.forms import LoginForm
from app.models import Admin

@home.route("/")
def index():
    return "<h1 style='color:red'>home</h1>"

@home.route("/login/",methods=["GET","POST"])
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
            return redirect(url_for("admin.index"))
        # if data["usertype"] == 2:
        #     agent = Agent.query.filter_by(email=data["email"]).first()
        #     if not agent.check_pwd(data["password"]):
        #         flash("Wrong password!")
        #         return redirect(url_for("home.login"))
        #     session["username"] = data["email"]
        #     session["url"] = "agent.index"
        #     session["type"] = 2
        #     return redirect(url_for("home.index"))
        # if data["usertype"] == 3:
        #     staff = Staff.query.filter_by(username=data["email"]).first()
        #     if not staff.check_pwd(data["password"]):
        #         flash("Wrong password!")
        #         return redirect(url_for("home.login"))
        #     session["username"] = data["email"]
        #     session["url"] = "staff.index"
        #     session["type"] = 3
        #     return redirect(url_for("staff.index"))
    return render_template("home/login.html",form=form)

@home.route("/logout/")
def logout():
    session.pop("username",None)
    session.pop("type", None)
    return redirect(url_for("home.login"))
