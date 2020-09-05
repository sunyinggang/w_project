#encoding = utf-8
"""
 Created by Felix on 
"""
__author__ = 'Felix'

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class InformationForm(FlaskForm):
   name= StringField(
        validators=[
            DataRequired("Please input Name！")
        ],
        render_kw={
            "class": "form-control"
        }
   )
   building_number = StringField(
        validators=[
            DataRequired("Please input Building_number！")
        ],
        render_kw={
            "class": "form-control"
        }
    )
   street = StringField(
        validators=[
            DataRequired("Please input Strees！")
        ],
        render_kw={
            "class": "form-control"
        }
    )
   city = StringField(
        validators=[
            DataRequired("Please input City！")
        ],
        render_kw={
            "class": "form-control"
        }
    )
   state = StringField(
        validators=[
            DataRequired("Please input State！")
        ],
        render_kw={
            "class": "form-control"
        }
    )
   phone_number = StringField(
        validators=[
            DataRequired("Please input Phone_number！")
        ],
        render_kw={
            "class": "form-control"
        }
    )
   passport_number = StringField(
       validators=[
           DataRequired("Please input Passport_number！")
       ],
       render_kw={
           "class": "form-control"
       }
   )
   passport_expiration = StringField(
        validators=[
            DataRequired("Please input Passport_expiration！")
        ],
       render_kw={
           "class": "form-control",
           "id": "datetimepicker",
           "value": "1900-01-01 00:00"
       }
    )
   passport_country = StringField(
        validators=[
            DataRequired("Please input Passport_country！")
        ],
        render_kw={
            "class": "form-control"
        }
    )
   date_of_birth = StringField(
        validators=[
            DataRequired("Please input Date of Birth！")
        ],
        render_kw={
            "class": "form-control",
            "id": "datetimepicker2",
            "value": "1900-01-01 00:00"
        }
    )
   submit = SubmitField(
        "Confirm search",
        render_kw={
            "class": "btn btn-primary"
        }
    )

