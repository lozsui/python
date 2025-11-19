"""
Dieses Skript zeigt wie die Logging-Konfiguration aus einer yaml-Datei aus-
gelesen werden kann. Im Beispiel hier wir die Konfiguration aus
006b_configure_yaml.yaml ausgelesen.
"""

import logging
import logging.config

import yaml

with open("006b_configure_yaml.yaml", "r") as f:
    config = yaml.safe_load(f)
logging.config.dictConfig(config)

logger = logging.getLogger("logger1")

# For log levels to choose from see
# https://docs.python.org/3/library/logging.html#logging-levels
logger.debug("debug message")
logger.info("info message")
logger.warning("warn message")
logger.error("error message")
logger.critical("critical message")
logger.critical("critical message")
