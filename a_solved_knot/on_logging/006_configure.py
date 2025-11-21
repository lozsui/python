"""
In diesem Skript werden Logging-Konfigurationen auf Code-Ebene gemacht.
"""

import logging

logger = logging.getLogger("logger1")
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
"""
note-1

Siehe auch https://docs.python.org/3/library/logging.html#logging-levels

Ändere auf DEBUG, INFO, WARNING, ERROR oder CRITICAL und gucke wie sich der
Output weiter unten (siehe note-2)
"""
ch.setLevel(logging.DEBUG)

# create formatter
# Exercise: Play with datefmt='%Y-%m-%d %H:%M:%S' and see changes in output
# https://docs.python.org/3/library/logging.html#formatter-objects
# https://docs.python.org/3/library/logging.html#logrecord-attributes
formatter = logging.Formatter(
    fmt="%(filename)s %(asctime)s - %(name)s - %(levelname)s - %(message)s - %(ip)s",
    datefmt="%Y-%m-%d %H:%M",
    style="%",
    defaults={"ip": None},
)

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# note-2 (output) ist abhängig von Log-Level unter 'note-1' weiter oben.
logger.debug("debug message", extra={"ip": "42.42.42.42"})
logger.info("info message")
logger.warning("warn message")
logger.error("error message")
logger.critical("critical message")
