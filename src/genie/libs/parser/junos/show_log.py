""" show_log.py

JunOs parsers for the following show commands:
    * show log {filename}
    * show log {filename} | match {match}
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, Schema)


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
    cli_command = ['show log {filename}',
        'show log {filename} | except {except_show_log} | match {match}']

    def cli(self, output=None, filename=None, except_show_log=None, match=None):
        if not output:
            if match:
                out = self.device.execute(self.cli_command[1].format(
                    filename=filename,
                    except_show_log="show log",
                    match=match))
            else:
                out = self.device.execute(self.cli_command[0].format(filename=filename))
        else:
            out = output

        ret_dict = {}

        lines = out.splitlines()
        if len(lines) > 1:
            ret_dict['file-content'] = out.splitlines()[1:]

        return ret_dict