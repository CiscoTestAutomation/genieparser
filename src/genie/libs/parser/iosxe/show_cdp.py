'''  show_cdp.py

IOSXE parsers for the following show commands:

    * 'show cdp neighbors'
    * 'show cdp neighbors detail'
    * 'show cdp neighbors {interface} detail'
    * 'show cdp'

'''

# Python
import re

# Metaparser
from genie.libs.parser.utils.common import Common
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional
from genie import parsergen


class ShowCdpNeighborsSchema(MetaParser):

    ''' Schema for:
        * 'show cdp neighbors'
        * 'show cdp neighbors {interface}'
    '''

    schema = {
        'cdp': {
            Optional('index'): {
                Any(): {
                    Optional('device_id'): str,
                    Optional('local_interface'): str,
                    Optional('hold_time'): int,
                    Optional('capability'): str,
                    Optional('platform'): str,
                    Optional('port_id'): str
                }
            },
            'total_entries': int
        }
    }


# ================================
# Parser for 'show cdp neighbors'
# ================================
class ShowCdpNeighbors(ShowCdpNeighborsSchema):

    exclude = ['hold_time']

    cli_command = ['show cdp neighbors', 'show cdp neighbors {interface}']

    def cli(self, interface='', output=None):

        if output is None:
            if interface:
                out = self.device.execute(self.cli_command[1].format(interface=interface))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
        #                   S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone,
        #                   D - Remote, C - CVTA, M - Two-port Mac Relay

        # Specifically for situations when Platform and Port Id are concatenated        
        # RX-SWV.cisco.com Fas 0/1            167         T S       WS-C3524-XFas 0/13
        # C2950-1          Fas 0/0            148         S I       WS-C2950T-Fas 0/15
        p1 = re.compile(r'^(?P<device_id>\S+) +'
                        r'(?P<local_interface>[a-zA-Z]+[\s]*[\d\/\.]+) +'
                        r'(?P<hold_time>\d+) +(?P<capability>[RTBSsHIrPDCM\s]+)( +'
                        r'(?P<platform>\S+))?'
                        r'(\s+(?P<port_id>(Fa|Gi|GE).\s*\d*\/*\d*))?$')

        # No platform
        # R5.cisco.com Gig 0/0 125 R B Gig 0/0
        # SEP08000F8BA7FD  Gig 1/0/7         179              H P   Mitel 532 Port 1
        p2 = re.compile(r'^(?P<device_id>\S+) +'
                        r'(?P<local_interface>[a-zA-Z]+[\s]*[\d\/\.]+) +'
                        r'(?P<hold_time>\d+) +'
                        r'(?P<capability>[RTBSsHIrPDCM\s]+)'
                        r'(?: +(?P<platform>[\w\-]+ (\d+)?))?( +'
                        r'(?P<port_id>[a-zA-Z0-9\/]+( [a-zA-Z0-9\/\s]+)?))?$')

        # device6 Gig 0 157 R S I C887VA-W-W Gi 0
        # SEP08000FA9B170  Gig 1/0/9         158              H P   Mitel 532 Port 1
        p3 = re.compile(r'^(?P<device_id>\S+) +'
                        r'(?P<local_interface>[a-zA-Z]+[\s]*[\d\/\.]+) +'
                        r'(?P<hold_time>\d+) +(?P<capability>[RTBSsHIrPDCM\s]+)( +'
                        r'(?P<platform>\S+(?: \d+)?))?( '
                        r'(?P<port_id>[\s\S]+))?$')

        # p4 and p5 for two-line output, where device id is on a separate line
        # bgp-n93-d(FDO24140U7J)
        #                     Eth1/37/2      161    R S s     N9K-C93240YC- Eth1/6 
        # ott-bgp-laas(JAF1429BAKA)
        #                     Eth1/39/1      159    R S I s
        # ENT-DNAC-EG00-ESX03
        #                     Ten 1/1/2      154         S    VMware ES vmnic2
        p4 = re.compile(r'^(?P<device_id>\S+)$')
        p5 = re.compile(r'(?P<local_interface>[a-zA-Z]+[\s]*[\d/.]+) +'
                        r'(?P<hold_time>\d+) +(?P<capability>[RTBSsHIrPDCM\s]+)( +'
                        r'(?P<platform>VMware ES|\S+))?( (?P<port_id>[\.a-zA-Z0-9/\s]+))?$')

        # Total cdp entries displayed : 13
        p6 = re.compile(r'^Total cdp entries displayed :\s+(?P<total_entries>\d+)$')
        device_id_index = 0
        parsed_dict = {}

        for line in out.splitlines():
            line = line.strip()

            result = p1.match(line)

            if not result:
                result = p2.match(line)
                if not result:
                    result = p3.match(line)
            if result:

                device_id_index += 1

                device_dict = parsed_dict.setdefault('cdp', {}) \
                        .setdefault('index', {}).setdefault(device_id_index, {})

                group = result.groupdict()
                device_dict['device_id'] = group['device_id'].strip()
                device_dict['local_interface'] = Common.convert_intf_name\
                    (intf=group['local_interface'].strip())
                device_dict['hold_time'] = int(group['hold_time'])
                device_dict['capability'] = group['capability'].strip()
                if group['platform']:
                    device_dict['platform'] = group['platform'].strip()
                elif not group['platform']:
                    device_dict['platform'] = ''

                device_dict['port_id'] = Common.convert_intf_name\
                    (intf=group['port_id'].strip())
                continue

            result = p4.match(line)
            if result:
                group = result.groupdict()
                if 'Eth' not in group['device_id']:
                    device_id_index += 1
                    device_dict = parsed_dict.setdefault('cdp', {}) \
                        .setdefault('index', {}).setdefault(device_id_index, {})
                    device_dict['device_id'] = group['device_id'].strip()
                else:
                    device_dict['port_id'] = Common \
                        .convert_intf_name(intf=group['device_id'].strip())
                continue

            result = p5.match(line)
            if result:
                group = result.groupdict()
                device_dict = parsed_dict.setdefault('cdp', {}) \
                    .setdefault('index', {}).setdefault(device_id_index, {})
                device_dict['local_interface'] = Common \
                    .convert_intf_name(intf=group['local_interface'].strip())
                device_dict['hold_time'] = int(group['hold_time'])
                device_dict['capability'] = group['capability'].strip()
                if group['platform']:
                    device_dict['platform'] = group['platform'].strip()

                if group['port_id']:
                    device_dict['port_id'] = Common \
                        .convert_intf_name(intf=group['port_id'].strip())
                continue
            
            # Total cdp entries displayed : 13
            m = p6.match(line)
            if m:
                parsed_dict['cdp']['total_entries'] = int(m.groupdict()['total_entries'])

        return parsed_dict


class ShowCdpNeighborsDetailSchema(MetaParser):
    ''' Schema for:
        * 'show cdp neighbors detail'
    '''

    schema = {
        'total_entries_displayed': int,
        Optional('index'): {
            Any(): {
                Optional('device_id'): str,
                'platform': str,
                Optional('capabilities'): str,
                'local_interface': str,
                Optional('port_id'): str,
                'hold_time': int,
                Optional('software_version'): str,
                'entry_addresses': {
                    Any(): {
                        Optional('type'): str,
                    },
                },
                'management_addresses': {
                    Any(): {
                        Optional('type'): str,
                    },
                },
                Optional('duplex_mode'): str,
                Optional('advertisement_ver'): int,
                Optional('native_vlan'): str,
                Optional('vtp_management_domain'): str,
                Optional('power_drawn'): float,
                Optional('power_request_id'): int,
                Optional('power_mgmt_id_1'): int,
                Optional('power_req_level'): str,
                Optional('power_available_id'): int,
                Optional('power_mgmt_id_2'): int,
                Optional('available_power'): float,
                Optional('mgmt_power'): float},
            },
        }


# =======================================
# Parser for 'show cdp neighbors details'
# =======================================
class ShowCdpNeighborsDetail(ShowCdpNeighborsDetailSchema):
    ''' Parser for:
        * 'show cdp neighbors detail'
        * 'show cdp neighbors {interface} detail'
    '''
    cli_command = ['show cdp neighbors detail', 'show cdp neighbors {interface} detail']

    exclude = ['hold_time']

    def cli(self, interface=None, output=None):

        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0].format(interface=interface)
            output = self.device.execute(cmd)

        # Device ID: R7(9QBDKB58F76)
        # Device ID:
        deviceid_re = re.compile(r'Device\s+ID:\s*(?P<device_id>\S+)?')

        # Platform: N9K-9000v,  Capabilities: Router Switch CVTA phone port
        # Platform: N9K_9000v,  Capabilities: Router Switch Two-port phone port
        # Platform: cisco WS_C6506_E,  Capabilities: Router Switch-6506 IGMP
        # Platform: cisco WS-C6506-E,  Capabilities: Router Switch_6506 IGMP
        # Platform: Meraki MV21 Cloud Managed Indoor HD Dom
        # Platform: Mitel 5320e,DN 2142      ,  Capabilities: Host Phone
        # Platform: "CTS-CODEC-SX80",  Capabilities: Host Phone
        platf_cap_re = re.compile(r'Platform:\s+(?P<platform>[\w +(\-|\_\/:)\"]+'
                                  r'(?:,[\w ]+)?)(\,\s*Capabilities:\s+'
                                  r'(?P<capabilities>[\w\s\-]+))?$')

        # Interface: GigabitEthernet0/0,  Port ID (outgoing port): mgmt0
        # Interface: Ethernet0/1,  Port ID (outgoing port): Ethernet0/1
        # Interface: GigabitEthernet0/0,  Port ID (outgoing port): GigabitEthernet0/0
        # Interface: GigabitEthernet0/0/2,  Port ID (outgoing port): GigabitEthernet0/0/3
        # Interface: GigabitEthernet3/0/29,  Port ID (outgoing port): Port 0
        # Interface: Serial0/0/0:1,  Port ID (outgoing port): Serial1/4:1
        # Interface: FastEthernet0/0.1,  Port ID (outgoing port): GigabitEthernet7/27
        # Interface: GigabitEthernet0/5, Port ID (outgoing port):
        interface_port_re = re.compile(r'^Interface:\s*'
                                       r'(?P<interface>[\w\s\-\/\/\:\.]+)\s*\,'
                                       r'*\s*Port\s*ID\s*[\(\w\)\s\:]+:\s*'
                                       r'(?P<port_id>[\S\s]+)?$')

        # Native VLAN: 42
        native_vlan_re = re.compile(r'^Native\s*VLAN\s*:\s*'
                                    r'(?P<native_vlan>\d+)')

        # VTP Management Domain: 'Accounting Group'
        vtp_management_domain_re = re.compile(r'^VTP\s*Management\s*'
                                              r'Domain\s*:\s*'
                                              r'\W*(?P<vtp_management_domain>([a-zA-Z\s]+'
                                              r'))\W*')

        # Holdtime : 126 sec
        hold_time_re = re.compile(r'^Holdtime\s*:\s*\s*(?P<hold_time>\d+)')

        # advertisement version: 2
        advertver_re = re.compile(r'^advertisement\s*version:\s*'
                                  r'(?P<advertisement_ver>\d+)')

        # Cisco IOS Software, IOSv Software (VIOS-ADVENTERPRISEK9-M), Version 15.7(3)M3, RELEASE SOFTWARE (fc2)
        software_version_re = re.compile(r'^(?P<software_version>[\s\S]+)$')

        # Duplex: full
        # Duplex Mode: half
        duplex_re = re.compile(r'^Duplex\s*(Mode)*:\s*(?P<duplex_mode>\w+)')

        # Regexes for Flags:
        # Version:
        software_version_flag_re = re.compile(r'^Version\s*:\s*')
        # Management address(es):
        mngaddress_re = re.compile(r'^Management\s*address\s*\([\w]+\)\s*\:\s*')
        # Entry address(es):
        entryaddress_re = re.compile(r'^Entry\s*address\s*\(\w+\)\s*\:\s*')

        # IPv6 address: FE80::203:E3FF:FE6A:BF81  (link-local)
        # IPv6 address: 2001:DB8:1000:8A10::C0A8:BC06  (global unicast)
        ipv6_adress_re = re.compile(r'^IPv6\s*address\s*:\s*(?P<ip_adress>\S+)'
                                    r'\s*\((?P<type>[\s\w\-]+)\)')
        # IP address: 172.16.1.204
        ipaddress_re = re.compile(r'^IP\s*address:\s*(?P<id_adress>\S*)')
        
        # Power drawn: 0.099 Watts
        power_drawn_re = re.compile(r'^Power\s*drawn\s*:\s*(?P<power_drawn>\d+\.\d+)')
         
        # Power request id: 2, Power management id: 5
        power_ids_re_1 = re.compile(r'^Power\s+request\s+id:\s*(?P<power_request_id>\d+)\s*,\s*Power\s+management\s+id:\s*(?P<power_mgmt_id_1>\d+)')
         
        # Power request levels are:29289 15400 0 0 0
        power_req_level_re = re.compile(r'^Power\s+request\s+levels\s+are:\s*(?P<power_req_level>\d+(?:\s+\d+)*)')
         
        # Power available id:      1       Power management id:      2
        power_ids_re_2 = re.compile(r'^Power\s+available\s+id:\s*(?P<power_available_id>\d+)\s*Power\s+management\s+id:\s*(?P<power_mgmt_id_2>\d+)')
         
        # Power available is:  0.055 Watts Management Power is:  0.003 Watts
        power_avail_re = re.compile(r'^Power\s+available\s+is:\s*(?P<available_power>\d+\.\d+)\s+Watts\s*Management\s+Power\s+is:\s*(?P<mgmt_power>\d+\.\d+)\s+Watts')

        # 0 or 1 flags
        entry_address_flag = 0
        management_address_flag = 0
        software_version_flag = 0

        # Init vars
        parsed_dict = {}
        index_device = 0
        for line in output.splitlines():
            line = line.strip()

            # Device ID: R7(9QBDKB58F76)
            # Device ID:
            result = deviceid_re.match(line)

            if result:
                index_device += 1
                parsed_dict['total_entries_displayed'] = index_device
                devices_dict = parsed_dict.setdefault('index', {})\
                    .setdefault(index_device, {})

                if result.group('device_id'):
                    device_id = result.group('device_id')
                    devices_dict['device_id'] = device_id
                management_address_flag = 0

                # Init keys
                devices_dict['duplex_mode'] = ''
                devices_dict['vtp_management_domain'] = ''
                devices_dict['native_vlan'] = ''
                devices_dict['management_addresses'] = {}
                devices_dict['entry_addresses'] = {}

                continue

            # Platform: N9K-9000v,  Capabilities: Router Switch CVTA phone port
            # Platform: N9K_9000v,  Capabilities: Router Switch Two-port phone port
            # Platform: cisco WS_C6506_E,  Capabilities: Router Switch-6506 IGMP
            # Platform: cisco WS-C6506-E,  Capabilities: Router Switch_6506 IGMP
            # Platform: Meraki MV21 Cloud Managed Indoor HD Dom
            # Platform: Mitel 5320e,DN 2142      ,  Capabilities: Host Phone
            # Platform: "CTS-CODEC-SX80",  Capabilities: Host Phone
            result = platf_cap_re.match(line)

            if result:
                platf_cap_dict = result.groupdict()

                if platf_cap_dict['capabilities']:
                    devices_dict['capabilities'] = \
                        platf_cap_dict['capabilities']

                devices_dict['platform'] = \
                    platf_cap_dict['platform']

                entry_address_flag = 0

                continue

            # Interface: GigabitEthernet0/0,  Port ID (outgoing port): mgmt0
            # Interface: Ethernet0/1,  Port ID (outgoing port): Ethernet0/1
            # Interface: GigabitEthernet0/0,  Port ID (outgoing port): GigabitEthernet0/0
            # Interface: GigabitEthernet0/0/2,  Port ID (outgoing port): GigabitEthernet0/0/3
            # Interface: GigabitEthernet3/0/29,  Port ID (outgoing port): Port 0
            # Interface: Serial0/0/0:1,  Port ID (outgoing port): Serial1/4:1
            # Interface: FastEthernet0/0.1,  Port ID (outgoing port): GigabitEthernet7/27
            # Interface: GigabitEthernet0/5, Port ID (outgoing port):
            result = interface_port_re.match(line)

            if result:
                interface_port_dict = result.groupdict()
                if interface_port_dict['port_id']:
                    devices_dict['port_id'] = \
                        interface_port_dict['port_id']
                devices_dict['local_interface'] = \
                    interface_port_dict['interface']
                continue

            # Holdtime : 126 sec
            result = hold_time_re.match(line)

            if result:
                devices_dict['hold_time'] = \
                    int(result.group('hold_time'))
                continue

            # Management address(es):
            if mngaddress_re.match(line):
                management_address_flag = 1

            # Entry address(es):
            if entryaddress_re.match(line):
                entry_address_flag = 1

            # IP address: 172.16.1.204
            result = ipaddress_re.match(line)

            if result:

                ip_adress = result.group('id_adress')

                if management_address_flag:
                    devices_dict['management_addresses']\
                        [ip_adress] = {}

                if entry_address_flag:
                    devices_dict['entry_addresses']\
                        [ip_adress] = {}

                continue

            # IPv6 address: FE80::203:E3FF:FE6A:BF81  (link-local)
            # IPv6 address: 2001:DB8:1000:8A10::C0A8:BC06  (global unicast)
            result = ipv6_adress_re.match(line)

            if result:
                ipv6_address_dict = result.groupdict()

                if management_address_flag:
                    devices_dict['management_addresses']\
                        [ipv6_address_dict['ip_adress']] = \
                        {'type': ipv6_address_dict['type']}

                if entry_address_flag:
                    devices_dict['entry_addresses']\
                        [ipv6_address_dict['ip_adress']] = \
                        {'type': ipv6_address_dict['type']}

                continue

            # advertisement version: 2
            result = advertver_re.match(line)
            if result:
                software_version_flag = 0
                devices_dict['advertisement_ver'] = \
                    int(result.group('advertisement_ver'))
                continue

            # Regexes for Flags:
            # Version:
            if software_version_flag_re.match(line):
                software_version_flag = 1
                continue

            if software_version_flag:
                # Cisco IOS Software, IOSv Software (VIOS-ADVENTERPRISEK9-M), Version 15.7(3)M3, RELEASE SOFTWARE (fc2)
                result = software_version_re.match(line)
                if result:
                    sw_version = devices_dict.get('software_version', '')
                    # append lines to software_version
                    sw_version = '\n'.join(filter(
                        None, [sw_version, result.group('software_version')]))
                    devices_dict['software_version'] = sw_version
                continue

            result = native_vlan_re.match(line)

            if result:
                devices_dict['native_vlan'] = \
                    result.group('native_vlan')
                continue

            result = vtp_management_domain_re.match(line)

            if result:
                devices_dict['vtp_management_domain'] = \
                    result.group('vtp_management_domain')
                continue

            # Duplex: full
            # Duplex Mode: half
            result = duplex_re.match(line)

            if result:
                devices_dict['duplex_mode'] = \
                    result.group('duplex_mode')
                continue
            
            # Power drawn: 0.099 Watts
            result = power_drawn_re.match(line)

            if result:
                devices_dict['power_drawn'] = \
                    float(result.group('power_drawn'))
                continue
            
            # Power request id: 2, Power management id: 5
            result = power_ids_re_1.match(line)

            if result:
                power_ids_dict_1 = result.groupdict()
                if power_ids_dict_1['power_request_id']:
                    devices_dict['power_request_id'] = \
                        int(power_ids_dict_1['power_request_id'])
                devices_dict['power_mgmt_id_1'] = \
                    int(power_ids_dict_1['power_mgmt_id_1'])
                continue

            # Power request levels are:29289 15400 0 0 0
            result = power_req_level_re.match(line)

            if result:
                devices_dict['power_req_level'] = \
                    result.group('power_req_level')
                continue
            
            # Power available id:      1       Power management id:      2
            result = power_ids_re_2.match(line)

            if result:
                power_ids_dict_2 = result.groupdict()
                if power_ids_dict_2['power_available_id']:
                    devices_dict['power_available_id'] = \
                        int(power_ids_dict_2['power_available_id'])
                devices_dict['power_mgmt_id_2'] = \
                    int(power_ids_dict_2['power_mgmt_id_2'])
                continue
            
            # Power available is:  0.055 Watts Management Power is:  0.003 Watts
            result = power_avail_re.match(line)

            if result:
                power_avail_dict = result.groupdict()
                if power_avail_dict['available_power']:
                    devices_dict['available_power'] = \
                        float(power_avail_dict['available_power'])
                devices_dict['mgmt_power'] = \
                    float(power_avail_dict['mgmt_power'])
                continue


        return parsed_dict


class ShowCdpTrafficSchema(MetaParser):
    """
    Schema for:
        * 'Show CDP Traffic'
    """

    schema = {
        'total_output': int,
        'total_input': int,
        'hdr': int,
        'checksum': int,
        'encaps': int,
        'memory': int,
        'invalid': int,
        'cdp_ver1_output': int,
        'cdp_ver1_input': int,
        'cdp_ver2_output': int,
        'cdp_ver2_input': int,
    }


class ShowCdpTraffic(ShowCdpTrafficSchema):
    """
    Parser for 'show cdp traffic'
    """

    cli_command = 'show cdp traffic'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        
        meta_dict = dict()

        # Total packets output: 297183, Input: 2546
        p0 = re.compile(r'^Total\s+packets\s+output:\s+(?P<total_output>\d+),\s+Input:\s+(?P<total_input>\d+)$')

        # Hdr syntax: 0, Chksum error: 0, Encaps failed: 0
        p1 = re.compile(r'^Hdr\s+syntax:\s+(?P<hdr>\d+),\s+Chksum\s+error:\s+(?P<checksum>\d+),\s+Encaps\s+failed:\s+(?P<encaps>\d+)$')

        # No memory: 0, Invalid packet: 0,
        p2 = re.compile(r'^No\s+memory:\s+(?P<memory>\d+),\s+Invalid\s+packet:\s+(?P<invalid>\d+),$')

        # CDP version 1 advertisements output: 0, Input: 0
        p3 = re.compile(r'^CDP\s+version\s+1\s+advertisements\s+output:\s+(?P<cdp_ver1_output>\d+),\s+Input:\s+(?P<cdp_ver1_input>\d+)$')

        # CDP version 2 advertisements output: 285442, Input: 870
        p4 = re.compile(r'^CDP\s+version\s+2\s+advertisements\s+output:\s+(?P<cdp_ver2_output>\d+),\s+Input:\s+(?P<cdp_ver2_input>\d+)$')

        for line in output.splitlines():
            line = line.strip()
            
            # Total packets output: 297183, Input: 2546
            match = p0.match(line)
            if match:
                meta_dict.update({key: int(value) for key, value in match.groupdict().items()})
                continue
            
            # Hdr syntax: 0, Chksum error: 0, Encaps failed: 0
            match = p1.match(line)
            if match:
                meta_dict.update({key: int(value) for key, value in match.groupdict().items()})
                continue
            
            # No memory: 0, Invalid packet: 0,
            match = p2.match(line)
            if match:
                meta_dict.update({key: int(value) for key, value in match.groupdict().items()})
                continue
            
            # CDP version 1 advertisements output: 0, Input: 0
            match = p3.match(line)
            if match:
                meta_dict.update({key: int(value) for key, value in match.groupdict().items()})
                continue
            
            # CDP version 2 advertisements output: 285442, Input: 870
            match = p4.match(line)
            if match:
                meta_dict.update({key: int(value) for key, value in match.groupdict().items()})
                continue
        
        return meta_dict


class ShowCdpInterfaceSchema(MetaParser):
    """
    Schema for:
        * 'Show CDP Interface'
        * 'Show CDP Interface <Interface>'
    """

    schema = {
        'interface': {
            Any(): {
                'state': str,
                'protocol_state': str,
                'encapsulation': str,
                'cdp_interval': int,
                'hold_time': int,
            },
        },
        Optional('cdp_enabled_interfaces'): int,
        Optional('interfaces_up'): int,
        Optional('interfaces_down'): int
    }


class ShowCdpInterface(ShowCdpInterfaceSchema):
    """
    Parser for 'show cdp interface <interface>'
    """

    cli_command = 'show cdp interface'

    def cli(self, interface_type=None, interface_number=None, output=None):
        if output is None:
            if interface_type and interface_number:
                self.cli_command += f' {interface_type} {interface_number}'
            output = self.device.execute(self.cli_command)
        
        meta_dict = dict()

        # TwentyFiveGigE3/1/1 is down, line protocol is down
        # GigabitEthernet0/0 is administratively down, line protocol is down
        p0 = re.compile(r'^(?P<interface>[a-zA-Z\-\/\d\.]+)\s+is\s+(?P<state>[\w\s]+),\s+line\s+protocol\s+is\s+(?P<protocol_state>\w+)$')

        # Encapsulation ARPA
        p1 = re.compile(r'^Encapsulation\s+(?P<encapsulation>\w+)$')

        # Sending CDP packets every 60 seconds
        p2 = re.compile(r'^Sending\s+CDP\s+packets\s+every\s+(?P<cdp_interval>\d+)\s+seconds$')
  
        # Holdtime is 180 seconds
        p3 = re.compile(r'^Holdtime\s+is\s+(?P<hold_time>\d+)\s+seconds$')

        # cdp enabled interfaces : 172
        p4 = re.compile(r'^cdp\s+enabled\s+interfaces\s+:\s+(?P<cdp_enabled_interfaces>\d+)$')

        # interfaces up          : 7
        p5 = re.compile(r'^interfaces\s+up\s+:\s+(?P<interfaces_up>\d+)$')
        
        # interfaces down        : 166
        p6 = re.compile(r'^interfaces\s+down\s+:\s+(?P<interfaces_down>\d+)$')

        ret_int = lambda dicty: {key: int(value) for key, value in dicty.items()}

        for line in output.splitlines():
            line = line.strip()
            
            # TwentyFiveGigE3/1/1 is down, line protocol is down
            match = p0.match(line)
            if match:
                tmp_dict = match.groupdict()
                intf_dict = meta_dict.setdefault('interface', {}).setdefault(tmp_dict.pop('interface'), tmp_dict)
                continue
            
            # Encapsulation ARPA
            match = p1.match(line)
            if match:
                intf_dict.update(match.groupdict())
                continue

            # Sending CDP packets every 60 seconds
            match = p2.match(line)
            if match:
                intf_dict.update(ret_int(match.groupdict()))
                continue
            
            # Holdtime is 180 seconds
            match = p3.match(line)
            if match:
                intf_dict.update(ret_int(match.groupdict()))
                continue
            
            # cdp enabled interfaces : 172
            match = p4.match(line)
            if match:
                meta_dict.update(ret_int(match.groupdict()))
                continue
            
            # interfaces up          : 7
            match = p5.match(line)
            if match:
                meta_dict.update(ret_int(match.groupdict()))
                continue
            
            # interfaces down        : 166
            match = p6.match(line)
            if match:
                meta_dict.update(ret_int(match.groupdict()))
                continue
        
        return meta_dict


class ShowCdpEntrySchema(MetaParser):
    """Schema for show cdp entry [<WORD>|*]"""
    schema = {
        Optional('interface'): {
            Any(): {
                'port': {
                    Any(): {
                        'device_id': str,
                        'hold_time': int,
                        'cdp_version': int,
                        'peer_mac': str,
                        'vtp_mgmt_domain': str,
                        Optional('native_vlan'): int,
                        'duplex': str,
                        'platform': str,
                        'system_description': str
                    }
                }
            }
        }
    }


class ShowCdpEntry(ShowCdpEntrySchema):
    """Parser for show cdp entry {* | word}"""

    cli_command = ['show cdp entry {entry}', 'show cdp entry *']

    def cli(self, entry='', output=None):
        if output is None:
            if entry:
                cmd = self.cli_command[0].format(entry=entry)
            else:
                cmd = self.cli_command[1]
            output = self.device.execute(cmd)

        meta_dict = {}

        # Interface: GigabitEthernet0/0,  Port ID (outgoing port): GigabitEthernet1/0/18
        p0 = re.compile(r'^Interface:\s+(?P<intf>[\w\/\.\-]+),\s+Port\s+ID\s+\(outgoing port\):\s+(?P<port>[\w\/\.\-]+)$')

        # Device ID: 9300-24UX-1
        p1 = re.compile(r'^Device\s+ID:\s+(?P<device_id>[\S\s]+)$')

        # Platform: cisco C9300-24UX,
        p2 = re.compile(r'^Platform:\s+(?P<platform>.+),\s+Capabilities:')

        # Holdtime : 171 sec
        p3 = re.compile(r'^Holdtime\s+:\s+(?P<hold_time>\d+)\s+sec$')

        # Cisco IOS Software, Catalyst L3 Switch Software (CAT3K_CAA-UNIVERSALK9-M), Version 15.2(3.1.30)E1
        # Technical Support: http://www.cisco.com/techsupport
        # Copyright (c) 1986-2014 by Cisco Systems, Inc.
        # Compiled Fri 12-Dec-14 06:48 by gereddy
        p4 = re.compile(r'^(?P<system_description>(Cisco +IOS +Software|Technical Support|Copyright|Compiled).*)$')

        # Peer Source MAC: a03d.6ea4.6f04
        p5 = re.compile(r'^Peer\s+Source\s+MAC:\s+(?P<peer_mac>[a-f0-9A-F\.]+)$')

        # advertisement version: 2
        p6 = re.compile(r'^advertisement\s+version:\s+(?P<cdp_version>\d+)$')

        # VTP Management Domain: 'cisco'
        p7 = re.compile(r'^VTP\s+Management\s+Domain:\s+\'(?P<vtp_mgmt_domain>.*)\'$')

        # Native VLAN: 1
        p8 = re.compile(r'^Native\s+VLAN:\s+(?P<native_vlan>\d+)$')

        # Duplex: full
        p9 = re.compile(r'^Duplex:\s+(?P<duplex>\w+)$')

        tmp_dict = dict()
        system_description = list()
        ret_int = lambda dicty: {key: int(value) for key, value in dicty.items()}

        for line in output.splitlines():
            line = line.strip()
            
            # Interface: GigabitEthernet0/0,  Port ID (outgoing port): GigabitEthernet1/0/18
            match = p0.match(line)
            if match:
                port_dict = meta_dict.setdefault('interface', {
                }).setdefault(match.groupdict()['intf'], {
                }).setdefault('port', {
                }).setdefault(match.groupdict()['port'], {})
                port_dict.update(tmp_dict)
                tmp_dict.clear()
                continue
            
            # Device ID: 9300-24UX-1
            match = p1.match(line)
            if match:
                tmp_dict.update(match.groupdict())
                continue
            
            # Platform: cisco C9300-24UX,
            match = p2.match(line)
            if match:
                tmp_dict.update(match.groupdict())
                continue
            
            # Holdtime : 171 sec
            match = p3.match(line)
            if match:
                port_dict.update(ret_int(match.groupdict()))
                continue

            # Cisco IOS Software, Catalyst L3 Switch Software (CAT3K_CAA-UNIVERSALK9-M), Version 15.2(3.1.30)E1
            # Technical Support: http://www.cisco.com/techsupport
            # Copyright (c) 1986-2014 by Cisco Systems, Inc.
            # Compiled Fri 12-Dec-14 06:48 by gereddy
            match = p4.match(line)
            if match:
                system_description.append(match.groupdict()['system_description'])
                continue
            
            # Peer Source MAC: a03d.6ea4.6f04
            match = p5.match(line)
            if match:
                port_dict.update(match.groupdict())
                continue
            
            # advertisement version: 2
            match = p6.match(line)
            if match:
                port_dict.update(ret_int(match.groupdict()))
                port_dict.update({'system_description': '\n'.join(system_description)})
                system_description.clear()
                continue
            
            # VTP Management Domain: 'cisco'
            match = p7.match(line)
            if match:
                port_dict.update(match.groupdict())
                continue
            
            # Native VLAN: 1
            match = p8.match(line)
            if match:
                port_dict.update(ret_int(match.groupdict()))
                continue
            
            # Duplex: full
            match = p9.match(line)
            if match:
                port_dict.update(match.groupdict())
                continue
        
        return meta_dict


class ShowCdpSchema(MetaParser):
    '''Schema for show cdp'''
    schema = {
        'interval': int,
        'holdtime': int,
        'cdpv2': str
    }


class ShowCdp(ShowCdpSchema):
    '''Parser for show cdp'''

    cli_command = 'show cdp'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        
        # Sending CDP packets every 60 seconds
        p1 = re.compile(r'^Sending CDP packets every (?P<interval>\d+) seconds$')

        # Sending a holdtime value of 180 seconds
        p2 = re.compile(r'^Sending a holdtime value of (?P<holdtime>\d+) seconds$')

        # Sending CDPv2 advertisements is  enabled
        p3 = re.compile(r'^Sending CDPv2 advertisements is\s+(?P<cdpv2>\w+)$')

        ret_dict = dict()

        for line in output.splitlines():
            line = line.strip()

            # Sending CDP packets every 60 seconds
            m = p1.match(line)
            if m:
                ret_dict.setdefault('interval', int(m.groupdict()['interval']))
                continue

            # Sending a holdtime value of 180 seconds
            m = p2.match(line)
            if m:
                ret_dict.setdefault('holdtime', int(m.groupdict()['holdtime']))
                continue
            
            # Sending CDPv2 advertisements is  enabled
            m = p3.match(line)
            if m:
                ret_dict.setdefault('cdpv2', m.groupdict()['cdpv2'])
                continue
    
        return ret_dict