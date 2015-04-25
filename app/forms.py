from flask.ext.wtf import Form
from wtforms import StringField, BooleanField,SubmitField
from wtforms.validators import DataRequired
from wtforms import TextField, PasswordField, validators

class LoginForm(Form):
    username = StringField('ACBHCS login', validators=[DataRequired()])
    password = PasswordField('Password', [validators.Required()])
    remember_me = BooleanField('remember_me', default=False)
    submit=SubmitField('Submit')