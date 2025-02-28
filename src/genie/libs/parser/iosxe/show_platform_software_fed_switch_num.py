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
    cli_command = ["show platform software fed active statistics init", 
                   "show platform software fed {switch} active statistics init"]
    def cli(self, switch=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[1].format(switch=switch)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)
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
        "show platform software fed active ifm mappings port-le",
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
    
class ShowPlatformSoftwareFedSwitchActiveIfmInterfacesDetailSchema(MetaParser):
    """Schema for 'show platform software fed switch active ifm interfaces detail'"""
    
    schema = {
        "type_n_state": {
            Any(): {  
                "intializing": int, 
                "init_failed": int, 
                "init_done": int, 
                "ready": int,
                "pending_delete": int, 
                "delete": int
            }
        }
    }

class ShowPlatformSoftwareFedSwitchActiveIfmInterfacesDetail(ShowPlatformSoftwareFedSwitchActiveIfmInterfacesDetailSchema):
    """Parser for cli 'show platform software fed switch active ifm interfaces detail'"""
    
    cli_command =  ["show platform software fed active ifm interfaces detail", 
                    "show platform software fed {switch} {mode} ifm interfaces detail"]
    
    def cli(self, switch=None, mode='active', output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[1].format(switch=switch, mode=mode)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        # Matching patterns
        # Type_n_State      Intializing  Init_Failed  Init_Done    Ready    Pending_Delete  Delete
        # -----------------------------------------------------------------------------------------
        # ETHER                0            0            0          258         0             0
        p1 = re.compile(
            r"^(?P<type_n_state>[A-Za-z0-9 \-]+)\s+(?P<intializing>\d+)\s+(?P<init_failed>\d+)\s+(?P<init_done>\d+)\s+(?P<ready>\d+)\s+(?P<pending_delete>\d+)\s+(?P<delete>\d+)$"
        )

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # ETHER             0            0            0            258      0               0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                type_n_state_dict =(
                       ret_dict.setdefault("type_n_state",{})
                       .setdefault(group['type_n_state'].strip(),{})
                )
                type_n_state_dict.update(
                    {
                        "intializing": int(group["intializing"]),
                        "init_failed": int(group["init_failed"]),
                        "init_done": int(group["init_done"]),
                        "ready": int(group["ready"]),
                        "pending_delete": int(group["pending_delete"]),
                        "delete": int(group["delete"]),
                    }
                )
                continue
        return ret_dict

class ShowPlatformSoftwareFedSwitchFnfMonitorRulesAsic0Schema(MetaParser):
    """Schema for 'show platform software fed switch {switch_num} fnf monitor-rules asic 0'"""

    schema = {
        "match_any": {
            Any(): {
                "match_any": int,
                "vector_map": str,
                "value_map": str,
            }
        },
        "enable_match": {
            Any(): {
                "enable": int,
                "match_any": int,
                "rule_map": str,
            }
        }
    }

class ShowPlatformSoftwareFedSwitchFnfMonitorRulesAsic0(ShowPlatformSoftwareFedSwitchFnfMonitorRulesAsic0Schema):
    """Parser for 'show platform software fed switch {switch_num} fnf monitor-rules asic 0'"""

    cli_command = "show platform software fed switch {switch_num} fnf monitor-rules asic 0"

    def cli(self, switch_num, output=None):
        if output is None:
            cmd = self.cli_command.format(switch_num=switch_num)
            output = self.device.execute(cmd)

        ret_dict = {}

        # Matching Patterns
        # MatchAny   Vector Map   Value Map
        p1 = re.compile(r"^(?P<index>\d+)\s+(?P<match_any>\d+)\s+(?P<vector_map>0x[\da-fA-F]+)\s+(?P<value_map>0x[\da-fA-F]+)$")

        # Enable  MatchAny   Rule Map
        p2 = re.compile(r"^(?P<index>\d+)\s+(?P<enable>\d+)\s+(?P<match_any>\d+)\s+(?P<rule_map>0x[\da-fA-F]+)$")

        for line in output.splitlines():
            line = line.strip()

            # 0  0          0x0000       0x0000
            m = p1.match(line)
            if m:
                group = m.groupdict()
                index = group.pop("index")
                match_any_dict = ret_dict.setdefault("match_any", {}).setdefault(index, {})
                match_any_dict.update({
                    "match_any": int(group["match_any"]),
                    "vector_map": group["vector_map"],
                    "value_map": group["value_map"]
                })
                continue

            # 0     0       0     0x0000
            m = p2.match(line)
            if m:
                group = m.groupdict()
                index = group.pop("index")
                enable_match_dict = ret_dict.setdefault("enable_match", {}).setdefault(index, {})
                enable_match_dict.update({
                    "enable": int(group["enable"]),
                    "match_any": int(group["match_any"]),
                    "rule_map": group["rule_map"]
                })
                continue

        return ret_dict