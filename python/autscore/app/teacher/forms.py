from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import StringField, SubmitField, FileField, SelectField, HiddenField, TextAreaField
from wtforms.validators import DataRequired

from app.models import Class

classList = Class.query.all()

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
    keywords = TextAreaField(
        label="实验关键字",
        validators=[
            DataRequired("实验关键字不为空！")
        ],
        description="实验关键字",
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
    model_url = FileField(
        label="实验报告上传",
        validators=[
            # 文件必须选择;
            FileRequired("必须添加实验报告模板！"),
        ]
    )
    submit = SubmitField(
        "确认",
        render_kw={
            "class": "btn btn-primary"
        }
    )
    
class ClassFindForm(FlaskForm):
    class_name = SelectField(
        label="班级",
        validators=[
            DataRequired("请选择班级！")
        ],
        choices=[(v.id, v.name) for v in classList],
        render_kw={
            "class": "form-control"
        },
        coerce=int
    )
    id = HiddenField()
    submit = SubmitField(
        "确认",
        render_kw={
            "class": "btn btn-primary"
        }
    )

class ScoreForm(FlaskForm):
    score = StringField(
        label="分数",
        validators=[
            DataRequired("分数不为空！")
        ],
        description="分数",
        render_kw={
            "class": "form-control"
        }
    )
    submit = SubmitField(
        "确认",
        render_kw={
            "class": "btn btn-primary"
        }
    )

class KeyWordsForm(FlaskForm):
    keywords = TextAreaField(
        label="实验关键字",
        validators=[
            DataRequired("实验关键字不为空！")
        ],
        description="实验关键字",
        render_kw={
            "class": "form-control"
        }
    )
    submit = SubmitField(
        "修改",
        render_kw={
            "class": "btn btn-primary"
        }
    )