import argparse
import xml.etree.ElementTree as ET

"""
Run this script:

(.venv) PS C:\Temp\python> python -m ex002parse.parse_xml --help
python -m ex002parse.parse_xml --file=ex002parse/parse_xml.xml
"""

parser = argparse.ArgumentParser(description="Script to parse xml file")
parser.add_argument('--file', default='ex002parse/parse_xml.xml', help='Set path for file you want to parse.')

args = parser.parse_args()
file = args.file

tree = ET.parse(file)
root = tree.getroot()
print(f"Root tag: {root.tag}")

for book in root.findall('book'):
    title = book.find('title').text
    author = book.find('author').text
    year = book.find('year').text
    
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Year: {year}")
    print("----")