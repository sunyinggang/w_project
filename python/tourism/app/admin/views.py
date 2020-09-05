#encoding = utf-8
from . import admin
from flask import render_template, redirect, url_for, flash, session, request, send_from_directory
from app.admin.forms import LoginForm, CategoryForm,ProductForm
from app.models import Admin,Category,Product,People,Natural,History
from functools import wraps
from app import db, app
import os,uuid,datetime
from werkzeug.utils import secure_filename

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

@admin.route("/category/<int:page>/")
@user_login_req
def category(page=None):
    if page is None:
        page = 1
    category_list = Category.query.paginate(page=page,per_page=5)
    return render_template("admin/category.html",category_list=category_list)

@admin.route("/edit/category/<int:id>/",methods=["GET","POST"])
@user_login_req
def editCategory(id=None):
    form = CategoryForm()
    category = Category.query.get_or_404(id)
    if request.method == 'GET':
        form.name.data = category.name
    if form.validate_on_submit():
        data = form.data
        category.name = data["name"]
        db.session.add(category)
        db.session.commit()
        flash("修改成功", "ok")
        return redirect(url_for("admin.category",page=1))
    return render_template("admin/categoryAdd.html", form=form)

@admin.route("/del/category/<int:id>/",methods=["GET","POST"])
@user_login_req
def delCategory(id=None):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    flash("删除成功")
    return redirect(url_for("admin.category",page=1))

@admin.route("/product/<int:page>/")
@user_login_req
def product(page=None):
    if page is None:
        page = 1
    product_list = Product.query.join(Category).filter(
        Category.id == Product.category_id
    ).order_by(
        Product.create_time.desc()
    ).paginate(page=page,per_page=5)
    return render_template("admin/product.html",product_list=product_list)

@admin.route("/edit/product/<int:id>/", methods=["GET","POST"])
@user_login_req
def editProduct(id=None):
    form = ProductForm()
    product = Product.query.get_or_404(id)
    if request.method == "GET":
        form.content.data = product.content
    if request.method == 'POST':
        data = form.data
        if not os.path.exists(app.config["UP_DIR"]):
            os.makedirs(app.config["UP_DIR"])
            os.chmod(app.config["UP_DIR"],"rw")
        if form.img.data != "":
            file_img = secure_filename(form.img.data.filename)
            product.img = change_filename(file_img)
            form.img.data.save(app.config["UP_DIR"]+product.img)
        product.name = data["name"],
        product.category_id = data["category_id"],
        product.content = data["content"]
        db.session.add(product)
        db.session.commit()
        flash("修改成功！")
        return redirect(url_for("admin.editProduct",id=id))
    return render_template("admin/productEdit.html", form=form,product=product)

@admin.route("/del/product/<int:id>/", methods=["GET","POST"])
@user_login_req
def delProduct(id=None):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    flash("删除成功！")
    return redirect(url_for("admin.product",page=1))

@admin.route("/add/product/", methods=["GET","POST"])
@user_login_req
def addProduct():
    form = ProductForm()
    if request.method == 'POST':
        data = form.data
        file_img = secure_filename(form.img.data.filename)
        if not os.path.exists(app.config["UP_DIR"]):
            os.makedirs(app.config["UP_DIR"])
            os.chmod(app.config["UP_DIR"],"rw")
        img = change_filename(file_img)
        form.img.data.save(app.config["UP_DIR"]+img)
        product = Product(
            name = data["name"],
            img = img,
            category_id = data["category_id"],
            content = data["content"]
        )
        db.session.add(product)
        db.session.commit()
        flash("添加成功！")
        return redirect(url_for("admin.product",page=1))
    return render_template("admin/productAdd.html", form=form)

@admin.route("/people/<int:page>/")
@user_login_req
def people(page=None):
    if page is None:
        page = 1
    product_list = People.query.order_by(
        People.create_time.desc()
    ).paginate(page=page,per_page=10)
    return render_template("admin/people.html",product_list=product_list)

@admin.route("/edit/people/<int:id>/", methods=["GET","POST"])
@user_login_req
def editPeople(id=None):
    form = ProductForm()
    product = People.query.get_or_404(id)
    if request.method == "GET":
        form.content.data = product.content
    if request.method == 'POST':
        data = form.data
        if not os.path.exists(app.config["UP_DIR"]):
            os.makedirs(app.config["UP_DIR"])
            os.chmod(app.config["UP_DIR"],"rw")
        if form.img.data != "":
            file_img = secure_filename(form.img.data.filename)
            product.img = change_filename(file_img)
            form.img.data.save(app.config["UP_DIR"]+product.img)
        product.name = data["name"],
        product.content = data["content"]
        db.session.add(product)
        db.session.commit()
        flash("修改成功！")
        return redirect(url_for("admin.editPeople",id=id))
    return render_template("admin/peopleEdit.html", form=form,product=product)

@admin.route("/del/people/<int:id>/", methods=["GET","POST"])
@user_login_req
def delPeople(id=None):
    product = People.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    flash("删除成功！")
    return redirect(url_for("admin.people",page=1))

@admin.route("/add/people/", methods=["GET","POST"])
@user_login_req
def addPeople():
    form = ProductForm()
    if request.method == 'POST':
        data = form.data
        file_img = secure_filename(form.img.data.filename)
        if not os.path.exists(app.config["UP_DIR"]):
            os.makedirs(app.config["UP_DIR"])
            os.chmod(app.config["UP_DIR"],"rw")
        img = change_filename(file_img)
        form.img.data.save(app.config["UP_DIR"]+img)
        product = People(
            name = data["name"],
            img = img,
            content = data["content"]
        )
        db.session.add(product)
        db.session.commit()
        flash("添加成功！")
        return redirect(url_for("admin.people",page=1))
    return render_template("admin/peopleAdd.html", form=form)

@admin.route("/natural/<int:page>/")
@user_login_req
def natural(page=None):
    if page is None:
        page = 1
    product_list = Natural.query.order_by(
        Natural.create_time.desc()
    ).paginate(page=page,per_page=10)
    return render_template("admin/natural.html",product_list=product_list)

@admin.route("/edit/natural/<int:id>/", methods=["GET","POST"])
@user_login_req
def editNatural(id=None):
    form = ProductForm()
    product = Natural.query.get_or_404(id)
    if request.method == "GET":
        form.content.data = product.content
    if request.method == 'POST':
        data = form.data
        if not os.path.exists(app.config["UP_DIR"]):
            os.makedirs(app.config["UP_DIR"])
            os.chmod(app.config["UP_DIR"],"rw")
        if form.img.data != "":
            file_img = secure_filename(form.img.data.filename)
            product.img = change_filename(file_img)
            form.img.data.save(app.config["UP_DIR"]+product.img)
        product.name = data["name"],
        product.content = data["content"]
        db.session.add(product)
        db.session.commit()
        flash("修改成功！")
        return redirect(url_for("admin.editNatural",id=id))
    return render_template("admin/naturalEdit.html", form=form,product=product)

@admin.route("/del/natural/<int:id>/", methods=["GET","POST"])
@user_login_req
def delNatural(id=None):
    product = Natural.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    flash("删除成功！")
    return redirect(url_for("admin.natural",page=1))

@admin.route("/add/natural/", methods=["GET","POST"])
@user_login_req
def addNatural():
    form = ProductForm()
    if request.method == 'POST':
        data = form.data
        file_img = secure_filename(form.img.data.filename)
        if not os.path.exists(app.config["UP_DIR"]):
            os.makedirs(app.config["UP_DIR"])
            os.chmod(app.config["UP_DIR"],"rw")
        img = change_filename(file_img)
        form.img.data.save(app.config["UP_DIR"]+img)
        product = Natural(
            name = data["name"],
            img = img,
            content = data["content"]
        )
        db.session.add(product)
        db.session.commit()
        flash("添加成功！")
        return redirect(url_for("admin.natural",page=1))
    return render_template("admin/naturalAdd.html", form=form)


@admin.route("/history/<int:page>/")
@user_login_req
def history(page=None):
    if page is None:
        page = 1
    product_list = History.query.order_by(
        History.create_time.desc()
    ).paginate(page=page,per_page=10)
    return render_template("admin/history.html",product_list=product_list)

@admin.route("/edit/history/<int:id>/", methods=["GET","POST"])
@user_login_req
def editHistory(id=None):
    form = ProductForm()
    product =History.query.get_or_404(id)
    if request.method == "GET":
        form.content.data = product.content
    if request.method == 'POST':
        data = form.data
        if not os.path.exists(app.config["UP_DIR"]):
            os.makedirs(app.config["UP_DIR"])
            os.chmod(app.config["UP_DIR"],"rw")
        if form.img.data != "":
            file_img = secure_filename(form.img.data.filename)
            product.img = change_filename(file_img)
            form.img.data.save(app.config["UP_DIR"]+product.img)
        product.name = data["name"],
        product.content = data["content"]
        db.session.add(product)
        db.session.commit()
        flash("修改成功！")
        return redirect(url_for("admin.editHistory",id=id))
    return render_template("admin/historyEdit.html", form=form,product=product)

@admin.route("/del/history/<int:id>/", methods=["GET","POST"])
@user_login_req
def delHistory(id=None):
    product = History.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    flash("删除成功！")
    return redirect(url_for("admin.history",page=1))

@admin.route("/add/history/", methods=["GET","POST"])
@user_login_req
def addHistory():
    form = ProductForm()
    if request.method == 'POST':
        data = form.data
        file_img = secure_filename(form.img.data.filename)
        if not os.path.exists(app.config["UP_DIR"]):
            os.makedirs(app.config["UP_DIR"])
            os.chmod(app.config["UP_DIR"],"rw")
        img = change_filename(file_img)
        form.img.data.save(app.config["UP_DIR"]+img)
        product = History(
            name = data["name"],
            img = img,
            content = data["content"]
        )
        db.session.add(product)
        db.session.commit()
        flash("添加成功！")
        return redirect(url_for("admin.history",page=1))
    return render_template("admin/historyAdd.html", form=form)

def change_filename(filename):
    fileinfo = os.path.splitext(filename)
    filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S")+str(uuid.uuid4().hex)+fileinfo[-1]
    return filename

@admin.route("/add/category/",methods=["GET","POST"])
@user_login_req
def addCategory():
    form = CategoryForm()
    if form.validate_on_submit():
        data = form.data
        category = Category(
            name = data["name"]
        )
        db.session.add(category)
        db.session.commit()
        flash("添加成功", "ok")
        return redirect(url_for("admin.category",page=1))
    return render_template("admin/categoryAdd.html", form=form)