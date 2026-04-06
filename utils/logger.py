import logging
import os
from datetime import datetime


def get_logger(name=__name__):
    """
    Returns a configured logger instance.
    Logs to both console and a log file under /reports/logs/
    """
    # Create logs directory
    log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "reports", "logs")
    os.makedirs(log_dir, exist_ok=True)

    log_filename = os.path.join(log_dir, f"test_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

    logger = logging.getLogger(name)

    # Avoid duplicate handlers if logger already exists
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        # ── Console Handler ──────────────────────────────
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_format = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%H:%M:%S"
        )
        console_handler.setFormatter(console_format)

        # ── File Handler ─────────────────────────────────
        file_handler = logging.FileHandler(log_filename)
        file_handler.setLevel(logging.DEBUG)
        file_format = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(funcName)s:%(lineno)d | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        file_handler.setFormatter(file_format)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger