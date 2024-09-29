import logging
import os
from db.db import Log

def setup_logger(log_file='crypto.log'):
    logger = logging.getLogger("crypto_logger")
    logger.setLevel(logging.INFO)

    # Formatação do logger
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # StreamHandler (Console)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # FileHandler (Arquivo)
    if not os.path.exists('logs'):
        os.makedirs('logs')  # Cria um diretório de logs se não existir
    file_handler = logging.FileHandler(os.path.join('logs', log_file))
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

def save_log_to_db(logger, message, db_session):
    """Salva uma nova entrada de log no banco de dados com codificação iso8859-1."""
    try:
        # Codifica a mensagem
        encoded_message = message.encode('iso8859-1', errors='replace').decode('utf-8')  # Codifica para iso8859-1 e decodifica para utf-8
        
        # Salva o log na tabela
        log_entry = Log(message=encoded_message)
        db_session.add(log_entry)
        db_session.commit()
        logger.info(f"Log saved to database: {encoded_message}")  # Log no console
    except Exception as e:
        db_session.rollback()  # Reverte a transação em caso de erro
        logger.error(f"Error saving log to database: {e}")  # Log de erro

