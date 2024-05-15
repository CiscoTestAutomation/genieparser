"""
parser for:
* show line
"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


class ShowLineSchema(MetaParser):
    """Schema for show line"""
    schema = {
        'tty': {
            Any(): {
                'active': bool,
                'type': str,
                'speed': int,
                'overruns': str,
                'acci': str,
                'acco': str,
                'tty': str,
            },
        }
    }


class ShowLine(ShowLineSchema):
    """Parser for show line"""

    cli_command = 'show line'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        #    Tty             Speed     Overruns             Acc I/O
        # *  con0/RP0/CPU0  115200          0/0                 -/-
        #    con0/RP1/CPU0  115200          0/0                 -/-
        #    vty0               0          0/0                 -/-

        p1 = re.compile(r'(?P<active>\*)?\s*(?P<tty>[/\w]+)\s*(?P<speed>\d+)\s*(?P<overruns>\S+)\s*(?P<acci>\S+)/(?P<acco>\S+)$')

        ret_dict = {}

        lines = out.splitlines()
        for line in lines:
            line = line.strip()

            # *  con0/RP0/CPU0  115200          0/0                 -/-
            #    con0/RP1/CPU0  115200          0/0                 -/-
            #    vty0               0          0/0                 -/-
            m1 = p1.match(line)
            if m1:
                tty = m1.groupdict().get('tty')
                tty_dict = ret_dict.setdefault('tty', {}).setdefault(tty, {})
                tty_dict['tty'] = tty
                tty_dict['active'] = True if m1.groupdict().get('active') else False
                tty_dict['speed'] = int(m1.groupdict().get('speed'))
                tty_dict['overruns'] = m1.groupdict().get('overruns')
                tty_dict['acci'] = m1.groupdict().get('acci')
                tty_dict['acco'] = m1.groupdict().get('acco')
                if 'vty' in tty.lower():
                    tty_dict['type'] = 'TTY'
                elif 'con' in tty.lower():
                    tty_dict['type'] = 'CTY'
                continue

        return ret_dict
