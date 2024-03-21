import logging

from pythonjsonlogger import jsonlogger


def setup_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    log_keys = [
        "asctime",
        "filename",
        "funcName",
        "levelname",
        "lineno",
        "module",
        "message",
    ]

    def log_format(x):
        return [f"%({i:s})s" for i in x]

    custom_format = " ".join(log_format(log_keys))

    fr = jsonlogger.JsonFormatter(custom_format)
    logHandler = logging.StreamHandler()

    logHandler.setFormatter(fr)
    logger.addHandler(logHandler)
