from typing import Any
from enum import Enum

import logging


class LogLevel(Enum):
    '''
    What the stdlib did not provide!
    '''
    INFO = logging.INFO
    DEBUG = logging.DEBUG
    ERROR = logging.ERROR
    WARNING = logging.WARNING
    CRITICAL = logging.CRITICAL

    def __str__(self):
        return self.name
