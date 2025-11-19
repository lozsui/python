import logging
import logging.config

"""
Dieses Skript zeigt:

- Konfiguration von zwei Logger.
- Damit Log-Meldungen bis zur Konsole kommen, braucht es den
  'logging.StreamHandler' (note-1).
- 'logger1' hat Level INFO. 'logger2' hat Level WARNING.
- Wegen unterschiedlichen Log-Levels verhalten sich die beiden logger
  unterschiedlich beim Aufruf der Methoden 'info' respektive 'warning'
  (note-2).
- Siehe auch 100_log_levels.py
"""


def print_logger_infos():
    """Print all known loggers"""
    logger_dict = logging.Logger.manager.loggerDict
    for name, obj in logger_dict.items():
        if isinstance(obj, logging.Logger):
            print(
                f"Logger Name: {name}, Level: {obj.level}, Disabled: {obj.disabled}, Parent: {obj.parent.name}"
            )


# Documentation: https://docs.python.org/3/library/logging.config.html#logging-config-dictschema
configuration_dict = {
    "version": 1,
    "handlers": {
        "default": {"class": "logging.StreamHandler"},  # note-1
    },
    "loggers": {
        "logger1": {
            "handlers": [
                "default",
            ],
            "level": "INFO",
        },
        "logger2": {
            "handlers": [
                "default",
            ],
            "level": "WARNING",
        },
    },
}


logging.config.dictConfig(configuration_dict)
"""
Auch wenn 'logger1 = logging.getLogger("logger1")' und
'logger2 = logging.getLogger("logger2")' noch nicht ausgeführt wurden,
sind logger1 und logger2 dem 'System' bekannt.
"""
print_logger_infos()

logger1 = logging.getLogger("logger1")
logger2 = logging.getLogger("logger2")

"""
@note-1:

Ohne Konfiguration eines StreamHandlers würden die Log-Meldungen
unten nicht bis auf die Konsole kommen.
"""
# note-2
logger1.info(f"Message from {logger1.name}")
logger2.info(f"""You won't see me since level is set to WARNING for {logger2.name}.""")
logger2.warning(f"Message from {logger2.name}")
