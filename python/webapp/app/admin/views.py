#encoding = utf-8
from . import admin
from flask import render_template, redirect, url_for, flash, session, request, send_from_directory
from app.admin.forms import LoginForm, registerForm, CommodityForm
from app.models import Admin,Commodity
from functools import wraps
from app import db, app
import os,datetime,random
from flask_ckeditor import upload_success, upload_fail

def user_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "username" not in session:
            return redirect(url_for("admin.login", next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@admin.route("/")
@user_login_req
def index():
    return render_template("admin/index.html")


@admin.route("/login/", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        user = Admin.query.filter_by(username=data["username"]).first()
        if not user.check_pwd(data["password"]):
            flash("密码错误")
            return redirect(url_for("admin.login"))
        session["username"] = data["username"]
        session["userid"] = user.id
        return redirect(request.args.get("next") or url_for("admin.index"))
    return render_template("admin/login.html", form=form)


@admin.route("/logout/", methods=["GET"])
@user_login_req
def logout():
    session.pop("username",None)
    session.pop("userid", None)
    return redirect(url_for("admin.login"))


@admin.route("/signup/", methods=["GET","POST"])
def signup():
    form = registerForm()
    if form.validate_on_submit():
        data = form.data
        if data["password"] != data["passwordtwo"]:
            flash("密码不一致")
            return redirect(url_for("admin.signup"))
        user = Admin(
            username=data["username"],
            password=data["password"]
        )
        db.session.add(user)
        db.session.commit()
        flash("注册成功","ok")
        return redirect(url_for('admin.login'))
    return render_template("admin/signup.html",form=form)


@admin.route("/forms/", methods=["GET","POST"])
@user_login_req
def forms():
    form = CommodityForm()
    if form.validate_on_submit():
        data = form.data
        commodity = Commodity(
            title=data["title"],
            price=data["price"],
            os=data["os"],
            number=randID(),
            area=data["area"],
            server=data["server"],
            rank=data["rank"],
            type=data["type"],
            pet=data["pet"],
            sect=data["sect"],
            sex=data["sex"],
            bargain=data["bargain"],
            description=data["description"],
            content=data["content"]
        )
        db.session.add(commodity)
        db.session.commit()
        flash("添加成功","ok")
        return redirect(url_for("admin.forms"))
    return render_template("admin/forms.html",form=form)


@admin.route('/files/<path:filename>')
def uploaded_files(filename):
    path = app.config['UPLOADED_PATH']
    return send_from_directory(path, filename)

@admin.route('/upload/', methods=['POST'])
def upload():
    f = request.files.get('upload')
    extension = f.filename.split('.')[1].lower()
    if extension not in ['jpg', 'gif', 'png', 'jpeg']:
        return upload_fail(message='Image only!')
    f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    url = url_for('admin.uploaded_files', filename=f.filename)
    return upload_success(url=url)

@admin.route("/tables/<int:page>/", methods=["GET"])
@user_login_req
def tables(page=None):
    if page is None:
        page=1
    commodity_list = Commodity.query.filter(
        Commodity.role != 0
    ).order_by(
        Commodity.see.desc()
    ).order_by(
        Commodity.time.desc()
    ).paginate(page=page, per_page=12)
    return render_template("admin/tables.html",commodity_list=commodity_list)

@admin.route("/user/goods/<int:page>/", methods=["GET"])
@user_login_req
def userGoods(page=None):
    if page is None:
        page=1
    commodity_list = Commodity.query.filter(
        Commodity.role == 0
    ).order_by(
        Commodity.time.desc()
    ).paginate(page=page, per_page=12)
    return render_template("admin/userGoods.html",commodity_list=commodity_list)

@admin.route("/good/pass/<int:id>/", methods=["GET","POST"])
@user_login_req
def goodPass(id=None):
    commodity = Commodity.query.get_or_404(id)
    commodity.role = 2
    db.session.add(commodity)
    db.session.commit()
    flash("审核通过操作成功", "ok")
    return redirect(url_for("admin.userGoods", page=1))

@admin.route("/search/<int:page>/")
def search(page=None):
    if page is None:
        page = 1
    key = request.args.get("key","")
    commodity_list = Commodity.query.filter(
        Commodity.number.ilike('%' + key + '%')
    ).paginate(page=page, per_page=12)
    return render_template("admin/tables.html",key=key,commodity_list=commodity_list)

@admin.route("/edit/<int:id>/", methods=["GET","POST"])
@user_login_req
def edit(id=None):
    form = CommodityForm()
    commodity = Commodity.query.get_or_404(id)
    if request.method == "GET":
        img = commodity.content.split(',')
        form.description.data = commodity.description
        form.os.data = commodity.os
        form.sect.data = commodity.sect
        form.sex.data = commodity.sex
        form.bargain.data = commodity.bargain
        form.tel.data = commodity.tel
        form.wx.data = commodity.wx
    if form.validate_on_submit():
        data = form.data
        commodity.title = data["title"],
        commodity.price = data["price"],
        commodity.os = data["os"],
        commodity.number = data["number"],
        commodity.area = data["area"],
        commodity.server = data["server"],
        commodity.rank = data["rank"],
        commodity.type = data["type"],
        commodity.pet = data["pet"],
        commodity.sect = data["sect"],
        commodity.sex = data["sex"],
        commodity.bargain = data["bargain"],
        commodity.description = data["description"],
        commodity.content = data["content"],
        commodity.tel = data["tel"],
        commodity.wx = data["wx"]
        db.session.add(commodity)
        db.session.commit()
        flash("修改成功","ok")
        return redirect(url_for("admin.tables",page=1))
    return render_template("admin/forms_edit.html",form=form,commodity=commodity,img=img)

@admin.route("/see/<int:id>/", methods=["GET","POST"])
@user_login_req
def seeEdit(id=None):
    commodity = Commodity.query.get_or_404(id)
    if commodity.see == 0:
        commodity.see = 1
    else:
        commodity.see = 0
    db.session.add(commodity)
    db.session.commit()
    flash("修改成功", "ok")
    return redirect(url_for("admin.tables", page=1))

@admin.route("/del/<int:id>/", methods=["GET"])
@user_login_req
def delbook(id=None):
    commodity = Commodity.query.get_or_404(id)
    db.session.delete(commodity)
    db.session.commit()
    flash("删除成功","ok")
    return redirect(url_for("admin.tables",page=1))

def randID():
    nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")#当前时间
    str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"+nowTime
    sa = []
    for i in range(10):
        sa.append(random.choice(str))
    salt = ''.join(sa)
    return salt

