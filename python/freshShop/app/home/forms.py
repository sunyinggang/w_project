#encoding = utf-8
"""
 Created by Felix on 
"""
__author__ = 'Felix'
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,TextAreaField,FileField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField(
        validators=[
            DataRequired("请输入邮箱！")
        ],
        description="邮箱",
        render_kw={
            "class": "name_input",
            "placeholder": "请输入邮箱",
            "required": "required"
        }
    )
    password = PasswordField(
        validators=[
            DataRequired("请输入密码！")
        ],
        description="密码",
        render_kw={
            "class": "pass_input",
            "placeholder" : "请输入密码",
             "required": "required"
        }
    )
    submit = SubmitField(
        "登录",
        render_kw={
            "class": "input_submit"
        }
    )


class RegisterForm(FlaskForm):
    nickname = StringField(
        label="email",
        validators=[
            DataRequired("Please input your email！")
        ],
        description="email",
        render_kw={
            "placeholder": "昵称"
        }
    )
    password = PasswordField(
        label="password",
        validators=[
            DataRequired("Please input your password！")
        ],
        description="password",
        render_kw={
            "placeholder" : "密码"
        }
    )
    passwordtwo = PasswordField(
        label="password",
        validators=[
            DataRequired("Please enter your password again！")
        ],
        description="password",
        render_kw={
            "placeholder": "确认密码"
        }
    )
    email = StringField(
        label="email",
        validators=[
            DataRequired("Please input your email！")
        ],
        description="email",
        render_kw={
            "placeholder": "邮箱"
        }
    )
    submit = SubmitField(
        "注册"
    )


class AddressForm(FlaskForm):
    name = StringField(
        validators=[
            DataRequired("请输入姓名！")
        ],
        description="姓名",
        render_kw={
            "required": "required"
        }
    )
    phone = StringField(
        validators=[
            DataRequired("请输入手机号！")
        ],
        description="手机号",
        render_kw={
             "required": "required"
        }
    )
    address = TextAreaField(
        validators=[
            DataRequired("请输入详情地址！")
        ],
        description="详情地址",
        render_kw={
            "class": "site_area",
            "required": "required"
        }
    )
    submit = SubmitField(
        "提交",
        render_kw={
            "class": "info_submit"
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
    submit = SubmitField(
        "提交评价",
        render_kw={
            "class": "info_submit"
        }
    )