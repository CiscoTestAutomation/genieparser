'''
IOSXE C9350 parsers for the following show commands: 
show_switch.py
'''
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any

# import parser utils
from genie.libs.parser.utils.common import Common

class ShowSwitchStackPortSummarySchema(MetaParser):
    """Schema for ShowSwitchStackPortSummary"""

    schema = {
        'stackports': {
            Any(): {
                'port_status': str,
                'neighbor': str,
                'cable_length': str,
                'link_ok': str,
                'link_active': str,
                'sync_ok': str,
                'link_changes_count': int,
                'in_loopback': str,
            }
        }
    }

class ShowSwitchStackPortSummary(ShowSwitchStackPortSummarySchema):
    """
    Parser for:
        * show switch stack-port summary
    """

    cli_command = ['show switch stack-ports summary']
    
    def cli(self, output=None):
        if not output:
            # get output from device
            output = self.device.execute(self.cli_command[0])

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        # 1/1        OK           2/2         50cm           Yes       Yes           Yes       1                   No
        
        p1 = re.compile(r"^(?P<stackport_id>\S+)"
                        r" +(?P<port_status>\w+)"
                        r" +(?P<neighbor>\S+)"
                        r" +(?P<cable_length>\w+)"
                        r" +(?P<link_ok>\w+)"
                        r" +(?P<link_active>\w+)"
                        r" +(?P<sync_ok>\w+)"
                        r" +(?P<link_changes_count>\d+)"
                        r" +(?P<in_loopback>\w+)$")
        
        for line in output.splitlines():
           line = line.strip()
 
           # Sw#/Port#  Port Status  Neighbor  Cable Length   Link OK   Link Active   Sync OK   #Changes to LinkOK  In Loopback
           # -------------------------------------------------------------------------------------------------------------------
           # 1/1        OK           2/2            50cm           Yes       Yes           Yes       1                   No
           # 1/2        OK           3/1            50cm           Yes       Yes           Yes       1                   No
           # 2/1        OK           3/2            50cm           Yes       Yes           Yes       1                   No
           # 2/2        OK           1/1            50cm           Yes       Yes           Yes       1                   No
           # 3/1        OK           1/2            50cm           Yes       Yes           Yes       1                   No
           # 3/2        OK           2/1            50cm           Yes       Yes           Yes       1                   No
           m = p1.match(line)
           if m:
                group = m.groupdict()
                stackport_dict = ret_dict.setdefault('stackports', {}).setdefault(group['stackport_id'], {})
                stackport_dict['port_status'] = group['port_status']
                stackport_dict['neighbor'] = group['neighbor']
                stackport_dict['cable_length'] = group['cable_length']
                stackport_dict['link_ok'] = group['link_ok']
                stackport_dict['link_active'] = group['link_active']
                stackport_dict['sync_ok'] = group['sync_ok']
                stackport_dict['link_changes_count'] = int(group['link_changes_count'])
                stackport_dict['in_loopback'] = group['in_loopback']              
                continue 
        return ret_dict
