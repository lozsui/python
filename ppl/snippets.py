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
    splitted_by_full_stop = text.split(".")
    print("")
    for sentence in splitted_by_full_stop:
        print("sentence: " + sentence)
    return len(splitted_by_full_stop)
