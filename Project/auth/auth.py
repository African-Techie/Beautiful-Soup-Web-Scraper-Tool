from flask import Blueprint, flash, redirect, render_template, url_for, request
from flask_login import login_user, login_required, logout_user, current_user
from project.models import User
from project import db, login_manager

auth_bp = Blueprint('auth', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#register route
@auth_bp.route('/register', methods=['GET', 'POST'])
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

#login route
@auth_bp.route('/login', methods=['GET', 'POST'])
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

#logout route
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# Update account route
@auth_bp.route('/update_account', methods=['POST'])
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
@auth_bp.route('/delete_account', methods=['POST'])
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
@auth_bp.route('/download_csv', methods=['POST'])
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
