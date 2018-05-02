"""show_acl.py
   supported commands:
     *  show access-lists
"""
# Python
import re
import random

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use

# import parser utils
from genie.libs.parser.utils.common import Common


class ShowAccessListsSchema(MetaParser):
    """Schema for show access-lists"""
    schema = {
        Any():{
            'name': str,
            'type': str,
            Optional('per_user'): bool,
            Optional('aces'): {
                Any(): {
                    'name': str,
                    'matches': {
                        Optional('l2'): {
                            'eth': {
                                'destination_mac_address': str,
                                'source_mac_address': str,
                                Optional('ether_type'): str,
                                Optional('cos'): int,
                                Optional('vlan'): int,
                                Optional('protocol_family'): str,
                                Optional('lsap'): str,
                            }
                        },
                        Optional('l3'): {
                            Any(): {   # protocols
                                Optional('dscp'): str,
                                Optional('ttl'): int,
                                Optional('ttl_operator'): str,
                                'protocol': str,
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
                                    Optional('range'): {
                                        'lower_port': int,
                                        'upper_port': int,
                                    },
                                    Optional('operator'): {
                                        'operator': str,
                                        'port': str,
                                    }
                                },
                                Optional('destination_port'): {
                                   Optional('range'): {
                                        'lower_port': int,
                                        'upper_port': int,
                                    },
                                    Optional('operator'): {
                                        'operator': str,                                        
                                        'port': int,
                                    }
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

class ShowAccessLists(ShowAccessListsSchema):
    """Parser for show access-lists"""
    OPT_MAP = {
        'add-ext':       147,
       'any-options':   random.randint(0, 255),
       'com-security':  134,
       'dps':           151,
       'encode':        15,
       'eool':          0,
       'ext-ip':        145,
       'ext-security':  133,
       'finn':          205,
       'imitd':         144,
       'lsr':           131,
       'mtup':          11,
       'mtur':          12,
       'no-op':         1,
       'nsapa':         150,
       'record-route':  7,
       'router-alert':  148,
       'sdb':           149,
       'security':      130,
       'ssr':           137,
       'stream-id':     136,
       'timestamp':     68,
       'traceroute':    82,
       'ump':           152,
       'visa':          142,
       'zsu':           10
    }
    PRECED_MAP = {
        5: 'critical',
        3: 'flash',
        4: 'flash-override',
        2: 'immediate',
        6: 'internet',
        7: 'network',
        1: 'priority',
        0: 'routine'
    }
    OPER_MAP = {
        'bgp':          179,
        'chargen':      19,
        'cmd':          514,
        'daytime':      13,
        'discard':      9,
        'domain':       53,
        'echo':         7,
        'exec':         512,
        'finger':       79,
        'ftp':          21,
        'ftp-data':     20,
        'gopher':       70,
        'hostname':     101,
        'ident':        113,
        'irc':          194,
        'klogin':       543,
        'kshell':       544,
        'login':        513,
        'lpd':          515,
        'msrpc':        135,
        'nntp':         119,
        'onep-plain':   15001,
        'onep-tls':     15002,
        'pim-auto-rp':  496,
        'pop2':         109,
        'pop3':         110,
        'smtp':         25,
        'sunrpc':       111,
        'syslog':       514,
        'tacacs':       49,
        'talk':         517,
        'telnet':       23,
        'time':         37,
        'uucp':         540,
        'whois':        43,
        'www':          80,
       'biff':           512,
       'bootpc':         68,
       'bootps':         67,
       'discard':        9,
       'dnsix':          195,
       'domain':         53,
       'echo':           7,
       'isakmp':         500,
       'mobile-ip':      434,
       'nameserver':     42,
       'netbios-dgm':    138,
       'netbios-ns':     137,
       'netbios-ss':     139,
       'non500-isakmp':  4500,
       'ntp':            123,
       'pim-auto-rp':    496,
       'rip':            520,
       'ripv6':          21,
       'snmp':           161,
       'snmptrap':       162,
       'sunrpc':         111,
       'syslog':         514,
       'tacacs':         49,
       'talk':           517,
       'tftp':           69,
       'time':           37,
       'who':            513,
       'xdmcp':          177
    }

    def cli(self):
         # get output from device
        out = self.device.execute('show access-lists')

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p_ip = re.compile(r'^Extended +IP +access +list +(?P<name>[\w\-\.]+)( *\((?P<per_user>.*)\))?$')
        p_ipv6 = re.compile(r'^IPv6 +access +list +(?P<name>[\w\-\.]+)( *\((?P<per_user>.*)\))?$')
        p_mac = re.compile(r'^Extended +MAC +access +list +(?P<name>[\w\-\.]+)( *\((?P<per_user>.*)\))?$')
        p_ip_acl = re.compile(
            r'^(?P<seq>\d+)? +(?P<actions_forwarding>(deny|permit)) +'
            '(?P<protocol>\w+) +(((?P<src1>host +(\d+.){3}\d+|any))|'
            '(?P<src>(((\d+.){3}\d+ +(\d+.){3}\d+)|any)))'
            '( *(?P<src_operator>(eq|gt|lt|neq|range)) +'
            '(?P<src_port>[\w\-\s]+))?'
            '(?P<dst>( *host)? +(any|((\d+.){3}\d+ +(\d+.){3}\d+)|'
            '(\d+.){3}\d+))( *(?P<left>.*))?$')
        p_ipv6_acl = re.compile(
            r'^(?P<actions_forwarding>(deny|permit)) +'
            '(?P<protocol>(ahp|esp|hbh|icmp|ipv6|pcp|sctp|tcp|udp))'
            ' +(((?P<src1>host +[\w\:]+|any))|'
            '(?P<src>(any|([\w\:]+ +[\w\:]+))))'
            '( *(?P<src_operator>(eq|gt|lt|neq|range)) +(?P<src_port>[\w\-\s]+))?'
            '( +(((?P<dst1>host +[\w\:]+|any))|'
            '(?P<dst>any|([\w\:]+ +[\w\:]+))))( *(?P<left>.*))?'
            ' +sequence +(?P<seq>\d+)$')
        p_mac_acl = re.compile(
            r'^(?P<actions_forwarding>(deny|permit)) +'
            '(?P<src>(host *)?[\w\.]+) +(?P<dst>(host *)?[\w\.]+)( *(?P<left>.*))?$')

        for line in out.splitlines():
            line = line.strip()
            
            # Extended IP access list acl_name
            m_ip = p_ip.match(line)
            # IPv6 access list preauth_v6 (per-user)
            m_ipv6 = p_ipv6.match(line)
            # Extended MAC access list mac_acl 
            m_mac = p_mac.match(line)
            if m_ip:
                m = m_ip
                acl_type = 'ipv4-acl-type'
            elif m_ipv6:
                m = m_ipv6
                acl_type = 'ipv6-acl-type'
            elif m_mac:
                m = m_mac
                acl_type = 'eth-acl-type'
            else:
                m = None

            if m:
                group = m.groupdict()
                acl_dict = ret_dict.setdefault(group['name'], {})
                acl_dict['name'] = group['name']
                acl_dict['type'] = acl_type
                acl_dict.setdefault('per_user', True) if group['per_user'] else None
                continue

            # 10 permit ip any any (10031 matches)
            # 10 permit tcp any any eq 443
            # 30 deny ip any any
            # 10 permit tcp 192.168.1.0 0.0.0.255 host 1.1.1.1 established log
            # 20 permit tcp host 2.2.2.2 eq www telnet 443 any precedence network ttl eq 255
            m_v4 = p_ip_acl.match(line)

            # permit ipv6 host 2001::1 host 2001:1::2 sequence 20
            # permit udp any any eq domain sequence 10
            # permit esp any any dscp cs7 log sequence 60
            m_v6 = p_ipv6_acl.match(line)
            m = m_v4 if m_v4 else m_v6
            if m:
                group = m.groupdict()
                seq_dict = acl_dict.setdefault('aces', {}).setdefault(group['seq'], {})
                seq_dict['name'] = group['seq']
                # store values
                protocol = group['protocol']
                protocol = 'ipv4' if protocol == 'ip' else protocol
                actions_forwarding = group['actions_forwarding']
                src = group['src'] if group['src'] else group['src1']
                dst = group['dst']
                src = src.strip()
                if 'dst1' in group:
                    dst = dst if dst else group['dst1']
                dst = dst.strip()
                # optional keys
                src_operator = group['src_operator']
                src_port = group['src_port']
                left = str(group['left'])

                # actions
                seq_dict.setdefault('actions', {})\
                    .setdefault('forwarding', actions_forwarding)
                seq_dict['actions']['logging'] = 'log-syslog' if 'log' in left else 'log-none'

                # statistics
                if 'matches' in left:
                    seq_dict.setdefault('statistics', {})\
                        .setdefault('matched_packets',
                            int(re.search('\((\d+) +matches\)', left).groups()[0]))

                # l3 dict
                l3_dict = seq_dict.setdefault('matches', {}).setdefault('l3', {})\
                    .setdefault(protocol, {})
                l3_dict['protocol'] = protocol
                l3_dict.setdefault('source_network', {})\
                    .setdefault(src, {}).setdefault('source_network', src)
                l3_dict.setdefault('destination_network', {})\
                    .setdefault(dst, {}).setdefault('destination_network', dst)

                l3_dict.setdefault('dscp', re.search('dscp +(\w+)', left).groups()[0])\
                    if 'dscp' in left else None

                if 'ttl' in left:
                    ttl_group = re.search('ttl +(\w+) +(\d+)', left)
                    l3_dict['ttl_operator'] = ttl_group.groups()[0]
                    l3_dict['ttl'] = int(ttl_group.groups()[1])

                if 'precedence' in left:
                    prec = re.search('precedence +(\w+)', left).groups()[0]
                    if prec.isdigit():
                        l3_dict['precedence_code'] = int(prec)
                        try:
                            l3_dict['precedence'] = self.PRECED_MAP[prec]
                        except Exception:
                            pass
                    else:
                        l3_dict['precedence'] = prec

                # l4_dict
                l4_dict = seq_dict.setdefault('matches', {}).setdefault('l4', {})\
                    .setdefault(protocol, {})
                if 'options' in left:
                    options_name = re.sealrch('options +(\w+)', left).groups()[0]
                    if not options_name.isdigit():
                        try:
                            l4_dict['options'] = self.OPT_MAP[options_name]
                        except Exception:
                            pass
                        l4_dict['options_name'] = options_name
                    else:
                        l4_dict['options'] = options_name

                l4_dict['established'] = True \
                    if 'established' in left else False

                # source_port operator
                if src_port and src_operator:
                    if 'range' not in src_operator:
                        l4_dict.setdefault('source_port', {}).setdefault('operator', {})\
                            .setdefault('operator', src_operator)
                        l4_dict.setdefault('source_port', {}).setdefault('operator', {})\
                            .setdefault('port', src_port)
                    else:
                        lower_port = src_port.split()[0]
                        upper_port = src_port.split()[1]
                        if not lower_port.isdigit():
                            try:
                                lower_port = self.OPER_MAP[lower_port]
                            except Exception:
                                pass
                        else:
                            lower_port = int(lower_port)
                        if not upper_port.isdigit():
                            try:
                                upper_port = self.OPER_MAP[upper_port]
                            except Exception:
                                pass
                        else:
                            upper_port = int(upper_port)
                        l4_dict.setdefault('source_port', {}).setdefault('range', {})\
                            .setdefault('lower_port', lower_port)
                        l4_dict.setdefault('source_port', {}).setdefault('range', {})\
                            .setdefault('upper_port', upper_port)

                # destination_port operator
                dst_oper = re.search('^(eq|gt|lt|neq|range) +([\w\-]+)( +([\w\-]+))?', left)
                if dst_oper:
                    operator = dst_oper.groups()[0]
                    val1 = dst_oper.groups()[1]
                    if val1.isdigit():
                        val1 = int(val1)
                    else:
                        try:
                            val1 = self.OPER_MAP[val1]
                        except Exception:
                            pass
                    val2 = dst_oper.groups()[-1]
                    if val2 and val2.isdigit():
                        val2 = int(val2)
                    elif val2:
                        try:
                            val2 = self.OPER_MAP[val2]
                        except Exception:
                            pass
                    if 'range' not in operator:
                        l4_dict.setdefault('destination_port', {}).setdefault('operator', {})\
                            .setdefault('operator', operator)
                        l4_dict.setdefault('destination_port', {}).setdefault('operator', {})\
                            .setdefault('port', val1)
                    else:
                        l4_dict.setdefault('destination_port', {}).setdefault('range', {})\
                            .setdefault('lower_port', val1)
                        l4_dict.setdefault('destination_port', {}).setdefault('range', {})\
                            .setdefault('upper_port', val2)

                # icmp type and code
                if protocol == 'icmp':
                    code_group = re.search('^(\d+) +(\d+)', left)
                    if code_group:
                        l4_dict['type'] = int(code_group.groups()[0])
                        l4_dict['code'] = int(code_group.groups()[1])
                continue

            # deny   any any vlan 10
            # permit host aaaa.aaaa.aaaa host bbbb.bbbb.bbbb aarp
            m = p_mac_acl.match(line)
            if m:
                group = m.groupdict()
                seq = int(sorted(acl_dict.get('aces', {'0': 'dummy'}).keys())[-1]) + 10
                seq_dict = acl_dict.setdefault('aces', {}).setdefault(str(seq), {})
                seq_dict['name'] = str(seq)
                # store values
                actions_forwarding = group['actions_forwarding']
                src = group['src']
                dst = group['dst']
                src = src.strip()
                dst = dst.strip()
                left = str(group['left'])

                # actions
                seq_dict.setdefault('actions', {})\
                    .setdefault('forwarding', actions_forwarding)
                seq_dict['actions']['logging'] = 'log-syslog' if 'log' in left else 'log-none'

                # l2_dict
                l2_dict = seq_dict.setdefault('matches', {}).setdefault('l2', {})\
                    .setdefault('eth', {})
                l2_dict['destination_mac_address'] = dst
                l2_dict['source_mac_address'] = src

                if 'cos' in left:
                    l2_dict.setdefault('cos',
                            int(re.search('cos +(\d+)', left).groups()[0]))
                    # remove the cos from left
                    left = re.sub('cos +\d+', '', left)

                if 'vlan' in left:
                    l2_dict.setdefault('vlan',
                            int(re.search('vlan +(\d+)', left).groups()[0]))
                    # remove the vlan from left
                    left = re.sub('vlan +\d+', '', left)

                if 'protocol-family' in left:
                    l2_dict.setdefault('protocol_family',
                            re.search('protocol\-family +(\w+)', left).groups()[0])
                    # remove the protocol-family from left
                    left = re.sub('protocol\-family +\w+', '', left)

                if 'lsap' in left:
                    l2_dict.setdefault('lsap',
                            re.search('lsap +(\w+ +\w+)', left).groups()[0])
                    # remove the lsap from left
                    left = re.sub('lsap +\w+ +\w+', '', left)
                left = left.strip()
                if left:
                    l2_dict['ether_type'] = left

        return ret_dict
