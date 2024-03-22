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
            output = self.device.execute(self.cli_command)
        
        # Initial return dictionary
        parsed_dict = {}

        # 1     FEX-1_Device1             Online   N2K-C2348UPQ-10GE   FOC1234567A
        # 2     FEX-2_Device2             Online   N2K-C2348UPQ-10GE   FOC1234567B
        # 3     FEX-3_Device3             Online   N2K-C2348UPQ-10GE   FOC1234567C
        
        p1 = re.compile(r'(?P<number>(\d+)) +(?P<description>(\S+)) +(?P<state>(\S+)) +(?P<model>(\S+)) +(?P<serial>(\S+))$')

        for line in output.splitlines():
            line = line.strip()

            # 1     FEX-1_Device1             Online   N2K-C2348UPQ-10GE   FOC1234567A
            # 2     FEX-2_Device2             Online   N2K-C2348UPQ-10GE   FOC1234567B
            # 3     FEX-3_Device3             Online   N2K-C2348UPQ-10GE   FOC1234567C
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

