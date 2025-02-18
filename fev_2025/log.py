"""
Usando logging para acompanhar a execução.
"""

import logging

log_file = "execucao.log"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(log_file, encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%d-%m-%Y %H:%M:%S")

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)