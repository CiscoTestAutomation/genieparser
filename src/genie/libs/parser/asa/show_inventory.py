''' show_inventory.py

Parser for the following show commands:
    * show inventory
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any

# =============================================
# Schema for 'show inventory'
# =============================================
class ShowInventorySchema(MetaParser):
    """Schema for
        * show inventory
    """

    schema = {
        Any(): {
            'description': str,
            'pid': str,
            'vid': str,
            'sn': str
        }
    }

# =============================================
# Parser for 'show inventory'
# =============================================
class ShowInventory(ShowInventorySchema):
    """Parser for
        * show interface summary
    """

    cli_command = 'show inventory'

    def cli(self, output=None):
        if output is None:
            # excute command to get output
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Name: "Chassis", DESCR: "ASA 5555-X with SW, 8 GE Data, 1 GE Mgmt"
        # Name: "power supply 1", DESCR: "ASA 5545-X/5555-X AC Power Supply"
        p1 = re.compile(r'^Name:\s+"(?P<name>.+)",\s+DESCR:\s+"(?P<description>.+)"$')

        # PID: ASA5555, VID: V01, SN: AAAAA11111
        # PID: AAA-AAA-AAA, VID: N/A, SN: AAA111
        # PID: N/A, VID: N/A, SN: AAAAA11111
        # PID: N/A, VID: , SN: AAAAA11111
        p2 = re.compile(r'^PID:\s+(?P<pid>.+),\s+VID:\s?(?P<vid>.+),\s+SN:\s+(?P<sn>.+)$')

        for line in out.splitlines():
            line = line.strip()

            # Name: "Chassis", DESCR: "ASA 5555-X with SW, 8 GE Data, 1 GE Mgmt"
            # Name: "power supply 1", DESCR: "ASA 5545-X/5555-X AC Power Supply"
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                dict_name = ret_dict.setdefault(groups['name'], {})
                dict_name.update({'description': groups['description']})
                continue

            # PID: ASA5555, VID: V01, SN: AAAAA11111
            # PID: AAA-AAA-AAA, VID: N/A, SN: AAA111
            # PID: N/A, VID: N/A, SN: AAAAA11111
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                pid = groups['pid']
                pid = pid.replace(' ','')
                vid = groups['vid']
                vid = vid.replace(' ','')
                sn = groups['sn']
                sn = sn.replace(' ','')
                dict_name.update({'pid': pid})
                dict_name.update({'vid': vid})
                dict_name.update({'sn': sn})
                continue

        return ret_dict
