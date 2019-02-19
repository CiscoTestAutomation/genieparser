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
        'source': str,
        'zone': str,
        'day': str,
        'week_day': str,
        'month': str,
        'year': str,
        'time': str,
        'load': {
            'five_secs': str,
            'one_min': str,
            'five_min': str,
        },
        'busy': bool,
        'tty': str,
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
        p1 = re.compile(r'^Load +for +five +secs: +(?P<five_secs>[\d\/\%]+); '
                         '+one +minute: +(?P<one_min>[\d\%]+); '
                         '+five +minutes: +(?P<five_min>[\d\%]+)$')

        p2 = re.compile(r'^Time +source +is +(?P<source>\w+),'
                         ' +(?P<time>[\d\:\.]+) +(?P<zone>\w+)'
                         ' +(?P<week_day>\w+) +(?P<month>\w+) +'
                         '(?P<day>\d+) +(?P<year>\d+)$')

        p3 = re.compile(r'^((?P<busy>\*) +)?(?P<tty>\d+)'
                         ' +(?P<type>\w+)( +(?P<Tx>\d+)\/(?P<Rx>\d+))?'
                         ' +(?P<a>[\w\-]+) +(?P<modem>[\w\-]+)'
                         ' +(?P<roty>[\w\-]+) +(?P<acco>[\w\-]+)'
                         ' +(?P<acci>[\w\-]+) +(?P<uses>\d+)'
                         ' +(?P<noise>\d+) +(?P<overruns>[\d\/]+)'
                         ' +(?P<int>[\w\-]+)$')

        for line in out.splitlines():
            line = line.strip()

            # Load for five secs: 1%/0%; one minute: 2%; five minutes: 3%
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('load', {})
                ret_dict['load'].update({k:str(v) for k, v in group.items()})
                continue

            # Time source is NTP, 18:56:04.554 JST Mon Oct 17 2016
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({k:str(v) for k, v in group.items()})
                continue

            #     Tty Typ     Tx/Rx    A Modem  Roty AccO AccI   Uses   Noise  Overruns   Int
            #       1 AUX   9600/9600  -    -      -    -    -      0       0     0/0       -
            # *     2 VTY              -    -      -    -    -      3       0     0/0       -
            m = p3.match(line)
            if m:
                group = m.groupdict()
                if group['busy']:
                    ret_dict['busy'] = True
                else:
                    ret_dict['busy'] = False
                ret_dict['tty'] = group['tty']
                ret_dict['type'] = group['type']
                if 'tx' in group:
                    ret_dict['tx'] = int(group['tx'])
                    ret_dict['rx'] = int(group['rx'])
                ret_dict['a'] = group['a']
                ret_dict['modem'] = group['modem']
                ret_dict['roty'] = group['roty']
                ret_dict['acco'] = group['acco']
                ret_dict['acci'] = group['acci']
                ret_dict['uses'] = int(group['uses'])
                ret_dict['noise'] = int(group['noise'])
                ret_dict['overruns'] = group['overruns']
                ret_dict['int'] = group['int']
                continue

        return ret_dict


class ShowUsersSchema(MetaParser):
    """Schema for show users"""
    schema = {
        'source': str,
        'zone': str,
        'day': str,
        'week_day': str,
        'month': str,
        'year': str,
        'time': str,
        'load': {
            'five_secs': str,
            'one_min': str,
            'five_min': str,
        },
        'busy': bool,
        'line': str,
        'user': str,
        'host': str,
        'idle': str,
        'location': str,
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
        p1 = re.compile(r'^Load +for +five +secs: +(?P<five_secs>[\d\/\%]+); '
                         '+one +minute: +(?P<one_min>[\d\%]+); '
                         '+five +minutes: +(?P<five_min>[\d\%]+)$')

        p2 = re.compile(r'^Time +source +is +(?P<source>\w+),'
                         ' +(?P<time>[\d\:\.]+) +(?P<zone>\w+)'
                         ' +(?P<week_day>\w+) +(?P<month>\w+) +'
                         '(?P<day>\d+) +(?P<year>\d+)$')

        p3 = re.compile(r'^((?P<busy>\*) +)?(?P<line>[\w\s]+)'
                         ' +(?P<user>\w+) +(?P<host>\w+)'
                         ' +(?P<idle>[0-9\:]+) +(?P<location>[\d\.]+)$')

        for line in out.splitlines():
            line = line.strip()

            # Load for five secs: 1%/0%; one minute: 2%; five minutes: 3%
            m = p1.match(line)
            if m:
                group = m.groupdict()
                import pdb; pdb.set_trace
                ret_dict.setdefault('load', {})
                ret_dict['load'].update({k:str(v) for k, v in group.items()})
                continue

            # Time source is NTP, 18:56:04.554 JST Mon Oct 17 2016
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({k:str(v) for k, v in group.items()})
                continue

            #     Line       User       Host(s)              Idle       Location
            #    2 vty 0     nos        idle                 00:35:32 10.241.137.203
            #    3 vty 1     testuser   idle                 00:41:43 10.241.147.155
            # *  4 vty 2     testuser   idle                 00:00:07 10.241.146.52
            m = p3.match(line)
            if m:
                group = m.groupdict()
                if group['busy']:
                    ret_dict['busy'] = True
                else:
                    ret_dict['busy'] = False
                group.pop('busy')
                ret_dict.update({k:str(v) for k, v in group.items()})
                continue

        return ret_dict