#encoding = utf-8
from . import home
from flask import render_template, redirect, url_for, flash, session, request, send_from_directory
from app.models import Category,Product,Natural,History,People


@home.route("/")
def index():
    return render_template("home/index.html")


@home.route("/delicacy/<int:id>/")
def delicacy(id=None):
    category = Category.query.all()
    product_list = Product.query.filter(Product.category_id==id).all()
    return render_template("home/delicacy.html",category=category,product_list=product_list,id=id)

@home.route("/detail/<int:id>/")
def detail(id=None):
    category = Category.query.all()
    product = Product.query.filter_by(id=id).first_or_404()
    return render_template("home/detail.html",category=category,product=product)

@home.route("/detail/historic/<int:id>/")
def detailHistoric(id=None):
    category = '历史'
    product = History.query.filter_by(id=id).first_or_404()
    return render_template("home/detailT.html",product=product,category=category)

@home.route("/detail/people/<int:id>/")
def detailPeople(id=None):
    category = '人文'
    product = People.query.filter_by(id=id).first_or_404()
    return render_template("home/detailT.html",product=product,category=category)

@home.route("/detail/natural/<int:id>/")
def detailNatural(id=None):
    category = '自然'
    product = Natural.query.filter_by(id=id).first_or_404()
    return render_template("home/detailT.html",product=product,category=category)

@home.route("/natural/")
def natural():
    product_list = Natural.query.all()
    return render_template("home/natural.html",product_list=product_list)

@home.route("/human/")
def human():
    product_list = People.query.all()
    return render_template("home/human.html",product_list=product_list)

@home.route("/historic/")
def historic():
    product_list = History.query.all()
    return render_template("home/historic.html",product_list=product_list)

