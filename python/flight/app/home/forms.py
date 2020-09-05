#encoding = utf-8
#encoding = utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from app.models import Airline

airline = Airline.query.all()

class LoginForm(FlaskForm):
    email = StringField(
        label="email",
        validators=[
            DataRequired("Please input your email！")
        ],
        description="email",
        render_kw={
            "class": "form-control",
            "placeholder": "email or username"
        }
    )
    password = PasswordField(
        label="password",
        validators=[
            DataRequired("Please input your password！")
        ],
        description="password",
        render_kw={
            "class": "form-control",
            "placeholder" : "password"
        }
    )
    usertype = SelectField(
        label="usertype",
        validators=[
            DataRequired("Please input your usertype！")
        ],
        choices=[(1, 'Customer'), (2, 'Agent'), (3, 'Staff')],
        coerce=int,
        render_kw={
            "class": "form-control",
        }
    )
    submit = SubmitField(
        "submit",
        render_kw={
            "class": "btn btn-primary"
        }
    )

class RegisterForm(FlaskForm):
    email = StringField(
        label="email",
        validators=[
            DataRequired("Please input your email！")
        ],
        description="email",
        render_kw={
            "class": "form-control",
            "placeholder": "email"
        }
    )
    password = PasswordField(
        label="password",
        validators=[
            DataRequired("Please input your password！")
        ],
        description="password",
        render_kw={
            "class": "form-control",
            "placeholder" : "password"
        }
    )
    passwordtwo = PasswordField(
        label="password",
        validators=[
            DataRequired("Please enter your password again！")
        ],
        description="password",
        render_kw={
            "class": "form-control",
            "placeholder": "confirm password"
        }
    )
    usertype = SelectField(
        label="usertype",
        validators=[
            DataRequired("Please input your usertype！")
        ],
        choices=[(1, 'Customer'), (2, 'Agent')],
        coerce=int,
        render_kw={
            "class": "form-control",
        }
    )
    submit = SubmitField(
        "submit",
        render_kw={
            "class": "btn btn-primary"
        }
    )

class StaffRegisterForm(FlaskForm):
    username = StringField(
        label="username",
        validators=[
            DataRequired("Please input your username！")
        ],
        description="username",
        render_kw={
            "class": "form-control",
            "placeholder": "username"
        }
    )
    password = PasswordField(
        label="password",
        validators=[
            DataRequired("Please input your password！")
        ],
        description="password",
        render_kw={
            "class": "form-control",
            "placeholder" : "password"
        }
    )
    passwordtwo = PasswordField(
        label="password",
        validators=[
            DataRequired("Please enter your password again！")
        ],
        description="password",
        render_kw={
            "class": "form-control",
            "placeholder": "confirm password"
        }
    )
    airline_name = SelectField(
        label="airline_name",
        validators=[
            DataRequired("Please input your airline_name！")
        ],
        choices=[(v.name, v.name) for v in airline],
        render_kw={
            "class": "form-control",
        }
    )
    submit = SubmitField(
        "submit",
        render_kw={
            "class": "btn btn-primary"
        }
    )


class TicketForm(FlaskForm):
    flight_num = StringField(
        render_kw={
            "class": "form-control",
            "readonly": "readonly"
        }
    )
    departure_airport_name = StringField(
        render_kw={
            "class": "form-control",
            "readonly": "readonly"
        }
    )
    arrival_airport_name = StringField(
        render_kw={
            "class": "form-control",
            "readonly": "readonly"
        }
    )
    departure_time = StringField(
        render_kw={
            "class": "form-control",
            "readonly": "readonly",
            "id": "datetimepicker"
        }
    )
    arrival_time = StringField(
        render_kw={
            "class": "form-control",
            "readonly": "readonly",
            "id": "datetimepicker2"
        }
    )
    price = StringField(
        render_kw={
            "class": "form-control",
            "readonly": "readonly"
        }
    )
    rest_seat = StringField(
        render_kw={
            "class": "form-control",
            "readonly": "readonly"
        }
    )
    email = StringField(
        validators=[
            DataRequired("Please input User email！")
        ],
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