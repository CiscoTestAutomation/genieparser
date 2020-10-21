from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import re

# =======================================
# Schema for 'show boot-partition' introduced in vEdge version 14.1
# =======================================

class ShowBootPartitionSchema(MetaParser):
    schema = {
            'partition': {
                Any(): {
                    'active': str,
                    'version': str,
                    'timestamp': str,
                }
            }
        }

class ShowBootPartition(ShowBootPartitionSchema):
    """Parser for 'show boot-partition' on Viptela vEdge
    appliances - CLI"""
    cli_command = 'show boot-partition'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}
        
        # 1          X       14.2.4   2014-11-11T18:16:49+00:00
        # 2          -       14.2.3   2014-11-11T18:35:14+00:00
        p1 = re.compile(r'^(?P<partition>\d+) +(?P<active>\S+) +(?P<version>\S+) +(?P<timestamp>\S+)')

        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue
            
            # 1          X       14.2.4   2014-11-11T18:16:49+00:00
            # 2          -       14.2.3   2014-11-11T18:35:14+00:00
            m = p1.match(line)
            if m:
                group = m.groupdict()
                partition=int(group['partition'])
                partition_dict = result_dict.setdefault('partition', {}).setdefault(partition, {})
                partition_dict.update({'active': group['active']})
                partition_dict.update({'version': group['version']})
                partition_dict.update({'timestamp': group['timestamp']})
                continue
        
        return result_dict
