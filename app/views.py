from flask import render_template, flash, redirect,Flask,Response,request,url_for, g
from app import app,models, db
from flask.ext.login import LoginManager, UserMixin, login_required, current_user, login_user, logout_user
from forms import LoginForm, RequestShort,RequestLong,Which
import ldap


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
    flash("Logged Out.")
    return redirect(url_for("login"))

@app.route("/",methods=["GET"])
@app.route("/index",methods=["GET"])
def index():
    return Response(response="Hello World!",status=200)


@app.route("/start",methods=["GET","POST"])
@login_required
def start():
    form = Which()
    if form.validate_on_submit():
        # import pdb;pdb.set_trace()
        print form.formtype.data
        if form.formtype.data==u"Short":
            print 'True short'
            return redirect(url_for("short",))
        else:
            print 'True long'
            return redirect(url_for("long",))
    return render_template("start.html",email=g.user.email,name=g.user.name,form=form)

@app.route("/short",methods=["GET","POST"])
@login_required
def short():
    form = RequestShort()
    # import pdb;pdb.set_trace()
    if form.validate_on_submit():
      print 'submit'
      # import pdb;pdb.set_trace()
    return render_template("short.html",email=g.user.email,name=g.user.name,form=form)

@app.route("/long",methods=["GET","POST"])
@login_required
def long():
    form = RequestLong()
    if form.validate_on_submit():
      print 'submit'
      # import pdb;pdb.set_trace()
    return render_template("long.html",email=g.user.email,name=g.user.name,form=form)

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
            return redirect(request.args.get("next") or url_for("start"))
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