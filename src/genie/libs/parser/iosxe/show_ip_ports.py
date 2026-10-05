"""Parser for show ip ports all."""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or


class ShowIpPortsAllSchema(MetaParser):
    """Schema for show ip ports all."""

    schema = {
        'connections': {
            Any(): {
                'protocol': str,
                'local_address': str,
                'local_port': Or(int, str),
                'foreign_address': str,
                'foreign_port': Or(int, str),
                Optional('state'): str,
                Optional('pid'): int,
                'program_name': str,
            }
        }
    }


class ShowIpPortsAll(ShowIpPortsAllSchema):
    """Parser for show ip ports all."""

    cli_command = 'show ip ports all'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        connection_index = 0

        # tcp *:443 *:* LISTEN 324/[IOS]HTTP CORE
        # udp 1.2.43.1:646 *:* 593/[IOS]LDP Hello
        p1 = re.compile(
            r'^(?P<protocol>[A-Za-z][\w-]*)\s+'
            r'(?P<local_address>\S+):(?P<local_port>[^:\s]+)\s+'
            r'(?P<foreign_address>\S+):(?P<foreign_port>[^:\s]+)\s+'
            r'(?:(?P<state>[A-Z][A-Z0-9-]*)\s+)?'
            r'(?:(?P<pid>\d+)/)?(?P<program_name>.+)$'
        )

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # tcp *:443 *:* LISTEN 324/[IOS]HTTP CORE
            # udp 1.2.43.1:646 *:* 593/[IOS]LDP Hello
            match = p1.match(line)
            if not match:
                continue

            group = match.groupdict()
            connection_index += 1
            local_port = group['local_port']
            foreign_port = group['foreign_port']
            connection_dict = {
                'protocol': group['protocol'],
                'local_address': group['local_address'],
                'local_port': int(local_port) if local_port.isdigit() else local_port,
                'foreign_address': group['foreign_address'],
                'foreign_port': (
                    int(foreign_port) if foreign_port.isdigit() else foreign_port
                ),
                'program_name': group['program_name'].strip(),
            }
            if group['state']:
                connection_dict['state'] = group['state']
            if group['pid']:
                connection_dict['pid'] = int(group['pid'])
            ret_dict.setdefault('connections', {})[connection_index] = connection_dict

        return ret_dict
