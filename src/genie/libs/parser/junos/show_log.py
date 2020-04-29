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
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # show log messages
        p1 = re.compile(r'^show +log')

        for line in out.splitlines():
            line = line.strip()

            if not line:
                continue

            m = p1.match(line)
            if m:
                continue

            file_contents = ret_dict.setdefault("file-content", [])
            file_contents.append(line)

        import pprint
        pprint.pprint(ret_dict)

        return ret_dict