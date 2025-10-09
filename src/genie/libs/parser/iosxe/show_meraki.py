'''  show_meraki.py

IOSXE parsers for the following show command:

    * 'show meraki'
    * 'show meraki connect'
    * 'show meraki config monitor'
    * 'show meraki config updater'
    * 'show meraki migration'

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
    '''
    Parser for:
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

        # 1   MS390-24UX         Q3ED-6UWS-6TLX     N/A  N/A   N/A   C9K-C
        # 1   MS390-24UX         Q3ED-6UWS-6TLX     N/A  N/A   N/A   C9K-C[Monitoring]
        p2 = re.compile(r'^(?P<switch_num>\d+)\s+(?P<pid>[\w-]+)\s+(?P<serial_number>[\w\/-]+)\s+(?P<meraki_sn>[\w\/-]+)\s+(?P<mac_addr>[\w\/.:]+)\s+(?P<conversion_status>[\w\/-]+)\s+(?P<current_mode>[\w\-]+(\s\[[\w\s]+\])?)\s*$')

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
            Optional('vrf'): str,
            'status': str,
            'rx_packets': int,
            'tx_packets': int,
            'rx_errors': int,
            'tx_errors': int,
            'rx_drop_packets': int,
            'tx_drop_packets': int,
            Optional('rx_packets_delta'): int,
            Optional('tx_packets_delta'): int,
            Optional('rx_errors_delta'): int,
            Optional('tx_errors_delta'): int,
            Optional('rx_drop_packets_delta'): int,
            Optional('tx_drop_packets_delta'): int,
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
        #   Rx Packets (Last 5s):       18
        #   Tx Packets (Last 5s):       17
        #   Rx Errors (Last 5s):        0
        #   Tx Errors (Last 5s):        0
        #   Rx Drop Packets (Last 5s):  0
        #   Tx Drop Packets (Last 5s):  0

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

        # Pattern to match delta fields "(Last 5s)"
        delta_pattern = re.compile(r'\(last\s+\d+s\)', re.IGNORECASE)

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
            #   Rx Packets (Last 5s):       18
            #   Tx Packets (Last 5s):       17
            #   Rx Errors (Last 5s):        0
            #   Tx Errors (Last 5s):        0
            #   Rx Drop Packets (Last 5s):  0
            #   Tx Drop Packets (Last 5s):  0

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
                key = dict_val['key'].strip()
                
                # Check if the key contains "(last Xsecs)" pattern and convert to delta
                if delta_pattern.search(key):
                    # Remove the "(last Xsecs)" part and add "_delta" suffix
                    key_without_delta = delta_pattern.sub('', key).strip()
                    key_converted_to_lowercase_with_underscore = key_without_delta.replace(' ', '_').lower() + '_delta'
                else:
                    key_converted_to_lowercase_with_underscore = key.replace(' ', '_').lower()
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


class ShowMerakiConfigMonitorSchema(MetaParser):
    """Schema for:
        * 'show meraki config monitor'
    """
    schema = {
        Optional('err_msg'): str,
        Optional('current_state'): str,
        Optional('instances'): {
            Any(): {
                'config_change_time': str,
                'xpaths_seen': int,
                Optional('xpaths'): {
                    Any(): {
                        'path': str,
                        'operation': str,
                    }
                }
            }
        }
    }


class ShowMerakiConfigMonitor(ShowMerakiConfigMonitorSchema):
    """Parser for:
        * 'show meraki config monitor'
    """
    cli_command = "show meraki config monitor"

    def cli(self, output=None):
        if output is None:
            cmd = self.cli_command
            out = self.device.execute(cmd)
        else:
            out = output

        parsed_dict = {}

        # Begin Regex patterns to match output lines
        # service meraki connect is disabled
        p0 = re.compile(r"^(service meraki connect is disabled)$")

        #   Current state:                Ready
        p1 = re.compile(r"^Current state:\s+([A-Za-z].*)$")

        # 1.  Config change (UTC): 2025-04-02 08:03:05
        p2 = re.compile(r"^(\d*)\.\s*Config change \(UTC\):\s+(.*)$")

        #  Total number of xpaths seen: 6
        p3 = re.compile(r"^Total number of xpaths seen:\s+(\d*)$")

        #     XPATH: /ios:native/ios:errdisable/ios:detect/ios:cause/ios:loopdetect
        p4 = re.compile(r"^XPATH:\s+(.*)$")

        #    Operation: Create
        p5 = re.compile(r"^Operation:\s+(.*)$")

        current_section = 0
        current_subsection = 0

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # service meraki connect is disabled
            m = p0.match(line)
            if m:
                parsed_dict['err_msg'] = m.group(1)
                return parsed_dict

            #   Current state:                Ready
            m = p1.match(line)
            if m:
                parsed_dict['current_state'] = m.group(1)
                continue

            # 1.  Config change (UTC): 2025-04-02 08:03:05
            m = p2.match(line)
            if m:
                current_section = int(m.group(1))
                instances_dict = parsed_dict.setdefault('instances', {})
                instances_dict.setdefault(current_section, {})
                instances_dict[current_section]['config_change_time'] = m.group(2)
                current_subsection = 0
                continue

            if current_section:
                #  Total number of xpaths seen: 6
                m = p3.match(line)
                if m:
                    instances_dict[current_section]['xpaths_seen'] = int(m.group(1))
                    instances_dict[current_section].setdefault('xpaths', {})
                    continue

                #     XPATH: /ios:native/ios:errdisable/ios:detect/ios:cause/ios:loopdetect
                m = p4.match(line)
                if m:
                    current_subsection += 1
                    instances_dict[current_section]['xpaths'].setdefault(current_subsection, {})
                    instances_dict[current_section]['xpaths'][current_subsection]['path'] = m.group(1)
                    continue

                #    Operation: Create
                m = p5.match(line)
                if m:
                    instances_dict[current_section]['xpaths'][current_subsection]['operation'] = m.group(1)
                    continue
        return parsed_dict


class ShowMerakiConfigUpdaterSchema(MetaParser):
    """Schema for:
        * 'show meraki config updater'
    """
    schema = {
        Optional('err_msg'): str,
        Optional('config_updater'): {
            'current_state': str,
            Optional('last_save_time'): str,
            Optional('next_save_scheduled'): bool,
            Optional('next_save_time'): str
        },
        Optional('latest_operation'): {
            'operation': str,
            Optional('download_running_config'): {
                'status': str,
                Optional('start_time'): str,
                Optional('result_time'): str,
                Optional('config_location'): str,
                Optional('dashboard_status_code'): str,
                Optional('retry_timeout'): int,
                Optional('dashboard_provided'): bool,
                Optional('retry_attempt'): int,
                Optional('retry_count'): int,
                Optional('retry_time'): str
            },
            Optional('apply_running_config'): {
                'status': str,
                Optional('start_time'): str,
                Optional('result_time'): str
            },
            Optional('save_config'): {
                'status': str,
                Optional('start_time'): str,
                Optional('result_time'): str
            },
            Optional('get_running_config'): {
                'status': str,
                Optional('start_time'): str,
                Optional('result_time'): str,
                Optional('config_location'): str,
            },
            Optional('get_presigned_url'): {
                'status': str,
                Optional('start_time'): str,
                Optional('result_time'): str,
                Optional('dashboard_status_code'): str,
                Optional('retry_timeout'): int,
                Optional('dashboard_provided'): bool,
                Optional('retry_attempt'): int,
                Optional('retry_count'): int,
                Optional('retry_time'): str
            },
            Optional('upload_config'): {
                'status': str,
                Optional('start_time'): str,
                Optional('result_time'): str,
                Optional('dashboard_status_code'): str,
                Optional('retry_timeout'): int,
                Optional('dashboard_provided'): bool,
                Optional('retry_attempt'): int,
                Optional('retry_count'): int,
                Optional('retry_time'): str
            },
            Optional('check_uplink'): {
                'status': str,
                Optional('start_time'): str,
                Optional('result_time'): str
            }
        }
    }


class ShowMerakiConfigUpdater(ShowMerakiConfigUpdaterSchema):
    """Schema for:
        * 'show meraki config updater'
    """
    cli_command = "show meraki config updater"

    def cli(self, output=None):
        if output is None:
            cmd = self.cli_command
            out = self.device.execute(cmd)
        else:
            out = output

        parsed_dict = {}

        # Begin Regex patterns to match output lines
        # service meraki connect is disabled
        p0 = re.compile(r"^(service meraki connect is disabled)$")

        # Config Updater
        p1 = re.compile(r"^Config Updater\s*$")

        #   Current state:                Ready
        p2 = re.compile(r"^Current state:\s+([A-Za-z].*)$")

        # Last config save time(UTC): 2025-03-18 22:19:16
        p3 = re.compile(r"^Last config save time\(UTC\):\s+(.*)$")

        # Next config save is scheduled.
        p4a = re.compile(r"^Next config save is scheduled.\s*$")

        # No config save scheduled.
        p4b = re.compile(r"^No config save scheduled.\s*$")

        # Next config save time(UTC): 2025-03-18 22:51:20
        p5 = re.compile(r"^Next config save time\(UTC\):\s+(.*)$")

        # Latest operation
        p6 = re.compile(r"^Latest operation\s*$")

        #  Download running config: Pass
        p7 = re.compile(r"^Download running config:\s+([A-Za-z].*)$")

        #  Apply running config: Pass
        p8 = re.compile(r"^Apply running config:\s+([A-Za-z].*)$")

        #  Save config: Completed
        p9 = re.compile(r"^Save config:\s+([A-Za-z].*)$")

        #  Get running config: Pass
        p10 = re.compile(r"^Get running config:\s+([A-Za-z].*)$")

        #  Get presigned url: Pass
        p11 = re.compile(r"^Get presigned url:\s+([A-Za-z].*)$")

        #  Upload config: Pass
        p12 = re.compile(r"^Upload config:\s+([A-Za-z].*)$")

        #  Check uplink: Pass
        p13 = re.compile(r"^Check uplink:\s+([A-Za-z].*)$")

        #    start time(UTC): 2025-03-18 22:15:40
        p14 = re.compile(r"^start time\(UTC\):\s+(.*)$")

        #    result time(UTC): 2025-03-18 22:15:51
        p15 = re.compile(r"^result time\(UTC\):\s+(.*)$")

        #    Downloaded config location: /flash/meraki/config_updater/monitor/dwnld_running.config
        p16 = re.compile(r"^[A-Z][a-zA-Z]*\sconfig location:\s*(.*)$")

        #    dashboard status code: 204
        p17 = re.compile(r"^dashboard status code:\s+(\d*)$")

        #    retry timeout: 300 sec
        p18 = re.compile(r"^retry timeout:\s+(\d*)\s*sec$")

        #    dashboard provided: No
        p19 = re.compile(r"^dashboard provided:\s+(.*)$")

        #    retry count: 2/3
        p20 = re.compile(r"^retry count:\s+(\d*)/(\d*)$")

        #      retry time(UTC): 2025-03-25 18:42:25
        p21 = re.compile(r"^retry time\(UTC\):\s+(.*)$")

        current_section = None
        current_subsection = None

        
        # Keep track of whether we are looking for the latest operation
        # Read the latest operation two lines after we see "Latest Operation", when var is set to two
        latest_operation = 0
        current_dict = {}

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            if latest_operation:
                if latest_operation == 2:
                    latest_operation_dict['operation'] = line
                    latest_operation = 0
                else:
                    latest_operation += 1
                continue

            # service meraki connect is disabled
            m = p0.match(line)
            if m:
                parsed_dict['err_msg'] = m.group(1)
                return parsed_dict

            # Config Updater
            m = p1.match(line)
            if m:
                config_updater_dict = parsed_dict.setdefault("config_updater", {})
                continue

            #   Current state:                Ready
            m = p2.match(line)
            if m:
                config_updater_dict['current_state'] = m.group(1)
                continue

            # Last config save time(UTC): 2025-03-18 22:19:16
            m = p3.match(line)
            if m:
                config_updater_dict['last_save_time'] = m.group(1)
                continue

            # Next config save is scheduled.
            m = p4a.match(line)
            if m:
                config_updater_dict['next_save_scheduled'] = True
                continue

            # No config save scheduled.
            m = p4b.match(line)
            if m:
                config_updater_dict['next_save_scheduled'] = False
                continue

            # Next config save time(UTC): 2025-03-18 22:51:20
            m = p5.match(line)
            if m:
                config_updater_dict['next_save_time'] = m.group(1)
                continue

            # Latest operation
            m = p6.match(line)
            if m:
                latest_operation_dict = parsed_dict.setdefault("latest_operation", {})
                latest_operation = 1
                continue

            #  Download running config: Pass
            m = p7.match(line)
            if m:
                download_dict = latest_operation_dict.setdefault("download_running_config", {})
                download_dict['status'] = m.group(1)
                current_dict = download_dict
                continue

            #  Apply running config: Pass
            m = p8.match(line)
            if m:
                apply_dict = latest_operation_dict.setdefault("apply_running_config", {})
                apply_dict['status'] = m.group(1)
                current_dict = apply_dict
                continue

            #  Save config: Completed
            m = p9.match(line)
            if m:
                save_dict = latest_operation_dict.setdefault("save_config", {})
                save_dict['status'] = m.group(1)
                current_dict = save_dict
                continue

            #  Get running config: Pass
            m = p10.match(line)
            if m:
                get_dict = latest_operation_dict.setdefault("get_running_config", {})
                get_dict['status'] = m.group(1)
                current_dict = get_dict
                continue

            #  Get presigned url: Pass
            m = p11.match(line)
            if m:
                get_presigned_dict = latest_operation_dict.setdefault("get_presigned_url", {})
                get_presigned_dict['status'] = m.group(1)
                current_dict = get_presigned_dict
                continue

            #  Upload config: Pass
            m = p12.match(line)
            if m:
                upload_dict = latest_operation_dict.setdefault("upload_config", {})
                upload_dict['status'] = m.group(1)
                current_dict = upload_dict
                continue

            #  Check uplink: Pass
            m = p13.match(line)
            if m:
                uplink_dict = latest_operation_dict.setdefault("check_uplink", {})
                uplink_dict['status'] = m.group(1)
                current_dict = uplink_dict
                continue

            #    start time(UTC): 2025-03-18 22:15:40
            m = p14.match(line)
            if m:
                current_dict['start_time'] = m.group(1)
                continue

            #    result time(UTC): 2025-03-18 22:15:51
            m = p15.match(line)
            if m:
                current_dict['result_time'] = m.group(1)
                continue

            #    Downloaded config location: /flash/meraki/config_updater/monitor/dwnld_running.config
            m = p16.match(line)
            if m:
                current_dict['config_location'] = m.group(1)
                continue

            #    dashboard status code: 204
            m = p17.match(line)
            if m:
                current_dict['dashboard_status_code'] = m.group(1)
                continue

            #    retry timeout: 300 sec
            m = p18.match(line)
            if m:
                current_dict['retry_timeout'] = int(m.group(1))
                continue

            #    dashboard provided: No
            m = p19.match(line)
            if m:
                current_dict['dashboard_provided'] = m.group(1) != 'No'
                continue

            #    retry count: 2/3
            m = p20.match(line)
            if m:
                current_dict['retry_attempt'] = int(m.group(1))
                current_dict['retry_count'] = int(m.group(2))
                continue

            #      retry time(UTC): 2025-03-25 18:42:25
            m = p21.match(line)
            if m:
                current_dict['retry_time'] = m.group(1)
                continue

        return parsed_dict


class ShowMerakiMigrationSchema(MetaParser):
    """Schema for:
        * 'show meraki migration'
    """
    schema = {
        Optional('err_msg'): str,
        Optional('booted_mode'): str,
        Optional('in_progress'): bool,
        Optional('mode_migrating_to'): str,
        Optional('migration_status'): str,
        Optional('start_time'): str,
        Optional('incompatible_reasons'): ListOf(str)
    }


class ShowMerakiMigration(ShowMerakiMigrationSchema):
    """Parser for:
        * 'show meraki migration'
    """
    cli_command = "show meraki migration"

    def cli(self, output=None):
        if output is None:
            cmd = self.cli_command
            out = self.device.execute(cmd)
        else:
            out = output

        parsed_dict = {}

        # Begin Regex patterns to match output lines
        # Error: show meraki migration - No memory left
        p0 = re.compile(r"^(Error: show [a-z\-]* migration - No memory left)$")

        #   Current Booted Mode:              C9K-M
        p1 = re.compile(r"^Current Booted Mode:\s+(.*)$")

        #  Migration in Progress:            NO
        p2 = re.compile(r"^Migration in Progress:\s+(.*)$")

        #  Mode Migrating To:                C9K-C [Monitoring]
        p3 = re.compile(r"^Mode Migrating To:\s+(.*)$")

        #  Migration Status:                 Migration failed compatibility check. Run "show meraki compatibility"
        p4 = re.compile(r"^Migration Status:\s+(.*)$")

        #  Migration Start Time:             2025-04-07 20:28:41
        p5 = re.compile(r"^Migration Start Time:\s+(.*)$")

        #  Compatibility Failed Reasons:
        p6 = re.compile(r"^Compatibility Failed Reasons:\s*")

        reasons = False

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # Check if migration has some incompatible reasons, collect every line after into list
            if reasons:
                reasons_list = parsed_dict.setdefault('incompatible_reasons', [])
                reasons_list.append(line)
            else:
                # Error: show meraki migration - No memory left
                m = p0.match(line)
                if m:
                    parsed_dict['err_msg'] = m.group(1)
                    return parsed_dict

                #   Current Booted Mode:              C9K-M
                m = p1.match(line)
                if m:
                    parsed_dict['booted_mode'] = m.group(1)
                    continue

                #  Migration in Progress:            NO
                #  Migration in Progress:            YES
                m = p2.match(line)
                if m:
                    parsed_dict['in_progress'] = m.group(1) != 'NO'
                    continue

                #  Mode Migrating To:                C9K-C [Monitoring]
                m = p3.match(line)
                if m:
                    parsed_dict['mode_migrating_to'] = m.group(1)
                    continue

                #  Migration Status:                 Migration failed compatibility check. Run "show meraki compatibility"
                m = p4.match(line)
                if m:
                    parsed_dict['migration_status'] = m.group(1)
                    continue

                #  Migration Start Time:             2025-04-07 20:28:41
                m = p5.match(line)
                if m:
                    parsed_dict['start_time'] = m.group(1)
                    continue

                #  Compatibility Failed Reasons:
                m = p6.match(line)
                if m:
                    reasons = True
                    continue
        return parsed_dict
