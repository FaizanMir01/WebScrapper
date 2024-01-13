# Web Scraper with Python

This Python script is a simple web scraper that extracts and prints URLs from a specified webpage. It utilizes the `requests` library for making HTTP requests and the `BeautifulSoup` library for parsing HTML content.

## Import Libraries

- **requests:** Allows the script to send HTTP requests.
- **BeautifulSoup:** A library for pulling data out of HTML and XML files.

## Function Definition: `extract_urls`

### Parameters:

- `url:` The starting URL to scrape.
- `depth:` Current depth level in the recursion (default is 1).
- `max_depth:` Maximum depth to explore (default is 3).

