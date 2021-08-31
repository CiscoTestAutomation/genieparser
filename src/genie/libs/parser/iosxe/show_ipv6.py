"""
    show_ipv6.py
    IOSXE parsers for the following show commands:

    * show ipv6 neighbors
    * show ipv6 neighbors vrf <vrf>
    * show ipv6 neighbors <interface>
    * show ipv6 neighbors detail
    * show ipv6 neighbors vrf <vrf> detail
    * show ipv6 interface (from show_interface.py)
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

from genie.libs.parser.utils.common import Common


# ======================================================
# Parser for:
#          'show ipv6 neighbors'
#          'show ipv6 neighbors vrf <vrf>'
#          'show ipv6 neighbors detail'
#          'show ipv6 neighbors vrf <vrf> detail'
# ======================================================
class ShowIpv6NeighborsSchema(MetaParser):
    """Schema for :
                  'show ipv6 neighbors detail'
                  'show ipv6 neighbors vrf <vrf>'
    """

    schema = {
        'interface': {
            Any(): {
                'interface': str,
                'neighbors': {
                    Any(): {
                        'ip': str,  # Conf/Ops Str '2001:db8:8548:1::1'
                        'link_layer_address': str,  # Conf/Ops Str 'aaaa.beff.bcbc'
                        'age': str,
                        'neighbor_state': str,
                        Optional('trlv'): str,
                    },
                },
            },
        },
    }


class ShowIpv6Neighbors(ShowIpv6NeighborsSchema):
    """
       Parser for 'show ipv6 neighbors'
                  'show ipv6 neighbors vrf <vrf>'
                  'show ipv6 neighbors <interface>'
    """

    cli_command = ['show ipv6 neighbors vrf {vrf} {interface}',
                   'show ipv6 neighbors {interface}',
                   'show ipv6 neighbors vrf {vrf}',
                   'show ipv6 neighbors',]
    exclude = ['age' , 'neighbor_state']

    def cli(self, vrf='', interface='', output=None):
        if output is None:
            if vrf and interface:
                cmd = self.cli_command[0].format(vrf=vrf, interface=interface)
            elif interface:
                cmd = self.cli_command[1].format(interface=interface)
            elif vrf:
                cmd = self.cli_command[2].format(vrf=vrf)
            else:
                cmd = self.cli_command[3]
            out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        ret_dict = {}

        # IPv6 Address                              Age Link-layer Addr State Interface
        # 2001:db8:8548:1::2                                 0 fa16.3eff.09c8  REACH Gi2
        p1 = re.compile(r'^(?P<ip>([\w\:]+))\s+(?P<age>\S+)\s+'
                        '(?P<link_layer_address>\S+)\s+(?P<neighbor_state>\S+)'
                        '\s+(?P<interface>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # 2001:db8:8548:1::2                                 0 fa16.3eff.09c8  REACH Gi2
            m = p1.match(line)
            if m:
                ip = m.groupdict()['ip']
                age = m.groupdict()['age']
                link_layer_address = m.groupdict()['link_layer_address']
                neighbor_state = m.groupdict()['neighbor_state']
                interfaces = Common.convert_intf_name(m.groupdict()['interface'])
                interface = Common.convert_intf_name(m.groupdict()['interface'])

                interface_dict = ret_dict.setdefault('interface', {})\
                    .setdefault(interfaces, {})
                interface_dict['interface'] = interface

                neighbor_dict = interface_dict.setdefault('neighbors', {})\
                    .setdefault(ip, {})

                neighbor_dict['age'] = age
                neighbor_dict['ip'] = ip
                neighbor_dict['link_layer_address'] = link_layer_address
                neighbor_dict['neighbor_state'] = neighbor_state
                continue

        return ret_dict


class ShowIpv6NeighborsDetail(ShowIpv6NeighborsSchema):
    """
       Parser for 'show ipv6 neighbors detail'
                  'show ipv6 neighbors vrf <vrf> detail'
    """

    cli_command = ['show ipv6 neighbors vrf {vrf} detail',
                   'show ipv6 neighbors detail']
    exclude = ['age', 'neighbor_state']

    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
               cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}

        # IPv6 Address                              TRLV Age Link-layer Addr State Interface
        # FE80::F816:3EFF:FEFF:F3DC                   0    0 fa16.3eff.f3dc  REACH Gi2.90
        p1 = re.compile(r'^(?P<ip>([\w\:]+))\s+(?P<trlv>\S)\s+(?P<age>\S+)\s+'
                         '(?P<link_layer_address>\S+)\s+(?P<neighbor_state>\S+)\s+'
                         '(?P<interface>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # IPv6 Address                              TRLV Age Link-layer Addr State Interface
            # FE80::F816:3EFF:FEFF:F3DC                   0    0 fa16.3eff.f3dc  REACH Gi2.90
            m = p1.match(line)
            if m:
                ip = m.groupdict()['ip']
                trlv = m.groupdict()['trlv']
                age = m.groupdict()['age']
                link_layer_address = m.groupdict()['link_layer_address']
                neighbor_state = m.groupdict()['neighbor_state']
                interfaces = Common.convert_intf_name(m.groupdict()['interface'])
                interface = Common.convert_intf_name(m.groupdict()['interface'])

                interface_dict = ret_dict.setdefault('interface', {})\
                    .setdefault(interfaces, {})
                interface_dict['interface'] = interface

                neighbor_dict = interface_dict.setdefault('neighbors', {})\
                    .setdefault(ip, {})

                neighbor_dict['age'] = age
                neighbor_dict['ip'] = ip
                neighbor_dict['trlv'] = trlv
                neighbor_dict['link_layer_address'] = link_layer_address
                neighbor_dict['neighbor_state'] = neighbor_state
                continue

        return ret_dict

# ==================================
# Schema for:
#  * 'show ipv6 destination-guard policy <policy name>'
# ==================================
class ShowIpv6DestinationGuardPolicySchema(MetaParser):
    """Schema for show ipv6 destination-guard policy <policy>"""
    schema = {
        'enforcement': str,
        'entries': {
            int: {
                'target': str,
                'type': str,
                'policy': str,
                'feature': str,
                'target_type': str,
                'range': str,
            }
        }
    }

# ==================================
# Parser for:
#  * 'show ipv6 destination-guard policy {policy name}'
# ==================================
class ShowIpv6DestinationGuardPolicy(ShowIpv6DestinationGuardPolicySchema):
    """Parser for show ipv6 destination-guard policy {policy}"""
    cli_command = 'show ipv6 destination-guard policy {policy}'

    def cli(self, policy, output=None):
        if output is None:
            cmd = self.cli_command.format(policy=policy)
            out = self.device.execute(cmd)
        else:
            out = output

        destination_guard_policy_dict = {}
        # Destination guard policy poll configuration: 
        #   enforcement stressed
        # Policy poll is applied on the following targets: 
        # Target               Type  Policy               Feature        Target range
        # Twe1/0/1             PORT  poll                 Destination Guard vlan all
        # vlan 5               VLAN  poll                 Destination Guard vlan all
        # vlan 38              VLAN  poll                 Destination Guard vlan all
        # vlan 39              VLAN  poll                 Destination Guard vlan all


        #   enforcement always 
        enforcement_capture = re.compile(
            r"enforcement\s+(?P<enforcement>\S+)$"
        )
        # vlan 5               VLAN  poll                 Destination Guard vlan all
        entry_capture = re.compile(
            r"^(?P<target>((\S+\s\d+)|(\S+/\d+(/\d+)?)))\s+"
            r"(?P<type>\S+)\s+"
            r"(?P<policy>\S+)\s+"
            r"(?P<feature>\S+\s\S+)\s+"
            r"(?P<target_type>\S+)\s+"
            r"(?P<range>\S+)$"
        )

        entry_counter = 0
        for line in out.splitlines():
            line = line.strip()

            #   enforcement always
            match = enforcement_capture.match(line)
            if enforcement_capture.match(line):
                groups = match.groupdict()

                enforcement = groups['enforcement']

                destination_guard_policy_dict['enforcement'] = enforcement
                continue

            # vlan 5               VLAN  poll                 Destination Guard vlan all 
            match = entry_capture.match(line)
            if match:
                entry_counter += 1
                groups = match.groupdict()

                target = groups['target']
                type = groups['type']
                policy = groups['policy']
                feature = groups['feature']
                target_type = groups['target_type']
                rang = groups['range']

                index_dict = destination_guard_policy_dict.setdefault('entries', {}).setdefault(entry_counter, {})

                index_dict['target'] = target
                index_dict['type'] = type
                index_dict['policy'] = policy
                index_dict['feature'] = feature
                index_dict['target_type'] = target_type
                index_dict['range'] = rang
                continue

        return destination_guard_policy_dict

# ====================================================
# Schema for 'show ipv6 dhcp guard policy <policy name>'
# ====================================================
class ShowIpv6DhcpGuardPolicySchema(MetaParser):
    """ Schema for show ipv6 dhcp guard policy <policy name> """

    schema = {
        'dhcp_guard_policy_config': {            
            'policy_name': str,
            'trusted_port': bool,
            'device_role': str,
            Optional('max_preference'): int,
            Optional('min_preference'): int,
            Optional('access_list'): str,
            Optional('prefix_list') : str,
            "targets": {
                Optional(str): {
                    'target': str,
                    'type': str,
                    'feature': str,
                    'target_range': str
                    }
                }
            }
        }

# =============================================
# Parser for 'show ipv6 guard policy <policy name>'
# =============================================
class ShowIpv6DhcpGuardPolicy(ShowIpv6DhcpGuardPolicySchema):
    """ show ipv6 dhcp guard policy <policy name> """

    cli_command = 'show ipv6 dhcp guard policy {policy_name}'

    def cli(self, policy_name='', output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(policy_name=policy_name))
        else:
            output = output

        #Dhcp guard policy pol1 configuration:
        p = re.compile(r'^Dhcp\s+guard\s+policy\s+(?P<policy_name>.+)\s+configuration:$')
        
        #Device Role: dhcp server
        p1 = re.compile(r'^Device\sRole:\s(?P<device_role>dhcp (client|server))$')

        #Trusted Port 
        p2 = re.compile(r'^(?P<trusted_port>Trusted Port)$')

        #Max Preference: 255
        p3 = re.compile(r'^Max Preference:\s+((?P<max_preference>\d+))$')

        #Min Preference: 0
        p4 = re.compile(r'^Min Preference:(\s+(?P<min_preference>\d+))$')

        #Source Address Match Access List: acl1
        p5 = re.compile(r'^Source Address Match Access List:\s+(?P<access_list>\S+)$')

        #Prefix List Match Prefix List: abc
        p6 = re.compile(r'^Prefix List Match Prefix List:\s+(?P<prefix_list>\S+)$')

        #Target               Type  Policy               Feature        Target range
        # vlan 2               VLAN  pol1                 DHCP Guard     vlan all
        # Et0/0                PORT  pol1                 DHCP Guard     vlanall
        p7 = re.compile(r'^(?P<target>\S+\s*\S+)\s{2,}(?P<type>\S+)\s+\S+\s+(?P<feature>\S+\s\S+)\s+(?P<target_range>\S+.*\S+)$')

        parser_dict = {}

        for line in output.splitlines():
            line = line.strip()

            #Dhcp guard policy pol1 configuration:
            m = p.match(line)
            if m:
                policy_config_dict = parser_dict.setdefault('dhcp_guard_policy_config', {})
                policy_config_dict.update({'policy_name': m.groupdict()['policy_name']})
                policy_config_dict.setdefault('trusted_port', False)
                continue

            #Device Role: dhcp server
            m1 = p1.match(line)
            if m1:
                policy_config_dict = parser_dict.setdefault('dhcp_guard_policy_config', {})
                policy_config_dict.update({'device_role': m1.groupdict()['device_role']})
                continue
            
            #Trusted Port 
            m2 = p2.match(line)     
            if m2:
                policy_config_dict = parser_dict.setdefault('dhcp_guard_policy_config', {})
                policy_config_dict.update({'trusted_port': True})
                continue
            
            #Max Preference: 255
            m3 = p3.match(line)
            if m3:
                policy_config_dict = parser_dict.setdefault('dhcp_guard_policy_config', {})
                policy_config_dict.update({'max_preference': int(m3.groupdict()['max_preference'])})
                continue

            #Min Preference: 0
            m4 = p4.match(line)
            if m4:
                policy_config_dict = parser_dict.setdefault('dhcp_guard_policy_config', {})
                policy_config_dict.update({'min_preference':  int(m4.groupdict()['min_preference'])})
                continue

            #Source Address Match Access List: acl1
            m5 = p5.match(line)
            if m5:
                policy_config_dict = parser_dict.setdefault('dhcp_guard_policy_config', {})
                policy_config_dict.update({'access_list':  m5.groupdict()['access_list']})
                continue
            
            #Prefix List Match Prefix List: abc
            m6 = p6.match(line)
            if m6: 
                policy_config_dict.update({'prefix_list': m6.groupdict()['prefix_list']})
                continue

            #Target               Type  Policy               Feature        Target range
            #vlan 2               VLAN  pol1                 DHCP Guard     vlan all
            #Et0/0                PORT  pol1                 DHCP Guard     vlanall
            m7 = p7.match(line)
            if m7:
                policy_config_dict = parser_dict.setdefault('dhcp_guard_policy_config', {})
                targets_dict = policy_config_dict.setdefault('targets', {})
                target = m7.groupdict()['target']
                target_dict = targets_dict.setdefault(target, {})

                target_dict.update({'target': m7.groupdict()['target']})
                target_dict.update({'type':  m7.groupdict()['type']})
                target_dict.update({'feature':  m7.groupdict()['feature']})
                target_dict.update({'target_range': m7.groupdict()['target_range']})

        return parser_dict
