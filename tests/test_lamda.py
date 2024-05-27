"""
Inspired by https://github.com/PacktPublishing/The-Complete-Python-Course/tree/master/2_intro_to_python/lectures
"""

def test_lambda():
    average = lambda x: sum(x) / len(x)
    assert 2.5 == average([1, 2, 3, 4])