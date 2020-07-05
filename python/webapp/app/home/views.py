#encoding = utf-8
from . import home
from sqlalchemy import and_
from flask import render_template, redirect, url_for, flash, session, request, send_from_directory,make_response
from app.home.forms import CommodityForm
from app.models import Commodity,User
from app import db, app
from functools import wraps
import os,re,json,datetime,random,hashlib
from app.lib.aliyunsms.sms_send import send_sms
from app.lib.functions import change_filename
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename

def user_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "tel" not in session:
            return redirect(url_for("home.login", next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@home.route("/login/",methods=["GET","POST"])
def login():
    if request.method == 'POST':
        tel = request.form['phone']
        user = User.query.filter_by(tel=tel).count()
        if user == 0:
            return render_template("home/login_register.html",tel=tel)
        else:
            return render_template("home/login_user.html",tel=tel)
    return render_template("home/login_index.html")

@home.route("/login/register/",methods=["GET","POST"])
def loginRegister():
    if request.method == "GET":
        return render_template("home/login_register.html")
    phone = request.form["phone"]
    password = request.form["password"]
    password_con = request.form["password_con"]
    code = request.form["code"]
    if len(password) < 6 or len(password) > 20:
        d = {
            'code': 1,
            'msg': '密码长度不符合规范'
        }
        return json.dumps(d)
    if password != password_con:
        d = {
            'code': 1,
            'msg': '两次密码输入不一致'
        }
        return json.dumps(d)
    if 'sms_code' not in session:
        d = {
            'code': 1,
            'msg': '验证码已过期'
        }
        return json.dumps(d)
    if code != session["sms_code"]:
        d = {
            'code': 1,
            'msg': '验证码错误'
        }
        return json.dumps(d)
    user_v = User.query.filter_by(tel=phone).count()
    if user_v != 0:
        d = {
            'code': 1,
            'msg': '该手机号已注册！'
        }
        return json.dumps(d)
    user = User(
        tel = phone,
        password = generate_password_hash(password)
    )
    db.session.add(user)
    db.session.commit()
    d = {
        'code': 0,
        'msg': '注册成功'
    }
    return json.dumps(d)


@home.route("/login/user/",methods=["GET","POST"])
def loginUser():
    if request.method == 'POST':
        tel = request.form["phone"]
        password = request.form["password"]
        user = User.query.filter_by(tel=tel).first()
        if not user.check_pwd(password):
            d = {
                'code': 1,
                'msg': '密码错误'
            }
            return json.dumps(d)
        session["tel"] = tel
        session["user_id"] = user.id
        d = {
            'code': 0,
            'msg': '登录成功'
        }
        return json.dumps(d)
    return render_template("home/login_user.html")

@home.route("/login/forget/<tel>/",methods=["GET","POST"])
def loginForget(tel):
    tel = tel
    return render_template("home/forget.html",tel=tel)

@home.route("/login/editPass/",methods=["GET","POST"])
def loginEditPass():
    phone = request.form["phone"]
    password = request.form["password"]
    password_con = request.form["password_con"]
    code = request.form["code"]
    if len(password) < 6 or len(password) > 20:
        d = {
            'code': 1,
            'msg': '密码长度不符合规范'
        }
        return json.dumps(d)
    if password != password_con:
        d = {
            'code': 1,
            'msg': '两次密码输入不一致'
        }
        return json.dumps(d)
    if 'sms_code' not in session:
        d = {
            'code': 1,
            'msg': '验证码已过期'
        }
        return json.dumps(d)
    if code != session["sms_code"]:
        d = {
            'code': 1,
            'msg': '验证码错误'
        }
        return json.dumps(d)
    user = User.query.filter_by(tel=phone).first()
    user.password = generate_password_hash(password)
    db.session.add(user)
    db.session.commit()
    session.pop("tel", None)
    session.pop("user_id", None)
    d = {
        'code': 0,
        'msg': '重置密码成功'
    }
    return json.dumps(d)

@home.route("/logout/",methods=["GET","POST"])
@user_login_req
def logout():
    session.pop("tel",None)
    session.pop("user_id", None)
    return redirect(url_for("home.index"))


@home.route("/user/",methods=["GET","POST"])
@user_login_req
def user():
    return render_template("home/user.html")

@home.route("/")
def index():
    commodity_list = Commodity.query.order_by(
        Commodity.time.desc()
    ).limit(10).all()
    return render_template("home/index.html",commodity_list=commodity_list)


@home.route("/transaction/")
def transaction():
    return render_template("home/transaction.html")

@home.route("/suggest/")
def suggest():
    return render_template("home/suggest.html")

@home.route("/info/")
def info():
    return render_template("home/info.html")

@home.route("/sort/<int:page>/", methods=["GET"])
def sort(page=None):
    if page is None:
        page=1
    commodity_list = Commodity.query.filter(
        Commodity.role != 0
    ).order_by(
        Commodity.see.desc()
    ).order_by(
        Commodity.time.desc()
    ).paginate(page=page, per_page=10)
    return render_template("home/class.html",commodity_list=commodity_list)

@home.route("/price/asc/<int:page>/", methods=["GET"])
def priceAsc(page=None):
    if page is None:
        page=1
    commodity_list = Commodity.query.filter(
        Commodity.role != 0
    ).order_by(
        Commodity.price.asc()
    ).paginate(page=page, per_page=5)
    return render_template("home/class.html",commodity_list=commodity_list)

@home.route("/price/desc/<int:page>/", methods=["GET"])
def priceDesc(page=None):
    if page is None:
        page=1
    commodity_list = Commodity.query.filter(
        Commodity.role != 0
    ).order_by(
        Commodity.price.desc()
    ).paginate(page=page, per_page=5)
    return render_template("home/class.html",commodity_list=commodity_list)

@home.route("/detail/<int:id>/", methods=["GET"])
def detail(id=None):
    commodity = Commodity.query.get_or_404(id)
    img = commodity.content.split(',')
    return render_template("home/detail.html",commodity=commodity,img=img)

@home.route("/search/<int:page>/")
def search(page=None):
    if page is None:
        page = 1
    key = request.args.get("key","")
    commodity_list = Commodity.query.filter(
        Commodity.title.ilike('%' + key + '%')
    ).paginate(page=page, per_page=10)
    return render_template("home/class.html",key=key,commodity_list=commodity_list)

@home.route("/match/<int:page>/")
def match(page=None):
    if page is None:
        page = 1
    commodity_list = Commodity.query
    os = request.args.get("os", 0)
    minztprice = request.args.get("minztprice",0)
    maxztprice = request.args.get("maxztprice",0)
    type = request.args.get("duanwei",0)
    rank = request.args.get("shuliang",0)
    pet = request.args.get("pet",0)
    sex = request.args.get("mingwen",0)
    sect = request.args.get("price",0)
    if os:
        commodity_list = commodity_list.filter(Commodity.os == os)
    if minztprice:
        if maxztprice:
            commodity_list = commodity_list.filter(and_(Commodity.price >= minztprice,Commodity.price <= maxztprice))
    if type:
        commodity_list = commodity_list.filter(Commodity.type == type)
    if rank:
        if rank == '1':
            commodity_list = commodity_list.filter(and_(Commodity.rank >= 0, Commodity.rank <= 60))
        elif rank == '2':
            commodity_list = commodity_list.filter(and_(Commodity.rank >= 70, Commodity.rank <= 89))
        else:
            commodity_list = commodity_list.filter(and_(Commodity.rank >= 90, Commodity.rank <= 109))
    if pet:
        commodity_list = commodity_list.filter(Commodity.pet >= pet)
    if sex:
        commodity_list = commodity_list.filter(Commodity.sex == sex)
    if sect:
        commodity_list = commodity_list.filter(Commodity.sect == sect)
    commodity_list = commodity_list.paginate(page=page, per_page=10)
    return render_template("home/class.html",commodity_list=commodity_list)


@home.route("/sell/", methods=["GET","POST"])
@user_login_req
def sell():
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
            content=data["content"],
            tel=data["tel"],
            wx=data["wx"],
            role=0,
            user_id = session["user_id"]
        )
        db.session.add(commodity)
        db.session.commit()
        flash("添加成功","ok")
        return redirect(url_for("home.sell"))
    return render_template("home/sell.html",form=form)

def oneimg(str):
    return re.search(r'src=\"(.*?)\"', str).group(1)



@home.route('/upload/',methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        if not os.path.exists(app.config['UPLOADED_PATH']):
            os.makedirs(app.config['UPLOADED_PATH'])
            os.chmod(app.config['UPLOADED_PATH'],"rw")
        f_new_name = change_filename(f.filename)
        f.save(os.path.join(app.config['UPLOADED_PATH'], f_new_name))
        d = {
            'code': 0,
            'src' : f_new_name
        }
        return json.dumps(d)



@home.route('/sms_captcha/',methods=["GET","POST"])
def sms_captcha():
    tel = request.form['phone']
    timestamp = request.form['timestamp']
    sign = request.form['sign']
    res = validateCode(tel,timestamp,sign)
    if res == 1:
        result = random.randint(0, 999999)
        sms_code = "%06d" % result
        session["sms_code"] = sms_code
        params = {'code': sms_code }
        result = send_sms(tel, params)
        if result:
            d = {
                'code': 0,
                'msg': '已成功向 ' + tel + ' 发送验证短信'
            }
            return json.dumps(d)
        else:
            d = {
                'code': 400,
                'msg': '短信发送失败，请稍后再试'
            }
            return json.dumps(d)
    else:
        d = {
            'code': 500,
            'msg': '参数错误'
        }
        return json.dumps(d)


def randID():
    nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")#当前时间
    str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"+nowTime
    sa = []
    for i in range(26):
        sa.append(random.choice(str))
    salt = ''.join(sa)
    return salt


#验证前台发送短信的自定义令牌
def validateCode(telephone,timestamp,sign):
    salt = 'fgeWdLwg436t@$%$^'
    sign2 = hashlib.md5((timestamp + telephone + salt).encode('utf-8')).hexdigest()
    if sign == sign2:
        return 1
    else:
        return 0

def oneimg(str):
    img = str.split(',')
    return '/static/uploads/'+img[0]

env = app.jinja_env
env.filters['oneimg'] = oneimg