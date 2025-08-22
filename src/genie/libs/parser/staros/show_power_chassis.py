"""starOS implementation of show_power_chassis.py

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema

class PowerSchema(MetaParser):
    """Schema for show power chassis"""

    schema = {
        'power_info': {
            'Message': str
        },     
    }


class ShowPowerVersion(PowerSchema):
    """Parser for show power chassis"""

    cli_command = 'show power chassis'

    """
All power sources are good
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        power_dict = {}
        
        result_dict = {}

        # initial regexp pattern
        p0 = re.compile(r'(?P<info>^All power sources are good$)')

        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                if 'power_info' not in power_dict:
                    result_dict = power_dict.setdefault('power_info',{})
                info = m.groupdict()['info']
                result_dict['Message'] = info
                continue

        return power_dict