import pytest

"""
Der Sinn von Testklassen erschliesst sich mit noch nicht ganz.
Brian Okken sagt dazu: "Test classes are a way to group tests
that make sense to be grouped together."

Wie ausführen?

(.venv) PS C:\GIT\github\python\learnpytest> pytest .\test_class_level_marker.py::TestClassLevelMarker
(.venv) PS C:\GIT\github\python\learnpytest> pytest .\test_class_level_marker.py::TestClassLevelMarker::test_one
"""

@pytest.mark.smoke
class TestClassLevelMarker:
    def test_one(self):
        assert True


    def test_two(self):
        assert True
