"""
    show_ipv6.py
    IOSXE parsers for the following show commands:

    * show ipv6 neighbors
    * show ipv6 neighbors vrf <vrf>
    * show ipv6 neighbors <interface>
    * show ipv6 neighbors detail
    * show ipv6 neighbors vrf <vrf> detail
    * show ipv6 interface (from show_interface.py)
    * show ipv6 dhcp-ldra
    * show ipv6 dhcp-ldra statistics
    * show ipv6 routers
    * show ipv6 mrib route
    * show ipv6 mrib route {group}
    * show ipv6 mrib route {group} {source}
    * show ipv6 mrib route vrf {vrf}
    * show ipv6 mrib route vrf {vrf} {group}
    * show ipv6 mrib route vrf {vrf} {group} {source}   
    * show ipv6 mfib
    * show ipv6 mfib status
    * show ipv6 mfib {group}
    * show ipv6 mfib {group} {source}
    * show ipv6 mfib verbose
    * show ipv6 mfib {group} verbose
    *  show ipv6 mfib {group} {source} verbose
    *  show ipv6 mfib vrf {vrf}
    *  show ipv6 mfib vrf {vrf} {group}
    *  show ipv6 mfib vrf {vrf} {group} {source}
    *  show ipv6 mfib vrf {vrf} verbose
    *  show ipv6 mfib vrf {vrf} {group} verbose
    *  show ipv6 mfib vrf {vrf} {group} {source} verbose
    * show ipv6 dhcp pool
    * show ipv6 dhcp pool {poolname}
    * show ipv6 dhcp statistics
    * show ipv6 dhcp binding 
    * show ipv6 dhcp relay binding
    * show ipv6 general-prefix
    * show ipv6 pim neighbor {intf}
    * show ipv6 cef exact-route {source} {destination}
    * show ipv6 mfib count
    * sh ipv6 mfib FF03::1:1:1 count
    * sh ipv6 mfib FF03::1:1:1 10::1:1:200 count
    * show ipv6 virtual-reassembly features
    * show ipv6 mfib {group} active
    * show ipv6 traffic
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, ListOf

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
                        r'(?P<link_layer_address>\S+)\s+(?P<neighbor_state>\S+)'
                        r'\s+(?P<interface>\S+)$')

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
                         r'(?P<link_layer_address>\S+)\s+(?P<neighbor_state>\S+)\s+'
                         r'(?P<interface>\S+)$')

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

class ShowIpv6DhcpLdraSchema(MetaParser):
    """
        Schema for show ipv6 dhcp-ldra
    """
    schema = {
        'ldra': {
            'status': str,
            Any(): {
                'targets': list
            }
        }
    }

class ShowIpv6DhcpLdra(ShowIpv6DhcpLdraSchema):
    """
        Parser for show ipv6 dhcp-ldra
    """

    cli_command = 'show ipv6 dhcp-ldra'

    def cli(self, output=None):
        """
            Parse the output from the cli and return parsed data
        """

        if output is None:
            # get output from device
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        result_dict = {}

        # DHCPv6 LDRA is Enabled.
        p0 = re.compile(r'^DHCPv6 +LDRA +is +(?P<status>(Enabled|Disabled))')
        # DHCPv6 LDRA policy: client-facing-disable
        # DHCPv6 LDRA policy: client-facing-trusted
        # DHCPv6 LDRA policy: client-facing-untrusted
        # DHCPv6 LDRA policy: server-facing
        p1 = re.compile(r'^DHCPv6 +LDRA +policy: +(?P<policy>[a-zA-z\-]+)')
        #         Target: Gi1/0/20
        #         Target: Gi1/0/12 vlan 2     vlan 3     vlan 10
        #         Target: Gi1/0/11 vlan 4     vlan 5     vlan 11
        #         Target: Gi1/0/6 Gi1/0/7 Gi1/0/8 Gi1/0/9 Gi1/0/10 Gi1/0/13 Gi1/0/14 Gi1/0/15
        p2 = re.compile(r'^Target:\s+(?P<targets>[\w\/\s]+)')
        #                 Gi1/0/16 Gi1/0/17 Gi1/0/18 Gi1/0/19
        p3 = re.compile(r'^(?P<targets_ext>[\w\/\s]+)')

        for line in output.splitlines():
            line = line.strip()

            # skip empty lines
            if not line:
                continue

            # DHCPv6 LDRA is Enabled.
            m0 = p0.match(line)
            if m0:
                group = m0.groupdict()
                ldra_dict = result_dict.setdefault('ldra', group)
                continue

            # DHCPv6 LDRA policy: client-facing-disable
            # DHCPv6 LDRA policy: client-facing-trusted
            # DHCPv6 LDRA policy: client-facing-untrusted
            # DHCPv6 LDRA policy: server-facing
            m1 = p1.match(line)
            if m1:
                pol_group = {}
                m1_group = m1.groupdict()
                pol_group['policy'] = m1_group['policy'].replace('-', '_')
                ldra_dict[pol_group['policy']] = {}
                continue

            #         Target: Gi1/0/20
            #         Target: Gi1/0/12 vlan 2     vlan 3     vlan 10
            #         Target: Gi1/0/11 vlan 4     vlan 5     vlan 11
            #         Target: Gi1/0/6 Gi1/0/7 Gi1/0/8 Gi1/0/9 Gi1/0/10 Gi1/0/13 Gi1/0/14 Gi1/0/15
            m2 = p2.match(line)
            if m2:
                intf_group = m2.groupdict()
                intf_list = re.split(r'\s+(?!\d+)', intf_group['targets'])
                ldra_dict[pol_group['policy']]['targets'] = \
                    [Common.convert_intf_name(intf) for intf in intf_list]
                continue

            #                 Gi1/0/16 Gi1/0/17 Gi1/0/18 Gi1/0/19
            m3 = p3.match(line)
            if m3:
                intf_group_ext = m3.groupdict()
                intf_list = re.split(r'\s+(?!\d+)', intf_group_ext['targets_ext'])
                ldra_dict[pol_group['policy']]['targets'].extend(
                    [Common.convert_intf_name(intf) for intf in intf_list])
                continue

        return result_dict

class ShowIpv6DhcpLdraStatisticsSchema(MetaParser):
    """
        Schema for show ipv6 dhcp-ldra statistics
    """

    schema = {
        'statistics': {
            Any(): {
                'total_recvd': int,
                'total_sent': int,
                'total_discard': int,
                Optional('msg_sent'): {
                    Any(): int
                },
                Optional('msg_received'): {
                    Any(): int
                }
            }
        }
    }

class ShowIpv6DhcpLdraStatistics(ShowIpv6DhcpLdraStatisticsSchema):
    """
        Parser for show ipv6 dhcp-ldra statistics
    """

    cli_command = 'show ipv6 dhcp-ldra statistics'

    def cli(self, output=None):
        """
            Parse the output from the cli and return parsed data
        """

        if output is None:
            # get output from device
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        result_dict = {}

        #                 DHCPv6 LDRA client facing statistics.
        #                 DHCPv6 LDRA server facing statistics.
        p0 = re.compile(r'DHCPv6\s+LDRA\s+(?P<mode>[\w\s]+)\s+statistics')
        # Messages received                20
        p1 = re.compile(r'Messages\s+received\s+(?P<total_recvd>\d+)')
        # Messages sent                    20
        p2 = re.compile(r'Messages\s+sent\s+(?P<total_sent>\d+)')
        # Messages discarded               0
        p3 = re.compile(r'Messages\s+discarded\s+(?P<total_discard>\d+)')
        # Messages                         Received
        # Messages                         Sent
        p4 = re.compile(r'Messages\s+(?P<msg_mode>Received|Sent)')
        # SOLICIT                          1
        # REQUEST                          1
        # RENEW                            18
        # RELAY-FORWARD                    20
        p5 = re.compile(r'^(?P<msg_type>[a-zA-Z\-]+)\s+(?P<count>\d+)')

        for line in output.splitlines():
            line = line.strip()

            # skip empty lines
            if not line:
                continue

            #                 DHCPv6 LDRA client facing statistics.
            #                 DHCPv6 LDRA server facing statistics.
            m0 = p0.match(line)
            if m0:
                group = {}
                m0_group = m0.groupdict()
                group['mode'] = m0_group['mode'].replace(' ', '_')
                stats_dict = result_dict.setdefault('statistics', {})
                stats_dict[group['mode']] = {}
                continue

            # Messages received                20
            m1 = p1.match(line)
            if m1:
                recvd_group = m1.groupdict()
                recvd_group['total_recvd'] = int(recvd_group['total_recvd'])
                stats_dict[group['mode']].update(recvd_group)
                continue

            # Messages sent                    20
            m2 = p2.match(line)
            if m2:
                sent_group = m2.groupdict()
                sent_group['total_sent'] = int(sent_group['total_sent'])
                stats_dict[group['mode']].update(sent_group)
                continue

            # Messages discarded               0
            m3 = p3.match(line)
            if m3:
                discard_group = m3.groupdict()
                discard_group['total_discard'] = int(discard_group['total_discard'])
                stats_dict[group['mode']].update(discard_group)
                continue

            # Messages                         Received
            # Messages                         Sent
            m4 = p4.match(line)
            if m4:
                msg_mode_group = m4.groupdict()
                msg_dict = stats_dict[group['mode']].setdefault(f"msg_{msg_mode_group['msg_mode'].lower()}", {})
                continue

            # SOLICIT                          1
            # REQUEST                          1
            # RENEW                            18
            # RELAY-FORWARD                    20
            m5 = p5.match(line)
            if m5:
                msg_type_group = m5.groupdict()
                msg_dict[msg_type_group['msg_type'].lower().replace('-', '_')] = int(msg_type_group['count'])
                continue

        return result_dict

# ====================================================
#  schema for show ipv6 routers
# ====================================================
class ShowIpv6RoutersSchema(MetaParser):
    """Schema for 
       show ipv6 routers
       show ipv6 routers vrf {vrf}"""
    schema = {
        'router': {
            Any(): {
                Optional('status'): str,
                'interface': str,
                'last_update': int,
                'hops': int,
                'lifetime': int,
                'addr_flag': int,
                'other_flag': int,
                'mtu': int,
                'home_agent_flag': int,
                'preference': str,
                'reachable_time': int,
                'retransmit_time': int,
                'prefix': {
                    Any(): {
                        'valid_lifetime': int,
                        'preferred_lifetime': int
                    }
                }
            }
        }
    }

# ================================================================
# Parser for:
#   * 'show ipv6 routers'
#   * 'show ipv6 routers vrf {vrf}'
# ================================================================
class ShowIpv6Routers(ShowIpv6RoutersSchema):
    """ Parser for:
                show ipv6 routers
                show ipv6 routers vrf {vrf}
    """

    cli_command = ['show ipv6 routers',
                   'show ipv6 routers vrf {vrf}']

    def cli(self, vrf=None, output=None):
        """ cli for:
         ' show ipv6 routers '
         ' show ipv6 routers vrf {vrf}'
        """
        if output is None:
            if vrf and vrf != 'default':
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        # Router FE80::FA7A:41FF:FE25:2502 on Vlan100, last update 0 min, CONFLICT
        # Router FE80::FA7A:41FF:FE25:2502 on Vlan100, last update 0 min
        p1 = re.compile(r'^Router +(?P<router_link_local_ip>\S+)\s+\w+\s+'
                        r'(?P<interface>\S+), +last +update +'
                        r'(?P<last_update>\d+) +min(\,\s|)'
                        r'(?:(?P<status>\w+))?')

        # Hops 64, Lifetime 200 sec, AddrFlag=0, OtherFlag=0, MTU=1500
        p2 = re.compile(r'^Hops +(?P<hops>\d+), +Lifetime +(?P<lifetime>\d{1,4}) +sec, +AddrFlag+\=(?P<addr_flag>\d+), '
                        r'+OtherFlag\=(?P<other_flag>\d+), +MTU\=(?P<mtu>\d{1,4})$')

        # HomeAgentFlag=0, Preference=Low
        p3 = re.compile(r'^HomeAgentFlag\=(?P<home_agent_flag>\d+), +Preference\=(?P<preference>\w+)$')

        # Reachable time 0 (unspecified), Retransmit time 0 (unspecified)
        p4 = re.compile(r'^Reachable +time +(?P<reachable_time>\d+) \S+, +Retransmit +time +(?P<retransmit_time>\d+)')

        #Prefix 111::/64 onlink autoconfig
        p5 = re.compile(r'^Prefix +(?P<prefix_id>\S+) +onlink +autoconfig$')

        # Valid lifetime 12, preferred lifetime 8
        p6 = re.compile(r'^Valid +lifetime +(?P<valid_lifetime>\d+), +preferred +lifetime +(?P<preferred_lifetime>\d+)$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()


            # Router FE80::FA7A:41FF:FE25:2502 on Vlan100, last update 0 min, CONFLICT
            # Router FE80::FA7A:41FF:FE25:2502 on Vlan100, last update 0 min
            m = p1.match(line)
            if m:
                router_link_local = m.groupdict()['router_link_local_ip']
                router_dict = ret_dict.setdefault('router', {}).setdefault(
                    router_link_local, {})
                router_dict.update({
                    'interface': m.groupdict()['interface'],
                    'last_update': int(m.groupdict()['last_update'])
                })

                status = m.groupdict().get('status')
                if status:
                    router_dict['status'] = status
                continue


            # Hops 64, Lifetime 200 sec, AddrFlag=0, OtherFlag=0, MTU=1500
            m = p2.match(line)
            if m:
                router_dict.update({
                    'hops': int(m.groupdict()['hops']),
                    'lifetime': int(m.groupdict()['lifetime']),
                    'addr_flag': int(m.groupdict()['addr_flag']),
                    'other_flag': int(m.groupdict()['other_flag']),
                    'mtu': int(m.groupdict()['mtu'])
                })
                continue

            # HomeAgentFlag=0, Preference=Low
            m = p3.match(line)
            if m:
                router_dict.update({
                    'home_agent_flag': int(m.groupdict()['home_agent_flag']),
                    'preference': m.groupdict()['preference']
                })
                continue

            # Reachable time 0 (unspecified), Retransmit time 0 (unspecified)
            m = p4.match(line)
            if m:
                router_dict.update({
                    'reachable_time': int(m.groupdict()['reachable_time']),
                    'retransmit_time': int(m.groupdict()['retransmit_time'])
                })
                continue


            # Prefix 111::/64 onlink autoconfig
            m = p5.match(line)
            if m:
                prefix_num = m.groupdict()['prefix_id']
                prefix_dict = router_dict.setdefault('prefix', {}).setdefault(prefix_num, {})
                continue

            # Valid lifetime 12, preferred lifetime 8
            m = p6.match(line)
            if m:
                prefix_dict.update({
                    'valid_lifetime': int(m.groupdict()['valid_lifetime']),
                    'preferred_lifetime': int(m.groupdict()['preferred_lifetime'])
                })
                continue

        return ret_dict



class ShowIpv6MribSchema(MetaParser):
    """Schema for:
       show ipv6 mrib route
       show ipv6 mrib route {group}
       show ipv6 mrib route {group} {source} 
       show ipv6 mrib route vrf {vrf}
       show ipv6 mrib route vrf {vrf} {group}
       show ipv6 mrib route vrf {vrf} {group} {source}
    """
          
    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'multicast_group': {
                            Any(): {
                                'source_address': {
                                    Any(): {                            
                                        'rpf_nbr': str,
                                        Optional('flags'): str,                                  
                                        'incoming_interface_list': {
                                            Any(): {
                                                'ingress_flags': str,
                                            } 
                                        },
                                        'egress_interface_list': {
                                            Any(): {
                                                'egress_flags': str,
                                                Optional('egress_next_hop'): str,
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

class ShowIpv6Mrib(ShowIpv6MribSchema):
    """Parser for:
    show ipv6 mrib route
    show ipv6 mrib route {group}
    show ipv6 mrib route {group} {source}
    show ipv6 mrib route vrf {vrf}
    show ipv6 mrib route vrf {vrf} {group}
    show ipv6 mrib route vrf {vrf} {group} {source}"""

    cli_command = ['show ipv6 mrib route',  
                   'show ipv6 mrib route {group}',
                   'show ipv6 mrib route {group} {source}',
                   'show ipv6 mrib vrf {vrf} route', 
                   'show ipv6 mrib vrf {vrf} route {group}', 
                   'show ipv6 mrib vrf {vrf} route {group} {source}']


    def cli(self, vrf='default', group='',source='',address_family='ipv6',output=None):
        cmd="show ipv6 mrib "
        if output is None:
            
            if vrf != 'default':
                cmd += " vrf {vrf} ".format(vrf=vrf)            
            cmd += "route"                        
            if group:
                cmd += " {group}".format(group=group)
            if source:
                cmd += " {source}".format(source=source)               
                  
            output = self.device.execute(cmd)

        # initial variables        
        mrib_dict = {}
        sub_dict = {}
        outgoing = False				 
					 
        # (*,225.1.1.1) RPF nbr: 10.10.10.1 Flags: C          
        # (3.3.3.3,225.1.1.1) RPF nbr: 10.10.10.1 Flags:
        # (*,FF05:1:1::1) RPF nbr: 2001:150:1:1::1 Flags: C
        #(2001:192:168:7::11,FF05:1:1::1) RPF nbr: 2001:150:1:1::1 Flags: L C

        p1 = re.compile(r'^\((?P<source_address>[\w\:\.\*\/]+)\,'
                     r'(?P<multicast_group>[\w\:\.\/]+)\)'
                     r' +RPF nbr: (?P<RPF_nbr>[\w\:\.\/]+)'
                     r'\s+Flags\:(?P<mrib_flags>[\w\s]+|$)')

        # GigabitEthernet2/0/6 Flags: A NS 
        # Tunnel1 Flags: A NS  		 
        p2 = re.compile(r'^(?P<ingress_if>[\w\.\/\, ]+)'
                         r'\s+Flags\: +(?P<ingress_flags>A[\s\w]+|[\s\w]+ +A[\s\w]+|A$)') 
						 
        #  LISP0.1 Flags: F NS  Next-hop: 100.154.154.154
        #  LISP0.1 Flags: F NS   Next-hop: (100.11.11.11, 235.1.3.167)
        p3 = re.compile(r'^(?P<egress_if>[\w\.\/\,]+)'
                        r'\s+Flags\:\s+(?P<egress_flags>F[\s\w]+)+Next-hop\:\s+(?P<egress_next_hop>([\w\:\.\*\/]+)|(\([\w\:\.\*\/]+\, +[\w\:\.\*\/]+\)))')

        #  Vlan2006 Flags: F LI NS
        p4=re.compile(r'^(?P<egress_if>[\w\.\/\, ]+)'
                        r'\s+Flags\: +(?P<egress_flags>F[\s\w]+)')            

        for line in output.splitlines():
            line=(line.strip()).replace('\t',' ')

            mrib_dict.setdefault('vrf',{})         

            mrib_data = mrib_dict['vrf'].setdefault(vrf,{}).setdefault('address_family',{}).setdefault(address_family,{})     

            #  (*,225.1.1.1) Flags: C HW
            # (70.1.1.10,225.1.1.1) Flags: HW
            #  (*,FF05:1:1::1) Flags: C HW
            # (2001:70:1:1::10,FF05:1:1::1) Flags: HW
            m = p1.match(line)
            if m:
                group = m.groupdict()
                source_address = group['source_address']
                multicast_group = group['multicast_group']

                mrib_data.setdefault('multicast_group',{})
                sub_dict = mrib_data['multicast_group']\
                    .setdefault(multicast_group,{})\
                    .setdefault('source_address',{})\
                    .setdefault(source_address,{})                
                sub_dict['rpf_nbr'] = m.groupdict()['RPF_nbr']
                sub_dict['flags'] = m.groupdict()['mrib_flags']
                
                continue
                
            # GigabitEthernet2/0/6 Flags: A NS	
            # Tunnel50 Flags: A            
            sw_data=sub_dict
            m=p2.match(line)
            if m:
                group = m.groupdict()
                ingress_interface = group['ingress_if']
                ing_intf_dict=sw_data.setdefault('incoming_interface_list',{}).setdefault(ingress_interface,{})   
                ing_intf_dict['ingress_flags'] = group['ingress_flags']
                continue
                    

            #  LISP0.1 Flags: F NS  Next-hop: 100.154.154.154 
            # LISP0.1 Flags: F NS	Next-hop: (100.11.11.11, 235.1.3.167)
            m=p3.match(line)
            if m:
                group = m.groupdict()
                egress_interface = group['egress_if']  

                if group['egress_next_hop']:
                     
                    egress_next_hop = group['egress_next_hop']
                    #Overlay interfaces have multiple egress interfaces with same  ID
                    #appending egress interface with nexthop to get complete data structure
                    # LISP0.1 Flags: F      Next-hop: 100.154.154.154
                    # LISP0.1 Flags: F      Next-hop: 100.33.33.33
                    # LISP0.1 Flags: F      Next-hop: 100.88.88.88

                    egress_interface = group['egress_if']+'-'+egress_next_hop

                egress_data=sw_data.setdefault('egress_interface_list',{}).setdefault(egress_interface,{})  
                egress_data['egress_flags'] = group['egress_flags']                 
                egress_data['egress_next_hop'] =  group['egress_next_hop']
                   
                continue    

            # Vlan2001 Flags: F NS
            m=p4.match(line)
            if m:
                group = m.groupdict()
                egress_flags = group['egress_flags'] 
                egress_interface = group['egress_if']
                    
                egress_data=sw_data.setdefault('egress_interface_list',{}).setdefault(egress_interface,{})                                    
                egress_data['egress_flags'] = egress_flags                  
                  
                continue                     
                       
        return mrib_dict

# ========================================================
# Parser for 'show ipv6 mfib status'
# ========================================================

class ShowIpv6MfibStatusSchema(MetaParser):
    """
    Schema for 'show ipv6 mfib status'

    """
    schema = {
        'configuration_status' : str,
        'operational_status' : str,
        'initialization_state' : str,
        'total_signalling_packets_queued' : int,
        'Process_status' : {
            'status' : str,
            'pid' : int
        },
        'table' : {
            'active' : int,
            'mrib' : int,
            'io' : int
        },
    }

class ShowIpv6MfibStatus(ShowIpv6MfibStatusSchema):

    '''
    Parser for 'show ipv6 mfib status'

    '''

    cli_command = 'show ipv6 mfib status'
    def cli(self,output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        
        # Configuration Status: enabled
        p1 = re.compile(r'^Configuration Status: +(?P<configuration_status>\w+)$')

        # Operational Status: running
        p2 = re.compile(r'^Operational Status: +(?P<operational_status>\w+)$')

        # Initialization State: Running
        p3 = re.compile(r'^Initialization State: +(?P<initialization_state>\w+)$')

        # Total signalling packets queued: 0
        p4 = re.compile(r'^Total signalling packets queued: +(?P<total_signalling_packets_queued>\d+)$')

        # Process Status: may enable - 3 - pid 737
        p5 = re.compile(r'^Process Status: may +(?P<status>\w+) - \d+ - pid +(?P<pid>\d+)')

        # Tables 1/1/0 (active/mrib/io)
        p6 = re.compile(r'^Tables (?P<active>\d)+(\/)+(?P<mrib>\d)(\/)+(?P<io>\d) +(\()+active+(\/)+mrib+(\/)+io+(\))$')
        
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            
            # Configuration Status: enabled
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['configuration_status'] = group['configuration_status']
                continue

            # Operational Status: running
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['operational_status'] = group['operational_status']
                continue

            # Initialization State: Running
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict['initialization_state'] = group['initialization_state']
                continue

            # Total signalling packets queued: 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict['total_signalling_packets_queued'] = int(group['total_signalling_packets_queued'])
                continue

            # Process Status: may enable - 3 - pid 737
            m = p5.match(line)
            if m:
                group = m.groupdict()
                process_dict = ret_dict.setdefault('Process_status',{})
                process_dict.update({
                    'status': group['status'],
                    'pid': int(group['pid'])
                })
                continue

            # Tables 1/1/0 (active/mrib/io)
            m = p6.match(line)
            if m:
                group = m.groupdict()
                table_dict = ret_dict.setdefault('table',{})
                table_dict.update({
                    'active' : int(group['active']),
                    'mrib' : int(group['mrib']),
                    'io' : int(group['io'])
                    })
                continue

        return ret_dict

# Schema for  show ipv6 mfib
# Schema for  show ipv6 mfib {group}
# Schema for  show ipv6 mfib {group} {source}
# Schema for  show ipv6 mfib verbose
# Schema for  show ipv6 mfib {group} verbose
# Schema for  show ipv6 mfib {group} {source} verbose
# Schema for  show ipv6 mfib vrf {vrf}
# Schema for  show ipv6 mfib vrf {vrf} {group}
# Schema for  show ipv6 mfib vrf {vrf} {group} {source}
# Schema for  show ipv6 mfib vrf {vrf} verbose
# Schema for  show ipv6 mfib vrf {vrf} {group} verbose
# Schema for  show ipv6 mfib vrf {vrf} {group} {source} verbose

# =====================================
class ShowIpv6MfibSchema(MetaParser):
    """Schema for:
      show ipv6 mfib
      show ipv6 mfib {group}
      show ipv6 mfib {group} {source}
      show ipv6 mfib verbose
      show ipv6 mfib {group} verbose
      show ipv6 mfib {group} {source} verbose
      show ipv6 mfib vrf {vrf}
      show ipv6 mfib vrf {vrf} {group}
      show ipv6 mfib vrf {vrf} {group} {source}
      show ipv6 mfib vrf {vrf} verbose
      show ipv6 mfib vrf {vrf} {group} verbose
      show ipv6 mfib vrf {vrf} {group} {source} verbose"""

    schema = {
        'vrf':
            {Any():
                {'address_family':
                    {Any():
                        {Optional('multicast_group'):
                            {Any():
                                {Optional('source_address'):
                                    {Any():
                                       {
                                            Optional('oif_ic_count'): Or(str,int),
                                            Optional('oif_a_count'): Or(str,int),
                                            Optional('flags'): str,
                                            Optional('sw_packet_count'): Or(str,int),
                                            Optional('sw_packets_per_second'): Or(str,int),
                                            Optional('sw_average_packet_size'): Or(str,int),
                                            Optional('sw_kbits_per_second'): Or(str,int),
                                            Optional('sw_total'): Or(str,int),
                                            Optional('sw_rpf_failed'): Or(str,int),
                                            Optional('sw_other_drops'): Or(str,int),
                                            Optional('hw_packet_count'): Or(str,int),
                                            Optional('hw_packets_per_second'): Or(str,int),
                                            Optional('hw_average_packet_size'): Or(str,int),
                                            Optional('hw_kbits_per_second'): Or(str,int),
                                            Optional('hw_total'): Or(str,int),
                                            Optional('hw_rpf_failed'): Or(str,int),
                                            Optional('hw_other_drops'): Or(str,int),
                                            Optional('incoming_interfaces'): {
                                                Any(): {
                                                     Optional('ingress_flags'): str,                                                  	
                                                     Optional('ingress_vxlan_version'): str,
                                                     Optional('ingress_vxlan_cap'): str,
                                                     Optional('ingress_vxlan_vni'): str,
                                                     Optional('ingress_vxlan_nxthop'): str,
                                                     Optional('ingress_mdt_ip'): str,
                                                    }
                                                },
                                            Optional('outgoing_interfaces'): {
                                                Any(): {
                                                     Optional('egress_flags'): str,
                                                     Optional('egress_rloc'): str,
                                                     Optional('egress_underlay_mcast'): str,
                                                     Optional('egress_adj_mac'): str,
                                                     Optional('egress_hw_pkt_count'): Or(str,int),
                                                     Optional('egress_fs_pkt_count'): Or(str,int),
                                                     Optional('egress_ps_pkt_count'): Or(str,int),
                                                     Optional('egress_pkt_rate'): Or(str,int),
                                                     Optional('egress_vxlan_version'): str,
                                                     Optional('egress_vxlan_cap'): str,
                                                     Optional('egress_vxlan_vni'): str,
                                                     Optional('egress_vxlan_nxthop'): str,
                                                     Optional('egress_mdt_ip'): str,
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    }
                },
            }

# =====================================
# Parser for  show ipv6 mfib
# Parser for  show ipv6 mfib {group}
# Parser for  show ipv6 mfib {group} {source}
# Parser for  show ipv6 mfib verbose
# Parser for  show ipv6 mfib {group} verbose
# Parser for  show ipv6 mfib {group} {source} verbose
# Parser for  show ipv6 mfib vrf {vrf}
# Parser for  show ipv6 mfib vrf {vrf} {group}
# Parser for  show ipv6 mfib vrf {vrf} {group} {source}
# Parser for  show ipv6 mfib vrf {vrf} verbose
# Parser for  show ipv6 mfib vrf {vrf} {group} verbose
# Parser for  show ipv6 mfib vrf {vrf} {group} {source} verbose 

# =====================================
class ShowIpv6Mfib(ShowIpv6MfibSchema):
    """Parser for:
      show ipv6 mfib
      show ipv6 mfib {group}
      show ipv6 mfib {group} {source}
      show ipv6 mfib verbose
      show ipv6 mfib {group} verbose
      show ipv6 mfib {group} {source} verbose
      show ipv6 mfib vrf {vrf}
      show ipv6 mfib vrf {vrf} {group}
      show ipv6 mfib vrf {vrf} {group} {source}
      show ipv6 mfib vrf {vrf} verbose
      show ipv6 mfib vrf {vrf} {group} verbose
      show ipv6 mfib vrf {vrf} {group} {source} verbose"""
    cli_command = ['show ipv6 mfib',
                   'show ipv6 mfib {group}',
                   'show ipv6 mfib {group} {source}',
                   'show ipv6 mfib {verbose}',
                   'show ipv6 mfib {group} {verbose}',
                   'show ipv6 mfib {group} {source} {verbose}',
                   'show ipv6 mfib vrf {vrf}',
                   'show ipv6 mfib vrf {vrf} {group}',
                   'show ipv6 mfib vrf {vrf} {group} {source}',
                   'show ipv6 mfib vrf {vrf} {verbose}',
                   'show ipv6 mfib vrf {vrf} {group} {verbose}',
                   'show ipv6 mfib vrf {vrf} {group} {source} {verbose}' ]


    def cli(self, vrf='Default',verbose='',group='',source='', address_family='ipv6',output=None):
        cmd="show ipv6 mfib"
        if output is None:

            if vrf != 'Default':
                cmd += " vrf {vrf}".format(vrf=vrf)

            if group:
                cmd += " {group}".format(group=group)
            if source:
                cmd += " {source}".format(source=source)
            if verbose:
                cmd += " {verbose}".format(verbose=verbose)

            out = self.device.execute(cmd)
        else:
            out = output

        # initial variables

        mfib_dict = {}
        sub_dict = {}
        outgoing = False
        egress_data = {}
        egress_data_update = False
        #Default
        #VRF vrf1
        p1 = re.compile(r'^(VRF\s+)?(?P<vrf>[\w]+)$')

        #  (*,225.1.1.1) Flags: C HW
        # (70.1.1.10,225.1.1.1) Flags: HW
        #  (*,FF05:1:1::1) Flags: C HW
        # (2001:70:1:1::10,FF05:1:1::1) Flags: HW
        p3 = re.compile(r'^\((?P<source_address>[\w\:\.\*\/]+)\,'
                     r'(?P<multicast_group>[\w\:\.\/]+)\)'
                     r'\s+Flags\:\s*(?P<mfib_flags>[\w\s]*)$')
        #0x1AF0  OIF-IC count: 0, OIF-A count: 1
        p4 = re.compile(r'\w+ +OIF-IC count: +(?P<oif_ic_count>[\w]+)'
                   r'\, +OIF-A count: +(?P<oif_a_count>[\w]+)$')
        # SW Forwarding: 0/0/0/0, Other: 0/0/0
        p5 = re.compile(r'SW Forwarding\:\s+(?P<sw_packet_count>[\w]+)\/'
                     r'(?P<sw_packets_per_second>[\w]+)\/'
                     r'(?P<sw_average_packet_size>[\w]+)\/'
                     r'(?P<sw_kbits_per_second>[\w]+)\,'
                     r'\s+Other\: +(?P<sw_total>[\w]+)\/'
                     r'(?P<sw_rpf_failed>[\w]+)\/'
                     r'(?P<sw_other_drops>[\w]+)$')
        #HW Forwarding:   222/0/204/0, Other: 0/0/0
        p6 = re.compile(r'^HW\s+Forwarding\:\s+(?P<hw_packet_count>[\w]+)\/'
                     r'(?P<hw_packets_per_second>[\w]+)\/'
                     r'(?P<hw_average_packet_size>[\w]+)\/'
                     r'(?P<hw_kbits_per_second>[\w]+)\,'
                     r'\s+Other\: +(?P<hw_total>[\w]+)\/'
                     r'(?P<hw_rpf_failed>[\w]+)\/'
                     r'(?P<hw_other_drops>[\w]+)$')
        # LISP0.1 Flags: A NS
        #  Null0 Flags: A
        #  GigabitEthernet1/0/1 Flags: A NS
        #Tunnel0, VXLAN Decap Flags: A
        #Vlan500, VXLAN v6 Encap (50000, 239.1.1.0) Flags: A
        #Port-channel5 Flags: RA A MA
        # Tunnel0, MDTv6overv4/::FFFF:226.10.10.10 Flags: A

        p7 = re.compile(r'^(?P<ingress_if>[\w\/\.\-\:]+)'
                        r'(?:,\s*MDTv6overv4\/(?:::FFFF:)?(?P<ingress_mdt_ip>\d+\.\d+\.\d+\.\d+))?'
                        r'(\,\s+VXLAN +(?P<ingress_vxlan_version>[v0-9]+)?(\s+)?(?P<ingress_vxlan_cap>[\w]+)(\s+)?(\(?(?P<ingress_vxlan_vni>[0-9]+)(\,\s+)?(?P<ingress_vxlan_nxthop>[\w:./]+)?\)?)?)?'
                        r' +Flags\: +(?P<ingress_flags>A[\s\w]+|[\s\w]+ +A[\s\w]+|A$)')

        #Vlan2001 Flags: F NS
        #LISP0.1, (100.11.11.11, 235.1.3.167) Flags:
        #Tunnel1, VXLAN v6 Decap Flags: F NS
        # Vlan200, VXLAN v4 Encap (10100, 239.1.1.1) Flags: F
        #L2LISP0.1502, L2LISP v6 Decap Flags: F NS
        #LISP0.101, 100:88:88::88 Flags: F
        #Port-channel5 Flags: RF F NS
        # Tunnel8, MDTv6overv4/::FFFF:226.10.10.10 Flags: F NS
        p8 = re.compile(r'^(?P<egress_if>[\w\/\.\-\:]+)'
                        r'(\,\s+L2LISP\s*v6\s*Decap\s*)?'
                        r'(?:,\s*MDTv6overv4\/(?:::FFFF:)?(?P<egress_mdt_ip>\d+\.\d+\.\d+\.\d+))?'
                        r'(\,\s+\(?(?P<egress_rloc>[\w:\.]+)(\,\s+)?(?P<egress_underlay_mcast>[\w\.]+)?\)?)?'
                        r'(\,\s+VXLAN +(?P<egress_vxlan_version>[v0-9]+)?(\s+)?(?P<egress_vxlan_cap>[\w]+)(\s+)?'
                        r'(\(?(?P<egress_vxlan_vni>[0-9]+)(\,\s+)?(?P<egress_vxlan_nxthop>[\w:.]+)?\)?)?)?'
                        r'\s+Flags\:\s?(?P<egress_flags>F[\s\w]+|[\s\w]+\s+F[\s\w]+|F$|[\s\w]+\s+F$|$)')
        

        #CEF: Adjacency with MAC: 01005E010101000A000120010800
        p9_1 = re.compile(r'^CEF\: +(?P<egress_adj_mac>[\w \:\(\)\.]+)$')
        #CEF: Special OCE (discard)
        p9_2 = re.compile(r'^CEF\: +(?P<egress_adj_mac>[\w \(\.\)]+)$')
        #Pkts: 0/0/2    Rate: 0 pps
        p10 = re.compile(r'^Pkts\:\s+(?P<egress_hw_pkt_count>[\w]+)\/'
                         r'(?P<egress_fs_pkt_count>[\w]+)\/'
                         r'(?P<egress_ps_pkt_count>[\w]+)'
                         r'\s+Rate\:\s+(?P<egress_pkt_rate>[\w]+)\s+pps$')

        for line in out.splitlines():
            line = line.strip()

            mfib_dict.setdefault('vrf',{})
            #Default   (Would not be displayed in the output)
            #VRF vrf1
            m = p1.match(line)
            if m:
                vrf=m.groupdict()['vrf']
                continue

            mfib_data = mfib_dict['vrf'].setdefault(vrf,{}).setdefault('address_family',{}).setdefault(address_family,{})

            #  (*,225.1.1.1) Flags: C HW
            # (70.1.1.10,225.1.1.1) Flags: HW
            #  (*,FF05:1:1::1) Flags: C HW
            # (2001:70:1:1::10,FF05:1:1::1) Flags: HW
            m = p3.match(line)
            if m:
                group = m.groupdict()
                source_address = group['source_address']
                multicast_group = group['multicast_group']

                mfib_data.setdefault('multicast_group',{})
                sub_dict = mfib_data.setdefault('multicast_group',{}).setdefault(
                    multicast_group,{}).setdefault('source_address',
                    {}).setdefault(source_address,{})

                sub_dict['flags'] = group['mfib_flags']
                continue

            sw_data=sub_dict
            #0x1AF0  OIF-IC count: 0, OIF-A count: 1
            m=p4.match(line)
            if m:
                group = m.groupdict()
                sw_data['oif_ic_count'] = int(group['oif_ic_count'])
                sw_data['oif_a_count'] = int(group['oif_a_count'])
                continue

            # SW Forwarding: 0/0/0/0, Other: 0/0/0
            m = p5.match(line)
            if m:
                changedict={}
                for key in m.groupdict().keys():
                  changedict[key] = int(m.groupdict()[key])
                sw_data.update(changedict)
                continue

            #HW Forwarding:   222/0/204/0, Other: 0/0/0
            m=p6.match(line)
            if m:
                changedict={}
                for key in m.groupdict().keys():
                  changedict[key] = int(m.groupdict()[key])
                sw_data.update(changedict)
                continue

            # LISP0.1 Flags: A NS
            #  Null0 Flags: A
            #  GigabitEthernet1/0/1 Flags: A NS
            m=p7.match(line)
            if m:
                group = m.groupdict()
                ingress_interface = group['ingress_if']
                ing_intf_dict = sw_data.setdefault('incoming_interfaces',{}).setdefault(ingress_interface,{})
                ing_intf_dict['ingress_flags'] = group['ingress_flags']
                if group['ingress_vxlan_cap']:
                    ing_intf_dict['ingress_vxlan_cap']=group['ingress_vxlan_cap']
                if group['ingress_vxlan_version']:
                    ing_intf_dict['ingress_vxlan_version']=group['ingress_vxlan_version']
                if group['ingress_vxlan_nxthop']:
                    ing_intf_dict['ingress_vxlan_nxthop']=group['ingress_vxlan_nxthop']
                if group['ingress_vxlan_vni']:
                    ing_intf_dict['ingress_vxlan_vni']=group['ingress_vxlan_vni']
                if group['ingress_mdt_ip']:
                    ing_intf_dict['ingress_mdt_ip']=group['ingress_mdt_ip']
                continue


            #Vlan2001 Flags: F NS
            #LISP0.1, (100.11.11.11, 235.1.3.167) Flags:
            # Vlan200, VXLAN v4 Encap (10100, 239.1.1.1) Flags: F
            m=p8.match(line)
            if m:
                group = m.groupdict()
                outgoing_interface=group['egress_if']
                if group['egress_rloc']:
                    egress_data['egress_rloc'] = group['egress_rloc']

                    #### adding this code for lisp and evpn interfaces with have unique
                    #### egress interface causing the last egress interface alone getting captured
                    #example below
                    # LISP0.1, 100.22.22.22 Flags: F
                    #Pkts: 0/0/1    Rate: 0 pps
                    #LISP0.1, 100.154.154.154 Flags: F
                    #Pkts: 0/0/1    Rate: 0 pps
                    #LISP0.1, 100.88.88.88 Flags: F
                    #Pkts: 0/0/1    Rate: 0 pps
                    #LISP0.1, 100.33.33.33 Flags: F

                    outgoing_interface='{},{}'.format(group['egress_if'], group['egress_rloc'])

                egress_data=sw_data.setdefault('outgoing_interfaces',{}).setdefault(outgoing_interface,{})
                egress_data_update = True
                egress_data['egress_flags'] = group['egress_flags']

                if group['egress_underlay_mcast']:
                    egress_data['egress_underlay_mcast'] = group['egress_underlay_mcast']

                if group['egress_vxlan_cap']:
                    egress_data['egress_vxlan_cap'] = group['egress_vxlan_cap']
                if group['egress_vxlan_version']:
                    egress_data['egress_vxlan_version'] = group['egress_vxlan_version']
                if group['egress_vxlan_vni']:
                    egress_data['egress_vxlan_vni'] = group['egress_vxlan_vni']
                if group['egress_vxlan_nxthop']:
                    egress_data['egress_vxlan_nxthop'] = group['egress_vxlan_nxthop']
                if group['egress_mdt_ip']:
                    egress_data['egress_mdt_ip']=group['egress_mdt_ip']
                continue
            #CEF: Adjacency with MAC: 01005E010101000A000120010800
            m=p9_1.match(line)
            if m and egress_data_update:
                group = m.groupdict()                 
                egress_data['egress_adj_mac'] = group['egress_adj_mac']
                continue
            #CEF: Special OCE (discard)
            m=p9_2.match(line)
            if m and egress_data_update:
                group = m.groupdict()
                egress_data['egress_adj_mac'] = group['egress_adj_mac']
                continue
            #Pkts: 0/0/2    Rate: 0 pps
            m=p10.match(line)
            if m and egress_data_update:
                changedict={}
                for key in m.groupdict().keys():
                  changedict[key] = int(m.groupdict()[key])
                egress_data.update(changedict)
                continue
        return mfib_dict


# ====================================================
#  schema for show ipv6 dhcp pool
# ====================================================
class ShowIpv6DhcpPoolSchema(MetaParser):
    """Schema for show ipv6 dhcp pool"""
    schema = {
            Any(): {
                Optional('address_allocation_prefix'): str,
                Optional('valid_lifetime'): int,
                Optional('preferred_lifetime'): int,
                Optional('in_use_address'): int,
                Optional('conflicts'): int,
                Optional('domain_name'): str,
                'active_clients': int
            },
    }

# ================================================================
# Parser for:
#   * 'show ipv6 dhcp pool'
#   * 'show ipv6 dhcp pool {poolname}'
# ================================================================
class ShowIpv6DhcpPool(ShowIpv6DhcpPoolSchema):
    """ Parser for:
                show ipv6 dhcp pool
                show ipv6 dhcp pool {poolname}
    """
    cli_command = ['show ipv6 dhcp pool {poolname}','show ipv6 dhcp pool']
    def cli(self, poolname='', output=None):
        """ cli for:
         ' show ipv6 dhcp pool '
        """

        if output is None:
            if poolname:
                output = self.device.execute(self.cli_command[0].format(poolname=poolname))
            else:
                 output= self.device.execute(self.cli_command[1])

        # Initialize dictionary
        pool_dict = {}

        #DHCPv6 pool: pool1
        p1 = re.compile(r'^DHCPv6 +pool: +(?P<pool_name>\S+)$')

        #Address allocation prefix: 2510:1::/64 valid 300 preferred 300 (1 in use, 0 conflicts)
        p2 = re.compile(r'^Address +allocation +prefix: +(?P<address_allocation_prefix>\S+) +valid +(?P<valid_lifetime>\d+) +preferred +(?P<preferred_lifetime>\d+) +\S(?P<in_use_address>\d+) +in +use, +(?P<conflicts>\d+) +conflicts\S$')

        #Domain name: cisco.com
        p3 = re.compile(r'^Domain +name: +(?P<domain_name>\S+)$')

        #Active clients: 1
        p4 = re.compile(r'Active +clients: +(?P<active_clients>\d+)$')

        for line in output.splitlines():
            line = line.strip()
            #DHCPv6 pool: pool1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                pool = group['pool_name']
                if pool not in pool_dict:
                    pool_dict[pool] = {}
                continue

            #Address allocation prefix: 2510:1::/64 valid 300 preferred 300 (1 in use, 0 conflicts)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                pool_dict[pool]['address_allocation_prefix'] = group['address_allocation_prefix']
                pool_dict[pool]['valid_lifetime'] = int(group['valid_lifetime'])
                pool_dict[pool]['preferred_lifetime'] = int(group['preferred_lifetime'])
                pool_dict[pool]['in_use_address'] = int(group['in_use_address'])
                pool_dict[pool]['conflicts'] = int(group['conflicts'])
                continue

            #Domain name: cisco.com
            m = p3.match(line)
            if m:
                group = m.groupdict()
                pool_dict[pool]['domain_name'] = group['domain_name']
                continue

            #Active Clients: 1
            m = p4.match(line)
            if m:
                group = m.groupdict()
                pool_dict[pool]['active_clients'] = int(group['active_clients'])
                continue

        return pool_dict


# ====================================================
#  schema for show ipv6 dhcp statistics
# ====================================================
class ShowIpv6DhcpStatisticsSchema(MetaParser):
    """Schema for sh ipv6 dhcp statistics"""
    schema = {
        'total_received': int,
        'total_sent': int,
        'total_discarded': int,
        'total_could_not_be_sent': int,
        Optional('type_received'): {
            Any(): int
        },
        Optional('type_sent'): {
            Any(): int
        },
        Optional('failed_reason'): {
            Any(): int
        }
    }

# ================================================================
# Parser for:
#   * 'show ipv6 dhcp statistics'
# ================================================================
class ShowIpv6DhcpStatistics(ShowIpv6DhcpStatisticsSchema):
    """ Parser for:
                sh ipv6 dhcp statistics
    """
    cli_command = ['show ipv6 dhcp statistics']
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # Messages received                2
        # Messages sent                    2
        # Messages discarded               0
        # Messages could not be sent       0        
        p1 = re.compile(r'^Messages +(?P<total_type>[a-zA-Z ]+)\s+(?P<total>\d+)$')

        # Messages                         Received
        # Messages                         Sent
        p2 = re.compile(r'^Messages\s+(?P<message_type>Received|Sent)$')

        # Send message failed due to:
        p3 = re.compile(r'^Send message +failed +due +to:$')

        # SOLICIT                          1
        # REQUEST                          1
        # ADVERTISE                        1
        # REPLY                            1
        # IPv6 protocol on outgoing interface not ready            6
        p4 = re.compile(r'^(?P<message_type>[a-zA-Z0-9 ]+)\s+(?P<count>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Messages received                2
            # Messages sent                    2
            # Messages discarded               0
            # Messages could not be sent       0  
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                total_type = groups['total_type'].strip().lower().replace(' ','_')
                key = f"total_{total_type}"
                ret_dict.update({key: int(groups['total'])})
                continue

            # Messages                         Received
            # Messages                         Sent
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                message_type = groups['message_type'].lower()
                key = f"type_{message_type}"
                current_dict = ret_dict.setdefault(key, {})
                continue

            # Send message failed due to:
            m = p3.match(line)
            if m:
                current_dict = ret_dict.setdefault('failed_reason', {})
                continue

            # SOLICIT                          1
            # REQUEST                          1
            # ADVERTISE                        1
            # REPLY                            1
            # IPv6 protocol on outgoing interface not ready            6
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                key = groups['message_type'].strip().lower().replace(' ', '_')
                current_dict.update({key: int(groups['count'])})
                continue

        return ret_dict

# ====================================================
#  schema for show ipv6 dhcp binding
# ====================================================
class ShowIpv6DhcpBindingSchema(MetaParser):
    """Schema for show ipv6 dhcp binding"""
    schema = {
        'client': {
            Any(): { # FE80::210:94FF:FE00:1
                'duid': str,
                'username': str,
                'vrf': str,
                Optional('interface'): str,
                Optional('ia_na'): {
                    Any(): { # 0x00000000
                        'ia_id': str, 
                        't1': int,
                        't2': int,
                        'address': {
                            Any(): { # 3001::B151:2E66:32A4:65E9
                                'preferred_lifetime': Or(int, str),
                                'valid_lifetime': Or(int, str),
                                Optional('expires'): {
                                    'month': str,
                                    'day': int,
                                    'year': int,
                                    'time': str,
                                    'remaining_seconds': int # (109686 seconds)
                                }
                            }
                        }
                    }
                },
                Optional('ia_pd'): {
                    Any(): { # 0x00100001
                        'ia_id': str,
                        't1': int,
                        't2': int,
                        'prefix': {
                            Any(): { # 2001:4::/48
                                'preferred_lifetime': Or(int, str),
                                'valid_lifetime': Or(int, str),
                                'expires': {
                                    'month': str,
                                    'day': int,
                                    'year': int,
                                    'time': str,
                                    'remaining_seconds': int # (109686 seconds)
                                }
                            }
                        }
                    }
                }
            }
        }
    }

# ================================================================
# Parser for:
#   * 'show ipv6 dhcp binding'
# ================================================================
class ShowIpv6DhcpBinding(ShowIpv6DhcpBindingSchema):
    """ Parser for:
                show ipv6 dhcp binding
    """
    cli_command = ['show ipv6 dhcp binding']
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        res_dict = {}

        # Client: FE80::210:94FF:FE00:1 
        p1 = re.compile(r'^(?P<client>Client):\s+(?P<client_address>\S+)$')

        # DUID: 00010001534573D7001094000001
        p2 = re.compile(r'^DUID:\s+(?P<duid>\S+)$')

        # Username : unassigned
        p3 = re.compile(r'^Username\s+:\s+(?P<username>\S+)$')

        # Interface : Ethernet0/0
        p4 = re.compile(r'^Interface\s+:\s+(?P<interface>\S+)$')

        # VRF : default
        p5 = re.compile(r'^VRF\s+:\s+(?P<vrf>\S+)$')

        # IA NA: IA ID 0x00000000, T1 43200, T2 69120
        # IA PD: IA ID 0x00100001, T1 302400, T2 483840
        p6 = re.compile(r'^(?P<ia>[A-Z ]+):\s+IA ID\s+(?P<ia_id>\S+),\s+T1\s+(?P<t1>\d+),\s+T2\s+(?P<t2>\d+)$')

        # Address: 3001::F8AB:B06E:8974:9359
        p71 = re.compile(r'^Address:\s+(?P<ipv6_address>\S+)$')

        # Prefix: 2001:4::/48
        p72 = re.compile(r'^Prefix:\s+(?P<ipv6_prefix>\S+)$')

        # preferred lifetime 86400, valid lifetime 172800
        # preferred lifetime INFINITY, , valid lifetime INFINITY,
        p8 = re.compile(r'^preferred lifetime\s+(?P<preferred_lifetime>\w+)(, ,|,)\s+valid lifetime\s+(?P<valid_lifetime>\w+)(,|)$')
        # expires at Feb 17 2022 08:58 AM (172782 seconds)
        p9 = re.compile(r'^(?P<expires>\w+) +at\s+(?P<month>\S+)\s+(?P<day>\d+)\s+(?P<year>\d+)\s+(?P<time>[0-9A-Z :]+)\s+\((?P<remaining_seconds>\d+) +seconds\)$')

        for line in output.splitlines():
            line = line.strip()

            # Client: FE80::210:94FF:FE00:1 
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                client = groups['client'].lower()
                client_address = groups['client_address']
                client_dict = res_dict.setdefault(client, {}).setdefault(client_address, {})
                continue

            # DUID: 00010001534573D7001094000001
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                client_dict.update({'duid' : groups['duid']})
                continue

            # Username : unassigned
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                client_dict.update({'username' : groups['username']})
                continue

            # Interface : Ethernet0/0
            m = p4.match(line)
            if m:
                client_dict.update({'interface':  m.groupdict()['interface']})
                continue

            # VRF : default
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                client_dict.update({'vrf' : groups['vrf']})
                continue

            # IA NA: IA ID 0x00000000, T1 43200, T2 69120
            # IA PD: IA ID 0x00100001, T1 302400, T2 483840
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                ia = groups['ia'].lower().strip().replace(' ','_')
                ia_id = groups['ia_id']
                ia_dict = res_dict.setdefault(client, {}).setdefault(client_address, {}).setdefault(ia, {}).setdefault(ia_id, {})
                ia_dict.update({
                    'ia_id' : ia_id,
                    't1' : int(groups['t1']),
                    't2' : int(groups['t2'])
                })
                continue

            # Address: 3001::F8AB:B06E:8974:9359
            m = p71.match(line)
            if m:
                groups = m.groupdict()
                address_key = 'address'
                ipv6_address = groups['ipv6_address']
                address_dict = res_dict.setdefault(client, {}).setdefault(client_address, {}).setdefault(ia, {}).setdefault(ia_id, {}).setdefault(address_key, {}).setdefault(ipv6_address,{})
                continue

            # Prefix: 2001:4::/48
            m = p72.match(line)
            if m:
                groups = m.groupdict()
                address_key = 'prefix'
                ipv6_address = groups['ipv6_prefix']
                address_dict = res_dict.setdefault(client, {}).setdefault(client_address, {}).setdefault(ia, {}).setdefault(ia_id, {}).setdefault(address_key, {}).setdefault(ipv6_address,{})
                continue

            # preferred lifetime 86400, valid lifetime 172800
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                if (groups['preferred_lifetime']).isdigit():
                    groups['preferred_lifetime'] = int(groups['preferred_lifetime'])
                if (groups['valid_lifetime']).isdigit():
                    groups['valid_lifetime'] = int(groups['valid_lifetime'])
                address_dict.update({
                    'preferred_lifetime': groups['preferred_lifetime'],
                    'valid_lifetime': groups['valid_lifetime']})
                continue

            # expires at Feb 17 2022 08:58 AM (172782 seconds)
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                expires = groups['expires']
                expires_dict = res_dict.setdefault(client, {}).setdefault(client_address, {}).setdefault(ia, {}).setdefault(ia_id, {}).setdefault(address_key, {}).setdefault(ipv6_address, {}).setdefault(expires, {})
                expires_dict.update({
                    'month' : groups['month'],
                    'day' : int(groups['day']),
                    'year' : int(groups['year']),
                    'time' : groups['time'],
                    'remaining_seconds' : int(groups['remaining_seconds'])
                })
                continue
        return res_dict

# =================================================
#  Schema for 'show ipv6 nhrp summary'
# =================================================
class ShowIpv6NhrpSummarySchema(MetaParser):
    """schema for show ipv6 nhrp summary"""
    schema = {
        'ipv6_nhrp': {
            "total": {
                'nhrp_entries': int,
                'size': int,
                'total_static_entries': int,
                'total_dynamic_entries': int,
                'total_incomplete_entries': int
            },
            "remote": {
                'remote_entries': int,
                'remote_static_entries': int,
                'remote_dynamic_entries': int,
                'remote_incomplete_entries': int,
                'nhop': int,
                'bfd': int,
                'default': int,
                'temporary': int,
                'route': {
                    'total': int,
                    'rib': int,
                    'h_rib': int,
                    'nho_rib': int,
                    'bgp': int
                },
                'lfib': int
            },
            "local": {
                'local': int,
                'local_static': int,
                'local_dynamic': int,
                'local_incomplete': int,
                'lfib': int
            }
        }
    }

# ===================================================
#  Parser for 'show ipv6 nhrp summary'
# ===================================================
class ShowIpv6NhrpSummary(ShowIpv6NhrpSummarySchema):
    """Parser for show ipv6 nhrp summary"""
    cli_command = 'show ipv6 nhrp summary'
    
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        #IPv6 NHRP cache 4 entries, 3072 bytes
        #IPv6 NHRP cache 1 entry, 784 bytes
        p1 = re.compile(r'^IPv6 +NHRP +cache +(?P<nhrp_entries>\d+) +entr(?:y|ies), +(?P<size>\d+)')
        #2 static 2 dynamic 0 incomplete
        p2 = re.compile(r'^(?P<total_static_entries>[\d]+) +static +(?P<total_dynamic_entries>[\d]+) +dynamic +(?P<total_incomplete_entries>[\d]+) +incomplete')
        #4 Remote
        p3 = re.compile(r'(?P<remote_entries>[\d]+) Remote')
        #2 static 2 dynamic 0 incomplete
        p4 = re.compile(r'^(?P<remote_static_entries>[\d]+) +static +(?P<remote_dynamic_entries>[\d]+) +dynamic +(?P<remote_incomplete_entries>[\d]+) +incomplete')
        #1 nhop 3 bfd
        p5 = re.compile(r'^(?P<nhop>[\d]+) +nhop +(?P<bfd>[\d]+) +bfd')
        #0 default 0 temporary
        p6 = re.compile(r'^(?P<default>[\d]+) +default +(?P<temporary>[\d]+) +temporary')
        #2 route
        p7 = re.compile(r'^(?P<total>[\d]+) +route')
        #2 rib (2 H 0 nho)
        p8 = re.compile(r'^(?P<rib>[\d]+) +rib +.(?P<h_rib>[\d]+) +H +(?P<nho_rib>[\d]+) +nho.')
        #0 bgp
        p9 = re.compile(r'^(?P<bgp>[\d]+) +bgp')
        #0 lfib
        p10 = re.compile(r'(?P<lfib>[\d]+) +lfib')
        #0 Local
        p11 = re.compile(r'^(?P<local>[\d]+) +Local')
        #0 static 0 dynamic 0 incomplete
        p12 = re.compile(r'^(?P<local_static>[\d]+) +static +(?P<local_dynamic>[\d]+) +dynamic +(?P<local_incomplete>[\d]+) +incomplete')
        #0 lfib
        p13 = re.compile(r'(?P<lfib>[\d]+) +lfib')

        # initial return dictionary
        nhrp = False
        remote = False
        local = False
        ret_dict = {}
  
        for line in out.splitlines():
            line=line.strip()
            #IPv6 NHRP cache 4 entries, 3072 bytes
            m = p1.match(line) 
            if m:
                group = m.groupdict()
                ipv6_nhrp = ret_dict.setdefault('ipv6_nhrp', {})
                total = ipv6_nhrp.setdefault('total',{})
                total.update({'nhrp_entries': int(group['nhrp_entries'])})
                total.update({'size': int(group['size'])})
                nhrp = True
                continue

            #2 static 2 dynamic 0 incomplete
            if nhrp:
                m = p2.match(line)
                if m:
                    group = m.groupdict()                
                    total.update({'total_static_entries': int(group['total_static_entries'])})
                    total.update({'total_dynamic_entries': int(group['total_dynamic_entries'])})
                    total.update({'total_incomplete_entries': int(group['total_incomplete_entries'])})
                    continue
                nhrp = False
                remote = True

            if remote:
                #4 Remote
                m = p3.match(line)
                if m:
                    group = m.groupdict()
                    remote = ipv6_nhrp.setdefault('remote',{})
                    remote.update({'remote_entries': int(group['remote_entries'])})
                    continue                            

                #2 static 2 dynamic 0 incomplete
                m = p4.match(line)
                if m:                
                    group = m.groupdict()
                    remote.update({'remote_static_entries': int(group['remote_static_entries'])})
                    remote.update({'remote_dynamic_entries': int(group['remote_dynamic_entries'])})
                    remote.update({'remote_incomplete_entries': int(group['remote_incomplete_entries'])})
                    continue

                #1 nhop 3 bfd
                m = p5.match(line)
                if m:
                    group = m.groupdict()
                    remote.update({'nhop': int(group['nhop'])})
                    remote.update({'bfd': int(group['bfd'])})
                    continue            

                #0 default 0 temporary
                m = p6.match(line)
                if m:
                    group = m.groupdict()
                    remote.update({'default': int(group['default'])})
                    remote.update({'temporary': int(group['temporary'])})
                    continue
                
                #2 route
                m = p7.match(line)
                if m:
                    group = m.groupdict()
                    route = remote.setdefault('route',{})
                    route.update({'total': int(group['total'])})
                    continue
                
                #2 rib (2 H 0 nho)
                m = p8.match(line)
                if m:
                    group = m.groupdict()
                    route.update({'rib': int(group['rib'])})
                    route.update({'h_rib': int(group['h_rib'])})
                    route.update({'nho_rib': int(group['nho_rib'])})
                    continue

                #0 bgp
                m = p9.match(line)
                if m:
                    group = m.groupdict()
                    route.update({'bgp': int(group['bgp'])})
                    continue

                #0 lfib
                m = p10.match(line)
                if m:
                    group = m.groupdict()
                    remote.update({'lfib': int(group['lfib'])})
                    continue
                remote = False
                local = True

            #0 Local
            if local:
                m = p11.match(line)
                if m:
                    group = m.groupdict()
                    local = ipv6_nhrp.setdefault('local',{})
                    local.update({'local': int(group['local'])})                
                    continue

                #0 static 0 dynamic 0 incomplete
                m = p12.match(line)
                if m:                
                    group = m.groupdict()
                    local.update({'local_static': int(group['local_static'])})
                    local.update({'local_dynamic': int(group['local_dynamic'])})
                    local.update({'local_incomplete': int(group['local_incomplete'])})
                    continue

                #0 lfib
                m = p13.match(line)
                if m:
                    group = m.groupdict()
                    local.update({'lfib': int(group['lfib'])})
                    continue

        return ret_dict

# ====================================================
#  schema for show ipv6 cef summary
# ====================================================
class ShowIpv6CefSummarySchema(MetaParser):
    """Schema for show ipv6 cef summary
                  show ipv6 cef vrf <vrf> summary

    """
    schema = {
        'vrf':{
            Any():{
                'prefixes': {
                    'fwd': int,
                    'non_fwd': int,
                    'total_prefix': int
                },
                'table_id': str,
                'epoch': int
            }
        }
    }

# ====================================================
#  parser for show ipv6 cef summary
# ====================================================
class ShowIpv6CefSummary(ShowIpv6CefSummarySchema):
    cli_command = ['show ipv6 cef summary', 'show ipv6 cef vrf {vrf} summary']

    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # Vrf red
        p1 = re.compile(r'^VRF +(?P<vrf>\S+)$')

        # 6 prefixes (6/0 fwd/non-fwd)
        p2 = re.compile(r'^(?P<total_prefix>\d+) +prefixes +\((?P<fwd>\d+)\/(?P<non_fwd>\d+)+ fwd\/non-fwd\)$')

        # Table id 0x1E000001
        p3 = re.compile(r'^Table id (?P<table_id>\S+)$')

        #Database epoch:        0 (6 entries at this epoch)
        p4 = re.compile(r'^Database epoch: +(?P<epoch>\d+) +\(\d+ entries at this epoch\)$')


        ret_dict = {}
        m = ''
        for line in out.splitlines():
            line = line.strip()
            
            # Vrf red
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                vrf_dict = ret_dict.setdefault('vrf',{}).setdefault(vrf, {})
                continue

            # 6 prefixes (6/0 fwd/non-fwd)
            m = p2.match(line)
            if m:
                prefix_dict = vrf_dict.setdefault('prefixes',{})
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items() if v is not None}
                prefix_dict.update(group)
                continue
            
            # Table id 0x1E000001
            m = p3.match(line)
            if m:
                vrf_dict.update(m.groupdict())
                continue

            # Database epoch:        0 (6 entries at this epoch)
            m = p4.match(line)
            if m:
              vrf_dict.update({'epoch': int(m.groupdict()['epoch'])}) 
              continue

        return ret_dict

# ====================================================
#  schema for show ipv6 static recursive
# ====================================================
class ShowIpv6StaticRecursiveSchema(MetaParser):
    """Schema for show ipv6 static recursive
    """
    schema = {
        Any():{
            'via': list,
            'distance': int,
            'installed': bool
        }
    }

# ====================================================
#  parser for show ipv6 static recursive
# ====================================================
class ShowIpv6StaticRecursive(ShowIpv6StaticRecursiveSchema):
    cli_command = ['show ipv6 static recursive']

    def cli(self, output=None):
        if output is None:
            cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # for routes installed in RIB
        # *   2005::/64 via 2001::2, distance 1
        p1 = re.compile(r'^(?P<installed>\*?) *(?P<prefix>[a-f0-9:]+:\/\d+) via (?P<nhop>[a-f0-9:]+)'
                        r', distance (?P<distance>\d+)$')
        
        
        ret_dict = {}
        m = ''
        for line in out.splitlines():
            line = line.strip()
            
            # *   2005::/64 via 2001::2, distance 1
            m = p1.match(line)
            if m:
                prefix = m.groupdict()['prefix']
                pref_dict = ret_dict.setdefault(prefix,{})
                via_list = pref_dict.setdefault('via', [])
                via_list.append(m.groupdict()['nhop'])
                pref_dict.setdefault('distance', int(m.groupdict()['distance']))
                if m.groupdict()['installed']:
                    pref_dict.setdefault('installed', True)
                else:
                    pref_dict.setdefault('installed', False)
                continue

        return ret_dict

# ====================================================
#  schema for show ipv6 mld snooping
# ====================================================
class showIpv6MldSnoopingSchema(MetaParser):
    """Schema for show ipv6 mld snooping
    """
    schema = {
        'global_mld_snooping_configuration': {
            'mld_snooping': str,
            'global_pim_snooping': str,
            'mldv2_snooping': str,
            'listener_message_suppression': str,
            'tcn_solicit_query': str,
            'tcn_flood_query_count': str,
            'robustness_variable': str,
            'last_listener_query_count': str,
            'last_listener_query_interval': str,
        },
        'vlans':{  
            Any(): {
                'mld_snooping': str,
                'robustness_variable': str,
                'last_listener_query_count': str,
                'last_listener_query_interval': str,
                'pim_snooping': str,
                'mld_immediate_leave': str,
                Optional('explicit_host_tracking'): str
            }
        },            
    }

# ====================================================
#   Parser for show ipv6 mld snooping
# ====================================================
class showIpv6MldSnooping(showIpv6MldSnoopingSchema):
    """parser for show ipv6 mld snooping
    """
    cli_command = 'show ipv6 mld snooping'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command) 

        # Global MLD Snooping configuration
        p1 = re.compile(r'^Global MLD Snooping configuration:$')
        # Vlan 1
        p2 = re.compile(r'^Vlan +(?P<vlan>\d+):$')
        # MLD snooping                        : Disabled
        p3 = re.compile(r'^(?P<key>.*) +: +(?P<value>.*)$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()
            
            # Global MLD Snooping configuration:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                dest_dict = ret_dict.setdefault('global_mld_snooping_configuration',{})
                continue
            # Vlan 1:
            m = p2.match(line)
            if m:
                group = m.groupdict()
                dest_dict = ret_dict.setdefault('vlans',{}).setdefault('vlan_' + group['vlan'],{})
                continue
            # Pim Snooping                        : Disabled
            m = p3.match(line)
            if m:
                group = m.groupdict()
                key = group['key'].lower().strip().replace(' ', '_')
                dest_dict[key] = group['value']
                continue

        return ret_dict
    

# ======================================================
# Schema for 'show ipv6 dhcp relay binding '
# ======================================================

class ShowIpv6DhcpRelayBindingSchema(MetaParser):
    """Schema for show ipv6 dhcp relay binding"""

    schema = {
        'dhcpv6_relay_binding': {
            Any(): {
                'prefix': str,
                'interface': str,            
                'duid': str,
                'iaid': int,
                'lifetime': int,
                'expiration': str,
            },
        },
        'num_relay_binding': int,
        'num_iapd_binding': int,
        'num_iana_binding': int,
        'num_relay_binding_bulk_lease': int,
    }


# ======================================================
# Parser for 'show ipv6 dhcp relay binding '
# ======================================================
class ShowIpv6DhcpRelayBinding(ShowIpv6DhcpRelayBindingSchema):
    """Parser for show ipv6 dhcp relay binding"""

    cli_command = 'show ipv6 dhcp relay binding'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Prefix: 2001:DB8:1201::/48 (TwentyFiveGigE1/0/1)
        p1 = re.compile(r"^Prefix:\s+(?P<prefix>\S+)\s+\((?P<interface>\S+)\)$")
        
        #   DUID: 00030001ECCE131F6700
        p1_1 = re.compile(r"^\s+DUID:\s+(?P<duid>\S+)$")
        
        #   IAID: 8388609
        p1_2 = re.compile(r"^\s+IAID:\s+(?P<iaid>\d+)$")
        
        #   lifetime: 1800
        p1_3 = re.compile(r"^\s+lifetime:\s+(?P<lifetime>\d+)$")
        
        #   expiration: 19:51:56 UTC Mar 21 2023
        p1_4 = re.compile(r"^\s+expiration:\s+(?P<expiration>\S+\s+\S+\s+\S+\s+\S+\s+\S+)$")
        
        #   Total number of Relay bindings = 1
        p2 = re.compile(r"^\s+Total\s+number\s+of\s+Relay\s+bindings\s+=\s+(?P<num_relay_binding>\d+)$")
        
        #   Total number of IAPD bindings = 1
        p3 = re.compile(r"^\s+Total\s+number\s+of\s+IAPD\s+bindings\s+=\s+(?P<num_iapd_binding>\d+)$")
        
        #   Total number of IANA bindings = 0
        p4 = re.compile(r"^\s+Total\s+number\s+of\s+IANA\s+bindings\s+=\s+(?P<num_iana_binding>\d+)$")
        
        #   Total number of Relay bindings added by Bulk lease = 0
        p5 = re.compile(r"^\s+Total\s+number\s+of\s+Relay\s+bindings\s+added\s+by\s+Bulk\s+lease\s+=\s+(?P<num_relay_binding_bulk_lease>\d+)$")

        ret_dict = {}

        for line in output.splitlines():

            # Prefix: 2001:DB8:1201::/48 (TwentyFiveGigE1/0/1)
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                interface_var = Common.convert_intf_name(dict_val['interface'])
                interface_dict = ret_dict.setdefault('dhcpv6_relay_binding', {})\
                    .setdefault(interface_var, {})
                interface_dict['prefix'] = dict_val['prefix']
                interface_dict['interface'] = interface_var
                continue

            #   DUID: 00030001ECCE131F6700
            m = p1_1.match(line)
            if m:
                interface_dict['duid'] = m.groupdict()['duid']
                continue

            #   IAID: 8388609
            m = p1_2.match(line)
            if m:
                interface_dict['iaid'] = int(m.groupdict()['iaid'])
                continue

            #   lifetime: 1800
            m = p1_3.match(line)
            if m:
                interface_dict['lifetime'] = int(m.groupdict()['lifetime'])
                continue

            #   expiration: 19:51:56 UTC Mar 21 2023
            m = p1_4.match(line)
            if m:
                interface_dict['expiration'] = m.groupdict()['expiration']
                continue

            #   Total number of Relay bindings = 1
            m = p2.match(line)
            if m:
                ret_dict['num_relay_binding'] = int(m.groupdict()['num_relay_binding'])
                continue

            #   Total number of IAPD bindings = 1
            m = p3.match(line)
            if m:
                ret_dict['num_iapd_binding'] = int(m.groupdict()['num_iapd_binding'])
                continue

            #   Total number of IANA bindings = 0
            m = p4.match(line)
            if m:
                ret_dict['num_iana_binding'] = int(m.groupdict()['num_iana_binding'])
                continue

            #   Total number of Relay bindings added by Bulk lease = 0
            m = p5.match(line)
            if m:
                ret_dict['num_relay_binding_bulk_lease'] = int(m.groupdict()['num_relay_binding_bulk_lease'])
                continue

        return ret_dict

# ======================================================
# Schema for 'show ipv6 cef exact-route {source} {destination}'
# ======================================================

class ShowIpv6cefExactRouteSchema(MetaParser):
    """ Schema for the commands:
            * show ipv6 cef exact-route {source} {destination}
    """

    schema = {
        "ip_adj": str,
        "ip_addr": str,
        "source": str,
        "destination": str
    }

class ShowIpv6cefExactRoute(ShowIpv6cefExactRouteSchema):
    """
        * show ipv6 cef exact-route
    """

    cli_command = 'show ipv6 cef exact-route {source} {destination}'

    def cli(self, source, destination, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(source=source, destination=destination))

        # 11:1:0:1::1 -> 11:0:0:2::2 => IP adj out of Port-channel1, addr 11:0:0:2::2
        p1 = re.compile(r'^(?P<source>[\d\:]+) +-> +(?P<destination>[\d\:]+) +=> IP adj out of +(?P<ip_adj>[\w\-\.\/]+), +addr +(?P<ip_addr>[\d\:]+)$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()
            # 11:1:0:1::1 -> 11:0:0:2::2 => IP adj out of Port-channel1, addr 11:0:0:2::2
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['source'] = group['source']
                ret_dict['destination'] = group['destination']
                ret_dict['ip_adj'] = group['ip_adj']
                ret_dict['ip_addr'] = group['ip_addr']
                continue

        return ret_dict

#===============================================================================
# Schema for 'show ipv6 general-prefix'
#===============================================================================

class ShowIpv6GeneralPrefixSchema(MetaParser):
    """Schema for show ipv6 general-prefix"""

    schema = {
        'ipv6_prefix': {
            Any(): {
                'prefix': str,
                'acquired_via': str,
                'valid_lifetime': int,
                'preferred_lifetime': int,
                Optional('interfaces'): list,
            }
        }
    }

#===============================================================================
# Parser for 'show ipv6 general-prefix'
#===============================================================================
class ShowIpv6GeneralPrefix(ShowIpv6GeneralPrefixSchema):
    """Parser for show ipv6 general-prefix"""

    cli_command = 'show ipv6 general-prefix'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # IPv6 Prefix pd_prefix, acquired via DHCP PD
        p1 = re.compile(r'^IPv6 Prefix (?P<prefix_name>\S+), acquired via (?P<acquired_via>.+)$')

        # 2001:DB8:1200::/48 Valid lifetime 1735, preferred lifetime 535
        p2 = re.compile(r'^(?P<prefix>\S+) Valid lifetime (?P<valid_lifetime>\d+), preferred lifetime (?P<preferred_lifetime>\d+)$')

        # GigabitEthernet10/0/47 (Address command)
        p3 = re.compile(r'^(?P<interface>\S+) \(Address command\)$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # IPv6 Prefix pd_prefix, acquired via DHCP PD
            m = p1.match(line)
            if m:
                group = m.groupdict()
                prefix_name = group['prefix_name']
                prefix_dict = ret_dict.setdefault('ipv6_prefix', {}).setdefault(prefix_name, {})
                prefix_dict['acquired_via'] = group['acquired_via']
                continue

            # 2001:DB8:1200::/48 Valid lifetime 1735, preferred lifetime 535
            m = p2.match(line)
            if m:
                group = m.groupdict()
                prefix_dict['prefix'] = group['prefix']
                prefix_dict['valid_lifetime'] = int(group['valid_lifetime'])
                prefix_dict['preferred_lifetime'] = int(group['preferred_lifetime'])
                continue

            # GigabitEthernet10/0/47 (Address command)
            m = p3.match(line)
            if m:
                group = m.groupdict()
                interfaces = prefix_dict.setdefault('interfaces', [])
                interfaces.append(group['interface'])
                continue

        return ret_dict
    

class ShowIpv6PimNeighborIntfSchema(MetaParser):
    """Schema for show ipv6 pim neighbor Te0/0/4"""
    schema = {
        'interface': str,
        'neighbors': {
            Any(): {
                'uptime': str,
                'expires': str,
                'mode': str,
                'dr_priority': int,
                'bsr_priority': int,
                'hello_interval': str,
                'neighbor_interface': str,
                'neighbor_state': str,
            }
        }
    }

class ShowIpv6PimNeighborIntf(ShowIpv6PimNeighborIntfSchema):
    """Parser for show ipv6 pim neighbor Te0/0/4"""

    cli_command = 'show ipv6 pim neighbor {interface}'

    def cli(self, interface=None, output=None):
        if output is None:
            cmd = self.cli_command.format(interface=interface)
            output = self.device.execute(cmd)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Regular expressions for parsing the output
        # Example: "PIM Neighbor Table for Interface: GigabitEthernet0/0/0"
        p1 = re.compile(r'^PIM +Neighbor +Table +for +Interface: +(?P<interface>\S+)$')

        # Example: "Neighbor Address: 192.168.1.1"
        p2 = re.compile(r'^Neighbor +Address: +(?P<neighbor_address>\S+)$')

        # Example: "Uptime: 00:15:23"
        p3 = re.compile(r'^Uptime: +(?P<uptime>\S+)$')

        # Example: "Expires: 00:01:47"
        p4 = re.compile(r'^Expires: +(?P<expires>\S+)$')

        # Example: "Mode: Dense"
        p5 = re.compile(r'^Mode: +(?P<mode>\S+)$')

        # Example: "DR Priority: 1"
        p6 = re.compile(r'^DR +Priority: +(?P<dr_priority>\d+)$')

        # Example: "BSR Priority: 5"
        p7 = re.compile(r'^BSR +Priority: +(?P<bsr_priority>\d+)$')

        # Example: "Hello Interval: 30 seconds"
        p8 = re.compile(r'^Hello +Interval: +(?P<hello_interval>[\d\s\w]+)$')

        # Example: "Neighbor Interface: GigabitEthernet0/0/0"
        p9 = re.compile(r'^Neighbor +Interface: +(?P<neighbor_interface>\S+)$')

        # Example: "Neighbor State: Up"
        p10 = re.compile(r'^Neighbor +State: +(?P<neighbor_state>\S+)$')


        for line in output.splitlines():
            line = line.strip()

            # PIM Neighbor Table for Interface: GigabitEthernet0/0/0
            m = p1.match(line)
            if m:
                interface = m.group('interface')
                parsed_dict['interface'] = interface
                continue

            # Neighbor Address: 192.168.1.1
            m = p2.match(line)
            if m:
                neighbor_address = m.group('neighbor_address')
                neighbor_dict = parsed_dict.setdefault('neighbors', {}).setdefault(neighbor_address, {})
                continue

            # Uptime: 00:15:23
            m = p3.match(line)
            if m:
                neighbor_dict['uptime'] = m.group('uptime')
                continue

            # Expires: 00:01:47
            m = p4.match(line)
            if m:
                neighbor_dict['expires'] = m.group('expires')
                continue

            # Mode: Dense
            m = p5.match(line)
            if m:
                neighbor_dict['mode'] = m.group('mode')
                continue

            # DR Priority: 1
            m = p6.match(line)
            if m:
                neighbor_dict['dr_priority'] = int(m.group('dr_priority'))
                continue

            # BSR Priority: 5
            m = p7.match(line)
            if m:
                neighbor_dict['bsr_priority'] = int(m.group('bsr_priority'))
                continue

            # Hello Interval: 30 seconds
            m = p8.match(line)
            if m:
                neighbor_dict['hello_interval'] = m.group('hello_interval')
                continue

            # Neighbor Interface: GigabitEthernet0/0/1
            m = p9.match(line)
            if m:
                neighbor_dict['neighbor_interface'] = m.group('neighbor_interface')
                continue

            # Neighbor State: Up
            m = p10.match(line)
            if m:
                neighbor_dict['neighbor_state'] = m.group('neighbor_state')
                continue

        return parsed_dict



# ====================================================
#  schema for show ipv6 mfib count
# ====================================================
class ShowIpv6MfibCountSchema(MetaParser):
    """Schema for show ipv6 mfib count"""
    
    schema = {
        'ip_multicast_statistics': {
            'total_routes': int,
            'total_groups': int,
            'average_sources_per_group': float,
            'forwarding_counts_description': str,
            'other_counts_description': str,
            'groups': {
                Any(): {
                    Optional('rp_tree'): {
                        'forwarding': {
                            'pkt_count': int,
                            'pkts_per_second': int,
                            'avg_pkt_size': int,
                            'kilobits_per_second': int,
                        },
                        'other': {
                            'total': int,
                            'rpf_failed': int,
                            'other_drops': int,
                        }
                    },
                    Optional('sources'): {
                        Any(): {
                            'forwarding': {
                                'pkt_count': int,
                                'pkts_per_second': int,
                                'avg_pkt_size': int,
                                'kilobits_per_second': int,
                            },
                            'other': {
                                'total': int,
                                'rpf_failed': int,
                                'other_drops': int,
                            }
                        }
                    },
                    Optional('total_shown'): {
                        'source_count': int,
                        'pkt_count': int,
                    }
                }
            }
        }
    }

# ====================================================
#  parser for show ipv6 mfib count
# ====================================================
class ShowIpv6MfibCount(ShowIpv6MfibCountSchema):
    """Parser for show ipv6 mfib count"""
    
    cli_command = 'show ipv6 mfib count'
    
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        
        # Initialize return dictionary
        ret_dict = {}
        
        # IP Multicast Statistics
        p1 = re.compile(r'^IP Multicast Statistics$')
        
        # 54 routes, 7 groups, 0.14 average sources per group
        p2 = re.compile(r'^(?P<routes>\d+) routes, (?P<groups>\d+) groups, (?P<avg_sources>[\d\.]+) average sources per group$')
        
        # Forwarding Counts: Pkt Count/Pkts per second/Avg Pkt Size/Kilobits per second
        p3 = re.compile(r'^Forwarding Counts: (?P<forward_desc>.+)$')
        
        # Other counts: Total/RPF failed/Other drops(OIF-null, rate-limit etc)
        p4 = re.compile(r'^Other counts: (?P<other_desc>.+)$')
        
        # Group: FF00::/8
        p5 = re.compile(r'^Group: (?P<group>[\w\:\/]+)$')
        
        # RP-tree:    Forwarding: 0/0/0/0, Other: 0/0/0
        p6 = re.compile(r'^RP-tree:\s+Forwarding: (?P<pkt_count>\d+)/(?P<pkts_per_sec>\d+)/(?P<avg_pkt_size>\d+)/(?P<kbps>\d+), Other: (?P<total>\d+)/(?P<rpf_failed>\d+)/(?P<other_drops>\d+)$')
        
        # Source: 10::1:1:200,   Forwarding: 367/10/100/7, Other: 0/0/0
        p7 = re.compile(r'^Source: (?P<source>[\w\:\.]+),\s+Forwarding: (?P<pkt_count>\d+)/(?P<pkts_per_sec>\d+)/(?P<avg_pkt_size>\d+)/(?P<kbps>\d+), Other: (?P<total>\d+)/(?P<rpf_failed>\d+)/(?P<other_drops>\d+)$')
        
        # Tot. shown: Source count: 1, pkt count: 369
        p8 = re.compile(r'^Tot\. shown: Source count: (?P<source_count>\d+), pkt count: (?P<pkt_count>\d+)$')
        
        current_group = None
        
        for line in output.splitlines():
            line = line.strip()
            
            # IP Multicast Statistics
            m = p1.match(line)
            if m:
                stats_dict = ret_dict.setdefault('ip_multicast_statistics', {})
                continue
            
            # 54 routes, 7 groups, 0.14 average sources per group
            m = p2.match(line)
            if m:
                group = m.groupdict()
                stats_dict['total_routes'] = int(group['routes'])
                stats_dict['total_groups'] = int(group['groups'])
                stats_dict['average_sources_per_group'] = float(group['avg_sources'])
                continue
            
            # Forwarding Counts: Pkt Count/Pkts per second/Avg Pkt Size/Kilobits per second
            m = p3.match(line)
            if m:
                group = m.groupdict()
                stats_dict['forwarding_counts_description'] = group['forward_desc']
                continue
            
            # Other counts: Total/RPF failed/Other drops(OIF-null, rate-limit etc)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                stats_dict['other_counts_description'] = group['other_desc']
                continue
            
            # Group: FF00::/8
            m = p5.match(line)
            if m:
                group = m.groupdict()
                current_group = group['group']
                groups_dict = stats_dict.setdefault('groups', {})
                groups_dict.setdefault(current_group, {})
                continue
            
            # RP-tree:    Forwarding: 0/0/0/0, Other: 0/0/0
            m = p6.match(line)
            if m and current_group:
                group = m.groupdict()
                group_dict = stats_dict['groups'][current_group]
                rp_tree_dict = group_dict.setdefault('rp_tree', {})
                
                forwarding_dict = rp_tree_dict.setdefault('forwarding', {})
                forwarding_dict['pkt_count'] = int(group['pkt_count'])
                forwarding_dict['pkts_per_second'] = int(group['pkts_per_sec'])
                forwarding_dict['avg_pkt_size'] = int(group['avg_pkt_size'])
                forwarding_dict['kilobits_per_second'] = int(group['kbps'])
                
                other_dict = rp_tree_dict.setdefault('other', {})
                other_dict['total'] = int(group['total'])
                other_dict['rpf_failed'] = int(group['rpf_failed'])
                other_dict['other_drops'] = int(group['other_drops'])
                continue
            
            # Source: 10::1:1:200,   Forwarding: 367/10/100/7, Other: 0/0/0
            m = p7.match(line)
            if m and current_group:
                group = m.groupdict()
                group_dict = stats_dict['groups'][current_group]
                sources_dict = group_dict.setdefault('sources', {})
                source_name = group['source']
                source_dict = sources_dict.setdefault(source_name, {})
                
                forwarding_dict = source_dict.setdefault('forwarding', {})
                forwarding_dict['pkt_count'] = int(group['pkt_count'])
                forwarding_dict['pkts_per_second'] = int(group['pkts_per_sec'])
                forwarding_dict['avg_pkt_size'] = int(group['avg_pkt_size'])
                forwarding_dict['kilobits_per_second'] = int(group['kbps'])
                
                other_dict = source_dict.setdefault('other', {})
                other_dict['total'] = int(group['total'])
                other_dict['rpf_failed'] = int(group['rpf_failed'])
                other_dict['other_drops'] = int(group['other_drops'])
                continue
            
            # Tot. shown: Source count: 1, pkt count: 369
            m = p8.match(line)
            if m and current_group:
                group = m.groupdict()
                group_dict = stats_dict['groups'][current_group]
                total_shown_dict = group_dict.setdefault('total_shown', {})
                total_shown_dict['source_count'] = int(group['source_count'])
                total_shown_dict['pkt_count'] = int(group['pkt_count'])
                continue
        
        return ret_dict

# ==============================================================================
# Schema and Parser for 'show ipv6 mfib {group} (source} count'
# ==============================================================================
class ShowIpv6MfibGroupCountSchema(MetaParser):
    """Schema for show ipv6 mfib {group} count
                  show ipv6 mfib {group} {source} count"""
    schema = {
        'vrf': {
            Any(): {
                'routes': int,
                'star_g': int,
                'star_g_m': int,
                'group': {
                    Any(): {
                        Optional('rp_tree'): {
                            'sw_forwarding': {
                                'pkt_count': int,
                                'pkts_per_second': int,
                                'avg_pkt_size': int,
                                'kilobits_per_second': int,
                            },
                            'other': {
                                'total': int,
                                'rpf_failed': int,
                                'other_drops': int,
                            },
                            'hw_forwarding': {
                                'pkt_count': int,
                                'pkts_per_second': int,
                                'avg_pkt_size': int,
                                'kilobits_per_second': int,
                            },
                            'hw_other': {
                                'total': int,
                                'rpf_failed': int,
                                'other_drops': int,
                            },
                        },
                        'source': {
                            Any(): {
                                'sw_forwarding': {
                                    'pkt_count': int,
                                    'pkts_per_second': int,
                                    'avg_pkt_size': int,
                                    'kilobits_per_second': int,
                                },
                                'other': {
                                    'total': int,
                                    'rpf_failed': int,
                                    'other_drops': int,
                                },
                                'hw_forwarding': {
                                    'pkt_count': int,
                                    'pkts_per_second': int,
                                    'avg_pkt_size': int,
                                    'kilobits_per_second': int,
                                },
                                'hw_other': {
                                    'total': int,
                                    'rpf_failed': int,
                                    'other_drops': int,
                                },
                            }
                        },
                        'totals': {
                            'source_count': int,
                            'packet_count': int,
                        }
                    }
                },
                'groups': int,
                'average_sources_per_group': float,
            }
        }
    }


class ShowIpv6MfibGroupCount(ShowIpv6MfibGroupCountSchema):
    """Parser for show ipv6 mfib {group} count"""

    cli_command = 'show ipv6 mfib {group} {source} count'

    def cli(self, group="", source="", output=None):
        if output is None:
            cmd = self.cli_command.format(group=group, source=source)
            output = self.device.execute(cmd)

        ret = {} # Changed 'parsed' to 'ret' for consistency with later usage

        # Regex patterns
        # Default
        p1 = re.compile(r'^(?P<vrf_name>Default)$')

        # 56 routes, 9 (*,G)s, 46 (*,G/m)s
        p2 = re.compile(r'(?P<routes>\d+)\s+routes,\s+(?P<g_count>\d+)\s+\(\*,G\)s,\s+(?P<gm_count>\d+)\s+\(\*,G/m\)s')

        # Group: FF03::1:1:1
        p3 = re.compile(r'Group:\s+(?P<group>[0-9A-Fa-f:]+)')

        # RP-tree,
        p4 = re.compile(r'^\s*RP-tree,\s*$')

        # SW Forwarding: 0/0/0/0, Other: 0/0/0
        p5 = re.compile(r'SW Forwarding:\s*(?P<sw_pkts>\d+)/(?P<sw_pps>\d+)/(?P<sw_avg>\d+)/(?P<sw_kbps>\d+),\s*Other:\s*(?P<sw_tot>\d+)/(?P<sw_rpf>\d+)/(?P<sw_other>\d+)')

        # HW Forwarding:   0/0/0/0, Other: 0/0/0
        p6 = re.compile(r'HW Forwarding:\s*(?P<hw_pkts>\d+)/(?P<hw_pps>\d+)/(?P<hw_avg>\d+)/(?P<hw_kbps>\d+),\s*Other:\s*(?P<hw_tot>\d+)/(?P<hw_rpf>\d+)/(?P<hw_other>\d+)')

        # Source: 10::1:1:200,
        p7 = re.compile(r'Source:\s*(?P<src_ip>[0-9A-Fa-f:]+),')

        # Totals - Source count: 1, Packet count: 5
        p8 = re.compile(r'Totals\s*-\s*Source count:\s*(?P<source_count>\d+),\s*Packet count:\s*(?P<packet_count>\d+)')

        # Groups: 1, 1.00 average sources per group
        p9 = re.compile(r'Groups:\s*(?P<groups>\d+),\s*(?P<avg_sources>[\d.]+)\s+average sources per group')


        # Skip header lines
        lines = output.splitlines()
        current_vrf = None 
        current_group = None
        current_source = None

        for line in lines:
            line = line.strip()

            # Skip empty lines and header lines
            if not line or line.startswith('Forwarding Counts:') or line.startswith('Other counts:'):
                continue

            # Default
            m = p1.match(line)
            if m:
                current_vrf = m.group('vrf_name')
                continue

            # Parse route summary line
            # 56 routes, 9 (*,G)s, 46 (*,G/m)s
            m = p2.match(line)
            if m:
                vrf_dict = ret.setdefault('vrf', {}).setdefault(current_vrf, {})
                vrf_dict['routes'] = int(m.group('routes'))
                vrf_dict['star_g'] = int(m.group('g_count'))
                vrf_dict['star_g_m'] = int(m.group('gm_count'))
                continue

            # Parse group line
            # Group: FF03::1:1:1
            m = p3.match(line)
            if m:
                current_group = m.group('group')
                vrf_dict = ret.setdefault('vrf', {}).setdefault(current_vrf, {})
                group_dict = vrf_dict.setdefault('group', {}).setdefault(current_group, {})
                continue

            # Parse RP-tree line
            # RP-tree,
            m = p4.match(line)
            if m:
                group_dict = ret['vrf'][current_vrf]['group'][current_group]
                group_dict.setdefault('rp_tree', {})
                continue

            # Parse Source line
            # Source: 10::1:1:200,
            m = p7.match(line)
            if m:
                current_source = m.group('src_ip')
                group_dict = ret['vrf'][current_vrf]['group'][current_group]
                sources = group_dict.setdefault('source', {})
                sources.setdefault(current_source, {})
                continue

            # Parse SW Forwarding line
            # SW Forwarding: 0/0/0/0, Other: 0/0/0
            m = p5.match(line)
            if m:
                group_dict = ret['vrf'][current_vrf]['group'][current_group]
                if 'rp_tree' in group_dict and current_source is None:
                    # RP-tree SW forwarding
                    group_dict['rp_tree']['sw_forwarding'] = {
                        'pkt_count': int(m.group('sw_pkts')),
                        'pkts_per_second': int(m.group('sw_pps')),
                        'avg_pkt_size': int(m.group('sw_avg')),
                        'kilobits_per_second': int(m.group('sw_kbps')),
                    }
                    group_dict['rp_tree']['other'] = {
                        'total': int(m.group('sw_tot')),
                        'rpf_failed': int(m.group('sw_rpf')),
                        'other_drops': int(m.group('sw_other')),
                    }
                elif current_source:
                    # Source SW forwarding
                    sources = group_dict.setdefault('source', {})
                    sources[current_source]['sw_forwarding'] = {
                        'pkt_count': int(m.group('sw_pkts')),
                        'pkts_per_second': int(m.group('sw_pps')),
                        'avg_pkt_size': int(m.group('sw_avg')),
                        'kilobits_per_second': int(m.group('sw_kbps')),
                    }
                    sources[current_source]['other'] = {
                        'total': int(m.group('sw_tot')),
                        'rpf_failed': int(m.group('sw_rpf')),
                        'other_drops': int(m.group('sw_other')),
                    }
                continue

            # Parse HW Forwarding line
            # HW Forwarding:   0/0/0/0, Other: 0/0/0
            m = p6.match(line)
            if m:
                group_dict = ret['vrf'][current_vrf]['group'][current_group]
                if 'rp_tree' in group_dict and current_source is None:
                    # RP-tree HW forwarding
                    group_dict['rp_tree']['hw_forwarding'] = {
                        'pkt_count': int(m.group('hw_pkts')),
                        'pkts_per_second': int(m.group('hw_pps')),
                        'avg_pkt_size': int(m.group('hw_avg')),
                        'kilobits_per_second': int(m.group('hw_kbps')),
                    }
                    group_dict['rp_tree']['hw_other'] = {
                        'total': int(m.group('hw_tot')),
                        'rpf_failed': int(m.group('hw_rpf')),
                        'other_drops': int(m.group('hw_other')),
                    }
                elif current_source:
                    # Source HW forwarding
                    sources = group_dict.setdefault('source', {})
                    sources[current_source]['hw_forwarding'] = {
                        'pkt_count': int(m.group('hw_pkts')),
                        'pkts_per_second': int(m.group('hw_pps')),
                        'avg_pkt_size': int(m.group('hw_avg')),
                        'kilobits_per_second': int(m.group('hw_kbps')),
                    }
                    sources[current_source]['hw_other'] = {
                        'total': int(m.group('hw_tot')),
                        'rpf_failed': int(m.group('hw_rpf')),
                        'other_drops': int(m.group('hw_other')),
                    }
                continue


            # Parse Totals line
            # Totals - Source count: 1, Packet count: 5
            m = p8.match(line)
            if m:
                group_dict = ret['vrf'][current_vrf]['group'][current_group]
                group_dict['totals'] = {
                    'source_count': int(m.group('source_count')),
                    'packet_count': int(m.group('packet_count')),
                }
                # Reset current_source after processing totals
                current_source = None
                continue

            # Parse Groups summary line
            # Groups: 1, 1.00 average sources per group
            m = p9.match(line)
            if m:
                vrf_dict = ret['vrf'][current_vrf]
                vrf_dict['groups'] = int(m.group('groups'))
                vrf_dict['average_sources_per_group'] = float(m.group('avg_sources'))
                continue

        return ret

# ==============================================
# Schema for show ipv6 virtual-reassembly features
# ==============================================
class ShowIpv6VirtualReassemblyFeaturesSchema(MetaParser):
    """Schema for show ipv6 virtual-reassembly features"""

    schema = {
        'interfaces': {
            Any(): {
                'status': str,
                'direction': str,
                'enabled_features': str
            }
        }
    }


# ==============================================
# Parser for show ipv6 virtual-reassembly features
# ==============================================
class ShowIpv6VirtualReassemblyFeatures(ShowIpv6VirtualReassemblyFeaturesSchema):
    """Parser for show ipv6 virtual-reassembly features"""

    cli_command = 'show ipv6 virtual-reassembly features'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the result dict
        result_dict = {}

        # NVI0:
        p1 = re.compile(r'^(?P<interface>\S+):$')

        # IPV6 Virtual Fragment Reassembly (IPV6 VFR) Current Status is ENABLED [out]
        p2 = re.compile(r'^IPV6 Virtual Fragment Reassembly \(IPV6 VFR\) Current Status is'
                        r' (?P<status>\w+)(?: \[(?P<direction>\w+)\])?$')

        # Features to use if IPV6 VFR is Enabled:NAT64
        p3 = re.compile(r'^Features to use if IPV6 VFR is Enabled:(?P<features>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # NVI0:
            m = p1.match(line)
            if m:
                interface = m.groupdict()['interface']
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(interface, {})
                continue

            # IPV6 Virtual Fragment Reassembly (IPV6 VFR) Current Status is ENABLED [out]
            m = p2.match(line)
            if m:
                group = m.groupdict()
                intf_dict['status'] = group['status']
                if group['direction']:
                    intf_dict['direction'] = group['direction'].lower()
                continue

            # Features to use if IPV6 VFR is Enabled:NAT64
            m = p3.match(line)
            if m:
                intf_dict['enabled_features'] = m.groupdict()['features']
                continue

        return result_dict

# ==============================================================================
# Schema and Parser for 'show ipv6 mfib {group} active'
# ==============================================================================

class ShowIpv6MfibGroupActiveSchema(MetaParser):
    """Schema for show ipv6 mfib {group} active"""
    schema = {
        'active_multicast_sources': {
            'threshold_kbps': int,
            Optional('sources'): {
                Any(): {  # Source IP address
                    'group': str,
                    'rate_kbps': int,
                    Optional('interface'): str,
                }
            }
        }
    }

class ShowIpv6MfibGroupActive(ShowIpv6MfibGroupActiveSchema):
    """Parser for show ipv6 mfib {group} active"""

    cli_command = 'show ipv6 mfib {group} active'

    def cli(self, group="", output=None):
        if output is None:
            cmd = self.cli_command.format(group=group)
            output = self.device.execute(cmd)

        ret = {}

        # Active Multicast Sources - sending >= 4 kbps
        p1 = re.compile(r'^Active Multicast Sources - sending >= (?P<unit>\d+) kbps$')

        # Default
        p2 = re.compile(r'^(?P<vrf_name>Default)$')

        # (2001:DB8::1, FF03::1:1:1) 100 kbps GigabitEthernet0/0/1
        p3 = re.compile(r'\((?P<source_ip>[0-9A-Fa-f:]+),\s*(?P<group_ip>[0-9A-Fa-f:]+)\)\s+(?P<rate>\d+)\s*kbps(?:\s+(?P<interface>\S+))?')

        lines = output.strip().splitlines()

        for line in lines:
            # Active Multicast Sources - sending >= 4 kbps
            m = p1.match(line)
            if m:
                threshold = int(m.group('unit'))
                active_dict = ret.setdefault('active_multicast_sources', {})
                active_dict['threshold_kbps'] = threshold
                continue

            # Parse VRF line
            # Default
            m = p2.match(line)
            if m:
                continue

            # (2001:DB8::1, FF03::1:1:1) 100 kbps GigabitEthernet0/0/1
            m = p3.match(line)
            if m:
                source_ip = m.group('source_ip').strip()
                group_ip = m.group('group_ip').strip()
                rate = int(m.group('rate'))
                interface = m.group('interface')
                vrf_dict = ret['active_multicast_sources']
                sources = vrf_dict.setdefault('sources', {})
                source_dict = sources.setdefault(source_ip, {})
                source_dict['group'] = group_ip
                source_dict['rate_kbps'] = rate
                if interface:
                    source_dict['interface'] = interface
                continue

        return ret


class ShowIpv6TrafficSchema(MetaParser):
    """Schema for show ipv6 traffic"""

    schema = {
        "ipv6_statistics": {
            "received": {
                "total": int,
                "total_bytes": int,
                "local_destination": int,
                "source_routed": int,
                "truncated": int,
                "no_route": int,
                "format_errors": int,
                "hop_count_exceeded": int,
                "bad_header": int,
                "unknown_option": int,
                "bad_source": int,
                "unknown_protocol": int,
                "not_a_router": int,
                "fragments": int,
                "total_reassembled": int,
                "reassembly_timeouts": int,
                "reassembly_failures": int
            },
            "sent": {
                "total": int,
                "total_bytes": int,
                "generated": int,
                "forwarded": int,
                "fragmented": int,
                "fragments": int,
                "failed": int,
                "encapsulation_failed": int,
                "no_route": int,
                "too_big": int,
                "rpf_drops": int,
                "rpf_suppressed_drops": int
            },
            "multicast": {
                "received": int,
                "received_bytes": int,
                "sent": int,
                "sent_bytes": int
            }
        },
        "icmp_statistics": {
            "received": {
                "input": int,
                "checksum_errors": int,
                "too_short": int,
                "unknown_info_type": int,
                "unknown_error_type": int,
                "unreachable": {
                    "routing": int,
                    "admin": int,
                    "neighbor": int,
                    "address": int,
                    "port": int,
                    "sa_policy": int,
                    "reject_route": int
                },
                "parameter": {
                    "error": int,
                    "header": int,
                    "option": int
                },
                "hopcount_expired": int,
                "reassembly_timeout": int,
                "too_big": int,
                "bad_embedded_ipv6": int,
                "echo_request": int,
                "echo_reply": int,
                "group_query": int,
                "group_report": int,
                "group_reduce": int,
                "router_solicit": int,
                "router_advert": int,
                "redirects": int,
                "neighbor_solicit": int,
                "neighbor_advert": int
            },
            "sent": {
                "output": int,
                "rate_limited": int,
                "unreachable": {
                    "routing": int,
                    "admin": int,
                    "neighbor": int,
                    "address": int,
                    "port": int,
                    "sa_policy": int,
                    "reject_route": int
                },
                "parameter": {
                    "error": int,
                    "header": int,
                    "option": int
                },
                "hopcount_expired": int,
                "reassembly_timeout": int,
                "too_big": int,
                "echo_request": int,
                "echo_reply": int,
                "group_query": int,
                "group_report": int,
                "group_reduce": int,
                "router_solicit": int,
                "router_advert": int,
                "redirects": int,
                "neighbor_solicit": int,
                "neighbor_advert": int
            }
        },
        "udp_statistics": {
            "received": {
                "input": int,
                "checksum_errors": int,
                "length_errors": int,
                "no_port": int,
                "dropped": int
            },
            "sent": {
                "output": int
            }
        },
        "tcp_statistics": {
            "received": {
                "input": int,
                "checksum_errors": int
            },
            "sent": {
                "output": int,
                "retransmitted": int
            }
        }
    }


class ShowIpv6Traffic(ShowIpv6TrafficSchema):
    """Parser for show ipv6 traffic"""

    cli_command = "show ipv6 traffic"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        if not output:
            return ret_dict

        section = None
        sub_section = None
        icmp_sub_sub = None

        # IPv6 statistics:
        p1 = re.compile(r"^IPv6 statistics:$")
        # ICMP statistics:
        p2 = re.compile(r"^ICMP statistics:$")
        # UDP statistics:
        p3 = re.compile(r"^UDP statistics:$")
        # TCP statistics:
        p4 = re.compile(r"^TCP statistics:$")
        #         Rcvd:  2 total, 112 total_bytes, 2 local destination
        p5 = re.compile(r"^Rcvd:\s+(\d+) total, (\d+) total_bytes, (\d+) local destination$")
        #                0 source-routed, 0 truncated, 0 no route
        p6 = re.compile(r"^(\d+) source-routed, (\d+) truncated, (\d+) no route$")
        #                0 format errors, 0 hop count exceeded
        p7 = re.compile(r"^(\d+) format errors, (\d+) hop count exceeded$")
        #                0 bad header, 0 unknown option, 0 bad source
        p8 = re.compile(r"^(\d+) bad header, (\d+) unknown option, (\d+) bad source$")
        #                0 unknown protocol, 0 not a router
        p9 = re.compile(r"^(\d+) unknown protocol, (\d+) not a router$")
        #                0 fragments, 0 total reassembled
        p10 = re.compile(r"^(\d+) fragments, (\d+) total reassembled$")
        #                0 reassembly timeouts, 0 reassembly failures
        p11 = re.compile(r"^(\d+) reassembly timeouts, (\d+) reassembly failures$")
        #         Sent:  161 total, 18670 total_bytes
        p12 = re.compile(r"^Sent:\s+(\d+) total, (\d+) total_bytes$")
        #                162 generated, 161 forwarded
        p13 = re.compile(r"^(\d+) generated, (\d+) forwarded$")
        #                0 fragmented into 0 fragments, 0 failed
        p14 = re.compile(r"^(\d+) fragmented into (\d+) fragments, (\d+) failed$")
        #                0 encapsulation failed, 0 no route, 0 too big
        p15 = re.compile(r"^(\d+) encapsulation failed, (\d+) no route, (\d+) too big$")
        #                0 RPF drops, 0 RPF suppressed drops
        p16 = re.compile(r"^(\d+) RPF drops, (\d+) RPF suppressed drops$")
        #         Mcast: 2 received, 112 received bytes
        p17 = re.compile(r"^Mcast:\s+(\d+) received, (\d+) received bytes$")
        #                0 sent, 0 sent bytes
        p18 = re.compile(r"^(\d+) sent, (\d+) sent bytes$")
        #         Rcvd: 2 input, 0 checksum errors, 0 too short
        p19 = re.compile(r"^Rcvd:\s+(\d+) input, (\d+) checksum errors, (\d+) too short$")
        #               0 unknown info type, 0 unknown error type
        p20 = re.compile(r"^(\d+) unknown info type, (\d+) unknown error type$")
        #               unreach: 0 routing, 0 admin, 0 neighbor, 0 address, 0 port
        p21 = re.compile(r"^unreach:\s+(\d+) routing, (\d+) admin, (\d+) neighbor, (\d+) address, (\d+) port$")
        #                        0 sa policy, 0 reject route
        p22 = re.compile(r"^(\d+) sa policy, (\d+) reject route$")
        #               parameter: 0 error, 0 header, 0 option
        p23 = re.compile(r"^parameter:\s+(\d+) error, (\d+) header, (\d+) option$")
        #               0 hopcount expired, 0 reassembly timeout,0 too big
        p24 = re.compile(r"^(\d+) hopcount expired, (\d+) reassembly timeout,(\d+) too big$")
        #               0 bad embedded ipv6
        p25 = re.compile(r"^(\d+) bad embedded ipv6$")
        #               0 echo request, 0 echo reply
        p26 = re.compile(r"^(\d+) echo request, (\d+) echo reply$")
        #               0 group query, 0 group report, 0 group reduce
        p27 = re.compile(r"^(\d+) group query, (\d+) group report, (\d+) group reduce$")
        #               2 router solicit, 0 router advert, 0 redirects
        p28 = re.compile(r"^(\d+) router solicit, (\d+) router advert, (\d+) redirects$")
        #               0 neighbor solicit, 0 neighbor advert
        p29 = re.compile(r"^(\d+) neighbor solicit, (\d+) neighbor advert$")
        #         Sent: 162 output, 0 rate-limited
        p30 = re.compile(r"^Sent:\s+(\d+) output, (\d+) rate-limited$")
        #               unreach: 0 routing, 0 admin, 0 neighbor, 0 address, 0 port
        p31 = re.compile(r"^unreach:\s+(\d+) routing, (\d+) admin, (\d+) neighbor, (\d+) address, (\d+) port$")
        #                        0 sa policy, 0 reject route
        p32 = re.compile(r"^(\d+) sa policy, (\d+) reject route$")
        #               parameter: 0 error, 0 header, 0 option
        p33 = re.compile(r"^parameter:\s+(\d+) error, (\d+) header, (\d+) option$")
        #               0 hopcount expired, 0 reassembly timeout,0 too big
        p34 = re.compile(r"^(\d+) hopcount expired, (\d+) reassembly timeout,(\d+) too big$")
        #               0 echo request, 0 echo reply
        p35 = re.compile(r"^(\d+) echo request, (\d+) echo reply$")
        #               0 group query, 0 group report, 0 group reduce
        p36 = re.compile(r"^(\d+) group query, (\d+) group report, (\d+) group reduce$")
        #               0 router solicit, 162 router advert, 0 redirects
        p37 = re.compile(r"^(\d+) router solicit, (\d+) router advert, (\d+) redirects$")
        #               0 neighbor solicit, 0 neighbor advert
        p38 = re.compile(r"^(\d+) neighbor solicit, (\d+) neighbor advert$")
        #   Rcvd: 0 input, 0 checksum errors, 0 length errors
        p39 = re.compile(r"^Rcvd:\s+(\d+) input, (\d+) checksum errors, (\d+) length errors$")
        #         0 no port, 0 dropped
        p40 = re.compile(r"^(\d+) no port, (\d+) dropped$")
        #   Sent: 0 output
        p41 = re.compile(r"^Sent:\s+(\d+) output$")
        #   Rcvd: 0 input, 0 checksum errors
        p42 = re.compile(r"^Rcvd:\s+(\d+) input, (\d+) checksum errors$")
        #   Sent: 0 output, 0 retransmitted
        p43 = re.compile(r"^Sent:\s+(\d+) output, (\d+) retransmitted$")

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # IPv6 statistics:
            m = p1.match(line)
            if m:
                section = "ipv6_statistics"
                ret_dict.setdefault(section, {})
                sub_section = None
                continue

            # ICMP statistics:
            m = p2.match(line)
            if m:
                section = "icmp_statistics"
                ret_dict.setdefault(section, {})
                sub_section = None
                icmp_sub_sub = None
                continue

            # UDP statistics:
            m = p3.match(line)
            if m:
                section = "udp_statistics"
                ret_dict.setdefault(section, {})
                sub_section = None
                continue

            # TCP statistics:
            m = p4.match(line)
            if m:
                section = "tcp_statistics"
                ret_dict.setdefault(section, {})
                sub_section = None
                continue

            #         Rcvd:  2 total, 112 total_bytes, 2 local destination
            m = p5.match(line)
            if m and section == "ipv6_statistics":
                sub_section = "received"
                d = ret_dict[section].setdefault(sub_section, {})
                d["total"] = int(m.group(1))
                d["total_bytes"] = int(m.group(2))
                d["local_destination"] = int(m.group(3))
                continue

            #                0 source-routed, 0 truncated, 0 no route
            m = p6.match(line)
            if m and section == "ipv6_statistics" and sub_section == "received":
                d = ret_dict[section][sub_section]
                d["source_routed"] = int(m.group(1))
                d["truncated"] = int(m.group(2))
                d["no_route"] = int(m.group(3))
                continue

            #                0 format errors, 0 hop count exceeded
            m = p7.match(line)
            if m and section == "ipv6_statistics" and sub_section == "received":
                d = ret_dict[section][sub_section]
                d["format_errors"] = int(m.group(1))
                d["hop_count_exceeded"] = int(m.group(2))
                continue

            #                0 bad header, 0 unknown option, 0 bad source
            m = p8.match(line)
            if m and section == "ipv6_statistics" and sub_section == "received":
                d = ret_dict[section][sub_section]
                d["bad_header"] = int(m.group(1))
                d["unknown_option"] = int(m.group(2))
                d["bad_source"] = int(m.group(3))
                continue

            #                0 unknown protocol, 0 not a router
            m = p9.match(line)
            if m and section == "ipv6_statistics" and sub_section == "received":
                d = ret_dict[section][sub_section]
                d["unknown_protocol"] = int(m.group(1))
                d["not_a_router"] = int(m.group(2))
                continue

            #                0 fragments, 0 total reassembled
            m = p10.match(line)
            if m and section == "ipv6_statistics" and sub_section == "received":
                d = ret_dict[section][sub_section]
                d["fragments"] = int(m.group(1))
                d["total_reassembled"] = int(m.group(2))
                continue

            #                0 reassembly timeouts, 0 reassembly failures
            m = p11.match(line)
            if m and section == "ipv6_statistics" and sub_section == "received":
                d = ret_dict[section][sub_section]
                d["reassembly_timeouts"] = int(m.group(1))
                d["reassembly_failures"] = int(m.group(2))
                continue

            #         Sent:  161 total, 18670 total_bytes
            m = p12.match(line)
            if m and section == "ipv6_statistics":
                sub_section = "sent"
                d = ret_dict[section].setdefault(sub_section, {})
                d["total"] = int(m.group(1))
                d["total_bytes"] = int(m.group(2))
                continue

            #                162 generated, 161 forwarded
            m = p13.match(line)
            if m and section == "ipv6_statistics" and sub_section == "sent":
                d = ret_dict[section][sub_section]
                d["generated"] = int(m.group(1))
                d["forwarded"] = int(m.group(2))
                continue

            #                0 fragmented into 0 fragments, 0 failed
            m = p14.match(line)
            if m and section == "ipv6_statistics" and sub_section == "sent":
                d = ret_dict[section][sub_section]
                d["fragmented"] = int(m.group(1))
                d["fragments"] = int(m.group(2))
                d["failed"] = int(m.group(3))
                continue

            #                0 encapsulation failed, 0 no route, 0 too big
            m = p15.match(line)
            if m and section == "ipv6_statistics" and sub_section == "sent":
                d = ret_dict[section][sub_section]
                d["encapsulation_failed"] = int(m.group(1))
                d["no_route"] = int(m.group(2))
                d["too_big"] = int(m.group(3))
                continue

            #                0 RPF drops, 0 RPF suppressed drops
            m = p16.match(line)
            if m and section == "ipv6_statistics" and sub_section == "sent":
                d = ret_dict[section][sub_section]
                d["rpf_drops"] = int(m.group(1))
                d["rpf_suppressed_drops"] = int(m.group(2))
                continue

            #         Mcast: 2 received, 112 received bytes
            m = p17.match(line)
            if m and section == "ipv6_statistics":
                sub_section = "multicast"
                d = ret_dict[section].setdefault(sub_section, {})
                d["received"] = int(m.group(1))
                d["received_bytes"] = int(m.group(2))
                continue

            #                0 sent, 0 sent bytes
            m = p18.match(line)
            if m and section == "ipv6_statistics" and sub_section == "multicast":
                d = ret_dict[section][sub_section]
                d["sent"] = int(m.group(1))
                d["sent_bytes"] = int(m.group(2))
                continue

            #         Rcvd: 2 input, 0 checksum errors, 0 too short
            m = p19.match(line)
            if m and section == "icmp_statistics":
                sub_section = "received"
                ret_dict[section].setdefault(sub_section, {})
                d = ret_dict[section][sub_section]
                d["input"] = int(m.group(1))
                d["checksum_errors"] = int(m.group(2))
                d["too_short"] = int(m.group(3))
                continue

            #               0 unknown info type, 0 unknown error type
            m = p20.match(line)
            if m and section == "icmp_statistics" and sub_section == "received":
                d = ret_dict[section][sub_section]
                d["unknown_info_type"] = int(m.group(1))
                d["unknown_error_type"] = int(m.group(2))
                continue

            #               unreach: 0 routing, 0 admin, 0 neighbor, 0 address, 0 port
            m = p21.match(line)
            if m and section == "icmp_statistics" and sub_section == "received":
                d = ret_dict[section][sub_section].setdefault("unreachable", {})
                d["routing"] = int(m.group(1))
                d["admin"] = int(m.group(2))
                d["neighbor"] = int(m.group(3))
                d["address"] = int(m.group(4))
                d["port"] = int(m.group(5))
                icmp_sub_sub = "unreachable"
                continue

            #                        0 sa policy, 0 reject route
            m = p22.match(line)
            if m and section == "icmp_statistics" and sub_section == "received" and icmp_sub_sub == "unreachable":
                d = ret_dict[section][sub_section]["unreachable"]
                d["sa_policy"] = int(m.group(1))
                d["reject_route"] = int(m.group(2))
                icmp_sub_sub = None
                continue

            #               parameter: 0 error, 0 header, 0 option
            m = p23.match(line)
            if m and section == "icmp_statistics" and sub_section == "received":
                d = ret_dict[section][sub_section].setdefault("parameter", {})
                d["error"] = int(m.group(1))
                d["header"] = int(m.group(2))
                d["option"] = int(m.group(3))
                icmp_sub_sub = "parameter"
                continue

            #               0 hopcount expired, 0 reassembly timeout,0 too big
            m = p24.match(line)
            if m and section == "icmp_statistics" and sub_section == "received":
                d = ret_dict[section][sub_section]
                d["hopcount_expired"] = int(m.group(1))
                d["reassembly_timeout"] = int(m.group(2))
                d["too_big"] = int(m.group(3))
                continue

            #               0 bad embedded ipv6
            m = p25.match(line)
            if m and section == "icmp_statistics" and sub_section == "received":
                d = ret_dict[section][sub_section]
                d["bad_embedded_ipv6"] = int(m.group(1))
                continue

            #               0 echo request, 0 echo reply
            m = p26.match(line)
            if m and section == "icmp_statistics" and sub_section == "received":
                d = ret_dict[section][sub_section]
                d["echo_request"] = int(m.group(1))
                d["echo_reply"] = int(m.group(2))
                continue

            #               0 group query, 0 group report, 0 group reduce
            m = p27.match(line)
            if m and section == "icmp_statistics" and sub_section == "received":
                d = ret_dict[section][sub_section]
                d["group_query"] = int(m.group(1))
                d["group_report"] = int(m.group(2))
                d["group_reduce"] = int(m.group(3))
                continue

            #               2 router solicit, 0 router advert, 0 redirects
            m = p28.match(line)
            if m and section == "icmp_statistics" and sub_section == "received":
                d = ret_dict[section][sub_section]
                d["router_solicit"] = int(m.group(1))
                d["router_advert"] = int(m.group(2))
                d["redirects"] = int(m.group(3))
                continue

            #               0 neighbor solicit, 0 neighbor advert
            m = p29.match(line)
            if m and section == "icmp_statistics" and sub_section == "received":
                d = ret_dict[section][sub_section]
                d["neighbor_solicit"] = int(m.group(1))
                d["neighbor_advert"] = int(m.group(2))
                continue

            #         Sent: 162 output, 0 rate-limited
            m = p30.match(line)
            if m and section == "icmp_statistics":
                sub_section = "sent"
                ret_dict[section].setdefault(sub_section, {})
                d = ret_dict[section][sub_section]
                d["output"] = int(m.group(1))
                d["rate_limited"] = int(m.group(2))
                continue

            #               unreach: 0 routing, 0 admin, 0 neighbor, 0 address, 0 port
            m = p31.match(line)
            if m and section == "icmp_statistics" and sub_section == "sent":
                d = ret_dict[section][sub_section].setdefault("unreachable", {})
                d["routing"] = int(m.group(1))
                d["admin"] = int(m.group(2))
                d["neighbor"] = int(m.group(3))
                d["address"] = int(m.group(4))
                d["port"] = int(m.group(5))
                icmp_sub_sub = "unreachable"
                continue

            #                        0 sa policy, 0 reject route
            m = p32.match(line)
            if m and section == "icmp_statistics" and sub_section == "sent" and icmp_sub_sub == "unreachable":
                d = ret_dict[section][sub_section]["unreachable"]
                d["sa_policy"] = int(m.group(1))
                d["reject_route"] = int(m.group(2))
                icmp_sub_sub = None
                continue

            #               parameter: 0 error, 0 header, 0 option
            m = p33.match(line)
            if m and section == "icmp_statistics" and sub_section == "sent":
                d = ret_dict[section][sub_section].setdefault("parameter", {})
                d["error"] = int(m.group(1))
                d["header"] = int(m.group(2))
                d["option"] = int(m.group(3))
                icmp_sub_sub = "parameter"
                continue

            #               0 hopcount expired, 0 reassembly timeout,0 too big
            m = p34.match(line)
            if m and section == "icmp_statistics" and sub_section == "sent":
                d = ret_dict[section][sub_section]
                d["hopcount_expired"] = int(m.group(1))
                d["reassembly_timeout"] = int(m.group(2))
                d["too_big"] = int(m.group(3))
                continue

            #               0 echo request, 0 echo reply
            m = p35.match(line)
            if m and section == "icmp_statistics" and sub_section == "sent":
                d = ret_dict[section][sub_section]
                d["echo_request"] = int(m.group(1))
                d["echo_reply"] = int(m.group(2))
                continue

            #               0 group query, 0 group report, 0 group reduce
            m = p36.match(line)
            if m and section == "icmp_statistics" and sub_section == "sent":
                d = ret_dict[section][sub_section]
                d["group_query"] = int(m.group(1))
                d["group_report"] = int(m.group(2))
                d["group_reduce"] = int(m.group(3))
                continue

            #               0 router solicit, 162 router advert, 0 redirects
            m = p37.match(line)
            if m and section == "icmp_statistics" and sub_section == "sent":
                d = ret_dict[section][sub_section]
                d["router_solicit"] = int(m.group(1))
                d["router_advert"] = int(m.group(2))
                d["redirects"] = int(m.group(3))
                continue

            #               0 neighbor solicit, 0 neighbor advert
            m = p38.match(line)
            if m and section == "icmp_statistics" and sub_section == "sent":
                d = ret_dict[section][sub_section]
                d["neighbor_solicit"] = int(m.group(1))
                d["neighbor_advert"] = int(m.group(2))
                continue

            #   Rcvd: 0 input, 0 checksum errors, 0 length errors
            m = p39.match(line)
            if m and section == "udp_statistics":
                sub_section = "received"
                d = ret_dict[section].setdefault(sub_section, {})
                d["input"] = int(m.group(1))
                d["checksum_errors"] = int(m.group(2))
                d["length_errors"] = int(m.group(3))
                continue

            #         0 no port, 0 dropped
            m = p40.match(line)
            if m and section == "udp_statistics" and sub_section == "received":
                d = ret_dict[section][sub_section]
                d["no_port"] = int(m.group(1))
                d["dropped"] = int(m.group(2))
                continue

            #   Sent: 0 output
            m = p41.match(line)
            if m and section == "udp_statistics":
                sub_section = "sent"
                d = ret_dict[section].setdefault(sub_section, {})
                d["output"] = int(m.group(1))
                continue

            #   Rcvd: 0 input, 0 checksum errors
            m = p42.match(line)
            if m and section == "tcp_statistics":
                sub_section = "received"
                d = ret_dict[section].setdefault(sub_section, {})
                d["input"] = int(m.group(1))
                d["checksum_errors"] = int(m.group(2))
                continue

            #   Sent: 0 output, 0 retransmitted 
            m = p43.match(line)
            if m and section == "tcp_statistics":
                sub_section = "sent"
                d = ret_dict[section].setdefault(sub_section, {})
                d["output"] = int(m.group(1))
                d["retransmitted"] = int(m.group(2))
                continue

        return ret_dict



class ShowIpv6VirtualReassemblySchema(MetaParser):
    '''Schema for show ipv6 virtual-reassembly'''
    schema = {
        'interfaces': {
            Any(): {  # Interface name as key (e.g., 'NVI0')
                'status': str,
                'direction': str,
                'max_reassemblies': int,
                'max_fragments': int,
                'timeout': int,
                'drop_fragments': str,
                'current_reassembly_count': int,
                'current_fragment_count': int,
                'total_reassembly_count': int,
                'total_reassembly_timeout_count': int,
            }
        }
    }

class ShowIpv6VirtualReassembly(ShowIpv6VirtualReassemblySchema):
    '''Parser for show ipv6 virtual-reassembly'''
    
    cli_command = 'show ipv6 virtual-reassembly'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        result = {}

        # NVI0:
        p0 = re.compile(r'^(?P<interface>\S+):$')
        
        # IPv6 Virtual Fragment Reassembly (IPV6VFR) is ENABLED [out]
        p1 = re.compile(r'^\s*IPv6 Virtual Fragment Reassembly \(IPV6VFR\) is (?P<status>\w+) \[(?P<direction>\w+)\]')
        
        # IPv6 configured concurrent reassemblies (max-reassemblies): 1024
        p2 = re.compile(r'^\s*IPv6 configured concurrent reassemblies \(max-reassemblies\):\s*(?P<max_reassemblies>\d+)')
        
        # IPv6 configured fragments per reassembly (max-fragments): 16
        p3 = re.compile(r'^\s*IPv6 configured fragments per reassembly \(max-fragments\):\s*(?P<max_fragments>\d+)')
        
        # IPv6 configured reassembly timeout (timeout): 3 seconds
        p4 = re.compile(r'^\s*IPv6 configured reassembly timeout \(timeout\):\s*(?P<timeout>\d+)\s*seconds')
        
        # IPv6 configured drop fragments: OFF
        p5 = re.compile(r'^\s*IPv6 configured drop fragments:\s*(?P<drop_fragments>\w+)')
        
        # IPv6 current reassembly count:0
        p6 = re.compile(r'^\s*IPv6 current reassembly count:\s*(?P<current_reassembly>\d+)')
        
        # IPv6 current fragment count:0
        p7 = re.compile(r'^\s*IPv6 current fragment count:\s*(?P<current_fragment>\d+)')
        
        # IPv6 total reassembly count:0
        p8 = re.compile(r'^\s*IPv6 total reassembly count:\s*(?P<total_reassembly>\d+)')
        
        # IPv6 total reassembly timeout count:0
        p9 = re.compile(r'^\s*IPv6 total reassembly timeout count:\s*(?P<total_timeout>\d+)')

        current_interface = None

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # NVI0:
            m0 = p0.match(line)
            if m0:
                current_interface = m0.group('interface')
                interfaces = result.setdefault('interfaces', {})
                interfaces[current_interface] = {}
                continue

            # IPv6 Virtual Fragment Reassembly (IPV6VFR) is ENABLED [out]
            m1 = p1.match(line)
            if m1 and current_interface:
                result['interfaces'][current_interface]['status'] = m1.group('status')
                result['interfaces'][current_interface]['direction'] = m1.group('direction')
                continue

            # IPv6 configured concurrent reassemblies (max-reassemblies): 1024
            m2 = p2.match(line)
            if m2 and current_interface:
                result['interfaces'][current_interface]['max_reassemblies'] = int(m2.group('max_reassemblies'))
                continue

            # IPv6 configured fragments per reassembly (max-fragments): 16
            m3 = p3.match(line)
            if m3 and current_interface:
                result['interfaces'][current_interface]['max_fragments'] = int(m3.group('max_fragments'))
                continue

            # IPv6 configured reassembly timeout (timeout): 3 seconds
            m4 = p4.match(line)
            if m4 and current_interface:
                result['interfaces'][current_interface]['timeout'] = int(m4.group('timeout'))
                continue

            # IPv6 configured drop fragments: OFF
            m5 = p5.match(line)
            if m5 and current_interface:
                result['interfaces'][current_interface]['drop_fragments'] = m5.group('drop_fragments')
                continue

            # IPv6 current reassembly count:0
            m6 = p6.match(line)
            if m6 and current_interface:
                result['interfaces'][current_interface]['current_reassembly_count'] = int(m6.group('current_reassembly'))
                continue

            # IPv6 current fragment count:0
            m7 = p7.match(line)
            if m7 and current_interface:
                result['interfaces'][current_interface]['current_fragment_count'] = int(m7.group('current_fragment'))
                continue

            # IPv6 total reassembly count:0
            m8 = p8.match(line)
            if m8 and current_interface:
                result['interfaces'][current_interface]['total_reassembly_count'] = int(m8.group('total_reassembly'))
                continue

            # IPv6 total reassembly timeout count:0
            m9 = p9.match(line)
            if m9 and current_interface:
                result['interfaces'][current_interface]['total_reassembly_timeout_count'] = int(m9.group('total_timeout'))
                continue

        return result




class ShowIpv6VirtualReassemblySchema(MetaParser):
    '''Schema for show ipv6 virtual-reassembly'''
    schema = {
        'interfaces': {
            Any(): {  # Interface name as key (e.g., 'NVI0')
                'status': str,
                'direction': str,
                'max_reassemblies': int,
                'max_fragments': int,
                'timeout': int,
                'drop_fragments': str,
                'current_reassembly_count': int,
                'current_fragment_count': int,
                'total_reassembly_count': int,
                'total_reassembly_timeout_count': int,
            }
        }
    }

class ShowIpv6VirtualReassembly(ShowIpv6VirtualReassemblySchema):
    '''Parser for show ipv6 virtual-reassembly'''
    
    cli_command = 'show ipv6 virtual-reassembly'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        result = {}

        # NVI0:
        p0 = re.compile(r'^(?P<interface>\S+):$')
        
        # IPv6 Virtual Fragment Reassembly (IPV6VFR) is ENABLED [out]
        p1 = re.compile(r'^\s*IPv6 Virtual Fragment Reassembly \(IPV6VFR\) is (?P<status>\w+) \[(?P<direction>\w+)\]')
        
        # IPv6 configured concurrent reassemblies (max-reassemblies): 1024
        p2 = re.compile(r'^\s*IPv6 configured concurrent reassemblies \(max-reassemblies\):\s*(?P<max_reassemblies>\d+)')
        
        # IPv6 configured fragments per reassembly (max-fragments): 16
        p3 = re.compile(r'^\s*IPv6 configured fragments per reassembly \(max-fragments\):\s*(?P<max_fragments>\d+)')
        
        # IPv6 configured reassembly timeout (timeout): 3 seconds
        p4 = re.compile(r'^\s*IPv6 configured reassembly timeout \(timeout\):\s*(?P<timeout>\d+)\s*seconds')
        
        # IPv6 configured drop fragments: OFF
        p5 = re.compile(r'^\s*IPv6 configured drop fragments:\s*(?P<drop_fragments>\w+)')
        
        # IPv6 current reassembly count:0
        p6 = re.compile(r'^\s*IPv6 current reassembly count:\s*(?P<current_reassembly>\d+)')
        
        # IPv6 current fragment count:0
        p7 = re.compile(r'^\s*IPv6 current fragment count:\s*(?P<current_fragment>\d+)')
        
        # IPv6 total reassembly count:0
        p8 = re.compile(r'^\s*IPv6 total reassembly count:\s*(?P<total_reassembly>\d+)')
        
        # IPv6 total reassembly timeout count:0
        p9 = re.compile(r'^\s*IPv6 total reassembly timeout count:\s*(?P<total_timeout>\d+)')

        current_interface = None

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # NVI0:
            m0 = p0.match(line)
            if m0:
                current_interface = m0.group('interface')
                interfaces = result.setdefault('interfaces', {})
                interfaces[current_interface] = {}
                continue

            # IPv6 Virtual Fragment Reassembly (IPV6VFR) is ENABLED [out]
            m1 = p1.match(line)
            if m1 and current_interface:
                result['interfaces'][current_interface]['status'] = m1.group('status')
                result['interfaces'][current_interface]['direction'] = m1.group('direction')
                continue

            # IPv6 configured concurrent reassemblies (max-reassemblies): 1024
            m2 = p2.match(line)
            if m2 and current_interface:
                result['interfaces'][current_interface]['max_reassemblies'] = int(m2.group('max_reassemblies'))
                continue

            # IPv6 configured fragments per reassembly (max-fragments): 16
            m3 = p3.match(line)
            if m3 and current_interface:
                result['interfaces'][current_interface]['max_fragments'] = int(m3.group('max_fragments'))
                continue

            # IPv6 configured reassembly timeout (timeout): 3 seconds
            m4 = p4.match(line)
            if m4 and current_interface:
                result['interfaces'][current_interface]['timeout'] = int(m4.group('timeout'))
                continue

            # IPv6 configured drop fragments: OFF
            m5 = p5.match(line)
            if m5 and current_interface:
                result['interfaces'][current_interface]['drop_fragments'] = m5.group('drop_fragments')
                continue

            # IPv6 current reassembly count:0
            m6 = p6.match(line)
            if m6 and current_interface:
                result['interfaces'][current_interface]['current_reassembly_count'] = int(m6.group('current_reassembly'))
                continue

            # IPv6 current fragment count:0
            m7 = p7.match(line)
            if m7 and current_interface:
                result['interfaces'][current_interface]['current_fragment_count'] = int(m7.group('current_fragment'))
                continue

            # IPv6 total reassembly count:0
            m8 = p8.match(line)
            if m8 and current_interface:
                result['interfaces'][current_interface]['total_reassembly_count'] = int(m8.group('total_reassembly'))
                continue

            # IPv6 total reassembly timeout count:0
            m9 = p9.match(line)
            if m9 and current_interface:
                result['interfaces'][current_interface]['total_reassembly_timeout_count'] = int(m9.group('total_timeout'))
                continue

        return result
