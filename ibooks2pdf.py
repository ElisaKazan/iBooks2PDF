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
import subprocess

def main():

    dir = create_directory()
    run_ibooks()


def run_ibooks():
    subprocess.check_call(["/usr/bin/open", "-n", "-a", "/Applications/iBooks.app", "/Users/elisakazan/Library/Containers/com.apple.BKAgentService/Data/Documents/iBooks/Books/902018641.ibooks"])

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

    return directory

if __name__ == '__main__':
    main()
