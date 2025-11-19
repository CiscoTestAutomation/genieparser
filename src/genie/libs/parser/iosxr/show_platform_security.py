"""Parsers for IOSXR show platform security commands.

* show platform security tam device-info location all

"""

import re
from typing import Dict, Pattern

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (
    Any,
    Optional,
    Schema,
)


class ShowPlatformSecurityTamDeviceInfoLocationAllSchema(MetaParser):
    """Schema definition for show platform security tam device-info location all parser."""

    schema = {
        "node": {
            str: {
                Optional("type"): str,
                Optional("pid"): str,
                Optional("serial_number"): str,
                Optional("firmware_version"): str,
                Optional("server_version"): str,
                Optional("server_package_version"): str,
                Optional("client_package_version"): str,
            }
        }
    }


class ShowPlatformSecurityTamDeviceInfoLocationAll(
    ShowPlatformSecurityTamDeviceInfoLocationAllSchema
):
    """Parser for 'show platform security tam device-info location all' command."""

    cli_command = "show platform security tam device-info location all"

    def cli(self, output: str = None) -> Dict[str, Any]:
        """Parse CLI output and return structured data."""
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize return dictionary
        parsed_dict: Dict[str, Any] = {}

        # Compiled regular expressions for parsing with named groups
        # Node - 0/0/CPU0
        p0: Pattern[str] = re.compile(r"Node - (?P<node_name>.+)")
        # Device Type            -     AIKIDO Extended
        p1: Pattern[str] = re.compile(r"Device Type\s+-\s+(?P<type>.+)")
        # Device PID             -     88-LC0-36FH-M
        p2: Pattern[str] = re.compile(r"Device PID\s+-\s+(?P<pid>.+)")
        # Device Serial Number   -     FOC2601N5UN
        p3: Pattern[str] = re.compile(r"Device Serial Number\s+-\s+(?P<serial_number>.+)")
        # Device Firmware Version-     0x26.0013
        p4: Pattern[str] = re.compile(r"Device Firmware Version-\s+(?P<firmware_version>.+)")
        # Server Version         -     3
        p5: Pattern[str] = re.compile(r"Server Version\s+-\s+(?P<server_version>.+)")
        # Server Package Version -     10.5.0
        p6: Pattern[str] = re.compile(r"Server Package Version\s+-\s+(?P<server_package_version>.+)")
        # Client Package Version -     10.5.0
        p7: Pattern[str] = re.compile(r"Client Package Version\s+-\s+(?P<client_package_version>.+)")

        current_node = None

        for line in output.splitlines():
            line = line.strip()

            # Node - 0/0/CPU0
            node_match = p0.match(line)
            if node_match:
                current_node = node_match.group("node_name")
                parsed_dict.setdefault("node", {})
                if current_node not in parsed_dict["node"]:
                    parsed_dict["node"][current_node] = {}
                continue

            if current_node is None:
                continue

            # Match device information using compiled patterns
            # Device Type            -     AIKIDO Extended
            type_match = p1.match(line)
            if type_match:
                parsed_dict["node"][current_node]["type"] = type_match.group("type")
                continue

            # Device PID             -     88-LC0-36FH-M
            pid_match = p2.match(line)
            if pid_match:
                parsed_dict["node"][current_node]["pid"] = pid_match.group("pid")
                continue

            # Device Serial Number   -     FOC2601N5UN
            serial_match = p3.match(line)
            if serial_match:
                parsed_dict["node"][current_node]["serial_number"] = serial_match.group("serial_number")
                continue

            # Device Firmware Version-     0x26.0013
            firmware_version_match = p4.match(line)
            if firmware_version_match:
                parsed_dict["node"][current_node]["firmware_version"] = firmware_version_match.group("firmware_version")
                continue

            # Server Version         -     3
            server_version_match = p5.match(line)
            if server_version_match:
                parsed_dict["node"][current_node]["server_version"] = server_version_match.group("server_version")
                continue

            # Server Package Version -     10.5.0
            server_package_match = p6.match(line)
            if server_package_match:
                parsed_dict["node"][current_node]["server_package_version"] = server_package_match.group("server_package_version")
                continue

            # Client Package Version -     10.5.0
            client_package_match = p7.match(line)
            if client_package_match:
                parsed_dict["node"][current_node]["client_package_version"] = client_package_match.group("client_package_version")
                continue

        return parsed_dict
