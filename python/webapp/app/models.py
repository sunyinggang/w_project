#encoding = utf-8
from datetime import datetime
from app import db
from sqlalchemy import Column, Integer, String, ForeignKey,DECIMAL,Text
from werkzeug.security import check_password_hash

class Admin(db.Model):
    id = Column(Integer,primary_key=True)
    username = Column(String)
    password = Column(String)

    def check_pwd(self, pwd):
        return self.password == pwd

class User(db.Model):
    id = Column(Integer,primary_key=True)
    tel = Column(String)
    password = Column(String)

    def check_pwd(self, pwd):
        return check_password_hash(self.password,pwd)

class Commodity(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Integer)
    os = Column(String)
    number = Column(String)
    area = Column(String)
    server = Column(String)
    rank = Column(Integer)
    type = Column(String)
    pet = Column(Integer)
    sect = Column(String)
    sex = Column(String)
    bargain = Column(String)
    description = Column(String)
    content = Column(Text)
    see = Column(Integer, default=0)
    tel = Column(String, default='')
    wx = Column(String, default='')
    role = Column(Integer, default=1)
    user_id = Column(Integer)
    time = Column(db.DateTime, default=datetime.now)