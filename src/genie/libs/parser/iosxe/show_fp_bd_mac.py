''' show_fp_bd_mac.py

IOSXE parsers for the following show commands:

    * show platform software bridge-domain Fp active <bd_id> mac-table
    * show platform software bridge-domain Fp active <bd_id> mac-table <mac_address>

Copyright (c) 2021 by Cisco Systems, Inc.
All rights reserved.
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional, Any

# import parser utils
from genie.libs.parser.utils.common import Common

# ====================================
# Parser for 'show platform software bridge-domain Fp active <bd_id> mac-table'
# ====================================
class ShowFpBdMacSchema(MetaParser):
    """Schema for show platform software bridge-domain Fp active <bd_id> mac-table 
                  show platform software bridge-domain Fp active <bd_id> mac-table <mac_address>"""

    schema = {
        'mac': {
            Any(): {
                'bd_id': int,
                'nhop_type': str,
                Optional('nhop_name'): str,
                Optional('nhop_idx'): str,
                'flags': str,
            }
        }
    }


class ShowFpBdMac(ShowFpBdMacSchema):
    """Parser for show platform software bridge-domain Fp active <bd_id> mac-table 
                  show platform software bridge-domain Fp active <bd_id> mac-table <mac_address>"""

    cli_command = ['show platform software bridge-domain Fp active {bd_id} mac-table',
                   'show platform software bridge-domain Fp active {bd_id} mac-table {mac_address}']

    def cli(self, bd_id=None, mac_address=None, output=None):
    
        cli = self.cli_command
        
        if output is None:
            if mac_address:
                cli = self.cli_command[1].format(bd_id=bd_id, mac_address=mac_address)
            else:
                cli = self.cli_command[0].format(bd_id=bd_id)
            output = self.device.execute(cli)

        # initial return dictionary
        ret_dict = {}

        # MAC               BD        Nhop Type   Nhop Name/Idx                             Flags
        p1 = re.compile(r'^MAC +BD +Nhop +Type +Nhop +Name\/Idx +Flags$')

        # ffff.ffff.fffe    111       olist       0x297c                                    none
        p2 = re.compile(r'^(?P<mac>[\d\.a-fA-F]+) +(?P<bd_id>[\d]+) +(?P<nhop_type>\w+) +(?P<nhop_idx>0x[\w\d]+) +(?P<flags>\w+)$')

        # aabb.0000.0011    111       efp         GigabitEthernet6.EFP111                   none
        p3 = re.compile(r'^(?P<mac>[\d\.a-fA-F]+) +(?P<bd_id>[\d]+) +(?P<nhop_type>[\w]+) +(?P<nhop_name>[\w\d\.\/]+) +(?P<flags>\w+)$')

        # aabb.0000.0021    111       oce         EVPN(0xe8bd90a0)/0xa9f                    none
        p4 = re.compile(r'^(?P<mac>[\d\.a-fA-F]+) +(?P<bd_id>[\d]+) +(?P<nhop_type>\w+) +(?P<nhop_name>[\w\d\.\(\)]+)+\/+(?P<nhop_idx>0x[\w\d]+) +(?P<flags>\w+)$')

        for line in output.splitlines():
            line = line.strip()

            # MAC               BD        Nhop Type   Nhop Name/Idx                             Flags
            m = p1.match(line)
            if m:
                macs_dict = ret_dict.setdefault('mac', {})
                continue

            # ffff.ffff.fffe    111       olist       0x297c                                    none
            m = p2.match(line)
            if m:
                group = m.groupdict()
                mac_dict = macs_dict.setdefault(group['mac'], {})
                mac_dict.update({
                    'bd_id': int(group['bd_id']),
                    'nhop_type': group['nhop_type'],
                    'nhop_idx': group['nhop_idx'],
                    'flags': group['flags']
                })
                continue

            # aabb.0000.0011    111       efp         GigabitEthernet6.EFP111                   none
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict['mac'][group['mac']] = {}
                mac_dict = macs_dict.setdefault(group['mac'], {})
                mac_dict.update({
                    'bd_id': int(group['bd_id']),
                    'nhop_type': group['nhop_type'],
                    'nhop_name': group['nhop_name'],
                    'flags': group['flags']
                })
                continue

            # aabb.0000.0021    111       oce         EVPN(0xe8bd90a0)/0xa9f                    none
            m = p4.match(line)
            if m:
                group = m.groupdict()
                mac_dict = macs_dict.setdefault(group['mac'], {})
                mac_dict.update({
                    'bd_id': int(group['bd_id']),
                    'nhop_type': group['nhop_type'],
                    'nhop_name': group['nhop_name'],
                    'nhop_idx': group['nhop_idx'],
                    'flags': group['flags']
                })
                continue

        return ret_dict
