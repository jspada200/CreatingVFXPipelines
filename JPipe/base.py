import logging
import colorlog


class JPipeBase:
    def __init__(self):
        self._logger = logging.getLogger("JPipe")
        self._logger.handlers.clear()
        self._logger.propagate = False
        if not self._logger.hasHandlers():
            handler = logging.StreamHandler()
            handler.setLevel(logging.DEBUG)

            formatter = colorlog.ColoredFormatter(
                "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s",
                datefmt=None,
                reset=True,
                log_colors={
                    'DEBUG':    'cyan',
                    'INFO':     'green',
                    'WARNING':  'yellow',
                    'ERROR':    'red',
                    'CRITICAL': 'red,bg_white',
                },
                secondary_log_colors={},
                style='%'
            )

            handler.setFormatter(formatter)
            self._logger.addHandler(handler)

    def info(self, msg):
        self._logger.info(msg)

    def error(self, msg):
        self._logger.error(msg)

    def debug(self, msg):
        self._logger.debug(msg)

    def warn(self, msg):
        self._logger.warning(msg)
