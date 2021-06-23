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
                int:
                    {
                        'stat': str,
                        'time': str,
                        'majflt': int,
                        'trs': int,
                        'rss': int,
                        'vsz': int,
                        'mem_percent': float,
                        'command': str,
                        Optional('tty'): str
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

        # parser should never match
        # PID TTY      STAT     TIME MAJFLT  TRS   RSS    VSZ %MEM COMMAND
        # this is field headings and should not be considered

        # 7482 ?        Ssl  00:05:05    158    0 219576 1053628  3.7 /opt/mtx/bin/grpc -i 2626 -I
        # 27344 pts/0    Sl+  00:00:20      0   63 117180 709928  1.9 /isan/bin/vsh.bin
        p1 = re.compile(
            r'(?P<pid>^\d+)\s+(?P<tty>\S+)\s+(?P<stat>\S+)\s+(?P<time>\d+:\d+:\d+)\s+(?P<majflt>\d+)\s+('
            r'?P<trs>\d+)\s+(?P<rss>\d+)\s+(?P<vsz>\d+)\s+(?P<mem_percent>\d+\.\d+)\s+(?P<command>.+$)')

        ret_dict = {}

        for line in out.splitlines():
            stripped_line = line.strip()

            # 27344 pts/0    Sl+  00:00:20      0   63 117180 709928  1.9 /isan/bin/vsh.bin
            m = p1.match(stripped_line)
            if m:

                pid = int(m.groupdict()['pid'])
                tty = m.groupdict()['tty']

                ret_dict.setdefault('pid', {}).setdefault(pid, {})

                ret_dict.get('pid').get(pid).update({'stat': m.groupdict()['stat'], 'time': m.groupdict()['time'],
                        'majflt': int(m.groupdict()['majflt']), 'trs': int(m.groupdict()['trs']),
                        'rss': int(m.groupdict()['rss']), 'vsz': int(m.groupdict()['vsz']),
                        'mem_percent': float(m.groupdict()['mem_percent']), 'command': m.groupdict()['command']})

                if tty != '?':
                    ret_dict.get('pid').get(pid).update({'tty': tty})

        return ret_dict
