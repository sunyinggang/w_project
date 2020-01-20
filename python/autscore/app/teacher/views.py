from flask import render_template, session, flash, redirect, url_for

from . import teacher
from .forms import ExperimentForm
from .. import db
from ..models import Experiment


@teacher.route("/")
def index():
    return render_template("teacher/teacher.html")

@teacher.route("/class/")
def tclass():
    return render_template("teacher/tclass.html")

@teacher.route("/experiment/<int:page>/")
def experiment(page=None):
    if page is None:
        page = 1
    experiment_list = Experiment.query.paginate(page=page,per_page=5)
    return render_template("teacher/texperiment.html",experiment_list = experiment_list)

@teacher.route("/create/flight/",methods=["POST","GET"])
def addExperiment():
    form = ExperimentForm()
    teacher_id = session["id"]
    if form.validate_on_submit():
        data = form.data
        experiment = Experiment.query.filter_by(name=data["name"]).count()
        if experiment == 1:
            flash("实验名称已存在!")
            return redirect(url_for("admin.classAdd"))
        experiment = Experiment(
            name=data["name"],
            teacher_id = teacher_id,
            start_time = data["start_time"],
            end_time = data["end_time"]
        )
        db.session.add(experiment)
        db.session.commit()
        flash("添加成功！")
        return redirect(url_for("teacher.experiment", page=1))
    return render_template("teacher/addExperiment.html",form=form)

@teacher.route("/score/")
def score():
    return render_template("teacher/tscore.html")

@teacher.route("/student/")
def student():
    return render_template("teacher/tstudent.html")
