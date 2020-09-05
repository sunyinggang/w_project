#encoding = utf-8
"""
 Created by Felix on 
"""
__author__ = 'Felix'
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField(
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
