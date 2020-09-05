#encoding = utf-8
from . import home
from flask import render_template, redirect, url_for,flash,session,request
from app.home.forms import LoginForm, registerForm, BookForm
from app.models import User,Book
from functools import wraps
from app import db


def user_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "username" not in session:
            return redirect(url_for("home.login", next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@home.route("/")
@user_login_req
def index():
    return render_template("home/index.html")

@home.route("/aindex")
def aindex():
    return render_template("home/aindex.html")


@home.route("/login/", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        user = User.query.filter_by(username=data["username"]).first()
        if not user.check_pwd(data["password"]):
            flash("密码错误")
            return redirect(url_for("home.login"))
        if user.usertype != data["usertype"]:
            flash("用户类型不正确")
            return redirect(url_for("home.login"))
        session["username"] = data["username"]
        session["userid"] = user.id
        if user.usertype == 1:
            return redirect(url_for("home.index"))
        return redirect(url_for("home.aindex"))
    return render_template("home/login.html", form=form)


@home.route("/logout/", methods=["GET"])
@user_login_req
def logout():
    session.pop("username",None)
    session.pop("userid", None)
    return redirect(url_for("home.login"))


@home.route("/signup/", methods=["GET","POST"])
def signup():
    form = registerForm()
    if form.validate_on_submit():
        data = form.data
        if data["password"] != data["passwordtwo"]:
            flash("密码不一致")
            return redirect(url_for("home.signup"))
        user = User(
            username=data["username"],
            password=data["password"],
            usertype=data["usertype"]
        )
        db.session.add(user)
        db.session.commit()
        flash("注册成功","ok")
        return redirect(url_for('home.login'))
    return render_template("home/signup.html",form=form)


@home.route("/forms/", methods=["GET","POST"])
@user_login_req
def forms():
    form = BookForm()
    if form.validate_on_submit():
        data = form.data
        book = Book(
            title=data["title"],
            date=data["date"],
            day=data["day"],
            user_id=session["userid"]
        )
        db.session.add(book)
        db.session.commit()
        flash("添加成功","ok")
        return redirect(url_for("home.forms"))
    return render_template("home/forms.html",form=form)

@home.route("/aforms/", methods=["GET"])
@user_login_req
def aforms():

    return render_template("home/aforms.html")

@home.route("/tables/", methods=["GET"])
@user_login_req
def tables():
    book_list = Book.query.filter(
        Book.user_id == session["userid"]
    ).all()
    return render_template("home/tables.html",book_list=book_list)

@home.route("/atables/", methods=["GET"])
@user_login_req
def atables():
    book_list = Book.query.join(
        User
    ).filter(
        User.id == Book.user_id
    ).all()
    return render_template("home/atables.html",book_list=book_list)


@home.route("/edit/<int:id>/", methods=["GET","POST"])
@user_login_req
def edit(id=None):
    form = BookForm()
    book = Book.query.get_or_404(id)
    if form.validate_on_submit():
        data = form.data
        book.title=data["title"],
        book.date=data["date"],
        book.day=data["day"]
        db.session.add(book)
        db.session.commit()
        flash("恢复成功","ok")
        return redirect(url_for("home.tables"))
    return render_template("home/forms_edit.html",form=form,book=book)

@home.route("/aedit/<int:id>/", methods=["GET","POST"])
@user_login_req
def aedit(id=None):
    form = BookForm()
    book = Book.query.get_or_404(id)
    if form.validate_on_submit():
        data = form.data
        book.title=data["title"],
        book.date=data["date"],
        book.day=data["day"]
        db.session.add(book)
        db.session.commit()
        flash("修改成功","ok")
        return redirect(url_for("home.atables"))
    return render_template("home/aforms_edit.html",form=form,book=book)

@home.route("/del/<int:id>/", methods=["GET"])
@user_login_req
def delbook(id=None):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    flash("删除成功","ok")
    book_list = Book.query.filter(
        Book.user_id == session["userid"]
    ).all()
    return render_template("home/tables.html",book_list=book_list)


@home.route("/adel/<int:id>/", methods=["GET"])
@user_login_req
def adelbook(id=None):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    flash("删除成功","ok")
    book_list = Book.query.all()
    return render_template("home/atables.html",book_list=book_list)
