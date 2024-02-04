from flask import Flask, Response, jsonify, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required
from io import StringIO
from bs4 import BeautifulSoup
import requests
from requests import get
import csv
from datetime import datetime
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MY NAME IS EDDIE OGYNER'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://eddie:root@localhost/orion1'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

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
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        email = request.form['email']
        password = request.form['password1']

        if User.query.filter_by(email=email).first():
            flash('Email already exists!', category='error')
            return redirect(url_for('register'))

        if User.query.filter_by(email=email).first():
            flash('Email already in use!', category='error')
            return redirect(url_for('register'))

        user = User(first_name=first_name, last_name=last_name, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        flash('Registration Successful!', category='success')
        login_user(user)
        return redirect(url_for('login'))
    return render_template('register.html')

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('dashboard'))
        elif not User.query.filter_by(email=email).first():
            flash('User not registered!', category='error')
            return redirect(url_for('login'))
        else:
            flash('Invalid Email or Password!', category='error')
            return redirect(url_for('login'))
    return render_template('login.html')

# User Dashboard
@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.is_authenticated:
        logged_in_email = current_user.email
    else:
        logged_in_email = None

    return render_template('dashboard.html', email=logged_in_email)

# Fetching/rendering scraping details, parameters, and data
@app.route('/scrape', methods=['GET', 'POST'])
@login_required
def scrape():
    target_url = request.form['target_url']
    parent_tag = request.form['parent_element']
    desired_elements = request.form['desired_elements'].split(',')

    extracted_data = {}  # Initialize extracted_data as an empty dictionary
    
    try:
        extracted_data = scrape_website(target_url, parent_tag, desired_elements)
        
        # Check if extracted_data is empty
        if not extracted_data:
            flash('No data extracted. Please check your scraping parameters and try again.', category='alert alert-info alert-dismissable fade show')
        
        scraped_items = ScrapedItem(target_url=target_url, user=current_user)
        db.session.add(scraped_items)
        db.session.commit()
            
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            flash('URL not found. Please check the URL and try again.', category='alert alert-danger alert-dismissable fade show')
    except requests.exceptions.RequestException:
        flash('Invalid URL or network error. Please try again.', category='alert alert-danger alert-dismissable fade show')
    except Exception as e:
        flash('Unexpected error occurred during scraping. Please try again.', category='alert alert-danger alert-dismissable fade show')

    return render_template('dashboard.html', extracted_data=extracted_data, scraped_data=current_user.scraped_items)

#Scraping
def scrape_website(target_url, parent_tag, desired_elements):
    try:
        response = requests.get(target_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        raise

    soup = BeautifulSoup(response.content, 'html.parser')

    extracted_data = {}

    parent_elements = soup.find_all(parent_tag)

    for parent_element in parent_elements:
        for element_selector in desired_elements:
            element_data = parent_element.select(element_selector)

            if element_data:
                # If the key doesn't exist in extracted_data, create it
                if element_selector not in extracted_data:
                    extracted_data[element_selector] = []

                # Append the text content of all matching elements to the list
                extracted_data[element_selector].extend([item.text for item in element_data])

    print("Extracted data:", extracted_data)
    return extracted_data

# Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# Update account
@app.route('/update_account', methods=['POST'])
def update_account():
    # Get the form data
    form_data = request.form.to_dict()

    # Check if user exists
    existing_user = User.query.filter_by(email=form_data.get('email', None)).first()

    # Check if email address has changed
    if existing_user and existing_user.id != current_user.id:
        return jsonify({'success': False, 'error': 'Email address already exists'})

    # Update user information
    for key, value in form_data.items():
        if key in ('first_name', 'last_name', 'email', 'password'):
            setattr(current_user, key, value)

    # Commit changes to the database
    db.session.commit()

    return jsonify({'success': True})

# Delete account
@app.route('/delete_account', methods=['POST'])
@login_required
def delete_account():
    email = current_user.email

    # Check if user exists
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'success': False, 'error': 'User not found'})

    # Delete user from the database
    db.session.delete(user)
    db.session.commit()

    return jsonify({'success': True})

# download csv file
@app.route('/download_csv', methods=['POST'])
def download_csv():
    csv_data = request.form.get('csv_data')

    # Parse the CSV data
    csv_rows = [row.split(',') for row in csv_data.strip().split('\n')]

    # Create a CSV file in-memory
    csv_file = StringIO()
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(csv_rows)

    # Create a response with the CSV file
    response = Response(csv_file.getvalue(), content_type='text/csv')
    response.headers["Content-Disposition"] = "attachment; filename=scraped_data.csv"

    return response

# Run the Flask Application
if __name__ == '__main__':
    app.run(debug=True)
