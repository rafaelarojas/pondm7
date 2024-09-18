import logging

def setup_logger():
    # Configura o logger
    logger = logging.getLogger("crypto_logger")
    logger.setLevel(logging.INFO)

    # Formato do log
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Log para arquivo
    file_handler = logging.FileHandler('crypto.log')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # Log para console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Instância global do logger
logger = setup_logger()
