from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, SubmitField, DateField,TextAreaField,SelectMultipleField,IntegerField,PasswordField,StringField,DateTimeField,RadioField
from wtforms import validators
from wtforms import widgets

class LoginForm(Form):
    username = StringField('ACBHCS login', validators=[validators.DataRequired()])
    password = PasswordField('Password', [validators.Required()])
    remember_me = BooleanField('remember_me', default=False)
    submit=SubmitField('Submit')

class Request(Form):
    username = TextField('Project *', [validators.Required(),validators.Length(min=2, max=50)] ) 
    email = TextField('Project *', [validators.Required(),validators.Length(min=2, max=50)] ) 
    guid = TextField('Project *', [validators.Required(),validators.Length(min=2, max=50)] ) 
    requestDate= DateTimeField( 'Deadline',  format='%c',validators = [validators.Required()])
    requestDeadlineLapse= IntegerField('Lapse between ')
    requestedBy= TextField('If requesting for someone else, who?') 
    deadline= DateTimeField( 'Deadline',  format='%c',validators = [validators.Required()])
    priority= RadioField('Label', choices=[('value','description'),('value_two','whatever')],coerce=unicode)
    deliveryFormat= TextField('', [validators.Required(),validators.Length(min=2, max=50)] ) 
    timeframe= TextField('', [validators.Required(),validators.Length(min=2, max=50)] ) 
    increments= TextField('', [validators.Required(),validators.Length(min=2, max=50)] ) 
    specialPop= TextField('', [validators.Required(),validators.Length(min=2, max=50)] ) 
    agency= TextField('', [validators.Required(),validators.Length(min=2, max=50)] ) 
    ru = TextField('', [validators.Required(),validators.Length(min=2, max=50)] ) 
    typeOfService= TextField('', [validators.Required(),validators.Length(min=2, max=50)] ) 
    dataElements= TextField('', [validators.Required(),validators.Length(min=2, max=50)] ) 
    briefDescription= TextAreaField('Goal', [validators.Required(),validators.Length(min=2, max=200,message='not the right length')])
    longDescription= TextAreaField('Goal', [validators.Required(),validators.Length(min=2, max=200,message='not the right length')])
    specialInstructions= TextField('', [validators.Required(),validators.Length(min=2, max=50)] ) 
    audience= TextAreaField('Goal', [validators.Required(),validators.Length(min=2, max=200,message='not the right length')])
    purpose= TextAreaField('Goal', [validators.Required(),validators.Length(min=2, max=200,message='not the right length')])
    columnsRequired= TextAreaField('Goal', [validators.Required(),validators.Length(min=2, max=200,message='not the right length')])
    assinged= TextField('If requesting for someone else, who?') 
    completeDate= DateTimeField( 'Deadline',  format='%c',validators = [validators.Required()])
    reviewed= TextField('', [validators.Required(),validators.Length(min=2, max=50)] ) 
    userCategory= RadioField('Label', choices=[('value','description'),('value_two','whatever')],coerce=unicode)
