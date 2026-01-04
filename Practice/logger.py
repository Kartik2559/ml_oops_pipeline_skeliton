from datetime import datetime

class Logger:
    def _timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def info(self, msg):
        print(f"{self._timestamp()} [INFO] {msg}")

    def error(self, msg):
        print(f"{self._timestamp()} [INFO] {msg}")


logger = Logger()

logger.info("Training Started")
logger.error("File not opening")