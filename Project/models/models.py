from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

# User database model
class User(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

    scraped_items = relationship('ScrapedItem', backref='user', lazy=True, cascade='all, delete-orphan')
    def get_id(self):
        return str(self.user_id)

# Scraped Item database model
class ScrapedItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    target_url = db.Column(db.String(255), nullable=False)
    scrape_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    
