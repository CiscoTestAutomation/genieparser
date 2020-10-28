"""
show_ip_demo.py

IOSXE parsers for the following show commands:
    * show ip aliases

"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


class ShowIpAliasSchema(MetaParser):

    schema = {
        'vrf': {
            Any(): {
                'index': {
                    Any(): {
                        'address_type': str,
                        'ip_address': str,
                        Optional('port'): int,
                    }
                }
            }
        }
    }

class ShowIpAliases(ShowIpAliasSchema):
    """
    Parser for:
        * show ip aliases
    """

    cli_command = ['show ip aliases', 'show ip aliases vrf {vrf}']

    def cli(self, vrf=None, output=None):
        if not output:
            if not vrf:
                cmd = self.cli_command[0]
            else:
                cmd = self.cli_command[1].format(vrf=vrf)

            output = self.device.execute(cmd)

        ret_dict = {}

        if not vrf:
            vrf = 'default'

        index = 0

        # Interface                10.169.197.94
        # Interface                10.169.197.94         80
        p1 = re.compile(r"^(?P<address_type>\S+) +(?P<ip_address>\S+)(?: +(?P<port>\d+))?$")

        for line in output.splitlines():
            line = line.strip()

            # Interface                10.169.197.94
            # Interface                10.169.197.94         80
            m = p1.match(line)
            if m:
                group = m.groupdict()
                index += 1

                index_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {}).\
                    setdefault('index', {}).setdefault(index, {})

                index_dict.update({'address_type': group['address_type']})
                index_dict.update({'ip_address': group['ip_address']})

                if group['port']:
                    index_dict.update({'port': int(group['port'])})

                continue

        return ret_dict













