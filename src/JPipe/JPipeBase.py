from logging import Logger


class JPipeBase:
    def __init__(self):
        self._logger = Logger(__name__)

    def info(self, msg):
        self._logger.info(msg)

    def error(self, msg):
        self._logger.error(msg)

    def debug(self, msg):
        self._logger.debug(msg)
