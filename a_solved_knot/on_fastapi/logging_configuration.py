from logging.config import dictConfig

from configuration import DevConfig


def configure_logging(config) -> None:
    # https://docs.python.org/3/library/logging.config.html#logging-config-api
    # https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig
    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "filters": {
                "correlation_id": {
                    "()": "asgi_correlation_id.CorrelationIdFilter",
                    "uuid_length": config.UUID_LENGTH,
                    "default_value": "-",
                }
            },
            "formatters": {
                "json": {
                    "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
                    "datefmt": "%Y-%m-%dT:%H:%M:%S",
                    "format": "%(asctime)s.%(msecs)03d %(levelname)s %(correlation_id)s %(name)s %(lineno)d %(message)s",
                },
                "simple_formatter": {
                    "class": "logging.Formatter",
                    "format": "%(asctime)s.%(msecs)03d %(levelname)s %(correlation_id)s %(name)s %(lineno)d %(message)s",
                    "datefmt": "%Y-%m-%dT:%H:%M:%S",
                },
            },
            "handlers": {
                "default": {
                    "class": "logging.StreamHandler",
                    "level": "DEBUG",
                    "formatter": "simple_formatter",
                    "filters": ["correlation_id"],
                },
                "rotating_file": {
                    "class": "logging.handlers.RotatingFileHandler",
                    "level": "DEBUG",
                    "formatter": "json",
                    "filename": "on_fastapi.log",
                    "maxBytes": 1024 * 1024,  # 1MB
                    "backupCount": 2,
                    "encoding": "utf8",
                    "filters": ["correlation_id"],
                },
            },
            "loggers": {
                "uvicorn": {"handlers": ["default", "rotating_file"], "level": "INFO"},
                "calculator": {
                    "handlers": ["default", "rotating_file"],
                    "level": "DEBUG" if isinstance(config, DevConfig) else "INFO",
                    "propagate": False,
                },
            },
            "root": {
                "handlers": ["default", "rotating_file"],
                "level": "INFO",
            }
        }
    )
