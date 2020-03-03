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

class ChangeForm(FlaskForm):
    password = PasswordField(
        label="旧密码",
        validators=[
            DataRequired("旧密码不能为空！")
        ],
        description="旧密码",
        render_kw={
            "class": "form-control form-control-sm",
            "placeholder": "请输入旧密码"
        }
    )
    newpassword = PasswordField(
        label="新密码",
        validators=[
            DataRequired("新密码不能为空！")
        ],
        description="新密码",
        render_kw={
            "class": "form-control form-control-sm",
            "placeholder" : "请输入6~15位新密码"
        }
    )
    newpasswordt = PasswordField(
        label="密码",
        validators=[
            DataRequired("密码不能为空！")
        ],
        description="密码",
        render_kw={
            "class": "form-control form-control-sm",
            "placeholder": "请确认新密码"
        }
    )
    submit = SubmitField(
        "确认修改",
        render_kw={
            "class": "btn btn-primary btn-sm btn-sub-save"
        }
    )



