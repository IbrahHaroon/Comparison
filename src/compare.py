import requests
from bs4 import BeautifulSoup

# Plan to create user agent script

# Define our scrape function to get dimensions from given file path (for now)
# For now, this code will only take one url and print the dimensions
def scrapeProducts(file):
    # Open the file and  parse
    fileData = open(file, "r", encoding="utf-8")
    parsedData = BeautifulSoup(fileData, "html.parser")
    dimensions = parsedData.find(attrs={'class': 'product-dimensions'})
    if dimensions:
        print("Product dimensions: ", dimensions.get_text(strip=True))
    else:
        print("Dimensions not found.")
    fileData.close







# For our dummy product, the class name for dimensions is called "product-dimensions"
# For Microcenter, the class name for dimensions is called "spec-body"
# For Amazon, the class name for dimensions is called "a-size-base prodDetAttrValue"
