#encoding = utf-8
from datetime import datetime
from app import db
from sqlalchemy import Column, Integer, String, ForeignKey,Text
from sqlalchemy.orm import relationship


class Admin(db.Model):
    id = Column(Integer,primary_key=True)
    username = Column(String)
    password = Column(String)

    def check_pwd(self, pwd):
        return self.password == pwd

class Category(db.Model):
    id = Column(Integer,primary_key=True)
    name = Column(String)

class Product(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    img = Column(String)
    category = relationship('Category')
    category_id = Column(Integer, ForeignKey('category.id'))
    content = Column(Text)
    create_time = Column(db.DateTime, default=datetime.now)

class People(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    img = Column(String)
    content = Column(Text)
    create_time = Column(db.DateTime, default=datetime.now)

class Natural(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    img = Column(String)
    content = Column(Text)
    create_time = Column(db.DateTime, default=datetime.now)

class History(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    img = Column(String)
    content = Column(Text)
    create_time = Column(db.DateTime, default=datetime.now)