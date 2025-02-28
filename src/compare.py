import requests
from bs4 import BeautifulSoup
import os
from pathlib import Path
import re
from graph import plot_voxels_matplotlib

input_dir = Path.cwd()
target_directory = list(input_dir.rglob('dummyProduct1.html'))
if target_directory:
    file = open(target_directory[0], 'r')
    print('File found.')
else:
    print('File not found, exiting script.')
    exit()
# Plan to create user agent script


# Define our REGEX function to extract our dimensions from the dimensions string
def extract_dimensions(s):
    # Extract numbers from the string using regex
    numbers = re.findall(r"[-+]?\d*\.?\d+", s)
    
    # Convert them to float (to support decimal values)
    if len(numbers) >= 3:
        x, y, z = map(float, numbers[:3])
        return x, y, z
    else:
        raise ValueError("Invalid input format. Expected at least three numbers.")

# Define our scrape function to get dimensions from given file path (for now)
# For now, this code will only take one url and print the dimensions
# It will also return the dimensions in order to graph
def scrapeProducts(file):
    # Open the file and  parse
    parsedData = BeautifulSoup(file, "html.parser")
    dimensions = parsedData.find(attrs={'class': 'product-dimensions'})
    if dimensions:
        #print("Product dimensions: ", dimensions.get_text(strip=True))
        #return dimensions.get_text(strip=True)
        x, y, z = extract_dimensions(dimensions.get_text(strip=True))
        
        xr = int(round(x))
        yr = int(round(y))
        zr = int(round(z))
        print(xr, yr, zr)
        plot_voxels_matplotlib(xr, yr, zr)
        return xr, yr, zr

    else:
        print("Dimensions not found.")
    

scrapeProducts(file)






# For our dummy product, the class name for dimensions is called "product-dimensions"
# For Microcenter, the class name for dimensions is called "spec-body"
# For Amazon, the class name for dimensions is called "a-size-base prodDetAttrValue"
