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
195048015249884310307534473617759227526: User(u"Steve", 2),
4: User(u"Stevex", 4),
3: User(u"Creeper", 3, False),
} 


@login_manager.user_loader
def load_user(id):
  print 'during the load_user'
  print USERS.get(int((id)) )
  return USERS.get(int((id)) )


@app.route("/",methods=["GET"])
def index():
    return Response(response="Hello World!",status=200)


@app.route("/protected/",methods=["GET"])
@login_required
def protected():
    return Response(response="Hello Protected World!", status=200)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        l = ldap.initialize("ldap://10.129.18.101")
        l.simple_bind_s("program\%s" % form.username.data,form.password.data)
        print "Authentification Successful"
        r=l.search_s('cn=Users,dc=BHCS,dc=Internal',ldap.SCOPE_SUBTREE,'(sAMAccountName=*%s*)' % form.username.data,['mail','objectGUID'])
        email=r[0][1]['mail'][0]   
        GUID=r[0][1]['objectGUID'][0]    
        import uuid
        guid = uuid.UUID(bytes=GUID)
        print guid.int
        print USERS.get((guid.int))
        login_user(load_user(1),remember=True)
        import pdb;pdb.set_trace()
        flash("Logged in successfully.")
        return redirect(request.args.get("next") or url_for("protected"))
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