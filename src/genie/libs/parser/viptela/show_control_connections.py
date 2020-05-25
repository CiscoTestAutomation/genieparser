# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
from genie import parsergen

import re

# ===========================================
# Schema for 'show control connections'
# ===========================================


class ShowControlConnectionsSchema(MetaParser):

    """ Schema for "show control connections" """

    schema = {
        "local_color": {
            Any(): {
                "peer_system_ip": {
                    Any(): {
                        "controller_group_id": str,
                        "domain_id": str,
                        "peer_private_ip": str,
                        "peer_private_port": str,
                        "peer_protocol": str,
                        "peer_public_ip": str,
                        "peer_public_port": str,
                        "peer_type": str,
                        "proxy_state": str,
                        "site_id": str,
                        "state": str,
                        "uptime": str,
                    },
                },
            },
        },
    }


# ===========================================
# Parser for 'show control connections'
# ===========================================


class ShowControlConnections(ShowControlConnectionsSchema):

    """ Parser for "show control connections" """

    cli_command = "show control connections"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        #                                                                                        PEER                                          PEER                                          CONTROLLER 
        # PEER    PEER PEER            SITE       DOMAIN PEER                                    PRIV  PEER                                    PUB                                           GROUP      
        # TYPE    PROT SYSTEM IP       ID         ID     PRIVATE IP                              PORT  PUBLIC IP                               PORT  LOCAL COLOR     PROXY STATE UPTIME      ID         
        # vsmart  tls  172.16.255.19   300        1      10.0.12.19                              23556 10.0.37.19                              23556 lte             Yes   up     0:00:16:22  0        
        p1 = re.compile(
            r"(?P<peer_type>\w+)\s+(?P<peer_protocol>\w+)\s+(?P<peer_system_ip>\S+)"
            r"\s+(?P<site_id>\d+)\s+(?P<domain_id>\d+)\s+(?P<peer_private_ip>\S+)"
            r"\s+(?P<peer_private_port>\d+)\s+(?P<peer_public_ip>\S+)\s+"
            r"(?P<peer_public_port>\d+)\s+(?P<local_color>\S+)\s+(?P<proxy_state>\w+)"
            r"\s+(?P<state>\S+)\s+(?P<uptime>\S+)\s+(?P<controller_group_id>\S+)"
        )

        for line in out.splitlines():
            line = line.strip()

            # helper text
            m = p1.match(line)
            if m:
                group = m.groupdict()
                color = group["local_color"]

                parsed_dict.setdefault("local_color", {}).\
                            setdefault(color, {})
                connection_dict = parsed_dict["local_color"][color].\
                                    setdefault("peer_system_ip", {})
                color_dict = connection_dict.setdefault(group["peer_system_ip"], {})
                
                keys = ["peer_type", "peer_protocol", "site_id", \
                        "domain_id", "peer_private_ip", "peer_private_port",\
                        "peer_public_ip", "peer_public_port", "proxy_state",\
                        "uptime", "state", "controller_group_id"]
                
                for k in keys:
                    color_dict[k] = group[k]

                continue

        return parsed_dict

