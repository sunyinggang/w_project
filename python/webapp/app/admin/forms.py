#encoding = utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField,HiddenField
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
    submit = SubmitField(
        "注册",
        render_kw={
            "class": "btn btn-primary"
        }
    )

class CommodityForm(FlaskForm):
    title = StringField(
        render_kw={
            "class": "form-control",
            "required": "required"
        }
    )
    price = StringField(
        render_kw={
            "class": "form-control",
            "required": "required"
        }
    )
    os = SelectField(
        choices=[('苹果专区', '苹果专区'), ('安卓专区', '安卓专区'), ('双平台苹果登入', '双平台苹果登入'), ('双平台安卓登录', '双平台安卓登录')],
        render_kw={
            "class": "form-control",
        }
    )
    number = StringField(
        render_kw={
            "class": "form-control",
            "required": "required"
        }
    )
    area = StringField(
        render_kw={
            "class": "form-control",
            "required": "required"
        }
    )
    server = StringField(
        render_kw={
            "class": "form-control",
            "required": "required"
        }
    )
    rank = StringField(
        render_kw={
            "class": "form-control",
            "required": "required"
        }
    )
    type = SelectField(
        choices=[('无账号绑定', '无账号绑定'), ('手机绑定', '手机绑定'), ('签订合同账号', '签订合同账号'), ('有绑定账号', '有绑定账号')],
        render_kw={
            "class": "form-control",
        }
    )
    pet = StringField(
        render_kw={
            "class": "form-control",
            "required": "required"
        }
    )
    sect = SelectField(
        choices=[('大唐官府', '大唐官府'), ('方寸山', '方寸山'), ('狮驼岭', '狮驼岭'), ('普陀山', '普陀山'),
                 ('龙宫', '龙宫'), ('阴曹地府', '阴曹地府'), ('魔王山', '魔王山'), ('化生寺', '化生寺'),
                 ('月宫', '月宫')],
        render_kw={
            "class": "form-control",
        }
    )
    sex = SelectField(
        choices=[('男', '男'), ('女', '女')],
        render_kw={
            "class": "form-control",
        }
    )
    bargain = SelectField(
        choices=[('可议价', '可议价'), ('不可议价', '不可议价')],
        render_kw={
            "class": "form-control",
        }
    )
    description = TextAreaField(
        render_kw={
            "class": "form-control",
            "required": "required"
        }
    )
    tel = StringField(
        render_kw={
            "class": "form-control"
        }
    )
    wx = StringField(
        render_kw={
            "class": "form-control"
        }
    )
    content = HiddenField()
    submit = SubmitField(
        "确定",
        render_kw={
            "class": "btn btn-primary"
        }
    )


