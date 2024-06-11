"""starOS implementation of show temperature.py

"""
from os import stat_result
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema

class ShowTemperatureSchema(MetaParser):
    """Schema for show temperature"""

    schema = {
        'temperature_table': {
            Any(): {
                'STATE': str,
            },
        }    
    }


class ShowTemperature(ShowTemperatureSchema):
    """Parser for show temperature"""

    cli_command = 'show temperature'

    """
Card  1:   Normal
Card  2:   Normal
Card  3:   Normal
Card  4:   Normal
Card  5:   Normal
Card  6:   Normal
Card  7:   Normal
Card  8:   Normal
Card  9:   Normal
Card 10:   Normal
Card 11:   Normal
Card 12:   Normal
Card 14:   Normal
Card 15:   Normal
Card 16:   Normal
Card 17:   Normal
Fan Lower Rear: 26 C
Fan Upper Rear: 43 C
Fan Lower Front: 24 C
Fan Upper Front: 33 C
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        temperature_dict = {}
        result_dict = {}

        # initial regexp pattern
        p0 = re.compile(r'^\w+\s+(?P<card>\d+).\s+(?P<state>\w+$)')
        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                if 'temperature_table' not in temperature_dict:
                    result_dict = temperature_dict.setdefault('temperature_table',{})
                card = m.groupdict()['card']
                state = m.groupdict()['state']

                result_dict[card] = {}
                result_dict[card]['STATE'] = state
                continue

        return temperature_dict