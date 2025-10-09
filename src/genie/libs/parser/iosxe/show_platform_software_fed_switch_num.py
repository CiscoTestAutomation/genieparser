"""show_platform_software_fed.py

    * "show platform software fed switch active ifm mappings lpn",
    * "sh platform software fed switch {switch_num} ifm mappings lpn"
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

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

class ShowPlatformSoftwareFedSwitchFnfSwStatsShowSchema(MetaParser):
    """Schema for 'show platform software fed switch {switch_num} fnf sw-stats-show'"""
    schema = {
        'software_statistics': {
            'fnf_ageing_timeout': float,
            'flow_learning_timeout': float,
            'offload_timeout': float,
            'flow_region_entry_count': str,
            'num_ipc_errors': int,
            'num_flow_errors': int,
            'num_init_errors': int,
            'num_misc_errors': int,
            'num_config_errors': int,
        }
    }

class ShowPlatformSoftwareFedSwitchFnfSwStatsShow(ShowPlatformSoftwareFedSwitchFnfSwStatsShowSchema):
    """Parser for 'show platform software fed switch {switch_num} fnf sw-stats-show'"""

    cli_command = 'show platform software fed switch {switch_num} fnf sw-stats-show'

    def cli(self, switch_num, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch_num=switch_num))

        ret_dict = {}

        # Software Statistics:
        # ======================
        # fnf_ageing_timeout:
        p1 = re.compile(r'^\d+: fnf_ageing_timeout:\s+(?P<fnf_ageing_timeout>.+)$')

        # flow_learning_timeout:
        p2 = re.compile(r'^\d+: flow_learning_timeout:\s+(?P<flow_learning_timeout>\d+)\s+millisec$')

        # offload_timeout:
        p3 = re.compile(r'^\d+: offload_timeout:\s+(?P<offload_timeout>.+)$')

        # Flow region entry count:
        p4 = re.compile(r'^\d+: Flow region entry count:\s*(?P<flow_region_entry_count>.*)$')

        # num_ipc_errors:
        p5 = re.compile(r'^\d+: num_ipc_errors:\s+(?P<num_ipc_errors>\d+)$')

        # num_flow_errors:
        p6 = re.compile(r'^\d+: num_flow_errors:\s+(?P<num_flow_errors>\d+)$')

        # num_init_errors:
        p7 = re.compile(r'^\d+: num_init_errors:\s+(?P<num_init_errors>\d+)$')

        # num_misc_errors:
        p8 = re.compile(r'^\d+: num_misc_errors:\s+(?P<num_misc_errors>\d+)$')

        # num_config_errors:
        p9 = re.compile(r'^\d+: num_config_errors:\s+(?P<num_config_errors>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # 1: fnf_ageing_timeout:		6 sec
            m = p1.match(line)
            if m:
                group = m.groupdict()
                stats_dict = ret_dict.setdefault('software_statistics', {})
                stats_dict['fnf_ageing_timeout'] = float(group['fnf_ageing_timeout'].split()[0])
                continue

            # 2: flow_learning_timeout:	500 millisec
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('software_statistics', {})['flow_learning_timeout'] = float(group['flow_learning_timeout'])
                continue

            # 3: offload_timeout:		500 millisec
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('software_statistics', {})['offload_timeout'] = float(group['offload_timeout'].split()[0])
                continue

            # 4: Flow region entry count:
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('software_statistics', {})['flow_region_entry_count'] = group['flow_region_entry_count']
                continue

            # 5: num_ipc_errors:			0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('software_statistics', {})['num_ipc_errors'] = int(group['num_ipc_errors'])
                continue

            # 6: num_flow_errors:			0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('software_statistics', {})['num_flow_errors'] = int(group['num_flow_errors'])
                continue

            # 7: num_init_errors:			0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('software_statistics', {})['num_init_errors'] = int(group['num_init_errors'])
                continue

            # 8: num_misc_errors:			0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('software_statistics', {})['num_misc_errors'] = int(group['num_misc_errors'])
                continue

            # 9: num_config_errors:			0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('software_statistics', {})['num_config_errors'] = int(group['num_config_errors'])
                continue

        return ret_dict

class ShowPlatformSoftwareFedSwitchFnfMonitorsDumpSchema(MetaParser):
    """Schema for 'show platform software fed switch {switch_num} fnf monitors-dump'"""

    schema = {
        "monitors": {
            Any(): {
                Optional("profile_id"): str,
                Optional("ref_ct"): int,
                Optional("monitor_type"): int,
                Optional("monitor_type_desc"): str,
                Optional("wdavc_monitor_create_requested"): bool,
                Optional("wdavc_remote_monitoring_remote_caching"): int,
                Optional("flags"): str,
                Optional("is_wireless"): str,
                Optional("wireless_flags"): int,
                Optional("assurance_mon"): str,
                Optional("mon_field_cnt"): int,
                Optional("is_etta_over_fnf"): str,
                Optional("ettaOrBaseProfile"): str,
                Optional("etta_refcnt"): int,
                Optional("swc_flag"): str,
                Optional("active_timeout"): int,
                Optional("inactive_timeout"): int,
                Optional("fields"): {
                    Optional(Any()): {
                        Optional("size"): int,
                        Optional("param"): int,
                        Optional("flags"): int,
                        Optional("offset"): int,
                    }
                }
            }
        }
    }

class ShowPlatformSoftwareFedSwitchFnfMonitorsDump(ShowPlatformSoftwareFedSwitchFnfMonitorsDumpSchema):
    """Parser for 'show platform software fed switch {switch_num} fnf monitors-dump'"""

    cli_command = "show platform software fed switch {switch_num} fnf monitors-dump"

    def cli(self, switch_num, output=None):
        if output is None:
            cmd = self.cli_command.format(switch_num=switch_num)
            output = self.device.execute(cmd)

        ret_dict = {}

        # Matching Patterns
        # Monitor (0x71e214026f78):
        p1 = re.compile(r"^Monitor \((?P<monitor_id>0x[\da-fA-F]+)\):$")

        # profile_id(0xb277d7d7) ref_ct(0) monitor_type(4, FNF/FNF based feature)
        p2 = re.compile(r"^profile_id\((?P<profile_id>0x[\da-fA-F]+)\) ref_ct\((?P<ref_ct>\d+)\) monitor_type\((?P<monitor_type>\d+), (?P<monitor_type_desc>.+)\)$")

        # wdavc_monitor_create_requested(False)
        p3 = re.compile(r"^wdavc_monitor_create_requested\((?P<wdavc_monitor_create_requested>\w+)\)$")

        # wdavc_remote_monitoring_remote_caching(0)
        p4 = re.compile(r"^wdavc_remote_monitoring_remote_caching\((?P<wdavc_remote_monitoring_remote_caching>\d+)\)$")

        # flags(0x0000) is_wireless(No) wireless_flags(0)
        p5 = re.compile(r"^flags\((?P<flags>0x[\da-fA-F]+)\) is_wireless\((?P<is_wireless>\w+)\) wireless_flags\((?P<wireless_flags>\d+)\)$")

        # assurance_mon(No) mon_field_cnt(9)     is_etta_over_fnf No ettaOrBaseProfile(00000000)
        p6 = re.compile(r"^assurance_mon\((?P<assurance_mon>\w+)\) mon_field_cnt\((?P<mon_field_cnt>\d+)\)\s+is_etta_over_fnf (?P<is_etta_over_fnf>\w+) ettaOrBaseProfile\((?P<ettaOrBaseProfile>[\da-fA-F]+)\)$")

        # etta_refcnt(0) swc_flag No
        p7 = re.compile(r"^etta_refcnt\((?P<etta_refcnt>\d+)\) swc_flag (?P<swc_flag>\w+)$")

        # Active timeout (300) Inactive timeout (300)
        p8 = re.compile(r"^Active timeout \((?P<active_timeout>\d+)\) Inactive timeout \((?P<inactive_timeout>\d+)\)$")

        # field(93) size(4) param(0) flags(1) offset(0)
        p9 = re.compile(r"^field\((?P<field>\d+)\) size\((?P<size>\d+)\) param\((?P<param>\d+)\) flags\((?P<flags>\d+)\) offset\((?P<offset>\d+)\)$")

        for line in output.splitlines():
            line = line.strip()

            # Monitor (0x71e214026f78):
            m = p1.match(line)
            if m:
                group = m.groupdict()
                current_monitor = group["monitor_id"]
                monitor_dict = ret_dict.setdefault("monitors", {}).setdefault(current_monitor, {})
                continue

            # profile_id(0xb277d7d7) ref_ct(0) monitor_type(4, FNF/FNF based feature)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                monitor_dict.update({
                    "profile_id": group["profile_id"],
                    "ref_ct": int(group["ref_ct"]),
                    "monitor_type": int(group["monitor_type"]),
                    "monitor_type_desc": group["monitor_type_desc"]
                })
                continue

            # wdavc_monitor_create_requested(False)
            m = p3.match(line)
            if m:
                group = m.groupdict()
                monitor_dict["wdavc_monitor_create_requested"] = group["wdavc_monitor_create_requested"] == "True"
                continue

            # wdavc_remote_monitoring_remote_caching(0)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                monitor_dict["wdavc_remote_monitoring_remote_caching"] = int(group["wdavc_remote_monitoring_remote_caching"])
                continue

            # flags(0x0000) is_wireless(No) wireless_flags(0)
            m = p5.match(line)
            if m:
                group = m.groupdict()
                monitor_dict.update({
                    "flags": group["flags"],
                    "is_wireless": group["is_wireless"],
                    "wireless_flags": int(group["wireless_flags"])
                })
                continue

            # assurance_mon(No) mon_field_cnt(9)     is_etta_over_fnf No ettaOrBaseProfile(00000000)
            m = p6.match(line)
            if m:
                group = m.groupdict()
                monitor_dict.update({
                    "assurance_mon": group["assurance_mon"],
                    "mon_field_cnt": int(group["mon_field_cnt"]),
                    "is_etta_over_fnf": group["is_etta_over_fnf"],
                    "ettaOrBaseProfile": group["ettaOrBaseProfile"]
                })
                continue

            # etta_refcnt(0) swc_flag No
            m = p7.match(line)
            if m:
                group = m.groupdict()
                monitor_dict.update({
                    "etta_refcnt": int(group["etta_refcnt"]),
                    "swc_flag": group["swc_flag"]
                })
                continue

            # Active timeout (300) Inactive timeout (300)
            m = p8.match(line)
            if m:
                group = m.groupdict()
                monitor_dict.update({
                    "active_timeout": int(group["active_timeout"]),
                    "inactive_timeout": int(group["inactive_timeout"])
                })
                continue

            # field(93) size(4) param(0) flags(1) offset(0)
            m = p9.match(line)
            if m:
                group = m.groupdict()
                field = group.pop("field")
                field_dict = monitor_dict.setdefault("fields", {}).setdefault(field, {})
                field_dict.update({k: int(v) for k, v in group.items()})
                continue

        return ret_dict

class ShowPlatformSoftwareFedSwitchFnfProfilesDumpSchema(MetaParser):
    """Schema for 'show platform software fed switch {switch_num} fnf profiles-dump'"""

    schema = {
        "profiles": {
            Any(): {
                "record_sz": int,
                "ref": int,
                "timeout": {
                    "a": int,
                    "i": int,
                    "u": int,
                },
                "type": int,
                "wdavc_fnf_max_cache_size": int,
                "wdavc_remote_monitoring_remote_caching": int,
            }
        }
    }

class ShowPlatformSoftwareFedSwitchFnfProfilesDump(ShowPlatformSoftwareFedSwitchFnfProfilesDumpSchema):
    """Parser for 'show platform software fed switch {switch_num} fnf profiles-dump'"""

    cli_command = "show platform software fed switch {switch_num} fnf profiles-dump"

    def cli(self, switch_num, output=None):
        if output is None:
            cmd = self.cli_command.format(switch_num=switch_num)
            output = self.device.execute(cmd)

        ret_dict = {}

        # Matching pattern
        # ProfileID(b277d7d7) record_sz(46) ref(0) timeout a(300) i(300) u(1800) type(1) wdavc_fnf_max_cache_size(10000) wdavc_remote_monitoring_remote_caching(0)
        p1 = re.compile(
            r"^ProfileID\((?P<profile_id>\S+)\) record_sz\((?P<record_sz>\d+)\) ref\((?P<ref>\d+)\) "
            r"timeout a\((?P<a>\d+)\) i\((?P<i>\d+)\) u\((?P<u>\d+)\) type\((?P<type>\d+)\) "
            r"wdavc_fnf_max_cache_size\((?P<wdavc_fnf_max_cache_size>\d+)\) "
            r"wdavc_remote_monitoring_remote_caching\((?P<wdavc_remote_monitoring_remote_caching>\d+)\)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # ProfileID(b277d7d7) record_sz(46) ref(0) timeout a(300) i(300) u(1800) type(1) wdavc_fnf_max_cache_size(10000) wdavc_remote_monitoring_remote_caching(0)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                profile_id = group.pop("profile_id")
                timeout = {
                    "a": int(group.pop("a")),
                    "i": int(group.pop("i")),
                    "u": int(group.pop("u")),
                }
                profile_dict = ret_dict.setdefault("profiles", {}).setdefault(profile_id, {})
                profile_dict.update({
                    "record_sz": int(group["record_sz"]),
                    "ref": int(group["ref"]),
                    "timeout": timeout,
                    "type": int(group["type"]),
                    "wdavc_fnf_max_cache_size": int(group["wdavc_fnf_max_cache_size"]),
                    "wdavc_remote_monitoring_remote_caching": int(group["wdavc_remote_monitoring_remote_caching"]),
                })
                continue

        return ret_dict

class ShowPlatformSoftwareFedSwitchFnfProfileMapsDumpSchema(MetaParser):
    """Schema for 'show platform software fed switch {switch_num} fnf profile-maps-dump'"""

    schema = {
        "profile_maps": {
            Any(): {
                "iif_id": str,
                "fmask_hdl_ingress": int,
                "fmask_hdl_egress": int,
            }
        }
    }


class ShowPlatformSoftwareFedSwitchFnfProfileMapsDump(ShowPlatformSoftwareFedSwitchFnfProfileMapsDumpSchema):
    """Parser for 'show platform software fed switch {switch_num} fnf profile-maps-dump'"""

    cli_command = "show platform software fed switch {switch_num} fnf profile-maps-dump"

    def cli(self, switch_num, output=None):
        if output is None:
            cmd = self.cli_command.format(switch_num=switch_num)
            output = self.device.execute(cmd)

        ret_dict = {}

        # Matching pattern
        # profile map (0x7b4dc0032908:2994198487) iif_id(bc) fmask_hdl_ingress(3959422977) fmask_hdl_egress(0)
        p1 = re.compile(
            r"^profile map \((?P<profile_map_id>0x[\da-fA-F]+:\d+)\) iif_id\((?P<iif_id>\w+)\) "
            r"fmask_hdl_ingress\((?P<fmask_hdl_ingress>\d+)\) fmask_hdl_egress\((?P<fmask_hdl_egress>\d+)\)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # profile map (0x7b4dc0032908:2994198487) iif_id(bc) fmask_hdl_ingress(3959422977) fmask_hdl_egress(0)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                profile_map_id = group.pop("profile_map_id")
                profile_map_dict = ret_dict.setdefault("profile_maps", {}).setdefault(profile_map_id, {})
                profile_map_dict.update({
                    "iif_id": group["iif_id"],
                    "fmask_hdl_ingress": int(group["fmask_hdl_ingress"]),
                    "fmask_hdl_egress": int(group["fmask_hdl_egress"]),
                })
                continue

        return ret_dict