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
        "file-content": str
    }

class ShowLogFilename(ShowLogFilenameSchema):
    """ Parser for:
            * show log {filename}
    """
    cli_command = 'show log {filename}'

    def cli(self, output=None, filename=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            file_contents = ret_dict.setdefault("file-content", "")
            file_contents += line+"\n"
            ret_dict['file-content'] = file_contents

        import pprint
        pprint.pprint(ret_dict)
        return ret_dict