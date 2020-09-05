#encoding = utf-8
from . import customer
from flask import render_template,session,request,flash,redirect,url_for
from app.models import Flight,Ticket,Customer
from app import db
from sqlalchemy import and_
from app.home.views import user_login_req
from app.customer.forms import InformationForm

@customer.route("/")
@user_login_req
def index():
    q = db.session.query(Ticket.flight_num).filter(Ticket.user_email == session["username"])
    flight_list = db.session.query(Flight).filter(Flight.flight_num.in_(q))
    return render_template("customer/customer.html",flight_list=flight_list)

@customer.route("/info/",methods=["POST","GET"])
@user_login_req
def info():
    form = InformationForm()
    customer = Customer.query.filter_by(email=session["username"]).first_or_404()
    if form.validate_on_submit():
        data = form.data
        customer.name = data["name"]
        customer.building_number = data["building_number"]
        customer.street = data["street"]
        customer.city = data["city"]
        customer.state = data["state"]
        customer.phone_number = data["phone_number"]
        customer.passport_number = data["passport_number"]
        customer.passport_expiration = data["passport_expiration"]
        customer.passport_country = data["passport_country"]
        customer.date_of_birth = data["date_of_birth"]
        db.session.add(customer)
        db.session.commit()
        flash("Modify success！")
        return redirect(url_for("customer.info"))
    return render_template("customer/personal-info.html",form=form,customer=customer)

@customer.route("/search/")
@user_login_req
def search():
    departure_city = request.args.get("departure_city")
    arrival_city = request.args.get("arrival_city")
    start_time = request.args.get("start_time")
    end_time = request.args.get("end_time")
    flight_list = Flight.query
    if departure_city:
        flight_list = flight_list.filter(Flight.departure_city==departure_city)
    if arrival_city:
        flight_list = flight_list.filter(Flight.arrival_city==arrival_city)
    if start_time:
        if end_time:
            flight_list = flight_list.filter(and_(Flight.departure_time >= start_time,Flight.arrival_time <= end_time))
        else:
            flight_list = flight_list.filter(Flight.departure_time >= start_time)
    else:
        if end_time:
            flight_list = flight_list.filter(Flight.arrival_time <= end_time)

    return render_template("customer/customer.html", flight_list=flight_list)

