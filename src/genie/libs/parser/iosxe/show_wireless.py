import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ========================================
# Schema for:
#  * 'show wireless stats ap join summary'
# ========================================
class ShowWirelessStatsApJoinSummarySchema(MetaParser):
    """Schema for show wireless stats ap join summary."""

    schema = {}


# ========================================
# Parser for:
#  * 'show wireless stats ap join summary'
# ========================================
class ShowWirelessStatsApJoinSummary(ShowWirelessStatsApJoinSummarySchema):
    """Parser for show wireless stats ap join summary"""

    cli_command = ["show wireless stats ap join summary"]

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])
        else:
            output = output

        ap_count_capture = re.compile(r"^Number of APs:\s+(?P<ap_count>\d+)$")

        ap_join_capture = re.compile(
            r"^"
            r"(?P<base_mac>[a-f0-9]{4}\.[a-f0-9]{4}\.[a-f0-9]{4})\s+"
            r"(?P<visitors_mac>[a-f0-9]{4}\.[a-f0-9]{4}\.[a-f0-9]{4})\s+"
            r"(?P<ap_name>\S+)\s+(?P<ip_address>[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\s+"
            r"(?P<status>Not Joined|Joined)\s+"
            r"(?P<failure_phase>\S+)\s+"
            r"(?P<disconnect_reason>.*)"
            r"$"
        )

        wireless_info_obj = {}

        for line in output.splitlines():
            line = line.strip()

            if ap_count_capture.match(line):
                ap_count_match = ap_count_capture.match(line)

                # only grab the first entry from output
                if not wireless_info_obj.get("ap_count"):
                    group = ap_count_match.groupdict()
                    wireless_info_obj.update(group)

            if ap_join_capture.match(line):
                ap_join_match = ap_join_capture.match(line)
                group = ap_join_match.groupdict()

                ap_info_dict = {group["base_mac"]: {}}
                ap_info_dict[group["base_mac"]].update(group)
                ap_info_dict[group["base_mac"]].pop("base_mac")

                if not wireless_info_obj.get("base_mac"):
                    wireless_info_obj["base_mac"] = {}

                wireless_info_obj["base_mac"].update(ap_info_dict)

        return wireless_info_obj