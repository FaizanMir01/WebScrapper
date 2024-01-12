import requests
from bs4 import BeautifulSoup
import re


def extract_urls(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text,'html.parser')

        # Find all anchor tags (a) with an href attribute
        links = soup.find_all('a', href=True)

        # Extract and print the URLs
        for link in links:
            print(link['href'])
    else:
        print(f"Error: {response.status_code}")


# Example usage
url_to_scrape = "https://website_url_here"
extract_urls(url_to_scrape)
