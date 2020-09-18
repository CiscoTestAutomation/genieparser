import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ===================================
# Schema for:
#  * 'show wireless mobility ap-list'
# ===================================
class ShowWirelessMobilityApListSchema(MetaParser):
    """Schema for show wireless mobility ap-list."""

    schema = {
        "ap_name": {
            Any(): {
                "ap_radio_mac": str,
                "controller_ip": str,
                "learnt_from": str,
            }
        }
    }


# ===================================
# Parser for:
#  * 'show wireless mobility ap-list'
# ===================================
class ShowWirelessMobilityApList(ShowWirelessMobilityApListSchema):
    """Parser for show wireless mobility ap-list"""

    cli_command = ["show wireless mobility ap-list"]

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])
        else:
            output = output

        # AP name                           AP radio MAC      Controller IP     Learnt from
        # --------------------------------------------------------------------------------------
        # b80-72-cap30                    58bf.eab3.1420    10.10.7.177      Self
        # b80-81-cap4                     58bf.ea13.62a0    10.10.7.177      Self
        # b80-52-cap6                     58bf.ea13.75e0    10.10.7.177      Self

        # AP name                           AP radio MAC      Controller IP     Learnt from
        ap_header_capture = re.compile(
            r"^AP\s+name\s+AP\s+radio\s+MAC\s+Controller\s+IP\s+Learnt\s+from$"
        )

        # b80-72-cap30                    58bf.eab3.1420    10.10.7.177      Self
        ap_info_capture = re.compile(
            r"^(?P<ap_name>\S+)\s+(?P<ap_radio_mac>\S{4}\.\S{4}\.\S{4})\s+(?P<controller_ip>\d+\.\d+\.\d+\.\d+)\s+(?P<learnt_from>\S+)$"
        )

        ap_info_obj = {}

        for line in output.splitlines():

            line = line.strip()

            if ap_header_capture.match(line):
                continue

            elif ap_info_capture.match(line):
                ap_info_capture_match = ap_info_capture.match(line)
                groups = ap_info_capture_match.groupdict()

                if not ap_info_obj.get("ap_name", {}):
                    ap_info_obj["ap_name"] = {}

                ap_name_dict = {
                    # ap_name: b80-72-cap30
                    groups["ap_name"]: {
                        # radio_mac: 58bf.eab3.1420
                        "ap_radio_mac": groups["ap_radio_mac"],
                        # controller_ip: 10.10.7.177
                        "controller_ip": groups["controller_ip"],
                        # learnt_from: Self
                        "learnt_from": groups["learnt_from"],
                    }
                }

                ap_info_obj["ap_name"].update(ap_name_dict)

        return ap_info_obj
