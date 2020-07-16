import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional


# ===========================
# Schema for:
#  * 'show stackwise-virtual'
# ===========================
class ShowStackwise_VirtualSchema(MetaParser):
    """Schema for show stackwise-virtual."""

    schema = {
        "domain": int,
        "enabled": bool,
        Optional("switches"): {
            int: {
                  "id": int,
                  "ports": {
                     "a_side": str,
                     "b_side": str,
                },
            }
        },
    }


# ===========================
# Parser for:
#  * 'show stackwise-virtual'
# ===========================
class ShowStackwise_Virtual(ShowStackwise_VirtualSchema):
    """Parser for show stackwise-virtual"""

    cli_command = ["show stackwise-virtual"]

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])
        else:
            output = output

        stackwise_obj = {}
        for line in output.splitlines():
            # remove headers and empty lines
            if re.match(r"^\s*$", line) or line.startswith("-----"):
                continue
            # remove erroneous line
            elif re.match(r"Stackwise\s+Virtual\s+Configuration:", line):
                continue
            # remove headers
            elif re.match(r"Switch\s+Stackwise\s+Virtual\s+Link\s+Ports", line):
                continue

            # Stackwise Virtual : Enabled
            enabled_capture = "(?P<enabled>Enabled|Disabled)"
            pattern = re.compile(f"Stackwise\s+Virtual\s+:\s+{enabled_capture}")
            if pattern.match(line):
                match = pattern.match(line)
                enabled = True if match.group("enabled") == "Enabled" else False
                stackwise_obj["enabled"] = enabled
                continue

            # Domain Number : 100
            domain_capture = "(?P<domain>\d+)"
            pattern = re.compile(f"Domain\s+Number\s+:\s+{domain_capture}")
            if pattern.match(line):
                match = pattern.match(line)
                stackwise_obj["domain"] = int(match.group("domain"))
                continue

            # 1       1                       TenGigabitEthernet1/0/47"
            switch_capture = "(?P<switch>\d+)"
            vlink_capture = "(?P<vlink>\d+)"
            port_capture = "(?P<port>\S+)"
            pattern = re.compile(f"{switch_capture}\s+{vlink_capture}\s+{port_capture}")
            if pattern.match(line):
                match = pattern.match(line)
                switch = int(match.group("switch"))
                a_side = match.group("port")
                vlink = match.group("vlink")
                if not stackwise_obj.get("switches"):
                    stackwise_obj["switches"] = {}
                stackwise_obj["switches"][switch] = {
                    "ports": {"a_side": a_side, "b_side": "b_side"}
                }
                stackwise_obj["switches"][switch]["id"] = int(vlink)
                continue

            #                                 TenGigabitEthernet1/0/47"
            pattern = re.compile("\s{10,}(?P<port>\S+)\s*$")
            if pattern.match(line):
                b_side = match.group("port")
                vlink = match.group("vlink")
                stackwise_obj["switches"][switch]["ports"]["b_side"] = b_side
                continue
            raise ValueError(f"The following line was encounterd, and did not match any known pattern: '{line}'")
        return stackwise_obj
