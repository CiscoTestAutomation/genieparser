"""show_session.py

"""
import re
import genie.parsergen as pg
# import parser utils
from genie.libs.parser.utils.common import Common

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
                Optional('idle'): str,
                Optional('location'): str, 
            },
        },
        Optional('interface'): {
            Any(): {
                'user': {
                    Any(): {
                        'mode': str,
                        'idle': str,
                        Optional('peer_address'): str,
                    },
                },
            },
        },
        Optional('connection_details'): {
            Any(): {
                'intf': str,
                'u_name': str,
                'mode': str,
                'idle_time': str,
                'peer_address': str
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

        #     Line       User       Host(s)              Idle       Location
        #    3 vty 1     testuser   idle                 00:41:43   10.0.0.2
        # *  4 vty 1     admin      idle                 00:00:00   xxx-xxxxxxx-nitro2.cisco.com
        # *  2 vty 0     admin      idle                 00:00:00
        # *  0 con 0                idle                 01:58
        #    10 vty 0               Virtual-Access2      0          1212321
        #    0 con 0                idle
        # *   2 vty 0         user1           idle            0   SERVICE1.CISCO.COM
        p1 = re.compile(r'^(?:(?P<active>\*))?( +)?(?P<line>\d+ \S+ \d+)(?: {1,9}(?P<user>\S+))? '
                        r'+(?P<host>\S+)( +)?(?P<idle>\S+)?(?: +(?P<location>\S+))?')
        # counting spaces from 1-9, check if class errors in future releases

        #                                                    			 foo-bar.cisco.com
        p1_1 = re.compile(r'^(?P<location>\S+)$')

        #  Interface    User               Mode         Idle     Peer Address
        #  unknown      NETCONF(ONEP)      com.cisco.ne 00:00:49
        p2 = re.compile(r'^(?P<interface>\S+) +(?P<user>\S+) +(?P<mode>\S+) '
                        r'+(?P<idle>[\d\:]+)( +(?P<peer_address>\S+)?)?$')

        # Vi2.1        lns@cisco.com      PPPoVPDN     -        21.21.21.7
        p3 = re.compile(r'^(?P<intf>[A-Za-z\d\.]+) +(?P<u_name>\S+) +(?P<mode>\S+)'
                        r' +(?P<idle_time>\S+) +(?P<peer_address>[\d\.]+)$')

        # initial return dictionary
        ret_dict = {}
        var = 1
        inter_flag = False
        for line in out.splitlines():
            line = line.strip()

            # *  4 vty 1     admin      idle                 00:00:00 xxx-xxxxxxx-nitro2.cisco.com
            m = p1.match(line)
            if m:
                group = m.groupdict()
                term_line = group.pop('line')
                if group['active']:
                    active = True
                else:
                    active = False
                del group['active']

                if not group['location']:
                    del group['location']

                if not group['user']:
                    del group['user']

                if not group['idle']:
                    del group['idle']

                line_dict = ret_dict.setdefault('line', {}).setdefault(term_line, {})
                line_dict.update(group)
                line_dict.update({'active': active})

            #                                                    			 foo-bar.cisco.com
            m = p1_1.match(line)
            if m:
                if not inter_flag:
                    line_dict.update(m.groupdict())
                else:
                    intf_dict.update({'peer_address': m.groupdict()['location']})

            #  unknown      NETCONF(ONEP)      com.cisco.ne 00:00:49
            m = p2.match(line)
            if m:
                group = m.groupdict()
                intf = group['interface']
                intf_dict = ret_dict.setdefault('interface', {}).setdefault(intf, {}).\
                    setdefault('user', {}).setdefault(group['user'], {})

                intf_dict.update({
                    'mode': group['mode'],
                    'idle': group['idle'],
                    })

                if not group['peer_address']:
                    del group['peer_address']
                else:
                    intf_dict.update({'peer_address': group['peer_address']})

                inter_flag = True

            # Vi2.1        lns@cisco.com      PPPoVPDN     -        21.21.21.7
            m = p3.match(line)
            if m:
                ret_dict.setdefault('connection_details', {})
                ret_dict["connection_details"].setdefault(var, {})
                groups = m.groupdict()
                ret_dict["connection_details"][var]['intf'] = groups['intf']
                ret_dict["connection_details"][var]['u_name'] = groups['u_name']
                ret_dict["connection_details"][var]['mode'] = groups['mode']
                ret_dict["connection_details"][var]['idle_time'] = groups['idle_time']
                ret_dict["connection_details"][var]['peer_address'] = groups['peer_address']
                var += 1

        return ret_dict
