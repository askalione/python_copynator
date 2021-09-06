import sys, logging
from logging.handlers import TimedRotatingFileHandler

LOG_FILE = './copynator.log'
LOG_FORMAT = '%(asctime)s — %(levelname)s — %(message)s'
LOG_DATE_FORMAT = '%m.%d.%Y %H:%M:%S'

LOG_FORMATTER = logging.Formatter(LOG_FORMAT, LOG_DATE_FORMAT)

def get_console_handler():
   handler = logging.StreamHandler(sys.stdout)
   handler.setFormatter(LOG_FORMATTER)
   return handler
   
   
def get_file_handler(file):
   handler = TimedRotatingFileHandler(file, when='midnight')
   handler.setFormatter(LOG_FORMATTER)
   return handler
   
   
def get_logger():
   logger = logging.getLogger('copynator')
   logger.setLevel(logging.DEBUG)
   logger.addHandler(get_console_handler())
   logger.addHandler(get_file_handler(LOG_FILE))
   logger.propagate = False
   return logger