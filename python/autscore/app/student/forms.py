from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

from app.models import Class


class ClassForm(FlaskForm):
    class_name = SelectField(
        label="班级",
        validators=[
            DataRequired("请选择班级！")
        ],
        render_kw={
            "class": "form-control"
        },
        coerce=int
    )
    submit = SubmitField(
        "确认",
        render_kw={
            "class": "btn btn-primary"
        }
    )

    def __init__(self, *args, **kwargs):
        super(ClassForm, self).__init__(*args, **kwargs)
        self.class_name.choices = [(v.id, v.name) for v in Class.query.all()]