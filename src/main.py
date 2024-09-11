import compare
import os


# Main program
if __name__ == "__main__":
    # Specify the path to the HTML file
    filePath = os.path.join(os.path.dirname(__file__), "tests", "dummyProduct1.html")
    # Call the scrapeProducts function from compare.py
    compare.scrapeProducts(filePath)