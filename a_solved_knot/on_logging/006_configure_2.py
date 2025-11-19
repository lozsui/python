import logging
import logging.config

"""
Skript baut auf 006_configure_0.py auf. Siehe Kommentare A, B und C unten.

Siehe auch 006_configure_dict.py wie der Filter
'asgi_correlation_id.CorrelationIdFilter' eingebunden werden kann.
"""


# A: Define class ImportantFilter
class ImportantFilter(logging.Filter):
    def filter(self, record):
        # Only log messages that contain the keyword "IMPORTANT"
        return "IMPORTANT" in record.getMessage()


# Documentation: https://docs.python.org/3/library/logging.config.html#logging-config-dictschema
configuration_dict = {
    "version": 1,
    "filters": {
        # B: Make 'ImportantFilter' known as 'important_only'. Note: If it is
        # not defined in same script try to do something like
        # ' "filters_module.ImportantFilter" '.
        "important_only": {
            "()": ImportantFilter,
        },
    },
    "handlers": {
        # C: Make default handler use 'important_only'.
        "default": {
            "class": "logging.StreamHandler",
            "filters": ["important_only"],
        },
    },
    "loggers": {
        "logger1": {
            "handlers": [
                "default",
            ],
            "level": "INFO",
        },
    },
}


logging.config.dictConfig(configuration_dict)
logger1 = logging.getLogger("logger1")

logger1.info("Magic word is missing.")
logger1.info("Magic word is not important.")
logger1.info("Magic word is IMPORTANT (in capital letters).")
