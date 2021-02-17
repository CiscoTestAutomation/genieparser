"""show_vdc.py

Parser for the following show commands:
    * show vdc
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# import parser utils
from genie.libs.parser.utils.common import Common

class ShowVdcResourceDetailSchema(MetaParser):
    """Schema for 
        * show vdc resource detail
        * show vdc resource {resource} detail
    """

    schema = {
        "resources": {
            Any(): {
                "total_used": int, 
                "total_unused": int, 
                "total_free": int, 
                "total_avail": int, 
                "total": int, 
                "vdcs": {
                    Any(): {
                        "min": int, 
                        "max": int, 
                        "used": int, 
                        "unused": int, 
                        "free": int, 
                    }
                }
            }
        }
    }

class ShowVdcResourceDetail(ShowVdcResourceDetailSchema):
    """Parser for
        * show vdc resource detail
        * show vdc resource {resource} detail
    """
    
    cli_command = [
        'show vdc resource detail',
        'show vdc resource {resource} detail',
    ]

    def cli(self, resource=None, output=None):
        if not output:
            if resource:
                out = self.device.execute(self.cli_command[1].format(resource=resource))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        ret_dict = {}

        #   vlan               422 used     0 unused   3672 free   3672 avail   4094 total
        #   port-channel         2 used     0 unused    509 free    509 avail    511 total
        p1 = re.compile(r'^ *(?P<name>\S+) +(?P<total_used>\d+) +used +'
                        r'(?P<total_unused>\d+) +unused +(?P<total_free>\d+) +'
                        r'free +(?P<total_avail>\d+) +avail +(?P<total>\d+) +total$')

        #           example.cisco.com            16        4094      422       0         3672
        #           example.cisco.com            2         4096      2         0         4094
        p2 = re.compile(r'^ *(?P<name>\S+) +(?P<min>\d+) +(?P<max>\d+) +'
                        r'(?P<used>\d+) +(?P<unused>\d+) +(?P<free>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            #   vlan               422 used     0 unused   3672 free   3672 avail   4094 total
            #   port-channel         2 used     0 unused    509 free    509 avail    511 total
            m = p1.match(line)
            if m:
                group = m.groupdict()
                name = group.pop('name')
                resources_dict = ret_dict.setdefault('resources', {})
                resource_dict = resources_dict.setdefault(name, {})
                resource_dict.update({key:int(val) for key,val in group.items()})
                vdcs = resource_dict.setdefault('vdcs', {})                
                continue

            #           example.cisco.com            16        4094      422       0         3672
            #           example.cisco.com            2         4096      2         0         4094
            m = p2.match(line)
            if m:
                group = m.groupdict()
                name = group.pop('name')
                vdc_dict = vdcs.setdefault(name, {})
                vdc_dict.update({key:int(val) for key,val in group.items()})
                continue

        return ret_dict