#encoding = utf-8
from . import staff
from flask import render_template,session,redirect,url_for,flash,request
from app.home.views import user_login_req
from app.staff.forms import AirportForm, AirplaneForm, FlightForm, FightStatusForm, InformationForm
from app.models import Airplane, Airport, Flight, Staff, Ticket,Agent
from app import db
from sqlalchemy import and_,func
import datetime
from calendar import monthrange
from decimal import Decimal

@staff.route("/")
@user_login_req
def index():
    flight_list = Flight.query.all()
    return render_template("staff/index.html",flight_list=flight_list)

@staff.route("/info/",methods=["POST","GET"])
@user_login_req
def info():
    form = InformationForm()
    staff = Staff.query.filter_by(username=session["username"]).first_or_404()
    if form.validate_on_submit():
        data = form.data
        staff.first_name = data["first_name"],
        staff.last_name = data["last_name"],
        staff.date_of_birth = data["date_of_birth"]
        db.session.add(staff)
        db.session.commit()
        flash("Modify success！")
        return redirect(url_for("staff.info"))
    return render_template("staff/personal-info.html",form=form,staff=staff)

@staff.route("/create/flight/",methods=["POST","GET"])
@user_login_req
def createFlight():
    form = FlightForm()
    staffname = session["username"]
    staff = Staff.query.filter_by(username=staffname).first()
    if form.validate_on_submit():
        data = form.data
        airplane = Airplane.query.filter_by(id=data["airplane_name"]).first()
        flight = Flight.query.filter_by(flight_num=data["flight_num"]).count()
        departure_airport = Airport.query.filter_by(name=data["departure_airport_name"]).first()
        arrival_airport = Airport.query.filter_by(name=data["arrival_airport_name"]).first()
        if flight == 1:
            flash("The flight number already exists!")
            return redirect(url_for("staff.createFlight"))
        if data["departure_airport_name"] == data["arrival_airport_name"]:
            flash("Dont't input the same location about departure_airport_name and arrival_airport_name")
            return redirect(url_for("staff.createFlight"))
        flight = Flight(
            flight_num=data["flight_num"],
            departure_time=data["departure_time"],
            arrival_time = data["arrival_time"],
            departure_airport_name = data["departure_airport_name"],
            arrival_airport_name = data["arrival_airport_name"],
            departure_city = departure_airport.city,
            arrival_city = arrival_airport.city,
            price = data["price"],
            status= "upcoming",
            rest_seat= airplane.seats,
            airline_name= staff.airline_name,
            airplane_id = data["airplane_name"]
        )
        db.session.add(flight)
        db.session.commit()
        flash("Add success！")
        return redirect(url_for("staff.createFlight"))
    return render_template("staff/createFlight.html",form=form,staff=staff)


@staff.route("/airplane/list/")
@user_login_req
def airplaneList():
    staff = Staff.query.filter(Staff.username == session["username"]).first_or_404()
    airplane_list = Airplane.query.filter(Airplane.airline_name == staff.airline_name)
    return render_template("staff/airplaneList.html",airplane_list=airplane_list)

@staff.route("/airport/list/")
@user_login_req
def airportList():
    airport_list = Airport.query.all()
    return render_template("staff/airportList.html",airport_list=airport_list)

@staff.route("/airplane/del/<id>/",methods=["GET","POST"])
@user_login_req
def delAirplane(id=None):
    airplane = Airplane.query.filter_by(id=id).first_or_404()
    db.session.delete(airplane)
    db.session.commit()
    flash("Delete Success!")
    return redirect(url_for('staff.airplaneList'))

@staff.route("/airport/del/<id>/",methods=["GET","POST"])
@user_login_req
def delAirport(id=None):
    airport = Airport.query.filter_by(name=id).first_or_404()
    db.session.delete(airport)
    db.session.commit()
    flash("Delete Success!")
    return redirect(url_for('staff.airportList'))




@staff.route("/add/airplane/",methods=["POST","GET"])
@user_login_req
def addAirplane():
    form = AirplaneForm()
    staffname = session["username"]
    staff = Staff.query.filter_by(username=staffname).first()
    if form.validate_on_submit():
        data = form.data
        airplane = Airplane.query.filter_by(id=data["id"]).count()
        if airplane == 1:
            flash("The airport name already exists!")
            return redirect(url_for("staff.addAirplane"))
        airplane = Airplane(
            id=data["id"],
            seats=data["seats"],
            airline_name= data["airline_name"]
        )
        db.session.add(airplane)
        db.session.commit()
        flash("Add success！")
        return redirect(url_for("staff.addAirplane"))
    return render_template("staff/addAircraft.html",form=form,staff=staff)

@staff.route("/add/airport/",methods=["GET","POST"])
@user_login_req
def addAirport():
    form = AirportForm()
    if form.validate_on_submit():
        data = form.data
        airport = Airport.query.filter_by(name=data["name"]).count()
        if airport == 1:
            flash("The airport name already exists!")
            return redirect(url_for("staff.addAirport"))
        airport = Airport(
            name=data["name"],
            city=data["city"]
        )
        db.session.add(airport)
        db.session.commit()
        flash("Add success！")
        return redirect(url_for("staff.addAirport"))
    return render_template("staff/addAirport.html",form=form)

@staff.route("/view/customers/")
@user_login_req
def viewCustomer():
    customer_list = db.session.query(Ticket.user_email,func.count(Ticket.user_email)).group_by(Ticket.user_email).order_by(func.count(Ticket.user_email).desc()).all()
    return render_template("staff/viewCustomers.html",customer_list=customer_list)

@staff.route("/total/sales/")
@user_login_req
def totalSales():
    start_time = request.args.get("start_time")
    end_time = request.args.get("end_time")
    staff = Staff.query.filter(Staff.username == session["username"]).first()
    time = datetime.datetime.now()
    first_day = datetime.date(time.year, time.month, 1)
    pre_month = first_day - datetime.timedelta(days=1)
    first_day_of_pre_month = datetime.date(pre_month.year, pre_month.month, 1)
    last_year = int(time.year) - 1
    last_year_first = datetime.date(last_year,1,1)
    last_year_last = datetime.date(last_year,12,31)
    ticket_last_month = Ticket.query.filter(Ticket.airline_name == staff.airline_name).filter(and_(Ticket.puechases_time>=first_day_of_pre_month,Ticket.puechases_time<=pre_month))
    ticket_last_year = Ticket.query.filter(Ticket.airline_name == staff.airline_name).filter(and_(Ticket.puechases_time>=last_year_first,Ticket.puechases_time<=last_year_last))
    month_sum = year_sum = sum = 0
    for m in ticket_last_month:
        month_sum += m.price
    for y in ticket_last_year:
        year_sum += y.price
    ticket_list = Ticket.query.filter(Ticket.airline_name == staff.airline_name)
    if start_time:
        if end_time:
            ticket_list = Ticket.query.filter(and_(Ticket.puechases_time >= start_time,Ticket.puechases_time <= end_time))
        else:
            ticket_list = Ticket.query.filter(Ticket.puechases_time >= start_time)
    else:
        if end_time:
            ticket_list = Ticket.query.filter(Ticket.puechases_time <= end_time)
    for v in ticket_list:
        sum += v.price
    return render_template("staff/reportSalesrank.html",month_sum=month_sum,year_sum=year_sum,sum=sum)

@staff.route("/month/sales/")
@user_login_req
def monthSales():
    staff = Staff.query.filter(Staff.username == session["username"]).first()
    time = datetime.datetime.now()
    year = int(time.year)
    ticket_list = []
    for v in range(1,13):
        sum = 0
        left = datetime.date(year,v,1)
        right = monthlastday(year,v)
        ticket = db.session.query(Ticket).filter(Ticket.puechases_time.between(left,right)).filter(Ticket.airline_name == staff.airline_name).all()
        for k in ticket:
            sum += int(k.price)
        ticket_list.append(sum)
    return render_template("staff/reportMonthsales.html",ticket_list=ticket_list)

def monthlastday(y,m):
    d = monthrange(y,m)[1]
    return datetime.date(y, m, d)
@staff.route("/sales/rank/")
@user_login_req
def salesRank():
    staff = Staff.query.filter(Staff.username == session["username"]).first()
    time = datetime.datetime.now()
    first_day = datetime.date(time.year, time.month, 1)
    pre_month = first_day - datetime.timedelta(days=1)
    first_day_of_pre_month = datetime.date(pre_month.year, pre_month.month, 1)
    last_year = int(time.year) - 1
    last_year_first = datetime.date(last_year,1,1)
    last_year_last = datetime.date(last_year,12,31)
    ticket_last_month = db.session.query(Ticket.booking_agent_ID, func.count(Ticket.booking_agent_ID)).group_by(Ticket.booking_agent_ID).filter(Ticket.airline_name == staff.airline_name).filter(Ticket.puechases_time.between(first_day_of_pre_month, pre_month)).order_by(func.count(Ticket.booking_agent_ID).desc()).limit(5)
    ticket_last_year = db.session.query(Ticket.booking_agent_ID, func.count(Ticket.booking_agent_ID)).group_by(Ticket.booking_agent_ID).filter(Ticket.airline_name == staff.airline_name).filter(Ticket.puechases_time.between(last_year_first,last_year_last)).order_by(func.count(Ticket.booking_agent_ID).desc()).limit(5)
    agent_email_month = {}
    agent_email_year = {}
    for m in ticket_last_month:
        agent = Agent.query.filter(Agent.booking_agent_id == m.booking_agent_ID).first()
        agent_email_month[agent.booking_agent_id] = agent.email
    for y in ticket_last_year:
        agent = Agent.query.filter(Agent.booking_agent_id == y.booking_agent_ID).first()
        agent_email_year[agent.booking_agent_id] = agent.email
    return render_template("staff/agentSalesrank.html",ticket_last_month=ticket_last_month,ticket_last_year=ticket_last_year,agent_email_year=agent_email_year,agent_email_month=agent_email_month)

@staff.route("/com/rank/")
@user_login_req
def comRank():
    staff = Staff.query.filter(Staff.username == session["username"]).first()
    time = datetime.datetime.now()
    last_year = int(time.year)
    left = datetime.date(last_year,1,1)
    right = datetime.date(last_year,12,31)
    agent_list = db.session.query(Ticket.booking_agent_ID, func.sum(Ticket.price* Decimal(0.1))).group_by(Ticket.booking_agent_ID).filter(Ticket.puechases_time.between(left,right)).filter(Ticket.airline_name == staff.airline_name).order_by(func.sum(Ticket.price).desc()).limit(5)
    agent_email = {}
    for v in agent_list:
        agent = Agent.query.filter(Agent.booking_agent_id == v.booking_agent_ID).first()
        agent_email[v.booking_agent_ID] = agent.email
    return render_template("staff/agentComrank.html",agent_list=agent_list,agent_email=agent_email)

@staff.route("/flight/status/<id>/",methods=["GET","POST"])
@user_login_req
def flyStauts(id=None):
    form = FightStatusForm()
    flight = Flight.query.filter_by(flight_num=id).first_or_404()
    if form.validate_on_submit():
        data = form.data
        flight.status = data["status"]
        db.session.add(flight)
        db.session.commit()
        flash("修改成功")
        return redirect(url_for('staff.index'))
    return render_template("staff/flightStatus.html",form=form,flight=flight)

@staff.route("/cus/detail/<id>/",methods=["GET","POST"])
@user_login_req
def cusdetail(id=None):
    q = db.session.query(Ticket.flight_num).filter(Ticket.user_email == '1234@qq.com')
    flight_list = db.session.query(Flight).filter(Flight.flight_num.in_(q))
    return render_template("staff/customerTicket.html",flight_list=flight_list,email=id)


@staff.route("/search/")
@user_login_req
def search():
    departure_airport = request.args.get("departure_airport")
    arrival_airport = request.args.get("arrival_airport")
    departure_city = request.args.get("departure_city")
    arrival_city = request.args.get("arrival_city")
    start_time = request.args.get("start_time")
    end_time = request.args.get("end_time")
    flight_list = Flight.query
    if departure_airport:
        flight_list = flight_list.filter(Flight.departure_airport_name==departure_airport)
    if arrival_airport:
        flight_list = flight_list.filter(Flight.arrival_airport_name==arrival_airport)
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

    return render_template("staff/index.html", flight_list=flight_list)

