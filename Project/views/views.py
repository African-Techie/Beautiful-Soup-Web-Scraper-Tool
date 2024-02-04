from flask import render_template
from models import ScrapedData
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required

from flask import Flask, request
app = Flask(__name__)

@app.route('./dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

def scrape():
    target_url = request.form['target_url']
    desired_elements = request.form['desired_elements'].split(',')

    extracted_data = None

    try:
        extracted_data = scrape_website(target_url, desired_elements)
    except requests.exceptions.RequestException:
        flash('Invalid URL or network error. Please try again.')
    except requests.exceptions.HTTPError as e:
        if e.status_code == 404:
            flash('URL not found. Please check the URL and try again.')
        else:
            flash('Error retrieving website content. Please try again.')
    except Exception as e:
        flash('Unexpected error occurred during scraping. Please try again.')

    return render_template('dashboard.html', extracted_data=extracted_data)


# User Dashboard
@app.route('./dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

# Home Page
@app.route('./')
def index():
    return render_template('index.html')


# Logout
@app.route('./logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

