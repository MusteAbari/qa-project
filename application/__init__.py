from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@35.246.60.242:3306/projectdb"
app.config["SECRET_KEY"] = 'privateproject'

db = SQLAlchemy(app)

from application import routes
