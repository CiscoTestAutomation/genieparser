import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any

# ===========================================
# Schema for 'show orchestrator connections'
# ===========================================


class ShowOrchestratorConnectionsSchema(MetaParser):
    """ Schema for "show orchestrator connections" """

    schema = {
        "remote_color": {
            Any(): {
                "peer_system_ip": {
                    Any(): {
                        "domain_id": str,
                        "peer_private_ip": str,
                        "peer_private_port": str,
                        "peer_protocol": str,
                        "peer_public_ip": str,
                        "peer_public_port": str,
                        "peer_instance": str,
                        "peer_type": str,
                        "site_id": str,
                        "state": str,
                        "organization_name": str,
                        "uptime": str,
                    },
                },
            },
        },
    }


# ===========================================
# Parser for 'show orchestrator connections'
# ===========================================


class ShowOrchestratorConnections(ShowOrchestratorConnectionsSchema):
    """ Parser for "show orchestrator connections" """

    cli_command = "show orchestrator connections"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        #  0        vedge    dtls     10.114.254.5     202010012   1           10.114.11.1      12346    10.114.11.1      12346   custom1          up              sdwan-svs           25:15:04:11

        # Will match single word org names, double/triple and more word org names separated by a hypen or underscore
        p1 = re.compile(
            r"(?P<peer_instance>\w+)\s+(?P<peer_type>\w+)\s+(?P<peer_protocol>\w+)\s+(?P<peer_system_ip>\S+)"
            r"\s+(?P<site_id>\d+)\s+(?P<domain_id>\d+)\s+(?P<peer_private_ip>\S+)"
            r"\s+(?P<peer_private_port>\d+)\s+(?P<peer_public_ip>\S+)\s+"
            r"(?P<peer_public_port>\d+)\s+(?P<remote_color>\S+)\s+\s+(?P<state>\S+)\s+"
            r"(?P<organization_name>\w+-?\w+-?\w+?)\s+(?P<uptime>\S+)"
        )

        for line in out.splitlines():
            line = line.strip()

            # helper text
            m = p1.match(line)
            if m:
                group = m.groupdict()
                color = group["remote_color"]

                parsed_dict.setdefault("remote_color", {}). \
                    setdefault(color, {})
                connection_dict = parsed_dict["remote_color"][color]. \
                    setdefault("peer_system_ip", {})
                color_dict = connection_dict.setdefault(group["peer_system_ip"], {})

                keys = ["peer_instance", "peer_type", "peer_protocol", "site_id", \
                        "domain_id", "peer_private_ip", "peer_private_port", \
                        "peer_public_ip", "peer_public_port", "state", \
                        "organization_name", "uptime"]

                for k in keys:
                    color_dict[k] = group[k]

                continue

        return parsed_dict
