# Python
import re
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any

# =============================================================================
# Schema for 'show  platform software fed {switch} active punt asic-cause brief'
# =============================================================================
class ShowPlatformSoftwareFedActivePuntAsicCauseBriefSchema(MetaParser):
    """Schema for show platform software fed {switch} active punt asic-cause brief"""
    schema = {
        'cause_name':{
             Any(): {
                'source': str,
                'rx_cur': int,
                'rx_delta': int,
                'drop_cur': int,
                'drop_delta': int,
            }
        }
    }

# =============================================================================
# Parser for 'show  platform software fed {switch} active punt asic-cause brief'
# =============================================================================

class ShowPlatformSoftwareFedActivePuntAsicCauseBrief(ShowPlatformSoftwareFedActivePuntAsicCauseBriefSchema):
    """Parser for show platform software fed {switch} active punt asic-cause brief"""
 
    cli_command = ['show platform software fed {switch} active punt asic-cause brief',\
                    'show platform software fed active punt asic-cause brief']

    def cli(self, switch='', output=None):
        if output is None:
            if switch:
                output = self.device.execute(self.cli_command[0].format(switch=switch))
            else:
                output = self.device.execute(self.cli_command[1])

        # initial return dictionary
        ret_dict = {}

        # UKNWN   UNKNOWN                       218          218          218          218
        # INMIR   ARP MIRROR                    368          368            0            0
        p1 = re.compile(r'^(?P<source>\w+)(?:\s*)'
                        r'(?P<cause_name>\w+(\s(\S{1,}))+|(\w+\s)+\w*\S\w*\S*|\w*\S\w*\S|\w+((\s\w+){1,}))(?:\s*)'
                        r'(?P<rx_cur>\d+)(?:\s*)(?P<rx_delta>\d+)(?:\s*)(?P<drop_cur>\d+)(?:\s*)(?P<drop_delta>\d+)$')

        for line in output.splitlines():
            line = line.strip()
            
            # UKNWN   UNKNOWN                       218          218          218          218
            # INMIR   ARP MIRROR                    368          368            0            0      
            m = p1.match(line)
            if m:
                group = m.groupdict()
                cause_name = group.pop('cause_name')
                sub_dict = ret_dict.setdefault('cause_name', {}).setdefault(cause_name, {})
                source = group.pop('source')
                sub_dict['source'] = source
                sub_dict.update({k: int(v) for k, v in group.items()})
                continue

        return ret_dict