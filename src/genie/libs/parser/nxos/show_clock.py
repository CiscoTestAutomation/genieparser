import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional


class ShowClockSchema(MetaParser):
    """Schema for show clock"""

    schema = {
        'timezone': str,
        'day': str,
        'day_of_week': str,
        'month': str,
        'year': str,
        'time': str,
        Optional('time_source'): str,
    }


class ShowClock(ShowClockSchema):
    """Parser for show clock"""

    cli_command = 'show clock'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # 05:00:53.034 IST Sat Jan 01 2000
        p1 = re.compile(
            r'^(?P<time>\d{2}:\d{2}:\d{2}\.\d{3}) '
            r'(?P<timezone>\w+) (?P<day_of_week>\w+) '
            r'(?P<month>\w+) (?P<day>\d{1,2}) '
            r'(?P<year>\d{4})$'
        )

        # Time source is Hardware Calendar
        p2 = re.compile(
            r'^Time +source +is +(?P<time_source>[^\r\n]+)$'
        )

        # A11-EK-64# sh clock
        p3 = re.compile(r'^\S+#\s+sh clock$')

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # 05:00:53.034 IST Sat Jan 01 2000
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update(groups)
                continue

            # Time source is Hardware Calendar
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['time_source'] = groups['time_source']
                continue

            # A11-EK-64# sh clock
            m = p3.match(line)
            if m:
                continue

        return ret_dict
