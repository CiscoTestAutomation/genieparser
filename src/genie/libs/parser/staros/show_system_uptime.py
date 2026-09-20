"""starOS implementation of show_system_uptime.py

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema

class TimeSchema(MetaParser):
    """Schema for show system uptime"""

    schema = {
        'uptime_info': {
            'DAYS': str,
            'HOURS': str,
            'MINUTES': str
        }     
    }


class ShowTime(TimeSchema):
    """Parser for show system uptime"""

    cli_command = 'show system uptime'

    """
System uptime: 69D 1H 34M

    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        time_dict = {}
        
        result_dict = {}

        # initial regexp pattern
        p0 = re.compile(r'\w+\s\w+:\s(?P<day>\d+D)\s(?P<hour>\d+H)\s(?P<minute>\d+M)')

        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                if 'uptime_info' not in time_dict:
                    result_dict = time_dict.setdefault('uptime_info',{})
                day = m.groupdict()['day']
                hour = m.groupdict()['hour']
                minute = m.groupdict()['minute']
                result_dict['DAYS'] = day
                result_dict['HOURS'] = hour
                result_dict['MINUTES'] = minute
                continue

        return time_dict