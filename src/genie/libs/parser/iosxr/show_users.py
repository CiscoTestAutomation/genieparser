"""show_users.py

"""
import re
import genie.parsergen as pg

# import parser utils
from genie.libs.parser.utils.common import Common

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

class ShowUsersSchema(MetaParser):
    """Schema for show users on iosxr
    > show users
    Thu Jan 28 15:14:53.365 UTC
      Line            User                 Service  Conns   Idle        Location
    * con0/RP0/CPU0   admin                hardware     0  00:00:00
    """
    # LOCATION is optional
    # ACTIVE will be True if * at the begining of the output line
    schema = {
        'line': {
            Any(): {
                'active': bool,
                'user': str,
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
        
        # * con0/RP0/CPU0   admin   hardware     0  00:00:00
        p = re.compile(r'(?P<active>\*)? *(?P<line>\S+) +(?P<user>\S+) +(?P<service>\S+) +(?P<conns>\d+) +(?P<idle>[\d:]+)*(?P<location>[^*]+)?$')

        for cur_line in out.splitlines():
            cur_line = cur_line.strip()

            # * con0/RP0/CPU0   admin   hardware     0  00:00:00
            m = p.match(cur_line)
            
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
                user_dict[line]['active'] = True if active == '*' else False
                user_dict[line]['user'] = user
                user_dict[line]['service'] = service
                user_dict[line]['conns'] = conns
                user_dict[line]['idle'] = idle
                
                # check if location is not empty and set
                if location:
                    user_dict[line]['location'] = location.strip()
                continue    
        return ret_dict
