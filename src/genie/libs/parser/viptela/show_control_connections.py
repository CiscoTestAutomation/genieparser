# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
from genie import parsergen
from pprint import pprint
import re

# ===========================================
# Schema for 'show control connections'
# ===========================================


class ShowControlConnectionsSchema(MetaParser):

    """ Schema for "show control connections" """

    schema = {
        "control_connections": {
            Any(): {
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
                    "uptime": str,
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
            "\s+(?P<site_id>\d+)\s+(?P<domain_id>\d+)\s+(?P<peer_private_ip>\S+)"
            "\s+(?P<peer_private_port>\d+)\s+(?P<peer_public_ip>\S+)\s+"
            "(?P<peer_public_port>\d+)\s+(?P<local_color>\S+)\s+(?P<proxy_state>\w+)"
            "\s+(?P<uptime>\S+)\s+(?P<controller_group_id>\S+)"
        )

        for line in out.splitlines():
            line = line.strip()

            # helper text
            m = p1.match(line)
            if m:
                group = m.groupdict()
                color = group["local_color"]
                parsed_dict.setdefault("control_connections", {}).setdefault(color, {})
                connection_dict = parsed_dict["control_connections"][color]
                color_dict = connection_dict.setdefault(group["peer_system_ip"], {})
                color_dict["peer_type"] = group["peer_type"]
                color_dict["peer_protocol"] = group["peer_protocol"]
                color_dict["site_id"] = group["site_id"]
                color_dict["domain_id"] = group["domain_id"]
                color_dict["peer_private_ip"] = group["peer_private_ip"]
                color_dict["peer_private_port"] = group["peer_private_port"]
                color_dict["peer_public_ip"] = group["peer_public_ip"]
                color_dict["peer_public_port"] = group["peer_public_port"]
                color_dict["proxy_state"] = group["proxy_state"]
                color_dict["uptime"] = group["uptime"]
                color_dict["controller_group_id"] = group["controller_group_id"]

                continue

        return parsed_dict

