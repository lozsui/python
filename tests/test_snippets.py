"""
No comment.
"""

import pytest
import os
import ppl.snippets


def test_word_count():
    os.chdir('../files')
    with open("word_count.txt", "r") as fh:
        assert ppl.snippets.count_words(fh.read()) == 100


def test_count_sentences():
    os.chdir('../files')
    with open("word_count.txt", "r") as fh:
        assert ppl.snippets.count_sentences(fh.read()) == 6


def test_get_metadata_from_image():
    os.chdir('../files')
    with open("test_metadata", "r") as fh:
        ppl.snippets.get_metadata_from_image(fh)
