# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any

# Python
import re

# ==============================
# Schema for 'show fex'
# ==============================

class ShowFexSchema(MetaParser):

    ''' Schema for "show fex" '''

    schema = {
        'fexes': {
            Any(): {
                'description': str,
                'state': str,
                'model': str,
                'serial_number': str
            }
        }
    }

# ==============================
# Parser for 'show fex'
# ==============================

class ShowFex(ShowFexSchema):

    ''' Parser for "show fex"'''

    cli_command = 'show fex'

    def cli(self, output=None):
        if output is None:
            # Get output from device
            out = self.device.execute(self.cli_command)
        else:
            out = output 
        # Initial return dictionary
        parsed_dict = {}

        p1 = re.compile(r'(?P<number>(\d+)) +(?P<description>(\S+)) +(?P<state>(\S+)) +(?P<model>(\S+)) +(?P<serial>(\S+))$')

        for line in out.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                group = m.groupdict()
                fex = group['number']
                fex_dict = parsed_dict.setdefault('fexes', {}).setdefault(fex, {})
                fex_dict['description'] = group['description']
                fex_dict['state'] = group['state']
                fex_dict['model'] = group['model']
                fex_dict['serial_number'] = group['serial']

        return parsed_dict

