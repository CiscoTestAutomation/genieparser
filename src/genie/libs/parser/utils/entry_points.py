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
          <function> is a callable that returns a dictionary of parsers

Notes
-----
The following is an example User provided function that returns a dictionary of
parser to be added into the genie framework.  The key is the os_name, for
example 'nxos', and the value is a list of MetaParser class definitions.

    def add_my_parsers():
        return {
            'iosxe': [
                iosxe.show_interface_transceiver.ShowInterfaceTransceiver
            ],
            'nxos': [
                nxos.show_interface_transceiver.ShowInterfaceTransceiver
            ]
        }

"""

import sys
import pkg_resources
import logging

from . import common

log = logging.getLogger(__name__)

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

    cli_commands = parser.cli_command
    if isinstance(cli_commands, str):
        cli_commands = [cli_commands]

    try:
        parser_data = common.parser_data
    except AttributeError:
        parser_data = common._load_parser_json()

    for cmd in cli_commands:
        
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
        if not callable(loader_function):
            log.warning('unable to load parsers from entry point '
                        '{name} as it is not callable.'.format(name=ep.name))
            continue

        parser_dict = loader_function()
        for os_name, parser_list in parser_dict.items():
            for parser in parser_list:
                add_parser(parser=parser, os_name=os_name)


load_entry_points()
