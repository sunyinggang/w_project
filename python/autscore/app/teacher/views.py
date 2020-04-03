import os
import time

from flask import render_template, session, flash, redirect, url_for, request
from sqlalchemy import func
from werkzeug.security import generate_password_hash

from . import teacher
from .forms import ExperimentForm, ClassFindForm, ScoreForm, KeyWordsForm
from .. import db
from ..home.forms import ChangeForm
from ..models import Experiment, Teacher, Select, Student, Class


@teacher.route("/")
def index():
    return render_template("teacher/teacher.html")

@teacher.route("/change/",methods=["GET","POST"])
def change():
    form = ChangeForm()
    if form.validate_on_submit():
        data = form.data
        if data["password"] != data["passwordt"]:
            flash("两次密码不一致！")
            return redirect(url_for("teacher.change"))
        teacher = Teacher.query.filter_by(username=session["username"]).first()
        teacher.password = generate_password_hash(data["password"])
        db.session.add(teacher)
        db.session.commit()
        flash("密码修改成功，重新登录！")
        return redirect(url_for("home.logout"))
    return render_template("teacher/change.html", form=form)

@teacher.route("/experiment/<int:page>/")
def experiment(page=None):
    if page is None:
        page = 1
    experiment_list = Experiment.query.filter_by(teacher_id=session["id"]).paginate(page=page,per_page=5)
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
            return redirect(url_for("teacher.experiment",page=1))
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
            keywords=data["keywords"],
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

@teacher.route("/experiment/edit/keywords/<id>/",methods=["POST","GET"])
def editKeyWords(id=None):
    experiment = Experiment.query.filter_by(id=id).first_or_404()
    form = KeyWordsForm(keywords=experiment.keywords)
    if form.validate_on_submit():
        data = form.data
        experiment.keywords = data["keywords"]
        db.session.add(experiment)
        db.session.commit()
        flash("修改成功！")
        return redirect(url_for("teacher.experiment", page=1))
    return render_template("teacher/keywords.html",form=form,experiment=experiment)

@teacher.route("/experiment/del/")
def delExperiment():
    id = request.args.get("id")
    experiment = Experiment.query.filter_by(id=id).first_or_404()
    db.session.delete(experiment)
    db.session.commit()
    flash("删除成功！")
    return redirect(url_for('teacher.experiment', page=1))

@teacher.route("/score/<int:page>/")
def score(page=None):
    if page is None:
        page = 1
    experiment_list = Experiment.query.filter_by(teacher_id=session["id"]).paginate(page=page,per_page=5)
    select_all = db.session.query(Select.experiment_id,func.count(Select.student_id)).group_by(Select.experiment_id).all()
    select_submit = db.session.query(Select.experiment_id, func.count(Select.student_id)).group_by(Select.experiment_id).filter(Select.is_aut==1).all()
    print(select_all)
    print(select_submit)
    return render_template("teacher/tscore.html",experiment_list = experiment_list,select_all=select_all,select_submit=select_submit)

@teacher.route("/student/<int:page>/",methods=["POST","GET"])
def student(page=None):
    form = ClassFindForm()
    if form.validate_on_submit():
        data = form.data
        id = data["id"]
        experiment = Experiment.query.filter_by(id=id).first_or_404()
        select_list = Select.query.join(
            Experiment, Student, Class
        ).filter(
            Select.is_aut != 0
        ).filter(
            Experiment.id == id
        ).filter(
            Select.student_id == Student.id
        ).filter(
            Class.id == Student.class_id
        ).filter(
            Student.class_id == data["class_name"]
        ).filter(
            Experiment.id == Select.experiment_id
        ).paginate(page=page, per_page=5)
        return render_template("teacher/tstudent.html", form=form, experiment=experiment, select_list=select_list,
                               id=id)
    if page is None:
        page = 1
    id = request.args.get('id')
    experiment = Experiment.query.filter_by(id=id).first_or_404()
    select_list = Select.query.join(
        Experiment,Student,Class
    ).filter(
        Select.is_aut != 0
    ).filter(
        Experiment.id==id
    ).filter(
        Select.student_id == Student.id
    ).filter(
        Class.id == Student.class_id
    ).filter(
        Experiment.id == Select.experiment_id
    ).paginate(page=page,per_page=5)
    return render_template("teacher/tstudent.html",form=form,experiment = experiment,select_list = select_list,id=id)

@teacher.route("/addScore/<id>/",methods=["POST","GET"])
def addScore(id=None):
    form = ScoreForm()
    select = Select.query.filter_by(id=id).first_or_404()
    student = Student.query.filter_by(id=select.student_id).first_or_404()
    if form.validate_on_submit():
        data = form.data
        select = Select.query.filter_by(id=id).first_or_404()
        select.tea_score = data["score"]
        db.session.add(select)
        db.session.commit()
        flash("评分成功！")
        return redirect(url_for('teacher.addScore',id=id))
    return render_template("teacher/addScore.html",form=form,student=student,select=select)
