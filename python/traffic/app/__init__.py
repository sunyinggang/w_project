import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@127.0.0.1/traffic"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = '8906ced739ec4d3a80c0bcecfb15fb8c'
app.config['UPLOADED_PATH'] = os.path.join(os.path.abspath(os.path.dirname(__file__)),"static/uploads/")
app.debug = True

db = SQLAlchemy(app)

from app.user import user as user_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(user_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("admin/404.html"),404



