"""show_vpdn.py
IOSXE parsers for the following show commands:
    * 'show vpdn'
    * 'show vpdn tunnel'
    * 'show vpdn tunnel pptp all'
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


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

