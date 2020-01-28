from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

from app.models import Class

classList = Class.query.all()

class ClassForm(FlaskForm):
    class_name = SelectField(
        label="班级",
        validators=[
            DataRequired("请选择班级！")
        ],
        choices=[(v.id, v.name) for v in classList],
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