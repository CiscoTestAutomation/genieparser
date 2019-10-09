import os
import sys
import yaml
import json
import pprint
import pathlib
import logging
import inspect
import argparse
import itertools
import importlib

from genie.metaparser import MetaParser

IGNORE_DIR = ['.git', '__pycache__', 'template', 'tests']
IGNORE_FILE = ['__init__.py', 'base.py', 'utils.py']
AVAILABLE_FUNC = ['cli', 'xml', 'yang', 'rest']

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
log = logging.getLogger(__name__)

def format(d, tab=0):
    s = ['{\n']
    if d is None:
        return d
    for k,v in d.items():
        if isinstance(v, dict):
            v = format(v, tab+1)
        else:
            v = repr(v)
        s.append('%s%r: %s,\n' % ('  '*tab, k, v))
    s.append('%s}' % ('  '*tab))
    return ''.join(s)

class CreateApiDoc(object):
    def __init__(self, datafile):
        assert 'VIRTUAL_ENV' in os.environ

        with open(datafile, 'r') as f:
            self.datafile = yaml.safe_load(f)
        self.output = {}
        self.output['tokens'] = []

    def _expand(self, name):
        if '$env(VIRTUAL_ENV)' in name:
            # Replace '$env(VIRTUAL_ENV)' with the actual value
            return name.replace('$env(VIRTUAL_ENV)', os.environ['VIRTUAL_ENV'])
        return name

    def _find_parsers(self, mod):
        parsers = []
        for name, obj in inspect.getmembers(mod):
            # starts with _ are ignored
            if name.startswith('_'):
                continue

            # skip if not class
            if not inspect.isclass(obj):
                continue

            # skip anything not defined in this module
            try:
                if inspect.getsourcefile(obj) != mod.__file__:
                    continue
            except:
                # getsourcefile fails for builtin objects
                # we aren't interested in those anyway
                continue

            # Inherits from metaparser + have a funciton which is from the
            # available func
            if issubclass(obj, MetaParser) and hasattr(obj, 'cli_command'):
                parsers.append(obj)
        return parsers

    def _add_parser(self, parser, cli, tokens, mod):
        if cli not in self.output:
            self.output[cli] = {}

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
        output['schema'] = format(parser.schema)
        output['uid'] = cli.replace(' ','_').replace('{', '').replace('}', '').replace('|', '_')
        line = inspect.getsourcelines(parser)[-1]

        temp_url = mod.__file__.replace(os.path.join(
                       os.environ['VIRTUAL_ENV'], 'pypi', 'genieparser') + '/', '')

        style = self.root['url']['style']

        if style == 'bitbucket':
            url = '{p}{t}#{l}'.format(p=self.root['url']['link'], t=temp_url, l=line)
        elif style == 'github':
            url = p=self.root['url']['link'].format(branch=self.root['url']['branch'])
            url = '{p}{t}#L{l}'.format(p=url, t=temp_url, l=line)

        output['url'] = url


    def _add_parsers(self, item, tokens):
        # Find all classes which has a function named parse
        # Will give module path
        module_path = self.root['root'] + str(item).rsplit('.', 1)[0].\
                                  replace(self.module_loc, '').replace('/', '.')
        mod = importlib.import_module(module_path)
        parsers = self._find_parsers(mod)
        if parsers:
            pass
        for parser in parsers:
            if isinstance(parser.cli_command, list):
                for cli in parser.cli_command:
                    self._add_parser(parser, cli, tokens, mod)
            else:
                self._add_parser(parser, parser.cli_command, tokens, mod)



    def _recursive_find(self, item, token):
        for item in item.iterdir():
            if item.is_dir():
                if item.name in IGNORE_DIR:
                    # Ignore
                    continue
                else:
                    self._recursive_find(item, token + [item.name])

            elif item.is_file():
                if item.name in IGNORE_FILE or item.suffix != '.py':
                    continue
                # Then add it to the self.datafile
                self._add_parsers(item, token)

    def find_all_apis(self):
        if 'root_directories' not in self.datafile:
            return {}

        for name, values in self.datafile['root_directories'].items():
            log.info("Learning '{name}'".format(name=name))

            # Figure out location of package so you can walk it
            self.root = values
            self.package = self.root['root']
            self.module_loc = importlib.import_module(self.root['root']).__path__[0]

            # Walk all file in there and go through the parsers
            self._recursive_find(pathlib.Path(self.module_loc), [])


def find_diff(l1, l2):
    '''Difference between list1 and list2'''
    diff = []
    for list1, list2 in itertools.zip_longest(l1, l2):
        if list2 != list1:
            diff.append(list2)
    return diff


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-datafile',
                        metavar='FILE',
                        type=str,
                        default=None,
                        help='File containing directory information')
    parser.add_argument('-save_location',
                        metavar='FILE',
                        type=str,
                        default=None,
                        help='Location to save the output file')
    custom_args = parser.parse_known_args()[0]

    apiDoc = CreateApiDoc(custom_args.datafile)
    apiDoc.find_all_apis()

    output = json.dumps(apiDoc.output)

    os.makedirs(os.path.dirname(custom_args.save_location), exist_ok=True)
    with open(custom_args.save_location, 'w+') as f:
        f.write(output)
