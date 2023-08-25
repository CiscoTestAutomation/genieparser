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

class ShowEnvironmentAllIncludeLocationSchema(MetaParser):
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


class ShowEnvironmentAllIncludeLocation(ShowEnvironmentAllIncludeLocationSchema):
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

class ShowHwProgrammableAllSchema(MetaParser):
    """Schema for show hw-programmable all"""
    schema = {
        Any(): {
            'cpld_ver': str,
            'fpga_ver': str
        }
    }

class ShowHwProgrammableAll(ShowHwProgrammableAllSchema):
    """Parser for show hw-programmable all"""

    cli_command = 'show hw-programmable all'

    def cli(self, output=None):
        """parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        """
        if output is None:
            output = self.device.execute(self.cli_command)

        platform_dict = {}

        #R0                14111801                  18102401       
        p1 = re.compile(r'^(?P<slot>\w+) +(?P<cpld_version>\d+|N\/A) +(?P<fpga_version>[\w\.\(\)\/]+)$')

        for line in output.splitlines():
            line = line.strip()

            # R0         14111801            18102401
            m = p1.match(line)
            if m:
                fpga_ver = m.groupdict()['fpga_version']
                cpld_ver = m.groupdict()['cpld_version']
                slot = m.groupdict()['slot']

                platform_dict[slot] = {'fpga_ver': fpga_ver, 'cpld_ver': cpld_ver}

        return platform_dict
