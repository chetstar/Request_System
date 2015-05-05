from flask.ext.wtf import Form
from wtforms import validators
from wtforms import widgets
from wtforms import TextField, BooleanField, SubmitField, DateField,TextAreaField,SelectMultipleField,IntegerField,PasswordField,StringField,DateTimeField,FormField,RadioField,SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField

class Which(Form):
    formtype = RadioField('how ready are you', choices=[('Long','Long'),('Short','Short')],coerce=unicode)
    submit=SubmitField('Submit')

class LoginForm(Form):
    username = StringField('ACBHCS login', validators=[validators.DataRequired()])
    password = PasswordField('Password', [validators.Required()])
    remember_me = BooleanField('remember_me', default=False)
    submit=SubmitField('Submit')

# [validators.Required(),validators.Length(min=2, max=50)]
class Request(Form):
    # test= QuerySelectField(query_factory=Requests.with_entities(Requests.id)) 
    jobTitle= TextField('This will be the ID we use to communicate about the request.')
    emanio = BooleanField('Yes, I have looked at Emanio Context <a href="http://covecontext/RunDashboard.i4?dashUUID=2e74cf96-b33b-4a7a-b53f-4310ce259dc6&primaryOrg=1&clientOrg=1">click here to check</a>.', default=False)
    MHorSUD= RadioField('Is this MHS or SUD Services related?', choices=[('MHS','MHS'),('SUD','SUD Services')],coerce=unicode)
    longDescription= TextAreaField('Describe what you want to investigate.', )
    keyQuestions= TextAreaField('What are the questions you want answered?', )
    problem= TextAreaField('If the data shows a problem, describe your intervention or what data you might you need for that intervention')
    audience= TextAreaField('Whith whom or in what forum do you plan to share this data?',)
    columnsRequired= TextAreaField('List all the data-points that you need.', )
    agency= TextField('For what Agencies do want this data?', ) 
    ru = TextField('For what Programs?',  ) 
    deadlinetime = SelectField(u'What Hour?', choices=[(8,'8 am'), (9, '9 a.m'), (12, 'noon')])
    deadlinedate= DateField( '',  format='%m/%d/%Y',validators = [validators.Required()])
    deadlineWhy = TextField('Why?')
    priority= RadioField('Priority', choices=[('1','Just Curious'),('2',''),('3','Medium'),('4',''),('5','Top Priority')],coerce=unicode)
    requestedBy= TextField("If this isn't your request, who is it for?") 
    # deliveryFormat= TextField('Format for Delivery', [validators.Required(),validators.Length(min=2, max=50)] ) 
    # start and end?
    timeframe= TextField('From what timeframe do you want data? .e.g. Most recent fiscal year. Most recent calendar year. etc.',  ) 
    timeBreakdown = TextField("what's the smallest increment of time you want to see the data. e.g. month, quarterly or annually.",  ) 
    specialPop= TextField('Are you interested in a Special Population? e.g. Foster kids or dissabled adults, etc.',  ) 
    typeOfService= TextField('Are there specific types of services you want? e.g. Crisis, Hospital, etc.', ) 
    specialInstructions= TextField('Any special instructions?',  ) 
    specialFacts= TextAreaField('Are there any facts or circumstances we should know to fulfil this request?') 
    submit=SubmitField('Submit')

class Staff(Form):
    assinged= TextField('Staff Assigned?') 
    completeDate= DateTimeField( 'Date Completed',  format='%c')
    reviewed= TextField('Reviewed by?') 
    submit=SubmitField('Submit')
