import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ===================================
# Schema for:
#  * 'show wireless mobility summary'
# ===================================
class ShowWirelessMobilitySummarySchema(MetaParser):
    """Schema for show wireless mobility summary."""

    schema = {
        
    }


# ===================================
# Parser for:
#  * 'show wireless mobility summary'
# ===================================
class ShowWirelessMobilitySummary(ShowWirelessMobilitySummarySchema):
    """Parser for show wireless mobility summary"""

    cli_command = ['show wireless mobility summary']

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        # Mobility Summary
        mobility_summary_capture = re.compile(r"^Mobility\s+Summary$")

        # Controllers configured in the Mobility Domain:
        controller_config_capture = re.compile(
            r"^Controllers\s+configured\s+in\s+the\s+Mobility\s+Domain:$"
        )

        #  IP                                        Public Ip                                  MAC Address         Group Name                       Multicast IPv4    Multicast IPv6                              Status                       PMTU
        controller_header_capture = re.compile(
            r"^\s+IP\s+Public Ip\s+MAC Address\s+Group Name\s+Multicast IPv4\s+Multicast IPv6\s+Status\s+PMTU\s$"
        )

        # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        controller_delimiter_capture = re.compile(
            r"^--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------$"
        )

        # Wireless Management VLAN: 299
        mgmt_vlan_capture = re.compile(r"^Wireless Management VLAN:\s+(?P<mgmt_vlan>\S+)$")

        # Wireless Management IP Address: 10.10.7.177
        mgmt_ipv4_capture = re.compile(
            r"^Wireless Management IP Address:\s+(?P<mgmt_ipv4>\S+)$"
        )

        # Wireless Management IPv6 Address:
        mgmt_ipv6_capture = re.compile(
            r"^Wireless Management IPv6 Address:\s+(?P<mgmt_ipv6>\S+)$"
        )

        # Mobility Control Message DSCP Value: 48
        mobility_control_capture = re.compile(
            r"^Mobility Control Message DSCP Value:\s+(?P<control_message>\S+)$"
        )

        # Mobility Keepalive Interval/Count: 10/3
        mobility_keepalive_capture = re.compile(
            r"^Mobility Keepalive Interval/Count:\s+(?P<keepalive>\S+)$"
        )

        # Mobility Group Name: b80-mobility
        mobility_group_capture = re.compile(r"^Mobility Group Name:\s+(?P<group_name>\S+)$")

        # Mobility Multicast Ipv4 address: 0.0.0.0
        mobility_multicast_ipv4_capture = re.compile(
            r"^Mobility Multicast Ipv4 address:\s+(?P<multicast_ipv4>\S+)$"
        )

        # Mobility Multicast Ipv6 address: ::
        mobility_multicast_ipv6_capture = re.compile(
            r"^Mobility Multicast Ipv6 address:\s+(?P<multicast_ipv6>\S+)$"
        )

        # Mobility MAC Address: 58bf.ea35.b60b
        mobility_mac_capture = re.compile(r"^Mobility MAC Address:\s+(?P<mac_address>\S+)$")

        # Mobility Domain Identifier: 0x61b3
        mobility_domain_capture = re.compile(
            r"^Mobility Domain Identifier:\s+(?P<domain_id>\S+)$"
        )

        # 10.10.7.177                               N/A                                        58bf.ea35.b60b      b80-mobility                0.0.0.0           ::                                          N/A                          N/A
        controller_config_capture = re.compile(
            r"^(?P<ipv4>\d+\.\d+\.\d+\.\d+)\s+(?P<public_ip>\S+)\s+(?P<mac_address>\S+)\s+(?P<group_name>\S+)\s+(?P<multicast_ipv4>\d+\.\d+\.\d+\.\d+)\s+(?P<multicast_ipv6>\S+)\s+(?P<status>\S+)\s+(?P<pmtu>\S+)$"
        )

        ap_info_obj = {"mobility_summary": {}, "controller_config": {}}

        mobility_summary_dict = ap_info_obj["mobility_summary"]

        controller_config_dict = ap_info_obj["controller_config"]

        for line in output.splitlines():

            if mobility_summary_capture.match(line):
                continue

            elif controller_config_capture.match(line):
                continue

            elif controller_header_capture.match(line):
                continue

            elif controller_delimiter_capture.match(line):
                continue

            elif mgmt_vlan_capture.match(line):
                match = mgmt_vlan_capture.match(line)
                mobility_summary_dict["mgmt_vlan"] = match.group("mgmt_vlan")

            elif mgmt_ipv4_capture.match(line):
                match = mgmt_ipv4_capture.match(line)
                mobility_summary_dict["mgmt_ipv4"] = match.group("mgmt_ipv4")

            elif mgmt_ipv6_capture.match(line):
                match = mgmt_ipv6_capture.match(line)
                mobility_summary_dict["mgmt_ipv6"] = match.group("mgmt_ipv6")

            elif mobility_control_capture.match(line):
                match = mobility_control_capture.match(line)
                mobility_summary_dict["control_message"] = match.group("control_message")

            elif mobility_keepalive_capture.match(line):
                match = mobility_keepalive_capture.match(line)
                mobility_summary_dict["keepalive"] = match.group("keepalive")

            elif mobility_group_capture.match(line):
                match = mobility_group_capture.match(line)
                mobility_summary_dict["group_name"] = match.group("group_name")

            elif mobility_multicast_ipv4_capture.match(line):
                match = mobility_multicast_ipv4_capture.match(line)
                mobility_summary_dict["multicast_ipv4"] = match.group("multicast_ipv4")

            elif mobility_multicast_ipv6_capture.match(line):
                match = mobility_multicast_ipv6_capture.match(line)
                mobility_summary_dict["multicast_ipv6"] = match.group("multicast_ipv6")

            elif mobility_mac_capture.match(line):
                match = mobility_mac_capture.match(line)
                mobility_summary_dict["mac_address"] = match.group("mac_address")

            elif mobility_domain_capture.match(line):
                match = mobility_domain_capture.match(line)
                mobility_summary_dict["domain_id"] = match.group("domain_id")

            elif controller_config_capture.match(line):
                match = controller_config_capture.match(line)
                groups = match.groupdict()
                controller_config_dict[groups]

        return ap_info_obj
