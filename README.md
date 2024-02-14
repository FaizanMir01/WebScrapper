# Web Scraper with Python

This Python script is a simple web scraper that extracts and prints URLs from a specified webpage. It utilizes the `requests` library for making HTTP requests and the `BeautifulSoup` library for parsing HTML content.
### 1. Main.py
Used to get urls from single Page
### 2. recursive.py
Recursively explores URLs up to a specified depth.\
### 3.second.py
This Python script extracts URLs from a given webpage up to a certain depth and stores them in an Excel file. Here's an explanation of how it works:

The script uses the requests library to send a GET request to a specified URL to fetch the webpage content.

If the request is successful (status code 200), the HTML content of the webpage is parsed using BeautifulSoup.

Using BeautifulSoup, all anchor tags (<a>) with an href attribute are extracted. These tags typically contain links to other webpages.

The script creates an Excel workbook using the openpyxl library and accesses the active sheet.

It iterates over each extracted link, checks if it starts with 'http://' or 'https://', and prints the URL to the console.

If the depth is within the specified limit (max_depth), the script recursively calls itself with the new URL, incrementing the depth by 1.

The URLs are appended to the Excel sheet.

Finally, the Excel file is saved with the provided filename, and a message is printed to indicate the successful completion of the process.

This script can be useful for web scraping tasks where you need to extract and analyze links from a webpage, such as building a sitemap or collecting data for further processing. Adjusting the max_depth parameter allows you to control the depth of the scraping, preventing infinite recursion.

### Vulnerable.py
this file will take the urls from xl sheet and check for sql injection vulnerablity using sql_map.

## Import Libraries

- **requests:** Allows the script to send HTTP requests.
- **BeautifulSoup:** A library for pulling data out of HTML and XML files.

## Function Definition: `extract_urls`

### Parameters:

- `url:` The starting URL to scrape.
- `depth:` Current depth level in the recursion (default is 1).
- `max_depth:` Maximum depth to explore (default is 3).

