import datetime
import os
import time

import docx
import jieba
from gensim import corpora,models,similarities

from flask import render_template, session, flash, redirect, url_for, make_response, send_file, request
from werkzeug.security import generate_password_hash

from . import student
from app.student.forms import ClassForm
from .. import db
from ..home.forms import ChangeForm
from ..models import Experiment, Select, Teacher, Student, Class


@student.route("/index/")
def index():
    return render_template("student/student.html")

@student.route("/change/",methods=["GET","POST"])
def change():
    student = Student.query.filter_by(id=session["id"]).first_or_404()
    if student.class_id == 0:
        flash("请先选择班级！")
        return redirect(url_for("student.selectClass"))
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
    student = Student.query.filter_by(id=session["id"]).first_or_404()
    if student.class_id == 0:
        flash("请先选择班级！")
        return redirect(url_for("student.selectClass"))
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
    select = Select.query.filter_by(student_id=session["id"]).all()
    for i in range(len(select)):
        if select[i].experiment_id == int(id):
            flash("已选择此实验！")
            return redirect(url_for('student.score', page=1))
    sel = Select(
        experiment_id = id,
        student_id = session["id"],
        select_time= datetime.datetime.now()
    )
    db.session.add(sel)
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
    experiment = Experiment.query.filter_by(id=select.experiment_id).first_or_404()
    aut_score = TfIdf(new_filename,experiment.keywords)
    select.word_url = new_filename
    select.aut_score = aut_score
    select.is_aut = 1
    db.session.add(select)
    db.session.commit()
    flash("上传成功，已完成自动评分！")
    return redirect(url_for("student.score", page=1))

@student.route("/score/del/")
def scoreDel():
    id = request.args.get("id")
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

@student.route("/info/")
def info():
    student =  Student.query.filter_by(id=session["id"]).first_or_404()
    if student.class_id == 0:
        flash("请先选择班级！")
        return redirect(url_for("student.selectClass"))
    else:
        student = Student.query.join(
            Class
        ).filter(
            Student.class_id == Class.id
        ).filter(
            Student.id == session["id"]
        ).first()
        return render_template("student/info.html",student = student)

@student.route("/selectClass/", methods=['POST', 'GET'])
def selectClass():
    form = ClassForm()
    if form.validate_on_submit():
        data = form.data
        student = Student.query.filter_by(id=session["id"]).first_or_404()
        student.class_id = data["class_name"]
        db.session.add(student)
        db.session.commit()
        flash("选择班级成功！")
        return redirect(url_for("student.info"))
    return render_template("student/selectClass.html",form = form)

def TfIdf(fileUrl,keywords):
    UPLOAD_FOLDER = 'static\\upload\\'
    baseUrl = os.path.abspath(os.path.dirname(__file__)).replace("student","")
    file_dir = os.path.join(baseUrl, UPLOAD_FOLDER)
    file_dir = file_dir + fileUrl
    # 读取word文档
    document = docx.Document(file_dir)
    # 读取实验中的表格内容
    tables = document.tables
    #读取第一个表格（默认就一个表格）
    tb = tables[0]
    #读取表格行数
    tb_rows = tb.rows
    result = ""
    for j in range(3, len(tb_rows)):
        result += tb.cell(j, 1).text

    all_doc = []
    all_doc.append(result)
    all_doc.append("")

    # 1、将实验内容all_doc_list与关键词doc_test_list制作为分词列表
    all_doc_list = []
    for doc in all_doc:
        doc_list = [word for word in jieba.cut(doc)]
        all_doc_list.append(doc_list)
    doc_test_list = [word for word in jieba.cut(keywords)]
    # 2、基于文件集建立【词典】，并提取词典特征数
    dictionary = corpora.Dictionary(all_doc_list)
    # 3、基于词典，将【分词列表集】转换为【稀疏向量集】，也就是【语料库】
    corpus = [dictionary.doc2bow(doc) for doc in all_doc_list]
    # 4、使用“TF-TDF模型”处理【语料库】
    tfidf = models.TfidfModel(corpus)
    # 5、同理，用词典把关键词也转换为稀疏向量
    doc_test_vec = dictionary.doc2bow(doc_test_list)
    # 6、对稀疏向量建立索引
    index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dictionary.keys()))
    # 7、相似的计算
    sim = index[tfidf[doc_test_vec]]
    t = sorted(enumerate(sim), key=lambda item: -item[1])
    score = int(t[0][1] * 100)
    return score



