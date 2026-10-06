"""show_nat.py

NXOS parsers for the following show commands:
    * show ip nat timeout
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser


class ShowIpNatTimeoutSchema(MetaParser):
    """Schema for show ip nat timeout"""

    schema = {
        'timeout_values': {
            'unit': str,
            'tcp': int,
            'udp': int,
            'dyn': int,
            'sampling': int,
            'syn': int,
            'finrst': int,
        },
    }


class ShowIpNatTimeout(ShowIpNatTimeoutSchema):
    """Parser for show ip nat timeout"""

    cli_command = 'show ip nat timeout'

    def cli(self, output=None, **kwargs):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # IP NAT Timeout values (in sec)
        p1 = re.compile(r'^IP +NAT +Timeout +values +\(in +(?P<unit>\w+)\)$')

        # TCP:3600
        # UDP:3600
        # DYN:3600
        # Sampling:43200
        # SYN:60
        # FINRST:60
        p2 = re.compile(r'^(?P<name>TCP|UDP|DYN|Sampling|SYN|FINRST):(?P<value>\d+)$')

        key_map = {
            'TCP': 'tcp',
            'UDP': 'udp',
            'DYN': 'dyn',
            'Sampling': 'sampling',
            'SYN': 'syn',
            'FINRST': 'finrst',
        }

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # IP NAT Timeout values (in sec)
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                timeout_values_dict = ret_dict.setdefault('timeout_values', {})
                timeout_values_dict['unit'] = groups['unit']
                continue

            # TCP:3600
            # UDP:3600
            # DYN:3600
            # Sampling:43200
            # SYN:60
            # FINRST:60
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                timeout_values_dict = ret_dict.setdefault('timeout_values', {})
                timeout_values_dict[key_map[groups['name']]] = int(
                    groups['value']
                )
                continue

        return ret_dict
