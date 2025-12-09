import logging

logger = logging.getLogger(__name__)


def add(a: int, b: int):
    logger.info(f"Calculating sum of {a} + {b}.")
    return a + b
