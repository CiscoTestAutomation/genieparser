"""show_platform_hardware_fed.py

    * 'show platform hardware fed switch active fwd-asic resource tcam utilization'
    * 'show platform hardware fed switch active fwd-asic drops exceptions'
    * 'show platform hardware fed switch active fwd-asic resource tcam table pbr record 0 format 0 | begin {nat_region}'
    * 'show platform hardware fed switch active fwd-asic resource tcam table acl | begin {INPUT_NAT}'
    * 'show platform hardware fed active qos schedule interface {interface}'
    * 'show platform hardware fed active qos schedule interface {sub_interface}'
    * 'show platform hardware fed active qos queue stats interface {interface}'
    * 'show platform hardware fed switch {state} qos queue stats interface {interface}'
    * 'show platform hardware fed active qos queue label2qmap qmap-egress-data interface {interface}'
    * 'show platform hardware fed switch {state} qos queue label2qmap qmap-egress-data interface {interface}'
    * 'show platform hardware fed switch active fwd resource utilization | include LABEL'
    * 'show platform hardware fed switch active fwd resource utilization | include LABEL'
    * 'show platform hardware fed active qos queue config interface'
    * 'show platform hardware fed switch <no> qos queue config interface'
    * 'show platform hardware fed active fwd-asic register read register-name xyz asic n core m'
    * 'show platform hardware fed switch x fwd-asic register read register-name xyz asic n core m'
    * 'show platform hardware fed switch <state> fwd-asic abstraction print-resource-handle <client_le> 1'
    * 'show platform hardware fed switch active matm macTable'
    * 'show platform hardware fed switch active qos dscp-cos counters interface {interface}'
    * 'show platform hardware fed active qos queue stats oq multicast attach'
    * 'show platform hardware fed switch {switch_num} qos queue stats oq multicast attach'
    * 'show platform hardware fed active fwd-asic traps npu-traps asic 0'
    * 'show platform hardware fed active fwd-asic traps tm-traps asic 0'
    * 'show platform hardware fed active fwd-asic drops asic 0 slice 0'
    * 'show platform hardware fed switch active fwd-asic drops asic 0 slice 0'
    * 'show platform hardware fed switch {type} fwd-asic insight npl_summary_diff{files_compare}'
    * 'show platform hardware fed switch {switch} fwd-asic drops asic {asic}'
    * 'show platform hardware fed switch active vlan {num} ingress'
    * 'show platform hardware fed switch standby vlan {num} ingress'
    * 'show platform hardware fed switch {sw_number} qos queue config interface {interface} queue {queue_id} | include {match}'
    * 'show platform hardware fed switch {sw_number} qos scheduler interface {interface} | include {match}'
    * 'show platform software fed switch {sw_number} qos interface {interface} ingress npd detailed | include {match}'
    * 'show platform hardware fed switch {switch} fwd-asic insight l3u_nexthop{nh_gid}'

"""
# Python
import re
import logging
from collections import OrderedDict
from sys import int_info
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use, And, ListOf
from genie.libs.parser.utils.common import Common
from genie.parsergen import oper_fill_tabular

# genie.parsergen
try:
    import genie.parsergen
except (ImportError, OSError):
    pass

# pyATS
from pyats.utils.exceptions import SchemaTypeError

log = logging.getLogger(__name__)

class ShowPlatformHardwareFedSwitchActiveFwdAsicDropsExceptionsSchema(MetaParser):
    """Schema for show platform hardware fed switch active fwd-asic drops exceptions in svl"""

    schema = {
        "asic": {
            Any(): {
                "name": {
                    Any(): {
                        "prev": int,
                        "current": int,
                        "delta": int,
                    }
                }
            }
        }
    }


class ShowPlatformHardwareFedSwitchActiveFwdAsicDropsExceptions(
    ShowPlatformHardwareFedSwitchActiveFwdAsicDropsExceptionsSchema
):
    """Parser for show platform hardware fed switch active fwd-asic drops exceptions in svl
    and show platform hardware fed active fwd-asic drops exceptions"""

    cli_command = [
        "show platform hardware fed {switch} active fwd-asic drops exceptions",
        "show platform hardware fed active fwd-asic drops exceptions",
    ]

    def cli(self, switch="", output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(switch=switch)
            else:
                cmd = self.cli_command[1]

            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # ****EXCEPTION STATS ASIC INSTANCE 0 (asic/core 0/0)****
        p1 = re.compile(
            r"^\*{4}EXCEPTION +STATS +ASIC +INSTANCE +(?P<asic>\d) +\(asic/core \d\/\d\)\*{4}$"
        )

        # 0  0  NO_EXCEPTION                                   354740102   354740637    535
        p2 = re.compile(
            r"^\d +\d +(?P<name>\w+) +(?P<prev>\d+) +(?P<current>\d+) +(?P<delta>\d+)$"
        )

        for line in out.splitlines():
            line = line.strip()

            # ****EXCEPTION STATS ASIC INSTANCE 0 (asic/core 0/0)****
            m = p1.match(line)
            if m:
                group = m.groupdict()
                asic_dict = ret_dict.setdefault("asic", {}).setdefault(
                    group["asic"], {}
                )
                continue
            # 0  0  NO_EXCEPTION                                   354740102   354740637    535
            m = p2.match(line)
            if m:
                group = m.groupdict()
                dir_dict = asic_dict.setdefault("name", {}).setdefault(
                    group["name"], {}
                )
                group.pop("name")
                dir_dict.update({k: int(v) for k, v in group.items()})
                continue
        return ret_dict


class ShowPlatformHardwareFedActiveVlanIngressSchema(MetaParser):

    """Schema for show platform hardware fed active vlan {num} ingress"""

    schema = {
        "vlan_id": int,
        "forwarding_state": {"tagged_list": list, "untagged_list": list},
        "flood_list": list,
    }


class ShowPlatformHardwareFedActiveVlanIngress(
    ShowPlatformHardwareFedActiveVlanIngressSchema
):

    """Parser for show platform hardware fed active vlan {num} ingress"""

    cli_command = "show platform hardware fed active vlan {num} ingress"

    def cli(self, num, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(num=num))
        ret_dict = {}

        # vlan id is:: 1
        p1 = re.compile(r"^vlan\s+id\s+is::\s* (?P<vlan_id>\d+)")

        # Interfaces in forwarding state: : Gi1/0/15(Tagged), Fo5/0/9(Untagged)
        p2 = re.compile(
            r"^Interfaces\s+in\s+forwarding state\s*:\s*:\s*(?P<forwarding_state>[\w\/\.\s\(\w\)\,]+)$"
        )

        # flood list: : Gi1/0/15, Fo5/0/9
        p3 = re.compile(r"^flood\s+list\s*:\s+:\s+(?P<flood_list>([\w\/\.\s\,]+)$)")

        # Gi1/0/15
        p4 = re.compile(r"^(?P<intf>([\w\/\.\s]+))")

        for line in output.splitlines():
            line = line.strip()

            # vlan id is:: 1
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                ret_dict["vlan_id"] = int(group["vlan_id"])

            # Interfaces in forwarding state: : Gi1/0/15(Tagged), Fo5/0/9(Untagged)
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                for intf in group["forwarding_state"].split(", "):
                    intf_match = p4.match(intf)
                    ret_dict.setdefault("forwarding_state", {}).setdefault(
                        "tagged_list", []
                    )
                    ret_dict["forwarding_state"].setdefault("untagged_list", [])

                    ret_dict["forwarding_state"].setdefault("untagged_list", [])
                    if ("Tagged" in intf) and (intf_match):
                        ret_dict["forwarding_state"]["tagged_list"].append(
                            Common.convert_intf_name(intf_match["intf"])
                        )
                    if ("Untagged" in intf) and (intf_match):
                        ret_dict["forwarding_state"]["untagged_list"].append(
                            Common.convert_intf_name(intf_match["intf"])
                        )

            # flood list: : Gi1/0/15, Fo5/0/9
            m3 = p3.match(line)
            if m3:
                flood_list_group = m3.groupdict()
                for interface in flood_list_group["flood_list"].split(", "):
                    intf_match = p4.match(interface)
                    ret_dict.setdefault("flood_list", [])
                    if intf_match:
                        ret_dict["flood_list"].append(
                            Common.convert_intf_name(intf_match["intf"])
                        )
        return ret_dict


class ShowPlatformHardwareFedActiveQosScheduleSchema(MetaParser):
    """Parser for show platform hardware fed active qos schedule for interface and sub_interface"""

    schema = {
        "interface": {
            Any(): {
                "port_Scheduler": {
                    "Interface_SCH_OID": int,
                    "System_Port_SCH_OID": int,
                    "Priority_Propagation": str,
                    "Sub_interface_Q_Mode": str,
                    "Logical_Port": str,
                    "TC_Profile": {
                        "SDK_OID": int,
                        "TC": {
                            "TC0": int,
                            "TC1": int,
                            "TC2": int,
                            "TC3": int,
                            "TC4": int,
                            "TC5": int,
                            "TC6": int,
                            "TC7": int,
                        },
                    },
                },
                "Interface_Scheduler": {
                    "CIR": {"Credit": int, "Transmit": int, "Weight": int},
                    "PIR": {"Credit": int, "Transmit": int, "Weight": int},
                },
                "Interface_Scheduler_OQPG": {
                    "PG_TYPE": {
                        Any(): {
                            Optional("OQPG_0"): str,
                            Optional("OQPG_1"): str,
                            Optional("OQPG_2"): str,
                            Optional("OQPG_3"): str,
                            Optional("OQPG_4"): str,
                            Optional("OQPG_5"): str,
                            Optional("OQPG_6"): str,
                            Optional("OQPG_7"): str,
                        },
                    }
                },
                "OQPG": {
                    Any(): {
                        "LPSE_OQ_0": str,
                        "LPSE_OQ_1": str,
                        Optional("OQ_2"): str,
                        Optional("OQ_3"): str,
                        Optional("OQ_4"): str,
                        Optional("OQ_5"): str,
                        Optional("OQ_6"): str,
                        Optional("OQ_7"): str,
                    },
                },
                "LPSE_OID": int,
                Optional("LPSE_CIR_Rate"): int,
                Optional("LPSE_CIR_Burst"): str,
                Optional("LPSE_PIR_Rate"): int,
                Optional("LPSE_PIR_Burst"): str,
                Optional("LPSE_Main_Int"): int,
                Optional("LPSE_OQSE_CIR"): int,
                Optional("LPSE_OQSE_CIR_Burst"): str,
                Optional("LPSE_OQSE_PIR"): int,
                Optional("LPSE_OQSE_PIR_Burst"): str,
                Optional("LPSE_Total"): int,
                "oqse_oid": int,
                "oq_id": int,
                "oq_scheduling_mode": str,
                Optional("oq_credit_cir"): int,
                Optional("oq_credit_cir_burst"): str,
                "oq_credit_pir": int,
                "oq_credit_pir_burst": str,
                Optional("oq_transmit_pir"): int,
                Optional("oq_transmit_pir_burst"): str,
            }
        }
    }


class ShowPlatformHardwareFedActiveQosScheduleInterface(
    ShowPlatformHardwareFedActiveQosScheduleSchema
):
    """
    Parser for:
        * show platform hardware fed active qos schedule interface
    """

    cli_command = [
        "show platform hardware fed switch {switch_var} qos schedule interface {interface}",
        "show platform hardware fed active qos schedule interface {interface}",
    ]

    def cli(self, interface, output=None, switch_var=None):
        if output is None:
            if switch_var is None:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0].format(
                    switch_var=switch_var, interface=interface
                )

            output = self.device.execute(cmd)

        ret_dict = {}
        list1 = ["Credit PIR    ", "Credit Burst  ", "Transmit PIR  ", "Transmit Burst"]

        # Interface  : Gi1/0/2
        p1 = re.compile(r"^Interface +: (?P<intf>[\w+\/\.\-]+)")

        # | Interface SCH OID     : 3125
        p2 = re.compile(r"\| Interface SCH OID +: (?P<Interface_SCH_OID>\d+)")

        # System Port SCH OID   : 3129
        p3 = re.compile(r"\| System Port SCH OID +: (?P<System_Port_SCH_OID>\d+)")

        # Priority Propagation  : Disabled
        p4 = re.compile(r"\| Priority Propagation +: (?P<Priority_Propagation>\w+)")

        # Sub-interface Q Mode  : Enabled - Priority Propagation
        p5 = re.compile(r"\| Sub-interface Q Mode +: (?P<Sub_interface_Q>[\w+-]+)")

        # Logical Port          : Enabled
        p6 = re.compile(r"\| Logical Port +: (?P<Logical_Port>\w+)")

        # TC Profile            : SDK OID    :   110
        p7 = re.compile(r"\| TC Profile +: SDK OID +: +(?P<SDK_OID>\d+)$")

        # |                       : VOQ Offset :   0 |   0 |   0 |   0 |   0 |   0 |   0 |   2
        p8 = re.compile(
            r"\| +: VOQ Offset : +(?P<TC0>\d+) \| +(?P<TC1>\d+) \| +(?P<TC2>\d+) \| +(?P<TC3>\d+) \| +(?P<TC4>\d+) \| +(?P<TC5>\d+) \| +(?P<TC6>\d+) \| +(?P<TC7>\d+)$"
        )

        # |           | Credit        : 20000000000
        p9 = re.compile(r"\| +\| Credit +: (?P<Credit>\d+)")

        # | CIR [RR]  | Transmit      : 20000000000
        p10 = re.compile(r"\| CIR \[RR\] +\| Transmit +: (?P<Transmit>\d+)")

        # |           | Weight        : 1
        p11 = re.compile(r"\|           \| Weight        : (?P<Weight>\d+)")

        # | PIR [WFQ] | Transmit      : 20000000000
        p12 = re.compile(r"\| PIR \[WFQ\] +\| Transmit +: (?P<Transmit>\d+)")

        # |    |Credit CIR    || 0                | 0                | 0                | 0                | 0                | 0                | 0                | 60000000000      |
        # | RR |Credit Burst  || 0                | 0                | 0                | 0                | 0                | 0                | 0                | SDK Default      |
        p13 = re.compile(
            r"\| (\w+ | +)\|(?P<PG_TYPE>[\w+ ]+) +\|\| (?P<OQPG_0>\d+) +\| (?P<OQPG_1>\d+) +\| (?P<OQPG_2>\d+) +\| (?P<OQPG_3>\d+) +\| (?P<OQPG_4>\d+) +\| (?P<OQPG_5>\d+) +\| (?P<OQPG_6>\d+) +\| (?P<OQPG_7>[a-zA-z0-9 ]{1,11})"
        )

        # | OQ List           || 0                | 1                |                  | 3                | 4                | 5                | 6                | 2 7              |
        p13_1 = re.compile(
            r"\| (?P<PG_TYPE>[\w+ ]+) +\|\| (?P<OQPG_0>[\d+ ]) +\| (?P<OQPG_1>[\d+ ]) +\| (?P<OQPG_2>[\d+ ]) +\| (?P<OQPG_3>[\d+ ]) +\| (?P<OQPG_4>[\d+ ]) +\| (?P<OQPG_5>[\d+ ]) +\| (?P<OQPG_6>[\d+ ]) +\| (?P<OQPG_7>[a-zA-z0-9 ]{1,11})"
        )

        # | Credit PIR        || 60000000000      | 60000000000      | 4000000000       | 60000000000      | 60000000000      | 60000000000      | 60000000000      | 60000000000      |
        # | Credit Burst      || SDK Default      | SDK Default      | SDK Default      | SDK Default      | SDK Default      | SDK Default      | SDK Default      | SDK Default      |
        # | Transmit PIR      || 60000000000      | 60000000000      | 4000000000       | 60000000000      | 60000000000      | 60000000000      | 60000000000      | 60000000000      |
        # | Transmit Burst    || SDK Default      | SDK Default      | SDK Default      | SDK Default      | SDK Default      | SDK Default      | SDK Default      | SDK Default      |
        # | Weights : UC : MC ||      8 : 2       |      8 : 2       |      8 : 2       |      8 : 2       |      8 : 2       |      8 : 2       |      8 : 2       |      8 : 2       |
        # | OQSE OID          || LPSE OID : 3138 (0xC42  )           | 3132 (0xC3C  )   | 3133 (0xC3D  )   | 3134 (0xC3E  )   | 3135 (0xC3F  )   | 3136 (0xC40  )   | 3137 (0xC41  )   |

        p14 = re.compile(
            r"\| (?P<OQ_Number>[\w+ ]{1,14}) +\|\| (?P<LPSE_OQ_0>[a-zA-Z0-9 ]{1,11}) +\| (?P<LPSE_OQ_1>[a-zA-Z0-9 ]{1,11}) +\| (?P<OQ_2>[a-zA-Z0-9 ]{1,11}) +\| (?P<OQ_3>[a-zA-Z0-9 ]{1,11}) +\| (?P<OQ_4>[a-zA-Z0-9 ]{1,11}) +\| (?P<OQ_5>[a-zA-Z0-9 ]{1,11}) +\| (?P<OQ_6>[a-zA-Z0-9 ]{1,11}) +\| (?P<OQ_7>[a-zA-Z0-9 ]{1,11})"
        )

        # | Credit PIR        || 20000000000      | 20000000000      |
        # | Credit Burst      || SDK Default      | SDK Default      |
        # | Transmit PIR      || 20000000000      | 20000000000      |
        # | Transmit Burst    || SDK Default      | SDK Default      |
        # | LPSE OID          || 3138 (0xC42  )                      |
        p14_1 = re.compile(
            r"\| (?P<OQ_Number>[\w+ ]{1,14}) +\|\| (?P<LPSE_OQ_0>[a-zA-Z0-9 ]{1,11}) +\| (?P<LPSE_OQ_1>[a-zA-Z0-9 ]{1,11})"
        )

        # | LPSE OID          || 3138 (0xC42  )
        p15 = re.compile(r"\| LPSE OID +\|\| (?P<LPSE_OID>\d+)")

        # | LPSE OID                            : 3138 (  0xC42)
        p16 = re.compile(r"\| LPSE OID +: (?P<LPSE_OID>\d+)")

        # | LPSE CIR (Priority Queue) Rate      : 2000000000
        p17 = re.compile(
            r"\| LPSE CIR \(Priority Queue\) Rate +: (?P<LPSE_CIR_Rate>\d+)"
        )

        # | LPSE CIR (Priority Queue) Burst     : SDK Default
        p18 = re.compile(
            r"\| LPSE CIR \(Priority Queue\) Burst +: (?P<LPSE_CIR_Burst>[\w+ ]{1,11})"
        )

        # | LPSE PIR (Sub-Interface Port) Rate  : 2000000000
        p19 = re.compile(
            r"\| LPSE PIR \(Sub-Interface Port\) Rate  : (?P<LPSE_PIR_Rate>\d+)"
        )

        # | LPSE PIR (Sub-Interface Port) Burst : SDK Default
        p20 = re.compile(
            r"\| LPSE PIR (Sub-Interface Port) Burst : (?P<LPSE_PIR_Burst>[\w+ ]{1,11})"
        )

        # | LPSE Main Interface OQSE  : 3130 (0xC3A  )   | 3131 (0xC3B  )   |
        p21 = re.compile(r"\| LPSE Main Interface OQSE  : (?P<LPSE_Main_Int>\d+)")

        # | LPSE OQSE Credit CIR      : 60000000000      | 60000000000      |
        p22 = re.compile(r"\| LPSE OQSE Credit CIR +: (?P<LPSE_OQSE_CIR>\d+)")

        # | LPSE OQSE Credit CIR Burst: SDK Default      | SDK Default      |
        p23 = re.compile(
            r"\| LPSE OQSE Credit CIR Burst: (?P<LPSE_OQSE_CIR_Burst>[\w+ ]{1,11})"
        )

        # | LPSE OQSE Credit PIR      : 60000000000      | 60000000000      |
        p24 = re.compile(r"\| LPSE OQSE Credit PIR +: (?P<LPSE_OQSE_PIR>\d+)")

        # | LPSE OQSE Credit PIR Burst: SDK Default      | SDK Default      |
        p25 = re.compile(
            r"\| LPSE OQSE Credit PIR Burst: (?P<LPSE_OQSE_PIR_Burst>[\w+ ]{1,11})"
        )

        # | LPSE Total Attached OQSEs : 2
        p26 = re.compile(r"\| LPSE Total Attached OQSEs : (?P<LPSE_Total>\d+)")
        # | OQSE OID              : 4234
        p27 = re.compile(r"\| OQSE OID\s+: (?P<oqse_oid>\d+)")

        # | OQ    ID              : 0
        p28 = re.compile(r"\| OQ    ID\s+: (?P<oq_id>\d+)")

        # | Scheduling Mode       : Logical Port SP WFQ
        p29 = re.compile(r"\| Scheduling Mode\s+: (?P<oq_scheduling_mode>\w+)")

        # | Credit CIR            : 2000000000
        p30 = re.compile(r"\| Credit CIR\s+: (?P<oq_credit_cir>\d+)")

        # | Credit CIR Burst      : SDK Default
        p31 = re.compile(r"\| Credit CIR Burst\s+:(?P<oq_credit_cir_burst>\w+)")

        # | Credit PIR            : 2000000000
        p32 = re.compile(r"\| Credit PIR\s+: (?P<oq_credit_pir>\w+)")

        # | Credit PIR Burst      : SDK Default
        p33 = re.compile(r"\| Credit PIR Burst\s+: (?P<oq_credit_pir_burst>\w+)")

        # | Transmit PIR          : 60000000000
        p34 = re.compile(r"\| Transmit PIR\s+: (?P<oq_transmit_pir>\d+)")

        # | Transmit PIR Burst    : SDK Default
        p35 = re.compile(r"\| Transmit PIR Burst\s+: (?P<oq_transmit_pir_burst>\d+)")

        flag_CIR = 0
        for line in output.splitlines():
            line = line.strip()

            # Interface  : Gi1/0/2
            m = p1.match(line)
            if m:
                interface = m.groupdict()["intf"]
                interface_dict = ret_dict.setdefault("interface", {})
                interface_dict1 = interface_dict.setdefault(interface, {})
                Port_Scheduler_dict = interface_dict1.setdefault("port_Scheduler", {})
                continue

            # | Interface SCH OID     : 3125
            m = p2.match(line)
            if m:
                Port_Scheduler_dict["Interface_SCH_OID"] = int(
                    m.groupdict()["Interface_SCH_OID"]
                )
                continue

            # System Port SCH OID   : 3129
            m = p3.match(line)
            if m:
                Port_Scheduler_dict["System_Port_SCH_OID"] = int(
                    m.groupdict()["System_Port_SCH_OID"]
                )
                continue

            # Priority Propagation  : Disabled
            m = p4.match(line)
            if m:
                Port_Scheduler_dict["Priority_Propagation"] = m.groupdict()[
                    "Priority_Propagation"
                ]
                continue

            # Sub-interface Q Mode  : Enabled - Priority Propagation
            m = p5.match(line)
            if m:
                Port_Scheduler_dict["Sub_interface_Q_Mode"] = m.groupdict()[
                    "Sub_interface_Q"
                ]
                continue

            # Logical Port          : Enabled
            m = p6.match(line)
            if m:
                Port_Scheduler_dict["Logical_Port"] = m.groupdict()["Logical_Port"]
                continue

            # TC Profile            : SDK OID    :   110
            m = p7.match(line)
            if m:
                Tc_profile_dict = Port_Scheduler_dict.setdefault("TC_Profile", {})
                Tc_profile_dict["SDK_OID"] = int(m.groupdict()["SDK_OID"])
                continue

            # |                       : VOQ Offset :   0 |   0 |   0 |   0 |   0 |   0 |   0 |   2
            m = p8.match(line)
            if m:
                TC_dict = Tc_profile_dict.setdefault("TC", {})
                TC_dict["TC0"] = int(m.groupdict()["TC0"])
                TC_dict["TC1"] = int(m.groupdict()["TC1"])
                TC_dict["TC2"] = int(m.groupdict()["TC2"])
                TC_dict["TC3"] = int(m.groupdict()["TC3"])
                TC_dict["TC4"] = int(m.groupdict()["TC4"])
                TC_dict["TC5"] = int(m.groupdict()["TC5"])
                TC_dict["TC6"] = int(m.groupdict()["TC6"])
                TC_dict["TC7"] = int(m.groupdict()["TC7"])
                continue

            # |           | Credit        : 20000000000
            m = p9.match(line)
            if m and flag_CIR < 1:
                Interface_Scheduler_dict = interface_dict1.setdefault(
                    "Interface_Scheduler", {}
                )
                CIR_dict = Interface_Scheduler_dict.setdefault("CIR", {})
                CIR_dict["Credit"] = int(m.groupdict()["Credit"])
                flag_CIR = 1
                continue

            # | CIR [RR]  | Transmit      : 20000000000
            m = p10.match(line)
            if m and flag_CIR < 2:
                CIR_dict["Transmit"] = int(m.groupdict()["Transmit"])
                flag_CIR = 2
                continue

            # |           | Weight        : 1
            m = p11.match(line)
            if m and flag_CIR < 3 and flag_CIR > 1:
                CIR_dict["Weight"] = int(m.groupdict()["Weight"])
                flag_CIR = 3
                continue

            # | PIR [WFQ] | Transmit      : 20000000000
            m = p9.match(line)
            if m:
                PIR_dict = Interface_Scheduler_dict.setdefault("PIR", {})
                PIR_dict["Credit"] = int(m.groupdict()["Credit"])
                continue

            # |    |Credit CIR    || 0                | 0                | 0                | 0                | 0                | 0                | 0                | 60000000000      |
            m = p12.match(line)
            if m:
                PIR_dict["Transmit"] = int(m.groupdict()["Transmit"])
                continue

            # |           | Weight        : 1
            m = p11.search(line)
            if m:
                PIR_dict["Weight"] = int(m.groupdict()["Weight"])
                continue

            # |    |Credit CIR    || 0                | 0                | 0                | 0                | 0                | 0                | 0                | 60000000000      |
            m = p13.match(line)
            if m:
                Interface_Scheduler_OQPG_dict = interface_dict1.setdefault(
                    "Interface_Scheduler_OQPG", {}
                )
                PG_TYPE_dict = Interface_Scheduler_OQPG_dict.setdefault("PG_TYPE", {})
                PG_TYPE_Name = m.groupdict()["PG_TYPE"].strip()
                OQPG_dict = PG_TYPE_dict.setdefault(PG_TYPE_Name, {})
                OQPG_dict["OQPG_0"] = m.groupdict()["OQPG_0"]
                OQPG_dict["OQPG_1"] = m.groupdict()["OQPG_1"]
                OQPG_dict["OQPG_2"] = m.groupdict()["OQPG_2"]
                OQPG_dict["OQPG_3"] = m.groupdict()["OQPG_3"]
                OQPG_dict["OQPG_4"] = m.groupdict()["OQPG_4"]
                OQPG_dict["OQPG_5"] = m.groupdict()["OQPG_5"]
                OQPG_dict["OQPG_6"] = m.groupdict()["OQPG_6"]
                OQPG_dict["OQPG_7"] = m.groupdict()["OQPG_7"].strip()
                continue

            # | OQ List           || 0                | 1                |                  | 3                | 4                | 5                | 6                | 2 7              |
            m = p13_1.match(line)
            if m:
                PG_TYPE_Name = m.groupdict()["PG_TYPE"].strip()
                OQPG_dict = PG_TYPE_dict.setdefault(PG_TYPE_Name, {})
                if not m.groupdict()["OQPG_0"].isspace():
                    OQPG_dict["OQPG_0"] = m.groupdict()["OQPG_0"]
                if not m.groupdict()["OQPG_1"].isspace():
                    OQPG_dict["OQPG_1"] = m.groupdict()["OQPG_1"]
                if not m.groupdict()["OQPG_2"].isspace():
                    OQPG_dict["OQPG_2"] = m.groupdict()["OQPG_2"]
                if not m.groupdict()["OQPG_3"].isspace():
                    OQPG_dict["OQPG_3"] = m.groupdict()["OQPG_3"]
                if not m.groupdict()["OQPG_4"].isspace():
                    OQPG_dict["OQPG_4"] = m.groupdict()["OQPG_4"]
                if not m.groupdict()["OQPG_5"].isspace():
                    OQPG_dict["OQPG_5"] = m.groupdict()["OQPG_5"]
                if not m.groupdict()["OQPG_0"].isspace():
                    OQPG_dict["OQPG_6"] = m.groupdict()["OQPG_6"]
                if not m.groupdict()["OQPG_0"].isspace():
                    OQPG_dict["OQPG_7"] = m.groupdict()["OQPG_7"].strip()
                continue

            # | Credit PIR        || 60000000000      | 60000000000      | 4000000000       | 60000000000      | 60000000000      | 60000000000      | 60000000000      | 60000000000      |
            m = p14.match(line)
            if m:
                LPSE_OQPG_dict = interface_dict1.setdefault("OQPG", {})
                OQ_Number = m.groupdict()["OQ_Number"].strip()
                LPSE_dict = LPSE_OQPG_dict.setdefault(OQ_Number, {})
                LPSE_dict["LPSE_OQ_0"] = m.groupdict()["LPSE_OQ_0"]
                LPSE_dict["LPSE_OQ_1"] = m.groupdict()["LPSE_OQ_1"]
                LPSE_dict["OQ_2"] = m.groupdict()["OQ_2"]
                LPSE_dict["OQ_3"] = m.groupdict()["OQ_3"]
                LPSE_dict["OQ_4"] = m.groupdict()["OQ_4"]
                LPSE_dict["OQ_5"] = m.groupdict()["OQ_5"]
                LPSE_dict["OQ_6"] = m.groupdict()["OQ_6"]
                LPSE_dict["OQ_7"] = m.groupdict()["OQ_7"]
                continue

            # | Credit PIR        || 20000000000      | 20000000000      |
            m = p14_1.match(line)
            if m and m.groupdict()["OQ_Number"] in list1:
                LPSE_OQPG_dict = interface_dict1.setdefault("OQPG", {})
                OQ_Number = m.groupdict()["OQ_Number"].strip()
                LPSE_dict = LPSE_OQPG_dict.setdefault(OQ_Number, {})
                LPSE_dict["LPSE_OQ_0"] = m.groupdict()["LPSE_OQ_0"]
                LPSE_dict["LPSE_OQ_1"] = m.groupdict()["LPSE_OQ_1"]
                continue

            # | LPSE OID
            m = p16.match(line)
            if m:
                interface_dict1["LPSE_OID"] = int(m.groupdict()["LPSE_OID"])
                continue
            # | LPSE CIR (Priority Queue) Rate      : 2000000000
            m = p17.match(line)
            if m:
                interface_dict1["LPSE_CIR_Rate"] = int(m.groupdict()["LPSE_CIR_Rate"])
                continue

            # | LPSE CIR (Priority Queue) Burst     : SDK Default
            m = p18.match(line)
            if m:
                interface_dict1["LPSE_CIR_Burst"] = m.groupdict()["LPSE_CIR_Burst"]
                continue

            # | LPSE PIR (Sub-Interface Port) Rate  : 2000000000
            m = p19.match(line)
            if m:
                interface_dict1["LPSE_PIR_Rate"] = int(m.groupdict()["LPSE_PIR_Rate"])
                continue

            # | LPSE PIR (Sub-Interface Port) Burst : SDK Default
            m = p20.match(line)
            if m:
                interface_dict1["LPSE_PIR_Burst"] = m.groupdict()["LPSE_PIR_Burst"]
                continue

            # | LPSE Main Interface OQSE  : 3130 (0xC3A  )   | 3131 (0xC3B  )   |
            m = p21.match(line)
            if m:
                interface_dict1["LPSE_Main_Int"] = int(m.groupdict()["LPSE_Main_Int"])
                continue

            # | LPSE OQSE Credit CIR      : 60000000000      | 60000000000      |
            m = p22.match(line)
            if m:
                interface_dict1["LPSE_OQSE_CIR"] = int(m.groupdict()["LPSE_OQSE_CIR"])
                continue

            # | LPSE OQSE Credit CIR Burst: SDK Default      | SDK Default      |
            m = p23.match(line)
            if m:
                interface_dict1["LPSE_OQSE_CIR_Burst"] = m.groupdict()[
                    "LPSE_OQSE_CIR_Burst"
                ]
                continue

            # | LPSE OQSE Credit PIR      : 60000000000      | 60000000000      |
            m = p24.match(line)
            if m:
                interface_dict1["LPSE_OQSE_PIR"] = int(m.groupdict()["LPSE_OQSE_PIR"])
                continue

            # | LPSE OQSE Credit PIR Burst: SDK Default      | SDK Default      |
            m = p25.match(line)
            if m:
                interface_dict1["LPSE_OQSE_PIR_Burst"] = m.groupdict()[
                    "LPSE_OQSE_PIR_Burst"
                ]
                continue

            # | LPSE Total Attached OQSEs : 2
            m = p26.match(line)
            if m:
                interface_dict1["LPSE_Total"] = int(m.groupdict()["LPSE_Total"])
                continue

            # | OQSE OID              : 4234
            m = p27.match(line)
            if m:
                interface_dict1["oqse_oid"] = int(m.groupdict()["oqse_oid"])
                continue

            # | OQ    ID              : 0
            m = p28.match(line)
            if m:
                interface_dict1["oq_id"] = int(m.groupdict()["oq_id"])
                continue

            # | Scheduling Mode       : Logical Port SP WFQ
            m = p29.match(line)
            if m:
                interface_dict1["oq_scheduling_mode"] = m.groupdict()[
                    "oq_scheduling_mode"
                ]
                continue

            # | Credit CIR            : 2000000000
            m = p30.match(line)
            if m:
                interface_dict1["oq_credit_cir"] = int(m.groupdict()["oq_credit_cir"])
                continue

            # | Credit CIR Burst      : SDK Default
            m = p31.match(line)
            if m:
                interface_dict1["oq_credit_cir_burst"] = m.groupdict()[
                    "oq_credit_cir_burst"
                ]
                continue

            # | Credit PIR            : 2000000000
            m = p32.match(line)
            if m:
                interface_dict1["oq_credit_pir"] = int(m.groupdict()["oq_credit_pir"])
                continue

            # | Credit PIR Burst      : SDK Default
            m = p33.match(line)
            if m:
                interface_dict1["oq_credit_pir_burst"] = m.groupdict()[
                    "oq_credit_pir_burst"
                ]
                continue

            # | Transmit PIR          : 60000000000
            m = p34.match(line)
            if m:
                interface_dict1["oq_transmit_pir"] = int(
                    m.groupdict()["oq_transmit_pir"]
                )
                continue

            # | Transmit PIR Burst    : SDK Default
            m = p35.match(line)
            if m:
                interface_dict1["oq_transmit_pir_burst"] = m.groupdict()[
                    "oq_transmit_pir_burst"
                ]

                continue
        return ret_dict


class ShowPlatformHardwareFedActiveQosQueueStatsSchema(MetaParser):
    """Schema for show platform hardware fed active qos queue stats"""

    schema = {
        "enqueue_counters": {
            int: {
                "buffers_count": int,
                "enqueue_th0": int,
                "enqueue_th1": int,
                "enqueue_th2": int,
                Optional("q_policer"): int,
            },
        },
        "drop_counters": {
            int: {
                "drop_th0": int,
                "drop_th1": int,
                "drop_th2": int,
                "s_buf_drop": int,
                "q_eb_drop": int,
                Optional("q_policer_drop"): int,
            },
        },
    }


class ShowPlatformHardwareFedActiveQosQueueStats(
    ShowPlatformHardwareFedActiveQosQueueStatsSchema
):
    """
    Parser for:
        * show platform hardware fed active qos queue stats interface
        * show platform hardware fed switch 1 qos queue stats interface
    """

    cli_command = [
        "show platform hardware fed active qos queue stats interface {interface}",
        "show platform hardware fed switch {switch_num} qos queue stats interface {interface}",
    ]

    def cli(self, interface, output=None, switch_num=None):
        if output is None:
            if switch_num is None:
                cmd = self.cli_command[0].format(interface=interface)
            else:
                cmd = self.cli_command[1].format(
                    switch_num=switch_num, interface=interface
                )

            output = self.device.execute(cmd)

        ret_dict = {}

        drop_section = False

        """
        ----------------------------------------------------------------------------------------------
        Q Buffers          Enqueue-TH0          Enqueue-TH1          Enqueue-TH2             Qpolicer
        (Count)              (Bytes)              (Bytes)              (Bytes)              (Bytes)
        -- ------- -------------------- -------------------- -------------------- --------------------
        0       0                    0                13114            129171972                    0
        1       0                    0                    0            546062296                    0
        2       0                    0                    0                    0                    0
        3       0                    0                    0                    0                    0
        4       0                    0                    0                    0                    0
        5       0                    0                    0                    0                    0
        6       0                    0                    0                    0                    0
        7       0                    0                    0                    0                    0
       """

        p1 = re.compile(
            r"^(?P<Q>\d)\s+(?P<buffers_count>\d+)\s+(?P<enqueue_th0>\d+)\s+(?P<enqueue_th1>\d+)\s+(?P<enqueue_th2>\d+)\s+(?P<qpolicer>\d+)$"
        )

        #  Q Buffers          Enqueue-TH0          Enqueue-TH1          Enqueue-TH2
        p1_1 = re.compile(
            r"^(?P<Q>\d)\s+(?P<buffers_count>\d+)\s+(?P<enqueue_th0>\d+)\s+(?P<enqueue_th1>\d+)\s+(?P<enqueue_th2>\d+)$"
        )

        """
        --------------------------------------------------------------------------------------------------------------------------------
        Q             Drop-TH0             Drop-TH1             Drop-TH2             SBufDrop              QebDrop         QpolicerDrop
                      (Bytes)              (Bytes)              (Bytes)              (Bytes)              (Bytes)              (Bytes)
        -- -------------------- -------------------- -------------------- -------------------- -------------------- --------------------
        0                    0                    0                    0                    0                    0                    0
        1                    0                    0                    0                    0                    0                    0
        2                    0                    0                    0                    0                    0                    0
        3                    0                    0                    0                    0                    0                    0
        4                    0                    0                    0                    0                    0                    0
        5                    0                    0                    0                    0                    0                    0
        6                    0                    0                    0                    0                    0                    0
        7                    0                    0                    0                    0                    0                    0
        """

        p2 = re.compile(
            r"^(?P<Q>\d)\s+(?P<drop_th0>\d+)\s+(?P<drop_th1>\d+)\s+(?P<drop_th2>\d+)\s+(?P<sbufDrop>\d+)\s+(?P<qebDrop>\d+)\s+(?P<qpolicerDrop>\d+)$"
        )

        # Queue Drop-TH0 Drop-TH1 Drop-TH2 SBufDrop QebDrop
        p2_1 = re.compile(
            r"^(?P<Q>\d)\s+(?P<drop_th0>\d+)\s+(?P<drop_th1>\d+)\s+(?P<drop_th2>\d+)\s+(?P<sbufDrop>\d+)\s+(?P<qebDrop>\d+)$"
        )

        # AQM Global counters
        p3 = re.compile(r"^AQM Global counters$")

        # Asic:1 Core:0 DATA Port:8 Hardware Drop Counters
        p4 = re.compile(r"^Asic:.*Hardware Drop Counters$")

        for line in output.splitlines():
            line = line.strip()

            m = p3.match(line)
            if m:
                enqueue_counters = ret_dict.setdefault("enqueue_counters", {})
                drop_counters = ret_dict.setdefault("drop_counters", {})

            """
            ----------------------------------------------------------------------------------------------
            Q Buffers          Enqueue-TH0          Enqueue-TH1          Enqueue-TH2             Qpolicer
            (Count)              (Bytes)              (Bytes)              (Bytes)              (Bytes)
            -- ------- -------------------- -------------------- -------------------- --------------------
            0       0                    0                13114            129171972                    0
            1       0                    0                    0            546062296                    0
            2       0                    0                    0                    0                    0
            3       0                    0                    0                    0                    0
            4       0                    0                    0                    0                    0
            5       0                    0                    0                    0                    0
            6       0                    0                    0                    0                    0
            7       0                    0                    0                    0                    0
            """

            # AQM Global counters
            m = p1.match(line)
            if not drop_section and m:
                group = m.groupdict()
                q = int(group["Q"])
                enqueue_dict = enqueue_counters.setdefault(q, {})
                enqueue_dict.update(
                    {
                        "buffers_count": int(group["buffers_count"]),
                        "enqueue_th0": int(group["enqueue_th0"]),
                        "enqueue_th1": int(group["enqueue_th1"]),
                        "enqueue_th2": int(group["enqueue_th2"]),
                        "q_policer": int(group["qpolicer"]),
                    }
                )
                continue

            m = p1_1.match(line)
            if not drop_section and m:
                group = m.groupdict()
                q = int(group["Q"])
                enqueue_dict = enqueue_counters.setdefault(q, {})
                enqueue_dict.update(
                    {
                        "buffers_count": int(group["buffers_count"]),
                        "enqueue_th0": int(group["enqueue_th0"]),
                        "enqueue_th1": int(group["enqueue_th1"]),
                        "enqueue_th2": int(group["enqueue_th2"]),
                    }
                )
                continue

            # Asic:1 Core:0 DATA Port:8 Hardware Drop Counters
            m = p4.match(line)
            if m:
                # Entering "drop_section"
                drop_section = True
            """
            --------------------------------------------------------------------------------------------------------------------------------
            Q             Drop-TH0             Drop-TH1             Drop-TH2             SBufDrop              QebDrop         QpolicerDrop
                      (Bytes)              (Bytes)              (Bytes)              (Bytes)              (Bytes)              (Bytes)
            -- -------------------- -------------------- -------------------- -------------------- -------------------- --------------------
            0                    0                    0                    0                    0                    0                    0
            1                    0                    0                    0                    0                    0                    0
            2                    0                    0                    0                    0                    0                    0
            3                    0                    0                    0                    0                    0                    0
            4                    0                    0                    0                    0                    0                    0
            5                    0                    0                    0                    0                    0                    0
            6                    0                    0                    0                    0                    0                    0
            7                    0                    0                    0                    0                    0                    0
            """

            m = p2.match(line)
            if drop_section and m:
                group = m.groupdict()
                q = int(group["Q"])
                drop_dict = drop_counters.setdefault(q, {})
                drop_dict.update(
                    {
                        "drop_th0": int(group["drop_th0"]),
                        "drop_th1": int(group["drop_th1"]),
                        "drop_th2": int(group["drop_th2"]),
                        "s_buf_drop": int(group["sbufDrop"]),
                        "q_eb_drop": int(group["qebDrop"]),
                        "q_policer_drop": int(group["qpolicerDrop"]),
                    }
                )
                continue

            m = p2_1.match(line)
            if drop_section and m:
                group = m.groupdict()
                q = int(group["Q"])
                drop_dict = drop_counters.setdefault(q, {})
                drop_dict.update(
                    {
                        "drop_th0": int(group["drop_th0"]),
                        "drop_th1": int(group["drop_th1"]),
                        "drop_th2": int(group["drop_th2"]),
                        "s_buf_drop": int(group["sbufDrop"]),
                        "q_eb_drop": int(group["qebDrop"]),
                    }
                )
                continue

        return ret_dict


class ShowPlatformHardwarelabel2qmapQmapegressdataSchema(MetaParser):
    """Schema for show platform hardware fed active qos queue stats"""

    schema = {
        Any(): {
            "queue": int,
            "threshold": int,
            "v_queue": int,
        },
    }


class ShowPlatformHardwareFedActiveQosQueuelabel2qmapQmapegressdataInterface(
    ShowPlatformHardwarelabel2qmapQmapegressdataSchema
):

    """
    Parser for:
        * show platform hardware fed active qos queue label2qmap qmap-egress-data interface
        * show platform hardware fed switch 1 qos queue label2qmap qmap-egress-data interface
    """

    cli_command = [
        "show platform hardware fed active qos queue label2qmap qmap-egress-data interface {interface}",
        "show platform hardware fed switch {switch_num} qos queue label2qmap qmap-egress-data interface {interface}",
    ]

    def cli(self, interface, output=None, switch_num=None):
        if output is None:
            if switch_num is None:
                cmd = self.cli_command[0].format(interface=interface)
            else:
                cmd = self.cli_command[1].format(
                    switch_num=switch_num, interface=interface
                )

            output = self.device.execute(cmd)

        ret_dict = {}

        """
        Egress DATA Queue Mapping  -  Asic/Core/Port: 0/0/0

        ===============================================================================
        Label   Q Threshold  VQ  |  Label   Q Threshold  VQ  |  Label   Q Threshold  VQ
        ===== === ========= ===  |  ===== === ========= ===  |  ===== === ========= ===
        0   1         2   0         1   1         2   0         2   1         2   0
        3   1         2   0         4   1         2   0         5   1         2   0
        """
        p1 = re.compile(
            r"(?P<Label>\d+)\s+(?P<Q>\d+)\s+(?P<Threshold>\d+)\s+(?P<VQ>\d+)\s+"
            + r"(?P<Label1>\d+)\s+(?P<Q1>\d+)\s+(?P<Threshold1>\d+)\s+(?P<VQ1>\d+)\s+"
            + r"(?P<Label2>\d+)\s+(?P<Q2>\d+)\s+(?P<Threshold2>\d+)\s+(?P<VQ2>\d+)"
        )

        for line in output.splitlines():
            line = line.strip()
            """
            Egress DATA Queue Mapping  -  Asic/Core/Port: 0/0/0
            ===============================================================================
            Label   Q Threshold  VQ  |  Label   Q Threshold  VQ  |  Label   Q Threshold  VQ
            ===== === ========= ===  |  ===== === ========= ===  |  ===== === ========= ===
              0   1         2   0         1   1         2   0         2   1         2   0
              3   1         2   0         4   1         2   0         5   1         2   0
            """

            m = p1.match(line)
            if m:
                group = m.groupdict()
                label = int(group["Label"])
                label_dic = ret_dict.setdefault(label, {})
                label_dic["queue"] = int(group["Q"])
                label_dic["threshold"] = int(group["Threshold"])
                label_dic["v_queue"] = int(group["VQ"])
                label1 = int(group["Label1"])
                label_dic1 = ret_dict.setdefault(label1, {})
                label_dic1["queue"] = int(group["Q1"])
                label_dic1["threshold"] = int(group["Threshold1"])
                label_dic1["v_queue"] = int(group["VQ1"])
                label2 = int(group["Label2"])
                label_dic2 = ret_dict.setdefault(label2, {})
                label_dic2["queue"] = int(group["Q2"])
                label_dic2["threshold"] = int(group["Threshold2"])
                label_dic2["v_queue"] = int(group["VQ2"])
                continue
        return ret_dict


# ======================================================================================
#  Schema for
#  * 'show platform hardware fed switch active fwd resource utilization | include LABEL'
# =======================================================================================
class ShowPlatformHardwareFedSwitchActiveFwdResourceUtilizationLabelSchema(MetaParser):
    """Schema for 'show platform hardware fed switch active fwd resource utilization | include LABEL'"""

    schema = {
        "resource_name": {
            Any(): {
                "allocated": int,
                "free": int,
            }
        }
    }


# =======================================================================================
#  Parser for
#  * 'show platform hardware fed switch active fwd resource utilization | include LABEL'
# =======================================================================================


class ShowPlatformHardwareFedSwitchActiveFwdResourceUtilizationLabel(
    ShowPlatformHardwareFedSwitchActiveFwdResourceUtilizationLabelSchema
):
    """
    Parser for :
        * show platform hardware fed switch active fwd resource utilization | include LABEL
    """

    cli_command = "show platform hardware fed switch active fwd resource utilization | include {label}"

    def cli(self, label="", output=None):
        if output is None:
            cmd = self.cli_command.format(label=label)
            output = self.device.execute(cmd)
        else:
            output = output
        # initial return dictionary
        ret_dict = {}
        # RSC_LABEL_STACK_ID           6       65531
        p1 = re.compile(r"(?P<resource_name>\S+)\s+(?P<allocated>\d+)\s+(?P<free>\d+)$")
        for line in output.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                group = m.groupdict()
                resource_name = group["resource_name"]
                sub_dict = ret_dict.setdefault("resource_name", {}).setdefault(
                    resource_name, {}
                )

                allocated = group["allocated"]
                sub_dict["allocated"] = int(allocated)

                free = group["free"]
                sub_dict["free"] = int(free)
                continue

        return ret_dict


# ================================================================================
# Parser Schema for 'show platform hardware fed active qos queue config interface'
#            or 'show platform hardware fed switch <no> qos queue config interface'
# ================================================================================
class ShowPlatformHardwareFedActiveQosQueueConfigInterfaceSchema(MetaParser):
    """Schema for show platform hardware fed active qos queue config interface"""

    schema = {
        Optional("asic"): int,
        Optional("core"): int,
        "data_port": int,
        "gpn": int,
        Optional("linkspeed"): str,
        "afd": str,
        Optional("flatafd"): str,
        "qosmap": int,
        "hw_queues": {
            "min": int,
            "max": int,
        },
        "drainfast": str,
        "portsoftstart": {
            "min": int,
            "max": int,
        },
        Optional("buffersharing"): str,
        "queue": {
            int: {
                "dts": int,
                "hardmax": int,
                "softmax": int,
                "portsmin": int,
                "glblsmin": int,
                "portstend": int,
                Optional("qenable"): str,
                "priority": int,
                "schedule_mode": str,
                "weight": int,
                "shaping_step": int,
                Optional("sharpedweight"): int,
                "weight0": int,
                "max_th0": int,
                "min_th0": int,
                "weight1": int,
                "max_th1": int,
                "min_th1": int,
                "weight2": int,
                "max_th2": int,
                "min_th2": int,
            },
        },
        Optional("port"): {
            "priority": int,
            "schedule_mode": str,
            "weight": int,
            "shaping_step": int,
            Optional("sharpedweight"): int,
        },
    }


# ================================================================================
# Parser for 'show platform hardware fed active qos queue config interface'
#         or 'show platform hardware fed switch <no> qos queue config interface'
# ================================================================================
class ShowPlatformHardwareFedActiveQosQueueConfigInterface(
    ShowPlatformHardwareFedActiveQosQueueConfigInterfaceSchema
):
    cli_command = [
        "show platform hardware fed active qos queue config interface {interface}",
        "show platform hardware fed switch {switch_num} qos queue config interface {interface}",
    ]

    def cli(self, interface, switch_num=None, output=None):
        if output is None:
            if switch_num is None:
                cmd = self.cli_command[0].format(interface=interface)
            else:
                cmd = self.cli_command[1].format(
                    switch_num=switch_num, interface=interface
                )

            output = self.device.execute(cmd)

        ret_dict = {}

        """
        Asic:1 Core:1 DATA Port:70 GPN:325 LinkSpeed:0xa
        AFD:Disabled FlatAFD:Disabled QoSMap:0 HW Queues: 560 - 567
        """
        p1 = re.compile(
            r"^Asic:(?P<asic>\d+)\s+Core:(?P<core>\d+)\s+DATA Port:(?P<data_port>\d+)\s+GPN:(?P<gpn>\d+)\s+LinkSpeed:(?P<linkspeed>\S+)$"
        )
        p2 = re.compile(
            r"^AFD:(?P<afd>\S+)\s+FlatAFD:(?P<flatafd>\S+)\s+QoSMap:(?P<qosmap>\d+)\s+HW Queues:\s*(?P<hw_queue1>\d+)\s*-\s*(?P<hw_queue2>\d+)$"
        )

        """
        DATA Port:0 GPN:97 AFD:Disabled QoSMap:0 HW Queues: 0 - 7
        """
        p2_1 = re.compile(
            r"^DATA Port:(?P<data_port>\d+)\s+GPN:(?P<gpn>\d+)\s+AFD:(?P<afd>\S+)\s+QoSMap:(?P<qosmap>\d+)\s+HW Queues:\s*(?P<hw_queue1>\d+)\s*-\s*(?P<hw_queue2>\d+)$"
        )

        """
        DrainFast:Disabled PortSoftStart:3 - 42000 BufferSharing:Disabled
        """
        p3 = re.compile(
            r"^DrainFast:(?P<drainfast>\S+)\s+PortSoftStart:(?P<portsoftstart1>\d+)\s*-\s*(?P<portsoftstart2>\d+)\s+BufferSharing:(?P<buffersharing>\S+)$"
        )

        """
        DrainFast:Disabled PortSoftStart:2 - 2016
        """
        p3_1 = re.compile(
            r"^DrainFast:(?P<drainfast>\S+)\s+PortSoftStart:(?P<portsoftstart1>\d+)\s*-\s*(?P<portsoftstart2>\d+)$"
        )

        """
           DTS  Hardmax  Softmax   PortSMin  GlblSMin  PortStEnd   QEnable
          ----- --------  --------  --------  --------  ---------  -------
        0   1  2   224   5 42000   0     0   0     0   1 42000      En
        1   1  0     0   5 42000   1  1312   0     0   1 42000      En
        """
        p4 = re.compile(
            r"^(?P<q_no>\d+)\s+(?P<dts>\d+)\s+(\d+)\s+(?P<hardmax>\d+)\s+"
            r"(\d+)\s+(?P<softmax>\d+)\s+(\d+)\s+(?P<portsmin>\d+)\s+(\d+)\s+(?P<glblsmin>\d+)\s+"
            r"(\d+)\s+(?P<portstend>\d+)\s+(?P<qenable>\S+)$"
        )

        """
          DTS  Hardmax  Softmax   PortSMin  GlblSMin  PortStEnd
          ----- --------  --------  --------  --------  ---------
        0   1  2   224   5 42000   0     0   0     0   1 42000
        1   1  0     0   5 42000   1  1312   0     0   1 42000
        """
        p4_1 = re.compile(
            r"^(?P<q_no>\d+)\s+(?P<dts>\d+)\s+(\d+)\s+(?P<hardmax>\d+)\s+"
            r"(\d+)\s+(?P<softmax>\d+)\s+(\d+)\s+(?P<portsmin>\d+)\s+(\d+)\s+(?P<glblsmin>\d+)\s+"
            r"(\d+)\s+(?P<portstend>\d+)$"
        )

        """
        Priority   Shaped/shared   weight  shaping_step  sharpedWeight
        --------   -------------   ------  ------------   -------------
        0      0     Shared            50           0           0

        """
        p5 = re.compile(
            r"^(?P<q_no>\d+)\s+(?P<priority>\d+)\s+(?P<mode>\S+)\s+"
            r"(?P<weight>\d+)\s+(?P<shaping_step>\d+)\s+(?P<sharpedweight>\d+)$"
        )

        """
        Priority   Shaped/shared   weight  shaping_step
        --------   -------------   ------  ------------
        0      0     Shared            50           0

        """
        p5_1 = re.compile(
            r"^(?P<q_no>\d+)\s+(?P<priority>\d+)\s+(?P<mode>\S+)\s+"
            r"(?P<weight>\d+)\s+(?P<shaping_step>\d+)$"
        )

        """
           Weight0 Max_Th0 Min_Th0 Weigth1 Max_Th1 Min_Th1  Weight2 Max_Th2 Min_Th2
        ------- ------- ------- ------- ------- -------  ------- ------- ------
        0       0   33647       0       0   37605       0       0   42224       0
        1       0   33468       0       0   37406       0       0   42000       0

        """
        p6 = re.compile(
            r"^(?P<q_no>\d+)\s+(?P<weight0>\d+)\s+(?P<max_th0>\d+)\s+(?P<min_th0>\d+)\s+"
            r"(?P<weight1>\d+)\s+(?P<max_th1>\d+)\s+(?P<min_th1>\d+)\s+"
            r"(?P<weight2>\d+)\s+(?P<max_th2>\d+)\s+(?P<min_th2>\d+)$"
        )

        """
        Port       Port            Port    Port          Port
        Priority   Shaped/shared   weight  shaping_step  sharpedWeight
        --------   -------------   ------  ------------  -------------
            2     Sharped           100        1023      1023

        or (older releases)

         Port       Port            Port    Port
        Priority   Shaped/shared   weight  shaping_step
        --------   -------------   ------  ------------
            2     Shaped          1023        1023


        """
        p7 = re.compile(
            r"^(?P<priority>\d+)\s+(?P<mode>\S+)\s+(?P<weight>\d+)\s+(?P<step>\d+)\s+(?P<s_weight>\d+)$"
        )
        p7_1 = re.compile(
            r"^(?P<priority>\d+)\s+(?P<mode>\S+)\s+(?P<weight>\d+)\s+(?P<step>\d+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict["asic"] = int(group["asic"])
                ret_dict["core"] = int(group["core"])
                ret_dict["data_port"] = int(group["data_port"])
                ret_dict["gpn"] = int(group["gpn"])
                ret_dict["linkspeed"] = group["linkspeed"].lower()
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict["afd"] = group["afd"].lower()
                ret_dict["flatafd"] = group["flatafd"].lower()
                ret_dict["qosmap"] = int(group["qosmap"])
                ret_dict["hw_queues"] = dict()
                ret_dict["hw_queues"]["min"] = int(group["hw_queue1"])
                ret_dict["hw_queues"]["max"] = int(group["hw_queue2"])
                continue

            m = p2_1.match(line)
            if m:
                group = m.groupdict()
                ret_dict["data_port"] = int(group["data_port"])
                ret_dict["gpn"] = int(group["gpn"])
                ret_dict["afd"] = group["afd"].lower()
                ret_dict["qosmap"] = int(group["qosmap"])
                ret_dict["hw_queues"] = dict()
                ret_dict["hw_queues"]["min"] = int(group["hw_queue1"])
                ret_dict["hw_queues"]["max"] = int(group["hw_queue2"])
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict["drainfast"] = group["drainfast"].lower()
                ret_dict["portsoftstart"] = dict()
                ret_dict["portsoftstart"]["min"] = int(group["portsoftstart1"])
                ret_dict["portsoftstart"]["max"] = int(group["portsoftstart2"])
                ret_dict["buffersharing"] = group["buffersharing"].lower()
                continue

            m = p3_1.match(line)
            if m:
                group = m.groupdict()
                ret_dict["drainfast"] = group["drainfast"].lower()
                ret_dict["portsoftstart"] = dict()
                ret_dict["portsoftstart"]["min"] = int(group["portsoftstart1"])
                ret_dict["portsoftstart"]["max"] = int(group["portsoftstart2"])
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault("queue", dict()).setdefault(
                    int(group["q_no"]), dict()
                )
                ret_dict["queue"][int(group["q_no"])]["dts"] = int(group["dts"])
                ret_dict["queue"][int(group["q_no"])]["hardmax"] = int(group["hardmax"])
                ret_dict["queue"][int(group["q_no"])]["softmax"] = int(group["softmax"])
                ret_dict["queue"][int(group["q_no"])]["portsmin"] = int(
                    group["portsmin"]
                )
                ret_dict["queue"][int(group["q_no"])]["glblsmin"] = int(
                    group["glblsmin"]
                )
                ret_dict["queue"][int(group["q_no"])]["portstend"] = int(
                    group["portstend"]
                )
                ret_dict["queue"][int(group["q_no"])]["qenable"] = group[
                    "qenable"
                ].lower()
                continue

            m = p4_1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault("queue", dict()).setdefault(
                    int(group["q_no"]), dict()
                )
                ret_dict["queue"][int(group["q_no"])]["dts"] = int(group["dts"])
                ret_dict["queue"][int(group["q_no"])]["hardmax"] = int(group["hardmax"])
                ret_dict["queue"][int(group["q_no"])]["softmax"] = int(group["softmax"])
                ret_dict["queue"][int(group["q_no"])]["portsmin"] = int(
                    group["portsmin"]
                )
                ret_dict["queue"][int(group["q_no"])]["glblsmin"] = int(
                    group["glblsmin"]
                )
                ret_dict["queue"][int(group["q_no"])]["portstend"] = int(
                    group["portstend"]
                )
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault("queue", dict()).setdefault(
                    int(group["q_no"]), dict()
                )
                ret_dict["queue"][int(group["q_no"])]["priority"] = int(
                    group["priority"]
                )
                ret_dict["queue"][int(group["q_no"])]["schedule_mode"] = group[
                    "mode"
                ].lower()
                ret_dict["queue"][int(group["q_no"])]["weight"] = int(group["weight"])
                ret_dict["queue"][int(group["q_no"])]["shaping_step"] = int(
                    group["shaping_step"]
                )
                ret_dict["queue"][int(group["q_no"])]["sharpedweight"] = int(
                    group["sharpedweight"]
                )
                continue

            m = p5_1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault("queue", dict()).setdefault(
                    int(group["q_no"]), dict()
                )
                ret_dict["queue"][int(group["q_no"])]["priority"] = int(
                    group["priority"]
                )
                ret_dict["queue"][int(group["q_no"])]["schedule_mode"] = group[
                    "mode"
                ].lower()
                ret_dict["queue"][int(group["q_no"])]["weight"] = int(group["weight"])
                ret_dict["queue"][int(group["q_no"])]["shaping_step"] = int(
                    group["shaping_step"]
                )
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault("queue", dict()).setdefault(
                    int(group["q_no"]), dict()
                )
                ret_dict["queue"][int(group["q_no"])]["weight0"] = int(group["weight0"])
                ret_dict["queue"][int(group["q_no"])]["max_th0"] = int(group["max_th0"])
                ret_dict["queue"][int(group["q_no"])]["min_th0"] = int(group["min_th0"])
                ret_dict["queue"][int(group["q_no"])]["weight1"] = int(group["weight1"])
                ret_dict["queue"][int(group["q_no"])]["max_th1"] = int(group["max_th1"])
                ret_dict["queue"][int(group["q_no"])]["min_th1"] = int(group["min_th1"])
                ret_dict["queue"][int(group["q_no"])]["weight2"] = int(group["weight2"])
                ret_dict["queue"][int(group["q_no"])]["max_th2"] = int(group["max_th2"])
                ret_dict["queue"][int(group["q_no"])]["min_th2"] = int(group["min_th2"])
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict["port"] = dict()
                ret_dict["port"]["priority"] = int(group["priority"])
                ret_dict["port"]["schedule_mode"] = group["mode"].lower()
                ret_dict["port"]["weight"] = int(group["weight"])
                ret_dict["port"]["shaping_step"] = int(group["step"])
                ret_dict["port"]["sharpedweight"] = int(group["s_weight"])
                continue

            m = p7_1.match(line)
            if m:
                group = m.groupdict()
                ret_dict["port"] = dict()
                ret_dict["port"]["priority"] = int(group["priority"])
                ret_dict["port"]["schedule_mode"] = group["mode"].lower()
                ret_dict["port"]["weight"] = int(group["weight"])
                ret_dict["port"]["shaping_step"] = int(group["step"])
                continue

        return ret_dict


# ======================================================
# Parser for 'show platform hardware fed switch {switch} fwd-asic resource utilization'
# ======================================================
class ShowPlatformHardwareFedSwitchResourceUtilizationSchema(MetaParser):
    """Schema for show platform hardware fed switch {switch} fwd-asic resource utilization"""

    schema = {
        "asic_instance": {
            Any(): {
                "resource": {
                    Any(): {"resource_name": str, "allocated": int, "free": int}
                }
            },
        },
    }


class ShowPlatformHardwareFedSwitchResourceUtilization(
    ShowPlatformHardwareFedSwitchResourceUtilizationSchema
):
    """Parser for show platform hardware fed switch {switch} fwd-asic resource utilization"""

    cli_command = [
        "show platform hardware fed active fwd-asic resource utilization",
        "show platform hardware fed switch {switch} fwd-asic resource utilization",
    ]

    def cli(self, switch=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[1].format(switch=switch)
            else:
                cmd = self.cli_command[0]

            output = self.device.execute(cmd)

        # Resource Info for ASIC Instance:    0
        p1 = re.compile(r"^Resource Info for ASIC Instance:\s+(?P<asic_instance>\d+)$")

        # RSC_DI                     149       41525
        p2 = re.compile(
            r"^(?P<resource_name>\w+)\s+(?P<allocated>\d+)\s+(?P<free>\d+)$"
        )

        ret_dict = {}
        current_asic = "0"

        for line in output.splitlines():
            line = line.strip()

            # Resource Info for ASIC Instance: 0
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                current_asic = dict_val["asic_instance"]

            # RSC_DI                      149       41525
            m = p2.match(line)
            if m:
                dict_val = m.groupdict()
                asic_group = ret_dict.setdefault("asic_instance", {})
                asic_dict = ret_dict["asic_instance"].setdefault(current_asic, {})
                resource_var = dict_val["resource_name"]
                resource_group = ret_dict["asic_instance"][current_asic].setdefault(
                    "resource", {}
                )
                resource_dict = ret_dict["asic_instance"][current_asic][
                    "resource"
                ].setdefault(resource_var, {})
                resource_dict["resource_name"] = dict_val["resource_name"]
                resource_dict["allocated"] = int(dict_val["allocated"])
                resource_dict["free"] = int(dict_val["free"])
                continue

        return ret_dict


# ======================================================
# Parser for 'show platform hardware fed switch active qos dscp-cos counters interface {interface} '
# ======================================================
class ShowPlatformHardwareFedSwitchActiveQosDscpCosCountersInterfaceSchema(MetaParser):
    """Schema for show platform hardware fed switch active qos dscp-cos counters interface {interface}"""

    schema = {
        Optional("heading"): str,
        "direction": {Any(): {"qos": {Any(): {"frames": int, "bytes": int}}}},
    }


class ShowPlatformHardwareFedSwitchActiveQosDscpCosCountersInterface(
    ShowPlatformHardwareFedSwitchActiveQosDscpCosCountersInterfaceSchema
):
    """Parser for show platform hardware fed {switch} qos dscp-cos counters interface {interface}"""

    cli_command = [
        "show platform hardware fed {switch} {switch_var} qos dscp-cos counters interface {interface}",
        "show platform hardware fed {switch_var} qos dscp-cos counters interface {interface}",
    ]

    def cli(self, interface, switch_var, switch="", output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(
                    switch=switch, switch_var=switch_var, interface=interface
                )
            else:
                cmd = self.cli_command[1].format(
                    switch_var=switch_var, interface=interface
                )
            output = self.device.execute(cmd)

        #               Frames        Bytes
        p0 = re.compile(r"^(?P<heading>\AFrames[\s]+ +Bytes)$")

        # Ingress DSCP0 0             0
        # Egress DSCP0 0             0
        p1 = re.compile(
            r"^(?P<direction>\w+)\s+(?P<qos>\S+)\s+(?P<frames>\d+)\s+(?P<bytes>\d+)$"
        )

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            #               Frames        Bytes
            m = p0.match(line)
            if m:
                group = m.groupdict()
                ret_dict["heading"] = group["heading"].strip()
                continue

            # Ingress DSCP0 0             0
            # Egress DSCP0 0             0
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                dir_dict = ret_dict.setdefault("direction", {}).setdefault(
                    dict_val["direction"].lower(), {}
                )
                qos_dict = dir_dict.setdefault("qos", {}).setdefault(
                    dict_val["qos"], {}
                )
                qos_dict["frames"] = int(dict_val["frames"])
                qos_dict["bytes"] = int(dict_val["bytes"])
                continue

        return ret_dict


class ShowPlatformHardwareFedSwitchActiveQosDscpCosCountersInterface(
    ShowPlatformHardwareFedSwitchActiveQosDscpCosCountersInterfaceSchema
):
    """Parser for show platform hardware fed {switch} qos dscp-cos counters interface {interface}"""

    cli_command = [
        "show platform hardware fed {switch} {switch_var} qos dscp-cos counters interface {interface}",
        "show platform hardware fed {switch_var} qos dscp-cos counters interface {interface}",
    ]

    def cli(self, interface, switch_var, switch="", output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(
                    switch=switch, switch_var=switch_var, interface=interface
                )
            else:
                cmd = self.cli_command[1].format(
                    switch_var=switch_var, interface=interface
                )
            output = self.device.execute(cmd)

        #               Frames        Bytes
        p0 = re.compile(r"^(?P<heading>\AFrames[\s]+ +Bytes)$")

        # Ingress DSCP0 0             0
        # Egress DSCP0 0             0
        p1 = re.compile(
            r"^(?P<direction>\w+)\s+(?P<qos>\S+)\s+(?P<frames>\d+)\s+(?P<bytes>\d+)$"
        )

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            #               Frames        Bytes
            m = p0.match(line)
            if m:
                group = m.groupdict()
                ret_dict["heading"] = group["heading"].strip()
                continue

            # Ingress DSCP0 0             0
            # Egress DSCP0 0             0
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                dir_dict = ret_dict.setdefault("direction", {}).setdefault(
                    dict_val["direction"].lower(), {}
                )
                qos_dict = dir_dict.setdefault("qos", {}).setdefault(
                    dict_val["qos"], {}
                )
                qos_dict["frames"] = int(dict_val["frames"])
                qos_dict["bytes"] = int(dict_val["bytes"])
                continue

        return ret_dict


class ShowPlatformHardwareFedQosSchedulerSdkInterfaceSchema(MetaParser):
    """Schema for show platform hardware fed {switch} {mode} qos scheduler sdk interface {interface}"""

    schema = {
        "interface": {
            Any(): {
                "interface_id": str,
                "port_scheduler": {
                    "interface_sch_oid": int,
                    "interface_sch_id": str,
                    "system_port_sch_oid": int,
                    "system_port_sch_id": str,
                    "priority_propagation": str,
                    "sub_interface_q_mode": str,
                    "logical_port": str,
                    "tc_profile": {"sdk_oid": int, "tc": {Any(): {"voq_offset": int}}},
                },
                "interface_scheduler": {
                    Any(): {"credit": int, "transmit": int, "weight": int}
                },
                "interface_scheduler_oqpg": {
                    Any(): {
                        "rr": {
                            "credit_cir": str,
                            "credit_burst": str,
                            "transmit_cir": str,
                            "transmit_burst": str,
                        },
                        "wfq": {"weights_pir": int, "weights_actual": int},
                        Optional("oq_list"): list,
                    }
                },
                "lpse_oqse_oqpg": {
                    Any(): {
                        "oqpg_associated": str,
                        "credit_pir": str,
                        "credit_burst": str,
                        "transmit_pir": str,
                        "transmit_burst": str,
                        Optional("weights"): {"uc": int, "mc": int},
                        Optional("oqse_oid"): {"oid": int, "id": str},
                    }
                },
                "lpse": {
                    "oid": int,
                    "id": str,
                    "cir_weight": list,
                    "eir_weight": list,
                    Optional("main_interface_oqse"): list,
                    Optional("oqse_credit_cir"): list,
                    Optional("oqse_credit_cir_burst"): list,
                    Optional("oqse_credit_pir"): list,
                    Optional("oqse_credit_pir_burst"): list,
                    Optional("total_attached_oqse"): int,
                    Optional("lpse_cir_priority_queue_rate"): list,
                    Optional("lpse_cir_priority_queue_burst"): list,
                    Optional("lpse_pir_sub_interface_port_rate"): list,
                    Optional("lpse_pir_sub_interface_port_burst"): list,
                },
                "oqse_voq_vsc": {
                    "oq_id": {
                        Any(): {
                            "oqse_oid": int,
                            "oqse_id": str,
                            "scheduling_mode": str,
                            Optional("credit_cir"): str,
                            Optional("credit_cir_burst"): str,
                            Optional("credit_pir"): str,
                            Optional("credit_pir_burst"): str,
                            Optional("transmit_pir"): str,
                            Optional("transmit_pir_burst"): str,
                            "rr_weights": list,
                            "rr_weights_actual": list,
                            "rr": {
                                Any(): {
                                    "in_slice": {
                                        Any(): {
                                            "in_device": int,
                                            "vsc_id": int,
                                            "voq_id": int,
                                            "vsc_pir": int,
                                            "vsc_burst": int,
                                        }
                                    }
                                }
                            },
                        }
                    }
                },
            }
        }
    }


class ShowPlatformHardwareFedQosSchedulerSdkInterface(
    ShowPlatformHardwareFedQosSchedulerSdkInterfaceSchema
):
    """Parser for show platform hardware fed {switch} {mode} qos scheduler sdk interface {interface}"""

    cli_command = [
        "show platform hardware fed {mode} qos scheduler sdk interface {interface}",
        "show platform hardware fed {switch} {mode} qos scheduler sdk interface {interface}",
    ]

    def cli(self, mode, interface, switch=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[1].format(
                    switch=switch, mode=mode, interface=interface
                )
            else:
                cmd = self.cli_command[0].format(mode=mode, interface=interface)

            output = self.device.execute(cmd)

        # Interface              : HundredGigE1/0/5 (0x54A)
        p0 = re.compile(r"^Interface\s+: (?P<interface>\S+) \((?P<interface_id>\S+)\)$")

        # Port Scheduler Configuration
        p1_0 = re.compile(r"^Port Scheduler Configuration$")

        # Interface SCH OID     : 1343 (  0x53F)
        p1_1 = re.compile(
            r"^Interface SCH OID\s+: (?P<interface_sch_oid>\d+)\s+\(\s*(?P<interface_sch_id>\S+)\)$"
        )

        # System Port SCH OID   : 1347 (  0x543)
        # System Port SCH OID   : 746  (  0x2EA)
        p1_2 = re.compile(
            r"^System Port SCH OID\s+: (?P<system_port_sch_oid>\d+)\s+\(\s*(?P<system_port_sch_id>\S+)\)$"
        )

        # Priority Propagation  : Disabled
        p1_3 = re.compile(r"^Priority Propagation\s+: (?P<priority_propagation>\w+)$")

        # Sub-interface Q Mode  : Disabled - No Priority Propagation
        p1_4 = re.compile(r"^Sub-interface Q Mode  : (?P<sub_interface_q_mode>.+)$")

        # Logical Port          : Enabled
        p1_5 = re.compile(r"^Logical Port\s+: (?P<logical_port>\w+)$")

        # TC Profile            : SDK OID    :   209
        p1_6 = re.compile(r"^TC Profile\s+: SDK OID\s+:\s+(?P<sdk_oid>\d+)$")

        # : TC         : TC0 | TC1 | TC2 | TC3 | TC4 | TC5 | TC6 | TC7
        p1_7 = re.compile(r"^: TC         : (?P<tc>[\w\s\|]+)$")

        # : VOQ Offset :   0 |   1 |   2 |   3 |   4 |   5 |   6 |   7
        p1_8 = re.compile(r"^: VOQ Offset :\s+(?P<voq_offset>[\d\s\|]+)$")

        # Interface Scheduler Configuration
        p2_0 = re.compile(r"^Interface Scheduler Configuration$")

        # Credit        : 12000081000
        p2_1 = re.compile(r"^Credit\s+: (?P<credit>\d+)$")

        # CIR [RR]  | Transmit      : 12000081000
        # PIR [WFQ] | Transmit      : 12000081000
        p2_2 = re.compile(
            r"^(?P<interface_scheduler>\w+) \[.+\]\s+\| Transmit\s+: (?P<transmit>\d+)$"
        )

        # Weight        : 1
        p2_3 = re.compile(r"^Weight\s+: (?P<weight>\d+)$")

        # Interface Scheduler - OQPG  Configuration
        p3_0 = re.compile(r"^Interface Scheduler - OQPG  Configuration$")

        # PG TYPE           || OQPG-0           | OQPG-1           | OQPG-2           | OQPG-3
        #            | OQPG-4           | OQPG-5           | OQPG-6           | OQPG-7
        p3_1 = re.compile(r"PG TYPE           \|\| (?P<oqpg>[OQPG\-\d\s\|]+)")

        # Credit CIR    || 0                | 0                | 0                | 0
        # | 0                | 0                | 0                | SDK Default
        p3_2 = re.compile(r"^Credit CIR\s+\|\| (?P<credit_cir>[\w\|\s]+)$")

        # RR |Credit Burst  || 0                | 0                | 0                | 0
        # | 0                | 0                | 0                | 30
        p3_3 = re.compile(r"^RR \|Credit Burst\s+\|\| (?P<credit_burst>[\w\|\s]+)$")

        # Transmit CIR  || 0                | 0                | 0                | 0
        #                 | 0                | 0                | 0                | SDK Default
        p3_4 = re.compile(
            r"^(?P<transmit_type>Transmit CIR\s+|Transmit Burst)\|\| (?P<transmit_values>[\w\|\s]+)$"
        )

        # WFQ|Weights PIR  || 0                | 0                | 0                | 0
        # | 0                | 0                | 0                | 30
        p3_5 = re.compile(r"^WFQ\|Weights PIR\s+\|\| (?P<weights_pir>[\w\|\s]+)$")

        # Weights Actual|| 63               | 63               | 63               | 63
        #                | 63               | 63               | 63               | 63
        p3_6 = re.compile(r"^Weights Actual\|\| (?P<weights_actual>[\w\|\s]+)$")

        # OQ List           || 0                |                  |                  |
        #                   |                  |                  |                  | 1 2 3 4 5 6 7
        p3_7 = re.compile(r"^OQ List\s+\|\| (?P<oq_list>[\d\|\s]+)$")

        # LPSE/OQSE <->  OQPG  Configuration
        p4_0 = re.compile(r"^LPSE\/OQSE <\->\s+OQPG\s+Configuration$")

        # OQ Number         ||    LPSE-OQ-0     |    LPSE-OQ-1     | OQ-2             | OQ-3
        #              | OQ-4             | OQ-5             | OQ-6             | OQ-7
        p4_1 = re.compile(r"^OQ Number\s+\|\|\s+(?P<oq_number>[LPSE\-OQ\d\|\s]+)$")

        # OQPG Associated   || OQPG-0           | OQPG-1           | OQPG-7 [P]       | OQPG-7 [P]
        #        | OQPG-7 [P]       | OQPG-7 [P]       | OQPG-7 [P]       | OQPG-7 [P]
        p4_2 = re.compile(
            r"^OQPG Associated\s+\|\|(?P<oqpg_associated>[OQPG\-\d\s\[P\]\|]+)$"
        )

        # Credit PIR        || SDK Default      | 94921872         | 189843744        | 94921872
        #          | 94921872         | 147656256        | 94921872         | 189843744
        p4_3 = re.compile(
            r"^(?P<lpse_type>Credit PIR|Credit Burst|Transmit PIR|Transmit Burst)\s+\|\| (?P<lpse_values>[\w\|\s]+)$"
        )

        # Weights : UC : MC ||      8 : 2       |      8 : 2       |      8 : 2       |      8 : 2
        #        |      8 : 2       |      8 : 2       |      8 : 2       |      8 : 2
        p4_4 = re.compile(r"^Weights : UC : MC \|\|\s+(?P<uc_mc>[\d:\s\|]+)$")

        # OQSE OID          || LPSE OID : 1356 (0x54C  )           | 1350 (0x546  )   | 1351 (0x547  )
        #    | 1352 (0x548  )   | 1353 (0x549  )   | 1354 (0x54A  )   | 1355 (0x54B  )
        p4_5 = re.compile(
            r"^OQSE OID\s+\|\| LPSE OID : (?P<lpse_oid>\d+) \((?P<lpse_id>\w+)\s*\)\s+\|\s+(?P<oqse_oid>[\d\s\(\)\w\|]+)$"
        )

        # LPSE Configuration
        p5_0 = re.compile(r"^LPSE Configuration$")

        # LPSE OID                  : 1356 (  0x54C)
        p5_1 = re.compile(r"^LPSE OID\s+: (?P<oid>\d+)\s+\(\s+(?P<id>\w+)\)$")

        # LPSE CIR Weight           :   1 :   1 :   1 :   1 :   1 :   1 :   1 :   1
        p5_2 = re.compile(r"^LPSE CIR Weight\s+:(?P<cir_weight>[\s\d:]+)$")

        # LPSE EIR Weight           :   1 :   1 :   1 :   1 :   1 :   1 :   1 :   1
        p5_3 = re.compile(r"^LPSE EIR Weight\s+:(?P<eir_weight>[\s\d:]+)$")

        # LPSE Main Interface OQSE  : 1348 (0x544  )   | 1349 (0x545  )
        p5_4 = re.compile(
            r"^LPSE Main Interface OQSE\s+: (?P<main_interface_oqse>[\d\s\w\(\)\|]+)$"
        )

        # LPSE OQSE Credit CIR      : SDK Default      | 94921872
        p5_5 = re.compile(r"^LPSE OQSE Credit CIR\s+: (?P<oqse_credit_cir>[\w\s\|]+)$")

        # LPSE OQSE Credit CIR Burst: 0                | 30
        p5_6 = re.compile(
            r"^LPSE OQSE Credit CIR Burst: (?P<oqse_credit_cir_burst>[\w\s\|]+)$"
        )

        # LPSE OQSE Credit PIR      : SDK Default      | 94921872
        p5_7 = re.compile(r"^LPSE OQSE Credit PIR\s+: (?P<oqse_credit_pir>[\w\s\|]+)$")

        # LPSE OQSE Credit PIR Burst: 30               | 0
        p5_8 = re.compile(
            r"^LPSE OQSE Credit PIR Burst: (?P<oqse_credit_pir_burst>[\w\s\|]+)$"
        )

        # LPSE Total Attached OQSEs : 2
        p5_9 = re.compile(r"^LPSE Total Attached OQSEs : (?P<total_attached_oqse>\d+)$")

        # LPSE CIR (Priority Queue) Rate      : SDK Default
        p5_10 = re.compile(
            r"^LPSE CIR \(Priority Queue\) Rate\s+: (?P<lpse_cir_priority_queue_rate>[\w\s\|]+)$"
        )

        # LPSE CIR (Priority Queue) Burst     : 30
        p5_11 = re.compile(
            r"^LPSE CIR \(Priority Queue\) Burst\s+: (?P<lpse_cir_priority_queue_burst>[\w\s\|]+)$"
        )

        # LPSE PIR (Sub-Interface Port) Rate  : SDK Default
        p5_12 = re.compile(
            r"^LPSE PIR \(Sub\-Interface Port\) Rate\s+: (?P<lpse_pir_sub_interface_port_rate>[\w\s\|]+)$"
        )

        # LPSE PIR (Sub-Interface Port) Burst : 30
        p5_13 = re.compile(
            r"^LPSE PIR \(Sub\-Interface Port\) Burst\s+: (?P<lpse_pir_sub_interface_port_burst>[\w\s\|]+)$"
        )

        # OQSE <-> VOQ-VSC Configuration
        p6_0 = re.compile(r"^OQSE <\-> VOQ\-VSC Configuration$")

        # OQSE OID              : 1348 (  0x544)
        # OQSE OID              : 749  (  0x2ED)
        p6_1 = re.compile(
            r"^OQSE OID              : (?P<oqse_oid>\d+)\s+\(\s*(?P<oqse_id>\w+)\)$"
        )

        # OQ    ID              : 0
        p6_2 = re.compile(r"^OQ    ID              : (?P<oq_id>\d+)$")

        # Scheduling Mode       : Logical Port SP SP
        p6_3 = re.compile(r"^Scheduling Mode       : (?P<scheduling_mode>.+)$")

        # Credit CIR            : SDK Default
        # Credit PIR            : 189843744
        # Transmit PIR          : 232031248
        p6_4 = re.compile(
            r"^(?P<cir_pir>(Credit|Transmit) (CIR|PIR))\s+: (?P<credit>.+)$"
        )

        # Credit CIR Burst      : 0
        # Credit PIR Burst      : 30
        # Transmit PIR Burst    : 30
        p6_5 = re.compile(
            r"^(?P<cir_pir>(Credit|Transmit) (CIR|PIR) Burst)\s+: (?P<credit_burst>.+)$"
        )

        # RR Weights            :   1 :   1 :   1 :   1 : N/A : N/A : N/A : N/A
        p6_6 = re.compile(r"^RR Weights            :\s+(?P<rr_weights>[\w\s:\/]+)$")

        # RR Weights Actual     : 255 : 255 : 255 : 255 : N/A : N/A : N/A : N/A
        p6_7 = re.compile(
            r"^RR Weights Actual\s+:\s+(?P<rr_weights_actual>[\w\s:\/]+)$"
        )

        # RR3      || In Device |                    0 |                    0 |                    0 |
        #                     0 |                    0 |                    0
        p6_8 = re.compile(
            r"^(?P<rr>RR\d+)      \|\| In Device \|\s+(?P<in_device>[\w\s\|]+)$"
        )

        # In Slice  |                    0 |                    1 |                    2 |
        #                     3 |                    4 |                    5
        p6_9 = re.compile(r"^In Slice\s+\|\s+(?P<in_slice>[\w\s\|]+)$")

        # VSC ID    |                  352 |                  416 |                  480 |
        #                   544 |                  608 |                  672
        p6_10 = re.compile(r"^VSC ID\s+\|\s+(?P<vsc_id>[\w\s\|]+)$")

        # VOQ ID    |                52576 |                52576 |                52576 |
        #                 52576 |                52576 |                52576
        p6_11 = re.compile(r"^VOQ ID\s+\|\s+(?P<voq_id>[\w\s\|]+)$")

        # VSC PIR   |        2678399959040 |        2678399959040 |        2678399959040 |
        #         2678399959040 |        2678399959040 |        2678399959040
        p6_12 = re.compile(r"^VSC PIR\s+\|\s+(?P<vsc_pir>[\w\s\|]+)$")

        # VSC Burst |                  511 |                  511 |                  511 |
        #                   511 |                  511 |                  511
        p6_13 = re.compile(r"^VSC Burst\s+\|\s+(?P<vsc_burst>[\w\s\|]+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip(" |")

            # Interface              : HundredGigE1/0/5 (0x54A)
            m = p0.match(line)
            if m:
                int_dict = ret_dict.setdefault("interface", {}).setdefault(
                    Common.convert_intf_name(m.groupdict()["interface"]), {}
                )
                int_dict["interface_id"] = m.groupdict()["interface_id"]
                continue

            # Port Scheduler Configuration
            m = p1_0.match(line)
            if m:
                port_schedule_dict = int_dict.setdefault("port_scheduler", {})
                continue

            # Interface SCH OID     : 1343 (  0x53F)
            m = p1_1.match(line)
            if m:
                port_schedule_dict["interface_sch_oid"] = int(
                    m.groupdict()["interface_sch_oid"]
                )
                port_schedule_dict["interface_sch_id"] = m.groupdict()[
                    "interface_sch_id"
                ]
                continue

            # System Port SCH OID   : 1347 (  0x543)
            m = p1_2.match(line)
            if m:
                port_schedule_dict["system_port_sch_oid"] = int(
                    m.groupdict()["system_port_sch_oid"]
                )
                port_schedule_dict["system_port_sch_id"] = m.groupdict()[
                    "system_port_sch_id"
                ]
                continue

            # Priority Propagation  : Disabled
            m = p1_3.match(line)
            if m:
                port_schedule_dict["priority_propagation"] = m.groupdict()[
                    "priority_propagation"
                ]
                continue

            # Sub-interface Q Mode  : Disabled - No Priority Propagation
            m = p1_4.match(line)
            if m:
                port_schedule_dict["sub_interface_q_mode"] = m.groupdict()[
                    "sub_interface_q_mode"
                ]
                continue

            # Logical Port          : Enabled
            p1_5 = re.compile(r"^Logical Port\s+: (?P<logical_port>\w+)$")
            m = p1_5.match(line)
            if m:
                port_schedule_dict["logical_port"] = m.groupdict()["logical_port"]
                continue

            # TC Profile            : SDK OID    :   209
            m = p1_6.match(line)
            if m:
                tc_profile_dict = port_schedule_dict.setdefault("tc_profile", {})
                tc_profile_dict["sdk_oid"] = int(m.groupdict()["sdk_oid"])
                continue

            # : TC         : TC0 | TC1 | TC2 | TC3 | TC4 | TC5 | TC6 | TC7
            m = p1_7.match(line)
            if m:
                tc_list = m.groupdict()["tc"].lower().split(" | ")
                tc_dict = tc_profile_dict.setdefault("tc", {})
                continue

            # : VOQ Offset :   0 |   1 |   2 |   3 |   4 |   5 |   6 |   7
            m = p1_8.match(line)
            if m:
                voq_offset_list = m.groupdict()["voq_offset"].lower().split(" | ")
                [
                    tc_dict.setdefault(tc_id, {}).setdefault(
                        "voq_offset", int(voq_offset)
                    )
                    for tc_id, voq_offset in zip(tc_list, voq_offset_list)
                ]
                continue

            # Interface Scheduler Configuration
            m = p2_0.match(line)
            if m:
                scheduler_dict = int_dict.setdefault("interface_scheduler", {})
                continue

            # Credit        : 12000081000
            m = p2_1.match(line)
            if m:
                credit = int(m.groupdict()["credit"])
                continue

            # CIR [RR]  | Transmit      : 12000081000
            # PIR [WFQ] | Transmit      : 12000081000
            m = p2_2.match(line)
            if m:
                interface_scheduler = scheduler_dict.setdefault(
                    m.groupdict()["interface_scheduler"].lower(), {}
                )
                interface_scheduler["credit"] = credit
                interface_scheduler["transmit"] = int(m.groupdict()["transmit"])
                continue

            # Weight        : 1
            m = p2_3.match(line)
            if m:
                interface_scheduler["weight"] = int(m.groupdict()["weight"])
                continue

            # Interface Scheduler - OQPG  Configuration
            m = p3_0.match(line)
            if m:
                scheduler_oqpg_dict = int_dict.setdefault(
                    "interface_scheduler_oqpg", {}
                )
                continue

            # PG TYPE           || OQPG-0           | OQPG-1           | OQPG-2           | OQPG-3
            #            | OQPG-4           | OQPG-5           | OQPG-6           | OQPG-7
            m = p3_1.match(line)
            if m:
                oqpg_list = (
                    m.groupdict()["oqpg"]
                    .lower()
                    .replace("-", "_")
                    .replace(" ", "")
                    .split("|")
                )
                continue

            # Credit CIR    || 0                | 0                | 0                | 0
            # | 0                | 0                | 0                | SDK Default
            m = p3_2.match(line)
            if m:
                credit_cir_values = re.sub(
                    r"\s+", " ", m.groupdict()["credit_cir"]
                ).split(" | ")
                continue

            # RR |Credit Burst  || 0                | 0                | 0                | 0
            # | 0                | 0                | 0                | 30
            m = p3_3.match(line)
            if m:
                credit_burst_list = re.sub(
                    r"\s+", " ", m.groupdict()["credit_burst"]
                ).split(" | ")
                [
                    scheduler_oqpg_dict.setdefault(oqpg_id, {})
                    .setdefault("rr", {})
                    .update({"credit_cir": credit_cir, "credit_burst": credit_burst})
                    for oqpg_id, credit_cir, credit_burst in zip(
                        oqpg_list, credit_cir_values, credit_burst_list
                    )
                ]
                continue

            # Transmit CIR  || 0                | 0                | 0                | 0
            #                 | 0                | 0                | 0                | SDK Default
            m = p3_4.match(line)
            if m:
                transmit_type = (
                    m.groupdict()["transmit_type"].lower().strip().replace(" ", "_")
                )
                transmit_values_list = re.sub(
                    r"\s+", " ", m.groupdict()["transmit_values"]
                ).split(" | ")
                [
                    scheduler_oqpg_dict.setdefault(oqpg_id, {})
                    .setdefault("rr", {})
                    .setdefault(transmit_type, transmit_value)
                    for oqpg_id, transmit_value in zip(oqpg_list, transmit_values_list)
                ]
                continue

            # WFQ|Weights PIR  || 0                | 0                | 0                | 0
            # | 0                | 0                | 0                | 30
            m = p3_5.match(line)
            if m:
                weights_pir_list = re.sub(
                    r"\s+", " ", m.groupdict()["weights_pir"]
                ).split(" | ")
                [
                    scheduler_oqpg_dict.setdefault(oqpg_id, {})
                    .setdefault("wfq", {})
                    .setdefault("weights_pir", int(weights_pir))
                    for oqpg_id, weights_pir in zip(oqpg_list, weights_pir_list)
                ]
                continue

            # Weights Actual|| 63               | 63               | 63               | 63
            #                | 63               | 63               | 63               | 63
            m = p3_6.match(line)
            if m:
                weights_actual_list = re.sub(
                    r"\s+", " ", m.groupdict()["weights_actual"]
                ).split(" | ")
                [
                    scheduler_oqpg_dict.setdefault(oqpg_id, {})
                    .setdefault("wfq", {})
                    .setdefault("weights_actual", int(weights_actual))
                    for oqpg_id, weights_actual in zip(oqpg_list, weights_actual_list)
                ]
                continue

            # OQ List           || 0                |                  |                  |
            #                   |                  |                  |                  | 1 2 3 4 5 6 7
            m = p3_7.match(line)
            if m:
                oq_list = re.sub(r"\s{2}", "", m.groupdict()["oq_list"]).split("|")
                [
                    scheduler_oqpg_dict.setdefault(oqpg_id, {}).setdefault(
                        "oq_list", oq.split()
                    )
                    for oqpg_id, oq in zip(oqpg_list, oq_list)
                ]
                continue

            # LPSE/OQSE <->  OQPG  Configuration
            m = p4_0.match(line)
            if m:
                lpse_oqse_oqpg_dict = int_dict.setdefault("lpse_oqse_oqpg", {})
                continue

            # OQ Number         ||    LPSE-OQ-0     |    LPSE-OQ-1     | OQ-2             | OQ-3
            #              | OQ-4             | OQ-5             | OQ-6             | OQ-7
            m = p4_1.match(line)
            if m:
                oq_number_list = (
                    re.sub(r"\s+", " ", m.groupdict()["oq_number"])
                    .lower()
                    .replace("-", "_")
                    .split(" | ")
                )
                continue

            # OQPG Associated   || OQPG-0           | OQPG-1           | OQPG-7 [P]       | OQPG-7 [P]
            #        | OQPG-7 [P]       | OQPG-7 [P]       | OQPG-7 [P]       | OQPG-7 [P]
            m = p4_2.match(line)
            if m:
                oqpg_associated_list = re.sub(
                    r"\s+", " ", m.groupdict()["oqpg_associated"]
                ).split(" | ")
                [
                    lpse_oqse_oqpg_dict.setdefault(oq_number, {}).setdefault(
                        "oqpg_associated", oqpg_associated.strip()
                    )
                    for oq_number, oqpg_associated in zip(
                        oq_number_list, oqpg_associated_list
                    )
                ]
                continue

            # Credit PIR        || SDK Default      | 94921872         | 189843744        | 94921872
            #          | 94921872         | 147656256        | 94921872         | 189843744
            m = p4_3.match(line)
            if m:
                lpse_type = m.groupdict()["lpse_type"].lower().replace(" ", "_")
                lpse_list = re.sub(r"\s+", " ", m.groupdict()["lpse_values"]).split(
                    " | "
                )
                [
                    lpse_oqse_oqpg_dict.setdefault(oq_number, {}).setdefault(
                        lpse_type, lpse
                    )
                    for oq_number, lpse in zip(oq_number_list, lpse_list)
                ]
                continue

            # Weights : UC : MC ||      8 : 2       |      8 : 2       |      8 : 2       |      8 : 2
            #        |      8 : 2       |      8 : 2       |      8 : 2       |      8 : 2
            m = p4_4.match(line)
            if m:
                uc_mc_list = re.sub(r"\s+", " ", m.groupdict()["uc_mc"]).split(" | ")
                [
                    lpse_oqse_oqpg_dict.setdefault(oq_number, {})
                    .setdefault("weights", {})
                    .update(
                        {
                            "uc": int(weight.split(" : ")[0]),
                            "mc": int(weight.split(" : ")[1]),
                        }
                    )
                    for oq_number, weight in zip(oq_number_list, uc_mc_list)
                ]
                continue

            # OQSE OID          || LPSE OID : 1356 (0x54C  )           | 1350 (0x546  )   | 1351 (0x547  )
            #    | 1352 (0x548  )   | 1353 (0x549  )   | 1354 (0x54A  )   | 1355 (0x54B  )
            m = p4_5.match(line)
            if m:
                lpse_oid = int(m.groupdict()["lpse_oid"])
                lpse_id = m.groupdict()["lpse_id"]
                oqse_oid_list = [f"{lpse_oid}({lpse_id}", f"{lpse_oid}({lpse_id}"]
                oqse_oid_list.extend(
                    re.sub(r"\s+|\)", "", m.groupdict()["oqse_oid"]).split("|")
                )
                [
                    lpse_oqse_oqpg_dict.setdefault(oq_number, {})
                    .setdefault("oqse_oid", {})
                    .update(
                        {
                            "oid": int(oqse_oid.split("(")[0]),
                            "id": oqse_oid.split("(")[1],
                        }
                    )
                    for oq_number, oqse_oid in zip(oq_number_list, oqse_oid_list)
                ]
                continue

            # LPSE Configuration
            m = p5_0.match(line)
            if m:
                lpse_dict = int_dict.setdefault("lpse", {})
                continue

            # LPSE OID                  : 1356 (  0x54C)
            m = p5_1.match(line)
            if m:
                lpse_dict["oid"] = int(m.groupdict()["oid"])
                lpse_dict["id"] = m.groupdict()["id"]
                continue

            # LPSE CIR Weight           :   1 :   1 :   1 :   1 :   1 :   1 :   1 :   1
            m = p5_2.match(line)
            if m:
                lpse_dict["cir_weight"] = (
                    m.groupdict()["cir_weight"].replace(" ", "").split(":")
                )
                continue

            # LPSE EIR Weight           :   1 :   1 :   1 :   1 :   1 :   1 :   1 :   1
            m = p5_3.match(line)
            if m:
                lpse_dict["eir_weight"] = (
                    m.groupdict()["eir_weight"].replace(" ", "").split(":")
                )
                continue

            # LPSE Main Interface OQSE  : 1348 (0x544  )   | 1349 (0x545  )
            m = p5_4.match(line)
            if m:
                lpse_dict["main_interface_oqse"] = re.sub(
                    r"\s+", " ", m.groupdict()["main_interface_oqse"]
                ).split(" | ")
                continue

            # LPSE OQSE Credit CIR      : SDK Default      | 94921872
            m = p5_5.match(line)
            if m:
                lpse_dict["oqse_credit_cir"] = re.sub(
                    r"\s+", " ", m.groupdict()["oqse_credit_cir"]
                ).split(" | ")
                continue

            # LPSE OQSE Credit CIR Burst: 0                | 30
            m = p5_6.match(line)
            if m:
                lpse_dict["oqse_credit_cir_burst"] = re.sub(
                    r"\s+", " ", m.groupdict()["oqse_credit_cir_burst"]
                ).split(" | ")
                continue

            # LPSE OQSE Credit PIR      : SDK Default      | 94921872
            m = p5_7.match(line)
            if m:
                lpse_dict["oqse_credit_pir"] = re.sub(
                    r"\s+", " ", m.groupdict()["oqse_credit_pir"]
                ).split(" | ")
                continue

            # LPSE OQSE Credit PIR Burst: 30               | 0
            m = p5_8.match(line)
            if m:
                lpse_dict["oqse_credit_pir_burst"] = re.sub(
                    r"\s+", " ", m.groupdict()["oqse_credit_pir_burst"]
                ).split(" | ")
                continue

            # LPSE Total Attached OQSEs : 2
            m = p5_9.match(line)
            if m:
                lpse_dict["total_attached_oqse"] = int(
                    m.groupdict()["total_attached_oqse"]
                )
                continue

            # LPSE CIR (Priority Queue) Rate      : SDK Default
            m = p5_10.match(line)
            if m:
                lpse_dict["lpse_cir_priority_queue_rate"] = re.sub(
                    r"\s+", " ", m.groupdict()["lpse_cir_priority_queue_rate"]
                ).split(" | ")
                continue

            # LPSE CIR (Priority Queue) Burst     : 30
            m = p5_11.match(line)
            if m:
                lpse_dict["lpse_cir_priority_queue_burst"] = re.sub(
                    r"\s+", " ", m.groupdict()["lpse_cir_priority_queue_burst"]
                ).split(" | ")
                continue

            # LPSE PIR (Sub-Interface Port) Rate  : SDK Default
            m = p5_12.match(line)
            if m:
                lpse_dict["lpse_pir_sub_interface_port_rate"] = re.sub(
                    r"\s+", " ", m.groupdict()["lpse_pir_sub_interface_port_rate"]
                ).split(" | ")
                continue

            # LPSE PIR (Sub-Interface Port) Burst : 30
            m = p5_13.match(line)
            if m:
                lpse_dict["lpse_pir_sub_interface_port_burst"] = re.sub(
                    r"\s+", " ", m.groupdict()["lpse_pir_sub_interface_port_burst"]
                ).split(" | ")
                continue

            # OQSE <-> VOQ-VSC Configuration
            m = p6_0.match(line)
            if m:
                oqse_voq_vsc_dict = int_dict.setdefault("oqse_voq_vsc", {})
                continue

            # OQSE OID              : 1348 (  0x544)
            # OQSE OID              : 749  (  0x2ED)
            m = p6_1.match(line)
            if m:
                oqse_oid = int(m.groupdict()["oqse_oid"])
                oqse_id = m.groupdict()["oqse_id"]
                continue

            # OQ    ID              : 0
            m = p6_2.match(line)
            if m:
                oq_id_dict = oqse_voq_vsc_dict.setdefault("oq_id", {}).setdefault(
                    m.groupdict()["oq_id"], {}
                )
                oq_id_dict["oqse_oid"] = oqse_oid
                oq_id_dict["oqse_id"] = oqse_id
                continue

            # Scheduling Mode       : Logical Port SP SP
            m = p6_3.match(line)
            if m:
                oq_id_dict["scheduling_mode"] = m.groupdict()["scheduling_mode"]
                continue

            # Credit CIR            : SDK Default
            # Credit PIR            : 189843744
            # Transmit PIR          : 232031248
            m = p6_4.match(line)
            if m:
                cir_pir = m.groupdict()["cir_pir"].lower().replace(" ", "_")
                oq_id_dict[cir_pir] = m.groupdict()["credit"]
                continue

            # Credit CIR Burst      : 0
            # Credit PIR Burst      : 30
            # Transmit PIR Burst    : 30
            m = p6_5.match(line)
            if m:
                cir_pir = m.groupdict()["cir_pir"].lower().replace(" ", "_")
                oq_id_dict[cir_pir] = m.groupdict()["credit_burst"]
                continue

            # RR Weights            :   1 :   1 :   1 :   1 : N/A : N/A : N/A : N/A
            m = p6_6.match(line)
            if m:
                oq_id_dict["rr_weights"] = re.sub(
                    r"\s+", " ", m.groupdict()["rr_weights"]
                ).split(" : ")
                continue

            # RR Weights Actual     : 255 : 255 : 255 : 255 : N/A : N/A : N/A : N/A
            m = p6_7.match(line)
            if m:
                oq_id_dict["rr_weights_actual"] = re.sub(
                    r"\s+", " ", m.groupdict()["rr_weights_actual"]
                ).split(" : ")
                continue

            # RR3      || In Device |                    0 |                    0 |                    0 |
            #                     0 |                    0 |                    0
            m = p6_8.match(line)
            if m:
                rr_dict = oq_id_dict.setdefault("rr", {}).setdefault(
                    m.groupdict()["rr"].lower(), {}
                )
                in_device_list = re.sub(r"\s+", " ", m.groupdict()["in_device"]).split(
                    " | "
                )
                continue

            # In Slice  |                    0 |                    1 |                   2 |
            #                     3 |                    4 |                    5
            m = p6_9.match(line)
            if m:
                in_slice_list = re.sub(r"\s+", " ", m.groupdict()["in_slice"]).split(
                    " | "
                )
                [
                    rr_dict.setdefault("in_slice", {})
                    .setdefault(in_slice, {})
                    .setdefault("in_device", int(in_device))
                    for in_slice, in_device in zip(in_slice_list, in_device_list)
                ]
                continue

            # VSC ID    |                  352 |                  416 |                  480 |
            #                   544 |                  608 |                  672
            m = p6_10.match(line)
            if m:
                vsc_id_list = re.sub(r"\s+", " ", m.groupdict()["vsc_id"]).split(" | ")
                [
                    rr_dict.setdefault("in_slice", {})
                    .setdefault(in_slice, {})
                    .setdefault("vsc_id", int(vsc_id))
                    for in_slice, vsc_id in zip(in_slice_list, vsc_id_list)
                ]
                continue

            # VOQ ID    |                52576 |                52576 |                52576 |
            #                 52576 |                52576 |                52576
            m = p6_11.match(line)
            if m:
                voq_id_list = re.sub(r"\s+", " ", m.groupdict()["voq_id"]).split(" | ")
                [
                    rr_dict.setdefault("in_slice", {})
                    .setdefault(in_slice, {})
                    .setdefault("voq_id", int(voq_id))
                    for in_slice, voq_id in zip(in_slice_list, voq_id_list)
                ]
                continue

            # VSC PIR   |        2678399959040 |        2678399959040 |        2678399959040 |
            #         2678399959040 |        2678399959040 |        2678399959040
            m = p6_12.match(line)
            if m:
                vsc_pir_list = re.sub(r"\s+", " ", m.groupdict()["vsc_pir"]).split(" | ")
                [
                    rr_dict.setdefault("in_slice", {})
                    .setdefault(in_slice, {})
                    .setdefault("vsc_pir", int(vsc_pir))
                    for in_slice, vsc_pir in zip(in_slice_list, vsc_pir_list)
                ]
                continue

            # VSC Burst |                  511 |                  511 |                  511 |
            #                   511 |                  511 |                  511
            m = p6_13.match(line)
            if m:
                vsc_burst_list = re.sub(r"\s+", " ", m.groupdict()["vsc_burst"]).split(
                    " | "
                )
                [
                    rr_dict.setdefault("in_slice", {})
                    .setdefault(in_slice, {})
                    .setdefault("vsc_burst", int(vsc_burst))
                    for in_slice, vsc_burst in zip(in_slice_list, vsc_burst_list)
                ]
                continue

        return ret_dict


class ShowPlatformHardwareFedQosQueueStatsOqMulticastSchema(MetaParser):
    """
    Schema for
        * 'show platform hardware fed {switch} {mode} qos queue stats oq multicast interface {interface} oq_id {oq_id}'
    """

    schema = {
        "interface": {
            Any(): {
                "oq_id": {
                    Any(): {
                        "packets": {"enqueued": int, "dropped": int},
                        "bytes": {"enqueued": int, "dropped": int},
                    }
                }
            }
        }
    }


class ShowPlatformHardwareFedQosQueueStatsOqMulticast(
    ShowPlatformHardwareFedQosQueueStatsOqMulticastSchema
):
    """
    Parser for
        * 'show platform hardware fed {switch} {mode} qos queue stats oq multicast interface {interface} oq_id {oq_id}'
    """

    cli_command = [
        "show platform hardware fed {mode} qos queue stats oq multicast interface {interface} oq_id {oq_id}",
        "show platform hardware fed {switch} {mode} qos queue stats oq multicast interface {interface} oq_id {oq_id}",
    ]

    def cli(self, mode, interface, oq_id, switch=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[1].format(
                    switch=switch, mode=mode, interface=interface, oq_id=oq_id
                )
            else:
                cmd = self.cli_command[0].format(
                    mode=mode, interface=interface, oq_id=oq_id
                )

            output = self.device.execute(cmd)

        # Multicast OQ stats for : HundredGigE1/0/5, oq_id:7
        p1 = re.compile(
            r"^Multicast OQ stats for : (?P<interface>\S+), oq_id:(?P<oq_id>\d+)$"
        )

        # |          |              Packets              |               Bytes               |
        p2 = re.compile(r"^\|\s+\|\s+Packets\s+\|\s+Bytes\s+\|$")

        # | Enqueued |                         452993529 |                      469432571476 |
        p3 = re.compile(
            r"^\|\s+Enqueued\s+\|\s+(?P<packets>\d+)\s+\|\s+(?P<bytes>\d+)\s+\|$"
        )

        # | Dropped  |                           1457949 |                       44346943560 |
        p4 = re.compile(
            r"^\|\s+Dropped\s+\|\s+(?P<packets>\d+)\s+\|\s+(?P<bytes>\d+)\s+\|$"
        )

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Multicast OQ stats for : HundredGigE1/0/5, oq_id:7
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group["interface"])
                oq_dict = (
                    ret_dict.setdefault("interface", {})
                    .setdefault(interface, {})
                    .setdefault("oq_id", {})
                    .setdefault(group["oq_id"], {})
                )
                continue

            # |          |              Packets              |               Bytes               |
            m = p2.match(line)
            if m:
                packets_dict = oq_dict.setdefault("packets", {})
                bytes_dict = oq_dict.setdefault("bytes", {})
                continue

            # | Enqueued |                         452993529 |                      469432571476 |
            m = p3.match(line)
            if m:
                group = m.groupdict()
                packets_dict["enqueued"] = int(group["packets"])
                bytes_dict["enqueued"] = int(group["bytes"])
                continue

            # | Dropped  |                           1457949 |                       44346943560 |
            m = p4.match(line)
            if m:
                group = m.groupdict()
                packets_dict["dropped"] = int(group["packets"])
                bytes_dict["dropped"] = int(group["bytes"])
                continue

        return ret_dict


class ShowPlatformHardwareFedQosQueueStatsOqMulticastOqId(
    ShowPlatformHardwareFedQosQueueStatsOqMulticast
):
    """
    Parser for
        * 'show platform hardware fed {switch} {mode} qos queue stats oq multicast interface {interface} oq_id {oq_id} clear-on-read'
    """

    cli_command = [
        "show platform hardware fed {mode} qos queue stats oq multicast interface {interface} oq_id {oq_id} clear-on-read",
        "show platform hardware fed {switch} {mode} qos queue stats oq multicast interface {interface} oq_id {oq_id} clear-on-read",
    ]

    def cli(self, mode, interface, oq_id, switch=None, output=None):
        return super().cli(
            mode=mode, interface=interface, oq_id=oq_id, switch=switch, output=output
        )


class ShowPlatformHardwareFedSwitchQosQueueConfigSchema(MetaParser):
    """
    Schema for
        * 'show platform hardware fed switch {switch_var} qos queue config interface {interface}'
    """

    schema = {
        "interface": {
            Any(): {
                "interface_id": str,
                "voq_id": str,
                "voq_oid": str,
                "voq_set_size": str,
                "base_voq_id": str,
                "base_vsc_ids": list,
                "voq_state": str,
                "voq_flush": str,
                "is_empty": str,
                "profile_oid": {
                    Any(): {
                        "profile_id": str,
                        "device_id": str,
                        "cgm_type": str,
                        "profile_reference_count": str,
                        "is_reserved": str,
                        "for_speeds": str,
                        "associated_voq_offsets": Or(str, list),
                        "hbm_enabled": str,
                        Optional("hgm_block_size"): str,
                        Optional("red_enabled"): str,
                        Optional("fcn_enabled"): str,
                        Optional("queue_user_config"): {
                            "q_limit_hbm_blocks": str,
                            "red_ema_coefficient": str,
                            Optional("red_flag"): {
                                Any(): {
                                    Optional("minimun_hbm_blocks"): str,
                                    Optional("maximum_hbm_blocks"): str,
                                    Optional("maximum_probability"): str,
                                },
                            },
                        },
                        Optional("queue_hw_values"): {
                            "red_action": str,
                            "red_drop_thresholds": list,
                            "hbm_free_thresholds": list,
                            "hbm_voq_age_thresholds": list,
                            "hbm_voq_thresholds": list,
                            Optional("red_flag"): {
                                Any(): {
                                    "red_drop_probabilities": list,
                                }
                            },
                        },
                    }
                },
            }
        }
    }


class ShowPlatformHardwareFedSwitchQosQueueConfig(
    ShowPlatformHardwareFedSwitchQosQueueConfigSchema
):
    """
    Parser for
        * 'show platform hardware fed switch {switch_var} qos queue config interface {interface}'
    """

    cli_command = [
        "show platform hardware fed {switch_var} qos queue config interface {interface}",
        "show platform hardware fed {switch} {switch_var} qos queue config interface {interface}",
    ]

    def cli(self, interface, switch=None, switch_var=None, output=None):
        if output is None:
            if switch and switch_var:
                cmd = self.cli_command[1].format(
                    switch=switch, switch_var=switch_var, interface=interface
                )
            else:
                cmd = self.cli_command[0].format(
                    switch_var=switch_var, interface=interface
                )

            output = self.device.execute(cmd)

            # Interface : HundredGigE2/0/34.100 (0x54C)
            p0 = re.compile(
                r"^Interface\s+: (?P<interface>\S+) \((?P<interface_id>\S+)\)$"
            )

            # VOQ OID        : 2114(0x842)
            p1 = re.compile(r"^VOQ OID\s+: (?P<voq_oid>\S+)\((?P<voq_id>\S+)\)$")

            # VOQ Set Size   : 3
            p2 = re.compile(r"^VOQ Set Size\s+: (?P<voq_set_size>\S+)$")

            # Base VOQ ID    : 28952
            p3 = re.compile(r"^Base VOQ ID\s+: (?P<base_voq_id>\S+)$")

            # Base VSC IDs   : 728, 792, 856, 920, 984, 1048
            p4 = re.compile(r"^Base VSC IDs\s+: (?P<base_vsc_ids>[\w\s\,]+)$")

            # VOQ State      : Active
            p5 = re.compile(r"^VOQ State\s+: (?P<voq_state>\S+)$")

            # VOQ Flush      : Flush not active
            p6 = re.compile(r"^VOQ Flush\s+: (?P<voq_flush>.+)$")

            # Is Empty       : Yes
            p7 = re.compile(r"^Is Empty\s+: (?P<is_empty>.+)$")

            # Profile OID            : 433(0x1B1)
            p8_1 = re.compile(
                r"^Profile OID\s+: (?P<profile_oid>\d+)\((?P<profile_id>\w+)\)$"
            )

            # Device ID              : 0
            p9 = re.compile(r"^Device ID\s+: (?P<device_id>\d+)$")

            # CGM Type               : Unicast
            p10 = re.compile(r"^CGM Type\s+: (?P<cgm_type>\w+)$")

            # Profile reference count: 73
            p11 = re.compile(
                r"^Profile reference count\s*: (?P<profile_reference_count>\d+)$"
            )

            # Is Reserved            : Yes
            p12 = re.compile(r"^Is Reserved\s+: (?P<is_reserved>[\w\s]+)$")

            # For speeds             : 10000000000
            p13 = re.compile(r"^For speeds\s+: (?P<for_speeds>\d+)$")

            # Associated VOQ Offsets : 0
            p14 = re.compile(
                r"^Associated VOQ Offsets\s+: (?P<associated_voq_offsets>[\d, ]+)$"
            )

            # HBM Enabled            : Enabled
            p15 = re.compile(r"^HBM Enabled\s+: (?P<hbm_enabled>\w+)$")

            # HBM Block Size         : 6144
            p16 = re.compile(r"^HBM Block Size\s+: (?P<hgm_block_size>\w+)$")

            # RED Enabled            : Enabled
            p17 = re.compile(r"^RED Enabled\s+: (?P<red_enabled>\w+)$")

            # FCN Enabled            : Disabled
            p18 = re.compile(r"^FCN Enabled\s+: (?P<fcn_enabled>\w+)$")

            # Queue User Config      :
            p19 = re.compile(r"^Queue User Config\s+:$")

            # Q-Limit(HBM Blocks)    : 4882
            p19_1 = re.compile(
                r"^Q-Limit\(HBM Blocks\)\s+: (?P<q_limit_hbm_blocks>\d+)$"
            )

            # RED EMA Coefficient    : 1.000000
            p19_2 = re.compile(
                r"^RED EMA Coefficient\s+: (?P<red_ema_coefficient>[\w\.]+)$"
            )

            # RED Green :
            p19_3 = re.compile(r"^RED\s+(?P<red_flag>[\w\s]+)\s+:$")

            # Minium(HBM BLOCKS)   : 0
            p19_4 = re.compile(
                r"^Minium\(HBM BLOCKS\)\s*: (?P<minimun_hbm_blocks>\d+)$"
            )

            # Maximum(HBM BLOCKS)  : 1220
            p19_5 = re.compile(
                r"^Maximum\(HBM BLOCKS\)\s*: (?P<maximum_hbm_blocks>\d+)$"
            )

            # Maximum Probability  : 0
            p19_6 = re.compile(
                r"^Maximum Probability\s*: (?P<maximum_probability>\d+)$"
            )

            # Queue H/W Values       :
            p20 = re.compile(r"^Queue H/W Values\s+:$")

            # RED Action                     : Drop
            p20_1 = re.compile(r"^RED Action\s+: (?P<red_action>\w+)$")

            # RED Drop thresholds            : 0, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220
            p20_2 = re.compile(
                r"^RED Drop thresholds\s+: (?P<red_drop_thresholds>[\w\s\,]+)$"
            )

            # RED Drop Probabilities[Green]  : 0.000000, 0.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000
            p20_3 = re.compile(
                r"^RED Drop Probabilities\[(?P<red_flag>[\w]+)\]\s+: (?P<red_drop_probabilities>[\w\s\,\.]+)$"
            )

            # HBM Free Thresholds            : 10000, 20000, 40000, 60000, 124992, 250000, 500000, 1000000
            p20_4 = re.compile(
                r"^HBM Free Thresholds\s+: (?P<hbm_free_thresholds>[\w\s\,\.]+)$"
            )

            # HBM VOQ Age Thresholds         : 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 16, 24, 32, 64, 128
            p20_5 = re.compile(
                r"^HBM VOQ Age Thresholds\s+: (?P<hbm_voq_age_thresholds>[\w\s\,\.]+)$"
            )

            # HBM VOQ Thresholds             : 96, 992, 2000, 4000, 6000, 8000, 12000, 16000, 24000, 32000, 40000, 48000, 56000, 64000, 64512, 65536,
            p20_6 = re.compile(
                r"^HBM VOQ Thresholds\s+: (?P<hbm_voq_thresholds>[\w\s\,\.]+)$"
            )

            ret_dict = {}

            for line in output.splitlines():
                line = line.strip()

                # Interface              : HundredGigE1/0/5 (0x54A)
                m = p0.match(line)
                log.info("i am in p0")
                if m:
                    int_dict = ret_dict.setdefault("interface", {}).setdefault(
                        Common.convert_intf_name(m.groupdict()["interface"]), {}
                    )
                    int_dict["interface_id"] = m.groupdict()["interface_id"]
                    continue

                # VOQ OID        : 2114(0x842)
                m = p1.match(line)
                if m:
                    int_dict["voq_id"] = m.groupdict()["voq_id"]
                    int_dict["voq_oid"] = m.groupdict()["voq_oid"]
                    continue

                # VOQ Set Size   : 3
                m = p2.match(line)
                if m:
                    int_dict["voq_set_size"] = m.groupdict()["voq_set_size"]
                    continue

                # Base VOQ ID    : 28952
                m = p3.match(line)
                if m:
                    int_dict["base_voq_id"] = m.groupdict()["base_voq_id"]
                    continue

                # Base VSC IDs   : 728, 792, 856, 920, 984, 1048
                m = p4.match(line)
                if m:
                    int_dict["base_vsc_ids"] = (
                        m.groupdict()["base_vsc_ids"].replace(" ", "").split(",")
                    )
                    continue

                # VOQ State      : Active
                m = p5.match(line)
                if m:
                    int_dict["voq_state"] = m.groupdict()["voq_state"]
                    continue

                # VOQ Flush      : Flush not active
                m = p6.match(line)
                if m:
                    int_dict["voq_flush"] = m.groupdict()["voq_flush"]
                    continue

                # Is Empty       : Yes
                m = p7.match(line)
                if m:
                    int_dict["is_empty"] = m.groupdict()["is_empty"]
                    continue

                # Profile OID            : 433(0x1B1)
                m = p8_1.match(line)
                if m:
                    profile_dict = int_dict.setdefault("profile_oid", {}).setdefault(
                        m.groupdict()["profile_oid"], {}
                    )
                    profile_dict["profile_id"] = m.groupdict()["profile_id"]
                    continue

                # Device ID              : 0
                m = p9.match(line)
                if m:
                    profile_dict["device_id"] = m.groupdict()["device_id"]
                    continue

                # CGM Type               : Unicast
                m = p10.match(line)
                if m:
                    profile_dict["cgm_type"] = m.groupdict()["cgm_type"]
                    continue

                # Profile reference count: 73
                m = p11.match(line)
                if m:
                    profile_dict["profile_reference_count"] = m.groupdict()[
                        "profile_reference_count"
                    ]
                    continue

                # Is Reserved            : Yes
                m = p12.match(line)
                if m:
                    profile_dict["is_reserved"] = m.groupdict()["is_reserved"]
                    continue

                # For speeds             : 10000000000
                m = p13.match(line)
                if m:
                    profile_dict["for_speeds"] = m.groupdict()["for_speeds"]
                    continue

                # Associated VOQ Offsets : 0
                m = p14.match(line)
                if m:
                    profile_dict["associated_voq_offsets"] = (
                        m.groupdict()["associated_voq_offsets"]
                        .replace(" ", "")
                        .split(",")
                    )
                    continue

                # HBM Enabled            : Enabled
                m = p15.match(line)
                if m:
                    profile_dict["hbm_enabled"] = m.groupdict()["hbm_enabled"]
                    continue

                # HBM Block Size         : 6144
                m = p16.match(line)
                if m:
                    profile_dict["hgm_block_size"] = m.groupdict()["hgm_block_size"]
                    continue

                # RED Enabled            : Enabled
                m = p17.match(line)
                if m:
                    profile_dict["red_enabled"] = m.groupdict()["red_enabled"]
                    continue

                # FCN Enabled            : Disabled
                m = p18.match(line)
                if m:
                    profile_dict["fcn_enabled"] = m.groupdict()["fcn_enabled"]
                    continue

                # Queue User Config      :
                m = p18.match(line)
                if m:
                    profile_dict["fcn_enabled"] = m.groupdict()["fcn_enabled"]
                    continue

                # Queue User Config      :
                m = p19.match(line)
                if m:
                    queue_config_dict = profile_dict.setdefault("queue_user_config", {})
                    continue

                # Q-Limit(HBM Blocks)    : 1220
                m = p19_1.match(line)
                if m:
                    queue_config_dict["q_limit_hbm_blocks"] = m.groupdict()[
                        "q_limit_hbm_blocks"
                    ]
                    continue

                # RED EMA Coefficient    : 1.000000
                m = p19_2.match(line)
                if m:
                    queue_config_dict["red_ema_coefficient"] = m.groupdict()[
                        "red_ema_coefficient"
                    ]
                    continue

                # RED Green :
                m = p19_3.match(line)
                if m:
                    red_dict = queue_config_dict.setdefault("red_flag", {}).setdefault(
                        m.groupdict()["red_flag"], {}
                    )
                    continue

                # Minium(HBM BLOCKS)   : 0
                m = p19_4.match(line)
                if m:
                    red_dict["minimun_hbm_blocks"] = m.groupdict()["minimun_hbm_blocks"]
                    continue

                # Maximum(HBM BLOCKS)  : 1220
                m = p19_5.match(line)
                if m:
                    red_dict["maximum_hbm_blocks"] = m.groupdict()["maximum_hbm_blocks"]
                    continue

                # Maximum Probability  : 0
                m = p19_6.match(line)
                if m:
                    red_dict["maximum_probability"] = m.groupdict()[
                        "maximum_probability"
                    ]
                    continue

                # Queue H/W Values       :
                m = p20.match(line)
                if m:
                    queue_hw_dict = profile_dict.setdefault("queue_hw_values", {})
                    continue

                # RED Action                     : Drop
                m = p20_1.match(line)
                if m:
                    queue_hw_dict["red_action"] = m.groupdict()["red_action"]
                    continue

                # RED Drop thresholds            : 0, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220
                m = p20_2.match(line)
                if m:
                    queue_hw_dict["red_drop_thresholds"] = (
                        m.groupdict()["red_drop_thresholds"].replace(" ", "").split(",")
                    )
                    continue

                # RED Drop Probabilities[Green]  : 0.000000, 0.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000
                m = p20_3.match(line)
                if m:
                    red_hw_dict = queue_hw_dict.setdefault("red_flag", {}).setdefault(
                        m.groupdict()["red_flag"], {}
                    )
                    red_hw_dict["red_drop_probabilities"] = (
                        m.groupdict()["red_drop_probabilities"]
                        .replace(" ", "")
                        .split(",")
                    )
                    continue

                # HBM Free Thresholds            : 10000, 20000, 40000, 60000, 124992, 250000, 500000, 1000000
                m = p20_4.match(line)
                if m:
                    queue_hw_dict["hbm_free_thresholds"] = (
                        m.groupdict()["hbm_free_thresholds"].replace(" ", "").split(",")
                    )
                    continue

                # HBM VOQ Age Thresholds         : 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 16, 24, 32, 64, 128
                m = p20_5.match(line)
                if m:
                    queue_hw_dict["hbm_voq_age_thresholds"] = (
                        m.groupdict()["hbm_voq_age_thresholds"]
                        .replace(" ", "")
                        .split(",")
                    )
                    continue

                # HBM VOQ Thresholds             : 96, 992, 2000, 4000, 6000, 8000, 12000, 16000, 24000, 32000, 40000, 48000, 56000, 64000, 64512, 65536,
                m = p20_6.match(line)
                if m:
                    queue_hw_dict["hbm_voq_thresholds"] = (
                        m.groupdict()["hbm_voq_thresholds"].replace(" ", "").split(",")
                    )
                    continue

            return ret_dict


# ======================================================================
# Parser for 'show platform hardware fed active fwd-asic traps npu-traps asic 0'
# ======================================================================
class ShowPlatformHardwareFedActiveFwdAsicTrapsNputrapsSchema(MetaParser):
    """Schema for show platform hardware fed active fwd-asic traps npu-traps asic 0"""

    schema = {
        "trap_id": {
            Any(): {
                "npu_trap_name": str,
                "asic": int,
                "prev": int,
                "current": int,
                "delta": int,
            },
        },
    }


class ShowPlatformHardwareFedActiveFwdAsicTrapsNputraps(
    ShowPlatformHardwareFedActiveFwdAsicTrapsNputrapsSchema
):
    """Parser for show platform hardware fed active fwd-asic traps npu-traps asic 0"""

    cli_command = [
        "show platform hardware fed {switch} {switch_var} fwd-asic traps npu-traps asic {asic_id}",
        "show platform hardware fed {switch_var} fwd-asic traps npu-traps asic {asic_id}",
    ]

    def cli(self, switch_var, asic_id, switch="", output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(
                    switch=switch, switch_var=switch_var, asic_id=asic_id
                )
            else:
                cmd = self.cli_command[1].format(switch_var=switch_var, asic_id=asic_id)

            output = self.device.execute(cmd)

        # ------------------------------------------------------------------------------------------------------------------------
        # Trap ID |     Asic     |                   NPU Trap Name                    |     Prev     |   Current    |    Delta
        # ------------------------------------------------------------------------------------------------------------------------
        #     1 |            0 |                       la_event_e_ETHERNET_ACL_DROP |            0 |            0 |            0
        #     2 |            0 |                 la_event_e_ETHERNET_ACL_FORCE_PUNT |            0 |            0 |            0
        #     4 |            0 |      la_event_e_ETHERNET_NO_TERMINATION_ON_L3_PORT |      8276565 |      8276565 |            0
        p1 = re.compile(
            r"^(?P<trap_id>[\d]+)+\s+\|+\s+(?P<asic>[\d]+)+\s+\|+\s+(?P<npu_trap_name>[\w\_]+)+\s+\|+\s+(?P<prev>[\d]+)+\s+\|+\s+(?P<current>[\d]+)+\s+\|+\s+(?P<delta>[\d]+)$"
        )

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            #     1 |            0 |                       la_event_e_ETHERNET_ACL_DROP |            0 |            0 |            0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                id_dict = ret_dict.setdefault("trap_id", {}).setdefault(
                    m.groupdict()["trap_id"], {}
                )
                id_dict["npu_trap_name"] = group["npu_trap_name"]
                id_dict["asic"] = int(group["asic"])
                id_dict["prev"] = int(group["prev"])
                id_dict["current"] = int(group["current"])
                id_dict["delta"] = int(group["delta"])

        return ret_dict


# ======================================================================
# Parser for 'show platform hardware fed active fwd-asic traps tm-traps asic 0'
# ======================================================================
class ShowPlatformHardwareFedActiveFwdAsicTrapsTMtrapsSchema(MetaParser):
    """Schema for show platform hardware fed active fwd-asic traps tm-traps asic 0"""

    schema = {
        "trap_id": {
            Any(): {
                "tm_trap_name": str,
                "asic": int,
                "prev": int,
                "current": int,
                "delta": int,
            },
        },
    }


class ShowPlatformHardwareFedActiveFwdAsicTrapsTMtraps(
    ShowPlatformHardwareFedActiveFwdAsicTrapsTMtrapsSchema
):
    """Parser for show platform hardware fed active fwd-asic traps tm-traps asic 0"""

    cli_command = [
        "show platform hardware fed {switch} {switch_var} fwd-asic traps tm-traps asic {asic_id}",
        "show platform hardware fed {switch_var} fwd-asic traps tm-traps asic {asic_id}",
    ]

    def cli(self, switch_var, asic_id, switch="", output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(
                    switch=switch, switch_var=switch_var, asic_id=asic_id
                )
            else:
                cmd = self.cli_command[1].format(switch_var=switch_var, asic_id=asic_id)

            output = self.device.execute(cmd)

        # ------------------------------------------------------------------------------------------------------------------------
        # Trap ID |     Asic     |                   TM Trap                     |     Prev     |   Current    |    Delta
        # ------------------------------------------------------------------------------------------------------------------------
        # 1 |  0 |                la_tm_traps_e_EXACT_METER_PACKET_GOT_DROPPED_DUE_TO_EXACT_METER |            0 |            0 |            0
        # 2 |  0 |    la_tm_traps_e_STATISTICAL_METER_PACKET_GOT_DROPPED_DUE_TO_STATISTICAL_METER |            0 |            0 |            0
        # 3 |  0 |                               la_tm_traps_e_ETHERNET_METERS_PACKET_OUT_OF_RATE |            0 |            0 |            0

        p1 = re.compile(
            r"^(?P<trap_id>[\d]+)+\s+\|+\s+(?P<asic>[\d]+)+\s+\|+\s+(?P<tm_trap_name>[\w\_]+)+\s+\|+\s+(?P<prev>[\d]+)+\s+\|+\s+(?P<current>[\d]+)+\s+\|+\s+(?P<delta>[\d]+)$"
        )

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            #     1 |            0 |                       la_tm_traps_e_ETHERNET_METERS_PACKET_OUT_OF_RATE |            0 |            0 |            0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                id_dict = ret_dict.setdefault("trap_id", {}).setdefault(
                    m.groupdict()["trap_id"], {}
                )
                id_dict["tm_trap_name"] = group["tm_trap_name"]
                id_dict["asic"] = int(group["asic"])
                id_dict["prev"] = int(group["prev"])
                id_dict["current"] = int(group["current"])
                id_dict["delta"] = int(group["delta"])

        return ret_dict


# ======================================================================
# Parser for 'show platform hardware fed active fwd-asic drops asic 0 slice 0 '
# ======================================================================


class ShowPlatformHardwareFedActiveFwdasicdropsSchema(MetaParser):
    """Schema for
    * show platform hardware fed active fwd-asic drops asic {asic} slice {slice}
    * show platform hardware fed switch active fwd-asic drops asic {asic} slice {slice}
    """

    schema = {
        "counter_index": {
            int: {
                "id": int,
                "counter_name": str,
                "slice_number": int,
                "ifg_number": int,
                "field_value": int,
            }
        }
    }


class ShowPlatformHardwareFedActiveFwdasicdrops(
    ShowPlatformHardwareFedActiveFwdasicdropsSchema
):
    """Parser for
    * show platform hardware fed active fwd-asic drops asic {asic} slice {slice}
    * show platform hardware fed switch active fwd-asic drops asic {asic} slice {slice}
    """

    cli_command = [
        "show platform hardware fed {switch} {switch_var} fwd-asic drops asic {asic_id} slice {slice_id}",
        "show platform hardware fed {switch_var} fwd-asic drops asic {asic_id} slice {slice_id}",
    ]

    def cli(self, switch_var, asic_id, slice_id, switch="", output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(
                    switch=switch,
                    switch_var=switch_var,
                    asic_id=asic_id,
                    slice_id=slice_id,
                )
            else:
                cmd = self.cli_command[1].format(
                    switch_var=switch_var, asic_id=asic_id, slice_id=slice_id
                )

            output = self.device.execute(cmd)

        # Note: Slice and IFG showing -1 are global counters
        # ==================================================================================================================
        # |  #   |                      Counters Name                        |slice_number|   ifg_number  |  field_value   |
        # ==================================================================================================================
        # |  1    |RX IFGB0 Port0 drop_counter TC0                             |0|0|               0|
        # |  81   |RX IFGB0 Port0 partial_drop_counter TC0                     |0|0|               0|
        # ===================================================================================================================

        p1 = re.compile(
            r"^\|+\s+(?P<id>\d+)+\s+\|+(?P<counter_name>[\w\s\_\-\=\(\)\']+)\s+\|+\s*(?P<slice_number>\d+)+\s*\|+\s*(?P<ifg_number>[\d\-]+)+\s*\|+\s+(?P<field_value>\d+)+\|$"
        )

        ret_dict = {}
        counter_index = 1

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                id_dict = ret_dict.setdefault("counter_index", {}).setdefault(
                    counter_index, {}
                )
                id_dict["id"] = int(group["id"].strip())
                id_dict["counter_name"] = group["counter_name"].strip()
                id_dict["slice_number"] = int(group["slice_number"])
                id_dict["ifg_number"] = int(group["ifg_number"])
                id_dict["field_value"] = int(group["field_value"])
                counter_index += 1

        return ret_dict


class ShowPlatformHardwareFedSwitchActiveNpuSlotPortInfoSchema(MetaParser):
    """Schema for show platform hardware fed switch active npu slot 1 port 23 port-info"""

    schema = {
        "sw_port_debug_states": {
            Any(): Or(int, str),
        },
        "led_port_debug_states": {
            Any(): Or(int, str),
        },
        "lc_present": int,
        "outstanding_ports_to_be_deleted": int,
        "total_failed_deleted_ports": int,
    }


class ShowPlatformHardwareFedSwitchActiveNpuSlotPortInfo(
    ShowPlatformHardwareFedSwitchActiveNpuSlotPortInfoSchema
):
    cli_command = (
        "show platform hardware fed switch {mode} npu slot 1 port {port_num} port-info"
    )

    def cli(self, mode, port_num, output=None):
        if output is None:
            output = self.device.execute(
                self.cli_command.format(mode=mode, port_num=port_num)
            )

        ret_dict = {}
        # SW port debug states
        p0 = re.compile(r"^\|\s*SW port debug states\s*\|$")

        # LED port debug states
        p1 = re.compile(r"^\|\s*LED port debug states\s*\|$")

        # LC present
        p2 = re.compile(r"^\s*LC present\s+(?P<lc_present>\d+)$")

        # Outstanding ports to be deleted
        p3 = re.compile(
            r"^\s*Outstanding ports to be deleted\s+(?P<outstanding_ports_to_be_deleted>\d+)$"
        )

        # Total failed Deleted ports
        p4 = re.compile(
            r"^\s*Total failed deleted ports\s+(?P<total_failed_deleted_ports>\d+)$"
        )

        # General Key: value
        p5 = re.compile(r"^\|?(?P<key>[\w\s/]+)\|\s*(?P<value>.+)$")

        for line in output.splitlines():
            line = line.strip()

            # SW port debug states
            m = p0.match(line)
            if m:
                root_dict = ret_dict.setdefault("sw_port_debug_states", {})
                continue

            # LED port debug states
            m = p1.match(line)
            if m:
                root_dict = ret_dict.setdefault("led_port_debug_states", {})
                continue

            # Match Outstanding ports to be deleted
            m = p2.match(line)
            if m:
                ret_dict["lc_present"] = int(m.group("lc_present"))
                continue

            # Match Outstanding ports to be deleted
            m = p3.match(line)
            if m:
                ret_dict["outstanding_ports_to_be_deleted"] = int(
                    m.group("outstanding_ports_to_be_deleted")
                )
                continue

            # Match Total failed deleted ports
            m = p4.match(line)
            if m:
                ret_dict["total_failed_deleted_ports"] = int(
                    m.group("total_failed_deleted_ports")
                )
                continue

            # Match SW and LED port debug states data
            m = p5.match(line)
            if m:
                group = m.groupdict()
                key = (
                    group["key"]
                    .strip()
                    .lower()
                    .replace(" ", "_")
                    .replace("|", "")
                    .replace("-", "_")
                    .replace("/", "_")
                )
                value = group["value"].strip()
                if value.isdigit():
                    root_dict[key] = int(value)
                else:
                    root_dict[key] = value

        return ret_dict


class ShowPlatformHardwareFedSwitchActiveNpuSlotPortLinkstatusSchema(MetaParser):
    """Schema for show  platform  hardware fed  switch  active  npu  slot  1  port 23 link_status"""

    schema = {
        "mpp_port_details": {
            Any(): Or(int, str),
        },
        "autoneg_details": {
            Any(): Or(int, str),
        },
        "autoneg_status": {
            Any(): Or(int, str),
        },
        "mib_counters": {
            Any(): int,
        },
        "port": int,
        "cmd": str,
        "rc": str,
        "rsn": str,
    }


class ShowPlatformHardwareFedSwitchActiveNpuSlotPortLinkstatus(
    ShowPlatformHardwareFedSwitchActiveNpuSlotPortLinkstatusSchema
):
    """
    ShowPlatformHardwareFedSwitchActiveNpuSlotPortLinkstatus
    """

    cli_command = "show platform hardware fed switch {mode} npu slot 1 port {port_num} link_status"

    def cli(self, mode, port_num, output=None):
        if output is None:
            output = self.device.execute(
                self.cli_command.format(mode=mode, port_num=port_num)
            )

        ret_dict = {}

        # MPP PORT DETAILS
        p0 = re.compile(r"^MPP +PORT +DETAILS$")

        # link_state: 1 pcs_status: 0  high_ber: 0
        p1 = re.compile(
            r"^link_state\: +(?P<link_state>\d+) +pcs_status\: +(?P<pcs_status>\d+) +high_ber\: +(?P<high_ber>\d+)$"
        )

        # get_state = LINK_UP
        p2 = re.compile(r"^get_state +\= +(?P<get_state>.*)$")

        # Autoneg Details
        p3 = re.compile(r"^Autoneg +Details$")

        # Autoneg Status
        p4 = re.compile(r"^Autoneg +Status$")

        # MIB counters
        p5 = re.compile(r"^MIB +counters$")

        # Genral - Speed:         speed_gbps1
        p6 = re.compile(r"^(?P<key>[\s*\w]+.*)\: +(?P<value>[\S\s]+.*)$")

        # Port = 22 cmd = (port_diag unit 0 port 22 slot 0) rc = 0x0 rsn = success
        p7 = re.compile(
            r"^Port +\= +(?P<port>\d+) +cmd +\= +\((?P<cmd>[\s*\w]+)\) +rc +\= +(?P<rc>\w+) +rsn +\= +(?P<rsn>\w+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # MPP PORT DETAILS
            m = p0.match(line)
            if m:
                root_dict = ret_dict.setdefault("mpp_port_details", {})
                continue

            #'114      329      0     0'
            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict["link_state"] = int(group["link_state"])
                root_dict["pcs_status"] = int(group["pcs_status"])
                root_dict["high_ber"] = int(group["high_ber"])
                continue

            # get_state = LINK_UP
            m = p2.match(line)
            if m:
                group = m.groupdict()
                root_dict["get_state"] = group["get_state"].strip()
                continue

            # Autoneg Details
            m = p3.match(line)
            if m:
                root_dict = ret_dict.setdefault("autoneg_details", {})
                continue

            # Autoneg Status
            m = p4.match(line)
            if m:
                root_dict = ret_dict.setdefault("autoneg_status", {})
                continue

            # MIB counters
            m = p5.match(line)
            if m:
                root_dict = ret_dict.setdefault("mib_counters", {})
                continue

            # Genral - Speed:         speed_gbps1
            m = p6.match(line)
            if m:
                group = m.groupdict()
                key = (
                    group["key"]
                    .strip()
                    .lower()
                    .replace(":", "")
                    .replace("-", "_")
                    .replace(" ", "_")
                )
                if group["value"].isdigit():
                    root_dict.update({key: int(group["value"])})
                else:
                    root_dict.update({key: group["value"]})
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict["port"] = int(group["port"])
                ret_dict["cmd"] = group["cmd"]
                ret_dict["rc"] = group["rc"]
                ret_dict["rsn"] = group["rsn"]
                continue

        return ret_dict


class ShowPlatformHardwareFedSwitchActiveNpuSlotPortLinkstatusSchema(MetaParser):
    """Schema for show  platform  hardware fed  switch  active  npu  slot  1  port 23 link_status"""

    schema = {
        "mpp_port_details": {
            Any(): Or(int, str),
        },
        "autoneg_details": {
            Any(): Or(int, str),
        },
        "autoneg_status": {
            Any(): Or(int, str),
        },
        "mib_counters": {
            Any(): int,
        },
        "port": int,
        "cmd": str,
        "rc": str,
        "rsn": str,
    }


class ShowPlatformHardwareFedSwitchActiveNpuSlotPortLinkstatus(
    ShowPlatformHardwareFedSwitchActiveNpuSlotPortLinkstatusSchema
):
    """
    ShowPlatformHardwareFedSwitchActiveNpuSlotPortLinkstatus
    """

    cli_command = "show platform hardware fed switch {mode} npu slot 1 port {port_num} link_status"

    def cli(self, mode, port_num, output=None):
        if output is None:
            output = self.device.execute(
                self.cli_command.format(mode=mode, port_num=port_num)
            )

        ret_dict = {}

        # MPP PORT DETAILS
        p0 = re.compile(r"^MPP +PORT +DETAILS$")

        # link_state: 1 pcs_status: 0  high_ber: 0
        p1 = re.compile(
            r"^link_state\: +(?P<link_state>\d+) +pcs_status\: +(?P<pcs_status>\d+) +high_ber\: +(?P<high_ber>\d+)$"
        )

        # get_state = LINK_UP
        p2 = re.compile(r"^get_state +\= +(?P<get_state>.*)$")

        # Autoneg Details
        p3 = re.compile(r"^Autoneg +Details$")

        # Autoneg Status
        p4 = re.compile(r"^Autoneg +Status$")

        # MIB counters
        p5 = re.compile(r"^MIB +counters$")

        # Genral - Speed:         speed_gbps1
        p6 = re.compile(r"^(?P<key>[\s*\w]+.*)\: +(?P<value>[\S\s]+.*)$")

        # Port = 22 cmd = (port_diag unit 0 port 22 slot 0) rc = 0x0 rsn = success
        p7 = re.compile(
            r"^Port +\= +(?P<port>\d+) +cmd +\= +\((?P<cmd>[\s*\w]+)\) +rc +\= +(?P<rc>\w+) +rsn +\= +(?P<rsn>\w+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # MPP PORT DETAILS
            m = p0.match(line)
            if m:
                root_dict = ret_dict.setdefault("mpp_port_details", {})
                continue

            #'114      329      0     0'
            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict["link_state"] = int(group["link_state"])
                root_dict["pcs_status"] = int(group["pcs_status"])
                root_dict["high_ber"] = int(group["high_ber"])
                continue

            # get_state = LINK_UP
            m = p2.match(line)
            if m:
                group = m.groupdict()
                root_dict["get_state"] = group["get_state"].strip()
                continue

            # Autoneg Details
            m = p3.match(line)
            if m:
                root_dict = ret_dict.setdefault("autoneg_details", {})
                continue

            # Autoneg Status
            m = p4.match(line)
            if m:
                root_dict = ret_dict.setdefault("autoneg_status", {})
                continue

            # MIB counters
            m = p5.match(line)
            if m:
                root_dict = ret_dict.setdefault("mib_counters", {})
                continue

            # Genral - Speed:         speed_gbps1
            m = p6.match(line)
            if m:
                group = m.groupdict()
                key = (
                    group["key"]
                    .strip()
                    .lower()
                    .replace(":", "")
                    .replace("-", "_")
                    .replace(" ", "_")
                )
                if group["value"].isdigit():
                    root_dict.update({key: int(group["value"])})
                else:
                    root_dict.update({key: group["value"]})
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict["port"] = int(group["port"])
                ret_dict["cmd"] = group["cmd"]
                ret_dict["rc"] = group["rc"]
                ret_dict["rsn"] = group["rsn"]
                continue

        return ret_dict


class ShowPlatformHwFedActiveQosQStatsInternalCpuPolicerSchema(MetaParser):
    """Schema for show platform hardware fed active qos queue stats internal cpu policer"""

    schema = {
        "cpu_queue_statistics": {
            Any(): {
                "cpu_qid": int,
                "cpu_picidx": int,
                "cpu_queue_name": str,
                "cpu_enabled": str,
                "cpu_default_rate": int,
                "cpu_set_rate": int,
                "q_drop_bytes": int,
                "q_drop_frames": int,
            }
        },
        "cpu_policer_stats": {
            Any(): {
                "index": int,
                "accept_bytes": int,
                "accept_frames": int,
                "drop_bytes": int,
                "drop_frames": int,
            }
        },
        "cpp_classes_qmap": {
            Any(): {"cpp_picidx": int, "cpp_class": str, "cpp_enabled": str}
        },
        "sec_policer_config": {
            Any(): {
                "sec_qid": int,
                "sec_level1_picidx": int,
                "sec_level2_picidx": str,
                "sec_queue_name": str,
                "sec_enabled": str,
            }
        },
        "policer_index_map": {
            Any(): {
                "cpp_level2_picidx": int,
                "cpp_level1_picidx": str,
                "cpp_default_rate": int,
                "cpp_set_rate": int,
            }
        },
    }


class ShowPlatformHwFedActiveQosQStatsInternalCpuPolicer(
    ShowPlatformHwFedActiveQosQStatsInternalCpuPolicerSchema
):
    """Parser for show platform hardware fed active qos queue stats internal cpu policer"""

    cli_command = [
        "show platform hardware fed {state} qos queue stats internal cpu policer",
        "show platform hardware fed {switch} {state} qos queue stats internal cpu policer",
    ]

    def cli(self, state="active", switch=None, output=None):
        if output is None:
            if state and switch:
                cmd = self.cli_command[1].format(state=state, switch=switch)
            else:
                cmd = self.cli_command[0].format(state=state)
            output = self.device.execute(cmd)

        # 0    11     DOT1X Auth                  Yes     1000      1000     0            0
        p1 = re.compile(
            r"^(?P<cpu_qid>\d+)\s+(?P<cpu_picidx>\d+)\s+(?P<cpu_queue_name>[\w\s]+)\s+(?P<cpu_enabled>Yes|No)\s+(?P<cpu_default_rate>\d+)\s+(?P<cpu_set_rate>\d+)\s+(?P<q_drop_bytes>\d+)\s+(?P<q_drop_frames>\d+)$"
        )

        # 1          281306           1403            0             0
        p2 = re.compile(
            r"^(?P<index>\d+)\s+(?P<accept_bytes>\d+)\s+(?P<accept_frames>\d+)\s+(?P<drop_bytes>\d+)\s+(?P<drop_frames>\d+)$"
        )

        # 20        :   1  2  8                        17000     17000
        p3 = re.compile(
            r"^(?P<cpp_level2_picidx>\d+)\s+:(?P<cpp_level1_picidx>[\w\s]+)\s+(?P<cpp_default_rate>[\d]+)\s+(?P<cpp_set_rate>[\d]+)$"
        )

        # 0      system-cpp-police-data                   :  ICMP GEN/ BROADCAST/ ICMP Redirect/
        p4 = re.compile(
            r"^(?P<cpp_picidx>\d+)\s+(?P<cpp_class>[\-\w\s]+)\s+:(?P<cpp_enabled>[\-\w\s\/]+)$"
        )

        # 30   9       21      MCAST Data                  Yes
        # 31   3       -       Gold Pkt                    No
        p5 = re.compile(
            r"^(?P<sec_qid>\d+)\s+(?P<sec_level1_picidx>\d+)\s+(?P<sec_level2_picidx>[\-\d]+)\s+(?P<sec_queue_name>[\w\s]+)\s+(?P<sec_enabled>Yes|No)$"
        )

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # 0    11     DOT1X Auth                  Yes     1000      1000     0            0
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                template_var = dict_val["cpu_queue_name"].strip()
                if "cpu_queue_statistics" not in ret_dict:
                    cpu_queue_statistics = ret_dict.setdefault(
                        "cpu_queue_statistics", {}
                    )
                if template_var not in ret_dict["cpu_queue_statistics"]:
                    cpu_queue_stats = ret_dict["cpu_queue_statistics"].setdefault(
                        template_var, {}
                    )
                cpu_queue_stats["cpu_qid"] = int(dict_val["cpu_qid"])
                cpu_queue_stats["cpu_picidx"] = int(dict_val["cpu_picidx"])
                cpu_queue_stats["cpu_queue_name"] = dict_val["cpu_queue_name"].strip()
                cpu_queue_stats["cpu_enabled"] = dict_val["cpu_enabled"]
                cpu_queue_stats["cpu_default_rate"] = int(dict_val["cpu_default_rate"])
                cpu_queue_stats["cpu_set_rate"] = int(dict_val["cpu_set_rate"])
                cpu_queue_stats["q_drop_bytes"] = int(dict_val["q_drop_bytes"])
                cpu_queue_stats["q_drop_frames"] = int(dict_val["q_drop_frames"])
                continue

            # 1          281306           1403            0             0
            m = p2.match(line)
            if m:
                dict_val = m.groupdict()
                if "cpu_policer_stats" not in ret_dict:
                    cpu_policer_stats = ret_dict.setdefault("cpu_policer_stats", {})
                template_var = int(dict_val["index"])
                if template_var not in ret_dict["cpu_policer_stats"]:
                    cpu_policer_stats = ret_dict["cpu_policer_stats"].setdefault(
                        template_var, {}
                    )
                cpu_policer_stats["index"] = int(dict_val["index"])
                cpu_policer_stats["accept_bytes"] = int(dict_val["accept_bytes"])
                cpu_policer_stats["accept_frames"] = int(dict_val["accept_frames"])
                cpu_policer_stats["drop_bytes"] = int(dict_val["drop_bytes"])
                cpu_policer_stats["drop_frames"] = int(dict_val["drop_frames"])
                continue

            # 20        :   1  2  8                        17000     17000
            m = p3.match(line)
            if m:
                dict_val = m.groupdict()
                if "policer_index_map" not in ret_dict:
                    policer_index_map = ret_dict.setdefault("policer_index_map", {})
                template_var = dict_val["cpp_level2_picidx"]
                if template_var not in ret_dict["policer_index_map"]:
                    policer_index_map = ret_dict["policer_index_map"].setdefault(
                        template_var, {}
                    )
                policer_index_map["cpp_level2_picidx"] = int(
                    dict_val["cpp_level2_picidx"]
                )
                policer_index_map["cpp_level1_picidx"] = dict_val["cpp_level1_picidx"]
                policer_index_map["cpp_default_rate"] = int(
                    dict_val["cpp_default_rate"]
                )
                policer_index_map["cpp_set_rate"] = int(dict_val["cpp_set_rate"])
                continue

            # 0      system-cpp-police-data                   :  ICMP GEN/ BROADCAST/ ICMP Redirect/
            m = p4.match(line)
            if m:
                dict_val = m.groupdict()
                if "cpp_classes_qmap" not in ret_dict:
                    cpp_classes_qmap = ret_dict.setdefault("cpp_classes_qmap", {})
                template_var = dict_val["cpp_picidx"].strip()
                if template_var not in ret_dict["cpp_classes_qmap"]:
                    cpp_classes_qmap = ret_dict["cpp_classes_qmap"].setdefault(
                        template_var, {}
                    )
                cpp_classes_qmap["cpp_picidx"] = int(dict_val["cpp_picidx"])
                cpp_classes_qmap["cpp_class"] = dict_val["cpp_class"].strip()
                cpp_classes_qmap["cpp_enabled"] = dict_val["cpp_enabled"]
                continue

            # 31   3       -       Gold Pkt                    No
            m = p5.match(line)
            if m:
                dict_val = m.groupdict()
                if "sec_policer_config" not in ret_dict:
                    sec_policer_config = ret_dict.setdefault("sec_policer_config", {})
                template_var = dict_val["sec_qid"].strip()
                if template_var not in ret_dict["sec_policer_config"]:
                    sec_policer_config = ret_dict["sec_policer_config"].setdefault(
                        template_var, {}
                    )
                sec_policer_config["sec_qid"] = int(dict_val["sec_qid"])
                sec_policer_config["sec_level1_picidx"] = int(
                    dict_val["sec_level1_picidx"]
                )
                sec_policer_config["sec_level2_picidx"] = dict_val["sec_level2_picidx"]
                sec_policer_config["sec_queue_name"] = dict_val[
                    "sec_queue_name"
                ].strip()
                sec_policer_config["sec_enabled"] = dict_val["sec_enabled"]
                continue

        return ret_dict


class ShowPlatHardFedActiveQosQueueStatsOqMulticastAttachSchema(MetaParser):
    """Schema for show platform hardware fed switch {switch_num} qos queue stats oq multicast attach"""

    schema = {
        "oq_id": {
            Any(): {
                "interface": str,
            },
        },
    }


class ShowPlatHardFedActiveQosQueueStatsOqMulticastAttach(
    ShowPlatHardFedActiveQosQueueStatsOqMulticastAttachSchema
):
    """Parser for show platform hardware fed switch {switch_num} qos queue stats oq multicast attach"""

    cli_command = [
        "show platform hardware fed active qos queue stats oq multicast attach",
        "show platform hardware fed switch {switch_num} qos queue stats oq multicast attach",
    ]

    def cli(self, switch_num=None, output=None):
        if output is None:
            if switch_num:
                cmd = self.cli_command[1].format(switch_num=switch_num)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        #  HundredGigE1/0/5              6
        p1 = re.compile(r"^(?P<interface>\S+)\s+(?P<oq_id>\d+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            #  HundredGigE1/0/5              6
            m = p1.match(line)
            if m:
                oq_dict = ret_dict.setdefault("oq_id", {}).setdefault(
                    int(m.groupdict()["oq_id"]), {}
                )
                oq_dict.setdefault(
                    "interface", Common.convert_intf_name(m.groupdict()["interface"])
                )
                continue

        return ret_dict


# ================================================================================
# Parser Schema for 'show platform hardware fed active fwd-asic register read register-name'
# ================================================================================
class ShowPlatformHardwareRegisterReadAsicSchema(MetaParser):
    """
    This parser should fit any platform hardware Register Read CLIs:
    i.e.
    show platform hardware fed active fwd-asic register read register-name xyz asic n core m
    show platform hardware fed switch x fwd-asic register read register-name xyz asic n core m
    """

    schema = {"asic": {int: {"core": {int: {Any(): str}}}}}


class ShowPlatformHardwareRegisterReadAsic(ShowPlatformHardwareRegisterReadAsicSchema):
    """
    show platform hardware fed active fwd-asic register read register-name xyz asic n core m
    show platform hardware fed switch x fwd-asic register read register-name xyz asic n core m
    """

    cli_command = [
        "show platform hardware fed active fwd-asic register read register-name {reg_name} asic {asic} core {core}",
        "show platform hardware fed switch {switch_no} fwd-asic register read register-name {reg_name} asic {asic} core {core}",
    ]

    def cli(self, reg_name, asic, core, switch_no=None, output=None):
        if output is None:
            if not switch_no:
                cmd = self.cli_command[0].format(
                    reg_name=reg_name, asic=asic, core=core
                )
            else:
                cmd = self.cli_command[1].format(
                    reg_name=reg_name, asic=asic, core=core, switch_no=switch_no
                )
            output = self.device.execute(cmd)

        ret_dict = {}

        # For asic 1 core 0
        p0 = re.compile(r"^For +asic +(?P<asic>\d+) +core +(?P<core>\d+)$")

        # <key>: <value>   i.e. waitTimer                 : 0xfffbfff88
        p1 = re.compile(r"^(?P<key>\S+)\s*:\s*(?P<hex>0[xX][0-9a-fA-F]+)$")

        for line in output.splitlines():
            line = line.strip()

            # For asic 1 core 0 (Initilize the dict of the asic/core combination)
            m = p0.match(line)
            if m:
                parsed = m.groupdict()
                asic = int(parsed["asic"])
                core = int(parsed["core"])
                ret_dict.setdefault("asic", dict())
                ret_dict["asic"].setdefault(asic, dict())
                ret_dict["asic"][asic].setdefault("core", dict())
                ret_dict["asic"][asic]["core"].setdefault(core, dict())
                current_ret_dict = ret_dict["asic"][asic]["core"][core]
                continue

            # <key>: <value> ... any values that can match this pattern will be put under the asic/core dict
            m = p1.match(line)
            if m:
                parsed = m.groupdict()
                current_ret_dict[parsed["key"]] = parsed["hex"]

        return ret_dict


class ShowPlatformHardwareFedPortPrbscmdSchema(MetaParser):
    """Schema for show platform hardware fed switch {mode} npu slot 1 port {port_num} prbs_cmd {num}"""

    schema = {
        'port': int,
        Optional('slot'): int,
        'cmd': str,
        'rc': str,
        Optional('rsn'): str,
        Optional('reason'): str,
   }


class ShowPlatformHardwareFedPortPrbscmd(ShowPlatformHardwareFedPortPrbscmdSchema):
    """
    show platform hardware fed {switch} {mode} npu slot 1 port {port_num} prbs_cmd {num}
    """

    cli_command = ['show platform hardware fed {switch} {mode} npu slot 1 port {port_num} prbs_cmd {num}',
                   'show platform hardware fed {mode} npu slot 1 port {port_num} prbs_cmd {num}']

    def cli(self, mode, port_num, num, switch=None, output=None):

        if output is None:
            if switch:
                output = self.device.execute(self.cli_command[0].format(switch=switch, mode=mode,port_num=port_num,num=num))
            else:
                output = self.device.execute(self.cli_command[1].format(mode=mode,port_num=port_num,num=num))


        ret_dict = {}

        # Port = 40 Slot = 1 cmd = () rc = 0x16 reason = (null)
        p0 = re.compile(r'^Port +\= +(?P<port>\d+) +Slot +\= +(?P<slot>\d+) +cmd +\= +(?P<cmd>\([\s*\w]*\)) +rc +\= +(?P<rc>\w+) +reason(?P<reason>.*)$')

        # Port = 39 cmd = (prbs_stop unit 0 port 39 slot 1 serdes_level 1 polynomial 31) rc = 0x0 rsn = success
        p1  =  re.compile(r'^Port +\= +(?P<port>\d+) +cmd +\= +(?P<cmd>\([\s*\w]*\)) +rc +\= +(?P<rc>\w+) +rsn +\= +(?P<rsn>.*)$')


        for line in output.splitlines():
            line = line.strip()

            # Port = 40 Slot = 1 cmd = () rc = 0x16 reason = (null)
            m = p0.match(line)
            if m:
                group = m.groupdict()
                ret_dict['port'] = int(group['port'])
                ret_dict['slot'] = int(group['slot'])
                ret_dict['cmd'] = group['cmd']
                ret_dict['rc'] = group['rc']
                ret_dict['reason'] = group['reason']
                continue

            # Port = 39 cmd = (prbs_stop unit 0 port 39 slot 1 serdes_level 1 polynomial 31) rc = 0x0 rsn = success
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['port'] = int(group['port'])
                ret_dict['cmd'] = group['cmd']
                ret_dict['rc'] = group['rc']
                ret_dict['rsn'] = group['rsn']
                continue

        return ret_dict

class ShowPlatformHardwareFedPrbsPolynomialSchema(MetaParser):
    """Schema for show platform hardware fed switch {mode} npu slot 1 port {port_num} prbs_polynomial {num}"""

    schema = {
        'port': int,
        Optional('slot'): int,
        'cmd': str,
        'rc': str,
        Optional('rsn'): str,
        Optional('reason'): str,
   }


class ShowPlatformHardwareFedPrbsPolynomial(ShowPlatformHardwareFedPrbsPolynomialSchema):
    """
    show platform hardware fed switch {mode} npu slot 1 port {port_num} prbs_polynomial {num}
    """

    cli_command = ['show platform hardware fed {switch} {mode} npu slot 1 port {port_num} prbs_polynomial {num}',
                   'show platform hardware fed {mode} npu slot 1 port {port_num} prbs_polynomial {num}']

    def cli(self, mode, port_num, num, switch=None, output=None):

        if output is None:
            if  switch:
                output = self.device.execute(self.cli_command[0].format(switch=switch, mode=mode,port_num=port_num,num=num))
            else:
                output = self.device.execute(self.cli_command[1].format(mode=mode,port_num=port_num,num=num))

        ret_dict = {}

        # Port = 40 Slot = 1 cmd = () rc = 0x16 reason = (null)
        p0 = re.compile(r'^Port +\= +(?P<port>\d+) +Slot +\= +(?P<slot>\d+) +cmd +\= +(?P<cmd>\([\s\w]*\)) +rc +\= +(?P<rc>\w+) +reason(?P<reason>.*)$')

        # Port = 39 cmd = (prbs_stop unit 0 port 39 slot 1 serdes_level 1 polynomial 31) rc = 0x0 rsn = success
        p1  =  re.compile(r'^Port +\= +(?P<port>\d+) +cmd +\= +(?P<cmd>\([\s\w]*\)) +rc +\= +(?P<rc>\w+) +rsn +\= +(?P<rsn>.*)$')


        for line in output.splitlines():
            line = line.strip()

            # Port = 40 Slot = 1 cmd = () rc = 0x16 reason = (null)
            m = p0.match(line)
            if m:
                group = m.groupdict()
                ret_dict['port'] = int(group['port'])
                ret_dict['slot'] = int(group['slot'])
                ret_dict['cmd'] = group['cmd']
                ret_dict['rc'] = group['rc']
                ret_dict['reason'] = group['reason']
                continue

            # Port = 39 cmd = (prbs_stop unit 0 port 39 slot 1 serdes_level 1 polynomial 31) rc = 0x0 rsn = success
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['port'] = int(group['port'])
                ret_dict['cmd'] = group['cmd']
                ret_dict['rc'] = group['rc']
                ret_dict['rsn'] = group['rsn']
                continue

        return ret_dict

class ShowPlatformHardwareFedloopbackSchema(MetaParser):
    """Schema for show platform hardware fed switch {mode} npu slot 1 port {port_num} loopback {num}"""

    schema = {
        Optional('npu_pdsf_procagent_config_loopback'): str,
        Optional('npu_pdsf_port_config_loopback'): str,
        'port': int,
        Optional('slot'): int,
        'cmd': str,
        'rc': str,
        Optional('rsn'): str,
        Optional('reason'): str,
   }


class ShowPlatformHardwareFedloopback(ShowPlatformHardwareFedloopbackSchema):
    """
    show platform hardware fed switch {mode} npu slot 1 port {port_num} loopback {num}
    """

    cli_command = ['show platform hardware fed {switch} {mode} npu slot 1 port {port_num} loopback {num}',
                   'show platform hardware fed {mode} npu slot 1 port {port_num} loopback {num}']

    def cli(self, mode, port_num, num, switch=None, output=None):

        if output is None:
            if switch:
                output = self.device.execute(self.cli_command[0].format(switch=switch, mode=mode,port_num=port_num,num=num))
            else:
                output = self.device.execute(self.cli_command[1].format(mode=mode,port_num=port_num,num=num))

        ret_dict = {}

        #npu_pdsf_procagent_config_loopback : asic inst 0 port 39 mode 1 command 20
        p1 =  re.compile(r'^npu_pdsf_procagent_config_loopback\s*\:\s*(?P<npu_pdsf_procagent_config_loopback>.*)$')

        #npu_pdsf_l1_port_config_loopback [asic 0 port 39 mode 1]: returned 0 ()
        p2  = re.compile(r'^\w+\s*\[[\s*\w]+\]\:(?P<npu_pdsf_port_config_loopback>.*)$')

        # Port = 40 Slot = 1 cmd = () rc = 0x16 reason = (null)
        p3 = re.compile(r'^Port +\= +(?P<port>\d+) +Slot +\= +(?P<slot>\d+) +cmd +\= +(?P<cmd>\([\s*\S]*\)) +rc +\= +(?P<rc>\w+) +reason(?P<reason>.*)$')

        # Port = 39 cmd = (prbs_stop unit 0 port 39 slot 1 serdes_level 1 polynomial 31) rc = 0x0 rsn = success
        p4  =  re.compile(r'^Port +\= +(?P<port>\d+) +cmd +\= +(?P<cmd>\([\s*\S]*\)) +rc +\= +(?P<rc>\w+) +rsn +\= +(?P<rsn>.*)$')


        for line in output.splitlines():
            line = line.strip()

            #npu_pdsf_procagent_config_loopback : asic inst 0 port 39 mode 1 command 20
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['npu_pdsf_procagent_config_loopback'] = group['npu_pdsf_procagent_config_loopback']
                continue

            #npu_pdsf_l1_port_config_loopback [asic 0 port 39 mode 1]: returned 0 ()
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['npu_pdsf_port_config_loopback'] = group['npu_pdsf_port_config_loopback']
                continue

            # Port = 40 Slot = 1 cmd = () rc = 0x16 reason = (null)
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict['port'] = int(group['port'])
                ret_dict['slot'] = int(group['slot'])
                ret_dict['cmd'] = group['cmd']
                ret_dict['rc'] = group['rc']
                ret_dict['reason'] = group['reason']
                continue

            # Port = 39 cmd = (prbs_stop unit 0 port 39 slot 1 serdes_level 1 polynomial 31) rc = 0x0 rsn = success
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict['port'] = int(group['port'])
                ret_dict['cmd'] = group['cmd']
                ret_dict['rc'] = group['rc']
                ret_dict['rsn'] = group['rsn']
                continue

        return ret_dict


class ShowPlatformHardwareFedSwitchActiveStandbyFwdAsicInsightNplSummaryDiffSchema(MetaParser):
    """
    Schema for show platform hardware fed switch {type} fwd-asic insight npl_summary_diff{files_compare}
    show platform hardware fed switch {type} fwd-asic insight npl_summary_diff{files_compare}
    """
    schema = {
            'table_name':{
                  Any(): {
                    'length_subtables_f1': int,
                    'length_subtables_f2': int,
                    'nb_subtables_f1': int,
                    'nb_subtables_f2': int
              }
            }
        }

class ShowPlatformHardwareFedSwitchActiveStandbyFwdAsicInsightNplSummaryDiff(ShowPlatformHardwareFedSwitchActiveStandbyFwdAsicInsightNplSummaryDiffSchema):
    """ Parser for show platform hardware fed switch {type} fwd-asic insight npl_summary_diff{files_compare}     """

    cli_command = 'show platform hardware fed switch {type} fwd-asic insight npl_summary_diff{files_compare}'

    def cli(self, type,files_compare, output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(type=type,files_compare=files_compare))

        ret_dict = {}

        # table_name                               length_subtables_f1            length_subtables_f2            nb_subtables_f1                nb_subtables_f2
        # mac_forwarding_table                     (3,)                           (4,)                           1                              1                              nb_subtables_f2
        p1 = re.compile(r"^(?P<table_name>\S+)\s+.(?P<length_subtables_f1>\d+)\S+\s+.(?P<length_subtables_f2>\d+)\S+\s+.(?P<nb_subtables_f1>\d+)\s+(?P<nb_subtables_f2>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            # table_name                               length_subtables_f1            length_subtables_f2            nb_subtables_f1                nb_subtables_f2
            # mac_forwarding_table                     (3,)                           (4,)                           1                              1                              nb_subtables_f2
            m = p1.match(line)
            if m:
                group=m.groupdict()
                result_dict=ret_dict.setdefault('table_name', {}).setdefault(group['table_name'], {})
                result_dict.update({
                    'length_subtables_f1': int(group['length_subtables_f1']),
                    'length_subtables_f2': int(group['length_subtables_f2']),
                    'nb_subtables_f1': int(group['nb_subtables_f1']),
                    'nb_subtables_f2': int(group['nb_subtables_f2'])
                })
                continue

        return ret_dict





# ======================================================================
# Parser for 'show platform hardware fed switch active fwd-asic drops asic 0 '
# ======================================================================


class ShowPlatformHardwareFedSwitchActiveFwdasicdropsasicSchema(MetaParser):
    """Schema for
    * show platform hardware fed switch {switch} fwd-asic drops asic {asic}
    """

    schema = {
        "counter_index": {
            int: {
                "id": int,
                "counter_name": str,
                "slice_number": int,
                "ifg_number": int,
                "prev_value": int,
                "current_value": int,
                "delta": int
            }
        }
    }


class ShowPlatformHardwareFedSwitchActiveFwdasicdropsasic(
    ShowPlatformHardwareFedSwitchActiveFwdasicdropsasicSchema
):
    """Parser for
    * show platform hardware fed switch {switch} fwd-asic drops asic {asic}
    """

    cli_command = "show platform hardware fed switch {switch} fwd-asic drops asic {asic}"

    def cli(self, switch, asic, output=None):
        if output is None:
            if switch:
                output = self.device.execute(
                self.cli_command.format(switch=switch, asic=asic)
            )

        #Note: Slice and IFG showing -1 are global counters
        #======================================================================================================================================================#
        #|  #     |                      Counters Name                        |slice_number|   ifg_number  |  prev_value   |  current_value  |     delta      #|
        #======================================================================================================================================================
        #|  1    |Fwd drop counter (DSP==1): pkts                             |          -1|             -1|              0|                0|               0|
        #|  2    |Fwd drop counter (DSP==1): bytes                            |          -1|             -1|              0|                0|               0|
        #|  3    |RX_METER Slice0 drop_pkts                                   |           0|             -1|              0|                0|               0|
        #|  4    |FLLB Slice0 drop_pkts                                       |

        p1 = re.compile(
            r"^\|+\s+(?P<id>\d+)+\s+\|+(?P<counter_name>[\w\s\_\-\=\(\)\']+)\s+\|+\s*(?P<slice_number>\d+)+\s*\|+\s*(?P<ifg_number>[\d\-]+)+\s*\|+\s+(?P<prev_value>\d+)+\s*\|+\s+(?P<current_value>\d+)+\s*\|+\s+(?P<delta>\d+)+\|$"
        )

        ret_dict = {}
        counter_index = 1

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                id_dict = ret_dict.setdefault("counter_index", {}).setdefault(
                    counter_index, {}
                )
                id_dict["id"] = int(group["id"].strip())
                id_dict["counter_name"] = group["counter_name"].strip()
                id_dict["slice_number"] = int(group["slice_number"])
                id_dict["ifg_number"] = int(group["ifg_number"])
                id_dict["prev_value"] = int(group["prev_value"])
                id_dict["current_value"] = int(group["current_value"])
                id_dict["delta"] = int(group["delta"])
                counter_index += 1

        return ret_dict

# ================================================================================
# Schema for 'show platform hardware fed switch active vlan {num} ingress'
# ================================================================================
class ShowPlatformHardwareFedSwitchActiveVlanIngressSchema(MetaParser):

    """Schema for show platform hardware fed switch active vlan {num} ingress"""
    schema = {
        'vlan_id' : int,
        Optional('forwarding_state') : {
            Optional('tagged_list') : ListOf(str),
            Optional('untagged_list') : ListOf(str)
        },
        Optional('flood_list'): ListOf(str)
    }

# ================================================================================
# Parser for 'show platform hardware fed switch active vlan {num} ingress'
# ================================================================================

class ShowPlatformHardwareFedSwitchActiveVlanIngress(

    ShowPlatformHardwareFedSwitchActiveVlanIngressSchema):

    """Parser for show platform hardware fed switch active vlan {num} ingress"""

    cli_command = 'show platform hardware fed switch active vlan {num} ingress'

    def cli(self, num, output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(num=num))
        ret_dict = {}

        # vlan id is:: 1
        p1 = re.compile(r'^vlan\s+id\s+is::\s* (?P<vlan_id>\d+)')

        # Interfaces in forwarding state: : Gi1/0/15(Tagged), Fo5/0/9(Untagged)
        p2 = re.compile(r'^Interfaces\s+in\s+forwarding state\s*:\s*:\s*(?P<forwarding_state>[\w\/\.\s\(\w\)\,]+)$')

        # flood list: : Gi1/0/15, Fo5/0/9
        p3 = re.compile(r'^flood\s+list\s*:\s+:\s+(?P<flood_list>([\w\/\.\s\,]+)$)')

        # Gi1/0/15
        p4 = re.compile(r'^(?P<intf>([\w\/\.\s]+))')

        for line in output.splitlines():
            line = line.strip()

            # vlan id is:: 1
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                ret_dict["vlan_id"] = int(group["vlan_id"])
                continue

            # Interfaces in forwarding state: : Gi1/0/15(Tagged), Fo5/0/9(Untagged)
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                for intf in group['forwarding_state'].split(', '):
                    intf_match = p4.match(intf)
                    ret_dict.setdefault('forwarding_state', {}).setdefault('tagged_list',[])
                    ret_dict['forwarding_state'].setdefault('untagged_list',[])

                    ret_dict['forwarding_state'].setdefault('untagged_list',[])
                    if ('Tagged' in intf) and (intf_match):
                        ret_dict['forwarding_state']['tagged_list'].append(Common.convert_intf_name(intf_match["intf"]))
                    if ('Untagged' in intf) and (intf_match):
                        ret_dict['forwarding_state']['untagged_list'].append(Common.convert_intf_name(intf_match["intf"]))
                continue

            # flood list: : Gi1/0/15, Fo5/0/9
            m3 = p3.match(line)
            if m3:
                flood_list_group = m3.groupdict()
                for interface in flood_list_group['flood_list'].split(', '):
                    intf_match = p4.match(interface)
                    ret_dict.setdefault('flood_list',[])
                    if intf_match:
                        ret_dict['flood_list'].append(Common.convert_intf_name(intf_match['intf']))
                continue
        return ret_dict

# ================================================================================
# Schema for 'show platform hardware fed switch standby vlan {num} ingress'
# ================================================================================
class ShowPlatformHardwareFedSwitchStandbyVlanIngressSchema(MetaParser):

    """Schema for show platform hardware fed switch standby vlan {num} ingress"""
    schema = {
        'vlan_id' : int,
        Optional('forwarding_state') : {
            Optional('tagged_list') : ListOf(str),
            Optional('untagged_list') : ListOf(str)
        },
        Optional('flood_list'):ListOf(str)
    }

# ================================================================================
# Parser for 'show platform hardware fed switch standby vlan {num} ingress'
# ================================================================================

class ShowPlatformHardwareFedSwitchStandbyVlanIngress(

    ShowPlatformHardwareFedSwitchStandbyVlanIngressSchema):

    """Parser for show platform hardware fed switch standby vlan {num} ingress"""

    cli_command = 'show platform hardware fed switch standby vlan {num} ingress'

    def cli(self, num, output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(num=num))
        ret_dict = {}

        # vlan id is:: 1
        p1 = re.compile(r'^vlan\s+id\s+is::\s* (?P<vlan_id>\d+)')

        # Interfaces in forwarding state: : Gi1/0/15(Tagged), Fo5/0/9(Untagged)
        p2 = re.compile(r'^Interfaces\s+in\s+forwarding state\s*:\s*:\s*(?P<forwarding_state>[\w\/\.\s\(\w\)\,]+)$')

        # flood list: : Gi1/0/15, Fo5/0/9
        p3 = re.compile(r'^flood\s+list\s*:\s+:\s+(?P<flood_list>([\w\/\.\s\,]+)$)')

        # Gi1/0/15
        p4 = re.compile(r'^(?P<intf>([\w\/\.\s]+))')

        for line in output.splitlines():
            line = line.strip()

			# vlan id is:: 1
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                ret_dict["vlan_id"] = int(group["vlan_id"])
                continue

            # Interfaces in forwarding state: : Gi1/0/15(Tagged), Fo5/0/9(Untagged)
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                for intf in group['forwarding_state'].split(', '):
                    intf_match = p4.match(intf)
                    ret_dict.setdefault('forwarding_state', {}).setdefault('tagged_list',[])
                    ret_dict['forwarding_state'].setdefault('untagged_list',[])

                    ret_dict['forwarding_state'].setdefault('untagged_list',[])
                    if ('Tagged' in intf) and (intf_match):
                        ret_dict['forwarding_state']['tagged_list'].append(Common.convert_intf_name(intf_match["intf"]))
                    if ('Untagged' in intf) and (intf_match):
                        ret_dict['forwarding_state']['untagged_list'].append(Common.convert_intf_name(intf_match["intf"]))
                continue

            # flood list: : Gi1/0/15, Fo5/0/9
            m3 = p3.match(line)
            if m3:
                flood_list_group = m3.groupdict()
                for interface in flood_list_group['flood_list'].split(', '):
                    intf_match = p4.match(interface)
                    ret_dict.setdefault('flood_list',[])
                    if intf_match:
                        ret_dict['flood_list'].append(Common.convert_intf_name(intf_match['intf']))
                continue
        return ret_dict

# ======================================================
# Schema for 'show platform hardware fed switch {sw_number} qos queue config interface {interface} queue {queue_id} | include {match}'
# ======================================================

class ShowPlatformHardwareFedSwitchQosQueueConfigInterfaceQueueIncludeSchema(MetaParser):
    schema = {
        Optional('type'): str,
        'q_limit_blocks':  int,
    }

# ======================================================
# Parser for 'show platform hardware fed switch {sw_number} qos queue config interface {interface} queue {queue_id} | include {match}'
# ======================================================

class ShowPlatformHardwareFedSwitchQosQueueConfigInterfaceQueueInclude(ShowPlatformHardwareFedSwitchQosQueueConfigInterfaceQueueIncludeSchema):
    """Parser for show platform hardware fed switch {sw_number} qos queue config interface {interface} queue {queue_id} | include {match}"""
    cli_command = ['show platform hardware fed switch {sw_number} qos queue config interface {interface} queue {queue_id} | include {match}']


    def cli(self,interface,queue_id,match,sw_number,output=None):
        if output is None:
            cmd = self.cli_command[0].format(sw_number=sw_number,interface=interface,queue_id=queue_id,match=match)
            out = self.device.execute(cmd)
        else:
            out = output

        # Initialize the dictionary for the parsed output.
        result_dict = {}

        # Q-Limit(Blocks    )    : 100000
        # Q-Limit(Bytes    )    : 100000
        p1 = re.compile(r'^Q-Limit\((?P<type>Blocks|Bytes)\s+\)\s+:\s+(?P<q_limit_blocks>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # Q-Limit(Blocks    )    : 100000
            # Q-Limit(Bytes    )    : 100000
            m = p1.match(line)
            if m:
                group = m.groupdict()
                result_dict['type'] = group['type']
                result_dict['q_limit_blocks'] = int(group['q_limit_blocks'])
                continue
        return result_dict

# ======================================================
# Schema for 'show platform hardware fed switch {sw_number} qos scheduler interface {interface} | include {match}'
# ======================================================
class ShowPlatformHardwareFedSwitchQosSchedulerInterfaceIncludeSchema(MetaParser):
    schema = {
        'voq_offset': ListOf(int),
    }

# ======================================================
# Parser for 'show platform hardware fed switch {sw_number} qos scheduler interface {interface} | include {match} '
# ======================================================

class ShowPlatformHardwareFedSwitchQosSchedulerInterfaceInclude(ShowPlatformHardwareFedSwitchQosSchedulerInterfaceIncludeSchema):
    """Parser for show platform hardware fed switch {sw_number} qos scheduler interface {interface} | include {match}"""
    cli_command = ['show platform hardware fed switch {sw_number} qos scheduler interface {interface} | include {match}']

    def cli(self, sw_number,interface,match,output=None):
        if output is None:
            cmd = self.cli_command[0].format(sw_number=sw_number,interface=interface,match=match)
            out = self.device.execute(cmd)
        else:
            out = output

        # Initialize the dictionary for the parsed output.
        result_dict = {}

        # |                       : VOQ Offset :   0 |   0 |   0 |   0 |   0 |   5 |   6 |   7
        p1 = re.compile(r'^\|\s+:\s+VOQ\s+Offset\s+:\s+(?P<voq_offset>\d+\s+\|\s+\d+\s+\|\s+\d+\s+\|\s+\d+\s+\|\s+\d+\s+\|\s+\d+\s+\|\s+\d+\s+\|\s+\d+)')

        for line in out.splitlines():
            line = line.strip()

            # |                       : VOQ Offset :   0 |   0 |   0 |   0 |   0 |   5 |   6 |   7
            m = p1.match(line)
            if m:
                voq_offset = m.groupdict()['voq_offset'].split('|')
                result_dict['voq_offset'] = [int(i.strip()) for i in voq_offset]
                continue
        return result_dict

# ======================================================
# Schema for 'show platform software fed switch {sw_number} qos interface {interface} ingress npd detailed | include {match}'
# ======================================================
class ShowPlatformHardwareFedSwitchQosInterfaceIngressNdpDetailedIncludeSchema(MetaParser):
    schema = {
        'interface': str,
        'location': str,
        'direction': str,
        'cgid': str,
        'no_of_classes': int
    }

# ======================================================
# Parser for 'show platform software fed switch {sw_number} qos interface {interface} ingress npd detailed | include {match}'
# ======================================================

class ShowPlatformHardwareFedSwitchQosInterfaceIngressNdpDetailedInclude(ShowPlatformHardwareFedSwitchQosInterfaceIngressNdpDetailedIncludeSchema):
    """Parser for show platform software fed switch {sw_number} qos interface {interface} ingress npd detailed | include {match}"""
    cli_command = ['show platform software fed switch {sw_number} qos interface {interface} ingress npd detailed | include {match}']

    def cli(self, sw_number,interface,match, output=None):
        if output is None:
            cmd = self.cli_command[0].format(sw_number=sw_number,interface=interface,match=match)
            out = self.device.execute(cmd)
        else:
            out = output

        # Initialize the dictionary for the parsed output.
        ret_dict = {}

        # [GigabitEthernet1/0/2, pm-dc1-tc6, Ingress]: CGID = 0x634E00
        p1 = re.compile(r'^\[(?P<interface>\S+),\s+(?P<location>\S+),\s+(?P<direction>\S+)]:\s+CGID\s+=\s+(?P<cgid>\S+)$')

        #  No of classes: 1
        p2 = re.compile(r'^\s*No of classes:\s+(?P<no_of_classes>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # [GigabitEthernet1/0/2, pm-dc1-tc6, Ingress]: CGID = 0x634E00
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['interface'] = group['interface']
                ret_dict['location'] = group['location']
                ret_dict['direction'] = group['direction']
                ret_dict['cgid'] = group['cgid']
                continue

            #  No of classes: 1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['no_of_classes'] = int(group['no_of_classes'])
                continue

        return ret_dict

class ShowPlatformHardwareFedSwitchActiveSgaclResourceUsageSchema(MetaParser):
    # Schema for 'show platform hardware fed switch active sgacl resource usage'
    schema = {
        'device_id': int,
        'policy_entries': {
            'used': int,
            'max': int
        }
    }

class ShowPlatformHardwareFedSwitchActiveSgaclResourceUsage(ShowPlatformHardwareFedSwitchActiveSgaclResourceUsageSchema):
    # Parser for 'show platform hardware fed switch active sgacl resource usage'

    cli_command = 'show platform hardware fed switch active sgacl resource usage'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # ------------------------ SG-ACL Usage for Device ID 0 ------------------------
        p1 = re.compile(r'^.*SG-ACL Usage for Device ID (?P<device_id>\d+).*$')

        # Policy Entries : Used = 5, Max = 508
        p2 = re.compile(r'^Policy Entries : Used = (?P<used>\d+), Max = (?P<max>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # ------------------------ SG-ACL Usage for Device ID 0 ------------------------
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['device_id'] = int(group['device_id'])
                continue

            # Policy Entries : Used = 5, Max = 508
            m = p2.match(line)
            if m:
                group = m.groupdict()
                result_dict=ret_dict.setdefault('policy_entries',{})
                result_dict['used']=int(group['used'])
                result_dict['max']=int(group['max'])
                continue

        return ret_dict

class ShowPlatformHardwareFedSwitchActiveFwdAsicInsightL3unexthopSchema(MetaParser):
    """schema for show platform hardware fed switch ac fwd-asic insight l3u_nexthop{nh_gid}"""

    schema = {
        'nh_gid': int,
        'hex': str,
        'Value': {
            'destmac': str,
            'oid': str,
            'nh_payload': {
                'bd_mirror_cmd': str,
                'eve_vid1': str,
                'eve_vid2': str,
                'l2_flood': str,
                'l2_port': str,
                'lif_policy_id': str,
                'rtf_conf_set': str
            },
            Optional('l3_sa_vlan_or_l2_dlp_attr'): {
                'l3_sa_lsb': {
                    'sa_prefix_index': str,
                    'tpid_sa_lsb': {
                        'sa_lsb': str,
                        'tpid': str
                    }
                }
            }
        }
    }

class ShowPlatformHardwareFedSwitchActiveFwdAsicInsightL3unexthop(ShowPlatformHardwareFedSwitchActiveFwdAsicInsightL3unexthopSchema):
    """ Parser for show platform hardware fed switch {switch} fwd-asic insight l3u_nexthop{nh_gid} """

    cli_command = 'show platform hardware fed switch {switch} fwd-asic insight l3u_nexthop{nh_gid}'

    def cli(self, switch, nh_gid, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch=switch, nh_gid=nh_gid))

        ret_dict = {}

        # Nexthop with nh_gid: 0,0x0
        p1 = re.compile(r'Nexthop with nh_gid:\s+(?P<nh_gid>\d+).(?P<hex>\S+)$')

        # Value:
        p2 = re.compile(r'Value:$')

        # nh_da(dmac): 00:00:00:00:00:00/0x0
        p3 = re.compile(r'nh_da.dmac.\S+\s+(?P<destmac>\w+:\w+:\w+:\w+:\w+:\w+)\/(?P<oid>\w+)$')

        # nh_payload:
        p4 = re.compile(r'nh_payload:$')

        # bd_mirror_cmd: 0/0x0
        p5 = re.compile(r'bd_mirror_cmd:\s+(?P<bd_mirror_cmd>\S+)$')

        # eve_vid1: 0/0x0
        p6 = re.compile(r'eve_vid1:\s+(?P<eve_vid1>\S+)$')

        # eve_vid2: 0/0x0
        p7 = re.compile(r'eve_vid2:\s+(?P<eve_vid2>\S+)$')

        # l2_flood: 0/0x0
        p8 = re.compile(r'l2_flood:\s+(?P<l2_flood>\S+)$')

        # l2_port: 0/0x0
        p9 = re.compile(r'l2_port:\s+(?P<l2_port>\S+)$')

        # lif_policy_id: 0/0x0
        p10 = re.compile(r'lif_policy_id:\s+(?P<lif_policy_id>\S+)$')

        # rtf_conf_set: 0/0x0
        p11 = re.compile(r'rtf_conf_set:\s+(?P<rtf_conf_set>\S+)$')

        # l3_sa_vlan_or_l2_dlp_attr:
        p12 = re.compile(r'l3_sa_vlan_or_l2_dlp_attr:$')

        # l3_sa_lsb:
        p13 = re.compile(r'l3_sa_lsb:$')

        # sa_prefix_index: 0/0x0
        p14 = re.compile(r'sa_prefix_index:\s+(?P<sa_prefix_index>\S+)$')

        # tpid_sa_lsb:
        p15 = re.compile(r'tpid_sa_lsb:$')

        # sa_lsb: 0/0x0
        p16 = re.compile(r'sa_lsb:\s+(?P<sa_lsb>\S+)$')

        # tpid: 0/0x0
        p17 = re.compile(r'tpid:\s+(?P<tpid>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # Nexthop with nh_gid: 1,0x1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['nh_gid'] = int(group['nh_gid'])
                ret_dict['hex'] = group['hex']
                continue

            # Value:
            m = p2.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault('Value', {})
                continue
            # nh_da(dmac): 00:00:00:00:00:00/0x0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                root_dict['destmac'] = group['destmac']
                root_dict['oid'] = group['oid']
                continue
            # nh_payload:
            m = p4.match(line)
            if m:
                group = m.groupdict()
                result_dict = root_dict.setdefault('nh_payload', {})
                continue
            # bd_mirror_cmd: 0/0x0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                result_dict['bd_mirror_cmd'] = group['bd_mirror_cmd']
                continue
            # eve_vid1: 0/0x0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                result_dict['eve_vid1'] = group['eve_vid1']
                continue
            # eve_vid2: 0/0x0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                result_dict['eve_vid2'] = group['eve_vid2']
                continue
            # l2_flood: 0/0x0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                result_dict['l2_flood'] = group['l2_flood']
                continue
            # l2_port: 0/0x0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                result_dict['l2_port'] = group['l2_port']
                continue
            # lif_policy_id: 0/0x0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                result_dict['lif_policy_id'] = group['lif_policy_id']
                continue
            # rtf_conf_set: 0/0x0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                result_dict['rtf_conf_set'] = group['rtf_conf_set']
                continue
            # l3_sa_vlan_or_l2_dlp_attr:
            m = p12.match(line)
            if m:
                group = m.groupdict()
                results_dict = root_dict.setdefault('l3_sa_vlan_or_l2_dlp_attr', {})
                continue
            # l3_sa_lsb:
            m = p13.match(line)
            if m:
                group = m.groupdict()
                l3_dict = results_dict.setdefault('l3_sa_lsb', {})
                continue
            # sa_prefix_index: 0/0x0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                l3_dict['sa_prefix_index'] = group['sa_prefix_index']
                continue
            # tpid_sa_lsb:
            m = p15.match(line)
            if m:
                group = m.groupdict()
                tpid_dict = l3_dict.setdefault('tpid_sa_lsb', {})
                continue
            # sa_lsb: 0/0x0
            m = p16.match(line)
            if m:
                group = m.groupdict()
                tpid_dict['sa_lsb'] = group['sa_lsb']
                continue
            # tpid: 0/0x0
            m = p17.match(line)
            if m:
                group = m.groupdict()
                tpid_dict['tpid'] = group['tpid']
                continue

        return ret_dict


class ShowPlatformHardwareFedNpuDscDumpSchema(MetaParser):
    """Schema for show platform hardware fed switch active npu slot 1 port 23 link_status"""

    schema = {
        'npu_pdsf_procagent_get_eye_common':str,
        'mpp_port_detai1': {
            Any(): {
                'mac_state_histogram': {
                    Any(): Or(int,str),
                },
                'mac_port_config': {
                   Any(): Or(int,str),
                },
                'mac_port_status': {
                    Any(): Or(int,str),
                },
                'mib_counters': {
                    Any(): Or(int,str),
                },
                Optional('state_transition_history'): {
                    Any():{
                       'state': str,
                       'timestamp': str,
                    },
                },
            },
        },
        'multiport_detail': {
            Any(): {
                'device_info': {
                    Any(): str,
                },
                'mac_state_histogram':{
                    Any(): Or(int,str),
                    'serdes_0': {
                        Any(): Or(int,str),
                    },
                },
                'mac_port_config': {
                    Any(): Or(int,str),
                    'serdes_info': {
                        Any(): Or(int,str),
                    },
                },
                'mac_port_status': {
                    'am_lock': {
                        Any(): str,
                    },
                    Any(): Or(int,str),
                    'mac_pcs_lane_mapping': {
                        Any(): Or(int,str),
                    },
                },
                'mac_port_soft_state': {
                    Any(): Or(int,str),
                },
                'mib_counters': {
                    Any(): Or(int,str),
                    Optional('tx_mac_tc_fc_frames_ok'): {
                        Any(): Or(int,str),
                    },
                    Optional('tx_xoff_state_duration'): {
                        Any(): Or(int,str),
                    },
                    Optional('rx_mac_tc_fc_frames_ok'): {
                        Any(): Or(int,str),
                    },
                    Optional('rx_xoff_state_duration'): {
                        Any(): Or(int,str),
                    },
                },
                'test_mode': {
                    Any(): Or(int,str),
                },
                'state_transition_history': {
                    Any():{
                       'state': str,
                       'timestamp': str,
                    },
                },
                'serdes_parameters': {
                    'index_0': {
                        Any(): Or(int,str),
                    },
                },
                'serdes_config':{
                    'serdes_settings': {
                        'rx_settings': {
                            Any(): Or(int,str),
                            'targ_shadow':{
                                Any(): Or(int,str),
                            }
                        },
                        'tx_settings': {
                            Any(): Or(int,str),
                            'tx_fir': {
                                Any(): Or(int,str),
                            },
                        },
                        'flow_chart_settings': {
                            Any(): Or(int,str),
                        },
                    },
                },
                'serdes_status':{
                    'firmware_version': {
                        Any(): str,
                    },
                    'rx_status': {
                        Any(): Or(int,str),
                        'firs': {
                            Any(): Or(int,str),
                        }
                    },
                    'fw_rx_status': {
                        Any(): Or(int,str),
                    },
                    'fir_shadow': {
                        Any(): Or(int,str),
                    },
                },
                'eye_capture':{
                    'veye_data': {
                        Any(): Or(int,str),
                        'veye_values': {
                            Any(): Or(int,str),
                        },
                    },
                },
                'reg_dump':{
                    'quad_reg':{
                        Any(): Or(int,str),
                    },
                    'p_reg':{
                        Any(): Or(int,str),
                    },
                    's_reg':{
                        Any(): Or(int,str),
                    },
                    'rxdtop':{
                        Any(): Or(int,str),
                    },
                    'txdtop':{
                        Any(): Or(int,str),
                    },
                    'autoneg':{
                        Any(): Or(int,str),
                    },
                    'linktraining':{
                        Any(): Or(int,str),
                    },
                    'rx_sts':{
                        Any():Or(int,str),
                    },
                    'an_debug_1':{
                        Any(): Or(int,str),
                    },
                    'an_debug_2':{
                        Any(): Or(int,str),
                    },
                    'lt_debug_1':{
                        Any(): Or(int,str),
                    },
                    'lt_debug_2':{
                        Any(): Or(int,str),
                    },
                },
            },
        },
        'mac_port_link_down': {
            Any():{
                Any(): Or(int,str),
                'rx_deskew_fifo_overflow_count': {
                    Any(): Or(int,str),
                },
                'rx_pma_sig_ok_loss_interrupt_register_count': {
                    Any(): Or(int,str),
                },
            },
        },
        'mac_port_link_error': {
            Any(): {
                Any(): Or(int,str),
            },
        },
        'mac_port_link_debounce': {
            Any(): {
                Any(): Or(int,str),
            },
        },
        'port': int,
        Optional('slot'): int,
        'cmd': str,
        'rc': str,
        Optional('rsn'): str,
        Optional('reason'): str,
    }

class ShowPlatformHardwareFedNpuDscDump(ShowPlatformHardwareFedNpuDscDumpSchema):
    """
    ShowPlatformHardwareFedSwitchActiveNpuSlotPortDscDump
    """

    cli_command = 'show platform hardware fed switch {mode} npu slot 1 port {port_num} dsc_dump'

    def cli(self, mode, port_num, output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(mode=mode,port_num=port_num))

        ret_dict = {}

        # npu_pdsf_procagent_get_eye_common : asic inst 0 port 14 link 32 command 8
        p1 = re.compile(r'^npu_pdsf_procagent_get_eye_common\s*\: +(?P<npu_pdsf_procagent_get_eye_common>[\S\s]+.*)$')

        # "mpp_port_0_0_36:7": {
        p2  =  re.compile(r'^\"(?P<key>mpp_port_\d+_\d+_\d+\:\d+)\"\:\s*\{$')

        # "mac_state_histogram": {
        p2_1  =  re.compile(r'^\"mac_state_histogram\"\:\s*\{$')

        # "mac_port_status": {
        p2_2 = re.compile(r'^\"mac_port_status\"\:\s*\{$')

        # "mib_counters": {
        p2_3 = re.compile(r'^\"mib_counters\"\:\s*\{$')

        # "tx_mac_tc_fc_frames_ok": [
        p2_3_1 = re.compile(r'^\"tx_mac_tc_fc_frames_ok\"\:\s*\[$')

        # "tx_xoff_state_duration": [
        p2_3_2 = re.compile(r'^\"tx_xoff_state_duration\"\:\s*\[$')

        # "rx_mac_tc_fc_frames_ok": [
        p2_3_3 = re.compile(r'^\"rx_mac_tc_fc_frames_ok\"\:\s*\[$')

        # "rx_xoff_state_duration": [
        p2_3_4 = re.compile(r'^\"rx_xoff_state_duration\"\:\s*\[$')

        # "multiport_phy_0_0_36": {
        p3 = re.compile(r'^\"(?P<key>multiport_phy_\d+_\d+_\d+)\"\: +\{$')

        # "device_info": {
        p3_1 = re.compile(r'^\"device_info\"\:\s*\{$')

        # "serdes_0": {
        p3_1_1 = re.compile(r'^\"serdes_\d+\"\:\s*\{$')

        # "mac_port_config": {
        p3_2 =  re.compile(r'^\"mac_port_config\"\:\s*\{$')

        # "serdes_info_36": {
        p3_2_1 = re.compile(r'^\"serdes_info_\d+\"\:\s*\{$')

        # am_lock": [
        p3_3_1 = re.compile(r'^\"am_lock\"\:\s*\[$')

        # "mac_pcs_lane_mapping": [
        p3_3_2 =  re.compile(r'^\"mac_pcs_lane_mapping\"\:\s*\[$')

        # "mac_port_soft_state": {
        p3_4  = re.compile(r'^\"mac_port_soft_state\"\:\s*\{$')

        # "test_mode": {
        p3_5 = re.compile(r'^\"test_mode\"\:\s*\{$')

        # "state_transition_history": [
        p3_6 = re.compile(r'^\"state_transition_history\"\:\s*\[$')

        # "serdes_parameters": {
        p3_7 = re.compile(r'^\"serdes_parameters\"\:\s*\{$')

        # "index_0": {
        p3_7_1 = re.compile(r'^\"index_0\"\:\s*\{$')

        # "serdes_config": {
        p3_8 = re.compile(r'^\"serdes_config\"\:\s*\{$')

        #  "serdes_settings": [
        p3_8_1 = re.compile(r'^\"serdes_settings\"\:\s*\[$')

        # "rx_settings": {
        p3_8_1_1 = re.compile(r'^\"rx_settings\"\:\s*\{$')

        # "targ_shadow": [
        p3_8_1_1_1 =  re.compile(r'^\"targ_shadow\"\:\s*\[$')

        # "tx_settings": {
        p3_8_1_2  =  re.compile(r'^\"tx_settings\"\:\s*\{$')

        # "tx_fir": [
        p3_8_1_2_1 = re.compile(r'^\"tx_fir\"\:\s*\[$')

        # "flow_chart_settings": {
        p3_8_1_3 =  re.compile(r'^\"flow_chart_settings\"\:\s*\{$')

        # "serdes_status": {
        p3_9 = re.compile(r'^\"serdes_status\"\:\s*\{$')

        # "Firmware_Version": {
        p3_9_1 =  re.compile(r'^\"Firmware_Version\"\:\s*\{$')

        # "rx_status": [
        p3_9_2 = re.compile(r'^\"rx_status\"\:\s*\[$')

        # "firs": [
        p3_9_2_1 = re.compile(r'^\"firs\":\s*\[$')

        # "fw_rx_status": [
        p3_9_3 = re.compile(r'^\"fw_rx_status\"\:\s*\[$')

        # "fir_shadow": [
        p3_9_4 =  re.compile(r'^\"fir_shadow\"\:\s*\[$')

        # "eye_capture": {
        p3_10 = re.compile (r'^\"eye_capture\"\:\s*\{$')

        # "veye_data": [
        p3_10_1 = re.compile(r'^\"veye_data\"\:\s*\[$')

        # "veye_values": [
        p3_10_1_1 = re.compile(r'^\"veye_values\"\:\s*\[$')

        # "reg_dump": {
        p3_11 = re.compile(r'^\"reg_dump\"\:\s*\{$')

        # "Quad_Reg": [
        p3_11_1 = re.compile(r'^\"Quad_Reg\"\:\s*\[$')

        # "P_Reg": [
        p3_11_2 = re.compile(r'^\"P_Reg\"\:\s*\[$')

        # "S_reg": [
        p3_11_3 = re.compile(r'^\"S_reg\"\:\s*\[$')

        # "RXDTOP": [
        p3_11_4 = re.compile(r'^\"RXDTOP\"\:\s*\[$')

        # "TXDTOP": [
        p3_11_5 = re.compile(r'^\"TXDTOP\"\:\s*\[$')

        # "AutoNeg": [
        p3_11_6 = re.compile(r'^\"AutoNeg\"\:\s*\[$')

        # "LinkTraining": [
        p3_11_7 = re.compile(r'^\"LinkTraining\"\:\s*\[$')

        # "RX_STS": [
        p3_11_8 = re.compile(r'^\"RX_STS\"\:\s*\[$')

        # "an_debug_1": [
        p3_11_9 = re.compile(r'^\"an_debug_1\"\:\s*\[$')

        # ""an_debug_2": [
        p3_11_10 = re.compile(r'^\"an_debug_2\"\:\s*\[$')

        # "lt_debug_1": [
        p3_11_11 = re.compile(r'^\"lt_debug_1\"\:\s*\[$')

        # "lt_debug_2": [
        p3_11_12 = re.compile(r'^\"lt_debug_2\"\:\s*\[$')

        # "mac_port_0_0_36.link_down_histogram": {
        p4= re.compile(r'^\"(?P<key>mac_port_\d+_\d+_\d+\.link_down_histogram)\"\:\s*\{$')

        # "rx_deskew_fifo_overflow_count": [
        p4_1 = re.compile(r'^\"rx_deskew_fifo_overflow_count\"\:\s*\[$')

        # "rx_pma_sig_ok_loss_interrupt_register_count": [
        p4_2 = re.compile(r'^\"rx_pma_sig_ok_loss_interrupt_register_count\"\:\s*\[$')

        # "mac_port_0_0_36.link_error_histogram": {
        p5 =  re.compile(r'^\"(?P<key>mac_port_\d+_\d+_\d+\.link_error_histogram)\"\:\s*\{$')

        # "mac_port_0_0_36.link_debounce_state": {
        p6 = re.compile(r'^\"(?P<key>mac_port_\d+_\d+_\d+.link_debounce_state)\"\:\s*\{$')

        # Port = 40 Slot = 1 cmd = () rc = 0x16 reason = (null)
        p7 = re.compile(r'^Port +\= +(?P<port>\d+) +Slot +\= +(?P<slot>\d+) +cmd +\= +(?P<cmd>\([\s*\S]*\)) +rc +\= +(?P<rc>\w+) +reason(?P<reason>.*)$')

        # Port = 39 cmd = (prbs_stop unit 0 port 39 slot 1 serdes_level 1 polynomial 31) rc = 0x0 rsn = success
        p7_1 = re.compile(r'^Port +\= +(?P<port>\d+) +cmd +\= +(?P<cmd>\([\s*\S]*\)) +rc +\= +(?P<rc>\w+) +rsn +\= +(?P<rsn>.*)$')

        # "PRE_INIT": 0,
        p8 = re.compile(r'^\"(?P<key>\w+)\"\:\s*(?P<value>.*)$')

        # false
        p8_1 = re.compile(r'^(?P<value>\w+)$')

        # 64,
        p8_2 = re.compile(r'^(?P<value>[-]?\d+)\,$')

        #],
        p8_3 =  re.compile(r'^\]\,?$')

        cnt = index_flag = stat_cnt = multiport_flag = 0

        for line in output.splitlines():
            line = line.strip()

            # npu_pdsf_procagent_get_eye_common : asic inst 0 port 14 link 32 command 8
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['npu_pdsf_procagent_get_eye_common'] =  group['npu_pdsf_procagent_get_eye_common']
                continue

            # "mpp_port_0_0_36:7": {
            m = p2.match(line)
            if m:
                group = m.groupdict()
                port  =  group['key']
                curr_dict = ret_dict.setdefault('mpp_port_detai1', {}).setdefault(group['key'], {})
                continue

            # "mac_state_histogram": {
            m = p2_1.match(line)
            if m:
                group = m.groupdict()
                if multiport_flag == 1:
                    curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mac_state_histogram', {})
                else:
                    curr_dict =  ret_dict.setdefault('mpp_port_detai1', {}).setdefault(port, {}).setdefault('mac_state_histogram', {})
                continue

            # "mac_port_status": {
            m = p2_2.match(line)
            if m:
                group = m.groupdict()
                if multiport_flag == 1:
                    curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mac_port_status', {})
                else:
                    curr_dict =  ret_dict.setdefault('mpp_port_detai1', {}).setdefault(port, {}).setdefault('mac_port_status', {})
                continue

            # "mib_counters": {
            m = p2_3.match(line)
            if m:
                group = m.groupdict()
                if multiport_flag == 1:
                    curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mib_counters', {})
                else:
                    curr_dict = ret_dict.setdefault('mpp_port_detai1', {}).setdefault(port, {}).setdefault('mib_counters', {})
                continue

            # "tx_mac_tc_fc_frames_ok": [
            m = p2_3_1.match(line)
            if m:
                index_flag  =  1
                group = m.groupdict()
                handle_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mib_counters', {})
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mib_counters', {}).setdefault('tx_mac_tc_fc_frames_ok', {})
                continue

            # "tx_xoff_state_duration": [
            m = p2_3_2.match(line)
            if m:
                index_flag  =  1
                group = m.groupdict()
                handle_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mib_counters', {})
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mib_counters', {}).setdefault('tx_xoff_state_duration', {})
                continue

            # "rx_mac_tc_fc_frames_ok": [
            m = p2_3_3.match(line)
            if m:
                index_flag  =  1
                group = m.groupdict()
                handle_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mib_counters', {})
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mib_counters', {}).setdefault('rx_mac_tc_fc_frames_ok', {})
                continue

            # "rx_xoff_state_duration": [
            m = p2_3_4.match(line)
            if m:
                index_flag  =  1
                group = m.groupdict()
                handle_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mib_counters', {})
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mib_counters', {}).setdefault('rx_xoff_state_duration', {})
                continue

            # "multiport_phy_0_0_36": {
            m = p3.match(line)
            if m:
                multiport_flag = 1
                group = m.groupdict()
                port  =  group['key']
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {})
                continue

            # "device_info": {
            m = p3_1.match(line)
            if  m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('device_info', {})
                continue

            # "serdes_0": {
            m = p3_1_1.match(line)
            if m:
                group = m.groupdict()
                curr_dict = curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mac_state_histogram', {}).setdefault('serdes_0', {})
                continue

            # "mac_port_config": {
            m = p3_2.match(line)
            if m:
                group = m.groupdict()
                if multiport_flag == 1:
                    curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mac_port_config', {})
                else:
                    curr_dict = ret_dict.setdefault('mpp_port_detai1', {}).setdefault(port, {}).setdefault('mac_port_config', {})
                continue

            # "serdes_info_36": {
            m = p3_2_1.match(line)
            if  m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mac_port_config', {}).setdefault('serdes_info', {})
                continue

            # am_lock": [
            m = p3_3_1.match(line)
            if m:
                index_flag  =  1
                group = m.groupdict()
                handle_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mac_port_status', {})
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mac_port_status', {}).setdefault('am_lock', {})
                continue

            # "mac_pcs_lane_mapping": [
            m = p3_3_2.match(line)
            if m:
                index_flag = 1
                group = m.groupdict()
                handle_dict  = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mac_port_status', {})
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mac_port_status', {}).setdefault('mac_pcs_lane_mapping', {})
                continue

            # "mac_port_soft_state": {
            m = p3_4.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mac_port_soft_state', {})
                continue

            # "test_mode": {
            m = p3_5.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('test_mode', {})
                continue

            # "state_transition_history": [
            m = p3_6.match(line)
            if m:
                group = m.groupdict()
                index_flag = 1
                if multiport_flag == 1:
                    curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('state_transition_history', {})
                else:
                    curr_dict = ret_dict.setdefault('mpp_port_detai1', {}).setdefault(port, {}).setdefault('state_transition_history', {})
                handle_dict  =  curr_dict
                continue

            # "serdes_parameters": {
            m = p3_7.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_parameters', {})
                continue

            # "index_0": {
            m = p3_7_1.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_parameters', {}).setdefault('index_0', {})
                continue

            # "serdes_config": {
            m = p3_8.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_config', {})
                continue

            #  "serdes_settings": [
            m = p3_8_1.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_config', {}).setdefault('serdes_settings', {})
                continue

            # "rx_settings": {
            m = p3_8_1_1.match(line)
            if  m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_config', {}).setdefault('serdes_settings', {}).setdefault('rx_settings', {})
                continue

            # "targ_shadow": [
            m = p3_8_1_1_1.match(line)
            if  m:
                group = m.groupdict()
                index_flag = 1
                handle_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_config', {}).setdefault('serdes_settings', {}).setdefault('rx_settings', {})
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_config', {}).setdefault('serdes_settings', {}).setdefault('rx_settings', {}).setdefault('targ_shadow', {})
                continue

            # "tx_settings": {
            m = p3_8_1_2.match(line)
            if  m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_config', {}).setdefault('serdes_settings', {}).setdefault('tx_settings', {})
                continue

            # "tx_fir": [
            m = p3_8_1_2_1.match(line)
            if  m:
                group = m.groupdict()
                index_flag = 1
                handle_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_config', {}).setdefault('serdes_settings', {}).setdefault('tx_settings', {})
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_config', {}).setdefault('serdes_settings', {}).setdefault('tx_settings', {}).setdefault('tx_fir', {})
                continue

            # "flow_chart_settings": {
            m = p3_8_1_3.match(line)
            if  m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_config', {}).setdefault('serdes_settings', {}).setdefault('flow_chart_settings', {})
                continue

            # "serdes_status": {
            m = p3_9.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_status', {})
                continue

            # "Firmware_Version": {
            m = p3_9_1.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_status', {}).setdefault('firmware_version', {})
                continue

            # "rx_status": [
            m = p3_9_2.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_status', {}).setdefault('rx_status', {})
                continue

            # "firs": [
            m = p3_9_2_1.match(line)
            if m:
                group = m.groupdict()
                index_flag = 1
                handle_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_status', {}).setdefault('rx_status', {})
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_status', {}).setdefault('rx_status', {}).setdefault('firs',{})
                continue

            # "fw_rx_status": [
            m = p3_9_3.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_status', {}).setdefault('fw_rx_status', {})
                continue

            # "fir_shadow": [
            m = p3_9_4.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_status', {}).setdefault('fir_shadow', {})
                continue

            # "eye_capture": {
            m = p3_10.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('eye_capture', {})
                continue

            # "veye_data": [
            m = p3_10_1.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('eye_capture', {}).setdefault('veye_data',{})
                continue

            # "veye_values": [
            m = p3_10_1_1.match(line)
            if m:
                group = m.groupdict()
                index_flag = 1
                handle_dict  = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('eye_capture', {}).setdefault('veye_data',{})
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('eye_capture', {}).setdefault('veye_data',{}).setdefault('veye_values', {})
                continue

            # "reg_dump": {
            m = p3_11.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('reg_dump', {})
                continue

            # "Quad_Reg": [
            m = p3_11_1.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('reg_dump', {}).setdefault('quad_reg',{})
                continue

            # "P_Reg": [
            m = p3_11_2.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('reg_dump', {}).setdefault('p_reg',{})
                continue

            # "S_reg": [
            m = p3_11_3.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('reg_dump', {}).setdefault('s_reg',{})
                continue

            # "RXDTOP": [
            m = p3_11_4.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('reg_dump', {}).setdefault('rxdtop',{})
                continue

            # "TXDTOP": [
            m = p3_11_5.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('reg_dump', {}).setdefault('txdtop',{})
                continue

            # "AutoNeg": [
            m = p3_11_6.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('reg_dump', {}).setdefault('autoneg',{})
                continue

            # "LinkTraining": [
            m = p3_11_7.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('reg_dump', {}).setdefault('linktraining',{})
                continue

            # "RX_STS": [
            m = p3_11_8.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('reg_dump', {}).setdefault('rx_sts',{})
                continue

            # "an_debug_1": [
            m = p3_11_9.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('reg_dump', {}).setdefault('an_debug_1',{})
                continue

            # ""an_debug_2": [
            m = p3_11_10.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('reg_dump', {}).setdefault('an_debug_2',{})
                continue

            # "lt_debug_1": [
            m = p3_11_11.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('reg_dump', {}).setdefault('lt_debug_1',{})
                continue

            # "lt_debug_2": [
            m = p3_11_12.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('reg_dump', {}).setdefault('lt_debug_2',{})
                continue

            # "mac_port_0_0_36.link_down_histogram": {
            m = p4.match(line)
            if  m:
                group = m.groupdict()
                port = group['key']
                curr_dict = ret_dict.setdefault('mac_port_link_down', {}).setdefault(group['key'], {})
                continue

            # "rx_deskew_fifo_overflow_count": [
            m = p4_1.match(line)
            if m:
                group = m.groupdict()
                index_flag = 1
                handle_dict = ret_dict.setdefault('mac_port_link_down', {}).setdefault(port, {})
                curr_dict = ret_dict.setdefault('mac_port_link_down', {}).setdefault(port, {}).setdefault('rx_deskew_fifo_overflow_count',{})
                continue

            # "rx_pma_sig_ok_loss_interrupt_register_count": [
            m = p4_2.match(line)
            if  m:
                group = m.groupdict()
                index_flag = 1
                handle_dict = ret_dict.setdefault('mac_port_link_down', {}).setdefault(port, {})
                curr_dict = ret_dict.setdefault('mac_port_link_down', {}).setdefault(port, {}).setdefault('rx_pma_sig_ok_loss_interrupt_register_count',{})
                continue

            # "mac_port_0_0_36.link_error_histogram": {
            m = p5.match(line)
            if  m:
                group = m.groupdict()
                port = group['key']
                curr_dict = ret_dict.setdefault('mac_port_link_error', {}).setdefault(group['key'], {})
                continue

            # "mac_port_0_0_36.link_debounce_state": {
            m = p6.match(line)
            if m:
                group = m.groupdict()
                port = group['key']
                curr_dict = ret_dict.setdefault('mac_port_link_debounce', {}).setdefault(group['key'], {})
                continue

            # Port = 40 Slot = 1 cmd = () rc = 0x16 reason = (null)
            m = p7.match(line)
            if  m:
                group = m.groupdict()
                ret_dict['port'] = int(group['port'])
                ret_dict['slot'] = int(group['slot'])
                ret_dict['cmd'] = group['cmd']
                ret_dict['rc'] = group['rc']
                ret_dict['reason'] = group['reason']
                continue

            # Port = 39 cmd = (prbs_stop unit 0 port 39 slot 1 serdes_level 1 polynomial 31) rc = 0x0 rsn = success
            m = p7_1.match(line)
            if  m:
                group = m.groupdict()
                ret_dict['port'] = int(group['port'])
                ret_dict['cmd'] = group['cmd']
                ret_dict['rc'] = group['rc']
                ret_dict['rsn'] = group['rsn']
                continue

            # "PRE_INIT": 0,
            m = p8.match(line)
            if m:
                group = m.groupdict()
                key = group['key'].lower()
                value = group['value'].strip(',').strip('"').strip()

                if value in {'{', '['}:
                    continue

                if key == 'new_state':
                    stat_cnt += 1
                    curr_dict = curr_dict.setdefault(stat_cnt, {})
                    curr_dict['state'] = value
                elif key == 'timestamp':
                    curr_dict['timestamp'] = value
                    curr_dict = handle_dict  # Reset to handle_dict for the next entry
                else:
                    try:
                        value = int(value)
                    except ValueError:
                        pass
                    curr_dict[key] = value

            # false
            m = p8_1.match(line)
            if  m:
                group = m.groupdict()
                cnt  = cnt + 1
                key = cnt
                try:
                    group['value'] = int(group['value'])
                except:
                    #If it is a word, do not convert it to int.
                    pass
                curr_dict.update({key: group['value']})
                continue

            # 64,
            m = p8_2.match(line)
            if m:
                group = m.groupdict()
                cnt  = cnt + 1
                key  = cnt
                group['value'] = int(group['value'])
                curr_dict.update({key: group['value']})
                continue

            # ],
            m = p8_3.match(line)
            if  m:
                if index_flag == 1:
                    curr_dict  = handle_dict
                    index_flag = 0
                    cnt = 0
                continue

        return ret_dict


class ShowPlatformHardwareFedSwitchActiveFwdAsicResourceTcamTableSghashSchema(MetaParser):
    """Schema for show platform hardware fed switch active fwd-asic resource tcam table sghash all"""

    schema = {
        'device_id': int,
        'total_entries': int,
        's_no': {
            Any(): {
                'sgt': int,
                'dgt': int,
                'monitor_mode': int,
                'acl_id': int,
                'ip_version': str
            }
        }
    }

class ShowPlatformHardwareFedSwitchActiveFwdAsicResourceTcamTableSghash(ShowPlatformHardwareFedSwitchActiveFwdAsicResourceTcamTableSghashSchema):
    """Parser for
    * 'show platform hardware fed switch active fwd-asic resource tcam table sghash all'
    * 'show platform hardware fed switch {switch_var} fwd-asic resource tcam table sghash asic_no {asic_no}'
    * 'show platform hardware fed switch {switch_var} fwd-asic insight sgmatrix({max_asic})'
    """

    cli_command = [
        "show platform hardware fed switch {switch_var} fwd-asic resource tcam table sghash all",
        "show platform hardware fed switch {switch_var} fwd-asic resource tcam table sghash asic_no {asic_no}",
        "show platform hardware fed switch {switch_var} fwd-asic insight sgmatrix({max_asic})"
    ]

    def cli(self, switch_var, max_asic=None, asic_no=None, output=None):
        if output is None:
            if asic_no is not None:
                cmd = self.cli_command[1].format(switch_var=switch_var, asic_no=asic_no)
            elif switch_var and max_asic:
                cmd = self.cli_command[2].format(switch_var=switch_var, max_asic=max_asic)
            else:
                cmd = self.cli_command[0].format(switch_var=switch_var)
            output = self.device.execute(cmd)

        ret_dict = {}

        # List of SG-ACL Matrix Cells for Device ID = 0
        p1 = re.compile(r'^.*List of SG-ACL Matrix Cells for Device ID = (?P<device_id>\d+).*$')

        # Total Entries: 7
        p2 = re.compile(r'^Total Entries: (?P<total_entries>\d+)$')

        # S_NO    SGT        DGT             Monitor Mode    ACL_ID     IP_version
        # 1       4          6               0               5          ipv4
        p3 = re.compile(r'^(?P<s_no>\d+)\s+(?P<sgt>\d+)\s+(?P<dgt>\d+)\s+(?P<monitor_mode>\d+)\s+(?P<acl_id>\d+)\s+(?P<ip_version>\w+)$')

        for line in output.splitlines():
            line = line.strip()

            # List of SG-ACL Matrix Cells for Device ID = 0
            m = p1.search(line)
            if m:
                ret_dict['device_id'] = int(m.group('device_id'))
                continue

            # Total Entries: 7
            m = p2.match(line)
            if m:
                ret_dict['total_entries'] = int(m.group('total_entries'))
                continue

            # S_NO    SGT        DGT             Monitor Mode    ACL_ID     IP_version
            # 1       4          6               0               5          ipv4
            m = p3.match(line)
            if m:
                group = m.groupdict()
                s_no = int(group["s_no"])
                sec_dict = ret_dict.setdefault('s_no', {}).setdefault(s_no, {})
                sec_dict["sgt"] = int(group["sgt"])
                sec_dict["dgt"] = int(group["dgt"])
                sec_dict["monitor_mode"] = int(group["monitor_mode"])
                sec_dict["acl_id"] = int(group["acl_id"])
                sec_dict["ip_version"] = group["ip_version"]
                continue

        return ret_dict


class ShowPlatformHardwareFedSwitchActiveFwdAsicInsightSdkObjectsSchema(MetaParser):
    """Schema for 'show platform hardware fed switch active fwd-asic insight sdk_objects'"""
    schema = {
        'sdk_objects': {
            Any(): {
                'cookie': str,
                'device_oid': str,
                'oid': str
            }
        }
    }

class ShowPlatformHardwareFedSwitchActiveFwdAsicInsightSdkObjects(ShowPlatformHardwareFedSwitchActiveFwdAsicInsightSdkObjectsSchema):
    """Parser for 'show platform hardware fed switch active fwd-asic insight sdk_objects'"""

    cli_command = "show platform hardware fed switch active fwd-asic insight sdk_objects({otype})"

    def cli(self, otype, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(otype=otype))

        # Initialize the parsed dictionary
        ret_dict = {}

        # - # 1
        p1 = re.compile(r'^- # (?P<object_id>\d+)$')

        # cookie: ''
        p2 = re.compile(r"^cookie:\s*'(?P<cookie>.*)'$")

        # device: =oref('device', oid=0x0)
        p3 = re.compile(r'^device: =oref\(\'device\', oid=(?P<device_oid>.*)\)$')

        # oid: =0x225
        p4 = re.compile(r'^oid: =(?P<oid>.*)$')

        for line in output.splitlines():
            line = line.strip()

            # - # 1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                result_dict=ret_dict.setdefault("sdk_objects", {}).setdefault(int(group['object_id']), {})
                continue

            # cookie: ''
            m = p2.match(line)
            if m:
                group = m.groupdict()
                result_dict['cookie'] = group['cookie']
                continue

            # device: =oref('device', oid=0x0)
            m = p3.match(line)
            if m:
                group = m.groupdict()
                result_dict['device_oid'] = group['device_oid']
                continue

            # oid: =0x226
            m = p4.match(line)
            if m:
                group = m.groupdict()
                result_dict['oid'] = group['oid']
                continue

        return ret_dict


class ShowPlatformHardwareFedSwitchActiveFwdAsicInsightSdkObjectSchema(MetaParser):
    """Schema for 'show platform hardware fed switch active fwd-asic insight sdk_object'"""
    schema = {
        'sdk_objects':{
            Optional('aggregation_mode'): str,
            'cookie': str,
            'device_oid': str,
            'oid': str,
            Optional('set_size'): str
            }
    }

class ShowPlatformHardwareFedSwitchActiveFwdAsicInsightSdkObject(ShowPlatformHardwareFedSwitchActiveFwdAsicInsightSdkObjectSchema):
    """Parser for 'show platform hardware fed switch active fwd-asic insight sdk_object'"""

    cli_command = "show platform hardware fed switch active fwd-asic insight sdk_object({otype})"

    def cli(self, otype, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(otype=otype))

        # Initialize the parsed dictionary
        ret_dict = {}

        # aggregation_mode: =0x0
        p1 = re.compile(r'^aggregation_mode: =(?P<aggregation_mode>.*)$')

        # cookie: ''
        p2 = re.compile(r"^cookie:\s*'(?P<cookie>.*)'$")

        # device: =oref('device', oid=0x0)
        p3 = re.compile(r'^device: =oref\(\'device\', oid=(?P<device_oid>.*)\)$')

        # oid: =0x225
        p4 = re.compile(r'^oid: =(?P<oid>.*)$')

        # set_size: =0x1
        p5 = re.compile(r'^set_size: =(?P<set_size>.*)$')

        for line in output.splitlines():
            line = line.strip()

            result_dict = ret_dict.setdefault("sdk_objects", {})

            # aggregation_mode: =0x0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                result_dict['aggregation_mode'] = group['aggregation_mode']
                continue

            # cookie: ''
            m = p2.match(line)
            if m:
                group = m.groupdict()
                result_dict['cookie'] = group['cookie']
                continue

            # device: =oref('device', oid=0x0)
            m = p3.match(line)
            if m:
                group = m.groupdict()
                result_dict['device_oid'] = group['device_oid']
                continue

            # oid: =0x226
            m = p4.match(line)
            if m:
                group = m.groupdict()
                result_dict['oid'] = group['oid']
                continue

            # set_size: =0x1
            m = p5.match(line)
            if m:
                group = m.groupdict()
                result_dict['set_size'] = group['set_size']
                continue

        return ret_dict


class ShowPlatformHardwareFedSwitchFwdAsicInsightIpv4SgtMappingSchema(MetaParser):
    """Schema for
    * 'show platform hardware fed switch {switch} fwd-asic insight ipv4_sgt_mapping({devid})'
    """
    schema = {
        'total_ipv4_sgt_em_entries': int,
        'total_ipv4_sgt_lpm_entries': int,
        Optional('entries'): list,
    }

class ShowPlatformHardwareFedSwitchFwdAsicInsightIpv4SgtMapping(ShowPlatformHardwareFedSwitchFwdAsicInsightIpv4SgtMappingSchema):
    """Parser for
    * 'show platform hardware fed switch {switch_var} fwd-asic insight ipv4_sgt_mapping({devid})'
    """

    cli_command = "show platform hardware fed switch {switch_var} fwd-asic insight ipv4_sgt_mapping({devid})"


    def cli(self, switch_var, devid, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch_var=switch_var, devid=devid))

        # Initialize the parsed dictionary
        parsed_dict = {}
        entries = []

        # Total IPv4-SGT EM entries = 4
        p1 = re.compile(r'^Total IPv4-SGT EM entries\s*=\s*(?P<total_ipv4_sgt_em_entries>\d+)$')

        # Total IPv4-SGT LPM entries = 3
        p2 = re.compile(r'^Total IPv4-SGT LPM entries\s*=\s*(?P<total_ipv4_sgt_lpm_entries>\d+)$')

        # SNo.   IPv4-ADDRESS   MASKLEN VRFID SGT   VALID
        # 0      30.0.0.2       32      0     4     1
        p3 = re.compile(r'^(?P<sno>\d+)\s+(?P<ipv4_address>\S+)\s+(?P<masklen>\d+)\s+(?P<vrfid>\d+)\s+(?P<sgt>\d+)\s+(?P<valid>\d+)$')

        # Process each line of the output
        for line in output.splitlines():
            line = line.strip()

            # Total IPv4-SGT EM entries = 4
            m = p1.match(line)
            if m:
                parsed_dict['total_ipv4_sgt_em_entries'] = int(m.group('total_ipv4_sgt_em_entries'))
                continue

            # Total IPv4-SGT LPM entries = 3
            m = p2.match(line)
            if m:
                parsed_dict['total_ipv4_sgt_lpm_entries'] = int(m.group('total_ipv4_sgt_lpm_entries'))
                continue

            # SNo.   IPv4-ADDRESS   MASKLEN VRFID SGT   VALID
            # 0      30.0.0.2       32      0     4     1
            m = p3.match(line)
            if m:
                entries.append({
                    'sno': int(m.group('sno')),
                    'ipv4_address': m.group('ipv4_address'),
                    'masklen': int(m.group('masklen')),
                    'vrfid': int(m.group('vrfid')),
                    'sgt': int(m.group('sgt')),
                    'valid': int(m.group('valid'))
                })
                continue

        if entries:
            parsed_dict['entries'] = entries

        return parsed_dict


class ShowPlatformHardwareFedSwitchFwdAsicInsightIpv6SgtMappingSchema(MetaParser):
    """Schema for
    * 'show platform hardware fed switch {switch} fwd-asic insight ipv6_sgt_mapping({devid})'
    """

    schema = {
        'total_ipv6_sgt_em_entries': int,
        'total_ipv6_sgt_lpm_entries': int,
        Optional('entries'): list
    }

class ShowPlatformHardwareFedSwitchFwdAsicInsightIpv6SgtMapping(ShowPlatformHardwareFedSwitchFwdAsicInsightIpv6SgtMappingSchema):
    """Parser for
    * 'show platform hardware fed switch {switch_var} fwd-asic insight ipv6_sgt_mapping({devid})'
    """

    cli_command = 'show platform hardware fed switch {switch_var} fwd-asic insight ipv6_sgt_mapping({devid})'

    def cli(self, switch_var, devid, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch_var=switch_var, devid=devid))

        # Initialize the parsed dictionary
        parsed_dict = {}
        entries = []

        # Total IPv6-SGT EM entries = 2
        p1 = re.compile(r'^Total IPv6-SGT EM entries\s*=\s*(?P<total_ipv6_sgt_em_entries>\d+)$')

        # Total IPv6-SGT LPM entries = 4
        p2 = re.compile(r'^Total IPv6-SGT LPM entries\s*=\s*(?P<total_ipv6_sgt_lpm_entries>\d+)$')

        # SNo.   IPv6-ADDRESS  MASKLEN VRFID SGT   VALID
        # 0      30::2          128     0     40002 1
        p3 = re.compile(r'^(?P<sno>\d+)\s+(?P<ipv6_address>[0-9a-fA-F:.]+)\s+(?P<masklen>\d+)\s+(?P<vrfid>\d+)\s+(?P<sgt>\d+)\s+(?P<valid>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Total IPv6-SGT EM entries = 2
            m = p1.match(line)
            if m:
                parsed_dict['total_ipv6_sgt_em_entries'] = int(m.group('total_ipv6_sgt_em_entries'))
                continue

            # Total IPv6-SGT LPM entries = 4
            m = p2.match(line)
            if m:
                parsed_dict['total_ipv6_sgt_lpm_entries'] = int(m.group('total_ipv6_sgt_lpm_entries'))
                continue

            # SNo.   IPv6-ADDRESS    MASKLEN VRFID SGT   VALID
            # 0      30::2           128     0     40002 1
            m = p3.match(line)
            if m:
                entries.append({
                    'sno': int(m.group('sno')),
                    'ipv6_address': m.group('ipv6_address'),
                    'masklen': int(m.group('masklen')),
                    'vrfid': int(m.group('vrfid')),
                    'sgt': int(m.group('sgt')),
                    'valid': int(m.group('valid'))
                })
                continue

        if entries:
            parsed_dict['entries'] = entries

        return parsed_dict


class ShowPlatformHardwareFedSwitchFwdAsicInsightIpSourceGuardDefSchema(MetaParser):
    """Schema for 'show platform hardware fed switch {switch} fwd-asic insight ip_source_guard_def'"""
    schema = {
        'acl_entries':{
            'acl_oid': int,
            'acl_key_profile_oid': int,
            'acl_match_key_fields': ListOf(str),
            'acl_cmd_profile_oid': int,
            'acl_commands': ListOf(str)
        }
    }

class ShowPlatformHardwareFedSwitchFwdAsicInsightIpSourceGuardDef(ShowPlatformHardwareFedSwitchFwdAsicInsightIpSourceGuardDefSchema):
    """Parser for 'show platform hardware fed switch {switch} fwd-asic insight ip_source_guard_def'"""

    cli_command = [
        'show platform hardware fed switch {switch} fwd-asic insight ip_source_guard_def',
        'show platform hardware fed switch {switch} fwd-asic insight ip_source_guard_def({devid})'
    ]

    def cli(self, switch, devid=None, output=None):
        if output is None:
            if devid is not None:
                output = self.device.execute(self.cli_command[1].format(devid=devid,switch=switch))
            else:
                output = self.device.execute(self.cli_command[0].format(switch=switch))

        # Initialize the parsed dictionary
        ret_dict = {}

        #| 1358    | 1115                | SA                   | 1357                | IPSG_VIOLATION_DROP   |
        p1 = re.compile(r'^\|\s+(?P<acl_oid>\d+)\s+\|\s+(?P<acl_key_profile_oid>\d+)\s+\|\s+(?P<acl_match_key_fields>.+?)\s+\|\s+(?P<acl_cmd_profile_oid>\d+)\s+\|\s+(?P<acl_commands>.+?)\s+\|$')

        #|         |                     | VLAN_OUTER           |                     | FORCE_TRAP_WITH_EVENT |
        p2 = re.compile(r'^\|\s+\|\s+\|(?P<acl_match_key_fields>.+?)\s+\|\s+\|\s+(?P<acl_commands>.+?)\s+\|')


        for line in output.splitlines():
            line = line.strip()

            # | 1358    | 1115                | SA                   | 1357                | IPSG_VIOLATION_DROP   |
            m = p1.match(line)
            if m:
                group = m.groupdict()
                result_dict = ret_dict.setdefault("acl_entries",{})
                result_dict['acl_oid']= int(group['acl_oid'])
                result_dict['acl_key_profile_oid']= int(group['acl_key_profile_oid'])
                result_dict['acl_match_key_fields']= [group['acl_match_key_fields']]
                result_dict['acl_cmd_profile_oid']= int(group['acl_cmd_profile_oid'])
                result_dict['acl_commands']= [group['acl_commands']]
                continue

            # |         |                     | VRF_GID              |                     | COUNTER               |
            m = p2.match(line)
            if m :
                group = m.groupdict()
                result_dict['acl_match_key_fields'].append(group['acl_match_key_fields'])
                result_dict['acl_commands'].append(group['acl_commands'])
                continue

        return ret_dict


class ShowPlatformHardwareFedSwitchFwdAsicInsightIpSourceGuardAclSchema(MetaParser):
    """Schema for 'show platform hardware fed switch {switch} fwd-asic insight ip_source_guard_acl'"""
    schema = {
        'acl_entries': {
            'priority': {
                Any(): {
                    'ssp': str,
                    'ipv4_sip': str,
                    'source_mac': str,
                    'vlan': str,
                    'protocol': str,
                    'dport': str,
                    'sport': str,
                    'drop': str,
                    'hit_count': str,
                    'counter_oid': str,
                    Optional('ipv4_sip_mask'): str,
                    Optional('source_mac_mask'): str
                }
            }
        }
    }

class ShowPlatformHardwareFedSwitchFwdAsicInsightIpSourceGuardAcl(ShowPlatformHardwareFedSwitchFwdAsicInsightIpSourceGuardAclSchema):
    """Parser for 'show platform hardware fed switch {switch} fwd-asic insight ip_source_guard_acl'"""

    cli_command = [
        'show platform hardware fed switch {switch} fwd-asic insight ip_source_guard_acl',
        'show platform hardware fed switch {switch} fwd-asic insight ip_source_guard_acl({devid})'
    ]

    def cli(self, switch, devid=None, output=None):
        if output is None:
            if devid is not None:
                output = self.device.execute(self.cli_command[1].format(devid=devid, switch=switch))
            else:
                output = self.device.execute(self.cli_command[0].format(switch=switch))

        # Initialize the parsed dictionary
        ret_dict = {}

        # +----------+-----+------------------------+--------------------------+------+----------+-------+-------+------+-----------+-------------+
        # | Priority | SSP | IPV4 SIP               | Source mac               | Vlan | Protocol | DPort | SPort | Drop | Hit count | Counter oid |
        # +----------+-----+------------------------+--------------------------+------+----------+-------+-------+------+-----------+-------------+
        # | 0        |     |                        |                          |      | 17       | 67    | 68    |      | 18        | 1359        |
        p1 = re.compile(r'^\|\s+(?P<priority>\d+)\s+\|\s+(?P<ssp>\S*)\s+\|\s+(?P<ipv4_sip>\S*)\s+\|\s+(?P<source_mac>\S*)\s+\|\s+(?P<vlan>\S*)\s+\|\s+(?P<protocol>\S*)\s+\|\s+(?P<dport>\S*)\s+\|\s+(?P<sport>\S*)\s+\|\s+(?P<drop>\S*)\s+\|\s+(?P<hit_count>\d+)\s+\|\s+(?P<counter_oid>\d+)\s+\|$')

        # | 3        | 60  | IP   : 30.0.0.2        | Mac  : 00:12:01:00:00:01 | 30   |          |       |       |      | 0         | 2479        |
        p1_1 = re.compile(r'^\|\s+(?P<priority>\d+)\s+\|\s+(?P<ssp>\S*)\s+\|\s+IP\s*:\s*(?P<ipv4_sip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\|\s+Mac\s*:\s*(?P<source_mac>[\w:]+)\s+\|\s+(?P<vlan>\S*)\s+\|\s+(?P<protocol>\S*)\s+\|\s+(?P<dport>\S*)\s+\|\s+(?P<sport>\S*)\s+\|\s+(?P<drop>\S*)\s+\|\s+(?P<hit_count>\d+)\s+\|\s+(?P<counter_oid>\d+)\s+\|$')

        # |          |     | Mask : 255.255.255.255 | Mask : ff:ff:ff:ff:ff:ff |      |          |       |       |      |           |             |
        p1_2 = re.compile(r'^\|\s+\|\s+\|\s+Mask\s*:\s*(?P<ipv4_sip_mask>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\|\s+Mask\s*:\s*(?P<source_mac_mask>[\w:]+)\s+\|')

        current_priority = None

        for line in output.splitlines():
            line = line.strip()

            # Match the main ACL entry line
            m = p1.match(line)
            if m:
                group = m.groupdict()
                current_priority = int(group["priority"])
                result_dict = ret_dict.setdefault("acl_entries", {}).setdefault("priority", {}).setdefault(current_priority, {})
                result_dict['ssp'] = group['ssp']
                result_dict['ipv4_sip'] = group['ipv4_sip']
                result_dict['source_mac'] = group['source_mac']
                result_dict['vlan'] = group['vlan']
                result_dict['protocol'] = group['protocol']
                result_dict['dport'] = group['dport']
                result_dict['sport'] = group['sport']
                result_dict['drop'] = group['drop']
                result_dict['hit_count'] = group['hit_count']
                result_dict['counter_oid'] = group['counter_oid']
                continue

            # Match the detailed ACL entry line with IP and MAC
            m = p1_1.match(line)
            if m:
                group = m.groupdict()
                current_priority = int(group["priority"])
                result_dict = ret_dict.setdefault("acl_entries", {}).setdefault("priority", {}).setdefault(current_priority, {})
                result_dict['ssp'] = group['ssp']
                result_dict['ipv4_sip'] = group['ipv4_sip']
                result_dict['source_mac'] = group['source_mac']
                result_dict['vlan'] = group['vlan']
                result_dict['protocol'] = group['protocol']
                result_dict['dport'] = group['dport']
                result_dict['sport'] = group['sport']
                result_dict['drop'] = group['drop']
                result_dict['hit_count'] = group['hit_count']
                result_dict['counter_oid'] = group['counter_oid']
                continue

            # Match the mask line
            m = p1_2.match(line)
            if m and current_priority is not None:
                group = m.groupdict()
                result_dict = ret_dict["acl_entries"]["priority"][current_priority]
                result_dict['ipv4_sip_mask'] = group['ipv4_sip_mask']
                result_dict['source_mac_mask'] = group['source_mac_mask']
                continue

        return ret_dict


class ShowPlatformHardwareFedSwitchActiveFwdAsicInsightS1SgtMappingStatusV4Schema(MetaParser):
    """Schema for
    * 'show platform hardware fed switch {switch} fwd-asic insight s1_sgt_mapping_status_v4({devid})'
    """

    schema = {
        'sgt': {
            Any(): {
                'ip_address': str,
                'ip_version': int,
                'vrf_gid': int,
                'vrf_cookie': str
            }
        }
    }

class ShowPlatformHardwareFedSwitchActiveFwdAsicInsightS1SgtMappingStatusV4(ShowPlatformHardwareFedSwitchActiveFwdAsicInsightS1SgtMappingStatusV4Schema):
    """Parser for
    * 'show platform hardware fed switch {switch} fwd-asic insight s1_sgt_mapping_status_v4({devid})'
    """

    cli_command = 'show platform hardware fed switch {switch} fwd-asic insight s1_sgt_mapping_status_v4({devid})'

    def cli(self, switch, devid, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch=switch, devid=devid))

        # Initialize the parsed dictionary
        ret_dict = {}

        # | SGT | IP address  | IP version | VRF gid | VRF cookie |
        # | 20  | 20.0.0.2/32 | 4          | 0       |            |
        p1 = re.compile(r'^\|\s*(?P<sgt>\d+)\s*\|\s*(?P<ip_address>[0-9a-fA-F:.\/]+)\s*\|\s*(?P<ip_version>\d+)\s*\|\s*(?P<vrf_gid>\d+)\s*\|\s*(?P<vrf_cookie>.*?)\s*\|$')

        for line in output.splitlines():
            line = line.strip()

            # | SGT | IP address  | IP version | VRF gid | VRF cookie |
            # | 20  | 20.0.0.2/32 | 4          | 0       |            |
            m = p1.match(line)
            if m:
                group = m.groupdict()
                result_dict = ret_dict.setdefault('sgt', {}).setdefault(int(group['sgt']), {})
                result_dict['ip_address'] = group['ip_address']
                result_dict['ip_version'] = int(group['ip_version'])
                result_dict['vrf_gid'] = int(group['vrf_gid'])
                result_dict['vrf_cookie'] = group['vrf_cookie'].strip()

        return ret_dict


class ShowPlatformHardwareFedSwitchActiveFwdAsicInsightS1SgtMappingStatusV6Schema(MetaParser):
    """Schema for
    'show platform hardware fed switch {switch} fwd-asic insight s1_sgt_mapping_status_v6({devid})'
    """

    schema = {
        'sgt': {
            Any(): ListOf({
                'ip_address': str,
                'ip_version': int,
                'vrf_gid': int,
                'vrf_cookie': str
            })
        }
    }

class ShowPlatformHardwareFedSwitchActiveFwdAsicInsightS1SgtMappingStatusV6(ShowPlatformHardwareFedSwitchActiveFwdAsicInsightS1SgtMappingStatusV6Schema):
    """Parser for
    * 'show platform hardware fed switch {switch} fwd-asic insight s1_sgt_mapping_status_v6({devid})'
    """

    cli_command = 'show platform hardware fed switch {switch} fwd-asic insight s1_sgt_mapping_status_v6({devid})'

    def cli(self, switch, devid, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch=switch, devid=devid))

        # Initialize the parsed dictionary
        ret_dict = {}

        # | SGT | IP address   | IP version | VRF gid | VRF cookie |
        # | 10  | 10:10::2/128 | 6          | 0       |            |
        p1 = re.compile(r'^\|\s*(?P<sgt>\d+)\s*\|\s*(?P<ip_address>[0-9a-fA-F:.\/]+)\s*\|\s*(?P<ip_version>\d+)\s*\|\s*(?P<vrf_gid>\d+)\s*\|\s*(?P<vrf_cookie>.*?)\s*\|$')

        for line in output.splitlines():
            line = line.strip()

            # | SGT | IP address   | IP version | VRF gid | VRF cookie |
            # | 10  | 10:10::2/128 | 6          | 0       |            |
            m = p1.match(line)
            if m:
                group = m.groupdict()
                sgt = int(group['sgt'])
                sgt_list = ret_dict.setdefault('sgt', {}).setdefault(sgt, [])
                sgt_list.append({
                    'ip_address': group['ip_address'],
                    'ip_version': int(group['ip_version']),
                    'vrf_gid': int(group['vrf_gid']),
                    'vrf_cookie': group['vrf_cookie'].strip()
                })

        return ret_dict


class ShowPlatformHardwareFedSwitchActiveFwdAsicInsightS1SecGroupsMatrixMapStatusSchema(MetaParser):
    """Schema for 'show platform hardware fed switch active fwd-asic insight s1_sec_groups_matrix_map_status({devid})'"""
    schema = {
        'sec_groups_matrix_map_status': {
            Any(): {
                'sgt': int,
                'dgt': int,
                'ip_version': str,
                'monitor_mode': bool,
                'bincode': int,
                'acl_oid': int,
                'acl_cookie': str,
                'cell_counter_oid': int,
                'permit_counter': int,
                'deny_counter': int
            }
        }
    }

class ShowPlatformHardwareFedSwitchActiveFwdAsicInsightS1SecGroupsMatrixMapStatus(ShowPlatformHardwareFedSwitchActiveFwdAsicInsightS1SecGroupsMatrixMapStatusSchema):
    """Parser for 'show platform hardware fed switch active fwd-asic insight s1_sec_groups_matrix_map_status({devid})'"""

    cli_command = "show platform hardware fed switch {switch} fwd-asic insight s1_sec_groups_matrix_map_status({devid})"

    def cli(self, switch, devid, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch=switch, devid=devid))

        # Initialize the parsed dictionary
        ret_dict = {}

        # R| 65535 | 65534 | IPV4       | True         | 1       | 2000    |            | 1999             | 0              | 0            |
        p1 = re.compile(r'^\|\s*(?P<sgt>\d+)\s*\|\s*(?P<dgt>\d+)\s*\|\s*(?P<ip_version>\S+)\s*\|\s*(?P<monitor_mode>\S+)\s*\|\s*(?P<bincode>\d+)\s*\|\s*(?P<acl_oid>\d+)\s*\|\s*(?P<acl_cookie>\S*)\s*\|\s*(?P<cell_counter_oid>\d+)\s*\|\s*(?P<permit_counter>\d+)\s*\|\s*(?P<deny_counter>\d+)\s*\|$')

        for line in output.splitlines():
            line = line.strip()

            # Match the table rows
            # | 65535 | 65534 | IPV4       | True         | 1       | 2000    |            | 1999             | 0              | 0            |
            m = p1.match(line)
            if m:
                group = m.groupdict()
                entry = {
                    'sgt': int(group['sgt']),
                    'dgt': int(group['dgt']),
                    'ip_version': group['ip_version'],
                    'monitor_mode': group['monitor_mode'].lower() == 'true',
                    'bincode': int(group['bincode']),
                    'acl_oid': int(group['acl_oid']),
                    'acl_cookie': group['acl_cookie'],
                    'cell_counter_oid': int(group['cell_counter_oid']),
                    'permit_counter': int(group['permit_counter']),
                    'deny_counter': int(group['deny_counter'])
                }
                ret_dict.setdefault('sec_groups_matrix_map_status', {}).setdefault(f"{group['sgt']}_{group['dgt']}_{group['ip_version']}", entry)
                continue

        return ret_dict


class ShowPlatformHardwareFedSwitchActiveFwdAsicInsightL2MirrorCommandErspanSchema(MetaParser):
    """Schema for:
        show platform hardware fed switch active fwd-asic insight l2_mirror_command_erspan({mirror_gid})
    """
    schema = {
        'l2_mirror_command_erspan': {
            'mirror_gid': {
                Any(): {
                    'dest_port_tc': int,
                    'dest_port_gid': int,
                    'probability': float,
                    'source_mac': str,
                    'dest_mac': str,
                    'vlan_tag': int,
                    'source_ip': str,
                    'dest_ip': str,
                    'dest_port': int,
                    'ttl': int,
                    'counter_data': list
                }
            }
        }
    }

class ShowPlatformHardwareFedSwitchActiveFwdAsicInsightL2MirrorCommandErspan(ShowPlatformHardwareFedSwitchActiveFwdAsicInsightL2MirrorCommandErspanSchema):
    cli_command = "show platform hardware fed switch active fwd-asic insight l2_mirror_command_erspan({mirror_gid})"

    def cli(self, mirror_gid, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(mirror_gid=mirror_gid))

        ret_dict = {}

        # +------------+--------------+---------------+-------------+-------------------+-------------------+----------+-----------+---------+-----------+-----+-----------------+
        # | Mirror GID | Dest port TC | Dest port GID | Probability |     Source Mac    |      Dest Mac     | Vlan Tag | Source Ip | Dest Ip | Dest port | TTL |   Counter Data  |
        # +------------+--------------+---------------+-------------+-------------------+-------------------+----------+-----------+---------+-----------+-----+-----------------+
        # |          2 |            1 |            10 |         1.0 | 6c:b2:ae:4a:90:c5 | 4e:41:50:00:01:14 |        1 |  4.4.4.1  | 4.4.4.2 |     29130 | 255 | [10000,1180000] |
        # |            |              |               |             |                   |                   |          |           |         |           |     |                 |
        # +------------+--------------+---------------+-------------+-------------------+-------------------+----------+-----------+---------+-----------+-----+-----------------+
        p1 = re.compile(
            r"^\|\s*(?P<mirror_gid>\d+)\s*\|\s*(?P<dest_port_tc>\d+)\s*\|\s*"
            r"(?P<dest_port_gid>\d+)\s*\|\s*(?P<probability>[\d.]+)\s*\|\s*"
            r"(?P<source_mac>[\da-fA-F:]+)\s*\|\s*(?P<dest_mac>[\da-fA-F:]+)\s*\|\s*"
            r"(?P<vlan_tag>\d+)\s*\|\s*(?P<source_ip>[\d.]+)\s*\|\s*(?P<dest_ip>[\d.]+)\s*"
            r"\|\s*(?P<dest_port>\d+)\s*\|\s*(?P<ttl>\d+)\s*\|\s*(?P<counter_data>\[.*?\])\s*\|$"
        )

        for line in output.splitlines():
            line = line.strip()

            # +------------+--------------+---------------+-------------+-------------------+-------------------+----------+-----------+---------+-----------+-----+-----------------+
            # | Mirror GID | Dest port TC | Dest port GID | Probability |     Source Mac    |      Dest Mac     | Vlan Tag | Source Ip | Dest Ip | Dest port | TTL |   Counter Data  |
            # +------------+--------------+---------------+-------------+-------------------+-------------------+----------+-----------+---------+-----------+-----+-----------------+
            # |          2 |            1 |            10 |         1.0 | 6c:b2:ae:4a:90:c5 | 4e:41:50:00:01:14 |        1 |  4.4.4.1  | 4.4.4.2 |     29130 | 255 | [10000,1180000] |
            # |            |              |               |             |                   |                   |          |           |         |           |     |                 |
            # +------------+--------------+---------------+-------------+-------------------+-------------------+----------+-----------+---------+-----------+-----+-----------------+
            m = p1.match(line)
            if m:
                group = m.groupdict()
                mirror_dict = ret_dict.setdefault('l2_mirror_command_erspan', {}).setdefault('mirror_gid', {}).setdefault(int(group['mirror_gid']), {})
                mirror_dict['dest_port_tc'] = int(group['dest_port_tc'])
                mirror_dict['dest_port_gid'] = int(group['dest_port_gid'])
                mirror_dict['probability'] = float(group['probability'])
                mirror_dict['source_mac'] = group['source_mac']
                mirror_dict['dest_mac'] = group['dest_mac']
                mirror_dict['vlan_tag'] = int(group['vlan_tag'])
                mirror_dict['source_ip'] = group['source_ip']
                mirror_dict['dest_ip'] = group['dest_ip']
                mirror_dict['dest_port'] = int(group['dest_port'])
                mirror_dict['ttl'] = int(group['ttl'])
                mirror_dict['counter_data'] = eval(group['counter_data'])
                continue

        return ret_dict


class ShowPlatformHardwareFedSwitchActiveFwdAsicInsightL2MirrorCommandStatusSchema(MetaParser):
    """Schema for:
        show platform hardware fed switch active fwd-asic insight l2_mirror_command_status
    """
    schema = {
        'l2_mirror_command_status': {
            'mirror_gid': {
                Any(): {
                    'mirror_type': str,
                    'dest_port_gid': int,
                    'dest_port_tc': int,
                }
            }
        }
    }

class ShowPlatformHardwareFedSwitchActiveFwdAsicInsightL2MirrorCommandStatus(ShowPlatformHardwareFedSwitchActiveFwdAsicInsightL2MirrorCommandStatusSchema):
    """Parser for:
        show platform hardware fed switch active fwd-asic insight l2_mirror_command_status
    """

    cli_command = "show platform hardware fed switch active fwd-asic insight l2_mirror_command_status"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        ret_dict = {}

        # +------------+-------------+---------------+--------------+
        # | Mirror GID | Mirror Type | Dest port GID | Dest port TC |
        # +------------+-------------+---------------+--------------+
        # |         21 |      L2     |           260 |            2 |
        p1 = re.compile(r"^\|\s*(?P<mirror_gid>\d+)\s*\|\s*(?P<mirror_type>\S+)\s*\|\s*"
                        r"(?P<dest_port_gid>\d+)\s*\|\s*(?P<dest_port_tc>\d+)\s*\|$")

        for line in output.splitlines():
            line = line.strip()

            # +------------+-------------+---------------+--------------+
            # | Mirror GID | Mirror Type | Dest port GID | Dest port TC |
            # +------------+-------------+---------------+--------------+
            # |         21 |      L2     |           260 |            2 |
            m = p1.match(line)
            if m:
                group = m.groupdict()
                mirror_gid = int(group['mirror_gid'])
                mirror_dict = ret_dict.setdefault('l2_mirror_command_status', {}).setdefault('mirror_gid', {}).setdefault(mirror_gid, {})
                mirror_dict['mirror_type'] = group['mirror_type']
                mirror_dict['dest_port_gid'] = int(group['dest_port_gid'])
                mirror_dict['dest_port_tc'] = int(group['dest_port_tc'])
                continue

        return ret_dict


class ShowPlatformHardwareFedSwitchFwdAsicInsightL2mRoutesSchema(MetaParser):
    schema = {
        'l2m_routes': {
            'switch_gid': {
                int: {
                    'switch_cookie': int,
                    'ip_version': int,
                    'saddr': str,
                    'gaddr': str,
                    'l2_mcg_gid': int,
                    'l2_mcg_cookie': str,
                }
            }
        }
    }

class ShowPlatformHardwareFedSwitchFwdAsicInsightL2mRoutes(ShowPlatformHardwareFedSwitchFwdAsicInsightL2mRoutesSchema):
    cli_command = "show platform hardware fed switch {switch_id} fwd-asic insight l2m_routes({switch_gid})"

    def cli(self, switch_id, switch_gid, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch_id=switch_id, switch_gid=switch_gid))

        ret_dict = {}

        # +------------+---------------+------------+-----------------------------------------+------------+------------+----------------+
        # | switch-gid | switch-cookie | ip-version | saddr                                   | gaddr      | l2-mcg-gid | l2-mcg-cookie  |
        # +------------+---------------+------------+-----------------------------------------+------------+------------+----------------+
        # | 100        |      100      | 6          | ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff | ff1e::21:1 | 8271       | urid:0x20::657 |
        # |            |               |            |                                         |            |            |                |
        # +------------+---------------+------------+-----------------------------------------+------------+------------+----------------+
        p1 = re.compile(
            r"^\|\s*(?P<switch_gid>\d+)\s*\|\s*(?P<switch_cookie>\d+)\s*\|\s*(?P<ip_version>\d+)\s*\|\s*"
            r"(?P<saddr>[\da-fA-F:]+)\s*\|\s*(?P<gaddr>[\da-fA-F:]+)\s*\|\s*(?P<l2_mcg_gid>\d+)\s*\|\s*"
            r"(?P<l2_mcg_cookie>[\w:]+)\s*\|$"
        )

        for line in output.splitlines():
            line = line.strip()
            # +------------+---------------+------------+-----------------------------------------+------------+------------+----------------+
            # | switch-gid | switch-cookie | ip-version | saddr                                   | gaddr      | l2-mcg-gid | l2-mcg-cookie  |
            # +------------+---------------+------------+-----------------------------------------+------------+------------+----------------+
            # | 100        |      100      | 6          | ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff | ff1e::21:1 | 8271       | urid:0x20::657 |
            # |            |               |            |                                         |            |            |                |
            # +------------+---------------+------------+-----------------------------------------+------------+------------+----------------+
            m = p1.match(line)
            if m:
                group = m.groupdict()
                switch_dict = ret_dict.setdefault('l2m_routes', {}).setdefault('switch_gid', {}).setdefault(int(group['switch_gid']), {})
                switch_dict['switch_cookie'] = int(group['switch_cookie'])
                switch_dict['ip_version'] = int(group['ip_version'])
                switch_dict['saddr'] = group['saddr']
                switch_dict['gaddr'] = group['gaddr']
                switch_dict['l2_mcg_gid'] = int(group['l2_mcg_gid'])
                switch_dict['l2_mcg_cookie'] = group['l2_mcg_cookie']
                continue

        return ret_dict


class ShowPlatformHardwareFedSwitchFwdAsicInsightL2mGroupsSchema(MetaParser):
    schema = {
        'l2m_groups': {
            'l2_mcg_gid': {
                int: {
                    'l2_mcg_cookie': str,
                    'num_members': int,
                    'replication_paradigm': str,
                    'egress_counter_id': int,
                    'egress_counter_data': list,
                }
            }
        }
    }


class ShowPlatformHardwareFedSwitchFwdAsicInsightL2mGroups(ShowPlatformHardwareFedSwitchFwdAsicInsightL2mGroupsSchema):
    cli_command = "show platform hardware fed switch {switch_id} fwd-asic insight l2m_groups({l2_mcg_gid})"

    def cli(self, switch_id, l2_mcg_gid, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch_id=switch_id, l2_mcg_gid=l2_mcg_gid))

        ret_dict = {}

        # +------------+----------------+-------------+----------------------+-------------------+---------------------+
        # | l2-mcg-gid | l2-mcg-cookie  | num-members | replication-paradigm | egress-counter-id | egress-counter-data |
        # +------------+----------------+-------------+----------------------+-------------------+---------------------+
        # | 8271       | urid:0x20::657 | 1           |        EGRESS        | 0                 | [0,0]               |
        # |            |                |             |                      |                   |                     |
        # +------------+----------------+-------------+----------------------+-------------------+---------------------+
        p1 = re.compile(
            r"^\|\s*(?P<l2_mcg_gid>\d+)\s*\|\s*(?P<l2_mcg_cookie>[\w:]+)\s*\|\s*(?P<num_members>\d+)\s*\|\s*"
            r"(?P<replication_paradigm>\w+)\s*\|\s*(?P<egress_counter_id>\d+)\s*\|\s*(?P<egress_counter_data>\[.*?\])\s*\|$"
        )

        for line in output.splitlines():
            line = line.strip()

            # +------------+----------------+-------------+----------------------+-------------------+---------------------+
            # | l2-mcg-gid | l2-mcg-cookie  | num-members | replication-paradigm | egress-counter-id | egress-counter-data |
            # +------------+----------------+-------------+----------------------+-------------------+---------------------+
            # | 8271       | urid:0x20::657 | 1           |        EGRESS        | 0                 | [0,0]               |
            # |            |                |             |                      |                   |                     |
            # +------------+----------------+-------------+----------------------+-------------------+---------------------+
            m = p1.match(line)
            if m:
                group = m.groupdict()
                group_dict = ret_dict.setdefault('l2m_groups', {}).setdefault('l2_mcg_gid', {}).setdefault(int(group['l2_mcg_gid']), {})
                group_dict['l2_mcg_cookie'] = group['l2_mcg_cookie']
                group_dict['num_members'] = int(group['num_members'])
                group_dict['replication_paradigm'] = group['replication_paradigm']
                group_dict['egress_counter_id'] = int(group['egress_counter_id'])
                group_dict['egress_counter_data'] = eval(group['egress_counter_data'])
                continue

        return ret_dict


class ShowPlatformHardwareFedSwitchFwdAsicInsightIfmPortStatusSchema(MetaParser):
    """Schema for:
        show platform hardware fed switch {switch_id} fwd-asic insight ifm_port_status({system_port_gid})
    """

    schema = {
        'sysport': {
            Any(): {
                'sysport_gid': int,
                'port_type': str,
                'status': str,
                'mpp_port_id': int,
                'rx_fc_mode': str,
                'speed': float,
                'sysport_cookie': str,
                'tx_fc_mode': str,
                'port_status_info': {
                    'admin_state': str,
                    'fec_mode': str,
                    'loopback_mode': str,
                    'link_mgmt': str,
                    'prbs_mode': str,
                    'full_duplex': str,
                    'auto_neg': str,
                    'link_state': str,
                    'mtu': int
                },
                'serdes': str
            }
        }
    }

class ShowPlatformHardwareFedSwitchFwdAsicInsightIfmPortStatus(ShowPlatformHardwareFedSwitchFwdAsicInsightIfmPortStatusSchema):
    """Parser for:
       show platform hardware fed switch {switch_id} fwd-asic insight ifm_port_status({system_port_gid})
    """

    cli_command = "show platform hardware fed switch {switch_id} fwd-asic insight ifm_port_status({system_port_gid})"

    def cli(self, switch_id, system_port_gid, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch_id=switch_id,system_port_gid=system_port_gid))

        ret_dict = {}

        # | sysport_gid: 305        | port_type: MPP_PORT | status: EN-UP | mpp_port_id: 1 | rx_fc_mode: PAUSE | speed: 1.0          |
        p1 = re.compile(r'^\|\s*sysport_gid:\s*(?P<sysport_gid>\d+)\s*\|\s*port_type:\s*(?P<port_type>\S+)\s*\|\s*status:\s*(?P<status>\S+)\s*\|\s*mpp_port_id:\s*(?P<mpp_port_id>\d+)\s*\|\s*rx_fc_mode:\s*(?P<rx_fc_mode>\S+)\s*\|\s*speed:\s*(?P<speed>\d+\.\d+)\s*\|$')

        # | sysport_cookie: Gi2/0/9 |                     |               |                | tx_fc_mode: NONE  | admin_state: True   |
        p2 = re.compile(r'^\|\s*sysport_cookie:\s*(?P<sysport_cookie>\S+)\s*\|\s*\|\s*\|\s*\|\s*tx_fc_mode:\s*(?P<tx_fc_mode>\S+)\s*\|\s*(?P<feature>\S+):\s*(?P<value>\S+)\s*\|$')

        # | serdes:                 |                     |               |                |                   | fec_mode: NONE      |
        p3 = re.compile(r'^\|\s*serdes:\s*(?P<serdes>\S*)\s*\|\s*\|\s*\|\s*\|\s*\|\s*(?P<feature>\S+):\s*(?P<value>\S+)\s*\|$')

        # |                         |                     |               |                |                   | auto_neg: False     |
        # |                         |                     |               |                |                   | link_state: UP      |
        p4 = re.compile(r'^\|\s*\|\s*\|\s*\|\s*\|\s*\|\s*(?P<feature>\S+):\s*(?P<value>[A-Za-z]+)\s*\|$')

        # |                         |                     |               |                |                   | mtu: 1522           |
        p5 = re.compile(r'^\|\s*\|\s*\|\s*\|\s*\|\s*\|\s*(?P<feature>\S+):\s*(?P<value>\d+)\s*\|$')

        for line in output.splitlines():
            line = line.strip()

            # | sysport_gid: 305        | port_type: MPP_PORT | status: EN-UP | mpp_port_id: 1 | rx_fc_mode: PAUSE | speed: 1.0          |
            m = p1.match(line)
            if m:
                group = m.groupdict()
                sysport_gid = int(group['sysport_gid'])
                port_data = ret_dict.setdefault('sysport', {}).setdefault(sysport_gid, {})
                port_data.update({
                    'sysport_gid': sysport_gid,
                    'port_type': group['port_type'],
                    'status': group['status'],
                    'mpp_port_id': int(group['mpp_port_id']),
                    'rx_fc_mode': group['rx_fc_mode'],
                    'speed': float(group['speed'])
                })
                continue

            # | sysport_cookie: Gi2/0/9 |                     |               |                | tx_fc_mode: NONE  | admin_state: True   |
            m = p2.match(line)
            if m:
                group = m.groupdict()
                port_data['sysport_cookie'] = group['sysport_cookie']
                port_data['tx_fc_mode'] = group['tx_fc_mode']
                port_info = port_data.setdefault("port_status_info", {})
                port_info[group['feature']] = group['value']
                continue

            # | serdes:                 |                     |               |                |                   | fec_mode: NONE      |
            m = p3.match(line)
            if m:
                group = m.groupdict()
                port_data['serdes'] = group['serdes']
                port_info = port_data.setdefault("port_status_info", {})
                port_info[group['feature']] = group['value']
                continue

            # |                         |                     |               |                |                   | auto_neg: False     |
            # |                         |                     |               |                |                   | link_state: UP      |
            m = p4.match(line)
            if m:
                group = m.groupdict()
                port_info[group['feature']] = group['value']
                continue

            # |                         |                     |               |                |                   | mtu: 1522           |
            m = p5.match(line)
            if m:
                group = m.groupdict()
                port_info[group['feature']] = int(group['value'])
                continue

        return ret_dict


class ShowPlatformHardwareFedSwitchFwdAsicInsightPortSerdesStatusSchema(MetaParser):
    """Schema for:
        show platform hardware fed switch {switch_id} fwd-asic insight ifm_port_serdes_status({system_port_gid})
    """

    schema = {
        'port_info': {
            Any(): {
                'port_oid': int,
                'sysport_gid': int,
                'serdes': str,
                Optional('port_cookie'): Or(str, None),
                'lane_info': {
                    'speed': float,
                    'serdes_speed': float,
                    'serdes_tx_ready': str,
                    'serdes_rx_ready': str,
                    'signal_strength_type': str,
                    'signal_strength_val': float,
                    'rx_ffe_taps': str,
                    'lane': int,
                    'signal_ok': str
                }
            }
        }
    }

class ShowPlatformHardwareFedSwitchFwdAsicInsightPortSerdesStatus(ShowPlatformHardwareFedSwitchFwdAsicInsightPortSerdesStatusSchema):
    """Parser for:
        show platform hardware fed switch {switch_id} fwd-asic insight ifm_port_serdes_status({system_port_gid})
    """

    cli_command = "show platform hardware fed switch {switch_id} fwd-asic insight ifm_port_serdes_status({system_port_gid})"

    def cli(self, switch_id, system_port_gid, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch_id=switch_id, system_port_gid=system_port_gid))

        ret_dict = {}

        # | port_oid: 1910 |             | sysport_gid: 305 | serdes: 0/0/29-29 | speed: 1.0                       |
        p1 = re.compile(r'^\|\s*port_oid:\s*(?P<port_oid>\d+)\s*\|\s*(?P<port_cookie>\S*)\s*\|\s*sysport_gid:\s*(?P<sysport_gid>\d+)\s*\|\s*serdes:\s*(?P<serdes>\S+)\s*\|\s*(?P<lane>\S+):\s*(?P<value>\S+)\s*\|$')

        # |                |             |                  |                   | serdes_rx_ready: True            |
        # |                |             |                  |                   | signal_strength_type: SERDES_MSE |
        p2 = re.compile(r'^\|\s*\|\s*\|\s*\|\s*\|\s*(?P<lane>\S+):\s*(?P<value>[A-Za-z-_]+|N/A)\s*\|$')

        # |                |             |                  |                   | signal_strength_val: 184328.0    |
        # |                |             |                  |                   | rx_ffe_taps: N/A                 |
        p3 = re.compile(r'^\|\s*\|\s*\|\s*\|\s*\|\s*(?P<lane>\S+):\s*(?P<value>\d+\.\d+)\s*\|$')

        # |                |             |                  |                   | lane: 0                          |
        p4 = re.compile(r'^\|\s*\|\s*\|\s*\|\s*\|\s*(?P<lane>\S+):\s*(?P<value>\d+)\s*\|$')

        for line in output.splitlines():
            line = line.strip()

            # | port_oid: 1910 |             | sysport_gid: 305 | serdes: 0/0/29-29 | speed: 1.0                       |
            m = p1.match(line)
            if m:
                group = m.groupdict()
                port_oid = int(group['port_oid'])
                port_data = ret_dict.setdefault('port_info', {}).setdefault(port_oid, {})
                port_data.update({
                    'port_oid': int(group['port_oid']),
                    'sysport_gid': int(group['sysport_gid']),
                    'serdes': group['serdes'],
                    'port_cookie': group['port_cookie'] if group['port_cookie'] else None
                })

                lane_info = port_data.setdefault('lane_info', {})
                lane_info[group["lane"]] = float(group["value"]) if group["lane"] == "speed" else group["value"]
                continue

            # |                |             |                  |                   | serdes_rx_ready: True            |
            # |                |             |                  |                   | signal_strength_type: SERDES_MSE |
            m = p2.match(line)
            if m:
                group = m.groupdict()
                lane_info[group["lane"]] = group["value"]
                continue

            # |                |             |                  |                   | serdes_speed: 1.0                |
            # |                |             |                  |                   | signal_strength_val: 184328.0    |
            m = p3.match(line)
            if m:
                group = m.groupdict()
                lane_info[group["lane"]] = float(group["value"])
                continue

            # |                |             |                  |                   | lane: 0                          |
            m = p4.match(line)
            if m:
                group = m.groupdict()
                lane_info[group["lane"]] = int(group["value"])
                continue

        return ret_dict


class ShowPlatformHardwareFedSwitchFwdAsicInsightIfmPortAn37StatusSchema(MetaParser):
    """Schema for show platform hardware fed switch {switch_id} fwd-asic insight ifm_port_an37_status({system_port_gid})"""

    schema = {
        'port_info': {
            Any(): {
                'port_oid': int,
                'sysport_gid': int,
                'sysport_cookie': str,
                'serdes': str,
                'mpp_port_idx': int,
                'port_state': str,
                'an37_mode': str,
                'port_an37_info': {
                    'port_speed': float,
                    'full_duplex': str,
                    'rx_state': int,
                    'auto_neg_enabled': str,
                    'an_completed': str,
                    'link_status': str,
                    'tx_state': int,
                },
            }
        }
    }

class ShowPlatformHardwareFedSwitchFwdAsicInsightIfmPortAn37Status(ShowPlatformHardwareFedSwitchFwdAsicInsightIfmPortAn37StatusSchema):
    """Parser for show platform hardware fed switch {switch_id} fwd-asic insight ifm_port_an37_status({system_port_gid})"""

    cli_command = 'show platform hardware fed switch {switch_id} fwd-asic insight ifm_port_an37_status({system_port_gid})'

    def cli(self, switch_id, system_port_gid, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch_id=switch_id, system_port_gid=system_port_gid))

        parsed_data = {}

        # | port_oid: 1910 |             | sysport_gid: 305 | sysport_cookie: Gi2/0/9 | serdes: 0/0/29-29 | mpp_port_idx: 0 | port_state: LINK_UP | an37_mode: AN37_SGMII |     port_speed: 1.0     |
        p1 = re.compile(r'^\|\s*port_oid:\s*(?P<port_oid>\d+)\s*\|\s*\|\s*sysport_gid:\s*(?P<sysport_gid>\d+)\s*\|\s*sysport_cookie:\s*(?P<sysport_cookie>\S+)\s*\|\s*serdes:\s*(?P<serdes>\S+)\s*\|\s*mpp_port_idx:\s*(?P<mpp_port_idx>\d+)\s*\|\s*port_state:\s*(?P<port_state>\S+)\s*\|\s*an37_mode:\s*(?P<an37_mode>\S+)\s*\|\s*(?P<port_an37_info>\S+):\s*(?P<value>\S+)\s*\|$')

        # |                |             |                  |                         |                   |                 |                     |                       |    full_duplex: True    |
        # |                |             |                  |                         |                   |                 |                     |                       | auto_neg_enabled: False |
        p2 = re.compile(r'^\|\s*\|\s*\|\s*\|\s*\|\s*\|\s*\|\s*\|\s*\|\s*(?P<port_an37_info>\S+):\s*(?P<value>[A-Za-z-_]+)\s*\|$')

        # |                |             |                  |                         |                   |                 |                     |                       |       tx_state: 0       |
        p3 = re.compile(r'^\|\s*\|\s*\|\s*\|\s*\|\s*\|\s*\|\s*\|\s*\|\s*(?P<port_an37_info>\S+):\s*(?P<value>\d+)\s*\|$')

        # |                |             |                  |                         |                   |                 |                     |                       |       rx_state: 2       |
        # |                |             |                  |                         |                   |                 |                     |                       |       tx_state: 0       |
        p4 = re.compile(r'^\|\s*\|\s*\|\s*\|\s*\|\s*\|\s*\|\s*\|\s*\|\s*(?P<port_an37_info>\S+):\s*(?P<value>\d+\.\d+)\s*\|$')

        for line in output.splitlines():
            line = line.strip()

            # | port_oid: 1910 |             | sysport_gid: 305 | sysport_cookie: Gi2/0/9 | serdes: 0/0/29-29 | mpp_port_idx: 0 | port_state: LINK_UP | an37_mode: AN37_SGMII |     port_speed: 1.0     |
            m = p1.match(line)
            if m:
                group = m.groupdict()
                port_oid = int(group['port_oid'])
                port_data = parsed_data.setdefault('port_info', {}).setdefault(port_oid, {})

                port_data.update({
                    'port_oid': int(group['port_oid']),
                    'sysport_gid': int(group["sysport_gid"]),
                    'sysport_cookie': group['sysport_cookie'],
                    'serdes': group['serdes'],
                    'mpp_port_idx': int(group["mpp_port_idx"]),
                    'port_state': group['port_state'],
                    'an37_mode': group['an37_mode']
                })
                port_an37_info = port_data.setdefault('port_an37_info', {})
                port_an37_info[group["port_an37_info"]] = float(group["value"]) if group["port_an37_info"] == "port_speed" else group["value"]

                continue

            # |                |             |                  |                         |                   |                 |                     |                       |   an_completed: False   |
            # |                |             |                  |                         |                   |                 |                     |                       |     link_status: UP     |
            m = p2.match(line)
            if m:
                group = m.groupdict()
                port_an37_info[group["port_an37_info"]] = group["value"]
                continue

            # |                |             |                  |                         |                   |                 |                     |                       |       rx_state: 2       |
            # |                |             |                  |                         |                   |                 |                     |                       |       tx_state: 0       |
            m = p3.match(line)
            if m:
                group = m.groupdict()
                port_an37_info[group["port_an37_info"]] = int(group["value"])
                continue

            # |                |             |                  |                         |                   |                 |                     |                       |       port_speed: 1.0       |
            m = p4.match(line)
            if m:
                group = m.groupdict()
                port_an37_info[group["port_an37_info"]] = float(group["value"])
                continue

        return parsed_data


class ShowPlatformHardwareFedSwitchFwdAsicInsightIfmPortAnltStatusSchema(MetaParser):
    """Schema for show platform hardware fed switch {switch_id} fwd-asic insight ifm_port_anlt_status({system_port_gid})"""

    schema = {
        'port_info': {
            Any(): {
                'port_oid': int,
                'sysport_gid': int,
                'sysport_cookie': str,
                'serdes': str,
                'port_state': str,
                'auto_neg_enabled': str,
                'anlt_mode': str,
                'port_speed': float,
                'fec_mode': str
            }
        }
    }

class ShowPlatformHardwareFedSwitchFwdAsicInsightIfmPortAnltStatus(ShowPlatformHardwareFedSwitchFwdAsicInsightIfmPortAnltStatusSchema):
    """Parser for show platform hardware fed switch {switch_id} fwd-asic insight ifm_port_anlt_status({system_port_gid})"""

    cli_command = 'show platform hardware fed switch {switch_id} fwd-asic insight ifm_port_anlt_status({system_port_gid})'

    def cli(self, switch_id, system_port_gid, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch_id=switch_id, system_port_gid=system_port_gid))

        parsed_data = {}

        #|     1910 |             |         305 | Gi2/0/9        | 0/0/29-29 |  LINK_UP   |          False           |    NONE   |    1.0     |   NONE   |
        p1 = re.compile(r'^\S\s+(?P<port_oid>\d+)\s+\S\s+(?P<port_cookie>\S*)\s+\S\s+(?P<sysport_gid>\d+)\s+\S\s+(?P<sysport_cookie>\S+)\s+\S\s+(?P<serdes>\S+)\s+\S\s+(?P<port_state>\S+)\s+\S\s+(?P<auto_neg_enabled>\S+)\s+\S\s+(?P<anlt_mode>\S+)\s+\S\s+(?P<port_speed>\S+)\s+\S\s+(?P<fec_mode>\S+)\s+\S$')

        for line in output.splitlines():
            line = line.strip()

            # |     1910 |             |         305 | Gi2/0/9        | 0/0/29-29 |  LINK_UP   |          False           |    NONE   |    1.0     |   NONE   |
            m = p1.match(line)
            if m:
                group = m.groupdict()
                port_oid = int(group['port_oid'])
                port_data = parsed_data.setdefault('port_info', {}).setdefault(port_oid, {})

                port_data.update({
                    'port_oid': int(group['port_oid']),
                    'sysport_gid': int(group["sysport_gid"]),
                    'sysport_cookie': group['sysport_cookie'],
                    'serdes': group['serdes'],
                    'port_state': group['port_state'],
                    'auto_neg_enabled': group['auto_neg_enabled'],
                    'anlt_mode': group['anlt_mode'],
                    'port_speed': float(group['port_speed']),
                    'fec_mode': group['fec_mode']
                })
                continue

        return parsed_data


class ShowPlatformHardwareFedSwitch1FwdAsicInsightIfmLagMembersSchema(MetaParser):
    """Schema for 'show platform hardware fed switch {switch_id} fwd-asic insight ifm_lag_members({lag_gid})'"""
    schema = {
        'ifm_lag_members': {
            Any(): {
                'lag_gid': int,
                'member_index': int,
                'port_type': str,
                'port_id': int,
                'rx_enabled': str,
                'tx_enabled': str,
                'weight': float,
                'empty_lag_port': str,
                'sysport_detail': {
                    'sysport_gid': int,
                    'sysport_cookie': str,
                    'serdes': str
                }
            }
        }
    }

class ShowPlatformHardwareFedSwitch1FwdAsicInsightIfmLagMembers(ShowPlatformHardwareFedSwitch1FwdAsicInsightIfmLagMembersSchema):
    """Parser for 'show platform hardware fed switch {switch_id} fwd-asic insight ifm_lag_members({lag_gid})'"""

    cli_command = 'show platform hardware fed switch {switch_id} fwd-asic insight ifm_lag_members({lag_gid})'

    def cli(self, switch_id, lag_gid, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch_id=switch_id, lag_gid=lag_gid))

        parsed_data = {}

        # |      41 |      3       | MPP_PORT    |    2200 |    True    |    True    |  0.25  |     False      | {'sysport_gid': 85, 'sysport_cookie': 'Gi1/0/45', 'serdes': ''} |
        p1 = re.compile(r'^\S\s+(?P<lag_gid>\d+)\s+\S\s+(?P<member_index>\d+)\s+\S\s+(?P<port_type>\S+)\s+\S\s+(?P<port_id>\d+)\s+\S\s+(?P<rx_enabled>\S+)\s+\S\s+(?P<tx_enabled>\S+)\s+\S\s+(?P<weight>[\d\.]+)\s+\S\s+(?P<empty_lag_port>\S+)\s+\S\s+\S\S+:\s+(?P<sysport_gid>\d+),\s+\S+\s+\S(?P<sysport_cookie>\w+\/\d\/\d)\S+\s+\S+\s+(?P<serdes>\S*)\S\s+\S$')

        for line in output.splitlines():
            line = line.strip()

            # |      41 |      3       | MPP_PORT    |    2200 |    True    |    True    |  0.25  |     False      | {'sysport_gid': 85, 'sysport_cookie': 'Gi1/0/45', 'serdes': ''} |
            m = p1.match(line)
            if m:
                group = m.groupdict()
                lag_gid = f"{int(group['lag_gid'])}_{int(group['member_index'])}"
                lag_data =parsed_data.setdefault('ifm_lag_members', {}).setdefault(lag_gid, {})
                lag_data.update({
                    'lag_gid': int(group['lag_gid']),
                    'member_index': int(group['member_index']),
                    'port_type': group['port_type'],
                    'port_id': int(group['port_id']),
                    'rx_enabled': group['rx_enabled'],
                    'tx_enabled': group['tx_enabled'],
                    'weight': float(group['weight']),
                    'empty_lag_port': group['empty_lag_port']
                })

                sysport_detail=lag_data.setdefault("sysport_detail",{})
                sysport_detail.update({
                    'sysport_gid': int(group['sysport_gid']),
                    'sysport_cookie': group['sysport_cookie'],
                    'serdes': group['serdes']
                })

        return parsed_data


class ShowPlatformHardwareFedSwitchFwdAsicInsightL2AttachmentCircuitStatusSchema(MetaParser):
    """Schema for show platform hardware fed switch {switch_id} fwd-asic insight l2_attachment_circuit_status()"""

    schema = {
        'l2_circuit_status': {
            'l2_ace_info': {
                Any(): {
                    'ac_type': str,
                    'eth_port_oid': int,
                    'sysport_gid': int,
                    'ac_gid': int,
                    'sysport_cookie': str,
                    'ac_cookie': str
                }
            },
            'l3_ace_info': {
                Any(): {
                    'ac_type': str,
                    'vlan_tag': int,
                    'sysport_gid': int,
                    'ac_gid': int,
                    Optional('vlan_tag2'): int,
                    'eth_port_oid': int,
                    'sysport_cookie': str,
                    Optional('ac_cookie'): str
                }
            },
            'svi_ace_info': {
                Any(): {
                    'ac_type': str,
                    'switch_gid': int,
                    'vlan_tag': int,
                    'svi_gid': int,
                    'switch_cookie': int
                }
            }
        }
    }

class ShowPlatformHardwareFedSwitchFwdAsicInsightL2AttachmentCircuitStatus(ShowPlatformHardwareFedSwitchFwdAsicInsightL2AttachmentCircuitStatusSchema):
    """Parser for show platform hardware fed switch {switch_id} fwd-asic insight l2_attachment_circuit_status()"""

    cli_command = 'show platform hardware fed switch {switch_id} fwd-asic insight l2_attachment_circuit_status()'

    def cli(self, switch_id, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch_id=switch_id))

        parsed_data = {}

        # | ac_type: L2-DENSE   |                    | eth_port_oid: 1440    | sysport_gid: 41          |
        p1 = re.compile(r'^\S\s+ac_type:\s+(?P<ac_type>\S+)\s+\S\s+\S\s+eth_port_oid:\s+(?P<eth_port_oid>\d+)\s+\S\s+sysport_gid:\s+(?P<sysport_gid>\d+)\s+\S$')

        # | ac_gid: 122880      |                    |                       | sysport_cookie: Gi1/0/1  |
        p2 = re.compile(r'^\S\s+ac_gid:\s+(?P<ac_gid>\d+)\s+\S\s+\S\s+\S\s+sysport_cookie:\s+(?P<sysport_cookie>\S+)\s+\S$')

        #| ac_cookie: Gi1/0/1  |                    |                       |                          |
        p3 = re.compile(r'^\S\s+ac_cookie:\s+(?P<ac_cookie>\S+)\s+\S\s+\S\s+\S\s+\S$')

        #| ac_type: L3         |                    | vlan_tag: 1           | sysport_gid: 10          |
        p1_1 = re.compile(r'^\S\s+ac_type:\s+(?P<ac_type>\S+)\s+\S\s+\S\s+vlan_tag:\s+(?P<vlan_tag>\d+)\s+\S\s+sysport_gid:\s+(?P<sysport_gid>\d+)\s+\S$')

        #| ac_gid: 4098        |                    | eth_port_oid: 578     | sysport_cookie: Re1      |
        p2_1 = re.compile(r'^\S\s+ac_gid:\s+(?P<ac_gid>\d+)\s+\S\s+\S\s+eth_port_oid:\s+(?P<eth_port_oid>\d+)\s+\S\s+sysport_cookie:\s+(?P<sysport_cookie>\S+)\s+\S$')

        #| ac_gid: 4135        |                    | vlan_tag2: 4001       | sysport_cookie: Re1      |
        p2_2 = re.compile(r'^\S\s+ac_gid:\s+(?P<ac_gid>\d+)\s+\S\s+\S\s+vlan_tag2:\s+(?P<vlan_tag2>\d+)\s+\S\s+sysport_cookie:\s+(?P<sysport_cookie>\S+)\s+\S$')

        # |                     |                    | eth_port_oid: 578     |                          |
        p3_2 = re.compile(r'^\S\s+\S\s+\S\s+eth_port_oid:\s+(?P<eth_port_oid>\d+)\s+\S\s+\S$')

        #| ac_type: SVI        | switch_gid: 1      | vlan_tag: 1           |                          |
        p4 = re.compile(r'^\S\s+ac_type:\s+(?P<ac_type>\S+)\s+\S\s+switch_gid:\s+(?P<switch_gid>\d+)\s+\S\s+vlan_tag:\s+(?P<vlan_tag>\d+)\s+\S\s+\S$')

        #| svi_gid: 1          | switch_cookie: 1   |                       |                          |
        p5 = re.compile(r'^\S\s+svi_gid:\s+(?P<svi_gid>\d+)\s+\S\s+switch_cookie:\s+(?P<switch_cookie>\d+)\s+\S\s+\S\s+\S$')


        for line in output.splitlines():
            line = line.strip()

            # | ac_type: L2-DENSE   |                    | eth_port_oid: 1440    | sysport_gid: 41          |
            m = p1.match(line)
            if m:
                group = m.groupdict()
                eth_port_oid= int(group['eth_port_oid'])
                port_data = parsed_data.setdefault('l2_circuit_status', {}).setdefault("l2_ace_info",{}).setdefault(eth_port_oid, {})
                port_data["ac_type"]=group['ac_type']
                port_data["eth_port_oid"]= int(group['eth_port_oid'])
                port_data["sysport_gid"]=int(group['sysport_gid'])


                continue
            # | ac_gid: 122880      |                    |                       | sysport_cookie: Gi1/0/1  |
            m = p2.match(line)
            if m:
                group = m.groupdict()
                port_data["ac_gid"]=int(group['ac_gid'])
                port_data["sysport_cookie"]=group['sysport_cookie']
                continue

            # | ac_cookie: Gi1/0/1  |                    |                       |                          |
            m = p3.match(line)
            if m:
                group = m.groupdict()
                port_data["ac_cookie"]=group['ac_cookie']
                continue

            # | ac_type: L3         |                    | vlan_tag: 1           | sysport_gid: 10          |
            m = p1_1.match(line)
            if m:
                group = m.groupdict()
                vlan_tag= int(group['vlan_tag'])
                port_data = parsed_data.setdefault('l2_circuit_status', {}).setdefault("l3_ace_info",{}).setdefault(vlan_tag, {})
                port_data["ac_type"]=group['ac_type']
                port_data["vlan_tag"]= int(group['vlan_tag'])
                port_data["sysport_gid"]=int(group['sysport_gid'])
                continue

            # | ac_gid: 4098        |                    | eth_port_oid: 578     | sysport_cookie: Re1      |
            m = p2_1.match(line)
            if m:
                group = m.groupdict()
                port_data["ac_gid"]=int(group['ac_gid'])
                port_data["eth_port_oid"]= int(group['eth_port_oid'])
                port_data["sysport_cookie"]=group['sysport_cookie']
                continue

            # | ac_gid: 4135        |                    | vlan_tag2: 4001       | sysport_cookie: Re1      |
            m = p2_2.match(line)
            if m:
                group = m.groupdict()
                port_data["ac_gid"]=int(group['ac_gid'])
                port_data["vlan_tag2"]= int(group['vlan_tag2'])
                port_data["sysport_cookie"]=group['sysport_cookie']
                continue

            # |                     |                    | eth_port_oid: 578     |                          |
            m = p3_2.match(line)
            if m:
                group = m.groupdict()
                port_data["eth_port_oid"]=int(group['eth_port_oid'])
                continue

            #| ac_type: SVI        | switch_gid: 1      | vlan_tag: 1           |                          |
            m = p4.match(line)
            if m:
                group = m.groupdict()
                switch_gid= int(group['switch_gid'])
                port_data = parsed_data.setdefault('l2_circuit_status', {}).setdefault("svi_ace_info",{}).setdefault(switch_gid, {})
                port_data["ac_type"]=group['ac_type']
                port_data["switch_gid"]= int(group['switch_gid'])
                port_data["vlan_tag"]=int(group['vlan_tag'])
                continue

            #| svi_gid: 1          | switch_cookie: 1   |                       |                          |
            m = p5.match(line)
            if m:
                group = m.groupdict()
                port_data["svi_gid"]=int(group['svi_gid'])
                port_data["switch_cookie"]=int(group['switch_cookie'])
                continue

        return parsed_data

class ShowPlatformHardwareFedSwitchFwdAsicResourceTcamTableNflAclFormat0Schema(MetaParser):
    """Schema for 'show platform hardware fed switch {switch_num} fwd-asic resource tcam table nfl_acl format 0'"""
    schema = {
        'regions': {
            Any(): {
                'type': int,
                'asic': int,
                'entries': list
            }
        }
    }

class ShowPlatformHardwareFedSwitchFwdAsicResourceTcamTableNflAclFormat0(ShowPlatformHardwareFedSwitchFwdAsicResourceTcamTableNflAclFormat0Schema):
    """Parser for 'show platform hardware fed switch {switch_num} fwd-asic resource tcam table nfl_acl format 0'"""

    cli_command = 'show platform hardware fed switch {switch_num} fwd-asic resource tcam table nfl_acl format 0'

    def cli(self, switch_num, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch_num=switch_num))

        ret_dict = {}

        # Printing entries for region INGRESS_NFL_ACL_CONTROL (325) type 6 asic 0
        p1 = re.compile(r'^Printing entries for region (?P<region>\S+) \((?P<region_id>\d+)\) type (?P<type>\d+) asic (?P<asic>\d+)$')

        # TAQ-5 Index-224 (A:0,C:0) Valid StartF-1 StartA-1 SkipF-0 SkipA-0
        p2 = re.compile(r'^(?P<entry>TAQ-\d+ Index-\d+ \(A:\d+,C:\d+\) Valid StartF-\d+ StartA-\d+ SkipF-\d+ SkipA-\d+)$')

        # Mask1 00f00000:00000000:00000000:00000000:00000000:00000000:00000000:00000000
        p3 = re.compile(r'^(?P<mask>Mask\d+ [0-9a-fA-F:]+)$')

        for line in output.splitlines():
            line = line.strip()

            # Printing entries for region INGRESS_NFL_ACL_CONTROL (325) type 6 asic 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                current_region = group['region']
                region_dict = ret_dict.setdefault('regions', {}).setdefault(current_region, {})
                region_dict['type'] = int(group['type'])
                region_dict['asic'] = int(group['asic'])
                region_dict['entries'] = []
                continue

            # TAQ-5 Index-224 (A:0,C:0) Valid StartF-1 StartA-1 SkipF-0 SkipA-0
            m = p2.match(line)
            if m:
                entry = m.group('entry')
                if current_region:
                    ret_dict['regions'][current_region]['entries'].append(entry)
                continue

            # Mask1 00f00000:00000000:00000000:00000000:00000000:00000000:00000000:00000000
            m = p3.match(line)
            if m:
                mask = m.group('mask')
                if current_region:
                    ret_dict['regions'][current_region]['entries'].append(mask)
                continue

        return ret_dict
