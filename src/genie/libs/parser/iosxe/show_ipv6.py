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
    """Schema for show ipv6 routers"""
    schema = {
        'router': {
            Any(): {
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
# ================================================================
class ShowIpv6Routers(ShowIpv6RoutersSchema):
    """ Parser for:
                show ipv6 routers
    """

    cli_command = ['show ipv6 routers']

    def cli(self, output=None):
        """ cli for:
         ' show ipv6 routers '
        """

        if output is None:
            output = self.device.execute(self.cli_command)

        #Router FE80::FA7A:41FF:FE25:2502 on Vlan100, last update 0 min, CONFLICT
        p1 = re.compile(r'^Router +(?P<router_link_local_ip>\S+)\s+\w+\s+(?P<interface>\S+), +last +update +(?P<last_update>\d+) +min, +CONFLICT$')

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
            m = p1.match(line)
            if m:
                router_link_local = m.groupdict()['router_link_local_ip']
                router_dict = ret_dict.setdefault('router', {}).setdefault(router_link_local, {})
                router_dict.update({
                    'interface': m.groupdict()['interface'],
                    'last_update':int(m.groupdict()['last_update'])
                })
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
