from typing import Any
from enum import Enum

import logging


class LogLevel(Enum):
    '''
    What the stdlib did not provide!
    '''
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

    def __str__(self):
        return self.name


class Counter(dict):
    """
    Like a dict, but returns 0 if the key isn't found.
    """

    def __missing__(self, key: Any) -> int:
        return 0
