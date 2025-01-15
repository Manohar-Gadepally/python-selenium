import logging


class Logger:
    @staticmethod
    def get_logger():
        logger = logging.getLogger(__name__)
        file_handler = logging.FileHandler('.\\logs')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger
