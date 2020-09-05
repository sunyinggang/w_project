#encoding = utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField,FileField
from wtforms.validators import DataRequired
from app.models import Category

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
            DataRequired("请输入美食分类名！")
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
            DataRequired("请书写美食名称！")
        ],
        render_kw={
            "class": "form-control"
        }
    )
    img = FileField(
        validators=[
            DataRequired("请上传美食图片！")
        ],
        render_kw={
            "class": "form-control"
        }
    )
    category_id = SelectField(
        validators=[
            DataRequired("请选择美食分类！")
        ],
        choices=[(v.id, v.name) for v in category],
        render_kw={
            "class": "form-control",
        }
    )
    content = TextAreaField(
        validators=[
            DataRequired("请填写美食价格！")
        ],
        render_kw={
            "class": "form-control"
        }
    )
    submit = SubmitField(
        "确定",
        render_kw={
            "class": "btn btn-primary"
        }
    )


