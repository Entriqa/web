from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, \
    BooleanField, SubmitField
from wtforms.validators import DataRequired


class Form(FlaskForm):
    surname = StringField('Фамилия')
    name = StringField('Имя')
    education = StringField('Образование')
    profession = StringField('Профессия')
    sex = 
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
