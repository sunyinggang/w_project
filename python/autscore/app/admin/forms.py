from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired


class ClassForm(FlaskForm):
    name = StringField(
        label="班级名",
        validators=[
            DataRequired("班级名不为空！")
        ],
        description="班级名",
        render_kw={
            "class": "form-control",
            "placeholder": "格式：系别-年级-班级（如：软件-16-3）"
        }
    )
    submit = SubmitField(
        "确认",
        render_kw={
            "class": "btn btn-primary"
        }
    )


