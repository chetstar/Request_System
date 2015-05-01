from flask.ext.wtf import Form
from wtforms import validators
from wtforms import widgets
from wtforms import TextField, BooleanField, SubmitField, DateField,TextAreaField,SelectMultipleField,IntegerField,PasswordField,StringField,DateTimeField,FormField,RadioField

class Which(Form):
    formtype = RadioField('how ready are you', choices=[('Long','Long'),('Short','Short')],coerce=unicode)
    submit=SubmitField('Submit')

class LoginForm(Form):
    username = StringField('ACBHCS login', validators=[validators.DataRequired()])
    password = PasswordField('Password', [validators.Required()])
    remember_me = BooleanField('remember_me', default=False)
    submit=SubmitField('Submit')

# [validators.Required(),validators.Length(min=2, max=50)]
class RequestShort(Form):
    # userCategory=  RadioField(
        # 'System of Care',
        # [validators.Required()],
        # choices=[('choice1', 'Choice One'), ('choice2', 'Choice Two')], default='choice1'    )
    emanio = BooleanField('Have you checked Emanio?', default=False)
    MHorSUD= RadioField('MHS or SUD Services?', choices=[('MHS','MHS'),('SUD','SUD Services')],coerce=unicode)
    longDescription= TextAreaField('Describe the problem you want to investigate.', [validators.Required(),validators.Length(min=0, max=200,message='not the right length')])
    keyQuestions= TextAreaField('What are the questions you want answered?', [validators.Required(),validators.Length(min=0, max=200,message='not the right length')])
    problem= TextAreaField('If the data shows a problem, describe your intervention or what data you might you need for that intervention',
    	 [validators.Required(),validators.Length(min=2, max=200,message='not the right length')])
    audience= TextAreaField('Whith whom or in what forum do you plan to share this data?', [validators.Required(),validators.Length(min=0, max=200,message='not the right length')])
    columnsRequired= TextAreaField('List all the data-points that you need.', [validators.Required(),validators.Length(min=0, max=200,message='not the right length')])
    agency= TextField('For what Agencies do want this data?', [validators.Required(),validators.Length(min=0, max=50)] ) 
    ru = TextField('For what Programs?',  ) 
    jobTitle= TextAreaField('How do you want to refer to this request?', [validators.Required(),validators.Length(min=0, max=50,message='not the right length')])
    deadline= DateTimeField( 'When would you like to recieve this by?')
    priority= RadioField('Priority', choices=[('1','Just Curious'),('2',''),('3','Medium'),('4',''),('5','Top Priority')],coerce=unicode)
    requestedBy= TextField("If this isn't your request, who is it for?") 
 
class RequestLong(Form):
    shortForm = FormField(RequestShort)
    # deliveryFormat= TextField('Format for Delivery', [validators.Required(),validators.Length(min=2, max=50)] ) 
    # start and end?
    timeframe= TextField('From what timeframe do you want data? .e.g. Most recent fiscal year. Most recent calendar year. etc.', [validators.Required(),validators.Length(min=2, max=50)] ) 
    timeBreakdown = TextField("what's the smallest increment of time you want to see the data. e.g. month, quarterly or annually.", [validators.Required(),validators.Length(min=2, max=50)] ) 
    specialPop= TextField('Are you interested in a Special Population? e.g. Foster kids or dissabled adults, etc.', [validators.Required(),validators.Length(min=2, max=50)] ) 
    typeOfService= TextField('Are there specific types of services you want? e.g. Crisis, Hospital, etc.', [validators.Required(),validators.Length(min=2, max=50)] ) 
    specialInstructions= TextField('Any special instructions?', [validators.Required(),validators.Length(min=2, max=50)] ) 
    specialFacts= TextAreaField('Are there any facts or circumstances we should know to fulfil this request?') 
    submit=SubmitField('Submit')

class Staff(Form):
    assinged= TextField('Staff Assigned?') 
    completeDate= DateTimeField( 'Date Completed',  format='%c')
    reviewed= TextField('Reviewed by?') 
    submit=SubmitField('Submit')
