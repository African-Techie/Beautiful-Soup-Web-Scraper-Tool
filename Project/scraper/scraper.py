from requests import get
from bs4 import BeautifulSoup
import requests
from flask import Flask
from flask import Blueprint, jsonify, Response, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from your_project import db
from your_project.models import ScrapedItem
from your_project.views.views import scrape_website

scraper_bp = Blueprint('scraper', __name__)

@scraper_bp.route('/scrape', methods=['GET', 'POST'])
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

    return render_template('./dashboard.html', extracted_data=extracted_data, scraped_data=current_user.scraped_items)

@scraper_bp.route('/scrape', methods=['POST'])
@login_required
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

