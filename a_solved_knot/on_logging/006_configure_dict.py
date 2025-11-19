import logging
import logging.config

configuration_dict = {
    "version": 1,
    "disable_existing_loggers": False,  # note-1
    "filters": {
        "correlation_id": {
            "()": "asgi_correlation_id.CorrelationIdFilter",
            "uuid_length": 32,
            "default_value": "-",
        }
    },
    "formatters": {
        "json": {  # JSON-Formatter für Konsole und Datei
            "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "datefmt": "%Y-%m-%dT:%H:%M:%S",
            "format": "%(asctime)s.%(msecs)03d %(levelname)-8s %(correlation_id)s %(name)s %(lineno)d %(message)s",
        },
    },
    "handlers": {
        "default": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "json",  # JSON-Formatter verwenden
            "filters": ["correlation_id"],
        },
        "rotating_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "json",  # JSON-Formatter verwenden
            "filename": "lfpapi.log",
            "maxBytes": 1024 * 1024,  # 1MB
            "backupCount": 2,
            "encoding": "utf8",
            "filters": ["correlation_id"],
        },
    },
    "loggers": {
        "logger1": {"handlers": ["default", "rotating_file"], "level": "INFO"},
        "logger2": {
            "handlers": ["default", "rotating_file"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}


def print_logger_infos():
    """Print all known loggers"""
    logger_dict = logging.Logger.manager.loggerDict
    for name, obj in logger_dict.items():
        if isinstance(obj, logging.Logger):
            print(f"Logger Name: {name}, Level: {obj.level}, Disabled: {obj.disabled}")


logger = logging.getLogger("My Logger")

logging.config.dictConfig(configuration_dict)
print_logger_infos()

"""
@note-1:

Man kann hier von True auf False wechseln oder umgekehrt. Die Ausgabe von
print_logger_infos() wechselt entsprechend von beispielsweise
'Logger Name: My Logger, Level: 0, Disabled: True' auf
'Logger Name: My Logger, Level: 0, Disabled: False' oder umgekehrt.
"""
