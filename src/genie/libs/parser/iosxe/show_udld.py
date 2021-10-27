"""  show_udld.py

IOSXE parsers for the following show command:

    * 'show udld interface {interface}'
    * 'show udld neighbor'

"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional,Or

# import parser utils
from genie.libs.parser.utils.common import Common

class ShowUdldInterfaceSchema(MetaParser):
    """Schema for 
        * show udld {interface}
    """

    schema = {
        'interfaces': {
            Any(): {
                'port_enable_administrative_configuration_setting' : str,
                'port_enable_operational_state' : str,
                'current_bidirectional_state' : str,
            },       
        }
    }


class ShowUdldInterface(ShowUdldInterfaceSchema):               
    """Parser for 
        * show udld {interface}
    """

    cli_command = ['show udld {interface}']

    def cli(self, interface="", output=None):
        if output is None:
            cmd = self.cli_command[0].format(interface = interface)
            output = self.device.execute(cmd)
        
        ret_dict = {}
        #Interface Gi1/0/7
        p1 = re.compile(r"^Interface\s+(?P<interface>[\w/]+)$")

        #Port enable administrative configuration setting: Enabled
        p2 = re.compile(r"^Port+\s+enable+\s+administrative+\s+configuration+\s+setting:+\s+(?P<port_enable_administrative_configuration_setting>\w+)$")
        
        #Port enable operational state: Enabled
        p3 = re.compile(r"^Port+\s+enable+\s+operational+\s+state:+\s+(?P<port_enable_operational_state>\w+)$")

        #Current bidirectional state: Bidirectional
        p4 = re.compile(r"^Current+\s+bidirectional+\s+state:+\s+(?P<current_bidirectional_state>\w+)$")

        #Port enable administrative configuration setting: Enabled / in alert mode
        p5 = re.compile(r"^Port+\s+enable+\s+administrative+\s+configuration+\s+setting:+\s+(?P<port_enable_administrative_configuration_setting>(\w+\s+\/+\s+\w+\s+\w+\s+\w+))$")
        
        #Port enable operational state: Enabled / in alert mode
        p6 = re.compile(r"^Port+\s+enable+\s+operational+\s+state:+\s+(?P<port_enable_operational_state>(\w+\s+\/+\s+\w+\s+\w+\s+\w+))$")


        for line in output.splitlines():
            line = line.strip()

            #Interface Gi1/0/15
            m = p1.match(line)
            if m:
                interface = Common.convert_intf_name(m.group(1))
                ret_dict.setdefault('interfaces', {})\
                    .setdefault(interface, {})
                stack_dict1 = ret_dict['interfaces'][interface]
                continue

            #Port enable administrative configuration setting: Enabled
            m = p2.match(line)
            if m:
                stack_dict1['port_enable_administrative_configuration_setting'] = m.group('port_enable_administrative_configuration_setting')
                continue

            #Port enable operational state: Enabled
            m = p3.match(line)
            if m:
                stack_dict1['port_enable_operational_state'] = m.group('port_enable_operational_state')
                continue

            # Current bidirectional state: Bidirectional
            m = p4.match(line)
            if m:
                stack_dict1['current_bidirectional_state'] = m.group('current_bidirectional_state')
                continue
            
            #Port enable administrative configuration setting: Enabled / in alert mode
            m = p5.match(line)
            if m:
                stack_dict1['port_enable_administrative_configuration_setting'] = m.group('port_enable_administrative_configuration_setting')
                continue

            #Port enable operational state: Enabled / in alert mode
            m = p6.match(line)
            if m:
                stack_dict1['port_enable_operational_state'] = m.group('port_enable_operational_state')
                continue

        return ret_dict


class ShowUdldNeighborSchema(MetaParser):
    """Schema for 
        * show udld neighbor
    """

    schema = {
        'interfaces': {
            Any() : {
                'device_name' : str,
                'device_id' : str,
                'port_id' : str,
                'neighbor_state' : str,
            },
        },
        'total_number_of_bidirectional_entries_displayed' : int,
    }


class ShowUdldNeighbor(ShowUdldNeighborSchema):
    """Parser for 
        * show udld neighbor
    """

    cli_command = ['show udld neighbor']

    def cli(self, output=None):
        if output is None:
            cmd = self.cli_command[0]
            output = self.device.execute(cmd)
        
        ret_dict = {}
        
        #Gi1/0/13       9077EEFE7F0     1            70:D3:79:84:69:        Bidirectional
        p1 = re.compile(r'^(?P<port>\w+\/\d+\/\d+) *'
                        r'(?P<device_name>\w+) +'
                        r'(?P<device_id>\w+) +'
                        r'(?P<port_id>([a-fA-F\d]{2}:){5}) +'
                        r'(?P<neighbor_state>\w+)$')

        #Total number of bidirectional entries displayed: 1
        p2 = re.compile(r"^Total+\s+number+\s+of+\s+bidirectional+\s+entries+\s+displayed:+\s+(?P<total_number_of_bidirectional_entries_displayed>\d+)$")
        
                                
        for line in output.splitlines():
            line = line.strip()
        #Gi1/0/13       9077EEFE7F0     1            Gi1/0/15        Bidirectional    
            m = p1.match(line)
            if m:
                group = m.groupdict()
                port = Common.convert_intf_name(group.pop('port'))
                stack_dict_1 = ret_dict.setdefault('interfaces', {}).setdefault(port, {})
                stack_dict_1.update({k:v for k, v in group.items()})
                continue
                
        #Total number of bidirectional entries displayed: 1
            m = p2.match(line)
            if m:
                ret_dict['total_number_of_bidirectional_entries_displayed'] = int(m.group('total_number_of_bidirectional_entries_displayed'))
                continue

        return ret_dict
