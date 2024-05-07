"""show_dhcp.py

IOSXR parsers for the following show commands:
    * 'show dhcp ipv4 proxy binding'
    * 'show dhcp ipv4 proxy binding interface {interface_name}'
    * 'show dhcp ipv4 server binding'
    * 'show dhcp ipv4 server binding interface {interface_name}'
    * 'show dhcp {ip_type} {user_command} interface {interface_name}'
    * 'show dhcp vrf {vrf_name} {ip_type} {user_command} statistics'
"""

# Python
import re
import logging
import collections
from ipaddress import ip_address, ip_network
from sys import version

# Metaparser
from genie.libs.parser.base import *
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use, ListOf

# Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# ========================================
# Parser for 'show dhcp ipv4 proxy binding'
# Parser for 'show dhcp ipv4 proxy binding interface {interface_name}'
# ========================================

class ShowDhcpIpv4ProxyBindingSchema(MetaParser):

    ''' Schema for:
        show dhcp ipv4 proxy binding
        show dhcp ipv4 proxy binding interface {interface_name}
    '''
    schema = {
        'vrf': {
            Any(): {
                'interface_name': {
                    Any(): {
                        'mac_address': str,
                        'ip_address': str,
                        'state': str,
                        'lease_remaining': int,
                        'sublabel': str
                    }
                }
            }
        }
    }

class ShowDhcpIpv4ProxyBinding(ShowDhcpIpv4ProxyBindingSchema):

    ''' Parser for:
        show dhcp ipv4 proxy binding
        show dhcp ipv4 proxy binding interface {interface_name}
    '''

    cli_command = ['show dhcp ipv4 proxy binding',
                   'show dhcp ipv4 proxy binding interface {interface_name}']

    def cli (self, interface_name=None, output=None):
        if output is None:
            if interface_name:
                output = self.device.execute(self.cli_command[1].format(interface_name=interface_name))
            else:
                output = self.device.execute(self.cli_command[0])
        else:
            output = output

        result_dict = {}

        # 5001.0009.0002  51.1.1.3        BOUND      80989      Gi0/0/0/3.500        DHCP-VRF   0x0
        p1 = re.compile(r'^((?P<mac_address>[\w\.]+)\s+(?P<ip_address>[\w\.]+)'
                        '\s+(?P<state>\w+)\s+(?P<lease_remaining>\d+)\s+'
                        '(?P<interface_name>\S+)\s+(?P<vrf_name>\S+)\s+'
                        '(?P<sublabel>\S+))$')


        for line in output.splitlines():
            line = line.strip() # strip whitespace from beginning and end

            # 5001.0009.0002  51.1.1.3        BOUND      80989      Gi0/0/0/3.500        DHCP-VRF   0x0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                result_dict.setdefault('vrf', {}). \
                    setdefault(group['vrf_name'], {})
                interface_name_dict = result_dict['vrf'][group['vrf_name']]. \
                    setdefault("interface_name", {})
                int_dict = interface_name_dict.setdefault(group["interface_name"], {})
                int_dict['mac_address'] = group['mac_address']
                int_dict['ip_address'] = group['ip_address']
                int_dict['state'] = group['state']
                int_dict['lease_remaining'] = int(group['lease_remaining'])
                int_dict['sublabel'] = group['sublabel']
                continue

        return result_dict

# ========================================
# Parser for 'show dhcp ipv4 server binding'
# Parser for 'show dhcp ipv4 server binding interface {interface_name}'
# ========================================

class ShowDhcpIpv4ServerBinding(ShowDhcpIpv4ProxyBinding):

    ''' Parser for:
        show dhcp ipv4 server binding
        show dhcp ipv4 server binding interface {interface_name}
    '''

    cli_command = ['show dhcp ipv4 server binding',
                   'show dhcp ipv4 server binding interface {interface_name}']

    def cli (self, interface_name=None, output=None):
        if output is None:
            if interface_name:
                cmd = self.cli_command[1].format(interface_name=interface_name)
            else:
                cmd = self.cli_command[0]
        else:
            output = output

        output = self.device.execute(cmd)

        # Call super
        return super().cli(output=output)

# ========================================
# Parser for 'show dhcp {ip_type} {user_command} interface {interface_name}'
# ========================================

class ShowDhcpIpInterfaceSchema(MetaParser):

    ''' Schema for:
        show dhcp {ip_type} {user_command} interface {interface_name}
    '''
    schema = {
        'dhcp': {
            Any(): str,
        }
    }

class ShowDhcpIpInterface(ShowDhcpIpInterfaceSchema):

    ''' Parser for:
        show dhcp {ip_type} {user_command} interface {interface_name}
    '''

    cli_command = ['show dhcp {ip_type} {user_command} interface {interface_name}']

    def cli (self, ip_type=None, user_command=None, interface_name=None, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0].format(ip_type=ip_type,\
                                                                    user_command=user_command,\
                                                                    interface_name=interface_name))

        # Interface:          Bundle-Ether15.1001
        # Profile Name:       CATL
        p1 = re.compile(r'^(?P<key>[\S\s]+):\s+(?P<value>[\S\s]+)$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Interface:          Bundle-Ether15.1001
            # Profile Name:       CATL
            m = p1.match(line)
            if m:
                group = m.groupdict()
                dhcp_dict = ret_dict.setdefault('dhcp', {})
                key = group['key'].replace(' ','_').lower()
                value = group['value']
                dhcp_dict[key] = value
                continue

        return ret_dict

# ========================================
# Schema for 'show dhcp vrf {vrf_name} {ip_type} {user_command} statistics'
# ========================================

class ShowDhcpVrfIpStatisticsSchema(MetaParser):

    ''' Schema for:
        show dhcp vrf {vrf_name} {ip_type} {user_command} statistics
    '''
    schema = {
        'vrf': {
            Any(): {
                'type': {
                    Any(): {
                        'receive': int,
                        'transmit': int,
                        'drop': int
                    }
                }
            }
        }
    }

# ========================================
# Parser for 'show dhcp vrf {vrf_name} {ip_type} {user_command} statistics'
# ========================================

class ShowDhcpVrfIpStatistics(ShowDhcpVrfIpStatisticsSchema):

    ''' Parser for:
        show dhcp vrf {vrf_name} {ip_type} {user_command} statistics
    '''

    cli_command = ['show dhcp vrf {vrf_name} {ip_type} {user_command} statistics']

    def cli (self, ip_type=None, user_command=None, vrf_name=None, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0].format(ip_type=ip_type,\
                                                                    user_command=user_command,\
                                                                    vrf_name=vrf_name))

        # DHCP IPv4 Proxy/Server Statistics for VRF default:
        # DHCP IPv4 Relay Statistics for VRF default:
        # DHCP IPv4 Relay Statistics for VRF DHCP-VRF:
        p1 = re.compile(r'^DHCP\s+IPv4\s+\S+\s+Statistics\s+for\s+VRF\s+(?P<vrf_name>\S+):$')

        # DISCOVER         |            0  |            0  |            0  |
        # BOOTP-REQUEST    |            0  |            0  |            0  |
        p2 = re.compile(r'^(?P<type>[\w-]+)\s+\|\s+(?P<receive>\d+)\s+\|\s+(?P<transmit>\d+)\s+\|\s+(?P<drop>\d+)\s+\|$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # DHCP IPv4 Proxy/Server Statistics for VRF default:
            # DHCP IPv4 Relay Statistics for VRF default:
            # DHCP IPv4 Relay Statistics for VRF DHCP-VRF:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vrf_dict = ret_dict.setdefault('vrf', {}).setdefault(group['vrf_name'], {})
                continue

            # DISCOVER         |            0  |            0  |            0  |
            # BOOTP-REQUEST    |            0  |            0  |            0  |
            m = p2.match(line)
            if m:
                group = m.groupdict()
                type_dict = vrf_dict.setdefault('type', {}).setdefault(group['type'], {})
                type_dict.update({'receive': int(group['receive'])})
                type_dict.update({'transmit': int(group['transmit'])})
                type_dict.update({'drop': int(group['drop'])})
                continue

        return ret_dict
