''' show_l2protocol.py

IOSXE parsers for the following show commands:

    * show l2protocol-tunnel interface {interface}

Copyright (c) 2023 by Cisco Systems, Inc.
All rights reserved.
'''

import re

from genie.libs.parser.utils.common import Common
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any


class ShowL2ProtocolTunnelInterfaceSchema(MetaParser):
    """Schema for show l2protocol-tunnel interface {interface}"""

    schema = {
        "cos": str,
        "port": {
            Any(): {
                "protocol": {
                    Any(): {
                        "shutdown_threshold": str,
                        "drop_threshold": str,
                        "encaps_counter": str,
                        "decaps_counter": str,
                        "drop_counter": str,
                    }
                }
            }
        },
    }


class ShowL2ProtocolTunnelInterface(ShowL2ProtocolTunnelInterfaceSchema):
    """Parser for show l2protocol-tunnel interface {interface}"""

    cli_command = "show l2protocol-tunnel interface {interface}"

    def cli(self, interface, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface))

        # COS for Encapsulated Packets: 5
        p1 = re.compile(r"^[\S\s]+: (?P<cos>\d+)$")

        # Gi1/0/20            cdp             40        30            7         1         0
        p2 = re.compile(r"^(?P<port>\S+)\s+(?P<protocol>\w+)\s+(?P<shutdown_threshold>\d+|\-+)\s+"
			r"(?P<drop_threshold>\d+|\-+)\s+(?P<encaps_counter>\d+|\-+)\s+(?P<decaps_counter>\d+|\-+)\s+(?P<drop_counter>\d+|\-+)$")

        # lldp          ----        20            4         3         0
        p3 = re.compile(r"^(?P<protocol>\w+)\s+(?P<shutdown_threshold>\d+|\-+)\s+(?P<drop_threshold>\d+|\-+)?"
			r"\s+(?P<encaps_counter>\d+|\-+)?\s+(?P<decaps_counter>\d+|\-+)?\s+(?P<drop_counter>\d+|\-+)?$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # COS for Encapsulated Packets: 5
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict["cos"] = dict_val["cos"]

            # Gi1/0/20            cdp             40        30            7         1         0
            m = p2.match(line)
            if m:
                dict_val = m.groupdict()
                port_dict = ret_dict.setdefault("port", {}).setdefault(
                    dict_val["port"], {}
                )
                protocol_dict = port_dict.setdefault("protocol", {}).setdefault(
                    dict_val["protocol"], {}
                )
                protocol_dict["shutdown_threshold"] = dict_val["shutdown_threshold"]
                protocol_dict["drop_threshold"] = dict_val["drop_threshold"]
                protocol_dict["encaps_counter"] = dict_val["encaps_counter"]
                protocol_dict["decaps_counter"] = dict_val["decaps_counter"]
                protocol_dict["drop_counter"] = dict_val["drop_counter"]

            # lldp          ----        20            4         3         0
            m = p3.match(line)
            if m:
                dict_val = m.groupdict()
                protocol_dict = port_dict.setdefault("protocol", {}).setdefault(
                    dict_val["protocol"], {}
                )
                protocol_dict["shutdown_threshold"] = dict_val["shutdown_threshold"]
                protocol_dict["drop_threshold"] = dict_val["drop_threshold"]
                protocol_dict["encaps_counter"] = dict_val["encaps_counter"]
                protocol_dict["decaps_counter"] = dict_val["decaps_counter"]
                protocol_dict["drop_counter"] = dict_val["drop_counter"]

        return ret_dict
