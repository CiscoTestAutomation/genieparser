'''  show_meraki.py

IOSXE parsers for the following show command:

    * 'show meraki'
    * 'show meraki connect'

'''

# Python
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional
from genie.metaparser.util.schemaengine import (Schema, Any, Optional, Or, And, Default, Use, ListOf)

# import parser utils
from genie.libs.parser.utils.common import Common


class ShowMerakiSchema(MetaParser):
    """ Schema for:
        * 'show meraki'
        * 'show meraki switch {switch}'
    """ 

    schema = {
        'meraki': {
            'switch': {
                Any(): {
                    'switch_num': int,
                    'pid': str,
                    'serial_number': str,
                    'meraki_sn': str,
                    'mac_addr': str,
                    'conversion_status': str, 
                    'current_mode': str   
                }, 
            }, 
        },
    }


class ShowMeraki(ShowMerakiSchema):
    '''Parser for:
        * 'show meraki'
        * 'show meraki switch {switch}'
    '''

    cli_command = ['show meraki', 'show meraki switch {switch}']

    def cli(self, switch = '', output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[1].format(switch=switch)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # 1       C9300-24T  FJC2311T0DA Q5EE-DJYN-CRGR  4cbc.4812.3550   Registered         C9K-C
        # 2       C9300-24U  FJC1527A0BC N/A             4cbc.4812.2881   ACT2 write failed  C9K-C
        # 3       C9300-48UX FJC2317T0DT Q3EA-AZYP-WDFH  4cbc.4812.2501   Registered         C9K-C
        # 4       C9300-48TX FJC2311T0AJ N/A             5cbc.4812.3479   N/A                C9K-C
        # 1   C9300-24UX         FCW2248D19Q    Q5TD-GJZW-GLBA  0029.c29a.8e00    Registered   C9K-C [Monitoring]
        p1 = re.compile(r'^(?P<switch_num>\d+)\s+(?P<pid>[\w-]+)\s+(?P<serial_number>[\w]+)\s+(?P<meraki_sn>[\w\/-]+)\s+(?P<mac_addr>[\w\.:]+)\s+(?P<conversion_status>[\w\s\/-]+)\s+(?P<current_mode>[\w\-]+(\s\[[\w\s]+\])?)$')
        
        # 1   MS390-24U          Q3EC-CTH2-U    N/A             N/A               N/A          C9K-C
        # 1   MS390-24U          Q3EC-CTH2-U    N/A             N/A               N/A          C9K-C [Monitoring]
        p2 = re.compile(r'^(?P<switch_num>\d+)\s+(?P<pid>[\w-]+)\s+(?P<serial_number>[\w\/-]+)\s+(?P<meraki_sn>\w\/\w)\s+(?P<mac_addr>\w\/\w)\s+(?P<conversion_status>\w\/\w)\s+(?P<current_mode>[\w\-]+(\s\[[\w\s]+\])?)$')

        parsed_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # 1       C9300-24T  FJC2311T0DA Q5EE-DJYN-CRGR  4cbc.4812.3550   Registered         C9K-C
            # 2       C9300-24U  FJC1527A0BC N/A             4cbc.4812.2881   ACT2 write failed  C9K-C
            # 3       C9300-48UX FJC2317T0DT Q3EA-AZYP-WDFH  4cbc.4812.2501   Registered         C9K-C
            # 4       C9300-48TX FJC2311T0AJ N/A             5cbc.4812.3479   N/A                C9K-C
            m = p1.match(line)
            if m:
                group = m.groupdict()
                device_dict = parsed_dict.setdefault('meraki', {}) \
                    .setdefault('switch', {}).setdefault(group['switch_num'], {})
                device_dict['switch_num'] = int(group['switch_num'])
                device_dict['pid'] = group['pid']
                device_dict['serial_number'] = group['serial_number']
                device_dict['meraki_sn'] = group['meraki_sn']
                device_dict['mac_addr'] = group['mac_addr']
                device_dict['conversion_status'] = group['conversion_status'].strip()
                device_dict['current_mode'] = group['current_mode']
                continue
            
            # 1   MS390-24U          Q3EC-CTH2-U    N/A             N/A               N/A          C9K-C
            m = p2.match(line)
            if m:
                group = m.groupdict()
                device_dict = parsed_dict.setdefault('meraki', {}) \
                    .setdefault('switch', {}).setdefault(group['switch_num'], {})
                device_dict['switch_num'] = int(group['switch_num'])
                device_dict['pid'] = group['pid']
                device_dict['serial_number'] = group['serial_number']
                device_dict['meraki_sn'] = group['meraki_sn']
                device_dict['mac_addr'] = group['mac_addr']
                device_dict['conversion_status'] = group['conversion_status'].strip()
                device_dict['current_mode'] = group['current_mode']
                continue
        
        return parsed_dict


class ShowMerakiConnectSchema(MetaParser):
    """Schema for show meraki connect"""

    schema = {
        'service_meraki_connect': str,
        Optional('meraki_tunnel_config'): {
            'fetch_state': str,
            Optional('fetch_fail'): str,
            Optional('last_fetch(utc)'): str,
            Optional('next_fetch(utc)'): str,
            Optional('config_server'): str,
            Optional('primary'): str,
            Optional('secondary'): str,
            Optional('client_ipv6_addr'): str,
            Optional('network_name') : str,
        },
        Optional('meraki_tunnel_state'): {
            'primary': str,
            'secondary': str,
            Optional('primary_last_change(utc)'): str,
            Optional('secondary_last_change(utc)'): str,
            Optional('client_last_restart(utc)'): str,
        },
        Optional('meraki_tunnel_interface'): {
            'status': str,
            'rx_packets': int,
            'tx_packets': int,
            'rx_errors': int,
            'tx_errors': int,
            'rx_drop_packets': int,
            'tx_drop_packets': int,
        },
       Optional('meraki_device_registration'):{
        'url': str,
        Optional('devices'): {
            Any(): {
            'pid': str,
            'serial_number': str,
            Optional('meraki_id'): str,
            Optional('cloud_id'): str,
            'mac_address': str,
            'status': str,
            Optional('error'): str,
            'timestamp(utc)': str,
            },
        }
    }
}


class ShowMerakiConnect(ShowMerakiConnectSchema):
    """Parser for show meraki connect"""

    cli_command = 'show meraki connect'

    def cli(self, output=None):
        if output is None:
            cmd = self.cli_command
            out = self.device.execute(cmd)
        else:
            out = output
        #   Service meraki connect: enable
        #   Fetch State:                Config fetch succeeded
        #   Fetch Fail:                 no failure
        #   Last Fetch(UTC):            2023-06-28 11:10:59
        #   Next Fetch(UTC):            2023-06-28 12:27:35
        #   Config Server:              cs556-2037.meraki.com
        #   Primary:                    usw.nt.meraki.com
        #   Secondary:                  use.nt.meraki.com
        #   Client IPv6 Addr:           FD0A:9B09:1F7:1:229:C2FF:FE9A:8E00
        #   Network Name:               meraki admin network - wireless
        
        #   Primary:                    Up
        #   Secondary:                  Up
        #   Primary Last Change(UTC):   2023-06-27 14:19:59
        #   Secondary Last Change(UTC): 2023-06-27 14:19:59
        #   Client Last Restart(UTC):   2023-06-26 18:15:55
        #   Status:                     Enable
        #   Rx Packets:                 949740
        #   Tx Packets:                 221488
        #   Rx Errors:                  0
        #   Tx Errors:                  0
        #   Rx Drop Packets:            0
        #   Tx Drop Packets:            0
        
        #   url:                        https://catalyst.meraki.com/nodes/register
        #   Device Number:              1
        #   PID:                        C9300-24U
        #   Serial Number:              FJC2342S0TH
        #   Meraki ID:                  Q5TC-J9PK-HK4R
        #   Mac Address:                6C:71:0D:3D:EA:80
        #   Status:                     Registered
        #   Timestamp(UTC):             2015-01-04 06:59:22
        #   Cloud ID:                   Q2ZZ-VYED-JVDA
        p1 = re.compile(r"^(?P<key>.+): +(?P<value>.+)$")
        
        # Meraki Tunnel Config
        # Meraki Tunnel State
        # Meraki Tunnel Interface
        # Meraki Device Registration
        p2 = re.compile(r"^(?P<key>[A-Z][a-z]+(\s+[A-Z][a-z]+)+)$")
        
        #service meraki connect is disabled
        p3 = re.compile(r"^(service\s+meraki\s+connect)\s+is\s+(disabled)$")
        
        ret_dict = {} #level-0 dictionary
        stack_dict_index = 0 #level-1 dictionary
        stack_dict_1_index = 0 #level-2 dictionary

        for line in out.splitlines():
            #   Service meraki connect: enable
            #   Fetch State:                Config fetch succeeded
            #   Fetch Fail:                 no failure
            #   Last Fetch(UTC):            2023-06-28 11:10:59
            #   Next Fetch(UTC):            2023-06-28 12:27:35
            #   Config Server:              cs556-2037.meraki.com
            #   Primary:                    usw.nt.meraki.com
            #   Secondary:                  use.nt.meraki.com
            #   Client IPv6 Addr:           FD0A:9B09:1F7:1:229:C2FF:FE9A:8E00
            #   Network Name:               meraki admin network - wireless
            
            #   Primary:                    Up
            #   Secondary:                  Up
            #   Primary Last Change(UTC):   2023-06-27 14:19:59
            #   Secondary Last Change(UTC): 2023-06-27 14:19:59
            #   Client Last Restart(UTC):   2023-06-26 18:15:55
            #   Status:                     Enable
            #   Rx Packets:                 949740
            #   Tx Packets:                 221488
            #   Rx Errors:                  0
            #   Tx Errors:                  0
            #   Rx Drop Packets:            0
            #   Tx Drop Packets:            0
            
            #   url:                        https://catalyst.meraki.com/nodes/register
            #   Device Number:              1
            #   PID:                        C9300-24U
            #   Serial Number:              FJC2342S0TH
            #   Meraki ID:                  Q5TC-J9PK-HK4R
            #   Mac Address:                6C:71:0D:3D:EA:80
            #   Status:                     Registered
            #   Timestamp(UTC):             2015-01-04 06:59:22
            #   Cloud ID:                   Q2ZZ-VYED-JVDA
                
            m1 = p1.match(line)
            if m1:
                # Extract matched groups from the regex match object
                dict_val = m1.groupdict()
                # Process the key and value from the matched groups
                key_converted_to_lowercase_with_underscore = dict_val['key'].strip().replace(' ', '_').lower()
                value = dict_val['value'].strip()
                # Check if stack_dict_index is greater than 0
                if stack_dict_index > 0:
                    # Check if the key is 'device_number' to create new parent dictionary 'device_number' level-2 under 'meraki_device_registration'     
                    if key_converted_to_lowercase_with_underscore == 'device_number': 
                        # Set up dictionary structure for devices according to switch number
                        stack_dict.setdefault('devices', {}).setdefault(value, {})
                        stack_dict_1 = stack_dict['devices'][value]
                        stack_dict_1_index += 1
                    # Check if stack_dict_1_index is greater than 0 then parent dictionary will be 'device_number' level-2
                    elif stack_dict_1_index > 0:
                        stack_dict_1[key_converted_to_lowercase_with_underscore] = int(value) if value.isdigit() else value
                    # Update stack_dict with key-value pair then parent dictionary will be level-1 
                    else:
                        stack_dict[key_converted_to_lowercase_with_underscore] = int(value) if value.isdigit() else value
                else:
                    # Update ret_dict with key-value pair then parent dictionary will be level-0
                    ret_dict[key_converted_to_lowercase_with_underscore] = int(value) if value.isdigit() else value
            
            # Meraki Tunnel Config
            # Meraki Tunnel State
            # Meraki Tunnel Interface
            # Meraki Device Registration      
            
            m2 = p2.match(line)
            if m2:
                dict_val = m2.groupdict()
                key_converted_to_lowercase_with_underscore = dict_val['key'].strip().replace(' ', '_').lower()
                # Update ret_dict with new parent dictionary will be level-1
                ret_dict.setdefault(key_converted_to_lowercase_with_underscore, {})
                stack_dict = ret_dict[key_converted_to_lowercase_with_underscore]
                stack_dict_index += 1
                continue 
            
            m3  = p3.match(line)
            if m3:
                key_converted_to_lowercase_with_underscore = m3.group(1).strip().replace(' ', '_').lower()
                #if meraki mode is disabled append the key-value pair to ret_dict level-0
                ret_dict[key_converted_to_lowercase_with_underscore] = m3.group(2)
                continue
            
        return ret_dict
