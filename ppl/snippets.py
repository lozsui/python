# -*- coding: utf-8 -*-

"""
Snippets I came across.
"""


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
    return no_of_sentences


def get_metadata_from_image(fh):
    # https://stackoverflow.com/questions/21697645/how-to-extract-metadata-from-a-image-using-python
    return None