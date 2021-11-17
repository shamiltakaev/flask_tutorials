from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.fields.choices import SelectField
from wtforms.fields.form import FormField
from wtforms.fields.list import FieldList
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    login = StringField("Login", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign In")

class AddNewTask(FlaskForm):
    description = StringField("Описание задачи", validators=[DataRequired()])
    modules = SelectField("Выберите модуль", validators=[DataRequired()],
    choices=["1", "2"])
    submit = SubmitField("Добавить задачу")