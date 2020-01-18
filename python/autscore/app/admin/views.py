import os

from flask import render_template, send_from_directory, make_response, send_file, request

import app
from . import admin

@admin.route("/")
def index():
    return render_template("admin/admin.html")

@admin.route("/aclass/")
def aclass():
    return render_template("admin/aclass.html")

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
def fileo():
    print(request.files)
    file = request.files['fileo']
    print('file', type(file), file)
    print(file.filename)    # 打印文件名
    #
    # f = file.read()    #文件内容
    # data = xlrd.open_workbook(file_contents=f)
    # table = data.sheets()[0]
    # names = data.sheet_names()  # 返回book中所有工作表的名字
    # status = data.sheet_loaded(names[0])  # 检查sheet1是否导入完毕
    # print(status)
    # nrows = table.nrows  # 获取该sheet中的有效行数
    # ncols = table.ncols  # 获取该sheet中的有效列数
    # print(nrows)
    # print(ncols)
    # s = table.col_values(0)  # 第1列数据
    # for i in s:
    #     ii = i.strip()
    #     print(len(ii))
    return 'OK'

@admin.route("/astudent/")
def astudent():
    return render_template("admin/astudent.html")

@admin.route("/ateacher/")
def ateacher():
    return render_template("admin/ateacher.html")




