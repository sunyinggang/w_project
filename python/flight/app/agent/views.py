#encoding = utf-8

from . import agent
from flask import render_template,session,request
from app.models import Flight,Ticket,Agent
from app import db
from sqlalchemy import and_
import datetime
from app.home.views import user_login_req
from decimal import Decimal

@agent.route("/")
@user_login_req
def index():
    agent = Agent.query.filter(Agent.email == session["username"]).first()
    q = db.session.query(Ticket.flight_num).filter(Ticket.booking_agent_ID == agent.booking_agent_id)
    flight_list = db.session.query(Flight).filter(Flight.flight_num.in_(q))
    return render_template("agent/index.html", flight_list=flight_list)

@agent.route("/info/")
@user_login_req
def info():
    agent = Agent.query.filter(Agent.email == session["username"]).first()
    return render_template("agent/personal-info.html",agent=agent)

@agent.route("/base/")
@user_login_req
def combase():
    agent = Agent.query.filter(Agent.email == session["username"]).first()
    ticket_list = Ticket.query.filter(Ticket.booking_agent_ID == agent.booking_agent_id).filter(Ticket.puechases_time>=get_day_nday_ago(30))
    sum=n=0
    for v in ticket_list:
        sum+= (v.price * Decimal(0.1))
        n+=1
    sum = round(sum, 2)
    return render_template("agent/commission-base.html",sum=sum,n=n)

def get_day_nday_ago(n):
    now_time = datetime.datetime.now()
    change_time = now_time + datetime.timedelta(days=-n)
    return change_time .strftime('%Y-%m-%d')


@agent.route("/comsearch/")
@user_login_req
def comsearch():
    start_time = request.args.get("start_time")
    end_time = request.args.get("end_time")
    agent = Agent.query.filter(Agent.email == session["username"]).first()
    ticket_list = Ticket.query.filter(Ticket.booking_agent_ID == agent.booking_agent_id)
    if start_time:
        if end_time:
            ticket_list = ticket_list.filter(and_(Ticket.puechases_time >= start_time, Ticket.puechases_time <= end_time))
        else:
            ticket_list = ticket_list.filter(Ticket.puechases_time >= start_time)
    else:
        if end_time:
            ticket_list = ticket_list.filter(Ticket.puechases_time <= end_time)
    sum = n = 0
    for v in ticket_list:
        sum += (v.price * Decimal(0.1))
        n += 1
    sum = round(sum,2)
    return render_template("agent/commission-search.html",sum=sum,n=n)


@agent.route("/search/")
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

    return render_template("agent/index.html", flight_list=flight_list)

