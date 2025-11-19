import logging
import logging.config

"""
Dieses Skript zeigt wie man Log-Messages in eine Datei ausgeben kann. Es baut
auf 006_configure_0.py auf. Siehe Kommentar zu configuration_dict was in
diesem Skript dazu kommt.
"""

# Documentation: https://docs.python.org/3/library/logging.config.html#logging-config-dictschema
"""
Unter 'handlers' wird der Handler 'rotating_file' eingeführt (siehe A). Unter
'B' wird der logger1 so konfiguriert, dass Log-Meldungen neu auch an den
Handler 'rotating_file' weitergegeben werden.
"""
configuration_dict = {
    "version": 1,
    "handlers": {
        "default": {"class": "logging.StreamHandler"},
        "rotating_file": {  # A
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "filename": "006_configure_1.log",
            "maxBytes": 1024 * 1024,  # 1MB
            "backupCount": 2,
            "encoding": "utf8",
        },
    },
    "loggers": {
        "logger1": {
            "handlers": ["default", "rotating_file"],  # B
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
logger1 = logging.getLogger("logger1")
logger2 = logging.getLogger("logger2")

logger1.info(f"Message from {logger1.name}")
logger2.info(f"""You won't see me since level is set to WARNING for {logger2.name}.""")
logger2.warning(f"Message from {logger2.name}")
