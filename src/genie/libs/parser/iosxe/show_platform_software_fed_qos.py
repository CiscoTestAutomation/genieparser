"""show_platform_software_fed_qos.py

    * 'show platform software fed active qos policy target status'
    * 'show platform software fed switch {switch} qos policy target status'
    * 'show platform software fed {switch} {mode} qos interface {interface} ingress npd'
    * 'show platform software fed {mode} qos interface {interface} ingress npd'
    * 'show platform software fed {switch} {mode} qos interface {interface} ingress npd detailed'
    * 'show platform software fed {mode} qos interface {interface} ingress npd detailed'
    * 'show platform software fed {switch} {mode} qos interface {interface} egress sdk detailed'
    * 'show platform software fed {mode} qos interface {interface} egress sdk detailed'
    * 'show platform software fed {switch} {mode} qos interface {interface} ingress sdk'
    * 'show platform software fed {mode} qos interface {interface} ingress sdk'
    * 'show platform software fed {switch} {mode} qos interface {interface} ingress sdk detailed'
    * 'show platform software fed {mode} qos interface {interface} ingress sdk detailed'
    * 'show platform software fed {switch} {mode} qos interface {interface} ingress npi detailed'
    * 'show platform software fed {mode} qos interface {interface} ingress npi detailed'
    * 'show platform software fed active qos policy target status'
    * 'show platform software fed switch {switch} qos policy target status'
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
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use, And
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


class ShowPlatformSoftwareFedQosPolicyTargetSchema(MetaParser):
    """search for
    * show platform software fed active qos policy target brief
    """

    schema = {
        "tcg_sum_for_policy": {
            Any(): {
                "interface": {
                    Any(): {
                        "loc": str,
                        "iif_id": str,
                        "direction": str,
                        "tccg": int,
                        "child": int,
                        "mpq": str,
                        "state_cfg": str,
                        "state_opr": str,
                        "address": str,
                    },
                }
            },
        }
    }


class ShowPlatformSoftwareFedQosPolicyTarget(
    ShowPlatformSoftwareFedQosPolicyTargetSchema
):
    """parser for
    * show platform software fed active qos policy target brief
    """

    cli_command = "show platform software fed active qos policy target brief"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(
                "show platform software fed active qos policy target brief"
            )
        else:
            out = output

        ret_dict = {}

        # TCG summary for policy: system-cpp-policy
        p1 = re.compile(r"TCG\ssummary\sfor\spolicy:\s+(?P<policy>\S+)")
        # L:2 GigabitEthernet4/0/9  0x00000000000056  IN    4     0 3/2/0   VALID,SET_INHW  0x7fe0a79f0b88
        p2 = re.compile(
            r"(?P<loc>\S+)\s+(?P<interface>[\w\-\/\s]+)\s+(?P<iif_id>\S+)\s+(?P<direction>(OUT|IN))\s+(?P<tccg>\d+)\s+(?P<child>\d+)\s+(?P<mpq>[\w//]+)\s+(?P<state_cfg>\w+),(?P<state_opr>\S+)\s+(?P<address>\S+)"
        )

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                if "tcg_sum_for_policy" not in ret_dict:
                    sum_dict = ret_dict.setdefault("tcg_sum_for_policy", {})
                policy = str(group["policy"])
                sum_dict[policy] = {}
                sum_dict[policy]["interface"] = {}
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface = str(group["interface"])
                interface = interface.strip()
                sum_dict[policy]["interface"][interface] = {}
                sum_dict[policy]["interface"][interface]["loc"] = str(group["loc"])
                sum_dict[policy]["interface"][interface]["iif_id"] = str(
                    group["iif_id"]
                )
                sum_dict[policy]["interface"][interface]["direction"] = str(
                    group["direction"]
                )
                sum_dict[policy]["interface"][interface]["tccg"] = int(group["tccg"])
                sum_dict[policy]["interface"][interface]["child"] = int(group["child"])
                sum_dict[policy]["interface"][interface]["mpq"] = str(group["mpq"])
                sum_dict[policy]["interface"][interface]["state_cfg"] = str(
                    group["state_cfg"]
                )
                sum_dict[policy]["interface"][interface]["state_opr"] = str(
                    group["state_opr"]
                )
                sum_dict[policy]["interface"][interface]["address"] = str(
                    group["address"]
                )
                continue

        return ret_dict


class ShowPlatformSoftwareFedSwitchActiveQosPolicyTargetSchema(MetaParser):
    """schema for
    * show platform software fed switch active qos policy target brief
    """

    schema = {
        "tcg_sum_for_policy": {
            Any(): {
                "interface": {
                    Any(): {
                        "loc": str,
                        "iif_id": str,
                        "direction": str,
                        "tccg": int,
                        "child": int,
                        "mpq": str,
                        "state_cfg": str,
                        "state_opr": str,
                        "address": str,
                    },
                }
            },
        }
    }


class ShowPlatformSoftwareFedSwitchActiveQosPolicyTarget(
    ShowPlatformSoftwareFedSwitchActiveQosPolicyTargetSchema
):
    """parser for
    * show platform software fed switch active qos policy target brief
    """

    cli_command = "show platform software fed switch active qos policy target brief"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # TCG summary for policy: system-cpp-policy
        p1 = re.compile(r"TCG\ssummary\sfor\spolicy:\s+(?P<policy>\S+)")
        # L:2 GigabitEthernet4/0/9  0x00000000000056  IN    4     0 3/2/0   VALID,SET_INHW  0x7fe0a79f0b88
        p2 = re.compile(
            r"(?P<loc>\S+)\s+(?P<interface>[\w\-\/\s]+)\s+(?P<iif_id>\S+)\s+(?P<direction>(OUT|IN))\s+(?P<tccg>\d+)\s+(?P<child>\d+)\s+(?P<mpq>[\w//]+)\s+(?P<state_cfg>\w+),(?P<state_opr>\S+)\s+(?P<address>\S+)"
        )

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                if "tcg_sum_for_policy" not in ret_dict:
                    sum_dict = ret_dict.setdefault("tcg_sum_for_policy", {})
                policy = str(group["policy"])
                sum_dict[policy] = {}
                sum_dict[policy]["interface"] = {}
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface = str(group["interface"])
                interface = interface.strip()
                sum_dict[policy]["interface"][interface] = {}
                sum_dict[policy]["interface"][interface]["loc"] = str(group["loc"])
                sum_dict[policy]["interface"][interface]["iif_id"] = str(
                    group["iif_id"]
                )
                sum_dict[policy]["interface"][interface]["direction"] = str(
                    group["direction"]
                )
                sum_dict[policy]["interface"][interface]["tccg"] = int(group["tccg"])
                sum_dict[policy]["interface"][interface]["child"] = int(group["child"])
                sum_dict[policy]["interface"][interface]["mpq"] = str(group["mpq"])
                sum_dict[policy]["interface"][interface]["state_cfg"] = str(
                    group["state_cfg"]
                )
                sum_dict[policy]["interface"][interface]["state_opr"] = str(
                    group["state_opr"]
                )
                sum_dict[policy]["interface"][interface]["address"] = str(
                    group["address"]
                )
                continue

        return ret_dict


# ======================================================
# Parser for 'show platform software fed active qos policy summary '
# ======================================================


class ShowPlatformSoftwareFedActiveQosPolicySummarySchema(MetaParser):
    """Schema for show platform software fed active qos policy summary"""

    schema = {
        "cg_id": {
            Any(): {
                "classes": int,
                "targets": int,
                "child": int,
                "cfg_err": int,
                "in_hw": int,
                "op_error": int,
                "policy_name": str,
            },
        },
    }


class ShowPlatformSoftwareFedActiveQosPolicySummary(
    ShowPlatformSoftwareFedActiveQosPolicySummarySchema
):
    """Parser for show platform software fed active qos policy summary"""

    cli_command = "show platform software fed active qos policy summary"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # 15212688   22     33      0     0      33    0     system-cpp-policy
        p1 = re.compile(
            r"^(?P<cg_id>\d+)\s+(?P<classes>\d+)\s+(?P<targets>\d+)\s+(?P<child>\d+)\s+(?P<cfg_err>\d+)\s+(?P<in_hw>\d+)\s+(?P<op_error>\d+)\s+(?P<policy_name>\S+)$"
        )

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # 15212688   22     33      0     0      33    0     system-cpp-policy
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                cg_id = int(dict_val["cg_id"])
                cg_id_dict = ret_dict.setdefault("cg_id", {})
                policy_map_dict = cg_id_dict.setdefault(cg_id, {})
                policy_map_dict["classes"] = int(dict_val["classes"])
                policy_map_dict["targets"] = int(dict_val["targets"])
                policy_map_dict["child"] = int(dict_val["child"])
                policy_map_dict["cfg_err"] = int(dict_val["cfg_err"])
                policy_map_dict["in_hw"] = int(dict_val["in_hw"])
                policy_map_dict["op_error"] = int(dict_val["op_error"])
                policy_map_dict["policy_name"] = dict_val["policy_name"]
                continue

        return ret_dict


# ======================================================
# Schema for 'show platform software fed switch {switch} qos policy target status '
# ======================================================
class ShowPlatformSoftwareFedSwitchQosPolicyTargetStatusSchema(MetaParser):
    """Schema for show platform software fed switch {switch} qos policy target status"""

    schema = {
        "interface": {
            Any(): {
                "policy": {
                    Any(): {
                        "iif_id": str,
                        "dir": str,
                        "state": str,
                        "loc": str,
                    }
                }
            }
        }
    }


# ======================================================
# Parser for 'show platform software fed switch {switch} qos policy target status '
# ======================================================
class ShowPlatformSoftwareFedSwitchQosPolicyTargetStatus(
    ShowPlatformSoftwareFedSwitchQosPolicyTargetStatusSchema
):
    """Parser for show platform software fed switch {switch} qos policy target status"""

    cli_command = [
        "show platform software fed active qos policy target status",
        "show platform software fed switch {switch} qos policy target status",
    ]

    def cli(self, switch=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[0]
            else:
                cmd = self.cli_command[1].format(switch=switch)

            output = self.device.execute(cmd)

        # L:3 GigabitEthernet3/0/3  0x0000000000006a OUT VALID,SET_INHW  pm1
        p1 = re.compile(
            r"^(?P<loc>\S+)\s+(?P<interface>\S+)\s+(?P<iif_id>\S+)\s+(?P<dir>\w+)\s+(?P<state>[\w,_\-]+)\s+(?P<policy>\S+)$"
        )

        ret_dict = {}

        for line in output.splitlines():
            # L:3 GigabitEthernet3/0/3  0x0000000000006a OUT VALID,SET_INHW  pm1
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                interface_var = dict_val["interface"]
                policy_dict = (
                    ret_dict.setdefault("interface", {})
                    .setdefault(interface_var, {})
                    .setdefault("policy", {})
                    .setdefault(dict_val["policy"], {})
                )
                policy_dict["iif_id"] = dict_val["iif_id"]
                policy_dict["dir"] = dict_val["dir"]
                policy_dict["state"] = dict_val["state"]
                policy_dict["loc"] = dict_val["loc"]
                continue

        return ret_dict


# =====================================================================
# Super Parser for:
#   * 'show platform software fed {switch} {mode} qos interface {interface} ingress npd detailed',
#   * 'show platform software fed {mode} qos interface {interface} ingress npd detailed',
#   * 'show platform software fed {switch} {mode} qos interface {interface} ingress npd',
#   * 'show platform software fed {mode} qos interface {interface} ingress npd',
#   * 'show platform software fed {switch} {mode} qos interface {interface} egress sdk detailed',
#   * 'show platform software fed {mode} qos interface {interface} egress sdk detailed',
#   * 'show policy-map target service-group {num}',
#   * 'show policy-map control-plane'
#   * 'show policy-map interface',
# =====================================================================
class ShowPlatformSoftwareFedQosInterfaceSuperParserSchema(MetaParser):
    """Schema for show platform software fed {switch} {mode} qos interface {interface} ingress npd detailed"""

    schema = {
        Optional("interface"): {
            Any(): {
                "cgid": str,
                "no_of_classes": int,
                "tcg_ref_count": int,
                "filter_state": str,
                "vmr_state": str,
            }
        },
        "qos_profile_information": {
            "oid": str,
            "ref_count": int,
            "no_of_counter": int,
            Optional("no_of_meters"): int,
            Optional("marking_source"): str,
            "tunnel_mode": str,
            "need_filter_table_update": str,
            Optional("dscp"): {
                Any(): {
                    "remap": int,
                    Optional("encap"): int,
                    Optional("etos"): int,
                    Optional("qos_group"): int,
                    Optional("epcp"): int,
                    Optional("tc"): int,
                    Optional("eexp"): int,
                    Optional("ile"): str,
                    Optional("dp"): str,
                    Optional("meter"): str,
                    Optional("counteroffset"): int,
                    Optional("mc_offset"): int,
                }
            },
            Optional("cos_dei"): {
                Any(): {
                    "remap": int,
                    Optional("encap"): int,
                    Optional("etos"): int,
                    Optional("qos_group"): int,
                    Optional("epcp"): int,
                    Optional("tc"): int,
                    Optional("eexp"): int,
                    Optional("ile"): str,
                    Optional("dp"): str,
                    Optional("meter"): str,
                    Optional("counteroffset"): int,
                    Optional("mc_offset"): int,
                }
            },
            Optional("exp"): {
                Any(): {
                    "remap": int,
                    Optional("encap"): int,
                    Optional("etos"): int,
                    Optional("qos_group"): int,
                    Optional("epcp"): int,
                    Optional("tc"): int,
                    Optional("eexp"): int,
                    Optional("ile"): str,
                    Optional("dp"): str,
                    Optional("meter"): str,
                    Optional("counteroffset"): int,
                    Optional("mc_offset"): int,
                }
            },
        },
        Optional("markdown_table"): {
            "oid": str,
            "dscp": {Any(): {"green": int, "yellow": int, "red": int}},
            "pcpdei": {Any(): {"green": int, "yellow": int, "red": int}},
            "exp": {Any(): {"green": int, "yellow": int, "red": int}},
            "encapexp": {Any(): {"green": int, "yellow": int, "red": int}},
        },
        Optional("ipv4_acl"): {
            Optional("oid"): str,
            Optional("l3_oid"): str,
            Optional("l2_oid"): str,
            "number_of_aces": int,
            Optional("ace"): {
                Any(): {
                    "class_id": str,
                    "ipv4_src_address": str,
                    "ipv4_src_mask": str,
                    "ipv4_dst_address": str,
                    "ipv4_dst_mask": str,
                    "protocol": str,
                    "protocol_mask": str,
                    "dscp": str,
                    "dscp_mask": str,
                    "ttl_start": str,
                    "ttl_end": str,
                    "tcp_flags": str,
                    "tcp_mask": str,
                    "ip_flags": str,
                    "ip_mask": str,
                    "src_port_start": str,
                    "src_port_end": str,
                    "dst_port_start": str,
                    "dst_port_end": str,
                    Optional("result_action"): {
                        "remark_value": str,
                        "encap_value": str,
                        "qos_group": str,
                        "traffic_class": str,
                        "drop_precedence": str,
                        "overwrite_phb": str,
                        "overwrite_qos_group": str,
                        "overwrite_encap": str,
                        "overwrite_fwd_tag": str,
                        "meter_enabled": str,
                        "meter_counter_offset": str,
                    },
                }
            },
        },
        Optional("ipv6_acl"): {
            Optional("oid"): str,
            Optional("l3_oid"): str,
            Optional("l2_oid"): str,
            "number_of_aces": int,
            Optional("ace"): {
                Any(): {
                    "class_id": str,
                    "ipv6_src_address": str,
                    "ipv6_src_mask": str,
                    "ipv6_dst_address": str,
                    "ipv6_dst_mask": str,
                    "protocol": str,
                    "protocol_mask": str,
                    "dscp": str,
                    "dscp_mask": str,
                    "ttl_start": str,
                    "ttl_end": str,
                    "tcp_flags": str,
                    "tcp_mask": str,
                    "ip_flags": str,
                    "ip_mask": str,
                    "src_port_start": str,
                    "src_port_end": str,
                    "dst_port_start": str,
                    "dst_port_end": str,
                    Optional("result_action"): {
                        "remark_value": str,
                        "encap_value": str,
                        "qos_group": str,
                        "traffic_class": str,
                        "drop_precedence": str,
                        "overwrite_phb": str,
                        "overwrite_qos_group": str,
                        "overwrite_encap": str,
                        "overwrite_fwd_tag": str,
                        "meter_enabled": str,
                        "meter_counter_offset": str,
                    },
                }
            },
        },
        Optional("bind_information"): {
            "port_type": str,
            Optional("iqp_counter_size"): int,
            Optional("iqp_counter_oid"): str,
            Optional("eqp_counter_size"): int,
            Optional("eqp_counter_oid"): str,
            Optional("meter_type"): str,
            Optional("meter_set_oid"): str,
            Optional("no_of_meters"): int,
            "system_port_oid": str,
            "port_oid": str,
            "speed": int,
            "port_internal_state": str,
            Optional("meter_set_info"): {
                Any(): {
                    "cir": int,
                    "eir": int,
                    "profile_oid": str,
                    "action_profile_oid": str,
                }
            },
        },
    }


# =====================================================================
# Super Parser for:
#   * 'show platform software fed {switch} {mode} qos interface {interface} ingress npd detailed',
#   * 'show platform software fed {mode} qos interface {interface} ingress npd detailed',
#   * 'show platform software fed {switch} {mode} qos interface {interface} ingress npd',
#   * 'show platform software fed {mode} qos interface {interface} ingress npd',
#   * 'show platform software fed {switch} {mode} qos interface {interface} egress sdk detailed',
#   * 'show platform software fed {mode} qos interface {interface} egress sdk detailed',
#   * 'show policy-map target service-group {num}',
#   * 'show policy-map control-plane'
#   * 'show policy-map interface',
# =====================================================================
class ShowPlatformSoftwareFedQosInterfaceSuperParser(
    ShowPlatformSoftwareFedQosInterfaceSuperParserSchema
):
    """Parser for show platform software fed {switch} {mode} qos interface {interface} ingress npd detailed"""

    cli_command = [
        "show platform software fed {switch} {mode} qos interface {interface} ingress npd detailed",
        "show platform software fed {mode} qos interface {interface} ingress npd detailed",
    ]

    def cli(self, mode, interface, switch=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(
                    switch=switch, mode=mode, interface=interface
                )
            else:
                cmd = self.cli_command[1].format(mode=mode, interface=interface)

            output = self.device.execute(cmd, timeout=600)

        # [HundredGigE1/0/5, map1, Ingress]: CGID = 0x738310
        # [HundredGigE1/0/1.1, map1, Ingress]: CGID = 0x738310
        # [Port-channel10, map1, Ingress]: CGID = 0x738310
        p1 = re.compile(r"^\[(?P<interface>[\w\/\.\-]+),.+$")

        # cgid: 0x738310
        p1_1 = re.compile(r"^cgid:\s+(?P<cgid>\w+)$")

        # No of classes: 4
        p1_2 = re.compile(r"^No of classes:\s+(?P<no_of_classes>\d+)$")

        # TCG ref count: 1
        p1_3 = re.compile(r"^TCG ref count:\s+(?P<tcg_ref_count>\d+)$")

        # Filter state: UP TO DATE
        p1_4 = re.compile(r"^Filter state:\s+(?P<filter_state>[\w\s]+)$")

        # VMR state: UP TO DATE
        p1_5 = re.compile(r"^VMR state:\s+(?P<vmr_state>[\w\s]+)$")

        # NPD: Ingress QOS Profile information
        # SDK: Egress QOS Profile information
        # SDK: Ingress QOS Profile information
        p2 = re.compile(r"^(NPD|SDK): (Ingress|Egress) QOS Profile information$")

        # OID: 0x82E
        p2_1 = re.compile(r"^OID:\s+(?P<oid>\w+)$")

        # Ref Count: 1
        p2_2 = re.compile(r"^Ref Count:\s+(?P<ref_count>\d+)$")

        # No of  Counter: 1
        p2_3 = re.compile(r"^No of\s+Counter:\s+(?P<no_of_counter>\d+)$")

        # No of meters: 3
        p2_4 = re.compile(r"^No of meters:\s+(?P<no_of_meters>\d+)$")

        # Tunnel Mode: RE-EVALUATE
        p2_5 = re.compile(r"^Tunnel Mode:\s+(?P<tunnel_mode>[\w\-\s]+)$")

        # Need filter table update: UPTODATE
        p2_6 = re.compile(
            r"^Need filter table update:\s+(?P<need_filter_table_update>[\w\s]+)$"
        )

        # Marking source: Tag
        p2_7 = re.compile(r"^Marking source:\s+(?P<marking_source>\w+)$")

        # DSCP      Remap   Encap   Qos Group   TC  DP  Meter MCOffset
        # COS_DEI   Remap   Encap   Qos Group   TC  DP  Meter MCOffset
        # EXP      Remap   Encap   Qos Group   TC  DP  Meter MCOffset
        # DSCP      Remap   ETOS    EPCP    EExp   ILE   CounterOffset
        p3 = re.compile(
            r"^(?P<table>DSCP|COS_DEI|EXP)\s+Remap\s+(Encap|ETOS)\s+(Qos Group|EPCP)\s+(TC|EExp)\s+(DP|ILE)\s+(Meter|CounterOffset)(\s+MCOffset)?$"
        )

        # 0          0       0         0       0   G     N      3
        p3_1 = re.compile(
            r"^(?P<counter>\d+)\s+(?P<remap>\d+)\s+(?P<encap>\d+)\s+(?P<qos_group>\d+)\s+"
            r"(?P<tc>\d+)\s+(?P<dp>\w+)\s+(?P<meter>\w+)\s+(?P<mc_offset>\d+)$"
        )

        # 0          0       0         0       0   G     N      3
        p3_2 = re.compile(
            r"^(?P<counter>\d+)\s+(?P<remap>\d+)\s+(?P<etos>\d+)\s+(?P<epcp>\d+)\s+"
            r"(?P<eexp>\d+)\s+(?P<ile>\w+)\s+(?P<counteroffset>\w+)$"
        )

        # Markdown Table-Map OID: 0x5EE
        p4 = re.compile(r"^Markdown Table-Map OID: (?P<oid>\w+)$")

        # DSCP       Green   Yellow     Red
        # PCPDEI      Green   Yellow     Red
        # EXP        Green   Yellow     Red
        p4_0 = re.compile(r"^(?P<table>\w+)\s+Green\s+Yellow\s+Red$")

        # 1           1       1        1
        p4_1 = re.compile(
            r"^(?P<counter>\d+)\s+(?P<green>\d+)\s+(?P<yellow>\d+)\s+(?P<red>\d+)$"
        )

        # IPV4 ACL (OID: 0x593, No of ACEs: 3)
        # IPV6 ACL (OID: 0x5DC, No of ACEs: 3)
        # IPV4 ACL (OID(L3/L2): 0xAF6/0xAF5, No of ACEs: 3)
        # IPV6 ACL (OID(L3/L2): 0xAF8/0xAF7, No of ACEs: 3)
        p5 = re.compile(
            r"^(?P<acl_version>\w+ ACL) \(OID(\(L3\/L2\))?: ((?P<l3_oid>\w+)\/(?P<l2_oid>\w+))?(?P<oid>\w+)?, No of ACEs: (?P<number_of_aces>\d+)\)$"
        )

        # IPV4 ACE Key/Mask
        # IPV6 ACE Key/Mask
        p5_0 = re.compile(r"^(IPV4|IPV6) ACE Key/Mask$")

        # Class id: 0x0
        p5_1 = re.compile(r"^Class id: (?P<class_id>\w+)$")

        # IPv4 Src/Mask: 0.0.0.0/0.0.0.0
        # IPv6 Src/Mask: ::/::
        p5_2 = re.compile(
            r"^(?P<ip_version>\w+)\sSrc\/Mask:\s(?P<src_address>\S+)\/(?P<src_mask>\S+)$"
        )

        # IPv4 Dst/Mask: 0.0.0.0/0.0.0.0
        # IPv6 Dst/Mask: ::/::
        p5_3 = re.compile(
            r"^(?P<ip_version>\w+)\sDst\/Mask:\s(?P<dst_address>\S+)\/(?P<dst_mask>\S+)$"
        )

        # Protocol/Mask: 0x0/0x0
        p5_4 = re.compile(
            r"^Protocol\/Mask:\s(?P<protocol>\w+)\/(?P<protocol_mask>\w+)$"
        )

        # DSCP/Mask: 0x8/0x3f
        p5_5 = re.compile(r"^DSCP\/Mask:\s(?P<dscp>\w+)\/(?P<dscp_mask>\w+)$")

        # TTL Start/End: 0x0/0x0
        p5_6 = re.compile(r"^TTL Start\/End:\s(?P<ttl_start>\w+)\/(?P<ttl_end>\w+)$")

        # TCP Flags/Mask: 0x0/0x0
        p5_7 = re.compile(r"^TCP Flags\/Mask:\s(?P<tcp_flags>\w+)\/(?P<tcp_mask>\w+)$")

        # IP Flags/Mask: 0x0/0x0
        p5_8 = re.compile(r"^IP Flags\/Mask:\s(?P<ip_flags>\w+)\/(?P<ip_mask>\w+)$")

        # Src Port Start/End: 0x0/0x0
        p5_9 = re.compile(
            r"^Src Port Start\/End:\s(?P<src_port_start>\w+)\/(?P<src_port_end>\w+)$"
        )

        # Dst Port Start/End: 0x0/0x0
        p5_10 = re.compile(
            r"^Dst Port Start\/End:\s(?P<dst_port_start>\w+)\/(?P<dst_port_end>\w+)$"
        )

        # Result Action
        p6 = re.compile(r"^Result Action$")

        # Remark value: 0
        p6_1 = re.compile(r"^Remark value:\s(?P<remark_value>\w+)$")

        # Encap value: 0
        p6_2 = re.compile(r"^Encap value:\s(?P<encap_value>\w+)$")

        # QOS Group: 0
        p6_3 = re.compile(r"^QOS Group:\s(?P<qos_group>\w+)$")

        # Traffic Class: 0
        p6_4 = re.compile(r"^Traffic Class:\s(?P<traffic_class>\w+)$")

        # Drop Precedence: G
        p6_5 = re.compile(r"^Drop Precedence:\s(?P<drop_precedence>\w+)$")

        # Overwrite PHB: N
        p6_6 = re.compile(r"^Overwrite PHB:\s(?P<overwrite_phb>\w+)$")

        # Overwrite QOS Group: N
        p6_7 = re.compile(r"^Overwrite QOS Group:\s(?P<overwrite_qos_group>\w+)$")

        # Overwrite Encap: N
        p6_8 = re.compile(r"^Overwrite Encap:\s(?P<overwrite_encap>\w+)$")

        # Overwrite Fwd Tag: N
        p6_9 = re.compile(r"^Overwrite Fwd Tag:\s(?P<overwrite_fwd_tag>\w+)$")

        # Meter Enabled: Y
        p6_10 = re.compile(r"^Meter Enabled:\s(?P<meter_enabled>\w+)$")

        # Meter or Counter offset: 0
        p6_11 = re.compile(r"^Meter or Counter offset:\s(?P<meter_counter_offset>\w+)$")

        # NPD: Bind Information
        # SDK: Bind Information
        p7 = re.compile(r"^(NPD|SDK): Bind Information$")

        # Port Type: L3
        # Port Type: L2 ETHER CHANNEL
        p7_1 = re.compile(r"^Port Type:\s+(?P<port_type>.+)$")

        # IQP counter size: 1
        p7_2 = re.compile(r"^IQP counter size:\s+(?P<iqp_counter_size>\d+)$")

        # IQP Counter OID: 0x0
        p7_3 = re.compile(r"^IQP Counter OID:\s+(?P<iqp_counter_oid>\w+)$")

        # Meter Type: EXACT
        # Meter Type: IFG EXACT
        p7_4 = re.compile(r"^Meter Type:\s+(?P<meter_type>[\w\s]+)$")

        # Meter set OID: 0x831
        p7_5 = re.compile(r"^Meter set OID:\s+(?P<meter_set_oid>\w+)$")

        # No of meters: 4
        p7_6 = re.compile(r"^No of meters:\s+(?P<no_of_meters>\d+)$")

        # System port OID: 0x5ED
        p7_7 = re.compile(r"^System port OID:\s+(?P<system_port_oid>\w+)$")

        # Port OID: 0x5E9
        p7_8 = re.compile(r"^Port OID:\s+(?P<port_oid>\w+)$")

        # Speed: 10000000000
        p7_9 = re.compile(r"^Speed:\s+(?P<speed>\w+)$")

        # Port Internal State: Active
        p7_10 = re.compile(r"^Port Internal State:\s+(?P<port_internal_state>\w+)$")

        # EQP counter size: 5
        p7_11 = re.compile(r"^EQP counter size:\s+(?P<eqp_counter_size>\d+)$")

        # EQP Counter OID: 0xAC6
        p7_12 = re.compile(r"^EQP Counter OID:\s+(?P<eqp_counter_oid>\w+)$")

        # Meter Set info
        p8 = re.compile(r"^Meter Set info$")

        # CIR: 1000000000
        p8_1 = re.compile(r"^CIR:\s+(?P<cir>\d+)$")

        # EIR: 1000000000
        p8_2 = re.compile(r"^EIR:\s+(?P<eir>\d+)$")

        # Profile OID: 0x832
        p8_3 = re.compile(r"^Profile OID:\s+(?P<profile_oid>\w+)$")

        # Action Profile OID: 0x110
        p8_4 = re.compile(r"^Action Profile OID:\s+(?P<action_profile_oid>\w+)$")

        ret_dict = {}
        meter_set_count = 0
        ace_count = 0

        for line in output.splitlines():
            line = line.strip()

            # [HundredGigE1/0/5, map1, Ingress]: CGID = 0x738310
            # [HundredGigE1/0/1.1, map1, Ingress]: CGID = 0x738310
            m = p1.match(line)
            if m:
                int_dict = ret_dict.setdefault("interface", {}).setdefault(
                    Common.convert_intf_name(m.groupdict()["interface"]), {}
                )
                continue

            # cgid: 0x738310
            m = p1_1.match(line)
            if m:
                int_dict.setdefault("cgid", m.groupdict()["cgid"])
                continue

            # No of classes: 4
            m = p1_2.match(line)
            if m:
                int_dict.setdefault(
                    "no_of_classes", int(m.groupdict()["no_of_classes"])
                )
                continue

            # TCG ref count: 1
            m = p1_3.match(line)
            if m:
                int_dict.setdefault(
                    "tcg_ref_count", int(m.groupdict()["tcg_ref_count"])
                )
                continue

            # Filter state: UP TO DATE
            m = p1_4.match(line)
            if m:
                int_dict.setdefault("filter_state", m.groupdict()["filter_state"])
                continue

            # VMR state: UP TO DATE
            m = p1_5.match(line)
            if m:
                int_dict.setdefault("vmr_state", m.groupdict()["vmr_state"])
                continue

            # NPD: Ingress QOS Profile information
            # SDK: Egress QOS Profile information
            # SDK: Ingress QOS Profile information
            m = p2.match(line)
            if m:
                qos_dict = ret_dict.setdefault("qos_profile_information", {})
                continue

            # OID: 0x82E
            m = p2_1.match(line)
            if m:
                qos_dict.setdefault("oid", m.groupdict()["oid"])
                continue

            # Ref Count: 1
            m = p2_2.match(line)
            if m:
                qos_dict.setdefault("ref_count", int(m.groupdict()["ref_count"]))
                continue

            # No of  Counter: 1
            m = p2_3.match(line)
            if m:
                qos_dict.setdefault(
                    "no_of_counter", int(m.groupdict()["no_of_counter"])
                )
                continue

            # No of meters: 3
            m = p2_4.match(line)
            if m and "no_of_meters" not in qos_dict:
                qos_dict.setdefault("no_of_meters", int(m.groupdict()["no_of_meters"]))
                continue

            # Tunnel Mode: RE-EVALUATE
            m = p2_5.match(line)
            if m:
                qos_dict.setdefault("tunnel_mode", m.groupdict()["tunnel_mode"])
                continue

            # Need filter table update: UPTODATE
            m = p2_6.match(line)
            if m:
                qos_dict.setdefault(
                    "need_filter_table_update",
                    m.groupdict()["need_filter_table_update"],
                )
                continue

            # Marking source: Tag
            m = p2_7.match(line)
            if m:
                qos_dict.setdefault("marking_source", m.groupdict()["marking_source"])
                continue

            # DSCP      Remap   Encap   Qos Group   TC  DP  Meter MCOffset
            # COS_DEI   Remap   Encap   Qos Group   TC  DP  Meter MCOffset
            # EXP      Remap   Encap   Qos Group   TC  DP  Meter MCOffset
            # DSCP      Remap   ETOS    EPCP    EExp   ILE   CounterOffset
            m = p3.match(line)
            if m:
                table_dict = qos_dict.setdefault(m.groupdict()["table"].lower(), {})
                continue

            # 0          0       0         0       0   G     N      3
            m = p3_1.match(line)
            if m:
                result = m.groupdict()
                table_count_dict = table_dict.setdefault(result["counter"], {})
                table_count_dict["remap"] = int(result["remap"])
                table_count_dict["encap"] = int(result["encap"])
                table_count_dict["qos_group"] = int(result["qos_group"])
                table_count_dict["tc"] = int(result["tc"])
                table_count_dict["dp"] = result["dp"]
                table_count_dict["meter"] = result["meter"]
                table_count_dict["mc_offset"] = int(result["mc_offset"])
                continue

            # 0          0       0         0       0   G     N      3
            m = p3_2.match(line)
            if m:
                result = m.groupdict()
                table_count_dict = table_dict.setdefault(result["counter"], {})
                table_count_dict["remap"] = int(result["remap"])
                table_count_dict["etos"] = int(result["etos"])
                table_count_dict["epcp"] = int(result["epcp"])
                table_count_dict["eexp"] = int(result["eexp"])
                table_count_dict["ile"] = result["ile"]
                table_count_dict["counteroffset"] = int(result["counteroffset"])
                continue

            # Markdown Table-Map OID: 0x5EE
            m = p4.match(line)
            if m:
                markdown_dict = ret_dict.setdefault("markdown_table", {})
                markdown_dict["oid"] = m.groupdict()["oid"]
                continue

            # DSCP       Green   Yellow     Red
            # PCPDEI      Green   Yellow     Red
            # EXP        Green   Yellow     Red
            m = p4_0.match(line)
            if m:
                table_name = m.groupdict()["table"].lower().replace(" ", "_")
                markdown_table_dict = markdown_dict.setdefault(table_name, {})
                continue

            # 1           1       1        1
            m = p4_1.match(line)
            if m:
                values = m.groupdict()
                markdown_each_table = markdown_table_dict.setdefault(
                    values["counter"], {}
                )
                markdown_each_table["green"] = int(values["green"])
                markdown_each_table["yellow"] = int(values["yellow"])
                markdown_each_table["red"] = int(values["red"])
                continue

            # IPV4 ACL (OID: 0x593, No of ACEs: 3)
            # IPV6 ACL (OID: 0x5DC, No of ACEs: 3)
            m = p5.match(line)
            if m:
                values = m.groupdict()
                acl_name = values["acl_version"].lower().replace(" ", "_")
                if acl_name not in ret_dict.keys():
                    ace_count = 0
                acl_dict = ret_dict.setdefault(acl_name, {})
                if values["oid"]:
                    acl_dict["oid"] = values["oid"]
                else:
                    acl_dict["l3_oid"] = values["l3_oid"]
                    acl_dict["l2_oid"] = values["l2_oid"]
                acl_dict["number_of_aces"] = int(values["number_of_aces"])

            # IPV4 ACE Key/Mask
            # IPV6 ACE Key/Mask
            m = p5_0.match(line)
            if m:
                ace_dict = acl_dict.setdefault("ace", {}).setdefault(ace_count, {})
                ace_count += 1
                continue

            # Class id: 0x0
            m = p5_1.match(line)
            if m:
                ace_dict["class_id"] = m.groupdict()["class_id"]
                continue

            # IPv4 Src/Mask: 0.0.0.0/0.0.0.0
            # IPv6 Src/Mask: ::/::
            m = p5_2.match(line)
            if m:
                values = m.groupdict()
                ip_version = values["ip_version"].lower()
                ace_dict[f"{ip_version}_src_address"] = values["src_address"]
                ace_dict[f"{ip_version}_src_mask"] = values["src_mask"]
                continue

            # IPv4 Dst/Mask: 0.0.0.0/0.0.0.0
            # IPv6 Dst/Mask: ::/::
            m = p5_3.match(line)
            if m:
                values = m.groupdict()
                ip_version = values["ip_version"].lower()
                ace_dict[f"{ip_version}_dst_address"] = values["dst_address"]
                ace_dict[f"{ip_version}_dst_mask"] = values["dst_mask"]
                continue

            # Protocol/Mask: 0x0/0x0
            m = p5_4.match(line)
            if m:
                ace_dict["protocol"] = m.groupdict()["protocol"]
                ace_dict["protocol_mask"] = m.groupdict()["protocol_mask"]
                continue

            # DSCP/Mask: 0x8/0x3f
            m = p5_5.match(line)
            if m:
                ace_dict["dscp"] = m.groupdict()["dscp"]
                ace_dict["dscp_mask"] = m.groupdict()["dscp_mask"]
                continue

            # TTL Start/End: 0x0/0x0
            m = p5_6.match(line)
            if m:
                ace_dict["ttl_start"] = m.groupdict()["ttl_start"]
                ace_dict["ttl_end"] = m.groupdict()["ttl_end"]
                continue

            # TCP Flags/Mask: 0x0/0x0
            m = p5_7.match(line)
            if m:
                ace_dict["tcp_flags"] = m.groupdict()["tcp_flags"]
                ace_dict["tcp_mask"] = m.groupdict()["tcp_mask"]
                continue

            # IP Flags/Mask: 0x0/0x0
            m = p5_8.match(line)
            if m:
                ace_dict["ip_flags"] = m.groupdict()["ip_flags"]
                ace_dict["ip_mask"] = m.groupdict()["ip_mask"]
                continue

            # Src Port Start/End: 0x0/0x0
            m = p5_9.match(line)
            if m:
                ace_dict["src_port_start"] = m.groupdict()["src_port_start"]
                ace_dict["src_port_end"] = m.groupdict()["src_port_end"]
                continue

            # Dst Port Start/End: 0x0/0x0
            m = p5_10.match(line)
            if m:
                ace_dict["dst_port_start"] = m.groupdict()["dst_port_start"]
                ace_dict["dst_port_end"] = m.groupdict()["dst_port_end"]
                continue

            # Result Action
            m = p6.match(line)
            if m:
                ace_action_dict = ace_dict.setdefault("result_action", {})
                continue

            # Remark value: 0
            m = p6_1.match(line)
            if m:
                ace_action_dict["remark_value"] = m.groupdict()["remark_value"]
                continue

            # Encap value: 0
            m = p6_2.match(line)
            if m:
                ace_action_dict["encap_value"] = m.groupdict()["encap_value"]
                continue

            # QOS Group: 0
            m = p6_3.match(line)
            if m:
                ace_action_dict["qos_group"] = m.groupdict()["qos_group"]
                continue

            # Traffic Class: 0
            m = p6_4.match(line)
            if m:
                ace_action_dict["traffic_class"] = m.groupdict()["traffic_class"]
                continue

            # Drop Precedence: G
            m = p6_5.match(line)
            if m:
                ace_action_dict["drop_precedence"] = m.groupdict()["drop_precedence"]
                continue

            # Overwrite PHB: N
            m = p6_6.match(line)
            if m:
                ace_action_dict["overwrite_phb"] = m.groupdict()["overwrite_phb"]
                continue

            # Overwrite QOS Group: N
            m = p6_7.match(line)
            if m:
                ace_action_dict["overwrite_qos_group"] = m.groupdict()[
                    "overwrite_qos_group"
                ]
                continue

            # Overwrite Encap: N
            m = p6_8.match(line)
            if m:
                ace_action_dict["overwrite_encap"] = m.groupdict()["overwrite_encap"]
                continue

            # Overwrite Fwd Tag: N
            m = p6_9.match(line)
            if m:
                ace_action_dict["overwrite_fwd_tag"] = m.groupdict()[
                    "overwrite_fwd_tag"
                ]
                continue

            # Meter Enabled: Y
            m = p6_10.match(line)
            if m:
                ace_action_dict["meter_enabled"] = m.groupdict()["meter_enabled"]
                continue

            # Meter or Counter offset: 0
            m = p6_11.match(line)
            if m:
                ace_action_dict["meter_counter_offset"] = m.groupdict()[
                    "meter_counter_offset"
                ]
                continue

            # NPD: Bind Information
            # SDK: Bind Information
            m = p7.match(line)
            if m:
                bind_dict = ret_dict.setdefault("bind_information", {})
                continue

            # Port Type: L3
            m = p7_1.match(line)
            if m:
                bind_dict.setdefault("port_type", m.groupdict()["port_type"])
                continue

            # IQP counter size: 1
            m = p7_2.match(line)
            if m:
                bind_dict.setdefault(
                    "iqp_counter_size", int(m.groupdict()["iqp_counter_size"])
                )
                continue

            # IQP Counter OID: 0x0
            m = p7_3.match(line)
            if m:
                bind_dict.setdefault(
                    "iqp_counter_oid", m.groupdict()["iqp_counter_oid"]
                )
                continue

            # Meter Type: EXACT
            # Meter Type: IFG EXACT
            m = p7_4.match(line)
            if m:
                bind_dict.setdefault("meter_type", m.groupdict()["meter_type"])
                continue

            # Meter set OID: 0x831
            m = p7_5.match(line)
            if m:
                bind_dict.setdefault("meter_set_oid", m.groupdict()["meter_set_oid"])
                continue

            # No of meters: 4
            m = p7_6.match(line)
            if m:
                bind_dict.setdefault("no_of_meters", int(m.groupdict()["no_of_meters"]))
                continue

            # System port OID: 0x5ED
            m = p7_7.match(line)
            if m:
                bind_dict.setdefault(
                    "system_port_oid", m.groupdict()["system_port_oid"]
                )
                continue

            # Port OID: 0x5E9
            m = p7_8.match(line)
            if m:
                bind_dict.setdefault("port_oid", m.groupdict()["port_oid"])
                continue

            # Speed: 10000000000
            m = p7_9.match(line)
            if m:
                bind_dict.setdefault("speed", int(m.groupdict()["speed"]))
                continue

            # Port Internal State: Active
            m = p7_10.match(line)
            if m:
                bind_dict.setdefault(
                    "port_internal_state", m.groupdict()["port_internal_state"]
                )
                continue

            # EQP counter size: 1
            m = p7_11.match(line)
            if m:
                bind_dict.setdefault(
                    "eqp_counter_size", int(m.groupdict()["eqp_counter_size"])
                )
                continue

            # EQP Counter OID: 0x0
            m = p7_12.match(line)
            if m:
                bind_dict.setdefault(
                    "eqp_counter_oid", m.groupdict()["eqp_counter_oid"]
                )
                continue

            # Meter Set info
            m = p8.match(line)
            if m:
                meter_info_dict = bind_dict.setdefault("meter_set_info", {})
                continue

            # CIR: 1000000000
            m = p8_1.match(line)
            if m:
                meter_cnt_dict = meter_info_dict.setdefault(str(meter_set_count), {})
                meter_cnt_dict.setdefault("cir", int(m.groupdict()["cir"]))
                meter_set_count += 1
                continue

            # EIR: 1000000000
            m = p8_2.match(line)
            if m:
                meter_cnt_dict.setdefault("eir", int(m.groupdict()["eir"]))
                continue

            # Profile OID: 0x832
            m = p8_3.match(line)
            if m:
                meter_cnt_dict.setdefault("profile_oid", m.groupdict()["profile_oid"])
                continue

            # Action Profile OID: 0x110
            m = p8_4.match(line)
            if m:
                meter_cnt_dict.setdefault(
                    "action_profile_oid", m.groupdict()["action_profile_oid"]
                )
                continue

        return ret_dict


class ShowPlatformSoftwareFedQosInterfaceIngressNpdDetailed(
    ShowPlatformSoftwareFedQosInterfaceSuperParser
):
    """Parser for show platform software fed {switch} {mode} qos interface {interface} ingress npd detailed"""

    cli_command = [
        "show platform software fed {switch} {mode} qos interface {interface} ingress npd detailed",
        "show platform software fed {mode} qos interface {interface} ingress npd detailed",
    ]

    def cli(self, mode, interface, switch=None, output=None):
        return super().cli(mode=mode, interface=interface, switch=switch, output=output)


class ShowPlatformSoftwareFedQosInterfaceIngressNpd(
    ShowPlatformSoftwareFedQosInterfaceSuperParser
):
    """Parser for show platform software fed {switch} {mode} qos interface {interface} ingress npd"""

    cli_command = [
        "show platform software fed {switch} {mode} qos interface {interface} ingress npd",
        "show platform software fed {mode} qos interface {interface} ingress npd",
    ]

    def cli(self, mode, interface, switch=None, output=None):
        return super().cli(mode=mode, interface=interface, switch=switch, output=output)


class ShowPlatformSoftwareFedQosInterfaceEgressSdkDetailed(
    ShowPlatformSoftwareFedQosInterfaceSuperParser
):
    """Parser for show platform software fed {switch} {mode} qos interface {interface} egress sdk detailed"""

    cli_command = [
        "show platform software fed {switch} {mode} qos interface {interface} egress sdk detailed",
        "show platform software fed {mode} qos interface {interface} egress sdk detailed",
    ]

    def cli(self, mode, interface, switch=None, output=None):
        return super().cli(mode=mode, interface=interface, switch=switch, output=output)


class ShowPlatformSoftwareFedQosInterfaceIngressSdk(
    ShowPlatformSoftwareFedQosInterfaceSuperParser
):
    """Parser for show platform software fed {switch} {mode} qos interface {interface} ingress sdk"""

    cli_command = [
        "show platform software fed {switch} {mode} qos interface {interface} ingress sdk",
        "show platform software fed {mode} qos interface {interface} ingress sdk",
    ]

    def cli(self, mode, interface, switch=None, output=None):
        return super().cli(mode=mode, interface=interface, switch=switch, output=output)


class ShowPlatformSoftwareFedQosInterfaceIngressSdkDetailed(
    ShowPlatformSoftwareFedQosInterfaceSuperParser
):
    """Parser for show platform software fed {switch} {mode} qos interface {interface} ingress sdk detailed"""

    cli_command = [
        "show platform software fed {switch} {mode} qos interface {interface} ingress sdk detailed",
        "show platform software fed {mode} qos interface {interface} ingress sdk detailed",
    ]

    def cli(self, mode, interface, switch=None, output=None):
        return super().cli(mode=mode, interface=interface, switch=switch, output=output)


class ShowPlatformSoftwareFedQosInterfaceEgressNpdDetailed(
    ShowPlatformSoftwareFedQosInterfaceSuperParser
):
    """Parser for show platform software fed {switch} {mode} qos interface {interface} egress npd detailed"""

    cli_command = [
        "show platform software fed {switch} {mode} qos interface {interface} egress npd detailed",
        "show platform software fed {mode} qos interface {interface} egress npd detailed",
    ]

    def cli(self, mode, interface, switch=None, output=None):
        return super().cli(mode=mode, interface=interface, switch=switch, output=output)


class ShowPlatformSoftwareFedQosInterfaceIngressNpiDetailedSchema(MetaParser):
    """Schema for show platform software fed {switch} {mode} qos interface {interface} ingress npi detailed"""

    schema = {
        Optional("interface"): {
            Any(): {
                "cgid": str,
                "no_of_classes": int,
                "tcg_ref_count": int,
                "filter_state": str,
                "vmr_state": str,
            }
        },
        "classmap": {
            Any(): {
                "cgid": str,
                "clid": str,
                "tccg_ref_count": int,
                "null_bind_count": int,
                "class_seq_number": str,
                "child_classes": int,
                Optional("filter"): {Any(): {"value": str}},
            }
        },
        Optional("tcg"): {
            "npi_tcg": {
                "config_state": str,
                "operational_state": str,
                "parent_info": list,
                "child_tcg": int,
                "mark_action": int,
                "police_action": int,
                "queue_action": int,
                "no_of_tccg": int,
            },
            Optional("tccg"): {
                Any(): {
                    "class_map_name": str,
                    "clid": str,
                    "child_cgid": str,
                    "null_bind": bool,
                    Optional("action"): {
                        Any(): {
                            "action_type": str,
                            "marking_method": str,
                            Optional("mark_value"): int,
                            Optional("mark_type"): str,
                            "qos_group": int,
                            "traffic_class": int,
                            "discard_class": int,
                            Optional("table_id"): str,
                            Optional("table_name"): str,
                            Optional("map"): {Any(): {Any(): int}},
                            Optional("default_value"): int,
                            Optional("default_behavior"): str,
                        }
                    },
                }
            },
        },
    }


class ShowPlatformSoftwareFedQosInterfaceIngressNpiDetailed(
    ShowPlatformSoftwareFedQosInterfaceIngressNpiDetailedSchema
):
    """Parser for show platform software fed {switch} {mode} qos interface {interface} ingress npi detailed"""

    cli_command = [
        "show platform software fed {switch} {mode} qos interface {interface} ingress npi detailed",
        "show platform software fed {mode} qos interface {interface} ingress npi detailed",
    ]

    def cli(self, mode, interface, switch=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(
                    switch=switch, mode=mode, interface=interface
                )
            else:
                cmd = self.cli_command[1].format(mode=mode, interface=interface)
            output = self.device.execute(cmd)

        # [HundredGigE1/0/5, map1, Ingress]: CGID = 0x738310
        # [HundredGigE1/0/5.100, map1, Ingress]: CGID = 0x738310
        p1 = re.compile(r"^\[(?P<interface>[\w\/\.\-]+),.+$")

        # cgid: 0x738310
        p1_1 = re.compile(r"^cgid:\s+(?P<cgid>\w+)$")
        # No of classes: 4
        p1_2 = re.compile(r"^No of classes:\s+(?P<no_of_classes>\d+)$")

        # TCG ref count: 1
        p1_3 = re.compile(r"^TCG ref count:\s+(?P<tcg_ref_count>\d+)$")

        # Filter state: UP TO DATE
        p1_4 = re.compile(r"^Filter state:\s+(?P<filter_state>[\w\s]+)$")

        # VMR state: UP TO DATE
        p1_5 = re.compile(r"^VMR state:\s+(?P<vmr_state>[\w\s]+)$")

        # Classmap Information
        p2 = re.compile(r"^Classmap Information$")

        # Class name: cs1(cgid: 0x738310, clid: 0x6A611)
        p2_1 = re.compile(
            r"^Class name: (?P<class_name>[\w\s\-]+)\(cgid: (?P<cgid>\w+)\, clid: (?P<clid>\w+)\)$"
        )
        # TCCG ref count: 1
        p2_2 = re.compile(r"^TCCG ref count: (?P<tccg_ref_count>\d+)$")

        # NULL Bind count: 1
        p2_3 = re.compile(r"^NULL Bind count: (?P<null_bind_count>\d+)$")

        # Class seq no.: 0x1FFFFF
        p2_4 = re.compile(r"^Class seq no\.: (?P<class_seq_number>\w+)$")
        # No of child classes: 0
        p2_5 = re.compile(r"^No of child classes: (?P<child_classes>\d+)$")

        # Filter: FILTER_MATCH_IP_DSCP
        p2_6 = re.compile(r"^Filter: (?P<filter_name>[\w\s]+)$")

        # Value: 0x8
        p2_7 = re.compile(r"^Value: (?P<value>\w+)$")

        # TCG Information
        p3 = re.compile(r"^TCG Information$")

        # NPI TCG Values:
        p3_1 = re.compile(r"^NPI TCG Values:$")

        # Config state: VALID
        p3_2 = re.compile(r"^Config state: (?P<config_state>[\w\s]+)$")
        # Operational state: IN HARDWARE
        p3_3 = re.compile(r"^Operational state: (?P<operational_state>[\w\s]+)$")

        # Parent Info: [0x0, 0x0, 0]
        p3_4 = re.compile(r"^Parent Info: \[(?P<parent_info>[\w\s\,]+)\]$")

        # No of Child TCGs: 0
        p3_5 = re.compile(r"^No of Child TCGs: (?P<child_tcg>\d+)$")

        # Mark Action count: 1
        p3_6 = re.compile(r"^Mark Action count: (?P<mark_action>\d+)$")

        # Police Action count: 3
        p3_7 = re.compile(r"^Police Action count: (?P<police_action>\d+)$")

        # Queue Action count: 0
        p3_8 = re.compile(r"^Queue Action count: (?P<queue_action>\d+)$")

        # No of TCCGs: 4
        p3_9 = re.compile(r"^No of TCCGs: (?P<no_of_tccg>\d+)$")

        #  TCCG 0:
        p4 = re.compile(r"^TCCG (?P<tccg>\d+):$")

        # Class-map name: cs5(0x6A651)
        p4_1 = re.compile(
            r"^Class-map name: (?P<class_map_name>[\w\s\-]+)\((?P<clid>\w+)\)$"
        )

        # Child cgid: 0x0
        p4_2 = re.compile(r"^Child cgid: (?P<child_cgid>\w+)$")

        # Null Bind: True
        p4_3 = re.compile(r"^Null Bind: (?P<null_bind>\w+)$")

        # Action 0
        p4_4 = re.compile(r"^Action (?P<action>\d+)$")

        # Action Type: Marking
        p4_5 = re.compile(r"^Action Type: (?P<action_type>[\w\s]+)$")

        # Marking Method : Normal
        p4_6 = re.compile(r"^Marking Method : (?P<marking_method>[\w\s]+)$")

        # Mark value: 32
        p4_7 = re.compile(r"^Mark value: (?P<mark_value>\d+)$")

        # Mark Type: DSCP
        p4_8 = re.compile(r"^Mark Type: (?P<mark_type>\w+)$")

        # QoS Group: 255
        p4_9 = re.compile(r"^QoS Group: (?P<qos_group>\d+)$")
        # Traffic Class: 255
        p4_10 = re.compile(r"^Traffic Class: (?P<traffic_class>\d+)$")

        # Discard Class: 255
        p4_11 = re.compile(r"^Discard Class: (?P<discard_class>\d+)$")

        # Table id: 0x3B8D
        p4_12 = re.compile(r"^Table id: (?P<table_id>\w+)$")

        # Table Name: t1
        p4_13 = re.compile(r"^Table Name: (?P<table_name>\w+)$")

        # Map: L2 COS -> L2 COS
        # Map: DSCP -> DSCP
        # Map: L2 COS -> Traffic Class
        p4_14 = re.compile(r"^Map: (?P<map>.+\->.+)$")

        # 1 -> 7
        # 2 -> 6
        p4_15 = re.compile(r"^(?P<key>\d+)\s+\->\s+(?P<value>\d+)$")

        # Default value: 0
        p4_16 = re.compile(r"^Default value: (?P<default_value>\d+)$")

        # Default Behavior: Copy
        p4_17 = re.compile(r"^Default Behavior: (?P<default_behavior>.+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # [HundredGigE1/0/5, map1, Ingress]: CGID = 0x738310
            m = p1.match(line)
            if m:
                int_dict = ret_dict.setdefault("interface", {}).setdefault(
                    Common.convert_intf_name(m.groupdict()["interface"]), {}
                )
                continue
            # cgid: 0x738310
            m = p1_1.match(line)
            if m:
                int_dict.setdefault("cgid", m.groupdict()["cgid"])
                continue

            # No of classes: 4
            m = p1_2.match(line)
            if m:
                int_dict.setdefault(
                    "no_of_classes", int(m.groupdict()["no_of_classes"])
                )
                continue

            # TCG ref count: 1
            m = p1_3.match(line)
            if m:
                int_dict.setdefault(
                    "tcg_ref_count", int(m.groupdict()["tcg_ref_count"])
                )
                continue
            # Filter state: UP TO DATE
            m = p1_4.match(line)
            if m:
                int_dict.setdefault("filter_state", m.groupdict()["filter_state"])
                continue
            # VMR state: UP TO DATE
            m = p1_5.match(line)
            if m:
                int_dict.setdefault("vmr_state", m.groupdict()["vmr_state"])
                continue
            # Classmap Information
            m = p2.match(line)
            if m:
                classmap_dict = ret_dict.setdefault("classmap", {})
                continue

            # Class name: cs1(cgid: 0x738310, clid: 0x6A611)
            m = p2_1.match(line)
            if m:
                class_dict = classmap_dict.setdefault(m.groupdict()["class_name"], {})
                class_dict["cgid"] = m.groupdict()["cgid"]
                class_dict["clid"] = m.groupdict()["clid"]
                continue

            # TCCG ref count: 1
            m = p2_2.match(line)
            if m:
                class_dict["tccg_ref_count"] = int(m.groupdict()["tccg_ref_count"])
                continue

            # NULL Bind count: 1
            m = p2_3.match(line)
            if m:
                class_dict["null_bind_count"] = int(m.groupdict()["null_bind_count"])
                continue

            # Class seq no.: 0x1FFFFF
            m = p2_4.match(line)
            if m:
                class_dict["class_seq_number"] = m.groupdict()["class_seq_number"]
                continue

            # No of child classes: 0
            m = p2_5.match(line)
            if m:
                class_dict["child_classes"] = int(m.groupdict()["child_classes"])
                continue

            # Filter: FILTER_MATCH_IP_DSCP
            m = p2_6.match(line)
            if m:
                filt_dict = class_dict.setdefault("filter", {}).setdefault(
                    m.groupdict()["filter_name"].lower(), {}
                )
                continue

            # Value: 0x8
            m = p2_7.match(line)
            if m:
                filt_dict["value"] = m.groupdict()["value"]
                continue

            # TCG Information
            m = p3.match(line)
            if m:
                tcg_dict = ret_dict.setdefault("tcg", {})
                continue
            # NPI TCG Values:
            m = p3_1.match(line)
            if m:
                npi_tcg_dict = tcg_dict.setdefault("npi_tcg", {})
                continue
            # Config state: VALID
            m = p3_2.match(line)
            if m:
                npi_tcg_dict["config_state"] = m.groupdict()["config_state"]
                continue
            # Operational state: IN HARDWARE
            m = p3_3.match(line)
            if m:
                npi_tcg_dict["operational_state"] = m.groupdict()["operational_state"]
                continue

            # Parent Info: [0x0, 0x0, 0]
            m = p3_4.match(line)
            if m:
                npi_tcg_dict["parent_info"] = m.groupdict()["parent_info"].split(", ")
                continue

            # No of Child TCGs: 0
            m = p3_5.match(line)
            if m:
                npi_tcg_dict["child_tcg"] = int(m.groupdict()["child_tcg"])
                continue

            # Mark Action count: 1
            m = p3_6.match(line)
            if m:
                npi_tcg_dict["mark_action"] = int(m.groupdict()["mark_action"])
                continue
            # Police Action count: 3
            m = p3_7.match(line)
            if m:
                npi_tcg_dict["police_action"] = int(m.groupdict()["police_action"])
                continue

            # Queue Action count: 0
            m = p3_8.match(line)
            if m:
                npi_tcg_dict["queue_action"] = int(m.groupdict()["queue_action"])
                continue

            # No of TCCGs: 4
            m = p3_9.match(line)
            if m:
                npi_tcg_dict["no_of_tccg"] = int(m.groupdict()["no_of_tccg"])
                continue

            #  TCCG 0:
            m = p4.match(line)
            if m:
                tccg_dict = tcg_dict.setdefault("tccg", {}).setdefault(
                    m.groupdict()["tccg"], {}
                )
                continue

            # Class-map name: cs5(0x6A651)
            m = p4_1.match(line)
            if m:
                tccg_dict["class_map_name"] = m.groupdict()["class_map_name"]
                tccg_dict["clid"] = m.groupdict()["clid"]
                continue

            # Child cgid: 0x0
            m = p4_2.match(line)
            if m:
                tccg_dict["child_cgid"] = m.groupdict()["child_cgid"]
                continue

            # Null Bind: True
            m = p4_3.match(line)
            if m:
                tccg_dict["null_bind"] = (
                    True if m.groupdict()["null_bind"] == "True" else False
                )
                continue

            # Action 0
            m = p4_4.match(line)
            if m:
                action_dict = tccg_dict.setdefault("action", {}).setdefault(
                    m.groupdict()["action"], {}
                )
                continue

            # Action Type: Marking
            m = p4_5.match(line)
            if m:
                action_dict["action_type"] = m.groupdict()["action_type"]
                continue

            # Marking Method : Normal
            m = p4_6.match(line)
            if m:
                action_dict["marking_method"] = m.groupdict()["marking_method"]
                continue

            # Mark value: 32
            m = p4_7.match(line)
            if m:
                action_dict["mark_value"] = int(m.groupdict()["mark_value"])
                continue

            # Mark Type: DSCP
            m = p4_8.match(line)
            if m:
                action_dict["mark_type"] = m.groupdict()["mark_type"]
                continue

            # QoS Group: 255
            m = p4_9.match(line)
            if m:
                action_dict["qos_group"] = int(m.groupdict()["qos_group"])
                continue

            # Traffic Class: 255
            m = p4_10.match(line)
            if m:
                action_dict["traffic_class"] = int(m.groupdict()["traffic_class"])
                continue

            # Discard Class: 255
            m = p4_11.match(line)
            if m:
                action_dict["discard_class"] = int(m.groupdict()["discard_class"])
                continue

            # Table id: 0x3B8D
            m = p4_12.match(line)
            if m:
                action_dict["table_id"] = m.groupdict()["table_id"]
                continue

            # Table Name: t1
            m = p4_13.match(line)
            if m:
                action_dict["table_name"] = m.groupdict()["table_name"]
                continue

            # Map: L2 COS -> L2 COS
            # Map: DSCP -> DSCP
            # L2 COS -> Traffic Class
            m = p4_14.match(line)
            if m:
                map = (
                    m.groupdict()["map"]
                    .strip()
                    .replace("->", "to")
                    .replace(" ", "_")
                    .lower()
                )
                map_dict = action_dict.setdefault("map", {}).setdefault(map, {})
                continue

            # 1 -> 7
            # 2 -> 6
            m = p4_15.match(line)
            if m:
                map_dict[int(m.groupdict()["key"])] = int(m.groupdict()["value"])
                continue

            # Default value: 0
            m = p4_16.match(line)
            if m:
                action_dict["default_value"] = int(m.groupdict()["default_value"])
                continue

            # Default Behavior: Copy
            m = p4_17.match(line)
            if m:
                action_dict["default_behavior"] = m.groupdict()["default_behavior"]
                continue

        return ret_dict