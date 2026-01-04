## Encapsulation + Composition

import logging
import os

class AppLogger:
    def __init__(self, name:str, log_file: str = 'logs/app.log'):
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:
            file_handler = logging.FileHandler(log_file)
            console_handler = logging.StreamHandler()

            formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

    def info(self, message: str):
        self.logger.info(message)

    def error(self, message: str):
        self.logger.error(message)