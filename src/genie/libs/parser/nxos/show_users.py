"""show_users.py

"""
import re
import genie.parsergen as pg

# import parser utils
from genie.libs.parser.utils.common import Common

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

class ShowUsersSchema(MetaParser):
    """Schema for show users on nxos
    > show users
        NAME     LINE         TIME         IDLE          PID COMMENT
        admin    pts/0        Jan 28 13:44   .          8096 *
    """
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
        
            # admin    pts/0        Jan 28 13:44   .          8096 *
            m = p.match(cur_line)
            
            if m:
                user_dict = ret_dict.setdefault('line',{})
                group = m.groupdict()
                active = group['active']
                name = group['name']
                line = group['line']
                time = group['time']
                idle = group['idle']
                pid = group['pid']
                comment = group['comment']
            
                # declare line dictionary inside root dictionary
                user_dict[line] = {}

                # check if line is active and set boolean feild
                user_dict[line]['active'] = True if active == '*' else False

                user_dict[line]['name'] = name
                user_dict[line]['time'] = time
                user_dict[line]['idle'] = idle
                user_dict[line]['pid'] = pid

                # check if comment is not empty and set
                if comment:
                    user_dict[line]['comment'] = comment
                continue    
        return ret_dict

