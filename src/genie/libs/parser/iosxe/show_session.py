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
                'idle': str,
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

        pg_result = pg.oper_fill_tabular(device_output=out, device_os='iosxe',
                                         index=[1],
                                         header_fields=[' ', ' Line', 'User', 'Host\(s\)', 'Idle', '  Location'],
                                         label_fields=['busy', 'line', 'user', 'host', 'idle', 'location'],
                                         table_terminal_pattern='Interface\s+User\s+Mode\s+Idle\s+Peer\s+Address')

        # returns a dictionary
        pg_entries = pg_result.entries
        line_dict = {}

        # ============= iosxe pg_entries ================
        # {'2 vty 0': {'busy': '',
        #      'host': 'idle',
        #      'idle': '00:35:32',
        #      'line': '2 vty 0',
        #      'location': '10.0.0.1',
        #      'user': 'nos'},
        #   '4 vty 2': {'busy': '*',
        #              'host': 'idle',
        #              'idle': '00:00:07',
        #              'line': '4 vty 2',
        #              'location': '10.0.0.3',
        #              'user': 'testuser'}}

        # ============= ios pg_entries ================
        # {'*  0 con 0': {'busy': '',
        #         'host': 'idle',
        #         'idle': '01:58',
        #         'line': '*  0 con 0',
        #         'location': '',
        #         'user': ''},
        #  '10 vty 0': {'busy': '',
        #               'host': 'Virtual-Access2',
        #               'idle': '0',
        #               'line': '10 vty 0',
        #               'location': '1212321',
        #               'user': ''}}

        for k in pg_entries.keys():

            curr_dict = pg_entries[k]

            # ----------------------------
            # Check keys and assign values
            # ----------------------------

            # 'busy'
            busy = False
            if '*' in curr_dict['busy'] or '*' in k:
                busy = True

            # may have empty values:
            # 'user'
            # 'host'
            # 'location'
            for empty in ['user', 'host', 'location']:
                if curr_dict[empty] == '':
                    del curr_dict[empty]

            # ----------------------------
            # Build the parsed output
            # ----------------------------

            # handle ios sample output:
            # 'line': '*  0 con 0',
            line_pattern = re.compile(r'\*\s+(?P<line>[\s\S]+)')
            m = line_pattern.match(curr_dict['line'])
            if m:
                line_val = m.groupdict()['line']
            else:
                line_val = curr_dict['line']

            line_sub_dict = line_dict.setdefault(line_val, {})
            for key in ['user', 'host', 'idle', 'location']:
                if key in curr_dict:
                    line_sub_dict[key] = curr_dict[key]
            line_sub_dict['active'] = busy

        if bool(line_dict):
            ret_dict.setdefault('line', line_dict)

        # Interface    User               Mode         Idle     Peer Address
        # unknown      NETCONF(ONEP)      com.cisco.ne 00:00:49
        # unknown      a(ONEP)            com.cisco.sy 00:00:49

        interface_result = pg.oper_fill_tabular(device_output=out,
                                                device_os='iosxe',
                                                index=[0,1],
                                                header_fields=['Interface', 'User', 'Mode', 'Idle', 'Peer Address'])

        interface_entries = interface_result.entries

        # ========= interface_entries =====================
        # {'unknown': {'NETCONF(ONEP)': {'Idle': '00:00:49',
        #                        'Interface': 'unknown',
        #                        'Mode': 'com.cisco.ne',
        #                        'Peer Address': '',
        #                        'User': 'NETCONF(ONEP)'},
        #              'a(ONEP)': {'Idle': '00:00:49',
        #                       'Interface': 'unknown',
        #                       'Mode': 'com.cisco.sy',
        #                       'Peer Address': '',
        #                       'User': 'a(ONEP)'}}}

        if bool(interface_entries):
            column1_key = [*interface_entries.keys()][0]
            intf_dicts = interface_entries[column1_key]

            user_dict = {}
            interface_dict = {}
            for k in intf_dicts.keys():
                curr_dict = intf_dicts[k]

                user_sub_dict = user_dict.setdefault('user', {}).\
                                          setdefault(curr_dict['User'], {})

                user_sub_dict.update({'idle': curr_dict['Idle'],
                                      'mode': curr_dict['Mode']})

                if curr_dict['Peer Address']:
                    user_sub_dict['peer_address'] = curr_dict['Peer Address']

                interface_dict.setdefault(curr_dict['Interface'], user_dict)

            if bool(interface_dict):
                ret_dict.setdefault('interface', interface_dict)

        return ret_dict