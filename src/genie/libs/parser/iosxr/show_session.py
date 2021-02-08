"""show_session.py

"""
import re
import genie.parsergen as pg

# import parser utils
from genie.libs.parser.utils.common import Common

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

class ShowUsersSchema(MetaParser):
    """Schema for show users on iosxr"""
    # LOCATION is optional
    # ACTIVE will be True if * at the begining of the output line
    schema = {
        'date': str,
        'line': {
            Any(): {
                'active': bool,
                Optional('user'): str,
                'service': str,
                'conns': str,
                'idle': str,
                Optional('location'): str, 
            },
        },
    }


class ShowUsers(ShowUsersSchema):
    """Parser for show users on iosxr"""

    cli_command = 'show users'
    """
    Thu Jan 28 15:14:53.365 UTC
      Line            User                 Service  Conns   Idle        Location
    * con0/RP0/CPU0   admin                hardware     0  00:00:00
    """
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        # initial root return dictionary
        ret_dict = {}

        # Thu Jan 28 15:14:53.365 UTC
        p1 = re.compile(r'^(?P<date>^\w.+UTC)$')
        
        # * con0/RP0/CPU0   admin   hardware     0  00:00:00
        p2 = re.compile(r'(?P<active>\*)? *(?P<line>\S+) +(?P<user>\S+) +(?P<service>\S+) +(?P<conns>\d+) +(?P<idle>[\d:]+)*(?P<location>[^*]+)?$')

        for cur_line in out.splitlines():
            cur_line = cur_line.strip()

            # match the date
            m = p1.match(cur_line)

            if m:
                if 'date' not in ret_dict:
                    user_dict = ret_dict.setdefault('date',{})
                ret_dict['date'] = m.groupdict()['date']
                continue

            # match output line
            m = p2.match(cur_line)
            
            if m:
                if 'line' not in ret_dict:
                    user_dict = ret_dict.setdefault('line',{})
                active = m.groupdict()['active']
                line = m.groupdict()['line']
                user = m.groupdict()['user']
                service = m.groupdict()['service']
                conns = m.groupdict()['conns']
                idle = m.groupdict()['idle']
                location = m.groupdict()['location']
            
                # declare line dictionary inside root dictionary
                user_dict[line] = {}
                
                # check if line is active and set boolean feild
                if active == '*':
                    user_dict[line]['active'] = True
                else:
                    user_dict[line]['active'] = False
                user_dict[line]['user'] = user
                user_dict[line]['service'] = service
                user_dict[line]['conns'] = conns
                user_dict[line]['idle'] = idle
                
                # check if location is not empty and set
                if location:
                    user_dict[line]['location'] = location.strip()
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