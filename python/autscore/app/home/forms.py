from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField(
        label="账号",
        validators=[
            DataRequired("账号不能为空！")
        ],
        description="账号",
        render_kw={
            "class": "form-control",
            "placeholder": "学号或工号"
        }
    )
    password = PasswordField(
        label="密码",
        validators=[
            DataRequired("密码不能为空！")
        ],
        description="密码",
        render_kw={
            "class": "form-control",
            "placeholder" : "密码"
        }
    )
    usertype = SelectField(
        label="用户类型",
        validators=[
            DataRequired("请选择用户类型！")
        ],
        choices=[(1, '教务'), (2, '教师'), (3, '学生')],
        coerce=int,
        render_kw={
            "class": "form-control",
        }
    )
    submit = SubmitField(
        "登录",
        render_kw={
            "class": "btn btn-primary"
        }
    )
