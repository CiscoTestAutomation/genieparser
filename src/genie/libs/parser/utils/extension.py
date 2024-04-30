import logging
import pathlib
import inspect
import itertools
import importlib
from genie.metaparser import MetaParser
from genie.json.make_json import MakeParsers

log = logging.getLogger(__name__)

class ExtendParsers(MakeParsers):
    # Files and directories to ignore while walking package
    IGNORE_DIR = ['.git', '__pycache__', 'template', 'tests']
    IGNORE_FILE = ['__init__.py', 'base.py', 'utils.py']

    def __init__(self, package):
        self.output = {'tokens': {}, 'extend_info': []}
        self.package = package
        self.root = {
            'root': package,
            'mod_name': 'parser',
            'url': {
                'link':
                'https://github.com/CiscoTestAutomation/genieparser/tree/{branch}/',
                'branch': 'master',
                'style': 'github',
            },
        }
        self.module_loc = importlib.import_module(package).__path__[0]
        self.package_location = self.module_loc
        log.debug(f'Parser extension: {package} {self.package_location}')

    def extend(self):
        # Walk all files in the given package and find all parsers
        log.debug(f'Parser module: {self.module_loc}')
        self._recursive_find(pathlib.Path(self.module_loc))
