import xml.etree.ElementTree as ET
from pathlib import Path

def test_parse_my_library():
    here = Path(__file__).parent
    file = here / 'library.xml'

    tree = ET.parse(file)
    root = tree.getroot()
    print(f"Root tag: {root.tag}")

    for book in root.findall('book'):
        title = book.find('title').text
        author = book.find('author').text
        year = book.find('year').text
        
        assert title in ['Python Programming', 'Machine Learning']
        assert author in ['John Doe', 'Jane Smith']
        assert year in ['2020', '2019']
