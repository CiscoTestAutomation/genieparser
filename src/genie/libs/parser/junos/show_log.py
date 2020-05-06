""" show_log.py

JunOs parsers for the following show commands:
    * show log {filename}
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, SchemaTypeError, Schema)


class ShowLogFilenameSchema(MetaParser):
    """ Schema for:
            * show log {filename}
    """

    schema = {
        "file-content": list
    }

class ShowLogFilename(ShowLogFilenameSchema):
    """ Parser for:
            * show log {filename}
    """
    cli_command = 'show log {filename}'

    def cli(self, output=None, filename=None):
        if not output:
            out = self.device.execute(self.cli_command.format(filename=filename))
        else:
            out = output

        ret_dict = {}

        lines = out.splitlines()
        if len(lines) > 1:
            ret_dict['file-content'] = out.splitlines()[1:]

        return ret_dict