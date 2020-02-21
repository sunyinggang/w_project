#encoding = utf-8
from datetime import datetime
from app import db
from sqlalchemy import Column, Integer, String, ForeignKey,DECIMAL,Text
from sqlalchemy.orm import relationship


class Admin(db.Model):
    id = Column(Integer,primary_key=True)
    username = Column(String)
    password = Column(String)

    def check_pwd(self, pwd):
        return self.password == pwd

class User(db.Model):
    id = Column(Integer,primary_key=True)
    nickname = Column(String)
    email = Column(String)
    password = Column(String)
    # address = relationship('Address')
    # address_id = Column(Integer, ForeignKey('address.id'),default=0)

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
    price = Column(Integer)
    content = Column(Text)
    create_time = Column(db.DateTime, default=datetime.now)

class Cart(db.Model):
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer)
    product = relationship('Product')
    product_id = Column(Integer,ForeignKey('product.id'))
    count = Column(Integer)

class Address(db.Model):
    id = Column(Integer,primary_key=True)
    user = relationship('User')
    user_id = Column(Integer,ForeignKey('user.id'))
    name = Column(String)
    phone = Column(String)
    address = Column(Text)
    status = Column(Integer,default=0)

class Order(db.Model):
    id = Column(Integer,primary_key=True)
    order_no = Column(String)
    user_id = Column(Integer)
    status = Column(Integer,default=1)
    total_price = Column(DECIMAL)
    total_count = Column(Integer)
    snap_address = Column(String)
    review_status = Column(Integer, default=0)
    create_time = Column(db.DateTime, default=datetime.now)

class OrderProduct(db.Model):
    id = Column(Integer,primary_key=True)
    order_id = Column(Integer)
    product_id = Column(Integer)
    name = Column(String)
    img = Column(String)
    price = Column(DECIMAL)
    count = Column(Integer)

class Announcement(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(Text)
    create_time = Column(db.DateTime, default=datetime.now)

class Help(db.Model):
    id = Column(Integer, primary_key=True)
    info = Column(Text)
    problem = Column(Text)
    distribution = Column(Text)

class Review(db.Model):
    id = Column(Integer,primary_key=True)
    user = relationship('User')
    user_id = Column(Integer,ForeignKey('user.id'))
    order_id = Column(Integer)
    product_id = Column(Integer)
    content = Column(Text)
    img = Column(String)
    create_time = Column(db.DateTime, default=datetime.now)
