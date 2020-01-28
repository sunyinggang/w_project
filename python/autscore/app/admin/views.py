import os

import xlrd
from flask import render_template, send_from_directory, make_response, send_file, request, flash, redirect, url_for, \
    session
from werkzeug.security import generate_password_hash
from app import db

from . import admin
from .forms import ClassForm
from ..home.forms import ChangeForm
from ..models import Teacher, Student, Class, Admin


@admin.route("/")
def index():
    return render_template("admin/admin.html")

@admin.route("/change/",methods=["GET","POST"])
def change():
    form = ChangeForm()
    if form.validate_on_submit():
        data = form.data
        if data["password"] != data["passwordt"]:
            flash("两次密码不一致！")
            return redirect(url_for("admin.change"))
        admin = Admin.query.filter_by(username=session["username"]).first()
        admin.password = generate_password_hash(data["password"])
        db.session.add(admin)
        db.session.commit()
        flash("密码修改成功，重新登录！")
        return redirect(url_for("home.logout"))
    return render_template("admin/change.html", form=form)

@admin.route("/aclass/<int:page>/",methods=["GET"])
def aclass(page=None):
    if page is None:
        page = 1
    class_list = Class.query.paginate(page=page,per_page=5)
    return render_template("admin/aclass.html",class_list = class_list)

@admin.route("/aclass/add", methods=['POST', 'GET'])
def classAdd():
    form = ClassForm()
    if form.validate_on_submit():
        data = form.data
        aclass = Class.query.filter_by(name=data["name"]).count()
        if aclass == 1:
            flash("班级名已存在!")
            return redirect(url_for("admin.classAdd"))
        aclass = Class(
            name=data["name"]
        )
        db.session.add(aclass)
        db.session.commit()
        flash("添加成功！")
        return redirect(url_for("admin.aclass",page=1))
    return render_template("admin/addclass.html",form=form)

@admin.route("/aclass/del/<id>/",methods=["GET","POST"])
def classDel(id=None):
    aclass = Class.query.filter_by(id=id).first_or_404()
    db.session.delete(aclass)
    db.session.commit()
    flash("删除成功！")
    return redirect(url_for('admin.aclass',page=1))

@admin.route("/ainput/")
def ainput():
    return render_template("admin/ainput.html")

@admin.route("/download/", methods=['GET'])
def download():
    UPLOAD_FOLDER = 'app/admin/'
    ROOT_FOLDER = os.path.join(os.getcwd(), UPLOAD_FOLDER)  # 整合绝对路径
    response = make_response(send_file(ROOT_FOLDER + "模板文件.xls"))
    return response


@admin.route("/fileo/", methods=['POST', 'GET'])
def fileOne():
    file = request.files['fileo']
    f = file.read()    #文件内容
    data = xlrd.open_workbook(file_contents=f)
    table = data.sheets()[0]
    nrows = table.nrows  # 获取该sheet中的有效行数
    ncols = table.ncols  # 获取该sheet中的有效列数
    list = []
    for i in range(nrows):
        rowlist = []
        for j in range(ncols):
            rowlist.append(table.cell_value(i, j))
        list.append(rowlist)
    del list[0]  # 删掉第一行，第一行获取的是文件的头，一般不用插到数据库里面

    for a in list:
        teachers = Teacher()
        teachers.username = a[0]
        teachers.name = a[1]
        teachers.password = generate_password_hash("123456")
        db.session.add(teachers)
        db.session.commit()
    flash("导入成功！")
    return redirect(url_for('admin.ateacher',page = 1))

@admin.route("/filet/", methods=['POST', 'GET'])
def fileTow():
    file = request.files['filet']
    f = file.read()    #文件内容
    data = xlrd.open_workbook(file_contents=f)
    table = data.sheets()[0]
    nrows = table.nrows  # 获取该sheet中的有效行数
    ncols = table.ncols  # 获取该sheet中的有效列数
    list = []
    for i in range(nrows):
        rowlist = []
        for j in range(ncols):
            rowlist.append(table.cell_value(i, j))
        list.append(rowlist)
    del list[0]  # 删掉第一行，第一行获取的是文件的头，一般不用插到数据库里面

    for a in list:
        students = Student()
        students.username = a[0]
        students.name = a[1]
        students.class_name = a[2]
        students.password = generate_password_hash("123456")
        db.session.add(students)
        db.session.commit()
    flash("导入成功！")
    return redirect(url_for('admin.astudent',page = 1))

@admin.route("/astudent/<int:page>/",methods=["GET"])
def astudent(page=None):
    if page is None:
        page = 1
    student_list = Student.query.paginate(page=page,per_page=5)
    return render_template("admin/astudent.html",student_list=student_list)

@admin.route("/astudent/del/<id>/",methods=["GET","POST"])
def studentDel(id=None):
    student = Student.query.filter_by(id=id).first_or_404()
    db.session.delete(student)
    db.session.commit()
    flash("删除成功！")
    return redirect(url_for('admin.astudent'))

@admin.route("/astudent/search/<int:page>/")
def studentSearch(page=None):
    if page is None:
        page = 1
    username = request.args.get("username")
    student_list = Student.query
    if username:
        student_list = student_list.filter(Student.username==username).paginate(page=page,per_page=5)
    return render_template("admin/astudent.html",student_list = student_list)

@admin.route("/astudent/edit/<id>/",methods=["GET","POST"])
def studentEdit(id=None):
    student = Student.query.filter_by(id=id).first_or_404()
    student.password = generate_password_hash("123456")
    db.session.add(student)
    db.session.commit()
    flash("修改成功")
    return redirect(url_for("admin.astudent"))


@admin.route("/ateacher/<int:page>/",methods=["GET"])
def ateacher(page=None):
    if page is None:
        page = 1
    teacher_list = Teacher.query.paginate(page=page,per_page=5)
    return render_template("admin/ateacher.html",teacher_list = teacher_list)

@admin.route("/ateacher/del/<id>/",methods=["GET","POST"])
def ateacherDel(id=None):
    teacher = Teacher.query.filter_by(id=id).first_or_404()
    db.session.delete(teacher)
    db.session.commit()
    flash("删除成功！")
    return redirect(url_for('admin.ateacher'))

@admin.route("/ateacher/search/")
def teacherSearch():
    username = request.args.get("username")
    teacher_list = Teacher.query
    if username:
        teacher_list = teacher_list.filter(Teacher.username==username)
    return render_template("admin/ateacher.html",teacher_list = teacher_list)

@admin.route("/ateacher/edit/<id>/",methods=["GET","POST"])
def teacherEdit(id=None):
    teacher = Teacher.query.filter_by(id=id).first_or_404()
    teacher.password = generate_password_hash("123456")
    db.session.add(teacher)
    db.session.commit()
    flash("修改成功")
    return redirect(url_for("admin.ateacher"))




