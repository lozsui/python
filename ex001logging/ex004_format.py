import logging

"""
For details see https://docs.python.org/3/library/logging.html#logrecord-attributes
"""
logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)
logging.debug("This message should appear on the console")
logging.info("So should this")
logging.warning("And this, too")

"""
logging.basicConfig can only be called once per session to
configure the root logger.

If one attempts to call logging.basicConfig() again, it has no
effect unless the logging system is reinitialized.
"""
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(format="%(asctime)s %(message)s")
logging.warning("is when this event was logged.")
