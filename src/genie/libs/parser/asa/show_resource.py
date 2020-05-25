""" show_resource.py

Parser for the following show commands:
    * show resource usage
"""

import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                                Any, \
                                                Optional


# =============================================
# Schema for 'show resource usage'
# =============================================
class ShowResourceUsageSchema(MetaParser):
    """Schema for
        * show resource usage
    """
    schema = {
        'context': {
            Any(): {
                'resource': {
                    Any(): {
                        'current': int,
                        'peak': int,
                        Optional('limit'): int,
                        'denied': int,
                    }
                }
            }
        }
    }


# =============================================
# Parser for 'show resource usage'
# =============================================
class ShowResourceUsage(ShowResourceUsageSchema):
    """Parser for
        * show resource usage
    """

    cli_command = 'show resource usage'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # --------------------------------------------------------
        # Regular expression patterns
        # --------------------------------------------------------
        # Resource              Current         Peak      Limit        Denied Context
        # SSH                         1            5          5             0 System
        # Syslogs [rate]             18          861        N/A             0 System

        p = re.compile(r'^^(?P<resource>[\s\S]+)\s+(?P<current>\d+)\s+'
                       r'(?P<peak>\d+)\s+(?P<limit>\d+|N\/A)\s+'
                       r'(?P<denied>\d+)\s+(?P<context>\S+)$$')

        # --------------------------------------------------------
        # Parse the output
        # --------------------------------------------------------
        for line in out.splitlines():
            line = line.strip()

            m = p.match(line)
            if m:
                group = m.groupdict()
                context_dict = parsed_dict.setdefault('context', {}).\
                                            setdefault(group['context'], {})
                resource_dict = context_dict.setdefault('resource', {}).\
                                            setdefault(group['resource'].strip(), {})

                for k in ['current', 'peak', 'limit', 'denied']:
                    if group[k] != 'N/A':
                        resource_dict[k] = int(group[k])
                    continue

        return parsed_dict
