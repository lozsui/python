import logging
import logging.config
import yaml

with open('ex006_configure_2.yaml', 'r') as f:
    config = yaml.safe_load(f)
logging.config.dictConfig(config)

# create logger
logger = logging.getLogger('simpleExample')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
