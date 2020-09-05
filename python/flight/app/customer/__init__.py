#encoding = utf-8
from flask import Blueprint

customer = Blueprint("customer",__name__)

import app.customer.views


