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
        'source': str,
        'zone': str,
        'day': str,
        'week_day': str,
        'month': str,
        'year': str,
        'time': str,
        'load': {
            'five_secs': str,
            'one_min': str,
            'five_min': str,
        }
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
        p1 = re.compile(r'^Load +for +five +secs: +(?P<five_secs>[\d\/\%]+); '
                         '+one +minute: +(?P<one_min>[\d\%]+); '
                         '+five +minutes: +(?P<five_min>[\d\%]+)$')

        p2 = re.compile(r'^Time +source +is +(?P<source>\w+),'
                         ' +(?P<time>[\d\:\.]+) +(?P<zone>\w+)'
                         ' +(?P<week_day>\w+) +(?P<month>\w+) +'
                         '(?P<day>\d+) +(?P<year>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # Load for five secs: 1%/0%; one minute: 2%; five minutes: 3%
            m = p1.match(line)
            if m:
                group = m.groupdict()
                import pdb; pdb.set_trace
                ret_dict.setdefault('load', {})
                ret_dict['load'].update({k:str(v) for k, v in group.items()})
                continue

            # Time source is NTP, 18:56:04.554 JST Mon Oct 17 2016
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({k:str(v) for k, v in group.items()})
                continue

        return ret_dict