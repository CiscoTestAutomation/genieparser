from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any
from pprint import pprint
import re

# =====================================
# Schema for 'show sdwan bfd sessions'
# =====================================


class ShowSdwanBfdSessionsSchema(MetaParser):

    """ Schema for "show sdwan bfd sessions """

    schema = {
        "bfd_sessions": {
            Any(): {
                Any(): {
                    "destination_public_ip": str,
                    "destination_public_port": str,
                    "detect_multiplier": str,
                    "encapsulation": str,
                    "remote_tloc_color": str,
                    "site_id": str,
                    "source_ip": str,
                    "state": str,
                    "transitions": str,
                    "tx_interval": str,
                    "uptime": str,
                },
            },
        },
    }


# =====================================
# Parser for 'show sdwan bfd sessions'
# =====================================

class ShowSdwanBfdSessions(ShowSdwanBfdSessionsSchema):

    """ Parser for "show sdwan bfd sessions" """

    cli_command = "show sdwan bfd sessions"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        p1 = re.compile(
            r"(?P<system_ip>\S+)\s+(?P<site_id>\d+)\s+(?P<state>\w+)\s+" \
            "(?P<source_tloc_color>\S+)\s+(?P<remote_tloc_color>\S+)\s+" \
            "(?P<source_ip>\S+)\s+(?P<destination_public_ip>\S+)\s+" \
            "(?P<destination_public_port>\d+)\s+(?P<encapsulation>\w+)\s+" \
            "(?P<detect_multiplier>\d+)\s+(?P<tx_interval>\d+)\s+" \
            "(?P<uptime>\S+)\s+(?P<transitions>\d+)"
        )

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                system_ip = group["system_ip"]
                parsed_dict.setdefault("bfd_sessions", {}).setdefault(system_ip, {})
                session_dict = parsed_dict["bfd_sessions"][system_ip]
                ip_dict = session_dict.setdefault(group["source_tloc_color"], {})
                ip_dict["site_id"] = group["site_id"]
                ip_dict["state"] = group["state"]
                ip_dict["source_ip"] = group["source_ip"]
                ip_dict["remote_tloc_color"] = group["remote_tloc_color"]
                ip_dict["destination_public_ip"] = group["destination_public_ip"]
                ip_dict["destination_public_port"] = group["destination_public_port"]
                ip_dict["encapsulation"] = group["encapsulation"]
                ip_dict["detect_multiplier"] = group["detect_multiplier"]
                ip_dict["tx_interval"] = group["tx_interval"]
                ip_dict["uptime"] = group["uptime"]
                ip_dict["transitions"] = group["transitions"]

                continue

        return parsed_dict



