import os
import json


def test_read_json():
    test_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'files', 'test-read-json.json'))
    with open(test_file, "r") as fh:
        configuration = json.load(fh)
        assert isinstance(configuration, dict)
        assert configuration['environment'] == "development"
