from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, HiddenField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    phone = StringField(
        label="手机号码",
        validators=[
            DataRequired()
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "手机号码"
        }
    )
    password = PasswordField(
        label="密码",
        validators=[
            DataRequired()
        ],
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
            DataRequired()
        ],
        render_kw={
            "class": "form-control form-control-sm",
            "placeholder": "请输入旧密码"
        }
    )
    newpassword = PasswordField(
        label="新密码",
        validators=[
            DataRequired()
        ],
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

class DriverForm(FlaskForm):
    name = StringField(
        label="姓名",
        validators=[
            DataRequired()
        ],
        render_kw={
            "class": "form-control form-control-sm",
            "placeholder": "请输入司机姓名"
        }
    )
    phone = StringField(
        label="手机号码",
        validators=[
            DataRequired()
        ],
        render_kw={
            "class": "form-control form-control-sm",
            "placeholder": "请输入手机号码"
        }
    )
    address = StringField(
        label="住址",
        validators=[
            DataRequired()
        ],
        render_kw={
            "class": "form-control form-control-sm",
            "placeholder": "请输入司机姓名"
        }
    )
    idcardz = HiddenField(
        render_kw={
            "id": "path-1"
        }
    )
    idcardf = HiddenField(
        render_kw={
            "id": "path-2"
        }
    )
    drivercardz = HiddenField(
        render_kw={
            "id": "path-3"
        }
    )
    drivercardf = HiddenField(
        render_kw={
            "id": "path-4"
        }
    )
    content = StringField(
        label="备注",
        render_kw={
            "class": "form-control form-control-sm",
            "placeholder": "更多备注信息"
        }
    )
    submit = SubmitField(
        "确认添加",
        render_kw={
            "class": "btn btn-primary btn-sm ml-3 btn-sub-save"
        }
    )

