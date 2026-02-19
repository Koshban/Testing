import logging
import os
import inspect
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGS_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOGS_DIR, exist_ok=True)  # Ensure logs directory exists
now = datetime.now().strftime('%Y%m%d_%H%M')
scriptname = os.path.splitext(os.path.basename(__file__))[0]
logfilename = os.path.join(LOGS_DIR, f'{scriptname}_{now}.log')

LOG_FORMAT = '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s'

logging.basicConfig(
    level = logging.DEBUG,
    format = LOG_FORMAT,
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(logfilename)
    ]
)

logger = logging.getLogger()

def get_logger(logger_name=None, log_path=None):
    """
    Returns a logger configured to log to log_path and console,
    with function and filename in the log format.
    """
    if logger_name is None:
        # Try to get the caller's filename
        frame = inspect.stack()[1]
        logger_name = os.path.splitext(os.path.basename(frame.filename))[0]

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # Avoid adding handlers multiple times
    if not logger.hasHandlers():
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s'
        )
        if log_path:
            file_handler = logging.FileHandler(log_path)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    return logger