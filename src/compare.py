import requests
from bs4 import BeautifulSoup

# Define our scrape function to get dimensions from given url
# For now, this code will only take one url and print the dimensions
def scrapeProducts(url):
    # Request url data
    response = requests.get(url)
    htmlData = response.content
    # Verify that the response was succesful and parse data
    if response.status_code == 200:
        parsedData = BeautifulSoup(htmlData, "html.parser")
    


