"""show_vpdn.py
IOSXE parsers for the following show commands:
    * 'show vpdn'
    * 'show vpdn tunnel'
    * 'show vpdn tunnel pptp all'
    * 'show vpdn tunnel all'
    * 'show vpdn group-select default'
    * 'show vpdn group-select summary'
    * 'show vpdn session all'
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, ListOf, Optional, Or, Use


class ShowVpdnSchema(MetaParser):
    ''' Schema for:
            show vpdn
            show vpdn tunnel
    '''
    schema = {
        Optional('total_tunnels'): int,
        Optional('total_sessions'): int,
        Optional('tunnels'):{
            Any(): {
                'loc_tun_id': int,
                'rem_tun_id': int,
                'remote_name': str,
                'state': str,
                'remote_ip': str,
                'session_count': int,
                'vpdn_group': str,
            },
        },
        Optional('sessions'): {
            Any(): {
                'local_id': int,
                'remote_id': int,
                'tunnel_id': int,
                'username':str,
                'intf': str,
                'state': str,
                'last_chg': str,
                'uniq_id': int
            },
        },
        Optional('no_active_tunn'): str
    }


class ShowVpdnSuperParser(ShowVpdnSchema):
    ''' Parser for:
            show vpdn
            show vpdn tunnel
    '''

    def cli(self, output=None):

        res_dict = {}
        tunnel_index, sesion_index = 1, 1

        # L2TP Tunnel and Session Information Total tunnels 1 sessions 1
        p1 = re.compile(r'L2TP Tunnel and Session Information Total '
                r'tunnels +(?P<total_tunnels>\d+) +sessions +(?P<total_sessions>\d+)')

        # 35231      38883      LAC           est    18.18.18.1      1     1
        p2 = re.compile(r'(?P<loc_tun_id>\d+) +(?P<rem_tun_id>\d+) +(?P<remote_name>\S+)'
                r' +(?P<state>\S+) +(?P<remote_ip>[\d\.]+) +(?P<session_count>\d+)'
                r' +(?P<vpdn_group>\S+)')

        # 57471      22313      35231      lns@cisco.com, Vi2.1 est    00:00:09 2
        p3 = re.compile(r'(?P<local_id>\d+) +(?P<remote_id>\d+) +(?P<tunnel_id>\d+)'
                r' +(?P<username>[a-z@\.]+), +(?P<intf>\S+) +(?P<state>[a-z]+) +(?P<last_chg>[\d:]+)'
                r' +(?P<uniq_id>\d+)')

        # %%No active L2TP tunnels
        p4 = re.compile(r'^\%\%(?P<no_active_tunn>\S+) active L2TP tunnels$')

        for line in output.splitlines():
            line = line.strip()

            # L2TP Tunnel and Session Information Total tunnels 1 sessions 1
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                res_dict['total_tunnels'] = int(groups['total_tunnels'])
                res_dict['total_sessions'] = int(groups['total_sessions'])
                continue

            # 35231      38883      LAC           est    18.18.18.1      1     1
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                res_dict.setdefault('tunnels', {})
                tunnel_dict = res_dict['tunnels'].setdefault(tunnel_index, {})
                tunnel_dict.update({
                    'loc_tun_id': int(groups['loc_tun_id']),
                    'rem_tun_id': int(groups['rem_tun_id']),
                    'remote_name': groups['remote_name'],
                    'state': groups['state'],
                    'remote_ip': groups['remote_ip'],
                    'session_count': int(groups['session_count']),
                    'vpdn_group': groups['vpdn_group']
                })
                tunnel_index +=1
                continue

            # 57471      22313      35231      lns@cisco.com, Vi2.1 est    00:00:09 2
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                res_dict.setdefault('sessions', {})
                session_dict = res_dict['sessions'].setdefault(sesion_index, {})
                session_dict.update({
                    'local_id' : int(groups['local_id']),
                    'remote_id' : int(groups['remote_id']),
                    'tunnel_id' : int(groups['tunnel_id']),
                    'username' : groups['username'],
                    'intf' : groups['intf'],
                    'state' : groups['state'],
                    'last_chg' : groups['last_chg'],
                    'uniq_id' : int(groups['uniq_id'])
                })
                sesion_index +=1
                continue

            # %%No active L2TP tunnels
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                res_dict['no_active_tunn'] = groups['no_active_tunn']
                return res_dict

        return res_dict


class ShowVpdn(ShowVpdnSuperParser):
    ''' Parser for:
            show vpdn
    '''
    cli_command = 'show vpdn'

    def cli(self,output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        return super().cli(output=output)


class ShowVpdnTunnel(ShowVpdnSuperParser):
    ''' Parser for:
            show vpdn tunnel
    '''
    cli_command = 'show vpdn tunnel'

    def cli(self,output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        return super().cli(output=output)


class ShowVpdnTunnelPptpAllSchema(MetaParser):
    """Schema for show vpdn tunnel pptp all"""
    schema = {
        'total_tunnels': int,
        'total_sessions': int,
        'tunnels': {
            int: {
                'active_sessions': int,
                'state': str,
                'time_since_change': str,
                'remote_tunnel_name': str,
                'remote_internet_address': {
                    'ip': str,
                    'port': int,
                },
                'local_tunnel_name': str,
                'local_internet_address': {
                    'ip': str,
                    'port': int,
                },
                'vpdn_group': str,
                'packets_sent': int,
                'packets_received': int,
                'bytes_sent': int,
                'bytes_received': int,
                'last_clearing': str,
            }
        }
    }


class ShowVpdnTunnelPptpAll(ShowVpdnTunnelPptpAllSchema):
    """Parser for show vpdn tunnel pptp all"""

    cli_command = 'show vpdn tunnel pptp all'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Regular expressions for parsing the output
        # Total tunnels 1 sessions 1
        p0 = re.compile(r'^PPTP Tunnel Information Total tunnels (?P<total_tunnels>\d+) sessions (?P<total_sessions>\d+)$')
        # Tunnel id 40512, 1 active sessions
        p1 = re.compile(r'^Tunnel id (?P<tunnel_id>\d+), (?P<active_sessions>\d+) active sessions$')
        # Tunnel state is wt-cnnct, time since change 00:00:10
        p2 = re.compile(r'^Tunnel state is (?P<state>\S+), time since change (?P<time_since_change>[\d:]+)$')
        # Remote tunnel name is 100.1.1.1
        p3 = re.compile(r'^Remote tunnel name is (?P<remote_tunnel_name>\S+)$')
        # Internet Address 100.1.1.1, port 1723
        p4 = re.compile(r'^Internet Address (?P<ip>\S+), port (?P<port>\d+)$')
        # Local tunnel name is PG2
        p5 = re.compile(r'^Local tunnel name is (?P<local_tunnel_name>\S+)$')
        # VPDN group: PPTP
        p6 = re.compile(r'^VPDN group: (?P<vpdn_group>\S+)$')
        # 0 packets sent, 0 received, 0 bytes sent, 0 received
        p7 = re.compile(r'^(?P<packets_sent>\d+) packets sent, (?P<packets_received>\d+) received, (?P<bytes_sent>\d+) bytes sent, (?P<bytes_received>\d+) received$')
        # Last clearing of "show vpdn" counters never
        p8 = re.compile(r'^Last clearing of "show vpdn" counters (?P<last_clearing>.+)$')

        current_tunnel_id = None

        for line in output.splitlines():
            line = line.strip()

            # Total tunnels 1 sessions 1
            match = p0.match(line)
            if match:
                parsed_dict['total_tunnels'] = int(match.group('total_tunnels'))
                parsed_dict['total_sessions'] = int(match.group('total_sessions'))
                continue

            # Tunnel id 40512, 1 active sessions
            match = p1.match(line)
            if match:
                current_tunnel_id = int(match.group('tunnel_id'))
                tunnel_dict = parsed_dict.setdefault('tunnels', {}).setdefault(current_tunnel_id, {})
                tunnel_dict['active_sessions'] = int(match.group('active_sessions'))
                continue

            # Tunnel state is wt-cnnct, time since change 00:00:10
            match = p2.match(line)
            if match and current_tunnel_id is not None:
                tunnel_dict['state'] = match.group('state')
                tunnel_dict['time_since_change'] = match.group('time_since_change')
                continue

            # Remote tunnel name is 100.1.1.1
            match = p3.match(line)
            if match and current_tunnel_id is not None:
                tunnel_dict['remote_tunnel_name'] = match.group('remote_tunnel_name')
                continue
               
            # Local tunnel name is PG2
            match = p5.match(line)
            if match and current_tunnel_id is not None:
                tunnel_dict['local_tunnel_name'] = match.group('local_tunnel_name')
                continue
               
            # Internet Address 100.1.1.1, port 1723
            match = p4.match(line)
            if match and current_tunnel_id is not None:
                ip_port_data = {
                    'ip': match.group('ip'),
                    'port': int(match.group('port'))
                }
                
                if 'local_tunnel_name' in tunnel_dict:
                    tunnel_dict.setdefault('local_internet_address', {}).update(ip_port_data)
                else:
                    # Do the same for 'remote_internet_address'
                    tunnel_dict.setdefault('remote_internet_address', {}).update(ip_port_data)
                continue  
            # VPDN group: PPTP
            match = p6.match(line)
            if match and current_tunnel_id is not None:
                tunnel_dict['vpdn_group'] = match.group('vpdn_group')
                continue

            # 0 packets sent, 0 received, 0 bytes sent, 0 received
            match = p7.match(line)
            if match and current_tunnel_id is not None:
                tunnel_dict['packets_sent'] = int(match.group('packets_sent'))
                tunnel_dict['packets_received'] = int(match.group('packets_received'))
                tunnel_dict['bytes_sent'] = int(match.group('bytes_sent'))
                tunnel_dict['bytes_received'] = int(match.group('bytes_received'))
                continue

            # Last clearing of "show vpdn" counters never
            match = p8.match(line)
            if match and current_tunnel_id is not None:
                tunnel_dict['last_clearing'] = match.group('last_clearing')
                continue

        return parsed_dict



class ShowVpdnTunnelAllSchema(MetaParser):
    """Schema for show vpdn tunnel all"""
    schema = {
        'l2tp': {
            'total_tunnels': int,
            'total_sessions': int,
            'tunnels': {
                Any(): {
                    'status': str,
                    'remote_id': int,
                    'active_sessions': int,
                    'initiated': str,
                    'state': str,
                    'time_since_change': str,
                    'transport': {
                        'protocol': str,
                        'protocol_num': int
                    },
                    'remote': {
                        'tunnel_name': str,
                        'ip': str,
                        'port': int
                    },
                    'local': {
                        'tunnel_name': str,
                        'ip': str,
                        'port': int
                    },
                    'l2tp_class': str,
                    'counters': {
                        'since_last_clear': {
                            'packets': {
                                'sent': int,
                                'received': int
                            },
                            'bytes': {
                                'sent': int,
                                'received': int
                            },
                            'last_clearing': str
                        },
                        'ignore_last_clear': {
                            'packets': {
                                'sent': int,
                                'received': int
                            },
                            'bytes': {
                                'sent': int,
                                'received': int
                            }
                        }
                    },
                    'control': {
                        'ns': int,
                        'nr': int,
                        'local_rws': int,
                        'local_rws_is_default': bool,
                        'remote_rws': int,
                        'in_use_remote_rws': int,
                        'congestion_control_enabled': bool,
                        'message_authentication_enabled': bool,
                        'zlb_acks_sent': int
                    },
                    'pmtu_checking_enabled': bool,
                    'retransmission_time': {
                        'current': int,
                        'max': int,
                        'units': str
                    },
                    'unsent_queue': {
                        'size': int,
                        'max': int
                    },
                    'resend_queue': {
                        'size': int,
                        'max': int
                    },
                    'total_resends': int,
                    'out_of_order': {
                        'dropped_pkts': int,
                        'reorder_pkts': int
                    },
                    'peer_auth_failures': int,
                    'no_session_pak_queue_check': {
                        'current': int,
                        'of': int
                    },
                    'retransmit_time_distribution': ListOf(int),
                    'vpdn_group': str
                }
            }
        }
    }


class ShowVpdnTunnelAll(ShowVpdnTunnelAllSchema):
    """Parser for show vpdn tunnel all"""

    cli_command = "show vpdn tunnel all"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        if not output:
            return ret_dict

        # Sample output 1 - active tunnel:
        p1 = re.compile(r'^Sample output 1 - active tunnel:$')
        # Sample output 2 - no tunnels:
        p2 = re.compile(r'^Sample output 2 - no tunnels:$')
        # Sample output 3 - multiple tunnels:
        p3 = re.compile(r'^Sample output 3 - multiple tunnels:$')
        # L2TP Tunnel Information Total tunnels 1 sessions 1
        p4 = re.compile(r'^L2TP Tunnel Information Total tunnels (?P<total_tunnels>\d+)\s+sessions\s+(?P<total_sessions>\d+)$')
        # Tunnel id 679 is up, remote id is 58433, 1 active sessions
        p5 = re.compile(r'^Tunnel id (?P<tunnel_id>\d+)\s+is\s+(?P<status>\S+),\s+remote id is\s+(?P<remote_id>\d+),\s+(?P<active_sessions>\d+)\s+active sessions$')
        # Remotely initiated tunnel
        p6 = re.compile(r'^Remotely initiated tunnel$')
        # Locally initiated tunnel
        p7 = re.compile(r'^Locally initiated tunnel$')
        # Tunnel state is established, time since change 00:00:07
        p8 = re.compile(r'^Tunnel state is (?P<state>\S+),\s+time since change\s+(?P<time_since_change>[\d:]+)$')
        # Tunnel transport is UDP (17)
        p9 = re.compile(r'^Tunnel transport is (?P<protocol>\S+)\s+\((?P<protocol_num>\d+)\)$')
        # Remote tunnel name is lac
        p10 = re.compile(r'^Remote tunnel name is (?P<tunnel_name>\S+)$')
        # Internet Address 80.1.1.1, port 1701
        p11 = re.compile(r'^Internet Address (?P<ip>\S+),\s+port\s+(?P<port>\d+)$')
        # Local tunnel name is lns
        p12 = re.compile(r'^Local tunnel name is (?P<tunnel_name>\S+)$')
        # L2TP class for tunnel is vg_ip2
        p13 = re.compile(r'^L2TP class for tunnel is (?P<l2tp_class>\S+)$')
        # Counters, taking last clear into account:
        p14 = re.compile(r'^Counters, taking last clear into account:$')
        # 4 packets sent, 0 received
        p15 = re.compile(r'^(?P<sent>\d+)\s+packets\s+sent,\s+(?P<received>\d+)\s+received$')
        # 50 bytes sent, 0 received
        p16 = re.compile(r'^(?P<sent>\d+)\s+bytes\s+sent,\s+(?P<received>\d+)\s+received$')
        # Last clearing of counters never
        p17 = re.compile(r'^Last clearing of counters\s+(?P<last_clearing>.+)$')
        # Counters, ignoring last clear:
        p18 = re.compile(r'^Counters, ignoring last clear:$')
        # Control Ns 2, Nr 4
        p19 = re.compile(r'^Control Ns\s+(?P<ns>\d+),\s+Nr\s+(?P<nr>\d+)$')
        # Local RWS 1024 (default), Remote RWS 1024
        p20 = re.compile(r'^Local RWS\s+(?P<local_rws>\d+)(?P<is_default>\s+\(default\))?,\s+Remote RWS\s+(?P<remote_rws>\d+)$')
        # In Use Remote RWS 10
        p21 = re.compile(r'^In Use Remote RWS\s+(?P<in_use_remote_rws>\d+)$')
        # Control channel Congestion Control is disabled
        p22 = re.compile(r'^Control channel Congestion Control is\s+(?P<state>\S+)$')
        # Tunnel PMTU checking disabled
        p23 = re.compile(r'^Tunnel PMTU checking\s+(?P<state>\S+)$')
        # Retransmission time 1, max 1 seconds
        p24 = re.compile(r'^Retransmission time\s+(?P<current>\d+),\s+max\s+(?P<max>\d+)\s+(?P<units>\S+)$')
        # Unsent queuesize 0, max 0
        p25 = re.compile(r'^Unsent queuesize\s+(?P<size>\d+),\s+max\s+(?P<max>\d+)$')
        # Resend queuesize 0, max 1
        p26 = re.compile(r'^Resend queuesize\s+(?P<size>\d+),\s+max\s+(?P<max>\d+)$')
        # Total resends 0, ZLB ACKs sent 3
        p27 = re.compile(r'^Total resends\s+(?P<resends>\d+),\s+ZLB ACKs sent\s+(?P<zlb>\d+)$')
        # Total out-of-order dropped pkts 0
        p28 = re.compile(r'^Total out-of-order dropped pkts\s+(?P<dropped>\d+)$')
        # Total out-of-order reorder pkts 0
        p29 = re.compile(r'^Total out-of-order reorder pkts\s+(?P<reorder>\d+)$')
        # Total peer authentication failures 0
        p30 = re.compile(r'^Total peer authentication failures\s+(?P<failures>\d+)$')
        # Current no session pak queue check 0 of 5
        p31 = re.compile(r'^Current no session pak queue check\s+(?P<current>\d+)\s+of\s+(?P<of>\d+)$')
        # Retransmit time distribution: 0 0 0 0 0 0 0 0 0
        p32 = re.compile(r'^Retransmit time distribution:\s+(?P<vals>(?:\d+\s*)+)$')
        # Control message authentication is disabled
        p33 = re.compile(r'^Control message authentication is\s+(?P<state>\S+)$')
        # VPDN group for tunnel is vg_ip2
        p34 = re.compile(r'^VPDN group for tunnel is\s+(?P<vpdn_group>\S+)$')

        inside_sample1 = False
        header_parsed = False
        current_tunnel_id = None
        last_section = None
        counters_section = None  # 'since' or 'ignore'
        tunnel_dict = None

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Sample output 1 - active tunnel:
            m = p1.match(line)
            if m:
                inside_sample1 = True
                continue

            # Sample output 2 - no tunnels:
            m = p2.match(line)
            if m and inside_sample1:
                # Stop parsing after sample 1
                break
            if m and not inside_sample1:
                continue

            # Sample output 3 - multiple tunnels:
            m = p3.match(line)
            if m and inside_sample1:
                # Stop parsing after sample 1
                break
            if m and not inside_sample1:
                continue

            # L2TP Tunnel Information Total tunnels 1 sessions 1
            m = p4.match(line)
            if m:
                if header_parsed:
                    break
                header_parsed = True
                l2tp_dict = ret_dict.setdefault('l2tp', {})
                l2tp_dict['total_tunnels'] = int(m.group('total_tunnels'))
                l2tp_dict['total_sessions'] = int(m.group('total_sessions'))
                continue

            # If we haven't started parsing sample 1 yet, skip other lines
            if not header_parsed:
                continue

            # Tunnel id 679 is up, remote id is 58433, 1 active sessions
            m = p5.match(line)
            if m:
                current_tunnel_id = m.group('tunnel_id')
                tunnels_dict = ret_dict.setdefault('l2tp', {}).setdefault('tunnels', {})
                tunnel_dict = tunnels_dict.setdefault(current_tunnel_id, {})
                tunnel_dict['status'] = m.group('status')
                tunnel_dict['remote_id'] = int(m.group('remote_id'))
                tunnel_dict['active_sessions'] = int(m.group('active_sessions'))
                continue

            # Remotely initiated tunnel
            m = p6.match(line)
            if m and tunnel_dict is not None:
                tunnel_dict['initiated'] = 'remote'
                continue

            # Locally initiated tunnel
            m = p7.match(line)
            if m and tunnel_dict is not None:
                tunnel_dict['initiated'] = 'local'
                continue

            # Tunnel state is established, time since change 00:00:07
            m = p8.match(line)
            if m and tunnel_dict is not None:
                tunnel_dict['state'] = m.group('state')
                tunnel_dict['time_since_change'] = m.group('time_since_change')
                continue

            # Tunnel transport is UDP (17)
            m = p9.match(line)
            if m and tunnel_dict is not None:
                transport_dict = tunnel_dict.setdefault('transport', {})
                transport_dict['protocol'] = m.group('protocol')
                transport_dict['protocol_num'] = int(m.group('protocol_num'))
                continue

            # Remote tunnel name is lac
            m = p10.match(line)
            if m and tunnel_dict is not None:
                remote_dict = tunnel_dict.setdefault('remote', {})
                remote_dict['tunnel_name'] = m.group('tunnel_name')
                last_section = 'remote'
                continue

            # Internet Address 80.1.1.1, port 1701
            m = p11.match(line)
            if m and tunnel_dict is not None:
                ip = m.group('ip')
                port = int(m.group('port'))
                if last_section == 'remote':
                    rdict = tunnel_dict.setdefault('remote', {})
                    rdict['ip'] = ip
                    rdict['port'] = port
                elif last_section == 'local':
                    ldict = tunnel_dict.setdefault('local', {})
                    ldict['ip'] = ip
                    ldict['port'] = port
                continue

            # Local tunnel name is lns
            m = p12.match(line)
            if m and tunnel_dict is not None:
                local_dict = tunnel_dict.setdefault('local', {})
                local_dict['tunnel_name'] = m.group('tunnel_name')
                last_section = 'local'
                continue

            # L2TP class for tunnel is vg_ip2
            m = p13.match(line)
            if m and tunnel_dict is not None:
                tunnel_dict['l2tp_class'] = m.group('l2tp_class')
                continue

            # Counters, taking last clear into account:
            m = p14.match(line)
            if m and tunnel_dict is not None:
                counters_section = 'since'
                tunnel_dict.setdefault('counters', {}).setdefault('since_last_clear', {})
                continue

            # 4 packets sent, 0 received
            m = p15.match(line)
            if m and tunnel_dict is not None and counters_section is not None:
                sent = int(m.group('sent'))
                received = int(m.group('received'))
                if counters_section == 'since':
                    since = tunnel_dict.setdefault('counters', {}).setdefault('since_last_clear', {})
                    packets = since.setdefault('packets', {})
                    packets['sent'] = sent
                    packets['received'] = received
                elif counters_section == 'ignore':
                    ignore = tunnel_dict.setdefault('counters', {}).setdefault('ignore_last_clear', {})
                    packets = ignore.setdefault('packets', {})
                    packets['sent'] = sent
                    packets['received'] = received
                continue

            # 50 bytes sent, 0 received
            m = p16.match(line)
            if m and tunnel_dict is not None and counters_section is not None:
                sent = int(m.group('sent'))
                received = int(m.group('received'))
                if counters_section == 'since':
                    since = tunnel_dict.setdefault('counters', {}).setdefault('since_last_clear', {})
                    bytes_dict = since.setdefault('bytes', {})
                    bytes_dict['sent'] = sent
                    bytes_dict['received'] = received
                elif counters_section == 'ignore':
                    ignore = tunnel_dict.setdefault('counters', {}).setdefault('ignore_last_clear', {})
                    bytes_dict = ignore.setdefault('bytes', {})
                    bytes_dict['sent'] = sent
                    bytes_dict['received'] = received
                continue

            # Last clearing of counters never
            m = p17.match(line)
            if m and tunnel_dict is not None and counters_section == 'since':
                since = tunnel_dict.setdefault('counters', {}).setdefault('since_last_clear', {})
                since['last_clearing'] = m.group('last_clearing')
                continue

            # Counters, ignoring last clear:
            m = p18.match(line)
            if m and tunnel_dict is not None:
                counters_section = 'ignore'
                tunnel_dict.setdefault('counters', {}).setdefault('ignore_last_clear', {})
                continue

            # Control Ns 2, Nr 4
            m = p19.match(line)
            if m and tunnel_dict is not None:
                control = tunnel_dict.setdefault('control', {})
                control['ns'] = int(m.group('ns'))
                control['nr'] = int(m.group('nr'))
                continue

            # Local RWS 1024 (default), Remote RWS 1024
            m = p20.match(line)
            if m and tunnel_dict is not None:
                control = tunnel_dict.setdefault('control', {})
                control['local_rws'] = int(m.group('local_rws'))
                control['local_rws_is_default'] = True if m.group('is_default') else False
                control['remote_rws'] = int(m.group('remote_rws'))
                continue

            # In Use Remote RWS 10
            m = p21.match(line)
            if m and tunnel_dict is not None:
                control = tunnel_dict.setdefault('control', {})
                control['in_use_remote_rws'] = int(m.group('in_use_remote_rws'))
                continue

            # Control channel Congestion Control is disabled
            m = p22.match(line)
            if m and tunnel_dict is not None:
                control = tunnel_dict.setdefault('control', {})
                control['congestion_control_enabled'] = True if m.group('state').lower() == 'enabled' else False
                continue

            # Tunnel PMTU checking disabled
            m = p23.match(line)
            if m and tunnel_dict is not None:
                tunnel_dict['pmtu_checking_enabled'] = True if m.group('state').lower() == 'enabled' else False
                continue

            # Retransmission time 1, max 1 seconds
            m = p24.match(line)
            if m and tunnel_dict is not None:
                rtx = tunnel_dict.setdefault('retransmission_time', {})
                rtx['current'] = int(m.group('current'))
                rtx['max'] = int(m.group('max'))
                rtx['units'] = m.group('units')
                continue

            # Unsent queuesize 0, max 0
            m = p25.match(line)
            if m and tunnel_dict is not None:
                uq = tunnel_dict.setdefault('unsent_queue', {})
                uq['size'] = int(m.group('size'))
                uq['max'] = int(m.group('max'))
                continue

            # Resend queuesize 0, max 1
            m = p26.match(line)
            if m and tunnel_dict is not None:
                rq = tunnel_dict.setdefault('resend_queue', {})
                rq['size'] = int(m.group('size'))
                rq['max'] = int(m.group('max'))
                continue

            # Total resends 0, ZLB ACKs sent 3
            m = p27.match(line)
            if m and tunnel_dict is not None:
                tunnel_dict['total_resends'] = int(m.group('resends'))
                control = tunnel_dict.setdefault('control', {})
                control['zlb_acks_sent'] = int(m.group('zlb'))
                continue

            # Total out-of-order dropped pkts 0
            m = p28.match(line)
            if m and tunnel_dict is not None:
                ooo = tunnel_dict.setdefault('out_of_order', {})
                ooo['dropped_pkts'] = int(m.group('dropped'))
                continue

            # Total out-of-order reorder pkts 0
            m = p29.match(line)
            if m and tunnel_dict is not None:
                ooo = tunnel_dict.setdefault('out_of_order', {})
                ooo['reorder_pkts'] = int(m.group('reorder'))
                continue

            # Total peer authentication failures 0
            m = p30.match(line)
            if m and tunnel_dict is not None:
                tunnel_dict['peer_auth_failures'] = int(m.group('failures'))
                continue

            # Current no session pak queue check 0 of 5
            m = p31.match(line)
            if m and tunnel_dict is not None:
                nspq = tunnel_dict.setdefault('no_session_pak_queue_check', {})
                nspq['current'] = int(m.group('current'))
                nspq['of'] = int(m.group('of'))
                continue

            # Retransmit time distribution: 0 0 0 0 0 0 0 0 0
            m = p32.match(line)
            if m and tunnel_dict is not None:
                vals = m.group('vals').split()
                tunnel_dict['retransmit_time_distribution'] = [int(v) for v in vals]
                continue

            # Control message authentication is disabled
            m = p33.match(line)
            if m and tunnel_dict is not None:
                control = tunnel_dict.setdefault('control', {})
                control['message_authentication_enabled'] = True if m.group('state').lower() == 'enabled' else False
                continue

            # VPDN group for tunnel is vg_ip2
            m = p34.match(line)
            if m and tunnel_dict is not None:
                tunnel_dict['vpdn_group'] = m.group('vpdn_group')
                continue

        return ret_dict


class ShowVpdnGroupSelectDefaultSchema(MetaParser):
    """Schema for show vpdn group-select default"""
    schema = {
        "vpdn": {
            "group_select": {
                "default": {
                    "default_group": str,
                    "current_default_group": str,
                    "state": str,
                    "group_info": {
                        Any(): {
                            "protocol": str,
                            "domain_handling": str,
                            "priority": int
                        }
                    },
                    "protocols": {
                        Any(): {
                            "default_group": Or(str, None)
                        }
                    }
                }
            }
        }
    }


class ShowVpdnGroupSelectDefault(ShowVpdnGroupSelectDefaultSchema):
    """Parser for show vpdn group-select default"""

    cli_command = "show vpdn group-select default"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        if not output:
            return ret_dict

        # Default VPDN group: L2TP_GROUP
        p1 = re.compile(r"^Default VPDN group\s*:\s*(?P<default_group>\S+)$")
        # Default VPDN group information:
        p2 = re.compile(r"^Default VPDN group information\s*:\s*$")
        # Group Name      : L2TP_GROUP
        p3 = re.compile(r"^Group Name\s*:\s*(?P<group_name>\S+)$")
        # Protocol        : l2tp
        p4 = re.compile(r"^Protocol\s*:\s*(?P<protocol>\S+)$")
        # Domain Handling : Enabled
        p5 = re.compile(r"^Domain Handling\s*:\s*(?P<domain_handling>\S+)$")
        # Priority        : 1
        p6 = re.compile(r"^Priority\s*:\s*(?P<priority>\d+)$")
        # VPDN Default Group Selection
        p7 = re.compile(r"^VPDN Default Group Selection$")
        # Current Default Group : DEFAULT_L2TP
        p8 = re.compile(r"^Current Default Group\s*:\s*(?P<current_default_group>\S+)$")
        # State                 : Active
        p9 = re.compile(r"^State\s*:\s*(?P<state>\S+)$")
        # Default VPDN Group      Protocol
        p10 = re.compile(r"^Default VPDN Group\s+Protocol$")
        # vgdefault               l2tp
        p11 = re.compile(r"^(?P<group>\S+)\s+(?P<protocol>\S+)$")

        default_dict = ret_dict.setdefault("vpdn", {}).setdefault("group_select", {}).setdefault("default", {})

        in_group_info = False
        in_groups_table = False
        current_group_info_key = None

        for raw_line in output.splitlines():
            line = raw_line.strip()
            if not line:
                if in_groups_table:
                    in_groups_table = False
                continue

            # Skip non-informational lines
            lower_line = line.lower()
            if lower_line.startswith("example"):
                continue
            if set(line) == set("-"):
                continue
            if lower_line.startswith("show vpdn"):
                continue

            # Default VPDN group: L2TP_GROUP
            m = p1.match(line)
            if m:
                default_dict["default_group"] = m.group("default_group")
                continue

            # Default VPDN group information:
            m = p2.match(line)
            if m:
                in_group_info = True
                current_group_info_key = None
                continue

            # Group Name      : L2TP_GROUP
            m = p3.match(line)
            if m and in_group_info:
                current_group_info_key = m.group("group_name")
                gi_dict = default_dict.setdefault("group_info", {})
                gi_dict.setdefault(current_group_info_key, {})
                continue

            # Protocol        : l2tp
            m = p4.match(line)
            if m and in_group_info and current_group_info_key:
                gi_entry = default_dict.setdefault("group_info", {}).setdefault(current_group_info_key, {})
                gi_entry["protocol"] = m.group("protocol")
                continue

            # Domain Handling : Enabled
            m = p5.match(line)
            if m and in_group_info and current_group_info_key:
                gi_entry = default_dict.setdefault("group_info", {}).setdefault(current_group_info_key, {})
                gi_entry["domain_handling"] = m.group("domain_handling").lower()
                continue

            # Priority        : 1
            m = p6.match(line)
            if m and in_group_info and current_group_info_key:
                gi_entry = default_dict.setdefault("group_info", {}).setdefault(current_group_info_key, {})
                gi_entry["priority"] = int(m.group("priority"))
                continue

            # VPDN Default Group Selection
            m = p7.match(line)
            if m:
                # Nothing to set here; next lines carry values
                continue

            # Current Default Group : DEFAULT_L2TP
            m = p8.match(line)
            if m:
                default_dict["current_default_group"] = m.group("current_default_group")
                continue

            # State                 : Active
            m = p9.match(line)
            if m:
                default_dict["state"] = m.group("state")
                continue

            # Default VPDN Group      Protocol
            m = p10.match(line)
            if m:
                in_groups_table = True
                continue

            # vgdefault               l2tp
            # None                    pptp
            m = p11.match(line)
            if m and in_groups_table:
                group_name = m.group("group")
                protocol = m.group("protocol")
                protocols_dict = default_dict.setdefault("protocols", {})
                protocol_entry = protocols_dict.setdefault(protocol, {})
                protocol_entry["default_group"] = None if group_name.lower() == "none" else group_name
                continue

        return ret_dict


class ShowVpdnSessionAllSchema(MetaParser):
    """Schema for show vpdn session all"""
    schema = {
        "vpdn": {
            "sessions": {
                Any(): {
                    "session_id": int,
                    "status": str,
                    "tunnel_id": int,
                    "call_serial_number": int,
                    "remote_tunnel_name": str,
                    "internet_address": str,
                    "session_state": str,
                    "time_since_change": str,
                    "packets": {
                        "sent": int,
                        "received": int
                    },
                    "bytes": {
                        "sent": int,
                        "received": int
                    },
                    "mtu": int,
                    "username": str,
                    "interface": Or(str, None),
                    "remote_session_id": int,
                    "remote_tunnel_id": int,
                    "udp_checksums": str,
                    "sss_switching": str,
                    "sequencing": str,
                    "unique_id": int
                }
            }
        }
    }


class ShowVpdnSessionAll(ShowVpdnSessionAllSchema):
    """Parser for show vpdn session all"""

    cli_command = "show vpdn session all"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # Session id 5 is up, tunnel id 13695
        p1 = re.compile(r"^Session id (?P<session_id>\d+) is (?P<status>\S+), tunnel id (?P<tunnel_id>\d+)$")
        # Call serial number is 3355500002
        p2 = re.compile(r"^Call serial number is (?P<csn>\d+)$")
        # Remote tunnel name is User03
        p3 = re.compile(r"^Remote tunnel name is (?P<rtn>\S+)$")
        #   Internet address is 10.0.0.63
        p4 = re.compile(r"^\s*Internet address is (?P<ip>\S+)$")
        #   Session state is established, time since change 00:03:53
        p5 = re.compile(r"^\s*Session state is (?P<session_state>\S+), time since change (?P<time_since_change>[\w:]+)$")
        #     52 Packets sent, 52 received
        p6 = re.compile(r"^\s*(?P<pkts_sent>\d+)\s+Packets sent, (?P<pkts_recv>\d+) received$")
        #     2080 Bytes sent, 1316 received
        p7 = re.compile(r"^\s*(?P<bytes_sent>\d+)\s+Bytes sent, (?P<bytes_recv>\d+) received$")
        #   Session MTU is 1464 bytes
        p8 = re.compile(r"^\s*Session MTU is (?P<mtu>\d+) bytes$")
        #   Session username is nobody@cisco.com
        p9 = re.compile(r"^\s*Session username is (?P<username>\S+)$")
        #     Interface
        p10 = re.compile(r"^\s*Interface$")
        #     Remote session id is 692, remote tunnel id 58582
        p11 = re.compile(r"^\s*Remote session id is (?P<rsid>\d+), remote tunnel id (?P<rtid>\d+)$")
        #   UDP checksums are disabled
        p12 = re.compile(r"^\s*UDP checksums are (?P<udp_state>\S+)$")
        #   SSS switching enabled
        p13 = re.compile(r"^\s*SSS switching (?P<sss_state>\S+)$")
        #   Sequencing is off
        p14 = re.compile(r"^\s*Sequencing is (?P<seq_state>\S+)$")
        #   Unique ID is 8
        p15 = re.compile(r"^\s*Unique ID is (?P<uid>\d+)$")

        sessions_dict = None
        current_session = None

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Session id 5 is up, tunnel id 13695
            m = p1.match(line)
            if m:
                sessions_dict = ret_dict.setdefault("vpdn", {}).setdefault("sessions", {})
                session_id_int = int(m.group("session_id"))
                session_key = str(session_id_int)
                current_session = sessions_dict.setdefault(session_key, {})
                current_session["session_id"] = session_id_int
                current_session["status"] = m.group("status")
                current_session["tunnel_id"] = int(m.group("tunnel_id"))
                continue

            if current_session is None:
                continue

            # Call serial number is 3355500002
            m = p2.match(line)
            if m:
                current_session["call_serial_number"] = int(m.group("csn"))
                continue

            # Remote tunnel name is User03
            m = p3.match(line)
            if m:
                current_session["remote_tunnel_name"] = m.group("rtn")
                continue

            #   Internet address is 10.0.0.63
            m = p4.match(line)
            if m:
                current_session["internet_address"] = m.group("ip")
                continue

            #   Session state is established, time since change 00:03:53
            m = p5.match(line)
            if m:
                current_session["session_state"] = m.group("session_state")
                current_session["time_since_change"] = m.group("time_since_change")
                continue

            #     52 Packets sent, 52 received
            m = p6.match(line)
            if m:
                pkt_dict = current_session.setdefault("packets", {})
                pkt_dict["sent"] = int(m.group("pkts_sent"))
                pkt_dict["received"] = int(m.group("pkts_recv"))
                continue

            #     2080 Bytes sent, 1316 received
            m = p7.match(line)
            if m:
                bytes_dict = current_session.setdefault("bytes", {})
                bytes_dict["sent"] = int(m.group("bytes_sent"))
                bytes_dict["received"] = int(m.group("bytes_recv"))
                continue

            #   Session MTU is 1464 bytes
            m = p8.match(line)
            if m:
                current_session["mtu"] = int(m.group("mtu"))
                continue

            #   Session username is nobody@cisco.com
            m = p9.match(line)
            if m:
                current_session["username"] = m.group("username")
                continue

            #     Interface
            m = p10.match(line)
            if m:
                current_session["interface"] = None
                continue

            #     Remote session id is 692, remote tunnel id 58582
            m = p11.match(line)
            if m:
                current_session["remote_session_id"] = int(m.group("rsid"))
                current_session["remote_tunnel_id"] = int(m.group("rtid"))
                continue

            #   UDP checksums are disabled
            m = p12.match(line)
            if m:
                current_session["udp_checksums"] = m.group("udp_state")
                continue

            #   SSS switching enabled
            m = p13.match(line)
            if m:
                current_session["sss_switching"] = m.group("sss_state")
                continue

            #   Sequencing is off
            m = p14.match(line)
            if m:
                current_session["sequencing"] = m.group("seq_state")
                continue

            #   Unique ID is 8
            m = p15.match(line)
            if m:
                current_session["unique_id"] = int(m.group("uid"))
                continue

        return ret_dict


class ShowVpdnSessionSchema(MetaParser):
    """Schema for show vpdn session"""
    schema = {
        "vpdn": {
            "l2tp": {
                "total_tunnels": str,
                "total_sessions": str,
                "sessions": ListOf({
                    "local_id": int,
                    "remote_id": int,
                    "tunnel_id": int,
                    "interface": str,
                    "username": str,
                    "state": str,
                    "last_change": str,
                    "unique_id": int,
                }),
            },
            "l2f": {
                "total_tunnels": str,
                "total_sessions": str,
                "sessions": ListOf({
                    "clid": int,
                    "mid": int,
                    "username": str,
                    "interface": str,
                    "state": str,
                    "unique_id": int,
                }),
            },
            "pppoe": {
                "total_tunnels": str,
                "total_sessions": str,
                "sessions": ListOf({
                    "uid": int,
                    "sid": int,
                    "remote_mac": str,
                    "local_mac": str,
                    "outgoing_interface": str,
                    "interface": str,
                    "vast": Or(str, None),
                    "session_state": str,
                }),
            },
        }
    }


class ShowVpdnSession(ShowVpdnSessionSchema):
    """Parser for show vpdn session"""

    cli_command = "show vpdn session"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        if not output:
            return ret_dict

        vpdn_dict = ret_dict.setdefault("vpdn", {})

        current_section = None
        last_pppoe_session = None

        # L2TP Session Information Total tunnels X sessions Y
        p1 = re.compile(r'^L2TP Session Information Total tunnels\s+(?P<total_tunnels>\S+)\s+sessions\s+(?P<total_sessions>\S+)$')
        # L2F Session Information Total tunnels X sessions Y
        p2 = re.compile(r'^L2F Session Information Total tunnels\s+(?P<total_tunnels>\S+)\s+sessions\s+(?P<total_sessions>\S+)$')
        # PPPoE Session Information Total tunnels X sessions Y
        p3 = re.compile(r'^PPPoE Session Information Total tunnels\s+(?P<total_tunnels>\S+)\s+sessions\s+(?P<total_sessions>\S+)$')
        # 4     691   13695 Se0/0         user@domain.com      est      00:06:00  4
        p4 = re.compile(r'^(?P<local_id>\d+)\s+(?P<remote_id>\d+)\s+(?P<tunnel_id>\d+)\s+(?P<interface>\S+)\s+(?P<username>\S+)\s+(?P<state>\S+)\s+(?P<last_change>[\d:]+)\s+(?P<unique_id>\d+)$')
        # 1      2      user@domain.com            SSS Circuit   open    10
        p5 = re.compile(r'^(?P<clid>\d+)\s+(?P<mid>\d+)\s+(?P<username>\S+)\s+(?P<interface>.+?)\s+(?P<state>\S+)\s+(?P<unique_id>\d+)$')
        # 3      1      0030.949b.b4a0 Fa2/0          N/A       CNCT_FWDED
        p6 = re.compile(r'^(?P<uid>\d+)\s+(?P<sid>\d+)\s+(?P<remote_mac>\S+)\s+(?P<outgoing_interface>\S+)\s+(?P<interface>\S+)\s+(?P<session_state>\S+)$')
        #               0010.7b90.0840
        p7 = re.compile(r'^\s+(?P<local_mac>[0-9a-fA-F.]+)(?:\s+(?P<vast>\S+))?$')

        for raw_line in output.splitlines():
            line = raw_line.rstrip()
            if not line:
                continue

            # L2TP Session Information Total tunnels X sessions Y
            m = p1.match(line)
            if m:
                current_section = "l2tp"
                sec = vpdn_dict.setdefault("l2tp", {})
                sec["total_tunnels"] = m.group("total_tunnels")
                sec["total_sessions"] = m.group("total_sessions")
                sec.setdefault("sessions", [])
                continue

            # L2F Session Information Total tunnels X sessions Y
            m = p2.match(line)
            if m:
                current_section = "l2f"
                sec = vpdn_dict.setdefault("l2f", {})
                sec["total_tunnels"] = m.group("total_tunnels")
                sec["total_sessions"] = m.group("total_sessions")
                sec.setdefault("sessions", [])
                continue

            # PPPoE Session Information Total tunnels X sessions Y
            m = p3.match(line)
            if m:
                current_section = "pppoe"
                sec = vpdn_dict.setdefault("pppoe", {})
                sec["total_tunnels"] = m.group("total_tunnels")
                sec["total_sessions"] = m.group("total_sessions")
                sec.setdefault("sessions", [])
                continue

            # 4     691   13695 Se0/0         user@domain.com      est      00:06:00  4
            m = p4.match(line)
            if m and current_section == "l2tp":
                sessions = vpdn_dict.setdefault("l2tp", {}).setdefault("sessions", [])
                entry = {
                    "local_id": int(m.group("local_id")),
                    "remote_id": int(m.group("remote_id")),
                    "tunnel_id": int(m.group("tunnel_id")),
                    "interface": m.group("interface"),
                    "username": m.group("username"),
                    "state": m.group("state"),
                    "last_change": m.group("last_change"),
                    "unique_id": int(m.group("unique_id")),
                }
                sessions.append(entry)
                continue

            # 1      2      user@domain.com            SSS Circuit   open    10
            m = p5.match(line)
            if m and current_section == "l2f":
                sessions = vpdn_dict.setdefault("l2f", {}).setdefault("sessions", [])
                entry = {
                    "clid": int(m.group("clid")),
                    "mid": int(m.group("mid")),
                    "username": m.group("username"),
                    "interface": m.group("interface").strip(),
                    "state": m.group("state"),
                    "unique_id": int(m.group("unique_id")),
                }
                sessions.append(entry)
                continue

            # 3      1      0030.949b.b4a0 Fa2/0          N/A       CNCT_FWDED
            m = p6.match(line)
            if m and current_section == "pppoe":
                sessions = vpdn_dict.setdefault("pppoe", {}).setdefault("sessions", [])
                entry = {
                    "uid": int(m.group("uid")),
                    "sid": int(m.group("sid")),
                    "remote_mac": m.group("remote_mac"),
                    "outgoing_interface": m.group("outgoing_interface"),
                    "interface": m.group("interface"),
                    "vast": None,
                    "session_state": m.group("session_state"),
                }
                sessions.append(entry)
                last_pppoe_session = entry
                continue

            #               0010.7b90.0840
            m = p7.match(line)
            if m and current_section == "pppoe" and last_pppoe_session is not None:
                last_pppoe_session["local_mac"] = m.group("local_mac")
                vast_val = m.group("vast")
                if vast_val is not None:
                    last_pppoe_session["vast"] = vast_val
                continue

        return ret_dict


class ShowVpdnGroupSelectSummarySchema(MetaParser):
    """Schema for show vpdn group-select summary"""
    schema = {
        "vpdn_group_select_summary": {
            "groups": {
                Any(): {
                    Optional("vrf"): str,
                    Optional("remote_name"): str,
                    "source_ip": str,
                    "protocol": str,
                    "direction": str,
                }
            }
        }
    }


class ShowVpdnGroupSelectSummary(ShowVpdnGroupSelectSummarySchema):
    """Parser for show vpdn group-select summary"""

    cli_command = "show vpdn group-select summary"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        if not output:
            return ret_dict

        column_starts = {}

        # VPDN Group      Vrf        Remote Name   Source-IP       Protocol Direction
        p1 = re.compile(
            r'^VPDN\s+Group\s+Vrf\s+Remote\s+Name\s+Source-IP\s+Protocol\s+Direction$'
        )

        #  vg_lts1_ip2    lts1                      10.1.1.2        l2tp     accept-dialin
        p2 = re.compile(
            r'^\s*(?P<group>\S+)'
            r'(?:\s+(?P<vrf>\S+))?'
            r'(?:\s+(?P<remote_name>(?!\d{1,3}(?:\.\d{1,3}){3})\S+))?'
            r'\s+(?P<source_ip>\d{1,3}(?:\.\d{1,3}){3})'
            r'\s+(?P<protocol>\S+)'
            r'\s+(?P<direction>\S+)$'
        )

        vgs_dict = None

        for line in output.splitlines():
            line = line.rstrip()
            if not line.strip():
                continue

            # VPDN Group      Vrf        Remote Name   Source-IP       Protocol Direction
            m = p1.match(line.strip())
            if m:
                column_starts = {
                    "vrf": line.index("Vrf"),
                    "remote_name": line.index("Remote Name"),
                    "source_ip": line.index("Source-IP"),
                }
                continue

            #  vg_lts1_ip2    lts1                      10.1.1.2        l2tp     accept-dialin
            if column_starts and re.search(r'\d{1,3}(?:\.\d{1,3}){3}', line):
                group = line[:column_starts["vrf"]].strip()
                vrf = line[column_starts["vrf"]:column_starts["remote_name"]].strip()
                remote_name = line[column_starts["remote_name"]:column_starts["source_ip"]].strip()
                rest = line[column_starts["source_ip"]:].split()
                if not group or len(rest) < 3:
                    continue

                if vgs_dict is None:
                    vgs_dict = ret_dict.setdefault("vpdn_group_select_summary", {}).setdefault("groups", {})
                entry = vgs_dict.setdefault(group, {})
                if vrf:
                    entry["vrf"] = vrf
                if remote_name:
                    entry["remote_name"] = remote_name
                entry["source_ip"] = rest[0]
                entry["protocol"] = rest[1]
                entry["direction"] = rest[2]
                continue

            #  vg_lts1_ip2    lts1                      10.1.1.2        l2tp     accept-dialin
            m = p2.match(line.strip())
            if m:
                group = m.group("group")
                if vgs_dict is None:
                    vgs_dict = ret_dict.setdefault("vpdn_group_select_summary", {}).setdefault("groups", {})
                entry = vgs_dict.setdefault(group, {})
                if m.group("vrf"):
                    entry["vrf"] = m.group("vrf")
                if m.group("remote_name"):
                    entry["remote_name"] = m.group("remote_name")
                entry["source_ip"] = m.group("source_ip")
                entry["protocol"] = m.group("protocol")
                entry["direction"] = m.group("direction")
                continue

        return ret_dict
