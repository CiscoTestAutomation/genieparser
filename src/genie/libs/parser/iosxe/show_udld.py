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
                Optional('current_bidirectional_state') : str,
                Optional('current_operational_state'): str,
                Optional('message_interval_ms') : int,
                Optional('time_out_interval_ms'): int,
                Optional('port_fast_hello_configuration_setting'): str,
                Optional('port_fast_hello_interval_ms'): int,
                Optional('port_fast_hello_operational_state'): str,
                Optional('neighbor_fast_hello_configuration_setting'): str,
                Optional('neighbor_fast_hello_interval'): str,
                Optional('entries') : {
                    Any() : {
                        Optional('expiration_time_ms'): int,
                        Optional('cache_device_index'): int,
                        Optional('current_neighbor_state'): str,
                        Optional('device_id'): str,
                        Optional('port_id'): str,
                        Optional('neighbor_echo_1_device'): str,
                        Optional('neighbor_echo_1_port'): str,
                        Optional('tlv_message_interval_sec'): int,
                    
                    },
                },       
            },
        },
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
        p1 = re.compile(r"^Interface\s(?P<interface>[\w/]+)$")

        #Port enable administrative configuration setting: Enabled
        p2 = re.compile(r"^Port\s+enable\s+administrative\s+configuration\s+setting:\s+(?P<port_enable_administrative_configuration_setting>\w+)$")
        
        #Port enable operational state: Enabled
        p3 = re.compile(r"^Port\s+enable\s+operational\s+state:\s+(?P<port_enable_operational_state>\w+)$")

        #Current bidirectional state: Bidirectional
        p4 = re.compile(r"^Current\s+bidirectional\s+state:\s+(?P<current_bidirectional_state>\w+)$")

        #Port enable administrative configuration setting: Enabled / in alert mode
        p5 = re.compile(r"^Port\s+enable\s+administrative\s+configuration\s+setting:\s+(?P<port_enable_administrative_configuration_setting>.+)$")
        
        #Port enable operational state: Enabled / in alert mode
        p6 = re.compile(r"^Port\s+enable\s+operational\s+state:\s+(?P<port_enable_operational_state>.+)$")
        
        # Current operational state: Advertisement - Single neighbor detected
        p7 = re.compile(r"^Current\s+operational\s+state:\s+(?P<current_operational_state>.+)$")
        
        # Message interval: 15000 ms
        p8 = re.compile(r"^Message\s+interval:\s+(?P<message_interval_ms>\d+)")
        
        # Time out interval: 5000 ms
        p9 = re.compile(r"^Time\s+out\s+interval:\s+(?P<time_out_interval_ms>\d+)")
        
        # Port fast-hello configuration setting: Disabled
        p10 = re.compile(r"^Port\s+fast+\-+hello\s+configuration\s+setting:\s+(?P<port_fast_hello_configuration_setting>\w+)$")
        
        # Port fast-hello interval: 0 ms
        p11 = re.compile(r"^Port\s+fast+\-+hello\s+interval:\s+(?P<port_fast_hello_interval_ms>\d+)")
        
        # Port fast-hello operational state: Disabled
        p12 = re.compile(r"^Port\s+fast+\-+hello\s+operational\s+state:\s+(?P<port_fast_hello_operational_state>\w+)$")
        
        # Neighbor fast-hello configuration setting: Disabled
        p13 = re.compile(r"^Neighbor\s+fast+\-+hello\s+configuration\s+setting:\s+(?P<neighbor_fast_hello_configuration_setting>\w+)$")
        
        # Neighbor fast-hello interval: Unknown
        p14 = re.compile(r"^Neighbor\s+fast+\-+hello\s+interval:\s+(?P<neighbor_fast_hello_interval>\w+)$")
        
        # Entry 1
        p15 = re.compile(r"^Entry\s+1$")

        # Expiration time: 42600 ms
        p16 = re.compile(r"^Expiration\s+time:\s+(?P<expiration_time_ms>\d+)")
        
        # Cache Device index: 1
        p17 = re.compile(r"^Cache\s+Device\s+index:\s+(?P<cache_device_index>\d+)$")
        
        # Current neighbor state: Bidirectional
        p18 = re.compile(r"^Current\s+neighbor\s+state:\s+(?P<current_neighbor_state>\w+)$")
        
        # Device ID: A4B43937780
        p19 = re.compile(r"^Device\s+ID:\s+(?P<device_id>\w+)$")
        
        # Port ID: A4:B4:39:37:78:00/7
        p20 = re.compile(r"^Port\s+ID:\s+(?P<port_id>([a-fA-F\d]{2}:){5}[a-fA-F\d]{2}\/\d+)$")
        
        # Neighbor echo 1 device: 70D37984690
        p21 = re.compile(r"^Neighbor\s+echo\s+1\s+device:\s+(?P<neighbor_echo_1_device>\w+)$")
        
        # Neighbor echo 1 port: 70:D3:79:84:69:00/7
        p22 = re.compile(r"^Neighbor\s+echo\s+1\s+port:\s+(?P<neighbor_echo_1_port>([a-fA-F\d]{2}:){5}[a-fA-F\d]{2}\/\d+)$")
        
        # TLV Message interval: 15 sec
        p23 = re.compile(r"^TLV\s+Message\s+interval:\s+(?P<tlv_message_interval_sec>\d+)")
        
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
            
            # Current operational state: Advertisement - Single neighbor detected
            m = p7.match(line)
            if m:
                stack_dict1['current_operational_state'] = m.group('current_operational_state')
                continue
        
            # Message interval: 15000 ms
            m = p8.match(line)
            if m:
                stack_dict1['message_interval_ms'] = int(m.group('message_interval_ms'))
                continue
            
            # Time out interval: 5000 ms
            m = p9.match(line)
            if m:
                stack_dict1['time_out_interval_ms'] = int(m.group('time_out_interval_ms'))
                continue

            # Port fast-hello configuration setting: Disabled
            m = p10.match(line)
            if m:
                stack_dict1['port_fast_hello_configuration_setting'] = m.group('port_fast_hello_configuration_setting')
                continue
            
            # Port fast-hello interval: 0 ms
            m = p11.match(line)
            if m:   
                stack_dict1['port_fast_hello_interval_ms'] = int(m.group('port_fast_hello_interval_ms'))
                continue
            
            # Port fast-hello operational state: Disabled
            m = p12.match(line)
            if m:
                stack_dict1['port_fast_hello_operational_state'] = m.group('port_fast_hello_operational_state')
                continue
            
            # Neighbor fast-hello configuration setting: Disabled
            m = p13.match(line)
            if m:
                stack_dict1['neighbor_fast_hello_configuration_setting'] = m.group('neighbor_fast_hello_configuration_setting')
                continue
            
            # Neighbor fast-hello interval: Unknown
            m = p14.match(line)
            if m:
                stack_dict1['neighbor_fast_hello_interval'] = m.group('neighbor_fast_hello_interval')
                continue
            
            # Entry 1
            m = p15.match(line)
            if m:
                entry = m.group()
                entry = int(entry[-1])
                stack_dict1.setdefault('entries', {})\
                    .setdefault(entry, {})
                stack_dict2 = stack_dict1['entries'][entry]
                continue
            
            # Expiration time: 42600 ms
            m = p16.match(line)
            if m:
                stack_dict2['expiration_time_ms'] = int(m.group('expiration_time_ms'))
                continue
            
            # Cache Device index: 1
            m = p17.match(line)
            if m:
                stack_dict2['cache_device_index'] = int(m.group('cache_device_index'))
                continue
            
            # Current neighbor state: Bidirectional
            m = p18.match(line)
            if m:
                stack_dict2['current_neighbor_state'] = m.group('current_neighbor_state')
                continue
            
            # Device ID: A4B43937780
            m = p19.match(line)
            if m:
                stack_dict2['device_id'] = m.group('device_id')
                continue
            
            # Port ID: A4:B4:39:37:78:00/7
            m = p20.match(line)
            if m:
                stack_dict2['port_id'] = m.group('port_id')
                continue
            
            # Neighbor echo 1 device: 70D37984690
            m = p21.match(line)
            if m:
                stack_dict2['neighbor_echo_1_device'] = m.group('neighbor_echo_1_device')
                continue
            
            # Neighbor echo 1 port: 70:D3:79:84:69:00/7
            m = p22.match(line)
            if m:
                stack_dict2['neighbor_echo_1_port'] = m.group('neighbor_echo_1_port')
                continue

            # TLV Message interval: 15 sec
            m = p23.match(line)
            if m:
                stack_dict2['tlv_message_interval_sec'] = int(m.group('tlv_message_interval_sec'))
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
        p2 = re.compile(r"^Total\s+number\s+of\s+bidirectional\s+entries\s+displayed:\s+(?P<total_number_of_bidirectional_entries_displayed>\d+)$")
        
                                
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
