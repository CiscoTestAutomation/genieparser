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
                     '(?P<multicast_group>[\w\:\.\/]+)\)'
                     ' +RPF nbr: (?P<RPF_nbr>[\w\:\.\/]+)'
                     '\s+Flags\:(?P<mrib_flags>[\w\s]+|$)')

        # GigabitEthernet2/0/6 Flags: A NS 
        # Tunnel1 Flags: A NS  		 
        p2 = re.compile(r'^(?P<ingress_if>[\w\.\/\, ]+)'
                         '\s+Flags\: +(?P<ingress_flags>A[\s\w]+|[\s\w]+ +A[\s\w]+|A$)') 
						 
        #  LISP0.1 Flags: F NS  Next-hop: 100.154.154.154
        #  LISP0.1 Flags: F NS   Next-hop: (100.11.11.11, 235.1.3.167)
        p3 = re.compile(r'^(?P<egress_if>[\w\.\/\,]+)'
                        '\s+Flags\:\s+(?P<egress_flags>F[\s\w]+)+Next-hop\:\s+(?P<egress_next_hop>([\w\:\.\*\/]+)|(\([\w\:\.\*\/]+\, +[\w\:\.\*\/]+\)))')

        #  Vlan2006 Flags: F LI NS
        p4=re.compile(r'^(?P<egress_if>[\w\.\/\, ]+)'
                        '\s+Flags\: +(?P<egress_flags>F[\s\w]+)')            

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
                        {'multicast_group':
                            {Any():
                                {'source_address':
                                    {Any():
                                       {
                                            Optional('oif_ic_count'): int,
                                            Optional('oif_a_count'): int,
                                            Optional('flags'): str,
                                            Optional('sw_packet_count'): int,
                                            Optional('sw_packets_per_second'): int,
                                            Optional('sw_average_packet_size'): int,
                                            Optional('sw_kbits_per_second'): int,
                                            Optional('sw_total'): int,
                                            Optional('sw_rpf_failed'): int,
                                            Optional('sw_other_drops'): int,
                                            Optional('hw_packet_count'): int,
                                            Optional('hw_packets_per_second'): int,
                                            Optional('hw_average_packet_size'): int,
                                            Optional('hw_kbits_per_second'): int,
                                            Optional('hw_total'): int,
                                            Optional('hw_rpf_failed'): int,
                                            Optional('hw_other_drops'): int,
                                            'incoming_interfaces':
                                                {Any():
                                                    {
                                                     'ingress_flags': str,
                                                    }
                                                },
                                            Optional('outgoing_interfaces'):
                                                {Any():
                                                    {
                                                     Optional('egress_flags'): str,
                                                     Optional('egress_rloc'): str,
                                                     Optional('egress_underlay_mcast'): str,
                                                     Optional('egress_adj_mac'): str,
                                                     Optional('egress_hw_pkt_count'): int,
                                                     Optional('egress_fs_pkt_count'): int,
                                                     Optional('egress_ps_pkt_count'): int,
                                                     Optional('egress_pkt_rate'): int,
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
        #Default
        #VRF vrf1
        p1 = re.compile(r'^(VRF\s+)?(?P<vrf>[\w]+)$')

        #  (*,225.1.1.1) Flags: C HW
        # (70.1.1.10,225.1.1.1) Flags: HW
        #  (*,FF05:1:1::1) Flags: C HW
        # (2001:70:1:1::10,FF05:1:1::1) Flags: HW
        p3 = re.compile(r'^\((?P<source_address>[\w\:\.\*\/]+)\,'
                     '(?P<multicast_group>[\w\:\.\/]+)\)'
                     '\s+Flags\:\s+(?P<mfib_flags>[\w\s]+)$')
        #0x1AF0  OIF-IC count: 0, OIF-A count: 1
        p4 = re.compile(r'\w+ +OIF-IC count: +(?P<oif_ic_count>[\w]+)'
                   '\, +OIF-A count: +(?P<oif_a_count>[\w]+)$')
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

        p7 = re.compile(r'^(?P<ingress_if>[\w\.\/\, ]+)'
                         ' +Flags\: +(?P<ingress_flags>A[\s\w]+|[\s\w]+ +A[\s\w]+|A$)')

        #Vlan2001 Flags: F NS
        #LISP0.1, (100.11.11.11, 235.1.3.167) Flags:
        p8 = re.compile(r'^(?P<egress_if>[\w\.\/]+)'
                        '(\,\s+\(?(?P<egress_rloc>[\w\.]+)(\,\s+)?(?P<egress_underlay_mcast>[\w\.]+)?\)?)?'
						'\s+Flags\:\s?(?P<egress_flags>F[\s\w]+|[\s\w]+\s+F[\s\w]+|F$|[\s\w]+\s+F$|$)')

        #CEF: Adjacency with MAC: 01005E010101000A000120010800
        p9_1 = re.compile(r'^CEF\: +(?P<egress_adj_mac>[\w \:\(\)\.]+)$')
        #CEF: Special OCE (discard)
        p9_2 = re.compile(r'^CEF\: +(?P<egress_adj_mac>[\w \(\.\)]+)$')
        #Pkts: 0/0/2    Rate: 0 pps
        p10 = re.compile(r'^Pkts\:\s+(?P<egress_hw_pkt_count>[\w]+)\/'
                         '(?P<egress_fs_pkt_count>[\w]+)\/'
                         '(?P<egress_ps_pkt_count>[\w]+)'
                         '\s+Rate\:\s+(?P<egress_pkt_rate>[\w]+)\s+pps$')

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
                continue


            #Vlan2001 Flags: F NS
            #LISP0.1, (100.11.11.11, 235.1.3.167) Flags:
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
                egress_data['egress_flags'] = group['egress_flags']
                if group['egress_underlay_mcast']:
                    egress_data['egress_underlay_mcast'] = group['egress_underlay_mcast']

                continue
            #CEF: Adjacency with MAC: 01005E010101000A000120010800
            m=p9_1.match(line)
            if m:
                group = m.groupdict()                 
                egress_data['egress_adj_mac'] = group['egress_adj_mac']
                continue
            #CEF: Special OCE (discard)
            m=p9_2.match(line)
            if m:
                group = m.groupdict()
                egress_data['egress_adj_mac'] = group['egress_adj_mac']
                continue
            #Pkts: 0/0/2    Rate: 0 pps
            m=p10.match(line)
            if m:
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
                                'preferred_lifetime': int,
                                'valid_lifetime': int,
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
                },
                Optional('ia_pd'): {
                    Any(): { # 0x00100001
                        'ia_id': str,
                        't1': int,
                        't2': int,
                        'prefix': {
                            Any(): { # 2001:4::/48
                                'preferred_lifetime': int,
                                'valid_lifetime': int,
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
        p8 = re.compile(r'^preferred lifetime\s+(?P<preferred_lifetime>\d+),\s+valid lifetime\s+(?P<valid_lifetime>\S+)$')

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
                address_dict.update({
                    'preferred_lifetime' : int(groups['preferred_lifetime']),
                    'valid_lifetime' : int(groups['valid_lifetime'])})
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
