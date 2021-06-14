
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use


class DfSchema(MetaParser):

    schema = {
        'directory': {
            Any(): {
                'filesystem': str,
                'total': int,
                'used': int,
                'available': int,
                'use_percentage': int,
                'mounted_on': str
            }
        }

    }



class Df(DfSchema):

    cli_command = ['df', 'df {directory}']

    def cli(self, directory='', output=None):
        if output is None:
            if directory:
                out = self.device.execute(self.cli_command[1].format(directory=directory))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # Filesystem                  1K-blocks    Used Available Use% Mounted on
        # /dev/mapper/vg_ifc0-scratch  41153760 6944104  32096120  18% /home
        p1 = re.compile(r'(?P<filesystem>\S+)\s+(?P<blocks>\d+)\s+(?P<used>\d+)\s+(?P<available>\d+)\s+(?P<use_percentage>\d+)%\s+(?P<mounted_on>\S+)$')

        df_dict = {}

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                groups = m.groupdict()
                directory = groups['mounted_on']
                mount_dict = df_dict.setdefault('directory', {}).setdefault(directory, {})
                mount_dict['filesystem'] = groups['filesystem']
                mount_dict['total'] = int(groups['blocks']) * 1024
                mount_dict['used'] = int(groups['used']) * 1024
                mount_dict['available'] = int(groups['available']) * 1024
                mount_dict['use_percentage'] = int(groups['use_percentage'])
                mount_dict['mounted_on'] = groups['mounted_on']

        return df_dict
