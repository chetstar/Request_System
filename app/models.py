from app import db
from flask.ext.login import LoginManager, UserMixin
import datetime
 # class User(db.Model, UserMixin):
 #  name = db.Column(db.String(64), index=True)
 #  email = db.Column(db.String(120), index=True, unique=True)
 #  id = db.Column(db.String(120), index=True, unique=True)


 #  def __init__(self, name, id, active=True):
 #    self.name = name
 #    self.id = id
 #    self.active = active 

 #  def is_authenticated(self):
 #    return True

 #  def is_active(self):
 #    return self.active  
class User(db.Model):
    """An admin user capable of viewing reports.

    :param str email: email address of user
    :param str password: encrypted password for the user

    """
    __tablename__ = 'user'

    name=db.Column(db.String)
    email = db.Column(db.String, primary_key=True)
    authenticated = db.Column(db.Boolean, default=True)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False


class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True)
    emanio= db.Column(db.Integer)
    MHorSUD= db.Column(db.String(64), index=True)
    keyQuestions= db.Column(db.String(64), index=True)
    problem= db.Column(db.String(64), index=True)
    specialFacts= db.Column(db.String(64), index=True)
    requestDate= db.Column(db.DateTime, default=datetime.datetime.utcnow)
    requestDeadlineLapse= db.Column(db.Integer)
    requestedBy= db.Column(db.String(64), index=True)
    deadlinedate= db.Column(db.Date)
    priority= db.Column(db.String(64), index=True)
    deliveryFormat= db.Column(db.String(64), index=True)
    timeframe= db.Column(db.String(64), index=True)
    timeBreakdown= db.Column(db.String(64), index=True)
    specialPop= db.Column(db.String(64), index=True)
    agency= db.Column(db.String(64), index=True)
    ru = db.Column(db.String(64), index=True)
    typeOfService= db.Column(db.String(64), index=True)
    jobTitle= db.Column(db.String(64), index=True)
    longDescription= db.Column(db.String(64), index=True)
    specialInstructions= db.Column(db.String(64), index=True)
    audience= db.Column(db.String(64), index=True)
    columnsRequired= db.Column(db.String(64), index=True)
    assinged= db.Column(db.String(64), index=True)
    completeDate= db.Column(db.Date)
    reviewed= db.Column(db.String(64), index=True)
    userCategory= db.Column(db.String(64), index=True)


    def __repr__(self):
        return '<%r>' % (self.jobTitle)
