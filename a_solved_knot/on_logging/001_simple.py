import logging

"""
Wenn man 'logging.basicConfig(level=logging.INFO)' nicht schreibt,
wird nur die WARNING unten ausgegeben.
"""
logging.basicConfig(level=logging.INFO)

logging.warning('Watch out!')
logging.info('I told you so')
