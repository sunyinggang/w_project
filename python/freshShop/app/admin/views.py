#encoding = utf-8
from . import admin
from flask import render_template, redirect, url_for, flash, session, request,send_from_directory
from app.admin.forms import LoginForm, CategoryForm,ProductForm,AnnouncementForm,HelpForm,ReviewForm
from app.models import Admin,Category,Product,Announcement,Help,User,OrderProduct,Order,Address,Review
from functools import wraps
from app import db, app
import os,uuid,datetime
from werkzeug.utils import secure_filename
from sqlalchemy import func
from flask_ckeditor import upload_success, upload_fail

#登录验证器，验证是否登录
def user_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "username" not in session:
            return redirect(url_for("admin.login", next=request.url))
        return f(*args, **kwargs)
    return decorated_function

#首页
@admin.route("/")
@user_login_req
def index():
    return render_template("admin/index.html")

#登录处理
@admin.route("/login/", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        user = Admin.query.filter_by(username=data["username"]).first()
        if not user:
            flash("账号不存在")
            return redirect(url_for("admin.login"))
        if not user.check_pwd(data["password"]):
            flash("密码错误")
            return redirect(url_for("admin.login"))
        session["username"] = data["username"]
        session["userid"] = user.id
        return redirect(request.args.get("next") or url_for("admin.index"))
    return render_template("admin/login.html", form=form)

#退出
@admin.route("/logout/", methods=["GET"])
@user_login_req
def logout():
    session.pop("username",None)
    session.pop("userid", None)
    return redirect(url_for("admin.login"))

#查看商品分类
@admin.route("/category/<int:page>/")
@user_login_req
def category(page=None):
    if page is None:
        page = 1
    category_list = Category.query.paginate(page=page,per_page=5)
    return render_template("admin/category.html",category_list=category_list)

#修改商品分类
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

#删除商品分类
@admin.route("/del/category/<int:id>/",methods=["GET","POST"])
@user_login_req
def delCategory(id=None):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    flash("删除成功")
    return redirect(url_for("admin.category",page=1))

#查看商品列表
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

#修改商品信息
@admin.route("/edit/product/<int:id>/", methods=["GET","POST"])
@user_login_req
def editProduct(id=None):
    form = ProductForm()
    product = Product.query.get_or_404(id)
    if request.method == 'POST':
        data = form.data
        if not os.path.exists(app.config["UP_DIR"]):
            os.makedirs(app.config["UP_DIR"])
            os.chmod(app.config["UP_DIR"],"rw")
        if form.img.data != "":
            file_img = secure_filename(form.img.data.filename)
            product.img = change_filename(file_img)
            form.img.data.save(app.config["UP_DIR"]+product.img)
        product.name = data["name"]
        product.category_id = data["category_id"]
        product.price = data["price"]
        product.content = data["content"]
        db.session.add(product)
        db.session.commit()
        flash("修改成功！")
        return redirect(url_for("admin.editProduct",id=id))
    if request.method == "GET":
        form.content.data = product.content
    return render_template("admin/productEdit.html", form=form,product=product)

#删除商品
@admin.route("/del/product/<int:id>/", methods=["GET","POST"])
@user_login_req
def delProduct(id=None):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    flash("删除成功！")
    return redirect(url_for("admin.product",page=1))

#添加商品
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
            price = data["price"],
            content = data["content"]
        )
        db.session.add(product)
        db.session.commit()
        flash("添加成功！")
        return redirect(url_for("admin.product",page=1))
    return render_template("admin/productAdd.html", form=form)

#修改上传的图片名
def change_filename(filename):
    fileinfo = os.path.splitext(filename)
    filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S")+str(uuid.uuid4().hex)+fileinfo[-1]
    return filename

#添加商品分类
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

#查看公告
@admin.route("/announcement/<int:page>/")
@user_login_req
def announcement(page=None):
    if page is None:
        page = 1
    announcement_list = Announcement.query.order_by(
        Announcement.create_time.desc()
    ).paginate(page=page,per_page=5)
    return render_template("admin/announcement.html",announcement_list=announcement_list)

#添加公告
@admin.route("/add/announcement/",methods=["GET","POST"])
@user_login_req
def addAnnouncement():
    form = AnnouncementForm()
    if form.validate_on_submit():
        data = form.data
        announcement = Announcement(
            title = data["title"],
            content = data["content"]
        )
        db.session.add(announcement)
        db.session.commit()
        flash("添加成功！")
        return redirect(url_for('admin.announcement',page=1))
    return render_template("admin/announcementAdd.html",form=form)

#编辑公告
@admin.route("/edit/announcement/<int:id>/",methods=["GET","POST"])
@user_login_req
def editAnnouncement(id=None):
    form = AnnouncementForm()
    announcement = Announcement.query.get_or_404(id)
    if request.method == 'GET':
        form.title.data = announcement.title
        form.content.data = announcement.content
    if form.validate_on_submit():
        data = form.data
        announcement.title = data["title"]
        announcement.content = data["content"]
        db.session.add(announcement)
        db.session.commit()
        flash("修改成功！")
        return redirect(url_for('admin.announcement',page=1))
    return render_template("admin/announcementAdd.html",form=form)

#删除公告
@admin.route("/del/announcement/<int:id>/",methods=["GET","POST"])
@user_login_req
def delAnnouncement(id=None):
    announcement = Announcement.query.get_or_404(id)
    db.session.delete(announcement)
    db.session.commit()
    flash("删除成功")
    return redirect(url_for("admin.announcement",page=1))

#查找商品
@admin.route("/search/<int:page>/",methods=["GET"])
def search(page):
    if page is None:
        page = 1
    key = request.args.get('key','')
    product_list = Product.query.filter(
        Product.name.ilike('%'+key+'%')
    ).paginate(page=page,per_page=5)
    product_count = Product.query.filter(
        Product.name.ilike('%' + key + '%')
    ).count()
    if product_count == 0:
        flash("搜索内容不存在，请重新输入！")
        return render_template("admin/product.html", product_list=product_list)
    return render_template("admin/product.html", product_list=product_list)

#帮助中心
@admin.route("/help/",methods=["GET","POST"])
@user_login_req
def help():
    help = Help.query.first()
    form = HelpForm()
    if help is None:
        help.info = ''
        help.problem = ''
        help.distribution = ''
    if request.method == "GET":
        form.info.data = help.info
        form.problem.data = help.problem
        form.distribution.data = help.distribution
    if form.validate_on_submit():
        data = form.data
        help.info = data["info"]
        help.problem = data["problem"]
        help.distribution = data["distribution"]
        db.session.add(help)
        db.session.commit()
        flash("修改成功！")
        return redirect(url_for('admin.help'))
    return render_template("admin/help.html",form=form)

#会员列表
@admin.route("/member/<int:page>/")
@user_login_req
def member(page=None):
    if page is None:
        page = 1
    user_list = User.query.paginate(page=page,per_page=5)
    return render_template("admin/member.html",user_list=user_list)

#会员购买记录
@admin.route("/member/detail/<int:page>/",methods=["GET","POST"])
@user_login_req
def memberDetail(page=None):
    id = request.args.get('id')
    if page is None:
        page = 1
    order_list = Order.query.filter(Order.user_id == id).order_by(Order.create_time.desc()).paginate(page=page,per_page=5)
    mul_order_list = {}
    for v in order_list.items:
        mul_order_list[v.id] = OrderProduct.query.filter(OrderProduct.order_id == v.id).all()
    return render_template("admin/member_detail.html",order_list=order_list,mul_order_list=mul_order_list,id=id)

#查看会员商品评论
@admin.route("/review/<int:id>/")
@user_login_req
def review(id=None):
    form = ReviewForm()
    order_id = id
    order = Order.query.filter(Order.id == order_id).first()
    order_product = OrderProduct.query.filter(OrderProduct.order_id == order_id).all()
    review = Review.query.filter(Review.order_id == Order.id).first()
    form.content.data = review.content
    img = review.img
    return render_template("admin/review.html",form=form,order=order,order_product=order_product,img=img)

#查看未发货订单
@admin.route("/order/<int:page>/")
@user_login_req
def order(page=None):
    if page is None:
        page = 1
    order_list = Order.query.filter(Order.status == 1).order_by(Order.create_time.desc()).paginate(page=page,per_page=5)
    mul_order_list = {}
    for v in order_list.items:
        mul_order_list[v.id] = OrderProduct.query.filter(OrderProduct.order_id == v.id).all()
    return render_template("admin/order.html",order_list=order_list,mul_order_list=mul_order_list)

#订单发货
@admin.route("/pro/order/<int:id>/")
@user_login_req
def proOrder(id=None):
    order = Order.query.filter(Order.id == id).first()
    order.status = 2
    db.session.add(order)
    db.session.commit()
    flash("发货成功！")
    return redirect(url_for('admin.order',page=1))

#查看已发货订单
@admin.route("/already/order/<int:page>/")
@user_login_req
def alreadyOrder(page=None):
    if page is None:
        page = 1
    order_list = Order.query.filter(Order.status == 2).order_by(Order.create_time.desc()).paginate(page=page,per_page=5)
    mul_order_list = {}
    for v in order_list.items:
        mul_order_list[v.id] = OrderProduct.query.filter(OrderProduct.order_id == v.id).all()
    return render_template("admin/already_order.html",order_list=order_list,mul_order_list=mul_order_list)

#查看销售统计
@admin.route("/money/<int:page>/")
@user_login_req
def money(page=None):
    if page is None:
        page = 1
    order_list = Order.query.filter(Order.status == 1).all()#订单分开累加金额，status=1代表已支付订单，status=2代表已发货订单
    al_order_list = Order.query.filter(Order.status == 2).all()
    #查询商品销售排名，主要是通过对订单商品进行每个商品的数量count统计，然后进行倒序排序order_by
    product_list = db.session.query(OrderProduct.name, func.sum(OrderProduct.count),OrderProduct.product_id).group_by(
        OrderProduct.product_id).order_by(func.sum(OrderProduct.count).desc()).paginate(page=page,per_page=8)
    money = alreadyMoney = 0
    for v in order_list:#已支付订单金额
        money += v.total_price
    for v in al_order_list:#已发货订单金额
        alreadyMoney += v.total_price
    return render_template("admin/money.html",money=money,alreadyMoney=alreadyMoney,product_list=product_list)

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