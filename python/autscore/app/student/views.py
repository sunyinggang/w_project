import datetime
import os

from flask import render_template, session, flash, redirect, url_for, make_response, send_file, request

from . import student
from .. import db
from ..models import Experiment, Select, Teacher


@student.route("/index/")
def index():
    return render_template("student/student.html")

@student.route("/select/<int:page>/")
def select(page=None):
    if page is None:
        page = 1
    experiment_list = Experiment.query.paginate(page=page,per_page=5)
    return render_template("student/sselect.html",experiment_list = experiment_list)

@student.route("/select/search/<int:page>/")
def selectrSearch(page=None):
    if page is None:
        page = 1
    name = request.args.get("name")
    experiment_list = Experiment.query
    if name:
        experiment_list = experiment_list.filter(
            Experiment.name.ilike('%' + name + '%')
        ).paginate(page=page,per_page=5)
    return render_template("student/sselectSearch.html",experiment_list = experiment_list)

@student.route("/select/experiment/<id>/",methods=["GET","POST"])
def selectExp(id=None):
    select = Select(
        experiment_id = id,
        student_id = session["id"],
        select_time= datetime.datetime.now()
    )
    db.session.add(select)
    db.session.commit()
    flash("选择成功！")
    return redirect(url_for('student.score',page=1))

@student.route("/score/<int:page>/")
def score(page=None):
    if page is None:
        page = 1
    select_list = Select.query.join(
        Experiment
    ).filter(
        Experiment.id == Select.experiment_id
    ).filter(
        Select.student_id == session["id"]
    ).paginate(page=page,per_page=5)
    return render_template("student/sscore.html",select_list = select_list)

@student.route("/score/del/<id>/",methods=["GET","POST"])
def scoreDel(id=None):
    score = Select.query.filter_by(id=id).first_or_404()
    db.session.delete(score)
    db.session.commit()
    flash("删除成功！")
    return redirect(url_for('student.score',page=1))

@student.route("/download/<id>/", methods=['GET'])
def download(id=None):
    experiment = Experiment.query.filter_by(id=id).first_or_404()
    UPLOAD_FOLDER = 'app/static/upload/'+experiment.model_url
    file_dir = os.path.join(os.getcwd(), UPLOAD_FOLDER).replace('\\', '/')
    response = make_response(send_file(file_dir))
    return response





