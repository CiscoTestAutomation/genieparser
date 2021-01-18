import logging
import pathlib
import inspect
import itertools
import importlib
from genie.metaparser import MetaParser

log = logging.getLogger(__name__)

class ExtendParsers(object):
    # Files and directories to ignore while walking package
    IGNORE_DIR = ['.git', '__pycache__', 'template', 'tests']
    IGNORE_FILE = ['__init__.py', 'base.py', 'utils.py']

    def __init__(self, package):
        self.output = {'tokens': [], 'extend_info': []}
        self.package = package
        # Figure out location of package so you can walk it
        self.module_loc = importlib.import_module(package).__path__[0]

    @staticmethod
    def _find_parsers(mod):
        parsers = []
        for name, obj in inspect.getmembers(mod):
            # skip if starts with '_' or not class
            if name.startswith('_') or not inspect.isclass(obj):
                continue

            # skip anything not defined in this module
            try:
                if inspect.getsourcefile(obj) != mod.__file__:
                    continue
            except:
                # getsourcefile fails for builtin objects
                # we aren't interested in those anyway
                continue

            # Inherits from MetaParser + has an attribute called 'cli_command'
            if issubclass(obj, MetaParser) and hasattr(obj, 'cli_command'):
                parsers.append(obj)

        return parsers

    def _add_parser(self, parser, cli, tokens, mod):
        if cli not in self.output:
            self.output[cli] = {}

        extend_info = self.output['extend_info']
        extend_info.append("cli: '{}', tokens {}, class: {}"
                    .format(cli, tokens, parser.__name__))

        output = self.output[cli]
        for token in tokens:
            if token not in output:
                output[token] = {}
            output = output[token]
            if token not in self.output['tokens']:
                self.output['tokens'].append(token)

        output['module_name'] = mod.__name__.rsplit('.', 1)[-1]
        output['package'] = self.package
        output['class'] = parser.__name__
        output['doc'] = parser.__doc__
        output['uid'] = cli.replace(' ', '_').replace('{', '').replace('}', '').replace('|', '_')

    def _add_parsers(self, item, tokens):
        # Find all classes which has a function named parse
        # Will give module path
        path_list = [self.package] + tokens + [item.name.replace(item.suffix, '')]
        module_path = '.'.join(path_list)
        mod = importlib.import_module(module_path)
        parsers = self._find_parsers(mod)

        for parser in parsers:
            if isinstance(parser.cli_command, list):
                for cli in parser.cli_command:
                    self._add_parser(parser, cli, tokens, mod)
            else:
                self._add_parser(parser, parser.cli_command, tokens, mod)

    def _recursive_find(self, item, token):
        for item in item.iterdir():
            if item.is_dir():
                if item.name in self.IGNORE_DIR:
                    continue

                self._recursive_find(item, token + [item.name])

            elif item.is_file():
                if item.name in self.IGNORE_FILE or item.suffix != '.py':
                    continue

                # item is not a directory. item is not a file in IGNORE_FILE.
                # item is a python file. Find all parsers in file.
                self._add_parsers(item, token)

    def extend(self):
        # Walk all file in there and go through the parsers
        self._recursive_find(pathlib.Path(self.module_loc), [])
