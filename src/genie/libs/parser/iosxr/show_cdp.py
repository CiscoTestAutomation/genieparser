""" show_cdp.py

IOSXR parsers for the following commands:

    * 'show cdp neighbors'
    * 'show cdp neighbors detail'
    * 'show cdp'
    * 'show cdp interface'
    * 'show cdp interface {interface}'

"""

# Python
import re

# Metaparser
from genie.libs.parser.utils.common import Common
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


class ShowCdpNeighborsSchema(MetaParser):
    ''' Schema for:
            * 'show cdp neighbors'
    '''

    schema = {
        'cdp':
            {Optional('index'):
             {Any():
              {'device_id': str,
               'local_interface': str,
               'hold_time': int,
               Optional('capability'): str,
               Optional('platform'): str,
               'port_id': str, }, }, },
    }


# ================================
# Parser for 'show cdp neighbors'
# ================================
class ShowCdpNeighbors(ShowCdpNeighborsSchema):
    exclude = ['hold_time']

    cli_command = 'show cdp neighbors'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
        #                   S - Switch, H - Host, I - IGMP, r - Repeater
        #

        # Specifically for situations when Platform and Port Id are
        # concatenated
        p1 = re.compile(
            r'^(?P<device_id>\S+) +'
            r'(?P<local_interface>[a-zA-Z]+[\s]*[\d\/\.]+) +'
            r'(?P<hold_time>\d+) +(?P<capability>[RTBSHIrPDCM\s]+) +'
            r'(?P<platform>\S+)'
            '(?P<port_id>(Fa|Gi|GE).\s*\d*\/*\d*)$')

        # No platform
        p2 = re.compile(
            r'^(?P<device_id>\S+) +'
            r'(?P<local_interface>[a-zA-Z]+[\s]*[\d\/\.]+) +'
            r'(?P<hold_time>\d+) +(?P<capability>[RTBSHIrPDCM\s]+)'
            r'(?: +(?P<platform>[\w\-]+) )? +'
            '(?P<port_id>[a-zA-Z0-9\/\s]+)$')

        # device6 Gig 0 157 R S I C887VA-W-W Gi 0
        p3 = re.compile(
            r'^(?P<device_id>\S+) +'
            r'(?P<local_interface>[a-zA-Z]+[\s]*[\d\/\.]+) +'
            r'(?P<hold_time>\d+) +(?P<capability>[RTBSHIrPDCM\s]+) +'
            '(?P<platform>\S+) (?P<port_id>[a-zA-Z0-9\/\s]+)$')

        # p4 and p5 for two-line output, where device id is on a separate line
        p4 = re.compile(r'^(?P<device_id>\S+)$')
        p5 = re.compile(
            r'(?P<local_interface>[a-zA-Z]+[\s]*[\d/.]+) +'
            r'(?P<hold_time>\d+) +(?P<capability>[RTBSHIrPDCM\s]+) +'
            r'(?P<platform>\S+) (?P<port_id>[a-zA-Z0-9/\s]+)$')

        device_id_index = 0
        parsed_dict = {}
        devices_dict_info = {}

        for line in out.splitlines():
            line = line.strip()

            result = p1.match(line)
            if not result:
                result = p2.match(line)
                if not result:
                    result = p3.match(line)

            if result:
                device_id_index += 1

                device_dict = devices_dict_info.setdefault(device_id_index, {})

                group = result.groupdict()

                device_dict['device_id'] = group['device_id'].strip()
                device_dict['local_interface'] = Common.convert_intf_name(
                    intf=group['local_interface'].strip())
                device_dict['hold_time'] = int(group['hold_time'])
                device_dict['capability'] = group['capability'].strip()
                if group['platform']:
                    device_dict['platform'] = group['platform'].strip()
                elif not group['platform']:
                    device_dict['platform'] = ''

                device_dict['port_id'] = Common.convert_intf_name(
                    intf=group['port_id'].strip())
                continue

            result = p4.match(line)
            if result:
                group = result.groupdict()
                if 'Eth' not in group['device_id']:
                    device_id_index += 1
                    device_dict = parsed_dict.setdefault(
                        'cdp',
                        {}).setdefault(
                        'index',
                        {}).setdefault(
                        device_id_index,
                        {})
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
                elif not group['platform']:
                    device_dict['platform'] = ''

                device_dict['port_id'] = Common \
                    .convert_intf_name(intf=group['port_id'].strip())
                continue

        if device_id_index:
            parsed_dict.setdefault('cdp', {}). \
                setdefault('index', devices_dict_info)

        return parsed_dict


class ShowCdpNeighborsDetailSchema(MetaParser):
    """ Schema for:
        * 'show cdp neighbors detail'
    """

    schema = {
        'total_entries_displayed': int,
        Optional('index'): {
            Any():
                {'device_id': str,
                 Optional('system_name'): str,
                 'platform': str,
                 'capabilities': str,
                 'local_interface': str,
                 'port_id': str,
                 'hold_time': int,
                 'software_version': str,
                 'entry_addresses':
                     {Any():
                      {Optional('type'): str, }, },
                 Optional('duplex_mode'): str,
                 Optional('advertisement_ver'): int,
                 Optional('native_vlan'): str},
        },
    }


# =======================================
# Parser for 'show cdp neighbors details'
# =======================================


class ShowCdpNeighborsDetail(ShowCdpNeighborsDetailSchema):
    cli_command = 'show cdp neighbors detail'
    exclude = ['hold_time']

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Device ID: R3_nx.cisco.com(972ZZK4REQK)
        deviceid_re = re.compile(r'Device\s+ID:\s*(?P<device_id>\S+)')

        # SysName:R3_nx
        system_name_re = re.compile(r''
                                    'SysName\s*:\s*(?P<system_name>\S+)')

        # Entry address(es):
        entry_address_re = re.compile(
            r''
            'Entry\s*address\s*\(\w+\)\s*\:\s*')

        # IPv4 address: 172.16.1.204
        ipv4_address_re = re.compile(
            r'\S*IPv4\s*'
            'address:\s*(?P<ip_address>\S*)')

        # Platform: N9K-9000v,  Capabilities: Router Switch
        platf_cap_re = re.compile(
            r'Platform:\s*(?P<platform>[a-zA-Z\d +\-\/]+)'
            r'\s*\,\s*Capabilities:\s*'
            '(?P<capabilities>[a-zA-Z\d\s*\-\/]+)')

        # Interface: GigabitEthernet0/0/0/5
        interface_re = re.compile(
            r'Interface:\s*'
            r'(?P<local_interface>[\w\s\-\/\/]+)\s*')

        # Port ID (outgoing port): Ethernet1/2
        port_re = re.compile(
            r'Port\s*ID\s*[\(\w\)\s]+:\s*'
            r'(?P<port_id>\S+)')

        # Holdtime : 126 sec
        hold_time_re = re.compile(r'Holdtime\s*:\s*\s*(?P<hold_time>\d+)')

        # Version: Cisco IOS Software, IOSv Software (VIOS-ADVENTERPRISEK9-M),
        # Version 15.7(3)M3, RELEASE SOFTWARE (fc2)
        software_version_re = re.compile(r'(?P<software_version>[\s\S]+)')

        # Regexes for Flags:
        # Version:
        software_version_flag_re = re.compile(r'Version\s*:\s*')

        # advertisement version: 2
        advertver_re = re.compile(r'advertisement\s*version:\s*'
                                  '(?P<advertisement_ver>\d+)')

        # Native VLAN: 42
        native_vlan_re = re.compile(r'Native\s*VLAN\s*:\s*'
                                    '(?P<native_vlan>\d+)')

        # Duplex: full
        # Duplex Mode: half
        duplex_re = re.compile(r'Duplex\s*(Mode)*:\s*(?P<duplex_mode>\w+)')

        # 0 or 1 flags
        entry_address_flag = 0
        software_version_flag = 0

        parsed_dict = {}
        index_device = 0
        sw_version = []

        out = re.sub(r'\r', '', out)
        for line in out.splitlines():
            line = line.strip()

            result = deviceid_re.match(line)
            if result:
                index_device += 1
                parsed_dict['total_entries_displayed'] = index_device

                devices_dict = parsed_dict.setdefault('index', {}) \
                    .setdefault(index_device, {})

                device_id = result.group('device_id')
                devices_dict['device_id'] = device_id

                # Init keys

                devices_dict['duplex_mode'] = ''
                devices_dict['system_name'] = ''
                devices_dict['native_vlan'] = ''
                devices_dict['entry_addresses'] = {}

                continue

            result = system_name_re.match(line)
            if result:
                devices_dict['system_name'] = result.group('system_name')
                continue

            result = platf_cap_re.match(line)
            if result:
                platf_cap_dict = result.groupdict()

                devices_dict['capabilities'] = \
                    platf_cap_dict['capabilities']
                devices_dict['platform'] = \
                    platf_cap_dict['platform']

                entry_address_flag = 0
                continue

            result = interface_re.match(line)
            if result:
                devices_dict['local_interface'] = result.group(
                    'local_interface')
                continue

            result = port_re.match(line)
            if result:
                devices_dict['port_id'] = result.group('port_id')
                continue

            result = hold_time_re.match(line)
            if result:
                devices_dict['hold_time'] = \
                    int(result.group('hold_time'))
                continue

            if entry_address_re.match(line):
                entry_address_flag = 1

            result = ipv4_address_re.match(line)
            if result:
                ip_address = result.group('ip_address')

                if entry_address_flag:
                    devices_dict['entry_addresses'][ip_address] = {}
                continue

            result = advertver_re.match(line)
            if result:
                devices_dict['advertisement_ver'] = \
                    int(result.group('advertisement_ver'))
                continue

            if software_version_flag_re.match(line):
                software_version_flag = 1
                continue

            if software_version_flag:
                if line and not advertver_re.match(line):

                    sw_version.append(line)
                    continue
                elif not line or advertver_re.match(line):

                    parsed_sw_ver = '\n'.join(sw_version)

                    result = software_version_re.match(parsed_sw_ver)

                    devices_dict['software_version'] = \
                        result.group('software_version')
                    software_version_flag = 0
                    sw_version.clear()

            result = advertver_re.match(line)
            if result:
                devices_dict['advertisement_ver'] = \
                    int(result.group('advertisement_ver'))
                continue

            result = native_vlan_re.match(line)
            if result:
                devices_dict['native_vlan'] = \
                    result.group('native_vlan')
                continue

            result = duplex_re.match(line)
            if result:
                devices_dict['duplex_mode'] = \
                    result.group('duplex_mode')
                continue

        return parsed_dict

class ShowCdpSchema(MetaParser):
    """Schema for show cdp"""
    schema = {
        'enabled': bool,
        Optional('cdp_packets'): int,
        Optional('hold_timer'): int,
        Optional('cdpv2_advertisements'): str
    }

# =======================================
# Parser for 'show cdp'
# =======================================

class ShowCdp(ShowCdpSchema):
    """Parser for show cdp"""

    cli_command = 'show cdp'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        ret_dict = {}

        # Global CDP information:
        p1 = re.compile(r'^Global\s+CDP\s+information:$')

        # Sending CDP packets every 60 seconds
        p2 = re.compile(r'^Sending\s+CDP\s+packets\s+every\s+(?P<cdp_packets>\d+)\s+seconds$')

        # Sending a holdtime value of 180 seconds
        p3 = re.compile(r'^Sending\s+a\s+holdtime\s+value\s+of\s+(?P<hold_timer>\d+)\s+seconds$')

        # Sending CDPv2 advertisements is not enabled
        # Sending CDPv2 advertisements is enabled
        p4 = re.compile(r'^Sending\s+CDPv2\s+advertisements\s+is\s+(?P<cdpv2_advertisements>[\w ]+)$')

        # % CDP is not enabled
        p5 = re.compile(r'^%\s+CDP\s+is\s+not\s+enabled$')

        for line in output.splitlines():
            line = line.strip()

            # Global CDP information:
            m = p1.match(line)
            if m:
                ret_dict['enabled'] = True
                continue

            # Sending CDP packets every 60 seconds
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['cdp_packets'] = int(group['cdp_packets'])
                continue

            # Sending a holdtime value of 180 seconds
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict['hold_timer'] = int(group['hold_timer'])
                continue

            # Sending CDPv2 advertisements is not enabled
            # Sending CDPv2 advertisements is enabled
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict['cdpv2_advertisements'] = group['cdpv2_advertisements']
                continue

            # % CDP is not enabled
            m = p5.match(line)
            if m:
                ret_dict['enabled'] = False
                continue

        return ret_dict

class ShowCdpInterfaceSchema(MetaParser):
    """ Schema for:
        * 'show cdp interface {interface}'
        * 'show cdp interface'
    """

    schema = {
        'interfaces': {
            Any(): {
                'interface': str,
                'status': str,
                'encapsulation': str,
                'cdp_packets': int,
                'hold_timer': int
            }
        }
    }


# =======================================
# Parser for 'show cdp interface {interface}'
# Parser for 'show cdp interface'
# =======================================


class ShowCdpInterface(ShowCdpInterfaceSchema):
    ''' Parser for commands:
        * 'show cdp interface {interface}'
        * 'show cdp interface'
    '''

    cli_command = ['show cdp interface {interface}',
                   'show cdp interface']

    def cli(self, interface=None, output=None):

        if output is None:
            if interface:
                command = self.cli_command[0].format(interface=interface)
            else:
                command = self.cli_command[1]
            output = self.device.execute(command)

        # initial return dictionary
        ret_dict = {}

        # GigabitEthernet0/0/0/16 is Up
        # GigabitEthernet0/0/0/17 is Down
        # GigabitEthernet0/0/0/18 is Administratively Down
        # TenGigE0/0/2/0 is Down
        # TenGigE0/0/2/1 is Up
        p1 = re.compile(r'^(?P<interface_name>\S+)\s+is\s+(?P<status>[a-zA-Z ]+)$')

        # Encapsulation ether
        p2 = re.compile(r'^Encapsulation\s+(?P<encapsulation>\w+)$')

        # Sending CDP packets every 60 seconds
        p3 = re.compile(r'^Sending\s+CDP\s+packets\s+every\s+(?P<cdp_packets>\d+)\s+seconds$')

        # Holdtime is 180 seconds
        p4 = re.compile(r'^Holdtime\s+is\s+(?P<hold_timer>\d+)\s+seconds$')

        for line in output.splitlines():
            line = line.strip() # strip whitespace from beginning and end

            # GigabitEthernet0/0/0/16 is Up
            # GigabitEthernet0/0/0/17 is Down
            # GigabitEthernet0/0/0/18 is Administratively Down
            # TenGigE0/0/2/0 is Down
            # TenGigE0/0/2/1 is Up
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf = Common.convert_intf_name(group['interface_name'])
                int_dict = ret_dict.setdefault('interfaces', {}).setdefault(intf, {})
                int_dict.update({'interface': intf})
                int_dict.update({'status': group['status']})
                continue

            # Encapsulation ether
            m = p2.match(line)
            if m:
                group = m.groupdict()
                int_dict.update({'encapsulation': group['encapsulation']})
                continue

            # Sending CDP packets every 60 seconds
            m = p3.match(line)
            if m:
                group = m.groupdict()
                int_dict.update({'cdp_packets': int(group['cdp_packets'])})
                continue

            # Holdtime is 180 seconds
            m = p4.match(line)
            if m:
                group = m.groupdict()
                int_dict.update({'hold_timer': int(group['hold_timer'])})
                continue

        return ret_dict
