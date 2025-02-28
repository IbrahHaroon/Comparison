import compare
import os
from compare import scrapeProducts
from graph import plot_voxels_matplotlib

# Main program
if __name__ == "__main__":
    # Specify the path to the HTML file
    filePath = os.path.join(os.path.dirname(__file__), "tests", "dummyProduct1.html")
    # Call the scrapeProducts function from compare.py
    x, y, z = compare.scrapeProducts(filePath)
    plot_voxels_matplotlib(x, y, z)