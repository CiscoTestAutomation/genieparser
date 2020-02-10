"""show_session.py

"""
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

class ShowLineSchema(MetaParser):
    """Schema for show line"""
    schema = {
        'tty': {
            Any(): {
                'active': bool,
                'type': str,
                Optional('tx'): int,
                Optional('rx'): int,
                'a': str,
                'modem': str,
                'roty': str,
                'acco': str,
                'acci': str,
                'uses': int,
                'noise': int,
                'overruns': str,
                'int': str,
            },
        }
    }


class ShowLine(ShowLineSchema):
    """Parser for show line"""

    cli_command = 'show line'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        #     Tty Typ     Tx/Rx    A Modem  Roty AccO AccI   Uses   Noise  Overruns   Int
        #       1 AUX   9600/9600  -    -      -    -    -      0       0     0/0       -
        # *     2 VTY              -    -      -    -    -      3       0     0/0       -
        p1 = re.compile(r'^((?P<busy>\*) +)?(?P<tty>\d+)'
                         ' +(?P<type>\w+)( +(?P<tx>\d+)\/(?P<rx>\d+))?'
                         ' +(?P<a>[\w\-]+) +(?P<modem>[\w\-]+)'
                         ' +(?P<roty>[\w\-]+) +(?P<acco>[\w\-]+)'
                         ' +(?P<acci>[\w\-]+) +(?P<uses>\d+)'
                         ' +(?P<noise>\d+) +(?P<overruns>[\d\/]+)'
                         ' +(?P<int>[\w\-]+)$')

        for line in out.splitlines():
            line = line.strip()

            #     Tty Typ     Tx/Rx    A Modem  Roty AccO AccI   Uses   Noise  Overruns   Int
            #       1 AUX   9600/9600  -    -      -    -    -      0       0     0/0       -
            # *     2 VTY              -    -      -    -    -      3       0     0/0       -
            m = p1.match(line)
            if m:
                group = m.groupdict()
                tty = group['tty']
                tty_dict = ret_dict.setdefault('tty', {}).setdefault(tty, {})
                if group['busy']:
                    tty_dict['active'] = True
                else:
                    tty_dict['active'] = False
                tty_dict['type'] = group['type']
                if group['tx']:
                    tty_dict['tx'] = int(group['tx'])
                if group['rx']:
                    tty_dict['rx'] = int(group['rx'])
                tty_dict['a'] = group['a']
                tty_dict['modem'] = group['modem']
                tty_dict['roty'] = group['roty']
                tty_dict['acco'] = group['acco']
                tty_dict['acci'] = group['acci']
                tty_dict['uses'] = int(group['uses'])
                tty_dict['noise'] = int(group['noise'])
                tty_dict['overruns'] = group['overruns']
                tty_dict['int'] = group['int']
                continue

        return ret_dict


class ShowUsersSchema(MetaParser):
    """Schema for show users"""
    schema = {
        'line': {
            Any(): {
                'active': bool,
                Optional('user'): str,
                'host': str,
                'idle': str,
                Optional('location'): str, 
            },
        },
        'interface': {
            Any(): {
                'user': {
                    Any(): {
                        'mode': str,
                        'idle': str,
                        Optional('peer_address'): str,
                    }
                }
            }
        }
    }


class ShowUsers(ShowUsersSchema):
    """Parser for show users"""

    cli_command = 'show users'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        #     Line       User       Host(s)              Idle       Location
        #    2 vty 0     nos        idle                 00:35:32 10.0.0.1
        #    3 vty 1     testuser   idle                 00:41:43 10.0.0.2
        # *  4 vty 2     testuser   idle                 00:00:07 10.0.0.3
        # *  0 con 0                idle                 00:00:00
        #   10 vty 0             Virtual-Access2          0      1212321
        p1 = re.compile(r'^((?P<busy>\*) +)?(?P<line>[\d]+ +[\w]+ +[\d]+)'
                         '( +(?P<user>[0-9a-z\-_.]+))? +(?P<host>\S+)'
                         ' +(?P<idle>[0-9\:]+)( +(?P<location>[\S]+))?$')

        # Interface    User               Mode         Idle     Peer Address
        # unknown      NETCONF(ONEP)      com.cisco.ne 00:00:49
        # unknown      a(ONEP)            com.cisco.sy 00:00:49
        p2 = re.compile(r'^(?P<interface>\S+) +(?P<user>\S+) '
                        r'+(?P<mode>[a-z.]+) +(?P<idle>\S+)'
                        r'(:? +(?P<peer_address>\S+))?$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                line = group.pop('line').strip()
                line_dict = ret_dict.setdefault('line', {}).setdefault(line, {})
                if group['busy']:
                    line_dict['active'] = True
                else:
                    line_dict['active'] = False
                
                if group['user']:
                    line_dict['user'] = group['user']
                if group['location']:
                    line_dict['location'] = group['location']

                line_dict['host'] = group['host']
                line_dict['idle'] = group['idle']
                continue

            # Interface    User               Mode         Idle     Peer Address
            # unknown      NETCONF(ONEP)      com.cisco.ne 00:00:49
            # unknown      a(ONEP)            com.cisco.sy 00:00:49
            m = p2.match(line)
            if m:
                group = m.groupdict()
                intf_dict = ret_dict.setdefault('interface', {}).\
                                     setdefault(group['interface'], {}).\
                                     setdefault('user', {}).\
                                     setdefault(group['user'], {})
                intf_dict['mode'] = group['mode']
                intf_dict['idle'] = group['idle']
                if group['peer_address'] is not None:
                    intf_dict['peer_address'] = group['peer_address']
                continue

        return ret_dict