import pytest

@pytest.mark.smoke
class TestClassLevelMarker:
    def test_one(self):
        assert True


    def test_two(self):
        assert True
