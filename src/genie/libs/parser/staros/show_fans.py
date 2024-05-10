"""starOS implementation of show_fans.py

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema

class fanSchema(MetaParser):
    """Schema for show fans"""

    schema = {
        'fan_info': {
            Any():{
            'State':str,
            'Speed':str,
            'Temperature':str
            }
        },
    }


class Showfan(fanSchema):
    """Parser for show fans"""

    cli_command = 'show fans'

    """
        GGSN Service:
            In Use              : 298335
            Max Used            : 479038 ( Wednesday July 06 00:55:50 CDT 2022 )
            Limit               : 10000000
            License Status      : Within Acceptable Limits
        PGW Service:
            In Use              : 0
            Max Used            : 0 ( Never )
            Limit               : 10000000
            License Status      : Within Acceptable Limits
        SGW Service:
            In Use              : 0
            Max Used            : 0 ( Never )
            Limit               : 10000000
            License Status      : Within Acceptable Limits
        SAEGW Service:
            In Use              : 1582684
            Max Used            : 2866327 ( Wednesday July 06 01:17:00 CDT 2022 )
            Limit               : 10000000
            License Status      : Within Acceptable Limits
        ECS Information:
        Enhanced Charging Service:
            In Use              : 1823158
            Max Used            : 3116637 ( Wednesday July 06 01:12:00 CDT 2022 )
            Limit               : 16900000
            License Status      : Within Acceptable Limits
        P2P information:
        P2P Service:
            In Use              : 1571450
            Max Used            : 2720328 ( Wednesday July 06 01:11:30 CDT 2022 )
            Limit               : 6900000
            License Status      : Within Acceptable Limits
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        fan_dict = {}
        
        result_dict = {}

        # initial regexp pattern
        p0 = re.compile(r'(?P<fan>\w+\s\w+\s)\w+\s\w+:$')
        p1 = re.compile(r'State:\s+(?P<state>\w+)')
        p2 = re.compile(r'Speed:\s+(?P<speed>\w+.)')
        p3 = re.compile(r'Temperature:\s+(?P<temp>\w+.)')


        for line in out.splitlines():
            line = line.strip()
            
            m = p0.match(line)
            if m:
                if 'fan_info' not in fan_dict:
                    result_dict = fan_dict.setdefault('fan_info',{})
                fan = m.groupdict()['fan']
                result_dict[fan] = {}

            m = p1.match(line)
            if m:
                if 'fan_info' not in fan_dict:
                    result_dict = fan_dict.setdefault('fan_info',{})
                state = m.groupdict()['state']
                result_dict[fan]['State'] = state

            m = p2.match(line)
            if m:
                if 'fan_info' not in fan_dict:
                    result_dict = fan_dict.setdefault('fan_info',{})
                speed = m.groupdict()['speed']
                result_dict[fan]['Speed'] = speed
                
            m = p3.match(line)
            if m:
                if 'fan_info' not in fan_dict:
                    result_dict = fan_dict.setdefault('fan_info',{})
                temp = m.groupdict()['temp']
                result_dict[fan]['Temperature'] = temp
                continue

        return fan_dict