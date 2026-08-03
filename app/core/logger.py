import logging
from pathlib import Path

from app.core.settings import Settings


LOG_FOLDER = Path(Settings.LOG_FOLDER)
LOG_FOLDER.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_FOLDER / Settings.LOG_FILE


def configure_logging():
    """
    Configure application-wide file logging.
    """

    logger = logging.getLogger("MaintenanceSystem")

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8"
    )

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | "
        "%(name)s | %(message)s"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger


logger = configure_logging()