"""
show system internal processes memory
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Schema, Any, Optional,
                                                Or, And, Default, Use)
# Parser Utils
from genie.libs.parser.utils.common import Common


class ShowSystemInternalProcessesMemorySchema(MetaParser):
    """
    Schema for show system internal processes memory
    """

    schema = {
        'pid':
            {
                Any():
                    {
                        'stat': str,
                        'time': str,
                        'majflt': int,
                        'trs': int,
                        'rss': int,
                        'vsz': int,
                        'mem_percent': float,
                        'command': str,
                        'tty': str
                    }
            }
    }


class ShowSystemInternalProcessesMemory(ShowSystemInternalProcessesMemorySchema):
    """
    Parser for show system internal processes memory
    """
    cli_command = "show system internal processes memory"

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # 7482 ?        Ssl  00:05:05    158    0 219576 1053628  3.7 /opt/mtx/bin/grpc -i 2626 -I
        # 27344 pts/0    Sl+  00:00:20      0   63 117180 709928  1.9 /isan/bin/vsh.bin
        p1 = re.compile(
            r'^(?P<pid>\d+)\s+(?P<tty>\S+)\s+(?P<stat>\S+)\s+(?P<time>[\d:]+)\s+(?P<majflt>\d+)\s+(?P<trs>\d+)\s+'
            r'(?P<rss>\d+)\s+(?P<vsz>\d+)\s+(?P<mem_percent>[\d.]+)\s+(?P<command>.+$)')

        ret_dict = {}

        for line in out.splitlines():
            stripped_line = line.strip()

            # 27344 pts/0    Sl+  00:00:20      0   63 117180 709928  1.9 /isan/bin/vsh.bin
            # 7482 ?        Ssl  00:05:05    158    0 219576 1053628  3.7 /opt/mtx/bin/grpc -i 2626 -I
            m = p1.match(stripped_line)
            if m:

                group = m.groupdict()

                pid = int(group['pid'])

                pid_dict = ret_dict.setdefault('pid', {}).setdefault(pid, {})

                pid_dict['stat'] = group['stat']
                pid_dict['majflt'] = int(group['majflt'])
                pid_dict['trs'] = int(group['trs'])
                pid_dict['rss'] = int(group['rss'])
                pid_dict['vsz'] = int(group['vsz'])
                pid_dict['mem_percent'] = float(group['mem_percent'])
                pid_dict['command'] = group['command']
                pid_dict['tty'] = group['tty']
                pid_dict['time'] = group['time']

        return ret_dict
