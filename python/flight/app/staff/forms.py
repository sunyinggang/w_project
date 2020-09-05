#encoding = utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField,IntegerField
from wtforms.validators import DataRequired
from app.models import Airplane,Airport

airplane = Airplane.query.all()
airport = Airport.query.all()

class AirportForm(FlaskForm):
    name = StringField(
        label="name",
        validators=[
            DataRequired("Please input airport name！")
        ],
        description="name",
        render_kw={
            "class": "form-control"
        }
    )
    city = StringField(
        label="city",
        validators=[
            DataRequired("Please input airport city！")
        ],
        description="city",
        render_kw={
            "class": "form-control"
        }
    )
    submit = SubmitField(
        "submit",
        render_kw={
            "class": "btn btn-primary"
        }
    )

class AirplaneForm(FlaskForm):
    id = StringField(
        label="ID",
        validators=[
            DataRequired("Please input airplane ID！")
        ],
        description="ID",
        render_kw={
            "class": "form-control",
            "placeholder": "E.g: AA01"
        }
    )
    seats = IntegerField(
        label="seats",
        validators=[
            DataRequired("Please input airplane seats！")
        ],
        description="seats",
        render_kw={
            "class": "form-control"
        }
    )
    airline_name = StringField(
        label="Airline Name",
        description="Airline Name",
        render_kw={
            "class": "form-control",
            "readonly": "readonly"
        }
    )
    submit = SubmitField(
        "submit",
        render_kw={
            "class": "btn btn-primary"
        }
    )


class FlightForm(FlaskForm):
    flight_num = StringField(
        label="flight_num",
        validators=[
            DataRequired("Please input airplane Flight Number！")
        ],
        description="Flight Number",
        render_kw={
            "class": "form-control"
        }
    )
    departure_time = StringField(
        label="Departure Time",
        validators=[
            DataRequired("Please input Departure Time！")
        ],
        description="Departure Time",
        render_kw={
            "class": "form-control",
            "id": "datetimepicker",
            "value": "2018-11-09 00:00"
        }
    )
    arrival_time = StringField(
        label="Arrival Time",
        validators=[
            DataRequired("Please input Arrival Time！")
        ],
        description="Arrival Time",
        render_kw={
            "class": "form-control",
            "id": "datetimepicker2",
            "value": "2018-11-09 00:00"
        }
    )
    price = StringField(
        label="Price",
        validators=[
            DataRequired("Please input Price！")
        ],
        description="Price",
        render_kw={
            "class": "form-control"
        }
    )
    airline_name = StringField(
        label="Airline Name",
        description="Airline Name",
        render_kw={
            "class": "form-control",
            "readonly": "readonly"
        }
    )
    airplane_name = SelectField(
        label="Airplane Name",
        validators=[
            DataRequired("Please input Departure Airport Name！")
        ],
        choices=[(v.id, v.id) for v in airplane],
        render_kw={
            "class": "form-control"
        }
    )
    departure_airport_name = SelectField(
        label="Departure Airport Name",
        choices=[(v.name, v.name) for v in airport],
        render_kw={
            "class": "form-control"
        }
    )
    arrival_airport_name = SelectField(
        label="Arrival Airport Name",
        choices=[(v.name, v.name) for v in airport],
        render_kw={
            "class": "form-control"
        }
    )
    submit = SubmitField(
        "submit",
        render_kw={
            "class": "btn btn-primary"
        }
    )

class FightStatusForm(FlaskForm):
    flight_num = StringField(
        label="Flight Number",
        description="Flight Number",
        render_kw={
            "class": "form-control",
            "readonly": "readonly"
        }
    )
    status = SelectField(
        label="Flight Stutus",
        choices=[("upcoming","upcoming"),("in-progress","in-progress"),("delayed","delayed")],
        render_kw={
            "class": "form-control"
        }
    )
    submit = SubmitField(
        "submit",
        render_kw={
            "class": "btn btn-primary"
        }
    )

class SearchForm(FlaskForm):
    departure_airport= StringField(
        render_kw={
            "class": "form-control"
        }
    )
    arrival_airport= StringField(
        render_kw={
            "class": "form-control"
        }
    )
    departure_city= StringField(
        render_kw={
            "class": "form-control"
        }
    )
    arrival_city= StringField(
        render_kw={
            "class": "form-control"
        }
    )
    submit = SubmitField(
        "Confirm search",
        render_kw={
            "class": "btn btn-primary"
        }
    )

class InformationForm(FlaskForm):
    first_name= StringField(
        validators=[
            DataRequired("Please input First Name！")
        ],
        render_kw={
            "class": "form-control"
        }
    )
    last_name= StringField(
        validators=[
            DataRequired("Please input Last Name！")
        ],
        render_kw={
            "class": "form-control"
        }
    )
    date_of_birth= StringField(
        validators=[
            DataRequired("Please input Date of Birth！")
        ],
        render_kw={
            "class": "form-control",
            "id": "datetimepicker",
            "value": "1900-01-01 00:00"
        }
    )
    airline_name= StringField(
        render_kw={
            "class": "form-control",
            "readonly": "readonly"
        }
    )
    submit = SubmitField(
        "Confirm search",
        render_kw={
            "class": "btn btn-primary"
        }
    )