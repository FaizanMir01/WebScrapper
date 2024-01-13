import requests
from bs4 import BeautifulSoup


def extract_urls(url, depth=1, max_depth=3):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all anchor tags (a) with an href attribute
        links = soup.find_all('a', href=True)

        # Extract and print the URLs
        for link in links:
            print(link['href'])

            # Check if depth is within the limit and if the link is an absolute URL
            if depth < max_depth and link['href'].startswith(('http://', 'https://')):
                # Recursively call extract_urls with the new URL
                extract_urls(link['href'], depth=depth + 1, max_depth=max_depth)
    else:
        print(f"Error: {response.status_code}")


# Example usage
url_to_scrape = "https://www.google.com"
max_depth_value = 1
extract_urls(url_to_scrape, max_depth=max_depth_value)