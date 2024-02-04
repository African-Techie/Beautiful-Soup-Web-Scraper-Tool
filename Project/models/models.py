from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import JSON
from sqlalchemy import JSON

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)


class ScrapedData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    target_url = db.Column(db.String(255), nullable=False)
    extracted_data = db.Column(JSON, nullable=False)
