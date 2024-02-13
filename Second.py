import requests
from bs4 import BeautifulSoup
import openpyxl

def extract_urls(url, depth=1, max_depth=3, excel_filename='test1.xlsx'):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all anchor tags (a) with an href attribute
        links = soup.find_all('a', href=True)

        # Extract and store the URLs in an Excel file
        excel_file = openpyxl.Workbook()
        sheet = excel_file.active

        for link in links:
            url_to_store = link['href']

            # Check if the URL starts with 'http://' or 'https://'
            if url_to_store.startswith(('http://', 'https://')):
                # Print the URL to the console
                print(url_to_store)

                # Append the URL to the Excel sheet
                sheet.append([url_to_store])

                # Check if depth is within the limit
                if depth < max_depth:
                    # Recursively call extract_urls with the new URL
                    extract_urls(url_to_store, depth=depth + 1, max_depth=max_depth, excel_filename=excel_filename)

        # Save the Excel file
        excel_file.save(excel_filename)
        print(f"URLs saved to {excel_filename}")
    else:
        print(f"Error: {response.status_code}")

# Example usage
url_to_scrape = "https://kalasalingam.ac.in/"
max_depth_value = 1
extract_urls(url_to_scrape, max_depth=max_depth_value)
