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

#StatisticsInit
class ShowPlatformSoftwareFedSwitchActiveStatisticsInitSchema(MetaParser):
    """Schema for 'show platform software fed switch active statistics init'"""
    schema = {
        "function_name": {
            Any(): {
                "initialization_time": int,
            }
        }
    }
class ShowPlatformSoftwareFedSwitchActiveStatisticsInit(ShowPlatformSoftwareFedSwitchActiveStatisticsInitSchema):
    """parser for cli 'show platform software fed switch active statistics init' """
    cli_command = "show platform software fed switch active statistics init"
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        ret_dict = {}
          # Punject driver                           1911
          # Post/wait stack manager/sif manager events 59008448
        p1 = re.compile(r"^(?P<function_name>.+?)\s+(?P<initialization_time>\d+)$")        
        for line in output.splitlines():
            line = line.strip()
              # Punject driver                           1911
              # Post/wait stack manager/sif manager events 59008448
            m = p1.match(line)
            if m:
                group = m.groupdict()                
                function_name_dict = (
                    ret_dict.setdefault("function_name", {}).setdefault(group["function_name"], {})
                )
                function_name_dict.update(
                    {
                    "initialization_time": int(group["initialization_time"]),                    
                    }
                )
                continue          
        return ret_dict

# =============================================================================
#  Schema for
#  * 'show platform software fed switch active ifm mappings port-le'
#  * 'show platform software fed switch {switch_num} ifm mappings port-le'
# ==============================================================================
class ShowPlatformSoftwareFedSwitchNumberIfmMappingsPortLESchema(MetaParser):
    """Schema for 'show platform software fed switch active ifm mappings port-le'"""

    schema = {
        "port_le": {
            Any(): {
                "interface": str,
                "if_id": str,
                "type": str,
            }
        }
    }


# ===============================================================================
#  Parser for
#  * 'show platform software fed switch active ifm mappings port-le'
#  * 'sh platform software fed switch {switch_num} ifm mappings port-le'
# ================================================================================
class ShowPlatformSoftwareFedSwitchNumberIfmMappingsPortLE(ShowPlatformSoftwareFedSwitchNumberIfmMappingsPortLESchema):
    """
    Parser for:
        * "show platform software fed switch active ifm mappings port-le"
        * "show platform software fed switch {switch_num} ifm mappings port-le"
    """

    cli_command = [
        "show platform software fed switch active ifm mappings port-le",
        "show platform software fed switch {switch_num} ifm mappings port-le",
    ]

    def cli(self, switch_num="", output=None):
        if output is None:
            cmd = self.cli_command[1].format(switch_num=switch_num) if switch_num else self.cli_command[0]
            output = self.device.execute(cmd)

        # 0x000061c7543a9de8        TwentyFiveGigE1/1/0/10            0x00000012          PORT_LE
        p1 = re.compile(
            r"^(?P<port_le>0x[\da-fA-F]+)\s+(?P<interface>\S+)\s+(?P<if_id>0x[\da-fA-F]{8})\s+(?P<type>\S+)$"
        )

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # 0x000077ba14569e18        TwentyFiveGigE1/1/0/1             0x00000009          PORT_LE
            m = p1.match(line)
            if m:
                group = m.groupdict()
                port_le = group["port_le"]
                sub_dict = ret_dict.setdefault("port_le", {}).setdefault(port_le, {})

                sub_dict["interface"] = group["interface"]
                sub_dict["if_id"] = group["if_id"]
                sub_dict["type"] = group["type"]
                continue
        return ret_dict

