#encoding = utf-8
from flask import Blueprint

agent = Blueprint("agent",__name__)

import app.agent.views

