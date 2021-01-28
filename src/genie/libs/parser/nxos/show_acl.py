"""
show_acl.py

NXOS parsers for the following show commands:
    * show access-lists
    * show access-list <acl>
    * show access-lists summary
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# parser utils
from genie.libs.parser.utils.common import Common

# =======================================
# Schema for 'show access-lists'
# =======================================


class ShowAccessListsSchema(MetaParser):
    """ Schema for:
        'show access-lists'
    """
    schema = {
        Any(): {
            'name': str,
            'type': str,
            Optional('aces'): {
                Any(): {
                    'name': str,
                    'matches': {
                        Optional('l2'): {
                            'eth': {
                                'destination_mac_address': str,
                                'source_mac_address': str,
                                Optional('ether_type'): str,
                                Optional('vlan'): int,
                                Optional('mac_protocol_number'): str,
                            }
                        },
                        Optional('l3'): {
                            Any(): {   # protocols
                                'protocol': str,
                                Optional('ttl'): int,
                                Optional('ttl_operator'): str,
                                Optional('precedence'): str,
                                Optional('precedence_code'): int,
                                'destination_network': {
                                    Any(): {
                                        'destination_network': str,
                                    }
                                },
                                'source_network': {
                                    Any(): {
                                        'source_network': str,
                                    }
                                }
                            },
                        },
                        Optional('l4'): {
                            Any(): {   # protocols
                                Optional('type'): int,
                                Optional('code'): int,
                                Optional('acknowledgement_number'): int,
                                Optional('data_offset'): int,
                                Optional('reserved'): int,
                                Optional('flags'): str,
                                Optional('window_size'): int,
                                Optional('urgent_pointer'): int,
                                Optional('options'): int,
                                Optional('options_name'): str,
                                Optional('established'): bool,
                                Optional('source_port'): {
                                    Optional('operator'): {
                                        'operator': str,
                                        'port': str,
                                    },
                                    Optional('range'): {
                                        'lower_port': int,
                                        'upper_port': int,
                                    },
                                },
                                Optional('destination_port'): {
                                    Optional('operator'): {
                                        'operator': str,
                                        'port': str,
                                    },
                                    Optional('range'): {
                                        'lower_port': int,
                                        'upper_port': int,
                                    },
                                }
                            }
                        },
                    },
                    'actions': {
                        'forwarding': str,
                        Optional('logging'): str,
                    },
                    Optional('statistics'): {
                        'matched_packets': int,
                    }
                }
            }
        }
    }


# =======================================
# Parser for 'show access-lists'
# =======================================

class ShowAccessLists(ShowAccessListsSchema):
    """ Parser for
        'show access-lists'
        'show access-lists {acl}'
    """
    cli_command = ['show access-lists',
                   'show access-lists {acl}']

    def cli(self, acl="", output=None):
        if output is None:
            if acl:
                cmd = self.cli_command[1].format(acl=acl)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # IP access list acl_name
        # IP access list test22
        # IP access list NTP-ACL
        # IPV4 ACL 1
        p1_ip = re.compile(r'^((IP +access +list)|(IPV4 +ACL)) +(?P<name>\S+)$')

        # IPv6 access list ipv6_acl
        p1_ipv6 = re.compile(r'^IPv6 +access +list +(?P<name>\S+)$')

        # MAC access list mac_acl
        p1_mac = re.compile(r'^MAC +access +list +(?P<name>\S+)$')

        # --- IP access list ---
        # 10 permit ip any any
        # 10 permit tcp any any eq www
        # 20 permit tcp any any eq 22
        # 10 permit tcp 192.168.1.0 0.0.0.255 10.4.1.1/32 established log
        # 20 permit tcp 10.16.2.2/32 eq www any precedence network ttl 255
        # 30 deny ip any any
        # 10 permit ip 10.1.50.64/32 any [match=0]
        # 40 permit ip any any [match=4]

        # --- IPv6 access list ---
        # 10 permit ipv6 any any log
        # 20 permit ipv6 2001::1/128 2001:1::2/128
        # 30 permit tcp any eq 8443 2001:2::2/128
        # 10 permit udp any any
        p2_ip = re.compile(r'^(?P<seq>\S+) +(?P<actions_forwarding>permit|deny)'
                           r' +(?P<protocol>(?:ip|tcp|ipv6|udp)+) +(?P<source_network>(?:any|host|[\d.]+|[\d:.]+(?:\/\d+)?)?'
                           r'(?: [\d.]+)?)(?:( +(?P<src_operator>eq|gt|lt|neq|range)'
                           r' +(?P<src_port>[a-z\d ]{1,20})))? +(?P<destination_network>(?:any|host|[\d:.]+(?:\/\d+)?)'
                           r'(?: +[\d.]+)?)(?: +(?P<dst_operator>eq|gt|lt|neq|range)'
                           r' +(?P<dst_port>(?:\S ?)+\S))?(?P<established_log> +established +log)?'
                           r'(?: +precedence +(?P<precedence>network) +ttl +(?P<ttl>\d+))?'
                           r'(?: +\[match=(?P<match>\d+)\])?(?: +(?P<logging>log))?$')

        # --- MAC access list ---
        # 10 permit aaaa.bbff.8888 0000.0000.0000 bbbb.ccff.aaaa bbbb.ccff.aaaa aarp
        # 20 permit 0000.0000.0000 0000.0000.0000 any
        # 30 deny 0000.0000.0000 0000.0000.0000 aaaa.bbff.8888 0000.0000.0000 0x8041
        # 40 deny any any vlan 10
        # 50 permit aaaa.aaff.5555 ffff.ffff.0000 any aarp
        p2_mac = re.compile(r'^(?P<seq>\S+) +(?P<actions_forwarding>permit|deny) '
                            r'+(?P<source_mac_address>any|host|[\w]{4}.[\w]{4}.[\w]{4}'
                            r'(?: [\w]{4}.[\w]{4}.[\w]{4})?) '
                            r'+(?P<destination_mac_address>(?:any|host|[\w.]+|[\d.]+)(?: +[\w]{4}.[\w]{4}.[\w]{4})?)'
                            r'(?: +any)?(?: +(?P<ether_type>aarp))?(?: +vlan +(?P<vlan>\d+))?'
                            r'(?: (?P<mac_protocol_number>\w+))?$')

        result_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # IP access list acl_name
            # IP access list test22
            # IP access list NTP-ACL
            # IPV4 ACL 1
            m_ip = p1_ip.match(line)

            # IPv6 access list ipv6_acl
            m_ipv6 = p1_ipv6.match(line)

            # MAC access list mac_acl
            m_mac = p1_mac.match(line)

            if m_ip or m_ipv6 or m_mac:
                # 'type': type, # Conf/Ops Enum('ipv4-acl-type','ipv6-acl-type','eth-acl-type',
                # 'mixed-eth-ipv4-acl-type','mixed-eth-ipv6-acl-type','mixed-eth-ipv4-ipv6-acl-type')
                if m_ip:
                    group = m_ip.groupdict()
                    acl_type = 'ipv4-acl-type'
                elif m_ipv6:
                    group = m_ipv6.groupdict()
                    acl_type = 'ipv6-acl-type'
                else:
                    group = m_mac.groupdict()
                    acl_type = 'eth-acl-type'
                acl_dict = result_dict.setdefault(group['name'], {})
                acl_dict['name'] = group['name']
                acl_dict['type'] = acl_type

                continue

            # --- IP access list ---
            # --- IPv6 access list ---
            m = p2_ip.match(line)
            if m:
                group = m.groupdict()
                seq = group['seq']
                actions_forwarding = group['actions_forwarding']
                protocol = group['protocol']
                src_operator = group['src_operator']
                src_port = group['src_port']
                dst_operator = group['dst_operator']
                dst_port = group['dst_port']
                established_log = group['established_log']
                logging = group['logging']

                seq_dict = acl_dict.setdefault('aces', {}).setdefault(seq, {})
                seq_dict['name'] = group['seq']

                seq_dict.setdefault('actions', {}).setdefault('forwarding', actions_forwarding)
                if logging:
                    seq_dict.setdefault('actions', {}).setdefault('logging', 'log-syslog')

                if group['match']:
                    seq_dict.setdefault('statistics', {}).\
                        setdefault('matched_packets', int(group['match']))

                # l3 dict
                matches_dict = seq_dict.setdefault('matches', {})
                if protocol is ('ipv4' or 'ipv6'):
                    protocol_name = protocol
                else:
                    if acl_dict['type'] == 'ipv6-acl-type':
                        protocol_name = 'ipv6'
                    else:
                        protocol_name = 'ipv4'

                l3_dict = matches_dict.setdefault('l3', {}).setdefault(protocol_name, {})
                for i in ['protocol', 'ttl', 'precedence']:
                    if group[i]:
                        l3_dict[i] = int(group[i]) if i == 'ttl' else group[i]

                for i in ['source_network', 'destination_network']:
                    l3_dict.setdefault(i, {}).setdefault(group[i], {}). \
                            setdefault(i, group[i])

                # l4 dict
                if src_port or dst_port:
                    l4_dict = matches_dict.setdefault('l4', {}).setdefault(protocol, {})
                    if src_port and src_operator:
                        src_port_operator_dict = l4_dict.setdefault('source_port', {}). \
                                                         setdefault('operator', {})
                        src_port_operator_dict['operator'] = src_operator
                        src_port_operator_dict['port'] = src_port

                    elif dst_port and dst_operator:
                        dst_port_operator_dict = l4_dict.setdefault('destination_port', {}). \
                                                         setdefault('operator', {})
                        dst_port_operator_dict['operator'] = dst_operator
                        dst_port_operator_dict['port'] = dst_port

                if established_log:
                    l4_dict = matches_dict.setdefault('l4', {}).setdefault(protocol, {})
                    l4_dict['established'] = True

                continue

            # --- MAC access list ---
            m = p2_mac.match(line)
            if m:
                group = m.groupdict()
                seq = group['seq']

                seq_dict = acl_dict.setdefault('aces', {}).setdefault(seq, {})
                seq_dict['name'] = group['seq']
                seq_dict.setdefault('actions', {}).setdefault('forwarding', group['actions_forwarding'])

                # l2 dict
                matches_dict = seq_dict.setdefault('matches', {})
                l2_dict = matches_dict.setdefault('l2', {}).setdefault('eth', {})
                for i in ['source_mac_address', 'destination_mac_address', 'ether_type', 'vlan', 'mac_protocol_number']:
                    if group[i]:
                        l2_dict[i] = int(group[i]) if i == 'vlan' else group[i]

                continue

        return result_dict

# =======================================
# Schema for 'show access-lists summary'
# =======================================


class ShowAccessListsSummarySchema(MetaParser):
    """ Schema for:
        'show access-lists summary'
    """
    schema = {
        'acl': {
          Any(): { # 'ipv4_acl'
              'total_aces_configured': int,
          }
        },
        'attachment_points': {
            Any(): { # 'Ethernet1/1'
                'interface_id': str, #'Ethernet1/1'
                Optional('ingress'): {
                    Any(): { # 'ipv4_acl'
                        'name': str, # 'ipv4_acl'
                        Optional('type'): str, # 'Router ACL'
                        'active': bool,
                        'total_aces_configured': int,
                    }
                },
                Optional('egress'): {
                    Any(): {
                        'name': str,
                        Optional('type'): str,
                        'active': bool,
                        'total_aces_configured': int,
                    }
                }
            },
        }
    }

# =======================================
# Parser for 'show access-lists summary'
# =======================================


class ShowAccessListsSummary(ShowAccessListsSummarySchema):
    """ Parser for
        'show access-lists summary'
    """
    cli_command = 'show access-lists summary'

    def cli(self, acl="", output=None):
        if output is None:
            cmd = self.cli_command
            out = self.device.execute(cmd)
        else:
            out = output

        # IPV4 ACL acl_name
        # IPV6 ACL ipv6_acl2
        # IPV6 ACL __urpf_v6_acl__
        p1 = re.compile(r'^(?P<type>[A-Z0-9]+) +ACL +(?P<name>\S+)$')

        stack = []
        stacks = []
        start_flag = 0
        result_dict = {}
        for line in out.splitlines():
            acl_dict = result_dict.setdefault('acl', {})
            att_dict = result_dict.setdefault('attachment_points', {})
            m = p1.match(line)
            if m:
                if start_flag == 0:
                    start_flag += 1
                else:
                    stacks.append('\n'.join(stack))
                    stack = []
                    start_flag = 1

            if start_flag == 1:
                stack.append(line)

        stacks.append('\n'.join(stack))

        p = re.compile(r'^(?P<ip>[A-Z0-9]+) +ACL +(?P<name>\S+)\n +Total +ACEs +Configured: +(?P<total_configured>\d+)\n +Configured +on +interfaces:\n(?: +(?P<interface>\S+) +- +(?P<traffic>egress|ingress)( +\((?P<type>[\w\s]+)\))?\n)? +(?P<active>Active) +on +interfaces:(?:\n +(?P<interface2>\S+) +- +(?P<traffic2>egress|ingress)( +\((?P<type2>[\w\s]+)\))?)?')

        for s in stacks:
            m = p.match(s)
            if m:
                group = m.groupdict()
                ip = group['ip']
                name = group['name']
                total_configured = int(group['total_configured'])
                if not group['interface'] and not group['interface2']:
                    acl_dict.setdefault(name, {}).setdefault('total_aces_configured', total_configured)
                else:
                    sub_att_dict = att_dict.setdefault(group['interface'], {})
                    sub_att_dict['interface_id'] = group['interface']
                    traffic_dict = sub_att_dict.setdefault(group['traffic'], {}).\
                                                setdefault(name, {})

                    traffic_dict['name'] = name
                    if group['type']:
                        traffic_dict['type'] = group['type']
                    if group['active'] == 'Active':
                        active = True
                    else:
                        active = False
                    traffic_dict['active'] = True
                    traffic_dict['total_aces_configured'] = total_configured

        return result_dict

