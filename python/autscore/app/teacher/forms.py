from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ExperimentForm(FlaskForm):
    name = StringField(
        label="实验名称",
        validators=[
            DataRequired("实验名称不为空！")
        ],
        description="实验名称",
        render_kw={
            "class": "form-control"
        }
    )
    start_time = StringField(
        label="开始时间",
        validators=[
            DataRequired("开始时间不为空！")
        ],
        description="开始时间",
        render_kw={
            "class": "form-control",
            "id": "datetimepicker",
            "value": "2020-01-01 00:00"
        }
    )
    end_time = StringField(
        label="结束时间",
        validators=[
            DataRequired("结束时间不为空！")
        ],
        description="结束时间",
        render_kw={
            "class": "form-control",
            "id": "datetimepicker2",
            "value": "2020-01-01 00:00"
        }
    )
    submit = SubmitField(
        "确认",
        render_kw={
            "class": "btn btn-primary"
        }
    )