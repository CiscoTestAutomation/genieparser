"""show_platform_software_fed.py

    * 'show platform software fed active fnf et-analytics-flows'
    * 'show platform software fed active inject packet-capture detailed'
    * 'show platform software fed switch active ifm mappings lpn'
    * 'show platform software fed switch active ifm mappings lpn | include {interface}'
    * 'show platform software fed switch active ptp domain'
    * 'show platform software fed switch active ptp interface {interface}'
    * 'show platform software fed active acl usage'
    * 'show platform software fed active acl usage | include {aclName}'
    * 'show platform software fed switch {mode} port summary'
    * 'show platform software fed switch active ipsec counters if-id all'
    * 'show platform software fed {switch} active vt counter'
    * 'show platform software fed switch active vt all '
    * 'show platform software fed switch <state> ifm if-id <if_id>'
    * 'show platform software fed active vp summary interface if_id {interface_id}'
    * 'show platform software fed {switch} active ifm interfaces vlan'
    * 'show platform software fed active ifm interfaces vlan'
    * 'show platform software fed switch {switch} vp key {if_id} {vlan_id}'
    * 'show platform software fed active vt hardware if-id {ifid}'
    * 'show platform software fed switch {switch_var} vt hardware if-id {ifid}'
    * 'show platform software fed {switch} active ifm interfaces {label}'
    * 'show platform software fed active ifm interfaces {label}'
    * 'show platform software fed active ptp domain'
    * 'show platform software fed {switch} {mode} security-fed ipsg if-id {if_id}'
    * 'show platform software fed {mode} security-fed ipsg if-id {if_id}'
    * 'show platform software fed switch {switch} vp key {if_id} {vlan_id}'
    * 'show platform software fed switch {switch} fnf flow-record asic {asic} start-index {index} num-flows {flow_num}'
    * 'show platform software fed switch {switch} {mode} if-id {if_id}'
    * 'show platform software fed switch active nat interfaces'
    * 'show platform software fed switch active nat rules'
    * 'show platform software fed active drop packet-capture interface-stats'
    * 'show platform software fed active drop packet-capture statistics'
    * 'show platform software fed switch {switch_num} stp-vlan {vlan_id}'
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

class ShowPlatformSoftwareFedSwitchAclIfIdSchema(MetaParser):
    """Schema for show platform software fed switch {switch} {mode} if-id {if-id}"""

    schema = {
        "int_info": {
            "intf_type": str,
            "interface_client_mac": str,
            "interface_mac": str,
            "intfinfo": str,
            "intf_handle": str,
            "interface_type": str,
            "intf_if_id": str,
            "intf_direction": str,
            "intf_protocol_type": str,
            "policy_intf_handle": str,
            "policy_handle": str,
        },
        "policy_info": {
            "policy_info_handle": str,
            "policy_info_name": str,
            "policy_info_id": int,
            "policy_info_protocol": str,
            "policy_info_feature": str,
            "policy_number_of_acls": int,
        },
    }


class ShowPlatformSoftwareFedSwitchAclIfId(ShowPlatformSoftwareFedSwitchAclIfIdSchema):
    """Parser for show platform software fed switch {switch} {mode} if-id {if-id}"""

    cli_command = ["show platform software fed switch {switch} {mode} if-id {if_id}"]

    def cli(self, switch=None, mode=None, if_id=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(switch=switch, mode=mode, if_id=if_id)

            output = self.device.execute(cmd)

        ret_dict = {}

        # ##  INTFACE INFO: (INTF_TYPE: Group)
        p1 = re.compile(
            r"^\#\#\s\sINTFACE\sINFO\:\s\(INTF\_TYPE\:\s+(?P<intf_type>\S+)\)$"
        )

        # INTERFACE: Client MAC 00da.5516.1903
        p2 = re.compile(
            r"^INTERFACE\:\sClient\sMAC\s(?P<interface_client_mac>[\w\.]+)$"
        )

        # MAC 00da.5516.1903
        p3 = re.compile(r"^MAC\s(?P<interface_mac>[\w\.]+)$")

        #     intfinfo: 0x73e7d8169408
        p4 = re.compile(r"^intfinfo\:\s(?P<intfinfo>\w+)$")

        #     Interface handle: 0x3f0001ad
        p5 = re.compile(r"^Interface\shandle\:\s(?P<intf_handle>\w+)$")

        # Interface Type: Group
        p6 = re.compile(r"^Interface\s+Type:\s+(?P<interface_type>\w+)$")

        #     if-id: 0x000000001a4bff14
        p7 = re.compile(r"^if\-id\:\s(?P<intf_if_id>\w+)$")

        # Direction:  Input
        p8 = re.compile(r"^Direction\:\s\s(?P<intf_direction>\w+)$")

        # Protocol Type:IP
        p9 = re.compile(r"^Protocol\sType\:(?P<intf_protocol_type>\w+)$")

        # Policy Intface Handle: 0x1b00011f
        p10 = re.compile(r"^Policy\sIntface\sHandle\:\s(?P<policy_intf_handle>\w+)$")

        #     Policy Handle: 0x80000ba
        p11 = re.compile(r"^Policy\sHandle\:\s(?P<policy_handle>\w+)$")

        #     Policy handle       : 0x080000ba
        p12 = re.compile(r"^Policy\shandle\s{7}\:\s(?P<policy_info_handle>\w+)$")

        # Policy name         : implicit_deny_v6!implicit_deny:xACSACLx-IPV6-PERMIT_ALL_IPV6_TRAFFIC-61117e44!xACSACLx-IP-PERMIT_ALL_IPV4_TRAFFIC-57f6b0d3:
        p13 = re.compile(r"^Policy\sname\s{9}\:\s(?P<policy_info_name>[\w\-\!\_\:]+)$")

        # ID                  : 1296
        p14 = re.compile(r"^ID\s{18}\:\s(?P<policy_info_id>\d+)$")

        # Protocol            : [3] IPV4
        p15 = re.compile(r"^Protocol\s{12}:\s(?P<policy_info_protocol>[\[\]\s\w]+)$")

        # Feature             : [40] AAL_FEATURE_GACL
        p16 = re.compile(r"^Feature\s{13}\:\s(?P<policy_info_feature>[\[\]\_\s\w]+)$")

        # Number of ACLs      : 1
        p17 = re.compile(r"^Number\sof\sACLs\s{6}\:\s(?P<policy_number_of_acls>\d)$")

        for line in output.splitlines():
            line = line.strip()

            # ##  INTFACE INFO: (INTF_TYPE: Group)
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["intf_type"] = dict_val["intf_type"]
                continue

            # INTERFACE: Client MAC 00da.5516.1903
            m = p2.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["interface_client_mac"] = dict_val["interface_client_mac"]
                continue

            # MAC 00da.5516.1903
            m = p3.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["interface_mac"] = dict_val["interface_mac"]
                continue

            #     intfinfo: 0x73e7d8169408
            m = p4.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["intfinfo"] = dict_val["intfinfo"]
                continue

            #     Interface handle: 0x3f0001ad
            m = p5.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["intf_handle"] = dict_val["intf_handle"]
                continue

            #     Interface Type: Group
            m = p6.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["interface_type"] = dict_val["interface_type"]
                continue

            #    if-id: 0x000000001a4bff14
            m = p7.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["intf_if_id"] = dict_val["intf_if_id"]
                continue

            #    Direction:  Input
            m = p8.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["intf_direction"] = dict_val["intf_direction"]
                continue

            # Protocol Type:IP
            m = p9.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["intf_protocol_type"] = dict_val["intf_protocol_type"]
                continue

            # Policy Intface Handle: 0x1b00011f
            m = p10.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["policy_intf_handle"] = dict_val["policy_intf_handle"]
                continue

            #     Policy Handle: 0x80000ba
            m = p11.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["policy_handle"] = dict_val["policy_handle"]
                continue

            #     Policy handle       : 0x080000ba
            m = p12.match(line)
            if m:
                dict_val = m.groupdict()
                if "policy_info" not in ret_dict:
                    int_info = ret_dict.setdefault("policy_info", {})
                int_info["policy_info_handle"] = dict_val["policy_info_handle"]
                continue

            # Policy name         : implicit_deny_v6!implicit_deny:xACSACLx-IPV6-PERMIT_ALL_IPV6_TRAFFIC-61117e44!xACSACLx-IP-PERMIT_ALL_IPV4_TRAFFIC-57f6b0d3:
            m = p13.match(line)
            if m:
                dict_val = m.groupdict()
                if "policy_info" not in ret_dict:
                    int_info = ret_dict.setdefault("policy_info", {})
                int_info["policy_info_name"] = dict_val["policy_info_name"]
                continue

            # ID                  : 1296
            m = p14.match(line)
            if m:
                dict_val = m.groupdict()
                if "policy_info" not in ret_dict:
                    int_info = ret_dict.setdefault("policy_info", {})
                int_info["policy_info_id"] = int(dict_val["policy_info_id"])
                continue

            # Protocol            : [3] IPV4
            m = p15.match(line)
            if m:
                dict_val = m.groupdict()
                if "policy_info" not in ret_dict:
                    int_info = ret_dict.setdefault("policy_info", {})
                int_info["policy_info_protocol"] = dict_val["policy_info_protocol"]
                continue

            # Feature             : [40] AAL_FEATURE_GACL
            m = p16.match(line)
            if m:
                dict_val = m.groupdict()
                if "policy_info" not in ret_dict:
                    int_info = ret_dict.setdefault("policy_info", {})
                int_info["policy_info_feature"] = dict_val["policy_info_feature"]
                continue

            # Number of ACLs      : 1
            m = p17.match(line)
            if m:
                dict_val = m.groupdict()
                if "policy_info" not in ret_dict:
                    int_info = ret_dict.setdefault("policy_info", {})
                int_info["policy_number_of_acls"] = int(
                    dict_val["policy_number_of_acls"]
                )
                continue

        return ret_dict


class ShowPlatformSoftwareFedactiveFnfEtAnalyticsFlowsSchema(MetaParser):
    """Schema for
    * show platform software fed active fnf et-analytics-flows
    """

    schema = {
        "current-eta-records": int,
        "excess-packets-received": int,
        "excess-syn-received": int,
        "total-eta-fnf": int,
        "total-eta-idp": int,
        "total-eta-records": int,
        "total-eta-splt": int,
        "total-packets-out-of-order": int,
        "total-packets-received": int,
        "total-packets-retransmitted": int,
    }


class ShowPlatformSoftwareFedactiveFnfEtAnalyticsFlows(
    ShowPlatformSoftwareFedactiveFnfEtAnalyticsFlowsSchema
):
    """Parser for
    * show platform software fed active fnf et-analytics-flows
    """

    cli_command = "show platform software fed active fnf et-analytics-flows"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Total packets received     : 80
        p1 = re.compile(r"Total +packets +received +: +(?P<total_pkts>\d+)")

        # Excess packets received    : 60
        p2 = re.compile(r"Excess +packets +received +: +(?P<excess_pkts>\d+)")

        # Excess syn received        : 0
        p3 = re.compile(r"Excess +syn +received +: +(?P<excess_syn>\d+)")

        # Total eta records added    : 4
        p4 = re.compile(r"Total +eta +records +added +: +(?P<tot_eta>\d+)")

        # Current eta records        : 0
        p5 = re.compile(r"Current +eta +records +: +(?P<cur_eta>\d+)")

        # Total eta splt exported    : 2
        p6 = re.compile(r"Total +eta +splt +exported +: +(?P<eta_splt>\d+)")

        # Total eta IDP exported     : 2
        p7 = re.compile(r"Total +eta +IDP +exported +: +(?P<eta_idp>\d+)")

        # Total eta-fnf records      : 2
        p8 = re.compile(r"Total +eta\-fnf +records +: +(?P<eta_fnf>\d+)")

        # Total retransmitted pkts   : 0
        p9 = re.compile(r"Total +retransmitted +pkts +: +(?P<retr_pkts>\d+)")

        # Total out of order pkts    : 0
        p10 = re.compile(r"Total +out +of +order +pkts +: +(?P<order_pkts>\d+)")

        for line in out.splitlines():
            line = line.strip()

            # Total packets received     : 80
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                ret_dict["total-packets-received"] = int(group["total_pkts"])

            # Excess packets received    : 60
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                ret_dict["excess-packets-received"] = int(group["excess_pkts"])

            # Excess syn received        : 0
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                ret_dict["excess-syn-received"] = int(group["excess_syn"])

            # Total eta records added    : 4
            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()
                ret_dict["total-eta-records"] = int(group["tot_eta"])

            # Current eta records        : 0
            m5 = p5.match(line)
            if m5:
                group = m5.groupdict()
                ret_dict["current-eta-records"] = int(group["cur_eta"])

            # Total eta splt exported    : 2
            m6 = p6.match(line)
            if m6:
                group = m6.groupdict()
                ret_dict["total-eta-splt"] = int(group["eta_splt"])

            # Total eta IDP exported     : 2
            m7 = p7.match(line)
            if m7:
                group = m7.groupdict()
                ret_dict["total-eta-idp"] = int(group["eta_idp"])

            # Total eta-fnf records      : 2
            m8 = p8.match(line)
            if m8:
                group = m8.groupdict()
                ret_dict["total-eta-fnf"] = int(group["eta_fnf"])

            # Total retransmitted pkts   : 0
            m9 = p9.match(line)
            if m9:
                group = m9.groupdict()
                ret_dict["total-packets-retransmitted"] = int(group["retr_pkts"])

            # Total out of order pkts    : 0
            m10 = p10.match(line)
            if m10:
                group = m10.groupdict()
                ret_dict["total-packets-out-of-order"] = int(group["order_pkts"])
        return ret_dict


# =============================================
# Schema for 'show platform software fed active acl counters hardware'
# =============================================
class ShowPlatformSoftwareFedactiveAclCountersHardwareSchema(MetaParser):
    """Schema for
    * show platform software fed active acl counters hardware
    """

    schema = {
        "counters": {
            "unknown_stat_counter": int,
            "ingress_ipv4_forward": int,
            "ingress_ipv4_forward_from_cpu": int,
            "ingress_ipv4_pacl_drop": int,
            "ingress_ipv4_vacl_drop": int,
            "ingress_ipv4_racl_drop": int,
            "ingress_ipv4_gacl_drop": int,
            "ingress_ipv4_racl_drop_and_log": int,
            "ingress_ipv4_vacl_drop_and_log": int,
            "ingress_ipv4_pacl_cpu": int,
            "ingress_ipv4_vacl_cpu": int,
            "ingress_ipv4_racl_cpu": int,
            "ingress_ipv4_gacl_cpu": int,
            "ingress_ipv4_tcp_mss_cpu": int,
            "ingress_ipv6_forward": int,
            "ingress_ipv6_forward_from_cpu": int,
            "ingress_ipv6_pacl_drop": int,
            "ingress_ipv6_vacl_drop": int,
            "ingress_ipv6_racl_drop": int,
            "ingress_ipv6_gacl_drop": int,
            "ingress_ipv6_racl_drop_and_log": int,
            "ingress_ipv6_vacl_drop_and_log": int,
            "ingress_ipv6_pacl_cpu": int,
            "ingress_ipv6_pacl_sisf_cpu": int,
            "ingress_ipv6_vacl_cpu": int,
            "ingress_ipv6_vacl_sisf_cpu": int,
            "ingress_ipv6_racl_cpu": int,
            "ingress_ipv6_gacl_cpu": int,
            "ingress_ipv6_tcp_mss_cpu": int,
            "ingress_mac_forward": int,
            "ingress_mac_forward_from_cpu": int,
            "ingress_mac_pacl_drop": int,
            "ingress_mac_vacl_drop": int,
            "ingress_mac_racl_drop": int,
            "ingress_mac_gacl_drop": int,
            "ingress_mac_racl_drop_and_log": int,
            "ingress_mac_vacl_drop_and_log": int,
            "ingress_mac_pacl_cpu": int,
            "ingress_mac_vacl_cpu": int,
            "ingress_mac_racl_cpu": int,
            "ingress_mac_gacl_cpu": int,
            "ingress_dai_smac_validation_drop": int,
            "ingress_dai_dmac_validation_drop": int,
            "ingress_dai_ip_validation_drop": int,
            "ingress_arp_acl_permit": int,
            "ingress_arp_acl_drop": int,
            "ingress_auth_acl_drop": int,
            Optional("ingress_ipv4_ipclients_cpu"): int,
            Optional("ingress_ipv6_ipclients_cpu"): int,
            Optional("ingress_ipv4_ipclients_drop"): int,
            Optional("ingress_ipv6_ipclients_drop"): int,
            "egress_ipv4_forward": int,
            "egress_ipv4_forward_to_cpu": int,
            Optional("egress_ipv4_forward_from_cpu"): int,
            "egress_ipv4_pacl_drop": int,
            "egress_ipv4_vacl_drop": int,
            "egress_ipv4_racl_drop": int,
            "egress_ipv4_gacl_drop": int,
            "egress_ipv4_racl_drop_and_log": int,
            "egress_ipv4_vacl_drop_and_log": int,
            "egress_ipv4_pacl_cpu": int,
            "egress_ipv4_vacl_cpu": int,
            "egress_ipv4_racl_cpu": int,
            "egress_ipv4_gacl_cpu": int,
            "egress_ipv4_tcp_mss_cpu": int,
            "egress_ipv6_forward": int,
            "egress_ipv6_forward_to_cpu": int,
            Optional("egress_ipv6_forward_from_cpu"): int,
            "egress_ipv6_pacl_drop": int,
            "egress_ipv6_vacl_drop": int,
            "egress_ipv6_racl_drop": int,
            "egress_ipv6_gacl_drop": int,
            "egress_ipv6_racl_drop_and_log": int,
            "egress_ipv6_vacl_drop_and_log": int,
            "egress_ipv6_pacl_cpu": int,
            "egress_ipv6_vacl_cpu": int,
            "egress_ipv6_racl_cpu": int,
            "egress_ipv6_gacl_cpu": int,
            "egress_ipv6_tcp_mss_cpu": int,
            "egress_mac_forward": int,
            "egress_mac_forward_to_cpu": int,
            Optional("egress_mac_forward_from_cpu"): int,
            "egress_mac_pacl_drop": int,
            "egress_mac_vacl_drop": int,
            "egress_mac_racl_drop": int,
            "egress_mac_gacl_drop": int,
            "egress_mac_racl_drop_and_log": int,
            "egress_mac_vacl_drop_and_log": int,
            "egress_mac_pacl_cpu": int,
            "egress_mac_vacl_cpu": int,
            "egress_mac_racl_cpu": int,
            "egress_mac_gacl_cpu": int,
            "egress_ipv4_cpu_queues_drop": int,
            "egress_ipv4_p2p_drop": int,
            "egress_ipv6_p2p_drop": int,
            "egress_mac_p2p_drop": int,
            "egress_ipv4_p2p_redirect": int,
            "egress_ipv6_p2p_redirect": int,
            "egress_mac_p2p_redirect": int,
            "egress_ipv4_sgacl_drop": int,
            "egress_ipv6_sgacl_drop": int,
            "egress_ipv4_sgacl_test_cell_drop": int,
            "egress_ipv6_sgacl_test_cell_drop": int,
            "egress_ipv4_dns_response_cpu": int,
            "egress_ipv6_dns_response_cpu": int,
            "egress_ipv4_pre_sgacl_forward": int,
        }
    }


class ShowPlatformSoftwareFedactiveAclCountersHardware(
    ShowPlatformSoftwareFedactiveAclCountersHardwareSchema
):
    """Parser for
    * show platform software fed active acl counters hardware
    """

    cli_command = "show platform software fed active acl counters hardware"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # Unknown Stat Counter    : 80
        p1 = re.compile(r"Unknown\s+Stat\s+Counter\s+:\s+(?P<unknown_stats>\d+)")

        # Ingress IPv4 Forward             (0x8d000003):       40365 frames
        # Ingress IPv6 GACL Drop           (0x0a000015):           0 frames
        # Ingress MAC Forward              (0x9100001f):       28270 frames
        # Egress IPv4 Forward              (0x77000030):       20480 frames
        # Egress IPv6 Forward to CPU       (0x5c00003e):           0 frames
        p2 = re.compile(
            r"^(?P<counter_name>.+[^ ])\s+(\(.+\))?:\s+(?P<num_frames>\d+)\s+frames$"
        )

        for line in output.splitlines():
            line = line.strip()

            # Unknown Stat Counter             (0x49000001):      158905 frames
            m = p1.match(line)
            if m:
                group = m.groupdict()
                counters_dict = ret_dict.setdefault("counters", {})
                counters_dict["unknown_stat_counter"] = int(group["unknown_stats"])
                continue

            # Ingress IPv4 Forward             (0x8d000003):       40365 frames
            # Ingress IPv6 GACL Drop           (0x0a000015):           0 frames
            # Ingress MAC Forward              (0x9100001f):       28270 frames
            # Egress IPv4 Forward              (0x77000030):       20480 frames
            # Egress IPv6 Forward to CPU       (0x5c00003e):           0 frames
            m = p2.match(line)
            if m:
                group = m.groupdict()
                counter_name = group["counter_name"].lower().replace(" ", "_")
                counters_dict = ret_dict.setdefault("counters", {})
                counters_dict[counter_name] = int(group["num_frames"])
                continue

        return ret_dict


# ============================================================================
# Schema for 'show platform software fed active inject packet-capture detailed'
# ===========================================================================
class ShowPlatformSoftwareFedActiveInjectPacketCaptureDetailedSchema(MetaParser):
    """Schema for
    * show platform software fed active inject packet-capture detailed
    """

    schema = {
        "inject_packet_capture": str,
        "buffer_wrapping": str,
        "total_captured": int,
        "capture_capacity": int,
        "capture_filter": str,
        "inject_packet_number": {
            Any(): {
                "interface": {
                    "pal": {"iifd": str},
                },
                "metadata": {
                    "cause": str,
                    "sub_cause": str,
                    "q_no": str,
                    "linktype": str,
                },
                "ether_hdr_1": {"dest_mac": str, "src_mac": str},
                "ether_hdr_2": {"ether_type": str},
                "ipv4_hdr_1": {"dest_ip": str, "src_ip": str},
                "ipv4_hdr_2": {"packet_len": str, "ttl": str, "protocol": str},
                "udp_hdr": {"dest_port": str, "src_port": str},
                "doppler_frame_descriptor": {
                    "fdformat": str,
                    "system_ttl": str,
                    "fdtype": str,
                    "span_session_map": str,
                    "qoslabel": str,
                    "fpe_first_header_type": str,
                },
            }
        },
    }


# ================================================================
# Parser for:
#   * 'show platform software fed active inject packet-capture detailed'
# ================================================================
class ShowPlatformSoftwareFedActiveInjectPacketCaptureDetailed(
    ShowPlatformSoftwareFedActiveInjectPacketCaptureDetailedSchema
):
    """Parser for:
    show platform software fed active inject packet-capture detailed
    """

    cli_command = ["show platform software fed active inject packet-capture detailed"]

    def cli(self, output=None):
        """cli for:
        ' show platform software fed active inject packet-capture detailed '
        """

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Inject packet capturing: disabled. Buffer wrapping: disabled
        p1 = re.compile(
            r"^Inject +packet +capturing:+\s+(?P<inject_packet_capture>\w+)\.+\s+"
            r"Buffer +wrapping:\s+(?P<buffer_wrapping>\w+)$"
        )

        # Total captured so far: 4 packets. Capture capacity : 4096 packets
        p2 = re.compile(
            r"^Total +captured +so +far:\s(?P<total_captured>\d)+\s+packets+\.\s+"
            r"Capture +capacity +:\s+(?P<capture_capacity>\d+)+\s+packets$"
        )

        # Capture filter : "udp.port == 9995"
        p3 = re.compile(r"^Capture +filter +: +(?P<capture_filter>.+)$")

        # ------ Inject Packet Number: 1, Timestamp: 2021/09/15 07:40:40.603 ------
        p4 = re.compile(r"^-+\s+Inject +Packet +Number: +(?P<inject_packet_no>\d+)")

        # interface : pal:  [if-id: 0x00000000]
        p5 = re.compile(r"^interface +: pal: \s+\[+if-id: +(?P<iifd>\S+)$")

        # metadata  : cause: 2 [QFP destination lookup], sub-cause: 1, q-no: 0, linktype: MCP_LINK_TYPE_IP [1]
        p6 = re.compile(
            r"^metadata +: +cause: +(?P<cause>.+)"
            r"\s+sub-cause: +(?P<sub_cause>\d+)\, +q-no: +(?P<q_no>\d+)\,"
            r"\s+linktype: +(?P<linktype>.+)"
        )

        # ether hdr : dest mac: 3c57.3104.6a00, src mac: 3c57.3104.6a00
        p7 = re.compile(
            r"^ether +hdr +: +dest +mac: +(?P<dest_mac>\S+)\s+src +mac: +(?P<src_mac>\S+)"
        )

        # ether hdr : ethertype: 0x0800 (IPv4)
        p8 = re.compile(r"^ether +hdr +: +ethertype: +(?P<ether_type>.+)$")

        # ipv4  hdr : dest ip: 111.0.0.2, src ip: 111.0.0.1
        p9 = re.compile(
            r"^ipv4 +hdr +: +dest +ip: +(?P<dest_ip>\S+)\s+src +ip: +(?P<src_ip>\S+)"
        )

        # ipv4  hdr : packet len: 188, ttl: 255, protocol: 17 (UDP)
        p10 = re.compile(
            r"^ipv4 +hdr +: +packet +len: +(?P<packet_len>\d+)\,\s+ttl: +(?P<ttl>\d+)"
            r"\,+\s+protocol: +(?P<protocol>.+)$"
        )

        # udp   hdr : dest port: 9995, src port: 53926
        p11 = re.compile(
            r"^udp +hdr +: +dest +port: +(?P<dest_port>\d+)\,\s+src +port: +(?P<src_port>\d+)"
        )

        # Doppler Frame Descriptor :
        p12 = re.compile(
            r"^Doppler +Frame +Descriptor +:(?P<doppler_frame_descriptor>)$"
        )

        # fdFormat                  = 0x3            systemTtl                 = 0x8
        p13 = re.compile(
            r"^fdFormat\s+\= (?P<fdformat>\S+)\s+systemTtl\s+\= (?P<system_ttl>\S+$)"
        )

        # fdType                    = 0x1            spanSessionMap            = 0
        p14 = re.compile(
            r"^fdType\s+\= (?P<fdtype>\S+)\s+spanSessionMap\s+\= (?P<span_session_map>\S+$)"
        )

        # qosLabel                  = 0x81           fpeFirstHeaderType        = 0
        p15 = re.compile(
            r"^qosLabel\s+\= (?P<qoslabel>\S+)\s+fpeFirstHeaderType\s+\= (?P<fpe_first_header_type>\S+$)"
        )

        ret_dict = {}
        for line in out.splitlines():
            line = line.strip()

            # Inject packet capturing: disabled. Buffer wrapping: disabled
            m = p1.match(line)
            if m:
                ret_dict.update(
                    {
                        "inject_packet_capture": m.groupdict()["inject_packet_capture"],
                        "buffer_wrapping": m.groupdict()["buffer_wrapping"],
                    }
                )
                continue

            # Total captured so far: 4 packets. Capture capacity : 4096 packets
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update(
                    {
                        "total_captured": int(group["total_captured"]),
                        "capture_capacity": int(group["capture_capacity"]),
                    }
                )
                continue

            # Capture filter : "udp.port == 9995"
            m = p3.match(line)
            if m:
                ret_dict.update({"capture_filter": m.groupdict()["capture_filter"]})
                continue

            # ------ Inject Packet Number: 1, Timestamp: 2021/09/15 07:40:40.603 ------
            m = p4.match(line)
            if m:
                group = m.groupdict()
                inject_packet_num = group["inject_packet_no"]
                inject_packet_dict = ret_dict.setdefault(
                    "inject_packet_number", {}
                ).setdefault(inject_packet_num, {})
                continue

            # interface : pal:  [if-id: 0x00000000]
            m = p5.match(line)
            if m:
                group = m.groupdict()
                int_dict = ret_dict["inject_packet_number"][
                    inject_packet_num
                ].setdefault("interface", {})
                pal_dict = ret_dict["inject_packet_number"][inject_packet_num][
                    "interface"
                ].setdefault("pal", {})
                pal_dict["iifd"] = group["iifd"]
                continue

            # metadata  : cause: 2 [QFP destination lookup], sub-cause: 1, q-no: 0, linktype: MCP_LINK_TYPE_IP [1]
            m = p6.match(line)
            if m:
                group = m.groupdict()
                meta_data_dict = ret_dict["inject_packet_number"][
                    inject_packet_num
                ].setdefault("metadata", {})
                meta_data_dict["cause"] = group["cause"]
                meta_data_dict["sub_cause"] = group["sub_cause"]
                meta_data_dict["q_no"] = group["q_no"]
                meta_data_dict["linktype"] = group["linktype"]
                continue

            # ether hdr : dest mac: 3c57.3104.6a00, src mac: 3c57.3104.6a00
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ether_hdr_1_dict = ret_dict["inject_packet_number"][
                    inject_packet_num
                ].setdefault("ether_hdr_1", {})
                ether_hdr_1_dict["dest_mac"] = group["dest_mac"]
                ether_hdr_1_dict["src_mac"] = group["src_mac"]
                continue

            # ether hdr : ethertype: 0x0800 (IPv4)
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ether_hdr_2_dict = ret_dict["inject_packet_number"][
                    inject_packet_num
                ].setdefault("ether_hdr_2", {})
                ether_hdr_2_dict["ether_type"] = group["ether_type"]
                continue

            # ipv4  hdr : dest ip: 111.0.0.2, src ip: 111.0.0.1
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ipv4_hdr_1_dict = ret_dict["inject_packet_number"][
                    inject_packet_num
                ].setdefault("ipv4_hdr_1", {})
                ipv4_hdr_1_dict["dest_ip"] = group["dest_ip"]
                ipv4_hdr_1_dict["src_ip"] = group["src_ip"]
                continue

            # ipv4  hdr : packet len: 188, ttl: 255, protocol: 17 (UDP)
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ipv4_hdr_2_dict = ret_dict["inject_packet_number"][
                    inject_packet_num
                ].setdefault("ipv4_hdr_2", {})
                ipv4_hdr_2_dict["packet_len"] = group["packet_len"]
                ipv4_hdr_2_dict["ttl"] = group["ttl"]
                ipv4_hdr_2_dict["protocol"] = group["protocol"]
                continue

            # udp   hdr : dest port: 9995, src port: 53926
            m = p11.match(line)
            if m:
                group = m.groupdict()
                udp_hdr_dict = ret_dict["inject_packet_number"][
                    inject_packet_num
                ].setdefault("udp_hdr", {})
                udp_hdr_dict["dest_port"] = group["dest_port"]
                udp_hdr_dict["src_port"] = group["src_port"]
                continue

            # Doppler Frame Descriptor :
            m = p12.match(line)
            if m:
                group = m.groupdict()
                doppler_frame_des_dict = ret_dict["inject_packet_number"][
                    inject_packet_num
                ].setdefault("doppler_frame_descriptor", {})
                continue

            # fdFormat                  = 0x3            systemTtl                 = 0x8
            m = p13.match(line)
            if m:
                group = m.groupdict()
                doppler_frame_des_dict["fdformat"] = group["fdformat"]
                doppler_frame_des_dict["system_ttl"] = group["system_ttl"]
                continue

            # fdType                    = 0x1            spanSessionMap            = 0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                doppler_frame_des_dict["fdtype"] = group["fdtype"]
                doppler_frame_des_dict["span_session_map"] = group["span_session_map"]
                continue

            # qosLabel                  = 0x81           fpeFirstHeaderType        = 0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                doppler_frame_des_dict["qoslabel"] = group["qoslabel"]
                doppler_frame_des_dict["fpe_first_header_type"] = group[
                    "fpe_first_header_type"
                ]
                continue

        return ret_dict


# =============================================================================
#  Schema for
#  * 'show platform software fed switch active ifm mappings lpn'
#  * 'show platform software fed switch active ifm mappings lpn | {interface}'
# ==============================================================================
class ShowPlatformSoftwareFedSwitchActiveIfmMappingsLpnSchema(MetaParser):
    """Schema for 'show platform software fed switch active ifm mappings lpn'"""

    schema = {
        "interfaces": {
            Any(): {"lpn": int, "asic": int, "port": int, "if_id": str, "active": str}
        },
    }


# ===============================================================================
#  Parser for
#  * 'show platform software fed switch active ifm mappings lpn'
#  * 'show platform software fed switch active ifm mappings lpn | i {interface}'
# ================================================================================
class ShowPlatformSoftwareFedSwitchActiveIfmMappingsLpn(
    ShowPlatformSoftwareFedSwitchActiveIfmMappingsLpnSchema
):
    """
    Parser for :
        * show platform software fed switch active ifm mappings lpn
    """

    cli_command = [
        "show platform software fed switch active ifm mappings lpn",
        "show platform software fed switch active ifm mappings lpn | include {interface}",
    ]

    def cli(self, interface="", output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        # 19   1     18    TenGigabitEthernet1/0/19   0x0000001b  y
        p = re.compile(
            r"^(?P<lpn>\d+)\s+(?P<asic>\d+)\s+(?P<port>\d+)\s+(?P<interfaces>\S+)\s+(?P<if_id>(0x([\da-fA-F]){8}))\s+(?P<active>\S+)$"
        )

        # initial return dictionary
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # 19    1  18    TenGigabitEthernet1/0/19   0x0000001b  y
            m = p.match(line)
            if m:
                group = m.groupdict()
                interfaces = group["interfaces"]
                sub_dict = ret_dict.setdefault("interfaces", {}).setdefault(
                    interfaces, {}
                )

                lpn = group["lpn"]
                sub_dict["lpn"] = int(lpn)

                asic = group["asic"]
                sub_dict["asic"] = int(asic)

                port = group["port"]
                sub_dict["port"] = int(port)

                if_id = group["if_id"]
                sub_dict["if_id"] = if_id

                active = group["active"]
                sub_dict["active"] = active
                continue
        return ret_dict


# ======================================================================================
#  Schema for
#  * 'show platform software fed {switch} active ifm interfaces {label}'
#  * 'show platform software fed active ifm interfaces {label}'
# =======================================================================================
class ShowPlatformSoftwareFedSwitchActiveIfmInterfacesLabelSchema(MetaParser):
    """Schema for 'show platform software fed {switch} active ifm interfaces {label}'
    'show platform software fed active ifm interfaces {label}'
    """

    schema = {
        "interface_name": {
            Any(): {
                "if_id": str,
                "state": str,
            }
        }
    }


# =======================================================================================
#  Parser for
#  * 'show platform software fed {switch} active ifm interfaces {label}'
#  * 'show platform software fed active ifm interfaces {label}'
# =======================================================================================


class ShowPlatformSoftwareFedSwitchActiveIfmInterfacesLabel(
    ShowPlatformSoftwareFedSwitchActiveIfmInterfacesLabelSchema
):
    """
    Parser for :
        * 'show platform software fed {switch} active ifm interfaces {label}'
        * 'show platform software fed active ifm interfaces {label}'
    """

    cli_command = [
        "show platform software fed {switch} active ifm interfaces {label}",
        "show platform software fed active ifm interfaces {label}",
    ]

    label = ["lisp", "sw-subif"]

    def cli(self, label="", switch=None, output=None):
        if output is None:
            if switch and label:
                output = self.device.execute(
                    self.cli_command[0].format(switch=switch, label=label)
                )
            elif label:
                output = self.device.execute(self.cli_command[1].format(label=label))
            else:
                return ImportError
        else:
            output = output

        # initial return dictionary
        ret_dict = {}

        # LISP0.4103                        0x0000054d          Ready
        # LISP0                             0x0000054c          Ready
        p1 = re.compile(
            r"^(?P<interface_name>LISP0.\w+|LISP0)(?:\s*)(?P<if_id>0x\w+)(?:\s*)(?P<state>\w+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # LISP0.4103                        0x0000054d          Ready
            # LISP0                             0x0000054c          Ready
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface_name = group["interface_name"]
                sub_dict = ret_dict.setdefault("interface_name", {}).setdefault(
                    interface_name, {}
                )
                if_id = group["if_id"]
                sub_dict["if_id"] = str(if_id)
                state = group["state"]
                sub_dict["state"] = str(state)
                continue

        return ret_dict


# =================================================================
#  Schema for 'show platform software fed switch active ptp domain
# ================================================================
class ShowPlatformSoftwareFedSwitchActivePtpDomainSchema(MetaParser):
    """Schema for 'show platform software fed switch {switch} ptp domain"""

    schema = {
        "domain_number": {
            Any(): {
                "profile_type": str,
                "profile_state": str,
                Optional("clock_mode"): str,
                Optional("delay_mechanism"): str,
                Optional("ptp_clock"): str,
                Optional("mean_path_delay_ns"): int,
                "transport_method": str,
                "message_general_ip_dscp": int,
                "message_event_ip_dscp": int,
            }
        },
    }


# =================================================================
#  Parser for 'show platform software fed switch active ptp domain
# ================================================================
class ShowPlatformSoftwareFedSwitchActivePtpDomain(
    ShowPlatformSoftwareFedSwitchActivePtpDomainSchema
):
    """
    Parser for :
        * show platform software fed switch active ptp domain
    """

    cli_command = "show platform software fed switch active ptp domain"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Displaying data for domain number 0
        p1 = re.compile(
            r"^Displaying\sdata\sfor\sdomain\snumber\s(?P<domain_number>\d+)$"
        )

        # Profile Type : DEFAULT
        p2 = re.compile(r"^Profile\sType\s\:\s(?P<profile_type>[a-zA-Z]+)$")

        # Profile State: enabled
        p3 = re.compile(r"^Profile\sState\:\s(?P<profile_state>\S+)$")

        # Clock Mode : BOUNDARY CLOCK
        p4 = re.compile(r"^Clock\sMode\s\:\s(?P<clock_mode>[A-Z\s]+)$")

        # Delay Mechanism: : END-TO-END
        p5 = re.compile(r"^Delay\sMechanism\:\s\:\s(?P<delay_mechanism>[A-Z\-]+)$")

        # PTP clock : 1970-1-24 22:41:20
        p6 = re.compile(r"^PTP\sclock\s\:\s(?P<ptp_clock>[\d\-\:\s]+)$")

        # mean_path_delay 83 nanoseconds
        p7 = re.compile(r"^mean_path_delay\s(?P<mean_path_delay_ns>\d+)\snanoseconds$")

        # Transport Method : 802.3
        p8 = re.compile(r"^Transport\sMethod\s\:\s(?P<transport_method>[\w\.\-]+)$")

        # Message general ip dscp  : 47
        p9 = re.compile(
            r"^Message\sgeneral\sip\sdscp\s+\:\s(?P<message_general_ip_dscp>\d+)$"
        )

        # Message event ip dscp    : 59
        p10 = re.compile(
            r"^Message\sevent\sip\sdscp\s+\:\s(?P<message_event_ip_dscp>\d+)$"
        )

        # initial return dictionary
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Displaying data for domain number 0
            m = p1.match(line)
            if m:
                ret_dict.setdefault("domain_number", {})
                domain_number = m.groupdict()["domain_number"]
                sub_dict = ret_dict["domain_number"].setdefault(int(domain_number), {})
                continue

            # Profile Type : DEFAULT
            m = p2.match(line)
            if m:
                profile_type = m.groupdict()["profile_type"]
                sub_dict["profile_type"] = profile_type
                continue

            # Profile State: enabled
            m = p3.match(line)
            if m:
                profile_state = m.groupdict()["profile_state"]
                sub_dict["profile_state"] = profile_state
                continue

            # Clock Mode : BOUNDARY CLOCK
            m = p4.match(line)
            if m:
                clock_mode = m.groupdict()["clock_mode"]
                sub_dict["clock_mode"] = clock_mode
                continue

            # Delay Mechanism: : END-TO-END
            m = p5.match(line)
            if m:
                delay_mechanism = m.groupdict()["delay_mechanism"]
                sub_dict["delay_mechanism"] = delay_mechanism
                continue

            # PTP clock : 1970-1-24 22:41:20
            m = p6.match(line)
            if m:
                ptp_clock = m.groupdict()["ptp_clock"]
                sub_dict["ptp_clock"] = ptp_clock
                continue

            # mean_path_delay 83 nanoseconds
            m = p7.match(line)
            if m:
                mean_path_delay_ns = m.groupdict()["mean_path_delay_ns"]
                sub_dict["mean_path_delay_ns"] = int(mean_path_delay_ns)
                continue

            # Transport Method : 802.3
            m = p8.match(line)
            if m:
                transport_method = m.groupdict()["transport_method"]
                sub_dict["transport_method"] = transport_method
                continue

            # Message general ip dscp  : 47
            m = p9.match(line)
            if m:
                message_general_ip_dscp = m.groupdict()["message_general_ip_dscp"]
                sub_dict["message_general_ip_dscp"] = int(message_general_ip_dscp)
                continue

            # Message event ip dscp    : 59
            m = p10.match(line)
            if m:
                message_event_ip_dscp = m.groupdict()["message_event_ip_dscp"]
                sub_dict["message_event_ip_dscp"] = int(message_event_ip_dscp)
                continue
        return ret_dict


# ================================================================================
#  Schema for 'show platform software fed switch active ptp interface {interface}'
# ================================================================================
class ShowPlatformSoftwareFedSwitchActivePtpInterfaceInterfaceSchema(MetaParser):
    """Schema for 'show platform software fed switch active ptp interface {interface}'"""

    schema = {
        "ptp_interface": {
            "ptp_info": {
                "if_id": str,
                "version": int,
                Optional("ptp_vlan_is_valid"): str,
                Optional("ptp_vlan_id"): int,
            },
            "port_info": {
                "mac_address": str,
                "clock_identity": str,
                "number": int,
                Optional("mode"): int,
                "state": str,
                "port_enabled": str,
            },
            "num_info": {
                "num_sync_messages_transmitted": int,
                "num_followup_messages_transmitted": int,
                "num_sync_messages_received": int,
                "num_followup_messages_received": int,
                "num_delay_requests_transmitted": int,
                "num_delay_responses_received": int,
                "num_delay_requests_received": int,
                "num_delay_responses_transmitted": int,
            },
            "domain_value": int,
            "profile_type": str,
            "clock_mode": str,
            "delay_mechanism": str,
            "ptt_port_enabled": str,
            "sync_seq_num": int,
            "delay_req_seq_num": int,
            "log_mean_sync_interval": int,
            "log_mean_delay_interval": int,
            Optional("tag_native_vlan"): str,
        }
    }


# =================================================================================
#  Parser for 'show platform software fed switch active ptp interface {interface}'
# =================================================================================
class ShowPlatformSoftwareFedSwitchActivePtpInterfaceInterface(
    ShowPlatformSoftwareFedSwitchActivePtpInterfaceInterfaceSchema
):
    """
    Parser for :
        * show platform software fed switch active ptp interface {interface}
    """

    cli_command = [
        "show platform software fed switch {switch_var} ptp interface {interface}",
        "show platform software fed active ptp interface {interface}",
    ]

    def cli(self, interface="", output=None, switch_var=None):
        if switch_var is None:
            cmd = self.cli_command[1].format(interface=interface)
        else:
            cmd = self.cli_command[0].format(switch_var=switch_var, interface=interface)
        output = output or self.device.execute(cmd)

        # Displaying port data for if_id 2a
        # Displaying port data for if_id 29
        p1 = re.compile(r"^Displaying\sport\sdata\sfor\sif_id\s(?P<if_id>\S+)$")

        # Port Mac Address 34:ED:1B:7D:F2:A1
        p2 = re.compile(r"^Port\sMac\sAddress\s(?P<mac_address>([\da-fA-F]:?).*)$")

        # Port Clock Identity 34:ED:1B:FF:FE:7D:F2:80
        p3 = re.compile(
            r"^Port\sClock\sIdentity\s(?P<clock_identity>([\da-fA-F]:?).*)$"
        )

        # Port number 33
        p4 = re.compile(r"^Port\snumber\s(?P<number>\d+)$")

        # PTP Version 2
        p5 = re.compile(r"^PTP\sVersion\s(?P<version>\d+)$")

        # domain_value 0
        p6 = re.compile(r"^domain_value\s(?P<domain_value>\d+)$")

        # Profile Type: : DEFAULT
        p7 = re.compile(r"^Profile\sType\:\s\:\s(?P<profile_type>\S+)$")

        # Clock Mode : BOUNDARY CLOCK
        p8 = re.compile(r"^Clock\sMode\s\:\s(?P<clock_mode>.*)$")

        # Delay mechanism: End-to-End
        p9 = re.compile(r"^Delay\smechanism\:\s(?P<delay_mechanism>\S+)$")

        # port_enabled: TRUE
        p10 = re.compile(r"^port_enabled\:\s(?P<port_enabled>\S+)$")

        # ptt_port_enabled: TRUE
        p11 = re.compile(r"^ptt_port_enabled\:\s(?P<ptt_port_enabled>\S+)$")

        # Port state: : SLAVE
        p12 = re.compile(r"^Port\sstate\:\s\:\s(?P<state>\S+)$")

        # sync_seq_num 2189
        p13 = re.compile(r"^sync_seq_num\s(?P<sync_seq_num>\d+)$")

        # delay_req_seq_num 0
        p14 = re.compile(r"^delay_req_seq_num\s(?P<delay_req_seq_num>\d+)$")

        # log mean sync interval -3
        p15 = re.compile(
            r"^log\smean\ssync\sinterval\s(?P<log_mean_sync_interval>[-?\d]+)$"
        )

        # log mean delay interval -5
        p16 = re.compile(
            r"^log\smean\sdelay\sinterval\s(?P<log_mean_delay_interval>[-?\d]+)$"
        )

        # ptp vlan is valid : FALSE
        p17 = re.compile(r"^ptp\svlan\sis\svalid\s\:\s(?P<ptp_vlan_is_valid>\S+)$")

        # ptp vlan id 0
        p18 = re.compile(r"^ptp\svlan\sid\s(?P<ptp_vlan_id>\d+)$")

        # port mode 2
        p19 = re.compile(r"^port\smode\s(?P<mode>\d+)$")

        # tag native vlan : FALSE
        p20 = re.compile(r"^tag\snative\svlan\s\:\s(?P<tag_native_vlan>\S+)$")

        # num sync messages transmitted  0
        p21 = re.compile(
            r"^num\ssync\smessages\stransmitted\s+(?P<num_sync_messages_transmitted>\d+)$"
        )

        # num followup messages transmitted  0
        p22 = re.compile(
            r"^num\sfollowup\smessages\stransmitted\s+(?P<num_followup_messages_transmitted>\d+)$"
        )

        # num sync messages received  8758
        p23 = re.compile(
            r"^num\ssync\smessages\sreceived\s+(?P<num_sync_messages_received>\d+)$"
        )

        # num followup messages received  8757
        p24 = re.compile(
            r"^num\sfollowup\smessages\sreceived\s+(?P<num_followup_messages_received>\d+)$"
        )

        # num delay requests transmitted  8753
        p25 = re.compile(
            r"^num\sdelay\srequests\stransmitted\s+(?P<num_delay_requests_transmitted>\d+)$"
        )

        # num delay responses received 8753
        p26 = re.compile(
            r"^num\sdelay\sresponses\sreceived\s+(?P<num_delay_responses_received>\d+)$"
        )

        # num delay requests received  0
        p27 = re.compile(
            r"^num\sdelay\srequests\sreceived\s+(?P<num_delay_requests_received>\d+)$"
        )

        # num delay responses transmitted  0
        p28 = re.compile(
            r"^num\sdelay\sresponses\stransmitted\s+(?P<num_delay_responses_transmitted>\d+)$"
        )

        # initial return dictionary
        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Displaying port data for if_id 2a
            # Displaying port data for if_id 29
            m = p1.match(line)
            if m:
                ptp_interface = ret_dict.setdefault("ptp_interface", {})
                ptp_info = ptp_interface.setdefault("ptp_info", {})
                port_info = ptp_interface.setdefault("port_info", {})
                if_id = m.groupdict()["if_id"]
                ptp_info["if_id"] = if_id
                continue

            # Port Mac Address 34:ED:1B:7D:F2:A1
            m = p2.match(line)
            if m:
                mac_address = m.groupdict()["mac_address"]
                port_info["mac_address"] = mac_address
                continue

            # Port Clock Identity 34:ED:1B:FF:FE:7D:F2:80
            m = p3.match(line)
            if m:
                clock_identity = m.groupdict()["clock_identity"]
                port_info["clock_identity"] = clock_identity
                continue

            # Port number 33
            m = p4.match(line)
            if m:
                number = m.groupdict()["number"]
                port_info["number"] = int(number)
                continue

            # PTP Version 2
            m = p5.match(line)
            if m:
                version = m.groupdict()["version"]
                ptp_info["version"] = int(version)
                continue

            # domain_value 0
            m = p6.match(line)
            if m:
                domain_value = m.groupdict()["domain_value"]
                ptp_interface["domain_value"] = int(domain_value)
                continue

            # Profile Type: : DEFAULT
            m = p7.match(line)
            if m:
                profile_type = m.groupdict()["profile_type"]
                ptp_interface["profile_type"] = profile_type
                continue

            # Clock Mode : BOUNDARY CLOCK
            m = p8.match(line)
            if m:
                clock_mode = m.groupdict()["clock_mode"]
                ptp_interface["clock_mode"] = clock_mode
                continue

            # Delay mechanism: End-to-End
            m = p9.match(line)
            if m:
                delay_mechanism = m.groupdict()["delay_mechanism"]
                ptp_interface["delay_mechanism"] = delay_mechanism
                continue

            # port_enabled: TRUE
            m = p10.match(line)
            if m:
                port_enabled = m.groupdict()["port_enabled"]
                port_info["port_enabled"] = port_enabled
                continue

            # ptt_port_enabled: TRUE
            m = p11.match(line)
            if m:
                ptt_port_enabled = m.groupdict()["ptt_port_enabled"]
                ptp_interface["ptt_port_enabled"] = ptt_port_enabled
                continue

            # Port state: : SLAVE
            m = p12.match(line)
            if m:
                state = m.groupdict()["state"]
                port_info["state"] = state
                continue

            # sync_seq_num 36853
            m = p13.match(line)
            if m:
                sync_seq_num = m.groupdict()["sync_seq_num"]
                ptp_interface["sync_seq_num"] = int(sync_seq_num)
                continue

            # delay_req_seq_num 0
            m = p14.match(line)
            if m:
                delay_req_seq_num = m.groupdict()["delay_req_seq_num"]
                ptp_interface["delay_req_seq_num"] = int(delay_req_seq_num)
                continue

            # log mean sync interval -3
            m = p15.match(line)
            if m:
                log_mean_sync_interval = m.groupdict()["log_mean_sync_interval"]
                ptp_interface["log_mean_sync_interval"] = int(log_mean_sync_interval)
                continue

            # log mean delay interval -5
            m = p16.match(line)
            if m:
                log_mean_delay_interval = m.groupdict()["log_mean_delay_interval"]
                ptp_interface["log_mean_delay_interval"] = int(log_mean_delay_interval)
                continue

            # ptp vlan is valid : FALSE
            m = p17.match(line)
            if m:
                ptp_vlan_is_valid = m.groupdict()["ptp_vlan_is_valid"]
                ptp_info["ptp_vlan_is_valid"] = ptp_vlan_is_valid
                continue

            # ptp vlan id 0
            m = p18.match(line)
            if m:
                ptp_vlan_id = m.groupdict()["ptp_vlan_id"]
                ptp_info["ptp_vlan_id"] = int(ptp_vlan_id)
                continue

            # port mode 2
            m = p19.match(line)
            if m:
                mode = m.groupdict()["mode"]
                port_info["mode"] = int(mode)
                continue

            # tag native vlan : FALSE
            m = p20.match(line)
            if m:
                tag_native_vlan = m.groupdict()["tag_native_vlan"]
                ptp_interface["tag_native_vlan"] = tag_native_vlan
                continue

            # num sync messages transmitted  17250
            m = p21.match(line)
            if m:
                num_sync_messages_transmitted = m.groupdict()[
                    "num_sync_messages_transmitted"
                ]
                num_info = ptp_interface.setdefault("num_info", {})
                num_info["num_sync_messages_transmitted"] = int(
                    num_sync_messages_transmitted
                )
                continue

            # num followup messages transmitted  17250
            m = p22.match(line)
            if m:
                num_followup_messages_transmitted = m.groupdict()[
                    "num_followup_messages_transmitted"
                ]
                num_info["num_followup_messages_transmitted"] = int(
                    num_followup_messages_transmitted
                )
                continue

            # num sync messages received  75403
            m = p23.match(line)
            if m:
                num_sync_messages_received = m.groupdict()["num_sync_messages_received"]
                num_info["num_sync_messages_received"] = int(num_sync_messages_received)
                continue

            # num followup messages received  75401
            m = p24.match(line)
            if m:
                num_followup_messages_received = m.groupdict()[
                    "num_followup_messages_received"
                ]
                num_info["num_followup_messages_received"] = int(
                    num_followup_messages_received
                )
                continue

            # num delay requests transmitted  75941
            m = p25.match(line)
            if m:
                num_delay_requests_transmitted = m.groupdict()[
                    "num_delay_requests_transmitted"
                ]
                num_info["num_delay_requests_transmitted"] = int(
                    num_delay_requests_transmitted
                )
                continue

            # num delay responses received 75343
            m = p26.match(line)
            if m:
                num_delay_responses_received = m.groupdict()[
                    "num_delay_responses_received"
                ]
                num_info["num_delay_responses_received"] = int(
                    num_delay_responses_received
                )
                continue

            # num delay requests received  17278
            m = p27.match(line)
            if m:
                num_delay_requests_received = m.groupdict()[
                    "num_delay_requests_received"
                ]
                num_info["num_delay_requests_received"] = int(
                    num_delay_requests_received
                )
                continue

            # num delay responses transmitted  17278
            m = p28.match(line)
            if m:
                num_delay_responses_transmitted = m.groupdict()[
                    "num_delay_responses_transmitted"
                ]
                num_info["num_delay_responses_transmitted"] = int(
                    num_delay_responses_transmitted
                )
                continue
        return ret_dict


# =========================================================
#  Schema for
#  * 'show platform software fed active acl usage'
#  * 'show platform software fed active acl usage | include {acl_name}'
# =========================================================
class ShowPlatformSoftwareFedActiveAclUsageSchema(MetaParser):
    """Schema for 'show platform software fed active acl usage"""

    schema = {
        Optional("acl_usage"): {
            Optional("ace_software"): {
                Optional("vmr_max"): int,
                Optional("used"): int,
            },
            "acl_name": {
                Any(): {
                    "direction": {
                        Any(): {
                            "feature_type": str,
                            "acl_type": str,
                            "entries_used": int,
                        },
                    },
                },
            },
        }
    }


# =========================================================
#  Parser for
#  * 'show platform software fed active acl usage'
#  * 'show platform software fed active acl usage | include {acl_name}'
# =========================================================
class ShowPlatformSoftwareFedActiveAclUsage(
    ShowPlatformSoftwareFedActiveAclUsageSchema
):
    """
    Parser for :
        * show platform software fed active acl usage
        * show platform software fed active acl usage | include {acl_name}
    """

    cli_command = [
        "show platform software fed active acl usage",
        "show platform software fed active acl usage | include {acl_name}",
    ]

    def cli(self, acl_name="", output=None):
        if output is None:
            if acl_name:
                cmd = self.cli_command[1].format(acl_name=acl_name)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        ######  ACE Software VMR max:196608 used:253
        p1 = re.compile(
            r"^\#\#\#\#\#\s+ACE\sSoftware\sVMR\smax\:(?P<vmr_max>\d+)\sused\:(?P<used>\d+)$"
        )

        #   RACL        IPV4     Ingress   PBR-DMVPN    92
        p2 = re.compile(
            r"^(?P<feature_type>\S+)\s+(?P<acl_type>\S+)\s+(?P<direction>\S+)\s+(?P<name>\S+)\s+(?P<entries_used>\d+)$"
        )

        # initial return dictionary
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            acl_usage = ret_dict.setdefault("acl_usage", {})

            ######  ACE Software VMR max:196608 used:253
            m = p1.match(line)
            if m:
                group = m.groupdict()
                acl_usage = ret_dict.setdefault("acl_usage", {})
                ace_software = acl_usage.setdefault("ace_software", {})

                vmr_max = group["vmr_max"]
                ace_software["vmr_max"] = int(vmr_max)

                used = group["used"]
                ace_software["used"] = int(used)
                continue

            #   RACL        IPV4     Ingress   PBR-DMVPN    92
            m = p2.match(line)
            if m:
                group = m.groupdict()
                acl_name = acl_usage.setdefault("acl_name", {}).setdefault(
                    Common.convert_intf_name(group["name"]), {}
                )
                direction = acl_name.setdefault("direction", {}).setdefault(
                    Common.convert_intf_name(group["direction"]), {}
                )

                direction["feature_type"] = group["feature_type"]
                direction["acl_type"] = group["acl_type"]
                direction["entries_used"] = int(group["entries_used"])
                continue
        return ret_dict


# ============================================================================
# Schema for 'show platform software fed active inject packet-capture detailed'
# ===========================================================================
class ShowPlatformSoftwareFedActiveInjectPacketCaptureDetailedSchema(MetaParser):
    """Schema for
    * show platform software fed active inject packet-capture detailed
    """

    schema = {
        "inject_packet_capture": str,
        "buffer_wrapping": str,
        "total_captured": int,
        "capture_capacity": int,
        "capture_filter": str,
        "inject_packet_number": {
            Any(): {
                "interface": {
                    "pal": {"iifd": str},
                },
                "metadata": {
                    "cause": str,
                    "sub_cause": str,
                    "q_no": str,
                    "linktype": str,
                },
                "ether_hdr_1": {"dest_mac": str, "src_mac": str},
                "ether_hdr_2": {"ether_type": str},
                "ipv4_hdr_1": {"dest_ip": str, "src_ip": str},
                "ipv4_hdr_2": {"packet_len": str, "ttl": str, "protocol": str},
                "udp_hdr": {"dest_port": str, "src_port": str},
                "doppler_frame_descriptor": {
                    "fdformat": str,
                    "system_ttl": str,
                    "fdtype": str,
                    "span_session_map": str,
                    "qoslabel": str,
                    "fpe_first_header_type": str,
                },
            }
        },
    }


# ================================================================
# Parser for:
#   * 'show platform software fed active inject packet-capture detailed'
# ================================================================
class ShowPlatformSoftwareFedActiveInjectPacketCaptureDetailed(
    ShowPlatformSoftwareFedActiveInjectPacketCaptureDetailedSchema
):
    """Parser for:
    show platform software fed active inject packet-capture detailed
    """

    cli_command = ["show platform software fed active inject packet-capture detailed"]

    def cli(self, output=None):
        """cli for:
        ' show platform software fed active inject packet-capture detailed '
        """

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Inject packet capturing: disabled. Buffer wrapping: disabled
        p1 = re.compile(
            r"^Inject +packet +capturing:+\s+(?P<inject_packet_capture>\w+)\.+\s+"
            r"Buffer +wrapping:\s+(?P<buffer_wrapping>\w+)$"
        )

        # Total captured so far: 4 packets. Capture capacity : 4096 packets
        p2 = re.compile(
            r"^Total +captured +so +far:\s(?P<total_captured>\d)+\s+packets+\.\s+"
            r"Capture +capacity +:\s+(?P<capture_capacity>\d+)+\s+packets$"
        )

        # Capture filter : "udp.port == 9995"
        p3 = re.compile(r"^Capture +filter +: +(?P<capture_filter>.+)$")

        # ------ Inject Packet Number: 1, Timestamp: 2021/09/15 07:40:40.603 ------
        p4 = re.compile(r"^-+\s+Inject +Packet +Number: +(?P<inject_packet_no>\d+)")

        # interface : pal:  [if-id: 0x00000000]
        p5 = re.compile(r"^interface +: pal: \s+\[+if-id: +(?P<iifd>\S+)$")

        # metadata  : cause: 2 [QFP destination lookup], sub-cause: 1, q-no: 0, linktype: MCP_LINK_TYPE_IP [1]
        p6 = re.compile(
            r"^metadata +: +cause: +(?P<cause>.+)"
            r"\s+sub-cause: +(?P<sub_cause>\d+)\, +q-no: +(?P<q_no>\d+)\,"
            r"\s+linktype: +(?P<linktype>.+)"
        )

        # ether hdr : dest mac: 3c57.3104.6a00, src mac: 3c57.3104.6a00
        p7 = re.compile(
            r"^ether +hdr +: +dest +mac: +(?P<dest_mac>\S+)\s+src +mac: +(?P<src_mac>\S+)"
        )

        # ether hdr : ethertype: 0x0800 (IPv4)
        p8 = re.compile(r"^ether +hdr +: +ethertype: +(?P<ether_type>.+)$")

        # ipv4  hdr : dest ip: 111.0.0.2, src ip: 111.0.0.1
        p9 = re.compile(
            r"^ipv4 +hdr +: +dest +ip: +(?P<dest_ip>\S+)\s+src +ip: +(?P<src_ip>\S+)"
        )

        # ipv4  hdr : packet len: 188, ttl: 255, protocol: 17 (UDP)
        p10 = re.compile(
            r"^ipv4 +hdr +: +packet +len: +(?P<packet_len>\d+)\,\s+ttl: +(?P<ttl>\d+)"
            r"\,+\s+protocol: +(?P<protocol>.+)$"
        )

        # udp   hdr : dest port: 9995, src port: 53926
        p11 = re.compile(
            r"^udp +hdr +: +dest +port: +(?P<dest_port>\d+)\,\s+src +port: +(?P<src_port>\d+)"
        )

        # Doppler Frame Descriptor :
        p12 = re.compile(
            r"^Doppler +Frame +Descriptor +:(?P<doppler_frame_descriptor>)$"
        )

        # fdFormat                  = 0x3            systemTtl                 = 0x8
        p13 = re.compile(
            r"^fdFormat\s+\= (?P<fdformat>\S+)\s+systemTtl\s+\= (?P<system_ttl>\S+$)"
        )

        # fdType                    = 0x1            spanSessionMap            = 0
        p14 = re.compile(
            r"^fdType\s+\= (?P<fdtype>\S+)\s+spanSessionMap\s+\= (?P<span_session_map>\S+$)"
        )

        # qosLabel                  = 0x81           fpeFirstHeaderType        = 0
        p15 = re.compile(
            r"^qosLabel\s+\= (?P<qoslabel>\S+)\s+fpeFirstHeaderType\s+\= (?P<fpe_first_header_type>\S+$)"
        )

        ret_dict = {}
        for line in out.splitlines():
            line = line.strip()

            # Inject packet capturing: disabled. Buffer wrapping: disabled
            m = p1.match(line)
            if m:
                ret_dict.update(
                    {
                        "inject_packet_capture": m.groupdict()["inject_packet_capture"],
                        "buffer_wrapping": m.groupdict()["buffer_wrapping"],
                    }
                )
                continue

            # Total captured so far: 4 packets. Capture capacity : 4096 packets
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update(
                    {
                        "total_captured": int(group["total_captured"]),
                        "capture_capacity": int(group["capture_capacity"]),
                    }
                )
                continue

            # Capture filter : "udp.port == 9995"
            m = p3.match(line)
            if m:
                ret_dict.update({"capture_filter": m.groupdict()["capture_filter"]})
                continue

            # ------ Inject Packet Number: 1, Timestamp: 2021/09/15 07:40:40.603 ------
            m = p4.match(line)
            if m:
                group = m.groupdict()
                inject_packet_num = group["inject_packet_no"]
                inject_packet_dict = ret_dict.setdefault(
                    "inject_packet_number", {}
                ).setdefault(inject_packet_num, {})
                continue

            # interface : pal:  [if-id: 0x00000000]
            m = p5.match(line)
            if m:
                group = m.groupdict()
                int_dict = ret_dict["inject_packet_number"][
                    inject_packet_num
                ].setdefault("interface", {})
                pal_dict = ret_dict["inject_packet_number"][inject_packet_num][
                    "interface"
                ].setdefault("pal", {})
                pal_dict["iifd"] = group["iifd"]
                continue

            # metadata  : cause: 2 [QFP destination lookup], sub-cause: 1, q-no: 0, linktype: MCP_LINK_TYPE_IP [1]
            m = p6.match(line)
            if m:
                group = m.groupdict()
                meta_data_dict = ret_dict["inject_packet_number"][
                    inject_packet_num
                ].setdefault("metadata", {})
                meta_data_dict["cause"] = group["cause"]
                meta_data_dict["sub_cause"] = group["sub_cause"]
                meta_data_dict["q_no"] = group["q_no"]
                meta_data_dict["linktype"] = group["linktype"]
                continue

            # ether hdr : dest mac: 3c57.3104.6a00, src mac: 3c57.3104.6a00
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ether_hdr_1_dict = ret_dict["inject_packet_number"][
                    inject_packet_num
                ].setdefault("ether_hdr_1", {})
                ether_hdr_1_dict["dest_mac"] = group["dest_mac"]
                ether_hdr_1_dict["src_mac"] = group["src_mac"]
                continue

            # ether hdr : ethertype: 0x0800 (IPv4)
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ether_hdr_2_dict = ret_dict["inject_packet_number"][
                    inject_packet_num
                ].setdefault("ether_hdr_2", {})
                ether_hdr_2_dict["ether_type"] = group["ether_type"]
                continue

            # ipv4  hdr : dest ip: 111.0.0.2, src ip: 111.0.0.1
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ipv4_hdr_1_dict = ret_dict["inject_packet_number"][
                    inject_packet_num
                ].setdefault("ipv4_hdr_1", {})
                ipv4_hdr_1_dict["dest_ip"] = group["dest_ip"]
                ipv4_hdr_1_dict["src_ip"] = group["src_ip"]
                continue

            # ipv4  hdr : packet len: 188, ttl: 255, protocol: 17 (UDP)
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ipv4_hdr_2_dict = ret_dict["inject_packet_number"][
                    inject_packet_num
                ].setdefault("ipv4_hdr_2", {})
                ipv4_hdr_2_dict["packet_len"] = group["packet_len"]
                ipv4_hdr_2_dict["ttl"] = group["ttl"]
                ipv4_hdr_2_dict["protocol"] = group["protocol"]
                continue

            # udp   hdr : dest port: 9995, src port: 53926
            m = p11.match(line)
            if m:
                group = m.groupdict()
                udp_hdr_dict = ret_dict["inject_packet_number"][
                    inject_packet_num
                ].setdefault("udp_hdr", {})
                udp_hdr_dict["dest_port"] = group["dest_port"]
                udp_hdr_dict["src_port"] = group["src_port"]
                continue

            # Doppler Frame Descriptor :
            m = p12.match(line)
            if m:
                group = m.groupdict()
                doppler_frame_des_dict = ret_dict["inject_packet_number"][
                    inject_packet_num
                ].setdefault("doppler_frame_descriptor", {})
                continue

            # fdFormat                  = 0x3            systemTtl                 = 0x8
            m = p13.match(line)
            if m:
                group = m.groupdict()
                doppler_frame_des_dict["fdformat"] = group["fdformat"]
                doppler_frame_des_dict["system_ttl"] = group["system_ttl"]
                continue

            # fdType                    = 0x1            spanSessionMap            = 0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                doppler_frame_des_dict["fdtype"] = group["fdtype"]
                doppler_frame_des_dict["span_session_map"] = group["span_session_map"]
                continue

            # qosLabel                  = 0x81           fpeFirstHeaderType        = 0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                doppler_frame_des_dict["qoslabel"] = group["qoslabel"]
                doppler_frame_des_dict["fpe_first_header_type"] = group[
                    "fpe_first_header_type"
                ]
                continue

        return ret_dict


# =============================================================================
#  Schema for
#  * 'show platform software fed switch active ifm mappings lpn'
#  * 'show platform software fed switch active ifm mappings lpn | {interface}'
# ==============================================================================
class ShowPlatformSoftwareFedSwitchActiveIfmMappingsLpnSchema(MetaParser):
    """Schema for 'show platform software fed switch active ifm mappings lpn'"""

    schema = {
        "interfaces": {
            Any(): {"lpn": int, "asic": int, "port": int, "if_id": str, "active": str}
        },
    }


# ===============================================================================
#  Parser for
#  * 'show platform software fed switch active ifm mappings lpn'
#  * 'show platform software fed switch active ifm mappings lpn | i {interface}'
# ================================================================================
class ShowPlatformSoftwareFedSwitchActiveIfmMappingsLpn(
    ShowPlatformSoftwareFedSwitchActiveIfmMappingsLpnSchema
):
    """
    Parser for :
        * show platform software fed switch active ifm mappings lpn
    """

    cli_command = [
        "show platform software fed switch active ifm mappings lpn",
        "show platform software fed switch active ifm mappings lpn | include {interface}",
    ]

    def cli(self, interface="", output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        # 19   1     18    TenGigabitEthernet1/0/19   0x0000001b  y
        p = re.compile(
            r"^(?P<lpn>\d+)\s+(?P<asic>\d+)\s+(?P<port>\d+)\s+(?P<interfaces>\S+)\s+(?P<if_id>(0x([\da-fA-F]){8}))\s+(?P<active>\S+)$"
        )

        # initial return dictionary
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # 19    1  18    TenGigabitEthernet1/0/19   0x0000001b  y
            m = p.match(line)
            if m:
                group = m.groupdict()
                interfaces = group["interfaces"]
                sub_dict = ret_dict.setdefault("interfaces", {}).setdefault(
                    interfaces, {}
                )

                lpn = group["lpn"]
                sub_dict["lpn"] = int(lpn)

                asic = group["asic"]
                sub_dict["asic"] = int(asic)

                port = group["port"]
                sub_dict["port"] = int(port)

                if_id = group["if_id"]
                sub_dict["if_id"] = if_id

                active = group["active"]
                sub_dict["active"] = active
                continue
        return ret_dict


# =================================================================
#  Schema for 'show platform software fed switch {switch} ptp domain
# ================================================================
class ShowPlatformSoftwareFedSwitchActivePtpDomainSchema(MetaParser):
    """Schema for 'show platform software fed switch active ptp domain"""

    schema = {
        "domain_number": {
            Any(): {
                "profile_type": str,
                "profile_state": str,
                Optional("clock_mode"): str,
                Optional("delay_mechanism"): str,
                Optional("ptp_clock"): str,
                Optional("mean_path_delay_ns"): int,
                "transport_method": str,
                Optional("message_general_ip_dscp"): int,
                Optional("message_event_ip_dscp"): int,
                Optional("clocksource"): int,
                Optional("gm_capable"): str,
                Optional("grandmaster"): str,
                Optional("gm_present"): str,
                Optional("propagation_delay"): str,
            }
        },
    }


# =================================================================
#  Parser for 'show platform software fed switch {switch} ptp domain
# ================================================================
class ShowPlatformSoftwareFedSwitchActivePtpDomain(
    ShowPlatformSoftwareFedSwitchActivePtpDomainSchema
):
    """
    Parser for :
        * show platform software fed switch {switch} ptp domain
        * show platform software fed active ptp domain
    """

    cli_command = [
        "show platform software fed active ptp domain",
        "show platform software fed switch {switch} ptp domain",
    ]

    def cli(self, switch=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[1].format(switch=switch)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        # Displaying data for domain number 0
        p1 = re.compile(
            r"^Displaying\sdata\sfor\sdomain\snumber\s(?P<domain_number>\d+)$"
        )

        # Profile Type : DEFAULT
        p2 = re.compile(r"^Profile\sType\s\:\s(?P<profile_type>\w+)$")

        # Profile State: enabled
        p3 = re.compile(r"^Profile\sState\:\s(?P<profile_state>\S+)$")

        # Clock Mode : BOUNDARY CLOCK
        p4 = re.compile(r"^Clock\sMode\s\:\s(?P<clock_mode>[A-Z\s]+)$")

        # Delay Mechanism: : END-TO-END
        p5 = re.compile(r"^Delay\sMechanism\:\s\:\s(?P<delay_mechanism>[A-Z\-]+)$")

        # PTP clock : 1970-1-24 22:41:20
        p6 = re.compile(r"^PTP\sclock\s\:\s(?P<ptp_clock>[\d\-\:\s]+)$")

        # mean_path_delay 83 nanoseconds
        p7 = re.compile(r"^mean_path_delay\s(?P<mean_path_delay_ns>\d+)\snanoseconds$")

        # Transport Method : 802.3
        p8 = re.compile(r"^Transport\sMethod\s\:\s(?P<transport_method>[\w\.\-]+)$")

        # Message general ip dscp  : 47
        p9 = re.compile(
            r"^Message\sgeneral\sip\sdscp\s+\:\s(?P<message_general_ip_dscp>\d+)$"
        )

        # Message event ip dscp    : 59
        p10 = re.compile(
            r"^Message\sevent\sip\sdscp\s+\:\s(?P<message_event_ip_dscp>\d+)$"
        )

        # clocksource 160
        p11 = re.compile(r"^clocksource\s+(?P<clocksource>\d+)$")

        # Grandmaster: FALSE
        p12 = re.compile(r"^Grandmaster:\s+(?P<grandmaster>\w+)$")

        # gm_capable: TRUE
        p13 = re.compile(r"^gm_capable:\s+(?P<gm_capable>\w+)$")

        # gm_present: TRUE
        p14 = re.compile(r"^gm_present:\s+(?P<gm_present>\w+)$")

        # neighbor propagation delay threshold: 800 ns
        p15 = re.compile(
            r"^neighbor propagation delay threshold:\s+(?P<propagation_delay>[\w\s]+)$"
        )

        # initial return dictionary
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Displaying data for domain number 0
            m = p1.match(line)
            if m:
                ret_dict.setdefault("domain_number", {})
                domain_number = m.groupdict()["domain_number"]
                sub_dict = ret_dict["domain_number"].setdefault(int(domain_number), {})
                continue

            # Profile Type : DEFAULT
            m = p2.match(line)
            if m:
                profile_type = m.groupdict()["profile_type"]
                sub_dict["profile_type"] = profile_type
                continue

            # Profile State: enabled
            m = p3.match(line)
            if m:
                profile_state = m.groupdict()["profile_state"]
                sub_dict["profile_state"] = profile_state
                continue

            # Clock Mode : BOUNDARY CLOCK
            m = p4.match(line)
            if m:
                clock_mode = m.groupdict()["clock_mode"]
                sub_dict["clock_mode"] = clock_mode
                continue

            # Delay Mechanism: : END-TO-END
            m = p5.match(line)
            if m:
                delay_mechanism = m.groupdict()["delay_mechanism"]
                sub_dict["delay_mechanism"] = delay_mechanism
                continue

            # PTP clock : 1970-1-24 22:41:20
            m = p6.match(line)
            if m:
                ptp_clock = m.groupdict()["ptp_clock"]
                sub_dict["ptp_clock"] = ptp_clock
                continue

            # mean_path_delay 83 nanoseconds
            m = p7.match(line)
            if m:
                mean_path_delay_ns = m.groupdict()["mean_path_delay_ns"]
                sub_dict["mean_path_delay_ns"] = int(mean_path_delay_ns)
                continue

            # Transport Method : 802.3
            m = p8.match(line)
            if m:
                transport_method = m.groupdict()["transport_method"]
                sub_dict["transport_method"] = transport_method
                continue

            # Message general ip dscp  : 47
            m = p9.match(line)
            if m:
                message_general_ip_dscp = m.groupdict()["message_general_ip_dscp"]
                sub_dict["message_general_ip_dscp"] = int(message_general_ip_dscp)
                continue

            # Message event ip dscp    : 59
            m = p10.match(line)
            if m:
                message_event_ip_dscp = m.groupdict()["message_event_ip_dscp"]
                sub_dict["message_event_ip_dscp"] = int(message_event_ip_dscp)
                continue

            # clocksource 160
            m = p11.match(line)
            if m:
                sub_dict["clocksource"] = int(m.groupdict()["clocksource"])
                continue

            # Grandmaster: FALSE
            m = p12.match(line)
            if m:
                sub_dict["grandmaster"] = m.groupdict()["grandmaster"]
                continue

            # gm_capable: TRUE
            m = p13.match(line)
            if m:
                sub_dict["gm_capable"] = m.groupdict()["gm_capable"]
                continue

            # gm_present: TRUE
            m = p14.match(line)
            if m:
                sub_dict["gm_present"] = m.groupdict()["gm_present"]
                continue

            # neighbor propagation delay threshold: 800 ns
            m = p15.match(line)
            if m:
                sub_dict["propagation_delay"] = m.groupdict()["propagation_delay"]
                continue
        return ret_dict


# ================================================================================
#  Schema for 'show platform software fed switch active ptp interface {interface}'
# ================================================================================
class ShowPlatformSoftwareFedSwitchActivePtpInterfaceInterfaceSchema(MetaParser):
    """Schema for 'show platform software fed switch active ptp interface {interface}'"""

    schema = {
        "interface": {
            "ptp_info": {
                "version": int,
                Optional("ptp_vlan_is_valid"): str,
                Optional("ptp_vlan_id"): int,
            },
            "port_info": {
                "mac_address": str,
                "clock_identity": str,
                "number": int,
                Optional("mode"): int,
                "state": str,
                "port_enabled": str,
            },
            "num_info": {
                "num_sync_messages_transmitted": int,
                "num_followup_messages_transmitted": int,
                "num_sync_messages_received": int,
                "num_followup_messages_received": int,
                Optional("num_delay_requests_transmitted"): int,
                Optional("num_delay_responses_received"): int,
                Optional("num_delay_requests_received"): int,
                Optional("num_delay_responses_transmitted"): int,
            },
            "if_id": str,
            "domain_value": int,
            "profile_type": str,
            "clock_mode": str,
            "delay_mechanism": str,
            "ptt_port_enabled": str,
            "sync_seq_num": int,
            "delay_req_seq_num": int,
            Optional("log_mean_sync_interval"): int,
            Optional("log_mean_delay_interval"): int,
            Optional("tag_native_vlan"): str,
        }
    }


# =================================================================================
#  Parser for 'show platform software fed switch active ptp interface {interface}'
# =================================================================================
class ShowPlatformSoftwareFedSwitchActivePtpInterfaceInterface(
    ShowPlatformSoftwareFedSwitchActivePtpInterfaceInterfaceSchema
):
    """
    Parser for :
        * show platform software fed switch active ptp interface {interface}
    """

    cli_command = [
        "show platform software fed switch {switch_var} ptp interface {interface}",
        "show platform software fed active ptp interface {interface}",
    ]

    def cli(self, interface="", output=None, switch_var=None):
        if switch_var is None:
            cmd = self.cli_command[1].format(interface=interface)
        else:
            cmd = self.cli_command[0].format(switch_var=switch_var, interface=interface)
        output = self.device.execute(cmd)

        # Displaying port data for if_id 2a
        # Displaying port data for if_id 29
        p1 = re.compile(
            r"^Displaying\sport\sdata\sfor\sif_id\s(?P<if_id>[0-9a-fA-F]+)$"
        )

        # Port Mac Address 34:ED:1B:7D:F2:A1
        p2 = re.compile(r"^Port\sMac\sAddress\s(?P<mac_address>([\da-fA-F]:?).*)$")

        # Port Clock Identity 34:ED:1B:FF:FE:7D:F2:80
        p3 = re.compile(
            r"^Port\sClock\sIdentity\s(?P<clock_identity>([\da-fA-F]:?).*)$"
        )

        # Port number 33
        p4 = re.compile(r"^Port\snumber\s(?P<number>\d+)$")

        # PTP Version 2
        p5 = re.compile(r"^PTP\sVersion\s(?P<version>\d+)$")

        # domain_value 0
        p6 = re.compile(r"^domain_value\s(?P<domain_value>\d+)$")

        # Profile Type: : DEFAULT
        p7 = re.compile(r"^Profile\sType\:\s\:\s(?P<profile_type>\S+)$")

        # Clock Mode : BOUNDARY CLOCK
        p8 = re.compile(r"^Clock\sMode\s\:\s(?P<clock_mode>.*)$")

        # Delay mechanism: End-to-End
        p9 = re.compile(r"^Delay\smechanism\:\s(?P<delay_mechanism>\S+)$")

        # port_enabled: TRUE
        p10 = re.compile(r"^port_enabled\:\s(?P<port_enabled>\S+)$")

        # ptt_port_enabled: TRUE
        p11 = re.compile(r"^ptt_port_enabled\:\s(?P<ptt_port_enabled>\S+)$")

        # Port state: : SLAVE
        p12 = re.compile(r"^Port\sstate\:\s\:\s(?P<state>\S+)$")

        # sync_seq_num 2189
        p13 = re.compile(r"^sync_seq_num\s(?P<sync_seq_num>\d+)$")

        # delay_req_seq_num 0
        p14 = re.compile(r"^delay_req_seq_num\s(?P<delay_req_seq_num>\d+)$")

        # log mean sync interval -3
        p15 = re.compile(
            r"^log\smean\ssync\sinterval\s(?P<log_mean_sync_interval>[-?\d]+)$"
        )

        # log mean delay interval -5
        p16 = re.compile(
            r"^log\smean\sdelay\sinterval\s(?P<log_mean_delay_interval>[-?\d]+)$"
        )

        # ptp vlan is valid : FALSE
        p17 = re.compile(r"^ptp\svlan\sis\svalid\s\:\s(?P<ptp_vlan_is_valid>\S+)$")

        # ptp vlan id 0
        p18 = re.compile(r"^ptp\svlan\sid\s(?P<ptp_vlan_id>\d+)$")

        # port mode 2
        p19 = re.compile(r"^port\smode\s(?P<mode>\d+)$")

        # tag native vlan : FALSE
        p20 = re.compile(r"^tag\snative\svlan\s\:\s(?P<tag_native_vlan>\S+)$")

        # num sync messages transmitted  0
        p21 = re.compile(
            r"^num\ssync\smessages\stransmitted\s+(?P<num_sync_messages_transmitted>\d+)$"
        )

        # num followup messages transmitted  0
        p22 = re.compile(
            r"^num\sfollowup\smessages\stransmitted\s+(?P<num_followup_messages_transmitted>\d+)$"
        )

        # num sync messages received  8758
        p23 = re.compile(
            r"^num\ssync\smessages\sreceived\s+(?P<num_sync_messages_received>\d+)$"
        )

        # num followup messages received  8757
        p24 = re.compile(
            r"^num\sfollowup\smessages\sreceived\s+(?P<num_followup_messages_received>\d+)$"
        )

        # num delay requests transmitted  8753
        p25 = re.compile(
            r"^num\sdelay\srequests\stransmitted\s+(?P<num_delay_requests_transmitted>\d+)$"
        )

        # num delay responses received 8753
        p26 = re.compile(
            r"^num\sdelay\sresponses\sreceived\s+(?P<num_delay_responses_received>\d+)$"
        )

        # num delay requests received  0
        p27 = re.compile(
            r"^num\sdelay\srequests\sreceived\s+(?P<num_delay_requests_received>\d+)$"
        )

        # num delay responses transmitted  0
        p28 = re.compile(
            r"^num\sdelay\sresponses\stransmitted\s+(?P<num_delay_responses_transmitted>\d+)$"
        )

        # initial return dictionary
        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Displaying port data for if_id 2a
            # Displaying port data for if_id 29
            m = p1.match(line)
            if m:
                group = m.groupdict()
                sub_dict = ret_dict.setdefault("interface", {})
                sub_dict["if_id"] = group["if_id"]
                ptp_info = sub_dict.setdefault("ptp_info", {})
                port_info = sub_dict.setdefault("port_info", {})
                continue

            # Port Mac Address 34:ED:1B:7D:F2:A1
            m = p2.match(line)
            if m:
                mac_address = m.groupdict()["mac_address"]
                port_info["mac_address"] = mac_address
                continue

            # Port Clock Identity 34:ED:1B:FF:FE:7D:F2:80
            m = p3.match(line)
            if m:
                clock_identity = m.groupdict()["clock_identity"]
                port_info["clock_identity"] = clock_identity
                continue

            # Port number 33
            m = p4.match(line)
            if m:
                number = m.groupdict()["number"]
                port_info["number"] = int(number)
                continue

            # PTP Version 2
            m = p5.match(line)
            if m:
                version = m.groupdict()["version"]
                ptp_info["version"] = int(version)
                continue

            # domain_value 0
            m = p6.match(line)
            if m:
                domain_value = m.groupdict()["domain_value"]
                sub_dict["domain_value"] = int(domain_value)
                continue

            # Profile Type: : DEFAULT
            m = p7.match(line)
            if m:
                profile_type = m.groupdict()["profile_type"]
                sub_dict["profile_type"] = profile_type
                continue

            # Clock Mode : BOUNDARY CLOCK
            m = p8.match(line)
            if m:
                clock_mode = m.groupdict()["clock_mode"]
                sub_dict["clock_mode"] = clock_mode
                continue

            # Delay mechanism: End-to-End
            m = p9.match(line)
            if m:
                delay_mechanism = m.groupdict()["delay_mechanism"]
                sub_dict["delay_mechanism"] = delay_mechanism
                continue

            # port_enabled: TRUE
            m = p10.match(line)
            if m:
                port_enabled = m.groupdict()["port_enabled"]
                port_info["port_enabled"] = port_enabled
                continue

            # ptt_port_enabled: TRUE
            m = p11.match(line)
            if m:
                ptt_port_enabled = m.groupdict()["ptt_port_enabled"]
                sub_dict["ptt_port_enabled"] = ptt_port_enabled
                continue

            # Port state: : SLAVE
            m = p12.match(line)
            if m:
                state = m.groupdict()["state"]
                port_info["state"] = state
                continue

            # sync_seq_num 36853
            m = p13.match(line)
            if m:
                sync_seq_num = m.groupdict()["sync_seq_num"]
                sub_dict["sync_seq_num"] = int(sync_seq_num)
                continue

            # delay_req_seq_num 0
            m = p14.match(line)
            if m:
                delay_req_seq_num = m.groupdict()["delay_req_seq_num"]
                sub_dict["delay_req_seq_num"] = int(delay_req_seq_num)
                continue

            # log mean sync interval -3
            m = p15.match(line)
            if m:
                log_mean_sync_interval = m.groupdict()["log_mean_sync_interval"]
                sub_dict["log_mean_sync_interval"] = int(log_mean_sync_interval)
                continue

            # log mean delay interval -5
            m = p16.match(line)
            if m:
                log_mean_delay_interval = m.groupdict()["log_mean_delay_interval"]
                sub_dict["log_mean_delay_interval"] = int(log_mean_delay_interval)
                continue

            # ptp vlan is valid : FALSE
            m = p17.match(line)
            if m:
                ptp_vlan_is_valid = m.groupdict()["ptp_vlan_is_valid"]
                ptp_info["ptp_vlan_is_valid"] = ptp_vlan_is_valid
                continue

            # ptp vlan id 0
            m = p18.match(line)
            if m:
                ptp_vlan_id = m.groupdict()["ptp_vlan_id"]
                ptp_info["ptp_vlan_id"] = int(ptp_vlan_id)
                continue

            # port mode 2
            m = p19.match(line)
            if m:
                mode = m.groupdict()["mode"]
                port_info["mode"] = int(mode)
                continue

            # tag native vlan : FALSE
            m = p20.match(line)
            if m:
                tag_native_vlan = m.groupdict()["tag_native_vlan"]
                sub_dict["tag_native_vlan"] = tag_native_vlan
                continue

            # num sync messages transmitted  17250
            m = p21.match(line)
            if m:
                num_sync_messages_transmitted = m.groupdict()[
                    "num_sync_messages_transmitted"
                ]
                num_info = sub_dict.setdefault("num_info", {})
                num_info["num_sync_messages_transmitted"] = int(
                    num_sync_messages_transmitted
                )
                continue

            # num followup messages transmitted  17250
            m = p22.match(line)
            if m:
                num_followup_messages_transmitted = m.groupdict()[
                    "num_followup_messages_transmitted"
                ]
                num_info["num_followup_messages_transmitted"] = int(
                    num_followup_messages_transmitted
                )
                continue

            # num sync messages received  75403
            m = p23.match(line)
            if m:
                num_sync_messages_received = m.groupdict()["num_sync_messages_received"]
                num_info["num_sync_messages_received"] = int(num_sync_messages_received)
                continue

            # num followup messages received  75401
            m = p24.match(line)
            if m:
                num_followup_messages_received = m.groupdict()[
                    "num_followup_messages_received"
                ]
                num_info["num_followup_messages_received"] = int(
                    num_followup_messages_received
                )
                continue

            # num delay requests transmitted  75941
            m = p25.match(line)
            if m:
                num_delay_requests_transmitted = m.groupdict()[
                    "num_delay_requests_transmitted"
                ]
                num_info["num_delay_requests_transmitted"] = int(
                    num_delay_requests_transmitted
                )
                continue

            # num delay responses received 75343
            m = p26.match(line)
            if m:
                num_delay_responses_received = m.groupdict()[
                    "num_delay_responses_received"
                ]
                num_info["num_delay_responses_received"] = int(
                    num_delay_responses_received
                )
                continue

            # num delay requests received  17278
            m = p27.match(line)
            if m:
                num_delay_requests_received = m.groupdict()[
                    "num_delay_requests_received"
                ]
                num_info["num_delay_requests_received"] = int(
                    num_delay_requests_received
                )
                continue

            # num delay responses transmitted  17278
            m = p28.match(line)
            if m:
                num_delay_responses_transmitted = m.groupdict()[
                    "num_delay_responses_transmitted"
                ]
                num_info["num_delay_responses_transmitted"] = int(
                    num_delay_responses_transmitted
                )
                continue
        return ret_dict


# =========================================================
#  Schema for
#  * 'show platform software fed active acl usage'
#  * 'show platform software fed active acl usage | include {acl_name}'
# =========================================================
class ShowPlatformSoftwareFedActiveAclUsageSchema(MetaParser):
    """Schema for 'show platform software fed active acl usage"""

    schema = {
        Optional("acl_usage"): {
            Optional("ace_software"): {
                Optional("vmr_max"): int,
                Optional("used"): int,
            },
            "acl_name": {
                Any(): {
                    "direction": {
                        Any(): {
                            "feature_type": str,
                            "acl_type": str,
                            "entries_used": int,
                        },
                    },
                },
            },
        }
    }


# =========================================================
#  Parser for
#  * 'show platform software fed active acl usage'
#  * 'show platform software fed active acl usage | include {acl_name}'
# =========================================================
class ShowPlatformSoftwareFedActiveAclUsage(
    ShowPlatformSoftwareFedActiveAclUsageSchema
):
    """
    Parser for :
        * show platform software fed active acl usage
        * show platform software fed active acl usage | include {acl_name}
    """

    cli_command = [
        "show platform software fed active acl usage",
        "show platform software fed active acl usage | include {acl_name}",
    ]

    def cli(self, acl_name="", output=None):
        if output is None:
            if acl_name:
                cmd = self.cli_command[1].format(acl_name=acl_name)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        ######  ACE Software VMR max:196608 used:253
        p1 = re.compile(
            r"^\#\#\#\#\#\s+ACE\sSoftware\sVMR\smax\:(?P<vmr_max>\d+)\sused\:(?P<used>\d+)$"
        )

        #   RACL        IPV4     Ingress   PBR-DMVPN    92
        p2 = re.compile(
            r"^(?P<feature_type>\S+)\s+(?P<acl_type>\S+)\s+(?P<direction>\S+)\s+(?P<name>\S+)\s+(?P<entries_used>\d+)$"
        )

        # initial return dictionary
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            acl_usage = ret_dict.setdefault("acl_usage", {})

            ######  ACE Software VMR max:196608 used:253
            m = p1.match(line)
            if m:
                group = m.groupdict()
                acl_usage = ret_dict.setdefault("acl_usage", {})
                ace_software = acl_usage.setdefault("ace_software", {})

                vmr_max = group["vmr_max"]
                ace_software["vmr_max"] = int(vmr_max)

                used = group["used"]
                ace_software["used"] = int(used)
                continue

            #   RACL        IPV4     Ingress   PBR-DMVPN    92
            m = p2.match(line)
            if m:
                group = m.groupdict()
                acl_name = acl_usage.setdefault("acl_name", {}).setdefault(
                    Common.convert_intf_name(group["name"]), {}
                )
                direction = acl_name.setdefault("direction", {}).setdefault(
                    Common.convert_intf_name(group["direction"]), {}
                )

                direction["feature_type"] = group["feature_type"]
                direction["acl_type"] = group["acl_type"]
                direction["entries_used"] = int(group["entries_used"])
                continue
        return ret_dict


class ShowPlatformSoftwareFedSwitchPortSummarySchema(MetaParser):
    """
    Schema for show platform software fed switch {mode} port summary
    """

    schema = {
        "interface": {
            Any(): {
                "if_id": int,
                "port_enable": str,
            }
        }
    }


class ShowPlatformSoftwareFedSwitchPortSummary(
    ShowPlatformSoftwareFedSwitchPortSummarySchema
):
    """Parser for show platform software fed switch {mode} port summary"""

    cli_command = "show platform software fed switch {mode} port summary"

    def cli(self, mode, output=None):
        if output is None:
            # excute command to get output
            output = self.device.execute(self.cli_command.format(mode=mode))

        # initial variables
        ret_dict = {}

        # 1266           HundredGigE2/0/27/1             true
        p1 = re.compile("^(?P<if_id>\d+)\s+(?P<if_name>\S+)\s+(?P<port_enable>\w+)$")

        for line in output.splitlines():
            line = line.strip()

            # 1266           HundredGigE2/0/27/1             true
            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault("interface", {}).setdefault(
                    group["if_name"], {}
                )
                root_dict["if_id"] = int(group["if_id"])
                root_dict["port_enable"] = group["port_enable"]
                continue
        return ret_dict



# =======================================================================================================
#  Schema for:
#  * 'show platform software fed switch {switch_no} security-fed dhcp-snoop vlan vlan-id {vlan_id}'
# =======================================================================================================


class ShowPlatformSoftwareFedSwitchSecurityfedDhcpsnoopVlanVlanidSchema(MetaParser):

    """Schema for show platform software fed switch {switch_no} security-fed dhcp-snoop vlan vlan-id {vlan_id}"""

    schema = {
        "trust_status": str,
        "vlan": int,
        "snooping_handle": str,
        Optional("interfaces"): {
            Any(): {Optional("port"): str, Optional("mode"): str},
        },
    }


# =======================================================================================================
#  parser for:
#  *'show platform software fed switch {switch_no} security-fed dhcp-snoop vlan vlan-id {vlan_id}'
# =======================================================================================================


class ShowPlatformSoftwareFedSwitchSecurityfedDhcpsnoopVlanVlanid(
    ShowPlatformSoftwareFedSwitchSecurityfedDhcpsnoopVlanVlanidSchema
):

    """Parser for show platform software fed switch {switch_no} security-fed dhcp-snoop vlan vlan-id {vlan_id}"""

    cli_command = "show platform software fed switch {switch_no} security-fed dhcp-snoop vlan vlan-id {vlan_id}"

    def cli(self, switch_no, vlan_id, output=None):
        if output is None:
            output = self.device.execute(
                self.cli_command.format(switch_no=switch_no, vlan_id=vlan_id)
            )

        ret_dict = {}

        # DHCP Snooping disabled on vlan: 100
        p = re.compile(r"DHCP\s+Snooping\s+disabled\s+on\s+vlan\s*:\s*(?P<vlan>\d+)")

        # Valid Snooping DI handle:none
        p1 = re.compile(
            r"Valid\s+Snooping\s+DI\s+handle\s*:\s*(?P<snooping_handle>\S+)"
        )

        # No trust ports for this vlan
        p2 = re.compile(r"No\s+trust\s+ports\s+for\s+this\s+vlan")

        # GigabitEthernet1/0/3             trust
        p3 = re.compile(r"(?P<port>.*\d+\/\d+\/\d+)\s+(?P<mode>\S+)")

        for line in output.splitlines():
            line = line.strip()

            # DHCP Snooping disabled on vlan: 100
            m = p.match(line)
            if m:
                ret_dict["vlan"] = int(m.group(1))
                continue

            # Valid Snooping DI handle:none
            m1 = p1.match(line)
            if m1:
                ret_dict["snooping_handle"] = m1.group(1)
                continue

            # No trust ports for this vlan
            m2 = p2.match(line)
            if m2:
                ret_dict["trust_status"] = "no"
                return ret_dict

            #  GigabitEthernet1/0/3             trust
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                intf_dict = ret_dict.setdefault("interfaces", {}).setdefault(
                    group.pop("port"), {}
                )
                intf_dict.update({k: v for k, v in group.items()})
                ret_dict["trust_status"] = "yes"
                continue

        return ret_dict


class ShowPlatformSoftwareFedActiveSecurityFedSchema(MetaParser):

    """Schema for "show platform software fed {switch} active security-fed sis-redirect firewall all"
    show platform software fed active security-fed sis-redirect firewall all"""

    schema = {
        "service_ip": {
            Any(): {
                "service_id": int,
                "vrf_id": int,
                "firewall_ip": str,
                Optional("aal_hd1"): str,
                "redirect_hd1": str,
                "hmt_hd1": str,
            }
        }
    }


class ShowPlatformSoftwareFedActiveSecurityFed(
    ShowPlatformSoftwareFedActiveSecurityFedSchema
):
    """Schema for show platform software fed {switch} active security-fed sis-redirect firewall all"""

    cli_command = [
        "show platform software fed {switch} active security-fed sis-redirect firewall all",
        "show platform software fed active security-fed sis-redirect firewall all",
    ]

    def cli(self, switch="", output=None):
        if output is None:
            if not switch:
                cmd = self.cli_command[1]
            else:
                cmd = self.cli_command[0].format(switch=switch)
            output = self.device.execute(cmd)

        parsed_dict = {}
        # Printing firewall information
        # ---------------------------------------------------------------------------
        # | Service ID  | VRF ID  | IP            | Redirect Hdl    | HTM Hdl       |
        # ---------------------------------------------------------------------------
        #  3861840337    0         172.18.0.2      0x7fe0bb341f38    0x7fe0bb2f27d8
        #  3861840137    2         172.18.0.6      0x7fe0bb334788    0x7fe0bb67c118
        # ---------------------------------------------------------------------------

        #  3861840337    0         172.18.0.2      0x7fe0bb341f38    0x7fe0bb2f27d8

        #  Printing firewall information
        #  -------------------------------------------------------------------------------------------
        #  | Service ID  | VRF ID  | IP            | AAL Hdl       | Redirect Hdl    | HTM Hdl       |
        #  -------------------------------------------------------------------------------------------
        #  557985737     0         153.11.0.6      0x2a000014      0x7482b07260e8    0x7482b0726368
        #  -------------------------------------------------------------------------------------------
        p1 = re.compile(
            r"^(?P<service_id>\d+)\s+(?P<vrf_id>\d+)\s+(?P<firewall_ip>[\d.]+)\s+(?P<aal_hd1>0x[\da-f]+)\s+(?P<redirect_hd1>0x[\da-f]+)\s+(?P<hmt_hd1>0x[\da-f]+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            #  3861840337    0         172.18.0.2      0x7fe0bb341f38    0x7fe0bb2f27d8
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                service_id = int(groups["service_id"])
                vrf_id = int(groups["vrf_id"])
                firewall_ip = groups["firewall_ip"]
                aal_hd1 = groups["aal_hd1"]
                redirect_hd1 = groups["redirect_hd1"]
                hmt_hd1 = groups["hmt_hd1"]
                service_ip_dict = parsed_dict.setdefault("service_ip", {})

                firewall_ip_dict = service_ip_dict.setdefault(firewall_ip, {})
                firewall_ip_dict.update(
                    {
                        "service_id": service_id,
                        "vrf_id": vrf_id,
                        "firewall_ip": firewall_ip,
                        "aal_hd1": aal_hd1,
                        "redirect_hd1": redirect_hd1,
                        "hmt_hd1": hmt_hd1,
                    }
                )
                continue

        return parsed_dict


class ShowPlatformSoftwareFedActiveSecurityFedAclAllSchema(MetaParser):

    """Schema for "show platform software fed {switch} active security-fed sis-redirect acl all" """

    schema = {
        "firewall_id": {
            Any(): {
                "seq_no": {
                    Any(): {
                        "acl_id": int,
                        "firewall_id": int,
                        "stats_handle": str,
                        "frame_count": int,
                        "hardware_count": int,
                    },
                },
            }
        },
        "number_of_aces": int,
        "number_of_acls": int,
    }


class ShowPlatformSoftwareFedActiveSecurityFedAclAll(
    ShowPlatformSoftwareFedActiveSecurityFedAclAllSchema
):
    """Schema for show platform software fed {switch} active security-fed sis-redirect acl all"""

    cli_command = [
        "show platform software fed {switch} active security-fed sis-redirect acl all",
        "show platform software fed active security-fed sis-redirect acl all",
    ]

    def cli(self, switch="", output=None):
        if output is None:
            if not switch:
                cmd = self.cli_command[1]
            else:
                cmd = self.cli_command[0].format(switch=switch)
            output = self.device.execute(cmd)

        parsed_dict = {}

        # ------------------------------------------------------------------------------------------------
        # | ACL ID    | Seq no  | Firewall ID | Stats Handle |     Frame Count     |     Hw-Stats        |
        # ------------------------------------------------------------------------------------------------
        #  1405908841   1         1252352985    0x370000cb                   9862                   9862
        # ------------------------------------------------------------------------------------------------
        # Number of ACE's: 1
        # Number of ACL's: 1

        #  1405908841   1         1252352985    0x370000cb                   9862                   9862
        p1 = re.compile(
            r"^(?P<acl_id>\d+)\s+(?P<seq_number>\d+)\s+(?P<firewall_id>[\d.]+)\s+(?P<stats_handle>0x[\da-f]+)\s+(?P<frame_count>\d+)\s+(?P<hardware_count>\d+)$"
        )

        # Number of ACE's: 1
        p2 = re.compile(r"^Number of ACE's\s*:\s*(?P<number_of_aces>\d+)$")

        # Number of ACL's: 1
        p3 = re.compile(r"^Number of ACL's\s*:\s*(?P<number_of_acls>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            #  1405908841   1         1252352985    0x370000cb                   9862                   9862
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                acl_id = int(groups["acl_id"])
                seq_number = int(groups["seq_number"])
                firewall_id = int(groups["firewall_id"])
                stats_handle = groups["stats_handle"]
                frame_count = int(groups["frame_count"])
                hardware_count = int(groups["hardware_count"])
                firewall_id_dict = parsed_dict.setdefault("firewall_id", {})
                acl_dict = firewall_id_dict.setdefault(firewall_id, {}).setdefault(
                    "seq_no", {}
                )
                seq_dict = acl_dict.setdefault(seq_number, {})
                seq_dict.update(
                    {
                        "acl_id": acl_id,
                        "firewall_id": firewall_id,
                        "stats_handle": stats_handle,
                        "frame_count": frame_count,
                        "hardware_count": hardware_count,
                    }
                )
                continue

            # Number of ACE's: 1
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict["number_of_aces"] = int(groups["number_of_aces"])
                continue

            # Number of ACL's: 1
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                number_of_acls = int(groups["number_of_acls"])
                parsed_dict["number_of_acls"] = number_of_acls
                continue

        return parsed_dict


class ShowPlatformSoftwareFedActiveSecurityFedServiceDetailSchema(MetaParser):

    """Schema for "show platform software fed {switch} active security-fed sis-redirect firewall service-id {service_id} detail" """

    schema = {
        "service_id": str,
        "vrf_id": str,
        "firewall_ip": str,
        "redirect_hd1": str,
        "hmt_hd1": str,
        "router_prefix": str,
        "next_hop": str,
        "adj_last_modified": str,
        "adj_oce_type": str,
        "adj_oce_sub_type": str,
    }


class ShowPlatformSoftwareFedActiveSecurityFedServiceDetail(
    ShowPlatformSoftwareFedActiveSecurityFedServiceDetailSchema
):
    """Schema for show platform software fed {switch} active security-fed sis-redirect firewall service-id {service_id} detail"""

    cli_command = [
        "show platform software fed {switch} active security-fed sis-redirect firewall service-id {service_id} detail",
        "show platform software fed active security-fed sis-redirect firewall service-id {service_id} detail",
    ]

    def cli(self, service_id, switch="", output=None):
        if output is None:
            if not switch:
                cmd = self.cli_command[1].format(service_id=service_id)
            else:
                cmd = self.cli_command[0].format(service_id=service_id, switch=switch)
            output = self.device.execute(cmd)

        parsed_dict = {}

        # Service ID               : 3861840337
        # VRF ID                   : 0
        # IP                       : 172.18.0.2/32
        # Redirect Hdl             : 0x7fe0bb341f38
        # HTM Hdl                  : 0x7fe0bb2f27d8
        # Route Prefix             : 172.18.0.0/30
        # Next Hop                 : 60.60.60.62
        # Adj Last Modified        : 2021-10-17,06:43:16
        # Adj OCE Type             : ADJ
        # Adj OCE Sub-Type         : NONE

        # Service ID               : 3861840337
        p1 = re.compile(r"^Service ID\s+:\s+(?P<service_id>\d+)$")

        # VRF ID                   : 0
        p2 = re.compile(r"^VRF ID\s*:\s*(?P<vrf_id>\d+)$")

        # IP                       : 172.18.0.2/32
        p3 = re.compile(r"^IP\s*:\s*(?P<firewall_ip>[\d/.]+)$")

        # Redirect Hdl             : 0x7fe0bb341f38
        p4 = re.compile(r"^Redirect Hdl\s*:\s*(?P<redirect_hd1>\w+)$")

        # HTM Hdl                  : 0x7fe0bb2f27d8
        p5 = re.compile(r"^HTM Hdl\s*:\s*(?P<hmt_hd1>\w+)$")

        # Route Prefix             : 172.18.0.0/30
        p6 = re.compile(r"^Route Prefix\s*:\s*(?P<router_prefix>[\d/.]+)$")

        # Next Hop                 : 60.60.60.62
        p7 = re.compile(r"^Next Hop\s*:\s*(?P<next_hop>[\d/.]+)$")

        # Adj Last Modified        : 2021-10-17,06:43:16
        p8 = re.compile(
            r"^Adj Last Modified\s*:\s*(?P<adj_last_modified>[\w-]+,[\w:]+)$"
        )

        # Adj OCE Type             : ADJ
        p9 = re.compile(r"^Adj OCE Type\s*:\s*(?P<adj_oce_type>\w+)$")

        # Adj OCE Sub-Type         : NONE
        p10 = re.compile(r"^Adj OCE Sub-Type\s*:\s*(?P<adj_oce_sub_type>\w+)$")

        for line in output.splitlines():
            line = line.strip()

            # Service ID               : 3861840337
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                service_id = groups["service_id"]
                parsed_dict["service_id"] = service_id
                continue

            m = p2.match(line)
            if m:
                groups = m.groupdict()
                vrf_id = groups["vrf_id"]
                parsed_dict["vrf_id"] = vrf_id
                continue

            m = p3.match(line)
            if m:
                groups = m.groupdict()
                firewall_ip = groups["firewall_ip"]
                parsed_dict["firewall_ip"] = firewall_ip
                continue

            m = p4.match(line)
            if m:
                groups = m.groupdict()
                redirect_hd1 = groups["redirect_hd1"]
                parsed_dict["redirect_hd1"] = redirect_hd1
                continue

            m = p5.match(line)
            if m:
                groups = m.groupdict()
                hmt_hd1 = groups["hmt_hd1"]
                parsed_dict["hmt_hd1"] = hmt_hd1
                continue

            m = p6.match(line)
            if m:
                groups = m.groupdict()
                router_prefix = groups["router_prefix"]
                parsed_dict["router_prefix"] = router_prefix
                continue

            m = p7.match(line)
            if m:
                groups = m.groupdict()
                next_hop = groups["next_hop"]
                parsed_dict["next_hop"] = next_hop
                continue

            m = p8.match(line)
            if m:
                groups = m.groupdict()
                adj_last_modified = groups["adj_last_modified"]
                parsed_dict["adj_last_modified"] = adj_last_modified
                continue

            m = p9.match(line)
            if m:
                groups = m.groupdict()
                adj_oce_type = groups["adj_oce_type"]
                parsed_dict["adj_oce_type"] = adj_oce_type
                continue

            m = p10.match(line)
            if m:
                groups = m.groupdict()
                adj_oce_sub_type = groups["adj_oce_sub_type"]
                parsed_dict["adj_oce_sub_type"] = adj_oce_sub_type
                continue

        return parsed_dict


class ShowPlatformSoftwareFedIpsecCounterSchema(MetaParser):
    """Schema for show platform software fed switch active ipsec counters if-id all"""

    schema = {
        "if-id": str,
        Or("inbound_flow", "outbound_flow"): {
            "flow_id": int,
            "sa_index": int,
            "asic_instance": str,
            "packet_format_check_error": int,
            "invalid_sa": int,
            "auth_fail": int,
            "sequence_number_overflows": int,
            "anti_replay_fail": int,
            "packet_count": int,
            "byte_count": int,
        },
    }


class ShowPlatformSoftwareFedIpsecCounter(ShowPlatformSoftwareFedIpsecCounterSchema):
    """Parser for
    show platform software fed switch active ipsec counters if-id all
    """

    cli_command = "show platform software fed switch active ipsec counters if-id all"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        inbound_flag = True

        # Flow Stats for if-id 0x62
        p1 = re.compile(r"^[Ff]low +[Ss]tats +for +if-id +(?P<if_id>\w+)$")

        # Inbound Flow Info for flow id: 44
        p2 = re.compile(
            r"^[Ii]nbound +[Ff]low +[Ii]nfo +for +flow +id+\: +(?P<flow_id>\d+)$"
        )

        # SA Index: 3
        p3 = re.compile(r"^SA +Index+\: +(?P<sa_index>\d+)$")

        # Asic Instance 0: SA Stats
        p4 = re.compile(r"^[Aa]sic +Instance +0+\: +(?P<asic_instance>[\w\s]+)$")

        # Packet Format Check Error: 0
        p5 = re.compile(
            r"^[Pp]acket +[Ff]ormat +[Cc]heck +[Ee]rror+\: +(?P<packet_format_check_error>\d+)$"
        )

        # Invalid SA: 0
        p6 = re.compile(r"^[Ii]nvalid +SA+\: +(?P<invalid_sa>\d+)$")

        # Auth Fail: 0
        p7 = re.compile(r"^[Aa]uth +[Ff]ail+\: +(?P<auth_fail>\d+)$")

        # Sequence Number Overflows: 0
        p8 = re.compile(
            r"^[Ss]equence +[Nn]umber +[Oo]verflows+\: +(?P<sequence_number_overflows>\d+)$"
        )

        # Anti-Replay Fail: 0
        p9 = re.compile(r"^[Aa]nti\-+[Rr]eplay +[Ff]ail+\: +(?P<anti_replay_fail>\d+)$")

        # Packet Count: 2056
        p10 = re.compile(r"^[Pp]acket +[Cc]ount+\: +(?P<packet_count>\d+)$")

        # Byte Count: 177076
        p11 = re.compile(r"^[Bb]yte +[Cc]ount+\: +(?P<byte_count>\d+)$")

        # Outbound Flow Info for flow id: 43
        p12 = re.compile(
            r"^[Oo]utbound +[Ff]low +[Ii]nfo +for +flow +id+\: +(?P<flow_id>\d+)$"
        )

        for line in output.splitlines():
            line = line.strip()
            inbound_dict = ret_dict.setdefault("inbound_flow", {})
            outbound_dict = ret_dict.setdefault("outbound_flow", {})

            # Flow Stats for if-id 0x62
            m = p1.match(line)
            if m:
                ret_dict["if-id"] = m.groupdict()["if_id"]

            # Inbound Flow Info for flow id: 44
            m = p2.match(line)
            if m:
                inbound_flag = True
                inbound_dict["flow_id"] = int(m.groupdict()["flow_id"])
                expected_dict = inbound_dict
                continue

            # SA Index: 3
            m = p3.match(line)
            if m:
                expected_dict["sa_index"] = int(m.groupdict()["sa_index"])
                continue

            # Asic Instance 0: SA Stats
            m = p4.match(line)
            if m:
                expected_dict["asic_instance"] = m.groupdict()["asic_instance"]
                continue

            # Packet Format Check Error: 0
            m = p5.match(line)
            if m:
                expected_dict["packet_format_check_error"] = int(
                    m.groupdict()["packet_format_check_error"]
                )
                continue

            # Invalid SA: 0
            m = p6.match(line)
            if m:
                expected_dict["invalid_sa"] = int(m.groupdict()["invalid_sa"])
                continue

            # Auth Fail: 0
            m = p7.match(line)
            if m:
                expected_dict["auth_fail"] = int(m.groupdict()["auth_fail"])
                continue

            # Sequence Number Overflows: 0
            m = p8.match(line)
            if m:
                expected_dict["sequence_number_overflows"] = int(
                    m.groupdict()["sequence_number_overflows"]
                )
                continue

            # Anti-Replay Fail: 0
            m = p9.match(line)
            if m:
                expected_dict["anti_replay_fail"] = int(
                    m.groupdict()["anti_replay_fail"]
                )
                continue

            # Packet Count: 2056
            m = p10.match(line)
            if m:
                expected_dict["packet_count"] = int(m.groupdict()["packet_count"])
                continue

            # Byte Count: 177076
            m = p11.match(line)
            if m:
                expected_dict["byte_count"] = int(m.groupdict()["byte_count"])
                continue

            # Outbound Flow Info for flow id: 43
            m = p12.match(line)
            if m:
                inbound_flag = False
                outbound_dict["flow_id"] = int(m.groupdict()["flow_id"])
                expected_dict = outbound_dict
                continue

            # SA Index: 3
            m = p3.match(line)
            if m:
                expected_dict["sa_index"] = int(m.groupdict()["sa_index"])
                continue

            # Asic Instance 0: SA Stats
            m = p4.match(line)
            if m:
                expected_dict["asic_instance"] = m.groupdict()["asic_instance"]
                continue

            # Packet Format Check Error: 0
            m = p5.match(line)
            if m:
                expected_dict["packet_format_check_error"] = int(
                    m.groupdict()["packet_format_check_error"]
                )
                continue

            # Invalid SA: 0
            m = p6.match(line)
            if m:
                expected_dict["invalid_sa"] = int(m.groupdict()["invalid_sa"])
                continue

            # Auth Fail: 0
            m = p7.match(line)
            if m:
                expected_dict["auth_fail"] = int(m.groupdict()["auth_fail"])
                continue

            # Sequence Number Overflows: 0
            m = p8.match(line)
            if m:
                expected_dict["sequence_number_overflows"] = int(
                    m.groupdict()["sequence_number_overflows"]
                )
                continue

            # Anti-Replay Fail: 0
            m = p9.match(line)
            if m:
                expected_dict["anti_replay_fail"] = int(
                    m.groupdict()["anti_replay_fail"]
                )
                continue

            # Packet Count: 2056
            m = p10.match(line)
            if m:
                expected_dict["packet_count"] = int(m.groupdict()["packet_count"])
                continue

            # Byte Count: 177076
            m = p11.match(line)
            if m:
                expected_dict["byte_count"] = int(m.groupdict()["byte_count"])
                continue

        return ret_dict


# ====================================================
# Parser for show Platform Software Fed igmp snooping'
# ====================================================
class ShowPlatformSoftwareFedIgmpSnoopingSchema(MetaParser):
    """Schema for show Platform Software Fed igmp snooping"""

    schema = {
        "vlan": {
            Any(): {
                Optional("igmp_en"): str,
                Optional("pimsn_en"): str,
                Optional("snoop_state"): str,
                Optional("snoop_state"): str,
                Optional("flood_md"): str,
                Optional("op_state"): str,
                Optional("stp_tcn_flood"): str,
                Optional("route_en"): str,
                Optional("pim_en"): str,
                Optional("pvlan"): str,
                Optional("in_retry"): str,
                Optional("cck_ep"): str,
                Optional("iosd_md"): str,
                Optional("evpn_en"): str,
                Optional("l3m_adj"): str,
                Optional("mroute_port"): list,
                Optional("flood_port"): list,
                Optional("rep_han"): str,
            }
        }
    }


class ShowPlatformSoftwareFedIgmpSnooping(ShowPlatformSoftwareFedIgmpSnoopingSchema):
    """Parser for show Platform Software Fed igmp snooping"""

    cli_command = [
        "show platform software fed {switch_var} {state} ip igmp snooping vlan {vlan}",
        "show platform software fed {state} ip igmp snooping vlan {vlan}",
    ]

    def cli(self, state="", vlan="", switch_var=None, output=None):
        if output is None:
            if switch_var:
                cmd = self.cli_command[0].format(
                    state=state, switch_var=switch_var, vlan=vlan
                )
            else:
                cmd = self.cli_command[1].format(state=state, vlan=vlan)
            output = self.device.execute(cmd)

        platform_dict = {}

        # Vlan 20
        # ---------
        # IGMPSN Enabled : On

        # Vlan 20
        p0 = re.compile(r"^Vlan\:?\s+(?P<vlan>\d+)$")

        # IGMPSN Enabled : On
        p1 = re.compile("^IGMPSN\s+Enabled\s+:\s+(?P<igmp_en>[\s\w\s]+)$")

        # Snoop State     : ON
        p1_1 = re.compile("^Snoop\s+State\s+:\s+(?P<snoop_state>[\w\s]+)$")

        # Snoop State     : ON
        p1_1 = re.compile("^Snoop\s+State\s+:\s+(?P<snoop_state>[\w\s]+)$")

        # PIMSN Enabled : Off
        p2 = re.compile("^PIMSN\s+Enabled\s+:\s+(?P<pimsn_en>[\s\w\s]+)$")

        # Flood Mode : Off
        p3 = re.compile("^Flood\s+Mode\s+:\s+(?P<flood_md>[\s\w\s]+)$")

        # Oper State : Up
        p4 = re.compile("^Oper\s+State\s+:\s+(?P<op_state>[\s\w\s]+)$")

        # STP TCN Flood : Off
        # STP TCN State : Off
        p5 = re.compile(
            "^STP\s+TCN\s+(Flood|State)\s+:\s+(?P<stp_tcn_flood>[\s\w\s]+)$"
        )
        # STP TCN State : Off
        p5 = re.compile(
            "^STP\s+TCN\s+(Flood|State)\s+:\s+(?P<stp_tcn_flood>[\s\w\s]+)$"
        )

        # Routing Enabled : On
        p6 = re.compile("^Routing\s+Enabled\s+:\s+(?P<route_en>[\s\w\s]+)$")

        # PIM Enabled : On
        p7 = re.compile("^PIM\s+Enabled\s+:\s+(?P<pim_en>[\s\w\s]+)$")

        # PVLAN : No
        p8 = re.compile("^PVLAN\s+:\s+(?P<pvlan>[\s\w\s]+)$")

        # In Retry : 0x0
        p9 = re.compile("^In\s+Retry\s+:\s+(?P<in_retry>[\s\w\s]+)$")

        # CCK Epoch : 0x17
        p10 = re.compile("^CCK\s+Epoch\s+:\s+(?P<cck_ep>[\s\w\s]+)$")

        # IOSD Flood Mode : Off
        p11 = re.compile("^IOSD\s+Flood\s+Mode\s+:\s+(?P<iosd_md>[\s\w\s]+)$")

        # EVPN Proxy Enabled : On
        p12 = re.compile("^EVPN\s+Proxy\s+Enabled\s+:\s+(?P<evpn_en>[\s\w\s]+)$")

        # L3mcast Adj :
        p13 = re.compile("L3mcast\\s+Adj\\s+:(?P<l3m_adj>.*)")

        # Mrouter PortQ :
        p14 = re.compile("^Mrouter\s+[P|p]ort[Q|s]\s+:\s*")
        # nve1.VNI60020(0x200000071)
        p14_1 = re.compile("([A-Za-z]*\d[-().]*){10,}")

        # port:Port-channel10 (ec_member:HundredGigE1/0/5) (group_oif:0) (mrouter_flag:1)
        # port:Port-channel10 (ec_member:HundredGigE1/0/5) (group_oif:0) (mrouter_flag:1)
        # port:Port-channel100 (ec_member:HundredGigE2/5/0/2)
        # port:Port-channel0 (ec_member:HundredGigE1/0/5) (group_oif:0)
        # port:Port-channel77
        p14_2 = re.compile("^port:(?P<port>[\w\-\.]+)(\s+(?P<left>.*))?$")
        # port:Port-channel0 (ec_member:HundredGigE1/0/5) (group_oif:0)
        # port:Port-channel77
        p14_2 = re.compile("^port:(?P<port>[\w\-\.]+)(\s+(?P<left>.*))?$")

        # Flood PortQ :
        p15 = re.compile("^Flood [P|p]ort[Q|s]\s+:\s*")
        # TenGigabitEthernet7/0/13
        # FiveGigabitEthernet1/0/2
        # GigabitEthernet2/0/31
        p15_1 = re.compile("^[A-Za-z-]+[\d\/\.]+$")

        # REP RI handle : 0x0
        p16 = re.compile("^REP\s+RI\s+handle\s+:\s+(?P<rep_han>[\s\w\s]+)$")

        mroute_port_flag = 0
        mroute_list = []
        floodport_flag = 0
        floodport_list = []
        for line in output.splitlines():
            line = line.strip()

            # Vlan 20
            m = p0.match(line)
            if m:
                vlan = int(m.groupdict()["vlan"])
                mac_dict = platform_dict.setdefault("vlan", {}).setdefault(vlan, {})

            # IGMPSN Enabled : On
            m = p1.match(line)
            if m:
                mac_dict["igmp_en"] = m.groupdict()["igmp_en"]
                continue

            # Snoop State     : ON
            m = p1_1.match(line)
            if m:
                mac_dict["snoop_state"] = m.groupdict()["snoop_state"]
                continue

            # PIMSN Enabled : Off
            m = p2.match(line)
            if m:
                mac_dict["pimsn_en"] = m.groupdict()["pimsn_en"]
                continue

            # Flood Mode : Off
            m = p3.match(line)
            if m:
                mac_dict["flood_md"] = m.groupdict()["flood_md"]
                continue

            # Oper State : Up
            m = p4.match(line)
            if m:
                mac_dict["op_state"] = m.groupdict()["op_state"]
                continue

            # STP TCN Flood : Off
            m = p5.match(line)
            if m:
                mac_dict["stp_tcn_flood"] = m.groupdict()["stp_tcn_flood"]
                continue

            # Routing Enabled : On
            m = p6.match(line)
            if m:
                mac_dict["route_en"] = m.groupdict()["route_en"]
                continue

            # PIM Enabled : On
            m = p7.match(line)
            if m:
                mac_dict["pim_en"] = m.groupdict()["pim_en"]
                continue

            # PVLAN : No
            m = p8.match(line)
            if m:
                mac_dict["pvlan"] = m.groupdict()["pvlan"]
                continue

            # In Retry : 0x0
            m = p9.match(line)
            if m:
                mac_dict["in_retry"] = m.groupdict()["in_retry"]
                continue

            # CCK Epoch : 0x17
            m = p10.match(line)
            if m:
                mac_dict["cck_ep"] = m.groupdict()["cck_ep"]
                continue

            # IOSD Flood Mode : Off
            m = p11.match(line)
            if m:
                mac_dict["iosd_md"] = m.groupdict()["iosd_md"]
                continue

            # EVPN Proxy Enabled : On
            m = p12.match(line)
            if m:
                mac_dict["evpn_en"] = m.groupdict()["evpn_en"]
                continue

            # L3mcast Adj :
            m = p13.match(line)
            if m:
                mac_dict["l3m_adj"] = m.groupdict()["l3m_adj"]
                continue
            # else:
            #     mac_dict['l3m_adj'] = ''
            #     continue

            # Mrouter PortQ :
            m = p14.match(line)
            if m:
                mac_dict["mroute_port"] = mroute_list
                mroute_port_flag = 1
                continue

            # nve1.VNI60020(0x200000071)
            m = p14_1.match(line)
            if m:
                if mroute_port_flag == 1:
                    mroute_list.append(m.group(0))
                elif floodport_flag == 1:
                    floodport_list.append(m.group(0))

            # port:Port-channel100 (ec_member:HundredGigE2/5/0/2)
            m = p14_2.match(line)
            if m:
                if mroute_port_flag == 1:
                    mroute_list.append(m.groupdict()["port"].strip())

            # TenGigabitEthernet7/0/13
            # FiveGigabitEthernet1/0/2
            # GigabitEthernet2/0/31
            m = p15_1.match(line)
            if m:
                if mroute_port_flag == 1:
                    mroute_list.append(m.group(0))
                elif floodport_flag == 1:
                    floodport_list.append(m.group(0))

            # Flood PortQ :
            m = p15.match(line)
            if m:
                mroute_port_flag = 0
                floodport_flag = 1
                mac_dict["flood_port"] = floodport_list
                continue

            # REP RI handle : 0x0
            m = p16.match(line)
            if m:
                mac_dict["rep_han"] = m.groupdict()["rep_han"]
                continue

        return platform_dict


# ===================================================================
# Parser for show Platform Software Fed ip igmp snooping groups vlan'
# ===================================================================
class ShowPlatformSoftwareFedIgmpSnoopingGroupsSchema(MetaParser):
    """Schema for show Platform Software Fed ip igmp snooping groups vlan"""

    schema = {
        "vlan": {
            Any(): {
                Optional("group"): str,
                Optional("mem_port"): list,
                Optional("cck_ep"): int,
                Optional("fail_flag"): int,
                Optional("di_hand"): str,
                Optional("rep_ri"): str,
                Optional("si_hand"): str,
                Optional("htm_hand"): str,
            }
        }
    }


class ShowPlatformSoftwareFedIgmpSnoopingGroups(
    ShowPlatformSoftwareFedIgmpSnoopingGroupsSchema
):
    """Parser for show Platform Software Fed ip igmp snooping groups vlan"""

    cli_command = (
        "show platform software fed {state} ip igmp snooping groups vlan {vlan}"
    )

    def cli(self, state="", vlan="", output=None):
        if output is None:
            output = self.device.execute(
                self.cli_command.format(state=state, vlan=vlan)
            )
        platform_dict = {}

        # Vlan:20 Group:229.1.1.1
        # ---------------------------------
        # Member ports :
        # TenGigabitEthernet7/0/13
        # nve1.VNI60020(0x200000062)

        # Vlan:20 Group:229.1.1.1
        p0 = re.compile(r"(^Vlan+:+(?P<vlan>\d+))+\s+(Group:+(?P<group>\w.*))")

        # Member ports :
        p1 = re.compile(r"(^Member +ports   :(?P<mem_port>.*))")
        # TenGigabitEthernet7/0/13
        p1_1 = re.compile("([A-Za-z]*\d[-().]*){10,}")
        # nve1.VNI60020(0x200000062)
        p1_2 = re.compile("^[A-Za-z]+[\d\/]+$")

        # CCK_epoch : 1
        p2 = re.compile(r"(^CCK_epoch+ +:+ +(?P<cck_ep>\d.*)$)")

        # Failure Flags : 0
        p3 = re.compile(r"(^Failure+ +Flags+ +:+ +(?P<fail_flag>\d.*)$)")

        # DI handle : 0x7f95a2320408
        p4 = re.compile(r"(^DI+ +handle+ +:+ +(?P<di_hand>\w.*)$)")

        # REP RI handle : 0x7f95a2320718
        p5 = re.compile(r"(^REP+ +RI+ +handle+ +:+ +(?P<rep_ri>\w.*)$)")

        # SI handle : 0x7f95a2321998
        p6 = re.compile(r"(^SI+ +handle+ +:+ +(?P<si_hand>\w.*)$)")

        # HTM handle : 0x7f95a2321c28
        p7 = re.compile(r"(^HTM+ +handle+ +:+ +(?P<htm_hand>\w.*)$)")

        member_port_flag = 0
        member_list = []
        for line in output.splitlines():
            line = line.strip()

            # Vlan:20 Group:229.1.1.1
            m = p0.match(line)
            if m:
                vlan = m.groupdict()["vlan"]
                mac_dict = platform_dict.setdefault("vlan", {}).setdefault(vlan, {})
                mac_dict["group"] = m.groupdict()["group"]

            # Member ports :
            m = p1.match(line)
            if m:
                mac_dict["mem_port"] = member_list
                member_port_flag = 1
                continue
            # TenGigabitEthernet7/0/13
            m = p1_1.match(line)
            if m:
                if member_port_flag == 1:
                    member_list.append(m.group(0))
            # nve1.VNI60020(0x200000062)
            m = p1_2.match(line)
            if m:
                if member_port_flag == 1:
                    member_list.append(m.group(0))

            # CCK_epoch : 1
            m = p2.match(line)
            if m:
                mac_dict["cck_ep"] = int(m.groupdict()["cck_ep"])
                continue

            # Failure Flags : 0
            m = p3.match(line)
            if m:
                mac_dict["fail_flag"] = int(m.groupdict()["fail_flag"])
                continue

            # DI handle : 0x7f95a2320408
            m = p4.match(line)
            if m:
                mac_dict["di_hand"] = m.groupdict()["di_hand"]
                continue

            # REP RI handle : 0x7f95a2320718
            m = p5.match(line)
            if m:
                mac_dict["rep_ri"] = m.groupdict()["rep_ri"]
                continue

            # SI handle : 0x7f95a2321998
            m = p6.match(line)
            if m:
                mac_dict["si_hand"] = m.groupdict()["si_hand"]
                continue

            # HTM handle : 0x7f95a2321c28
            m = p7.match(line)
            if m:
                mac_dict["htm_hand"] = m.groupdict()["htm_hand"]
                continue

        return platform_dict


# =========================================================
#  Schema for
#  * 'show platform software fed switch {switch_num} acl usage'
#  * 'show platform software fed switch {switch_num} acl usage | include {acl_name}'
# =========================================================
class ShowPlatformSoftwareFedSwitchActiveAclUsageSchema(MetaParser):
    """Schema for 'show platform software fed switch {switch_num} acl usage"""

    schema = {
        Optional("acl_usage"): {
            Optional("ace_software"): {
                Optional("vmr_max"): int,
                Optional("used"): int,
            },
            "acl_name": {
                Any(): {
                    "direction": {
                        Any(): {
                            "feature_type": str,
                            "acl_type": str,
                            "entries_used": int,
                        }
                    }
                }
            },
        }
    }


# =========================================================
#  Parser for
#  * 'show platform software fed switch {switch_num} acl usage'
#  * 'show platform software fed switch {switch_num} acl usage | include {acl_name}'
# =========================================================
class ShowPlatformSoftwareFedSwitchActiveAclUsage(
    ShowPlatformSoftwareFedSwitchActiveAclUsageSchema
):
    """
    Parser for :
        * show platform software fed switch {switch_num} acl usage
        * show platform software fed switch {switch_num} acl usage | include {acl_name}
    """

    cli_command = [
        "show platform software fed switch {switch_num} acl usage",
        "show platform software fed switch {switch_num} acl usage | include {acl_name}",
    ]

    def cli(self, switch_num='active', acl_name="", output=None):
        if output is None:
            if acl_name:
                cmd = self.cli_command[1].format(switch_num=switch_num, acl_name=acl_name)
            else:
                cmd = self.cli_command[0].format(switch_num=switch_num)
            output = self.device.execute(cmd)

        ######  ACE Software VMR max:196608 used:253
        p1 = re.compile(
            r"^\#\#\#\#\#\s+ACE\sSoftware\sVMR\smax\:(?P<vmr_max>\d+)\sused\:(?P<used>\d+)$"
        )

        #   RACL        IPV4     Ingress   PBR-DMVPN    92
        p2 = re.compile(
            r"^(?P<feature_type>\S+)\s+(?P<acl_type>\S+)\s+(?P<direction>\S+)\s+(?P<name>\S+)\s+(?P<entries_used>\d+)$"
        )

        # initial return dictionary
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            acl_usage = ret_dict.setdefault("acl_usage", {})

            ######  ACE Software VMR max:196608 used:253
            m = p1.match(line)
            if m:
                group = m.groupdict()
                acl_usage = ret_dict.setdefault("acl_usage", {})
                ace_software = acl_usage.setdefault("ace_software", {})

                vmr_max = group["vmr_max"]
                ace_software["vmr_max"] = int(vmr_max)

                used = group["used"]
                ace_software["used"] = int(used)
                continue

            #   RACL        IPV4     Ingress   PBR-DMVPN    92
            m = p2.match(line)
            if m:
                group = m.groupdict()
                acl_name = acl_usage.setdefault("acl_name", {}).setdefault(
                    Common.convert_intf_name(group["name"]), {}
                )
                direction = acl_name.setdefault("direction", {}).setdefault(
                    Common.convert_intf_name(group["direction"]), {}
                )

                direction["feature_type"] = group["feature_type"]
                direction["acl_type"] = group["acl_type"]
                direction["entries_used"] = int(group["entries_used"])
                continue
        return ret_dict


# =============================================
# Schema for 'show platform software fed {switch} active vt counter'
# Schema for 'show platform software fed active vt counter'
# =============================================


class ShowPlatformSoftwareFedSwitchActiveVtCounterSchema(MetaParser):
    """Schema for show platform software fed switch active vt counter"""

    schema = {
        "number_of_vlans": int,
    }


class ShowPlatformSoftwareFedSwitchActiveVtCounter(
    ShowPlatformSoftwareFedSwitchActiveVtCounterSchema
):
    """Parser for show platform software fed switch active vt counter"""

    cli_command = [
        "show platform software fed switch {switch} active vt counter",
        "show platform software fed active vt counter",
    ]

    def cli(self, output=None, switch=""):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(switch=switch)
            else:
                cmd = self.cli_command[1]

            output = self.device.execute(cmd)

        # Total no of vlan mappings configured: 1
        p1 = re.compile(
            r"^Total\s+no\s+of\s+vlan\s+mappings\s+configured:\s+(?P<number_of_vlans>\d+)$"
        )
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            matched_values = p1.match(line)
            if matched_values:
                vlan_dict = matched_values.groupdict()
                ret_dict["number_of_vlans"] = int(vlan_dict["number_of_vlans"])
                continue
        return ret_dict


# ======================================================
# Parser for 'show platform software fed switch active vt all '
# ======================================================


class ShowPlatformSoftwareFedSwitchActiveVtAllSchema(MetaParser):
    """Schema for show platform software fed switch active vt all"""

    schema = {
        "interface_id": {
            Any(): {
                "cvlan_id": int,
                "svlan_id": int,
                "action": int,
            }
        }
    }


class ShowPlatformSoftwareFedSwitchActiveVtAll(
    ShowPlatformSoftwareFedSwitchActiveVtAllSchema
):
    """Parser for show platform software fed switch active vt all"""

    cli_command = "show platform software fed switch active vt all"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # interface_id  cvlan_id      svlan-id              action
        # 183           20            30                    1
        p1 = re.compile(
            r"^(?P<interface_id>\d+)\s+(?P<cvlan_id>\d+)\s+(?P<svlan_id>\d+)\s+(?P<action>\d+)$"
        )
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            matched_values = p1.match(line)
            if matched_values:
                parsed_dict = matched_values.groupdict()
                interface_id_var = parsed_dict["interface_id"]
                group = ret_dict.setdefault("interface_id", {}).setdefault(
                    interface_id_var, {}
                )
                group["cvlan_id"] = int(parsed_dict["cvlan_id"])
                group["svlan_id"] = int(parsed_dict["svlan_id"])
                group["action"] = int(parsed_dict["action"])
                continue
        return ret_dict


# ======================================================
# Parser for 'show platform software fed switch active vp summary vlan {vlan}'
# ======================================================


class ShowPlatformSoftwareFedSwitchActiveVpSummaryVlanSchema(MetaParser):
    """Schema for show platform software fed switch <active/standby> vp summary vlan <vlan>"""

    schema = {
        "if_id": {
            Any(): {
                "vlan_id": int,
                "pvlan_mode": str,
                "pvlan_vlan": int,
                "stp_state": str,
                "vtp_pruned": str,
                "untagged": str,
            },
        },
    }


class ShowPlatformSoftwareFedSwitchActiveVpSummaryVlan(
    ShowPlatformSoftwareFedSwitchActiveVpSummaryVlanSchema
):
    """Parser for show platform software fed switch active vp summary vlan <vlan>"""

    cli_command = [
        "show platform software fed {switch_var} {switch} vp summary vlan {vlan}",
        "show platform software fed {switch} vp summary vlan {vlan}",
    ]

    def cli(self, switch=None, vlan=None, switch_var=None, output=None):
        if output is None:
            if switch_var:
                cmd = self.cli_command[0].format(
                    switch=switch, switch_var=switch_var, vlan=vlan
                )
            else:
                cmd = self.cli_command[1].format(switch=switch, vlan=vlan)

            output = self.device.execute(cmd, timeout=600)

        #               32          100         none            1  forwarding          No                No
        p1 = re.compile(
            r"^(?P<if_id>\d+)\s+(?P<vlan_id>\d+)\s+(?P<pvlan_mode>\w+)\s+(?P<pvlan_vlan>\d+)\s+(?P<stp_state>\w+)\s+(?P<vtp_pruned>\w+)\s+(?P<untagged>\w+)$"
        )

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            #               32          100         none            1  forwarding          No                No
            match_obj = p1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if_id_var = dict_val["if_id"]
                if "if_id" not in ret_dict:
                    if_id = ret_dict.setdefault("if_id", {})
                if if_id_var not in ret_dict["if_id"]:
                    if_id_dict = ret_dict["if_id"].setdefault(if_id_var, {})
                if_id_dict["vlan_id"] = int(dict_val["vlan_id"])
                if_id_dict["pvlan_mode"] = dict_val["pvlan_mode"]
                if_id_dict["pvlan_vlan"] = int(dict_val["pvlan_vlan"])
                if_id_dict["stp_state"] = dict_val["stp_state"]
                if_id_dict["vtp_pruned"] = dict_val["vtp_pruned"]
                if_id_dict["untagged"] = dict_val["untagged"]
                continue

        return ret_dict


# ======================================================
# Schema for 'show platform software fed switch <state> ifm if-id <if_id> '
# ======================================================


class ShowPlatformSoftwareFedSwitchStateIfmIfIdIf_idSchema(MetaParser):
    """Schema for show platform software fed switch <state> ifm if-id <if_id>"""

    schema = {
        "int_info": {
            Optional("name"): str,
            "if_id": str,
            Optional("blk_ptr"): str,
            Optional("blk_state"): str,
            Optional("state"): str,
            Optional("status"): str,
            Optional("ref_count"): int,
            Optional("type"): str,
            Optional("create_time"): str,
            Optional("last_modfd_time"): str,
            Optional("cur_time"): str,
            Optional("mac"): str,
            Optional("parent_if_id"): str,
            Optional("client_if_id"): str,
            Optional("switch_num"): int,
            Optional("client_type"): int,
            Optional("asic_num"): int,
            Optional("client_le"): str,
            Optional("dns_punt"): str,
            Optional("ref_count_feature"): str,
        },
        Optional("port_info"): {
            Optional("handle"): str,
            Optional("type"): str,
            Optional("identifier"): str,
            Optional("unit"): str,
        },
        Optional("port_logical_subblk"): {
            Optional("client_le_handle"): str,
            Optional("parent_identifier"): str,
            Optional("asic_num"): str,
            Optional("switch_num"): str,
            Optional("rewr_type"): str,
            Optional("client_mac"): str,
            Optional("ri_handle"): int,
            Optional("di_handle"): int,
            Optional("dst_adj_handle"): int,
            Optional("dst_lkp_handle"): int,
            Optional("src_adj_handle"): str,
            Optional("src_lkp_handle"): int,
        },
        Optional("port_l2_subblk"): {
            Optional("enabled"): str,
            Optional("allow_dot1q"): str,
            Optional("allow_native"): str,
            Optional("def_vlan"): int,
            Optional("allow_priority_tag"): str,
            Optional("allow_unkn_ucast"): str,
            Optional("allow_unkn_mcast"): str,
            Optional("allow_unkn_bcast"): str,
            Optional("protected"): str,
            Optional("ipv4_arp_snp"): str,
            Optional("ipv6_arp_snp"): str,
            Optional("jumbo_mtu"): int,
            Optional("learning_mode"): int,
            Optional("vepa"): str,
            Optional("app_hosting"): str,
        },
        Optional("port_qos_subblk"): {
            Optional("trust_type"): str,
            Optional("def_value"): int,
            Optional("ingrs_tbl_map"): str,
            Optional("egrs_tbl_map"): str,
            Optional("q_map"): str,
        },
        Optional("port_cts_subblk"): {
            Optional("disable_sgacl"): str,
            Optional("trust"): str,
            Optional("propagate"): str,
            Optional("port_sgt"): str,
        },
        Optional("ifm_feature_ref_counts"): {
            Optional("fid"): str,
            Optional("ref_count"): int,
        },
    }


# ======================================================
# Parser for 'show platform software fed switch <state> ifm if-id <if_id> '
# ======================================================
class ShowPlatformSoftwareFedSwitchStateIfmIfIdIf_id(
    ShowPlatformSoftwareFedSwitchStateIfmIfIdIf_idSchema
):
    """Parser for show platform software fed switch <state> ifm if-id <if_id>"""

    cli_command = "show platform software fed switch {state} ifm if-id {if_id}"

    def cli(self, state=None, if_id=None, output=None):
        if output is None:
            cmd = self.cli_command.format(state=state, if_id=if_id)
            output = self.device.execute(cmd)

        # Interface Name          : C320150491
        p1 = re.compile(r"^Interface\s+Name\s+:\s+(?P<name>\S+)$")
        # Interface IF_ID         : 0x0000000013151bdb
        p1_1 = re.compile(r"^Interface\s+IF_ID\s+:\s+(?P<if_id>\S+)$")
        # Interface Block Pointer : 0x7f16cd385568
        p1_2 = re.compile(r"^Interface\s+Block\s+Pointer\s+:\s+(?P<blk_ptr>\S+)$")
        # Interface Block State   : READY
        p1_3 = re.compile(r"^Interface\s+Block\s+State\s+:\s+(?P<blk_state>\w+)$")
        # Interface State         : Enabled
        p1_4 = re.compile(r"^Interface\s+State\s+:\s+(?P<state>\w+)$")
        # Interface Status        : ADD, UPD
        p1_5 = re.compile(r"^Interface\s+Status\s+:\s+(?P<status>\S+\s+\S+)$")
        # Interface Ref-Cnt       : 2
        p1_6 = re.compile(r"^Interface\s+Ref-Cnt\s+:\s+(?P<ref_count>\d+)$")
        # Interface Type          : WIRED_CLIENT
        p1_7 = re.compile(r"^Interface\s+Type\s+:\s+(?P<type>\S+)$")
        # Created Time            : 2022/09/29 12:17:16.343
        p1_8 = re.compile(r"^Created\s+Time\s+:\s+(?P<create_time>\S+\s+\S+)$")
        # Last Modified Time      : 2022/09/29 12:17:16.387
        p1_9 = re.compile(
            r"^Last\s+Modified\s+Time\s+:\s+(?P<last_modfd_time>\S+\s+\S+)$"
        )
        # Current Time            : 2022/09/29 12:29:36.705
        p1_10 = re.compile(r"^Current\s+Time\s+:\s+(?P<cur_time>\S+\s+\S+)$")
        #   mac            : 001b.0c18.918d
        p1_11 = re.compile(r"^mac\s+:\s+(?P<mac>\S+)$")
        #   parent if_id   : 0x0000000000000020
        p1_12 = re.compile(r"^parent\s+if_id\s+:\s+(?P<parent_if_id>\S+)$")
        #   Client if_id   : 0x0000000013151bdb
        p1_13 = re.compile(r"^Client\s+if_id\s+:\s+(?P<client_if_id>\S+)$")
        #   Switch Num     : 1
        p1_14 = re.compile(r"^Switch\s+Num\s+:\s+(?P<switch_num>\d+)$")
        #   Client type    : 1
        p1_15 = re.compile(r"^Client\s+type\s+:\s+(?P<client_type>\d+)$")
        #   ASIC Num       : 1
        p1_16 = re.compile(r"^ASIC\s+Num\s+:\s+(?P<asic_num>\d+)$")
        #   Client LE      : 0x7f16cd0caaa8
        p1_17 = re.compile(r"^Client\s+LE\s+:\s+(?P<client_le>\S+)$")
        #   DNS punt       : False
        p1_18 = re.compile(r"^DNS\s+punt\s+:\s+(?P<dns_punt>\S+)$")
        # Ref Count : 2 (feature Ref Counts + 1)
        p1_19 = re.compile(
            r"^Ref\s+Count\s+:\s+(?P<ref_count_feature>\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+)$"
        )
        #   Handle ............ [0x8b00013f]
        p2 = re.compile(r"^Handle\s+\.*\s+\[(?P<handle>\S+)\]$")
        #   Type .............. [Wired-client]
        p2_1 = re.compile(r"^Type\s+\.*\s+\[(?P<type>\S+)\]$")
        #   Identifier ........ [0x13151bdb]
        p2_2 = re.compile(r"^Identifier\s+\.*\s+\[(?P<identifier>\S+)\]$")
        #   Unit .............. [320150491]
        p2_3 = re.compile(r"^Unit\s+\.*\s+\[(?P<unit>\S+)\]$")
        #       Client LE handle .... [0x7f16cd0caaa8]
        p3 = re.compile(r"^Client\s+LE\s+handle\s+\.*\s+\[(?P<client_le_handle>\S+)\]$")
        #       Parent Identifier : 0x20
        p3_1 = re.compile(r"^Parent\s+Identifier\s+:\s+(?P<parent_identifier>\S+)$")
        #       Asic num          : 0x1
        p3_2 = re.compile(r"^Asic\s+num\s+:\s+(?P<asic_num>\S+)$")
        #       Switch num        : 0x1
        p3_3 = re.compile(r"^Switch\s+num\s+:\s+(?P<switch_num>\S+)$")
        #       Rewrite type      : 0x0
        p3_4 = re.compile(r"^Rewrite\s+type\s+:\s+(?P<rewr_type>\S+)$")
        #       Client mac        : 1:0:0:0:0:0
        p3_5 = re.compile(r"^Client\s+mac\s+:\s+(?P<client_mac>\S+)$")
        #       RI handle         : 53
        p3_6 = re.compile(r"^RI\s+handle\s+:\s+(?P<ri_handle>\d+)$")
        #       DI handle         : 0
        p3_7 = re.compile(r"^DI\s+handle\s+:\s+(?P<di_handle>\d+)$")
        #       Dst Adj  handle   : 0
        p3_8 = re.compile(r"^Dst\s+Adj\s+handle\s+:\s+(?P<dst_adj_handle>\d+)$")
        #       Dst Lookup handle : 0
        p3_9 = re.compile(r"^Dst\s+Lookup\s+handle\s+:\s+(?P<dst_lkp_handle>\d+)$")
        #       Src Adj  handle   : 0x53
        p3_10 = re.compile(r"^Src\s+Adj\s+handle\s+:\s+(?P<src_adj_handle>\S+)$")
        #       Src Lookup handle : 0
        p3_11 = re.compile(r"^Src\s+Lookup\s+handle\s+:\s+(?P<src_lkp_handle>\d+)$")

        #       Enabled ............. [No]
        p4 = re.compile(r"^Enabled\s+\.*\s+\[(?P<enabled>\w+)\]$")
        #       Allow dot1q ......... [No]
        p4_1 = re.compile(r"^Allow\s+dot1q\s+\.*\s+\[(?P<allow_dot1q>\w+)\]$")
        #       Allow native ........ [No]
        p4_2 = re.compile(r"^Allow\s+native\s+\.*\s+\[(?P<allow_native>\w+)\]$")
        #       Default VLAN ........ [0]
        p4_3 = re.compile(r"^Default\s+VLAN\s+\.*\s+\[(?P<def_vlan>\d+)\]$")
        #       Allow priority tag ... [No]
        p4_4 = re.compile(
            r"^Allow\s+priority\s+tag\s+\.*\s+\[(?P<allow_priority_tag>\w+)\]$"
        )
        #       Allow unknown unicast  [No]
        p4_5 = re.compile(
            r"^Allow\s+unknown\s+unicast\s+\[(?P<allow_unkn_ucast>\w+)\]$"
        )
        #       Allow unknown multicast[No]
        p4_6 = re.compile(r"^Allow\s+unknown\s+multicast\[(?P<allow_unkn_mcast>\w+)\]$")
        #       Allow unknown broadcast[No]
        p4_7 = re.compile(r"^Allow\s+unknown\s+broadcast\[(?P<allow_unkn_bcast>\w+)\]$")
        #       Protected ............ [No]
        p4_8 = re.compile(r"^Protected\s+\.*\s+\[(?P<protected>\w+)\]$")
        #       IPv4 ARP snoop ....... [No]
        p4_9 = re.compile(r"^IPv4\s+ARP\s+snoop\s+\.*\s+\[(?P<ipv4_arp_snp>\w+)\]$")
        #       IPv6 ARP snoop ....... [No]
        p4_10 = re.compile(r"^IPv6\s+ARP\s+snoop\s+\.*\s+\[(?P<ipv6_arp_snp>\w+)\]$")
        #       Jumbo MTU ............ [0]
        p4_11 = re.compile(r"^Jumbo\s+MTU\s+\.*\s+\[(?P<jumbo_mtu>\d+)\]$")
        #       Learning Mode ........ [0]
        p4_12 = re.compile(r"^Learning\s+Mode\s+\.*\s+\[(?P<learning_mode>\d+)\]$")
        #       Vepa ................. [Disabled]
        p4_13 = re.compile(r"^Vepa\s+\.*\s+\[(?P<vepa>\w+)\]$")
        #       App Hosting........... [Disabled]
        p4_14 = re.compile(r"^App\s+Hosting\.*\s+\[(?P<app_hosting>\S+)\]$")

        #       Trust Type .................... [0x7]
        p5 = re.compile(r"^Trust\s+Type\s+\.*\s+\[(?P<trust_type>\S+)\]$")
        #       Default Value ................. [0]
        p5_1 = re.compile(r"^Default\s+Value\s+\.*\s+\[(?P<def_value>\d+)\]$")
        #       Ingress Table Map ............. [0x0]
        p5_2 = re.compile(r"^Ingress\s+Table\s+Map\s+\.*\s+\[(?P<ingrs_tbl_map>\S+)\]$")
        #       Egress Table Map .............. [0x0]
        p5_3 = re.compile(r"^Egress\s+Table\s+Map\s+\.*\s+\[(?P<egrs_tbl_map>\S+)\]$")
        #       Queue Map ..................... [0x0]
        p5_4 = re.compile(r"^Queue\s+Map\s+\.*\s+\[(?P<q_map>\S+)\]$")

        #       Disable SGACL .................... [0x0]
        p6 = re.compile(r"^Disable\s+SGACL\s+\.*\s+\[(?P<disable_sgacl>\S+)\]$")
        #       Trust ............................ [0x0]
        p6_1 = re.compile(r"^Trust\s+\.*\s+\[(?P<trust>\S+)\]$")
        #       Propagate ........................ [0x0]
        p6_2 = re.compile(r"^Propagate\s+\.*\s+\[(?P<propagate>\S+)\]$")
        #       Port SGT ......................... [0xffff]
        p6_3 = re.compile(r"^Port\s+SGT\s+\.*\s+\[(?P<port_sgt>\S+)\]$")

        #   FID : 98 (AAL_FEATURE_L2_MULTICAST_IGMP), Ref Count : 1
        p7 = re.compile(
            r"^FID\s+:\s+(?P<fid>\S+\s+\S+),\s+Ref\s+Count\s+:\s+(?P<ref_count>\d+)$"
        )

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            # Interface Name          : C320150491
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["name"] = dict_val["name"]
                continue

            # Interface IF_ID         : 0x0000000013151bdb
            m = p1_1.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["if_id"] = dict_val["if_id"]
                continue

            # Interface Block Pointer : 0x7f16cd385568
            m = p1_2.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["blk_ptr"] = dict_val["blk_ptr"]
                continue

            # Interface Block State   : READY
            m = p1_3.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["blk_state"] = dict_val["blk_state"]
                continue

            # Interface State         : Enabled
            m = p1_4.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["state"] = dict_val["state"]
                continue

            # Interface Status        : ADD, UPD
            m = p1_5.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["status"] = dict_val["status"]
                continue

            # Interface Ref-Cnt       : 2
            m = p1_6.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["ref_count"] = int(dict_val["ref_count"])
                continue

            # Interface Type          : WIRED_CLIENT
            m = p1_7.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["type"] = dict_val["type"]
                continue

            # Created Time            : 2022/09/29 12:17:16.343
            m = p1_8.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["create_time"] = dict_val["create_time"]
                continue

            # Last Modified Time      : 2022/09/29 12:17:16.387
            m = p1_9.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["last_modfd_time"] = dict_val["last_modfd_time"]
                continue

            # Current Time            : 2022/09/29 12:29:36.705
            m = p1_10.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["cur_time"] = dict_val["cur_time"]
                continue

            #   mac            : 001b.0c18.918d
            m = p1_11.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["mac"] = dict_val["mac"]
                continue

            #   parent if_id   : 0x0000000000000020
            m = p1_12.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["parent_if_id"] = dict_val["parent_if_id"]
                continue

            #   Client if_id   : 0x0000000013151bdb
            m = p1_13.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["client_if_id"] = dict_val["client_if_id"]
                continue

            #   Switch Num     : 1
            m = p1_14.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["switch_num"] = int(dict_val["switch_num"])
                continue

            #   Client type    : 1
            m = p1_15.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["client_type"] = int(dict_val["client_type"])
                continue

            #   ASIC Num       : 1
            m = p1_16.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["asic_num"] = int(dict_val["asic_num"])
                continue

            #   Client LE      : 0x7f16cd0caaa8
            m = p1_17.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["client_le"] = dict_val["client_le"]
                continue

            #   DNS punt       : False
            m = p1_18.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["dns_punt"] = dict_val["dns_punt"]
                continue

            # Ref Count : 2 (feature Ref Counts + 1)
            m = p1_19.match(line)
            if m:
                dict_val = m.groupdict()
                if "int_info" not in ret_dict:
                    int_info = ret_dict.setdefault("int_info", {})
                int_info["ref_count_feature"] = dict_val["ref_count_feature"]
                continue

            #   Handle ............ [0x8b00013f]
            m = p2.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_info" not in ret_dict:
                    port_info = ret_dict.setdefault("port_info", {})
                port_info["handle"] = dict_val["handle"]
                continue

            #   Type .............. [Wired-client]
            m = p2_1.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_info" not in ret_dict:
                    port_info = ret_dict.setdefault("port_info", {})
                port_info["type"] = dict_val["type"]
                continue

            #   Identifier ........ [0x13151bdb]
            m = p2_2.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_info" not in ret_dict:
                    port_info = ret_dict.setdefault("port_info", {})
                port_info["identifier"] = dict_val["identifier"]
                continue

            #   Unit .............. [320150491]
            m = p2_3.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_info" not in ret_dict:
                    port_info = ret_dict.setdefault("port_info", {})
                port_info["unit"] = dict_val["unit"]
                continue

            #       Client LE handle .... [0x7f16cd0caaa8]
            m = p3.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_logical_subblk" not in ret_dict:
                    port_logical_subblk = ret_dict.setdefault("port_logical_subblk", {})
                port_logical_subblk["client_le_handle"] = dict_val["client_le_handle"]
                continue

            #       Parent Identifier : 0x20
            m = p3_1.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_logical_subblk" not in ret_dict:
                    port_logical_subblk = ret_dict.setdefault("port_logical_subblk", {})
                port_logical_subblk["parent_identifier"] = dict_val["parent_identifier"]
                continue

            #       Asic num          : 0x1
            m = p3_2.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_logical_subblk" not in ret_dict:
                    port_logical_subblk = ret_dict.setdefault("port_logical_subblk", {})
                port_logical_subblk["asic_num"] = dict_val["asic_num"]
                continue

            #       Switch num        : 0x1
            m = p3_3.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_logical_subblk" not in ret_dict:
                    port_logical_subblk = ret_dict.setdefault("port_logical_subblk", {})
                port_logical_subblk["switch_num"] = dict_val["switch_num"]
                continue

            #       Rewrite type      : 0x0
            m = p3_4.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_logical_subblk" not in ret_dict:
                    port_logical_subblk = ret_dict.setdefault("port_logical_subblk", {})
                port_logical_subblk["rewr_type"] = dict_val["rewr_type"]
                continue

            #       Client mac        : 1:0:0:0:0:0
            m = p3_5.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_logical_subblk" not in ret_dict:
                    port_logical_subblk = ret_dict.setdefault("port_logical_subblk", {})
                port_logical_subblk["client_mac"] = dict_val["client_mac"]
                continue

            #       RI handle         : 53
            m = p3_6.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_logical_subblk" not in ret_dict:
                    port_logical_subblk = ret_dict.setdefault("port_logical_subblk", {})
                port_logical_subblk["ri_handle"] = int(dict_val["ri_handle"])
                continue

            #       DI handle         : 0
            m = p3_7.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_logical_subblk" not in ret_dict:
                    port_logical_subblk = ret_dict.setdefault("port_logical_subblk", {})
                port_logical_subblk["di_handle"] = int(dict_val["di_handle"])
                continue

            #       Dst Adj  handle   : 0
            m = p3_8.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_logical_subblk" not in ret_dict:
                    port_logical_subblk = ret_dict.setdefault("port_logical_subblk", {})
                port_logical_subblk["dst_adj_handle"] = int(dict_val["dst_adj_handle"])
                continue

            #       Dst Lookup handle : 0
            m = p3_9.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_logical_subblk" not in ret_dict:
                    port_logical_subblk = ret_dict.setdefault("port_logical_subblk", {})
                port_logical_subblk["dst_lkp_handle"] = int(dict_val["dst_lkp_handle"])
                continue

            #       Src Adj  handle   : 0x53
            m = p3_10.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_logical_subblk" not in ret_dict:
                    port_logical_subblk = ret_dict.setdefault("port_logical_subblk", {})
                port_logical_subblk["src_adj_handle"] = dict_val["src_adj_handle"]
                continue

            #       Src Lookup handle : 0
            m = p3_11.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_logical_subblk" not in ret_dict:
                    port_logical_subblk = ret_dict.setdefault("port_logical_subblk", {})
                port_logical_subblk["src_lkp_handle"] = int(dict_val["src_lkp_handle"])
                continue

            #       Enabled ............. [No]
            m = p4.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_l2_subblk" not in ret_dict:
                    port_l2_subblk = ret_dict.setdefault("port_l2_subblk", {})
                port_l2_subblk["enabled"] = dict_val["enabled"]
                continue

            #       Allow dot1q ......... [No]
            m = p4_1.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_l2_subblk" not in ret_dict:
                    port_l2_subblk = ret_dict.setdefault("port_l2_subblk", {})
                port_l2_subblk["allow_dot1q"] = dict_val["allow_dot1q"]
                continue

            #       Allow native ........ [No]
            m = p4_2.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_l2_subblk" not in ret_dict:
                    port_l2_subblk = ret_dict.setdefault("port_l2_subblk", {})
                port_l2_subblk["allow_native"] = dict_val["allow_native"]
                continue

            #       Default VLAN ........ [0]
            m = p4_3.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_l2_subblk" not in ret_dict:
                    port_l2_subblk = ret_dict.setdefault("port_l2_subblk", {})
                port_l2_subblk["def_vlan"] = int(dict_val["def_vlan"])
                continue

            #       Allow priority tag ... [No]
            m = p4_4.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_l2_subblk" not in ret_dict:
                    port_l2_subblk = ret_dict.setdefault("port_l2_subblk", {})
                port_l2_subblk["allow_priority_tag"] = dict_val["allow_priority_tag"]
                continue

            #       Allow unknown unicast  [No]
            m = p4_5.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_l2_subblk" not in ret_dict:
                    port_l2_subblk = ret_dict.setdefault("port_l2_subblk", {})
                port_l2_subblk["allow_unkn_ucast"] = dict_val["allow_unkn_ucast"]
                continue

            #       Allow unknown multicast[No]
            m = p4_6.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_l2_subblk" not in ret_dict:
                    port_l2_subblk = ret_dict.setdefault("port_l2_subblk", {})
                port_l2_subblk["allow_unkn_mcast"] = dict_val["allow_unkn_mcast"]
                continue

            #       Allow unknown broadcast[No]
            m = p4_7.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_l2_subblk" not in ret_dict:
                    port_l2_subblk = ret_dict.setdefault("port_l2_subblk", {})
                port_l2_subblk["allow_unkn_bcast"] = dict_val["allow_unkn_bcast"]
                continue

            #       Protected ............ [No]
            m = p4_8.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_l2_subblk" not in ret_dict:
                    port_l2_subblk = ret_dict.setdefault("port_l2_subblk", {})
                port_l2_subblk["protected"] = dict_val["protected"]
                continue

            #       IPv4 ARP snoop ....... [No]
            m = p4_9.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_l2_subblk" not in ret_dict:
                    port_l2_subblk = ret_dict.setdefault("port_l2_subblk", {})
                port_l2_subblk["ipv4_arp_snp"] = dict_val["ipv4_arp_snp"]
                continue

            #       IPv6 ARP snoop ....... [No]
            m = p4_10.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_l2_subblk" not in ret_dict:
                    port_l2_subblk = ret_dict.setdefault("port_l2_subblk", {})
                port_l2_subblk["ipv6_arp_snp"] = dict_val["ipv6_arp_snp"]
                continue

            #       Jumbo MTU ............ [0]
            m = p4_11.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_l2_subblk" not in ret_dict:
                    port_l2_subblk = ret_dict.setdefault("port_l2_subblk", {})
                port_l2_subblk["jumbo_mtu"] = int(dict_val["jumbo_mtu"])
                continue

            #       Learning Mode ........ [0]
            m = p4_12.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_l2_subblk" not in ret_dict:
                    port_l2_subblk = ret_dict.setdefault("port_l2_subblk", {})
                port_l2_subblk["learning_mode"] = int(dict_val["learning_mode"])
                continue

            #       Vepa ................. [Disabled]
            m = p4_13.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_l2_subblk" not in ret_dict:
                    port_l2_subblk = ret_dict.setdefault("port_l2_subblk", {})
                port_l2_subblk["vepa"] = dict_val["vepa"]
                continue

            #       App Hosting........... [Disabled]
            m = p4_14.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_l2_subblk" not in ret_dict:
                    port_l2_subblk = ret_dict.setdefault("port_l2_subblk", {})
                port_l2_subblk["app_hosting"] = dict_val["app_hosting"]
                continue

            #       Trust Type .................... [0x7]
            m = p5.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_qos_subblk" not in ret_dict:
                    port_qos_subblk = ret_dict.setdefault("port_qos_subblk", {})
                port_qos_subblk["trust_type"] = dict_val["trust_type"]
                continue

            #       Default Value ................. [0]
            m = p5_1.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_qos_subblk" not in ret_dict:
                    port_qos_subblk = ret_dict.setdefault("port_qos_subblk", {})
                port_qos_subblk["def_value"] = int(dict_val["def_value"])
                continue

            #       Ingress Table Map ............. [0x0]
            m = p5_2.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_qos_subblk" not in ret_dict:
                    port_qos_subblk = ret_dict.setdefault("port_qos_subblk", {})
                port_qos_subblk["ingrs_tbl_map"] = dict_val["ingrs_tbl_map"]
                continue

            #       Egress Table Map .............. [0x0]
            m = p5_3.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_qos_subblk" not in ret_dict:
                    port_qos_subblk = ret_dict.setdefault("port_qos_subblk", {})
                port_qos_subblk["egrs_tbl_map"] = dict_val["egrs_tbl_map"]
                continue

            #       Queue Map ..................... [0x0]
            m = p5_4.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_qos_subblk" not in ret_dict:
                    port_qos_subblk = ret_dict.setdefault("port_qos_subblk", {})
                port_qos_subblk["q_map"] = dict_val["q_map"]
                continue

            #       Disable SGACL .................... [0x0]
            m = p6.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_cts_subblk" not in ret_dict:
                    port_cts_subblk = ret_dict.setdefault("port_cts_subblk", {})
                port_cts_subblk["disable_sgacl"] = dict_val["disable_sgacl"]
                continue

            #       Trust ............................ [0x0]
            m = p6_1.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_cts_subblk" not in ret_dict:
                    port_cts_subblk = ret_dict.setdefault("port_cts_subblk", {})
                port_cts_subblk["trust"] = dict_val["trust"]
                continue

            #       Propagate ........................ [0x0]
            m = p6_2.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_cts_subblk" not in ret_dict:
                    port_cts_subblk = ret_dict.setdefault("port_cts_subblk", {})
                port_cts_subblk["propagate"] = dict_val["propagate"]
                continue

            #       Port SGT ......................... [0xffff]
            m = p6_3.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_cts_subblk" not in ret_dict:
                    port_cts_subblk = ret_dict.setdefault("port_cts_subblk", {})
                port_cts_subblk["port_sgt"] = dict_val["port_sgt"]
                continue

            #   FID : 98 (AAL_FEATURE_L2_MULTICAST_IGMP), Ref Count : 1
            m = p7.match(line)
            if m:
                dict_val = m.groupdict()
                if "ifm_feature_ref_counts" not in ret_dict:
                    ifm_feature_ref_counts = ret_dict.setdefault(
                        "ifm_feature_ref_counts", {}
                    )
                ifm_feature_ref_counts["fid"] = dict_val["fid"]
                ifm_feature_ref_counts["ref_count"] = int(dict_val["ref_count"])
                continue

        return ret_dict


class ShowPlatformSoftwareFedActiveMonitorSchema(MetaParser):
    """
    Schema for 'show platform software fed active monitor {session}'
    """

    schema = {
        "session_type": str,
        "source_ports": {"rx": list, "tx": list},
        Optional("destination_ports"): list,
        Optional("source_vlans"): list,
        Optional("destination_vlans"): list,
        "source_rspan_vlan": int,
        "destination_rspan_vlan": int,
        "encap": str,
        "ingress_forwarding": str,
        Optional("filter_vlans"): list,
        "erspan_enable": int,
        "erspan_hw_programmed": int,
        "erspan_mandatory_cfg": int,
        "erspan_id": int,
        Optional("gre_protocol"): str,
        "mtu": int,
        "ip_tos": int,
        "ip_ttl": int,
        "cos": int,
        "vrf_id": int,
        "tunnel_if_id": int,
        "destination_ip": str,
        "org_ip": str,
        Optional("sgt_count"): int,
        Optional("sgt_tag"): str,
    }


class ShowPlatformSoftwareFedActiveMonitor(ShowPlatformSoftwareFedActiveMonitorSchema):
    """
    Parser for 'show platform software fed active monitor {session}'
    """

    cli_command = "show platform software fed active monitor {session}"

    def cli(self, session, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(session=session))

        # Session Type         : ERSPAN Source Session
        p1 = re.compile(r"^Session Type\s+:\s+(?P<session_type>[\w\s]+)$")

        # Source Ports         : RX: GigabitEthernet1/0/1 TenGigabitEthernet1/1/3 TX: None
        p2 = re.compile(
            r"^Source Ports\s+: RX:\s+(?P<rx>[\w\/\s]+)\sTX:\s+(?P<tx>[\w\/\s]+)$"
        )

        # Destination Ports    : TwoGigabitEthernet1/0/13
        p3 = re.compile(
            r"^Destination Ports\s+:\s+(?P<destination_ports>[\w\/\s]+(?<!None))$"
        )

        # Source VLANs         : None
        p4 = re.compile(r"^Source VLANs\s+:\s+(?P<source_vlans>[\w\-\d\s]+(?<!None))$")

        # Destination VLANs    : None
        p5 = re.compile(
            r"^Destination VLANs\s+:\s+(?P<destination_vlans>[\w\-\d\s]+(?<!None))$"
        )

        # Source RSPAN VLAN    : 0
        p6 = re.compile(r"^Source RSPAN VLAN\s+:\s+(?P<source_rspan_vlan>\d+)$")

        # DST RSPAN VLAN       : 0
        p7 = re.compile(r"^DST RSPAN VLAN\s+:\s+(?P<destination_rspan_vlan>\d+)$")

        # Encap                : Native
        p8 = re.compile(r"^Encap\s+:\s+(?P<encap>\S+)$")

        # Ingress Forwarding   : Disabled
        p9 = re.compile(r"^Ingress Forwarding\s+:\s+(?P<ingress_forwarding>\S+)$")

        # Filter VLANs         : None
        p10 = re.compile(r"^Filter VLANs\s+:\s+(?P<filter_vlans>[\d\s]+(?<!None))$")

        # ERSPAN Enable        : 1
        p11 = re.compile(r"^ERSPAN Enable\s+:\s+(?P<erspan_enable>\d+)$")

        # ERSPAN Hw Programmed : 1
        p12 = re.compile(r"^ERSPAN Hw Programmed\s+:\s+(?P<erspan_hw_programmed>\d+)$")

        # ERSPAN Mandatory Cfg : 1
        p13 = re.compile(r"^ERSPAN Mandatory Cfg\s+:\s+(?P<erspan_mandatory_cfg>\d+)$")

        # ERSPAN Id            : 3
        p14 = re.compile(r"^ERSPAN Id\s+:\s+(?P<erspan_id>\d+)$")

        # Gre Prot             : 88be
        p15 = re.compile(r"^Gre Prot\s+:\s+(?P<gre_protocol>\S+)$")

        # MTU                  : 9000
        p16 = re.compile(r"^MTU\s+:\s+(?P<mtu>\d+)$")

        # Ip Tos               : 0 (DSCP:0)
        p17 = re.compile(r"^Ip Tos\s+:\s+(?P<ip_tos>\d+).+$")

        # Ip Ttl               : 255
        p18 = re.compile(r"^Ip Ttl\s+:\s+(?P<ip_ttl>\d+)$")

        # Cos                  : 0
        p19 = re.compile(r"^Cos\s+:\s+(?P<cos>\d+)$")

        # Vrf Id               : 0
        p20 = re.compile(r"^Vrf Id\s+:\s+(?P<vrf_id>\d+)$")

        # Tunnel IfId          : 65
        p21 = re.compile(r"^Tunnel IfId\s+:\s+(?P<tunnel_if_id>\d+)$")

        # Dst Ip               : 1.1.3.2
        p22 = re.compile(r"^Dst Ip\s+:\s+(?P<destination_ip>\S+)$")

        # Org Ip               : 1.1.3.1
        p23 = re.compile(r"^Org Ip\s+:\s+(?P<org_ip>\S+)$")

        # SGT count            : 0
        p24 = re.compile(r"^SGT count\s+:\s+(?P<sgt_count>\d+)$")

        # SGT Tag(s)           :
        p25 = re.compile(r"^SGT Tag\(s\)\s+:\s+(?P<sgt_tag>\S+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                # ret_dict.update(m.groupdict())
                ret_dict["session_type"] = m.groupdict()["session_type"]
                continue

            m = p2.match(line)
            if m:
                port_dict = ret_dict.setdefault("source_ports", {})
                port_dict["rx"] = m.groupdict()["rx"].split()
                port_dict["tx"] = m.groupdict()["tx"].split()
                continue

            m = p3.match(line)
            if m:
                ret_dict.setdefault(
                    "destination_ports", m.groupdict()["destination_ports"].split(" ")
                )
                continue

            m = p4.match(line)
            if m:
                ret_dict.setdefault(
                    "source_vlans", m.groupdict()["source_vlans"].split(" ")
                )
                continue

            m = p5.match(line)
            if m:
                ret_dict.setdefault(
                    "destination_vlans", m.groupdict()["destination_vlans"].split(" ")
                )
                continue

            m = p6.match(line)
            if m:
                ret_dict.setdefault(
                    "source_rspan_vlan", int(m.groupdict()["source_rspan_vlan"])
                )
                continue

            m = p7.match(line)
            if m:
                ret_dict.setdefault(
                    "destination_rspan_vlan",
                    int(m.groupdict()["destination_rspan_vlan"]),
                )
                continue

            m = p8.match(line)
            if m:
                ret_dict.setdefault("encap", m.groupdict()["encap"])
                continue

            m = p9.match(line)
            if m:
                ret_dict.setdefault(
                    "ingress_forwarding", m.groupdict()["ingress_forwarding"]
                )
                continue

            m = p10.match(line)
            if m:
                ret_dict.setdefault("filter_vlans", m.groupdict()["filter_vlans"])
                continue

            m = p11.match(line)
            if m:
                ret_dict.setdefault(
                    "erspan_enable", int(m.groupdict()["erspan_enable"])
                )
                continue

            m = p12.match(line)
            if m:
                ret_dict.setdefault(
                    "erspan_hw_programmed", int(m.groupdict()["erspan_hw_programmed"])
                )
                continue

            m = p13.match(line)
            if m:
                ret_dict.setdefault(
                    "erspan_mandatory_cfg", int(m.groupdict()["erspan_mandatory_cfg"])
                )
                continue

            m = p14.match(line)
            if m:
                ret_dict.setdefault("erspan_id", int(m.groupdict()["erspan_id"]))
                continue

            m = p15.match(line)
            if m:
                ret_dict.setdefault("gre_protocol", m.groupdict()["gre_protocol"])
                continue

            m = p16.match(line)
            if m:
                ret_dict.setdefault("mtu", int(m.groupdict()["mtu"]))
                continue

            m = p17.match(line)
            if m:
                ret_dict.setdefault("ip_tos", int(m.groupdict()["ip_tos"]))
                continue

            m = p18.match(line)
            if m:
                ret_dict.setdefault("ip_ttl", int(m.groupdict()["ip_ttl"]))
                continue

            m = p19.match(line)
            if m:
                ret_dict.setdefault("cos", int(m.groupdict()["cos"]))
                continue

            m = p20.match(line)
            if m:
                ret_dict.setdefault("vrf_id", int(m.groupdict()["vrf_id"]))
                continue

            m = p21.match(line)
            if m:
                ret_dict.setdefault("tunnel_if_id", int(m.groupdict()["tunnel_if_id"]))
                continue

            m = p22.match(line)
            if m:
                ret_dict.setdefault("destination_ip", m.groupdict()["destination_ip"])
                continue

            m = p23.match(line)
            if m:
                ret_dict.setdefault("org_ip", m.groupdict()["org_ip"])
                continue

            m = p24.match(line)
            if m:
                ret_dict.setdefault("sgt_count", int(m.groupdict()["sgt_count"]))
                continue

            m = p25.match(line)
            if m:
                ret_dict.setdefault("sgt_tag", m.groupdict()["sgt_tag"])
                continue

        return ret_dict


class ShowPlatformSoftwareFedSwitchActiveMonitor(ShowPlatformSoftwareFedActiveMonitor):
    """
    Parser for 'show platform software fed switch active monitor {session}'
    """

    cli_command = "show platform software fed switch active monitor {session}"

    def cli(self, session, output=None):
        return super().cli(session=session, output=output)


# ======================================================
# Parser for 'show platform software fed {switch} active ifm interfaces vlan',
#            'show platform software fed active ifm interfaces vlan'
# ======================================================


class ShowPlatformSoftwareFedIfmInterfacesSchema(MetaParser):
    """Schema for 'show platform software fed {switch} active ifm interfaces vlan',
    'show platform software fed active ifm interfaces vlan'"""

    schema = {"interfaces": {Any(): {"if_id": str, "state": str}}}


class ShowPlatformSoftwareFedIfmInterfaces(ShowPlatformSoftwareFedIfmInterfacesSchema):
    """Parser for 'show platform software fed {switch} active ifm interfaces vlan',
    'show platform software fed active ifm interfaces vlan'"""

    cli_command = [
        "show platform software fed {switch} active ifm interfaces vlan",
        "show platform software fed active ifm interfaces vlan",
    ]

    def cli(self, switch="", output=None):
        if output is None:
            if switch:
                out = self.device.execute(self.cli_command[0].format(switch=switch))
            else:
                out = self.device.execute(self.cli_command[1])
        else:
            out = output

        ret_dict = {}

        # Vlan10 0x0000005d READY
        p1 = re.compile(
            r"^(?P<interface>\S+)\s+(?P<if_id>\d+x+\w+)\s+(?P<state>[\w\s]+)$"
        )

        for line in out.splitlines():
            line = line.strip()

            # Vlan10 0x0000005d READY
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = group["interface"]
                interface_dict = ret_dict.setdefault("interfaces", {}).setdefault(
                    interface, {}
                )
                interface_dict["if_id"] = group["if_id"]
                interface_dict["state"] = str(group["state"])
                continue

        return ret_dict


# ==========================================================================================
# Parser Schema for 'show platform software fed active vt hardware if-id'
# ==========================================================================================


class ShowPlatformSoftwareFedActiveVtHardwareIfIdSchema(MetaParser):
    """
    Schema for
        * 'show platform software fed active vt hardware if-id {if_id}'
    """

    schema = {
        "mapping": {
            Any(): {
                "vlan_id": int,
                "translated_vlan_id": int,
            }
        }
    }


# ==========================================================================================
# Parser for 'show platform software fed active vt hardware if-id'
# ==========================================================================================


class ShowPlatformSoftwareFedActiveVtHardwareIfId(
    ShowPlatformSoftwareFedActiveVtHardwareIfIdSchema
):
    """
    Parser for
        * 'show platform software fed active vt hardware if-id {if_id}'
    """

    cli_command = "show platform software fed active vt hardware if-id {if_id}"

    def cli(self, if_id, output=None):
        cmd = self.cli_command.format(if_id=if_id)

        if output is None:
            output = self.device.execute(cmd)

        ret_dict = {}
        # Forward Mapping
        # Reverse Mapping
        p1 = re.compile(r"^(?P<mapping>\S+) Mapping$")

        # 40            30
        p2 = re.compile(r"^(?P<vlan_id>\d+)\s*(?P<translated_id>\d+)$")

        for line in output.splitlines():
            line = line.strip()
            # Forward Mapping
            # Reverse Mapping
            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault("mapping", {}).setdefault(
                    group["mapping"].lower(), {}
                )
                continue

            # 40            30
            m = p2.match(line)
            if m:
                group = m.groupdict()
                root_dict["vlan_id"] = int(group["vlan_id"])
                root_dict["translated_vlan_id"] = int(group["translated_id"])

        return ret_dict


class ShowPlatformSoftwareFedActiveMonitorSchema(MetaParser):
    """
    Schema for 'show platform software fed active monitor {session}'
    """

    schema = {
        "session_type": str,
        "source_ports": {Optional("rx"): list, Optional("tx"): list},
        Optional("destination_ports"): list,
        Optional("source_vlans"): list,
        Optional("destination_vlans"): list,
        "source_rspan_vlan": int,
        "destination_rspan_vlan": int,
        "encap": str,
        "ingress_forwarding": str,
        Optional("filter_vlans"): list,
        "erspan_enable": int,
        "erspan_hw_programmed": int,
        "erspan_mandatory_cfg": int,
        "erspan_id": int,
        Optional("gre_protocol"): str,
        "mtu": int,
        "ip_tos": int,
        "ip_ttl": int,
        "cos": int,
        "vrf_id": int,
        "tunnel_if_id": int,
        "destination_ip": str,
        "org_ip": str,
        Optional("sgt_count"): int,
        Optional("sgt_tag"): str,
    }


class ShowPlatformSoftwareFedActiveMonitor(ShowPlatformSoftwareFedActiveMonitorSchema):
    """
    Parser for 'show platform software fed active monitor {session}'
    """

    cli_command = "show platform software fed active monitor {session}"

    def cli(self, session, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(session=session))

        # Session Type         : ERSPAN Source Session
        p1 = re.compile(r"^Session Type\s+:\s+(?P<session_type>[\w\s]+)$")

        # Source Ports         : RX: GigabitEthernet1/0/1 TenGigabitEthernet1/1/3 TX: None
        # Source Ports         : RX: FourHundredGigE1/0/31 TX:
        p2 = re.compile(
            r"^Source Ports\s+: RX:\s+(?P<rx>[\w\/\s]+)\sTX:\s*(?P<tx>[\w\/\s]+)?$"
        )
        # Source Ports         : RX: FourHundredGigE1/0/31 TX:
        p2 = re.compile(
            r"^Source Ports\s+: RX:\s+(?P<rx>[\w\/\s]+)\sTX:\s*(?P<tx>[\w\/\s]+)?$"
        )

        # Destination Ports    : TwoGigabitEthernet1/0/13
        p3 = re.compile(
            r"^Destination Ports\s+:\s+(?P<destination_ports>[\w\/\s]+(?<!None))$"
        )

        # Source VLANs         : None
        p4 = re.compile(r"^Source VLANs\s+:\s+(?P<source_vlans>[\w\-\d\s]+(?<!None))$")

        # Destination VLANs    : None
        p5 = re.compile(
            r"^Destination VLANs\s+:\s+(?P<destination_vlans>[\w\-\d\s]+(?<!None))$"
        )

        # Source RSPAN VLAN    : 0
        p6 = re.compile(r"^Source RSPAN VLAN\s+:\s+(?P<source_rspan_vlan>\d+)$")

        # DST RSPAN VLAN       : 0
        p7 = re.compile(r"^DST RSPAN VLAN\s+:\s+(?P<destination_rspan_vlan>\d+)$")

        # Encap                : Native
        p8 = re.compile(r"^Encap\s+:\s+(?P<encap>\S+)$")

        # Ingress Forwarding   : Disabled
        p9 = re.compile(r"^Ingress Forwarding\s+:\s+(?P<ingress_forwarding>\S+)$")

        # Filter VLANs         : None
        p10 = re.compile(r"^Filter VLANs\s+:\s+(?P<filter_vlans>[\d\s]+(?<!None))$")

        # ERSPAN Enable        : 1
        p11 = re.compile(r"^ERSPAN Enable\s+:\s+(?P<erspan_enable>\d+)$")

        # ERSPAN Hw Programmed : 1
        p12 = re.compile(r"^ERSPAN Hw Programmed\s+:\s+(?P<erspan_hw_programmed>\d+)$")

        # ERSPAN Mandatory Cfg : 1
        p13 = re.compile(r"^ERSPAN Mandatory Cfg\s+:\s+(?P<erspan_mandatory_cfg>\d+)$")

        # ERSPAN Id            : 3
        p14 = re.compile(r"^ERSPAN Id\s+:\s+(?P<erspan_id>\d+)$")

        # Gre Prot             : 88be
        p15 = re.compile(r"^Gre Prot\s+:\s+(?P<gre_protocol>\S+)$")

        # MTU                  : 9000
        p16 = re.compile(r"^MTU\s+:\s+(?P<mtu>\d+)$")

        # Ip Tos               : 0 (DSCP:0)
        p17 = re.compile(r"^Ip Tos\s+:\s+(?P<ip_tos>\d+).+$")

        # Ip Ttl               : 255
        p18 = re.compile(r"^Ip Ttl\s+:\s+(?P<ip_ttl>\d+)$")

        # Cos                  : 0
        p19 = re.compile(r"^Cos\s+:\s+(?P<cos>\d+)$")

        # Vrf Id               : 0
        p20 = re.compile(r"^Vrf Id\s+:\s+(?P<vrf_id>\d+)$")

        # Tunnel IfId          : 65
        p21 = re.compile(r"^Tunnel IfId\s+:\s+(?P<tunnel_if_id>\d+)$")

        # Dst Ip               : 1.1.3.2
        p22 = re.compile(r"^Dst Ip\s+:\s+(?P<destination_ip>\S+)$")

        # Org Ip               : 1.1.3.1
        p23 = re.compile(r"^Org Ip\s+:\s+(?P<org_ip>\S+)$")

        # SGT count            : 0
        p24 = re.compile(r"^SGT count\s+:\s+(?P<sgt_count>\d+)$")

        # SGT Tag(s)           :
        p25 = re.compile(r"^SGT Tag\(s\)\s+:\s+(?P<sgt_tag>\S+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                # ret_dict.update(m.groupdict())
                ret_dict["session_type"] = m.groupdict()["session_type"]
                continue

            m = p2.match(line)
            if m:
                port_dict = ret_dict.setdefault("source_ports", {})
                if m.groupdict()["rx"]:
                    port_dict["rx"] = m.groupdict()["rx"].split()
                if m.groupdict()["tx"]:
                    port_dict["tx"] = m.groupdict()["tx"].split()
                if m.groupdict()["rx"]:
                    port_dict["rx"] = m.groupdict()["rx"].split()
                if m.groupdict()["tx"]:
                    port_dict["tx"] = m.groupdict()["tx"].split()
                continue

            m = p3.match(line)
            if m:
                ret_dict.setdefault(
                    "destination_ports", m.groupdict()["destination_ports"].split(" ")
                )
                continue

            m = p4.match(line)
            if m:
                ret_dict.setdefault(
                    "source_vlans", m.groupdict()["source_vlans"].split(" ")
                )
                continue

            m = p5.match(line)
            if m:
                ret_dict.setdefault(
                    "destination_vlans", m.groupdict()["destination_vlans"].split(" ")
                )
                continue

            m = p6.match(line)
            if m:
                ret_dict.setdefault(
                    "source_rspan_vlan", int(m.groupdict()["source_rspan_vlan"])
                )
                continue

            m = p7.match(line)
            if m:
                ret_dict.setdefault(
                    "destination_rspan_vlan",
                    int(m.groupdict()["destination_rspan_vlan"]),
                )
                continue

            m = p8.match(line)
            if m:
                ret_dict.setdefault("encap", m.groupdict()["encap"])
                continue

            m = p9.match(line)
            if m:
                ret_dict.setdefault(
                    "ingress_forwarding", m.groupdict()["ingress_forwarding"]
                )
                continue

            m = p10.match(line)
            if m:
                ret_dict.setdefault("filter_vlans", m.groupdict()["filter_vlans"])
                continue

            m = p11.match(line)
            if m:
                ret_dict.setdefault(
                    "erspan_enable", int(m.groupdict()["erspan_enable"])
                )
                continue

            m = p12.match(line)
            if m:
                ret_dict.setdefault(
                    "erspan_hw_programmed", int(m.groupdict()["erspan_hw_programmed"])
                )
                continue

            m = p13.match(line)
            if m:
                ret_dict.setdefault(
                    "erspan_mandatory_cfg", int(m.groupdict()["erspan_mandatory_cfg"])
                )
                continue

            m = p14.match(line)
            if m:
                ret_dict.setdefault("erspan_id", int(m.groupdict()["erspan_id"]))
                continue

            m = p15.match(line)
            if m:
                ret_dict.setdefault("gre_protocol", m.groupdict()["gre_protocol"])
                continue

            m = p16.match(line)
            if m:
                ret_dict.setdefault("mtu", int(m.groupdict()["mtu"]))
                continue

            m = p17.match(line)
            if m:
                ret_dict.setdefault("ip_tos", int(m.groupdict()["ip_tos"]))
                continue

            m = p18.match(line)
            if m:
                ret_dict.setdefault("ip_ttl", int(m.groupdict()["ip_ttl"]))
                continue

            m = p19.match(line)
            if m:
                ret_dict.setdefault("cos", int(m.groupdict()["cos"]))
                continue

            m = p20.match(line)
            if m:
                ret_dict.setdefault("vrf_id", int(m.groupdict()["vrf_id"]))
                continue

            m = p21.match(line)
            if m:
                ret_dict.setdefault("tunnel_if_id", int(m.groupdict()["tunnel_if_id"]))
                continue

            m = p22.match(line)
            if m:
                ret_dict.setdefault("destination_ip", m.groupdict()["destination_ip"])
                continue

            m = p23.match(line)
            if m:
                ret_dict.setdefault("org_ip", m.groupdict()["org_ip"])
                continue

            m = p24.match(line)
            if m:
                ret_dict.setdefault("sgt_count", int(m.groupdict()["sgt_count"]))
                continue

            m = p25.match(line)
            if m:
                ret_dict.setdefault("sgt_tag", m.groupdict()["sgt_tag"])
                continue

        return ret_dict


class ShowPlatformSoftwareFedSwitchActiveMonitor(ShowPlatformSoftwareFedActiveMonitor):
    """
    Parser for 'show platform software fed switch active monitor {session}'
    """

    cli_command = [
        "show platform software fed switch active monitor {session}",
        "show platform software fed switch {switch_num} monitor {session}",
    ]

    def cli(self, session, switch_num=None, output=None):
        if switch_num:
            cli_command = self.cli_command[1].format(
                switch_num=switch_num, session=session
            )
        else:
            cli_command = self.cli_command[0].format(session=session)

        if output is None:
            output = self.device.execute(cli_command)

        return super().cli(session=session, output=output)


# ============================================================================
# Schema for 'show platform software fed switch active vt hardware if-id <>'
# ============================================================================


class ShowPlatformSoftwareFedSwitchActiveVtHardwareSchema(MetaParser):
    """Schema for show platfrom software fed switch active vt hardware if-id <>"""

    schema = {
        "forward_mapping": {Optional("translated_vlan"): int, Optional("cvlan"): int},
        "reverse_mapping": {Optional("translated_vlan"): int, Optional("svlan"): int},
    }


# ============================================================================
# Parser for 'show platform software fed switch active vt hardware if-id <>'
# ============================================================================


class ShowPlatformSoftwareFedSwitchActiveVtHardware(
    ShowPlatformSoftwareFedSwitchActiveVtHardwareSchema
):
    """Parser for 'show platform software fed switch active vt hardware if-id <>"""

    cli_command = [
        "show platform software fed active vt hardware if-id {ifid}",
        "show platform software fed switch {switch_var} vt hardware if-id {ifid}",
    ]

    def cli(self, ifid, switch_var=None, output=None):
        if output is None:
            if switch_var:
                cmd = self.cli_command[1].format(ifid=ifid, switch_var=switch_var)
            else:
                cmd = self.cli_command[0].format(ifid=ifid)

            output = self.device.execute(cmd)

        # Cvlan-id      Translated vlan-id
        p1 = re.compile(r"^Cvlan\-id\s+Translated vlan\-id$")

        # Svlan-id      Translated vlan-id
        p2 = re.compile(r"^Svlan\-id\s+Translated vlan\-id$")

        # 30            20
        p3 = re.compile(r"^(?P<vlan_id>\d+)\s+(?P<translated_vlan>\d+)$")

        ret_dict = {}
        reverse_map_flag = False
        for line in output.splitlines():
            line = line.strip()

            # Cvlan-id      Translated vlan-id
            m = p1.match(line)
            if m:
                map_dict = ret_dict.setdefault("forward_mapping", {})
                continue

            # Svlan-id      Translated vlan-id
            m = p2.match(line)
            if m:
                map_dict = ret_dict.setdefault("reverse_mapping", {})
                reverse_map_flag = True
                continue

            # 30            20
            m = p3.match(line)
            if m:
                if reverse_map_flag:
                    map_dict["svlan"] = int(m.groupdict()["vlan_id"])
                else:
                    map_dict["cvlan"] = int(m.groupdict()["vlan_id"])
                map_dict["translated_vlan"] = int(m.groupdict()["translated_vlan"])
                continue

        return ret_dict


class ShowPlatformSoftwareFedSecurityFedIpsgIfIdSchema(MetaParser):
    """
    Schema for
        * show platform software fed {switch} {mode} security-fed ipsg if-id {if_id}
        * show platform software fed {mode} security-fed ipsg if-id {if_id}
    """

    schema = {Or("ip", "mac"): {Any(): {"handle": int}}}


class ShowPlatformSoftwareFedSecurityFedIpsgIfId(
    ShowPlatformSoftwareFedSecurityFedIpsgIfIdSchema
):
    """
    Parser for
        * show platform software fed {switch} {mode} security-fed ipsg if-id {if_id}
        * show platform software fed {mode} security-fed ipsg if-id {if_id}
    """

    cli_command = [
        "show platform software fed {mode} security-fed ipsg if-id {if_id}",
        "show platform software fed {switch} {mode} security-fed ipsg if-id {if_id}",
    ]

    def cli(self, mode, if_id, switch=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[1].format(switch=switch, mode=mode, if_id=if_id)
            else:
                cmd = self.cli_command[0].format(mode=mode, if_id=if_id)

            output = self.device.execute(cmd)

        # 10.1.1.1           2056770536     00:11:01:00:00:01    2047852776
        p1 = re.compile(
            r"^(?P<ip>\S+)\s+(?P<ip_handle>\d+)\s+(?P<mac>\S+)\s+(?P<mac_handle>\d+)$"
        )

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # 10.1.1.1           2056770536     00:11:01:00:00:01    2047852776
            m = p1.match(line)
            if m:
                group_dict = m.groupdict()
                ip_dict = ret_dict.setdefault("ip", {}).setdefault(group_dict["ip"], {})
                ip_dict["handle"] = int(group_dict["ip_handle"])
                mac_dict = ret_dict.setdefault("mac", {}).setdefault(
                    group_dict["mac"], {}
                )
                mac_dict["handle"] = int(group_dict["mac_handle"])
                continue

        return ret_dict


# =======================================================================================================================
# Schema for 'show platform software fed switch {switch} fnf flow-record asic {asic} start-index {index} num-flows {flow} '
# =======================================================================================================================


class ShowPlatformSoftwareFedSwitchSwitchFnfFlowRecordAsicAsicStartIndexIndexNumFlowsFlowSchema(
    MetaParser
):
    """Schema for show platform software fed switch {switch} fnf flow-record asic {asic} start-index {index} num-flows {flow}"""

    schema = {
        "num_flows": int,
        "index_num": int,
        "asic_num": int,
        "id_details": {
            Any(): {
                "id": int,
                "first_seen": str,
                "last_seen": str,
                "sys_uptime": str,
                "pkt_count": str,
                "byte_count": str,
                "lookup_details": {
                    Any(): {
                        "lookup_num": int,
                        "lookup_type": str,
                        "lookup_value": str,
                    },
                },
            },
        },
    }


# =======================================================================================================================
# Parser for 'show platform software fed switch {switch} fnf flow-record asic {asic} start-index {index} num-flows {flow} '
# =======================================================================================================================
class ShowPlatformSoftwareFedSwitchSwitchFnfFlowRecordAsicAsicStartIndexIndexNumFlowsFlow(
    ShowPlatformSoftwareFedSwitchSwitchFnfFlowRecordAsicAsicStartIndexIndexNumFlowsFlowSchema
):
    """Parser for show platform software fed switch {switch} fnf flow-record asic {asic} start-index {index} num-flows {flow}"""

    cli_command = "show platform software fed switch {switch} fnf flow-record asic {asic} start-index {index} num-flows {flow}"

    def cli(self, switch, asic, index, flow, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # 11 flows starting at 0 for asic 0:
        p1 = re.compile(
            r"^(?P<num_flows>\d+)\s+flows\s+starting\s+at\s+(?P<index_num>\d+)\s+for\s+asic\s+(?P<asic_num>\d+):$"
        )
        # FirstSeen = 0x7647c, LastSeen = 0x76a55, sysUptime = 0x76aa8
        p2 = re.compile(
            r"^FirstSeen\s+=\s+(?P<first_seen>\S+),\s+LastSeen\s+=\s+(?P<last_seen>\S+),\s+sysUptime\s+=\s+(?P<sys_uptime>\S+)$"
        )
        # PKT Count = 0x0000000003c515d5, L2ByteCount = 0x00000001e28aea80
        p2_1 = re.compile(
            r"^PKT\s+Count\s+=\s+(?P<pkt_count>\S+),\s+L2ByteCount\s+=\s+(?P<byte_count>\S+)$"
        )
        # Idx 8256 :
        p2_2 = re.compile(r"^Idx\s+(?P<id>\d+)\s+:$")
        # {231, ALR_EGRESS_NET_FLOW_ACL_LOOKUP_TYPE1 = 0x01}
        p2_3 = re.compile(
            r"^\{(?P<lookup_num>\d+),\s+(?P<lookup_type>\S+)\s+=\s+(?P<lookup_value>\S+)\}$"
        )

        ret_dict = {}

        for line in output.splitlines():
            # 11 flows starting at 0 for asic 0:
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict["num_flows"] = int(dict_val["num_flows"])
                ret_dict["index_num"] = int(dict_val["index_num"])
                ret_dict["asic_num"] = int(dict_val["asic_num"])
                continue

            # FirstSeen = 0x7647c, LastSeen = 0x76a55, sysUptime = 0x76aa8
            m = p2.match(line)
            if m:
                dict_val = m.groupdict()
                id_dict["first_seen"] = dict_val["first_seen"]
                id_dict["last_seen"] = dict_val["last_seen"]
                id_dict["sys_uptime"] = dict_val["sys_uptime"]
                continue

            # PKT Count = 0x0000000003c515d5, L2ByteCount = 0x00000001e28aea80
            m = p2_1.match(line)
            if m:
                dict_val = m.groupdict()
                id_dict["pkt_count"] = dict_val["pkt_count"]
                id_dict["byte_count"] = dict_val["byte_count"]
                continue

            # Idx 8256 :
            m = p2_2.match(line)
            if m:
                dict_val = m.groupdict()
                id_var = dict_val["id"]
                id_details = ret_dict.setdefault("id_details", {})
                id_dict = ret_dict["id_details"].setdefault(id_var, {})
                id_dict["id"] = int(dict_val["id"])
                continue

            # {231, ALR_EGRESS_NET_FLOW_ACL_LOOKUP_TYPE1 = 0x01}
            m = p2_3.match(line)
            if m:
                dict_val = m.groupdict()
                lookup_id = dict_val["lookup_num"]
                lookup = ret_dict["id_details"][id_var].setdefault("lookup_details", {})
                lookup_dict = ret_dict["id_details"][id_var][
                    "lookup_details"
                ].setdefault(lookup_id, {})
                lookup_dict["lookup_type"] = dict_val["lookup_type"]
                lookup_dict["lookup_value"] = dict_val["lookup_value"]
                lookup_dict["lookup_num"] = int(dict_val["lookup_num"])
                continue

        return ret_dict


# ======================================================
# Parser for 'show platform software fed switch active acl info db summary '
# ======================================================


class ShowPlatformSoftwareFedSwitchActiveAclInfoDbSummarySchema(MetaParser):
    """Schema for show platform software fed switch active acl info db summary"""

    schema = {
        "acl_summary": {
            Any(): {
                "acl_name": str,
                "feature": str,
                "no_of_aces": int,
                "protocol": str,
                "ingress": str,
                "egress": str,
            }
        }
    }


class ShowPlatformSoftwareFedSwitchActiveAclInfoDbSummary(
    ShowPlatformSoftwareFedSwitchActiveAclInfoDbSummarySchema
):
    """Parser for show platform software fed switch active acl info db summary"""

    cli_command = "show platform software fed switch active acl info db summary"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # CG id     ACL name                                    Feature    No of ACEs     Protocol    Ingress    Egress
        # --------------------------------------------------------------------------------------------------------------
        # 13        acl-2                                       Racl       4              IPv4        N          Y
        # 17        acl-1                                       Racl       5              IPv4        Y          N
        p1 = re.compile(
            r"^(?P<cg_id>\d+)\s+(?P<acl_name>\S+)\s+(?P<feature>\w+)\s+(?P<no_of_aces>\d+)\s+(?P<protocol>\S+)\s+(?P<ingress>\w+)\s+(?P<egress>\w+)$"
        )

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            # CG id     ACL name                                    Feature    No of ACEs     Protocol    Ingress    Egress
            # --------------------------------------------------------------------------------------------------------------
            # 13        acl-2                                       Racl       4              IPv4        N          Y
            # 17        acl-1                                       Racl       5              IPv4        Y          N
            m = p1.match(line)
            if m:
                group = m.groupdict()
                cg_id = group["cg_id"]
                int_dict = ret_dict.setdefault("acl_summary", {}).setdefault(cg_id, {})
                int_dict["acl_name"] = group["acl_name"]
                int_dict["feature"] = group["feature"]
                int_dict["no_of_aces"] = int(group["no_of_aces"])
                int_dict["protocol"] = group["protocol"]
                int_dict["ingress"] = group["ingress"]
                int_dict["egress"] = group["egress"]
                continue

        return ret_dict


# ============================================================================
#  Schema for
#  * 'show platform software fed active acl bind db detail'
# ============================================================================
class ShowPlatformSoftwareFedActiveAclBindDbDetailSchema(MetaParser):
    """Schema for 'show platform software fed active acl bind db detail'"""

    schema = {
        "interface": {
            Any(): {
                "direction": {
                    Any(): {
                        "feature": {
                            Any(): {
                                "protocol": str,
                                "cg_id": int,
                                "cg_name": str,
                                "status": str,
                                "src_og_lkup_hdl": int,
                                "dst_og_lkup_hdl": int,
                            },
                        },
                    },
                },
            },
        },
    }


# ============================================================================
#  Parser for
#  * 'show platform software fed active acl bind db detail'
# ============================================================================
class ShowPlatformSoftwareFedActiveAclBindDbDetail(
    ShowPlatformSoftwareFedActiveAclBindDbDetailSchema
):
    """
    Parser for
    * 'show platform software fed active acl bind db detail'
    """

    cli_command = [
        "show platform software fed {switch} {switch_var} acl bind db detail",
        "show platform software fed {switch_var} acl bind db detail",
    ]

    def cli(self, switch_var, switch=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(switch=switch, switch_var=switch_var)
            else:
                cmd = self.cli_command[1].format(switch_var=switch_var)
            output = self.device.execute(cmd)

        # initial return dictionary
        ret_dict = {}

        # Interface Name: Hu1/0/2
        p1 = re.compile(r"^Interface Name:\s+(?P<interface>[\w\/\.]+)$")

        # Direction: Egress
        p2 = re.compile(r"^Direction:\s+(?P<direction>[\w\_]+)$")

        # Feature         : Pbr
        p3 = re.compile(r"^Feature\s+:\s(?P<feature>[\w]+)$")

        # Protocol        : IPv4
        p4 = re.compile(r"^Protocol\s+:\s(?P<protocol>[\w]+)$")

        # CG ID           : 1
        p5 = re.compile(r"^CG ID\s+:\s(?P<cg_id>[\d]+)$")

        # CG Name         : v4_rmap2
        p6 = re.compile(r"^CG Name\s+:\s(?P<cg_name>[\w\_\-]+)$")

        # Status          : Success
        p7 = re.compile(r"^Status\s+:\s(?P<status>[\w]+)$")

        # Src_og_lkup_hdl : 0
        p8 = re.compile(r"^Src_og_lkup_hdl\s+:\s(?P<src_og_lkup_hdl>[\d]+)$")

        # Dst_og_lkup_hdl : 0
        p9 = re.compile(r"^Dst_og_lkup_hdl\s+:\s(?P<dst_og_lkup_hdl>[\d]+)$")

        for line in output.splitlines():
            line = line.strip()

            # Interface Name: Hu1/0/2
            m = p1.match(line)
            if m:
                group = m.groupdict()
                int_dict = ret_dict.setdefault("interface", {}).setdefault(
                    Common.convert_intf_name(group["interface"]), {}
                )
                continue

            # Direction: Egress
            m = p2.match(line)
            if m:
                direction = m.groupdict()["direction"]
                dir_dict = int_dict.setdefault("direction", {}).setdefault(
                    direction, {}
                )
                continue

            # Feature         : Pbr
            m = p3.match(line)
            if m:
                dict_val = m.groupdict()
                direction_dict = dir_dict.setdefault("feature", {}).setdefault(
                    dict_val["feature"], {}
                )
                continue

            # Protocol        : IPv4
            m = p4.match(line)
            if m:
                dict_val = m.groupdict()
                direction_dict["protocol"] = dict_val["protocol"]
                continue

            # CG ID           : 1
            m = p5.match(line)
            if m:
                dict_val = m.groupdict()
                direction_dict["cg_id"] = int(dict_val["cg_id"])

            # CG Name         : v4_rmap2
            m = p6.match(line)
            if m:
                dict_val = m.groupdict()
                direction_dict["cg_name"] = dict_val["cg_name"]
                continue

            # Status          : Success
            m = p7.match(line)
            if m:
                dict_val = m.groupdict()
                direction_dict["status"] = dict_val["status"]
                continue

            # Src_og_lkup_hdl : 0
            m = p8.match(line)
            if m:
                dict_val = m.groupdict()
                direction_dict["src_og_lkup_hdl"] = int(dict_val["src_og_lkup_hdl"])
                continue

            # Dst_og_lkup_hdl : 0
            m = p9.match(line)
            if m:
                dict_val = m.groupdict()
                direction_dict["dst_og_lkup_hdl"] = int(dict_val["dst_og_lkup_hdl"])
                continue

        return ret_dict


# ============================================================================
#  Schema for
#  * 'show platform software fed switch active acl info db detail'
# ============================================================================
class ShowPlatformSoftwareFedActiveAclInfoDbDetailSchema(MetaParser):
    """Schema for show platform software fed switch active acl info db detail"""

    schema = {
        "cg_name": {
            Any(): {
                "cg_id": int,
                "feature": str,
                "prot": str,
                "region": str,
                "dir": str,
                "asic": int,
                "oid": str,
                "seq": {
                    Any(): {
                        Optional("ipv4_src_value"): str,
                        Optional("ipv4_src_mask"): str,
                        Optional("ipv4_dst_value"): str,
                        Optional("ipv4_dst_mask"): str,
                        Optional("ipv6_src_value"): str,
                        Optional("ipv6_src_mask"): str,
                        Optional("ipv6_dst_value"): str,
                        Optional("ipv6_dst_mask"): str,
                        "pro": {
                            Any(): {
                                "proto": str,
                                "frag": str,
                                "tcp_flg": str,
                                "tcp_op": str,
                                "src_port": str,
                                "dst_port": str,
                            },
                        },
                        "tost": {
                            Any(): {
                                "tos": str,
                                "ttl": str,
                                "cos": str,
                                "v4_opt": str,
                                "src_obj": str,
                                "dst_obj": str,
                            },
                        },
                        "result": str,
                        "counter": str,
                    },
                },
            },
        },
    }


# ============================================================================
#  Parser for
#  * 'show platform software fed switch active acl info db detail'
# ============================================================================
class ShowPlatformSoftwareFedActiveAclInfoDbDetail(
    ShowPlatformSoftwareFedActiveAclInfoDbDetailSchema
):
    """Parser for:
    * 'show platform software fed switch active acl info db detail'
    """

    cli_command = "show platform software fed switch active acl info db detail"

    def cli(self, output=None):
        if not output:
            output = self.device.execute(self.cli_command)

        proto_flag = False
        tos_flag = False

        # [CG ID 13]    CG Name: acl-2    Feature: Racl
        p1 = re.compile(
            r"^\[CG ID+\s+(?P<cg_id>[\d]+)\]+\s+CG+\s+Name:+\s(?P<cg_name>[\w\-]+)+\s+Feature:+\s(?P<feature>[\w]+)$"
        )

        # [CG ID 13]    Prot: IPv4
        p2 = re.compile(r"^\[CG ID+\s+(?P<cg_id>[\d]+)\]+\s+Prot:+\s(?P<prot>[\w]+)$")

        # [CG ID 13]    Region grp: 0xdc09b2a8
        p3 = re.compile(
            r"^\[CG ID+\s+(?P<cg_id>[\d]+)\]+\s+Region+\s+grp:+\s(?P<region>[\w\-]+)$"
        )

        # [CG ID 13]    Dir: Egress    SDK-handle(asic: 0, OID: 0x0000)
        p4 = re.compile(
            r"^\[CG ID+\s+(?P<cg_id>[\S\s]+)\]+\s+Dir:+\s(?P<dir>[\w]+)+\s+SDK-handle+\(asic:+\s+(?P<asic>[\d]+),\s+OID:+\s+(?P<oid>[\w\s]+)\)$"
        )

        # Seq Num:10
        p5 = re.compile(r"^Seq Num:+(?P<seq>[\d\w]+)$")

        # ipv4_src: value = 0x00000000       mask = 0x00000000
        p6 = re.compile(
            r"^ipv4_src:\s+value+\s=\s+(?P<ipv4_src_value>[\d\w]+)+\s+mask+\s=\s+(?P<ipv4_src_mask>[\d\w]+)$"
        )

        # ipv4_dst: value = 0x00000000       mask = 0x00000000
        p7 = re.compile(
            r"^ipv4_dst:\s+value+\s=\s+(?P<ipv4_dst_value>[\d\w]+)+\s+mask+\s=\s+(?P<ipv4_dst_mask>[\d\w]+)$"
        )

        # ipv6_src: value = 0x00001100.0x01000000.0x00000000.0x30000000
        p7_1 = re.compile(r"^ipv6_src:\s+value+\s=\s+(?P<ipv6_src_value>[\S]+)$")

        # ipv6_dst: value = 0x00001100.0x00000000.0x00000000.0x3000000
        p7_2 = re.compile(r"^ipv6_dst:\s+value+\s=\s+(?P<ipv6_dst_value>[\S]+)$")

        # mask = 0xffffffff.0xffffffff.0xffffffff.0xffffffff
        p7_3 = re.compile(r"^mask+\s=\s+(?P<ipv6_mask>[\S]+)$")

        # proto    frag    tcp_flg    tcp_op    src_port    dst_port
        p8_0 = re.compile(
            r"^proto+\s+frag+\s+tcp_flg+\s+tcp_op+\s+src_port+\s+dst_port$"
        )

        #  tos      ttl       cos      v4_opt    src_obj     dst_obj
        p8_1 = re.compile(
            r"^tos+\s+ttl+\s+cos+\s+[v4_opt|ext_hdr]+\s+src_obj+\s+dst_obj$"
        )

        # V:  0x1       0x0      0x0         0x0        0x0          0x0
        # M:  0xff       0x0      0x0         0x0        0x0          0x0
        p8 = re.compile(
            r"^(?P<pro_type>[\w\_]+)+:\s+(?P<proto>[\w]+)+\s+(?P<frag>[\w]+)+\s+(?P<tcp_flg>[\w]+)+\s+(?P<tcp_op>[\w]+)+\s+(?P<src_port>[\w]+)+\s+(?P<dst_port>[\w]+)$"
        )
        # V:  0x0       0x0      0x0         0x0        0x0          0x0
        # M:  0x0       0x0      0x0         0x0        0x0          0x0
        p9 = re.compile(
            r"^(?P<tos_type>[\w\_]+)+:\s+(?P<tos>[\w]+)+\s+(?P<ttl>[\w]+)+\s+(?P<cos>[\w]+)+\s+(?P<v4_opt>[\w]+)+\s+(?P<src_obj>[\w]+)+\s+(?P<dst_obj>[\w]+)$"
        )

        # Result  deny:0x1    Counter handle: 0x72c
        p10 = re.compile(
            r"^Result+\s+deny:+(?P<result>[\d\w]+)+\s+Counter handle:+(?P<counter>[\d\w\s]+)$"
        )

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # [CG ID 13]    CG Name: acl-2    Feature: Racl
            m = p1.match(line)
            if m:
                group = m.groupdict()
                int_dict = ret_dict.setdefault("cg_name", {}).setdefault(
                    (group["cg_name"]), {}
                )
                int_dict["feature"] = group["feature"]
                int_dict["cg_id"] = int(group["cg_id"])
                continue

            # [CG ID 13]    Prot: IPv4
            m = p2.match(line)
            if m:
                group = m.groupdict()
                int_dict["prot"] = group["prot"]
                continue

            # [CG ID 13]    Region grp: 0xdc09b2a8
            m = p3.match(line)
            if m:
                group = m.groupdict()
                int_dict["region"] = group["region"]
                continue

            # [CG ID 13]    Dir: Egress    SDK-handle(asic: 0, OID: 0x0000)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                int_dict["dir"] = group["dir"]
                int_dict["asic"] = int(group["asic"])
                int_dict["oid"] = group["oid"]
                continue

            # Seq Num:10
            m = p5.match(line)
            if m:
                group = m.groupdict()
                seq_dict = int_dict.setdefault("seq", {}).setdefault((group["seq"]), {})
                continue

            # ipv4_src: value = 0x00000000       mask = 0x00000000
            m = p6.match(line)
            if m:
                group = m.groupdict()
                seq_dict["ipv4_src_value"] = group["ipv4_src_value"]
                seq_dict["ipv4_src_mask"] = group["ipv4_src_mask"]
                continue

            # ipv4_dst: value = 0x00000000       mask = 0x00000000
            m = p7.match(line)
            if m:
                group = m.groupdict()
                seq_dict["ipv4_dst_value"] = group["ipv4_dst_value"]
                seq_dict["ipv4_dst_mask"] = group["ipv4_dst_mask"]
                continue

            # ipv6_src: value = 0x00001100.0x01000000.0x00000000.0x30000000
            m = p7_1.match(line)
            if m:
                group = m.groupdict()
                seq_dict["ipv6_src_value"] = group["ipv6_src_value"]
                ipv6src_flag = 1
                continue

            # ipv6_dst: value = 0x00001100.0x00000000.0x00000000.0x3000000
            m = p7_2.match(line)
            if m:
                group = m.groupdict()
                seq_dict["ipv6_dst_value"] = group["ipv6_dst_value"]
                ipv6dst_flag = 1
                continue

            # mask = 0xffffffff.0xffffffff.0xffffffff.0xffffffff
            m = p7_3.match(line)
            if m:
                group = m.groupdict()
                if ipv6src_flag == 1:
                    seq_dict["ipv6_src_mask"] = group["ipv6_mask"]
                    ipv6src_flag = 0
                    continue
                elif ipv6dst_flag == 1:
                    seq_dict["ipv6_dst_mask"] = group["ipv6_mask"]
                    ipv6dst_flag = 0
                    continue

            # proto    frag    tcp_flg    tcp_op    src_port    dst_port
            m = p8_0.match(line)
            if m:
                group = m.groupdict()
                proto_dict = seq_dict.setdefault("pro", {})
                proto_flag = True
                tos_flag = False
                continue

            # tos      ttl       cos      v4_opt    src_obj     dst_obj
            m = p8_1.match(line)
            if m:
                group = m.groupdict()
                tos_dict = seq_dict.setdefault("tost", {})
                tos_flag = True
                proto_flag = False
                continue

            # V:  0x1       0x0      0x0         0x0        0x0          0x0
            # M:  0xff       0x0      0x0         0x0        0x0          0x0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                if proto_flag == True and tos_flag == False:
                    proto_type_dict = proto_dict.setdefault((group["pro_type"]), {})
                    proto_type_dict["proto"] = group["proto"]
                    proto_type_dict["frag"] = group["frag"]
                    proto_type_dict["tcp_flg"] = group["tcp_flg"]
                    proto_type_dict["tcp_op"] = group["tcp_op"]
                    proto_type_dict["src_port"] = group["src_port"]
                    proto_type_dict["dst_port"] = group["dst_port"]
                    continue

            # V:  0x0       0x0      0x0         0x0        0x0          0x0
            # M:  0x0       0x0      0x0         0x0        0x0          0x0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                if tos_flag == True and proto_flag == False:
                    tos_type_dict = tos_dict.setdefault((group["tos_type"]), {})
                    tos_type_dict["tos"] = group["tos"]
                    tos_type_dict["ttl"] = group["ttl"]
                    tos_type_dict["cos"] = group["cos"]
                    tos_type_dict["v4_opt"] = group["v4_opt"]
                    tos_type_dict["src_obj"] = group["src_obj"]
                    tos_type_dict["dst_obj"] = group["dst_obj"]
                    continue

            # Result  deny:0x1    Counter handle: 0x72c
            m = p10.match(line)
            if m:
                group = m.groupdict()
                seq_dict["result"] = group["result"]
                seq_dict["counter"] = group["counter"]

        return ret_dict


# ============================================================================
#  Schema for
#  * 'show platform software fed switch active acl bind db summary'
#  * 'show platform software fed switch active acl bind db feature racl summary'
# ============================================================================
class ShowPlatformSoftwareFedActiveAclBindDbSummarySchema(MetaParser):
    """Schema for  'show platform software fed switch active acl bind db summary'
    'show platform software fed switch active acl bind db feature racl summary'
    """

    schema = {
        "interface": {
            Any(): {
                "feature": {
                    Any(): {
                        "protocol": str,
                        "status": str,
                        "cg_id": int,
                        "direction": str,
                    }
                }
            },
        },
    }


# ============================================================================
#  Parser for
#  * 'show platform software fed switch active acl bind db summary'
#  * 'show platform software fed switch active acl bind db feature racl summary'
# ============================================================================
class ShowPlatformSoftwareFedActiveAclBindDbSummary(
    ShowPlatformSoftwareFedActiveAclBindDbSummarySchema
):
    """
    Parser for
    * 'show platform software fed switch active acl bind db summary'
    * 'show platform software fed switch active acl bind db feature racl summary'
    """

    cli_command = [
        "show platform software fed {switch} {switch_var} acl bind db summary",
        "show platform software fed {switch_var} acl bind db summary",
        "show platform software fed {switch_var} acl bind db feature {feature_name} summary",
        "show platform software fed {switch} {switch_var} acl bind db feature {feature_name} summary",
    ]

    def cli(self, switch_var, switch=None, feature_name=None, output=None):
        if output is None:
            if switch and feature_name is None:
                cmd = self.cli_command[0].format(switch=switch, switch_var=switch_var)
            elif switch and feature_name:
                cmd = self.cli_command[3].format(
                    switch=switch, switch_var=switch_var, feature_name=feature_name
                )
            elif switch is None and feature_name is None:
                cmd = self.cli_command[1].format(switch_var=switch_var)
            elif switch is None and feature_name:
                cmd = self.cli_command[2].format(
                    switch_var=switch_var, feature_name=feature_name
                )

            output = self.device.execute(cmd)

        # initial return dictionary
        ret_dict = {}

        # Gi1/0/26.11  Racl          IPv4          Egress      13           Success
        # Gi1/0/25    Racl          IPv4          Ingress     17           Success
        # Gi1/0/26.11  Racl          IPv4          Egress      13           Success
        # Gi1/0/25    Racl          IPv4          Ingress     17           Success
        p1 = re.compile(
            r"^(?P<interface>[\w\-\.\/]+)\s+(?P<feature>\w+)\s+(?P<protocol>\w+)?\s+(?P<direction>\w+)\s+(?P<cg_id>\d+)\s+(?P<status>\w+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # Gi1/0/26.11  Racl          IPv4          Egress      13           Success
            # Gi1/0/25    Racl          IPv4          Ingress     17           Success
            # Gi1/0/26.11  Racl          IPv4          Egress      13           Success
            # Gi1/0/25    Racl          IPv4          Ingress     17           Success
            m = p1.match(line)
            if m:
                group = m.groupdict()
                int_dict = ret_dict.setdefault("interface", {}).setdefault(
                    Common.convert_intf_name(group["interface"]), {}
                )
                feature_dict = int_dict.setdefault("feature", {}).setdefault(
                    group["feature"], {}
                )
                feature_dict["cg_id"] = int(group["cg_id"])
                feature_dict["protocol"] = group["protocol"]
                feature_dict["direction"] = group["direction"]
                feature_dict["status"] = group["status"]
                continue

        return ret_dict


# ======================================================
# Parser for 'show platform software fed switch active learning stats '
# ======================================================


class ShowPlatformSoftwareFedSwitchActiveLearningStatsSchema(MetaParser):
    """
    Schema for
        * 'show platform software fed switch active learning stats'
    """

    schema = {
        "learning_cache": int,
        "iosd_notification": int,
        "iosd_cache": int,
        "l2_validation": int,
        "l2_matm": int,
        "l2_learning": int,
        "l3_validation": int,
        "l3_process": int,
        "l3_learning": int,
    }


class ShowPlatformSoftwareFedSwitchActiveLearningStats(
    ShowPlatformSoftwareFedSwitchActiveLearningStatsSchema
):
    """Parser for show platform software fed switch active learning stats"""

    cli_command = [
        "show platform software fed switch active learning stats",
        "show platform software fed {rp} learning stats",
    ]

    def cli(self, rp=None, output=None):
        if output is None:
            if rp:
                cmd = self.cli_command[1].format(rp=rp)
            else:
                cmd = self.cli_command[0]

            # Execute the command
            output = self.device.execute(cmd)

        # Learning cache parameter error: 0
        p1 = re.compile(
            r"^Learning\s+cache\s+parameter\s+error:\s+(?P<learning_cache>\d+)$"
        )

        # IOSd notification message count: 169042
        p2 = re.compile(
            r"^IOSd\s+notification\s+message\s+count:\s+(?P<IOSd_notification>\d+)$"
        )

        # IOSd notification cache count: 173791
        p3 = re.compile(r"^IOSd\s+notification\s+cache\s+count:\s+(?P<IOSd_cache>\d+)$")

        # L2 validation error: 2
        p4 = re.compile(r"^L2\s+validation\s+error:\s+(?P<L2_validation>\d+)$")

        # L2 matm add error: 0
        p5 = re.compile(r"^L2\s+matm\s+add\s+error:\s+(?P<L2_matm>\d+)$")

        # L2 learning cache: 173791
        p6 = re.compile(r"^L2\s+learning\s+cache:\s+(?P<L2_learning>\d+)$")

        # L3 validation error: 0
        p7 = re.compile(r"^L3\s+validation\s+error:\s+(?P<L3_validation>\d+)$")

        # L3 process error: 0
        p8 = re.compile(r"^L3\s+process\s+error:\s+(?P<L3_process>\d+)$")

        # L3 learning cache: 0
        p9 = re.compile(r"^L3\s+learning\s+cache:\s+(?P<L3_learning>\d+)$")

        ret_dict = {}

        for line in output.splitlines():
            # Learning cache parameter error: 0
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict["learning_cache"] = int(dict_val["learning_cache"])
                continue

            # IOSd notification message count: 169042
            m = p2.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict["iosd_notification"] = int(dict_val["IOSd_notification"])
                continue

            # IOSd notification cache count: 173791
            m = p3.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict["iosd_cache"] = int(dict_val["IOSd_cache"])
                continue

            # L2 validation error: 2
            m = p4.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict["l2_validation"] = int(dict_val["L2_validation"])
                continue

            # L2 matm add error: 0
            m = p5.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict["l2_matm"] = int(dict_val["L2_matm"])
                continue

            # L2 learning cache: 173791
            m = p6.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict["l2_learning"] = int(dict_val["L2_learning"])
                continue

            # L3 validation error: 0
            m = p7.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict["l3_validation"] = int(dict_val["L3_validation"])
                continue

            # L3 process error: 0
            m = p8.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict["l3_process"] = int(dict_val["L3_process"])
                continue

            # L3 learning cache: 0
            m = p9.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict["l3_learning"] = int(dict_val["L3_learning"])
                continue

        return ret_dict


# =================================================================
# Schema for 'show platform software fed switch active stp-vlan 1 '
# =================================================================


class ShowPlatformSoftwareFedSwitchActiveStpVlanSchema(MetaParser):
    """Schema for show platform software fed switch active stp-vlan {vlan_id}"""

    schema = {
        "hw_flood_list": list,
        "interface": {
            Any(): {
                "pvlan_mode": str,
                "stp_state": str,
                "vtp_pruned": str,
                "untagged": str,
                "ingress": str,
                "egress": str,
            }
        },
    }


# =================================================================
# Parser for 'show platform software fed switch active stp-vlan {vlan_id}'
# =================================================================


class ShowPlatformSoftwareFedSwitchActiveStpVlan(
    ShowPlatformSoftwareFedSwitchActiveStpVlanSchema
):
    """Parser for show platform software fed switch active stp-vlan {vlan_id}"""

    cli_command = [
        "show platform software fed switch {switch_num} stp-vlan {vlan_id}",
        "show platform software fed active stp-vlan {vlan_id}",
    ]

    def cli(self, vlan_id="", switch_num=None, output=None):
        if output is None:
            self.cli_command = (
                self.cli_command[0].format(switch_num=switch_num, vlan_id=vlan_id)
                if switch_num
                else self.cli_command[1].format(vlan_id=vlan_id)
            )
            output = self.device.execute(self.cli_command)

        #                    Interface   pvlan_mode   stp_state  vtp pruned          Untagged          Ingress           Egress
        p1 = re.compile(
            r"^(?P<interface>\S+) +(?P<pvlan_mode>\S+) +(?P<stp_state>\S+) +(?P<vtp_pruned>\S+) +(?P<untagged>\w+) +(?P<ingress>\w+) +(?P<egress>\w+)$"
        )

        # HW flood list: : Gi2/0/23, Gi2/0/10, Gi2/0/12, Gi2/0/14, Gi2/0/16, Ap2/0/1
        p2 = re.compile(r"^HW flood list\:\s+:(?P<hw_flood_list>[\w\s\,/\.]*)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # TenGigabitEthernet2/0/23         none    disabled          No               Yes         blocking         blocking
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                key_chain_dict = ret_dict.setdefault("interface", {}).setdefault(
                    Common.convert_intf_name(dict_val["interface"]), {}
                )
                key_chain_dict["pvlan_mode"] = dict_val["pvlan_mode"]
                key_chain_dict["stp_state"] = dict_val["stp_state"]
                key_chain_dict["vtp_pruned"] = dict_val["vtp_pruned"]
                key_chain_dict["untagged"] = dict_val["untagged"]
                key_chain_dict["ingress"] = dict_val["ingress"]
                key_chain_dict["egress"] = dict_val["egress"]
                continue

            # HW flood list: : Gi2/0/23, Gi2/0/10, Gi2/0/12, Gi2/0/14, Gi2/0/16, Ap2/0/1
            m = p2.match(line)
            if m:
                ret_dict["hw_flood_list"] = (
                    m.groupdict()["hw_flood_list"].replace(" ", "").split(",")
                    if len(m.groupdict()["hw_flood_list"]) > 0
                    else []
                )
                continue

        return ret_dict


# =================================================================
# Schema for 'show platform software fed switch active acl og-pcl '
# =================================================================


class ShowPlatformSoftwareFedSwitchActiveAclOgPclSchema(MetaParser):
    """Schema for show platform software fed switch active acl og-pcl"""

    schema = {
        Any(): {
            "lkup_id": str,
            "num_orgs": int,
            "ref_cnt": int,
            "bits_used": int,
            "prefixes": int,
            "in_HW": str,
        }
    }


# =================================================================
# Parser for 'show platform software fed switch active acl og-pcl '
# =================================================================


class ShowPlatformSoftwareFedSwitchActiveAclOgPcl(
    ShowPlatformSoftwareFedSwitchActiveAclOgPclSchema
):
    """Parser for show platform software fed switch active acl og-pcl"""

    cli_command = "show platform software fed switch active acl og-pcl"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # lkup-id   proto     num-ogs     ref-cnt    bits-used    prefixes  in HW
        # 0x3d      IPv4           1           2           1           4    Y
        p1 = re.compile(
            r"^(?P<lkup_id>\S+)\s+(?P<proto>\w+)\s+(?P<num_orgs>\d+)\s+(?P<ref_cnt>\d+)\s+(?P<bits_used>\d+)\s+(?P<prefixes>\d+)\s+(?P<in_HW>\S)$"
        )

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # 0x3d IPv4 1 2 1 4 Y
            m = p1.match(line)
            if m:
                group = m.groupdict()
                proto = group["proto"]
                int_dict = ret_dict.setdefault(proto, {})
                int_dict["lkup_id"] = group["lkup_id"]
                int_dict["num_orgs"] = int(group["num_orgs"])
                int_dict["ref_cnt"] = int(group["ref_cnt"])
                int_dict["bits_used"] = int(group["bits_used"])
                int_dict["prefixes"] = int(group["prefixes"])
                int_dict["in_HW"] = group["in_HW"]

                continue

        return ret_dict


# =============================================================
# Parser for 'show platform software fed switch active acl statistics events'
# =============================================================


class ShowPlatformSoftwareFedSwitchActiveAclStatisticsEventsSchema(MetaParser):
    schema = {
        "acl_statistics": {
            "acl_binds": int,
            "acl_bind_errors": int,
            "acl_unbinds": int,
            "acl_unbind_errors": int,
            "acl_rebinds": int,
            "acl_rebind_errors": int,
            "acl_edits": int,
            "acl_edit_errors": int,
            "og_creates": int,
            "og_create_errors": int,
            "og_deletes": int,
            "og_delete_errors": int,
            "og_edits": int,
            "og_edit_errors": int,
            "ipv4_ingress_acl_deny": int,
            "ipv4_egress_acl_deny": int,
            "ipv4_acl_implicit_deny": int,
            "ipv6_ingress_acl_deny": int,
            "ipv6_egress_acl_deny": int,
            "ipv6_acl_implicit_deny": int,
            Optional("mac_ingress_acl_deny"): int,
            Optional("mac_egress_acl_deny"): int,
            Optional("mac_acl_implicit_deny"): int,
        }
    }


class ShowPlatformSoftwareFedSwitchActiveAclStatisticsEvents(
    ShowPlatformSoftwareFedSwitchActiveAclStatisticsEventsSchema
):
    cli_command = "show platform software fed switch active acl statistics events"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # ACL Binds:                           13
        # ACL Bind Errors:                     1
        # ACL Unbinds:                         11
        # ACL Unbind Errors:                   0
        # ACL Rebinds:                         2
        # ACL Rebind Errors:                   0
        # ACL Edits:                           29
        # ACL Edit Errors:                     1
        # OG Creates:                          4
        # OG Create Errors:                    0
        # OG Deletes:                          4
        # OG Delete Errors:                    0
        # OG Edits:                            0
        # OG Edit Errors:                      0
        # IPv4 Ingress ACL Deny:               0
        # IPv4 Egress ACL Deny:                0
        # IPv4 ACL Implicit Deny:              0
        # IPv6 Ingress ACL Deny:               0
        # IPv6 Egress ACL Deny:                0
        # IPv6 ACL Implicit Deny:              0
        # Mac Ingress ACL Deny:                0
        # Mac Egress ACL Deny:                 0
        # Mac ACL Implicit Deny:               0
        p1 = re.compile(r"^(?P<stat_name>[\s\w]+):\s+(?P<stat_value>[\w]+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # ACL Binds:                           13
            # ACL Bind Errors:                     1
            # ACL Unbinds:                         11
            # ACL Unbind Errors:                   0
            # ACL Rebinds:                         2
            # ACL Rebind Errors:                   0
            # ACL Edits:                           29
            # ACL Edit Errors:                     1
            # OG Creates:                          4
            # OG Create Errors:                    0
            # OG Deletes:                          4
            # OG Delete Errors:                    0
            # OG Edits:                            0
            # OG Edit Errors:                      0
            # IPv4 Ingress ACL Deny:               0
            # IPv4 Egress ACL Deny:                0
            # IPv4 ACL Implicit Deny:              0
            # IPv6 Ingress ACL Deny:               0
            # IPv6 Egress ACL Deny:                0
            # IPv6 ACL Implicit Deny:              0
            # Mac Ingress ACL Deny:                0
            # Mac Egress ACL Deny:                 0
            # Mac ACL Implicit Deny:               0

            m = p1.match(line)
            if m:
                group = m.groupdict()
                int_dict = ret_dict.setdefault("acl_statistics", {})
                scrubbed = (group["stat_name"].strip()).replace(" ", "_")
                int_dict[scrubbed.lower()] = int(group["stat_value"])
                continue

        return ret_dict


# =======================================================================
# Schema for 'sh platform software fed switch active ifm interfaces svi'
# =======================================================================


class ShowPlatformSoftwareFedSwitchActiveIFMInterfacesSVISchema(MetaParser):
    """Schema for sh platform software fed switch active ifm interfaces svi"""

    schema = {"interface_name": {Any(): {"if_id": str, "state": str}}}


# ========================================================================
# Parser for 'sh platform software fed switch active ifm interfaces svi'
# ========================================================================
class ShowPlatformSoftwareFedSwitchActiveIFMInterfacesSVI(
    ShowPlatformSoftwareFedSwitchActiveIFMInterfacesSVISchema
):
    """Parser for sh platform software fed {switch} {active} ifm interfaces svi"""

    cli_command = [
        "show platform software fed {switch} {mode} ifm interfaces svi",
        "show platform software fed {mode} ifm interfaces svi",
    ]

    def cli(self, mode, switch=None, timeout=600, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(switch=switch, mode=mode)
            else:
                cmd = self.cli_command[1].format(mode=mode)

            output = self.device.execute(cmd, timeout=timeout)

        # Vlan1                             0x00000409          Ready
        p1 = re.compile(r"^(?P<interface_name>\S+)\s+(?P<if_id>\S+)\s+(?P<state>\S+)$")

        ret_dict = {}
        dict_value = {}

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            # Vlan1                             0x00000409          Ready
            if m:
                group = m.groupdict()
                interface_name = group["interface_name"]
                dict_value = ret_dict.setdefault("interface_name", {}).setdefault(
                    interface_name, {}
                )
                dict_value["if_id"] = str(group["if_id"])
                dict_value["state"] = str(group["state"])
                continue

        return ret_dict


# =============================================================================
# Schema for 'sh platform software fed switch active ifm mappings etherchannel'
# =============================================================================


class ShowPlatformSoftwareFedSwitchActiveIFMMappingsEtherchannelSchema(MetaParser):
    """Schema for sh platform software fed {switch} {active} ifm mappings etherchannel"""

    schema = {"interface_name": {Any(): {"channel_num": int, "if_id": str}}}


# =============================================================================
# Parser for 'sh platform software fed switch active ifm mappings etherchannel'
# =============================================================================
class ShowPlatformSoftwareFedSwitchActiveIFMMappingsEtherchannel(
    ShowPlatformSoftwareFedSwitchActiveIFMMappingsEtherchannelSchema
):
    """Parser for sh platform software fed {switch} {active} ifm mappings etherchannel"""

    cli_command = [
        "show platform software fed {switch} {mode} ifm mappings etherchannel",
        "show platform software fed {mode} ifm mappings etherchannel",
    ]

    def cli(self, mode, switch=None, timeout=600, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(switch=switch, mode=mode)
            else:
                cmd = self.cli_command[1].format(mode=mode)

            output = self.device.execute(cmd, timeout=timeout)

        # 241   Port-channel241                   0x00000038
        p1 = re.compile(
            r"^(?P<channel_num>\d+)\s+(?P<interface_name>\S+)\s+(?P<if_id>\S+)$"
        )

        ret_dict = {}
        dict_value = {}

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            # 241   Port-channel241                   0x00000038
            if m:
                group = m.groupdict()
                interface_name = group["interface_name"]
                dict_value = ret_dict.setdefault("interface_name", {}).setdefault(
                    interface_name, {}
                )
                dict_value["channel_num"] = int(group["channel_num"])
                dict_value["if_id"] = str(group["if_id"])
                continue

        return ret_dict


class ShowPlatformSoftwareFedSwitchActiveNatInterfacesSchema(MetaParser):
    """
    Schema for show platform software fed switch active nat interfaces
    """

    schema = {
        "index": {
            Any(): {
                "interface_name": str,
                "interface_id": str,
                "domain": str,
            },
        },
        "number_of_interfaces": int,
    }


class ShowPlatformSoftwareFedSwitchActiveNatInterfaces(
    ShowPlatformSoftwareFedSwitchActiveNatInterfacesSchema
):
    """
    show platform software fed switch active nat interfaces
    """

    cli_command = [
        "show platform software fed {switch} {mode} nat interfaces",
        "show platform software fed active nat interfaces",
    ]

    def cli(self, switch="", mode="", output=None):
        if output is None:
            if switch and mode:
                cmd = self.cli_command[0].format(switch=switch, mode=mode)
            else:
                cmd = self.cli_command[1]
            output = self.device.execute(cmd)

        ret_dict = {}
        index = 1

        #                 Interface Name |         Interface ID |  Domain |
        # ------------------------------------------------------------------
        #          GigabitEthernet1/0/23 |                0x44e | outside |
        #                         Vlan11 |                0x450 |  inside |
        p0 = re.compile(
            r"^(?P<interface_name>\S+)\s+\|+\s+(?P<interface_id>\w+)\s+\|+\s+(?P<domain>\S+)\s+\|$"
        )

        # Number of Interfaces : 2
        p1 = re.compile(r"^Number of Interfaces +: +(?P<number_of_interfaces>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            #                 Interface Name |         Interface ID |  Domain |
            # ------------------------------------------------------------------
            #          GigabitEthernet1/0/23 |                0x44e | outside |
            #                         Vlan11 |                0x450 |  inside |
            m = p0.match(line)
            if m:
                group = m.groupdict()
                index_dict = ret_dict.setdefault("index", {}).setdefault(index, {})
                index_dict["interface_name"] = group["interface_name"]
                index_dict["interface_id"] = group["interface_id"]
                index_dict["domain"] = group["domain"]
                index += 1
                continue

            # Number of Interfaces : 2
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict["number_of_interfaces"] = int(group["number_of_interfaces"])
                continue

        return ret_dict


class ShowPlatformSoftwareFedSwitchActiveNatRulesSchema(MetaParser):
    """
    Schema for show platform software fed switch active nat rules
    """

    schema = {
        "rules": {
            Optional(Or("static", "dynamic")): {
                Optional("index"): {
                    int: {
                        Optional("rule_id"): str,
                        Optional("type"): str,
                        Optional("domain"): str,
                        Optional("vrf"): int,
                        Optional("protocol"): str,
                        Optional("local_ip"): str,
                        Optional("local_port"): int,
                        Optional("global_ip"): str,
                        Optional("global_port"): int,
                        Optional("network"): int,
                        Optional("acl"): str,
                        Optional("pool_interface_ip"): str,
                        Optional("overload"): str,
                    },
                },
                "number_of_rules": int,
            },
        },
    }


class ShowPlatformSoftwareFedSwitchActiveNatRules(
    ShowPlatformSoftwareFedSwitchActiveNatRulesSchema
):
    """
    show platform software fed switch active nat rules
    """

    cli_command = [
        "show platform software fed {switch} {mode} nat rules",
        "show platform software fed active nat rules",
    ]

    def cli(self, switch="", mode="", output=None):
        if output is None:
            if switch and mode:
                cmd = self.cli_command[0].format(switch=switch, mode=mode)
            else:
                cmd = self.cli_command[1]
            output = self.device.execute(cmd)

        ret_dict = {}
        index = 1

        # STATIC Rules:
        p0 = re.compile(r"^STATIC Rules:$")

        # Rule ID | Type |  Domain |   VRF | Protocol |        Local IP |  Port |       Global IP |  Port | Network |
        # ---------------------------------------------------------------------------------------------------------------
        # 0xc     |  1-1 |  inside |     0 |      any |        15.0.0.1 |     0 |       135.0.0.1 |     0 |      32 |

        p1 = re.compile(
            r"^(?P<rule_id>\S+)\s+\|+\s+(?P<type>\d+-\d+|\s|\w+\/\w+)\s+\|+\s+(?P<domain>\w+)\s+\|+\s+(?P<vrf>\d+)\s+\|+\s+(?P<protocol>\S+)\s+\|+\s+(?P<local_ip>\S+)\s+\|+\s+(?P<local_port>\d+)\s+\|+\s+(?P<global_ip>\S+)\s+\|+\s+(?P<global_port>\d+)\s+\|+\s+(?P<network>\d+)\s+\|$"
        )

        # DYNAMIC Rules:
        p2 = re.compile(r"^DYNAMIC Rules:$")

        # Rule ID    |    Type |   VRF |                  Acl |    Pool/Interface_IP | Overload |
        # ----------------------------------------------------------------------------------------
        # 0x80000001 |  Inside |     0 |                    1 |            pool_in_1 |       No |
        p3 = re.compile(
            r"^(?P<rule_id>\S+)\s+\|+\s+(?P<type>\w+)\s+\|+\s+(?P<vrf>\d+)\s+\|+\s+(?P<acl>\S+)\s+\|+\s+(?P<pool_interface_ip>\S+)\s+\|+\s+(?P<overload>\S+)\s+\|$"
        )

        # Number of Rules : 2
        p4 = re.compile(r"^Number of Rules +: +(?P<number_of_rules>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            # STATIC Rules:
            m = p0.match(line)
            if m:
                group = m.groupdict()
                rules = ret_dict.setdefault("rules", {})
                rule_dict = rules.setdefault("static", {})

            # Rule ID | Type |  Domain |   VRF | Protocol |        Local IP |  Port |       Global IP |  Port | Network |
            # ---------------------------------------------------------------------------------------------------------------
            # 0xc     |  1-1 |  inside |     0 |      any |        15.0.0.1 |     0 |       135.0.0.1 |     0 |      32 |

            m = p1.match(line)
            if m:
                group = m.groupdict()
                index_dict = rule_dict.setdefault("index", {}).setdefault(index, {})
                index_dict["rule_id"] = group["rule_id"]
                index_dict["type"] = group["type"]
                index_dict["domain"] = group["domain"]
                index_dict["vrf"] = int(group["vrf"])
                index_dict["protocol"] = group["protocol"]
                index_dict["local_ip"] = group["local_ip"]
                index_dict["local_port"] = int(group["local_port"])
                index_dict["global_ip"] = group["global_ip"]
                index_dict["global_port"] = int(group["global_port"])
                index_dict["network"] = int(group["network"])
                index += 1

            # DYNAMIC Rules:
            m = p2.match(line)
            if m:
                group = m.groupdict()
                rules = ret_dict.setdefault("rules", {})
                rule_dict = rules.setdefault("dynamic", {})

            # Rule ID    |    Type |   VRF |                  Acl |    Pool/Interface_IP | Overload |
            # ----------------------------------------------------------------------------------------
            # 0x80000001 |  Inside |     0 |                    1 |            pool_in_1 |       No |
            m = p3.match(line)
            if m:
                group = m.groupdict()
                index_dict = rule_dict.setdefault("index", {}).setdefault(index, {})
                index_dict["rule_id"] = group["rule_id"]
                index_dict["type"] = group["type"]
                index_dict["vrf"] = int(group["vrf"])
                index_dict["acl"] = group["acl"]
                index_dict["pool_interface_ip"] = group["pool_interface_ip"]
                index_dict["overload"] = group["overload"]
                index += 1

            # Number of Rules : 2
            m = p4.match(line)
            if m:
                group = m.groupdict()
                rule_dict["number_of_rules"] = int(group["number_of_rules"])
                continue

        return ret_dict


class ShowPlatformSoftwareFedSwitchActiveNatRulesSchema(MetaParser):
    """
    Schema for show platform software fed switch active nat rules
    """

    schema = {
        "rules": {
            Optional(Or("static", "dynamic")): {
                Optional("index"): {
                    int: {
                        Optional("rule_id"): str,
                        Optional("type"): str,
                        Optional("domain"): str,
                        Optional("vrf"): int,
                        Optional("protocol"): str,
                        Optional("local_ip"): str,
                        Optional("local_port"): int,
                        Optional("global_ip"): str,
                        Optional("global_port"): int,
                        Optional("network"): int,
                        Optional("acl"): str,
                        Optional("pool_interface_ip"): str,
                        Optional("overload"): str,
                    },
                },
                "number_of_rules": int,
            },
        },
    }


class ShowPlatformSoftwareFedSwitchActiveNatRules(
    ShowPlatformSoftwareFedSwitchActiveNatRulesSchema
):
    """
    show platform software fed switch active nat rules
    """

    cli_command = [
        "show platform software fed {switch} {mode} nat rules",
        "show platform software fed active nat rules",
    ]

    def cli(self, switch="", mode="", output=None):
        if output is None:
            if switch and mode:
                cmd = self.cli_command[0].format(switch=switch, mode=mode)
            else:
                cmd = self.cli_command[1]
            output = self.device.execute(cmd)

        ret_dict = {}
        index = 1

        # STATIC Rules:
        p0 = re.compile(r"^STATIC Rules:$")

        # Rule ID | Type |  Domain |   VRF | Protocol |        Local IP |  Port |       Global IP |  Port | Network |
        # ---------------------------------------------------------------------------------------------------------------
        # 0xc     |  1-1 |  inside |     0 |      any |        15.0.0.1 |     0 |       135.0.0.1 |     0 |      32 |

        p1 = re.compile(
            r"^(?P<rule_id>\S+)\s+\|+\s+(?P<type>\d+-\d+|\s|\w+\/\w+)\s+\|+\s+(?P<domain>\w+)\s+\|+\s+(?P<vrf>\d+)\s+\|+\s+(?P<protocol>\S+)\s+\|+\s+(?P<local_ip>\S+)\s+\|+\s+(?P<local_port>\d+)\s+\|+\s+(?P<global_ip>\S+)\s+\|+\s+(?P<global_port>\d+)\s+\|+\s+(?P<network>\d+)\s+\|$"
        )

        # DYNAMIC Rules:
        p2 = re.compile(r"^DYNAMIC Rules:$")

        # Rule ID    |    Type |   VRF |                  Acl |    Pool/Interface_IP | Overload |
        # ----------------------------------------------------------------------------------------
        # 0x80000001 |  Inside |     0 |                    1 |            pool_in_1 |       No |
        p3 = re.compile(
            r"^(?P<rule_id>\S+)\s+\|+\s+(?P<type>\w+)\s+\|+\s+(?P<vrf>\d+)\s+\|+\s+(?P<acl>\S+)\s+\|+\s+(?P<pool_interface_ip>\S+)\s+\|+\s+(?P<overload>\S+)\s+\|$"
        )

        # Number of Rules : 2
        p4 = re.compile(r"^Number of Rules +: +(?P<number_of_rules>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            # STATIC Rules:
            m = p0.match(line)
            if m:
                group = m.groupdict()
                rules = ret_dict.setdefault("rules", {})
                rule_dict = rules.setdefault("static", {})

            # Rule ID | Type |  Domain |   VRF | Protocol |        Local IP |  Port |       Global IP |  Port | Network |
            # ---------------------------------------------------------------------------------------------------------------
            # 0xc     |  1-1 |  inside |     0 |      any |        15.0.0.1 |     0 |       135.0.0.1 |     0 |      32 |

            m = p1.match(line)
            if m:
                group = m.groupdict()
                index_dict = rule_dict.setdefault("index", {}).setdefault(index, {})
                index_dict["rule_id"] = group["rule_id"]
                index_dict["type"] = group["type"]
                index_dict["domain"] = group["domain"]
                index_dict["vrf"] = int(group["vrf"])
                index_dict["protocol"] = group["protocol"]
                index_dict["local_ip"] = group["local_ip"]
                index_dict["local_port"] = int(group["local_port"])
                index_dict["global_ip"] = group["global_ip"]
                index_dict["global_port"] = int(group["global_port"])
                index_dict["network"] = int(group["network"])
                index += 1

            # DYNAMIC Rules:
            m = p2.match(line)
            if m:
                group = m.groupdict()
                rules = ret_dict.setdefault("rules", {})
                rule_dict = rules.setdefault("dynamic", {})

            # Rule ID    |    Type |   VRF |                  Acl |    Pool/Interface_IP | Overload |
            # ----------------------------------------------------------------------------------------
            # 0x80000001 |  Inside |     0 |                    1 |            pool_in_1 |       No |
            m = p3.match(line)
            if m:
                group = m.groupdict()
                index_dict = rule_dict.setdefault("index", {}).setdefault(index, {})
                index_dict["rule_id"] = group["rule_id"]
                index_dict["type"] = group["type"]
                index_dict["vrf"] = int(group["vrf"])
                index_dict["acl"] = group["acl"]
                index_dict["pool_interface_ip"] = group["pool_interface_ip"]
                index_dict["overload"] = group["overload"]
                index += 1

            # Number of Rules : 2
            m = p4.match(line)
            if m:
                group = m.groupdict()
                rule_dict["number_of_rules"] = int(group["number_of_rules"])
                continue

        return ret_dict


class ShowPlatformSoftwareFedSwitchActiveNatInterfacesSchema(MetaParser):
    """
    Schema for show platform software fed switch active nat interfaces
    """

    schema = {
        "index": {
            Any(): {
                "interface_name": str,
                "interface_id": str,
                "domain": str,
            },
        },
        "number_of_interfaces": int,
    }


class ShowPlatformSoftwareFedSwitchActiveNatInterfaces(
    ShowPlatformSoftwareFedSwitchActiveNatInterfacesSchema
):
    """
    show platform software fed switch active nat interfaces
    """

    cli_command = [
        "show platform software fed {switch} {mode} nat interfaces",
        "show platform software fed active nat interfaces",
    ]

    def cli(self, switch="", mode="", output=None):
        if output is None:
            if switch and mode:
                cmd = self.cli_command[0].format(switch=switch, mode=mode)
            else:
                cmd = self.cli_command[1]
            output = self.device.execute(cmd)

        ret_dict = {}
        index = 1

        #                 Interface Name |         Interface ID |  Domain |
        # ------------------------------------------------------------------
        #          GigabitEthernet1/0/23 |                0x44e | outside |
        #                         Vlan11 |                0x450 |  inside |
        p0 = re.compile(
            r"^(?P<interface_name>\S+)\s+\|+\s+(?P<interface_id>\w+)\s+\|+\s+(?P<domain>\S+)\s+\|$"
        )

        # Number of Interfaces : 2
        p1 = re.compile(r"^Number of Interfaces +: +(?P<number_of_interfaces>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            #                 Interface Name |         Interface ID |  Domain |
            # ------------------------------------------------------------------
            #          GigabitEthernet1/0/23 |                0x44e | outside |
            #                         Vlan11 |                0x450 |  inside |
            m = p0.match(line)
            if m:
                group = m.groupdict()
                index_dict = ret_dict.setdefault("index", {}).setdefault(index, {})
                index_dict["interface_name"] = group["interface_name"]
                index_dict["interface_id"] = group["interface_id"]
                index_dict["domain"] = group["domain"]
                index += 1
                continue

            # Number of Interfaces : 2
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict["number_of_interfaces"] = int(group["number_of_interfaces"])
                continue

        return ret_dict


class ShowPlatformSoftwareFedSwitchActiveNatRulesSchema(MetaParser):
    """
    Schema for show platform software fed switch active nat rules
    """

    schema = {
        "rules": {
            Optional(Or("static", "dynamic")): {
                Optional("index"): {
                    int: {
                        Optional("rule_id"): str,
                        Optional("type"): str,
                        Optional("domain"): str,
                        Optional("vrf"): int,
                        Optional("protocol"): str,
                        Optional("local_ip"): str,
                        Optional("local_port"): int,
                        Optional("global_ip"): str,
                        Optional("global_port"): int,
                        Optional("network"): int,
                        Optional("acl"): str,
                        Optional("pool_interface_ip"): str,
                        Optional("overload"): str,
                    },
                },
                "number_of_rules": int,
            },
        },
    }


class ShowPlatformSoftwareFedSwitchActiveNatRules(
    ShowPlatformSoftwareFedSwitchActiveNatRulesSchema
):
    """
    show platform software fed switch active nat rules
    """

    cli_command = [
        "show platform software fed {switch} {mode} nat rules",
        "show platform software fed active nat rules",
    ]

    def cli(self, switch="", mode="", output=None):
        if output is None:
            if switch and mode:
                cmd = self.cli_command[0].format(switch=switch, mode=mode)
            else:
                cmd = self.cli_command[1]
            output = self.device.execute(cmd)

        ret_dict = {}
        index = 1

        # STATIC Rules:
        p0 = re.compile(r"^STATIC Rules:$")

        # Rule ID | Type |  Domain |   VRF | Protocol |        Local IP |  Port |       Global IP |  Port | Network |
        # ---------------------------------------------------------------------------------------------------------------
        # 0xc     |  1-1 |  inside |     0 |      any |        15.0.0.1 |     0 |       135.0.0.1 |     0 |      32 |

        p1 = re.compile(
            r"^(?P<rule_id>\S+)\s+\|+\s+(?P<type>\d+-\d+|\s|\w+\/\w+)\s+\|+\s+(?P<domain>\w+)\s+\|+\s+(?P<vrf>\d+)\s+\|+\s+(?P<protocol>\S+)\s+\|+\s+(?P<local_ip>\S+)\s+\|+\s+(?P<local_port>\d+)\s+\|+\s+(?P<global_ip>\S+)\s+\|+\s+(?P<global_port>\d+)\s+\|+\s+(?P<network>\d+)\s+\|$"
        )

        # DYNAMIC Rules:
        p2 = re.compile(r"^DYNAMIC Rules:$")

        # Rule ID    |    Type |   VRF |                  Acl |    Pool/Interface_IP | Overload |
        # ----------------------------------------------------------------------------------------
        # 0x80000001 |  Inside |     0 |                    1 |            pool_in_1 |       No |
        p3 = re.compile(
            r"^(?P<rule_id>\S+)\s+\|+\s+(?P<type>\w+)\s+\|+\s+(?P<vrf>\d+)\s+\|+\s+(?P<acl>\S+)\s+\|+\s+(?P<pool_interface_ip>\S+)\s+\|+\s+(?P<overload>\S+)\s+\|$"
        )

        # Number of Rules : 2
        p4 = re.compile(r"^Number of Rules +: +(?P<number_of_rules>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            # STATIC Rules:
            m = p0.match(line)
            if m:
                group = m.groupdict()
                rules = ret_dict.setdefault("rules", {})
                rule_dict = rules.setdefault("static", {})

            # Rule ID | Type |  Domain |   VRF | Protocol |        Local IP |  Port |       Global IP |  Port | Network |
            # ---------------------------------------------------------------------------------------------------------------
            # 0xc     |  1-1 |  inside |     0 |      any |        15.0.0.1 |     0 |       135.0.0.1 |     0 |      32 |

            m = p1.match(line)
            if m:
                group = m.groupdict()
                index_dict = rule_dict.setdefault("index", {}).setdefault(index, {})
                index_dict["rule_id"] = group["rule_id"]
                index_dict["type"] = group["type"]
                index_dict["domain"] = group["domain"]
                index_dict["vrf"] = int(group["vrf"])
                index_dict["protocol"] = group["protocol"]
                index_dict["local_ip"] = group["local_ip"]
                index_dict["local_port"] = int(group["local_port"])
                index_dict["global_ip"] = group["global_ip"]
                index_dict["global_port"] = int(group["global_port"])
                index_dict["network"] = int(group["network"])
                index += 1

            # DYNAMIC Rules:
            m = p2.match(line)
            if m:
                group = m.groupdict()
                rules = ret_dict.setdefault("rules", {})
                rule_dict = rules.setdefault("dynamic", {})

            # Rule ID    |    Type |   VRF |                  Acl |    Pool/Interface_IP | Overload |
            # ----------------------------------------------------------------------------------------
            # 0x80000001 |  Inside |     0 |                    1 |            pool_in_1 |       No |
            m = p3.match(line)
            if m:
                group = m.groupdict()
                index_dict = rule_dict.setdefault("index", {}).setdefault(index, {})
                index_dict["rule_id"] = group["rule_id"]
                index_dict["type"] = group["type"]
                index_dict["vrf"] = int(group["vrf"])
                index_dict["acl"] = group["acl"]
                index_dict["pool_interface_ip"] = group["pool_interface_ip"]
                index_dict["overload"] = group["overload"]
                index += 1

            # Number of Rules : 2
            m = p4.match(line)
            if m:
                group = m.groupdict()
                rule_dict["number_of_rules"] = int(group["number_of_rules"])
                continue

        return ret_dict


# ======================================================
# Parser for 'show platform software fed active fnf sw-stats-show'
# ======================================================
class ShowPlatformSoftwareFedSwitchActiveFnfSwStatsShowSchema(MetaParser):
    """Schema for show platform software fed active fnf sw-stats-show"""

    schema = {
        "fnf_statistics": {
            Any(): {
                Optional("id"): int,
                "value": int,
            },
        },
    }


class ShowPlatformSoftwareFedSwitchActiveFnfSwStatsShow(
    ShowPlatformSoftwareFedSwitchActiveFnfSwStatsShowSchema
):
    """Parser for show platform software fed active fnf sw-stats-show"""

    cli_command = [
        "show platform software fed {switch} {switch_var} fnf sw-stats-show",
        "show platform software fed {switch_var} fnf sw-stats-show",
    ]

    def cli(self, switch_var, switch="", output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(switch=switch, switch_var=switch_var)
            else:
                cmd = self.cli_command[1].format(switch_var=switch_var)
            output = self.device.execute(cmd)

        # monitor_action_message_rcvd:                    4
        # exporter_action_message_rcvd:                   0
        p1 = re.compile(r"(?P<statistic>[\w\_]+):\s+(?P<value>[\d]+)$")

        # 110: num_fin_rst_skip_flow_pend_del:    0
        # 111: num_wdavc_del_pend_set_same_state_warn: 0
        p2 = re.compile(r"^(?P<id>\d+):\s+(?P<statistic>[\w\_]+):\s+(?P<value>[\d]+)$")

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # monitor_action_message_rcvd:                    4
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                fnf_dict = ret_dict.setdefault("fnf_statistics", {}).setdefault(
                    dict_val["statistic"], {}
                )
                fnf_dict["value"] = int(dict_val["value"])
                continue

            # 110: num_fin_rst_skip_flow_pend_del:    0
            m = p2.match(line)
            if m:
                dict_val = m.groupdict()
                fnf_dict = ret_dict.setdefault("fnf_statistics", {}).setdefault(
                    dict_val["statistic"], {}
                )
                fnf_dict["value"] = int(dict_val["value"])
                fnf_dict["id"] = int(dict_val["id"])
                continue

        return ret_dict


# ============================================================================
# Parser for 'show platform software fed active drop packet-capture statistics'
# ============================================================================
class ShowPlatformSoftwareFedActiveDropPacketCaptureStatisticsSchema(MetaParser):
    """Schema for show platform software fed active drop packet-capture statistics"""

    schema = {
        "trap_id": {
            Any(): {"trap_name": str, "dropped_pkts": int, "rate": int},
        },
    }


class ShowPlatformSoftwareFedActiveDropPacketCaptureStatistics(
    ShowPlatformSoftwareFedActiveDropPacketCaptureStatisticsSchema
):
    """Parser for show platform software fed active drop packet-capture statistics"""

    cli_command = [
        "show platform software fed {switch} {switch_var} drop packet-capture statistics",
        "show platform software fed {switch_var} drop packet-capture statistics",
    ]

    def cli(self, switch_var, switch="", output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(switch=switch, switch_var=switch_var)
            else:
                cmd = self.cli_command[1].format(switch_var=switch_var)

            output = self.device.execute(cmd)

        #       Trap  Description                                                            Dropped Pkts          Rate
        # ----------------------------------------------------------------------------------------------------------
        # 225   EXACT_METER_PACKET_GOT_DROPPED_DUE_TO_EXACT_METER                          1659               0
        # 226   STATISTICAL_METER_PACKET_GOT_DROPPED_DUE_TO_STATISTICAL_METER               0                 0

        p1 = re.compile(
            r"^(?P<trap_id>[\d]+)+\s+(?P<trap_name>[\w\_]+)+\s+(?P<dropped_pkts>[\d]+)+\s+(?P<rate>[\d]+)$"
        )

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # 54    ETHERNET_SA_MULTICAST                                                       0                 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                id_dict = ret_dict.setdefault("trap_id", {}).setdefault(
                    m.groupdict()["trap_id"], {}
                )
                id_dict["trap_name"] = group["trap_name"]
                id_dict["dropped_pkts"] = int(group["dropped_pkts"])
                id_dict["rate"] = int(group["rate"])

        return ret_dict


# =======================================================================================
# Parser for 'show platform software fed active drop packet-capture interfaces-stats'
# =======================================================================================
class ShowPlatformSoftwareFedActiveDropPacketCaptureInterfacesStatsSchema(MetaParser):
    """Schema for show platform software fed active drop packet-capture interfaces-stats"""

    schema = {
        "interface": {
            Any(): {"if_id": str, "dropped_pkts": int},
        },
    }


class ShowPlatformSoftwareFedActiveDropPacketCaptureInterfacesStats(
    ShowPlatformSoftwareFedActiveDropPacketCaptureInterfacesStatsSchema
):
    """Parser for show platform software fed active drop packet-capture interfaces-stats"""

    cli_command = [
        "show platform software fed {switch} {switch_var} drop packet-capture interfaces-stats",
        "show platform software fed {switch_var} drop packet-capture interfaces-stats",
    ]

    def cli(self, switch_var, switch="", output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(switch=switch, switch_var=switch_var)
            else:
                cmd = self.cli_command[1].format(switch_var=switch_var)

            output = self.device.execute(cmd)

        # Interface                              If id             Dropped Pkts
        # --------------------------------------------------------------------------
        # HundredGigE1/0/3                       0x4CD                 504

        p1 = re.compile(
            r"^(?P<interface>[\w\/]+)+\s+(?P<if_id>[\w]+)+\s+(?P<dropped_pkts>[\d]+)$"
        )

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                id_dict = ret_dict.setdefault("interface", {}).setdefault(
                    m.groupdict()["interface"], {}
                )
                id_dict["if_id"] = group["if_id"]
                id_dict["dropped_pkts"] = int(group["dropped_pkts"])

        return ret_dict


class ShowPlatformSoftwareFedIfmSchema(MetaParser):
    schema = {"interfaces": {Any(): {"if_id": str, "state": str}}}


class ShowPlatformSoftwareFedIfm(ShowPlatformSoftwareFedIfmSchema):
    cli_command = [
        "show platform software fed {switch} active ifm interfaces tunnel",
        "show platform software fed active ifm interfaces tunnel",
    ]

    def cli(self, switch=None, output=None):
        if output is None:
            if switch is None:
                cmd = self.cli_command[1]
            else:
                cmd = self.cli_command[0].format(switch=switch)

            output = self.device.execute(cmd)
        parsed_dict = {}
        # Tunnel1 0x0000005d READY
        p1 = re.compile(
            r"^(?P<interface>(^[a-zA-Z]+[0-9]+)) +(?P<if_id>\w+) +(?P<state>[\w\s]+)$"
        )
        for line in output.splitlines():
            line = line.strip()

            # Tunnel1 0x0000005d READY
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = group["interface"]
                interface_dict = parsed_dict.setdefault("interfaces", {}).setdefault(
                    interface, {}
                )
                interface_dict["if_id"] = group["if_id"]
                interface_dict["state"] = str(group["state"])

                continue
        return parsed_dict


class ShowPlatformIfmMappingSchema(MetaParser):
    """Schema for show platform software fed switch active ifm mappings"""

    schema = {
        "interface": {
            Any(): {
                "if_id": str,
                "inst": int,
                "asic": int,
                "core": int,
                Optional("ifg_id"): int,
                "port": int,
                "subport": int,
                "mac": int,
                Optional("first_serdes"): int,
                Optional("last_serdes"): int,
                "cntx": int,
                "lpn": int,
                "gpn": int,
                "type": str,
                "active": str,
            },
        },
    }


# ============================================================
#  Parser for 'show platform software fed active ifm mappings'
# ============================================================
class ShowPlatformIfmMapping(ShowPlatformIfmMappingSchema):

    """Parser for show platform software fed switch active ifm mappings"""

    cli_command = [
        "show platform software fed switch {state} ifm mappings",
        "show platform software fed active ifm mappings",
    ]

    def cli(self, state=None, output=None):
        if output is None:
            if state:
                cmd = self.cli_command[0].format(state=state)
            else:
                cmd = self.cli_command[1]

            # Execute command to get output from device
            output = self.device.execute(cmd)

        # HundredGigE2/0/1          0x3      0   0    5      1    0      0     1    0            1            0    1    769  NIF    Y
        p1 = re.compile(
            r"^(?P<interface>\S+)\s+(?P<if_id>\S+)\s+(?P<inst>\d+)\s+(?P<asic>\d+)\s+(?P<core>\d+)\s+(?P<ifg_id>\d+)?\s+(?P<port>\d+)\s+(?P<subport>\d+)\s+(?P<mac>\d+)\s+(?P<first_serdes>\d+)?\s+(?P<last_serdes>\d+)?\s+(?P<cntx>\d+)\s+(?P<lpn>\d+)\s+(?P<gpn>\d+)\s+(?P<type>\w+)\s+(?P<active>\w+)\s*$"
        )

        # initial variables
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # HundredGigE2/0/1          0x3      0   0    5      1    0      0     1    0            1            0    1    769  NIF    Y
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface_dict = ret_dict.setdefault("interface", {}).setdefault(
                    group["interface"], {}
                )
                interface_dict["if_id"] = group["if_id"]
                interface_dict["inst"] = int(group["inst"])
                interface_dict["asic"] = int(group["asic"])
                interface_dict["core"] = int(group["core"])
                if group["ifg_id"] is not None:
                    interface_dict["ifg_id"] = int(group["ifg_id"])
                interface_dict["port"] = int(group["port"])
                interface_dict["subport"] = int(group["subport"])
                interface_dict["mac"] = int(group["mac"])
                if group["first_serdes"] is not None:
                    interface_dict["first_serdes"] = int(group["first_serdes"])
                if group["last_serdes"] is not None:
                    interface_dict["last_serdes"] = int(group["last_serdes"])
                interface_dict["cntx"] = int(group["cntx"])
                interface_dict["lpn"] = int(group["lpn"])
                interface_dict["gpn"] = int(group["gpn"])
                interface_dict["type"] = group["type"]
                interface_dict["active"] = group["active"]
                continue

        return ret_dict


# ======================================================
# Parser for 'show platform software fed switch active ifm if-id
# ======================================================
class ShSoftwareFedSchema(MetaParser):
    """Schema for show platform software fed switch active ifm if-id"""

    schema = {
        "intf_id": str,
        "intf_name": str,
        "intf_block_pointer": str,
        "intf_block_state": str,
        "intf_state": str,
        "intf_admin_mode": str,
        "intf_status": str,
        "int_ref_cnt": int,
        "interface_type": {
            "intf_type": str,
            "port_type": str,
            "port_location": str,
            "slot": int,
            "unit": int,
            "slot_unit": int,
            "snmp_index": int,
            "gpn": int,
            "ec_channel": int,
            "ec_index": int,
            "ipv4_mtu": int,
            "ipv6_mtu": int,
            Optional("ipv4_vrf_id"): int,
            Optional("ipv6_vrf_id"): int,
            "protocol_flags": str,
            Optional("misc_flags"): str,
            "icmpv4_flags": str,
            "icmpv6_flags": str,
            "mac_address": str,
            "qos_trust_type": str,
        },
        "ref_count": str,
        "port_phy_sub": {
            "affinity": str,
            "lpn": int,
            "gpn": int,
            "speed": str,
            "type": str,
            "mtu": int,
            "ac_profile": str,
        },
        "port_sub": {
            "mac_port_oid": int,
            "system_port_oid": int,
            "system_port_gid": int,
            "ethernet_port_oid": int,
            "vog_oid": int,
        },
        "platform_sub": {
            "asic": int,
            "core": int,
            "asic_port": int,
            "asic_sub_port": int,
            "ifg_id": int,
            "mac_num": int,
            "first_serdes": int,
            "last_serdes": int,
            "fc_mode": int,
            "fec_mode": int,
            "context_id": int,
        },
        "port_l2_sub": {
            "port_mode": str,
            "port_mode_set": str,
            "vlan": int,
            "ethertype": int,
            "bd_vlan": int,
            "status": int,
            "ac_profile": str,
        },
        Optional("port_l3_sub"): {
            Optional("vrf_id"): int,
            Optional("ipv4_routing"): str,
            Optional("ipv6_routing"): str,
            Optional("mpls"): str,
            Optional("pimv4"): str,
            Optional("pimv6"): str,
            Optional("ipv4_mtu"): int,
            Optional("ipv6_mtu"): int,
            Optional("l3_srv"): int,
            Optional("l3_srv_oid"): int,
        },
    }


class ShSoftwareFed(ShSoftwareFedSchema):

    """Parser for show platform software fed switch active ifm if-id {if_id}"""

    cli_command = [
        "show platform software fed switch {switch_type} ifm {if_id}",
        "show platform software fed active ifm {if_id}",
    ]

    def cli(self, if_id, switch_type="", out=None):
        if out is None:
            if switch_type is not None:
                cmd = self.cli_command[0].format(if_id=if_id, switch_type=switch_type)
            else:
                cmd = self.cli_command[1].format(if_id=if_id)

            out = self.device.execute(cmd)

        # Interface IF_ID : 0x0000000000000561
        p1 = re.compile(r"^Interface\s+IF_ID\s+:\s+(?P<intf_id>\S+)$")

        # Interface Name : HundredGigE1/6/0/19
        p2 = re.compile(r"^Interface\s+Name\s+:\s+(?P<intf_name>\S+)$")

        # Interface Block Pointer : 0x7feaa50bbc28
        p3 = re.compile(
            r"^Interface\s+Block\s+Pointer\s+:\s+(?P<intf_block_pointer>\S+)$"
        )

        # Interface Block State : Ready
        p4 = re.compile(r"^Interface\s+Block\s+State\s+:\s+(?P<intf_block_state>\w+)$")

        # Interface State : Enabled
        p5 = re.compile(r"^Interface\s+State\s+:\s+(?P<intf_state>\w+)$")

        # Interface Admin mode : Admin Up
        p6 = re.compile(
            r"^Interface\s+Admin\s+mode\s+:\s+(?P<intf_admin_mode>\S+\s+\S+)$"
        )

        # Interface Status : NPD
        p7 = re.compile(r"^Interface\s+Status\s+:\s+(?P<intf_status>\w.+)$")

        # Interface Ref-Cnt : 1
        p8 = re.compile(r"^Interface\s+Ref-Cnt\s+:\s+(?P<int_ref_cnt>\d+)$")

        # Interface Type : ETHER
        p9 = re.compile(r"^Interface\s+Type\s+:\s+(?P<intf_type>\w+)$")

        # Port Type : ROUTE PORT
        p9_1 = re.compile(r"^\s+Port\s+Type\s+:\s+(?P<port_type>\S+\s+\S+)$")

        # Port Location : LOCAL
        p9_2 = re.compile(r"^\s+Port\s+Location\s+:\s+(?P<port_location>\w+)$")

        # Slot : 13
        p9_3 = re.compile(r"^\s+Slot\s+:\s+(?P<slot>\d+)$")

        # Unit : 0
        p9_4 = re.compile(r"^\s+Unit\s+:\s+(?P<unit>\d+)$")

        # Slot Unit : 19
        p9_5 = re.compile(r"^\s+Slot\s+Unit\s+:\s+(?P<slot_unit>\d+)$")

        # SNMP IF Index : 119
        p9_6 = re.compile(r"^\s+SNMP\s+IF\s+Index\s+:\s+(?P<snmp_index>\d+)$")

        # GPN : 979
        p9_7 = re.compile(r"^\s+GPN\s+:\s+(?P<gpn>\d+)$")

        # EC Channel : 0
        p9_8 = re.compile(r"^\s+EC\s+Channel\s+:\s+(?P<ec_channel>\d+)$")

        # EC Index : 0
        p9_9 = re.compile(r"^\s+EC\s+Index\s+:\s+(?P<ec_index>\d+)$")

        # IPv4 MTU : 2000
        p9_10 = re.compile(r"^\s+IPv4\s+MTU\s+:\s+(?P<ipv4_mtu>\d+)$")

        # IPv6 MTU : 0
        p9_11 = re.compile(r"^\s+IPv6\s+MTU\s+:\s+(?P<ipv6_mtu>\d+)$")

        # IPv4 VRF ID : 0
        p9_12 = re.compile(r"^\s+IPv4\s+VRF\s+ID\s+:\s+(?P<ipv4_vrf_id>\d+)$")

        # IPv6 VRF ID : 65535
        p9_13 = re.compile(r"^\s+IPv6\s+VRF\s+ID\s+:\s+(?P<ipv6_vrf_id>\d+)$")

        # Protocol flags : 0x0003 [ ipv4 ipv6 ]
        p9_14 = re.compile(
            r"^\s+Protocol\s+flags\s+:\s+(?P<protocol_flags>\S+\s+\S+\s+\S+\s+\S+\s+\S+)$"
        )

        # Misc flags : 0x0041 [ ipv4 --- ]
        p9_15 = re.compile(
            r"^\s+Misc\s+flags\s+:\s+(?P<misc_flags>\S+\s+\S+\s+\S+\s+\S+\s+\S+)$"
        )

        # ICMPv4 flags : 0x03 [ unreachable redirect ]
        p9_16 = re.compile(
            r"^\s+ICMPv4\s+flags\s+:\s+(?P<icmpv4_flags>\S+\s+\S+\s+\S+\s+\S+\s+\S+)$"
        )

        # ICMPv6 flags : 0x03 [ unreachable redirect ]
        p9_17 = re.compile(
            r"^\s+ICMPv6\s+flags\s+:\s+(?P<icmpv6_flags>\S+\s+\S+\s+\S+\s+\S+\s+\S+)$"
        )

        # Mac Address : 6c:b2:ae:4a:54:c5
        p9_18 = re.compile(r"^\s+Mac\s+Address\s+:\s+(?P<mac_address>\S+)$")

        # QoS Trust Type : 3 (DSCP)
        p9_19 = re.compile(
            r"^\s+QoS\s+Trust\s+Type\s+:\s+(?P<qos_trust_type>\S+\s+\S+)$"
        )

        # Ref Count : 1 (feature Ref Counts + 1)
        p10 = re.compile(
            r"^Ref\s+Count\s+:\s+(?P<ref_count>\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+)$"
        )

        # Affinity .......... [local]
        p11 = re.compile(
            r"^\s+Affinity\s+\.\.\.\.\.\.\.\.\.\.\s+\[(?P<affinity>\w+)\]$"
        )

        # LPN ............... [19]
        p11_1 = re.compile(
            r"^\s+LPN\s+\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\s+\[(?P<lpn>\d+)\]$"
        )

        # GPN ............... [979]
        p11_2 = re.compile(
            r"^\s+GPN\s+\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\s+\[(?P<gpn>\d+)\]$"
        )

        # Speed ............. [40GB]
        p11_3 = re.compile(
            r"^\s+Speed\s+\.\.\.\.\.\.\.\.\.\.\.\.\.\s+\[(?P<speed>\S+)\]$"
        )

        # type .............. [IFM_PORT_TYPE_L3]
        p11_4 = re.compile(
            r"^\s+type\s+\.\.\.\.\.\.\.\.\.\.\.\.\.\.\s+\[(?P<type>\S+)\]$"
        )

        # MTU ............... [2022]
        p11_5 = re.compile(
            r"^\s+MTU\s+\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\s+\[(?P<mtu>\d+)\]$"
        )

        # ac profile ........ [IFM_AC_PROFILE_DEFAULT]
        p11_6 = re.compile(
            r"^\s+ac\s+profile\s+\.\.\.\.\.\.\.\.\s+\[(?P<ac_profile>\S+)\]$"
        )

        # Mac port oid................... [4444]
        p12 = re.compile(
            r"^\s+Mac\s+port\s+oid\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\s+\[(?P<mac_port_oid>\d+)\]$"
        )

        # System port oid................ [4448]
        p12_1 = re.compile(
            r"^\s+System\s+port\s+oid\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\s+\[(?P<system_port_oid>\d+)\]$"
        )

        # System port gid................ [223]
        p12_2 = re.compile(
            r"^\s+System\s+port\s+gid\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\s+\[(?P<system_port_gid>\d+)\]$"
        )

        # Ethernet port oid.............. [4459]
        p12_3 = re.compile(
            r"^\s+Ethernet\s+port\s+oid\.\.\.\.\.\.\.\.\.\.\.\.\.\.\s+\[(?P<ethernet_port_oid>\d+)\]$"
        )

        # Voq oid........................ [4446]
        p12_4 = re.compile(
            r"^\s+Voq\s+oid\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\s+\[(?P<vog_oid>\d+)\]$"
        )

        # Asic.............. [0]
        p13 = re.compile(r"^\s+Asic\.\.\.\.\.\.\.\.\.\.\.\.\.\.\s+\[(?P<asic>\d+)\]$")

        # Core.............. [5]
        p13_1 = re.compile(r"^\s+Core\.\.\.\.\.\.\.\.\.\.\.\.\.\.\s+\[(?P<core>\d+)\]$")

        # Asic Port......... [0]
        p13_2 = re.compile(
            r"^\s+Asic\s+Port\.\.\.\.\.\.\.\.\.\s+\[(?P<asic_port>\d+)\]$"
        )

        # Asic Sub Port..... [65535]
        p13_3 = re.compile(
            r"^\s+Asic\s+Sub\s+Port\.\.\.\.\.\s+\[(?P<asic_sub_port>\d+)\]$"
        )

        # Ifg Id............ [0]
        p13_4 = re.compile(
            r"^\s+Ifg\s+Id\.\.\.\.\.\.\.\.\.\.\.\.\s+\[(?P<ifg_id>\d+)\]$"
        )

        # Mac Num........... [211]
        p13_5 = re.compile(
            r"^\s+Mac\s+Num\.\.\.\.\.\.\.\.\.\.\.\s+\[(?P<mac_num>\d+)\]$"
        )

        # First Serdes...... [10]
        p13_6 = re.compile(
            r"^\s+First\s+Serdes\.\.\.\.\.\.\s+\[(?P<first_serdes>\d+)\]$"
        )

        # Last Serdes....... [11]
        p13_7 = re.compile(
            r"^\s+Last\s+Serdes\.\.\.\.\.\.\.\s+\[(?P<last_serdes>\d+)\]$"
        )

        # FC Mode........... [0]
        p13_8 = re.compile(
            r"^\s+FC\s+Mode\.\.\.\.\.\.\.\.\.\.\.\s+\[(?P<fc_mode>\d+)\]$"
        )

        # FEC Mode.......... [0]
        p13_9 = re.compile(
            r"^\s+FEC\s+Mode\.\.\.\.\.\.\.\.\.\.\s+\[(?P<fec_mode>\d+)\]$"
        )

        # Context Id........ [0]
        p13_10 = re.compile(
            r"^\s+Context\s+Id\.\.\.\.\.\.\.\.\s+\[(?P<context_id>\d+)\]$"
        )

        # L2 Port Mode ................ [port_mode_dynamic]
        p14 = re.compile(
            r"^\s+L2\s+Port\s+Mode\s+\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\s+\[(?P<port_mode>\S+)\]$"
        )

        # L2 Port Mode set............. [No]
        p14_1 = re.compile(
            r"^\s+L2\s+Port\s+Mode\s+set\.\.\.\.\.\.\.\.\.\.\.\.\.\s+\[(?P<port_mode_set>\w+)\]$"
        )

        # Default vlan ................ [0]
        p14_2 = re.compile(
            r"^\s+Default\s+vlan\s+\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\s+\[(?P<vlan>\d+)\]$"
        )

        # Ethertype.................... [8100]
        p14_3 = re.compile(
            r"^\s+Ethertype\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\s+\[(?P<ethertype>\d+)\]$"
        )

        # untagged port bd vlan ....... [0]
        p14_4 = re.compile(
            r"^\s+untagged\s+port\s+bd\s+vlan\s+\.\.\.\.\.\.\.\s+\[(?P<bd_vlan>\d+)\]$"
        )

        # status....................... [0]
        p14_5 = re.compile(
            r"^\s+status\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\s+\[(?P<status>\d+)\]$"
        )

        # ac profile .................. [IFM_AC_PROFILE_DEFAULT]
        p14_6 = re.compile(
            r"^\s+ac\s+profile\s+\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\s+\[(?P<ac_profile>\S+)\]$"
        )

        # VRF ID .................. [0]
        p15 = re.compile(
            r"^\s+VRF\s+ID\s+\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\s+\[(?P<vrf_id>\d+)\]$"
        )

        # IPv4 Routing Enabled .... [Yes]
        p15_1 = re.compile(
            r"^\s+IPv4\s+Routing\s+Enabled\s+\.\.\.\.\s+\[(?P<ipv4_routing>\w+)\]$"
        )

        # IPv6 Routing Enabled .... [No]
        p15_2 = re.compile(
            r"^\s+IPv6\s+Routing\s+Enabled\s+\.\.\.\.\s+\[(?P<ipv6_routing>\w+)\]$"
        )

        # MPLS Enabled ............ [No]
        p15_3 = re.compile(
            r"^\s+MPLS\s+Enabled\s+\.\.\.\.\.\.\.\.\.\.\.\.\s+\[(?P<mpls>\w+)\]$"
        )

        # Pimv4 Enabled ........... [No]
        p15_4 = re.compile(
            r"^\s+Pimv4\s+Enabled\s+\.\.\.\.\.\.\.\.\.\.\.\s+\[(?P<pimv4>\w+)\]$"
        )

        # Pimv6 Enabled ........... [No]
        p15_5 = re.compile(
            r"^\s+Pimv6\s+Enabled\s+\.\.\.\.\.\.\.\.\.\.\.\s+\[(?P<pimv6>\w+)\]$"
        )

        # IPv4 MTU ................ [2018]
        p15_6 = re.compile(
            r"^\s+IPv4\s+MTU\s+\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\s+\[(?P<ipv4_mtu>\d+)\]$"
        )

        # IPv6 MTU ................ [18]
        p15_7 = re.compile(
            r"^\s+IPv6\s+MTU\s+\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\s+\[(?P<ipv6_mtu>\d+)\]$"
        )

        # L3 srv port gid ......... [4312]
        p15_8 = re.compile(
            r"^\s+L3\s+srv\s+port\s+gid\s+\.\.\.\.\.\.\.\.\.\s+\[(?P<l3_srv>\d+)\]$"
        )

        # L3 srv port oid ......... [5489]
        p15_9 = re.compile(
            r"^\s+L3\s+srv\s+port\s+oid\s+\.\.\.\.\.\.\.\.\.\s+\[(?P<l3_srv_oid>\d+)\]$"
        )

        ret_dict = {}

        for line in out.splitlines():
            # Interface IF_ID : 0x0000000000000561
            match_obj = p1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                ret_dict["intf_id"] = dict_val["intf_id"]
                continue

            # Interface Name : HundredGigE1/6/0/19
            match_obj = p2.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                ret_dict["intf_name"] = dict_val["intf_name"]
                continue

            # Interface Block Pointer : 0x7feaa50bbc28
            match_obj = p3.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                ret_dict["intf_block_pointer"] = dict_val["intf_block_pointer"]
                continue

            # Interface Block State : Ready
            match_obj = p4.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                ret_dict["intf_block_state"] = dict_val["intf_block_state"]
                continue

            # Interface State : Enabled
            match_obj = p5.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                ret_dict["intf_state"] = dict_val["intf_state"]
                continue

            # Interface Admin mode : Admin Up
            match_obj = p6.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                ret_dict["intf_admin_mode"] = dict_val["intf_admin_mode"]
                continue

            # Interface Status : NPD
            match_obj = p7.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                ret_dict["intf_status"] = dict_val["intf_status"]
                continue

            # Interface Ref-Cnt : 1
            match_obj = p8.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                ret_dict["int_ref_cnt"] = int(dict_val["int_ref_cnt"])
                continue

            # Interface Type : ETHER
            match_obj = p9.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "interface_type" not in ret_dict:
                    interface_type = ret_dict.setdefault("interface_type", {})
                interface_type["intf_type"] = dict_val["intf_type"]
                continue

            # Port Type : ROUTE PORT
            match_obj = p9_1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "interface_type" not in ret_dict:
                    interface_type = ret_dict.setdefault("interface_type", {})
                interface_type["port_type"] = dict_val["port_type"]
                continue

            # Port Location : LOCAL
            match_obj = p9_2.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "interface_type" not in ret_dict:
                    interface_type = ret_dict.setdefault("interface_type", {})
                interface_type["port_location"] = dict_val["port_location"]
                continue

            # Slot : 13
            match_obj = p9_3.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "interface_type" not in ret_dict:
                    interface_type = ret_dict.setdefault("interface_type", {})
                interface_type["slot"] = int(dict_val["slot"])
                continue

            # Unit : 0
            match_obj = p9_4.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "interface_type" not in ret_dict:
                    interface_type = ret_dict.setdefault("interface_type", {})
                interface_type["unit"] = int(dict_val["unit"])
                continue

            # Slot Unit : 19
            match_obj = p9_5.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "interface_type" not in ret_dict:
                    interface_type = ret_dict.setdefault("interface_type", {})
                interface_type["slot_unit"] = int(dict_val["slot_unit"])
                continue

            # SNMP IF Index : 119
            match_obj = p9_6.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "interface_type" not in ret_dict:
                    interface_type = ret_dict.setdefault("interface_type", {})
                interface_type["snmp_index"] = int(dict_val["snmp_index"])
                continue

            # GPN : 979
            match_obj = p9_7.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "interface_type" not in ret_dict:
                    interface_type = ret_dict.setdefault("interface_type", {})
                interface_type["gpn"] = int(dict_val["gpn"])
                continue

            # EC Channel : 0
            match_obj = p9_8.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "interface_type" not in ret_dict:
                    interface_type = ret_dict.setdefault("interface_type", {})
                interface_type["ec_channel"] = int(dict_val["ec_channel"])
                continue

            # EC Index : 0
            match_obj = p9_9.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "interface_type" not in ret_dict:
                    interface_type = ret_dict.setdefault("interface_type", {})
                interface_type["ec_index"] = int(dict_val["ec_index"])
                continue

            # IPv4 MTU : 2000
            match_obj = p9_10.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "interface_type" not in ret_dict:
                    interface_type = ret_dict.setdefault("interface_type", {})
                interface_type["ipv4_mtu"] = int(dict_val["ipv4_mtu"])
                continue

            # IPv6 MTU : 0
            match_obj = p9_11.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "interface_type" not in ret_dict:
                    interface_type = ret_dict.setdefault("interface_type", {})
                interface_type["ipv6_mtu"] = int(dict_val["ipv6_mtu"])
                continue

            # IPv4 VRF ID : 0
            match_obj = p9_12.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "interface_type" not in ret_dict:
                    interface_type = ret_dict.setdefault("interface_type", {})
                interface_type["ipv4_vrf_id"] = int(dict_val["ipv4_vrf_id"])
                continue

            # IPv6 VRF ID : 65535
            match_obj = p9_13.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "interface_type" not in ret_dict:
                    interface_type = ret_dict.setdefault("interface_type", {})
                interface_type["ipv6_vrf_id"] = int(dict_val["ipv6_vrf_id"])
                continue

            # Protocol flags : 0x0003 [ ipv4 ipv6 ]
            match_obj = p9_14.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "interface_type" not in ret_dict:
                    interface_type = ret_dict.setdefault("interface_type", {})
                interface_type["protocol_flags"] = dict_val["protocol_flags"]
                continue

            # Misc flags : 0x0041 [ ipv4 --- ]
            match_obj = p9_15.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "interface_type" not in ret_dict:
                    interface_type = ret_dict.setdefault("interface_type", {})
                interface_type["misc_flags"] = dict_val["misc_flags"]
                continue

            # ICMPv4 flags : 0x03 [ unreachable redirect ]
            match_obj = p9_16.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "interface_type" not in ret_dict:
                    interface_type = ret_dict.setdefault("interface_type", {})
                interface_type["icmpv4_flags"] = dict_val["icmpv4_flags"]
                continue

            # ICMPv6 flags : 0x03 [ unreachable redirect ]
            match_obj = p9_17.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "interface_type" not in ret_dict:
                    interface_type = ret_dict.setdefault("interface_type", {})
                interface_type["icmpv6_flags"] = dict_val["icmpv6_flags"]
                continue

            #  Mac Address : 6c:b2:ae:4a:54:c5
            match_obj = p9_18.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "interface_type" not in ret_dict:
                    interface_type = ret_dict.setdefault("interface_type", {})
                interface_type["mac_address"] = dict_val["mac_address"]
                continue

            # QoS Trust Type : 3 (DSCP)
            match_obj = p9_19.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "interface_type" not in ret_dict:
                    interface_type = ret_dict.setdefault("interface_type", {})
                interface_type["qos_trust_type"] = dict_val["qos_trust_type"]
                continue

            # Ref Count : 1 (feature Ref Counts + 1)
            match_obj = p10.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                ret_dict["ref_count"] = dict_val["ref_count"]
                continue

            # Affinity .......... [local]
            match_obj = p11.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "port_phy_sub" not in ret_dict:
                    port_phy_sub = ret_dict.setdefault("port_phy_sub", {})
                port_phy_sub["affinity"] = dict_val["affinity"]
                continue

            # LPN ............... [19]
            match_obj = p11_1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "port_phy_sub" not in ret_dict:
                    port_phy_sub = ret_dict.setdefault("port_phy_sub", {})
                port_phy_sub["lpn"] = int(dict_val["lpn"])
                continue

            # GPN ............... [979]
            match_obj = p11_2.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "port_phy_sub" not in ret_dict:
                    port_phy_sub = ret_dict.setdefault("port_phy_sub", {})
                port_phy_sub["gpn"] = int(dict_val["gpn"])
                continue

            # Speed ............. [40GB]
            match_obj = p11_3.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "port_phy_sub" not in ret_dict:
                    port_phy_sub = ret_dict.setdefault("port_phy_sub", {})
                port_phy_sub["speed"] = dict_val["speed"]
                continue

            # type .............. [IFM_PORT_TYPE_L3]
            match_obj = p11_4.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "port_phy_sub" not in ret_dict:
                    port_phy_sub = ret_dict.setdefault("port_phy_sub", {})
                port_phy_sub["type"] = dict_val["type"]
                continue

            # MTU ............... [2022]
            match_obj = p11_5.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "port_phy_sub" not in ret_dict:
                    port_phy_sub = ret_dict.setdefault("port_phy_sub", {})
                port_phy_sub["mtu"] = int(dict_val["mtu"])
                continue

            # ac profile ........ [IFM_AC_PROFILE_DEFAULT]
            match_obj = p11_6.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "port_phy_sub" not in ret_dict:
                    port_phy_sub = ret_dict.setdefault("port_phy_sub", {})
                port_phy_sub["ac_profile"] = dict_val["ac_profile"]
                continue

            # Mac port oid................... [4444]
            match_obj = p12.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "port_sub" not in ret_dict:
                    port_sub = ret_dict.setdefault("port_sub", {})
                port_sub["mac_port_oid"] = int(dict_val["mac_port_oid"])
                continue

            # System port oid................ [4448]
            match_obj = p12_1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "port_sub" not in ret_dict:
                    port_sub = ret_dict.setdefault("port_sub", {})
                port_sub["system_port_oid"] = int(dict_val["system_port_oid"])
                continue

            # System port gid................ [223]
            match_obj = p12_2.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "port_sub" not in ret_dict:
                    port_sub = ret_dict.setdefault("port_sub", {})
                port_sub["system_port_gid"] = int(dict_val["system_port_gid"])
                continue

            # Ethernet port oid.............. [4459]
            match_obj = p12_3.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "port_sub" not in ret_dict:
                    port_sub = ret_dict.setdefault("port_sub", {})
                port_sub["ethernet_port_oid"] = int(dict_val["ethernet_port_oid"])
                continue

            # Voq oid........................ [4446]
            match_obj = p12_4.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "port_sub" not in ret_dict:
                    port_sub = ret_dict.setdefault("port_sub", {})
                port_sub["vog_oid"] = int(dict_val["vog_oid"])
                continue

            # Asic.............. [0]
            match_obj = p13.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "platform_sub" not in ret_dict:
                    platform_sub = ret_dict.setdefault("platform_sub", {})
                platform_sub["asic"] = int(dict_val["asic"])
                continue

            # Core.............. [5]
            match_obj = p13_1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "platform_sub" not in ret_dict:
                    platform_sub = ret_dict.setdefault("platform_sub", {})
                platform_sub["core"] = int(dict_val["core"])
                continue

            # Asic Port......... [0]
            match_obj = p13_2.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "platform_sub" not in ret_dict:
                    platform_sub = ret_dict.setdefault("platform_sub", {})
                platform_sub["asic_port"] = int(dict_val["asic_port"])
                continue

            # Asic Sub Port..... [65535]
            match_obj = p13_3.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "platform_sub" not in ret_dict:
                    platform_sub = ret_dict.setdefault("platform_sub", {})
                platform_sub["asic_sub_port"] = int(dict_val["asic_sub_port"])
                continue

            # Ifg Id............ [0]
            match_obj = p13_4.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "platform_sub" not in ret_dict:
                    platform_sub = ret_dict.setdefault("platform_sub", {})
                platform_sub["ifg_id"] = int(dict_val["ifg_id"])
                continue

            # Mac Num........... [211]
            match_obj = p13_5.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "platform_sub" not in ret_dict:
                    platform_sub = ret_dict.setdefault("platform_sub", {})
                platform_sub["mac_num"] = int(dict_val["mac_num"])
                continue

            # First Serdes...... [10]
            match_obj = p13_6.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "platform_sub" not in ret_dict:
                    platform_sub = ret_dict.setdefault("platform_sub", {})
                platform_sub["first_serdes"] = int(dict_val["first_serdes"])
                continue

            # Last Serdes....... [11]
            match_obj = p13_7.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "platform_sub" not in ret_dict:
                    platform_sub = ret_dict.setdefault("platform_sub", {})
                platform_sub["last_serdes"] = int(dict_val["last_serdes"])
                continue

            # FC Mode........... [0]
            match_obj = p13_8.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "platform_sub" not in ret_dict:
                    platform_sub = ret_dict.setdefault("platform_sub", {})
                platform_sub["fc_mode"] = int(dict_val["fc_mode"])
                continue

            # FEC Mode.......... [0]
            match_obj = p13_9.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "platform_sub" not in ret_dict:
                    platform_sub = ret_dict.setdefault("platform_sub", {})
                platform_sub["fec_mode"] = int(dict_val["fec_mode"])
                continue

            # Context Id........ [0]
            match_obj = p13_10.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "platform_sub" not in ret_dict:
                    platform_sub = ret_dict.setdefault("platform_sub", {})
                platform_sub["context_id"] = int(dict_val["context_id"])
                continue

            # L2 Port Mode ................ [port_mode_dynamic]
            match_obj = p14.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "port_l2_sub" not in ret_dict:
                    port_l2_sub = ret_dict.setdefault("port_l2_sub", {})
                port_l2_sub["port_mode"] = dict_val["port_mode"]
                continue

            # L2 Port Mode set............. [No]
            match_obj = p14_1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "port_l2_sub" not in ret_dict:
                    port_l2_sub = ret_dict.setdefault("port_l2_sub", {})
                port_l2_sub["port_mode_set"] = dict_val["port_mode_set"]
                continue

            # Default vlan ................ [0]
            match_obj = p14_2.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "port_l2_sub" not in ret_dict:
                    port_l2_sub = ret_dict.setdefault("port_l2_sub", {})
                port_l2_sub["vlan"] = int(dict_val["vlan"])
                continue

            # Ethertype.................... [8100]
            match_obj = p14_3.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "port_l2_sub" not in ret_dict:
                    port_l2_sub = ret_dict.setdefault("port_l2_sub", {})
                port_l2_sub["ethertype"] = int(dict_val["ethertype"])
                continue

            # untagged port bd vlan ....... [0]
            match_obj = p14_4.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "port_l2_sub" not in ret_dict:
                    port_l2_sub = ret_dict.setdefault("port_l2_sub", {})
                port_l2_sub["bd_vlan"] = int(dict_val["bd_vlan"])
                continue

            # status....................... [0]
            match_obj = p14_5.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "port_l2_sub" not in ret_dict:
                    port_l2_sub = ret_dict.setdefault("port_l2_sub", {})
                port_l2_sub["status"] = int(dict_val["status"])
                continue

            # ac profile .................. [IFM_AC_PROFILE_DEFAULT]
            match_obj = p14_6.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "port_l2_sub" not in ret_dict:
                    port_l2_sub = ret_dict.setdefault("port_l2_sub", {})
                port_l2_sub["ac_profile"] = dict_val["ac_profile"]
                continue

            # VRF ID .................. [0]
            match_obj = p15.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "port_l3_sub" not in ret_dict:
                    port_l3_sub = ret_dict.setdefault("port_l3_sub", {})
                port_l3_sub["vrf_id"] = int(dict_val["vrf_id"])
                continue

            # IPv4 Routing Enabled .... [Yes]
            match_obj = p15_1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "port_l3_sub" not in ret_dict:
                    port_l3_sub = ret_dict.setdefault("port_l3_sub", {})
                port_l3_sub["ipv4_routing"] = dict_val["ipv4_routing"]
                continue

            # IPv6 Routing Enabled .... [No]
            match_obj = p15_2.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "port_l3_sub" not in ret_dict:
                    port_l3_sub = ret_dict.setdefault("port_l3_sub", {})
                port_l3_sub["ipv6_routing"] = dict_val["ipv6_routing"]
                continue

            # MPLS Enabled ............ [No]
            match_obj = p15_3.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "port_l3_sub" not in ret_dict:
                    port_l3_sub = ret_dict.setdefault("port_l3_sub", {})
                port_l3_sub["mpls"] = dict_val["mpls"]
                continue

            # Pimv4 Enabled ........... [No]
            match_obj = p15_4.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "port_l3_sub" not in ret_dict:
                    port_l3_sub = ret_dict.setdefault("port_l3_sub", {})
                port_l3_sub["pimv4"] = dict_val["pimv4"]
                continue

            # Pimv6 Enabled ........... [No]
            match_obj = p15_5.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "port_l3_sub" not in ret_dict:
                    port_l3_sub = ret_dict.setdefault("port_l3_sub", {})
                port_l3_sub["pimv6"] = dict_val["pimv6"]
                continue

            # IPv4 MTU ................ [2018]
            match_obj = p15_6.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "port_l3_sub" not in ret_dict:
                    port_l3_sub = ret_dict.setdefault("port_l3_sub", {})
                port_l3_sub["ipv4_mtu"] = int(dict_val["ipv4_mtu"])
                continue

            # IPv6 MTU ................ [18]
            match_obj = p15_7.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "port_l3_sub" not in ret_dict:
                    port_l3_sub = ret_dict.setdefault("port_l3_sub", {})
                port_l3_sub["ipv6_mtu"] = int(dict_val["ipv6_mtu"])
                continue

            # L3 srv port gid ......... [4312]
            match_obj = p15_8.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "port_l3_sub" not in ret_dict:
                    port_l3_sub = ret_dict.setdefault("port_l3_sub", {})
                port_l3_sub["l3_srv"] = int(dict_val["l3_srv"])
                continue

            # L3 srv port oid ......... [5489]
            match_obj = p15_9.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if "port_l3_sub" not in ret_dict:
                    port_l3_sub = ret_dict.setdefault("port_l3_sub", {})
                port_l3_sub["l3_srv_oid"] = int(dict_val["l3_srv_oid"])
                continue

        return ret_dict


# ======================================================
# Parser for 'show platform software fed active vp summary interface if_id {interface_id} '
# ======================================================


class ShPlatformSoftwareFedActiveVpSummaryInterfaceIf_idSchema(MetaParser):
    """Schema for show platform software fed active vp summary interface if_id {interface_id}"""

    schema = {
        "interfaces": {
            Any(): {
                "if_id": str,
                "vlan_id": int,
                "pvln_mode": str,
                "pvlan": str,
                "stp_state": str,
                "vtp_pruned": str,
                "untag": str,
            },
        },
    }


class ShPlatformSoftwareFedActiveVpSummaryInterfaceIf_id(
    ShPlatformSoftwareFedActiveVpSummaryInterfaceIf_idSchema
):
    """Parser for show platform software fed active vp summary interface if_id {interface_id}"""

    cli_command = [
        "show platform software fed {mode} vp summary interface if_id {interface_id}",
        "show platform software fed {switch} {mode} vp summary interface if_id {interface_id}",
    ]

    def cli(self, interface_id, mode, switch=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[1].format(
                    interface_id=interface_id, mode=mode, switch=switch
                )
            else:
                cmd = self.cli_command[0].format(interface_id=interface_id, mode=mode)
            output = self.device.execute(cmd)

        #              102           80        trunk            1  forwarding          No                Yes
        p1 = re.compile(
            r"(?P<if_id>\d+)\s+(?P<vlan_id>\d+)\s+(?P<pvln_mode>\w+)\s+(?P<pvlan>\d+)\s+(?P<stp_state>\w+)\s+(?P<vtp_pruned>\w+)\s+(?P<untag>\w+)$"
        )

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            #              102           80        trunk            1  forwarding          No                Yes
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                vlan_id_var = dict_val["vlan_id"]
                interfaces = ret_dict.setdefault("interfaces", {})
                vlan_id_dict = ret_dict["interfaces"].setdefault(vlan_id_var, {})
                vlan_id_dict["if_id"] = dict_val["if_id"]
                vlan_id_dict["vlan_id"] = int(dict_val["vlan_id"])
                vlan_id_dict["pvln_mode"] = dict_val["pvln_mode"]
                vlan_id_dict["pvlan"] = dict_val["pvlan"]
                vlan_id_dict["stp_state"] = dict_val["stp_state"]
                vlan_id_dict["vtp_pruned"] = dict_val["vtp_pruned"]
                vlan_id_dict["untag"] = dict_val["untag"]
                continue

        return ret_dict


# ============================================================
#  Schema for 'show platform software fed active fnf record-count asic <asic num>'
# ============================================================
class ShowPlatformFedSwitchActiveFnfRecordCountAsicNumSchema(MetaParser):
    """Schema for show platform software fed active fnf record-count asic <asic num>
    show platform software fed switch active fnf record-count asic <asic num>"""

    schema = {
        "current_flow_count": int,
        "total_flows_learned": int,
        "hash_searched_flow_count": int,
        "overflow_searched_flow_count": int,
        "hash_unsearched_flow_count": int,
        "overflow_unsearched_flow_count": int,
        "total_flow_searched": int,
        "total_search_failures": int,
        "total_avc_cpu_copy_disable": int,
        "total_eta_cpu_copy_disable": int,
        "total_cpu_copy_disable": int,
        "total_avc_feature_flows": int,
        "total_eta_feature_flows": int,
        "total_eta_and_avc_feature_flows": int,
        "total_num_eta_flows_agedout": int,
        Optional("reflexive_claimed_flow"): int,
        Optional("reflexive_claimed_flow_deleted"): int,
        Optional("reflexive_stale_flow_aged_out"): int,
        Optional("reflexive_flow_deleted"): int,
        "total_flows_deleted": int,
        "total_delete_failures": int,
        "total_flow_aged_out": int,
        "total_stale_flow_deleted": int,
        "total_stale_flow_del_aborted": int,
        "total_packets_aged_out": int,
        "total_bytes_aged_out": int,
    }


# ============================================================================
#  Parser for
#  * 'show platform software fed active fnf record-count asic <asic num>'
#  * 'show platform software fed switch active fnf record-count asic <asic num>'
# ============================================================================
class ShowPlatformFedSwitchActiveFnfRecordCountAsicNum(
    ShowPlatformFedSwitchActiveFnfRecordCountAsicNumSchema
):
    """
    Parser for
    * 'show platform software fed active fnf record-count asic {asic_num}'
    * 'show platform software fed switch {state} fnf record-count asic {asic_num}'
    """

    cli_command = [
        "show platform hardware fed {state} fnf record-count asic {asic_num}",
        "show platform hardware fed {switch} {state} fnf record-count asic {asic_num}",
    ]

    def cli(self, asic_num, state, switch=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[1].format(
                    state=state, switch=switch, asic_num=asic_num
                )
            else:
                cmd = self.cli_command[0].format(state=state, asic_num=asic_num)
            output = self.device.execute(cmd)

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r"^(?P<pattern>[\w\s]+)= +(?P<value>\d+)$")

        # Current flow count               = 0
        # Total flows learned              = 0
        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                scrubbed = (group["pattern"].strip()).replace(" ", "_")
                ret_dict.update({scrubbed.lower(): int(group["value"])})
                continue

        return ret_dict


