import logging

"""
The format of the datefmt argument is the same as supported by
https://docs.python.org/3/library/time.html#time.strftime
"""
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
logging.warning('is when this event was logged.')
