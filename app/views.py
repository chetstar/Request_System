from flask import render_template, flash, redirect,Flask,Response,request,url_for, g
from app import app
from flask.ext.login import LoginManager, UserMixin, login_required, current_user, login_user, logout_user
from forms import LoginForm, validators
import ldap


login_manager = LoginManager()
login_manager.init_app(app) 
# login_manager.session_protection = None
#login_managerlogin_view = 'login'

class User(UserMixin):
  def __init__(self, name, id, active=True):
    self.name = name
    self.id = id
    self.active = active 

  def is_authenticated(self):
      return True

  def is_active(self):
    return self.active   

USERS = {
1: User(u"Notch", 1),
u'92bce19df203964b9dbbe7911f074e86': User(u"Chet", u'92bce19df203964b9dbbe7911f074e86'),
4: User(u"Stevex", 4),
3: User(u"Creeper", 3, False),
u'seven': User(u'Bob',u'seven')
} 


@login_manager.user_loader
def load_user(id):
  print 'during the load_user'
  print USERS.get(((id)) )
  return USERS.get(((id)) )

@app.route("/logout")
# @login_required
def logout():
    logout_user()
    flash("Logged Out.")
    return redirect(url_for("login"))

@app.route("/",methods=["GET"])
@app.route("/index",methods=["GET"])
def index():
    return Response(response="Hello World!",status=200)


@app.route("/start",methods=["GET"])
@login_required
def start():
    return render_template("start.html",
      email=request.args.get('email'), FullName=request.args.get('FullName'))

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            l = ldap.initialize("ldap://10.129.18.101")
            l.simple_bind_s("program\%s" % form.username.data,form.password.data)
            print "Authentification Successful"
            r=l.search_s('cn=Users,dc=BHCS,dc=Internal',ldap.SCOPE_SUBTREE,'(sAMAccountName=*%s*)' % form.username.data,['mail','objectGUID','displayName'])
            email=r[0][1]['mail'][0]   
            GUID=r[0][1]['objectGUID'][0]   
            FullName=r[0][1]['displayName'][0] 
            import uuid
            guid = uuid.UUID(bytes=GUID)
            print form.remember_me.data
            import pdb;pdb.set_trace()
            login_user(User(FullName,unicode(guid.hex)),remember=form.remember_me.data)
            flash("Logged in successfully.")
            return redirect(request.args.get("next") or url_for("start",email=email,FullName=FullName))
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