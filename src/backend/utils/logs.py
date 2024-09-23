import logging

def setup_logger():
    logger = logging.getLogger("crypto")
    logger.setLevel(logging.INFO)

    # Criando um FileHandler
    file_handler = logging.FileHandler("crypto.log")
    file_handler.setLevel(logging.INFO)

    # Criando um StreamHandler para exibir no console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Definindo o formato dos logs
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Adicionando os handlers ao logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
