from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, HiddenField
from wtforms.validators import DataRequired

from app.models import ExpenseType


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
            "class": "btn btn-success w-100"
        }
    )

class ExpenseForm(FlaskForm):
    type_id = SelectField(
        label="费用类型",
        render_kw={
            "class": "form-control"
        },
        coerce=int
    )
    content = StringField(
        label="内容",
        validators=[
            DataRequired()
        ],
        render_kw={
            "class": "form-control form-control-sm",
            "placeholder": "请输入费用内容，如更换轮胎"
        }
    )
    money = StringField(
        label="金额",
        validators=[
            DataRequired()
        ],
        render_kw={
            "class": "form-control form-control-sm",
            "placeholder": "请输入费用金额"
        }
    )
    add_time = StringField(
        label="日期",
        validators=[
            DataRequired()
        ],
        render_kw={
            "class": "form-control",
            "id": "datetimepicker",
            "value": "2020-01-01 00:00"
        }
    )
    note = TextAreaField(
        label="备注",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入备注内容"
        }
    )
    img_url = HiddenField(
        render_kw={
            "id": "path-1"
        }
    )
    submit = SubmitField(
        "确认添加",
        render_kw={
            "class": "btn btn-success btn-sub-save"
        }
    )

    def __init__(self, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        self.type_id.choices = [(v.id, v.name) for v in ExpenseType.query.all() if v.type == '支出']

class LeaveForm(FlaskForm):
    content = TextAreaField(
        label="请假原因",
        validators=[
            DataRequired()
        ],
        render_kw={
            "class": "form-control form-control-sm",
            "placeholder": "请输入请假原因"
        }
    )
    start_time = StringField(
        label="开始时间",
        validators=[
            DataRequired()
        ],
        render_kw={
            "class": "form-control",
            "id": "datetimepicker",
            "value": "2020-01-01 00:00"
        }
    )
    end_time = StringField(
        label="结束时间",
        validators=[
            DataRequired()
        ],
        render_kw={
            "class": "form-control",
            "id": "datetimepicker2",
            "value": "2020-01-01 00:00"
        }
    )
    note = TextAreaField(
        label="备注",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入备注内容"
        }
    )
    submit = SubmitField(
        "确认请假",
        render_kw={
            "class": "btn btn-success btn-sub-save"
        }
    )