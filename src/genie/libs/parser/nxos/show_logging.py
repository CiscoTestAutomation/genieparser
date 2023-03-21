''' show_logging.py

NXOS parsers for the following show commands:
    * show logging logfile
    * show logging logfile | include {include}
    * show logging level
    * show logging level {facility}
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
                {
                Any():
                    { 'default_severity': int,
                      'current_session_severity': int
                       }
                }
            }

class ShowLoggingLevel(ShowLoggingLevelSchema):
    '''Schema for:
        * 'show logging level'
        * 'show logging level {facility}'
    '''

    cli_command = [ 'show logging level', 'show logging level {facility}' ]

    def cli(self, facility='', output=None):

        if output is None:
            # Build the command
            if facility:
                cmd = self.cli_command[1].format(facility=facility)
            else:
                cmd = self.cli_command[0]

            # Execute the command
            output = self.device.execute(cmd)

        # Example
        # acllog                  2                       1
        p0 = re.compile(r'(?P<facility>\S+)\s+'
                        '(?P<default_severity>\d)\s+'
                        '(?P<current_session_severity>\d)')
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                facility_dict = ret_dict.setdefault('facility', {}).setdefault(m.groupdict()['facility'], {})

                for x in ['default_severity', 'current_session_severity']:
                    x_val = int(m.groupdict()[x])
                    ret_dict['facility'][facility][x] = x_val

        return ret_dict
