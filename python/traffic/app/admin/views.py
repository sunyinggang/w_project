from flask import render_template, flash, redirect, url_for

from . import admin
from .forms import LoginForm
from ..models import Admin


@admin.route("/")
def index():
    return render_template("admin/index.html")

@admin.route("/login/",methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(phone=data["phone"]).first()
        if not admin:
            flash("用户不存在！","err")
            return redirect(url_for("admin.login"))
    return render_template("admin/login.html",form=form)

