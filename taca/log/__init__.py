""" TACA logging module for external scripts
"""
import logging
from .. import __name__ as software
from .. import __version__ as version


class VersionFilter(logging.Filter):
    """ a filter that injects software version into log records
    """
    def filter(self, record):
        record.version = version
        return True


class NameFilter(logging.Filter):
    """ a filter that injects software version into log records
    """
    def filter(self, record):
        record.software = software
        return True

# get root logger
ROOT_LOG = logging.getLogger()
ROOT_LOG.setLevel(logging.INFO)

# Console logger
stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(software)s v%(version)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.addFilter(VersionFilter())
stream_handler.addFilter(NameFilter())
ROOT_LOG.addHandler(stream_handler)

LOG_LEVELS = {
    'ERROR': logging.ERROR,
    'WARN': logging.WARN,
    'INFO': logging.INFO,
    'DEBUG': logging.DEBUG
}


def init_logger_file(log_file, log_level='INFO'):
    """ Append a FileHandler to the root logger.

    :param str log_file: Path to the log file
    :param str log_level: Logging level
    """
    ROOT_LOG.handlers=[]
    log_level = LOG_LEVELS[log_level] if log_level in LOG_LEVELS.keys() else logging.INFO

    ROOT_LOG.setLevel(log_level)

    file_handle = logging.FileHandler(log_file)
    file_handle.setLevel(log_level)
    file_handle.setFormatter(formatter)
    file_handle.addFilter(VersionFilter())
    file_handle.addFilter(NameFilter())
    ROOT_LOG.addHandler(file_handle)
