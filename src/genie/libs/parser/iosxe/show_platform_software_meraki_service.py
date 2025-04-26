"""show_platform_software_meraki_service.py

IOSXE parsers for the following show command:

    * 'show platform software meraki-service'

"""

# Python
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional


class ShowPlatformSoftwareMerakiServiceSchema(MetaParser):
    """Schema for:
    * 'show platform software meraki-service'
    """

    schema = {
        "meraki_process_running": {
            "meraki_mgrd": bool,
            "meraki_tunnel_client": bool,
            "ios_console_service": bool,
            "nextunnel_packet_capture": bool,
            Optional("meraki_ncmd"): bool,
        }
    }


def is_running(value):
    """Check if the process is running"""
    return value.lower() == "running"


class ShowPlatformSoftwareMerakiService(
    ShowPlatformSoftwareMerakiServiceSchema
):
    """Parser for show platform software meraki-service"""

    cli_command = "show platform software meraki-service"

    def cli(self, output=None):
        if output is None:
            cmd = self.cli_command
            out = self.device.execute(cmd)
        else:
            out = output

        parsed_dict = {}
        meraki_process_summary = {}

        # Regex patterns to match the output lines
        # Meraki Mgrd                    : Running
        p0 = re.compile(r"^Meraki Mgrd\s+:\s+(.*)$")
        # Meraki Tunnel Client           : Running
        p1 = re.compile(r"^Meraki Tunnel Client\s+:\s+(.*)$")
        # IOS Console Service            : Running
        p2 = re.compile(r"^IOS Console Service\s+:\s+(.*)$")
        # Nextunnel Packet Capture       : Not Running
        p3 = re.compile(r"^Nextunnel Packet Capture\s+:\s+(.*)$")
        # Meraki Ncmd                    : Running
        p4 = re.compile(r"^Meraki Ncmd\s+:\s+(.*)$")

        for line in out.splitlines():
            line = line.strip()

            # Meraki Mgrd                    : Running
            m = p0.match(line)
            if m:
                meraki_process_summary["meraki_mgrd"] = is_running(m.group(1))
                continue

            # Meraki Tunnel Client           : Running
            m = p1.match(line)
            if m:
                meraki_process_summary["meraki_tunnel_client"] = is_running(
                    m.group(1)
                )
                continue

            # IOS Console Service            : Running
            m = p2.match(line)
            if m:
                meraki_process_summary["ios_console_service"] = is_running(
                    m.group(1)
                )
                continue

            # Nextunnel Packet Capture       : Not Running
            m = p3.match(line)
            if m:
                meraki_process_summary["nextunnel_packet_capture"] = is_running(
                    m.group(1)
                )
                continue

            # Meraki Ncmd                    : Running
            m = p4.match(line)
            if m:
                meraki_process_summary["meraki_ncmd"] = is_running(m.group(1))
                continue

        if meraki_process_summary:
            parsed_dict["meraki_process_running"] = meraki_process_summary

        return parsed_dict
