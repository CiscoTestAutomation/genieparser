"""show_system.py

"""
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                               Any, \
                                               Optional, \
                                               Or, \
                                               And, \
                                               Default, \
                                               Use


class ShowClockSchema(MetaParser):
    """Schema for show clock"""
    schema = {
        'timezone': str,
        'day': str,
        'day_of_week': str,
        'month': str,
        'year': str,
        'time': str,
    }


class ShowClock(ShowClockSchema):
    """Parser for show clock"""

    cli_command = 'show clock'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^(?P<time>[\d\:\.]+) +(?P<timezone>\w+)'
                         ' +(?P<day_of_week>\w+) +(?P<month>\w+) +'
                         '(?P<day>\d+) +(?P<year>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # 18:56:04.554 EST Mon Oct 17 2016
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({k:str(v) for k, v in group.items()})
                continue

        return ret_dict