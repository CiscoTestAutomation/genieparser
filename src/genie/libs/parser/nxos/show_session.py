"""show_session.py

"""
import re
import genie.parsergen as pg

# import parser utils
from genie.libs.parser.utils.common import Common

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

class ShowUsersSchema(MetaParser):
    """Schema for show users"""
    # COMMENT is optional
    # ACTIVE will be True if * at the end of output line
    schema = {
        'line': {
            Any(): {
                'name': str,
                'time': str,
                'idle': str,
                'pid': str,
                Optional('comment'): str,
                'active': bool,
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
    """
    NAME     LINE         TIME         IDLE          PID COMMENT
    admin    pts/0        Jan 28 13:44   .          8096 *
    """
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial root return dictionary
        ret_dict = {}

        # admin    pts/0        Jan 28 13:44   .          8096 *
        p = re.compile(r'(?P<name>\S+) +(?P<line>\S+) +(?P<time>[a-zA-Z]+(?=\s\d)\s\d+\s\d+:\d+) +(?P<idle>\S+) +(?P<pid>[\d:]+) *(?P<comment>[^*]+)? *(?P<active>\*)?$')

        for cur_line in out.splitlines():
            cur_line = cur_line.strip()
        
            # match each column
            m = p.match(cur_line)
            
            if m:
                user_dict = ret_dict.setdefault('line',{})
                active = m.groupdict()['active']
                name = m.groupdict()['name']
                line = m.groupdict()['line']
                time = m.groupdict()['time']
                idle = m.groupdict()['idle']
                pid = m.groupdict()['pid']
                comment = m.groupdict()['comment']
            
                # declare line dictionary inside root dictionary
                user_dict[line] = {}

                # check if line is active and set boolean feild
                if active == '*':
                    user_dict[line]['active'] = True
                else:
                    user_dict[line]['active'] = False
                user_dict[line]['name'] = name
                user_dict[line]['time'] = time
                user_dict[line]['idle'] = idle
                user_dict[line]['pid'] = pid

                # check if comment is not empty and set
                if comment:
                    user_dict[line]['comment'] = comment
                continue    
        return ret_dict



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