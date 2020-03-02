from app import db
from sqlalchemy import Column, Integer, String, Date, DateTime,TIMESTAMP,DECIMAL,Text
from werkzeug.security import check_password_hash

class Admin(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    password = Column(String)
    role = Column(Integer)

    def check_pwd(self, pwd):
        return check_password_hash(self.password, pwd)

