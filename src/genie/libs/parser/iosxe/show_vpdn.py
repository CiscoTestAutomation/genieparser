"""show_vpdn.py
IOSXE parsers for the following show commands:
    * 'show vpdn'
    * 'show vpdn tunnel'
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
