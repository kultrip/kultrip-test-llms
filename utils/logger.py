import logging
import sys
from typing import Optional

def setup_logger(
    name: str = "kultrip",
    level: int = logging.INFO,
    log_to_file: Optional[str] = None,
) -> logging.Logger:
    """
    Set up a logger for the application.

    Args:
        name: Name of the logger.
        level: Logging level (e.g., logging.DEBUG, logging.INFO).
        log_to_file: If set, logs will also be written to this file.

    Returns:
        Configured Logger object.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s [%(name)s] %(message)s",
        "%Y-%m-%d %H:%M:%S"
    )
    # Console handler
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # File handler (optional)
    if log_to_file:
        fh = logging.FileHandler(log_to_file)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    logger.propagate = False
    return logger

# Example usage:
# logger = setup_logger(level=logging.DEBUG, log_to_file="app.log")
# logger.info("Logger initialized.")
# logger.debug("Debug message.")
# logger.error("Error message.")