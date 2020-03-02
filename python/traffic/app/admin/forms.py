from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    phone = StringField(
        label="手机号码",
        validators=[
            DataRequired("手机号码不为空！")
        ],
        description="手机号码",
        render_kw={
            "class": "form-control",
            "placeholder": "手机号码"
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
    submit = SubmitField(
        "登录",
        render_kw={
            "class": "btn btn-primary w-100"
        }
    )



