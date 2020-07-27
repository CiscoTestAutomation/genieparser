from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any
import re
import genie.parsergen as pg


class ShowOmpSummarySchema(MetaParser):
# =====================================
# Parser for 'show omp summary'
# =====================================
 schema = {
        'admin_state': str,
        'alert_received': str,
        'alert_sent': str,
        'handshake_received': str,
        'handshake_sent': str,
        'hello_received': str,
        'hello_sent': str,
        'inform_received': str,
        'inform_sent': str,
        'mcast_routes_received': str,
        'mcast_routes_sent': str,
        'omp_uptime': str,
        'oper_state': str,
        'personality': str,
        'policy_received': str,
        'policy_sent': str,
        'routes_installed': str,
        'routes_received': str,
        'routes_sent': str,
        'services_installed': str,
        'services_received': str,
        'services_sent': str,
        'tlocs_installed': str,
        'tlocs_received': str,
        'tlocs_sent': str,
        'total_packets_sent': str,
        'update_received': str,
        'update_sent': str,
        'vsmart_peers': str,
 }

class ShowOmpSummary(ShowOmpSummarySchema):

    """ Parser for "show omp summary" """

    exclude = ['uptime']

    cli_command = "show omp summary"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        p1 = re.compile(r'^(?P<key>[\w0-9\-]+) + (?P<value>[\d\w\:]+)$')

        for line in out.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                key = groups['key'].replace('-', '_').lower()
                parsed_dict.update({key: (groups['value'])})

        print(parsed_dict)

        return parsed_dict