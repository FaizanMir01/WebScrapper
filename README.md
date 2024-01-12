# WebScrapper
This Python script is a web scraping tool designed to extract and print URLs from a given web page. The script uses the requests library to send a GET request to the specified URL and checks if the request is successful (status code 200). If successful, it uses BeautifulSoup, a Python library for pulling data out of HTML and XML files, to parse the HTML content of the page.

The script then searches for all anchor tags (<a>) with an href attribute (i.e., links) and extracts and prints the URLs. If there is an error with the request (status code other than 200), it prints an error message indicating the status code.
