'''Logger'''

import logging


class Logger():
    '''Logger'''
    def __init__(self,
                 name: str='root',
                 logger_type: str='base',
                 log_level: int=logging.DEBUG):
        '''
        Constructor
        @param name: str
            @default: 'root'
        @param logger_type: str
            @default: 'base'
            @options: ['base', 'systemd-journal']
        @param log_level: int
            @default: logging.DEBUG
            @options: logging.[INFO, DEBUG, WARNING, ERROR, CRITICAL]
        '''
        self.name = name
        self.logger_type = logger_type
        if logger_type == 'base':
            formatter = logging.Formatter(
                fmt='%(asctime)s [%(levelname)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

            handler = logging.StreamHandler()
            handler.setFormatter(formatter)

            logger = logging.getLogger(self.name)
            logger.setLevel(logging.DEBUG)
            logger.addHandler(handler)
        elif logger_type == 'systemd-journal':
            try:
                from systemd.journal import JournalHandler
                logging.root.addHandler(JournalHandler())
                logging.root.setLevel(logging.DEBUG)

            except Exception:
                raise OSError("Couldn't import systemd.journal.JournalHandler.")
        else:
            raise ValueError("{} is not a valid logger_type. Choose from {}".format(
                logger_type, possible_logger_types))


    def get_logger(self):
        '''
        Return the logger
        '''
        return self.logger
