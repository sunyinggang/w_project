from datetime import datetime

from app import db
from sqlalchemy import Column, Integer, String, Date, DateTime,TIMESTAMP,DECIMAL,Text
from werkzeug.security import check_password_hash, generate_password_hash


class Admin(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    password = Column(String)
    role = Column(Integer)

    def check_pwd(self, pwd):
        return check_password_hash(self.password, pwd)

class Driver(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    password = Column(String,default=generate_password_hash("123456"))
    address = Column(String)
    idcardz = Column(String)
    idcardf = Column(String)
    drivercardz = Column(String)
    drivercardf = Column(String)
    content = Column(Text)
    status = Column(Integer, default=0)

class Car(db.Model):
    id = Column(Integer, primary_key=True)
    tid = Column(Integer)
    number = Column(String)
    nickname = Column(String)
    capacity = Column(String)
    model = Column(String)
    img_url = Column(String)
    driver_id = Column(Integer)
    content = Column(String)
    status = Column(Integer, default=0)

class Expense(db.Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    user_type = Column(Integer)
    expense_type = Column(Integer)
    content = Column(String)
    money = Column(Integer)
    status = Column(Integer, default=0)
    add_time = Column(db.DateTime, default=datetime.now)
    note = Column(Text)
    img_url = Column(String)

class ExpenseType(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    content = Column(Text)

class Notice(db.Model):
    id = Column(Integer, primary_key=True)
    content = Column(String)
    add_time = Column(db.DateTime, default=datetime.now)
