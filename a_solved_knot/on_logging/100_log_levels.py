import logging
import logging.config

# Documentation: https://docs.python.org/3/library/logging.config.html#logging-config-dictschema
configuration_dict = {
    "version": 1,
    "handlers": {
        "default": {"class": "logging.StreamHandler"},  # note-1
    },
    "loggers": {
        "NOTSET0": {
            "handlers": [
                "default",
            ],
            "level": "NOTSET",
        },
        "DEBUG10": {
            "handlers": [
                "default",
            ],
            "level": "DEBUG",
        },
        "INFO20": {
            "handlers": [
                "default",
            ],
            "level": "INFO",
        },
        "WARNING30": {
            "handlers": [
                "default",
            ],
            "level": "WARNING",
        },
        "ERROR40": {
            "handlers": [
                "default",
            ],
            "level": "ERROR",
        },
        "CRITICAL50": {
            "handlers": [
                "default",
            ],
            "level": "CRITICAL",
        },
    },
}

logging.config.dictConfig(configuration_dict)
logger_dict = logging.Logger.manager.loggerDict


def run_method_on_loggers(level: str):
    print(f"*** {level}")
    for name, obj in logger_dict.items():
        if isinstance(obj, logging.Logger):
            log_method = getattr(obj, level, None)
            log_method(f"Logger Name: {name}, log method is {level}")


message_methods = ["debug", "info", "warning", "error", "critical"]

for message_method in message_methods:
    run_method_on_loggers(message_method)

"""
Auf der Konsole sieht es dann so aus:

*** debug
Logger Name: DEBUG10, log method is debug
*** info
Logger Name: DEBUG10, log method is info
Logger Name: INFO20, log method is info
*** warning
Logger Name: NOTSET0, log method is warning
Logger Name: DEBUG10, log method is warning
Logger Name: INFO20, log method is warning
Logger Name: WARNING30, log method is warning
*** error
Logger Name: NOTSET0, log method is error
Logger Name: DEBUG10, log method is error
Logger Name: INFO20, log method is error
Logger Name: WARNING30, log method is error
Logger Name: ERROR40, log method is error
*** critical
Logger Name: NOTSET0, log method is critical
Logger Name: DEBUG10, log method is critical
Logger Name: INFO20, log method is critical
Logger Name: WARNING30, log method is critical
Logger Name: ERROR40, log method is critical
Logger Name: CRITICAL50, log method is critical
"""
