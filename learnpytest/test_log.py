import logging


logger = logging.getLogger(__name__)

def process_data(data):
    if not data:
        logger.warning("No data provided!")
    else:
        logger.info("Processing data...")
    return len(data)

"""
captlog is a pytest fixture (--setup-show is your friend).

This example shows how a warning is captures.
"""
def test_capture_warning(caplog):
    with caplog.at_level(logging.WARNING):
        result = process_data([])
    
    assert result == 0
    assert "No data provided!" in caplog.text


"""
captlog is a pytest fixture (--setup-show is your friend).

This example shows how a info is captured.
"""
def test_capture_info(caplog):
    with caplog.at_level(logging.INFO):
        result = process_data([42])
    
    assert result == 1
    assert "Processing data..." in caplog.text