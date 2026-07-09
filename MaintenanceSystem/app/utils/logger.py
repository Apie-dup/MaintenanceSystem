import logging
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR / "maintenance.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


class Logger:

    @staticmethod
    def info(message):
        logging.info(message)

    @staticmethod
    def warning(message):
        logging.warning(message)

    @staticmethod
    def error(message):
        logging.error(message)