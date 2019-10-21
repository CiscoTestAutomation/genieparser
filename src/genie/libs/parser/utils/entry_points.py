"""
This file contains the code that enables external packages to dynamically add
parsers using the setuptools entry_point mechanism.  The developer is required
to add the following to their setup() invocation:

    setup(...
        entry_points={
            'genie.libs.parser': [
                "packagename = module.function"
            ]
        }
    )

    where <packagename> is the name of their specific package
          <module> is the module within their package that contains the function
          <function> is a callable that calls the add_parser() function for each
            parser the developer wants to add into the genie framework

"""

import sys
import pkg_resources
from .common import parser_data

ENTRY_POINT_NAME = 'genie.libs.parser'


def add_parser(parser, os_name):
    """
    Dynamically add the parser class found in module `mod` for the given
    network OS name `os_name`

    Notes
    -----
    The parser class is presumed to have a class attribute `cli_command` which
    is a list of command to add into the genie parser framework.

    Parameters
    ----------
    parser : class
        The parser class that implements a MetaParser

    os_name : str
        The NOS name for which the parser is supported, for example "nxos"
    """
    mod = sys.modules[parser.__module__]
    package = mod.__package__

    for cmd in parser.cli_command:
        if cmd not in parser_data:
            parser_data[cmd] = {}

        parser_data[cmd][os_name] = {
            'module_name': mod.__name__.rsplit('.', 1)[-1],
            'package': package,
            'class': parser.__name__
        }


def load_entry_points():
    for ep in pkg_resources.iter_entry_points(ENTRY_POINT_NAME):
        loader_function = ep.load()
        loader_function()


load_entry_points()
