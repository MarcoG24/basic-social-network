
import configparser
import inspect
import logging
import os

from logging import basicConfig


# Logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logformat = '[ %(levelname)s ] - %(asctime)-15s :: %(message)s'
basicConfig(format=logformat)

# Config parser
currentdir = os.path.dirname(
    os.path.abspath(inspect.getfile(inspect.currentframe()))
)
CONFIG_FILE = f'{currentdir}/config.ini'
logger.debug(f'Parsing {CONFIG_FILE} for {__name__}')
config = configparser.ConfigParser()
config.read(CONFIG_FILE)


__all__ = [
    'logger',
    'CONFIG_FILE',
    'config',
]
