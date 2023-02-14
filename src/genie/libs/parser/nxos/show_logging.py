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

class ShowLoggingLevelSchema(MetaParser):
    '''Schema for:
        * 'show logging level'
        * 'show logging level {name}'
    '''

    schema = { 'facility':
                { Any():
                    { 'def_severity': int,
                      'curr_severity': int }
                }
            }

class ShowLoggingLevel(ShowLoggingLevelSchema):
    '''Schema for:
        * 'show logging level'
    '''

    cli_command = 'show logging level'

    def cli(self, output=None):

        if (output is None):
            # Build the command
            cmd = self.cli_command

            # Execute the command
            out = self.device.execute(cmd)

        else:
            out = output

        p = re.compile(r'(?P<facility>\S+)\s+'
                        '(?P<def_severity>\d)\s+'
                        '(?P<curr_severity>\d)')
        ret_dict = {
            'facility': {}
        }

        for line in out.splitlines():
            line = line.strip()

            m = p.match(line)
            if m:
                facility = m.groupdict()['facility']
                if facility not in ret_dict['facility']:
                    ret_dict['facility'][facility] = {}

                for x in ['def_severity', 'curr_severity']:
                    x_val = m.groupdict()[x]
                    ret_dict['facility'][facility][x] = x_val

        return ret_dict
