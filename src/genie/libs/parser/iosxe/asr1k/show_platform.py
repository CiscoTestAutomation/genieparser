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
        'sensor_list': {
            Any(): {
                'sensor': {
                    Any(): {
                        'location': str,
                        'state': str,
                        'reading': str,
                    },
                }
            },
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
        sensor_list = None

        # initial regexp pattern
        p1 = re.compile(r'^Sensor +List: +(?P<sensor_list>[\w\s]+)$')

        p2 = re.compile(r'^(?P<sensor_name>([\w\d\:]+( [\w]+( [\w]+)?)?)) +(?P<location>[\w\d]+)'
                         ' +(?P<state>([\w]+ [\w]+ [\d%]+)|([\w]+)) +(?P<reading>[\w\d\s]+)$')

        for line in out.splitlines():
            line = line.strip()

            # Sensor List:  Environmental Monitoring
            m = p1.match(line)
            if m:
                group = m.groupdict()
                sensor_list = group['sensor_list']

            # Sensor           Location          State             Reading
            # V1: VMA          0                 Normal            1098 mV
            # V1: VMB          0                 Normal            1201 mV
            m = p2.match(line)
            if m and sensor_list:
                group = m.groupdict()
                sensor_name = group.pop('sensor_name')
                if sensor_name == 'Sensor':
                    continue
                fin_dict = ret_dict.setdefault('sensor_list', {}).setdefault(sensor_list, {}).\
                    setdefault('sensor', {}).setdefault(sensor_name, {})
                fin_dict.update({k:str(v) for k, v in group.items()})
                continue

        return ret_dict

class ShowEnvironmentAllSchema(MetaParser):
    """Schema for show environment all
                  show environment all | include <WORD>"""

    schema = {
        'sensor_list': {
            Any(): {
                'sensor': {
                    Any(): {
                        'location': str,
                        'state': str,
                        'reading': str,
                    },
                }
            },
        }
    }


class ShowEnvironmentAllIncludeLocation(ShowEnvironmentAllSchema):
    """Parser for show environment all | include Sensor |<WORD>"""

    cli_command = 'show environment all | include Sensor'

    def cli(self, key_word,output=None):
        if output is None:
            self.cli_command += ' |' + key_word
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}
        sensor_list = None

        # initial regexp pattern
        p1 = re.compile(r'^Sensor +List: +(?P<sensor_list>[\w\s]+)$')

        p2 = re.compile(r'^(?P<sensor_name>([\w\d\:]+( [\w]+( [\w]+)?)?)) +(?P<location>[\w\d]+)'
                         ' +(?P<state>([\w]+ [\w]+ [\d%]+)|([\w]+)) +(?P<reading>[\w\d\s]+)$')

        for line in out.splitlines():
            line = line.strip()

            # Sensor List:  Environmental Monitoring
            m = p1.match(line)
            if m:
                group = m.groupdict()
                sensor_list = group['sensor_list']

            # Sensor           Location          State             Reading
            # V1: VMA          0                 Normal            1098 mV
            # V1: VMB          0                 Normal            1201 mV
            m = p2.match(line)
            if m and sensor_list:
                group = m.groupdict()
                sensor_name = group.pop('sensor_name')
                if sensor_name == 'Sensor':
                    continue
                fin_dict = ret_dict.setdefault('sensor_list', {}).setdefault(sensor_list, {}).\
                    setdefault('sensor', {}).setdefault(sensor_name, {})
                fin_dict.update({k:str(v) for k, v in group.items()})
                continue

        return ret_dict