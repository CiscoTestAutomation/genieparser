''' show_l2protocol.py

IOSXE parsers for the following show commands:

    * show l2protocol-tunnel summary

Copyright (c) 2023 by Cisco Systems, Inc.
All rights reserved.
'''

import re

from genie.libs.parser.utils.common import Common
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any, Optional)


class ShowL2ProtocolTunnelSummarySchema(MetaParser):
    """Schema for show l2protocol-tunnel summary"""

    schema = {
        "cos": str,
        "drop": str,
        Optional("forward"): str,
        Optional("tunnel"): str,
        Optional("port"): {
            Any(): {
                "status": str,
                "protocol": {
                    Any(): {
                        "action": str,
                        "shutdown_threshold": str,
                        "drop_threshold": str,
                    }
                }
            }
        }
    }


class ShowL2ProtocolTunnelSummary(ShowL2ProtocolTunnelSummarySchema):
    """Parser for show l2protocol-tunnel summary"""

    cli_command = "show l2protocol-tunnel summary"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # COS for Encapsulated Packets: 5
        p1 = re.compile(r"^COS[\S\s]+: (?P<cos>\d+)$")

        # Drop Threshold for Encapsulated Packets: 0
        p2 = re.compile(r"^Drop[\S\s]+: (?P<drop>\d+)$")

        # Tunnel: Rewrites the destination MAC address of L2 PDUs with Cisco proprietary multicast address
        p3 = re.compile(r"^Tunnel: (?P<tunnel>[\w\W\s]+)$")

        # Forward: Transport L2 PDUs to peer device
        p4 = re.compile(r"^Forward: (?P<forward>[\w\W\s]+)$")

        # Twe1/0/21           up          cdp         tunnel    40        30
        p5 = re.compile(r"^(?P<port>\S+)\s+(?P<status>\S+)\s+(?P<protocol>\S+)\s+(?P<action>\S+)"
						r"\s+(?P<shutdown_threshold>\d+)\s+(?P<drop_threshold>\d+)$")

        # stp         tunnel    40        20
        # lldp        tunnel    ----      20
        p6 = re.compile(r"^(?P<protocol>\S+)\s+(?P<action>\S+)\s+(?P<shutdown_threshold>[\d\-]+)\s+(?P<drop_threshold>[\d\-]+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # COS for Encapsulated Packets: 5
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict["cos"] = dict_val["cos"]

            # Drop Threshold for Encapsulated Packets: 0
            m = p2.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict["drop"] = dict_val["drop"]

            # Tunnel: Rewrites the destination MAC address of L2 PDUs with Cisco proprietary multicast address
            m = p3.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict["tunnel"] = dict_val["tunnel"]

            # Forward: Transport L2 PDUs to peer device
            m = p4.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict["forward"] = dict_val["forward"]

            # Twe1/0/21           up          cdp         tunnel    40        30
            m = p5.match(line)
            if m:
                dict_val = m.groupdict()
                port_dict = ret_dict.setdefault("port", {}).setdefault(
                    Common.convert_intf_name(dict_val["port"]), {}
                )
                port_dict["status"] = dict_val["status"]
                protocol_dict = port_dict.setdefault("protocol", {}).setdefault(
                    dict_val["protocol"], {}
                )
                protocol_dict["action"] = dict_val["action"]
                protocol_dict["shutdown_threshold"] = dict_val["shutdown_threshold"]
                protocol_dict["drop_threshold"] = dict_val["drop_threshold"]

            # stp         tunnel    40        20
            m = p6.match(line)
            if m:
                dict_val = m.groupdict()
                protocol_dict = port_dict.setdefault("protocol", {}).setdefault(
                    dict_val["protocol"], {}
                )
                protocol_dict["action"] = dict_val["action"]
                protocol_dict["shutdown_threshold"] = dict_val["shutdown_threshold"]
                protocol_dict["drop_threshold"] = dict_val["drop_threshold"]

        return ret_dict
