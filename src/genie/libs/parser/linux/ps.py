''' ps.py

Linux parsers for the following commands:
    * ps -ef
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# parser utils
from genie.libs.parser.utils.common import Common

# ===================
# Schema for 'ps -ef'
# ===================
class PsSchema(MetaParser):
    ''' Schema for "ps -ef" '''

    schema = {
        'process': {
            Any(): {
                'uid': str,
                'pid': str,
                'ppid': str,
                'c': str,
                'stime': str,
                'tty': str,
                'time': str,
                'cmd': str
            }
        }
    }
 
# ===================
# Parser for 'ps -ef'
# ===================
class Ps(PsSchema):
 
    ''' Parser for "ps -ef"'''
    cli_command = 'ps -ef'

    def cli(self, output=None, grep=None):
        if output is None:
            command = "{} | grep {}".format(self.cli_command, grep) if grep else self.cli_command
            out = self.device.execute(command)
        else:
            out = output
 
        # Init vars
        parsed_dict = {}

        # root      2322     1  0  2019 tty2     00:00:00 /sbin/mingetty /dev/tty2      
        # root      2326     1  0  2019 tty3     00:00:00 /sbin/mingetty /dev/tty3       
        # root      2328     1  0  2019 tty4     00:00:00 /sbin/mingetty /dev/tty4                                       
        # root      2334     1  0  2019 tty5     00:00:00 /sbin/mingetty /dev/tty5                  
        # root      2341     1  0  2019 tty6     00:00:00 /sbin/mingetty /dev/tty6
        p1 = re.compile(r'^(?P<uid>(\S+))\s+(?P<pid>(\d+))'
            r'\s+(?P<ppid>(\d+))\s+(?P<c>(\S+))\s+(?P<stime>(\d+))'
            r'\s+(?P<tty>(\S+))\s+(?P<time>(\S+))\s+(?P<cmd>(.+))$')
 
        for line in out.splitlines():
            line = line.strip()
 
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                pid = groups['pid']
                parsed_dict.setdefault('process', {}).setdefault(pid, groups)
                continue
 
        return parsed_dict