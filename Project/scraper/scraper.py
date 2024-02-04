from requests import get
from bs4 import BeautifulSoup
import requests
from flask import Flask
app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
@login_required

def scrape_website(target_url, desired_elements):
    response = requests.get(target_url)
    soup = BeautifulSoup(response.content, 'lxml')

    # Extract relevant data from the scraped webpage
    extracted_data = {}
    for element in desired_elements:
        try:
            extracted_data[element] = soup.select_one(element).text
        except Exception as e:
            # Handle element-specific errors
            pass

    return extracted_data
