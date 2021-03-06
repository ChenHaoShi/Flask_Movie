import pymysql
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
from flask_redis import FlaskRedis
import os

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/movie'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = '41fdcc3fe2b44557af31a6ed5cfff630'
app.config["REDIS_URL"] = "redis://localhost:6379/0"
app.config['UP_DIR'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/")
app.config['FC_DIR'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/users/")
db = SQLAlchemy(app)
rd = FlaskRedis(app)

from .home import home as home_blueprint
from .admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('home/404.html'), 404