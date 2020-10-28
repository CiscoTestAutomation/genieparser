import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# =======================================
# Schema for:
#  * 'show telemetry internal connection'
# =======================================
class ShowTelemetryInternalConnectionSchema(MetaParser):
    """Schema for show telemetry internal connection."""

    schema = {
        Optional("peer_address"): str,
        Optional("port"): int,
        Optional("profile"): str,
        Optional("source_address"): str,
        Optional("state"): str,
        Optional("transport"): str,
        Optional("vrf"): int,
        Optional("index"): {
            int: {
                "peer_address": str,
                "port": int,
                "source_address": str,
                "state": str,
                "vrf": int,
            },
        },
    }


# =======================================
# Parser for:
#  * 'show telemetry internal connection'
# =======================================
class ShowTelemetryInternalConnection(ShowTelemetryInternalConnectionSchema):
    """Parser for show telemetry internal connection"""

    cli_command = "show telemetry internal connection"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)

        else:
            out = output

        # Telemetry connection

        # Peer Address    Port  VRF Source Address  Transport  State         Profile
        # --------------- ----- --- --------------- ---------- ------------- -------------
        # 10.37.174.7    25103   0 10.8.138.4      tls-native Active        sdn-network-101-wan

        # 10.37.174.7    25103   0 10.8.138.4      tls-native Active        sdn-network-101-wan
        no_index_capture = re.compile(
            r"^(?P<peer_address>\d+\.\d+\.\d+\.\d+)\s+(?P<port>\d+)\s+(?P<vrf>\d+)\s+(?P<source_address>\d+\.\d+\.\d+\.\d+)\s+(?P<transport>\S+)\s+(?P<state>\S+)\s+(?P<profile>\S+)$"
        )

        # 6 10.10.76.186              20830   0 10.64.47.177               Active
        index_capture = re.compile(
            r"(?P<index>\d+)\s+(?P<peer_address>[\d.]+)\s+(?P<port>\d+)\s+(?P<vrf>\d+)\s+(?P<source_address>\d+\.\d+\.\d+\.\d+)\s+(?P<state>\S+)"
        )

        tele_info_obj = {}

        for line in out.splitlines():
            line = line.strip()

            match = no_index_capture.match(line)
            if match:
                group = match.groupdict()

                # convert str to int
                int_list = ["port", "vrf"]
                for item in int_list:
                    group[item] = int(group[item])

                tele_info_obj.update(group)

                continue

            match = index_capture.match(line)
            if match:
                group = match.groupdict()

                # convert str to int
                int_list = ["port", "vrf", "index"]
                for item in int_list:
                    group[item] = int(group[item])

                # pull a key from group to use as new_key
                new_key = "index"
                new_group = {group[new_key]: {}}

                # update and pop new_key
                new_group[group[new_key]].update(group)
                new_group[group[new_key]].pop(new_key)

                if not tele_info_obj.get(new_key):
                    tele_info_obj = {new_key: {}}

                tele_info_obj[new_key].update(new_group)

                continue

        return tele_info_obj