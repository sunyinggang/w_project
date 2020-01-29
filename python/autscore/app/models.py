from app import db
from sqlalchemy import Column, Integer, String, Date, DateTime,TIMESTAMP,DECIMAL
from werkzeug.security import check_password_hash

class Admin(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    def check_pwd(self, pwd):
        return check_password_hash(self.password, pwd)

class Teacher(db.Model):
    __tablename__ = "teacher"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    name = Column(String)

    def check_pwd(self, pwd):
        return check_password_hash(self.password, pwd)

class Student(db.Model):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    name = Column(String)
    class_id = Column(Integer,db.ForeignKey('class.id'),default=0)
    select = db.relationship('Select', backref='student')

    def check_pwd(self, pwd):
        return check_password_hash(self.password, pwd)

class Class(db.Model):
    __tablename__ = "class"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    student = db.relationship('Student', backref='class')

class Experiment(db.Model):
    __tablename__ = "experiment"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    model_url = Column(String)
    teacher_id = Column(Integer)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    select = db.relationship('Select',backref='experiment')

class Select(db.Model):
    id = Column(Integer, primary_key=True)
    experiment_id = Column(Integer,db.ForeignKey('experiment.id'))
    student_id = Column(Integer,db.ForeignKey('student.id'))
    word_url = Column(String)
    select_time = Column(DateTime)
    add_time = Column(DateTime)
    aut_score = Column(Integer,default=0)
    tea_score = Column(Integer,default=0)
    is_aut = Column(Integer,default=0)