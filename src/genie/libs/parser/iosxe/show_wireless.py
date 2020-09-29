import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ========================================
# Schema for:
#  * 'show wireless stats ap join summary'
# ========================================
class ShowWirelessStatsApJoinSummarySchema(MetaParser):
    """Schema for show wireless stats ap join summary."""

    schema = {
        "ap_count": int,
        "base_mac": {
            Any(): {
                "ap_name": str,
                "disconnect_reason": str,
                "failure_phase": str,
                "ip_address": str,
                "status": str,
                "visitors_mac": str,
            }
        },
    }


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

        # Number of APs: 61

        # Base MAC        visitors MAC    AP Name                           IP Address                                Status      Last Failure Phase    Last Disconnect Reason
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # 706d.0598.6fc0  706d.0598.0320  AP706d.0598.0320                  10.10.116.22                             Not Joined  Join                  Ap auth pending
        # 706d.0544.d2c0  706d.0544.1bf0  visitors-hydra                    10.10.78.156                              Not Joined  Join                  Ap auth pending
        # 706d.0544.d580  706d.0544.1ca0  visitors-hydra                    10.10.82.200                             Not Joined  Join                  Ap auth pending
        # 0042.5a0a.1fb0  006b.f116.0ff0  visitors-1815i                     10.10.139.90                             Joined      Join                  Ap auth pending
        # 706d.0593.aac0  706d.0592.5148  visitors-hydra2                   10.10.36.138                               Not Joined  Join                  Ap auth pending
        # 706d.0593.ae20  706d.0592.5220  visitors-hydra5                   10.10.36.138                               Not Joined  Join                  Ap auth pending
        # 00be.7506.42c0  706d.0568.44d0  visitors-1815t                      10.10.236.197                            Joined      Join                  Ap auth pending
        # 706d.05be.6890  706d.053e.e3f0  visitors-1815i                    10.10.152.239                            Joined      Join                  Ap auth pending
        # 706d.05be.adc0  706d.053e.f540  visitors-mallorca                  10.10.40.15                              Not Joined  Join                  Ap auth pending
        # 706d.05be.bc20  706d.053e.f8d8  visitors-mallorca                  10.10.7.234                              Not Joined  Join                  Ap auth pending

        # Number of APs: 61
        ap_count_capture = re.compile(r"^Number of APs:\s+(?P<ap_count>\d+)$")

        # 706d.0598.6fc0  706d.0598.0320  AP706d.0598.0320                  10.10.116.22                             Not Joined  Join                  Ap auth pending
        ap_join_capture = re.compile(
            # 706d.0598.6fc0
            r"^(?P<base_mac>[a-f0-9]{4}\.[a-f0-9]{4}\.[a-f0-9]{4})\s+"
            # 706d.0598.0320
            r"(?P<visitors_mac>[a-f0-9]{4}\.[a-f0-9]{4}\.[a-f0-9]{4})\s+"
            # AP706d.0598.0320
            r"(?P<ap_name>\S+)\s+"
            # 10.10.116.22
            r"(?P<ip_address>[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\s+"
            # Not Joined
            r"(?P<status>Not Joined|Joined)\s+"
            # Join
            r"(?P<failure_phase>\S+)\s+"
            # Ap auth pending
            r"(?P<disconnect_reason>.*)$"
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

                # pull the base_mac to use as keys then pop it from the dict
                ap_info_dict = {group["base_mac"]: {}}
                ap_info_dict[group["base_mac"]].update(group)
                ap_info_dict[group["base_mac"]].pop("base_mac")

                if not wireless_info_obj.get("base_mac"):
                    wireless_info_obj["base_mac"] = {}

                wireless_info_obj["base_mac"].update(ap_info_dict)

        return wireless_info_obj