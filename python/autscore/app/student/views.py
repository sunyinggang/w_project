import datetime
import os
import time

from flask import render_template, session, flash, redirect, url_for, make_response, send_file, request
from werkzeug.security import generate_password_hash

from . import student
from .. import db
from ..home.forms import ChangeForm
from ..models import Experiment, Select, Teacher, Student


@student.route("/index/")
def index():
    return render_template("student/student.html")

@student.route("/change/",methods=["GET","POST"])
def change():
    form = ChangeForm()
    if form.validate_on_submit():
        data = form.data
        if data["password"] != data["passwordt"]:
            flash("两次密码不一致！")
            return redirect(url_for("student.change"))
        student = Student.query.filter_by(username=session["username"]).first()
        student.password = generate_password_hash(data["password"])
        db.session.add(student)
        db.session.commit()
        flash("密码修改成功，重新登录！")
        return redirect(url_for("home.logout"))
    return render_template("student/change.html", form=form)

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

@student.route("/word/add/<id>/",methods=["POST","GET"])
def addWord(id=None):
    UPLOAD_FOLDER = 'app/static/upload/'
    file_dir = os.path.join(os.getcwd(), UPLOAD_FOLDER)
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['file']  # 从表单的file字段获取文件，myfile为该表单的name值
    fname = f.filename
    ext = fname.rsplit('.', 1)[1]  # 获取文件后缀
    unix_time = int(time.time())
    new_filename = str(unix_time) + '.' + ext  # 修改了上传的文件名
    f.save(os.path.join(file_dir, new_filename))  # 保存文件到upload目录
    select = Select.query.filter_by(id=id).first_or_404()
    select.word_url = new_filename
    db.session.add(select)
    db.session.commit()
    flash("上传成功！")
    return redirect(url_for("student.score", page=1))

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





