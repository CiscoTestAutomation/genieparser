"""show_dhcp.py

IOSXR parsers for the following show commands:
    * 'show dhcp ipv4 proxy binding'
    * 'show dhcp ipv4 proxy binding interface {interface_name}'
    * 'show dhcp ipv4 server binding'
    * 'show dhcp ipv4 server binding interface {interface_name}'
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
