from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from celery import Celery
from flask_caching import Cache

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = '57916998bb0b13ce0d676dfde280ba139'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = 'armansinghgrewal@gmail.com'
# app.config['MAIL_PASSWORD'] = 'qdqxuqfvfwqjvsgm'
# mail = Mail(app)

# app.config["CELERY_BROKER_URL"] = "redis://localhost:6379/1"
# app.config["CELERY_RESULT_BACKEND"] = "redis://localhost:6379/2"
# celery = Celery(app.name,broker=app.config["CELERY_BROKER_URL"],result_backend=app.config["CELERY_RESULT_BACKEND"])
# celery.conf.timezone = 'Asia/Kolkata'

# app.config["CACHE_TYPE"] = "redis"
# app.config["CACHE_REDIS_URL"] = "redis://localhost:6379/0"
# cache = Cache(app)

@app.route('/')
def print_hello():
    return 'Hello, Flask!'


@app.route("/userLogin", methods=['POST'])
def userLogin():
    pass

@app.route("/userSignup", methods=['POST'])
def userSignup():
    pass

if __name__ == '__main__':
    app.run(debug=True)