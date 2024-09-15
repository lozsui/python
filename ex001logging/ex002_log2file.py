import logging
import argparse


parser = argparse.ArgumentParser(description="Script with dynamic logging level.")
parser.add_argument('--log', default='WARNING', help='Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)')

args = parser.parse_args()
loglevel = args.log

numeric_level = getattr(logging, loglevel.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % loglevel)

logger = logging.getLogger(__name__)
logging.basicConfig(filename='ex002_example.log', encoding='utf-8', level=numeric_level, filemode='w')

logger.debug('This message should got to the log file')
logger.info('So should this')
logger.warning('And this, too')
logger.error('And non-ASCII stuff, too, like Øresund and Malmö')
