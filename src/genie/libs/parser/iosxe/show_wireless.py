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
         Any(): {
             "controller_ip": str,
             "learnt_from": str,
             "radio_mac": str
         }
     }


# ===================================
# Parser for:
#  * 'show wireless mobility ap-list'
# ===================================
class ShowWirelessMobilityApList(ShowWirelessMobilityApListSchema):
    """Parser for show wireless mobility ap-list"""

    cli_command = ['show wireless mobility ap-list']

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])
        else:
            output = output

        # AP name                           AP radio MAC      Controller IP     Learnt from
        ap_header_capture = re.compile(
            r"^AP\s+name\s+AP\s+radio\s+MAC\s+Controller\s+IP\s+Learnt\s+from$")

        # --------------------------------------------------------------------------------------
        delimiter_capture = re.compile(
            r"^--------------------------------------------------------------------------------------$")

        # b80-72-cap30                    58bf.eab3.1420    10.10.7.177      Self
        ap_info_capture = re.compile(
                    r"^(?P<ap_name>\S+)\s+(?P<radio_mac>\S+)\s+(?P<controller_ip>\d+\.\d+\.\d+\.\d+)\s+(?P<learnt_from>\S+)") # could also do (?P<learnt_from>(Self))

        ap_info_obj = {}

        for line in output.splitlines():

            if ap_header_capture.match(line):
                continue
            if delimiter_capture.match(line):
                continue
            
            if ap_info_capture.match(line):
                ap_info_capture_match = ap_info_capture.match(line)
                groups = ap_info_capture_match.groupdict()

                # ap_name: b80-72-cap30
                ap_info_obj[groups['ap_name']] = {
                    # radio_mac: 58bf.eab3.1420
                    "radio_mac" : groups['radio_mac'],
                    # controller_ip: 10.10.7.177
                    "controller_ip": groups['controller_ip'],
                    # learnt_from: Self
                    "learnt_from": groups['learnt_from']
                }

        return ap_info_obj    