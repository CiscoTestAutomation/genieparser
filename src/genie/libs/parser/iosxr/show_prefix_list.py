"""show_prefix_list.py

IOSXR parser for the following show command:

    * show rpl prefix-set
    * show rpl prefix-set <name>
"""

# Python
import re

# MetaParser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


class ShowRplPrefixSetSchema(MetaParser):
    """Schema for:
        show rpl prefix-set
        show rpl prefix-set <name>"""

    schema = {
        "prefix_set_name": {
            Any(): {
                "prefix_set_name": str,
                "protocol": str,
                "prefixes": {
                    Any(): {
                        "prefix": str,
                        Optional("masklength_range"): str}
                },
            }
        }
    }


# =======================================
# Parser for 'show rpl prefix-set'
# Parser for 'show rpl prefix-set <name>'
# =======================================
class ShowRplPrefixSet(ShowRplPrefixSetSchema):
    """Parser for:
        show rpl prefix-set
        show rpl prefix-set <name>"""

    cli_command = ["show rpl prefix-set", "show rpl prefix-set {name}"]

    def cli(self, name="", output=None):
        if output is None:
            if not name:
                out = self.device.execute(self.cli_command[0])
            else:
                out = self.device.execute(
                    self.cli_command[1].format(name=name)
                )
        else:
            out = output

        # ==============
        # Compiled Regex
        # ==============

        # prefix-set test
        # prefix-set test6
        p1 = re.compile(r"^prefix\-set +(?P<name>\S+)$")

        # ipv4 version of below
        # 2001:db8:1::/64,
        # 2001:db8:2::/64 ge 65,
        # 2001:db8:3::/64 le 128,
        # 2001:db8:4::/64 ge 65 le 98
        # 10.246.192.0/24 eq 32,
        # 192.168.131.0/24,
        p2 = re.compile(
            r"^(?P<prefix>[\w\.:]+)"
            r"(?:(\/(?P<mask>\d+)))?"
            r"(?:(\s*(?P<range>[lgeq\d\s]+)))?,?$"
        )

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                name = group["name"]

                name_dict = ret_dict.setdefault(
                    "prefix_set_name", {}
                ).setdefault(name, {})
                name_dict.update({"prefix_set_name": name})
                continue

            m = p2.match(line)

            if m:
                group = m.groupdict()
                ranges = group["range"]
                mask = group["mask"]
                if mask is None:
                    prefix = group["prefix"]
                    if ':' in prefix:
                        mask = 128
                    elif '.' in prefix:
                        mask = 32
                else:
                    prefix = "{}/{}".format(group["prefix"], mask)

                if not ranges:
                    masklength_range = "{}..{}".format(mask, mask)
                else:
                    split_ranges = ranges.split()
                    if len(split_ranges) == 4:
                        masklength_range = "{}..{}".format(
                            split_ranges[1], split_ranges[3]
                        )
                    else:
                        if "le" in ranges:
                            masklength_range = "{}..{}".format(
                                mask, split_ranges[1]
                            )
                        else:
                            max_val = "128" if ":" in prefix else "32"
                            masklength_range = "{}..{}".format(
                                split_ranges[1], max_val
                            )

                name_dict.update(
                    {"protocol": "ipv6" if ":" in prefix else "ipv4"}
                )

                prefix_dict = name_dict.setdefault("prefixes", {}).setdefault(
                    "{} {}".format(prefix, masklength_range), {}
                )
                prefix_dict.update({"prefix": prefix})
                prefix_dict.update({"masklength_range": masklength_range})
                continue

        return ret_dict
