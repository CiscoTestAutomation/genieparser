"""show_platform_software_live_protect.py

    * 'show platform software live-protect shield'
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any


class ShowPlatformSoftwareLiveProtectShieldSchema(MetaParser):
    """Schema for show platform software live-protect shield"""

    schema = {
        "shield": {
            Any(): {
                "mode": str,
                "enforcing_hits": int,
                "monitoring_hits": int,
                "total_hits": int,
            }
        }
    }


class ShowPlatformSoftwareLiveProtectShield(
    ShowPlatformSoftwareLiveProtectShieldSchema
):
    """Parser for show platform software live-protect shield"""

    cli_command = "show platform software live-protect shield"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # # cve-2056-20000-v02    Enforcing     10       0      10 
        p1 = re.compile(
            r"^(?P<shield_id>\S+)\s{2,}"
            r"(?P<mode>\S+)\s{2,}"
            r"(?P<enforcing_hits>\d+)\s{2,}"
            r"(?P<monitoring_hits>\d+)\s{2,}"
            r"(?P<total_hits>\d+)\s*$"
        )

        for line in out.splitlines():
            line = line.strip()

            # cve-2026-20000-v01    Monitoring     10       0      10 
            m = p1.match(line)
            if m:
                group = m.groupdict()
                shield_id = group.pop("shield_id")
                shield_dict = ret_dict.setdefault("shield", {}).setdefault(
                    shield_id, {}
                )
                shield_dict["mode"] = group["mode"].lower()
                shield_dict["enforcing_hits"] = int(group["enforcing_hits"])
                shield_dict["monitoring_hits"] = int(group["monitoring_hits"])
                shield_dict["total_hits"] = int(group["total_hits"])

        return ret_dict
