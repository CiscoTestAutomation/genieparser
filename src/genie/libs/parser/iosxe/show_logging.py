''' show_logging.py

IOSXE parsers for the following show commands:
    * show logging
'''
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


# ==============================================
# Schema for:
#   * 'show logging'
# ==============================================
class ShowLoggingSchema(MetaParser):
    '''Schema for:
        * 'show logging'
    '''

    schema = {
        'logs': list,
        }


# ==============================================
# Parser for:
#   * 'show logging'
# ==============================================
class ShowLogging(ShowLoggingSchema):
    '''Parser for:
        * 'show logging'
    '''
    cli_command = 'show logging'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        parsed_dict = {}
        log_lines = []

        for line in out.splitlines():
            line = line.strip()

            # Add line to 'logs'
            if line:
                log_lines.append(line)
                parsed_dict['logs'] = log_lines
                continue

        return parsed_dict
