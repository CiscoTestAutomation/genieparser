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

        # Gi1/0/17            cdp lldp stp vtp    40/----/  40/  40     30/  20/  20/  20   up
        p5 = re.compile(r"^((?P<port>\S+)\s+)?(?P<protocol>\S+ \S+ \S+( \S+)?)\s+(?P<shutdown_threshold>[\d\-]+\/[\s\d\-]+\/[\s\d\-]+(\/\s+[\d\-]+)?)"
                        r"\s+(?P<drop_threshold>[\d\-]+\/[\s\d\-]+\/[\s\d\-]+(\/\s+[\d\-]+)?)(\s+(?P<status>\S+))?$")

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

            # Gi1/0/17            cdp lldp stp vtp    40/----/  40/  40     30/  20/  20/  20   up
            # ---- ---- udld    ----/----/----        ----/----/----
            m = p5.match(line)
            if m:
                dict_val = m.groupdict()
                if dict_val["port"]:
                    port_dict = ret_dict.setdefault("port", {}).setdefault(
                        Common.convert_intf_name(dict_val["port"]), {}
                    )
                    port_dict["status"] = dict_val["status"]
                protocol_list = dict_val["protocol"].strip().split()
                shutdown_list = dict_val["shutdown_threshold"].strip().replace('/', ' ').split()
                drop_list = dict_val["drop_threshold"].strip().replace('/', ' ').split()
                for each_lst in list(zip(protocol_list, shutdown_list, drop_list)):
                    protocol_dict = port_dict.setdefault("protocol", {}).setdefault(
                        each_lst[0], {}
                    )
                    protocol_dict["shutdown_threshold"] = each_lst[1]
                    protocol_dict["drop_threshold"] = each_lst[2]

        return ret_dict
