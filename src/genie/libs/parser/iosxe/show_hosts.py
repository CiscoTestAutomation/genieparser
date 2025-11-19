"""show_hosts.py

IOSXE parsers for the following show commands:

    * show hosts

"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, ListOf


# ==============================================
#  Schema for show hosts
# ==============================================
class ShowHostsSchema(MetaParser):
    """Schema for show hosts"""

    schema = {
        Optional('default_domain'): str,
        Optional('name_servers'): ListOf(str),
        Optional('hosts'): {
            Any(): {
                'ttl': int,
                'class': str,
                'type': str,
                'data': str,
            }
        }
    }

# ==============================================
#  Parser for show hosts
# ==============================================
class ShowHosts(ShowHostsSchema):
    """Parser for show hosts"""

    cli_command = 'show hosts'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # Default domain is not set
        # Default domain is example.com
        p1 = re.compile(r'^Default\s+domain\s+is\s+(?P<domain>\S+)$')

        # Name servers are 171.70.168.183
        # Name servers are 171.70.168.183, 8.8.8.8
        p2 = re.compile(r'^Name\s+servers\s+are\s+(?P<servers>.+)$')

        # 252.254.255.223.in-addr.arpa   10      IN      PTR     sj20lab-tftp1
        # sj20lab-tftp1  10      IN      A       223.255.254.252
        p3 = re.compile(r'^(?P<name>\S+)\s+(?P<ttl>\d+)\s+(?P<class>\S+)\s+(?P<type>\S+)\s+(?P<data>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            if not line or line.startswith('NAME') or line.startswith('-'):
                continue

            # Default domain is not set
            # Default domain is example.com
            m = p1.match(line)
            if m:
                group = m.groupdict()
                domain = group['domain']
                if domain != 'not' and domain != 'set':
                    ret_dict['default_domain'] = domain
                continue

            # Name servers are 171.70.168.183
            # Name servers are 171.70.168.183, 8.8.8.8
            m = p2.match(line)
            if m:
                group = m.groupdict()
                servers = [server.strip() for server in group['servers'].split(',')]
                ret_dict['name_servers'] = servers
                continue

            # 252.254.255.223.in-addr.arpa   10      IN      PTR     sj20lab-tftp1
            # sj20lab-tftp1  10      IN      A       223.255.254.252
            m = p3.match(line)
            if m:
                group = m.groupdict()
                hosts_dict = ret_dict.setdefault('hosts', {})
                host_name = group['name']
                hosts_dict[host_name] = {
                    'ttl': int(group['ttl']),
                    'class': group['class'],
                    'type': group['type'],
                    'data': group['data']
                }
                continue

        return ret_dict