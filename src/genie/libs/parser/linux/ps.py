''' ps.py

Linux parsers for the following commands:
    * ps -ef
    * ps -ef | grep {grep}
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
        'pid': {
            Any(): {
                'uid': str,
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
    cli_command = ['ps -ef', 'ps -ef | grep {grep}']

    def cli(self, output=None, grep=None):
        if output is None:
            command = self.cli_command[0]
            if grep:
                command = self.cli_command[1].replace('{grep}', grep)
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
        p1 = re.compile(r'^(?P<uid>\S+)\s+(?P<pid>\d+)\s+(?P<ppid>\d+)'
            + r'\s+(?P<c>\S+)\s+(?P<stime>\S+)\s+(?P<tty>\S+)'
            + r'\s+(?P<time>\S+)\s+(?P<cmd>.+)$')
 
        for line in out.splitlines():
            line = line.strip()
 
            m = p1.match(line)
            if m:
                if grep and 'grep {}'.format(grep) in line:
                    continue

                groups = m.groupdict()
                pid = groups['pid']
                del groups['pid']
                parsed_dict.setdefault('pid', {}).setdefault(pid, groups)

        #if len(parsed_dict) == 0:
        #    parsed_dict.setdefault('pid', {})

        return parsed_dict