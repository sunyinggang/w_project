#encoding = utf-8
from datetime import datetime
from app import db
from sqlalchemy import Column, Integer, String, Date, DateTime,TIMESTAMP,DECIMAL
from werkzeug.security import check_password_hash


class Airline(db.Model):
    name = Column(String, primary_key=True)
    def __repr__(self):
        return "<Airline %r>" % self.name

class Customer(db.Model):
    email = Column(String,primary_key=True)
    name = Column(String)
    password = Column(String)
    building_number = Column(String)
    street = Column(String)
    city = Column(String)
    state = Column(String)
    phone_number = Column(String)
    passport_number = Column(String)
    passport_expiration = Column(DateTime)
    passport_country = Column(String)
    date_of_birth = Column(Date)

    def check_pwd(self, pwd):
        return check_password_hash(self.password, pwd)

class Agent(db.Model):
    __tablename__ = "bookingagent"
    email = Column(String,primary_key=True)
    password = Column(String)
    booking_agent_id = Column(String)

    def check_pwd(self, pwd):
        return check_password_hash(self.password, pwd)

class Staff(db.Model):
    __tablename__ = "airlinestaff"
    username = Column(String, primary_key=True)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(String)
    airline_name = Column(String)


    def check_pwd(self, pwd):
        return check_password_hash(self.password, pwd)

class Airport(db.Model):
    name = Column(String, primary_key=True)
    city = Column(String)

class Airplane(db.Model):
    id = Column(String, primary_key=True)
    seats = Column(Integer)
    airline_name = Column(String)

class Flight(db.Model):
    flight_num = Column(String, primary_key=True)
    departure_time = Column(DateTime)
    arrival_time = Column(DateTime)
    price = Column(DECIMAL)
    status = Column(String)
    rest_seat = Column(Integer)
    airline_name = Column(String)
    departure_airport_name = Column(String)
    arrival_airport_name = Column(String)
    departure_city = Column(String)
    arrival_city = Column(String)
    airplane_id = Column(String)


class Ticket(db.Model):
    ticket_id = Column(String, primary_key=True)
    user_email = Column(String)
    airline_name = Column(String)
    flight_num = Column(String)
    price = Column(DECIMAL)
    booking_agent_ID = Column(String)
    puechases_time = Column(TIMESTAMP)