from flask import render_template, flash, redirect,Flask,Response,request,url_for, g,session
from app import app,models, db
from flask.ext.login import LoginManager, UserMixin, login_required, current_user, login_user, logout_user
from forms import LoginForm, Request, Which
import ldap
import datetime

login_manager = LoginManager()
login_manager.init_app(app) 
# login_manager.session_protection = None
#login_managerlogin_view = 'login'

# class User(UserMixin):
#   def __init__(self, name, id, active=True):
#     self.name = name
#     self.id = id
#     self.active = active 

#   def is_authenticated(self):
#       return True

#   def is_active(self):
#     return self.active   

# USERS = {
# 1: User(u"Notch", 1),
# u'92bce19df203964b9dbbe7911f074e86': User(u"Chet", u'92bce19df203964b9dbbe7911f074e86'),
# 4: User(u"Stevex", 4),
# 3: User(u"Creeper", 3, False),
# u'seven': User(u'Bob',u'seven')
# } 
            # p=models.Projects(name=pform.project.data,projectleader=pform.projectleader.data)
            # db.session.add(p)
            # db.session.commit()

# @login_manager.user_loader
# def load_user(id):
#   # import pdb;pdb.set_trace()
#   x=models.User.query.filter_by(id=(id)).first() 
#   return x

@login_manager.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve
    """
    g.user=current_user
    return models.User.query.get(user_id)


@app.route("/logout")
# @login_required
def logout():
    logout_user()
    session.pop('logged_in', None)
    flash("Logged Out.")
    # import pdb;pdb.set_trace()
    return redirect(url_for("login"))


@app.route("/pickaform",methods=["GET","POST"])
@login_required
def pickaform():
    form = Which()
    if form.validate_on_submit():
        # import pdb;pdb.set_trace()
        print form.formtype.data
        if form.formtype.data==u"Short":
            WHICH=1
        else:
            WHICH=2
        return redirect(url_for("requestform",WHICH=WHICH))
    return render_template("start.html",email=g.user.email,name=g.user.name,form=form,)


@app.route("/requests",methods=["GET","POST"])
@login_required
def requests():
    requestlist=models.Request.query.all()
    return render_template("requests.html",email=g.user.email,name=g.user.name,requestlist=requestlist)

@app.route("/followup",methods=["GET","POST"])
@login_required
def followup():
    # import pdb;pdb.set_trace()
    requestlist= models.Request.query.filter_by(email=g.user.email).all() 
    return render_template("followup.html",email=g.user.email,name=g.user.name,requestlist=requestlist)

    
@app.route("/requestform/<WHICH>",methods=["GET","POST"])
@login_required
def requestform(WHICH):
    form = Request()
    # import pdb;pdb.set_trace()
    if form.validate_on_submit():
      print 'submit'
      # import pdb;pdb.set_trace()
      p=models.Request(email=g.user.email,username=g.user.name,jobTitle=form.jobTitle.data,deadlinedate=form.deadlinedate.data,emanio=form.emanio.data,MHorSUD=form.MHorSUD.data,
        keyQuestions=form.keyQuestions.data, problem=form.problem.data,specialFacts=form.specialFacts.data,requestedBy=form.requestedBy.data, priority=form.priority.data,
        timeframe=form.timeframe.data,timeBreakdown=form.timeBreakdown.data,specialPop=form.specialPop.data,agency=form.agency.data,ru=form.ru.data,
         specialInstructions=form.specialInstructions.data, typeOfService=form.typeOfService.data, timeframestart=form.timeframestart.data, timeframeend=form.timeframeend.data, 
         longDescription=form.longDescription.data, requestDate=datetime.datetime.utcnow(),
         audience=form.audience.data,  columnsRequired=form.columnsRequired.data, deadlinetime=form.deadlinetime.data, deadlineWhy=form.deadlineWhy.data)
      db.session.add(p)
      db.session.commit()
      return redirect(url_for('followup'))
    else:
        flash('validation fail')
    if WHICH=='1':
        print 'short!!'
        return render_template("short.html",email=g.user.email,name=g.user.name,form=form)
    else:
        return render_template("long.html",email=g.user.email,name=g.user.name,form=form)

@app.route("/request/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            l = ldap.initialize("ldap://10.129.18.101")
            l.simple_bind_s("program\%s" % form.username.data,form.password.data)
            print "Authentification Successful"
            r=l.search_s('cn=Users,dc=BHCS,dc=Internal',ldap.SCOPE_SUBTREE,'(sAMAccountName=*%s*)' % form.username.data,['mail','objectGUID','displayName'])
            email=r[0][1]['mail'][0]   
            print email
            GUID=r[0][1]['objectGUID'][0]   
            FullName=r[0][1]['displayName'][0] 
            import uuid
            guid = uuid.UUID(bytes=GUID)
            print form.remember_me.data
            # g.user = current_user
            if not models.User.query.filter_by(email=unicode(email)).first(): 
              p=models.User(name=FullName,email=email)
              db.session.add(p)
              db.session.commit()            
            login_user(user_loader(unicode(email)),remember=form.remember_me.data)
            flash("Logged in successfully.")
            g.email=email
            session['logged_in'] = True
            # import pdb;pdb.set_trace()
            return redirect(request.args.get("next") or url_for("pickaform"))
        except Exception as e:
            flash("Invalid Credentials.")
            return render_template("login.html", form=form)
    return render_template("login.html", form=form)
# USERS.get('\x92\xbc\xe1\x9d\xf2\x03\x96K\x9d\xbb\xe7\x91\x1f\x07N\x86')
# @app.route('/')
# def index():
#     user = {'nickname': 'Chet'}  # fake user
#     return render_template('index.html',
#                            title='Home',
#                            user=user)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         flash('Login requested for OpenID="%s", remember_me=%s' %
#               (form.openid.data, str(form.remember_me.data)))
#         return redirect('/index')
#     return render_template('login.html', 
#                            title='Sign In',
#                            form=form)
