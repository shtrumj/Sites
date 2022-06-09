from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, PasswordField, EmailField,DateField
from wtforms.validators import InputRequired


class ServersForm(FlaskForm):
    SiteName = StringField('Site Name', validators=[InputRequired()])
    serverName = StringField('Server Name', validators=[InputRequired()])
    IPAddress = StringField('IP Address', validators=[InputRequired()])
    OS = StringField('Operation System', validators=[InputRequired()])
    HOST_IP = StringField('Host IP Address', validators=[InputRequired()])
    HOSTType = StringField('Host Type', validators=[InputRequired()])
    HOST_ILOM_IP = StringField('Host ILOM IP', validators=[InputRequired()])


class Users(FlaskForm):
    UserName = StringField('User Name', validators=[InputRequired()])
    Password = PasswordField('Password', validators=[InputRequired()])
    emailAdd = EmailField('Email Address', validators=[InputRequired()])


class Employees(FlaskForm):
    firstName = StringField('Employee First Name', validators=[InputRequired()])
    lastName = StringField('Employee Last Name', validators=[InputRequired()])
    email = StringField('Email Address', validators=[InputRequired()])
    cellPhone = StringField('Cellphone Number',validators=[InputRequired()])
    birthDay = DateField('Birthday', format ='%d/%m/%Y')


    # https://codeloop.org/flask-wtf-registration-form-with-sqlalchemy/
