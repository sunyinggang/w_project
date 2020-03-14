from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, HiddenField, SelectField, TextAreaField
from wtforms.validators import DataRequired

from app.models import Driver, ExpenseType


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

class CarForm(FlaskForm):
    number = StringField(
        label="车牌号码",
        validators=[
            DataRequired()
        ],
        render_kw={
            "class": "form-control form-control-sm",
            "placeholder": "请输入车牌号码"
        }
    )
    nickname = StringField(
        label="别名",
        render_kw={
            "class": "form-control form-control-sm",
            "placeholder": "请输入车辆别名，如1号车"
        }
    )
    capacity = StringField(
        label="车辆容量",
        validators=[
            DataRequired()
        ],
        render_kw={
            "class": "form-control form-control-sm",
            "placeholder": "请输入车辆载客量/载货量"
        }
    )
    model = StringField(
        label="车辆型号",
        validators=[
            DataRequired()
        ],
        render_kw={
            "class": "form-control form-control-sm",
            "placeholder": "请输入车辆型号"
        }
    )
    img_url = HiddenField(
        render_kw={
            "id": "path-1"
        }
    )
    # driver_id = SelectField(
    #     label="默认司机",
    #     validators=[
    #         DataRequired()
    #     ],
    #     render_kw={
    #         "class": "form-control"
    #     },
    #     coerce=int
    # )
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

    # def __init__(self, *args, **kwargs):
    #     super(CarForm, self).__init__(*args, **kwargs)
    #     self.driver_id.choices = [(v.id, v.name) for v in Driver.query.all()]

class NoticeForm(FlaskForm):
    content = TextAreaField(
        label="公告内容",
        validators=[
            DataRequired()
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "请输入公告内容"
        }
    )
    submit = SubmitField(
        "确认添加",
        render_kw={
            "class": "btn btn-primary btn-sm btn-sub-save"
        }
    )

class ScheduleForm(FlaskForm):
    unit = StringField(
        label="用车单位",
        validators=[
            DataRequired()
        ],
        render_kw={
            "class": "form-control form-control-sm",
            "placeholder": "请输入用车单位"
        }
    )
    user = StringField(
        label="用车人",
        validators=[
            DataRequired()
        ],
        render_kw={
            "class": "form-control form-control-sm",
            "placeholder": "请输入用车人姓名"
        }
    )
    phone = StringField(
        label="用车人电话",
        validators=[
            DataRequired()
        ],
        render_kw={
            "class": "form-control form-control-sm",
            "placeholder": "请输入用车人电话"
        }
    )
    start_point = StringField(
        label="起点",
        validators=[
            DataRequired()
        ],
        render_kw={
            "class": "form-control form-control-sm",
            "placeholder": "请输入起点"
        }
    )
    end_point = StringField(
        label="终点",
        validators=[
            DataRequired()
        ],
        render_kw={
            "class": "form-control form-control-sm",
            "placeholder": "请输入终点"
        }
    )
    start_time = StringField(
        label="出发时间",
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
            DataRequired("Please input Departure Time！")
        ],
        description="Departure Time",
        render_kw={
            "class": "form-control",
            "id": "datetimepicker2",
            "value": "2020-01-01 00:00"
        }
    )
    money = StringField(
        label="用车费用",
        validators=[
            DataRequired()
        ],
        render_kw={
            "class": "form-control form-control-sm",
            "placeholder": "请输入用车费用"
        }
    )
    driver_money = StringField(
        label="司机费用",
        validators=[
            DataRequired()
        ],
        render_kw={
            "class": "form-control form-control-sm",
            "placeholder": "请输入司机费用"
        }
    )
    content = TextAreaField(
        label="备注",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入备注"
        }
    )
    submit = SubmitField(
        "确认添加",
        render_kw={
            "class": "btn btn-primary btn-sm btn-sub-save"
        }
    )

class ExpenseTypeForm(FlaskForm):
    name = StringField(
        label="费用类型名称",
        validators=[
            DataRequired()
        ],
        render_kw={
            "class": "form-control form-control-sm",
            "placeholder": "请输入费用类型名称"
        }
    )
    type = SelectField(
        label="收入/支出",
        choices=[('收入', '收入'), ('支出', '支出')],
        render_kw={
            "class": "form-control",
        }
    )
    content = TextAreaField(
        label="备注",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入备注内容"
        }
    )
    submit = SubmitField(
        "确认添加",
        render_kw={
            "class": "btn btn-primary btn-sm btn-sub-save"
        }
    )

class ExpenseForm(FlaskForm):
    expense_type = SelectField(
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
            "class": "btn btn-primary btn-sm btn-sub-save"
        }
    )

    def __init__(self, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        self.expense_type.choices = [(v.id, v.name) for v in ExpenseType.query.all()]
