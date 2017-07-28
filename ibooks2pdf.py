"""
iBooks2PDF
Created by Elisa Kazan
July 2017

Description:
<TBD>

Run Script:
python ibooks2pdf.py

"""

# Imports
import sys
import os

def main():
    create_directory()


def create_directory():
    """
    Description:
        TBD
    Parameters:
        TBD
    Return:
        TBD
    """
    directory = "book-screenshots"

    if not os.path.exists(directory):
        os.makedirs(directory)
        print("Directory created")
    else:
        print("Directory exists")

if __name__ == '__main__':
    main()
