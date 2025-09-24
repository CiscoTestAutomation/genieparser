"""
show_subscriber.py
IOSXR parsers for the following show commands:

* `show subscriber session all summary`
"""

# Python
import re

# parser utils
from genie.libs.parser.utils.common import Common

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or, Schema


# =======================================
# Schema for 'show subscriber session all summary'
# =======================================
class ShowSubscriberSessionAllSummarySchema(MetaParser):
    """Schema for `show subscriber session all summary`"""

    schema = {
        "subscriber": {
            "session_summary": {
                "state": {
                    Or(
                        "pppoe", "ip_subscriber_dhcp", "ip_subscriber_packet"
                    ): {
                        Optional("initializing"): int,
                        Optional("connecting"): int,
                        Optional("connected"): int,
                        Optional("activated"): int,
                        Optional("idle"): int,
                        Optional("disconnecting"): int,
                        Optional("end"): int,
                        Optional("total"): int,
                    },
                },
                "address_family": {
                    Or(
                        "pppoe", "ip_subscriber_dhcp", "ip_subscriber_packet"
                    ): {
                        Optional("in_progress"): int,
                        Optional("ipv4_only"): int,
                        Optional("ipv6_only"): int,
                        Optional("dual_partial_up"): int,
                        Optional("dual_up"): int,
                        Optional("lac"): int,
                        Optional("total"): int,
                    },
                },
            }
        }
    }


# =======================================
# Parser for 'show subscriber session all summary'
# =======================================
class ShowSubscriberSessionAllSummary(ShowSubscriberSessionAllSummarySchema):
    """Parser for `show subscriber session all summary`"""

    cli_command = "show subscriber session all summary"

    # RP/0/RSP0/CPU0:Router#show subscriber session all summary
    # Thu Jan 01 00:00:00.000 UTC

    # Session Summary Information for all nodes

    #                 Type            PPPoE           IPSub           IPSub
    #                                                 (DHCP)          (PKT)
    #                 ====            =====           ======          =====

    # Session Counts by State:
    #         initializing            0               0               0
    #           connecting            0               0               0
    #            connected            0               0               0
    #            activated            0               0               666
    #                 idle            0               0               0
    #        disconnecting            0               0               0
    #                  end            0               0               0
    #               Total:            0               0               666

    # Session Counts by Address-Family/LAC:
    #          in progress            0               0               0
    #            ipv4-only            0               0               333
    #            ipv6-only            0               0               333
    #      dual-partial-up            0               0               0
    #              dual-up            0               0               0
    #                  lac            0               0               0
    #               Total:            0               0               666

    def cli(self, output=None) -> dict[str, object]:
        if output is None:
            # Execute command to get the raw output
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict: dict = {}

        # Locate sections with regex

        # Session Counts by State:
        #         initializing            0               0               0
        #           connecting            0               0               0
        #            connected            0               0               0
        #            activated            0               0               666
        #                 idle            0               0               0
        #        disconnecting            0               0               0
        #                  end            0               0               0
        #               Total:            0               0               666
        state_match = re.search(
            r"Session Counts by State:\s*(.+?)(?:\n\s*\n|\Z)",
            out,
            re.DOTALL | re.IGNORECASE,
        )

        # Session Counts by Address-Family/LAC:
        #          in progress            0               0               0
        #            ipv4-only            0               0               333
        #            ipv6-only            0               0               333
        #      dual-partial-up            0               0               0
        #              dual-up            0               0               0
        #                  lac            0               0               0
        #               Total:            0               0               666
        af_match = re.search(
            r"Session Counts by Address-Family/LAC:\s*(.+?)(?:\n\s*\n|\Z)",
            out,
            re.DOTALL | re.IGNORECASE,
        )

        # The actual section as string, or empty string if not found
        state_sec = state_match.group(1) if state_match else ""
        af_sec = af_match.group(1) if af_match else ""

        if state_sec or af_sec:
            # Column-to-key mapping (left-to-right numeric columns)
            svc_keys: list[str] = [
                "pppoe",
                "ip_subscriber_dhcp",
                "ip_subscriber_packet",
            ]

            # Build output skeleton
            ret_dict = {
                "subscriber": {
                    "session_summary": {
                        "state": {k: {} for k in svc_keys},
                        "address_family": {k: {} for k in svc_keys},
                    }
                }
            }

            # The following regex will match lines like, excluding the colon sign:
            #         initializing            0               0               0
            #           connecting            0               0               0
            #            connected            0               0               0
            #            activated            0               0               666
            #                 idle            0               0               0
            #        disconnecting            0               0               0
            #                  end            0               0               0
            #               Total:            0               0               666
            #          in progress            0               0               0
            #            ipv4-only            0               0               333
            #            ipv6-only            0               0               333
            #      dual-partial-up            0               0               0
            #              dual-up            0               0               0
            #                  lac            0               0               0
            #               Total:            0               0               666
            p = re.compile(
                r"^(?P<key>[A-Za-z0-9][A-Za-z0-9 \/\-\(\)\.]*?)(?::)?\s+(?P<pppoe>\d+)\s+(?P<dhcp>\d+)\s+(?P<pkt>\d+)$"
            )

            # State section the rows with regex only (fallback)
            for line in state_sec.splitlines():
                line = line.strip()

                if m := p.match(line):
                    key = (
                        m.group("key")
                        .replace(" ", "_")
                        .replace("-", "_")
                        .lower()
                    )
                    ret_dict["subscriber"]["session_summary"]["state"][
                        "pppoe"
                    ][key] = int(m.group("pppoe"))
                    ret_dict["subscriber"]["session_summary"]["state"][
                        "ip_subscriber_dhcp"
                    ][key] = int(m.group("dhcp"))
                    ret_dict["subscriber"]["session_summary"]["state"][
                        "ip_subscriber_packet"
                    ][key] = int(m.group("pkt"))

            # Address-Family section the rows with regex only (fallback)
            for line in af_sec.splitlines():
                line = line.strip()

                if m := p.match(line):
                    key = (
                        m.group("key")
                        .replace(" ", "_")
                        .replace("-", "_")
                        .lower()
                    )
                    ret_dict["subscriber"]["session_summary"][
                        "address_family"
                    ]["pppoe"][key] = int(m.group("pppoe"))
                    ret_dict["subscriber"]["session_summary"][
                        "address_family"
                    ]["ip_subscriber_dhcp"][key] = int(m.group("dhcp"))
                    ret_dict["subscriber"]["session_summary"][
                        "address_family"
                    ]["ip_subscriber_packet"][key] = int(m.group("pkt"))

        return ret_dict
