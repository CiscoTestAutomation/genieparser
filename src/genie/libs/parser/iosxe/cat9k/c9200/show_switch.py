''' 
show switch stack-ports summary
show switch stack-ports
'''
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any

# import parser utils

class ShowSwitchStackPortsSummarySchema(MetaParser):
    """Schema for ShowSwitchStackPortsSummary"""

    schema = {
        'stackports': {
            Any(): {
                'stackport_id': str,
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

class ShowSwitchStackPortsSummary(ShowSwitchStackPortsSummarySchema):
    """
    Parser for:
        * show switch stack-ports summary
    """
    cli_command = ['show switch stack-ports summary']

    def cli(self, output=None):
        if not output:
            output = self.device.execute(self.cli_command[0])
        
        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        # 1/1        OK           2/2            50cm           Yes       Yes           Yes       3                   No
        
        p1 = re.compile(r"^(?P<stackport_id>\S+)\s+"  
                r"(?P<port_status>\w+)\s+"  
                r"(?P<neighbor>\S+)\s+"  
                r"(?P<cable_length>\S+)\s+"  
                r"(?P<link_ok>\w+)\s+"  
                r"(?P<link_active>\w+)\s+"  
                r"(?P<sync_ok>\w+)\s+"  
                r"(?P<link_changes_count>\d+)\s+"  
                r"(?P<in_loopback>\w+)$")

        for line in output.splitlines():
            line = line.strip()
               
            # Sw#/Port#  Port Status  Neighbor  Cable Length   Link OK   Link Active   Sync OK   #Changes to LinkOK  In Loopback 
            # -------------------------------------------------------------------------------------------------------------------
            # 1/1        OK           2/2            50cm           Yes       Yes           Yes       3                   No                   No           
            # 1/2        OK           3/1            100cm          Yes       Yes           Yes       1                   No                   No      
      
            m = p1.match(line)
            if m:
                stackport_id = m.groupdict()['stackport_id']
                if 'stackports' not in ret_dict:
                    ret_dict['stackports'] = {}

                if stackport_id not in ret_dict:
                    ret_dict['stackports'][stackport_id] = {}

                ret_dict['stackports'][stackport_id]['stackport_id'] = stackport_id
                ret_dict['stackports'][stackport_id]['port_status'] = m.groupdict()['port_status']
                ret_dict['stackports'][stackport_id]['neighbor'] = m.groupdict()['neighbor']
                ret_dict['stackports'][stackport_id]['cable_length'] = m.groupdict()['cable_length']
                ret_dict['stackports'][stackport_id]['link_ok'] = m.groupdict()['link_ok']
                ret_dict['stackports'][stackport_id]['link_active'] = m.groupdict()['link_active']
                ret_dict['stackports'][stackport_id]['sync_ok'] = m.groupdict()['sync_ok']
                ret_dict['stackports'][stackport_id]['link_changes_count'] = int(m.groupdict()['link_changes_count'])
                ret_dict['stackports'][stackport_id]['in_loopback'] = m.groupdict()['in_loopback']
                                
                continue
        return ret_dict
