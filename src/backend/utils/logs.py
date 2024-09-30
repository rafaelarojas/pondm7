import logging
import os
from db.db import Log

def setup_logger(log_file='crypto.log'):
    logger = logging.getLogger("crypto_logger")
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    if not os.path.exists('logs'):
        os.makedirs('logs')
    file_handler = logging.FileHandler(os.path.join('logs', log_file))
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

def save_log_to_db(logger, message, db_session):
    """Salva uma nova entrada de log no banco de dados com codificação iso8859-1."""
    try:
        encoded_message = message.encode('iso8859-1', errors='replace').decode('utf-8')
        
        log_entry = Log(message=encoded_message)
        db_session.add(log_entry)
        db_session.commit()
        logger.info(f"Log saved to database: {encoded_message}")
    except Exception as e:
        db_session.rollback()
        logger.error(f"Error saving log to database: {e}")

