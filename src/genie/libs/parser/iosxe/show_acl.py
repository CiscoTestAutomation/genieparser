"""show_acl.py
   supported commands:
     *  show access-lists
"""

# Python
import re
import random

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Schema,
                                                Any,
                                                Optional,
                                                Or,
                                                And,
                                                Default,
                                                Use)

# import parser utils
from genie.libs.parser.utils.common import Common


class ShowAccessListsSchema(MetaParser):
    """Schema for show access-lists
                  show access-lists <acl>
                  show ip access-lists
                  show ip access-lists <acl>
                  show ipv6 access-list
                  show ipv6 access-list <acl>"""
    schema = {
        Any():{
            'name': str,
            'type': str,
            'acl_type': str, # 'standard', 'extended' or 'ipv6'
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
                                Optional('destination_network'): {
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
                                },
                                Optional('msg_type'): str,
                            }
                        },
                    },
                    'actions': {
                        'forwarding': str,
                        Optional('logging'): str,
                    },
                    Optional('statistics'): {
                        'matched_packets': Or(int,str)
                    }
                }
            }
        }
    }

class ShowAccessLists(ShowAccessListsSchema):
    """Parser for show access-lists
                  show access-lists <acl>"""

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

    cli_command = ['show access-lists',
                   'show access-lists {acl}']

    def cli(self, acl="", output=None):
        if output is None:
            if acl:
                cmd = self.cli_command[1].format(acl=acl)
            else:
                cmd = self.cli_command[0]
            # get output from device
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p_ip = re.compile(r'^(?P<acl_type>Extended|Standard) +IP +access +list[s]? '
                          r'+(?P<name>[\w\-\.#]+)( *\((?P<per_user>.*)\))?$')
        p_ip_1 = re.compile(r'^ip +access-list +extended +(?P<name>[\w\-'
                            r'\.#]+)( *\((?P<per_user>.*)\))?$')
        p_ipv6 = re.compile(r'^(?P<acl_type>IPv6) +access +list +(?P<name>[\w\-\.#]+)'
                            r'( *\((?P<per_user>.*)\))?.*$')
        p_mac = re.compile(r'^(?P<acl_type>Extended) +MAC +access +list +(?P<name>[\w\-\.'
                           r']+)( *\((?P<per_user>.*)\))?$')


        # 10 permit 10.2.0.0, wildcard bits 0.0.255.255
        # 20 permit 10.2.0.0
        # 20 deny   any
        # 10 permit 10.196.7.7
        # 30 deny   any
        # permit 172.20.10.10
        # permit 10.66.12.12
        # 10 permit 172.31.0.2 (1168716 matches)
        # 10 permit 172.31.0.0, wildcard bits 0.0.255.255 (8353358 matches)
        # 10 deny   10.4.1.2 log (18 matches)
        p_ip_acl_standard = re.compile(r'^(?P<seq>\d+)? '
                                       r'?(?P<actions_forwarding>permit|deny) '
                                       r'+(?P<src>\S+|any)( (?P<log>log))?(?:, +wildcard '
                                       r'+bits +(?P<wildcard_bits>any|\S+))'
                                       r'?(?: +\((?P<matched_packets>\d+|\S+)+ matches\))?$')

        # 10 permit ip host 10.3.3.3 host 10.5.5.34
        # 20 permit icmp any any
        # 30 permit ip host 10.34.2.2 host 10.2.54.2
        # 40 permit ip host 10.3.4.31 host 10.3.32.3 log
        # 30 deny tcp 10.55.0.0 0.0.0.255 192.168.220.0 0.0.0.255 eq www
        # 20 permit tcp host 10.16.2.2 eq www telnet 443 any precedence network ttl eq 255
        # 40 permit tcp any range ftp-data bgp any
        # 10 permit ip host 0.0.0.0 any
        # 20 permit ip 192.0.2.0 0.0.0.255 192.168.10.0 0.0.0.255
        # 30 deny tcp any any
        # 30 deny tcp 10.55.0.0 0.0.0.255 192.168.220.0 0.0.0.255 eq www
        # 10 permit ip any any(10031 matches)
        # 20 permit udp any host 10.4.1.1 eq 1985 (67 matches)
        # 10 permit tcp any any eq 443
        # 30 deny ip any any
        # 10 permit tcp 192.168.1.0 0.0.0.255 host 10.4.1.1 established log
        # 20 permit tcp host 10.16.2.2 eq www telnet 443 any precedence network ttl eq 255
        # 30 deny ip any any
        # 10 permit tcp any any eq www
        # 20 permit tcp any any eq 22
        # 30 permit icmp any any ttl-exceeded
        # 10 permit icmp any 10.120.194.64 0.0.0.63
        # 20 permit tcp any eq 443 10.120.194.64 0.0.0.63
        p_ip_acl = re.compile(
            r'^(?P<seq>\d+) +(?P<actions_forwarding>permit|deny) +(?P<protocol>\w+) '
            r'+(?P<src>(?:any|host +\d+.\d+.\d+.\d+|\d+.\d+.\d+.\d+ +\d+.\d+.\d+.\d+)?)'
            r'(?: +(?P<src_operator>eq|gt|lt|neq|range) '
            r'+(?P<src_port>.*?(?=(?: +any| +host +\d+.\d+.\d+.\d+| +\d+.\d+.\d+.\d+ +\d+.\d+.\d+.\d+)|$)))? '
            r'+(?P<dst>(?:any|host +\d+.\d+.\d+.\d+|\d+.\d+.\d+.\d+ +\d+.\d+.\d+.\d+)?)'
            r'(?: +(?P<dst_operator>eq|gt|lt|neq|range) +(?P<dst_port>(?:\S?)+\S))?(?: '
            r'+(?P<msg_type>ttl-exceeded|unreachable|packet-too-big|echo-reply|echo|'
            r'router-advertisement|mld-query+))?(?P<left>.+)?$')

        # permit tcp host 2001: DB8: 1: : 32 eq bgp host 2001: DB8: 2: : 32 eq 11000 sequence 1
        # permit tcp host 2001: DB8: 1: : 32 eq telnet host 2001: DB8: 2: : 32 eq 11001 sequence 2
        # permit ipv6 host 2001:: 1 host 2001: 1: : 2 sequence 20
        # permit tcp any eq www 8443 host 2001: 2001:db8:4:: 2 sequence 30
        # permit 2001:db8:9:9::3 2001:db8:10:10::4 2001:db8:1:1::1 2001:db8:24:24::6 log sequence 80
        # permit udp any any eq domain sequence 10
        # permit esp any any dscp cs7 log sequence 20
        # deny ipv6 any any sequence 30
        # permit ipv6 2001: DB8: : / 64 any sequence 10
        # permit esp host 2001: DB8: 5: : 1 any sequence 20
        # permit tcp host 2001: DB8: 1: : 1 eq www any eq bgp sequence 30
        # permit udp any host 2001: DB8: 1: : 1 sequence 40
        p_ipv6_acl = re.compile(
            r'^(?P<actions_forwarding>permit|deny) +(?P<protocol>ahp|esp|hbh'
            r'|icmp|ipv6|pcp|sctp|tcp|udp) +(?P<src>(?:any|(?:\w+)?(?::(?:\w+)?)'
            r'{2,7}(?:\/\d+)|(?:host|(?:\w+)?(?::(?:\w+)?){2,7}) '
            r'(?:\w+)?(?::(?:\w+)?){2,7}))(?: +(?P<src_operator>eq|gt|lt|neq|range)'
            r' +(?P<src_port>[\S ]+\S))? +(?P<dst>(?:any|(?:\w+)?(?::(?:\w+)?){2,7}(?:\/\d+)|'
            r'(?:host|(?:\w+)?(?::(?:\w+)?){2,7}) (?:\w+)?(?::(?:\w+)?){2,7}))(?: '
            r'+(?P<dst_operator>eq|gt|lt|neq|range) +(?P<dst_port>(?:\w+ ?)'
            r'+\w+))?(?: +(?P<msg_type>ttl-exceeded|unreachable|packet-too-big|echo-reply|echo|'
            r'router-advertisement|mld-query+))?(?P<left>.+)? +sequence +(?P<seq>\d+)$')

        p_mac_acl = re.compile(
            r'^(?P<actions_forwarding>(deny|permit)) +(?P<src>(host *)?[\w\.]+) '
            r'+(?P<dst>(host *)?[\w\.]+)( *(?P<left>.*))?$')
            
        # 70 permit ip object-group grt-interface-nets object-group grt-interface-nets
        # 90 permit esp object-group vpn-endpoints-dummydpd host 10.4.1.1 (14 matches)
        # 100 permit ahp object-group vpn-endpoints-dummydpd host 10.4.1.1
        # 110 permit udp object-group vpn-endpoints-dummydpd host 10.4.1.1 eq isakmp (122 matches)
        # 20 permit ip object-group GENIE any log-input
        # 10 deny ip any object-group GENIE log-input
        p_ip_object_group = re.compile(
            r'^(?P<seq>\d+) +(?P<actions_forwarding>permit|deny) +(?P<protocol>\w+) '
            r'+(?P<src>(?:any )?(?:object-group+)(?: '
            r'+\S+)?)(?: +(?P<src_operator>eq|gt|lt|neq|range) '
            r'+(?P<src_port>[\S ]+\S))? +(?P<dst>(?:host|object-group+)'
            r'(?: +\d+\.\d+\.\d+\.\d+)?(?: [a-zA-Z\-]*(?!.*[eq])+)?)?(?: +(?P<dst_operator>eq|gt|lt|neq|range) '
            r'+(?P<dst_port>(?:\S?)+))?(?: +(?P<msg_type>ttl-exceeded|unreachable|packet-too-big|echo-reply|echo|'
            r'router-advertisement|mld-query+))?(?P<left>.+)?$')

        for line in out.splitlines():
            line = line.strip()

            # Extended IP access list acl_name
            # Standard IP access list 1
            m_ip = p_ip.match(line)
            # ip access-list extended mylist2
            m_ip_1 = p_ip_1.match(line)
            # IPv6 access list preauth_v6 (per-user)
            m_ipv6 = p_ipv6.match(line)
            # Extended MAC access list mac_acl
            m_mac = p_mac.match(line)
            if m_ip or m_ip_1:
                if m_ip:
                    m = m_ip
                else:
                    m = m_ip_1
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
                acl_dict['acl_type'] = group['acl_type'].lower()
                acl_dict.setdefault('per_user', True) if group['per_user'] else None
                continue

            # permit 172.20.10.10
            # 10 permit 10.2.0.0, wildcard bits 0.0.255.255
            # 20 permit 10.2.0.0
            # 30 deny   any
            # 10 permit 172.31.0.2 (1168716 matches)
            # 10 permit 172.31.0.0, wildcard bits 0.0.255.255 (8353358 matches)
            m = p_ip_acl_standard.match(line)

            if m:
                group = m.groupdict()
                
                seq = group['seq']
                if seq == None:
                    seq = int(sorted(acl_dict.get('aces', {'0': 'dummy'}).keys())[-1]) + 10
                seq_dict = acl_dict.setdefault('aces', {}).setdefault(str(seq), {})
                seq_dict['name'] = str(seq)

                # store values
                actions_forwarding = group['actions_forwarding']
                src = group['src']
                protocol = 'ipv4'

                # actions
                seq_dict.setdefault('actions', {}).setdefault('forwarding', actions_forwarding)

                # l3 dict
                if group['wildcard_bits'] and 'wildcard_bits' in group:  
                    source_ipv4_network = group['src'] + ' ' + group['wildcard_bits']
                else:
                    if group['src'] == 'any':
                        source_ipv4_network = group['src']
                    else:
                        source_ipv4_network = group['src'] + ' ' + '0.0.0.0'

                if protocol is ('ipv4' or 'ipv6'):
                    protocol_name = protocol
                else:
                    if acl_dict['type'] == 'ipv6-acl-type':
                        protocol_name = 'ipv6'
                    else:
                        protocol_name = 'ipv4'

                l3_dict = seq_dict.setdefault('matches', {}).setdefault('l3', {}).setdefault(protocol_name, {})
                l3_dict['protocol'] = protocol
                l3_dict.setdefault('source_network', {}).setdefault(
                    source_ipv4_network, {}).setdefault('source_network', source_ipv4_network)

                if group['matched_packets']:
                    stats_dict = seq_dict.setdefault('statistics', {})
                    stats_dict.update(
                        {'matched_packets': group['matched_packets']})

                # Optional keys
                # actions
                log = group['log']
                seq_dict.setdefault('actions', {}) \
                    .setdefault('forwarding', actions_forwarding)

                if log:
                    seq_dict['actions']['logging'] = 'log-syslog'

                continue

            # 10 permit ip any any (10031 matches)
            # 10 permit tcp any any eq 443
            # 30 deny ip any any
            # 10 permit tcp 192.168.1.0 0.0.0.255 host 10.4.1.1 established log
            # 20 permit tcp host 10.16.2.2 eq www telnet 443 any precedence network ttl eq 255
            # 30 deny tcp 10.55.0.0 0.0.0.255 192.168.220.0 0.0.0.255 eq www
            # 40 permit tcp any range ftp-data bgp any
            m_v4 = p_ip_acl.match(line)

            # permit ipv6 host 2001::1 host 2001:1::2 sequence 20
            # permit udp any any eq domain sequence 10
            # permit esp any any dscp cs7 log sequence 60
            m_v6 = p_ipv6_acl.match(line)
            m_object_group = p_ip_object_group.match(line) 
            m = m_v4 if m_v4 else m_v6 if m_v6 else m_object_group
            if m:
                group = m.groupdict()
                seq_dict = acl_dict.setdefault('aces', {}).setdefault(group['seq'], {})
                seq_dict['name'] = group['seq']
                # store values
                protocol = group['protocol']
                protocol = 'ipv4' if protocol == 'ip' else protocol
                actions_forwarding = group['actions_forwarding']
                src = group['src'] if group['src'] else group['src1']
                dst = group.get('dst', None)
                src = src.strip()

                if dst:
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
                if ' matches' in left:
                    seq_dict.setdefault('statistics', {})\
                        .setdefault('matched_packets',
                            int(re.search('\((\d+) +matches\)', left).groups()[0]))

                # l3 dict
                if protocol is ('ipv4' or 'ipv6'):
                    protocol_name = protocol
                else:
                    if acl_dict['type'] == 'ipv6-acl-type':
                        protocol_name = 'ipv6'
                    else:
                        protocol_name = 'ipv4'

                l3_dict = seq_dict.setdefault('matches', {}).setdefault('l3', {})\
                    .setdefault(protocol_name, {})
                l3_dict['protocol'] = protocol
                l3_dict.setdefault('source_network', {})\
                    .setdefault(src, {}).setdefault('source_network', src)
                if dst:
                    l3_dict.setdefault('destination_network', {})\
                        .setdefault(dst, {}).setdefault('destination_network', dst)

                l3_dict.setdefault('dscp', re.search('dscp +(\w+)', left).groups()[0])\
                    if 'dscp' in left else None

                if 'ttl' in left:
                    ttl_group = re.search('ttl +(\w+) +(\d+)', left)
                    if ttl_group:
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
                    options_name = re.search('options +(\w+)', left).groups()[0]
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
                    
                if group['msg_type']:
                    l4_dict['msg_type'] = group['msg_type']
                    
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
                if group['dst_operator']:
                    dst_port = group['dst_port'].split()
                    if len(dst_port) == 1 and 'range' not in group:
                        val1 = group['dst_port']
                        if val1.isdigit():
                            val1 = int(val1)
                        else:
                            try:
                                val1 = self.OPER_MAP[val1]
                            except Exception:
                                pass
                        l4_dict_operator = l4_dict.setdefault('destination_port', {}).setdefault('operator', {})
                        l4_dst_dict = l4_dict_operator.setdefault('operator', group['dst_operator'])
                        l4_dict_port = l4_dict.setdefault('destination_port', {}).setdefault('operator', {})
                        l4_dict_port_val1 = l4_dict_port.setdefault('port', val1)

                    else:  
                        val1 = group['dst_port'].split()[0]
                        val2 = group['dst_port'].split()[1]
                        if '(' in val2:
                            val2 = val2.strip('(')
                        if val1.isdigit():
                            val1 = int(val1)
                        else:
                            try:
                                val1 = self.OPER_MAP[val1]
                            except Exception:
                                pass
                        if val2 and val2.isdigit():
                            val2 = int(val2)
                        elif val2:
                            try:
                                val2 = self.OPER_MAP[val2]
                            except Exception:
                                pass
                        
                        l4_dict_operator_lower = l4_dict.setdefault('destination_port', {}).setdefault('range', {})
                        l4_dst_dict_lower = l4_dict_operator_lower.setdefault('lower_port', val1)
                        l4_dict_port_upper = l4_dict.setdefault('destination_port', {}).setdefault('range', {})
                        l4_dst_dict_upper = l4_dict_port_upper.setdefault('upper_port', val2)

                # icmp type and code
                if protocol == 'icmp':
                    code_group = re.search(r'^(\d+) +(\d+)', left.strip())
                    if code_group:
                        l4_dict['type'] = int(code_group.groups()[0])
                        l4_dict['code'] = int(code_group.groups()[1])
                continue

            # deny   any any vlan 10
            # permit host aaaa.aaff.5555 host bbbb.bbff.7777 aarp
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


class ShowIpAccessLists(ShowAccessLists, ShowAccessListsSchema):
    """Parser for show ip access-lists
                  show ip access-lists <acl>"""

    cli_command = ['show ip access-lists',
                   'show ip access-lists {acl}']

    def cli(self, acl='', output=None):
        # Build command
        if output is None:
            if acl:
                cmd = self.cli_command[1].format(acl=acl)
            else:
                cmd = self.cli_command[0]
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        # Call super
        return super().cli(output=show_output)

class ShowIpv6AccessLists(ShowAccessLists, ShowAccessListsSchema):
    """Parser for show ipv6 access-lists
                  show ipv6 access-lists <acl>"""

    cli_command = ['show ipv6 access-list',
                   'show ipv6 access-list {acl}']

    def cli(self, acl='', output=None):
        # Build command
        if output is None:
            if acl:
                cmd = self.cli_command[1].format(acl=acl)
            else:
                cmd = self.cli_command[0]
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        # Call super
        return super().cli(output=show_output)
