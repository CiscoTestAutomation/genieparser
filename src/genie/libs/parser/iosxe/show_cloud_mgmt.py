'''  show_cloud_mgmt.py
IOSXE parsers for the following show command:
    * 'show cloud-mgmt'
    * 'show cloud-mgmt switch {switch}'
    * 'show cloud-mgmt connect'
    * 'show cloud-mgmt migration'
    * 'show cloud-mgmt config updater'
    * 'show cloud-mgmt config monitor'
    * 'show cloud-mgmt compatibility'

'''

# Python
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional
from genie.metaparser.util.schemaengine import (Schema, Any, Optional, Or, And, Default, Use, ListOf)
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# import parser utils
from genie.libs.parser.utils.common import Common


class ShowCloudMgmtSchema(MetaParser):
    """ Schema for:
        * 'show cloud-mgmt'
        * 'show cloud-mgmt switch {switch}'
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


class ShowCloudMgmt(ShowCloudMgmtSchema):
    '''
    Parser for:
        * 'show cloud-mgmt'
        * 'show cloud-mgmt switch {switch}'
    '''

    cli_command = ['show cloud-mgmt', 'show cloud-mgmt switch {switch}']

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


class ShowCloudMgmtConnectSchema(MetaParser):
    """Schema for show cloud-mgmt connect"""

    schema = {
        'service_cloud-mgmt_connect': str,
        Optional('cloud-mgmt_tunnel_config'): {
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
        Optional('cloud-mgmt_tunnel_state'): {
            'primary': str,
            'secondary': str,
            Optional('primary_last_change(utc)'): str,
            Optional('secondary_last_change(utc)'): str,
            Optional('client_last_restart(utc)'): str,
        },
        Optional('cloud-mgmt_tunnel_interface'): {
            Optional('vrf'): str,
            'status': str,
            'rx_packets': int,
            'tx_packets': int,
            'rx_errors': int,
            'tx_errors': int,
            'rx_drop_packets': int,
            'tx_drop_packets': int,
            Optional('rx_packets_(last_5s)'): int,
            Optional('tx_packets_(last_5s)'): int,
            Optional('rx_errors_(last_5s)'): int,
            Optional('tx_errors_(last_5s)'): int,
            Optional('rx_drop_packets_(last_5s)'): int,
            Optional('tx_drop_packets_(last_5s)'): int,
        },
       Optional('cloud-mgmt_device_registration'):{
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


class ShowCloudMgmtConnect(ShowCloudMgmtConnectSchema):
    """Parser for show cloud-mgmt connect"""

    cli_command = 'show cloud-mgmt connect'

    def cli(self, output=None):
        if output is None:
            cmd = self.cli_command
            out = self.device.execute(cmd)
        else:
            out = output
        #   Service cloud-mgmt connect: enable
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
        #   Cloud ID:                   Q5TC-J9PK-HK4R
        #   Mac Address:                6C:71:0D:3D:EA:80
        #   Status:                     Registered
        #   Timestamp(UTC):             2015-01-04 06:59:22
        #   Cloud ID:                   Q2ZZ-VYED-JVDA
        p1 = re.compile(r"^(?P<key>.+): +(?P<value>.+)$")

        # Cloud-Mgmt Tunnel Config
        # Cloud-Mgmt Tunnel State
        # Cloud-Mgmt Tunnel Interface
        # Cloud-Mgmt Device Registration
        p2 = re.compile(r"^(?P<key>(Cloud-Mgmt (Tunnel)?(Device)? (\w)+))$")

        #service cloud-mgmt connect is disabled
        p3 = re.compile(r"^(service\s+cloud-mgmt\s+connect)\s+is\s+(disabled)$")

        ret_dict = {} #level-0 dictionary
        stack_dict_index = 0 #level-1 dictionary
        stack_dict_1_index = 0 #level-2 dictionary

        for line in out.splitlines():
            #   Service cloud-mgmt connect: enable
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
            #   Cloud ID:                   Q5TC-J9PK-HK4R
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
                    # Check if the key is 'device_number' to create new parent dictionary 'device_number' level-2 under 'cloud-mgmt_device_registration'
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

            # Cloud-Mgmt Tunnel Config
            # Cloud-Mgmt Tunnel State
            # Cloud-Mgmt Tunnel Interface
            # Cloud-Mgmt Device Registration
            m2 = p2.match(line)
            if m2:
                dict_val = m2.groupdict()
                key_converted_to_lowercase_with_underscore = dict_val['key'].strip().replace(' ', '_').lower()
                # Update ret_dict with new parent dictionary will be level-1
                ret_dict.setdefault(key_converted_to_lowercase_with_underscore, {})
                stack_dict = ret_dict[key_converted_to_lowercase_with_underscore]
                stack_dict_index += 1
                continue

            m3 = p3.match(line)
            if m3:
                key_converted_to_lowercase_with_underscore = m3.group(1).strip().replace(' ', '_').lower()
                #if cloud-mgmt mode is disabled append the key-value pair to ret_dict level-0
                ret_dict[key_converted_to_lowercase_with_underscore] = m3.group(2)
                continue

        return ret_dict


class ShowCloudMgmtMigrationSchema(MetaParser):
    """Schema for show cloud-mgmt migration"""

    schema = {
        'cloud_mgmt_mode_migration_status': {
            'current_booted_mode': str,
            'migration_in_progress': str,
        }
    }


class ShowCloudMgmtMigration(ShowCloudMgmtMigrationSchema):
    """Parser for show cloud-mgmt migration"""

    cli_command = 'show cloud-mgmt migration'

    def cli(self, output=None):
        out = output if output is not None else self.device.execute(self.cli_command)

        ret_dict = {}

        # Cloud-Mgmt Mode Migration Status
        p1 = re.compile(r'^Cloud-Mgmt Mode Migration Status\s*$')

        # Current Booted Mode:              IE35xx-M
        p2 = re.compile(r'^Current Booted Mode:\s+(?P<current_booted_mode>\S+)\s*$')

        # Migration in Progress:            NO
        p3 = re.compile(r'^Migration in Progress:\s+(?P<migration_in_progress>\S+)\s*$')

        for line in out.splitlines():
            line = line.strip()

            # Cloud-Mgmt Mode Migration Status
            m1 = p1.match(line)
            if m1:
                continue

            #   Current Booted Mode:              IE35xx-M
            m2 = p2.match(line)
            if m2:
                ret_dict.setdefault('cloud_mgmt_mode_migration_status', {})['current_booted_mode'] = m2.group('current_booted_mode')
                continue

            #   Migration in Progress:            NO
            m3 = p3.match(line)
            if m3:
                ret_dict.setdefault('cloud_mgmt_mode_migration_status', {})['migration_in_progress'] = m3.group('migration_in_progress')
                continue

        return ret_dict


class ShowCloudMgmtConfigUpdaterSchema(MetaParser):
    """Schema for:
        * 'show cloud-mgmt config updater'
    """
    schema = {
        Optional('err_msg'): str,
        Optional('config_updater'): {
            'current_state': str,
            Optional('pending_local_changes'): bool,
            Optional('pending_local_changes_reason'): str,
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


class ShowCloudMgmtConfigUpdater(ShowCloudMgmtConfigUpdaterSchema):
    """Parser for:
        * 'show cloud-mgmt config updater'
    """
    cli_command = "show cloud-mgmt config updater"

    def cli(self, output=None):
        if output is None:
            cmd = self.cli_command
            out = self.device.execute(cmd)
        else:
            out = output

        parsed_dict = {}

        # service cloud-mgmt connect is disabled
        p0 = re.compile(r"^(service cloud-mgmt connect is disabled)$")

        # Config Updater
        p1 = re.compile(r"^Config Updater\s*$")

        #   Current state:                Ready
        p2 = re.compile(r"^Current state:\s+([A-Za-z].*)$")

        #   Pending local changes:        Yes (next upload will trigger consilience)
        p2a = re.compile(
            r"^(?:\*\*)?Pending local changes:\s+"
            r"(?P<pending_local_changes>Yes|No)"
            r"(?:\s+\((?P<pending_local_changes_reason>.*)\))?(?:\*\*)?$"
        )

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

        #    Downloaded config location: /flash/cloud_mgmt/config_updater/monitor/dwnld_running.config
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

            # service cloud-mgmt connect is disabled
            m = p0.match(line)
            if m:
                parsed_dict['err_msg'] = m.group(1)
                return parsed_dict

            # Config Updater
            m = p1.match(line)
            if m:
                config_updater_dict = parsed_dict.setdefault("config_updater", {})
                continue

            #   Current state:   Ready
            m = p2.match(line)
            if m:
                config_updater_dict['current_state'] = m.group(1)
                continue

            #   Pending local changes:        Yes (next upload will trigger consilience)
            m = p2a.match(line)
            if m:
                config_updater_dict['pending_local_changes'] = (
                    m.group('pending_local_changes') == 'Yes'
                )
                if m.group('pending_local_changes_reason'):
                    config_updater_dict['pending_local_changes_reason'] = m.group(
                        'pending_local_changes_reason'
                    )
                continue

            #   Last config save time(UTC): 2023-06-28 11:10:59
            m = p3.match(line)
            if m:
                config_updater_dict['last_save_time'] = m.group(1)
                continue

            #   Next config save is scheduled.
            m = p4a.match(line)
            if m:
                config_updater_dict['next_save_scheduled'] = True
                continue

            #   No config save scheduled.
            m = p4b.match(line)
            if m:
                config_updater_dict['next_save_scheduled'] = False
                continue

            #   Next config save time(UTC): 2023-06-28 12:27:35
            m = p5.match(line)
            if m:
                config_updater_dict['next_save_time'] = m.group(1)
                continue

            #   Latest Operation
            m = p6.match(line)
            if m:
                latest_operation_dict = parsed_dict.setdefault("latest_operation", {})
                latest_operation = 1
                continue

            #   Download running config:   Done
            m = p7.match(line)
            if m:
                download_dict = latest_operation_dict.setdefault("download_running_config", {})
                download_dict['status'] = m.group(1)
                current_dict = download_dict
                continue

            #   Apply running config:   Done
            m = p8.match(line)
            if m:
                apply_dict = latest_operation_dict.setdefault("apply_running_config", {})
                apply_dict['status'] = m.group(1)
                current_dict = apply_dict
                continue

            #   Save config:   Done
            m = p9.match(line)
            if m:
                save_dict = latest_operation_dict.setdefault("save_config", {})
                save_dict['status'] = m.group(1)
                current_dict = save_dict
                continue

            #   Get running config:   Done
            m = p10.match(line)
            if m:
                get_dict = latest_operation_dict.setdefault("get_running_config", {})
                get_dict['status'] = m.group(1)
                current_dict = get_dict
                continue

            #   Get presigned url:   Done
            m = p11.match(line)
            if m:
                get_presigned_dict = latest_operation_dict.setdefault("get_presigned_url", {})
                get_presigned_dict['status'] = m.group(1)
                current_dict = get_presigned_dict
                continue

            #   Upload config:   Done
            m = p12.match(line)
            if m:
                upload_dict = latest_operation_dict.setdefault("upload_config", {})
                upload_dict['status'] = m.group(1)
                current_dict = upload_dict
                continue

            #   Check uplink:   Done
            m = p13.match(line)
            if m:
                uplink_dict = latest_operation_dict.setdefault("check_uplink", {})
                uplink_dict['status'] = m.group(1)
                current_dict = uplink_dict
                continue

            #   start time(UTC): 2023-06-28 11:10:59
            m = p14.match(line)
            if m:
                current_dict['start_time'] = m.group(1)
                continue

            #   result time(UTC): 2023-06-28 11:10:59
            m = p15.match(line)
            if m:
                current_dict['result_time'] = m.group(1)
                continue

            #   Active config location: ...
            m = p16.match(line)
            if m:
                current_dict['config_location'] = m.group(1)
                continue

            #   dashboard status code: 200
            m = p17.match(line)
            if m:
                current_dict['dashboard_status_code'] = m.group(1)
                continue

            #   retry timeout: 10 sec
            m = p18.match(line)
            if m:
                current_dict['retry_timeout'] = int(m.group(1))
                continue

            #   dashboard provided: Yes
            m = p19.match(line)
            if m:
                current_dict['dashboard_provided'] = m.group(1) != 'No'
                continue

            #   retry count: 1/3
            m = p20.match(line)
            if m:
                current_dict['retry_attempt'] = int(m.group(1))
                current_dict['retry_count'] = int(m.group(2))
                continue

            #   retry time(UTC): 2023-06-28 11:10:59
            m = p21.match(line)
            if m:
                current_dict['retry_time'] = m.group(1)
                continue

        return parsed_dict


class ShowCloudMgmtCompatibilitySchema(MetaParser):
    """Schema for show cloud-mgmt compatibility"""

    schema = {
        Optional('cloud_mgmt_cloud_monitoring'): str,
        Optional('cloud_mgmt_cloud_management'): {
            'boot_mode': {
                Optional('mode'): str,
                'status': str,
                Optional('message'): str,
            },
            'switch_details': ListOf({
                'switch_number': int,
                'sku': {
                    'model': str,
                    'status': str,
                },
                'bootloader_version': {
                    'version': str,
                    'status': str,
                },
                Optional('expansion_modules'): ListOf({
                    'model': str,
                    Optional('status'): str,
                }),
                Optional('network_modules'): ListOf({
                    'model': str,
                    Optional('status'): str,
                }),
            }),
            Optional('compatible_expansion_modules'): ListOf(str),
            Optional('compatible_NMs'): ListOf(str),
        },
    }


class ShowCloudMgmtCompatibility(ShowCloudMgmtCompatibilitySchema):
    """Parser for show cloud-mgmt compatibility"""

    cli_command = 'show cloud-mgmt compatibility'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # Cloud-Mgmt Cloud Monitoring: Compatible
        p1 = re.compile(r'^Cloud-Mgmt Cloud Monitoring:\s+(?P<compatibility>\S+)\s*$')

        # Boot Mode        INSTALL  - Compatible
        # Boot Mode        Incompatible
        p2 = re.compile(r'^Boot Mode\s+(?P<rest>.+?)\s*$')

        # 1   IE-3500-8U3X    - Compatible    17_18_2r    - Compatible    IEM-3500-4MU - Compatible
        p3 = re.compile(
            r'^(?P<switch_number>\d+)\s+'
            r'(?P<sku_model>[\w-]+)\s+-\s+(?P<sku_status>\S+)\s+'
            r'(?P<bootloader_version>[\w_.-]+)\s+-\s+(?P<bootloader_status>\S+)'
            r'(?:\s+(?P<module_model>[\w./-]+|N/A)'
            r'(?:\s+-\s+(?P<module_status>\S+))?)?\s*$'
        )

        # Compatible EMs : IEM-3500-8T, IEM-3500-4MU
        p4 = re.compile(r'^Compatible EMs\s*:\s*(?P<ems>.*)\s*$')

        # Compatible NMs : NM-8X, NM-2Q
        p5 = re.compile(r'^Compatible NMs\s*:\s*(?P<nms>.*)\s*$')

        # Compatible SKUs: IE-9320-26S2C, ...
        p6 = re.compile(r'^Compatible SKUs\s*:\s*(?P<skus>.*)\s*$')

        # ===========================================================================================
        # Separator line e.g. ------- or =========
        p_sep = re.compile(r'^[=\-]{5,}\s*$')

        # Switch# header line or section labels that terminate multi-line buffers
        p_section_stop = re.compile(
            r'^(Switch#|Compatible EMs|Compatible NMs|Compatible SKUs|Cloud-Mgmt)'
        )

        # Switch detail data row: starts with a digit e.g. "1   IE-3500-8U3X ..."
        p_switch_row = re.compile(r'^\d+\s+')

        cloud_mgmt_dict = {}
        switch_details = []
        current_module_type = None
        # State variables for multi-line fields: Boot Mode message,
        # Compatible EMs, and Compatible NMs can each span multiple lines.
        # These buffers accumulate continuation lines until a terminator is seen.
        collecting_boot_msg = False
        boot_msg_buf = ''
        collecting_ems = False
        ems_buf = ''
        collecting_nms = False
        nms_buf = ''

        for line in out.splitlines():
            line = line.strip()

            if not line:
                continue

            # If accumulating a multi-line boot message, check for a terminator
            if collecting_boot_msg:
                if (p_sep.match(line) or p_section_stop.match(line) or p_switch_row.match(line)):
                    collecting_boot_msg = False
                    msg_clean = re.sub(r'\s+', ' ', boot_msg_buf).strip()
                    if msg_clean:
                        cloud_mgmt_dict.setdefault('boot_mode', {'status': 'Unknown'})['message'] = msg_clean
                    boot_msg_buf = ''
                else:
                    boot_msg_buf += ' ' + line
                    continue

            # If accumulating a multi-line Compatible EMs list, check for a terminator
            if collecting_ems:
                if (p_sep.match(line) or p_section_stop.match(line) or p_switch_row.match(line)):
                    collecting_ems = False
                    ems_clean = re.sub(r'\s+', ' ', ems_buf).strip().rstrip(' ,')
                    if ems_clean:
                        ems_list = [em.strip() for em in ems_clean.split(',') if em.strip()]
                        if ems_list:
                            cloud_mgmt_dict['compatible_expansion_modules'] = ems_list
                    ems_buf = ''
                else:
                    ems_buf += ' ' + line
                    continue

            # If accumulating a multi-line Compatible NMs list, check for a terminator
            if collecting_nms:
                if (p_sep.match(line) or p_section_stop.match(line) or p_switch_row.match(line)):
                    collecting_nms = False
                    nms_clean = re.sub(r'\s+', ' ', nms_buf).strip().rstrip(' ,')
                    if nms_clean:
                        nms_list = [nm.strip() for nm in nms_clean.split(',') if nm.strip()]
                        if nms_list:
                            cloud_mgmt_dict['compatible_NMs'] = nms_list
                    nms_buf = ''
                else:
                    nms_buf += ' ' + line
                    continue

            # Cloud-Mgmt Cloud Monitoring: Compatible
            m = p1.match(line)
            if m:
                parsed_dict['cloud_mgmt_cloud_monitoring'] = m.group('compatibility')
                continue

            # Boot Mode        INSTALL  - Compatible
            # Boot Mode        Incompatible
            m = p2.match(line)
            if m:
                rest = m.group('rest').strip()
                if ' - ' in rest:
                    mode, status = [x.strip() for x in rest.split(' - ', 1)]
                    cloud_mgmt_dict['boot_mode'] = {'mode': mode, 'status': status}
                else:
                    cloud_mgmt_dict['boot_mode'] = {'status': rest}
                collecting_boot_msg = True
                boot_msg_buf = ''
                continue

            # Switch# header row — skip
            if p_section_stop.match(line) and line.startswith('Switch#'):
                continue

            if 'Expansion Modules' in line:
                current_module_type = 'expansion_modules'
                continue

            if 'Network Modules' in line:
                current_module_type = 'network_modules'
                continue

            # 1   IE-3500-8U3X    - Compatible    17_18_2r    - Compatible    IEM-3500-4MU - Compatible
            m = p3.match(line)
            if m:
                switch_dict = {
                    'switch_number': int(m.group('switch_number')),
                    'sku': {'model': m.group('sku_model'), 'status': m.group('sku_status')},
                    'bootloader_version': {'version': m.group('bootloader_version'), 'status': m.group('bootloader_status')},
                }
                module_model = m.group('module_model')
                module_status = m.group('module_status')
                if module_model and module_model != 'N/A':
                    module_entry = {'model': module_model}
                    if module_status:
                        module_entry['status'] = module_status
                    if current_module_type == 'network_modules':
                        switch_dict['network_modules'] = [module_entry]
                    else:
                        switch_dict['expansion_modules'] = [module_entry]
                switch_details.append(switch_dict)
                continue

            # Compatible EMs : IEM-3500-8T, IEM-3500-4MU
            m = p4.match(line)
            if m:
                collecting_ems = True
                ems_buf = (m.group('ems') or '').strip()
                continue

            # Compatible NMs : NM-8X, NM-2Q
            m = p5.match(line)
            if m:
                collecting_nms = True
                nms_buf = (m.group('nms') or '').strip()
                continue

            m = p6.match(line)
            if m:
                continue

        # EOF finalize
        if collecting_boot_msg and boot_msg_buf.strip():
            cloud_mgmt_dict.setdefault('boot_mode', {'status': 'Unknown'})['message'] = re.sub(r'\s+', ' ', boot_msg_buf).strip()
        if collecting_ems and ems_buf.strip():
            ems_list = [em.strip() for em in re.sub(r'\s+', ' ', ems_buf).strip().rstrip(' ,').split(',') if em.strip()]
            if ems_list:
                cloud_mgmt_dict['compatible_expansion_modules'] = ems_list
        if collecting_nms and nms_buf.strip():
            nms_list = [nm.strip() for nm in re.sub(r'\s+', ' ', nms_buf).strip().rstrip(' ,').split(',') if nm.strip()]
            if nms_list:
                cloud_mgmt_dict['compatible_NMs'] = nms_list

        # Finalize cloud_mgmt_cloud_management section and add to parsed_dict
        # Only build the section if actual management data was collected
        if switch_details or cloud_mgmt_dict:
            cloud_mgmt_dict.setdefault('boot_mode', {'status': 'Unknown'})
            cloud_mgmt_dict['switch_details'] = switch_details
            parsed_dict['cloud_mgmt_cloud_management'] = cloud_mgmt_dict

        if not parsed_dict:
            raise SchemaEmptyParserError('No output found for show cloud-mgmt compatibility')

        return parsed_dict
