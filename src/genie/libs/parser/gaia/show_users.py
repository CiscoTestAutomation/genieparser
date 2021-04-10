""" show_users.py

Check Point Gaia parsers for the following show commands:
    * show users

"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


class ShowUsersSchema(MetaParser):
    schema = {
        'users': {
            Any(): {
               'uid': str,
                'gid': str,
                'home': str,
                'shell': str,
                'name': str,
                Optional('privileges'): str
            }
        }
    }

class ShowUsers(ShowUsersSchema):

    cli_command = ['show users']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}

        ''' Sample Output
        User             Uid       Gid       Home Dir.        Shell            Real Name               Privileges
        admin            0         0         /home/admin      /etc/cli.sh      Admin                   Access to Expert features
        monitor          102       100       /home/monitor    /etc/cli.sh      Monitor                 None
        somedude         10        20        /home/somewhere  /bin/bash        Some Dude               None
        user7730         0         0         /home/user7730   /bin/bash        n/a                                       
        '''

        p0 = re.compile(r'^(?P<username>[A-z0-9_-]{1,30})\s+(?P<uid>\d+)\s+(?P<gid>\d+)\s+(?P<home>\S+)\s+(?P<shell>\S+)\s+(?P<name>\S{1,30}\s?\S{1,30})([\ t]+(?P<privileges>\w+.*))?')
        
        for line in out.splitlines():
            line = line.strip()

            # admin            0         0         /home/admin      /etc/cli.sh      Admin                   Access to Expert features
            m = p0.match(line)
            if m:
                result_dict.setdefault('users',{})                
                new_user = m.groupdict()
                user = new_user['username']

                del new_user['username'] # username is used for top level key
                result_dict['users'][user] = new_user

                if result_dict['users'][user]['privileges'] is None:
                    del result_dict['users'][user]['privileges']

        return result_dict
