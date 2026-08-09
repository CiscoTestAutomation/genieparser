"""starOS implementation of show_resources.py

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema

class ResourcesSchema(MetaParser):
    """Schema for show resources"""

    schema = {
        'resources_info': {
            Any():{
            'License':str
            },
        }
    }


class ShowResources(ResourcesSchema):
    """Parser for show resources"""

    cli_command = 'show resources'

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
        resources_dict = {}
        
        result_dict = {}

        # initial regexp pattern
        p2 = re.compile(r'^(?P<service>\w+)\sService:')
        p3 = re.compile(r'^License\sStatus\s+:\s(?P<license>.+$)')

        for line in out.splitlines():
            line = line.strip()
            
            m = p2.match(line)
            if m:
                if 'resources_info' not in resources_dict:
                    result_dict = resources_dict.setdefault('resources_info',{})
                service = m.groupdict()['service']
                result_dict[service] = {}
                
            m = p3.match(line)
            if m:
                if 'resources_info' not in resources_dict:
                    result_dict = resources_dict.setdefault('resources_info',{})
                license = m.groupdict()['license']
                result_dict[service]['License'] = license
                continue

        return resources_dict