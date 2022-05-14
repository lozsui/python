# -*- coding: utf-8 -*-

"""
Snippets I came across.
"""

from PIL import Image
from bs4 import BeautifulSoup



def count_words(text):
    tokens = text.split()
    counter = 0
    for i in tokens:
        # try to ignore things like ,.:;
        if len(i)> 1:
            # print i
            counter += 1
    return counter


def count_sentences(text):
    """
    Hints for improvement
    - Last element in the splitted text is no sentence => minus 1 form no_of_sentences
    """
    splitted_by_full_stop = text.split(".")
    print("")
    for sentence in splitted_by_full_stop:
        print("sentence: " + sentence)
    no_of_sentences = len(splitted_by_full_stop)
    return no_of_sentences - 1


def get_metadata_from_image(file):
    with Image.open(file) as im:
        print(im.info)
        print(im.mode)
        print(im.format)
        print(im.format_description)
        print(im.im)
        print(im.palette)
        print(im.pyaccess)
        print(im.readonly)


def parse_html(file):
    with open(file, "r") as fh:
        html = fh.read()
        soup = BeautifulSoup(html, 'html.parser')
        for tr in soup.find_all("tr"):
            line = ""
            counter = 0
            for td in tr:
                counter += 1
                # print(counter)
                if counter in [1, 3]:
                    line = line + "|" + td.getText()
                # print(td.getText())
            print(line + "|")


