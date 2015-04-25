


from flask import Flask
from flask.ext.ldap import LDAP, login_required
app = Flask(__name__)
app.debug = True
app.config['LDAP_HOST'] = 'ldap://10.129.18.101'
app.config['LDAP_DOMAIN'] = 'program'
app.config['LDAP_SEARCH_BASE'] = 'cn=Users,DC=BHCS,DC=internal'
# app.config['LDAP_LOGIN_VIEW'] = 'custom_login'
app.config['LDAP_AUTH_VIEW'] = 'login'

ldap = LDAP(app)
app.secret_key = "welfhwdlhwdlfhwelfhwlehfwlehfelwehflwefwlehflwefhlwefhlewjfhwelfjhweflhweflhwel"
app.add_url_rule('/login', 'login', ldap.login, methods=['GET', 'POST'])

@app.route('/')
@login_required
def index():
    pass


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     pass

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")