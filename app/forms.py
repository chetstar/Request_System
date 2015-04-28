from flask.ext.wtf import Form
from wtforms import StringField, BooleanField,SubmitField
from wtforms.validators import DataRequired
from wtforms import TextField, PasswordField, validators

class LoginForm(Form):
    username = StringField('ACBHCS login', validators=[DataRequired()])
    password = PasswordField('Password', [validators.Required()])
    remember_me = BooleanField('remember_me', default=False)
    submit=SubmitField('Submit')

class Request(Form):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    guid = db.Column(db.String(64), index=True, unique=True)
    requestDate= db.Column(db.Date)
    requestDeadlineLapse= db.Column(db.Integer)
    requestedBy= db.Column(db.String(64), index=True)
    deadline= db.Column(db.Date)
    priority= db.Column(db.String(64), index=True)
    deliveryFormat= db.Column(db.String(64), index=True)
    timeframe= db.Column(db.String(64), index=True)
    increments= db.Column(db.String(64), index=True)
    specialPop= db.Column(db.String(64), index=True)
    agency= db.Column(db.String(64), index=True)
    ru = db.Column(db.String(64), index=True)
    typeOfService= db.Column(db.String(64), index=True)
    dataElements= db.Column(db.String(64), index=True)
    briefDescription= db.Column(db.String(64), index=True)
    longDescription= db.Column(db.String(64), index=True)
    specialInstructions= db.Column(db.String(64), index=True)
    audience= db.Column(db.String(64), index=True)
    purpose= db.Column(db.String(64), index=True)
    columnsRequired= db.Column(db.String(64), index=True)
    assinged= db.Column(db.String(64), index=True)
    completeDate= db.Column(db.Date)
    reviewed= db.Column(db.String(64), index=True)
    userCategory= db.Column(db.String(64), index=True,

    def __repr__(self):
        return '<%r>' % (self.briefDescription)
