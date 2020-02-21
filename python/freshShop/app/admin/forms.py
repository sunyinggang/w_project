#encoding = utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField,FileField
from wtforms.validators import DataRequired
from app.models import Category
from flask_ckeditor import CKEditorField

category = Category.query.all()

class LoginForm(FlaskForm):
    username = StringField(
        label="账号",
        validators=[
            DataRequired("请输入账号！")
        ],
        description="账号",
        render_kw={
            "class": "form-control",
            "placeholder": "账号",
            "required": "required"
        }
    )
    password = PasswordField(
        label="密码",
        validators=[
            DataRequired("请输入密码！")
        ],
        description="密码",
        render_kw={
            "class": "form-control",
            "placeholder" : "密码",
             "required": "required"
        }
    )
    submit = SubmitField(
        "登录",
        render_kw={
            "class": "btn btn-primary"
        }
    )

class CategoryForm(FlaskForm):
    name = StringField(
        validators=[
            DataRequired("请输入商品分类名！")
        ],
        render_kw={
            "class": "form-control",
            "required": "required"
        }
    )
    submit = SubmitField(
        "确定",
        render_kw={
            "class": "btn btn-primary"
        }
    )

class ProductForm(FlaskForm):
    name = StringField(
        validators=[
            DataRequired("请上传商品图片！")
        ],
        render_kw={
            "class": "form-control"
        }
    )
    img = FileField(
        render_kw={
            "class": "form-control"
        }
    )
    category_id = SelectField(
        validators=[
            DataRequired("请选择商品分类！")
        ],
        choices=[(v.id, v.name) for v in category],
        render_kw={
            "class": "form-control",
        }
    )
    price = StringField(
        validators=[
            DataRequired("请填写商品价格！")
        ],
        render_kw={
            "class": "form-control"
        }
    )
    content = CKEditorField('Content')
    submit = SubmitField(
        "确定",
        render_kw={
            "class": "btn btn-primary"
        }
    )

class AnnouncementForm(FlaskForm):
    title = StringField(
        render_kw={
            "class": "form-control",
            "required": "required"
        }
    )
    content = TextAreaField(
        render_kw={
            "class": "form-control",
            "required": "required"
        }
    )
    submit = SubmitField(
        "确定",
        render_kw={
            "class": "btn btn-primary"
        }
    )

class HelpForm(FlaskForm):
    info = TextAreaField(
        render_kw={
            "class": "form-control mytext",
            "required": "required"
        }
    )
    problem = TextAreaField(
        render_kw={
            "class": "form-control mytext",
            "required": "required"
        }
    )
    distribution = TextAreaField(
        render_kw={
            "class": "form-control mytext",
            "required": "required"
        }
    )
    submit = SubmitField(
        "确定",
        render_kw={
            "class": "btn btn-primary"
        }
    )

class ReviewForm(FlaskForm):
    content = TextAreaField(
        validators=[
            DataRequired("请输入商品评价！")
        ],
        description="商品评价",
        render_kw={
            "class": "site_area",
            "required": "required"
        }
    )
    img = FileField(
        render_kw={
            "class": "form-control",
            "required": "required"
        }
    )
