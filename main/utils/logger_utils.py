import logging


class Logger:
    @staticmethod
    def get_logger():
        logger = logging.getLogger(__name__)

        file_handler = logging.FileHandler('.\\logs')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s [%(filename)s:%(lineno)s - %(funcName)s() ] %("
                                      "message)s")
        file_handler.setFormatter(formatter)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(ch)
        logger.setLevel(logging.INFO)
        return logger
