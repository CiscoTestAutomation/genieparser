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


# =====================================================
# Schema for 'show orchestrator reverse-proxy-mapping'
# ====================================================

class ShowOrchestratorReverseProxyMappingSchema(MetaParser):
    """ Schema for "show orchestrator reverse-proxy-mapping" """

    schema = {
        'total_mappings' : int,
        'uuid' : {
            Any() : {
                Any() : {
                    'private_ip' : str,
                    'private_port' : str,
                    'proxy_ip' : str,
                    'proxy_port' : str
                }
            }
        }
    }

# ===========================================
# Parser for 'show orchestrator connections'
# ===========================================

class ShowOrchestratorReverseProxyMapping(ShowOrchestratorReverseProxyMappingSchema):
    """ Parser for "show orchestrator reverse-proxy-mapping" """

    cli_command = "show orchestrator reverse-proxy-mapping"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command + '| tab')
        else:
            output = output

        ret_dict = {}
        rp_dict = {}
        counter_dict = {}

        #2153b38d-09fe-413e-a70a-bb5a7c7453e4  26.0.1.20        23456    99.99.99.184  23456  
        #2153b38d-09fe-413e-a70a-bb5a7c7453e4  2600:0:0:1::20   23456    9999::184     23456  
        p1 = re.compile(r'^\s*(?P<uuid>[a-zA-Z0-9\-]+)\s+(?P<private_ip>[\d\.]+]|[a-fA-F\d\:]+)\s+'
                        r'(?P<private_port>\d+)\s+(?P<proxy_ip>[\d\.]+|[a-fA-F\d\:]+)\s+(?P<proxy_port>\d+)\s*$')

        for line in output.splitlines():
            if not line:
                continue

            #2153b38d-09fe-413e-a70a-bb5a7c7453e4  26.0.1.20        23456    99.99.99.184  23456  
            #2153b38d-09fe-413e-a70a-bb5a7c7453e4  2600:0:0:1::20   23456    9999::184     23456  
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                uuid = groups['uuid']
                rp_dict = ret_dict.setdefault('uuid', {})

                if uuid in counter_dict:
                    counter_dict[uuid] = counter_dict[uuid] + 1
                else:
                    counter_dict[uuid] = 1

                uuid_map_dict = rp_dict.setdefault(uuid, {})
                map_dict = uuid_map_dict.setdefault(counter_dict[uuid],{})
                map_dict['private_ip'] = groups['private_ip']
                map_dict['private_port'] = groups['private_port']
                map_dict['proxy_ip'] = groups['proxy_ip']
                map_dict['proxy_port'] = groups['proxy_port']

                continue

        # Code to count total numer of reverser-proxy mappings
        total_mappings = 0
        for mapping_count_per_uuid in counter_dict:
            total_mappings += counter_dict[mapping_count_per_uuid]    
        ret_dict['total_mappings'] = total_mappings

        return ret_dict
