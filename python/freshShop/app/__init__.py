#encoding = utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
import os
from flask_ckeditor import CKEditor

app = Flask(__name__)
ckeditor = CKEditor(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost/wfresh"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = '8906ced739ec4d3a80c0bcecfb15fb8c'
app.config['CKEDITOR_FILE_UPLOADER'] = 'admin.upload'
app.config['UPLOADED_PATH'] = os.path.join(os.path.abspath(os.path.dirname(__file__)),"static/uploads/")
app.config["UP_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)),"static/uploads/")
app.debug = True
db = SQLAlchemy(app)

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint


app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint,url_prefix="/admin")