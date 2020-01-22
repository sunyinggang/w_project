import os
import time

from flask import render_template, session, flash, redirect, url_for, request

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
    UPLOAD_FOLDER = 'app/static/upload/'
    file_dir = os.path.join(os.getcwd(), UPLOAD_FOLDER).replace('\\','/')
    return render_template("teacher/texperiment.html",experiment_list = experiment_list,file_dir = file_dir)

@teacher.route("/experiment/add/",methods=["POST","GET"])
def addExperiment():
    form = ExperimentForm()
    teacher_id = session["id"]
    if form.validate_on_submit():
        data = form.data
        experiment = Experiment.query.filter_by(name=data["name"]).count()
        if experiment == 1:
            flash("实验名称已存在!")
            return redirect(url_for("admin.classAdd"))
        UPLOAD_FOLDER = 'app/static/upload/'
        file_dir = os.path.join(os.getcwd(), UPLOAD_FOLDER)
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        f = request.files['model_url']  # 从表单的file字段获取文件，myfile为该表单的name值
        fname = f.filename
        ext = fname.rsplit('.', 1)[1]  # 获取文件后缀
        unix_time = int(time.time())
        new_filename = str(unix_time) + '.' + ext  # 修改了上传的文件名
        f.save(os.path.join(file_dir, new_filename))  # 保存文件到upload目录
        experiment = Experiment(
            name=data["name"],
            teacher_id = teacher_id,
            start_time = data["start_time"],
            end_time = data["end_time"],
            model_url= new_filename
        )
        db.session.add(experiment)
        db.session.commit()
        flash("添加成功！")
        return redirect(url_for("teacher.experiment", page=1))
    return render_template("teacher/addExperiment.html",form=form)

@teacher.route("/experiment/del/<id>/",methods=["POST","GET"])
def delExperiment(id=None):
    experiment = Experiment.query.filter_by(id=id).first_or_404()
    db.session.delete(experiment)
    db.session.commit()
    flash("删除成功！")
    return redirect(url_for('teacher.experiment', page=1))

@teacher.route("/score/")
def score():
    return render_template("teacher/tscore.html")

@teacher.route("/student/")
def student():
    return render_template("teacher/tstudent.html")
