"""ASR1K implementation of show_platform.py

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


class ShowEnvironmentAllSchema(MetaParser):
    """Schema for show environment all
                  show environment all | include <WORD>"""

    schema = {
        Optional('source'): str,
        Optional('zone'): str,
        Optional('day'): str,
        Optional('week_day'): str,
        Optional('month'): str,
        Optional('year'): str,
        Optional('time'): str,
        Optional('load'): {
            'five_secs': str,
            'one_min': str,
            'five_min': str,
        },
        Optional('sensor_list'): str,
        'sensor': {
            Any(): {
                'location': str,
                'state': str,
                'reading': str,
                'sensor_name': str,
            }
        }
    }


class ShowEnvironmentAll(ShowEnvironmentAllSchema):
    """Parser for show environment all
                  show environment all | include <WORD>"""

    cli_command = 'show environment all'

    def cli(self, key_word='',output=None):
        if output is None:
            if key_word:
                self.cli_command += ' | include ' + key_word
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

        p3 = re.compile(r'^Sensor +List: +(?P<sensor_list>[\w\s]+)$')

        p4 = re.compile(r'^(?P<sensor_name>([\w\d\:]+ [\w]+( [\w]+)?)) +(?P<location>[\w\d]+)'
                         ' +(?P<state>([\w]+ [\w]+ [\d%]+)|([\w]+)) +(?P<reading>[\w\d\s]+)$')

        for line in out.splitlines():
            line = line.strip()

            # Load for five secs: 1%/0%; one minute: 2%; five minutes: 3%
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('load', {})
                ret_dict['load'].update({k:str(v) for k, v in group.items()})
                continue

            # Time source is NTP, 18:56:04.554 JST Mon Oct 17 2016
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({k:str(v) for k, v in group.items()})
                continue

            # Sensor List:  Environmental Monitoring
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({k:str(v) for k, v in group.items()})

            # Sensor           Location          State             Reading
            # V1: VMA          0                 Normal            1098 mV
            # V1: VMB          0                 Normal            1201 mV
            m = p4.match(line)
            if m:
                group = m.groupdict()
                sensor_name = group['sensor_name']
                fin_dict = ret_dict.setdefault('sensor', {}).setdefault(sensor_name, {})
                fin_dict.update({k:str(v) for k, v in group.items()})
                continue

        return ret_dict