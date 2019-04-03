from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "password123"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://nathan:password123@localhost/hireme"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


app.config.from_object(__name__)
from app import views
