from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask.ext.script import Manager
# from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.login import LoginManager, UserMixin, login_required

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# migrate = Migrate(app, db)
# manager = Manager(app)
# manager.add_command('db', MigrateCommand)

Bootstrap(app)
app.config["SECRET_KEY"] = "ITSASECRET"


from app import views, models

