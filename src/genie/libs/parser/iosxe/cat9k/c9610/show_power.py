"""  show_power.py
IOSXE parsers for the following show command:
    * 'show power detail'
"""

import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional,Or
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# import parser utils
from genie.libs.parser.utils.common import Common


class ShowPowerDetailSchema(MetaParser):
    """Schema for :
        * show power detail
    """

    schema = {
        "power_supplies": {
            str: {
                "model": str,
                "type": str,
                "capacity": int,
                "status": str,
                "fan_states": {
                    "1": str,
                    "2": str
                }
            }
        },
        "current_configuration_mode": str,
        "current_operating_state": str,
        "redundant_power": int,
        "power_supplies_active": int,
        "power_supplies_available": int,
        "power_summary": {
            "used": int,
            "available": int
        },
        "power_budget_mode": str,
        "modules": {
            str: {
                "model": str,
                "state": str,
                "budget": int,
                "instantaneous": int,
                "peak": int,
                "out_of_reset": int,
                "in_reset": int
            }
        },
        "total_allocated_power": int,
        "total_required_power": int
    }


class ShowPowerDetail(ShowPowerDetailSchema):
    """Parser for:
       * show power detail
    """

    cli_command = 'show power detail'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret = {}

        # PS1     C9600-PWR-3KWAC       ac    3000 W    active     good  good
        p1 = re.compile(
            r'^(?P<ps>PS\d+)\s+'
            r'(?P<model>\S+)\s+'
            r'(?P<type>\S+)\s+'
            r'(?P<capacity>\d+)\s*W\s+'
            r'(?P<status>\S+)\s+'
            r'(?P<fan1>\S+)\s+(?P<fan2>\S+)\s*$'
        )

        # PS Current Configuration Mode : nplusn
        p2 = re.compile(r'^PS\s+Current\s+Configuration\s+Mode\s*:\s*(?P<mode>\S+)\s*$')

        # PS Current Operating State    : Fully-Protected
        p3 = re.compile(r'^PS\s+Current\s+Operating\s+State\s*:\s*(?P<state>\S[^\r\n]*)$')

        # Redundant Power               : 11760
        p4 = re.compile(r'^Redundant\s+Power\s*:\s*(?P<val>\d+)\s*$')

        # Power supplies currently active    : 8
        p5 = re.compile(r'^Power\s+supplies\s+currently\s+active\s*:\s*(?P<val>\d+)\s*$')

        # Power supplies currently available : 8
        p6 = re.compile(r'^Power\s+supplies\s+currently\s+available\s*:\s*(?P<val>\d+)\s*$')

        # Total          10140   11820  (always prefer Total over System Power)
        p7 = re.compile(r'^\s*Total\s+(?P<used>\d+)\s+(?P<available>\d+)\s*$')

        # Power Budget Mode           : Dual Sup
        p8 = re.compile(r'^Power\s+Budget\s+Mode\s*:\s*(?P<mode>\S[^\r\n]*)$')

        # 1    C9600X-LC-32CD        accepted  450     77             141   450     10
        # FT1  C9610-FAN             accepted  1000    67             76    1000    --
        p9 = re.compile(
            r'^(?P<mod>\S+)\s+'
            r'(?P<model>\S(?:.*\S)?)\s{2,}'
            r'(?P<state>\S+)\s{2,}'
            r'(?P<budget>\d+)\s{2,}'
            r'(?P<inst>\d+)\s{2,}'
            r'(?P<peak>\d+)\s{2,}'
            r'(?P<oor>\d+)\s{2,}'
            r'(?P<inreset>(?:\d+|--))\s*$'
        )

        # Total allocated power:  10140
        p10 = re.compile(r'^Total\s+allocated\s+power:\s*(?P<val>\d+)\s*$')
        # Total required power:   10140
        p11 = re.compile(r'^Total\s+required\s+power:\s*(?P<val>\d+)\s*$')

        # generic separators/headings to skip
        p12 = re.compile(r'^-+$')
        p13 = re.compile(r'^\s*Power\s+.*Fan\s+States', re.IGNORECASE)
        p14 = re.compile(r'^\s*Supply\s+Model\s+No', re.IGNORECASE)
        p15 = re.compile(r'^\s*Mod\s+Model\s+No', re.IGNORECASE)
        p16 = re.compile(r'^\s*Total\s*$', re.IGNORECASE)  # modules table footer 'Total' line (no numbers)

        for line in out.splitlines():
            line = line.rstrip()
            if not line:
                continue

            stripped = line.strip()
            if p12.match(stripped) or p13.match(stripped) or p14.match(stripped) or p15.match(stripped) or p16.match(stripped):
                continue

            # PS1     C9600-PWR-3KWAC       ac    3000 W    active     good  good
            m = p1.match(line)
            if m:
                gd = m.groupdict()
                ret.setdefault("power_supplies", {})
                ps_key = gd['ps']
                ret["power_supplies"][ps_key] = {
                    "model": gd["model"],
                    "type": gd["type"],
                    "capacity": int(gd["capacity"]),
                    "status": gd["status"],
                    "fan_states": {
                        "1": gd["fan1"],
                        "2": gd["fan2"],
                    }
                }
                continue

            # PS Current Configuration Mode : nplusn
            m = p2.match(line)
            if m:
                ret["current_configuration_mode"] = m.group("mode")
                continue

            # PS Current Operating State    : Fully-Protected
            m = p3.match(line)
            if m:
                ret["current_operating_state"] = m.group("state").strip()
                continue

            # Redundant Power               : 11760
            m = p4.match(line)
            if m:
                ret["redundant_power"] = int(m.group("val"))
                continue

            # Power supplies currently active    : 8
            m = p5.match(line)
            if m:
                ret["power_supplies_active"] = int(m.group("val"))
                continue

            # Power supplies currently available : 8
            m = p6.match(line)
            if m:
                ret["power_supplies_available"] = int(m.group("val"))
                continue

            # Power Summary: Total          10140   11820)
            m = p7.match(line)
            if m:
                gd = m.groupdict()
                ret.setdefault("power_summary", {})
                ret["power_summary"]["used"] = int(gd["used"])
                ret["power_summary"]["available"] = int(gd["available"])
                continue

            # Power Budget Mode           : Dual Sup
            m = p8.match(line)
            if m:
                ret["power_budget_mode"] = m.group("mode").strip()
                continue

            # 1    C9600X-LC-32CD        accepted  450     77             141   450     10
            m = p9.match(line)
            if m:
                gd = m.groupdict()
                mod_key = gd["mod"]
                in_reset_raw = gd["inreset"]
                ret.setdefault("modules", {})
                ret["modules"][mod_key] = {
                    "model": gd["model"],
                    "state": gd["state"],
                    "budget": int(gd["budget"]),
                    "instantaneous": int(gd["inst"]),
                    "peak": int(gd["peak"]),
                    "out_of_reset": int(gd["oor"]),
                    "in_reset": 0 if in_reset_raw == '--' else int(in_reset_raw),
                }
                continue

            # Total allocated power:  10140
            m = p10.match(line)
            if m:
                ret["total_allocated_power"] = int(m.group("val"))
                continue

            # Total required power:   10140
            m = p11.match(line)
            if m:
                ret["total_required_power"] = int(m.group("val"))
                continue

        return ret