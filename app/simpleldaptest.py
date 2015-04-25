from flask import Flask
from flask.ext.simpleldap import LDAP

app = Flask(__name__)
ldap = LDAP(app)

app.config['LDAP_BASE_DN'] = 'cn=Users,DC=BHCS,DC=internal'
app.config['LDAP_USERNAME'] = 'cn=Users,DC=BHCS,DC=internal'
app.config['LDAP_PASSWORD'] = 'password'

@app.route('/ldap')
@ldap.login_required
def ldap_protected():
    return 'Success!'


# # add Flask-related imports before this point
# from flask.ext.login import LoginManager, login_user, UserMixin, \
#     login_required, logout_user, current_user
# from wtforms import Form, TextField, PasswordField, validators
# # simpleldap is way more convenient than python-ldap
# import simpleldap
# from flask import Flask, render_template, request, flash,redirect,url_for,jsonify
# # initialize the Flask app
# app = Flask(__name__)
# import ldap
# # initialize the login manager
# login_manager = LoginManager()
# login_manager.init_app(app)

# ldapsrv = 'ldap://10.129.18.101'
# basedn =  'cn=Users,DC=BHCS,DC=internal'

# app.secret_key = "welfhwdlhwdlfhwelfhwlehfwlehfelwehflwefwlehflwefhlwefhlewjfhwelfjhweflhweflhwel"

# def ldap_fetch(uid=None, name=None, passwd=None):
#     try:
#         if name is not None and passwd is not None:
# l = ldap.initialize("ldap://10.129.18.101")
# l.simple_bind_s("program\%s" % form.username.data,form.password.data)
# print "Authentification Successful"
# r=l.search_s('cn=Users,dc=BHCS,dc=Internal',ldap.SCOPE_SUBTREE,'(sAMAccountName=*%s*)' % aform.username.data,['mail'])
#         return email=r[0][1]['mail']
#     except:
#         return None


# class User(UserMixin):
#     def __init__(self, uid=None, name=None, passwd=None):

#         self.active = False

#         ldapres = ldap_fetch(uid=uid, name=name, passwd=passwd)

#         if ldapres is not None:
#             self.name = ldapres['name']
#             self.id = ldapres['id']
#             # assume that a disabled user belongs to group 404
#             if ldapres['gid'] != 404:
#                 self.active = True
#             self.gid = ldapres['gid']

#     def is_active(self):
#         return self.active

#     def get_id(self):
#         return self.id


# @login_manager.user_loader
# def load_user(userid):
#     return User(uid=userid)


# class LoginForm(Form):
#     username = TextField("Username", [validators.Length(min=2, max=25)])
#     password = PasswordField('Password', [validators.Required()])


# @app.route("/", methods=["GET", "POST"])
# def login():
#     form = LoginForm(request.form)
#     if request.method == 'POST' and form.validate():
#         user = User(name=form.username.data, passwd=form.password.data)
#         if user.active is not False:
#             login_user(user)
#             flash("Logged in successfully.")
#             return redirect(url_for("some_secret_page"))
#     print 'fail'
#     return render_template("login.html", form=form)


# @app.route("/logout", methods=["GET", "POST"])
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")