import pytest


class Answer:

    def __init__(self):
        self.answer = 42
        self.__answer = 42
        self._answer = 42
    
    @property
    def answerrrr(self):
        return self.__answer

def test_no_name_mangling_1():
    assert 42 == Answer().answer

def test_no_name_mangling_2():
    assert 42 == Answer()._answer

def test_name_mangling():
    assert 42 == Answer()._Answer__answer

def test_answer_private():
    with pytest.raises(AttributeError):
        Answer().__answer

def test_answer():
    """
    With property decorator can make a otherwise
    private attribute a public attribute. In this
    example I am calling it answerrrr since answer is
    already publicly available.
    """
    assert 42 == Answer().answerrrr



