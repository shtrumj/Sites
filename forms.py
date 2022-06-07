from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired


class ServersForm(FlaskForm):
    SiteName = StringField('Site Name', validators=[InputRequired()])
    serverName = StringField('Server Name', validators=[InputRequired()])
    IPAddress = StringField('IP Address', validators=[InputRequired()])
    OS = StringField('Operation System', validators=[InputRequired()])
    HOST_IP = StringField('Host IP Address', validators=[InputRequired()])
    HOSTType = StringField('Host Type', validators=[InputRequired()])
    HOST_ILOM_IP = StringField('Host ILOM IP', validators=[InputRequired()])





    #https://codeloop.org/flask-wtf-registration-form-with-sqlalchemy/