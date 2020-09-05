#encoding = utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import pymysql

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost/wplane"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = '8906ced739ec4d3a80c0bcecfb15fb8c'
app.debug = True

db = SQLAlchemy(app)

from app.home import home as home_blueprint
from app.customer import customer as customer_blueprint
from app.agent import agent as agent_blueprint
from app.staff import staff as staff_blueprint


app.register_blueprint(home_blueprint)
app.register_blueprint(customer_blueprint, url_prefix="/customer")
app.register_blueprint(agent_blueprint, url_prefix="/agent")
app.register_blueprint(staff_blueprint, url_prefix="/staff")
