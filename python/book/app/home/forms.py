#encoding = utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired

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
    usertype = SelectField(
        label="用户类型",
        validators=[
            DataRequired("请选择用户类型！")
        ],
        choices=[(1, '学生'), (2, '管理员')],
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

class registerForm(FlaskForm):
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
            "placeholder": "密码",
            "required": "required"
        }
    )
    passwordtwo = PasswordField(
        label="密码",
        validators=[
            DataRequired("请再次输入密码！")
        ],
        description="密码",
        render_kw={
            "class": "form-control",
            "placeholder": "确认密码",
            "required": "required"
        }
    )
    usertype = SelectField(
        label="用户类型",
        validators=[
            DataRequired("请选择用户类型！")
        ],
        choices=[(1, '学生'), (2, '管理员')],
        coerce=int,
        render_kw={
            "class": "form-control",
        }
    )
    submit = SubmitField(
        "注册",
        render_kw={
            "class": "btn btn-primary"
        }
    )

class BookForm(FlaskForm):
    title = StringField(
        label="图书名称",
        validators=[
            DataRequired("请输入图书名称！")
        ],
        description="图书名称",
        render_kw={
            "class": "form-control",
            "required": "required"
        }
    )
    date = StringField(
        label="借书日期",
        validators=[
            DataRequired("请输入借书日期！")
        ],
        description="借书日期",
        render_kw={
            "class": "form-control",
            "required": "required"
        }
    )
    day = StringField(
        label="借书天数",
        validators=[
            DataRequired("请输入借书天数！")
        ],
        description="借书天数",
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


