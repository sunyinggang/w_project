#encoding = utf-8
from . import home
from flask import render_template, redirect, url_for, flash, session, request
from app.home.forms import LoginForm,RegisterForm,AddressForm,ReviewForm
from app.models import User,Category,Product,Announcement,Cart,Address,Order,OrderProduct,Review,Help
from app import db,app
from functools import wraps
from werkzeug.utils import secure_filename
from sqlalchemy import and_
import datetime,random,json,os,uuid


#登录验证器（验证是否登录）
def user_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "userid" not in session:
            flash("请先登录")
            return redirect(url_for("home.login"))
        return f(*args, **kwargs)
    return decorated_function


#首页
@home.route("/")
def index():
    category = Category.query.all()
    new_product = Product.query.order_by(
        Product.create_time.desc()
    ).limit(4)
    announcement_list = Announcement.query.order_by(Announcement.create_time.desc()).limit(5)
    product = {}
    for v in category:
        product[v.id] = Product.query.filter(Product.category_id==v.id).order_by(Product.create_time.desc()).limit(5)
    return render_template("home/index.html",category=category,new_product=new_product,product=product,announcement_list=announcement_list)

#登录
@home.route("/login/",methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        user = User.query.filter_by(email=data["email"]).first()
        if not user:
            flash("账号不存在")
            return redirect(url_for("home.login"))
        if not user.check_pwd(data["password"]):
            flash("密码错误")
            return redirect(url_for("home.login"))
        session["nickname"] = user.nickname
        session["userid"] = user.id
        return redirect(url_for("home.index"))
    return render_template("home/login.html",form=form)

#退出
@home.route("/loginout/",methods=["GET","POST"])
def loginout():
    session.pop("nickname", None)
    session.pop("userid", None)
    return redirect(url_for("home.index"))

#注册
@home.route("/register/",methods=["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        data = form.data
        if data["password"] != data["passwordtwo"]:
            flash("密码不一致")
            return redirect(url_for("home.register"))
        user = User.query.filter_by(email=data["email"]).count()
        if user == 1:
            flash("邮箱已注册")
            return redirect(url_for("home.register"))
        user = User(
            nickname = data["nickname"],
            email = data["email"],
            password = data["password"]
        )
        db.session.add(user)
        db.session.commit()
        flash("注册成功！")
        return redirect(url_for("home.login"))
    return render_template("home/register.html",form=form)

#某分类商品列表
@home.route("/list/<int:page>/",methods=["GET","POST"])
def list(page=None):
    if page is None:
        page = 1
    id = int(request.args.get('id'))
    category = Category.query.all()
    now_category = Category.query.filter(Category.id == id).first()
    new_product = Product.query.filter(Product.category_id == id).order_by(Product.create_time.desc()).limit(2)
    product_list = Product.query.filter(Product.category_id==id).order_by(Product.create_time.desc()).paginate(page=page,per_page=10)
    return render_template("home/list.html",now_category=now_category,category=category,product_list=product_list,new_product=new_product,id=id)

#商品详情
@home.route("/detail/<int:id>/")
def detail(id=None):
    product = Product.query.filter_by(id=id).first_or_404()
    category = Category.query.all()
    review_list = Review.query.join(User).filter(
        Review.product_id == id
    ).order_by(Review.create_time.desc()).all()
    now_category = Category.query.filter(Category.id == product.category_id).first()
    new_product = Product.query.filter(Product.category_id == product.category_id).order_by(Product.create_time.desc()).limit(2)
    return render_template("home/detail.html",product=product,new_product=new_product,category=category,now_category=now_category,review_list=review_list)

#购物车
@home.route("/cart/")
def cart():
    cart = Cart.query.join(Product).join(Category).filter(
        Cart.user_id == session["userid"]
    ).filter(
        Cart.product_id == Product.id
    ).filter(
        Product.category_id == Category.id
    ).all()
    count = Cart.query.filter(Cart.user_id == session["userid"]).count()
    return render_template("home/cart.html",cart=cart,count=count)

#添加商品到购物车
@home.route("/add/cart/",methods=["GET","POST"])
@user_login_req
def addCart():
    id = int(request.args.get('id'))
    count = int(request.args.get('count'))
    cart = Cart.query.filter(and_(Cart.product_id == id,Cart.user_id == session["userid"] )).first()
    if cart:
        cart.count = cart.count+count
        db.session.add(cart)
        db.session.commit()
        flash("添加成功！")
        return redirect(url_for("home.detail",id=id))
    else:
        cart = Cart(
            user_id = session["userid"],
            product_id = id,
            count = count
        )
        db.session.add(cart)
        db.session.commit()
        flash("添加成功！")
        return redirect(url_for("home.detail", id=id))

#删除购物车商品
@home.route("/del/cart/",methods=["GET"])
def delCart():
    id = int(request.args.get("cart_id"))
    cart = Cart.query.get_or_404(id)
    db.session.delete(cart)
    db.session.commit()
    flash("删除成功")
    return redirect(url_for('home.cart'))

#查看会员个人信息
@home.route("/user/info/")
def info():
    user_id = session["userid"]
    address = Address.query.filter(
        Address.user_id == user_id
    ).filter(
        Address.status == 1
    ).first()
    if address:
        return render_template("home/user_center_info.html", address=address)
    else:
        flash("首次完善个人收货地址后才可查看个人信息！")
        return redirect(url_for('home.siteAddOne'))

#首次添加地址
@home.route("/user/site/one/",methods=["POST","GET"])
def siteAddOne():
    form = AddressForm()
    if form.validate_on_submit():
        data = form.data
        address = Address(
            name = data["name"],
            phone = data["phone"],
            address = data["address"],
            user_id = session["userid"],
            status = 1
        )
        db.session.add(address)
        db.session.commit()
        flash("添加成功！")
        return redirect(url_for('home.info'))
    return render_template("home/user_center_site.html",form=form)

#填加收货地址
@home.route("/user/site/add/",methods=["POST","GET"])
def siteAdd():
    form = AddressForm()
    if form.validate_on_submit():
        data = form.data
        address = Address(
            name = data["name"],
            phone = data["phone"],
            address = data["address"],
            user_id = session["userid"]
        )
        db.session.add(address)
        db.session.commit()
        flash("添加成功！")
        return redirect(url_for('home.siteList',page=1))
    return render_template("home/user_center_site.html",form=form)

#删除收货地址
@home.route("/user/site/del/<int:id>/",methods=["GET","POST"])
def siteDel(id=None):
    address = Address.query.filter(Address.id == id).first()
    db.session.delete(address)
    db.session.commit()
    flash("删除成功！")
    return redirect(url_for('home.siteList',page=1))

#展示地址列表
@home.route("/user/site/list/<int:page>/")
def siteList(page):
    if page is None:
        page = 1
    user_id = session["userid"]
    address = Address.query.filter(
        Address.user_id == user_id
    ).filter(
        Address.status == 0
    ).paginate(page=page,per_page=2)
    return render_template('home/user_site_list.html',address=address)

#查看个人订单
@home.route("/user/order/<int:page>/")
def order(page):
    if page is None:
        page = 1
    else:
        page = page
    order_list = Order.query.filter(Order.user_id == session["userid"]).order_by(Order.create_time.desc()).paginate(page, per_page=1)
    mul_order_list = {}
    for v in order_list.items:
        mul_order_list[v.id] = OrderProduct.query.filter(OrderProduct.order_id == v.id).all()
    for page_number in order_list.iter_pages():
        print('page_number:', page_number, page_number.__class__)
    return render_template("home/user_center_order.html",order_list=order_list,mul_order_list=mul_order_list)

#修改收货地址
@home.route("/user/site/<int:id>/",methods=["GET","POST"])
def site(id=None):
    form = AddressForm()
    address = Address.query.filter(Address.id == id).first()
    if request.method == "GET":
        form.name.data = address.name
        form.phone.data = address.phone
        form.address.data = address.address
    if form.validate_on_submit():
        data = form.data
        address.name = data["name"],
        address.phone = data["phone"],
        address.address = data["address"]
        db.session.add(address)
        db.session.commit()
        flash("修改成功！")
        return redirect(url_for('home.info'))
    return render_template("home/user_center_site.html",form=form)

#设置为默认收货地址
@home.route("/user/site/edit/<int:id>/",methods=["GET","POST"])
def siteEdit(id=None):
    address_now = Address.query.filter(
        Address.user_id == session["userid"]
    ).filter(
        Address.status == 1
    ).first()
    address_now.status = 0
    db.session.add(address_now)
    address = Address.query.filter(Address.id == id).first()
    address.status = 1
    db.session.add(address)
    db.session.commit()
    flash("修改成功！")
    return redirect(url_for('home.info'))

#直接购买商品
@home.route("/place/order/",methods=["GET","POST"])
@user_login_req
def placeOrder():
    user_id = session["userid"]
    address = Address.query.filter(
        Address.user_id == user_id
    ).filter(
        Address.status == 1
    ).first()
    if address is None:
        flash("请先完善自己的收货地址！")
        return redirect(url_for('home.siteAddOne'))
    if request.method == 'GET':
        product_id = request.args.get('id')
        count= int(request.args.get('count'))
        product = Product.query.join(Category).filter(
            Product.id == product_id
        ).filter(
            Category.id == Product.category_id
        ).first()
        price = int(product.price)*count
        if price < 1000:
            return render_template("home/place_order.html", product=product, address=address, count=count)
        else:
            category_id = Category.query.filter(Category.name == '伴娘服').first()
            product_list = Product.query.filter(Product.category_id == category_id.id).all()
            if price < 2000:
                return render_template("home/place_order_m.html", product=product, address=address, count=count,product_list=product_list)
            else:
                return render_template("home/place_order_mr.html", product=product, address=address, count=count,
                                       product_list=product_list)
    if request.method == 'POST':
        product = json.loads(request.form.get('product'))
        product_s = request.form.get('product_s','')
        count = int(request.form.get('count'))
        address = request.form.get('address')
        if product_s == '':
            order = Order(
                order_no=randID(),
                user_id=session["userid"],
                total_price=product["price"]*count,
                total_count=count,
                snap_address=address
            )
            db.session.add(order)
            db.session.flush()
            order_id = order.id
            order_product = OrderProduct(
                 order_id=order_id,
                 product_id=product["id"],
                 name=product["name"],
                 img=product["img"],
                 price=product["price"],
                 count=count
            )
            db.session.add(order_product)
            db.session.commit()
            return redirect(url_for('home.order',page=1))
        else:
            product_m = json.loads(request.form.get('product_s'))
            order = Order(
                order_no=randID(),
                user_id=session["userid"],
                total_price=product["price"] * count + product_m["price"],
                total_count=count,
                snap_address=address
            )
            db.session.add(order)
            db.session.flush()
            order_id = order.id
            order_product = OrderProduct(
                order_id=order_id,
                product_id=product["id"],
                name=product["name"],
                img=product["img"],
                price=product["price"],
                count=count
            )
            db.session.add(order_product)
            order_product_m = OrderProduct(
                order_id=order_id,
                product_id=product_m["id"],
                name=product_m["name"],
                img=product_m["img"],
                price=product_m["price"],
                count=1
            )
            db.session.add(order_product_m)
            db.session.commit()
            return redirect(url_for('home.order', page=1))

#购物车中购买商品
@home.route("/place/mulorder/",methods=["GET","POST"])
def placeMulorder():
    user_id = session["userid"]
    address = Address.query.filter(
        Address.user_id == user_id
    ).filter(
        Address.status == 1
    ).first()
    if address is None:
        flash("请先完善自己的收货地址！")
        return redirect(url_for('home.siteAddOne'))
    if request.method == 'GET':
        product = json.loads(request.args.get('cart'))#携带购物车点击选择购买的商品信息
        product_list = []
        count = {}
        sum = 0
        itemCount = 0
        for v in product:#循环点击的每个商品
            productOne = Product.query.join(Category).filter(
                Product.id==v["product_id"]
            ).filter(
                Category.id == Product.category_id
            ).first()
            product_list.append(productOne)#商品存入一个新数组
            count[productOne.id] = v["count"]#存储每个商品的购买数量
            itemCount+=v["count"]#总的购买数量
            sum+=(v["count"]*productOne.price)#总价=每个商品单价*数量之和
        if sum < 1000:#商品总价小于1000直接进入订单确认
            return render_template("home/place_mulorder.html",product_list=product_list,itemCount=itemCount,address=address,count=count,sum=sum)
        else:
            category_id = Category.query.filter(Category.name == '伴娘服').first()
            product_list_b = Product.query.filter(Product.category_id == category_id.id).all()
            if sum < 2000:#总价小于两千
                return render_template("home/place_mulorder_m.html",product_list=product_list,product_list_b=product_list_b,itemCount=itemCount,address=address,count=count,sum=sum)
            else:#总价大于两千
                return render_template("home/place_mulorder_mr.html",product_list=product_list,product_list_b=product_list_b,itemCount=itemCount,address=address,count=count,sum=sum)
    if request.method == 'POST':#确认提交订单
        mul_product = json.loads(request.form.get('mul_product'))#获取到确认订单页面传入的商品信息
        sum = request.form.get('sum')
        product_s = request.form.get('product_s', '')
        itemCount = request.form.get('itemCount')
        count = json.loads(request.form.get('count'))
        address = request.form.get('address')
        if product_s == '':#此字段为空，代表没有选择伴娘服
            order = Order(#保存订单信息
                order_no=randID(),
                user_id=session["userid"],
                total_price=sum,
                total_count=itemCount,
                snap_address=address
            )
            db.session.add(order)
            db.session.flush()
            order_id = order.id#获取到上边创建的订单的id
            for v in mul_product:#循环每个购买的商品
                cart = Cart.query.filter(Cart.product_id==v["id"]).first()#在购物车获取到每个商品的信息
                id = str(v["id"])
                if cart.count == count[id]:#如果选中购买的数量等于购物车拥有的数量
                    db.session.delete(cart)#直接在购物车删除这个商品
                else:
                    cart.count=cart.count-count[id]#如果你购物车这个商品有好几个，你只选择其中一部分购买，代表这个商品你购物车还应该存在，但是要更新数量
                    db.session.add(cart)
                order_product = OrderProduct(#这个代表订单中具体的商品信息，一个订单包括多个订单商品
                    order_id=order_id,
                    product_id=v["id"],
                    name=v["name"],
                    img=v["img"],
                    price=v["price"],
                    count=count[id]
                )
                db.session.add(order_product)
            db.session.commit()
            return redirect(url_for('home.order',page=1))
        else:
            product_m = json.loads(request.form.get('product_s'))
            order = Order(
                order_no=randID(),
                user_id=session["userid"],
                total_price=float(sum) + product_m["price"],
                total_count=itemCount,
                snap_address=address
            )
            db.session.add(order)
            db.session.flush()
            order_id = order.id
            for v in mul_product:
                cart = Cart.query.filter(Cart.product_id == v["id"]).first()
                id = str(v["id"])
                if cart.count == count[id]:
                    db.session.delete(cart)
                else:
                    cart.count = cart.count - count[id]
                    db.session.add(cart)
                order_product = OrderProduct(
                    order_id=order_id,
                    product_id=v["id"],
                    name=v["name"],
                    img=v["img"],
                    price=v["price"],
                    count=count[id]
                )
                db.session.add(order_product)
            order_product_m = OrderProduct(
                order_id=order_id,
                product_id=product_m["id"],
                name=product_m["name"],
                img=product_m["img"],
                price=product_m["price"],
                count=1
            )
            db.session.add(order_product_m)
            db.session.commit()
            return redirect(url_for('home.order', page=1))

#评论
@home.route("/review/<int:id>/",methods=["GET","POST"])
def review(id=None):
    form = ReviewForm()
    order_id = id
    img = ''
    order = Order.query.filter(Order.id == order_id).first()
    order_product = OrderProduct.query.filter(OrderProduct.order_id == order_id).all()
    if order.review_status == 1:
        review = Review.query.filter(Review.order_id==order.id).first()
        form.content.data = review.content
        img = review.img
    if form.validate_on_submit():
        data = form.data
        file_img = secure_filename(form.img.data.filename)
        if not os.path.exists(app.config["UP_DIR"]):
            os.makedirs(app.config["UP_DIR"])
            os.chmod(app.config["UP_DIR"],"rw")
        img = change_filename(file_img)
        form.img.data.save(app.config["UP_DIR"]+img)
        for v in order_product:
            review = Review(
                user_id = session["userid"],
                order_id = order_id,
                product_id = v.product_id,
                content = data["content"],
                img = img
            )
            db.session.add(review)
        order.review_status = 1
        db.session.add(order)
        db.session.commit()
        flash("成功添加评价！")
        return redirect(url_for('home.order',page=1))
    return render_template("home/review.html",form=form,order=order,order_product=order_product,img=img)

#删除评论
@home.route("/del/review/<int:id>/",methods=["GET"])
def delReview(id=None):
    order_id = id
    order = Order.query.filter(Order.id == order_id).first()
    order.review_status = 0
    db.session.add(order)
    review = Review.query.filter(Review.order_id == order_id).first()
    db.session.delete(review)
    db.session.commit()
    flash("删除成功！")
    return redirect(url_for("home.order",page=1))

#搜索
@home.route("/search/<int:page>/",methods=["GET"])
def search(page=None):
    if page is None:
        page = 1
    key = request.args.get('key','')
    category = Category.query.all()
    new_product = Product.query.order_by(Product.create_time.desc()).limit(2)
    product_list = Product.query.filter(
        Product.name.ilike('%'+key+'%')
    ).paginate(page=page,per_page=10)
    product_count = Product.query.filter(
        Product.name.ilike('%' + key + '%')
    ).count()
    if product_count == 0:
        flash("搜索内容不存在，请重新输入！")
        return render_template("home/search_content.html",key=key, product_list=product_list,category=category,new_product=new_product)
    return render_template("home/search_content.html", key=key, product_list=product_list,category=category,new_product=new_product)

#查看公告
@home.route("/announcement/<int:id>/",methods=["GET"])
def announcement(id=None):
    announcement = Announcement.query.filter(Announcement.id == id).first()
    return render_template("home/announcement.html", announcement=announcement)

#帮助中心
@home.route("/help/")
def help():
    help = Help.query.filter(Help.id == 1).first()
    return render_template("home/help.html",help=help)

#创建订单号
def randID():
    nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")#当前时间
    str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"+nowTime
    sa = []
    for i in range(26):
        sa.append(random.choice(str))
    salt = ''.join(sa)
    return salt

#修改上传的图片名
def change_filename(filename):
    fileinfo = os.path.splitext(filename)
    filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S")+str(uuid.uuid4().hex)+fileinfo[-1]
    return filename
