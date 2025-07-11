''' show_inventory.py
IOSXR parsers for the following show commands:
    * show inventory raw
'''

# python
import re

# metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any


class ShowInventoryRawSchema(MetaParser):
    """Schema for show inventory raw"""
    schema = {
        'module_name':
            {Any():
                {'descr': str,
                 'pid': str,
                 'vid': str,
                 'sn': str,
                },
            },
        }

class ShowInventoryRaw(ShowInventoryRawSchema):
    """Parser for show inventory raw"""

    cli_command = 'show inventory raw'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        inventory_dict = {}

        # NAME: "Rack 0", DESCR: "Cisco XRv9K Centralized Virtual Router"
        # NAME: "Rack 0", DESCR: "Cisco 8203 1RU System with 32x400GE QSFP56-DD & 12x100GE QSFP28"
        # NAME: "0/FT2-FAN_1_Speed", DESCR: "Fan Speed Sensor"
        # NAME: "0/FT4", DESCR: "Sherman Fan Module Reverse Airflow / exhaust, BLUE"
        # NAME: "Optics0/0/0/0-Tx Lane 0 Power", DESCR: "Power Sensor"
        p1 = re.compile(r'^NAME:\s+"(?P<module_name>[^"]+)",'
                        r'\s+DESCR:\s+"(?P<descr>[^"]+)"$')

        # PID: 8201-32FH         , VID: V00, SN: FOC2422NMRH
        # PID: 8202-32FH-M[FB]   , VID: N/A, SN: FLM252604RR
        # PID: N/A               , VID: N/A, SN: N/A
        # PID: PSU6.3KW-HV       , VID: V01, SN: DTM2339018G
        p2 = re.compile(r'^PID:\s+(?P<pid>[\w\/\.\-\[\]]+|N\/A)\s*,'
                        r' VID:\s+(?P<vid>[\w\/\-]+|N\/A)\s*,'
                        r' SN:\s+(?P<sn>[\w\/\-]+|N\/A)$')

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # NAME: "0/FT4", DESCR: "Sherman Fan Module Reverse Airflow / exhaust, BLUE"
            # NAME: "Optics0/0/0/0-Tx Lane 0 Power", DESCR: "Power Sensor"
            m = p1.match(line)
            if m:
                module_name = m.groupdict()['module_name']
                module_dict = inventory_dict.setdefault('module_name', {}).setdefault(module_name, {})
                module_dict['descr'] = m.groupdict()['descr']
                continue

            # PID: 8201-32FH         , VID: V00, SN: FOC2422NMRH
            # PID: 8202-32FH-M[FB]   , VID: N/A, SN: FLM252604RR
            m = p2.match(line)
            if m:
                module_dict.update({
                    "pid": m.groupdict()['pid'],
                    "vid": m.groupdict()['vid'],
                    "sn": m.groupdict()['sn']
                })

        return inventory_dict
