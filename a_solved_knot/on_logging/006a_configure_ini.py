import logging
import logging.config

logging.config.fileConfig('006a_configure_2.conf')

# create logger
logger = logging.getLogger('Random-Name-fits-here')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
