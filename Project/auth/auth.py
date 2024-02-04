import dbm
from flask import app, flash, redirect, render_template, url_for, request
from flask_login import login_user, login_required, logout_user
from models import User, ScrapedData
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        email = request.form['email']
        password = request.form['password1']

        if User.query.filter_by(email=email).first():
            flash('email already exists!')
            return redirect(url_for('register'))

        if User.query.filter_by(email=email).first():
            flash('Email already in use!')
            return redirect(url_for('register'))

        user = User(first_name=first_name, last_name=last_name, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        flash('Registration Successful!')
        login_user(user)
        return redirect(url_for('dashboard'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password!')
            return redirect(url_for('login'))
    return render_template('login.html')


