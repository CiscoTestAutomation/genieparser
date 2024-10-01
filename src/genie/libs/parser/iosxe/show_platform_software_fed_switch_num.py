"""show_platform_software_fed.py

    * "show platform software fed switch active ifm mappings lpn",
    * "sh platform software fed switch {switch_num} ifm mappings lpn"
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any

# =============================================================================
#  Schema for
#  * 'show platform software fed switch active ifm mappings lpn'
#  * 'show platform software fed switch {switch_num} ifm mappings lpn'
# ==============================================================================
class ShowPlatformSoftwareFedSwitchNumberIfmMappingsLpnSchema(MetaParser):
    """Schema for 'show platform software fed switch active ifm mappings lpn'"""

    schema = {
        "interfaces": {
            Any(): {
                "lpn": int,
                "asic": int,
                "port": int,
                "if_id": str,
                "active": str
            }
        }
    }
        


# ===============================================================================
#  Parser for
#  * 'show platform software fed switch active ifm mappings lpn'
#  * 'sh platform software fed switch {switch_num} ifm mappings lpn'
# ================================================================================
class ShowPlatformSoftwareFedSwitchNumberIfmMappingsLpn(
    ShowPlatformSoftwareFedSwitchNumberIfmMappingsLpnSchema
):
    """
    Parser for :
        * show platform software fed switch active ifm mappings lpn
        * "show platform software fed switch {switch_num} ifm mappings lpn"
    """

    cli_command = [
        "show platform software fed switch active ifm mappings lpn",
        "show platform software fed switch {switch_num} ifm mappings lpn",
    ]

    def cli(self, switch_num="", output=None):
        if output is None:
            if switch_num:
                cmd = self.cli_command[1].format(switch_num=switch_num)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)
        
        # 19   1     18    TenGigabitEthernet1/0/19   0x0000001b  y
        # 61   1     60    FortyGigabitEthernet2/1/1  0x00000087  Y
        p = re.compile(
            r"^(?P<lpn>\d+)\s+(?P<asic>\d+)\s+(?P<port>\d+)\s+(?P<interfaces>\S+)\s+(?P<if_id>(0x([\da-fA-F]){8}))\s+(?P<active>\S+)$"
        )

        # initial return dictionary
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # 61   1     60    FortyGigabitEthernet2/1/1  0x00000087  Y
            m = p.match(line)
            if m:
                group = m.groupdict()
                interfaces = group["interfaces"]
                sub_dict = ret_dict.setdefault("interfaces", {}).setdefault(
                    interfaces, {}
                )

                sub_dict.setdefault("lpn", int(group["lpn"]))
                sub_dict.setdefault("asic", int(group["asic"]))
                sub_dict.setdefault("port", int(group["port"]))
                sub_dict.setdefault("if_id", group["if_id"])
                sub_dict.setdefault("active", group["active"])
                continue
        return ret_dict

