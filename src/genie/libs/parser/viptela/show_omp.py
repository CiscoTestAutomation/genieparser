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
        'alert_received': int,
        'alert_sent': int,
        'handshake_received': int,
        'handshake_sent': int,
        'hello_received': int,
        'hello_sent': int,
        'inform_received': int,
        'inform_sent': int,
        'mcast_routes_received': int,
        'mcast_routes_sent': int,
        'omp_uptime': str,
        'oper_state': str,
        'personality': str,
        'policy_received': int,
        'policy_sent': int,
        'routes_installed': int,
        'routes_received': int,
        'routes_sent': int,
        'services_installed': int,
        'services_received': int,
        'services_sent': int,
        'tlocs_installed': int,
        'tlocs_received': int,
        'tlocs_sent': int,
        'total_packets_sent': int,
        'update_received': int,
        'update_sent': int,
        'vsmart_peers': int,
 }

class ShowOmpSummary(ShowOmpSummarySchema):

    """ Parser for "show omp summary" """

    cli_command = "show omp summary"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        #show sdwan omp summary 
        #oper-state             UP
        # admin-state            UP
        # personality            vedge
        # omp-uptime             34:03:00:35
        # routes-received        5
        # routes-installed       3
        # routes-sent            2
        p1 = re.compile(r'^(?P<key>[\w0-9\-]+) + (?P<value>[\d\w\:]+)$')

        for line in out.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                key = groups['key'].replace('-', '_').lower()
                
                try:
                    value = int(groups['value'])
                except ValueError:
                    value = groups['value']

                parsed_dict.update({key: value})
        
        return parsed_dict