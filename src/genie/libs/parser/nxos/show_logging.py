''' show_logging.py

NXOS parsers for the following show commands:
    * show logging logfile
    * show logging logfile | include {include}
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


# ==============================================
# Schema for:
#   * 'show logging logfile'
#   * 'show logging logfile | include {include}'
# ==============================================
class ShowLoggingLogfileSchema(MetaParser):
    
    '''Schema for:
        * 'show logging logfile'
        * 'show logging logfile | include {include}'
    '''

    schema = {
        'logs': list,
        }


# ==============================================
# Parser for:
#   * 'show logging logfile'
#   * 'show logging logfile | include {include}'
# ==============================================
class ShowLoggingLogfile(ShowLoggingLogfileSchema):

    '''Schema for:
        * 'show logging logfile'
        * 'show logging logfile | include {include}'
    '''

    cli_command = ['show logging logfile | include {include}',
                   'show logging logfile',
                   ]
    exclude = ['logs']

    def cli(self, include='', output=None):

        if output is None:
            # Build the command
            if include:
                cmd = self.cli_command[0].format(include=include)
            else:
                cmd = self.cli_command[1]
            # Execute the command
            out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        parsed_dict = {}
        log_lines = []

        for line in out.splitlines():
            line = line.strip()

            # Add line to 'logs'
            if line and 'show logging logfile' not in line:
                log_lines.append(line)
                parsed_dict['logs'] = log_lines
                continue

        return parsed_dict
