#encoding = utf-8
from . import home
from flask import render_template,flash,redirect,url_for,session,request
from app.home.forms import LoginForm, RegisterForm, StaffRegisterForm, TicketForm
from werkzeug.security import generate_password_hash
from app.models import Customer, Agent, Staff, Flight, Ticket
from app import db
import random,string
from functools import wraps
from sqlalchemy import and_

def user_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "username" not in session:
            flash("please log in first!")
            return redirect(url_for("home.login"))
        return f(*args, **kwargs)
    return decorated_function


@home.route("/login/",methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        if data["usertype"] == 1:
            customer = Customer.query.filter_by(email=data["email"]).first()
            if not customer.check_pwd(data["password"]):
                flash("Wrong password!")
                return redirect(url_for("home.login"))
            session["username"] = data["email"]
            session["url"] = "customer.index"
            session["type"] = 1
            return redirect(url_for("home.index"))
        if data["usertype"] == 2:
            agent = Agent.query.filter_by(email=data["email"]).first()
            if not agent.check_pwd(data["password"]):
                flash("Wrong password!")
                return redirect(url_for("home.login"))
            session["username"] = data["email"]
            session["url"] = "agent.index"
            session["type"] = 2
            return redirect(url_for("home.index"))
        if data["usertype"] == 3:
            staff = Staff.query.filter_by(username=data["email"]).first()
            if not staff.check_pwd(data["password"]):
                flash("Wrong password!")
                return redirect(url_for("home.login"))
            session["username"] = data["email"]
            session["url"] = "staff.index"
            session["type"] = 3
            return redirect(url_for("staff.index"))
    return render_template("home/login.html",form=form)

@home.route("/signup/",methods=["GET","POST"])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        data = form.data
        if data["password"] != data["passwordtwo"]:
            flash("密码不一致")
            return redirect(url_for("home.signup"))
        if data["usertype"] == 1:
            customer = Customer.query.filter_by(email=data["email"]).count()
            if customer == 1:
                flash(generate_password_hash(data["password"]))
                return redirect(url_for("home.signup"))
            customer = Customer(
                email = data["email"],
                password = generate_password_hash(data["password"])
            )
            db.session.add(customer)
            db.session.commit()
            flash("Registration success！")
            return redirect(url_for("home.login"))
        if data["usertype"] == 2:
            agent = Agent.query.filter_by(email=data["email"]).count()
            if agent == 1:
                flash("The email already exists!")
                return redirect(url_for("home.signup"))
            agent = Agent(
                email=data["email"],
                password=generate_password_hash(data["password"]),
                booking_agent_id = ''.join(random.sample(string.ascii_letters + string.digits, 8))
            )
            db.session.add(agent)
            db.session.commit()
            flash("Registration success！")
            return redirect(url_for("home.login"))
    return render_template("home/signup.html",form=form)

@home.route("/stfsignup/",methods=["GET","POST"])
def stfSignup():
    form = StaffRegisterForm()
    if form.validate_on_submit():
        data = form.data
        if data["password"] != data["passwordtwo"]:
            flash("密码不一致")
            return redirect(url_for("home.stfSignup"))
        staff = Staff.query.filter_by(username=data["username"]).count()
        if staff == 1:
            flash("The username already exists!")
            return redirect(url_for("home.stfSignup"))
        staff = Staff(
            username=data["username"],
            password=generate_password_hash(data["password"]),
            airline_name=data["airline_name"]
        )
        db.session.add(staff)
        db.session.commit()
        flash("Registration success！")
        return redirect(url_for("home.login"))
    return render_template("home/staffsignup.html",form=form)

@home.route("/logout/")
def logout():
    session.pop("username",None)
    session.pop("url", None)
    session.pop("type", None)
    return redirect(url_for("home.login"))

@home.route("/")
def index():
    flight_list = Flight.query.filter(Flight.status == "upcoming")
    return render_template("home/index.html",flight_list=flight_list)

@home.route("/buy/flight/<id>/",methods=["GET","POST"])
@user_login_req
def buy(id=None):
    form = TicketForm()
    flight = Flight.query.filter_by(flight_num=id).first_or_404()
    if session['type'] == 1:
        email= session['username']
        booking_agent_ID = ''
    elif session['type'] == 2:
        email = ''
        agent = Agent.query.filter(Agent.email == session['username']).first()
        booking_agent_ID = agent.booking_agent_id
    if flight.rest_seat == 0:
        flash("The rest ticket are zero and cannot be purchased.")
        return redirect(url_for("home.index"))
    if form.validate_on_submit():
        data = form.data
        ticket = Ticket(
            ticket_id=''.join(random.sample(string.ascii_letters + string.digits, 6)),
            user_email = data["email"],
            airline_name = flight.airline_name,
            flight_num = data["flight_num"],
            price = data["price"],
            booking_agent_ID = booking_agent_ID
        )
        db.session.add(ticket)
        flight.rest_seat = flight.rest_seat-1
        db.session.add(flight)
        db.session.commit()
        flash("Buy success！")
        return redirect(url_for("home.index"))
    return render_template("home/buy-flight.html",form=form,flight=flight,email=email)

@home.route("/flight/status/")
def flystatus():
    flight_list = Flight.query.all()
    return render_template("home/flight-status.html",flight_list=flight_list)

@home.route("/search/")
def search():
    departure_airport = request.args.get("departure_airport")
    arrival_airport = request.args.get("arrival_airport")
    departure_city = request.args.get("departure_city")
    arrival_city = request.args.get("arrival_city")
    start_time = request.args.get("start_time")
    end_time = request.args.get("end_time")
    flight_list = Flight.query
    if departure_airport:
        flight_list = flight_list.filter(Flight.departure_airport_name == departure_airport)
    if arrival_airport:
        flight_list = flight_list.filter(Flight.arrival_airport_name == arrival_airport)
    if departure_city:
        flight_list = flight_list.filter(Flight.departure_city == departure_city)
    if arrival_city:
        flight_list = flight_list.filter(Flight.arrival_city == arrival_city)
    if start_time:
        if end_time:
            flight_list = flight_list.filter(and_(Flight.departure_time >= start_time, Flight.arrival_time <= end_time))
        else:
            flight_list = flight_list.filter(Flight.departure_time >= start_time)
    else:
        if end_time:
            flight_list = flight_list.filter(Flight.arrival_time <= end_time)

    return render_template("home/index.html", flight_list=flight_list)

