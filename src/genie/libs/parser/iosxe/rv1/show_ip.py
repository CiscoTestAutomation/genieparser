""" show_platform.py

IOSXE revision 1 parsers for the following show commands:

    * 'show inventory'
"""

#Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, ListOf, And,\
                                         Default, Use
# parser utils
from genie.libs.parser.utils.common import Common
from genie.libs.parser.iosxe.show_vrf import ShowVrfDetailSchema, ShowVrfDetailSuperParser


# ===================================================
# Schema for
#    * 'show ip dhcp snooping binding'
#    * 'show ip dhcp snooping binding interface {interface}'
#    * 'show ip dhcp snooping binding {mac}'
# ===================================================
class ShowIpDhcpSnoopingBindingSchema(MetaParser):
    ''' Schema for:
        * 'show ip dhcp snooping binding'
        * 'show ip dhcp snooping binding interface {interface}'
        * 'show ip dhcp snooping binding {mac}'
    '''

    schema = {
        Optional('interfaces'): {
            Any(): {
                'vlan': {
                    Any(): ListOf(
                        {
                        'mac': str,
                        'ip': str,
                        'lease': int,
                        'type': str,
                    },
                    ),
                },
            },
        },
        'total_bindings': int,
    }

    


# ===========================
# Parser for:
#   * 'show show ip dhcp snooping binding'
#   * 'show ip dhcp snooping binding interface {interface}'
#   * 'show ip dhcp snooping binding {mac}'
# ===========================
class ShowIpDhcpSnoopingBinding(ShowIpDhcpSnoopingBindingSchema):
    ''' Parser for:
        * 'show ip dhcp snooping binding'
        * 'show ip dhcp snooping binding interface {interface}'
        * 'show ip dhcp snooping binding {mac}'
     '''

    cli_command = ['show ip dhcp snooping binding',
                'show ip dhcp snooping binding interface {interface}',
                'show ip dhcp snooping binding {mac}']

    def cli(self, interface=None, mac=None, output=None):
        if output is None:
            if mac:
                cmd = self.cli_command[2].format(mac=mac)
            elif interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]

            output = self.device.execute(cmd)

        # Init vars
        ret_dict = {}

        # MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
        # ------------------  ---------------  ----------  -------------  ----  --------------------
        # 00:11:01:00:00:01   100.100.0.5      1124        dhcp-snooping   100   FiftyGigE6/0/25

        p1 = re.compile(r'^(?P<mac>\S+) +(?P<ip>\S+) +(?P<lease>\d+) +(?P<type>\S+) +(?P<vlan>\d+) +(?P<interface>\S+)$')

        # Total number of bindings: 1
        p2 = re.compile(r'^Total number of bindings: (?P<total_bindings>\d+)$')

        for line in output.splitlines():

            line = line.strip()
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vlan = group['vlan']
                interface = group['interface']

                # Build Dict

                intf_dict = ret_dict.setdefault('interfaces', {}).setdefault(interface, {})
                vlan_list = intf_dict.setdefault('vlan', {}).setdefault(vlan, [])

                # Set values
                vlan_list.append({
                    'mac': group['mac'],
                    'ip': group['ip'],
                    'lease': int(group['lease']),
                    'type': group['type']
                })
                continue

            # Total number of bindings: 1
            m = p2.match(line)
            if m:
                ret_dict['total_bindings'] = int(m.groupdict()['total_bindings'])
                continue

        return ret_dict

