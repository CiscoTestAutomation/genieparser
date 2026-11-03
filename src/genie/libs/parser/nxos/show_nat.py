"""show_nat.py

NXOS parsers for the following show commands:
    * show ip nat max
    * show ip nat timeout
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser


class ShowIpNatMaxSchema(MetaParser):
    """Schema for show ip nat max"""

    schema = {
        'max_dyn_translations': int,
        'max_all_host': int,
        'no_static': int,
        'no_dyn': int,
        'no_dyn_icmp': int,
    }


class ShowIpNatMax(ShowIpNatMaxSchema):
    """Parser for show ip nat max"""

    cli_command = 'show ip nat max'

    def cli(self, output=None, **kwargs):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # IP NAT Max values
        p1 = re.compile(r'^IP +NAT +Max +values$')

        # Max Dyn Translations:80
        p2 = re.compile(r'^Max +Dyn +Translations:(?P<max_dyn_translations>\d+)$')

        # Max all-host:0
        p3 = re.compile(r'^Max +all-host:(?P<max_all_host>\d+)$')

        # No.Static:650
        p4 = re.compile(r'^No\.Static:(?P<no_static>\d+)$')

        # No.Dyn:0
        p5 = re.compile(r'^No\.Dyn:(?P<no_dyn>\d+)$')

        # No.Dyn-ICMP:0
        p6 = re.compile(r'^No\.Dyn-ICMP:(?P<no_dyn_icmp>\d+)$')

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # IP NAT Max values
            m = p1.match(line)
            if m:
                continue

            # Max Dyn Translations:80
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['max_dyn_translations'] = int(
                    groups['max_dyn_translations']
                )
                continue

            # Max all-host:0
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['max_all_host'] = int(groups['max_all_host'])
                continue

            # No.Static:650
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['no_static'] = int(groups['no_static'])
                continue

            # No.Dyn:0
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['no_dyn'] = int(groups['no_dyn'])
                continue

            # No.Dyn-ICMP:0
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['no_dyn_icmp'] = int(groups['no_dyn_icmp'])
                continue

        return ret_dict


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
