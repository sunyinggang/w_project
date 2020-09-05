#encoding = utf-8
from datetime import datetime
from app import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class User(db.Model):
    id = Column(Integer,primary_key=True)
    username = Column(String)
    password = Column(String)
    usertype = Column(Integer)

    def check_pwd(self, pwd):
        return self.password == pwd


class Book(db.Model):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    user_id = Column(Integer, ForeignKey('user.id'))
    title = Column(String)
    date = Column(String)
    day = Column(Integer)