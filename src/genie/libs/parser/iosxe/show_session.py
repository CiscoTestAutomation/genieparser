"""show_session.py

"""
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                               Any, \
                                               Optional, \
                                               Or, \
                                               And, \
                                               Default, \
                                               Use


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
        p1 = re.compile(r'^((?P<busy>\*) +)?(?P<tty>\d+)'
                         ' +(?P<type>\w+)( +(?P<Tx>\d+)\/(?P<Rx>\d+))?'
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
                ret_dict.setdefault('tty', {}).setdefault(tty, {})
                if group['busy']:
                    ret_dict['tty'][tty]['active'] = True
                else:
                    ret_dict['tty'][tty]['active'] = False
                ret_dict['tty'][tty]['type'] = group['type']
                if 'tx' in group:
                    ret_dict['tty'][tty]['tx'] = int(group['tx'])
                    ret_dict['tty'][tty]['rx'] = int(group['rx'])
                ret_dict['tty'][tty]['a'] = group['a']
                ret_dict['tty'][tty]['modem'] = group['modem']
                ret_dict['tty'][tty]['roty'] = group['roty']
                ret_dict['tty'][tty]['acco'] = group['acco']
                ret_dict['tty'][tty]['acci'] = group['acci']
                ret_dict['tty'][tty]['uses'] = int(group['uses'])
                ret_dict['tty'][tty]['noise'] = int(group['noise'])
                ret_dict['tty'][tty]['overruns'] = group['overruns']
                ret_dict['tty'][tty]['int'] = group['int']
                continue

        return ret_dict


class ShowUsersSchema(MetaParser):
    """Schema for show users"""
    schema = {
        'line': {
            Any(): {
                'active': bool,
                'user': str,
                'host': str,
                'idle': str,
                'location': str, 
            },
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
        p1 = re.compile(r'^((?P<busy>\*) +)?(?P<line>[\w\s]+)'
                         ' +(?P<user>\w+) +(?P<host>\w+)'
                         ' +(?P<idle>[0-9\:]+) +(?P<location>[\d\.]+)$')

        for line in out.splitlines():
            line = line.strip()

            #     Line       User       Host(s)              Idle       Location
            #    2 vty 0     nos        idle                 00:35:32 10.0.0.1
            #    3 vty 1     testuser   idle                 00:41:43 10.0.0.2
            # *  4 vty 2     testuser   idle                 00:00:07 10.0.0.3
            m = p1.match(line)
            if m:
                group = m.groupdict()
                line = group.pop('line').strip()
                ret_dict.setdefault('line', {}).setdefault(line, {})
                if group['busy']:
                    ret_dict['line'][line]['active'] = True
                else:
                    ret_dict['line'][line]['active'] = False
                group.pop('busy')
                ret_dict['line'][line].update({k:str(v) for k, v in group.items()})
                continue

        return ret_dict