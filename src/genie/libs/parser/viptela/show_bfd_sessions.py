from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any
import re

# =====================================
# Schema for 'show bfd sessions'
# =====================================


class ShowBfdSessionsSchema(MetaParser):

    """ Schema for "show bfd sessions" command """

    schema = {
        "system_ip": {
            Any(): {
                'source_tloc_color': {
                    Any(): {
                        "destination_public_ip": str,
                        "destination_public_port": str,
                        "detect_multiplier": str,
                        "encapsulation": str,
                        "site_id": str,
                        "source_ip": str,
                        "remote_tloc_color": str,
                        "state": str,
                        "transitions": str,
                        "tx_interval": str,
                        "uptime": str,
                    },
                },
            },
        },
    }


# =====================================
# Parser for 'show bfd sessions'
# =====================================

class ShowBfdSessions(ShowBfdSessionsSchema):

    """ Parser for "show bfd sessions" """

    exclude = ['uptime']

    cli_command = "show bfd sessions"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # 172.16.241.1     30001001 up          mpls             mpls             172.16.189.2    172.16.171.2       12346       ipsec  20          1000           0:01:46:50      0            
        p1 = re.compile(
            r"(?P<system_ip>\S+)\s+(?P<site_id>\d+)\s+(?P<state>\w+)\s+"
            r"(?P<source_tloc_color>\S+)\s+(?P<remote_tloc_color>\S+)\s+"
            r"(?P<source_ip>\S+)\s+(?P<destination_public_ip>\S+)\s+"
            r"(?P<destination_public_port>\d+)\s+(?P<encapsulation>\w+)\s+"
            r"(?P<detect_multiplier>\d+)\s+(?P<tx_interval>\d+)\s+"
            r"(?P<uptime>\S+)\s+(?P<transitions>\d+)"
        )

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                system_ip = group["system_ip"]

                parsed_dict.setdefault("system_ip", {}).\
                            setdefault(system_ip, {})

                session_dict = parsed_dict["system_ip"][system_ip].\
                                    setdefault("source_tloc_color", {})
                                    
                ip_dict = session_dict.setdefault(group["source_tloc_color"], {})

                keys = ["site_id", "state", "source_ip", "remote_tloc_color",\
                        "destination_public_ip", "destination_public_port",\
                        "encapsulation", "detect_multiplier",\
                        "tx_interval", "uptime", "transitions"]

                for k in keys:
                    ip_dict[k] = group[k]

                continue

        return parsed_dict



