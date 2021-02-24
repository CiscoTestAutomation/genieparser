''' show_switch_stackports_summary.py


'''
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any

# import parser utils
from genie.libs.parser.utils.common import Common

class ShowSwitchStackPortsSummarySchema(MetaParser):
    """Schema for ShowSwitchStackPortsSummary"""

    schema = {
        'stackports': {
            Any(): {
                'stackport_id': str,
                'port_status': str,
                'neighbor': int,
                'cable_length': str,
                'link_ok': str,
                'link_active': str,
                'sync_ok': str,
                'link_changes_count': int,
                'in_loopback': str,
            }
        }
    }

class ShowSwitchStackPortsSummary(ShowSwitchStackPortsSummarySchema):
    """
    Parser for:
        * show switch stack-ports summary
    """

    cli_command = ['show switch stack-ports summary']

    def cli(self, output=None):
        if not output:
            # get output from device
            output = self.device.execute(self.cli_command[0])
        # else:
        #     output = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        # 1/1        OK           2         50cm           Yes       Yes           Yes       1                   No
        
        # index = 0

        p1 = re.compile(r"^(?P<stackport_id>\S+)"
                        " +(?P<port_status>\w+)"
                        " +(?P<neighbor>[\d+])"
                        " +(?P<cable_length>\w+)"
                        " +(?P<link_ok>\w+)"
                        " +(?P<link_active>\w+)"
                        " +(?P<sync_ok>\w+)"
                        " +(?P<link_changes_count>\d+)"
                        " +(?P<in_loopback>\w+)")

        for line in output.splitlines():
            line = line.strip()
               
            # Sw#/Port#  Port Status  Neighbor  Cable Length   Link OK   Link Active   Sync OK   #Changes to LinkOK  In Loopback 
            # -------------------------------------------------------------------------------------------------------------------
            # 1/1        OK           2         50cm           Yes       Yes           Yes       1                   No           
            # 1/2        OK           6         100cm          Yes       Yes           Yes       1                   No           
            # 2/1        OK           3         50cm           Yes       Yes           Yes       1                   No           
      
            m = p1.match(line)
            if m:
                stackport_id = m.groupdict()['stackport_id']
                if 'stackports' not in ret_dict:
                    ret_dict['stackports'] = {}

                if stackport_id not in ret_dict:
                    ret_dict['stackports'][stackport_id] = {}

                ret_dict['stackports'][stackport_id]['stackport_id'] = stackport_id
                ret_dict['stackports'][stackport_id]['port_status'] = m.groupdict()['port_status']
                ret_dict['stackports'][stackport_id]['neighbor'] = int(m.groupdict()['neighbor'])
                ret_dict['stackports'][stackport_id]['cable_length'] = m.groupdict()['cable_length']
                ret_dict['stackports'][stackport_id]['link_ok'] = m.groupdict()['link_ok']
                ret_dict['stackports'][stackport_id]['link_active'] = m.groupdict()['link_active']
                ret_dict['stackports'][stackport_id]['sync_ok'] = m.groupdict()['sync_ok']
                ret_dict['stackports'][stackport_id]['link_changes_count'] = int(m.groupdict()['link_changes_count'])
                ret_dict['stackports'][stackport_id]['in_loopback'] = m.groupdict()['in_loopback']
                                
                continue
        return ret_dict