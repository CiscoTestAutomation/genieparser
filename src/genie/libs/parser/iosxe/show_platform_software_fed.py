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
    * 'show platform software fed active fnf record-count asic {asic_num}'
    * 'show platform software fed switch {state} fnf record-count asic {asic_num}'
    * 'show platform software fed switch {type} ip ecr exact-route {sourceip} {destinationip} {sourceport} {destinationport} {protocol}'
    * 'show platform software fed switch active ip urpf'
    * 'show platform software fed active ip urpf'
    * 'show platform software fed switch {switch} ifm mappings gid {gid_num}'
    * 'show platform software fed switch {switch} ifm mappings {ifm_type}'
    * 'show platform software fed {mode} port if_id {if_id}'
    * 'show platform software fed {switch} {mode} port if_id {if_id}'
    * 'show platform software fed active ifm interface_name tunnel5'
    * 'show platform software fed switch active oifset urid <id>'
    * 'show platform software fed switch active oifset urid <id> detail'
    * 'show platform software fed switch active ifm interfaces virtualportgroup'
    * 'show platform software fed active ifm interfaces virtualportgroup'
    * 'show platform software fed switch {mode} ifm interfaces ethernet'
    * 'show platform software fed active ifm interfaces ethernet'
    * 'show platform software fed switch active ifm interfaces loopback'
    * 'show platform software fed active ifm interfaces loopback'
    * 'show platform software fed switch <switch> wdavc function wdavc_ft_show_all_flows_seg_ui' 
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
class ShowPlatformSoftwareFedSwitchActiveIfmInterfacesLabel(ShowPlatformSoftwareFedSwitchActiveIfmInterfacesLabelSchema):
    """
    Parser for :
        * 'show platform software fed {switch} active ifm interfaces {label}'
        * 'show platform software fed active ifm interfaces {label}'
    """

    cli_command = [
        "show platform software fed switch active ifm interfaces lisp",
        "show platform software fed active ifm interfaces lisp",
        "show platform software fed switch active ifm interfaces sw-subif",
        "show platform software fed active ifm interfaces sw-subif",
        "show platform software fed switch active ifm interfaces virtualportgroup",
        "show platform software fed active ifm interfaces virtualportgroup",
        "show platform software fed switch {mode} ifm interfaces ethernet",
        "show platform software fed active ifm interfaces ethernet",
        "show platform software fed switch active ifm interfaces loopback",
        "show platform software fed active ifm interfaces loopback"
    ]

    def cli(self, command=None, output=None, **kwargs):
        if output is None:
            output = self.device.execute(command)

        # initial return dictionary
        ret_dict = {}

        # LISP0.4103                        0x0000054d          Ready
        # LISP0                             0x0000054c          Ready
        # Loopback999999                    0x00000006          Ready
        # Null0                             0x00000400          Ready
        p1 = re.compile(r'^(?P<interface_name>\S+)(?:\s*)(?P<if_id>0x\w+)(?:\s*)(?P<state>\w+)$')

        for line in output.splitlines():
            line = line.strip()

            # LISP0.4103                        0x0000054d          Ready
            # LISP0                             0x0000054c          Ready
            # Loopback999999                    0x00000006          Ready
            # Null0                             0x00000400          Ready
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface_name = group["interface_name"]
                sub_dict = ret_dict.setdefault("interface_name", {}).setdefault(interface_name, {})
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
        "show platform software fed {mode} ifm mappings lpn",
        "show platform software fed {switch} {mode} ifm mappings lpn",
        "show platform software fed {switch} {mode} ifm mappings lpn | include {interface}",
    ]

    def cli(self, mode='active', switch=None, interface="", output=None):
        if output is None:
            if switch and interface:
                cmd = self.cli_command[2].format(switch=switch, mode=mode, interface=interface)
            elif switch:
                cmd = self.cli_command[1].format(switch=switch, mode=mode)
            else:
                cmd = self.cli_command[0].format(mode=mode)

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

    cli_command = ["show platform software fed switch {mode} port summary", 
                   "show platform software fed {mode} port summary"]

    def cli(self, command=None, output=None, **kwargs):
        if output is None:
            # excute command to get output
            output = self.device.execute(command)

        # initial variables
        ret_dict = {}

        # 1266           HundredGigE2/0/27/1             true
        p1 = re.compile(r"^(?P<if_id>\d+)\s+(?P<if_name>\S+)\s+(?P<port_enable>\w+)$")

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
        Optional("vlan"): int,
        Optional("snooping_handle"): str,
        Optional("handle_value"): str,
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
        p3 = re.compile(r"^(?P<port>[\w\-\/]+)\s+(?P<mode>\S+)$")

        # Value of Snooping DI handle is:: 0x5C4
        p4 = re.compile(r"^Value\s+of\s+Snooping\s+DI\s+handle\s+is::\s+(?P<handle_value>\S+)$")

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

            # Value of Snooping DI handle is:: 0x5C4
            m1 = p4.match(line)
            if m1:
                group = m1.groupdict()
                ret_dict["handle_value"] = group["handle_value"]
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
                Optional("protocol"): str,
                Optional("secondary_vlan"): str,
                Optional("vlan_urid"): str,
                Optional("d_users_count"): str,
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

        # (ipv4, vlan: 3000)
        p0_1 = re.compile(r'\(+(?P<protocol>\S+)+\,+\s+vlan\: +(?P<vlan>\d+)+\)')

        # IGMPSN Enabled : On
        p1 = re.compile(r"^IGMPSN\s+Enabled\s+:\s+(?P<igmp_en>[\s\w\s]+)$")

        # Snoop State     : ON
        p1_1 = re.compile(r"^Snoop\s+State\s+:\s+(?P<snoop_state>[\w\s]+)$")

        # Snoop State     : ON
        p1_1 = re.compile(r"^Snoop\s+State\s+:\s+(?P<snoop_state>[\w\s]+)$")

        # PIMSN Enabled : Off
        p2 = re.compile(r"^PIMSN\s+Enabled\s+:\s+(?P<pimsn_en>[\s\w\s]+)$")

        # Flood Mode : Off
        p3 = re.compile(r"^Flood\s+Mode\s+:\s+(?P<flood_md>[\s\w\s]+)$")

        # Oper State : Up
        p4 = re.compile(r"^Oper\s+State\s+:\s+(?P<op_state>[\s\w\s]+)$")

        # STP TCN Flood : Off
        # STP TCN State : Off
        p5 = re.compile(
            r"^STP\s+TCN\s+(Flood|State)\s+:\s+(?P<stp_tcn_flood>[\s\w\s]+)$"
        )
        # STP TCN State : Off
        p5 = re.compile(
            r"^STP\s+TCN\s+(Flood|State)\s+:\s+(?P<stp_tcn_flood>[\s\w\s]+)$"
        )

        # Routing Enabled : On
        p6 = re.compile(r"^Routing\s+Enabled\s+:\s+(?P<route_en>[\s\w\s]+)$")

        # PIM Enabled : On
        p7 = re.compile(r"^PIM\s+Enabled\s+:\s+(?P<pim_en>[\s\w\s]+)$")

        # Pim state               : ON
        p7_1 = re.compile(r'^Pim\s+state\s+:\s+(?P<pim_en>[\s\w\s]+)$')

        # PVLAN : No
        p8 = re.compile(r"^PVLAN\s+:\s+(?P<pvlan>[\s\w\s]+)$")

        # In Retry : 0x0
        p9 = re.compile(r"^In\s+Retry\s+:\s+(?P<in_retry>[\s\w\s]+)$")

        # CCK Epoch : 0x17
        p10 = re.compile(r"^CCK\s+Epoch\s+:\s+(?P<cck_ep>[\s\w\s]+)$")

        # IOSD Flood Mode : Off
        p11 = re.compile(r"^IOSD\s+Flood\s+Mode\s+:\s+(?P<iosd_md>[\s\w\s]+)$")

        # IOS Flood Mode          : OFF
        p11_1 = re.compile(r'^IOS\s+Flood\s+Mode\s+:\s+(?P<iosd_md>[\s\w\s]+)$')

        # EVPN Proxy Enabled : On
        p12 = re.compile(r"^EVPN\s+Proxy\s+Enabled\s+:\s+(?P<evpn_en>[\s\w\s]+)$")

        # Evpn Proxy              : OFF
        p12_1 = re.compile(r'^Evpn\s+Proxy\s+:\s+(?P<evpn_en>[\s\w\s]+)$')

        # L3mcast Adj :
        p13 = re.compile(r"L3mcast\s+Adj\s+:(?P<l3m_adj>.*)")

        # Mrouter PortQ :
        p14 = re.compile(r"^Mrouter\s+[P|p]ort[Q|s]\s+:\s*")
        # nve1.VNI60020(0x200000071)
        p14_1 = re.compile(r"([A-Za-z]*\d[-().]*){10,}")

        # port:Port-channel10 (ec_member:HundredGigE1/0/5) (group_oif:0) (mrouter_flag:1)
        # port:Port-channel10 (ec_member:HundredGigE1/0/5) (group_oif:0) (mrouter_flag:1)
        # port:Port-channel100 (ec_member:HundredGigE2/5/0/2)
        # port:Port-channel0 (ec_member:HundredGigE1/0/5) (group_oif:0)
        # port:Port-channel77
        p14_2 = re.compile(r"^port:(?P<port>[\w\-\.]+)(\s+(?P<left>.*))?$")

        # Port-channel10 (Port:HundredGigE1/0/5)
        p14_3 = re.compile(r"^(?P<port>[\w\-\.]+)\s+\((Port:(?P<left>.*))?$")

        # Flood PortQ :
        p15 = re.compile(r"^Flood [P|p]ort[Q|s]\s+:\s*")
        # TenGigabitEthernet7/0/13
        # FiveGigabitEthernet1/0/2
        # GigabitEthernet2/0/31
        p15_1 = re.compile(r"^[A-Za-z-]+[\d\/\.]+$")

        # REP RI handle : 0x0
        p16 = re.compile(r"^REP\s+RI\s+handle\s+:\s+(?P<rep_han>[\s\w\s]+)$")

        # Secondary Vlan          : NO
        p17 = re.compile(r'^Secondary\s+Vlan\s+:\s+(?P<secondary_vlan>[\s\w\s]+)$')

        # Vlan Urid               : 0x5000000000000008
        p18 = re.compile(r'^Vlan\s+Urid\s+:\s+(?P<vlan_urid>[\s\w\s]+)$')

        # Dependant users count   : 0
        p19 = re.compile(r'^Dependant\s+users\s+count\s+:\s+(?P<d_users_count>[\s\w\s]+)$')

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

            # (ipv4, vlan: 3000)
            m = p0_1.match(line)
            if m:
                vlan = int(m.groupdict()['vlan'])
                mac_dict = platform_dict.setdefault('vlan', {}).setdefault(vlan, {})
                mac_dict['protocol'] = m.groupdict()['protocol']

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

            # Pim state               : ON
            m = p7_1.match(line)
            if m:
                mac_dict['pim_en'] = m.groupdict()['pim_en']
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

            # IOS Flood Mode          : OFF
            m = p11_1.match(line)
            if m:
                mac_dict['iosd_md'] = m.groupdict()['iosd_md']
                continue

            # EVPN Proxy Enabled : On
            m = p12.match(line)
            if m:
                mac_dict["evpn_en"] = m.groupdict()["evpn_en"]
                continue

            # Evpn Proxy              : OFF
            m = p12_1.match(line)
            if m:
                mac_dict['evpn_en'] = m.groupdict()['evpn_en']
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

            # Port-channel10 (Port:HundredGigE1/0/5)
            m = p14_3.match(line)
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

            # Secondary Vlan          : NO
            m = p17.match(line)
            if m:
                mac_dict['secondary_vlan'] = m.groupdict()['secondary_vlan']
                continue

            # Vlan Urid               : 0x5000000000000008
            m = p18.match(line)
            if m:
                mac_dict['vlan_urid'] = m.groupdict()['vlan_urid']
                continue

            # Dependant users count   : 0
            m = p19.match(line)
            if m:
                mac_dict['d_users_count'] = m.groupdict()['d_users_count']
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
                Optional("d_users_count"): str,
                Optional("group_urid"): str,
            }
        }
    }


class ShowPlatformSoftwareFedIgmpSnoopingGroups(
    ShowPlatformSoftwareFedIgmpSnoopingGroupsSchema
):
    """Parser for show Platform Software Fed ip igmp snooping groups vlan"""

    cli_command = [
        "show platform software fed {switch_var} {state} ip igmp snooping groups vlan {vlan}",
        "show platform software fed {state} ip igmp snooping groups vlan {vlan}",
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

        # Vlan:20 Group:229.1.1.1
        # ---------------------------------
        # Member ports :
        # TenGigabitEthernet7/0/13
        # nve1.VNI60020(0x200000062)

        # Vlan:20 Group:229.1.1.1
        p0 = re.compile(r"(^Vlan+:+(?P<vlan>\d+))+\s+(Group:+(?P<group>\w.*))")

        # (Vlan: 13, 225.0.0.1)
        p0_1 = re.compile(r'\(+(Vlan\:+\s+(?P<vlan>\d+))+\,+\s+(?P<group>\S+)+\)')

        # Member ports :
        p1 = re.compile(r"(^Member +ports   :(?P<mem_port>.*))")

        # TenGigabitEthernet7/0/13
        p1_1 = re.compile(r"([A-Za-z]*\d[-().]*){10,}")

        # nve1.VNI60020(0x200000062)
        p1_2 = re.compile(r"^[A-Za-z]+[\d\/]+$")

        # Member ports            : 1
        p1_3 = re.compile(r"(^Member+\s+ports+\s+:+(?P<mem_port>.*))")

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

        # Dependent Users Count   : 0
        p8 = re.compile(r'^Dependent\s+Users\s+Count\s+:\s+(?P<d_users_count>[\s\w\s]+)$')

        # Group Urid              : 0x600000000000000d
        p9 = re.compile(r'^Group\s+Urid\s+:\s+(?P<group_urid>[\s\w\s]+)$')

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

            # (Vlan: 13, 225.0.0.1)
            m = p0_1.match(line)
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
                    continue

            # nve1.VNI60020(0x200000062)
            m = p1_2.match(line)
            if m:
                if member_port_flag == 1:
                    member_list.append(m.group(0))
                    continue

            # Member ports :
            m = p1_3.match(line)
            if m:
                mac_dict["mem_port"] = member_list
                member_port_flag = 1
                continue

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

            # Dependent Users Count   : 0
            m = p8.match(line)
            if m:
                mac_dict["d_users_count"] = m.groupdict()["d_users_count"]
                continue

            # Group Urid              : 0x600000000000000d
            m = p9.match(line)
            if m:
                mac_dict["group_urid"] = m.groupdict()["group_urid"]
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
        #   V_SISF                  IPV6            Ingress         sisf v6acl 0001DF9F     9
        p2 = re.compile(
            r"^(?P<feature_type>\S+)\s+(?P<acl_type>\S+)\s+(?P<direction>\S+)\s+(?P<name>.+?)\s+(?P<entries_used>\d+)$"
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
    ShowPlatformSoftwareFedSwitchActiveVtAllSchema):
    """Parser for show platform software fed switch active vt all"""

    cli_command = [
        "show platform software fed switch {switch} vt all",
        "show platform software fed active vt all",
    ]

    def cli(self, output=None, switch=""):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(switch=switch)
            else:
                cmd = self.cli_command[1]

            output = self.device.execute(cmd)

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
            Optional("intf_admin_mode"): str,
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
        Optional("interface_details"): {
            Optional("port_type"): str,
            Optional("port_location"): str,
            Optional("slot"): int,
            Optional("slot_unit"): int,
            Optional("unit"): int,
            Optional("snmp_index"): int,
            Optional("gpn"): int,
            Optional("ec_channel"): int,
            Optional("ec_index"): int,
            Optional("ipv4_mtu"): int,
            Optional("ipv6_mtu"): int,
            Optional("ipv4_vrf_id"): int,
            Optional("ipv6_vrf_id"): int,
            Optional("protocol_flags"): str,
            Optional("misc_flags"): str,
            Optional("icmpv4_flags"): str,
            Optional("icmpv6_flags"): str,
            Optional("mac_address"): str,
            Optional("qos_trust_type"): str,
        },
        Optional("port_phy_sub"): {
            Optional("affinity"): str,
            Optional("lpn"): int,
            Optional("gpn"): int,
            Optional("speed"): str,
            Optional("type"): str,
            Optional("mtu"): int,
            Optional("ac_profile"): str,
        },
        Optional("port_sub"): {
            Optional("mac_port_oid"): str,
            Optional("system_port_oid"): str,
            Optional("system_port_gid"): int,
            Optional("ethernet_port_oid"): str,
            Optional("port_sub_block_port_mode"): str,
            Optional("dense_mode_service_port_gid"): str,
            Optional("dense_mode_service_port_oid"): str,
            Optional("dense_mode_port_vid"): str,
            Optional("vog_oid"): str,
        },
        Optional("platform_sub"): {
            Optional("core"): int,
            Optional("asic_port"): int,
            Optional("mac_num"): int,
            Optional("asic"): int,
            Optional("asic_sub_port"): int,
            Optional("ifg_id"): int,
            Optional("first_serdes"): int,
            Optional("last_serdes"): int,
            Optional("fc_mode"): int,
            Optional("fec_mode"): int,
            Optional("context_id"): int,
        },
        Optional("port_l2_sub"): {
            Optional("port_mode"): str,
            Optional("port_mode_set"): str,
            Optional("vlan"): int,
            Optional("ethertype"): int,
            Optional("native_vlan_tagging"): str,
            Optional("bd_vlan"): int,
            Optional("status"): int,
            Optional("ac_profile"): str,

            Optional("l2_sub_block_port_vlan"): {
                Optional("l2_sub_block_port_vlan"): int,
                Optional("native_vlan_trunk"): int,
                Optional("untagged_port_bd_vlan"): int,
                Optional("default_vlan"): int,
            },
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
            Optional("cts_if_id"): str,
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

    cli_command = ["show platform software fed {state} ifm if-id {if_id}", 
                   "show platform software fed switch {state} ifm if-id {if_id}",
                   "show platform software fed switch {switch_number} ifm if-id {if_id}"]

    def cli(self, command=None, output=None, if_id = "", switch_number="", **kwargs):
        if output is None:
            output = self.device.execute(command)

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

        # Interface Admin mode : Admin Up
        p1_4_1 = re.compile(
            r"^Interface\s+Admin\s+mode\s+:\s+(?P<intf_admin_mode>\S+\s+\S+)$"
        )
        # Interface Status        : NPD
        p1_5 = re.compile(r"^Interface\s+Status\s+:\s+(?P<status>.*)$")
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
        # Port Type : ROUTE PORT
        p9_1 = re.compile(r"^Port Type+\s+:\s+(?P<port_type>.*)$")

        # Port Location : LOCAL
        p9_2 = re.compile(r"^Port Location+\s+:\s+(?P<port_location>.*)$")

        # Slot : 13
        p9_3 = re.compile(r"^Slot\s+:\s+(?P<slot>\d+)$")

        # Unit : 0
        p9_4 = re.compile(r"^Unit\s+:\s+(?P<unit>\d+)$")

        # Slot Unit : 19
        p9_5 = re.compile(r"^Slot\s+Unit\s+:\s+(?P<slot_unit>\d+)$")

        # SNMP IF Index : 119
        p9_6 = re.compile(r"^SNMP\s+IF\s+Index\s+:\s+(?P<snmp_index>\d+)$")

        # GPN : 979
        p9_7 = re.compile(r"^GPN\s+:\s+(?P<gpn>\d+)$")

        # EC Channel : 0
        p9_8 = re.compile(r"^EC\s+Channel\s+:\s+(?P<ec_channel>\d+)$")

        # EC Index : 0
        p9_9 = re.compile(r"^EC\s+Index\s+:\s+(?P<ec_index>\d+)$")

        # IPv4 MTU : 2000
        p9_10 = re.compile(r"^IPv4\s+MTU\s+:\s+(?P<ipv4_mtu>\d+)$")

        # IPv6 MTU : 0
        p9_11 = re.compile(r"^IPv6\s+MTU\s+:\s+(?P<ipv6_mtu>\d+)$")

        # IPv4 VRF ID : 0
        p9_12 = re.compile(r"^IPv4\s+VRF\s+ID\s+:\s+(?P<ipv4_vrf_id>\d+)$")

        # IPv6 VRF ID : 65535
        p9_13 = re.compile(r"^IPv6\s+VRF\s+ID\s+:\s+(?P<ipv6_vrf_id>\d+)$")

        # Protocol flags : 0x0003 [ ipv4 ipv6 ]
        p9_14 = re.compile(
            r"^Protocol\s+flags\s+:\s+(?P<protocol_flags>\S+\s+\S+\s+\S+\s+\S+\s+\S+)$"
        )

        # Misc flags : 0x0041 [ ipv4 --- ]
        p9_15 = re.compile(
            r"^Misc\s+flags\s+:\s+(?P<misc_flags>\S+\s+\S+\s+\S+\s+\S+\s+\S+)$"
        )

        # ICMPv4 flags : 0x03 [ unreachable redirect ]
        p9_16 = re.compile(
            r"^ICMPv4\s+flags\s+:\s+(?P<icmpv4_flags>\S+\s+\S+\s+\S+\s+\S+\s+\S+)$"
        )

        # ICMPv6 flags : 0x03 [ unreachable redirect ]
        p9_17 = re.compile(
            r"^ICMPv6\s+flags\s+:\s+(?P<icmpv6_flags>\S+\s+\S+\s+\S+\s+\S+\s+\S+)$"
        )

        # Mac Address : 6c:b2:ae:4a:54:c5
        p9_18 = re.compile(r"^Mac\s+Address\s+:\s+(?P<mac_address>\S+)$")

        # QoS Trust Type : 3 (DSCP)
        p9_19 = re.compile(
            r"^QoS\s+Trust\s+Type\s+:\s+(?P<qos_trust_type>\S+\s+\S+)$"
        )

        # Affinity .......... [local]
        p11 = re.compile(
            r"^Affinity\s+\.+\s+\[(?P<affinity>\w+)\]$"
        )

        # LPN ............... [19]
        p11_1 = re.compile(
            r"^LPN\s+\.+\s+\[(?P<lpn>\d+)\]$"
        )

        # GPN ............... [979]
        p11_2 = re.compile(
            r"^GPN\s+\.+\s+\[(?P<gpn>\d+)\]$"
        )

        # Speed ............. [40GB]
        p11_3 = re.compile(
            r"^Speed\s+\.+\s+\[(?P<speed>\S+)\]$"
        )

        # type .............. [IFM_PORT_TYPE_L3]
        p11_4 = re.compile(
            r"^type\s+\.+\s+\[(?P<type>\S+)\]$"
        )

        # MTU ............... [2022]
        p11_5 = re.compile(
            r"^MTU\s+\.+\s+\[(?P<mtu>\d+)\]$"
        )

        # ac profile ........ [IFM_AC_PROFILE_DEFAULT]
        p11_6 = re.compile(
            r"^ac\s+profile\s+\.{8}\s+\[(?P<ac_profile>\S+)\]$"
        )

        # Mac port oid................... [4444]
        p12 = re.compile(
            r"^Mac port oid\S+\s+\[(?P<mac_port_oid>\S+)\]$"
        )

        # System port oid................ [4448]
        p12_1 = re.compile(
            r"^System\s+port\s+oid\.+\s+\[(?P<system_port_oid>\S+)\]$"
        )

        # System port gid................ [223]
        p12_2 = re.compile(
            r"^System\s+port\s+gid\.+\s+\[(?P<system_port_gid>\d+)\]$"
        )

        # Ethernet port oid.............. [4459]
        p12_3 = re.compile(
            r"^Ethernet\s+port\s+oid\.+\s+\[(?P<ethernet_port_oid>\S+)\]$"
        )

        # Port mode...................... [Dense Mode] 
        p12_3_1 = re.compile(
            r"^Port mode\S+\s+\[(?P<port_sub_block_port_mode>.*)\]$"
        )

        # Dense mode service port gid.... [122994] 
        p12_3_2 = re.compile(
            r"^Dense mode service port gid....\s+\[(?P<dense_mode_service_port_gid>\S+)\]$"
        )

        # Dense mode service port oid.... [0xa0b(2571)] 
        p12_3_3 = re.compile(
            r"^Dense mode service port oid\S+\s+\[(?P<dense_mode_service_port_oid>\S+)\]$"
        )

        # Dense mode port vid............ [50] 
        p12_3_4 = re.compile(
            r"^Dense mode port vid\S+\s+\[(?P<dense_mode_port_vid>\d+)\]$"
        )

        # Voq oid........................ [4446]
        p12_4 = re.compile(
            r"^Voq\s+oid\.+\s+\[(?P<vog_oid>\S+)\]$"
        )

        # Asic.............. [0]
        p13 = re.compile(r"^Asic\.+\s+\[(?P<asic>\d+)\]$")

        # Core.............. [5]
        p13_1 = re.compile(r"^Core\.+\s+\[(?P<core>\d+)\]$")

        # Asic Port......... [0]
        p13_2 = re.compile(
            r"^Asic\s+Port\.+\s+\[(?P<asic_port>\d+)\]$"
        )

        # Asic Sub Port..... [65535]
        p13_3 = re.compile(
            r"^Asic\s+Sub\s+Port\.+\s+\[(?P<asic_sub_port>\d+)\]$"
        )

        # Ifg Id............ [0]
        p13_4 = re.compile(
            r"^Ifg\s+Id\.+\s+\[(?P<ifg_id>\d+)\]$"
        )

        # Mac Num........... [211]
        p13_5 = re.compile(
            r"^Mac\s+Num\.+\s+\[(?P<mac_num>\d+)\]$"
        )

        # First Serdes...... [10]
        p13_6 = re.compile(
            r"^First\s+Serdes\.+\s+\[(?P<first_serdes>\d+)\]$"
        )

        # Last Serdes....... [11]
        p13_7 = re.compile(
            r"^Last\s+Serdes\.+\s+\[(?P<last_serdes>\d+)\]$"
        )

        # FC Mode........... [0]
        p13_8 = re.compile(
            r"^FC\s+Mode\.+\s+\[(?P<fc_mode>\d+)\]$"
        )

        # FEC Mode.......... [0]
        p13_9 = re.compile(
            r"^FEC\s+Mode\.+\s+\[(?P<fec_mode>\d+)\]$"
        )

        # Context Id........ [0]
        p13_10 = re.compile(
            r"^Context\s+Id\.+\s+\[(?P<context_id>\d+)\]$"
        )

        # L2 Port Mode ................ [port_mode_dynamic]
        p14 = re.compile(
            r"^L2\s+Port\s+Mode\s+\.+\s+\[(?P<port_mode>\S+)\]$"
        )

        # L2 Port Mode set............. [No]
        p14_1 = re.compile(
            r"^L2\s+Port\s+Mode\s+set\.+\s+\[(?P<port_mode_set>\w+)\]$"
        )

        # Default vlan ................ [0]
        p14_2 = re.compile(
            r"^Default\s+vlan\s+\.+\s+\[(?P<vlan>\d+)\]$"
        )

        # Ethertype.................... [8100]
        p14_3 = re.compile(
            r"^Ethertype\.+\s+\[(?P<ethertype>\d+)\]$"
        )

        # Port vlan  .................. [50] 
        p14_3_1 = re.compile(
            r"^Port vlan\s+\S+\s+\[(?P<l2_sub_block_port_vlan>\d+)\]$"
        )

        # Native vlan (trunk) .............. [0] 
        p14_3_2 = re.compile(
            r"^Native vlan \(trunk\)\s+\.+\s+\[(?P<native_vlan_trunk>\d+)\]$"
        )

        # Untagged port bd vlan (access) ... [50]
        p14_3_3 = re.compile(
            r"^Untagged port bd vlan \(access\)\s+\.+\s+\[(?P<untagged_port_bd_vlan>\d+)\]$"
        )

        # Default vlan (dot1q tunnel) ...... [0] 
        p14_3_4 = re.compile(
            r"^Default vlan \(dot1q tunnel\)\s+\.+\s+\[(?P<default_vlan>\d+)\]$"
        )

        # Native Vlan Tagging.......... [Native Vlan None]
        p14_3_5 = re.compile(
            r"^Native Vlan Tagging\S+\s+\[(?P<native_vlan_tagging>.*)\]$"
        )

        # untagged port bd vlan ....... [0]
        p14_4 = re.compile(
            r"^untagged\s+port\s+bd\s+vlan\s+\.+\s+\[(?P<bd_vlan>\d+)\]$"
        )

        # status....................... [0]
        p14_5 = re.compile(
            r"^status\.+\s+\[(?P<status>\d+)\]$"
        )

        # ac profile .................. [IFM_AC_PROFILE_DEFAULT]
        p14_6 = re.compile(
            r"^ac\s+profile\s+\.{18}\s+\[(?P<ac_profile>\S+)\]$"
        )
        # Port CTS Subblock is NULL if_id = 0x14c3c6db 

        p19 = re.compile(
            r"^Port CTS Subblock is NULL if_id\s+=\s+(?P<cts_if_id>\S+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            # Interface Name          : C320150491
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                int_info = ret_dict.setdefault("int_info", {})
                int_info["name"] = dict_val["name"]
                continue

            # Interface IF_ID         : 0x0000000013151bdb
            m = p1_1.match(line)
            if m:
                dict_val = m.groupdict()
                int_info = ret_dict.setdefault("int_info", {})
                int_info["if_id"] = dict_val["if_id"]
                continue

            # Interface Block Pointer : 0x7f16cd385568
            m = p1_2.match(line)
            if m:
                dict_val = m.groupdict()
                int_info = ret_dict.setdefault("int_info", {})
                int_info["blk_ptr"] = dict_val["blk_ptr"]
                continue

            # Interface Block State   : READY
            m = p1_3.match(line)
            if m:
                dict_val = m.groupdict()
                int_info = ret_dict.setdefault("int_info", {})
                int_info["blk_state"] = dict_val["blk_state"]
                continue

            # Interface State         : Enabled
            m = p1_4.match(line)
            if m:
                dict_val = m.groupdict()
                int_info = ret_dict.setdefault("int_info", {})
                int_info["state"] = dict_val["state"]
                continue

            # Interface Admin mode : Admin Up
            m = p1_4_1.match(line)
            if m:
                dict_val = m.groupdict()
                int_info = ret_dict.setdefault("int_info", {})
                int_info["intf_admin_mode"] = dict_val["intf_admin_mode"]
                continue

            # Interface Status        : ADD, UPD
            m = p1_5.match(line)
            if m:
                dict_val = m.groupdict()
                int_info = ret_dict.setdefault("int_info", {})
                int_info["status"] = dict_val["status"]
                continue

            # Port Type : ROUTE PORT
            m = p9_1.match(line)
            if m:
                dict_val = m.groupdict()
                interface_details = ret_dict.setdefault("interface_details", {})
                interface_details["port_type"] = dict_val["port_type"]
                continue

            # Port Location : LOCAL
            m = p9_2.match(line)
            if m:
                dict_val = m.groupdict()
                interface_details = ret_dict.setdefault("interface_details", {})
                interface_details["port_location"] = dict_val["port_location"]
                continue

            # Slot : 13
            m = p9_3.match(line)
            if m:
                dict_val = m.groupdict()
                interface_details = ret_dict.setdefault("interface_details", {})
                interface_details["slot"] = int(dict_val["slot"])
                continue

            # Unit : 0
            m = p9_4.match(line)
            if m:
                dict_val = m.groupdict()
                interface_details = ret_dict.setdefault("interface_details", {})
                interface_details["unit"] = int(dict_val["unit"])
                continue

            # Slot Unit : 19
            m = p9_5.match(line)
            if m:
                dict_val = m.groupdict()
                interface_details = ret_dict.setdefault("interface_details", {})
                interface_details["slot_unit"] = int(dict_val["slot_unit"])
                continue

            # SNMP IF Index : 119
            m = p9_6.match(line)
            if m:
                dict_val = m.groupdict()
                interface_details = ret_dict.setdefault("interface_details", {})
                interface_details["snmp_index"] = int(dict_val["snmp_index"])
                continue

            # GPN : 979
            m = p9_7.match(line)
            if m:
                dict_val = m.groupdict()
                interface_details = ret_dict.setdefault("interface_details", {})
                interface_details["gpn"] = int(dict_val["gpn"])
                continue

            # EC Channel : 0
            m = p9_8.match(line)
            if m:
                dict_val = m.groupdict()
                interface_details = ret_dict.setdefault("interface_details", {})
                interface_details["ec_channel"] = int(dict_val["ec_channel"])
                continue

            # EC Index : 0
            m = p9_9.match(line)
            if m:
                dict_val = m.groupdict()
                interface_details = ret_dict.setdefault("interface_details", {})
                interface_details["ec_index"] = int(dict_val["ec_index"])
                continue

            # IPv4 MTU : 2000
            m = p9_10.match(line)
            if m:
                dict_val = m.groupdict()
                interface_details = ret_dict.setdefault("interface_details", {})
                interface_details["ipv4_mtu"] = int(dict_val["ipv4_mtu"])
                continue

            # IPv6 MTU : 0
            m = p9_11.match(line)
            if m:
                dict_val = m.groupdict()
                interface_details = ret_dict.setdefault("interface_details", {})
                interface_details["ipv6_mtu"] = int(dict_val["ipv6_mtu"])
                continue

            # IPv4 VRF ID : 0
            m = p9_12.match(line)
            if m:
                dict_val = m.groupdict()
                interface_details = ret_dict.setdefault("interface_details", {})
                interface_details["ipv4_vrf_id"] = int(dict_val["ipv4_vrf_id"])
                continue

            # IPv6 VRF ID : 65535
            m = p9_13.match(line)
            if m:
                dict_val = m.groupdict()
                interface_details = ret_dict.setdefault("interface_details", {})
                interface_details["ipv6_vrf_id"] = int(dict_val["ipv6_vrf_id"])
                continue

            # Protocol flags : 0x0003 [ ipv4 ipv6 ]
            m = p9_14.match(line)
            if m:
                dict_val = m.groupdict()
                interface_details = ret_dict.setdefault("interface_details", {})
                interface_details["protocol_flags"] = dict_val["protocol_flags"]
                continue

            # Misc flags : 0x0041 [ ipv4 --- ]
            m = p9_15.match(line)
            if m:
                dict_val = m.groupdict()
                interface_details = ret_dict.setdefault("interface_details", {})
                interface_details["misc_flags"] = dict_val["misc_flags"]
                continue

            # ICMPv4 flags : 0x03 [ unreachable redirect ]
            m = p9_16.match(line)
            if m:
                dict_val = m.groupdict()
                interface_details = ret_dict.setdefault("interface_details", {})
                interface_details["icmpv4_flags"] = dict_val["icmpv4_flags"]
                continue

            # ICMPv6 flags : 0x03 [ unreachable redirect ]
            m = p9_17.match(line)
            if m:
                dict_val = m.groupdict()
                interface_details = ret_dict.setdefault("interface_details", {})
                interface_details["icmpv6_flags"] = dict_val["icmpv6_flags"]
                continue

            # Mac Address : 6c:b2:ae:4a:54:c5
            m = p9_18.match(line)
            if m:
                dict_val = m.groupdict()
                interface_details = ret_dict.setdefault("interface_details", {})
                interface_details["mac_address"] = dict_val["mac_address"]
                continue

            # QoS Trust Type : 3 (DSCP)
            m = p9_19.match(line)
            if m:
                dict_val = m.groupdict()
                interface_details = ret_dict.setdefault("interface_details", {})
                interface_details["qos_trust_type"] = dict_val["qos_trust_type"]
                continue

            # Interface Ref-Cnt       : 2
            m = p1_6.match(line)
            if m:
                dict_val = m.groupdict()
                int_info = ret_dict.setdefault("int_info", {})
                int_info["ref_count"] = int(dict_val["ref_count"])
                continue

            # Interface Type          : WIRED_CLIENT
            m = p1_7.match(line)
            if m:
                dict_val = m.groupdict()
                int_info = ret_dict.setdefault("int_info", {})
                int_info["type"] = dict_val["type"]
                continue

            # Created Time            : 2022/09/29 12:17:16.343
            m = p1_8.match(line)
            if m:
                dict_val = m.groupdict()
                int_info = ret_dict.setdefault("int_info", {})
                int_info["create_time"] = dict_val["create_time"]
                continue

            # Last Modified Time      : 2022/09/29 12:17:16.387
            m = p1_9.match(line)
            if m:
                dict_val = m.groupdict()
                int_info = ret_dict.setdefault("int_info", {})
                int_info["last_modfd_time"] = dict_val["last_modfd_time"]
                continue

            # Current Time            : 2022/09/29 12:29:36.705
            m = p1_10.match(line)
            if m:
                dict_val = m.groupdict()
                int_info = ret_dict.setdefault("int_info", {})
                int_info["cur_time"] = dict_val["cur_time"]
                continue

            # mac : 001b.0c18.918d
            m = p1_11.match(line)
            if m:
                dict_val = m.groupdict()
                int_info = ret_dict.setdefault("int_info", {})
                int_info["mac"] = dict_val["mac"]
                continue

            # parent if_id   : 0x0000000000000020
            m = p1_12.match(line)
            if m:
                dict_val = m.groupdict()
                int_info = ret_dict.setdefault("int_info", {})
                int_info["parent_if_id"] = dict_val["parent_if_id"]
                continue

            # Client if_id   : 0x0000000013151bdb
            m = p1_13.match(line)
            if m:
                dict_val = m.groupdict()
                int_info = ret_dict.setdefault("int_info", {})
                int_info["client_if_id"] = dict_val["client_if_id"]
                continue

            # Switch Num     : 1
            m = p1_14.match(line)
            if m:
                dict_val = m.groupdict()
                int_info = ret_dict.setdefault("int_info", {})
                int_info["switch_num"] = int(dict_val["switch_num"])
                continue

            # Client type    : 1
            m = p1_15.match(line)
            if m:
                dict_val = m.groupdict()
                int_info = ret_dict.setdefault("int_info", {})
                int_info["client_type"] = int(dict_val["client_type"])
                continue

            # ASIC Num       : 1
            m = p1_16.match(line)
            if m:
                dict_val = m.groupdict()
                int_info = ret_dict.setdefault("int_info", {})
                int_info["asic_num"] = int(dict_val["asic_num"])
                continue

            # Client LE      : 0x7f16cd0caaa8
            m = p1_17.match(line)
            if m:
                dict_val = m.groupdict()
                int_info = ret_dict.setdefault("int_info", {})
                int_info["client_le"] = dict_val["client_le"]
                continue

            # DNS punt       : False
            m = p1_18.match(line)
            if m:
                dict_val = m.groupdict()
                int_info = ret_dict.setdefault("int_info", {})
                int_info["dns_punt"] = dict_val["dns_punt"]
                continue

            # Ref Count : 2 (feature Ref Counts + 1)
            m = p1_19.match(line)
            if m:
                dict_val = m.groupdict()
                int_info = ret_dict.setdefault("int_info", {})
                int_info["ref_count_feature"] = dict_val["ref_count_feature"]
                continue

            # Handle ............ [0x8b00013f]
            m = p2.match(line)
            if m:
                dict_val = m.groupdict()
                port_info = ret_dict.setdefault("port_info", {})
                port_info["handle"] = dict_val["handle"]
                continue

            # Type .............. [Wired-client]
            m = p2_1.match(line)
            if m:
                dict_val = m.groupdict()
                port_info = ret_dict.setdefault("port_info", {})
                port_info["type"] = dict_val["type"]
                continue

            # Identifier ........ [0x13151bdb]
            m = p2_2.match(line)
            if m:
                dict_val = m.groupdict()
                port_info = ret_dict.setdefault("port_info", {})
                port_info["identifier"] = dict_val["identifier"]
                continue

            # Unit .............. [320150491]
            m = p2_3.match(line)
            if m:
                dict_val = m.groupdict()
                port_info = ret_dict.setdefault("port_info", {})
                port_info["unit"] = dict_val["unit"]
                continue

            # Client LE handle .... [0x7f16cd0caaa8]
            m = p3.match(line)
            if m:
                dict_val = m.groupdict()
                port_logical_subblk = ret_dict.setdefault("port_logical_subblk", {})
                port_logical_subblk["client_le_handle"] = dict_val["client_le_handle"]
                continue

            # Parent Identifier : 0x20
            m = p3_1.match(line)
            if m:
                dict_val = m.groupdict()
                port_logical_subblk = ret_dict.setdefault("port_logical_subblk", {})
                port_logical_subblk["parent_identifier"] = dict_val["parent_identifier"]
                continue

            # Asic num          : 0x1
            m = p3_2.match(line)
            if m:
                dict_val = m.groupdict()
                port_logical_subblk = ret_dict.setdefault("port_logical_subblk", {})
                port_logical_subblk["asic_num"] = dict_val["asic_num"]
                continue

            #       Switch num        : 0x1
            m = p3_3.match(line)
            if m:
                dict_val = m.groupdict()
                port_logical_subblk = ret_dict.setdefault("port_logical_subblk", {})
                port_logical_subblk["switch_num"] = dict_val["switch_num"]
                continue

            #       Rewrite type      : 0x0
            m = p3_4.match(line)
            if m:
                dict_val = m.groupdict()
                port_logical_subblk = ret_dict.setdefault("port_logical_subblk", {})
                port_logical_subblk["rewr_type"] = dict_val["rewr_type"]
                continue

            #       Client mac        : 1:0:0:0:0:0
            m = p3_5.match(line)
            if m:
                dict_val = m.groupdict()
                port_logical_subblk = ret_dict.setdefault("port_logical_subblk", {})
                port_logical_subblk["client_mac"] = dict_val["client_mac"]
                continue

            #       RI handle         : 53
            m = p3_6.match(line)
            if m:
                dict_val = m.groupdict()
                port_logical_subblk = ret_dict.setdefault("port_logical_subblk", {})
                port_logical_subblk["ri_handle"] = int(dict_val["ri_handle"])
                continue

            #       DI handle         : 0
            m = p3_7.match(line)
            if m:
                dict_val = m.groupdict()
                port_logical_subblk = ret_dict.setdefault("port_logical_subblk", {})
                port_logical_subblk["di_handle"] = int(dict_val["di_handle"])
                continue

            #       Dst Adj  handle   : 0
            m = p3_8.match(line)
            if m:
                dict_val = m.groupdict()
                port_logical_subblk = ret_dict.setdefault("port_logical_subblk", {})
                port_logical_subblk["dst_adj_handle"] = int(dict_val["dst_adj_handle"])
                continue

            #       Dst Lookup handle : 0
            m = p3_9.match(line)
            if m:
                dict_val = m.groupdict()
                port_logical_subblk = ret_dict.setdefault("port_logical_subblk", {})
                port_logical_subblk["dst_lkp_handle"] = int(dict_val["dst_lkp_handle"])
                continue

            #       Src Adj  handle   : 0x53
            m = p3_10.match(line)
            if m:
                dict_val = m.groupdict()
                port_logical_subblk = ret_dict.setdefault("port_logical_subblk", {})
                port_logical_subblk["src_adj_handle"] = dict_val["src_adj_handle"]
                continue

            #       Src Lookup handle : 0
            m = p3_11.match(line)
            if m:
                dict_val = m.groupdict()
                port_logical_subblk = ret_dict.setdefault("port_logical_subblk", {})
                port_logical_subblk["src_lkp_handle"] = int(dict_val["src_lkp_handle"])
                continue

            #       Enabled ............. [No]
            m = p4.match(line)
            if m:
                dict_val = m.groupdict()
                port_l2_subblk = ret_dict.setdefault("port_l2_subblk", {})
                port_l2_subblk["enabled"] = dict_val["enabled"]

            #       Allow dot1q ......... [No]
            m = p4_1.match(line)
            if m:
                dict_val = m.groupdict()
                port_l2_subblk = ret_dict.setdefault("port_l2_subblk", {})
                port_l2_subblk["allow_dot1q"] = dict_val["allow_dot1q"]

            #       Allow native ........ [No]
            m = p4_2.match(line)
            if m:
                dict_val = m.groupdict()
                port_l2_subblk = ret_dict.setdefault("port_l2_subblk", {})
                port_l2_subblk["allow_native"] = dict_val["allow_native"]
                continue
            #       Default VLAN ........ [0]
            m = p4_3.match(line)
            if m:
                dict_val = m.groupdict()
                port_l2_subblk = ret_dict.setdefault("port_l2_subblk", {})
                port_l2_subblk["def_vlan"] = int(dict_val["def_vlan"])
                continue

            #       Allow priority tag ... [No]
            m = p4_4.match(line)
            if m:
                dict_val = m.groupdict()
                port_l2_subblk = ret_dict.setdefault("port_l2_subblk", {})
                port_l2_subblk["allow_priority_tag"] = dict_val["allow_priority_tag"]
                continue

            #       Allow unknown unicast  [No]
            m = p4_5.match(line)
            if m:
                dict_val = m.groupdict()
                port_l2_subblk = ret_dict.setdefault("port_l2_subblk", {})
                port_l2_subblk["allow_unkn_ucast"] = dict_val["allow_unkn_ucast"]
                continue

            #       Allow unknown multicast[No]
            m = p4_6.match(line)
            if m:
                dict_val = m.groupdict()
                port_l2_subblk = ret_dict.setdefault("port_l2_subblk", {})
                port_l2_subblk["allow_unkn_mcast"] = dict_val["allow_unkn_mcast"]
                continue

            #       Allow unknown broadcast[No]
            m = p4_7.match(line)
            if m:
                dict_val = m.groupdict()
                port_l2_subblk = ret_dict.setdefault("port_l2_subblk", {})
                port_l2_subblk["allow_unkn_bcast"] = dict_val["allow_unkn_bcast"]
                continue

            #       Protected ............ [No]
            m = p4_8.match(line)
            if m:
                dict_val = m.groupdict()
                port_l2_subblk = ret_dict.setdefault("port_l2_subblk", {})
                port_l2_subblk["protected"] = dict_val["protected"]
                continue

            #       IPv4 ARP snoop ....... [No]
            m = p4_9.match(line)
            if m:
                dict_val = m.groupdict()
                port_l2_subblk = ret_dict.setdefault("port_l2_subblk", {})
                port_l2_subblk["ipv4_arp_snp"] = dict_val["ipv4_arp_snp"]
                continue

            #       IPv6 ARP snoop ....... [No]
            m = p4_10.match(line)
            if m:
                dict_val = m.groupdict()
                port_l2_subblk = ret_dict.setdefault("port_l2_subblk", {})
                port_l2_subblk["ipv6_arp_snp"] = dict_val["ipv6_arp_snp"]
                continue

            #       Jumbo MTU ............ [0]
            m = p4_11.match(line)
            if m:
                dict_val = m.groupdict()
                port_l2_subblk = ret_dict.setdefault("port_l2_subblk", {})
                port_l2_subblk["jumbo_mtu"] = int(dict_val["jumbo_mtu"])
                continue

            #       Learning Mode ........ [0]
            m = p4_12.match(line)
            if m:
                dict_val = m.groupdict()
                port_l2_subblk = ret_dict.setdefault("port_l2_subblk", {})
                port_l2_subblk["learning_mode"] = int(dict_val["learning_mode"])
                continue

            #       Vepa ................. [Disabled]
            m = p4_13.match(line)
            if m:
                dict_val = m.groupdict()
                port_l2_subblk = ret_dict.setdefault("port_l2_subblk", {})
                port_l2_subblk["vepa"] = dict_val["vepa"]
                continue

            #       App Hosting........... [Disabled]
            m = p4_14.match(line)
            if m:
                dict_val = m.groupdict()
                port_l2_subblk = ret_dict.setdefault("port_l2_subblk", {})
                port_l2_subblk["app_hosting"] = dict_val["app_hosting"]
                continue

            #       Trust Type .................... [0x7]
            m = p5.match(line)
            if m:
                dict_val = m.groupdict()
                port_qos_subblk = ret_dict.setdefault("port_qos_subblk", {})
                port_qos_subblk["trust_type"] = dict_val["trust_type"]
                continue

            #       Default Value ................. [0]
            m = p5_1.match(line)
            if m:
                dict_val = m.groupdict()
                port_qos_subblk = ret_dict.setdefault("port_qos_subblk", {})
                port_qos_subblk["def_value"] = int(dict_val["def_value"])
                continue

            #       Ingress Table Map ............. [0x0]
            m = p5_2.match(line)
            if m:
                dict_val = m.groupdict()
                port_qos_subblk = ret_dict.setdefault("port_qos_subblk", {})
                port_qos_subblk["ingrs_tbl_map"] = dict_val["ingrs_tbl_map"]
                continue

            #       Egress Table Map .............. [0x0]
            m = p5_3.match(line)
            if m:
                dict_val = m.groupdict()
                port_qos_subblk = ret_dict.setdefault("port_qos_subblk", {})
                port_qos_subblk["egrs_tbl_map"] = dict_val["egrs_tbl_map"]
                continue

            #       Queue Map ..................... [0x0]
            m = p5_4.match(line)
            if m:
                dict_val = m.groupdict()
                port_qos_subblk = ret_dict.setdefault("port_qos_subblk", {})
                port_qos_subblk["q_map"] = dict_val["q_map"]
                continue

            #       Disable SGACL .................... [0x0]
            m = p6.match(line)
            if m:
                dict_val = m.groupdict()
                port_cts_subblk = ret_dict.setdefault("port_cts_subblk", {})
                port_cts_subblk["disable_sgacl"] = dict_val["disable_sgacl"]
                continue

            #       Trust ............................ [0x0]
            m = p6_1.match(line)
            if m:
                dict_val = m.groupdict()
                port_cts_subblk = ret_dict.setdefault("port_cts_subblk", {})
                port_cts_subblk["trust"] = dict_val["trust"]
                continue

            #       Propagate ........................ [0x0]
            m = p6_2.match(line)
            if m:
                dict_val = m.groupdict()
                port_cts_subblk = ret_dict.setdefault("port_cts_subblk", {})
                port_cts_subblk["propagate"] = dict_val["propagate"]
                continue

            #       Port SGT ......................... [0xffff]
            m = p6_3.match(line)
            if m:
                dict_val = m.groupdict()
                port_cts_subblk = ret_dict.setdefault("port_cts_subblk", {})
                port_cts_subblk["port_sgt"] = dict_val["port_sgt"]
                continue

            #   FID : 98 (AAL_FEATURE_L2_MULTICAST_IGMP), Ref Count : 1
            m = p7.match(line)
            if m:
                dict_val = m.groupdict()
                ifm_feature_ref_counts = ret_dict.setdefault("ifm_feature_ref_counts", {})
                ifm_feature_ref_counts["fid"] = dict_val["fid"]
                ifm_feature_ref_counts["ref_count"] = int(dict_val["ref_count"])
                continue

            # Affinity .......... [local]
            m = p11.match(line)
            if m:
                dict_val = m.groupdict()
                port_phy_sub = ret_dict.setdefault("port_phy_sub", {})
                port_phy_sub["affinity"] = dict_val["affinity"]
                continue

            # LPN ............... [19]
            m = p11_1.match(line)
            if m:
                dict_val = m.groupdict()
                port_phy_sub = ret_dict.setdefault("port_phy_sub", {})
                port_phy_sub["lpn"] = int(dict_val["lpn"])
                continue

            # GPN ............... [979]
            m = p11_2.match(line)
            if m:
                dict_val = m.groupdict()
                port_phy_sub = ret_dict.setdefault("port_phy_sub", {})
                port_phy_sub["gpn"] = int(dict_val["gpn"])
                continue

            # Speed ............. [40GB]
            m = p11_3.match(line)
            if m:
                dict_val = m.groupdict()
                port_phy_sub = ret_dict.setdefault("port_phy_sub", {})
                port_phy_sub["speed"] = dict_val["speed"]
                continue

            # type .............. [IFM_PORT_TYPE_L3]
            m = p11_4.match(line)
            if m:
                dict_val = m.groupdict()
                port_phy_sub = ret_dict.setdefault("port_phy_sub", {})
                port_phy_sub["type"] = dict_val["type"]
                continue

            # MTU ............... [2022]
            m = p11_5.match(line)
            if m:
                dict_val = m.groupdict()
                port_phy_sub = ret_dict.setdefault("port_phy_sub", {})
                port_phy_sub["mtu"] = int(dict_val["mtu"])
                continue

            # ac profile ........ [IFM_AC_PROFILE_DEFAULT]
            m = p11_6.match(line)
            if m:
                dict_val = m.groupdict()
                port_phy_sub = ret_dict.setdefault("port_phy_sub", {})
                port_phy_sub["ac_profile"] = dict_val["ac_profile"]
                continue

            # Mac port oid................... [4444]
            m = p12.match(line)
            if m:
                dict_val = m.groupdict()
                port_sub = ret_dict.setdefault("port_sub", {})
                port_sub["mac_port_oid"] = dict_val["mac_port_oid"]
                continue

            # System port oid................ [4448]
            m = p12_1.match(line)
            if m:
                dict_val = m.groupdict()
                port_sub = ret_dict.setdefault("port_sub", {})
                port_sub["system_port_oid"] = dict_val["system_port_oid"]
                continue

            # System port gid................ [223]
            m = p12_2.match(line)
            if m:
                dict_val = m.groupdict()
                port_sub = ret_dict.setdefault("port_sub", {})
                port_sub["system_port_gid"] = int(dict_val["system_port_gid"])
                continue

            # Ethernet port oid.............. [4459]
            m = p12_3.match(line)
            if m:
                dict_val = m.groupdict()
                port_sub = ret_dict.setdefault("port_sub", {})
                port_sub["ethernet_port_oid"] = dict_val["ethernet_port_oid"]
                continue
            
            # Port mode...................... [Dense Mode] 
            m = p12_3_1.match(line)
            if m:
                dict_val = m.groupdict()
                port_sub = ret_dict.setdefault("port_sub", {})
                port_sub["port_sub_block_port_mode"] = dict_val["port_sub_block_port_mode"]
                continue
            
            # Dense mode service port gid.... [122994] 
            m = p12_3_2.match(line)
            if m:
                dict_val = m.groupdict()
                port_sub = ret_dict.setdefault("port_sub", {})
                port_sub["dense_mode_service_port_gid"] = dict_val["dense_mode_service_port_gid"]
                continue
            
            # Dense mode service port oid.... [0xa0b(2571)] 
            m = p12_3_3.match(line)
            if m:
                dict_val = m.groupdict()
                port_sub = ret_dict.setdefault("port_sub", {})
                port_sub["dense_mode_service_port_oid"] = dict_val["dense_mode_service_port_oid"]
                continue

            # Dense mode port vid............ [50] 
            m = p12_3_4.match(line)
            if m:
                dict_val = m.groupdict()
                port_sub = ret_dict.setdefault("port_sub", {})
                port_sub["dense_mode_port_vid"] = dict_val["dense_mode_port_vid"]
                continue

            # Voq oid........................ [4446]
            m = p12_4.match(line)
            if m:
                dict_val = m.groupdict()
                port_sub = ret_dict.setdefault("port_sub", {})
                port_sub["vog_oid"] = dict_val["vog_oid"]
                continue

            # Asic.............. [0]
            m = p13.match(line)
            if m:
                dict_val = m.groupdict()
                platform_sub = ret_dict.setdefault("platform_sub", {})
                platform_sub["asic"] = int(dict_val["asic"])
                continue

            # Core.............. [5]
            m = p13_1.match(line)
            if m:
                dict_val = m.groupdict()
                platform_sub = ret_dict.setdefault("platform_sub", {})
                platform_sub["core"] = int(dict_val["core"])
                continue

            # Asic Port......... [0]
            m = p13_2.match(line)
            if m:
                dict_val = m.groupdict()
                platform_sub = ret_dict.setdefault("platform_sub", {})
                platform_sub["asic_port"] = int(dict_val["asic_port"])
                continue

            # Asic Sub Port..... [65535]
            m = p13_3.match(line)
            if m:
                dict_val = m.groupdict()
                platform_sub = ret_dict.setdefault("platform_sub", {})
                platform_sub["asic_sub_port"] = int(dict_val["asic_sub_port"])
                continue

            # Ifg Id............ [0]
            m = p13_4.match(line)
            if m:
                dict_val = m.groupdict()
                platform_sub = ret_dict.setdefault("platform_sub", {})
                platform_sub["ifg_id"] = int(dict_val["ifg_id"])
                continue

            # Mac Num........... [211]
            m = p13_5.match(line)
            if m:
                dict_val = m.groupdict()
                platform_sub = ret_dict.setdefault("platform_sub", {})
                platform_sub["mac_num"] = int(dict_val["mac_num"])
                continue

            # First Serdes...... [10]
            m = p13_6.match(line)
            if m:
                dict_val = m.groupdict()
                platform_sub = ret_dict.setdefault("platform_sub", {})
                platform_sub["first_serdes"] = int(dict_val["first_serdes"])
                continue

            # Last Serdes....... [11]
            m = p13_7.match(line)
            if m:
                dict_val = m.groupdict()
                platform_sub = ret_dict.setdefault("platform_sub", {})
                platform_sub["last_serdes"] = int(dict_val["last_serdes"])
                continue

            # FC Mode........... [0]
            m = p13_8.match(line)
            if m:
                dict_val = m.groupdict()
                platform_sub = ret_dict.setdefault("platform_sub", {})
                platform_sub["fc_mode"] = int(dict_val["fc_mode"])
                continue

            # FEC Mode.......... [0]
            m = p13_9.match(line)
            if m:
                dict_val = m.groupdict()
                platform_sub = ret_dict.setdefault("platform_sub", {})
                platform_sub["fec_mode"] = int(dict_val["fec_mode"])
                continue

            # Context Id........ [0]
            m = p13_10.match(line)
            if m:
                dict_val = m.groupdict()
                platform_sub = ret_dict.setdefault("platform_sub", {})
                platform_sub["context_id"] = int(dict_val["context_id"])
                continue

            # L2 Port Mode ................ [port_mode_dynamic]
            m = p14.match(line)
            if m:
                dict_val = m.groupdict()
                port_l2_sub = ret_dict.setdefault("port_l2_sub", {})
                port_l2_sub["port_mode"] = dict_val["port_mode"]
                continue

            # L2 Port Mode set............. [No]
            m = p14_1.match(line)
            if m:
                dict_val = m.groupdict()
                port_l2_sub = ret_dict.setdefault("port_l2_sub", {})
                port_l2_sub["port_mode_set"] = dict_val["port_mode_set"]
                continue

            # Default vlan ................ [0]
            m = p14_2.match(line)
            if m:
                dict_val = m.groupdict()
                port_l2_sub = ret_dict.setdefault("port_l2_sub", {})
                port_l2_sub["vlan"] = int(dict_val["vlan"])
                continue

            # Ethertype.................... [8100]
            m = p14_3.match(line)
            if m:
                dict_val = m.groupdict()
                port_l2_sub = ret_dict.setdefault("port_l2_sub", {})
                port_l2_sub["ethertype"] = int(dict_val["ethertype"])
                continue
            
            # Port vlan  .................. [50] 
            # Port vlan  .................. [50] 
            m = p14_3_1.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_l2_sub" not in ret_dict:
                    port_l2_sub = ret_dict.setdefault("port_l2_sub", {})
                if "l2_sub_block_port_vlan" not in port_l2_sub:
                    l2_sub_block_port_vlan = port_l2_sub.setdefault("l2_sub_block_port_vlan", {})
                l2_sub_block_port_vlan["l2_sub_block_port_vlan"] = int(dict_val["l2_sub_block_port_vlan"])
                continue
            
            # Native vlan (trunk) .............. [0]
            m = p14_3_2.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_l2_sub" not in ret_dict:
                    port_l2_sub = ret_dict.setdefault("port_l2_sub", {})
                if "l2_sub_block_port_vlan" not in l2_sub_block_port_vlan:
                    l2_sub_block_port_vlan = l2_sub_block_port_vlan.setdefault("l2_sub_block_port_vlan", {})
                l2_sub_block_port_vlan["native_vlan_trunk"] = int(dict_val["native_vlan_trunk"])
                continue
            
            #  Untagged port bd vlan (access) ... [50]
            m = p14_3_3.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_l2_sub" not in ret_dict:
                    port_l2_sub = ret_dict.setdefault("port_l2_sub", {})
                if "l2_sub_block_port_vlan" not in l2_sub_block_port_vlan:
                    l2_sub_block_port_vlan = l2_sub_block_port_vlan.setdefault("l2_sub_block_port_vlan", {})
                l2_sub_block_port_vlan["untagged_port_bd_vlan"] = int(dict_val["untagged_port_bd_vlan"])
                continue
            
            #  Default vlan (dot1q tunnel) ...... [0]
            m = p14_3_4.match(line)
            if m:
                dict_val = m.groupdict()
                if "port_l2_sub" not in ret_dict:
                    port_l2_sub = ret_dict.setdefault("port_l2_sub", {})
                if "l2_sub_block_port_vlan" not in l2_sub_block_port_vlan:
                    l2_sub_block_port_vlan = l2_sub_block_port_vlan.setdefault("l2_sub_block_port_vlan", {})
                l2_sub_block_port_vlan["default_vlan"] = int(dict_val["default_vlan"])
                continue
            
            # Native Vlan Tagging.......... [Native Vlan None]
            m = p14_3_5.match(line)
            if m:
                dict_val = m.groupdict()
                port_l2_sub = ret_dict.setdefault("port_l2_sub", {})
                port_l2_sub["native_vlan_tagging"] = dict_val["native_vlan_tagging"]
                continue
            
            # untagged port bd vlan ....... [0]
            m = p14_4.match(line)
            if m:
                dict_val = m.groupdict()
                port_l2_sub = ret_dict.setdefault("port_l2_sub", {})
                port_l2_sub["bd_vlan"] = int(dict_val["bd_vlan"])
                continue

            # status....................... [0]
            m = p14_5.match(line)
            if m:
                dict_val = m.groupdict()
                port_l2_sub = ret_dict.setdefault("port_l2_sub", {})
                port_l2_sub["status"] = int(dict_val["status"])
                continue

            # ac profile .................. [IFM_AC_PROFILE_DEFAULT]
            m = p14_6.match(line)
            if m:
                dict_val = m.groupdict()
                port_l2_sub = ret_dict.setdefault("port_l2_sub", {})
                port_l2_sub["ac_profile"] = dict_val["ac_profile"]
                continue

            # # Port CTS Subblock is NULL if_id = 0x14c3c6db 
            m = p19.match(line)
            if m:
                dict_val = m.groupdict()
                port_cts_subblk = ret_dict.setdefault("port_cts_subblk", {})
                port_cts_subblk["cts_if_id"] = dict_val["cts_if_id"]
                continue

        return ret_dict

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
        Optional("encap"): str,
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
        # Source Ports         : RX: Port-channel1 TX: Port-channel1
        p2 = re.compile(
            r"^Source Ports\s+: RX:\s+(?P<rx>[\w\/\-\s]+)\sTX:\s*(?P<tx>[\w\/\-\s]+)?$"
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
# Parser for 'show platform software fed {switch} {mode} acl info db summary '
# ======================================================
class ShowPlatformSoftwareFedSwitchActiveAclInfoDbSummarySchema(MetaParser):
    """Schema for:
       'show platform software fed switch active acl info db summary'
       'show platform software fed {switch} {mode} acl info db summary'
       'show platform software fed {mode} acl info db summary'
       'show platform software fed {switch} {mode} acl info db feature sgacl summary'
    """
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
    """Parser for:
       'show platform software fed switch active acl info db summary'
       'show platform software fed {switch} {mode} acl info db summary'
       'show platform software fed {mode} acl info db summary'
       'show platform software fed {switch} {mode} acl info db feature sgacl summary'
    """
    cli_command = [
        "show platform software fed switch active acl info db summary",
        "show platform software fed {switch} {mode} acl info db summary",
        "show platform software fed {mode} acl info db summary",
        "show platform software fed {switch} {mode} acl info db feature {feature_name} summary"
    ]

    def cli(self, switch=None, mode=None, feature_name=None, output=None):
        if output is None:
            if switch and mode and feature_name:
                cmd = self.cli_command[3].format(switch=switch, mode=mode, feature_name=feature_name)
            elif switch and mode:
                cmd = self.cli_command[1].format(switch=switch, mode=mode)
            elif mode:
                cmd = self.cli_command[2].format(mode=mode)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

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
        # CG Name         : PACLv6in!PACLv4in:filterACL6!filterACL4:
        p6 = re.compile(r"^CG Name\s+:\s(?P<cg_name>[\w\_\-\!\:]+)$")

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
                        Optional("counter"): str,
                        Optional("counter_asic") :str,
                        Optional("counter_oid") :str,
                        Optional("packet_count") :int,
                        Optional("logging") :str,
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
        * "show platform software fed {switch} {mode} acl info db detail",
        * "show platform software fed {mode} acl info db detail",
        * "show platform software fed {switch} {mode} acl info db feature {feature_name} detail",
        * "show platform software fed {switch} {mode} acl info db feature {feature_name} dir {in_out} cgid {cg_id} detail",
        * "show platform software fed {switch} {mode} acl info db feature {feature_name} dir {in_out} detail"
    """
    cli_command = [
        "show platform software fed {switch} {mode} acl info db detail",
        "show platform software fed {mode} acl info db detail",
        "show platform software fed {switch} {mode} acl info db feature {feature_name} detail",
        "show platform software fed {switch} {mode} acl info db feature {feature_name} dir {in_out} cgid {cg_id} detail",
        "show platform software fed {switch} {mode} acl info db feature {feature_name} dir {in_out} detail"
    ]

    def cli(self, mode, switch=None, feature_name=None, in_out=None, cg_id=None, output=None):
        if output is None:
            if switch and mode:
                cmd = self.cli_command[0].format(mode=mode, switch=switch)
            elif switch and mode and feature_name:
                cmd = self.cli_command[2].format(switch=switch, mode=mode, feature_name=feature_name)
            elif switch and mode and feature_name and in_out and cg_id:
                cmd = self.cli_command[3].format(switch=switch, mode=mode, feature_name=feature_name, in_out=in_out, cg_id=cg_id)
            elif switch and mode and feature_name and in_out:
                cmd = self.cli_command[4].format(switch=switch, mode=mode, feature_name=feature_name, in_out=in_out)    
            else:
                cmd = self.cli_command[1].format(mode=mode)

            output = self.device.execute(cmd)

        proto_flag = False
        tos_flag = False

        # [CG ID 13]    CG Name: acl-2    Feature: Racl
        p1 = re.compile(
            r"^\[CG ID+\s+(?P<cg_id>[\d]+)\]+\s+CG+\s+Name:+\s(?P<cg_name>[\w\-]+)+\s+Feature:+\s(?P<feature>[\w]+)$"
        )

        # [CG ID: 10]    CG Name: pre-auth
        p1_1 = re.compile(r'^\[CG ID: (?P<cg_id>\d+)\]\s+CG Name: (?P<cg_name>\S+)$')

        # [Sgacl, CG ID: 273]    CG Name: V4SGACL;000
        p1_2 = re.compile(r'\[\w+, CG ID: (?P<cg_id>\d+)\]\s+CG Name: (?P<cg_name>\S+)$')

        # [CG ID 13]    Prot: IPv4
        p2 = re.compile(r"^\[CG ID+\s+(?P<cg_id>[\d]+)\]+\s+Prot:+\s(?P<prot>[\w]+)$")

        # Feature: Pacl    Prot: IPv4
        p2_1 = re.compile(r'Feature: (?P<feature>\S+)\s+Prot: (?P<prot>\S+)')

        # [CG ID 13]    Region grp: 0xdc09b2a8
        p3 = re.compile(
            r"^\[CG ID+\s+(?P<cg_id>[\d]+)\]+\s+Region+\s+grp:+\s(?P<region>[\w\-]+)$"
        )

        # Region grp: 0x8c062308    Dir: Ingress
        p3_1 = re.compile(r'Region grp: (?P<region>\S+)\s+Dir: (?P<dir>\S+)')


        # [CG ID 13]    Dir: Egress    SDK-handle(asic: 0, OID: 0x0000)
        p4 = re.compile(
            r"^\[CG ID+\s+(?P<cg_id>[\S\s]+)\]+\s+Dir:+\s(?P<dir>[\w]+)+\s+SDK-handle+\(asic:+\s+(?P<asic>[\d]+),\s+OID:+\s+(?P<oid>[\w\s]+)\)$"
        )

        # SDK-handle(asic: 0, OID: 0xAC4)
        p4_1 = re.compile(r'SDK-handle\(asic: (?P<asic>\d+), OID: (?P<oid>\S+)\)')

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

        # Result  action: PERMIT    Logging: NO_LOG
        p10_1 = re.compile(r'Result\s+action: (?P<result>\S+)\s+Logging: (?P<logging>\S+)')

        # Counter handle: (asic: 0 , OID: 0xAC6 (0))
        p11 = re.compile(r'Counter handle: \(asic: (?P<counter_asic>\d+) , OID: (?P<counter_oid>\S+) \((?P<packet_count>\d+)\)\)')

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

            # [CG ID: 10]    CG Name: pre-auth
            m = p1_1.match(line)
            if m:
                group = m.groupdict()
                int_dict = ret_dict.setdefault("cg_name", {}).setdefault(
                    (group["cg_name"]), {}
                )
                int_dict["cg_id"] = int(group["cg_id"])
                continue

            # [Sgacl, CG ID: 273]    CG Name: V4SGACL;000
            m = p1_2.match(line)
            if m:
                group = m.groupdict()
                int_dict = ret_dict.setdefault("cg_name", {}).setdefault(
                    (group["cg_name"]), {}
                )
                int_dict["cg_id"] = int(group["cg_id"])
                continue

            # [CG ID 13]    Prot: IPv4
            m = p2.match(line)
            if m:
                group = m.groupdict()
                int_dict["prot"] = group["prot"]
                continue

            # Feature: Pacl    Prot: IPv4
            m = p2_1.match(line)
            if m:
                group = m.groupdict()
                int_dict["feature"] = group["feature"]
                int_dict["prot"] = group["prot"]
                continue

            # [CG ID 13]    Region grp: 0xdc09b2a8
            m = p3.match(line)
            if m:
                group = m.groupdict()
                int_dict["region"] = group["region"]
                continue

            # Region grp: 0x8c062308    Dir: Ingress
            m = p3_1.match(line)
            if m:
                group = m.groupdict()
                int_dict["region"] = group["region"]
                int_dict["dir"] = group["dir"]
                continue

            # [CG ID 13]    Dir: Egress    SDK-handle(asic: 0, OID: 0x0000)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                int_dict["dir"] = group["dir"]
                int_dict["asic"] = int(group["asic"])
                int_dict["oid"] = group["oid"]
                continue

            # SDK-handle(asic: 0, OID: 0xAC4)
            m = p4_1.match(line)
            if m:
                group = m.groupdict()
                int_dict["asic"] = int(group["asic"])
                int_dict["oid"] = group["oid"]
                continue

            # Seq Num:4294967295
            m = p5.match(line)
            if m:
                group = m.groupdict()
                seq_key = group["seq"]

                if seq_key in int_dict.setdefault("seq", {}):
                    # If it does, append _1, _2, etc., to make it unique
                    counter = 1
                    while f"{seq_key}_{counter}" in int_dict["seq"]:
                        counter += 1
                    seq_key = f"{seq_key}_{counter}"

                seq_dict = int_dict["seq"].setdefault(seq_key, {})
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

            # Result  action: PERMIT    Logging: NO_LOG
            m = p10_1.match(line)
            if m:
                group = m.groupdict()
                seq_dict["result"] = group["result"]
                seq_dict["logging"] = group["logging"]

            # Counter handle: (asic: 0 , OID: 0xAC6 (0))
            m = p11.match(line)
            if m:
                group = m.groupdict()
                seq_dict["counter_asic"] = group["counter_asic"]
                seq_dict["counter_oid"] = group["counter_oid"]
                seq_dict["packet_count"] = int(group["packet_count"])

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
                Optional("stp_state_hw"): str,
                "vtp_pruned": str,
                "untagged": str,
                "ingress": str,
                "egress": str,
                Optional("gid"): int,
                Optional("mac_learn"): str,
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
        # FiftyGigE1/0/11         none    disabled         Blocking          No         Yes         Blocking         Blocking         850        Enable
        p1_1 = re.compile(r"^(?P<interface>\S+) +(?P<pvlan_mode>\S+) +(?P<stp_state>\S+) +(?P<stp_state_hw>\S+) +(?P<vtp_pruned>\S+) +(?P<untagged>\w+) +(?P<ingress>\w+) +(?P<egress>\w+) +(?P<gid>\d+) +(?P<mac_learn>\S+)$")
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
                
                
            # FiftyGigE1/0/11         none    disabled         Blocking          No         Yes         Blocking         Blocking         850        Enable
            m = p1_1.match(line)
            if m:
                dict_val = m.groupdict()
                key_chain_dict = ret_dict.setdefault("interface", {}).setdefault(
                    Common.convert_intf_name(dict_val["interface"]), {}
                )
                key_chain_dict["pvlan_mode"] = dict_val["pvlan_mode"]
                key_chain_dict["stp_state"] = dict_val["stp_state"]
                key_chain_dict["stp_state_hw"] = dict_val["stp_state_hw"]
                key_chain_dict["vtp_pruned"] = dict_val["vtp_pruned"]
                key_chain_dict["untagged"] = dict_val["untagged"]
                key_chain_dict["ingress"] = dict_val["ingress"]
                key_chain_dict["egress"] = dict_val["egress"]
                key_chain_dict["gid"] = int(dict_val["gid"])
                key_chain_dict["mac_learn"] = dict_val["mac_learn"]
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

    cli_command = ["show platform software fed switch {mode} acl og-pcl", 
                   "show platform software fed active acl og-pcl"]

    def cli(self, command=None, output=None, **kwargs):
        if output is None:
            output = self.device.execute(command)

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
    cli_command = ["show platform software fed switch active acl statistics events",
                   "show platform software fed {switch} {mode} acl statistics events",
                   "show platform software fed {mode} acl statistics events"]

    def cli(self, switch=None, mode=None, output=None):
        if output is None:
            if switch and mode:
                cmd = self.cli_command[1].format(switch=switch, mode=mode)
            elif mode:
                cmd = self.cli_command[2].format(mode=mode)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

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
        "show platform software fed switch {mode} ifm mappings etherchannel",
        "show platform software fed active ifm mappings etherchannel",
    ]

    def cli(self, command=None, timeout=600, output=None, **kwargs):
        if output is None:
            output = self.device.execute(command, timeout=timeout)

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
        "show platform software fed {switch} {switch_type} ifm {if_id}",
        "show platform software fed active ifm {if_id}",
    ]

    def cli(self, if_id, switch=None, switch_type="", out=None):
        if out is None:
            if switch and switch_type:
                cmd = self.cli_command[0].format(if_id=if_id, switch=switch, switch_type=switch_type)
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
    * 'show platform hardware fed active fnf record-count asic {asic_num}'
    * 'show platform hardware fed switch {state} fnf record-count asic {asic_num}'
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

# ============================================================
#  Schema for 'show platform software fed active fnf record-count asic <asic num>'
# ============================================================
class ShowPlatformSoftwareFedActiveFnfRecordCountAsicNumSchema(MetaParser):
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
        "total_bytes_aged_out": int
        }


# ============================================================================
#  Parser for
#  * 'show platform software fed active fnf record-count asic <asic num>'
#  * 'show platform software fed switch active fnf record-count asic <asic num>'
# ============================================================================
class ShowPlatformSoftwareFedActiveFnfRecordCountAsicNum(ShowPlatformSoftwareFedActiveFnfRecordCountAsicNumSchema):
    """
    Parser for
    * 'show platform software fed active fnf record-count asic {asic_num}'
    * 'show platform software fed switch {state} fnf record-count asic {asic_num}'
    """

    cli_command = ['show platform software fed active fnf record-count asic {asic_num}',
                   'show platform software fed switch {state} fnf record-count asic {asic_num}']

    def cli(self, asic_num, state=None, output=None):
        if output is None:
            if state:
                cmd = self.cli_command[1].format(state=state, asic_num=asic_num)
            else:
                cmd = self.cli_command[0].format(asic_num=asic_num)
            output = self.device.execute(cmd)

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^(?P<pattern>[\S ]+)= +(?P<value>\d+)$')

        # Current flow count               = 0
        # Total flows learned              = 0
        # Hash searched flow count         = 0
        # Overflow searched flow count     = 0
        # Hash unsearched flow count       = 0
        # Overflow unsearched flow count   = 0
        # Total flow Searched              = 0
        # Total search failures            = 0
        # Total AVC cpu copy disable       = 0
        # Total ETA cpu copy disable       = 0
        # Total cpu copy disable           = 0
        # Total AVC feature flows          = 0
        # Total ETA feature flows          = 0
        # Total ETA and AVC feature flows  = 0
        # Total num_eta_flows_agedout      = 0
        # Total flows deleted              = 0
        # Total delete failures            = 0
        # Total flow aged out              = 0
        # Total stale flow deleted         = 0
        # Total stale flow del aborted     = 0
        # Total packets aged out           = 0
        # Total bytes aged out             = 0

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                scrubbed = (group['pattern'].strip()).replace(' ', '_')
                ret_dict.update({scrubbed.lower(): int(group['value'])})
                continue
        return ret_dict

class ShowPlatformSoftwareFedSwitchActiveipecrexactroutesourceipdestinationipSchema(MetaParser):
    """
    Schema for show platform software fed switch {type} ip ecr exact-route {sourceip} {destinationip} {sourceport} {destinationport} {protocol}
    show platform software fed switch {type} ip ecr exact-route {sourceip} {destinationip} {sourceport} {destinationport} {protocol}
    """

    schema = {
        'destport': str,
        }

class ShowPlatformSoftwareFedSwitchActiveipecrexactroutesourceipdestinationip(ShowPlatformSoftwareFedSwitchActiveipecrexactroutesourceipdestinationipSchema):
    """ Parser for show platform software fed switch {type} ip ecr exact-route {sourceip} {destinationip} {sourceport} {destinationport} {protocol}"""

    cli_command = ['show platform software fed switch {type} ip ecr exact-route {sourceip} {destinationip}',
                   'show platform software fed switch {type} ip ecr exact-route {sourceip} {destinationip} {sourceport} {destinationport} {protocol}']


    def cli(self, type, sourceip, destinationip,sourceport=None,destinationport=None,protocol=None, output=None):

        if output is None:
            if sourceport and destinationport and protocol :
                cmd = self.cli_command[1].format(type=type,sourceip=sourceip,destinationip=destinationip,sourceport=sourceport,destinationport=destinationport,protocol=protocol)
            else:
                cmd = self.cli_command[0].format(type=type,sourceip=sourceip,destinationip=destinationip)
            output = self.device.execute(cmd)

        ret_dict = {}
        #Dest Port:GigabitEthernet2/0/1
        p1 = re.compile(r'^Dest Port:(?P<destport>.*)$')

        for line in output.splitlines():
            line = line.strip()

            #Dest Port:GigabitEthernet2/0/1
            m = p1.match(line)
            if m:
                group=m.groupdict()
                ret_dict['destport']= group['destport']
                continue

        return ret_dict

# ====================================================
# Parser for show platform software fed igmp snooping vlan detail'
# ====================================================
class ShowPlatformSoftwareFedIgmpSnoopingVlanDetailSchema(MetaParser):
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
                Optional("protocol"): str,
                Optional("secondary_vlan"): str,
                Optional("vlan_urid"): str,
                Optional("d_users_count"): str,
                Optional("fset_urid_hash"): str,
                Optional("fset_aux_urid"): str,
                Optional("gid"): int,
                Optional("mcid_asic"): int,
                Optional("hw_info_asic"): 
                {
                    "hw_vlan_mcid_oid": str,
                    "multicast_state": str
                }
            }
        }
    }

class ShowPlatformSoftwareFedIgmpSnoopingVlanDetail(ShowPlatformSoftwareFedIgmpSnoopingVlanDetailSchema):
    """Parser for show Platform Software fed igmp snooping vlan detail"""

    cli_command = [
        "show platform software fed {switch_var} {state} ip igmp snooping vlan {vlan} detail",
        "show platform software fed {state} ip igmp snooping vlan {vlan} detail",
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

        # (ipv4, vlan: 3000)
        p0_1 = re.compile(r'^\(+(?P<protocol>\S+)+\,+\s+vlan\:\s+(?P<vlan>\d+)+\)$')

        # IGMPSN Enabled : On
        p1 = re.compile(r"^IGMPSN\s+Enabled\s+:\s+(?P<igmp_en>[\s\w\s]+)$")

        # Snoop State     : ON
        p1_1 = re.compile(r"^Snoop\s+State\s+:\s+(?P<snoop_state>[\w\s]+)$")

        # Snoop State     : ON
        p1_1 = re.compile(r"^Snoop\s+State\s+:\s+(?P<snoop_state>[\w\s]+)$")

        # PIMSN Enabled : Off
        p2 = re.compile(r"^PIMSN\s+Enabled\s+:\s+(?P<pimsn_en>[\s\w\s]+)$")

        # Flood Mode : Off
        p3 = re.compile(r"^Flood\s+Mode\s+:\s+(?P<flood_md>[\s\w\s]+)$")

        # Oper State : Up
        p4 = re.compile(r"^Oper\s+State\s+:\s+(?P<op_state>[\s\w\s]+)$")

        # STP TCN Flood : Off
        # STP TCN State : Off
        p5 = re.compile(
            r"^STP\s+TCN\s+(Flood|State)\s+:\s+(?P<stp_tcn_flood>[\s\w\s]+)$"
        )
        # STP TCN State : Off
        p5 = re.compile(
            r"^STP\s+TCN\s+(Flood|State)\s+:\s+(?P<stp_tcn_flood>[\s\w\s]+)$"
        )

        # Routing Enabled : On
        p6 = re.compile(r"^Routing\s+Enabled\s+:\s+(?P<route_en>[\s\w\s]+)$")

        # PIM Enabled : On
        p7 = re.compile(r"^PIM\s+Enabled\s+:\s+(?P<pim_en>[\s\w\s]+)$")

        # Pim state               : ON
        p7_1 = re.compile(r'^Pim\s+state\s+:\s+(?P<pim_en>[\s\w\s]+)$')

        # PVLAN : No
        p8 = re.compile(r"^PVLAN\s+:\s+(?P<pvlan>[\s\w\s]+)$")

        # In Retry : 0x0
        p9 = re.compile(r"^In\s+Retry\s+:\s+(?P<in_retry>[\s\w\s]+)$")

        # CCK Epoch : 0x17
        p10 = re.compile(r"^CCK\s+Epoch\s+:\s+(?P<cck_ep>[\s\w\s]+)$")

        # IOSD Flood Mode : Off
        p11 = re.compile(r"^IOSD\s+Flood\s+Mode\s+:\s+(?P<iosd_md>[\s\w\s]+)$")

        # IOS Flood Mode          : OFF
        p11_1 = re.compile(r'^IOS\s+Flood\s+Mode\s+:\s+(?P<iosd_md>[\s\w\s]+)$')

        # EVPN Proxy Enabled : On
        p12 = re.compile(r"^EVPN\s+Proxy\s+Enabled\s+:\s+(?P<evpn_en>[\s\w\s]+)$")

        # Evpn Proxy              : OFF
        p12_1 = re.compile(r'^Evpn\s+Proxy\s+:\s+(?P<evpn_en>[\s\w\s]+)$')

        # L3mcast Adj :
        p13 = re.compile(r"^L3mcast\s+Adj\s+:(?P<l3m_adj>.*)$")

        # Mrouter PortQ :
        p14 = re.compile(r"^Mrouter\s+[P|p]ort[Q|s]\s+:\s*")
        # nve1.VNI60020(0x200000071)
        p14_1 = re.compile(r"([A-Za-z]*\d[-().]*){10,}")

        # port:Port-channel10 (ec_member:HundredGigE1/0/5) (group_oif:0) (mrouter_flag:1)
        # port:Port-channel10 (ec_member:HundredGigE1/0/5) (group_oif:0) (mrouter_flag:1)
        # port:Port-channel100 (ec_member:HundredGigE2/5/0/2)
        # port:Port-channel0 (ec_member:HundredGigE1/0/5) (group_oif:0)
        # port:Port-channel77
        p14_2 = re.compile(r"^port:(?P<port>[\w\-\.]+)(\s+(?P<left>.*))?$")
        # port:Port-channel0 (ec_member:HundredGigE1/0/5) (group_oif:0)
        # port:Port-channel77
        p14_2 = re.compile(r"^port:(?P<port>[\w\-\.]+)(\s+(?P<left>.*))?$")

        # Flood PortQ :
        p15 = re.compile(r"^Flood [P|p]ort[Q|s]\s+:\s*")
        # TenGigabitEthernet7/0/13
        # FiveGigabitEthernet1/0/2
        # GigabitEthernet2/0/31
        p15_1 = re.compile(r"^[A-Za-z-]+[\d\/\.]+$")

        # REP RI handle : 0x0
        p16 = re.compile(r"^REP\s+RI\s+handle\s+:\s+(?P<rep_han>[\s\w\s]+)$")

        # Secondary Vlan          : NO
        p17 = re.compile(r'^Secondary\s+Vlan\s+:\s+(?P<secondary_vlan>[\s\w\s]+)$')
            
        # Vlan Urid               : 0x5000000000000008
        p18 = re.compile(r'^Vlan\s+Urid\s+:\s+(?P<vlan_urid>[\s\w\s]+)$')

        #  Fset Urid ( hash )      : 0x20000000000009af ( ed2a6e06 )
        p18_1 = re.compile(r'^Fset Urid \( hash \)\s+:\s+(?P<fset_urid_hash>[\S+\s]+.)$')

        # Fset Aux Urid           : 0x0
        p18_2 = re.compile(r'^Fset Aux Urid\s+:\s+(?P<fset_aux_urid>\S+)$')
            
        # Dependant users count   : 0
        p19 = re.compile(r'^Dependant\s+users\s+count\s+:\s+(?P<d_users_count>[\s\w\s]+)$')

        # Gid                     : 10604
        p20= re.compile(r'^Gid\s+:\s+(?P<gid>\d+)$')

        # Mcid Asic[0]            : 8997
        p21 = re.compile(r'^Mcid Asic\[(?P<asic>\d+)\]\s+:\s+(?P<mcid>\d+)$')

        # Hw Vlan Mcid Oid    : 8997 (cookie:urid:0x20::9af)
        p22 = re.compile(r'Hw Vlan Mcid Oid\s+:\s+(?P<hw_vlan_mcid_oid>[\S\s]+.)$')

        # Multicast state     : disabled
        p23 = re.compile(r'Multicast state\s+:\s+(?P<multicast_state>[\S\s]+.)$')


        port_list = None
        mroute_list = []
        floodport_list = []
        for line in output.splitlines():
            line = line.strip()

            # Vlan 20
            m = p0.match(line)
            if m:
                vlan = int(m.groupdict()["vlan"])
                mac_dict = platform_dict.setdefault("vlan", {}).setdefault(vlan, {})

            # (ipv4, vlan: 3000)
            m = p0_1.match(line)
            if m:
                vlan = int(m.groupdict()['vlan'])
                mac_dict = platform_dict.setdefault('vlan', {}).setdefault(vlan, {})
                mac_dict['protocol'] = m.groupdict()['protocol']

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

            # Pim state               : ON
            m = p7_1.match(line)
            if m:
                mac_dict['pim_en'] = m.groupdict()['pim_en']
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

            # IOS Flood Mode          : OFF
            m = p11_1.match(line)
            if m:
                mac_dict['iosd_md'] = m.groupdict()['iosd_md']
                continue

            # EVPN Proxy Enabled : On
            m = p12.match(line)
            if m:
                mac_dict["evpn_en"] = m.groupdict()["evpn_en"]
                continue

            # Evpn Proxy              : OFF
            m = p12_1.match(line)
            if m:
                mac_dict['evpn_en'] = m.groupdict()['evpn_en']
                continue

            # L3mcast Adj :
            m = p13.match(line)
            if m:
                mac_dict["l3m_adj"] = m.groupdict()["l3m_adj"]
                continue

            # Mrouter PortQ :
            m = p14.match(line)
            if m:
                mac_dict["mroute_port"] = mroute_list
                port_list = mroute_list
                continue

            # nve1.VNI60020(0x200000071)
            m = p14_1.match(line)
            if m:
                port_list.append(m.group(0))

            # port:Port-channel100 (ec_member:HundredGigE2/5/0/2)
            m = p14_2.match(line)
            if m:
                port_list.append(m.group(0))

            # TenGigabitEthernet7/0/13
            # FiveGigabitEthernet1/0/2
            # GigabitEthernet2/0/31
            m = p15_1.match(line)
            if m:
                port_list.append(m.group(0))

            # Flood PortQ :
            m = p15.match(line)
            if m:
                port_list = floodport_list
                mac_dict["flood_port"] = floodport_list
                continue

            # REP RI handle : 0x0
            m = p16.match(line)
            if m:
                mac_dict["rep_han"] = m.groupdict()["rep_han"]
                continue

            # Secondary Vlan          : NO
            m = p17.match(line)
            if m:
                mac_dict['secondary_vlan'] = m.groupdict()['secondary_vlan']
                continue
    
            # Vlan Urid               : 0x5000000000000008
            m = p18.match(line)
            if m:
                mac_dict['vlan_urid'] = m.groupdict()['vlan_urid']
                continue

            # Fset Urid ( hash )      : 0x20000000000009af ( ed2a6e06 )
            match = p18_1.match(line)
            if match:
                mac_dict['fset_urid_hash'] = match.group('fset_urid_hash')
                continue

            # Fset Aux Urid           : 0x0
            match = p18_2.match(line)
            if match:
                mac_dict['fset_aux_urid'] = match.group('fset_aux_urid')
                continue
    
            # Dependant users count   : 0
            m = p19.match(line)
            if m:
                mac_dict['d_users_count'] = m.groupdict()['d_users_count']
                continue

            #  Gid                     : 10604
            match = p20.match(line)
            if match:
                mac_dict['gid'] = int(match.group('gid'))
                continue

            # Mcid Asic[0]            : 8997
            match = p21.match(line)
            if match:
                mac_dict['mcid_asic'] = int(match.group('mcid'))
                continue

            # Hw Vlan Mcid Oid    : 8997 (cookie:urid:0x20::9af)
            match = p22.match(line)
            if match:
                mac_dict.setdefault('hw_info_asic', {})
                mac_dict['hw_info_asic']['hw_vlan_mcid_oid'] = match.group('hw_vlan_mcid_oid')
                continue

            # Multicast state     : disabled
            match = p23.match(line)
            if match:
                mac_dict.setdefault('hw_info_asic', {})
                mac_dict['hw_info_asic']['multicast_state'] = match.group('multicast_state')
                continue

        return platform_dict
    
class ShowPlatformSoftwareFedSwitchActiveInjectBriefSchema(MetaParser):
    """
    Schema for show platform software fed switch active inject ios-cause brief
    """

    schema = {
        "cause_dict": {
            Any(): {
                "cause": int,
                "rcvd": int,
                "dropped": int,
            },
        },
    }

class ShowPlatformSoftwareFedSwitchActiveInjectBrief(
    ShowPlatformSoftwareFedSwitchActiveInjectBriefSchema
):
    """
    show platform software fed switch active inject ios-cause brief
    """

    cli_command = [
        "show platform software fed {switch} {mode} inject ios-cause brief",
        "show platform software fed active inject ios-cause brief",
    ]

    def cli(self, switch=None, mode=None, output=None):
        if output is None:
            if switch and mode:
                cmd = self.cli_command[0].format(switch=switch, mode=mode)
            else:
                cmd = self.cli_command[1]
            output = self.device.execute(cmd)

        ret_dict = {}
        cause_dict = {}

        # Cause  Cause Info                      Rcvd                 Dropped
        # 1      L2 control/legacy               5458                 1
        # 2      QFP destination lookup          15                   0
        # 5      QFP <->RP keepalive             416                  0
        # 12     ARP request or response         3                    0
        # 25     Layer2 frame to BD              219930               0
        p0 = re.compile(r"^(?P<cause>\d+)\s+(?P<cause_info>[\w \/ \< \- \>]+)\s+(?P<rcvd>\d+)\s+(?P<dropped>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            # Cause  Cause Info                      Rcvd                 Dropped
            # 1      L2 control/legacy               5458                 1
            # 2      QFP destination lookup          15                   0
            # 5      QFP <->RP keepalive             416                  0
            # 12     ARP request or response         3                    0
            # 25     Layer2 frame to BD              219930               0
            m = p0.match(line)
            if m:
                group = m.groupdict()
                cause_info = group["cause_info"].strip()
                cause_dict = ret_dict.setdefault("cause_dict", {}).setdefault(cause_info, {})
                cause_dict.update({
                    'cause': int(group['cause']),
                    'rcvd': int(group['rcvd']),
                    'dropped': int(group['dropped']),
                })
                continue

        return ret_dict


class ShowPlatformSoftwareFedSwitchActiveIfmInterfacesInternalSchema(MetaParser):
    """Schema for show platform software fed switch active ifm interfaces internal {interface}"""
    schema = {
        'interface': {
            Any(): {
                'if_id': str,
                'interface_name': str,
                'interface_block_pointer': str,
                'interface_block_state': str,
                'interface_state': str,
                'interface_status': str,
                'interface_ref_cnt': int,
                'interface_type': str,
                'bootup_breakout_config': {
                    'port_type': str,
                    'port_location': str,
                    'slot': int,
                    'unit': int,
                    'slot_unit': int,
                    'num_queues': int
                },
                'ref_count': int,
                'feature_reference_count': str,
                'ifm_feature_subblock_information': {
                    'port_physical': {
                        'affinity': str,
                        'lpn': int,
                        'gpn': int,
                        'speed': str,
                        'type': str,
                        'mtu': int,
                        'ac_profile': str
                    },
                    'port': {
                        'mac_port_oid': int,
                        'system_port_oid': int,
                        'system_port_gid': int,
                        'ethernet_port_oid': int,
                        'voq_oid': int
                    },
                    'platform': {
                        'asic': int,
                        'core': int,
                        'asic_port': int,
                        'asic_sub_port': int,
                        'ifg_id': int,
                        'mac_num': int,
                        'first_serdes': int,
                        'last_serdes': int,
                        'fc_mode': int,
                        'fec_mode': int,
                        'context_id': int
                    },
                    'port_cts': {
                        'disable_sgacl': str,
                        'trust': str,
                        'propagate': str,
                        'port_sgt': str
                    }
                }
            }
        }
    }

class ShowPlatformSoftwareFedSwitchActiveIfmInterfacesInternal(ShowPlatformSoftwareFedSwitchActiveIfmInterfacesInternalSchema):
    """Parser for show platform software fed switch active ifm interfaces internal {interface}"""

    cli_command = 'show platform software fed switch active ifm interfaces internal {interface}'

    def cli(self, interface, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface))

        # Initial variables
        ret_dict = {}
        parsed_dict = {}
        subblock_dict = {}
        current_subblock = None
        current_subblock_name = None
        bootup_dict = None

        # Interface IF_ID         : 0x0015000000000001
        p1 = re.compile(r'^Interface IF_ID\s+:\s+(?P<if_id>.+)$')

        # Interface Name          : Puntport/0
        p2 = re.compile(r'^Interface Name\s+:\s+(?P<interface_name>.+)$')

        # Interface Block Pointer : 0x7c74d4279228
        p3 = re.compile(r'^Interface Block Pointer\s+:\s+(?P<interface_block_pointer>.+)$')

        # Interface Block State   : Ready
        p4 = re.compile(r'^Interface Block State\s+:\s+(?P<interface_block_state>.+)$')

        # Interface State         : Enabled
        p5 = re.compile(r'^Interface State\s+:\s+(?P<interface_state>.+)$')

        # Interface Status        : ADD
        p6 = re.compile(r'^Interface Status\s+:\s+(?P<interface_status>.+),$')

        # Interface Ref-Cnt       : 1
        p7 = re.compile(r'^Interface Ref-Cnt\s+:\s+(?P<interface_ref_cnt>\d+)$')

        # Interface Type          : INTERNAL INTERFACE
        p8 = re.compile(r'^Interface Type\s+:\s+(?P<interface_type>.+)$')

        # Port Type         : EGRESS CPU
        p9 = re.compile(r'^Port Type\s+:\s+(?P<port_type>.+)$')

        # Port Location     : REMOTE
        p10 = re.compile(r'^Port Location\s+:\s+(?P<port_location>.+)$')

        # Slot              : 0
        p11 = re.compile(r'^Slot\s+:\s+(?P<slot>\d+)$')

        #  Unit              : 0
        p12 = re.compile(r'^Unit\s+:\s+(?P<unit>\d+)$')

        # Slot Unit         : 0
        p13 = re.compile(r'^Slot Unit\s+:\s+(?P<slot_unit>\d+)$')

        # Num Queues        : 0
        p14 = re.compile(r'^Num Queues\s+:\s+(?P<num_queues>\d+)$')

        # Ref Count : 1 (feature Ref Counts + 1)
        p15 = re.compile(r'^Ref Count\s+:\s+(?P<ref_count>\d+)\s+\(feature Ref Counts \+ \d+\)$')

        # No Feature Reference count Present
        p16 = re.compile(r'^(?P<feature_reference_count>\w+)\s+Feature Reference count Present$')

        # Port Physical Subblock
        # Port Subblock [0]
        # Platform Subblock
        #  Port CTS Subblock
        p17 = re.compile(r'^(?P<SubblockName>.+) Subblock(\s+\[.+\])?$')

        # Affinity .......... [local]
        p18 = re.compile(r'^(?P<key>.+)\s+\.+\s+\[(?P<value>.+)\]$')

         # Mac port oid................... [0xe4(228)]
        p19 = re.compile(r'^(?P<key>.+?)\s*\.+\s*\[(?P<value>[^\]]+)\]$')

        for line in output.splitlines():
            line = line.strip()

            # Interface IF_ID         : 0x0015000000000001
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                parsed_dict = ret_dict.setdefault('interface', {}).setdefault(interface, {})
                parsed_dict['if_id'] = group['if_id']
                continue

            # Interface Name          : Puntport/0
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                parsed_dict['interface_name'] = group['interface_name']
                continue

            # Interface Block Pointer : 0x7c74d4279228
            m3 = p3.match(line)
            if m3:
                parsed_dict['interface_block_pointer'] = m3.group('interface_block_pointer')
                continue

            # Interface Block State   : Ready
            m4 = p4.match(line)
            if m4:
                parsed_dict['interface_block_state'] = m4.group('interface_block_state')
                continue

            # Interface State         : Enabled
            m5 = p5.match(line)
            if m5:
                parsed_dict['interface_state'] = m5.group('interface_state')
                continue

            # Interface Status        : ADD,
            m6 = p6.match(line)
            if m6:
                parsed_dict['interface_status'] = m6.group('interface_status')
                continue

            # Interface Ref-Cnt       : 1
            m7 = p7.match(line)
            if m7:
                parsed_dict['interface_ref_cnt'] = int(m7.group('interface_ref_cnt'))
                continue

            # Interface Type          : INTERNAL INTERFACE
            m8 = p8.match(line)
            if m8:
                parsed_dict['interface_type'] = m8.group('interface_type')
                continue

            # Port Type         : EGRESS CPU
            m9 = p9.match(line)
            if m9:
                bootup_dict = parsed_dict.setdefault('bootup_breakout_config', {})
                bootup_dict['port_type'] = m9.group('port_type')
                continue

            # Port Location     : REMOTE
            m10 = p10.match(line)
            if m10:
                if bootup_dict is None:
                    bootup_dict = parsed_dict.setdefault('bootup_breakout_config', {})
                bootup_dict['port_location'] = m10.group('port_location')
                continue

            # Slot              : 0
            m11 = p11.match(line)
            if m11:
                if bootup_dict is None:
                    bootup_dict = parsed_dict.setdefault('bootup_breakout_config', {})
                bootup_dict['slot'] = int(m11.group('slot'))
                continue

            #  Unit              : 0
            m12 = p12.match(line)
            if m12:
                if bootup_dict is None:
                    bootup_dict = parsed_dict.setdefault('bootup_breakout_config', {})
                bootup_dict['unit'] = int(m12.group('unit'))
                continue

            # Slot Unit         : 0
            m13 = p13.match(line)
            if m13:
                if bootup_dict is None:
                    bootup_dict = parsed_dict.setdefault('bootup_breakout_config', {})
                bootup_dict['slot_unit'] = int(m13.group('slot_unit'))
                continue

            # Num Queues        : 0
            m14 = p14.match(line)
            if m14:
                if bootup_dict is None:
                    bootup_dict = parsed_dict.setdefault('bootup_breakout_config', {})
                bootup_dict['num_queues'] = int(m14.group('num_queues'))
                continue

            # Ref Count : 1 (feature Ref Counts + 1)
            m15 = p15.match(line)
            if m15:
                parsed_dict['ref_count'] = int(m15.group('ref_count'))
                continue

            # No Feature Reference count Present
            m16 = p16.match(line)
            if m16:
                parsed_dict['feature_reference_count'] = m16.group('feature_reference_count')
                continue

            # Port Physical Subblock
            # Port Subblock [0]
            # Platform Subblock
            #  Port CTS Subblock
            m17 = p17.match(line)
            if m17:
                current_subblock_name = m17.group('SubblockName').strip().replace(' Subblock', '').lower()
                if current_subblock_name == 'port physical':
                    current_subblock_name = 'port_physical'
                elif current_subblock_name == 'port cts':
                    current_subblock_name = 'port_cts'

                current_subblock = subblock_dict.setdefault(current_subblock_name, {})
                continue

            # Affinity .......... [local]
            m18 = p18.match(line)
            if m18:
                key = m18.group('key').strip().lower().replace(' ', '_')
                value = m18.group('value').strip('[]').strip()
                if key in {'lpn', 'gpn', 'mtu'}:  # convert these fields to integers
                    value = int(value)
                if current_subblock is not None:
                    current_subblock[key] = value
                continue

            # Mac port oid................... [0xe4(228)]
            m19 = p19.match(line)
            if m19:
                key = m19.group('key').strip().lower().replace(' ', '_')
                value = m19.group('value').strip()
                if key in {'mac_port_oid', 'system_port_oid', 'system_port_gid', 'ethernet_port_oid', 'voq_oid'}:  # convert these fields to integers if they are not hex
                    try:
                        value = int(value.split('(')[-1].strip(')'))
                    except ValueError:
                        pass
                if key in {'asic', 'core', 'asic_port', 'asic_sub_port', 'ifg_id', 'mac_num', 'first_serdes', 'last_serdes', 'fc_mode', 'fec_mode', 'context_id'}:
                    value = int(value)
                if current_subblock is not None:
                    current_subblock[key] = value
                continue

        parsed_dict['ifm_feature_subblock_information'] = subblock_dict

        return ret_dict


class ShowPlatformSoftwareFedSwitchActiveAclBindDbIfidSchema(MetaParser):
    """Schema for
       'show platform software fed switch active acl bind db if-id {if_id} detail'
    """

    schema = {
        'interfaces': {
            Any(): {
                'bindings': ListOf({
                    'direction': str,
                    'feature': str,
                    'protocol': str,
                    'cg_id': int,
                    'cg_name': str,
                    'status': str,
                    'src_og_lkup_hdl': int,
                    'dst_og_lkup_hdl': int,
                })
            }
        }
    }

class ShowPlatformSoftwareFedSwitchActiveAclBindDbIfid(ShowPlatformSoftwareFedSwitchActiveAclBindDbIfidSchema):
    """ Parser for
    * 'show platform software fed switch active acl bind db if-id {if_id} detail'
    """

    cli_command = 'show platform software fed switch {switch_var} acl bind db if-id {if_id} detail'

    def cli(self, switch_var, if_id, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch_var=switch_var,if_id=if_id))

        ret_dict = {}

        # Interface Name: Gi2/0/10
        p1 = re.compile(r'^Interface Name: (?P<interface_name>\S+)$')

        # Direction: Ingress
        p2 = re.compile(r'^Direction: (?P<direction>\S+)$')

        # Feature         : Pacl
        p3 = re.compile(r'^Feature\s+: (?P<feature>\S+)$')

        # Protocol        : MAC
        p4 = re.compile(r'^Protocol\s+: (?P<protocol>\S+)$')

        # CG ID           : 1
        p5 = re.compile(r'^CG ID\s+: (?P<cg_id>\d+)$')

        # CG Name         : pacl_mac
        p6 = re.compile(r'^CG Name\s+: (?P<cg_name>\S+)$')

        # Status          : Success
        p7 = re.compile(r'^Status\s+: (?P<status>\S+)$')

        # Src_og_lkup_hdl : 0
        p8 = re.compile(r'^Src_og_lkup_hdl\s+: (?P<src_og_lkup_hdl>\d+)$')

        # Dst_og_lkup_hdl : 0
        p9 = re.compile(r'^Dst_og_lkup_hdl\s+: (?P<dst_og_lkup_hdl>\d+)$')

        current_interface = None
        current_direction = None
        binding = None

        for line in output.splitlines():
            line = line.strip()

            # Interface Name: Gi2/0/10
            m = p1.match(line)
            if m:
                ret_dict.setdefault('interfaces', {})
                interface_name = m.group('interface_name')
                current_interface = interface_name
                if interface_name not in ret_dict['interfaces']:
                    ret_dict['interfaces'][interface_name] = {
                        'bindings': []
                    }
                continue

            # Direction: Ingress
            m = p2.match(line)
            if m:
                current_direction = m.group('direction').lower()
                continue

            # Feature         : Pacl
            m = p3.match(line)
            if m:
                binding = {'feature': m.group('feature'), 'direction': current_direction}
                ret_dict['interfaces'][current_interface]['bindings'].append(binding)
                continue

            # Protocol        : MAC
            m = p4.match(line)
            if m:
                binding['protocol'] = m.group('protocol')
                continue

            # CG ID           : 1
            m = p5.match(line)
            if m:
                binding['cg_id'] = int(m.group('cg_id'))
                continue

            # CG Name         : pacl_mac
            m = p6.match(line)
            if m:
                binding['cg_name'] = m.group('cg_name')
                continue

            # Status          : Success
            m = p7.match(line)
            if m:
                binding['status'] = m.group('status')
                continue

            # Src_og_lkup_hdl : 0
            m = p8.match(line)
            if m:
                binding['src_og_lkup_hdl'] = int(m.group('src_og_lkup_hdl'))
                continue

            # Dst_og_lkup_hdl : 0
            m = p9.match(line)
            if m:
                binding['dst_og_lkup_hdl'] = int(m.group('dst_og_lkup_hdl'))
                continue

        return ret_dict


class ShowPlatformSoftwareFedSwitchActiveSecurityFedArpIfSchema(MetaParser):
    schema = {
        'fed_arp_snooping_port_data': {
            'if_id': int,
            'if_name': str,
            'arp_snoop_enable': bool,
            'punject_port_profile': bool,
            'etherchannel_member': bool,
            'etherchannel': bool,
            'etherchannel_if_id': int,
            'ref_cnt': int,
            Optional('asic_specific_section'): {
                Any(): {
                    'acl_oid': int,
                    'positions': {
                        Any(): {
                            'action': str,
                            'counter_oid': int
                        }
                    }
                }
            }            
        }
    }

class ShowPlatformSoftwareFedSwitchActiveSecurityFedArpIf(ShowPlatformSoftwareFedSwitchActiveSecurityFedArpIfSchema):
    """Parser for 'show platform software fed switch active security-fed arp if {if_id}', 
    'show platform software fed {switch} {switch_num} security-fed arp-snoop if-id {if_id}'"""

    cli_command = [
        'show platform software fed switch active security-fed arp if {if_id}',
        'show platform software fed {switch} {switch_num} security-fed arp-snoop if-id {if_id}'
        ]

    def cli(self, if_id, switch="", switch_num="", output=None):
        if output is None:
            if switch:
                output = self.device.execute(self.cli_command[1].format(if_id=if_id,switch=switch,switch_num=switch_num))
            else:
                output = self.device.execute(self.cli_command[0].format(if_id=if_id))

        # Initialize the parsed dictionary
        ret_dict = {}

        # FED ARP SNOOPING PORT Data :
        p0 = re.compile(r'^\s*FED ARP SNOOPING PORT Data\s*:\s*$')

        # if_id = 1180
        p1 = re.compile(r'^\s*if_id\s+=\s+(?P<if_id>\d+)\s*$')

        # if_name = GigabitEthernet3/0/10
        p2 = re.compile(r'^\s*if_name\s+=\s+(?P<if_name>\S+)\s*$')

        # ARP SNOOP enable: FALSE
        p3 = re.compile(r'^\s*ARP SNOOP enable:\s+(?P<arp_snoop_enable>\S+)\s*$')

        # Punject Port Profile: FALSE
        p4 = re.compile(r'^\s*Punject Port Profile:\s+(?P<punject_port_profile>\S+)\s*$')

        # EtherChannel member: FALSE
        p5 = re.compile(r'^\s*EtherChannel member:\s+(?P<etherchannel_member>\S+)\s*$')

        # EtherChannel: FALSE
        p6 = re.compile(r'^\s*EtherChannel:\s+(?P<etherchannel>\S+)\s*$')

        # EtherChannel if_id = 0
        p7 = re.compile(r'^\s*EtherChannel if_id\s+=\s+(?P<etherchannel_if_id>\d+)\s*$')

        # ref_cnt = 0
        p8 = re.compile(r'^\s*ref_cnt\s+=\s+(?P<ref_cnt>\d+)\s*$')

        # Information about ACL with OID(1398) on ASIC(0)
        p9 = re.compile(r'^Information about ACL with OID\((?P<acl_oid>\d+)\) on ASIC\((?P<asic>\d+)\)$')

        # 0        PUNT    1399
        p10 = re.compile(r'^(?P<position>\d+)\s+(?P<action>\S+)\s+(?P<counter_oid>\d+)$')

        asic_specific_section = {}
        current_asic = None
        current_acl_oid = None
        for line in output.splitlines():
            line = line.strip()

            # FED ARP SNOOPING PORT Data :
            m = p0.match(line)
            if m:
                ret_dict['fed_arp_snooping_port_data'] = {}
                data_dict = ret_dict['fed_arp_snooping_port_data']
                continue

            # if_id = 1180
            m = p1.match(line)
            if m:
                data_dict['if_id'] = int(m.group('if_id'))
                continue

            # ARP SNOOP enable: FALSE
            m = p2.match(line)
            if m:
                data_dict['if_name'] = m.group('if_name')
                continue

            # ARP SNOOP enable: FALSE
            m = p3.match(line)
            if m:
                data_dict['arp_snoop_enable'] = m.group('arp_snoop_enable') == 'TRUE'
                continue

            # Punject Port Profile: FALSE
            m = p4.match(line)
            if m:
                data_dict['punject_port_profile'] = m.group('punject_port_profile') == 'TRUE'
                continue

            # EtherChannel member: FALSE
            m = p5.match(line)
            if m:
                data_dict['etherchannel_member'] = m.group('etherchannel_member') == 'TRUE'
                continue

            # EtherChannel: FALSE
            m = p6.match(line)
            if m:
                data_dict['etherchannel'] = m.group('etherchannel') == 'TRUE'
                continue

            # EtherChannel if_id = 0
            m = p7.match(line)
            if m:
                data_dict['etherchannel_if_id'] = int(m.group('etherchannel_if_id'))
                continue

            # ref_cnt = 0
            m = p8.match(line)
            if m:
                data_dict['ref_cnt'] = int(m.group('ref_cnt'))
                continue

            # Information about ACL with OID(1398) on ASIC(0)
            m = p9.match(line)
            if m:
                current_acl_oid = int(m.group('acl_oid'))
                current_asic = int(m.group('asic'))
                asic_specific_section[current_asic] = {
                    'acl_oid': current_acl_oid,
                    'positions': {}
                }
                continue

            # 0        PUNT    1399
            m = p10.match(line)
            if m and current_asic is not None:
                position = int(m.group('position'))
                asic_specific_section[current_asic]['positions'][position] = {
                    'action': m.group('action'),
                    'counter_oid': int(m.group('counter_oid'))
                }
                continue

        if asic_specific_section:
            data_dict['asic_specific_section'] = asic_specific_section

        return ret_dict


class ShowPlatformSoftwareFedSwitchActiveSecurityFedArpVlanSchema(MetaParser):
    schema = {
        'fed_arp_snooping_vlan_data': {
            'vlan': int,
            'punject_switch_profile': bool,
            'arp_snoop_enable': bool,
            'acl_info': {
                'asic': int,
                'oid': int,
                'entries': list
            }
        }
    }

class ShowPlatformSoftwareFedSwitchActiveSecurityFedArpVlan(ShowPlatformSoftwareFedSwitchActiveSecurityFedArpVlanSchema):
    """Parser for 'show platform software fed switch active security-fed arp vlan {vlan}'"""

    cli_command = 'show platform software fed switch active security-fed arp vlan {vlan}'

    def cli(self, vlan, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(vlan=vlan))

        # Initialize the parsed dictionary
        ret_dict = {}

        # FED ARP SNOOPING VLAN Data :
        p0 = re.compile(r'^\s*FED ARP SNOOPING VLAN Data\s*:\s*$')

        # Vlan= 50
        p1 = re.compile(r'^\s*Vlan=\s+(?P<vlan>\d+)\s*$')

        # Punject Switch Profile: TRUE
        p2 = re.compile(r'^\s*Punject Switch Profile:\s+(?P<punject_switch_profile>\S+)\s*$')

        # ARP SNOOP enable: TRUE
        p3 = re.compile(r'^\s*ARP SNOOP enable:\s+(?P<arp_snoop_enable>\S+)\s*$')

        # Information about ACL with OID(552) on ASIC(0)
        p4 = re.compile(r'^\s*Information about ACL with OID\((?P<oid>\d+)\) on ASIC\((?P<asic>\d+)\)\s*$')

        # Position Action  Counter OID

        # ----------------------------

        # 0        PUNT    553
        p5 = re.compile(r'^\s*(?P<position>\d+)\s+(?P<action>\w+)\s+(?P<counter_oid>\d+)\s*$')

        # Parse each line of the output
        for line in output.splitlines():
            line = line.strip()

            # FED ARP SNOOPING VLAN Data :
            m = p0.match(line)
            if m:
                ret_dict['fed_arp_snooping_vlan_data'] = {}
                data_dict = ret_dict['fed_arp_snooping_vlan_data']
                continue

            # Vlan= 50
            m = p1.match(line)
            if m:
                data_dict['vlan'] = int(m.group('vlan'))
                continue

            # Punject Switch Profile: TRUE
            m = p2.match(line)
            if m:
                data_dict['punject_switch_profile'] = m.group('punject_switch_profile') == 'TRUE'
                continue

            # ARP SNOOP enable: TRUE
            m = p3.match(line)
            if m:
                data_dict['arp_snoop_enable'] = m.group('arp_snoop_enable') == 'TRUE'
                continue

            # Information about ACL with OID(552) on ASIC(0)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                acl_info_dict = data_dict.setdefault('acl_info', {})
                acl_info_dict['asic'] = int(group['asic'])
                acl_info_dict['oid'] = int(group['oid'])
                acl_info_dict['entries'] = []
                continue

            # Position Action  Counter OID

            # ----------------------------

            # 0        PUNT    553
            m = p5.match(line)
            if m:
                group = m.groupdict()
                entry = {
                    'position': int(group['position']),
                    'action': group['action'],
                    'counter_oid': int(group['counter_oid']),
                }
                acl_info_dict['entries'].append(entry)
                continue

        return ret_dict


class ShowPlatSoftFedSwAccessSecuritySecMacLrnTableSchema(MetaParser):
    """Schema for
    * 'show platform software fed switch {switch} access-security sec-mac-lrn-table summary'
    * 'show platform software fed switch {switch} access-security sec-mac-lrn-table mac {client_mac}'
    * 'show platform software fed switch {switch} access-security sec-mac-lrn-table interface if-id {if_id}'
    """
    schema = {
        'mac_entries': {
            Any(): {
                'interface': str,
                'vlan': int,
                'mac': str,
                'logical_id': int,
                'position': int,
                'asic_number': int,
                'auth_act': str,
                'restore_auth_act': str,
                'flag': str,
                'drop': str,
                'policy': str,
                'policy_oid': int,
                'packets': int,
            }
        }
    }

class ShowPlatSoftFedSwAccessSecuritySecMacLrnTable(ShowPlatSoftFedSwAccessSecuritySecMacLrnTableSchema):
    """
    Parser for
    * 'show platform software fed switch {switch} access-security sec-mac-lrn-table summary'
    * 'show platform software fed switch {switch} access-security sec-mac-lrn-table mac {client_mac}'
    * 'show platform software fed switch {switch} access-security sec-mac-lrn-table interface if-id {if_id}'
    """
    cli_command = [
        'show platform software fed switch {switch} access-security sec-mac-lrn-table summary',
        'show platform software fed switch {switch} access-security sec-mac-lrn-table mac {client_mac}',
        'show platform software fed switch {switch} access-security sec-mac-lrn-table interface if-id {if_id}'
    ]

    def cli(self, switch, client_mac=None, if_id=None, output=None):
        if output is None:
            if client_mac:
                cmd = self.cli_command[1].format(switch=switch, client_mac=client_mac)
            elif if_id:
                cmd = self.cli_command[2].format(switch=switch, if_id=if_id)
            else:
                cmd = self.cli_command[0].format(switch=switch)
            output = self.device.execute(cmd)

        # Initialize the parsed dictionary
        parsed_data = {}

        # 1 Gi3/0/10     50         0000.0033.3333   0          12288      0     FWD_ALL_LRN_DATA   None               NONE         No     NONE     551        0
        p1 = re.compile(
            r'(?P<se_no>\d+)\s+(?P<interface>\S+)\s+(?P<vlan>\d+)\s+(?P<mac>[0-9A-Fa-f.]+)\s+(?P<logical_id>\d+)\s+'
            r'(?P<position>\d+)\s+(?P<asic_number>\d+)\s+(?P<auth_act>\S+)\s+(?P<restore_auth_act>\S+)\s+(?P<flag>\S+)\s+'
            r'(?P<drop>\S+)\s+(?P<policy>\S+)\s+(?P<policy_oid>\S+)\s+(?P<packets>\d+)'
        )

        for line in output.splitlines():
            line = line.strip()

            # Match the line with the regular expression
            m = p1.match(line)
            if m:
                if 'mac_entries' not in parsed_data:
                    parsed_data['mac_entries'] = {}

                key = int(m.group('se_no'))
                parsed_data['mac_entries'][key] = {
                    'interface': m.group('interface'),
                    'vlan': int(m.group('vlan')),
                    'mac': m.group('mac'),
                    'logical_id': int(m.group('logical_id')),
                    'position': int(m.group('position')),
                    'asic_number': int(m.group('asic_number')),
                    'auth_act': m.group('auth_act'),
                    'restore_auth_act': m.group('restore_auth_act'),
                    'flag': m.group('flag'),
                    'drop': m.group('drop'),
                    'policy': m.group('policy'),
                    'policy_oid': int(m.group('policy_oid')),
                    'packets': int(m.group('packets'))
                }
                continue

        return parsed_data


class ShowPlatformSoftwareFedSwitchActiveAclInfoSdkDetailSchema(MetaParser):
    """Schema for
        * 'show platform software fed switch {switch_var} acl info sdk detail'
        * 'show platform software fed switch {switch_var} acl info sdk feature {feature_name} detail'
        * 'show platform software fed switch {switch_var} acl info sdk feature {feature_name} dir {in_out} cgid {cg_id} detail'
    """
    schema = {
        'class_group_name': {
            Any(): {
                'direction': str,
                'feature': str,
                'protocol': str,
                'cg_id': int,
                'pol_hdl': str,
                'oid': str,
                Optional('no_of_ace'): int,
                Any(): {
                    Optional("ipv4_src_value"): str,
                    Optional("ipv4_src_mask"): str,
                    Optional("ipv4_dst_value"): str,
                    Optional("ipv4_dst_mask"): str,
                    Optional("ipv6_src_mac_value"): str,
                    Optional("ipv6_src_mac_mask"): str,
                    Optional("ipv6_dst_mac_value"): str,
                    Optional("ipv6_dst_mac_mask"): str,
                    Any(): {
                        Optional('proto'): str,
                        Optional('ext_h'): str,
                        Optional('tos'): str,
                        Optional('tcp_flg'): str,
                        Optional('ttl'): str,
                        Optional('ipv4_flags'): str,
                        Optional('src_port'): str,
                        Optional('dst_port'): str,
                    },
                    'result_actions': {
                        'punt': str,
                        'drop': str,
                        'mirror': str,
                        'counter': str,
                        'counter_value': int,
                        Optional('mir_cum'): str,
                        Optional('mir_cmd'): str,
                    }
                }
            }
        }
    }

class ShowPlatformSoftwareFedSwitchActiveAclInfoSdkDetail(ShowPlatformSoftwareFedSwitchActiveAclInfoSdkDetailSchema):
    """Parser for
        * 'show platform software fed switch {switch_var} acl info sdk detail'
        * 'show platform software fed switch {switch_var} acl info sdk feature {feature_name} detail'
        * 'show platform software fed switch {switch_var} acl info sdk feature {feature_name} dir {in_out} cgid {cg_id} detail'
    """

    cli_command = [
        'show platform software fed switch {switch_var} acl info sdk detail',
        'show platform software fed switch {switch_var} acl info sdk feature {feature_name} detail',
        'show platform software fed switch {switch_var} acl info sdk feature {feature_name} dir {in_out} cgid {cg_id} detail'
    ]

    def cli(self, switch_var, feature_name=None, in_out=None, cg_id=None, output=None):
        if output is None:
            if switch_var and in_out and cg_id:
                cmd = self.cli_command[2].format(switch_var=switch_var, feature_name=feature_name, in_out=in_out, cg_id=cg_id)
            elif switch_var and feature_name:
                cmd = self.cli_command[1].format(switch_var=switch_var, feature_name=feature_name)
            else:
                cmd = self.cli_command[0].format(switch_var=switch_var)

            output = self.device.execute(cmd)

        parsed_dict = {}

        # Class Group Name: V4SGACL;000
        p1 = re.compile(r'^Class Group Name:\s+(?P<class_group_name>\S+)$')

        # Direction: Egress
        p2 = re.compile(r'^Direction:\s+(?P<direction>\S+)$')

        # Feature         : Sgacl
        p3 = re.compile(r'^Feature\s+:\s+(?P<feature>\S+)$')

        # Protocol        : IPv4
        p4 = re.compile(r'^Protocol\s+:\s+(?P<protocol>\S+)$')

        # CG ID           : 273
        p5 = re.compile(r'^CG ID\s+:\s+(?P<cg_id>\d+)$')

        # Pol Hdl         : 0x5405cf68
        p6 = re.compile(r'^Pol Hdl\s+:\s+(?P<pol_hdl>\S+)$')

        # ACL (OID: 0x81E, No of ACEs: 1)
        p7 = re.compile(r'^ACL\s+\(OID:\s+(?P<oid>\S+),\s+No\s+of\s+ACEs:\s+(?P<no_of_ace>\d+)\)$')

        # IPV4 ACE Key/Mask
        p8 = re.compile(r'^IPV4 ACE Key/Mask$')

        # ipv4_src: value = 0.0.0.0       mask = 0.0.0.0
        p9 = re.compile(r'^ipv4_src:\s+value\s+=\s+(?P<ipv4_src_value>\S+)\s+mask\s+=\s+(?P<ipv4_src_mask>\S+)$')

        # ipv4_dst: value = 0.0.0.0       mask = 0.0.0.0
        p10 = re.compile(r'^ipv4_dst:\s+value\s+=\s+(?P<ipv4_dst_value>\S+)\s+mask\s+=\s+(?P<ipv4_dst_mask>\S+)$')

        # IPV6 ACE Key/Mask
        p8_1 = re.compile(r'^IPV6 ACE Key/Mask$')

        # src_mac: value = 0x0.0x0.0x0.0x0.0x0.0x0
        p9_1 = re.compile(r'^src_mac:\s+value\s+=\s+(?P<ipv6_src_mac_value>[\S]+)$')

        # mask = 0x0.0x0.0x0.0x0.0x0.0x0
        p9_1_1 = re.compile(r'^mask\s+=\s+(?P<ipv6_src_mac_mask>[\S]+)$')

        # dst_mac: value = 0x0.0x0.0x0.0x0.0x0.0x0
        p10_1 = re.compile(r'^dst_mac:\s+value\s+=\s+(?P<ipv6_dst_mac_value>[\S]+)$')

        # mask = 0x0.0x0.0x0.0x0.0x0.0x0
        p10_1_1 = re.compile(r'^mask\s+=\s+(?P<ipv6_dst_mac_mask>[\S]+)$')

        # V:  0x0       0x0      0x0         0x0       0x0           0x0          0x0
        p11 = re.compile(r'^(?P<pro_type>[VM])\s*:\s+(?P<proto>\S+)\s+(?P<tos>\S+)\s+(?P<tcp_flg>\S+)\s+(?P<ttl>\S+)\s+(?P<ipv4_flags>\S+)\s+(?P<src_port>\S+)\s+(?P<dst_port>\S+)$')

        # V:  0x0       0x0      0x0         0x0       0x0           0x0          0x0
        p12 = re.compile(r'^(?P<pro_type>[VM])\s*:\s+(?P<ext_h>\S+)\s+(?P<tos>\S+)\s+(?P<tcp_flg>\S+)\s+(?P<ttl>\S+)\s+(?P<ipv4_flags>\S+)\s+(?P<src_port>\S+)\s+(?P<dst_port>\S+)$')

        # Result Action
        p13 = re.compile(r'^Result Action$')

        # Punt : N    Drop : N    Mirror: N    Counter: 0x0 (0)
        p14 = re.compile(r'^Punt\s*:\s*(?P<punt>\S+)\s+Drop\s*:\s*(?P<drop>\S+)\s+Mirror\s*:\s*(?P<mirror>\S+)\s+Counter:\s*(?P<counter>\S+)\s*\((?P<counter_value>\d+)\)$')

        # Punt: Y    Drop: N    Mir: N    Mir_Cum: 0x0   Mir_cmd: 0x0    Counter: 0x7bb (0)
        p15 = re.compile(r'^Punt\s*:\s*(?P<punt>\S+)\s+Drop\s*:\s*(?P<drop>\S+)\s+Mir\s*:\s*(?P<mirror>\S+)\s+Mir_Cum\s*:\s*(?P<mir_cum>\S+)\s+Mir_cmd\s*:\s*(?P<mir_cmd>\S+)\s+Counter:\s*(?P<counter>\S+)\s*\((?P<counter_value>\d+)\)$')

        current_protocol = None
        current_key_mask = None

        for line in output.splitlines():
            line = line.strip()

            # Class Group Name: V4SGACL;000
            m = p1.match(line)
            if m:
                group = m.groupdict()
                class_dict = parsed_dict.setdefault('class_group_name', {}).setdefault(group["class_group_name"], {})
                continue

            # Direction: Egress
            m = p2.match(line)
            if m:
                group = m.groupdict()
                class_dict["direction"] = group["direction"]
                continue

            # Feature         : Sgacl
            m = p3.match(line)
            if m:
                group = m.groupdict()
                class_dict["feature"] = group["feature"]
                continue

            # Protocol        : IPv4
            m = p4.match(line)
            if m:
                group = m.groupdict()
                class_dict["protocol"] = group["protocol"]
                current_protocol = group["protocol"]
                continue

            # CG ID           : 273
            m = p5.match(line)
            if m:
                group = m.groupdict()
                class_dict["cg_id"] = int(group["cg_id"])
                continue

            # Pol Hdl         : 0x5405cf68
            m = p6.match(line)
            if m:
                group = m.groupdict()
                class_dict["pol_hdl"] = group["pol_hdl"]
                continue

            # ACL (OID: 0x81E, No of ACEs: 1)
            m = p7.match(line)
            if m:
                group = m.groupdict()
                class_dict["oid"] = group["oid"]
                class_dict["no_of_ace"] = int(group["no_of_ace"])
                continue

            # IPV4 ACE Key/Mask
            m = p8.match(line)
            if m:
                key_base = 'ipv4_ace_key_mask'
                seq_key = key_base

                if seq_key in class_dict:
                    counter = 1
                    while f"{seq_key}_{counter}" in class_dict:
                        counter += 1
                    seq_key = f"{seq_key}_{counter}"

                ipv4_dict = class_dict.setdefault(seq_key, {})
                current_key_mask = ipv4_dict
                continue

            # ipv4_src: value = 0.0.0.0       mask = 0.0.0.0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ipv4_dict["ipv4_src_value"] = group["ipv4_src_value"]
                ipv4_dict["ipv4_src_mask"] = group["ipv4_src_mask"]
                continue

            # ipv4_dst: value = 0.0.0.0       mask = 0.0.0.0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ipv4_dict["ipv4_dst_value"] = group["ipv4_dst_value"]
                ipv4_dict["ipv4_dst_mask"] = group["ipv4_dst_mask"]
                continue

            # IPV6 ACE Key/Mask
            m = p8_1.match(line)
            if m:
                key_base = 'ipv6_ace_key_mask'
                seq_key = key_base

                if seq_key in class_dict:
                    counter = 1
                    while f"{seq_key}_{counter}" in class_dict:
                        counter += 1
                    seq_key = f"{seq_key}_{counter}"

                ipv6_dict = class_dict.setdefault(seq_key, {})
                current_key_mask = ipv6_dict
                continue

            # src_mac: value = 0x0.0x0.0x0.0x0.0x0.0x0
            m = p9_1.match(line)
            if m:
                group = m.groupdict()
                ipv6_dict["ipv6_src_mac_value"] = group["ipv6_src_mac_value"]
                current_mac = 'src_mac'
                continue

            # mask = 0x0.0x0.0x0.0x0.0x0.0x0
            m = p9_1_1.match(line)
            if m and current_mac == 'src_mac':
                group = m.groupdict()
                ipv6_dict["ipv6_src_mac_mask"] = group["ipv6_src_mac_mask"]
                current_mac = None
                continue

            # dst_mac: value = 0x0.0x0.0x0.0x0.0x0.0x0
            m = p10_1.match(line)
            if m:
                group = m.groupdict()
                ipv6_dict["ipv6_dst_mac_value"] = group["ipv6_dst_mac_value"]
                current_mac = 'dst_mac'
                continue

            # mask = 0x0.0x0.0x0.0x0.0x0.0x0
            m = p10_1_1.match(line)
            if m and current_mac == 'dst_mac':
                group = m.groupdict()
                ipv6_dict["ipv6_dst_mac_value"] = group["ipv6_dst_mac_mask"]
                current_mac = None
                continue

            # V:  0x0       0x0      0x0         0x0       0x0           0x0          0x0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                if current_protocol == 'IPv4':
                    pro_type_dict = ipv4_dict.setdefault(group["pro_type"], {})
                else:
                    pro_type_dict = ipv6_dict.setdefault(group["pro_type"], {})
                pro_type_dict['proto'] = group["proto"]
                pro_type_dict['tos'] = group["tos"]
                pro_type_dict['tcp_flg'] = group["tcp_flg"]
                pro_type_dict['ttl'] = group["ttl"]
                pro_type_dict['ipv4_flags'] = group["ipv4_flags"]
                pro_type_dict['src_port'] = group["src_port"]
                pro_type_dict['dst_port'] = group["dst_port"]
                continue

            # V:  0x0       0x0      0x0         0x0       0x0           0x0          0x0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                if current_protocol == 'IPv6':
                    pro_type_dict = ipv6_dict.setdefault(group["pro_type"], {})
                else:
                    pro_type_dict = ipv4_dict.setdefault(group["pro_type"], {})
                pro_type_dict['ext_h'] = group["ext_h"]
                pro_type_dict['tos'] = group["tos"]
                pro_type_dict['tcp_flg'] = group["tcp_flg"]
                pro_type_dict['ttl'] = group["ttl"]
                pro_type_dict['ipv4_flags'] = group["ipv4_flags"]
                pro_type_dict['src_port'] = group["src_port"]
                pro_type_dict['dst_port'] = group["dst_port"]
                continue

            # Result Action
            m = p13.match(line)
            if m:
                # No action needed, just sets context for p14 to follow
                continue

            # Punt : N    Drop : N    Mirror: N    Counter: 0x0 (0)
            m = p14.match(line)
            if m:
                group = m.groupdict()
                if current_key_mask is not None:
                    current_key_mask['result_actions'] = {
                        'punt': group["punt"],
                        'drop': group["drop"],
                        'mirror': group["mirror"],
                        'counter': group["counter"],
                        'counter_value': int(group["counter_value"])
                    }
                continue

            # Punt: Y    Drop: N    Mir: N    Mir_Cum: 0x0   Mir_cmd: 0x0    Counter: 0x7bb (0)
            m = p15.match(line)
            if m:
                group = m.groupdict()
                if current_key_mask is not None:
                    current_key_mask['result_actions'] = {
                        'punt': group["punt"],
                        'drop': group["drop"],
                        'mirror': group["mirror"],
                        'mir_cum': group["mir_cum"],
                        'mir_cmd': group["mir_cmd"],
                        'counter': group["counter"],
                        'counter_value': int(group["counter_value"])
                    }
                continue

        return parsed_dict


class ShowPlatformsoftwareFedActiveXcvrLpnLinkstatusSchema(MetaParser):
    """Schema for show platform software fed {switch} {mode} xcvr lpn {lpn_value} link_status"""

    schema = {
        'xcvr_link_status': {
            'link_state': str,
            'link_resets_count_on_port': int,
        },
   }

class ShowPlatformsoftwareFedActiveXcvrLpnLinkstatus(
    ShowPlatformsoftwareFedActiveXcvrLpnLinkstatusSchema):
    """
    show platform software fed {switch} {mode} xcvr lpn {lpn_value} link_status
    """

    cli_command = ['show platform software fed {switch} {mode} xcvr lpn {lpn_value} link_status',
                    'show platform software fed {mode} xcvr lpn {lpn_value} link_status']

    def cli(self, mode, lpn_value, switch=None, output=None):

        if output is None:
            if switch:
                output = self.device.execute(self.cli_command[0].format(switch=switch, mode=mode, lpn_value=lpn_value))
            else:
                output = self.device.execute(self.cli_command[1].format(mode=mode, lpn_value=lpn_value))

        ret_dict = {}

        # XCVR Link Status
        p1 = re.compile(r'^XCVR +Link +Status +\:$')

        # link state: UP
        p2 =  re.compile(r'^link +state\:(?P<link_state>.*)$')

        # Link Resets Count on port: 0
        p3 = re.compile(r'^Link +Resets +Count +on +port\:\s*(?P<link_resets_count_on_port>\d+)$')


        for line in output.splitlines():
            line = line.strip()

            # XCVR Link Status
            m = p1.match(line)
            if m:
                curr_dict = ret_dict.setdefault('xcvr_link_status', {})
                continue

            # link state: UP
            m = p2.match(line)
            if m:
                group = m.groupdict()
                curr_dict['link_state'] = group['link_state']
                continue

            # Link Resets Count on port: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                curr_dict['link_resets_count_on_port']  = int(group['link_resets_count_on_port'])
                continue

        return ret_dict


class ShowPlatformSoftwareFedSwitchActiveSecurityFedSisfStatisticsSchema(MetaParser):
    # Schema for 'show platform software fed switch active security-fed sisf statistics'
    schema = {
        'punject_punt_entries': {
            'oids': {
                Any(): {
                    'name': str,
                    'packets_hits': int
                }
            }
        }
    }

class ShowPlatformSoftwareFedSwitchActiveSecurityFedSisfStatistics(ShowPlatformSoftwareFedSwitchActiveSecurityFedSisfStatisticsSchema):
    # Parser for 'show platform software fed switch active security-fed sisf statistics'
    cli_command = [
        'show platform software fed switch {switch_var} security-fed sisf statistics',
        'show platform software fed switch {switch_var} security-fed sisf statistics {clear}']

    def cli(self, switch_var="", clear="", output=None):
        if output is None:
            if clear:
                cmd = self.cli_command[1].format(switch_var=switch_var, clear=clear)
            else:
                cmd = self.cli_command[0].format(switch_var=switch_var)
            output = self.device.execute(cmd)

        parsed_dict = {}

        # Name                              OID       Packets Hits
        # DHCPV6 SERVER TO ANY on PORT      558       0
        p1 = re.compile(r'^(?P<name>[\w\s]+?)\s+(?P<oid>\d+)\s+(?P<packets_hits>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Name                              OID       Packets Hits
            # DHCPV6 SERVER TO ANY on PORT      558       0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                result_dict=parsed_dict.setdefault('punject_punt_entries',{}).setdefault('oids',{}).setdefault(int(group['oid']),{})
                result_dict['name']=group['name']
                result_dict['packets_hits']=int(group['packets_hits'])
                continue

        return parsed_dict


class ShowPlatformSoftwareFedActiveIpUrpfSchema(MetaParser):
    """
        show platform software fed switch active ip urpf
    """
    schema = {
        'interface': {
            Any(): {
                'interface_id': str,
                'allow_default': str,
                Optional('flags'): str,
                Optional('urpf_mode'): str,
                Optional('allow_self_ping'): str,
                Optional('af'): str,
                Optional('acl_name'): str
            }
        }
    }


class ShowPlatformSoftwareFedActiveIpUrpf(ShowPlatformSoftwareFedActiveIpUrpfSchema):
    """
        show platform software fed switch active ip urpf
    """
    cli_command = ['show platform software fed active ip urpf',
                   'show platform software fed switch {mode} ip urpf']

    def cli(self, mode=None, output=None):
        if output is None:
            if mode:
                cli = self.cli_command[1].format(mode=mode)
            else:
                cli = self.cli_command[0]
            output = self.device.execute(cli)

        # Associated intfc name Vlan2
        p1 = re.compile(r'^Associated intfc name (?P<interface>\S+)$')

        # Vlan2: [0x4c1]
        p1_1 = re.compile(r'^(?P<interface>\S+)\: \[(?P<interface_id>.+)\]$')

        # Associated intfc id 223
        p1_2 = re.compile(r'^Associated intfc id (?P<interface_id>\d+)$')

        # Allow Default: Yes
        p2 = re.compile(r'^Allow.+Default\:\:* (?P<allow_default>\S+)$')

        # Flags:: 0x0
        p3 = re.compile(r'^Flags\:\:\s*(?P<flags>.+)$')

        # uRPF Mode: STRICT
        p4 = re.compile(r'^uRPF Mode\:\s*(?P<urpf_mode>.+)$')

        # Allow Self Ping: Yes
        p5 = re.compile(r'^Allow Self Ping\:\s*(?P<allow_self_ping>.+)$')

        # AF:: IPv4
        p6 = re.compile(r'^AF\:\:\s*(?P<af>.+)$')

        # ACL name:
        p7 = re.compile(r'^ACL name\:\s*(?P<acl_name>.+)$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Associated intfc name Vlan2
            m = p1.match(line)
            if m:
                intf_dict = ret_dict.setdefault('interface', {}).setdefault(Common.convert_intf_name(m.group('interface')), {})
                continue

            # Vlan2: [0x4c1]
            m = p1_1.match(line)
            if m:
                intf_dict = ret_dict.setdefault('interface', {}).setdefault(Common.convert_intf_name(m.group('interface')), {})
                intf_dict['interface_id'] = m.group('interface_id')
                continue

            # Associated intfc id 223
            m = p1_2.match(line)
            if m:
                intf_dict['interface_id'] = m.group('interface_id')
                continue

            # Allow Default: Yes
            m = p2.match(line)
            if m:
                intf_dict['allow_default'] = m.group('allow_default')
                continue

            # Flags:: 0x0
            m = p3.match(line)
            if m:
                intf_dict['flags'] = m.group('flags')
                continue

            # uRPF Mode: STRICT
            m = p4.match(line)
            if m:
                intf_dict['urpf_mode'] = m.group('urpf_mode')
                continue

            # Allow Self Ping: Yes
            m = p5.match(line)
            if m:
                intf_dict['allow_self_ping'] = m.group('allow_self_ping')
                continue

            # AF:: IPv4
            m = p6.match(line)
            if m:
                intf_dict['af'] = m.group('af')
                continue

            # ACL name:
            m = p7.match(line)
            if m:
                intf_dict['acl_name'] = m.group('acl_name')
                continue

        return ret_dict

class ShowPlatformSoftwareFedSwitchActiveifmMappingsgidSchema(MetaParser):
    """Schema for show platform software fed switch active ifm mappings gid gid_num"""

    schema = {
        'interface': {
            Any(): {
                'gid': int,
                'if_id': str,
                'if_type': str
            }
        }
    }

class ShowPlatformSoftwareFedSwitchActiveifmMappingsgid(ShowPlatformSoftwareFedSwitchActiveifmMappingsgidSchema):

    """Parser for show platform software fed switch active ifm mappings gid gid_num"""

    cli_command = "show platform software fed switch {switch} ifm mappings gid {gid_num}"

    def cli(self, switch, gid_num, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch=switch,gid_num=gid_num))

        ret_dict = {}

        # GID         Interface                         IF_ID               Type
        # -------------------------------------------------------------------------------------------
        # 122880      GigabitEthernet1/0/1              0x00000408          ETHER
        # 122881      GigabitEthernet1/0/2              0x00000409          ETHER
        # 122882      GigabitEthernet1/0/3              0x0000040a          ETHER

        p1 = re.compile(r"^(?P<gid>\d+)\s+(?P<interface>\S+)\s+(?P<if_id>\w+)\s+(?P<if_type>\w+)$")

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault('interface', {}).setdefault(group['interface'],{})
                root_dict['gid']=int(group['gid'])
                root_dict['if_id']=group['if_id']
                root_dict['if_type']=group['if_type']
                continue

        return ret_dict

class ShowPlatformSoftwareFedSwitchActiveCpuInterfacesSchema(MetaParser):
    """Schema for show platform software fed switch active cpu-interfaces """

    schema = {
        "queue": {
            Any(): {
                "retrieved": int,
                "dropped": int,
                "invalid": int,
                "hol_block": int,
            }
        }
    }

class ShowPlatformSoftwareFedSwitchActiveCpuInterfaces(ShowPlatformSoftwareFedSwitchActiveCpuInterfacesSchema):
    """parser for cli 'show platform software fed switch active cpu-interfaces'"""

    cli_command = ["show platform software fed active cpu-interface",
                   "show platform software fed {switch} active cpu-interface"]

    def cli(self, switch=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[1].format(switch=switch)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        #initial return dictionary
        ret_dict = {}

        # Matching patterns
        #   queue                 retrieved   dropped     invalid    hol-block
        # -------------------------------------------------------------------------
        #  Routing Protocol           15579       0           0           0
        #  L2 Protocol                361037      0           0           0
        #  sw forwarding              113         0           0           0

        p1 = re.compile(r"^(?P<queue>[A-Za-z0-9\- ]+?)\s+(?P<retrieved>\d+)\s+(?P<dropped>\d+)\s+(?P<invalid>\d+)\s+(?P<hol_block>\d+)$")

        for line in output.splitlines():
            line.strip()

            # Routing Protocol           15579       0           0           0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                queue_name = group['queue'].strip()
                queue_dict = (
                    ret_dict.setdefault("queue", {}).setdefault(group['queue'], {})
                )
                queue_dict.update(
                    {
                        "retrieved" : int(group["retrieved"]),
                        "dropped" : int(group["dropped"]),
                        "invalid" : int(group["invalid"]),
                        "hol_block" : int(group["hol_block"])
                    }
                )
        return ret_dict

class ShowPlatformSoftwareFedSwitchActiveIfmMappingsL3if_leSchema(MetaParser):
    """
        Schema for 'show platform software fed switch active ifm mappings l3if-le'
    """
    schema = {
        'interface': {
            Any(): {
                "l3if_le": str,
                "if_id": str,
                "type": str,
            }
        }
    }

class ShowPlatformSoftwareFedSwitchActiveIfmMappingsL3if_le(ShowPlatformSoftwareFedSwitchActiveIfmMappingsL3if_leSchema):
    cli_command = ["show platform software fed active ifm mappings l3if-le",
                   "show platform software fed {switch} active ifm mappings l3if-le"]

    def cli(self, switch=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[1].format(switch=switch)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        ret_dict = {}

        # Regex pattern to match the output lines
        # 0x000077ba149b9748 Vlan1   0x000000fa   SVI_L3_LE
        p1 = re.compile(r"^(?P<l3if_le>0x[0-9a-fA-F]+)\s+(?P<interface>\S+)\s+(?P<if_id>0x[0-9a-fA-F]+)\s+(?P<type>\S+)$")

        for line in output.splitlines():
            line = line.strip()

            # 0x000077ba149b9748 Vlan1 0x000000fa SVI_L3_LE
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface_dict = ret_dict.setdefault('interface', {}).setdefault(group['interface'], {})
                interface_dict.update(
                    {
                        "l3if_le": group["l3if_le"],
                        "if_id": group["if_id"],
                        "type": group["type"],
                    }
                )
                continue
        return ret_dict

class ShowPlatformSoftwareFedSwitchActiveIfmMappingsGpnSchema(MetaParser):
    """schema for 'show platform software fed switch active ifm mappings gpn'"""

    schema = {
       "gpn":{
            Any():{
                "interface": str,
                "if_id": str,
                "if_type": str,
            }
       }
    }


class ShowPlatformSoftwareFedSwitchActiveIfmMappingsGpn(ShowPlatformSoftwareFedSwitchActiveIfmMappingsGpnSchema):
    """parser for cli 'show platform software fed switch active ifm mappings gpn'"""

    cli_command = ["show platform software fed active ifm mappings gpn",
                   "show platform software fed {switch} {mode} ifm mappings gpn"]

    def cli(self, switch=None, mode='active', output = None):
        if output is None:
            if switch:
                cmd = self.cli_command[1].format(switch=switch, mode=mode)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)


        ret_dict = {}

        #GPN         Interface                         IF_ID               IF_TYPE
        #1           FortyGigabitEthernet1/0/1         0x00000009          ETHER

        p1 = re.compile(r"^(?P<gpn>\d+)\s+(?P<interface>\S+)\s+(?P<if_id>\S+)\s+(?P<if_type>\S+)$")

        for line in output.splitlines():
            line = line.strip()

            # 1 FortyGigabitEthernet1/0/1 0x00000009 ETHER
            m = p1.match(line)
            if m:
                group = m.groupdict()
                gpn_dict = ret_dict.setdefault("gpn", {}).setdefault(group['gpn'], {})

                gpn_dict.update(
                    {
                        "interface" : group["interface"],
                        "if_id" : group["if_id"],
                        "if_type" : group["if_type"],
                    }
                )
                continue

        return ret_dict


class ShowPlatformSoftwareFedSwitchActiveAclBindSdkDetailSchema(MetaParser):
    """Schema for
        show platform software fed {switch} {switch_var} acl {acl} sdk detail,
        show platform software fed {switch} {switch_var} acl {acl} sdk feature {feature_name} dir {dir} cgid {cg_id} detail,
        show platform software fed {switch} {switch_var} acl {acl} sdk feature {feature_name} dir {dir} detail asic {asic_no},
        show platform software fed {switch} {switch_var} acl {acl} sdk feature {feature_name} detail,
        show platform software fed {switch} {switch_var} acl {acl} sdk if-id {if_id} detail.
    """
    schema = {
        'interface_class_name': {
            Any(): {
                'direction': str,
                'feature': str,
                'protocol': str,
                'cg_id': int,
                Optional('cg_name'): str,
                Optional('pol_hdl'): str,
                Optional('oid'): str,
                Optional('no_of_ace'): int,
                Any(): {
                    'ipv4_src_value': str,
                    'ipv4_src_mask': str,
                    'ipv4_dst_value': str,
                    'ipv4_dst_mask': str,
                    Any(): {
                        'proto': str,
                        'tos': str,
                        'tcp_flg': str,
                        'ttl': str,
                        'ipv4_flags': str,
                        'src_port': str,
                        'dst_port': str
                    },
                    'result_actions': {
                        'punt': str,
                        'drop': str,
                        'mirror': str,
                        'counter': str,
                        'counter_value': int
                    }
                }
            }
        }
    }

class ShowPlatformSoftwareFedSwitchActiveAclBindSdkDetail(ShowPlatformSoftwareFedSwitchActiveAclBindSdkDetailSchema):
    """Parser for
        show platform software fed {switch} {switch_var} acl {acl} sdk detail,
        show platform software fed {switch} {switch_var} acl {acl} sdk feature {feature_name} dir {dir} cgid {cg_id} detail,
        show platform software fed {switch} {switch_var} acl {acl} sdk feature {feature_name} dir {dir} detail asic {asic_no},
        show platform software fed {switch} {switch_var} acl {acl} sdk feature {feature_name} detail,
        show platform software fed {switch} {switch_var} acl {acl} sdk if-id {if_id} detail.
    """

    cli_command = ['show platform software fed {switch} {switch_var} acl {acl} sdk detail',
        'show platform software fed {switch} {switch_var} acl {acl} sdk feature {feature_name} dir {dir} cgid {cg_id} detail',
        'show platform software fed {switch} {switch_var} acl {acl} sdk feature {feature_name} dir {dir} detail asic {asic_no}',
        'show platform software fed {switch} {switch_var} acl {acl} sdk feature {feature_name} detail',
        'show platform software fed {switch} {switch_var} acl {acl} sdk if-id {if_id} detail']

    def cli(self, switch=None, switch_var=None, acl=None, feature_name=None, dir=None, cg_id=None, asic_no=None, if_id=None, output=None):
        if output is None:
            if switch_var and acl and feature_name and cg_id:
                cmd = self.cli_command[1].format(switch=switch, switch_var=switch_var, acl=acl, feature_name=feature_name, dir=dir, cg_id=cg_id)

            elif switch_var and acl and feature_name and asic_no:
                cmd = self.cli_command[2].format(switch=switch, switch_var=switch_var, acl=acl, feature_name=feature_name, dir=dir, asic_no=asic_no)

            elif switch_var and acl and feature_name:
                cmd = self.cli_command[3].format(switch=switch, switch_var=switch_var, acl=acl, feature_name=feature_name)

            elif switch_var and acl and if_id:
                cmd = self.cli_command[4].format(switch=switch, switch_var=switch_var, acl=acl, if_id=if_id)

            elif switch_var and acl:
                cmd = self.cli_command[0].format(switch=switch, switch_var=switch_var, acl=acl)

            else:
                cmd = None

            output = self.device.execute(cmd)

        # Initialize the parsed dictionary
        ret_dict = {}
        current_key_mask = None

        # Interface Name: Gi2/0/31
        p1 = re.compile(r'^Interface Name:\s+(?P<interface_name>\S+)$')

        # Class Group Name: implicit_deny:xACSACLx-IP-PERMIT_ALL_IPV4_TRAFFIC-57f6b0d3:
        p1_1 = re.compile(r'^Class Group Name:\s+(?P<class_group_name>[\S]+)$')

        # Direction: Ingress
        p2 = re.compile(r'^Direction:\s+(?P<direction>\S+)$')

        # Feature         : Pacl
        p3 = re.compile(r'^Feature\s+:\s+(?P<feature>\S+)$')

        # Protocol        : IPv4
        p4 = re.compile(r'^Protocol\s+:\s+(?P<protocol>\S+)$')

        # CG ID           : 19
        p5 = re.compile(r'^CG ID\s+:\s+(?P<cg_id>\d+)$')

        # CG Name         : pre-auth
        p6 = re.compile(r'^CG Name\s+:\s+(?P<cg_name>\S+)$')

        # Pol Hdl         : 0x24073568
        p6_1 = re.compile(r'^Pol Hdl\s+:\s+(?P<pol_hdl>\S+)$')

        # ACL (OID: 0xB17, No of ACEs: 12)
        p7 = re.compile(r'^ACL\s+\(OID:\s+(?P<oid>\S+),\s+No\s+of\s+ACEs:\s+(?P<no_of_ace>\d+)\)$')

        # IPV4 ACE Key/Mask
        p8 = re.compile(r'^IPV4 ACE Key/Mask$')

        # ipv4_src: value = 0.0.0.0       mask = 0.0.0.0
        p9 = re.compile(r'ipv4_src:\s+value\s+=\s+(?P<ipv4_src_value>\S+)\s+mask\s+=\s+(?P<ipv4_src_mask>\S+)')

        # ipv4_dst: value = 0.0.0.0       mask = 0.0.0.0
        p10 = re.compile(r'ipv4_dst:\s+value\s+=\s+(?P<ipv4_dst_value>\S+)\s+mask\s+=\s+(?P<ipv4_dst_mask>\S+)')

        # V:  0x11       0x0      0x0         0x0       0x0           0x44          0x43
        p11 = re.compile(r'^(?P<pro_type>[VM])\s*:\s+(?P<proto>\S+)\s+(?P<tos>\S+)\s+(?P<tcp_flg>\S+)\s+(?P<ttl>\S+)\s+(?P<ipv4_flags>\S+)\s+(?P<src_port>\S+)\s+(?P<dst_port>\S+)$')

        # Result Action
        p12 = re.compile(r'^Result Action$')

        # Punt : N    Drop : N    Mirror: N    Counter: 0x0 (0)
        p13 = re.compile(r'^Punt\s*:\s*(?P<punt>\S+)\s+Drop\s*:\s*(?P<drop>\S+)\s+Mirror\s*:\s*(?P<mirror>\S+)\s+Counter:\s*(?P<counter>\S+)\s*\((?P<counter_value>\d+)\)$')

        for line in output.splitlines():
            line = line.strip()

            # Interface Name: Gi2/0/31
            m = p1.match(line)
            if m:
                group = m.groupdict()
                int_dict = ret_dict.setdefault("interface_class_name", {}).setdefault(group["interface_name"], {})
                continue

            # Class Group Name: implicit_deny:xACSACLx-IP-PERMIT_ALL_IPV4_TRAFFIC-57f6b0d3:
            m = p1_1.match(line)
            if m:
                group = m.groupdict()
                int_dict = ret_dict.setdefault("interface_class_name", {}).setdefault(group["class_group_name"], {})
                continue

            # Direction: Ingress
            m = p2.match(line)
            if m:
                group = m.groupdict()
                int_dict["direction"] = group["direction"]
                continue

            # Feature         : Pacl
            m = p3.match(line)
            if m:
                group = m.groupdict()
                int_dict["feature"] = group["feature"]
                continue

            # Protocol        : IPv4
            m = p4.match(line)
            if m:
                group = m.groupdict()
                int_dict["protocol"] = group["protocol"]
                continue

            # CG ID           : 19
            m = p5.match(line)
            if m:
                group = m.groupdict()
                int_dict["cg_id"] = int(group["cg_id"])
                continue

            # CG Name         : pre-auth
            m = p6.match(line)
            if m:
                group = m.groupdict()
                int_dict["cg_name"] = group["cg_name"]
                continue

            # Pol Hdl         : 0x24073568
            m = p6_1.match(line)
            if m:
                group = m.groupdict()
                int_dict["pol_hdl"] = group["pol_hdl"]
                continue

            # ACL (OID: 0xB17, No of ACEs: 12)
            m = p7.match(line)
            if m:
                group = m.groupdict()
                int_dict["oid"] = group["oid"]
                int_dict["no_of_ace"] = int(group["no_of_ace"])
                continue

            # IPV4 ACE Key/Mask
            m = p8.match(line)
            if m:
                if 'ipv4_ace_key_mask' not in int_dict:
                    seq_key = 'ipv4_ace_key_mask'
                else:
                    existing_keys = [key for key in int_dict if key.startswith('ipv4_ace_key_mask_')]
                    next_suffix = len(existing_keys) + 1
                    seq_key = f"ipv4_ace_key_mask_{next_suffix}"

                ipv4_dict = int_dict.setdefault(seq_key, {})
                current_key_mask = ipv4_dict
                continue

            # ipv4_src: value = 0.0.0.0       mask = 0.0.0.0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ipv4_dict["ipv4_src_value"] = group["ipv4_src_value"]
                ipv4_dict["ipv4_src_mask"] = group["ipv4_src_mask"]
                continue

            # ipv4_dst: value = 0.0.0.0       mask = 0.0.0.0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ipv4_dict["ipv4_dst_value"] = group["ipv4_dst_value"]
                ipv4_dict["ipv4_dst_mask"] = group["ipv4_dst_mask"]
                continue

            # V:  0x11       0x0      0x0         0x0       0x0           0x44          0x43
            m = p11.match(line)
            if m:
                group = m.groupdict()
                pro_type_dict = ipv4_dict.setdefault(group["pro_type"],{})
                pro_type_dict['proto']=group["proto"]
                pro_type_dict['tos']=group["tos"]
                pro_type_dict['tcp_flg']=group["tcp_flg"]
                pro_type_dict['ttl']=group["ttl"]
                pro_type_dict['ipv4_flags']=group["ipv4_flags"]
                pro_type_dict['src_port']=group["src_port"]
                pro_type_dict['dst_port']=group["dst_port"]
                continue

            # Result Action
            m = p12.match(line)
            if m:
                # No action needed, just sets context for p14 to follow
                continue

            # Punt : N    Drop : N    Mirror: N    Counter: 0x0 (0)
            m = p13.match(line)
            if m:
                group = m.groupdict()
                if current_key_mask is not None:
                    current_key_mask['result_actions'] = {
                        'punt': group["punt"],
                        'drop': group["drop"],
                        'mirror': group["mirror"],
                        'counter': group["counter"],
                        'counter_value': int(group["counter_value"])
                    }
                continue

        return ret_dict


class ShowPlatformSoftwareFedSwitchActiveAclBindSdkfeatureCgaclDetailSchema(MetaParser):
    """Schema for
       'show platform software fed switch active acl bind sdk feature cgacl detail'
    """

    schema = {
        'interfaces': {
            Any(): {
                'bindings': ListOf({
                    'direction': str,
                    'feature': str,
                    'protocol': str,
                    'cg_id': int,
                    'cg_name': str,
                    'status': str,
                    'src_og_lkup_hdl': int,
                    'dst_og_lkup_hdl': int,
                })
            }
        }
    }

class ShowPlatformSoftwareFedSwitchActiveAclBindSdkfeatureCgaclDetail(ShowPlatformSoftwareFedSwitchActiveAclBindSdkfeatureCgaclDetailSchema):
    """ Parser for
    * 'show platform software fed switch active acl bind sdk feature cgacl detail'
    """

    cli_command = 'Show platform software fed switch active acl bind sdk feature cgacl detail'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # Interface Name: Gi2/0/10
        p1 = re.compile(r'^Interface Name: (?P<interface_name>\S+)$')

        # Direction: Ingress
        p2 = re.compile(r'^Direction: (?P<direction>\S+)$')

        # Feature         : Pacl
        p3 = re.compile(r'^Feature\s+: (?P<feature>\S+)$')

        # Protocol        : MAC
        p4 = re.compile(r'^Protocol\s+: (?P<protocol>\S+)$')

        # CG ID           : 1
        p5 = re.compile(r'^CG ID\s+: (?P<cg_id>\d+)$')

        # CG Name         : pacl_mac
        p6 = re.compile(r'^CG Name\s+: (?P<cg_name>\S+)$')

        # Status          : Success
        p7 = re.compile(r'^Status\s+: (?P<status>\S+)$')

        # Src_og_lkup_hdl : 0
        p8 = re.compile(r'^Src_og_lkup_hdl\s+: (?P<src_og_lkup_hdl>\d+)$')

        # Dst_og_lkup_hdl : 0
        p9 = re.compile(r'^Dst_og_lkup_hdl\s+: (?P<dst_og_lkup_hdl>\d+)$')

        current_interface = None
        current_direction = None
        binding = None

        for line in output.splitlines():
            line = line.strip()

            # Interface Name: Gi2/0/10
            m = p1.match(line)
            if m:
                interface_name = m.group('interface_name')
                current_interface = interface_name
                intf_dict = ret_dict.setdefault('interfaces', {})
                intf_dict.setdefault(interface_name, {}).setdefault('bindings', [])
                continue

            # Direction: Ingress
            m = p2.match(line)
            if m:
                current_direction = m.group('direction').lower()
                continue

            # Feature         : Pacl
            m = p3.match(line)
            if m:
                binding = {'feature': m.group('feature'), 'direction': current_direction}
                ret_dict['interfaces'][current_interface]['bindings'].append(binding)
                continue

            # Protocol        : MAC
            m = p4.match(line)
            if m:
                binding['protocol'] = m.group('protocol')
                continue

            # CG ID           : 1
            m = p5.match(line)
            if m:
                binding['cg_id'] = int(m.group('cg_id'))
                continue

            # CG Name         : pacl_mac
            m = p6.match(line)
            if m:
                binding['cg_name'] = m.group('cg_name')
                continue

            # Status          : Success
            m = p7.match(line)
            if m:
                binding['status'] = m.group('status')
                continue

            # Src_og_lkup_hdl : 0
            m = p8.match(line)
            if m:
                binding['src_og_lkup_hdl'] = int(m.group('src_og_lkup_hdl'))
                continue

            # Dst_og_lkup_hdl : 0
            m = p9.match(line)
            if m:
                binding['dst_og_lkup_hdl'] = int(m.group('dst_og_lkup_hdl'))
                continue

        return ret_dict

class ShowPlatformSoftwareFedSwitchActiveIfmMappingsSchema(MetaParser):
    """schema for Show
        platform software fed switch active ifm mappings l2-attachment-circuit
        platform software fed switch active ifm mappings l3-attachment-circuit
        platform software fed switch active ifm mappings system-port
    """

    schema = {
        'interface': {
            Any(): {
                'gid': int,
                'if_id': str,
                'if_type': str
            }
        }
    }

class ShowPlatformSoftwareFedSwitchActiveIfmMappings(ShowPlatformSoftwareFedSwitchActiveIfmMappingsSchema):
    """Parser for show
        platform software fed switch active ifm mappings l2-attachment-circuit
        platform software fed switch active ifm mappings l3-attachment-circuit
        platform software fed switch active ifm mappings system-port
    """

    cli_command = "show platform software fed switch {switch} ifm mappings {ifm_type}"

    def cli(self, switch, ifm_type, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch=switch, ifm_type=ifm_type))

        ret_dict = {}

        # GID         Interface                         IF_ID               Type
        # -------------------------------------------------------------------------------------------
        # 122880      GigabitEthernet1/0/1              0x00000408          ETHER
        # 122881      GigabitEthernet1/0/2              0x00000409          ETHER
        # 122882      GigabitEthernet1/0/3              0x0000040a          ETHER

        p1 = re.compile(r"^(?P<gid>\d+)\s+(?P<interface>\S+)\s+(?P<if_id>\w+)\s+(?P<if_type>\w+)$")
        for line in output.splitlines():
            line = line.strip()

            # GID         Interface                         IF_ID               Type
            # -------------------------------------------------------------------------------------------
            # 122880      GigabitEthernet1/0/1              0x00000408          ETHER
            # 122881      GigabitEthernet1/0/2              0x00000409          ETHER
            # 122882      GigabitEthernet1/0/3              0x0000040a          ETHER
            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault('interface', {}).setdefault(group['interface'],{})
                root_dict['gid']=int(group['gid'])
                root_dict['if_id']=group['if_id']
                root_dict['if_type']=group['if_type']
                continue

        return ret_dict

class ShowPlatoformSoftwareFedSwitchActiveInsightNplTableSchema(MetaParser):
    """
    Parser for show platform hard fed switch {switch_type} fwd-asic insight npl_table{table_name}
    """
    schema = {
        'entries': {
            Any(): {
                Optional('key'): {
                    Optional('get_field_by_name'): str,
                    Optional('port'): {
                        Optional('id'): str,
                        Optional('smac'): str,
                        Optional('vid'): str,
                    },
                },
                Optional('mask'): {
                    Optional('get_field_by_name'): str,
                    Optional('port'): {
                        Optional('id'): str,
                        Optional('smac'): str,
                        Optional('vid'): str,
                    },
                },
                Optional('loc'): str,
                Optional('value'): {
                    Optional('action'): str,
                    Optional('payloads'): {
                        Optional('result_table'): {
                            Optional('client_policy_id'): str,
                            Optional('client_vlan'): str,
                            Optional('drop'): str,
                            Optional('ipv4_policy_valid'): str,
                            Optional('ipv6_policy_valid'): str,
                            Optional('vlan_overwrite'): str,
                        }
                    }
                }
            }
        }
    }

class ShowPlatoformSoftwareFedSwitchActiveInsightNplTable(ShowPlatoformSoftwareFedSwitchActiveInsightNplTableSchema):
    """
    Parser for show platform hard fed switch {switch_type} fwd-asic insight npl_table{table_name}
    """
    cli_command = "show platform hardware fed switch {switch_type} fwd-asic insight npl_table{table_name}"

    def cli(self, switch_type, table_name ,output=None):
        if output is None:
            cmd = self.cli_command.format(switch_type=switch_type,table_name=table_name)
        output = self.device.execute(cmd)

        result_dict = {}

        # - # 1
        p1 = re.compile(r'^- # (?P<entry_num>\d+)$')

        # get_field_by_name: =<bound method npl_dot1x_client_table_key_t.get_field_by_name
        p22 = re.compile(r"get_field_by_name:\s*=\s*(?P<get_field_by_name>[\s\S]+?)(?=port:|mask:|key:|$)")

        # id: =0x38
        p3 = re.compile(r"^id:\s*=\s*(?P<id>0x[0-9a-fA-F]+)$")

        # smac: =0x222222
        p4 = re.compile(r"^smac:\s*=\s*(?P<smac>0x[0-9a-fA-F]+)$")

        # vid: =0x0
        p5 = re.compile(r"^vid:\s*=\s*(?P<vid>0x[0-9a-fA-F]+)$")

        # loc: =0x0
        p6 = re.compile(r"^loc:\s*=\s*(?P<loc>0x[0-9a-fA-F]+)$")

        # action: NPL_DOT1X_CLIENT_TABLE_ACTION_WRITE(0x0)
        p7 = re.compile(r"^action:\s*(?P<action>.*)$")

        # client_policy_id: =0x7
        p8 = re.compile(r"^client_policy_id:\s*=\s*(?P<client_policy_id>0x[0-9a-fA-F]+)$")

        # client_vlan: =0x32
        p9 = re.compile(r"^client_vlan:\s*=\s*(?P<client_vlan>0x[0-9a-fA-F]+)$")

        # drop: =0x0
        p10 = re.compile(r"^drop:\s*=\s*(?P<drop>0x[0-9a-fA-F]+)$")

        # ipv4_policy_valid: =0x1
        p11 = re.compile(r"^ipv4_policy_valid:\s*=\s*(?P<ipv4_policy_valid>0x[0-9a-fA-F]+)$")

        # ipv6_policy_valid: =0x1
        p12 = re.compile(r"^ipv6_policy_valid:\s*=\s*(?P<ipv6_policy_valid>0x[0-9a-fA-F]+)$")

        # ipv6_policy_valid: =0x1
        p13 = re.compile(r"^vlan_overwrite:\s*=\s*(?P<vlan_overwrite>0x[0-9a-fA-F]+)$")

        inside_mask = False
        for line in output.splitlines():
            line = line.strip()

            # - # 1
            m = p1.match(line)
            if m:
                entry_num = int(m.group('entry_num'))
                entry_dict = result_dict.setdefault('entries', {}).setdefault(entry_num, {})
                inside_mask = False  # Reset flag
                continue

            # get_field_by_name: =<bound method npl_dot1x_client_table_key_t.get_field_by_name
            m = p22.search(line)
            if m:
                if inside_mask:
                    entry_dict.setdefault('mask', {})['get_field_by_name'] = m.group('get_field_by_name').strip()
                else:
                    entry_dict.setdefault('key', {})['get_field_by_name'] = m.group('get_field_by_name').strip()
                continue

            # Start of 'key' section
            if line.startswith('key:'):
                inside_mask = False
                continue

            # Start of 'mask' section
            if line.startswith('mask:'):
                inside_mask = True
                continue

            # id: =0x38
            m = p3.match(line)
            if m:
                if inside_mask:
                    entry_dict.setdefault('mask', {}).setdefault('port', {})['id'] = m.group('id')
                else:
                    entry_dict.setdefault('key', {}).setdefault('port', {})['id'] = m.group('id')
                continue

            # smac: =0x222222
            m = p4.match(line)
            if m:
                if inside_mask:
                    entry_dict.setdefault('mask', {}).setdefault('port', {})['smac'] = m.group('smac')
                else:
                    entry_dict.setdefault('key', {}).setdefault('port', {})['smac'] = m.group('smac')
                continue

            # vid: =0x0
            m = p5.match(line)
            if m:
                if inside_mask:
                    entry_dict.setdefault('mask', {}).setdefault('port', {})['vid'] = m.group('vid')
                else:
                    entry_dict.setdefault('key', {}).setdefault('port', {})['vid'] = m.group('vid')
                continue

            # vid: =0x0
            m = p6.match(line)
            if m:
                entry_dict['loc'] = m.group('loc')
                continue

            # action: NPL_DOT1X_CLIENT_TABLE_ACTION_WRITE(0x0)
            m = p7.match(line)
            if m:
                entry_dict.setdefault('value', {})['action'] = m.group('action')
                continue

            # client_policy_id: =0x7
            m = p8.match(line)
            if m:
                entry_dict.setdefault('value', {}).setdefault('payloads', {}).setdefault('result_table', {})['client_policy_id'] = m.group('client_policy_id')
                continue

            # client_vlan: =0x32
            m = p9.match(line)
            if m:
                entry_dict.setdefault('value', {}).setdefault('payloads', {}).setdefault('result_table', {})['client_vlan'] = m.group('client_vlan')
                continue

            #  drop: =0x0
            m = p10.match(line)
            if m:
                entry_dict.setdefault('value', {}).setdefault('payloads', {}).setdefault('result_table', {})['drop'] = m.group('drop')
                continue

            # ipv4_policy_valid: =0x1
            m = p11.match(line)
            if m:
                entry_dict.setdefault('value', {}).setdefault('payloads', {}).setdefault('result_table', {})['ipv4_policy_valid'] = m.group('ipv4_policy_valid')
                continue

            # ipv6_policy_valid: =0x1
            m = p12.match(line)
            if m:
                entry_dict.setdefault('value', {}).setdefault('payloads', {}).setdefault('result_table', {})['ipv6_policy_valid'] = m.group('ipv6_policy_valid')
                continue

            # vlan_overwrite: =0x1
            m = p13.match(line)
            if m:
                entry_dict.setdefault('value', {}).setdefault('payloads', {}).setdefault('result_table', {})['vlan_overwrite'] = m.group('vlan_overwrite')
                continue

        return result_dict

class ShowPlatSoftFedSwAcAccessSecurityClientTableMacSchema(MetaParser):
    """Schema for
    show platform software fed active switch access-security mac-client-table summary
    show platform software fed switch <switch_type> access-security mac-client-table interface if-id {port_if_id}
    show platform software fed switch <switch_type> access-security mac-client-table mac {client_mac}
    """

    schema = {
        'mac_client_table_summary': {
            int: {
                'interface': str,
                'mac': str,
                'logical_id': int,
                'position': int,
                'asic': int,
                'auth_act': str,
                'restore_auth_act': str,
                'flag': str,
                'drop': str,
                'ovrd_vlan': int,
                'proto': str,
                'policy_oid': int,
                'packets': int
            }
        }
    }


class ShowPlatSoftFedSwAcAccessSecurityClientTableMac(ShowPlatSoftFedSwAcAccessSecurityClientTableMacSchema):
    """Parser for various show commands related to mac-client-table summary."""

    cli_command = [
        "show platform software fed switch {switch_type} access-security mac-client-table summary",
        "show platform software fed switch {switch_type} access-security mac-client-table interface if-id {port_if_id}",
        "show platform software fed switch {switch_type} access-security mac-client-table mac {client_mac}",
    ]

    def cli(self, switch_type=None, port_if_id=None, client_mac=None, output=None):
        if output is None:
            if switch_type and port_if_id:
                cmd = self.cli_command[1].format(switch_type=switch_type, port_if_id=port_if_id)
            elif switch_type and client_mac:
                cmd = self.cli_command[2].format(switch_type=switch_type, client_mac=client_mac)
            else:
                cmd = self.cli_command[0].format(switch_type=switch_type)
            output = self.device.execute(cmd)

        #      Interface    MAC              Logical-ID Position   Asic# Auth-Act           Restore-Auth-Act   Flag         Drop   Ovrd-VLAN  Policy   Policy-OID Packets
        # ---- ------------ ---------------- ---------- ---------- ----- ------------------ ------------------ ------------ ------ ---------- -------- ---------- ----------
        #    1 Gi2/0/10     0000.0022.2421   0          4096       0     FWD_ALL_LRN_DATA   None               NONE         No     0          NONE     1076       3071
        #    2 Gi2/0/10     0000.0022.23D9   1          4097       0     FWD_ALL_LRN_DATA   None               NONE         No     0          NONE     4244       3064
        p1 = re.compile(
            r'(?P<index>\d+)\s+(?P<interface>\S+)\s+(?P<mac>\S+)\s+'
            r'(?P<logical_id>\d+)\s+(?P<position>\d+)\s+(?P<asic>\d+)\s+'
            r'(?P<auth_act>\S+)\s+(?P<restore_auth_act>\S+)\s+(?P<flag>\S+)\s+'
            r'(?P<drop>\S+)\s+(?P<ovrd_vlan>\d+)\s+(?P<proto>\S+)\s+'
            r'(?P<policy_oid>\d+)\s+(?P<packets>\d+)$'
        )

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                group = m.groupdict()
                index = int(group['index'])

                #      Interface    MAC              Logical-ID Position   Asic# Auth-Act           Restore-Auth-Act   Flag         Drop   Ovrd-VLAN  Policy   Policy-OID Packets
                # ---- ------------ ---------------- ---------- ---------- ----- ------------------ ------------------ ------------ ------ ---------- -------- ---------- ----------
                #    1 Gi2/0/10     0000.0022.2421   0          4096       0     FWD_ALL_LRN_DATA   None               NONE         No     0          NONE     1076       3071
                #    2 Gi2/0/10     0000.0022.23D9   1          4097       0     FWD_ALL_LRN_DATA   None               NONE         No     0          NONE     4244       3064

                if 'mac_client_table_summary' not in ret_dict:
                    ret_dict['mac_client_table_summary'] = {}
                # Populate the dictionary
                ret_dict['mac_client_table_summary'][index] = {
                    'interface': group['interface'],
                    'mac': group['mac'],
                    'logical_id': int(group['logical_id']),
                    'position': int(group['position']),
                    'asic': int(group['asic']),
                    'auth_act': group['auth_act'],
                    'restore_auth_act': group['restore_auth_act'],
                    'flag': group['flag'],
                    'drop': group['drop'],
                    'ovrd_vlan': int(group['ovrd_vlan']),
                    'proto': group['proto'],
                    'policy_oid': int(group['policy_oid']),
                    'packets': int(group['packets']),
                }
                continue  # Move to the next line after processing

        return ret_dict


class ShowPlatformSoftwareFedSwitchActiveEtherchannelLoadbalanceProtocolsSchema(MetaParser):
    """
    Schema for show platform software fed switch {switch} etherchannel {portchannelnum} load-balance {protocol_options}
    """
    schema = {
        'destinationport': str,
    }

class ShowPlatformSoftwareFedSwitchActiveEtherchannelLoadbalanceProtocols(ShowPlatformSoftwareFedSwitchActiveEtherchannelLoadbalanceProtocolsSchema):
    """Parser for 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance {protocol_options}'"""

    cli_command = [
        'show platform software fed switch {switch} etherchannel {portchannelnum} '
        'load-balance ip-fl-nh-port-v6 {sourceipv6} {destinationipv6} {ipv6_fl} '
        '{next_header} {sour_port} {dest_port}',
        'show platform software fed switch {switch} etherchannel {portchannelnum} '
        'load-balance ip-fl-nh-v6 {sourcemac} {destinationmac} {flow_label} {next_header}',
        'show platform software fed switch {switch} etherchannel {portchannelnum} '
        'load-balance ip-protocol-port-v4 {source} {destination} {protocol} {sour_port} '
        '{dest_port}',
        'show platform software fed switch {switch} etherchannel {portchannelnum} '
        'load-balance ip-protocol-v4 {source} {destination} {protocol}',
        'show platform software fed switch {switch} etherchannel {portchannelnum} '
        'load-balance mac-addr {sourcemac}',
        'show platform software fed switch {switch} etherchannel {portchannelnum} '
        'load-balance mac-ip-fl-nh-port-v6 {sourcemac} {sourceipv6} {destinationipv6} '
        '{ipv6_fl} {next_header} {sour_port} {dest_port}',
        'show platform software fed switch {switch} etherchannel {portchannelnum} '
        'load-balance mac-ip-fl-nh-v6 {sourcemac} {sourceipv6} {destinationipv6} {ipv6_fl} '
        '{next_header}',
        'show platform software fed switch {switch} etherchannel {portchannelnum} '
        'load-balance mac-ip-protocol-v4 {sourcemac} {sourceip} {destinationip} {protocol}',
        'show platform software fed switch {switch} etherchannel {portchannelnum} '
        'load-balance mac-ip-protocol-port-v4 {sourcemac} {sourceip} {destinationip} '
        '{protocol} {sour_port} {dest_port}',
        'show platform software fed switch {switch} etherchannel {portchannelnum} '
        'load-balance mac-vlan-ip-fl-nh-port-v6 {sourcemac} {vlan_id} {sourceipv6} '
        '{destinationipv6} {ipv6_fl} {next_header} {sour_port} {dest_port}',
        'show platform software fed switch {switch} etherchannel {portchannelnum} '
        'load-balance mac-vlan-ip-fl-nh-v6 {sourcemac} {vlan_id} {sourceipv6} '
        '{destinationipv6} {ipv6_fl} {next_header}',
        'show platform software fed switch {switch} etherchannel {portchannelnum} '
        'load-balance mac-vlan-ip-protocol-port-v4 {sourcemac} {vlan_id} {sourceip} '
        '{destinationip} {protocol} {sour_port} {dest_port}',
        'show platform software fed switch {switch} etherchannel {portchannelnum} '
        'load-balance mac-vlan-ip-protocol-v4 {sourcemac} {vlan_id} {sourceip} '
        '{destinationip} {protocol}',
        'show platform software fed switch {switch} etherchannel {portchannelnum} '
        'load-balance mac-vlanid {sourcemac} {vlan_id}'
    ]

    def cli(self, switch=None, portchannelnum=None, sourceipv6=None,
            destinationipv6=None, ipv6_fl=None, next_header=None,
            sour_port=None, dest_port=None, sourcemac=None, destinationmac=None,
            flow_label=None, source=None, destination=None, protocol=None,
            sourceip=None, destinationip=None, vlan_id=None, output=None):

        if output is None:
            if switch and portchannelnum and sourceipv6 and destinationipv6 and \
               ipv6_fl and next_header and sour_port and dest_port:
                cmd = self.cli_command[0].format(
                    switch=switch, portchannelnum=portchannelnum,
                    sourceipv6=sourceipv6, destinationipv6=destinationipv6,
                    ipv6_fl=ipv6_fl, next_header=next_header,
                    sour_port=sour_port, dest_port=dest_port)
            elif switch and portchannelnum and sourcemac and destinationmac and \
                 flow_label and next_header:
                cmd = self.cli_command[1].format(
                    switch=switch, portchannelnum=portchannelnum,
                    sourcemac=sourcemac, destinationmac=destinationmac,
                    flow_label=flow_label, next_header=next_header)
            elif switch and portchannelnum and source and destination and \
                 protocol and sour_port and dest_port:
                cmd = self.cli_command[2].format(
                    switch=switch, portchannelnum=portchannelnum,
                    source=source, destination=destination, protocol=protocol,
                    sour_port=sour_port, dest_port=dest_port)
            elif switch and portchannelnum and source and destination and protocol:
                cmd = self.cli_command[3].format(
                    switch=switch, portchannelnum=portchannelnum,
                    source=source, destination=destination, protocol=protocol)
            elif switch and portchannelnum and sourcemac:
                cmd = self.cli_command[4].format(
                    switch=switch, portchannelnum=portchannelnum,
                    sourcemac=sourcemac)
            elif switch and portchannelnum and sourcemac and sourceipv6 and \
                 destinationipv6 and ipv6_fl and next_header and sour_port and dest_port:
                cmd = self.cli_command[5].format(
                    switch=switch, portchannelnum=portchannelnum,
                    sourcemac=sourcemac, sourceipv6=sourceipv6,
                    destinationipv6=destinationipv6, ipv6_fl=ipv6_fl,
                    next_header=next_header, sour_port=sour_port, dest_port=dest_port)
            elif switch and portchannelnum and sourcemac and sourceipv6 and \
                 destinationipv6 and ipv6_fl and next_header:
                cmd = self.cli_command[6].format(
                    switch=switch, portchannelnum=portchannelnum,
                    sourcemac=sourcemac, sourceipv6=sourceipv6,
                    destinationipv6=destinationipv6, ipv6_fl=ipv6_fl,
                    next_header=next_header)
            elif switch and portchannelnum and sourcemac and sourceip and \
                 destinationip and protocol:
                cmd = self.cli_command[7].format(
                    switch=switch, portchannelnum=portchannelnum,
                    sourcemac=sourcemac, sourceip=sourceip,
                    destinationip=destinationip, protocol=protocol)
            elif switch and portchannelnum and sourcemac and sourceip and \
                 destinationip and protocol and sour_port and dest_port:
                cmd = self.cli_command[8].format(
                    switch=switch, portchannelnum=portchannelnum,
                    sourcemac=sourcemac, sourceip=sourceip,
                    destinationip=destinationip, protocol=protocol,
                    sour_port=sour_port, dest_port=dest_port)
            elif switch and portchannelnum and sourcemac and vlan_id and \
                 sourceipv6 and destinationipv6 and ipv6_fl and next_header and \
                 sour_port and dest_port:
                cmd = self.cli_command[9].format(
                    switch=switch, portchannelnum=portchannelnum,
                    sourcemac=sourcemac, vlan_id=vlan_id, sourceipv6=sourceipv6,
                    destinationipv6=destinationipv6, ipv6_fl=ipv6_fl,
                    next_header=next_header, sour_port=sour_port, dest_port=dest_port)
            elif switch and portchannelnum and sourcemac and vlan_id and \
                 sourceipv6 and destinationipv6 and ipv6_fl and next_header:
                cmd = self.cli_command[10].format(
                    switch=switch, portchannelnum=portchannelnum,
                    sourcemac=sourcemac, vlan_id=vlan_id, sourceipv6=sourceipv6,
                    destinationipv6=destinationipv6, ipv6_fl=ipv6_fl,
                    next_header=next_header)
            elif switch and portchannelnum and sourcemac and vlan_id and \
                 sourceip and destinationip and protocol and sour_port and dest_port:
                cmd = self.cli_command[11].format(
                    switch=switch, portchannelnum=portchannelnum,
                    sourcemac=sourcemac, vlan_id=vlan_id, sourceip=sourceip,
                    destinationip=destinationip, protocol=protocol,
                    sour_port=sour_port, dest_port=dest_port)
            elif switch and portchannelnum and sourcemac and vlan_id and \
                 sourceip and destinationip and protocol:
                cmd = self.cli_command[12].format(
                    switch=switch, portchannelnum=portchannelnum,
                    sourcemac=sourcemac, vlan_id=vlan_id, sourceip=sourceip,
                    destinationip=destinationip, protocol=protocol)
            elif switch and portchannelnum and sourcemac and vlan_id:
                cmd = self.cli_command[13].format(
                    switch=switch, portchannelnum=portchannelnum,
                    sourcemac=sourcemac, vlan_id=vlan_id)
            else:
                raise ValueError("No matching command found for the provided arguments")

            output = self.device.execute(cmd)

        # Initialize the dictionary for parsed output.
        ret_dict = {}

        # Dest Port: : GigabitEthernet1/0/4
        p1 = re.compile(r'^Dest\s+Port\S+\s+\S+\s(?P<destinationport>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # Dest Port: : GigabitEthernet1/0/4
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['destinationport'] = group['destinationport']
                continue

        return ret_dict


class ShowPlatformSoftwareFedSwitchSecurityFedSisfIfIdSchema(MetaParser):
    """Schema for show platform software fed switch security-fed sisf if-id"""
    schema = {
        'fed_sisf_port_data': {
            'interface': {
                'interface_id':{
                    Any(): {
                        'interface_oid': int,
                        'interface_name': str,
                        'target_port': str,
                        'sisf_enable': str,
                        'interface_local': str,
                        'asic_local': str,
                        Optional('etherchannel_member'): str,
                        Optional('programmed_status'): str,
                        'interface_active': str,
                        'internal_error': str,
                        'low_level_error': str,
                        'etherchannel': str,
                        'etherchannel_id': int,
                        'reference_count': int,
                        'num_oids_programmed': int,
                        'num_oids_on_asic': str,
                        'no_acl_diagnostic': int,
                        'invalid_acl_diagnostic': int,
                        'redundant_active_diagnostic': int,
                        'redundant_deactivate_diagnostic': int,
                        Optional('asic_specific'): {
                            'acl_info': {
                                'oid': int,
                                'on_asic': int,
                                'positions': {
                                    Any(): {
                                        'protocol': str,
                                        Optional('src_port'): int,
                                        Optional('dst_port'): int,
                                        'action': str,
                                        'counter_oid': int,
                                        Optional('message_type'): str,
                                        Optional('code'): int
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

class ShowPlatformSoftwareFedSwitchSecurityFedSisfIfId(ShowPlatformSoftwareFedSwitchSecurityFedSisfIfIdSchema):
    """Parser for
    * 'show platform software fed switch security-fed sisf if-id {if_id}'
    """
    cli_command = 'show platform software fed switch {switch_var} security-fed sisf if-id {if_id}'

    def cli(self, switch_var, if_id, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch_var=switch_var, if_id=if_id))

        parsed_data = {}

        # Interface ID (if-id) = 1035
        p1 = re.compile(r'^Interface ID \(if-id\) = (?P<interface_id>\d+)$')

        # Interface name = GigabitEthernet1/0/4
        p2 = re.compile(r'^Interface name = (?P<interface_name>\S+)$')

        # Interface OID = 1090
        p3 = re.compile(r'^Interface OID = (?P<interface_oid>\d+)$')

        # Target Port: TRUE
        p4 = re.compile(r'^(Target Port): (?P<target_port>\S+)$')

        # SISF enable: TRUE
        p5 = re.compile(r'^SISF enable: (?P<sisf_enable>\S+)$')

        # Interface Local: TRUE on ASIC 0x1
        p6 = re.compile(r'^Interface Local: (?P<interface_local_true>\S+) on ASIC (?P<asic_local>\S+)$')

        # EtherChannel member: TRUE (Not programmed)
        p7 = re.compile(r'^EtherChannel member: (?P<etherchannel_member>\S+)( \((?P<programmed_status>[\S\s]+)\))?$')

        # Interface active: TRUE
        p8 = re.compile(r'^Interface active: (?P<interface_active>\S+)$')

        # Internal error = None
        p9 = re.compile(r'^Internal error = (?P<internal_error>[\S\s]+)$')

        # Low-level error = None
        p10 = re.compile(r'^Low-level error = (?P<low_level_error>[\S\s]+)$')

        # EtherChannel: FALSE
        p11 = re.compile(r'^EtherChannel: (?P<etherchannel>\S+)$')

        # EtherChannel ID = 0
        p12 = re.compile(r'^EtherChannel ID = (?P<etherchannel_id>\d+)$')

        # Reference count = 0
        p13 = re.compile(r'^Reference count = (?P<reference_count>\d+)$')

        # Number of OIDs programmed = 1 on ASIC 0x1
        p14 = re.compile(r'^Number of OIDs programmed = (?P<num_oids_programmed>\d+) on ASIC (?P<num_oids_on_asic>\S+)$')

        # No ACL diagnostic = 0
        p15 = re.compile(r'^No ACL diagnostic = (?P<no_acl_diagnostic>\d+)$')

        # Invalid ACL diagnostic = 0
        p16 = re.compile(r'^Invalid ACL diagnostic = (?P<invalid_acl_diagnostic>\d+)$')

        # Redundant active diagnostic = 0
        p17 = re.compile(r'^Redundant active diagnostic = (?P<redundant_active_diagnostic>\d+)$')

        # Redundant deactivate diagnostic = 0
        p18 = re.compile(r'^Redundant deactivate diagnostic = (?P<redundant_deactivate_diagnostic>\d+)$')

        # Information about ACL with OID(557) on ASIC(0)
        p19 = re.compile(r'^Information about ACL with OID\((?P<acl_oid>\d+)\) on ASIC\((?P<acl_asic>\d+)\)$')

        # Position Protocol Src Port Dst Port Action  Counter OID
        # 0        UDP      547      0        PUNT    558
        p20 = re.compile(r'^(?P<position>\d+)\s+(?P<protocol>\w+)\s+(?P<src_port>\d+)\s+(?P<dst_port>\d+)\s+(?P<action>\S+)\s+(?P<counter_oid>\d+)$')

        # Position Protocol Message Type                     Code      Action  Counter OID
        # 3        ICMPv6   Neighbor Solicitation            0         PUNT    561
        p21 = re.compile(r'^(?P<position>\d+)\s+(?P<protocol>\w+)\s+(?P<message_type>[\S\s]+?)\s+(?P<code>\d+)\s+(?P<action>\S+)\s+(?P<counter_oid>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Interface ID (if-id) = 1035
            m = p1.match(line)
            if m:
                group=m.groupdict()
                interface_id=int(group['interface_id'])
                port_data_dict = parsed_data.setdefault('fed_sisf_port_data', {}).setdefault('interface', {}).setdefault('interface_id', {})
                int_dict=port_data_dict.setdefault(interface_id, {})
                continue

            # Interface name = GigabitEthernet1/0/4
            m = p2.match(line)
            if m:
                group = m.groupdict()
                int_dict['interface_name'] = group['interface_name']
                continue

            # Interface OID = 1090
            m = p3.match(line)
            if m:
                int_dict['interface_oid'] = int(m.group('interface_oid'))
                continue

            # Target Port: TRUE
            m = p4.match(line)
            if m:
                int_dict['target_port'] = m.group('target_port')
                continue

            # SISF enable: TRUE
            m = p5.match(line)
            if m:
                int_dict['sisf_enable'] = m.group('sisf_enable')
                continue

            # Interface Local: TRUE on ASIC 0x1
            m = p6.match(line)
            if m:
                group=m.groupdict()
                int_dict['interface_local'] = group['interface_local_true']
                int_dict['asic_local']= group['asic_local']
                continue

            # EtherChannel member: TRUE (Not programmed)
            m = p7.match(line)
            if m:
                int_dict['etherchannel_member'] = m.group('etherchannel_member')
                if m.group('programmed_status'):
                    int_dict['programmed_status'] = m.group('programmed_status')
                continue

            # Interface active: TRUE
            m = p8.match(line)
            if m:
                int_dict['interface_active'] = m.group('interface_active')
                continue

            # Internal error = None
            m = p9.match(line)
            if m:
                int_dict['internal_error'] = m.group('internal_error')
                continue

            # Low-level error = None
            m = p10.match(line)
            if m:
                int_dict['low_level_error'] = m.group('low_level_error')
                continue

            # EtherChannel: FALSE
            m = p11.match(line)
            if m:
                int_dict['etherchannel'] = m.group('etherchannel')
                continue

            # EtherChannel ID = 0
            m = p12.match(line)
            if m:
                int_dict['etherchannel_id'] = int(m.group('etherchannel_id'))
                continue

            # Reference count = 0
            m = p13.match(line)
            if m:
                int_dict['reference_count'] = int(m.group('reference_count'))
                continue

            # Number of OIDs programmed = 1 on ASIC 0x1
            m = p14.match(line)
            if m:
                int_dict['num_oids_programmed'] = int(m.group('num_oids_programmed'))
                int_dict['num_oids_on_asic']= m.group('num_oids_on_asic')
                continue

            # No ACL diagnostic = 0
            m = p15.match(line)
            if m:
                int_dict['no_acl_diagnostic'] = int(m.group('no_acl_diagnostic'))
                continue

            # Invalid ACL diagnostic = 0
            m = p16.match(line)
            if m:
                int_dict['invalid_acl_diagnostic'] = int(m.group('invalid_acl_diagnostic'))
                continue

            # Redundant active diagnostic = 0
            m = p17.match(line)
            if m:
                int_dict['redundant_active_diagnostic'] = int(m.group('redundant_active_diagnostic'))
                continue

            # Redundant deactivate diagnostic = 0
            m = p18.match(line)
            if m:
                int_dict['redundant_deactivate_diagnostic'] = int(m.group('redundant_deactivate_diagnostic'))
                continue

            # Information about ACL with OID(557) on ASIC(0)
            m = p19.match(line)
            if m:
                group=m.groupdict()
                asic_dict=int_dict.setdefault('asic_specific',{}).setdefault('acl_info',{})
                asic_dict['oid']= int(group['acl_oid'])
                asic_dict['on_asic']= int(group['acl_asic'])
                continue

            # Position Protocol Src Port Dst Port Action  Counter OID
            # 0        UDP      547      0        PUNT    558
            m = p20.match(line)
            if m:
                group=m.groupdict()
                position_dict=asic_dict.setdefault('positions',{}).setdefault(int(group['position']),{})
                position_dict['protocol']= group['protocol']
                position_dict['src_port']= int(group['src_port'])
                position_dict['dst_port']= int(group['dst_port'])
                position_dict['action']= group['action']
                position_dict['counter_oid']=int(group['counter_oid'])
                continue

            # Position Protocol Message Type                     Code      Action  Counter OID
            # 3        ICMPv6   Neighbor Solicitation            0         PUNT    561
            m = p21.match(line)
            if m:
                group=m.groupdict()
                position_dict=asic_dict.setdefault('positions',{}).setdefault(int(group['position']),{})
                position_dict['protocol']= group['protocol']
                position_dict['message_type']= group['message_type']
                position_dict['code']= int(group['code'])
                position_dict['action']= group['action']
                position_dict['counter_oid']=int(group['counter_oid'])
                continue

        return parsed_data


class ShowPlatformSoftwareFedSwitchSecurityFedSisfVlanSchema(MetaParser):
    """Schema for show platform software fed switch security-fed sisf vlan"""
    schema = {
    'fed_sisf_vlan_data': {
        'vlan': {
            Any(): {
                'interface_id': int,
                'target_vlan': str,
                'sisf_enable': str,
                'internal_error': str,
                'low_level_error': str,
                'num_oids_programmed': int,
                'num_oids_on_asic': str,
                'no_acl_diagnostic': int,
                'invalid_acl_diagnostic': int,
                'redundant_active_diagnostic': int,
                'redundant_deactivate_diagnostic': int,
                Optional('asic_specific'): {
                    'acl_info': {
                    'oid': int,
                    'on_asic': int,
                    'positions': {
                        Any(): {
                            'protocol': str,
                            Optional('src_port'): int,
                            Optional('dst_port'): int,
                            'action': str,
                            'counter_oid': int,
                            Optional('message_type'): str,
                            Optional('code'): int
                            }
                        }
                    }
                }
            }
        }
    }
}

class ShowPlatformSoftwareFedSwitchSecurityFedSisfVlan(ShowPlatformSoftwareFedSwitchSecurityFedSisfVlanSchema):
    """Parser for show platform software fed switch security-fed sisf vlan"""

    cli_command = 'show platform software fed switch {switch_var} security-fed sisf vlan {vlan}'

    def cli(self, switch_var, vlan, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch_var=switch_var, vlan=vlan))

        # Initialize the parsed dictionary
        parsed_data = {}
        current_section = None

        #Vlan = 30
        p1 = re.compile(r'^Vlan = (?P<vlan>\d+)$')

        # Interface ID (if-id) = 1035
        p2 = re.compile(r'^Interface ID \(if-id\) = (?P<interface_id>\d+)$')

        # Target VLAN: TRUE
        p3 = re.compile(r'^Target VLAN: (?P<target_vlan>\S+)$')

        # SISF enable: TRUE
        p4 = re.compile(r'^SISF enable: (?P<sisf_enable>\S+)$')

        # Internal error = None
        p5 = re.compile(r'^Internal error = (?P<internal_error>[\S\s]+)$')

        # Low-level error = None
        p6 = re.compile(r'^Low-level error = (?P<low_level_error>[\S\s]+)$')

        # Number of OIDs programmed = 1 on ASIC 0x1
        p7 = re.compile(r'^Number of OIDs programmed = (?P<num_oids_programmed>\d+) on ASIC (?P<num_oids_on_asic>\S+)$')

        # No ACL diagnostic = 0
        p8 = re.compile(r'^No ACL diagnostic = (?P<no_acl_diagnostic>\d+)$')

        # Invalid ACL diagnostic = 0
        p9 = re.compile(r'^Invalid ACL diagnostic = (?P<invalid_acl_diagnostic>\d+)$')

        # Redundant active diagnostic = 0
        p10 = re.compile(r'^Redundant active diagnostic = (?P<redundant_active_diagnostic>\d+)$')

        # Redundant deactivate diagnostic = 0
        p11 = re.compile(r'^Redundant deactivate diagnostic = (?P<redundant_deactivate_diagnostic>\d+)$')

        # Information about ACL with OID(557) on ASIC(0)
        p12 = re.compile(r'^Information about ACL with OID\((?P<acl_oid>\d+)\) on ASIC\((?P<acl_asic>\d+)\)$')

        # Position Protocol Src Port Dst Port Action  Counter OID
        # 0        UDP      547      0        PUNT    558
        p13 = re.compile(r'^(?P<position>\d+)\s+(?P<protocol>\w+)\s+(?P<src_port>\d+)\s+(?P<dst_port>\d+)\s+(?P<action>\S+)\s+(?P<counter_oid>\d+)$')

        # Position Protocol Message Type                     Code      Action  Counter OID
        # 3        ICMPv6   Neighbor Solicitation            0         PUNT    561
        p14 = re.compile(r'^(?P<position>\d+)\s+(?P<protocol>\w+)\s+(?P<message_type>[\S\s]+?)\s+(?P<code>\d+)\s+(?P<action>\S+)\s+(?P<counter_oid>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            #Vlan = 30
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vlan_id = int(group['vlan'])
                vlan_data_dict = parsed_data.setdefault('fed_sisf_vlan_data', {})
                vlan_dict = vlan_data_dict.setdefault('vlan', {}).setdefault(vlan_id, {})
                continue

            # Interface ID (if-id) = 1035
            m = p2.match(line)
            if m:
                vlan_dict['interface_id'] = int(m.group('interface_id'))
                continue

            # Target VLAN: TRUE
            m = p3.match(line)
            if m:
                vlan_dict['target_vlan'] = m.group('target_vlan')
                continue

            # SISF enable: TRUE
            m = p4.match(line)
            if m:
                vlan_dict['sisf_enable'] = m.group('sisf_enable')
                continue

            # Internal error = None
            m = p5.match(line)
            if m:
                vlan_dict['internal_error'] = m.group('internal_error')
                continue

            # Low-level error = None
            m = p6.match(line)
            if m:
                vlan_dict['low_level_error'] = m.group('low_level_error')
                continue

            # Number of OIDs programmed = 1 on ASIC 0x1
            m = p7.match(line)
            if m:
                vlan_dict['num_oids_programmed'] = int(m.group('num_oids_programmed'))
                vlan_dict['num_oids_on_asic']= m.group('num_oids_on_asic')
                continue

            # No ACL diagnostic = 0
            m = p8.match(line)
            if m:
                vlan_dict['no_acl_diagnostic'] = int(m.group('no_acl_diagnostic'))
                continue

            # Invalid ACL diagnostic = 0
            m = p9.match(line)
            if m:
                vlan_dict['invalid_acl_diagnostic'] = int(m.group('invalid_acl_diagnostic'))
                continue

            # Redundant active diagnostic = 0
            m = p10.match(line)
            if m:
                vlan_dict['redundant_active_diagnostic'] = int(m.group('redundant_active_diagnostic'))
                continue

            # Redundant deactivate diagnostic = 0
            m = p11.match(line)
            if m:
                vlan_dict['redundant_deactivate_diagnostic'] = int(m.group('redundant_deactivate_diagnostic'))
                continue

            # Information about ACL with OID(557) on ASIC(0)
            m = p12.match(line)
            if m:
                group=m.groupdict()
                asic_dict=vlan_dict.setdefault('asic_specific',{}).setdefault('acl_info',{})
                asic_dict['oid']= int(group['acl_oid'])
                asic_dict['on_asic']= int(group['acl_asic'])
                continue

            # Position Protocol Src Port Dst Port Action  Counter OID
            # 0        UDP      547      0        PUNT    558
            m = p13.match(line)
            if m:
                group=m.groupdict()
                position_dict=asic_dict.setdefault('positions',{}).setdefault(int(group['position']),{})
                position_dict['protocol']= group['protocol']
                position_dict['src_port']= int(group['src_port'])
                position_dict['dst_port']= int(group['dst_port'])
                position_dict['action']= group['action']
                position_dict['counter_oid']=int(group['counter_oid'])
                continue

            # Position Protocol Message Type                     Code      Action  Counter OID
            # 3        ICMPv6   Neighbor Solicitation            0         PUNT    561
            m = p14.match(line)
            if m:
                group=m.groupdict()
                position_dict=asic_dict.setdefault('positions',{}).setdefault(int(group['position']),{})
                position_dict['protocol']= group['protocol']
                position_dict['message_type']= group['message_type']
                position_dict['code']= int(group['code'])
                position_dict['action']= group['action']
                position_dict['counter_oid']=int(group['counter_oid'])
                continue

        return parsed_data

class ShowPlatformSoftwareFedSwitchActiveSgaclDetailSchema(MetaParser):
    """schema for
        show platform software fed switch {switch_type} sgacl detail

    """

    schema = {
        'global_enforcement_status' : str
    }

class ShowPlatformSoftwareFedSwitchActiveSgaclDetail(ShowPlatformSoftwareFedSwitchActiveSgaclDetailSchema):
    """Parser for
        show platform software fed switch {switch_type} sgacl detail
    """

    cli_command = "show platform software fed switch {switch_type} sgacl detail"

    def cli(self, switch_type,output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch_type=switch_type))

        ret_dict = {}

        # Global Enforcement: On
        p1 = re.compile(r"^Global\s+Enforcement:\s+(?P<global_enforcement_status>\S+)$")

        for line in output.splitlines():
            line = line.strip()

            # Global Enforcement: On
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['global_enforcement_status']=group['global_enforcement_status']
                continue

        return ret_dict

class ShowPlatformSoftwareFedSwitchActiveSgaclPortSchema(MetaParser):
    """schema for
        show platform software fed switch {switch_type} sgacl port

    """

    schema = {
        'port': {
            Any(): {
                'enforcement': str,
                'port_sgt': int,
                'trust': str,
                'propogate': str,
                Optional('interface_state'): str,
                Optional('ingress'): str,
                Optional('egress'): str,


            }
        }
    }

class ShowPlatformSoftwareFedSwitchActiveSgaclPort(ShowPlatformSoftwareFedSwitchActiveSgaclPortSchema):
    """Parser for
        show platform software fed switch {switch_type} sgacl port
    """

    cli_command = ['show platform software fed switch {switch_type} sgacl port',
                   'show platform software fed active sgacl port']

    def cli(self, switch_type=None,output=None):
        if output is None:
            if switch_type:
                cmd = self.cli_command[0].format(switch_type=switch_type)
            else:
                cmd = self.cli_command[1]
            output = self.device.execute(cmd)

        ret_dict = {}
        # Port                     Enforcement         Port-SGT      Trust       Propagate       Interface state
        # --------------------------------------------------------------------------------------------------------
        # HundredGigE0/26            Enabled                0          No            No              Pending
        # HundredGigE0/27            Enabled                0          No            No              Pending

        p1 = re.compile(r"^(?P<port>\S+)\s+(?P<enforcement>\S+)\s+(?P<port_sgt>\d+)\s+(?P<trust>\S+)\s+(?P<propogate>\S+)\s+(?P<interface_state>\S+)$")

        #Port            Status     Port-SGT  Trust  Propagate  IngressCache EgressCache
        #-------------------------------------------------------------------------------
        #Te1/0/1        Enabled         0     No      No          No          No
        #Te1/0/2        Enabled         0     No      No          No          No

        p2 = re.compile(r'^(?P<port>\S+)\s+(?P<enforcement>\S+)\s+(?P<port_sgt>-?\d+)\s+(?P<trust>\S+)\s+(?P<propogate>\S+)\s+(?P<ingress>\S+)\s+(?P<egress>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # Port                     Enforcement         Port-SGT      Trust       Propagate       Interface state
            # --------------------------------------------------------------------------------------------------------
            # HundredGigE0/26            Enabled                0          No            No              Pending
            # HundredGigE0/27            Enabled                0          No            No              Pending

            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault('port', {}).setdefault(group['port'],{})
                root_dict['enforcement']=group['enforcement']
                root_dict['port_sgt']=int(group['port_sgt'])
                root_dict['trust']=group['trust']
                root_dict['propogate']=group['propogate']
                root_dict['interface_state']=group['interface_state']

                continue
            #Te1/0/1        Enabled         0     No      No          No          No
            m = p2.match(line)
            if m:
                match_dict = m.groupdict()
                port_name = Common.convert_intf_name(match_dict['port'])
                port_dict = ret_dict.setdefault('port', {}).setdefault(port_name, {})
                port_dict.update({
                    'enforcement': match_dict['enforcement'],
                    'port_sgt': int(match_dict['port_sgt']),
                    'trust': match_dict['trust'],
                    'propogate': match_dict['propogate'],
                    'ingress': match_dict['ingress'],
                    'egress': match_dict['egress']
                })
                continue

        return ret_dict

class ShowPlatformSoftwareFedSwitchSecurityFedDhcpVlandetailSchema(MetaParser):
    """Schema for
    show platform software fed switch {switch_type} security-fed dhcp vlan {vlan_num} detail
    """
    schema = {
        'vlan': int,
        Optional('multicast_group_id'): {
            Optional('oid'): int,
            Optional('asic'): int
        },
        Optional('gid'): str,
        Optional('punject_switch_profile'): bool,
        Optional('trusted_ports'): {
            Any(): {
                'interface_id': str,
                'po_id': str
            }
        },
        Optional('acl_info'): {
            Optional('oid'): int,
            Optional('asic'): int,
            Optional('entries'): {
                Any(): {
                    'position': int,
                    'protocol': str,
                    'src_port': int,
                    'dst_port': int,
                    'action': str,
                    'counter_oid': int
                }
            }
        }
    }

class ShowPlatformSoftwareFedSwitchSecurityFedDhcpVlandetail(ShowPlatformSoftwareFedSwitchSecurityFedDhcpVlandetailSchema):
    """Parser for
    show platform software fed switch {switch_type} security-fed dhcp vlan {vlan_num} detail
    """

    cli_command = 'show platform software fed switch {switch_type} security-fed dhcp vlan {vlan_num} detail'

    def cli(self, switch_type, vlan_num, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch_type=switch_type,vlan_num=vlan_num))

        # Initialize parsed data structure
        parsed_dict = {}

        # Define regex patterns
        # Vlan= 50
        p1 = re.compile(r'^Vlan= +(?P<vlan>\d+)$')

        # Multicast Group with OID(2854) on ASIC(0)
        p2 = re.compile(r'^Multicast Group with OID\((?P<oid>\d+)\) on ASIC\((?P<asic>\d+)\)$')

        # Trusted ports multicast group GID:: 0x201C
        p3 = re.compile(r'^Trusted ports multicast group GID:: +(?P<gid>\S+)$')

        # Punject Switch Profile: TRUE
        p4 = re.compile(r'^Punject Switch Profile: +(?P<profile>\S+)$')

        #   Trusted Port                                                      Interface Id      PO ID
        # ----------------------------------------------------------------------------------------------------
        #   GigabitEthernet3/0/3                                              0x00000494        0x000004d9
        #   GigabitEthernet2/0/25                                             0x00000420        0x000004d9

        p5 = re.compile(r'^(?P<port>\S+) +(?P<interface_id>\S+) +(?P<po_id>\S+)$')

        # Information about ACL with OID(547) on ASIC(0)
        p6 = re.compile(r'^Information about ACL with OID\((?P<oid>\d+)\) on ASIC\((?P<asic>\d+)\)$')

        #  Position Protocol Src Port Dst Port Action  Counter OID
        # -------------------------------------------------------
        #  0        UDP      68       67       PUNT    548
        #  1        UDP      67       68       PUNT    548
        #  2        UDP      67       67       PUNT    548

        p7 = re.compile(r'^(?P<position>\d+) +(?P<protocol>\S+) +(?P<src_port>\d+) +(?P<dst_port>\d+) +(?P<action>\S+) +(?P<counter_oid>\d+)$')

        # Parse each line
        for line in output.splitlines():
            line = line.strip()

            # Vlan= 50
            m = p1.match(line)
            if m:
                parsed_dict['vlan'] = int(m.group('vlan'))
                continue

            # Multicast Group with OID(2854) on ASIC(0)
            m = p2.match(line)
            if m:
                parsed_dict['multicast_group_id'] = {
                    'oid': int(m.group('oid')),
                    'asic': int(m.group('asic'))
                }
                continue

            # Trusted ports multicast group GID:: 0x201C
            m = p3.match(line)
            if m:
                parsed_dict['gid'] = m.group('gid')
                continue

            # Punject Switch Profile: TRUE
            m = p4.match(line)
            if m:
                parsed_dict['punject_switch_profile'] = m.group('profile').lower() == 'true'
                continue

            #   Trusted Port                                                      Interface Id      PO ID
            # ----------------------------------------------------------------------------------------------------
            #   GigabitEthernet3/0/3                                              0x00000494        0x000004d9
            #   GigabitEthernet2/0/25                                             0x00000420        0x000004d9
            m = p5.match(line)
            if m:
                group = m.groupdict()
                port = group['port']
                if port.startswith(('GigabitEthernet', 'Port-channel')):
                    parsed_dict.setdefault('trusted_ports', {})
                    parsed_dict['trusted_ports'][port] = {
                            'interface_id': m.group('interface_id'),
                            'po_id': m.group('po_id')
                    }
                continue

            # Information about ACL with OID(547) on ASIC(0)
            m = p6.match(line)
            if m:
                parsed_dict['acl_info'] = {
                    'oid': int(m.group('oid')),
                    'asic': int(m.group('asic')),
                    'entries': {}
                }
                continue

            #  Position Protocol Src Port Dst Port Action  Counter OID
            # -------------------------------------------------------
            #  0        UDP      68       67       PUNT    548

            m = p7.match(line)
            if m:
                position = int(m.group('position'))
                parsed_dict['acl_info']['entries'][position] = {
                    'position': position,
                    'protocol': m.group('protocol'),
                    'src_port': int(m.group('src_port')),
                    'dst_port': int(m.group('dst_port')),
                    'action': m.group('action'),
                    'counter_oid': int(m.group('counter_oid'))
                }
                continue

        return parsed_dict

class ShowPlatformSoftwareFedSwitchActiveSecurityDhcpStatisticsSchema(MetaParser):
    """Schema for show platform software fed switch active security dhcp statistics"""

    schema = {
        'name': {
            Any(): {
                'oid': int,
                'packets_hits': int,
            },
        },
    }

class ShowPlatformSoftwareFedSwitchActiveSecurityDhcpStatistics(ShowPlatformSoftwareFedSwitchActiveSecurityDhcpStatisticsSchema):
    """Parser for show platform software fed switch {switch_type} security dhcp statistics"""

    cli_command = 'show platform software fed switch {switch_type} security dhcp statistics'

    def cli(self, switch_type, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch_type=switch_type))

        # Name                              OID       Packets Hits
        # --------------------------------------------------------
        # DHCP Snoop VLAN                   548       0
        # Other stats

        p1 = re.compile(r'^(?P<name>\S+(\s+\S+)*?)\s+(?P<oid>\d+)\s+(?P<packets_hits>\d+)$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Match the pattern
            # DHCP Snoop VLAN                   548       0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                oid = int(group['oid'])
                packets_hits = int(group['packets_hits'])

                ret_dict.setdefault('name', {}).setdefault('dhcp_snoop_vlan', {})
                ret_dict['name']['dhcp_snoop_vlan']['oid'] = oid
                ret_dict['name']['dhcp_snoop_vlan']['packets_hits'] = packets_hits
                continue

        return ret_dict


class ShowPlatformSoftwareFedSwitchActiveAccessSecurityTableSummarySchema(MetaParser):
    """Schema for
        'show platform software fed switch active access-security table summary'
        'show platform software fed switch active access-security table mac {mac_id}'
        'show platform software fed switch active access-security table interface if-id {if_id}'
    """
    schema = {
        'access_security_table_summary': {
            Any(): {
                Any(): {
                    'interface': str,
                    'logical_id': int,
                    'position': int,
                    'asic': int,
                    'auth_act': str,
                    'restore_auth_act': str,
                    'flag': str,
                    'policy_oid': int,
                    'packets': int,
                    Optional('mac'): str,
                    Optional('ovrd_vlan'): int,
                    Optional('vlan'): int,
                    Optional('policy'): str,
                    Optional('drop'): str
                }
            }
        }
    }

class ShowPlatformSoftwareFedSwitchActiveAccessSecurityTableSummary(ShowPlatformSoftwareFedSwitchActiveAccessSecurityTableSummarySchema):
    """Parser for
        'show platform software fed switch active access-security table summary'
        'show platform software fed switch active access-security table mac {mac_id}'
        'show platform software fed switch active access-security table interface if-id {if_id}'
    """

    cli_command = [
        'show platform software fed switch {switch_var} access-security table summary',
        'show platform software fed switch {switch_var} access-security table mac {mac_id}',
        'show platform software fed switch {switch_var} access-security table interface if-id {if_id}'
    ]

    def cli(self, switch_var, mac_id=None, if_id=None, output=None):
        if output is None:
            if if_id:
                cmd = self.cli_command[2].format(switch_var=switch_var, if_id=if_id)
            elif mac_id:
                cmd = self.cli_command[1].format(switch_var=switch_var, mac_id=mac_id)
            else:
                cmd = self.cli_command[0].format(switch_var=switch_var)

            output = self.device.execute(cmd)

        ret_dict = {}

        # 1 Gi2/0/34     B07D.479E.7D8D   0          4096       0     FWD_ALL_LRN_DATA   None               NONE         No     0          IPv4v6   2796       3
        p1 = re.compile(r'^\s*(?P<index>\d+)\s+(?P<interface>\S+)\s+(?P<mac>[0-9A-Fa-f\.]+)\s+(?P<logical_id>\d+)\s+(?P<position>\d+)\s+(?P<asic>\d+)\s+(?P<auth_act>\S+)\s+(?P<restore_auth_act>\S+)\s+(?P<flag>\S+)\s+(?P<drop>\S+)\s+(?P<ovrd_vlan>\d+)\s+(?P<policy>\S+)\s+(?P<policy_oid>\d+)\s+(?P<packets>\d+)$')

        # 1 Gi2/0/37     100        B07D.479E.7D90   0          12288      0     FWD_ALL_LRN_DATA   None               NONE         No     NONE     569        0
        p2 = re.compile(r'^\s*(?P<index>\d+)\s+(?P<interface>\S+)\s+(?P<vlan>\d+)\s+(?P<mac>[0-9A-Fa-f\.]+)\s+(?P<logical_id>\d+)\s+(?P<position>\d+)\s+(?P<asic>\d+)\s+(?P<auth_act>\S+)\s+(?P<restore_auth_act>\S+)\s+(?P<flag>\S+)\s+(?P<drop>\S+)\s+(?P<policy>\S+)\s+(?P<policy_oid>\d+)\s+(?P<packets>\d+)$')

        # 1 Gi2/0/34     0          24576      0     DROP_ALL_LRN_DATA  None               NONE         573        2
        p3 = re.compile(r'^\s*(?P<index>\d+)\s+(?P<interface>\S+)\s+(?P<logical_id>\d+)\s+(?P<position>\d+)\s+(?P<asic>\d+)\s+(?P<auth_act>\S+)\s+(?P<restore_auth_act>\S+)\s+(?P<flag>\S+)\s+(?P<policy_oid>\d+)\s+(?P<packets>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # 1 Gi2/0/34     B07D.479E.7D8D   0          4096       0     FWD_ALL_LRN_DATA   None               NONE         No     0          IPv4v6   2796       3
            m = p1.match(line)
            if m:
                group = m.groupdict()
                index = int(group.pop('index'))
                key = 'mac_client_port_and_mac_entries'
                mac_dict = ret_dict.setdefault('access_security_table_summary',{}).setdefault(key, {})
                entry = {
                    'interface': group['interface'],
                    'mac': group['mac'],
                    'logical_id': int(group['logical_id']),
                    'position': int(group['position']),
                    'asic': int(group['asic']),
                    'auth_act': group['auth_act'],
                    'restore_auth_act': group['restore_auth_act'],
                    'flag': group['flag'],
                    'drop': group['drop'],
                    'ovrd_vlan': int(group['ovrd_vlan']),
                    'policy': group['policy'],
                    'policy_oid': int(group['policy_oid']),
                    'packets': int(group['packets'])
                }
                mac_dict[index] = entry
                continue

            # 1 Gi2/0/37     100        B07D.479E.7D90   0          12288      0     FWD_ALL_LRN_DATA   None               NONE         No     NONE     569        0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                index = int(group.pop('index'))
                key = 'secure_mac_client_port_vlan_and_mac_entries'
                mac_dict = ret_dict.setdefault('access_security_table_summary',{}).setdefault(key, {})
                entry = {
                    'interface': group['interface'],
                    'vlan': int(group['vlan']),
                    'mac': group['mac'],
                    'logical_id': int(group['logical_id']),
                    'position': int(group['position']),
                    'asic': int(group['asic']),
                    'auth_act': group['auth_act'],
                    'restore_auth_act': group['restore_auth_act'],
                    'flag': group['flag'],
                    'drop': group['drop'],
                    'policy': group['policy'],
                    'policy_oid': int(group['policy_oid']),
                    'packets': int(group['packets'])
                }
                mac_dict[index] = entry
                continue

            # 1 Gi2/0/34     0          24576      0     DROP_ALL_LRN_DATA  None               NONE         573        2
            m = p3.match(line)
            if m:
                group = m.groupdict()
                index = int(group.pop('index'))
                key = 'default_client_port_only_entries'
                mac_dict = ret_dict.setdefault('access_security_table_summary',{}).setdefault(key, {})
                entry = {
                    'interface': group['interface'],
                    'logical_id': int(group['logical_id']),
                    'position': int(group['position']),
                    'asic': int(group['asic']),
                    'auth_act': group['auth_act'],
                    'restore_auth_act': group['restore_auth_act'],
                    'flag': group['flag'],
                    'policy_oid': int(group['policy_oid']),
                    'packets': int(group['packets'])
                }
                mac_dict[index] = entry
                continue

        return ret_dict


class ShowPlatformSoftwareFedSwitchActiveSecurityFedArpStatisticsSchema(MetaParser):
    """Schema for 'show platform software fed switch active security-fed arp statistics'"""
    schema = {
        'fed_arp_snooping_statistics': {
            'punject_punt_entries': {
                Any(): {
                    'oid': int,
                    'packet_hits': int
                }
            }
        }
    }

class ShowPlatformSoftwareFedSwitchActiveSecurityFedArpStatistics(ShowPlatformSoftwareFedSwitchActiveSecurityFedArpStatisticsSchema):
    """Parser for 'show platform software fed switch active security-fed arp statistics'"""

    cli_command = 'show platform software fed switch active security-fed arp statistics'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the parsed data structure
        ret_dict = {}

        # ARP Snoop Port                    551       0
        p1 = re.compile(r'(?P<name>[\w\s]+?)\s+(?P<oid>\d+)\s+(?P<packet_hits>\d+)')

        for line in output.splitlines():
            line = line.strip()

            # ARP Snoop Port                    551       0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                name = group['name'].strip()
                data_dict=ret_dict.setdefault('fed_arp_snooping_statistics', {}).setdefault('punject_punt_entries',{}).setdefault(name,{})
                data_dict['oid']=int(group['oid'])
                data_dict['packet_hits']=int(group['packet_hits'])
                continue

        return ret_dict


class ShowPlatformSoftwareFedSwitchActiveAccessSecurityTableUsageSchema(MetaParser):
    """Schema for 'show platform software fed switch active access-security table usage'"""
    schema = {
        'access_security_client_table_usage': {
            Any(): {
                'feature': str,
                'mask': str,
                'asic': int,
                'maximum': int,
                'in_use': int,
                'total_allocated': int,
                'total_freed': int,
            }
        }
    }

class ShowPlatformSoftwareFedSwitchActiveAccessSecurityTableUsage(ShowPlatformSoftwareFedSwitchActiveAccessSecurityTableUsageSchema):
    """Parser for 'show platform software fed switch active access-security table usage'"""

    cli_command = 'show platform software fed switch {switch_var} access-security table usage'

    def cli(self, switch_var, output=None):
        if output is None:
            cmd = self.cli_command.format(switch_var=switch_var)

        output = self.device.execute(cmd)

        ret_dict = {}

        # MAC-Client        Port-VLAN-MAC       0                4096             0                0                0
        p1 = re.compile(r'(?P<feature>\S+)\s+(?P<mask>\S+)\s+(?P<asic>\d+)\s+(?P<maximum>\d+)\s+(?P<in_use>\d+)\s+(?P<total_allocated>\d+)\s+(?P<total_freed>\d+)')

        for line in output.splitlines():
            line = line.strip()

            # MAC-Client        Port-VLAN-MAC       0                4096             0                0                0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                key = f"{group['feature']}_{group['mask']}".lower()
                data_dict = ret_dict.setdefault('access_security_client_table_usage', {}).setdefault(key, {})
                data_dict['feature'] = group['feature']
                data_dict['mask'] = group['mask']
                data_dict['asic'] = int(group['asic'])
                data_dict['maximum'] = int(group['maximum'])
                data_dict['in_use'] = int(group['in_use'])
                data_dict['total_allocated'] = int(group['total_allocated'])
                data_dict['total_freed'] = int(group['total_freed'])
                continue

        return ret_dict


class ShowPlatformSoftwareFedSwitchSecurityFedIpsgIfIdSchema(MetaParser):
    """Schema for 'show platform software fed switch {switch} security-fed ipsg if-id {if-id}'"""
    schema = {
        'ipsg_entries': {
            'mac': {
                Any(): {
                    'ip': str,
                    'ip_handle': str,
                    'mac_handle': str
                }
            }
        }
    }

class ShowPlatformSoftwareFedSwitchSecurityFedIpsgIfId(ShowPlatformSoftwareFedSwitchSecurityFedIpsgIfIdSchema):
    """Parser for 'show platform software fed switch {switch} security-fed ipsg if-id {if-id}'"""

    cli_command = 'show platform software fed switch {switch} security-fed ipsg if-id {if_id}'

    def cli(self, switch, if_id, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch=switch, if_id=if_id))

        # Initialize the parsed dictionary
        ret_dict = {}

        # IP                 Handle         Mac                  Handle
        # 50.0.0.2           1086     00:14:01:00:00:01    1086
        p1 = re.compile(r'^(?P<ip>[\d\.]+)\s+(?P<ip_handle>\d+)\s+(?P<mac>[\w:]+)\s+(?P<mac_handle>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # IP                 Handle         Mac                  Handle
            # 50.0.0.2           1086     00:14:01:00:00:01    1086
            m = p1.match(line)
            if m:
                group = m.groupdict()
                result_dict=ret_dict.setdefault('ipsg_entries', {}).setdefault('mac', {}).setdefault(group['mac'], {})
                result_dict['ip']= group['ip']
                result_dict['ip_handle']= group['ip_handle']
                result_dict['mac_handle']= group['mac_handle']
                continue

        return ret_dict

class ShowPlatformSoftwareFedSwitchActiveOifsetL3mHashSchema(MetaParser):
    """Schema for 'show platform software fed switch active oifset l3m hash {hash} detail'"""

    schema = {
        'type': str,
        'state': str,
        'md5': str,
        'fset_urid': str,
        'remote_port_count': int,
        'svi_port_count': int,
        'users_count': int,
        'mioitem_count': int,
        Optional('interfaces'): {
            int: {
                'adjid': str,
                'interface': str,
                'physicalif': str,
                'iftype': str,
                'flags': str,
                Optional('urids'): {
                    'mio': str,
                    'parent': str,
                    'child_repl': str,
                    'adj_obj': str,
                },
                Optional('asic'): {
                    'asic_index': str,
                    'l3_port_oid': int,
                    'port_oid': int,
                }
            }
        },
        'fset_mcidgid': int,
        'asic_0_mcid_oid': int,
        Optional('hw_ip_mcg_info_asic_0'): {
            int: {
                Optional('member_info'): {
                    'l3_port': int
                }
            }
        },
        Optional('users'): {
            str: {
                'urid': str,
                Optional('l3m_entry'): {
                    'mvrf': int,
                    'ip': str,
                    'group': str
                }
            }
        }
    }

class ShowPlatformSoftwareFedSwitchActiveOifsetL3mHash(ShowPlatformSoftwareFedSwitchActiveOifsetL3mHashSchema):
    """Parser for 'show platform software fed switch active oifset l3m hash 35ddf2ee detail'"""

    cli_command = [
        'show platform software fed {switch} {module} oifset l3m',
        'show platform software fed {switch} {module} oifset l3m hash {hash} detail'
    ]
    def cli(self, switch='', module='', hash='', output=None):
        if output is None:
            if hash:
                cmd = self.cli_command[1].format(switch=switch, module=module, hash=hash)
            else:
                cmd = self.cli_command[0].format(switch=switch, module=module)
            output = self.device.execute(cmd)

        # Initialize an empty result dictionary
        result = {}

        # Regex patterns to match the lines
        # Type: s_g_vrf              State: allocated       MD5:(35ddf2ee900391c0:6ced99293343193f)
        p1 = re.compile(r'Type:\s+(?P<type>\S+)\s+State:\s+(?P<state>\S+)\s+MD5:\((?P<md5>[\da-f:]+)\)')

        # Fset Urid                    : 0x3000000000000007
        p2 = re.compile(r'Fset Urid\s+:\s+(?P<fset_urid>\S+)')

        # Remote Port Count            : 0
        p3 = re.compile(r'Remote Port Count\s+:\s+(?P<remote_port_count>\d+)')

        #  Svi Port Count               : 0
        p4 = re.compile(r'Svi Port Count\s+:\s+(?P<svi_port_count>\d+)')

        # Users Count                  : 1
        p5 = re.compile(r'Users Count\s+:\s+(?P<users_count>\d+)')

        # Mioitem Count                : 1
        p6 = re.compile(r'Mioitem Count\s+:\s+(?P<mioitem_count>\d+)')

        # No. AdjID          Interface          PhysicalIf        IfType          Flags
        p7 = re.compile(r'^\s*(?P<no>\d+)\.\s+(?P<adjid>\S+)\s+(?P<interface>\S+)\s+(?P<physicalif>\S+)\s+(?P<iftype>\S+)\s+(?P<flags>\S+)')

        # Urids   => Mio:0x80::11 Parent:0x0 child_repl:0x0(------)  adj_obj:0x90::3
        p8 = re.compile(r'Urids\s+=>\s+Mio:(?P<mio>\S+)\s+Parent:(?P<parent>\S+)\s+child_repl:(?P<child_repl>\S+)\(\S+\s+adj_obj:(?P<adj_obj>\S+)')

        #  (Asic[0]=> l3_port_oid/port_oid : 2854 / 2105 )
        p9 = re.compile(r'\(Asic\[(?P<asic_index>\d+)\]=>\s+l3_port_oid\/port_oid\s+:\s+(?P<l3_port_oid>\d+)\s+\/\s+(?P<port_oid>\d+)\s+\)')

        #  Fset MCID Gid                : 8203
        p10 = re.compile(r'Fset MCID Gid\s+:\s+(?P<fset_mcidgid>\d+)')

        # Asic[0] mcid_oid             : 2868
        p11 = re.compile(r'Asic\[(?P<asic_index>\d+)\]\s+mcid_oid\s+:\s+(?P<asic_0_mcid_oid>\d+)')

        # Hw IP Mcg Info Asic[0] :
        p12 = re.compile(r'Hw IP Mcg Info Asic\[(?P<asic_index>\d+)\] :')

        # Idx.    Member Info
        p13 = re.compile(r'^\s*(?P<idx>\d+)\.\s+(?P<member_info>\S+\s*\S+)')

        # 1.    l3_port: 2854
        p14 = re.compile(r'^\s*(?P<idx>\d+)\.\s+l3_port:\s+(?P<l3_port>\d+)')

        # urid:0x1000000000000565 (l3m_entry: Mvrf:0 (2.2.2.2, 232.1.1.1))
        p15 = re.compile(r'urid:(?P<urid>\S+)\s+\(l3m_entry:\s+Mvrf:(?P<mvrf>\d+)\s+\((?P<ip>\d+\.\d+\.\d+\.\d+),\s+(?P<group>\d+\.\d+\.\d+\.\d+)\)\)')

        # Parsing logic
        for line in output.splitlines():
            line = line.strip()

            #  Type: s_g_vrf              State: allocated       MD5:(35ddf2ee900391c0:6ced99293343193f)
            m = p1.match(line)
            if m:
                result.update(m.groupdict())
                continue

            # Fset Urid                    : 0x3000000000000007
            m = p2.match(line)
            if m:
                result['fset_urid'] = m.group('fset_urid')
                continue

            # Remote Port Count            : 0
            m = p3.match(line)
            if m:
                result['remote_port_count'] = int(m.group('remote_port_count'))
                continue

            # Svi Port Count               : 0
            m = p4.match(line)
            if m:
                result['svi_port_count'] = int(m.group('svi_port_count'))
                continue

            #  Users Count                  : 1
            m = p5.match(line)
            if m:
                result['users_count'] = int(m.group('users_count'))
                continue

            # Mioitem Count                : 1
            m = p6.match(line)
            if m:
                result['mioitem_count'] = int(m.group('mioitem_count'))
                continue

            #      No. AdjID          Interface          PhysicalIf        IfType          Flags
            #    1. 0xf8004e31     Gi1/0/26           Gi1/0/26          phy_if          InHw
            m = p7.match(line)
            if m:
                interface = m.groupdict()
                interface['no'] = int(interface['no'])
                interface_key = interface.pop('no')  # Remove 'no' from the interface details
                result.setdefault('interfaces', {})[interface_key] = interface
                continue

            # Urids   => Mio:0x80::11 Parent:0x0 child_repl:0x0(------)  adj_obj:0x90::3
            m = p8.match(line)
            if m and 'interfaces' in result:
                urids = m.groupdict()
                result['interfaces'][interface_key]['urids'] = urids
                continue

            # (Asic[0]=> l3_port_oid/port_oid : 2854 / 2105 )
            m = p9.match(line)
            if m and 'interfaces' in result:
                asic = m.groupdict()
                asic['l3_port_oid'] = int(asic['l3_port_oid'])
                asic['port_oid'] = int(asic['port_oid'])
                result['interfaces'][interface_key]['asic'] = asic
                continue

            # Fset MCID Gid                : 8203
            m = p10.match(line)
            if m:
                result['fset_mcidgid'] = int(m.group('fset_mcidgid'))
                continue

            # Asic[0] mcid_oid             : 2868
            m = p11.match(line)
            if m:
                result['asic_0_mcid_oid'] = int(m.group('asic_0_mcid_oid'))
                continue

            # Idx.    Member Info
            #  1.    l3_port: 2854
            m = p14.match(line)
            if m:
                asic_info_key = int(m.group('idx'))
                asic_info = {
                    'member_info': {
                        'l3_port': int(m.group('l3_port'))
                    }
                }
                result.setdefault('hw_ip_mcg_info_asic_0', {})[asic_info_key] = asic_info
                continue

            # urid:0x1000000000000565 (l3m_entry: Mvrf:0 (2.2.2.2, 232.1.1.1))
            m = p15.match(line)
            if m:
                user = m.groupdict()
                urid = user.pop('urid')
                user_data = {
                    'urid': urid,
                    'l3m_entry': {
                        'mvrf': int(user.pop('mvrf')),
                        'ip': user.pop('ip'),
                        'group': user.pop('group')
                    }
                }
                result.setdefault('users', {})[urid] = user_data

        return result


class ShowPlatformSoftwareFedSwitchActiveIpMulticastInterfaceSchema(MetaParser):
    """Schema for
       * show platform software fed switch {module} ip multicast interface {if_id}
       * show platform software fed switch {module} ipv6 multicast interface {if_id}
    """

    schema = {
        'pim_state': str,
        'vrf_id': str,
        'hw_info_asic': {
            'hw_pim_state': str
        }
    }


class ShowPlatformSoftwareFedSwitchActiveIpMulticastInterface(ShowPlatformSoftwareFedSwitchActiveIpMulticastInterfaceSchema):
    """Parser for
       * show platform software fed switch {module} ip multicast interface {if_id}
       * show platform software fed switch {module} ipv6 multicast interface {if_id}
    """

    cli_command = [
        "show platform software fed {switch} {module} {ip_type} multicast interface {if_id}",
        "show platform software fed {module} {ip_type} multicast interface {if_id}"
    ]

    def cli(self, module, if_id, switch='', ip_type='', output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(module=module, if_id=if_id, switch=switch, ip_type=ip_type)
            else:
                cmd = self.cli_command[1].format(module=module, if_id=if_id, ip_type=ip_type)
            output = self.device.execute(cmd)

        # Initialize result dictionary
        ret_dict = {}

        # Pim State           :Enabled
        p1 = re.compile(r'^Pim State\s*:\s*(?P<pim_state>\S+)$')

        #   Vrf ID              :0
        p2 = re.compile(r'^Vrf ID\s*:\s*(?P<vrf_id>\S+)$')

        # Hw Pim State      :Enabled
        p3 = re.compile(r'^Hw Pim State\s*:\s*(?P<hw_pim_state>\S+)$')

        # Parse each line
        for line in output.splitlines():
            line = line.strip()

            #  Pim State           :Enabled
            match = p1.match(line)
            if match:
                ret_dict['pim_state'] = match.group('pim_state')
                continue

            #  Vrf ID              :0
            match = p2.match(line)
            if match:
                ret_dict['vrf_id'] = match.group('vrf_id')
                continue

            # Hw Pim State      :Enabled
            match = p3.match(line)
            if match:
                ret_dict.setdefault('hw_info_asic', {})['hw_pim_state'] = match.group('hw_pim_state')
                continue

        return ret_dict




class ShowPlatformSoftwareFedSwitchActivePortIfIdSchema(MetaParser):
    """Schema for show platform software fed switch active port if_id {if_id}"""
    schema = {
        "if_id": int,
        "if_name": str,
        "enable": bool,
        "speed": str,
        "operational_speed": Or(int, str),
        "duplex": str,
        "operational_duplex": str,
        "flowctrl": str,
        "csco_pd_enable": bool,
        "link_state": str,
        "csco_pd_restart_enable": bool,
        "tdr_result": bool,
        "psecure_inactivity_time": int,
        "psecure_feature_type": int,
        "loopback_enable": bool,
        "defaultVlan": int,
        "port_state": str,
        "mode": str,
    }

class ShowPlatformSoftwareFedSwitchActivePortIfId(ShowPlatformSoftwareFedSwitchActivePortIfIdSchema):
    """Parser for show platform software fed switch active port if_id {if_id}"""

    cli_command = ['show platform software fed {mode} port if_id {if_id}',
                   'show platform software fed {switch} {mode} port if_id {if_id}']

    def cli(self, mode, if_id, switch=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[1].format(switch=switch, mode=mode, if_id=if_id)
            else:
                cmd = self.cli_command[0].format(mode=mode, if_id=if_id)

            output = self.device.execute(cmd)

        ret_dict = {}

        # if_id = 186
        p1 = re.compile(r'^if_id\s*=\s*(?P<if_id>\d+)$')

        # if_name = GigabitEthernet0/0/0
        p2 = re.compile(r'^if_name\s*=\s*(?P<if_name>\S+)$')

        # enable : true
        p3 = re.compile(r'^enable\s*:\s*(?P<enable>\S+)$')

        # speed : auto
        p4 = re.compile(r'^speed\s*:\s*(?P<speed>\S+)$')

        # operational speed : 100
        p5 = re.compile(r'^operational speed\s*:\s*(?P<operational_speed>\S+)$')

        # duplex : auto
        p6 = re.compile(r'^duplex\s*:\s*(?P<duplex>\S+)$')

        # operational duplex : full
        p7 = re.compile(r'^operational duplex\s*:\s*(?P<operational_duplex>\S+)$')

        # flowctrl : none
        p8 = re.compile(r'^flowctrl\s*:\s*(?P<flowctrl>\S+)$')

        # csco pd enable : true
        p9 = re.compile(r'^csco pd enable\s*:\s*(?P<csco_pd_enable>\S+)$')

        # link state : up
        p10 = re.compile(r'^link state\s*:\s*(?P<link_state>\S+)$')

        # csco pd restart enable : true
        p11 = re.compile(r'^csco pd restart enable\s*:\s*(?P<csco_pd_restart_enable>\S+)$')

        # tdr_result : false
        p12 = re.compile(r'^tdr_result\s*:\s*(?P<tdr_result>\S+)$')

        # psecure_inactivity_time : 0
        p13 = re.compile(r'^psecure_inactivity_time\s*:\s*(?P<psecure_inactivity_time>\d+)$')

        # psecure_feature_type : 0
        p14 = re.compile(r'^psecure_feature_type\s*:\s*(?P<psecure_feature_type>\d+)$')

        # loopback enable : false
        p15 = re.compile(r'^loopback enable\s*:\s*(?P<loopback_enable>\S+)$')

        # defaultVlan : 1
        p16 = re.compile(r'^defaultVlan\s*:\s*(?P<defaultVlan>\d+)$')

        # port_state: Fed PM port ready
        p17 = re.compile(r'^port_state\s*:\s*(?P<port_state>.+)$')

        # mode : access
        p18 = re.compile(r'^mode\s*:\s*(?P<mode>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # if_id = 186
            m = p1.match(line)
            if m:
                ret_dict['if_id'] = int(m.groupdict()['if_id'])
                continue

            # if_name = TwoGigabitEthernet1/0/25
            m = p2.match(line)
            if m:
                ret_dict['if_name'] = m.groupdict()['if_name']
                continue

            # enable: true
            m = p3.match(line)
            if m:
                ret_dict['enable'] = m.groupdict()['enable'].lower() == 'true'
                continue

            # speed: auto
            m = p4.match(line)
            if m:
                ret_dict['speed'] = m.groupdict()['speed']
                continue

            # operational speed: 2500
            m = p5.match(line)
            if m:
                try:
                    ret_dict['operational_speed'] = int(m.groupdict()['operational_speed'])
                except ValueError:
                    ret_dict['operational_speed'] = m.groupdict()['operational_speed']
                continue

            # duplex: auto
            m = p6.match(line)
            if m:
                ret_dict['duplex'] = m.groupdict()['duplex']
                continue

            # operational duplex: full
            m = p7.match(line)
            if m:
                ret_dict['operational_duplex'] = m.groupdict()['operational_duplex']
                continue

            # flowctrl: on
            m = p8.match(line)
            if m:
                ret_dict['flowctrl'] = m.groupdict()['flowctrl']
                continue

            # csco pd enable: TRUE
            m = p9.match(line)
            if m:
                ret_dict['csco_pd_enable'] = m.groupdict()['csco_pd_enable'].lower() == 'true'
                continue

            # link state: UP
            m = p10.match(line)
            if m:
                ret_dict['link_state'] = m.groupdict()['link_state']
                continue

            # csco pd restart enable: TRUE
            m = p11.match(line)
            if m:
                ret_dict['csco_pd_restart_enable'] = m.groupdict()['csco_pd_restart_enable'].lower() == 'true'
                continue

            # tdr_result: FALSE
            m = p12.match(line)
            if m:
                ret_dict['tdr_result'] = m.groupdict()['tdr_result'].lower() == 'true'
                continue

            # psecure_inactivity_time: 0
            m = p13.match(line)
            if m:
                ret_dict['psecure_inactivity_time'] = int(m.groupdict()['psecure_inactivity_time'])
                continue

            # psecure_feature_type: 0
            m = p14.match(line)
            if m:
                ret_dict['psecure_feature_type'] = int(m.groupdict()['psecure_feature_type'])
                continue

            # loopback enable: FALSE
            m = p15.match(line)
            if m:
                ret_dict['loopback_enable'] = m.groupdict()['loopback_enable'].lower() == 'true'
                continue

            # defaultVlan: 4095
            m = p16.match(line)
            if m:
                ret_dict['defaultVlan'] = int(m.groupdict()['defaultVlan'])
                continue

            # port_state: Fed PM port ready
            m = p17.match(line)
            if m:
                ret_dict['port_state'] = m.groupdict()['port_state']
                continue

            # mode: routed
            m = p18.match(line)
            if m:
                ret_dict['mode'] = m.groupdict()['mode']
                continue

        return ret_dict


class ShowPlatformSoftwareFedActiveIfmInterfaceNameTunnel5Schema(MetaParser):
    """Schema for show platform software fed active ifm interface_name tunnel5"""
    schema = {
        'interface_if_id': str,
        'interface_name': str,
        'interface_block_pointer': str,
        'interface_block_state': str,
        'interface_state': str,
        'interface_status': str,
        'interface_ref_cnt': int,
        'interface_type': str,
        'bootup_breakout_config': {
            'slot': int,
            'port': int,
            'unit': int,
            'snmp_if_index': int,
            'tunnel_mode': str,
            'hw_support': str,
            'tunnel_vrf': int,
            'ipv4_mtu': int,
            'ipv6_mtu': int,
            'ipv4_vrf_id': int,
            'ipv6_vrf_id': int,
            'protocol_flags': str,
            'misc_flags': str,
            'icmpv4_flags': str,
            'icmpv6_flags': str,
        },
        'ref_count': int,
        'ifm_feature_subblock_information': {
            'port_l3tunnel_subblock': {
                'src_ip': str,
                'mtu': int,
                'mod_flags': int,
                'tun_mode': str,
                'vrf': int,
                'v6_tableid': str,
                'tvrf': int,
                'ttl': int,
                'tos': int,
                'stag': int,
                'tun_flags': int,
                'tun_enabled': str,
            },
            'port_l3tunnel_npd_subblock': {
                'rm_handle': int,
                'port_gid': int,
                'tport_gid': int,
                'asic': int,
                'port_oid': str,
                'tport_oid': str,
                'mdt_decap_oid': str,
                'ing_counter_oid': str,
                'egr_counter_oid': str,
            },
            'port_cts_subblock': {
                'disable_sgacl': str,
                'trust': str,
                'propagate': str,
                'port_sgt': str,
            }
        }
    }

class ShowPlatformSoftwareFedActiveIfmInterfaceNameTunnel5(ShowPlatformSoftwareFedActiveIfmInterfaceNameTunnel5Schema):
    """Parser for show platform software fed active ifm interface_name tunnel5"""

    cli_command = 'show platform software fed active ifm interface_name tunnel5'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # Interface IF_ID         : 0x000000000000044f
        p1 = re.compile(r'^Interface IF_ID\s+:\s+(?P<interface_if_id>\S+)$')

        # Interface Name          : Tunnel5
        p2 = re.compile(r'^Interface Name\s+:\s+(?P<interface_name>\S+)$')

        # Interface Block Pointer : 0x7d13d14ceb38
        p3 = re.compile(r'^Interface Block Pointer\s+:\s+(?P<interface_block_pointer>\S+)$')

        # Interface Block State   : Ready
        p4 = re.compile(r'^Interface Block State\s+:\s+(?P<interface_block_state>\S+)$')

        # Interface State         : Enabled
        p5 = re.compile(r'^Interface State\s+:\s+(?P<interface_state>\S+)$')

        # Interface Status        : UPD,
        p6 = re.compile(r'^Interface Status\s+:\s+(?P<interface_status>[\S\s]+)$')

        # Interface Ref-Cnt       : 1
        p7 = re.compile(r'^Interface Ref-Cnt\s+:\s+(?P<interface_ref_cnt>\d+)$')

        # Interface Type          : TUNNEL
        p8 = re.compile(r'^Interface Type\s+:\s+(?P<interface_type>\S+)$')

        # Bootup breakout Config Done Slot 0: Port: 0
        p9 = re.compile(r'^Bootup breakout Config Done Slot (?P<slot>\d+): Port: (?P<port>\d+)$')

        # Unit           : 0
        p10 = re.compile(r'^Unit\s+:\s+(?P<unit>\d+)$')

        # SNMP IF Index  : 0
        p11 = re.compile(r'^SNMP IF Index\s+:\s+(?P<snmp_if_index>\d+)$')

        # Tunnel Mode    : 12 [MDT GRE]
        p12 = re.compile(r'^Tunnel Mode\s+:\s+(?P<tunnel_mode>[\S\s]+)$')

        # Hw Support     : No
        p13 = re.compile(r'^Hw Support\s+:\s+(?P<hw_support>\S+)$')

        # Tunnel Vrf     : 0
        p14 = re.compile(r'^Tunnel Vrf\s+:\s+(?P<tunnel_vrf>\d+)$')

        # IPv4 MTU       : 0
        p15 = re.compile(r'^IPv4 MTU\s+:\s+(?P<ipv4_mtu>\d+)$')

        # IPv6 MTU       : 0
        p16 = re.compile(r'^IPv6 MTU\s+:\s+(?P<ipv6_mtu>\d+)$')

        # IPv4 VRF ID    : 0
        p17 = re.compile(r'^IPv4 VRF ID\s+:\s+(?P<ipv4_vrf_id>\d+)$')

        # IPv6 VRF ID    : 0
        p18 = re.compile(r'^IPv6 VRF ID\s+:\s+(?P<ipv6_vrf_id>\d+)$')

        # Protocol flags : 0x0007 [ ipv4 ipv6 pim_ipv4 ]
        p19 = re.compile(r'^Protocol flags\s+:\s+(?P<protocol_flags>[\S\s]+)$')

        # Misc flags     : 0x0005 [ ipv4 mcast_v4 ]
        p20 = re.compile(r'^Misc flags\s+:\s+(?P<misc_flags>[\S\s]+)$')

        # ICMPv4 flags   : 0x00 [ None ]
        p21 = re.compile(r'^ICMPv4 flags\s+:\s+(?P<icmpv4_flags>[\S\s]+)$')

        # ICMPv6 flags   : 0x00 [ None ]
        p22 = re.compile(r'^ICMPv6 flags\s+:\s+(?P<icmpv6_flags>[\S\s]+)$')

        # Ref Count : 1 (feature Ref Counts + 1)
        p23 = re.compile(r'^Ref Count\s+:\s+(?P<ref_count>\d+)')

        # Src IP ............ [1.1.1.1]
        p24 = re.compile(r'^Src IP\s+\.+\s+\[(?P<src_ip>\S+)\]$')

        # MTU ............... [1500]
        p25 = re.compile(r'^MTU\s+\.+\s+\[(?P<mtu>\d+)\]$')

        # mod_flags ......... [0]
        p26 = re.compile(r'^mod_flags\s+\.+\s+\[(?P<mod_flags>\d+)\]$')

        # Tun Mode .......... [0]
        p27 = re.compile(r'^Tun Mode\s+\.+\s+\[(?P<tun_mode>\d+)\]$')

        # vrf ............... [2]
        p28 = re.compile(r'^vrf\s+\.+\s+\[(?P<vrf>\d+)\]$')

        # v6_tableid ........ [0xffff]
        p29 = re.compile(r'^v6_tableid\s+\.+\s+\[(?P<v6_tableid>\S+)\]$')

        # tvrf .............. [0]
        p30 = re.compile(r'^tvrf\s+\.+\s+\[(?P<tvrf>\d+)\]$')

        # ttl ............... [0]
        p31 = re.compile(r'^ttl\s+\.+\s+\[(?P<ttl>\d+)\]$')

        # tos ............... [0]
        p32 = re.compile(r'^tos\s+\.+\s+\[(?P<tos>\d+)\]$')

        # stag .............. [0]
        p33 = re.compile(r'^stag\s+\.+\s+\[(?P<stag>\d+)\]$')

        # Tun flags ......... [0]
        p34 = re.compile(r'^Tun flags\s+\.+\s+\[(?P<tun_flags>\d+)\]$')

        # Tun Enabled ....... [Yes(1)]
        p35 = re.compile(r'^Tun Enabled\s+\.+\s+\[(?P<tun_enabled>[\S\s]+)\]$')

        # Rm handle ......... [0]
        p36 = re.compile(r'^Rm handle\s+\.+\s+\[(?P<rm_handle>\d+)\]$')

        # Port Gid .......... [17]
        p37 = re.compile(r'^Port Gid\s+\.+\s+\[(?P<port_gid>\d+)\]$')

        # tPort Gid ......... [16]
        p38 = re.compile(r'^tPort Gid\s+\.+\s+\[(?P<tport_gid>\d+)\]$')

        # Asic .............. [0]
        p39 = re.compile(r'^Asic\s+\.+\s+\[(?P<asic>\d+)\]$')

        # Port OID .......... [0x602]
        p40 = re.compile(r'^Port OID\s+\.+\s+\[(?P<port_oid>\S+)\]$')

        # tPort OID ......... [0x5fb]
        p41 = re.compile(r'^tPort OID\s+\.+\s+\[(?P<tport_oid>\S+)\]$')

        # mdt decap OID ...... [0x603]
        p42 = re.compile(r'^mdt decap OID\s+\.+\s+\[(?P<mdt_decap_oid>\S+)\]$')

        # Ing Counter OID ... [0x604]
        p43 = re.compile(r'^Ing Counter OID\s+\.+\s+\[(?P<ing_counter_oid>\S+)\]$')

        # Egr Counter OID ... [0x600]
        p44 = re.compile(r'^Egr Counter OID\s+\.+\s+\[(?P<egr_counter_oid>\S+)\]$')

        # Disable SGACL .................... [0x0]
        p45 = re.compile(r'^Disable SGACL\s+\.+\s+\[(?P<disable_sgacl>\S+)\]$')

        # Trust ............................ [0x0]
        p46 = re.compile(r'^Trust\s+\.+\s+\[(?P<trust>\S+)\]$')

        # Propagate ........................ [0x0]
        p47 = re.compile(r'^Propagate\s+\.+\s+\[(?P<propagate>\S+)\]$')

        # Port SGT ......................... [0xffff]
        p48 = re.compile(r'^Port SGT\s+\.+\s+\[(?P<port_sgt>\S+)\]$')

        for line in output.splitlines():
            line = line.strip()

            # Interface IF_ID         : 0x000000000000044f
            m = p1.match(line)
            if m:
                ret_dict['interface_if_id'] = m.groupdict()['interface_if_id']
                continue

            # Interface Name          : Tunnel5
            m = p2.match(line)
            if m:
                ret_dict['interface_name'] = m.groupdict()['interface_name']
                continue

            # Interface Block Pointer : 0x7d13d14ceb38
            m = p3.match(line)
            if m:
                ret_dict['interface_block_pointer'] = m.groupdict()['interface_block_pointer']
                continue

            # Interface Block State   : Ready
            m = p4.match(line)
            if m:
                ret_dict['interface_block_state'] = m.groupdict()['interface_block_state']
                continue

            # Interface State         : Enabled
            m = p5.match(line)
            if m:
                ret_dict['interface_state'] = m.groupdict()['interface_state']
                continue

            # Interface Status        : UPD,
            m = p6.match(line)
            if m:
                ret_dict['interface_status'] = m.groupdict()['interface_status']
                continue

            # Interface Ref-Cnt       : 1
            m = p7.match(line)
            if m:
                ret_dict['interface_ref_cnt'] = int(m.groupdict()['interface_ref_cnt'])
                continue

            # Interface Type          : TUNNEL
            m = p8.match(line)
            if m:
                ret_dict['interface_type'] = m.groupdict()['interface_type']
                continue

            # Bootup breakout Config Done Slot 0: Port: 0
            m = p9.match(line)
            if m:
                bootup_dict = ret_dict.setdefault('bootup_breakout_config', {})
                bootup_dict['slot'] = int(m.groupdict()['slot'])
                bootup_dict['port'] = int(m.groupdict()['port'])
                continue

            # Unit           : 0
            m = p10.match(line)
            if m:
                bootup_dict['unit'] = int(m.groupdict()['unit'])
                continue

            # SNMP IF Index  : 0
            m = p11.match(line)
            if m:
                bootup_dict['snmp_if_index'] = int(m.groupdict()['snmp_if_index'])
                continue

            # Tunnel Mode    : 12 [MDT GRE]
            m = p12.match(line)
            if m:
                bootup_dict['tunnel_mode'] = m.groupdict()['tunnel_mode']
                continue

            # Hw Support     : No
            m = p13.match(line)
            if m:
                bootup_dict['hw_support'] = m.groupdict()['hw_support']
                continue

            # Tunnel Vrf     : 0
            m = p14.match(line)
            if m:
                bootup_dict['tunnel_vrf'] = int(m.groupdict()['tunnel_vrf'])
                continue

            # IPv4 MTU       : 0
            m = p15.match(line)
            if m:
                bootup_dict['ipv4_mtu'] = int(m.groupdict()['ipv4_mtu'])
                continue

            # IPv6 MTU       : 0
            m = p16.match(line)
            if m:
                bootup_dict['ipv6_mtu'] = int(m.groupdict()['ipv6_mtu'])
                continue

            # IPv4 VRF ID    : 0
            m = p17.match(line)
            if m:
                bootup_dict['ipv4_vrf_id'] = int(m.groupdict()['ipv4_vrf_id'])
                continue

            # IPv6 VRF ID    : 0
            m = p18.match(line)
            if m:
                bootup_dict['ipv6_vrf_id'] = int(m.groupdict()['ipv6_vrf_id'])
                continue

            # Protocol flags : 0x0007 [ ipv4 ipv6 pim_ipv4 ]
            m = p19.match(line)
            if m:
                bootup_dict['protocol_flags'] = m.groupdict()['protocol_flags']
                continue

            # Misc flags     : 0x0005 [ ipv4 mcast_v4 ]
            m = p20.match(line)
            if m:
                bootup_dict['misc_flags'] = m.groupdict()['misc_flags']
                continue

            # ICMPv4 flags   : 0x00 [ None ]
            m = p21.match(line)
            if m:
                bootup_dict['icmpv4_flags'] = m.groupdict()['icmpv4_flags']
                continue

            # ICMPv6 flags   : 0x00 [ None ]
            m = p22.match(line)
            if m:
                bootup_dict['icmpv6_flags'] = m.groupdict()['icmpv6_flags']
                continue

            # Ref Count : 1 (feature Ref Counts + 1)
            m = p23.match(line)
            if m:
                ret_dict['ref_count'] = int(m.groupdict()['ref_count'])
                continue

            # Src IP ............ [1.1.1.1]
            m = p24.match(line)
            if m:
                subblock_dict = ret_dict.setdefault('ifm_feature_subblock_information', {}).setdefault('port_l3tunnel_subblock', {})
                subblock_dict['src_ip'] = m.groupdict()['src_ip']
                continue

            # MTU ............... [1500]
            m = p25.match(line)
            if m:
                subblock_dict['mtu'] = int(m.groupdict()['mtu'])
                continue

            # mod_flags ......... [0]
            m = p26.match(line)
            if m:
                subblock_dict['mod_flags'] = int(m.groupdict()['mod_flags'])
                continue

            # Tun Mode .......... [0]
            m = p27.match(line)
            if m:
                subblock_dict['tun_mode'] = m.groupdict()['tun_mode']
                continue

            # vrf ............... [2]
            m = p28.match(line)
            if m:
                subblock_dict['vrf'] = int(m.groupdict()['vrf'])
                continue

            # v6_tableid ........ [0xffff]
            m = p29.match(line)
            if m:
                subblock_dict['v6_tableid'] = m.groupdict()['v6_tableid']
                continue

            # tvrf .............. [0]
            m = p30.match(line)
            if m:
                subblock_dict['tvrf'] = int(m.groupdict()['tvrf'])
                continue

            # ttl ............... [0]
            m = p31.match(line)
            if m:
                subblock_dict['ttl'] = int(m.groupdict()['ttl'])
                continue

            # tos ............... [0]
            m = p32.match(line)
            if m:
                subblock_dict['tos'] = int(m.groupdict()['tos'])
                continue

            # stag .............. [0]
            m = p33.match(line)
            if m:
                subblock_dict['stag'] = int(m.groupdict()['stag'])
                continue

            # Tun flags ......... [0]
            m = p34.match(line)
            if m:
                subblock_dict['tun_flags'] = int(m.groupdict()['tun_flags'])
                continue

            # Tun Enabled ....... [Yes(1)]
            m = p35.match(line)
            if m:
                subblock_dict['tun_enabled'] = m.groupdict()['tun_enabled']
                continue

            # Rm handle ......... [0]
            m = p36.match(line)
            if m:
                npd_subblock_dict = ret_dict.setdefault('ifm_feature_subblock_information', {}).setdefault('port_l3tunnel_npd_subblock', {})
                npd_subblock_dict['rm_handle'] = int(m.groupdict()['rm_handle'])
                continue

            # Port Gid .......... [17]
            m = p37.match(line)
            if m:
                npd_subblock_dict['port_gid'] = int(m.groupdict()['port_gid'])
                continue

            # tPort Gid ......... [16]
            m = p38.match(line)
            if m:
                npd_subblock_dict['tport_gid'] = int(m.groupdict()['tport_gid'])
                continue

            # Asic .............. [0]
            m = p39.match(line)
            if m:
                npd_subblock_dict['asic'] = int(m.groupdict()['asic'])
                continue

            # Port OID .......... [0x602]
            m = p40.match(line)
            if m:
                npd_subblock_dict['port_oid'] = m.groupdict()['port_oid']
                continue

            # tPort OID ......... [0x5fb]
            m = p41.match(line)
            if m:
                npd_subblock_dict['tport_oid'] = m.groupdict()['tport_oid']
                continue

            # mdt decap OID ...... [0x603]
            m = p42.match(line)
            if m:
                npd_subblock_dict['mdt_decap_oid'] = m.groupdict()['mdt_decap_oid']
                continue

            # Ing Counter OID ... [0x604]
            m = p43.match(line)
            if m:
                npd_subblock_dict['ing_counter_oid'] = m.groupdict()['ing_counter_oid']
                continue

            # Egr Counter OID ... [
            m = p44.match(line)
            if m:
                npd_subblock_dict['egr_counter_oid'] = m.groupdict()['egr_counter_oid']
                continue

            # Disable SGACL .................... [0x0]
            m = p45.match(line)
            if m:
                cts_subblock_dict = ret_dict.setdefault('ifm_feature_subblock_information', {}).setdefault('port_cts_subblock', {})
                cts_subblock_dict['disable_sgacl'] = m.groupdict()['disable_sgacl']
                continue

            # Trust ............................ [0x0]
            m = p46.match(line)
            if m:
                cts_subblock_dict['trust'] = m.groupdict()['trust']
                continue

            # Propagate ........................ [0x0]
            m = p47.match(line)
            if m:
                cts_subblock_dict['propagate'] = m.groupdict()['propagate']
                continue

            # Port SGT ......................... [0xffff]
            m = p48.match(line)
            if m:
                cts_subblock_dict['port_sgt'] = m.groupdict()['port_sgt']
                continue

        return ret_dict

class ShowPlatformSoftwareFedSwitchActiveOifsetUridSchema(MetaParser):
    """Schema for
       * show platform software fed switch active oifset urid <id>
       * show platform software fed switch active oifset urid <id> detail
    """

    schema = {
        'type': str,
        'state': str,
        'md5': str,
        'fset_urid': str,
        'remote_port_count': int,
        Optional('svi_port_count'): int,
        'users_count': int,
        Optional('mioitem_count'): int,
        Optional('interfaces'): {
            int: {
                'adjid': str,
                'interface': str,
                'physicalif': str,
                'iftype': str,
                'flags': str,
                Optional('urids'): {
                    'mio': str,
                    'parent': str,
                    'child_repl': str,
                    'adj_obj': str,
                },
                Optional('asic'): {
                    'asic_index': str,
                    'l3_port_oid': int,
                    'port_oid': int,
                }
            }
        },
        Optional('fset_mcidgid'): int,
        'asic_0_mcid_oid': int,
        Optional('hw_ip_mcg_info_asic_0'): {
            int: {
                Optional('member_info'): {
                    'l2_mcg': int,
                    'cookie': str,
                    'l3_port': int,
                }
            }
        },
        Optional('users'): {
            str: {
                'urid': str,
                Optional('l3m_entry'): {
                    'mvrf': int,
                    'ip': str,
                    'group': str
                }
            }
        }
    }


class ShowPlatformSoftwareFedSwitchActiveOifsetUrid(ShowPlatformSoftwareFedSwitchActiveOifsetUridSchema):
    """Parser for
       * show platform software fed switch active oifset urid <id>
       * show platform software fed switch active oifset urid <id> detail
    """

    cli_command = [
        'show platform software fed switch {active} oifset urid {id}',
        'show platform software fed switch {active} oifset urid {id} {detail}'
    ]

    def cli(self, id, detail="",active="", output=None):
        if output is None:
            if detail:
                cmd = self.cli_command[1].format(id=id, active=active, detail=detail)
            else:
                cmd = self.cli_command[0].format(id=id, active=active)
            output = self.device.execute(cmd)

        # Initialize an empty result dictionary
        result = {}

        # Regex patterns to match the lines
        # Type: s_g_vrf              State: allocated       MD5:(606b9e45e551431a:e7637c8a2fbd4182)
        p1 = re.compile(r'Type:\s+(?P<type>\S+)\s+State:\s+(?P<state>\S+)\s+MD5:\((?P<md5>[\da-f:]+)\)')

        # Fset Urid                    : 0x3000000000000008
        p2 = re.compile(r'Fset Urid\s+:\s+(?P<fset_urid>\S+)')

        # Remote Port Count            : 0
        p3 = re.compile(r'Remote Port Count\s+:\s+(?P<remote_port_count>\d+)')

        # Svi Port Count               : 1
        p4 = re.compile(r'Svi Port Count\s+:\s+(?P<svi_port_count>\d+)')

        # Users Count                  : 1
        p5 = re.compile(r'Users Count\s+:\s+(?P<users_count>\d+)')

        # Mioitem Count                : 1
        p6 = re.compile(r'Mioitem Count\s+:\s+(?P<mioitem_count>\d+)')

        # No. AdjID          Interface          PhysicalIf        IfType          Flags
        p7 = re.compile(r'^\s*(?P<no>\d+)\.\s+(?P<adjid>\S+)\s+(?P<interface>\S+)\s+(?P<physicalif>\S+)\s+(?P<iftype>\S+)\s+(?P<flags>[\S\s]+)')

        # Urids   => Mio:0x80::6 Parent:0x60::4 child_repl:0x20::11(113854e3)  adj_obj:0x90::2
        p8 = re.compile(r'Urids\s+=>\s+Mio:(?P<mio>\S+)\s+Parent:(?P<parent>\S+)\s+child_repl:(?P<child_repl>\S+)\(\S+\s+adj_obj:(?P<adj_obj>\S+)')

        # (Asic[0]=> l3_port_oid/port_oid : 1543 / 0 )
        p9 = re.compile(r'\(Asic\[(?P<asic_index>\d+)\]=>\s+l3_port_oid\/port_oid\s+:\s+(?P<l3_port_oid>\d+)\s+\/\s+(?P<port_oid>\d+)\s+\)')

        # Fset MCID Gid                : 8216
        p10 = re.compile(r'Fset MCID Gid\s+:\s+(?P<fset_mcidgid>\d+)')

        # Asic[0] mcid_oid             : 1541
        p11 = re.compile(r'Asic\[(?P<asic_index>\d+)\]\s+mcid_oid\s+:\s+(?P<asic_0_mcid_oid>\d+)')

        # Hw IP Mcg Info Asic[0] :
        p12 = re.compile(r'Hw IP Mcg Info Asic\[(?P<asic_index>\d+)\] :')

        # Idx.    Member Info
        p13 = re.compile(r'^\s*(?P<idx>\d+)\.\s+(?P<member_info>\S+\s*\S+)')

        # 1.    l2_mcg: 1543 (cookie: urid:0x20::11), l3_port: 1505
        p14 = re.compile(r'^\s*(?P<idx>\d+)\.\s+l2_mcg:\s+(?P<l2_mcg>\d+)\s+\(cookie:\s+urid:(?P<cookie>\S+)\),\s+l3_port:\s+(?P<l3_port>\d+)')

        # urid:0x100000000000002f (l3m_entry: Mvrf:0 (13.13.13.2, 225.0.0.1))
        p15 = re.compile(r'urid:(?P<urid>\S+)\s+\(l3m_entry:\s+Mvrf:(?P<mvrf>\d+)\s+\((?P<ip>\d+\.\d+\.\d+\.\d+),\s+(?P<group>\d+\.\d+\.\d+\.\d+)\)\)')

        # Parsing logic
        for line in output.splitlines():
            line = line.strip()

            # Type: s_g_vrf              State: allocated       MD5:(606b9e45e551431a:e7637c8a2fbd4182)
            m = p1.match(line)
            if m:
                result.update(m.groupdict())
                continue

            # Fset Urid                    : 0x3000000000000008
            m = p2.match(line)
            if m:
                result['fset_urid'] = m.group('fset_urid')
                continue

            # Remote Port Count            : 0
            m = p3.match(line)
            if m:
                result['remote_port_count'] = int(m.group('remote_port_count'))
                continue

            # Svi Port Count               : 1
            m = p4.match(line)
            if m:
                result['svi_port_count'] = int(m.group('svi_port_count'))
                continue

            # Users Count                  : 1
            m = p5.match(line)
            if m:
                result['users_count'] = int(m.group('users_count'))
                continue

            # Mioitem Count                : 1
            m = p6.match(line)
            if m:
                result['mioitem_count'] = int(m.group('mioitem_count'))
                continue

            # No. AdjID          Interface          PhysicalIf        IfType          Flags
            # 1. 0xf8004af1     Vl20               -----------       svi_if          InHw IngressRep
            m = p7.match(line)
            if m:
                interface = m.groupdict()
                interface['no'] = int(interface['no'])
                interface_key = interface.pop('no')  # Remove 'no' from the interface details
                result.setdefault('interfaces', {})[interface_key] = interface
                continue

            # Urids   => Mio:0x80::6 Parent:0x60::4 child_repl:0x20::11(113854e3)  adj_obj:0x90::2
            m = p8.match(line)
            if m and 'interfaces' in result:
                urids = m.groupdict()
                result['interfaces'][interface_key]['urids'] = urids
                continue

            # (Asic[0]=> l3_port_oid/port_oid : 1543 / 0 )
            m = p9.match(line)
            if m and 'interfaces' in result:
                asic = m.groupdict()
                asic['l3_port_oid'] = int(asic['l3_port_oid'])
                asic['port_oid'] = int(asic['port_oid'])
                result['interfaces'][interface_key]['asic'] = asic
                continue

            # Fset MCID Gid                : 8216
            m = p10.match(line)
            if m:
                result['fset_mcidgid'] = int(m.group('fset_mcidgid'))
                continue

            # Asic[0] mcid_oid             : 1541
            m = p11.match(line)
            if m:
                result['asic_0_mcid_oid'] = int(m.group('asic_0_mcid_oid'))
                continue

            # Idx.    Member Info
            # 1.    l2_mcg: 1543 (cookie: urid:0x20::11), l3_port: 1505
            m = p14.match(line)
            if m:
                asic_info_key = int(m.group('idx'))
                asic_info = {
                    'member_info': {
                        'l2_mcg': int(m.group('l2_mcg')),
                        'cookie': m.group('cookie'),
                        'l3_port': int(m.group('l3_port'))
                    }
                }
                result.setdefault('hw_ip_mcg_info_asic_0', {})[asic_info_key] = asic_info
                continue

            # urid:0x100000000000002f (l3m_entry: Mvrf:0 (13.13.13.2, 225.0.0.1))
            m = p15.match(line)
            if m:
                user = m.groupdict()
                urid = user.pop('urid')
                user_data = {
                    'urid': urid,
                    'l3m_entry': {
                        'mvrf': int(user.pop('mvrf')),
                        'ip': user.pop('ip'),
                        'group': user.pop('group')
                    }
                }
                result.setdefault('users', {})[urid] = user_data
                continue

        return result


class ShowPlatformSoftwareFedSwitchActiveOifsetSchema(MetaParser):
    """Schema for show platform software fed switch active oifset"""
    schema = {
        'l2m_fset_current_count': int,
        'l2m_fset_max_reached': int,
        'l2m_current_vp_oif_count': int,
        'l2m_vp_oif_max_reached': int,
        'l2m_fset_last_used_urid': str,
        'l3m_fset_current_count': int,
        'l3m_fset_max_reached': int,
        'l3m_current_oif_count': int,
        'l3m_oif_max_reached': int,
        'l3m_fset_last_used_urid': str,
        'l3m_fset_oif_last_used_urid': str,
        'oif_obj_fset_current_count': int,
        'oif_obj_fset_max_reached': int,
    }

class ShowPlatformSoftwareFedSwitchActiveOifset(ShowPlatformSoftwareFedSwitchActiveOifsetSchema):
    """Parser for show platform software fed switch active oifset"""
    cli_command = [
        'show platform software fed {switch} {active} oifset',
        'show platform software fed {active} oifset'
        ]

    def cli(self, switch="", active="", output=None):
        if output is None:
            if switch:
                output = self.device.execute(self.cli_command[0].format(switch=switch, active=active))
            else:
                output = self.device.execute(self.cli_command[1].format(active=active))

        ret_dict = {}

        # L2M Fset Current Count / Max Reached          : 17 / 17
        p1 = re.compile(r'^L2M Fset Current Count / Max Reached\s+:\s+(?P<current>\d+)\s+/\s+(?P<max>\d+)$')

        # L2M current vp_oif count / Max Reached        : 2 / 4
        p2 = re.compile(r'^L2M current vp_oif count / Max Reached\s+:\s+(?P<current>\d+)\s+/\s+(?P<max>\d+)$')

        # L2M Fset Last Used Urid                       : 0x2000000000000011 (changes/sec:0 approx.)
        p3 = re.compile(r'^L2M Fset Last Used Urid\s+:\s+(?P<urid>\S+)\s+\(changes/sec:\d+\s+approx.\)$')

        # L3M Fset Current Count / Max Reached          : 11 / 13
        p4 = re.compile(r'^L3M Fset Current Count / Max Reached\s+:\s+(?P<current>\d+)\s+/\s+(?P<max>\d+)$')

        # L3M current oif count /Max Reached            : 8 / 8
        p5 = re.compile(r'^L3M current oif count /Max Reached\s+:\s+(?P<current>\d+)\s+/\s+(?P<max>\d+)$')

        # L3M Fset Last Used Urid                       : 0x300000000000000d (changes/sec:0 approx.)
        p6 = re.compile(r'^L3M Fset Last Used Urid\s+:\s+(?P<urid>\S+)\s+\(changes/sec:\d+\s+approx.\)$')

        # L3M Fset Oif Last Used Urid                   : 0x8000000000000008 (changes/sec:0 approx.)
        p7 = re.compile(r'^L3M Fset Oif Last Used Urid\s+:\s+(?P<urid>\S+)\s+\(changes/sec:\d+\s+approx.\)$')

        # Oif_Obj Fset Current Count / Max Reached      : 6 / 6
        p8 = re.compile(r'^Oif_Obj Fset Current Count / Max Reached\s+:\s+(?P<current>\d+)\s+/\s+(?P<max>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # L2M Fset Current Count / Max Reached          : 17 / 17
            m = p1.match(line)
            if m:
                ret_dict['l2m_fset_current_count'] = int(m.groupdict()['current'])
                ret_dict['l2m_fset_max_reached'] = int(m.groupdict()['max'])
                continue

            # L2M current vp_oif count / Max Reached        : 2 / 4
            m = p2.match(line)
            if m:
                ret_dict['l2m_current_vp_oif_count'] = int(m.groupdict()['current'])
                ret_dict['l2m_vp_oif_max_reached'] = int(m.groupdict()['max'])
                continue

            # L2M Fset Last Used Urid                       : 0x2000000000000011 (changes/sec:0 approx.)
            m = p3.match(line)
            if m:
                ret_dict['l2m_fset_last_used_urid'] = m.groupdict()['urid']
                continue

            # L3M Fset Current Count / Max Reached          : 11 / 13
            m = p4.match(line)
            if m:
                ret_dict['l3m_fset_current_count'] = int(m.groupdict()['current'])
                ret_dict['l3m_fset_max_reached'] = int(m.groupdict()['max'])
                continue

            # L3M current oif count /Max Reached            : 8 / 8
            m = p5.match(line)
            if m:
                ret_dict['l3m_current_oif_count'] = int(m.groupdict()['current'])
                ret_dict['l3m_oif_max_reached'] = int(m.groupdict()['max'])
                continue

            # L3M Fset Last Used Urid                       : 0x300000000000000d (changes/sec:0 approx.)
            m = p6.match(line)
            if m:
                ret_dict['l3m_fset_last_used_urid'] = m.groupdict()['urid']
                continue

            # L3M Fset Oif Last Used Urid                   : 0x8000000000000008 (changes/sec:0 approx.)
            m = p7.match(line)
            if m:
                ret_dict['l3m_fset_oif_last_used_urid'] = m.groupdict()['urid']
                continue

            # Oif_Obj Fset Current Count / Max Reached      : 6 / 6
            m = p8.match(line)
            if m:
                ret_dict['oif_obj_fset_current_count'] = int(m.groupdict()['current'])
                ret_dict['oif_obj_fset_max_reached'] = int(m.groupdict()['max'])
                continue

        return ret_dict
    
class ShowPlatformSoftwareFedSwAcAccessSecurityAuthAclSumSchema(MetaParser):
    """Schema for 'show platform software fed switch {switch_type} access-security auth-acl sum'"""
    schema = {
        'auth_acl_summary': {
            Any(): {
                'asic': int,
                'auth_behavior': str,
                'ipv4_acl_oid': int,
                'ipv4_drop_count': int,
                'ipv6_acl_oid': int,
                'ipv6_drop_count': int,
                'mac_acl_oid': int,
                'mac_drop_count': int,
            }
        }
    }

class ShowPlatformSoftwareFedSwAcAccessSecurityAuthAclSum(ShowPlatformSoftwareFedSwAcAccessSecurityAuthAclSumSchema):
    """Parser for 'show platform software fed switch {switch_type} access-security auth-acl summary'"""

    cli_command = 'show platform software fed switch {switch_type} access-security auth-acl summary'

    def cli(self, switch_type, output=None):
        if output is None:
            output = self.device.execute(
                self.cli_command.format(switch_type=switch_type)
            )

        # Initialize parsed_data as an empty dictionary
        parsed_data = {}
        
        # 0    FWD_ALL_LRN_ALL    487                   0                     497                   0                     507                   0
        # 0    FWD_ALL_LRN_DATA   489                   0                     499                   0                     509                   0
        # 0    DROP_ALL_NO_LRN    491                   0                     501                   0                     511                   0
        # 0    DROP_ALL_LRN_DATA  494                   0                     504                   0                     514                   0
        p1 = re.compile(
            r'(?P<asic>\d+)\s+(?P<auth_behavior>\S+)\s+(?P<ipv4_acl_oid>\d+)\s+(?P<ipv4_drop_count>\d+)\s+(?P<ipv6_acl_oid>\d+)\s+(?P<ipv6_drop_count>\d+)\s+(?P<mac_acl_oid>\d+)\s+(?P<mac_drop_count>\d+)'
        )

        for line in output.splitlines():
            line = line.strip()
            
            # 0    FWD_ALL_LRN_ALL    487                   0                     497                   0                     507                   0
            # 0    FWD_ALL_LRN_DATA   489                   0                     499                   0                     509                   0
            # 0    DROP_ALL_NO_LRN    491                   0                     501                   0                     511                   0
            # 0    DROP_ALL_LRN_DATA  494                   0                     504                   0                     514                   0
            match = p1.match(line)
            if match:
                key = f"{match.group('asic')}_{match.group('auth_behavior')}"
                parsed_data.setdefault("auth_acl_summary",{})
                parsed_data['auth_acl_summary'][key] = {
                    'asic': int(match.group('asic')),
                    'auth_behavior': match.group('auth_behavior'),
                    'ipv4_acl_oid': int(match.group('ipv4_acl_oid')),
                    'ipv4_drop_count': int(match.group('ipv4_drop_count')),
                    'ipv6_acl_oid': int(match.group('ipv6_acl_oid')),
                    'ipv6_drop_count': int(match.group('ipv6_drop_count')),
                    'mac_acl_oid': int(match.group('mac_acl_oid')),
                    'mac_drop_count': int(match.group('mac_drop_count'))
                }

        return parsed_data

class ShowPlatformsoftwarefedswitchactivesecurityfedpmifidSchema(MetaParser):
    """Schema for 'show platform security pm information'"""

    schema = {
        'iif_id': str,
        'iif_name': str,
        'auth_behavior': {
            'value': int,
            'description': str,
        },
        'secure_feature': {
            'flags': str,
            'description': str,
        },
        'psec_inactivity_time': int,
        Optional('l2_port_platform_information'): {
            'security_feature_flags': {
                'description': str,
                'asic': int,
                'accsec_logical_id': int,
            },
            'accsec_auth_acl_behavior': str,
            'l2_port_accsec_feature': str,
            'accsec_table_feature_type': str,
            'accsec_table_mask_type': str,
        }
    }

class ShowPlatformsoftwarefedswitchactivesecurityfedpmifid(ShowPlatformsoftwarefedswitchactivesecurityfedpmifidSchema):
    """Parser for 'show platform software fed switch {switch_type} security-fed pm if-id {port_if_id} '"""

    cli_command = "show platform software fed switch {switch_type} security-fed pm if-id {port_if_id}"

    def cli(self, switch_type,port_if_id,output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch_type=switch_type, port_if_id=port_if_id))

        # Initialize the dictionary
        ret_dict = {}

        # IIF-ID   = 000000000000040d 
        p1 = re.compile(r'IIF-ID\s*=\s*(?P<iif_id>\S+)')

        # IIF-Name = GigabitEthernet1/0/6
        p2 = re.compile(r'IIF-Name\s*=\s*(?P<iif_name>\S+)')

        # Auth Behavior Value  = 3
        p3 = re.compile(r'Auth Behavior Value\s*=\s*(?P<value>\d+)')

        # Auth Behavior Desc   = AL_BH_DROP_ALL_LRN_DATA
        p4 = re.compile(r'Auth Behavior Desc\s*=\s*(?P<description>\S+)')

        # Secure Feature Flags = 0x1
        p5 = re.compile(r'Secure Feature Flags\s*=\s*(?P<flags>\S+)')

        # Secure Feature Desc  = dot1x
        p6 = re.compile(r'Secure Feature Desc\s*=\s*(?P<description>\S+)')

        # PSec Inactivity Time = 0
        p7 = re.compile(r'PSec Inactivity Time\s*=\s*(?P<time>\d+)')

        # Security Feature Flags: dot1x (Asic: 0; Accsec Logical ID: 0)
        p8 = re.compile(r'Security Feature Flags:\s*(?P<description>\S+)\s*\(Asic:\s*(?P<asic>\d+);\s*Accsec Logical ID:\s*(?P<accsec_logical_id>\d+)\)')

        # @la_accsec_auth_acl_bh:LA_ACCSEC_AUTH_ACL_BH_DROP_ALL_LRN_DATA
        p9 = re.compile(r'@la_accsec_auth_acl_bh:(?P<accsec_auth_acl_behavior>\S+)')

        # @l2_port_accsec_ftr:L2_PORT_ACCSEC_FTR_ENABLE
        p10 = re.compile(r'@l2_port_accsec_ftr:(?P<l2_port_accsec_feature>\S+)')

        # @la_accsec_table_ftr_type:LA_ACCSEC_TBL_FTR_TYPE_DEFAULT_CLIENT
        p11 = re.compile(r'@la_accsec_table_ftr_type:(?P<accsec_table_feature_type>\S+)')

        # @la_accsec_table_mask_type:LA_ACCSEC_TBL_MASK_TYPE_PORT_ONLY
        p12 = re.compile(r'@la_accsec_table_mask_type:(?P<accsec_table_mask_type>\S+)')

        # Loop through each line of the output
        for line in output.splitlines():
            line = line.strip()

            # IIF-ID   = 000000000000040d 
            m = p1.match(line)
            if m:
                ret_dict['iif_id'] = m.group('iif_id')
                continue

            # IIF-Name = GigabitEthernet1/0/6 
            m = p2.match(line)
            if m:
                ret_dict['iif_name'] = m.group('iif_name')
                continue

            # Auth Behavior Value  = 3
            m = p3.match(line)
            if m:
                ret_dict.setdefault('auth_behavior', {})['value'] = int(m.group('value'))
                continue

            # Auth Behavior Desc   = AL_BH_DROP_ALL_LRN_DATA
            m = p4.match(line)
            if m:
                ret_dict['auth_behavior']['description'] = m.group('description')
                continue

            # Secure Feature Flags = 0x1
            m = p5.match(line)
            if m:
                ret_dict.setdefault('secure_feature', {})['flags'] = m.group('flags')
                continue

            # Secure Feature Desc  = dot1x
            m = p6.match(line)
            if m:
                ret_dict['secure_feature']['description'] = m.group('description')
                continue

            # PSec Inactivity Time = 0
            m = p7.match(line)
            if m:
                ret_dict['psec_inactivity_time'] = int(m.group('time'))
                continue

            # Security Feature Flags: dot1x (Asic: 0; Accsec Logical ID: 0)
            m = p8.match(line)
            if m:
                l2_port_platform = ret_dict.setdefault('l2_port_platform_information', {})
                l2_port_platform.setdefault('security_feature_flags', {})['description'] = m.group('description')
                l2_port_platform['security_feature_flags']['asic'] = int(m.group('asic'))
                l2_port_platform['security_feature_flags']['accsec_logical_id'] = int(m.group('accsec_logical_id'))
                continue

            # @la_accsec_auth_acl_bh:LA_ACCSEC_AUTH_ACL_BH_DROP_ALL_LRN_DATA
            m = p9.match(line)
            if m:
                ret_dict['l2_port_platform_information']['accsec_auth_acl_behavior'] = m.group('accsec_auth_acl_behavior')
                continue

            # @l2_port_accsec_ftr:L2_PORT_ACCSEC_FTR_ENABLE
            m = p10.match(line)
            if m:
                ret_dict['l2_port_platform_information']['l2_port_accsec_feature'] = m.group('l2_port_accsec_feature')
                continue

            # @la_accsec_table_ftr_type:LA_ACCSEC_TBL_FTR_TYPE_DEFAULT_CLIENT
            m = p11.match(line)
            if m:
                ret_dict['l2_port_platform_information']['accsec_table_feature_type'] = m.group('accsec_table_feature_type')
                continue

            # @la_accsec_table_mask_type:LA_ACCSEC_TBL_MASK_TYPE_PORT_ONLY
            m = p12.match(line)
            if m:
                ret_dict['l2_port_platform_information']['accsec_table_mask_type'] = m.group('accsec_table_mask_type')
                continue

        return ret_dict
    
class ShowPlatformSoftwareFedSwitchActiveAclInfoDbFeatureCgAclSummarySchema(MetaParser):
    """Schema for show platform software fed switch active acl info db feature cgacl summary"""

    schema = {
        'cg_id': {
          Any(): { 
                'acl_name': str,
                'feature': str,
                'no_of_aces': int,
                'protocol': str,
                'ingress': str,
                'egress': str,
            }
        }
    }
    

class ShowPlatformSoftwareFedSwitchActiveAclInfoDbFeatureCgAclSummary(ShowPlatformSoftwareFedSwitchActiveAclInfoDbFeatureCgAclSummarySchema):
    """Parser for show platform software fed switch active acl info db feature cgacl summary"""

    cli_command = 'show platform software fed switch {switch_mode} acl info db feature cgacl summary'

    def cli(self, switch_mode , output=None):
        if output is None:
            cmd = self.cli_command.format(switch_mode=switch_mode)
            output = self.device.execute(cmd) 
                   
        # 1040      implicit_deny:xACSACLx-IP-S1_PermitGW_DenyOther_V4-669eaa40:  Cgacl         8                 IPv4           Y              N
        p1 = re.compile(r"^\s*(?P<cg_id>\d+)\s+(?P<acl_name>[\w!:\-x]+)\s+(?P<feature>\S+)\s+(?P<no_of_aces>\d+)\s+(?P<protocol>\S+)\s+(?P<ingress>\S+)\s+(?P<egress>\S+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            
            # 1040      implicit_deny:xACSACLx-IP-S1_PermitGW_DenyOther_V4-669eaa40:  Cgacl         8                 IPv4           Y              N
            m = p1.match(line)
            if m:
                group = m.groupdict()
                index = int(group['cg_id'])
                ret_dict.setdefault('cg_id', {})
                ret_dict['cg_id'][index] = {
                    'acl_name': group['acl_name'],
                    'feature': group['feature'],
                    'no_of_aces': int(group['no_of_aces']),
                    'protocol': group['protocol'],
                    'ingress': group['ingress'],
                    'egress': group['egress'],
                }
            continue
        return ret_dict

class ShowPlatSoftFedSwAcAccessSecurityDcTableSummarySchema(MetaParser):
    """Schema for
    show plat soft fed sw ac access-security dc-table summary
    """

    schema = {
        'dc_table_summary': {
            Any(): {
                'interface': str,
                'logical_id': int,
                'position': int,
                'asic': int,
                'auth_act': str,
                'restore_auth_act': str,
                'flag': str,
                'policy_oid': int,
                'packets': int
            }
        }
    }

class ShowPlatSoftFedSwAcAccessSecurityDcTableSummary(ShowPlatSoftFedSwAcAccessSecurityDcTableSummarySchema):
    """Parser for
    show plat soft fed sw ac access-security dc-table summary
    show plat soft fed sw ac access-security dc-table interface if-id {port_if_id}
    """

    cli_command = [
        "show platform software fed {switch} {mode} access-security dc-table summary",
        "show platform software fed {switch} {mode} access-security dc-table interface if-id {port_if_id}"
    ]

    def cli(self, switch='', mode='', port_if_id='', output=None):
        if output is None:
            if port_if_id:
                cmd = self.cli_command[1].format(switch=switch, mode=mode, port_if_id=port_if_id)
            else:
                cmd = self.cli_command[0].format(switch=switch, mode=mode)

            output = self.device.execute(cmd)

        # Interface    Logical-ID Position   Asic# Auth-Act           Restore-Auth-Act   Flag         Policy-OID Packets    
        # --- ------------ ---------- ---------- ----- ------------------ ------------------ ------------ ---------- ---------- 
        # 1 Gi2/0/10     0          24576      0     DROP_ALL_LRN_DATA  None               NONE         573        152725830 
        p1 = re.compile(r'(?P<index>\d+)\s+(?P<interface>\S+)\s+(?P<logical_id>\d+)\s+(?P<position>\d+)\s+(?P<asic>\d+)\s+(?P<auth_act>\S+)\s+(?P<restore_auth_act>\S+)\s+(?P<flag>\S+)\s+(?P<policy_oid>\d+)\s+(?P<packets>\d+)$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                group = m.groupdict()
                index = int(group['index'])
    
                # Interface    Logical-ID Position   Asic# Auth-Act           Restore-Auth-Act   Flag         Policy-OID Packets    
                # --- ------------ ---------- ---------- ----- ------------------ ------------------ ------------ ---------- ---------- 
                # 1 Gi2/0/10     0          24576      0     DROP_ALL_LRN_DATA  None               NONE         573        152725830 
    
                ret_dict.setdefault('dc_table_summary', {})[index] = {
                    'interface': group['interface'],
                    'logical_id': int(group['logical_id']),
                    'position': int(group['position']),
                    'asic': int(group['asic']),
                    'auth_act': group['auth_act'],
                    'restore_auth_act': group['restore_auth_act'],
                    'flag': group['flag'],
                    'policy_oid': int(group['policy_oid']),
                    'packets': int(group['packets']),
                }
                continue

        return ret_dict
    
class ShowPlatformSoftwareFedSwitchActiveIpIgmpSnoopingGroupsVlanSchema(MetaParser):
    """Schema for 
    Show platform software fed {switch} {module} ip igmp snooping groups vlan {vlan_id} {group} detail
    Show platform software fed {switch} {module}  ipv6 mld snooping group vlan  {vlan_id} {group} detail"""

    schema = {
        "vlan": int,
        "ip_address": str,
        "member_ports_count": int,
        Optional("member_ports"): str,
        "dependant_users_count": int,
        "group_urid": str,
        "fset_urid_hash": str,
        "fset_aux_urid": str,
        "layer_3_stub_entry": str,
        "ec_seed": int,
        "gid": int,
        "mcid_asic": int,
        "hw_info_asic": {
            "hw_group_entry_asic": str
        }
    }

class ShowPlatformSoftwareFedSwitchActiveIpIgmpSnoopingGroupsVlan(ShowPlatformSoftwareFedSwitchActiveIpIgmpSnoopingGroupsVlanSchema):
    """Parser for 
    Show platform software fed {switch} {module} ip igmp snooping groups vlan {vlan_id} {group} detail
    Show platform software fed {switch} {module}  ipv6 mld snooping group vlan  {vlan_id} {group} detail"""


    cli_command = 'show platform software fed switch {switch_type} {ip_type} {snooping_type} snooping groups vlan {vlan_id} {group} detail'

    def cli(self, switch_type, vlan_id='', group='', snooping_type='', ip_type='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch_type=switch_type, ip_type=ip_type, snooping_type=snooping_type, vlan_id=vlan_id, group=group))

        ret_dict = {}

        # (Vlan: 3300, 225.1.1.1)
        p1 = re.compile(r'^\(Vlan: (?P<vlan>\d+), (?P<ip_address>\S+)\)$')

        # Member ports            : 1
        p2 = re.compile(r'^Member ports\s+:\s+(?P<member_ports_count>\d+)$')

        # GigabitEthernet3/0/18
        p3 = re.compile(r'(?P<intf>(?:\S+?gigabit\S*|[A-Za-z]+[0-9\/]+))$')

        # Dependent Users Count   : 0
        p4 = re.compile(r'^Dependent Users Count\s+:\s+(?P<dependant_users_count>\d+)$')

        # Group Urid              : 0x6000000000004c92
        p5 = re.compile(r'^Group Urid\s+:\s+(?P<group_urid>\S+)$')

        # Fset Urid ( Hash )      : 0x20000000000009b3 ( 99661bff )
        p6 = re.compile(r'^Fset Urid \( Hash \)\s+:\s+(?P<fset_urid_hash>[\S\s]+)$')

        # Fset Aux Urid           : 0x0
        p7 = re.compile(r'^Fset Aux Urid\s+:\s+(?P<fset_aux_urid>\S+)$')

        # Layer 3 Stub Entry      : No
        p8 = re.compile(r'^Layer 3 Stub Entry\s+:\s+(?P<layer_3_stub_entry>\S+)$')

        # Ec seed                 : 4
        p9 = re.compile(r'^Ec seed\s+:\s+(?P<ec_seed>\d+)$')

        # Gid                     : 10618
        p10 = re.compile(r'^Gid\s+:\s+(?P<gid>\d+)$')

        # Mcid Asic[0]            : 9172
        p11 = re.compile(r'^Mcid Asic\[(?P<asic>\d+)\]\s+:\s+(?P<mcid>\d+)$')

        # Hw Mcid Oid         : 9172 (cookie: urid:0x20::9b3)
        p12 = re.compile(r'Hw Mcid Oid\s+:\s+(?P<hw_vlan_mcid_oid>[\S\s]+.)$')

        for line in output.splitlines():
            line = line.strip()

            # (Vlan: 3300, 225.1.1.1)
            match = p1.match(line)
            if match:
                ret_dict['vlan'] = int(match.group('vlan'))
                ret_dict['ip_address'] = match.group('ip_address')
                continue

            # Member ports            : 1
            match = p2.match(line)
            if match:
                ret_dict['member_ports_count'] = int(match.group('member_ports_count'))
                continue

            # GigabitEthernet3/0/18
            match = p3.match(line)
            if match:
                ret_dict['member_ports'] = match.group('intf')
                continue

            # Dependent Users Count   : 0
            match = p4.match(line)
            if match:
                ret_dict['dependant_users_count'] = int(match.group('dependant_users_count'))
                continue

            # Group Urid              : 0x6000000000004c92
            match = p5.match(line)
            if match:
                ret_dict['group_urid'] = match.group('group_urid')
                continue

            # Fset Urid ( Hash )      : 0x20000000000009b3 ( 99661bff )
            match = p6.match(line)
            if match:
                ret_dict['fset_urid_hash'] = match.group('fset_urid_hash')
                continue

            # Fset Aux Urid           : 0x0
            match = p7.match(line)
            if match:
                ret_dict['fset_aux_urid'] = match.group('fset_aux_urid')
                continue

            # Layer 3 Stub Entry      : No
            match = p8.match(line)
            if match:
                ret_dict['layer_3_stub_entry'] = match.group('layer_3_stub_entry')
                continue

            # Ec seed                 : 4
            match = p9.match(line)
            if match:
                ret_dict['ec_seed'] = int(match.group('ec_seed'))
                continue

            # Gid                     : 10618
            match = p10.match(line)
            if match:
                ret_dict['gid'] = int(match.group('gid'))
                continue

            # Mcid Asic[0]            : 9172
            match = p11.match(line)
            if match:
                ret_dict['mcid_asic'] = int(match.group('mcid'))
                continue

            # Hw Mcid Oid         : 9172 (cookie: urid:0x20::9b3)
            match = p12.match(line)
            if match:
                ret_dict['hw_info_asic'] = {'hw_group_entry_asic': match.group('hw_vlan_mcid_oid')}
                continue

        return ret_dict
        
class ShowPlatformSoftwareFedSwitchActiveIpmfibVrfGroupDetailSchema(MetaParser):
    """Schema for 
    show platform software fed switch {active} ip mfib vrf {vrf_name} {group} detail
    Show platform software fed switch {active} ip mfib vrf {vrf_name} {group}
    Show platform software fed switch {active} ipv6 mfib vrf {vrf_name} {group} detail
    """
    schema ={
        'ip_range': {
            Any(): {
                'mvrf': int,
                'hw_flag': str,
                'mlist_hndl_id': str,
                'mlist_urid': str,
                'fset_urid': str,
                Optional('fset_urid_hash'): str,
                Optional('fset_aux_urid'): str,
                'rpf_adjacency_id': str,
                'cpu_credit': int,
                Optional('total_packets'): {
                    'count': int,
                    'pps': str
                },
                Optional('npi_mroute_ent'): str,
                Optional('svi_fwd_ifs'): int,
                'oif_details': {
                    Any(): {  # The interface names are dynamic
                        'adjid': str,
                        'interface': str,
                        'parent_if': str,
                        'hw_flag': str,
                        'flags': str,
                        Optional('intf_type'): str,
                        Optional('msg_type'): str
                    }
                },
                'gid': int,
                'mcid_oid_asics': {
                    'asic_id': int,
                    'mcid_oid': int
                },
                Optional('hardware_info'): {
                    Optional('asic_id'): int,
                    Optional('ip_mcid_oid'): int,
                    Optional('ip_mcid_oid_cookie'): str,
                    Optional('rpf_port_oid'): int,
                    Optional('punt_on_rpf_fail'): int,
                    Optional('punt_and_forward'): int,
                    Optional('use_rpfid'): int,
                    Optional('rpfid'): int,
                    Optional('enable_rpf_check'): int
                }
            }   
        }
    }

class ShowPlatformSoftwareFedSwitchActiveIpmfibVrfGroupDetail(ShowPlatformSoftwareFedSwitchActiveIpmfibVrfGroupDetailSchema):
  
    """Parser for show platform software fed switch {active} ip mfib vrf {vrf_name} {group} detail,
       show platform software fed switch {active} ip mfib vrf {vrf_name} {group},
       and show platform software fed switch {active} ipv6 mfib vrf {vrf_name} {group} detail"""

    # Merged IPv6 and detail handling into one command list using ip_type placeholder
    cli_command = [
        "show platform software fed switch {switch_type} {ip_type} mfib vrf {vrf_name} {group}",
        "show platform software fed switch {switch_type} {ip_type} mfib vrf {vrf_name} {group} detail",
    ]

    def cli(self, switch_type, vrf_name, group, ip_type, output=None):
        
        if output is None:
            # Determine which command to run based on ip_type (IPv6 vs IPv4) and detail flag
            if ip_type == 'ipv6':
                cmd_index = 1  # Use detailed command for IPv6
            else:
                cmd_index = 0  # Use regular command for IPv4
            
            # Generate the command based on the chosen index
            cmd = self.cli_command[cmd_index].format(
                switch_type=switch_type,
                vrf_name=vrf_name,
                group=group,
                ip_type=ip_type
            )

            # Execute the command on the device
            output = self.device.execute(cmd)

        parsed_dict = {}

        # Mvrf: 2  ( *, 227.0.1.95 ) Attrs: C 
        p1 = re.compile(r'Mvrf: (?P<mvrf_id>\d+)  \((?P<ip_range>[\S\s]+?)\) +Attrs:( C)?$')

        # Hw Flag                 : InHw 
        p2 = re.compile(r'^Hw Flag\s+:\s+(?P<hw_flag>\S+)$')

        # Mlist_hndl (Id)         : 0x1188151eb90 ( 0x57a ) 
        p3 = re.compile(r'^Mlist_hndl \(Id\)\s*:\s*(?P<mlist_hndl_id>[\S\s]+)$')


        # Mlist Urid              : 0x1000000000000546 
        p4 = re.compile(r'^Mlist Urid\s+:\s+(?P<mlist_urid>\S+)$')

        # Fset Urid (Hash)        : 0x3000000000000509 ( 1836cd06 )
        p5 = re.compile(r'^Fset Urid \(Hash\)\s*:\s*(?P<fset_urid>[\S\s]+)$')

        # Fset Aux Urid           : 0x0 
        p6 = re.compile(r'^Fset Aux Urid\s+:\s+(?P<fset_aux_urid>\S+)$')

        # RPF Adjacency ID        : 0xf80055d1 
        p7 = re.compile(r'^RPF Adjacency ID\s+:\s+(?P<rpf_adjacency_id>\S+)$')

        # CPU Credit              : 0 
        p8 = re.compile(r'^CPU Credit\s+:\s+(?P<cpu_credit>\d+)$')

        # Total Packets           : 0 ( 0 pps approx.) 
        p9 = re.compile(r'Total Packets\s+:\s+(?P<total_packets_count>\d+) \((?P<total_packets_pps>\s+\d+ pps approx.)\)')

        # npi_mroute_ent          : 0x11881a6a230 
        p10 = re.compile(r'^npi_mroute_ent\s+:\s+(?P<npi_mroute_ent>\S+)$')

        # svi_fwd_ifs             : 1 
        p11 = re.compile(r'^svi_fwd_ifs\s+:\s+(?P<svi_fwd_ifs>\d+)$')

        # OIF Details: 
        p12 = re.compile(r'^OIF Details:$')

        # AdjID          Interface          ParentIf        HwFlag      Flags      IntfType       MsgType 
        p13 = re.compile(r'^AdjID\s+Interface\s+ParentIf\s+HwFlag\s+Flags\s+(?:\s+IntfType\s+MsgType)?$')

        # 0xf80055d1     Vl103              --------         ---        A          SVI_IF         NORMAL  
        p14 = re.compile(r'^(?P<adjid>\S+)\s+(?P<interface>\S+)\s+(?P<parent_if>\S+)\s+(?P<hw_flag>\S+)\s+(?P<flags>\S+)\s*(?:\s+(?P<intf_type>\S+))?\s*(?:\s+(?P<msg_type>\S+))?$')
 
        # GID                   : 9487 
        p15 = re.compile(r'^GID\s+:\s+(?P<gid>\d+)$')

        # MCID OID Asic[0]      : 5270 
        p16 = re.compile(r'^MCID OID Asic\[(?P<asic_id>\d+)\]\s+:\s+(?P<mcid_oid>\d+)$')

        # Hardware Info ASIC[0] :
        p17 = re.compile(r'^Hardware Info ASIC\[(?P<asic_id>\d+)\] :$')

        #  IP MCID OID         :5270 (cookie: urid:0x30::509) 
        p18 = re.compile(r'IP MCID OID\s+:(?P<ip_mcid_oid>\d+) \(cookie: urid:(?P<cookie>[\S\s]+?)\)')

        # RPF PORT OID        :3286 
        p19 = re.compile(r'RPF PORT OID\s+:(?P<rpf_port_oid>\d+)')

        # punt_on_rpf_fail    :1 
        p20 = re.compile(r'^punt_on_rpf_fail\s+:(?P<punt_on_rpf_fail>\d+)')

        # punt_and_forward    :0 
        p21 = re.compile(r'^punt_and_forward\s+:(?P<punt_and_forward>\d+)')

        # use_rpfid           :0 
        p22 = re.compile(r'^use_rpfid\s+:(?P<use_rpfid>\d+)')

        # rpfid               :0 
        p23 = re.compile(r'^rpfid\s+:(?P<rpfid>\d+)')

        # enable_rpf_check    :1 
        p24 = re.compile(r'^enable_rpf_check\s+:(?P<enable_rpf_check>\d+)')

        for line in output.splitlines():
            line = line.strip()

            # # Mvrf: 2  ( *, 227.0.1.95 ) Attrs: C 
            match = p1.match(line)
            if match:
                mvrf_id = match.group('mvrf_id')
                ip_range = match.group('ip_range')
                parsed_dict.setdefault('ip_range', {}).setdefault(ip_range,{})
                parsed_dict.setdefault('ip_range', {})[ip_range]['mvrf'] = int(mvrf_id)
            
                continue

            # Hw Flag                 : InHw 
            match = p2.match(line)
            if match :
                parsed_dict.setdefault('ip_range', {}).setdefault(ip_range,{})
                parsed_dict['ip_range'][ip_range]['hw_flag'] = match.group('hw_flag')
                continue

            # Mlist_hndl (Id)         : 0x1188151eb90 ( 0x57a ) 
            match = p3.match(line)
            if match :
                parsed_dict.setdefault('ip_range', {}).setdefault(ip_range,{})
                parsed_dict['ip_range'][ip_range]['mlist_hndl_id'] = match.group('mlist_hndl_id')
                continue

            # Mlist Urid              : 0x1000000000000546 
            match = p4.match(line)
            if match :
                parsed_dict.setdefault('ip_range', {}).setdefault(ip_range,{})
                parsed_dict['ip_range'][ip_range]['mlist_urid'] = match.group('mlist_urid')
                continue

            # Fset Urid (Hash)        : 0x3000000000000509 ( 1836cd06 )
            match = p5.match(line)
            if match :
                parsed_dict.setdefault('ip_range', {}).setdefault(ip_range,{})
                parsed_dict['ip_range'][ip_range]['fset_urid'] = match.group('fset_urid')
                continue

            # Fset Aux Urid           : 0x0 
            match = p6.match(line)
            if match and ip_range:
                parsed_dict['ip_range'][ip_range]['fset_aux_urid'] = match.group('fset_aux_urid')
                continue

            # RPF Adjacency ID        : 0xf80055d1 
            match = p7.match(line)
            if match :
                parsed_dict.setdefault('ip_range', {}).setdefault(ip_range,{})
                parsed_dict['ip_range'][ip_range]['rpf_adjacency_id'] = match.group('rpf_adjacency_id')
                continue

            # CPU Credit              : 0 
            match = p8.match(line)
            if match :
                parsed_dict.setdefault('ip_range', {}).setdefault(ip_range,{})
                parsed_dict['ip_range'][ip_range]['cpu_credit'] = int(match.group('cpu_credit'))
                continue

            # Total Packets           : 0 ( 0 pps approx.) 
            match = p9.match(line)
            if match :
                parsed_dict['ip_range'][ip_range].setdefault('total_packets',{})
                parsed_dict['ip_range'][ip_range]['total_packets']['count'] = int(match.group('total_packets_count'))
                parsed_dict['ip_range'][ip_range]['total_packets']['pps'] = match.group('total_packets_pps')
                continue

            # npi_mroute_ent          : 0x11881a6a230 
            match = p10.match(line)
            if match :
                parsed_dict['ip_range'][ip_range]['npi_mroute_ent'] = match.group('npi_mroute_ent')
                continue

            # svi_fwd_ifs             : 1 
            match = p11.match(line)
            if match :
                parsed_dict['ip_range'][ip_range]['svi_fwd_ifs'] = int(match.group('svi_fwd_ifs'))
                continue

            # OIF Details: 
            match = p12.match(line)
            if match :
                continue

            # AdjID          Interface          ParentIf        HwFlag      Flags      IntfType       MsgType 
            match = p13.match(line)
            if match :
                continue

            # 0xf80055d1     Vl103              --------         ---        A          SVI_IF         NORMAL  
            match = p14.match(line)
            if match:
                
                adjid = match.group('adjid')
                interface = match.group('interface')
                
                # Skip header row and any other irrelevant rows
                if interface != 'Interface' and adjid != 'MCID' and adjid != 'IP':
                    parsed_dict['ip_range'][ip_range].setdefault('oif_details',{})
                    parsed_dict['ip_range'][ip_range]['oif_details'][interface] = {
                        'adjid':match.group('adjid'),
                        'interface': match.group('interface'),
                        'parent_if': match.group('parent_if'),
                        'hw_flag': match.group('hw_flag'),
                        'flags': match.group('flags'),
                        'intf_type': match.group('intf_type'),
                        'msg_type': match.group('msg_type')
                    }
                    continue

            # GID                   : 9487 
            match = p15.match(line)
            if match :
                parsed_dict['ip_range'][ip_range]['gid'] = int(match.group('gid'))
                continue

            # MCID OID Asic[0]      : 5270 
            match = p16.match(line)
            if match :
                asic_id = int(match.group('asic_id'))
                mcid_oid = int(match.group('mcid_oid'))
                parsed_dict['ip_range'][ip_range].setdefault('mcid_oid_asics', {})['asic_id'] = asic_id
                parsed_dict['ip_range'][ip_range].setdefault('mcid_oid_asics', {})['mcid_oid'] = mcid_oid
                continue

            # Hardware Info ASIC[0] :
            match = p17.match(line)
            if match :
                asic_id = int(match.group('asic_id'))
                parsed_dict['ip_range'][ip_range].setdefault('hardware_info', {})['asic_id'] = asic_id
                continue

            #  IP MCID OID         :5270 (cookie: urid:0x30::509) 
            match = p18.match(line)
            if match :
                parsed_dict['ip_range'][ip_range]['hardware_info']['ip_mcid_oid'] = int(match.group('ip_mcid_oid'))
                parsed_dict['ip_range'][ip_range]['hardware_info']["ip_mcid_oid_cookie"]=match.group('cookie')
                continue

            # RPF PORT OID        :3286 
            match = p19.match(line)
            if match :
                parsed_dict['ip_range'][ip_range]['hardware_info']['rpf_port_oid'] = int(match.group('rpf_port_oid'))
                continue

            # punt_on_rpf_fail    :1 
            match = p20.match(line)
            if match :
                parsed_dict['ip_range'][ip_range]['hardware_info']['punt_on_rpf_fail'] = int(match.group('punt_on_rpf_fail'))
                continue

            # punt_and_forward    :0 
            match = p21.match(line)
            if match :
                parsed_dict['ip_range'][ip_range]['hardware_info']['punt_and_forward'] = int(match.group('punt_and_forward'))
                continue

            # use_rpfid           :0 
            match = p22.match(line)
            if match :
                parsed_dict['ip_range'][ip_range]['hardware_info']['use_rpfid'] = int(match.group('use_rpfid'))
                continue

            # rpfid               :0 
            match = p23.match(line)
            if match :
                parsed_dict['ip_range'][ip_range]['hardware_info']['rpfid'] = int(match.group('rpfid'))
                continue

            # enable_rpf_check    :1 
            match = p24.match(line)
            if match :
                parsed_dict['ip_range'][ip_range]['hardware_info']['enable_rpf_check'] = int(match.group('enable_rpf_check'))
                continue

        return parsed_dict

class ShowPlatformSoftwareFedSwitchAclParallelKeyProfileEgressSchema(MetaParser):
    """Schema for:
       * show platform software fed {switch} {state} acl man parallel-key-profile egress all
    """
    schema = {
        'egress': {
            Any(): {  # Profile name
                "index": int,
                Optional("protocols"): {
                    Any(): {  # ETH, IPV4, IPV6
                        "oid": ListOf(int),
                        "ref_cnt": ListOf(int),
                        "e_values": {
                            Any(): ListOf(int),  # E0, E1, E2, E3
                        },
                        "no_of_key_prof": int,
                        "wide": bool,
                        "rtf": bool,
                        "stage": str,
                    }
                }
            }
        }
    }


class ShowPlatformSoftwareFedSwitchAclParallelKeyProfileEgress(ShowPlatformSoftwareFedSwitchAclParallelKeyProfileEgressSchema):
    """Parser for:
       * show platform software fed {switch} {state} acl man parallel-key-profile egress all
    """

    cli_command = "show platform software fed {switch} {state} acl man parallel-key-profile egress all"

    def cli(self, switch, state, output=None):
        if output is None:
            cmd = self.cli_command.format(switch=switch, state=state)
            output = self.device.execute(cmd)

        # Initialize variables
        ret_dict = {}
        current_profile = None
        current_protocol = None

        # [Egress Paralley Key Profile: RT, Idx: 1]
        p1 = re.compile(r"^\[Egress Paralley Key Profile: (?P<profile_name>[\w\-]+), Idx: (?P<index>\d+)\]$")
        
        # IPV4
        p2 = re.compile(r"^(?P<protocol>\w+)$")

        # OID:     [  571   493   493   493 ]
        p3 = re.compile(r"^OID:\s+\[\s+(?P<oid>[\d\s]+)\]$")

        # Ref cnt: [    1     1     0     0 ]
        p4 = re.compile(r"^Ref cnt:\s+\[\s+(?P<ref_cnt>[\d\s]+)\]$")

        # E0:   528,   531,   534,     0,     0,     0,     0,     0,     0,     0,     0,     0
        p5 = re.compile(r"^(?P<e_value>E\d):\s+(?P<values>[\d,\s]+)$")

        # No of Key Prof: 3    Wide: False    RTF: True    Stage: TRANS
        p6 = re.compile(
            r"^No of Key Prof:\s+(?P<no_of_key_prof>\d+)\s+Wide:\s+(?P<wide>\w+)\s+RTF:\s+(?P<rtf>\w+)\s+Stage:\s+(?P<stage>\w+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # [Egress Paralley Key Profile: RT, Idx: 1]
            m = p1.match(line)
            if m:
                profile_name = m.group("profile_name")
                index = int(m.group("index"))
                current_profile = profile_name
                profile_dict = ret_dict.setdefault("egress", {}).setdefault(current_profile, {"index": index})
                continue

            # IPV4
            m = p2.match(line)
            if m:
                current_protocol = m.group("protocol")
                protocol_dict = profile_dict.setdefault("protocols", {})
                protocol_dict[current_protocol] = {"e_values": {}}
                continue

            # OID:     [  571   493   493   493 ]
            m = p3.match(line)
            if m and current_protocol:
                oid = list(map(int, m.group("oid").split()))
                protocol_dict[current_protocol]["oid"] = oid
                continue

            # Ref cnt: [    1     1     0     0 ]
            m = p4.match(line)
            if m and current_protocol:
                ref_cnt = list(map(int, m.group("ref_cnt").split()))
                protocol_dict[current_protocol]["ref_cnt"] = ref_cnt
                continue

            # E0:   528,   531,   534,     0,     0,     0,     0,     0,     0,     0,     0,     0
            m = p5.match(line)
            if m and current_protocol:
                e_value = m.group("e_value")
                values = list(map(int, m.group("values").replace(",", "").split()))
                protocol_dict[current_protocol]["e_values"][e_value] = values
                continue

            # No of Key Prof: 3    Wide: False    RTF: True    Stage: TRANS
            m = p6.match(line)
            if m and current_protocol:
                protocol_dict[current_protocol].update(
                    {
                        "no_of_key_prof": int(m.group("no_of_key_prof")),
                        "wide": m.group("wide").lower() == "true",
                        "rtf": m.group("rtf").lower() == "true",
                        "stage": m.group("stage"),
                    }
                )
                continue

        return ret_dict

class ShowPlatformSoftwareFedSwitchActiveAclSgaclCellSgtDgtSchema(MetaParser):
    """Schema for show platform software fed switch {switch_type} acl sgacl cell {sgt} {dgt}"""

    schema = {
        'monitor_mode': str,
        'acl_cg_id': int,
        'protocol': str,
        'asic_num': {
            Any(): {
                'cell_oid':int,
            },
        },
        'asic_num1': {
            Any(): {
                'counter_oid':int,
            },
        },
    }

class ShowPlatformSoftwareFedSwitchActiveAclSgaclCellSgtDgt(ShowPlatformSoftwareFedSwitchActiveAclSgaclCellSgtDgtSchema):
    """Parser for show platform software fed switch {switch_type} acl sgacl cell {sgt} {dgt}"""

    cli_command = "show platform software fed switch {switch_type} acl sgacl cell {sgt} {dgt}"

    def cli(self, switch_type, sgt  ,dgt, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch_type=switch_type,sgt=sgt,dgt=dgt))

        # Initialize the dictionary
        ret_dict = {}

        # monintor mode: 0
        p1 = re.compile(r"^monintor mode:\s+(?P<monitor_mode>\d+)$")

        #ACL CG_ID:     273
        p2 = re.compile(r"^ACL CG_ID:\s+(?P<acl_cg_id>\d+)$")

        # Protocol:      IPv4
        p3 = re.compile(r"^Protocol:\s+(?P<protocol>\S+)$")

        # Asic Num:      0  Cell OID:      2076 
        p4 = re.compile(r"^Asic Num:\s+(?P<asic_num>\d+)\s+Cell OID:\s+(?P<cell_oid>\d+)$")

        # ASIC Num:      0  Counter OID:   2077 
        p5 = re.compile(r"^ASIC Num:\s+(?P<asic_num1>\d+)\s+Counter OID:\s+(?P<counter_oid>\d+)$")
            
        for line in output.splitlines():
            line = line.strip()

            # monintor mode: 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['monitor_mode']=group['monitor_mode']
                continue

            #ACL CG_ID:     273
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['acl_cg_id']=int(group['acl_cg_id'])
                continue
            
            # Protocol:      IPv4
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict['protocol']=group['protocol']
                continue

            # Asic Num:      0  Cell OID:      2076     
            m = p4.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault('asic_num', {}).setdefault(group['asic_num'],{})
                root_dict['cell_oid']=int(group['cell_oid'])
                continue
            
            # ASIC Num:      0  Counter OID:   2077 
            m = p5.match(line)
            if m:
                group = m.groupdict()
                root_dict_1 = ret_dict.setdefault('asic_num1', {}).setdefault(group['asic_num1'],{})
                root_dict_1['counter_oid']=int(group['counter_oid'])
                continue
        return ret_dict

class ShowPlatformSoftwareFedSwitchActiveSgaclVlanSchema(MetaParser):
    """Schema for show platform software fed switch {switch_type} sgacl vlan"""

    schema = {
        'vlan_id':{
            Any(): {
                'hw_state': str
            }
        }
       
    }

class ShowPlatformSoftwareFedSwitchActiveSgaclVlan(ShowPlatformSoftwareFedSwitchActiveSgaclVlanSchema):
    """Parser for show platform software fed switch {switch_type} sgacl vlan"""

    cli_command = "show platform software fed switch {switch_type} sgacl vlan"

    def cli(self, switch_type, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch_type=switch_type))

        # Initialize the dictionary
        ret_dict = {}

        # Vlan id        HW state
        # ---------------------------------
        # vlan50         Success

        p1 = re.compile(r"^(?P<vlan_id>\S+)\s+(?P<hw_state>\S+)$")
        
        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault('vlan_id', {}).setdefault(group['vlan_id'],{})
                root_dict['hw_state']=group['hw_state']
                continue
            
        return ret_dict 

class ShowPlatformSoftwareFedSwitchActiveSecurityfedWrclientsifidSchema(MetaParser):
    """Schema for show platform software fed switch {switch_type} security-fed wrclients if_id {port_if_id}""" 

    schema = {
        'interfaces': {
            Any(): {
                'client_ifid': str,
                'mac': str,
                'host_mode': str,
                'auth_behavior': str,
                'ipv4_cgacl_name': str,
                'ipv6_cgacl_name': str,
            }
        }
    }

class ShowPlatformSoftwareFedSwitchActiveSecurityfedWrclientsifid(ShowPlatformSoftwareFedSwitchActiveSecurityfedWrclientsifidSchema):
    """Parser for show platform software fed switch {switch_type} security-fed wrclients if_id {port_if_id}"""

    cli_command = "show platform software fed switch {switch_type} security-fed wrclients if_id {port_if_id}"
    def cli(self, switch_type, port_if_id, output=None):
        if output is None :
            output = self.device.execute(
                self.cli_command.format(switch_type=switch_type, port_if_id=port_if_id)
            )

        ret_dict = {}

        # 0x27fda427   0000.0033.3333   MULTI_AUTH    LA_BH_FWD_ALL_LRN_DATA  implicit_deny_v6!implicit_deny:xACSACLx-IPV6-S1_PermitGW_DenyOther_V6-669eaa28!xACSACLx-IP-S1_PermitGW_DenyOther_V4-669eaa40: implicit_deny_v6!implicit_deny:xACSACLx-IPV6-S1_PermitGW_DenyOther_V6-669eaa28!xACSACLx-IP-S1_PermitGW_DenyOther_V4-669eaa40:
        p1 = re.compile(
            r'^(?P<client_ifid>\w+)\s+(?P<mac>\S+)\s+(?P<host_mode>\S+)\s+(?P<auth_behavior>\S+)\s+'
            r'(?P<ipv4_cgacl_name>[\S\s]+)\s+(?P<ipv6_cgacl_name>[\S\s]+)$'
        )

        for line in output.splitlines():
            line = line.strip()

            # 0x27fda427   0000.0033.3333   MULTI_AUTH    LA_BH_FWD_ALL_LRN_DATA  implicit_deny_v6!implicit_deny:xACSACLx-IPV6-S1_PermitGW_DenyOther_V6-669eaa28!xACSACLx-IP-S1_PermitGW_DenyOther_V4-669eaa40: implicit_deny_v6!implicit_deny:xACSACLx-IPV6-S1_PermitGW_DenyOther_V6-669eaa28!xACSACLx-IP-S1_PermitGW_DenyOther_V4-669eaa40:        
            m = p1.match(line)
            if m:
                group = m.groupdict()
                client_ifid = group['client_ifid']
                ret_dict.setdefault('interfaces', {}).setdefault(client_ifid, {}).update({
                    'client_ifid': group['client_ifid'],
                    'mac': group['mac'],
                    'host_mode': group['host_mode'],
                    'auth_behavior': group['auth_behavior'],
                    'ipv4_cgacl_name': group['ipv4_cgacl_name'].strip(),
                    'ipv6_cgacl_name': group['ipv6_cgacl_name'].strip()
                })
                continue

        return ret_dict

class ShowPlatformSoftwareFedSwitchActiveOifsetUridl2mhashSchema(MetaParser):
    """
    Schema for
        * 'Show platform software fed {switch} {module} oifset l2m hash {hash_data} detail'
    """
    schema = {
    'type': str,
    'state': str,
    'md5': str,
    'fset_urid': str,
    Optional('remote_port_count'): int,
    'parent_urid': str,
    'users_count': int,
    'vp_oif_count': int,
    'fset_gid': int,
    'asic_mcid_oid': int,
    'hw_l2_mcg_info': str,
    Optional('vp_interface_details'): {
        Any(): {
            'vp_interface': str,
            'interface': str,
            'physical_interface': str,
            'flags': str,
            'hw_flags': str,
            'asic': {
                'asic_num': int,
                'l2_ac_oid': int,
            },
        },
    },
    'users': {
            Any(): {  # URID as the key
                'l2m_grp': {
                    'vlan': str,
                    'group_ip': str,
                },
            },
        },
    }

class ShowPlatformSoftwareFedSwitchActiveOifsetUridl2mhash(ShowPlatformSoftwareFedSwitchActiveOifsetUridl2mhashSchema):
    """
    Parser for
        * 'Show platform software fed {switch} {module} oifset l2m hash {hash_data} detail'
    """

    cli_command = 'show platform software fed switch {switch_type} oifset l2m hash {hash_id} detail'
    
    def cli(self, switch_type, hash_id=None, output=None):
        if output is None:
            if hash_id:
                cmd = self.cli_command.format(switch_type=switch_type, hash_id=hash_id)
                output = self.device.execute(cmd)

        vp_index = 0
        parsed_dict ={}
        vp_interfaces = {}
        users = {}

        # Type: oif_vp_handles       State: allocated       MD5:(99661bffcb26f8db:c644c3f264bb9bec)
        p1 = re.compile(r'^Type:\s+(?P<type>\S+)\s+State:\s+(?P<state>\S+)\s+MD5:\((?P<md5>\S+)\)$')

        # Fset Urid              : 0x20000000000009b3
        p2 = re.compile(r'^Fset\s+Urid\s+:\s+(?P<fset_urid>\S+)$')

        # Parent URID            : 0x20000000000009af
        p3 = re.compile(r'^Parent\s+URID\s+:\s+(?P<parent_urid>\S+)$')

        # Remote Port Count      : 2
        p4 = re.compile(r'^Remote\s+Port\s+:\s+(?P<remote_port_count>\d+)$')

        # Users Count            : 1
        p5 = re.compile(r'^Users\s+Count\s+:\s+(?P<users_count>\d+)$')

        # VP OIF Count           : 2
        p6 = re.compile(r'^VP\s+OIF\s+Count\s+:\s+(?P<vp_oif_count>\d+)$')

        # 1. Gi3/0/18Vlan3300         GigabitEthernet3/0/18    GigabitEthernet3/0/18   
        p7 = re.compile(r'^(?P<num>\d+)\. +(?P<vp_interface>\S+) +(?P<interface>\S+) +(?P<physical_interface>\S+)$')

        # flags:[ oif_port mrouter  ]    hw_flags: [ InHw  remote ]
        p8 = re.compile(r'^flags:\[\s+(?P<flags>.*)\s+\]\s+hw_flags:\s+\[\s+(?P<hw_flags>.*)\]$')

        #  (Asic[0]: l2_ac_oid: 0)
        p9 = re.compile(r'^\(Asic\[(?P<asic_num>\d+)\]:\s+l2_ac_oid:\s+(?P<l2_ac_oid>\d+)\)$')

        # FSET Gid               : 10618
        p10 = re.compile(r'^FSET\s+Gid\s+:\s+(?P<fset_gid>\d+)$')

        # Asic[0] mcid_oid       : 9172
        p11 = re.compile(r'^Asic\[0\] +mcid_oid *: *(?P<asic_mcid_oid>\d+)$')

        # Hw L2 Mcg Info Asic[0] :
        p12 = re.compile(r'^Hw +L2 +Mcg +Info +Asic\[0\] *: *(?P<hw_l2_mcg_info>.*)$')

        # urid:0x6000000000004c92 (l2m_grp: vlan:3300, 225.1.1.1)
        p13 = re.compile(r'^urid:(?P<urid>\S+)\s+\(l2m_grp:\s+vlan:(?P<vlan>\S+),\s+(?P<group_ip>\S+)\)$')

        for line in output.splitlines():
            line = line.strip()

            # Type: oif_vp_handles State: allocated MD5:(99661bffcb26f8db:c644c3f264bb9bec)
            m = p1.match(line)
            if m:
                parsed_dict.update(m.groupdict())
                continue

            # Fset Urid              : 0x20000000000009b3
            m = p2.match(line)
            if m:
                parsed_dict['fset_urid'] = m.group('fset_urid')
                continue

            # Parent URID            : 0x20000000000009af
            m = p3.match(line)
            if m:
                parsed_dict['parent_urid'] = m.group('parent_urid')
                continue

            # Remote Port Count      : 2
            m = p4.match(line)
            if m:
                parsed_dict['remote_port_count'] = int(m.group('remote_port_count'))
                continue

            # Users Count            : 1
            m = p5.match(line)
            if m:
                parsed_dict['users_count'] = int(m.group('users_count'))
                continue

            # VP OIF Count           : 2
            m = p6.match(line)
            if m:
                parsed_dict['vp_oif_count'] = int(m.group('vp_oif_count'))
                continue

            # 1. Gi3/0/18Vlan3300 GigabitEthernet3/0/18 GigabitEthernet3/0/18
            m = p7.match(line)
            if m:
                vp_index += 1
                vp_dict = parsed_dict.setdefault('vp_interface_details', {}).setdefault(vp_index, {})
                vp_dict.update({
                    'vp_interface': m.group('vp_interface'),
                    'interface': m.group('interface'),
                    'physical_interface': m.group('physical_interface')
                })
                continue

            # flags:[ oif_port mrouter  ] hw_flags: [ InHw  remote ]
            m = p8.match(line)
            if m:
                vp_dict['flags'] = m.group('flags')
                vp_dict['hw_flags'] = m.group('hw_flags')
                continue

            # (Asic[0]: l2_ac_oid: 0)
            m = p9.match(line)
            if m:
                vp_dict.setdefault('asic', {})['asic_num'] = int(m.group('asic_num'))
                vp_dict.setdefault('asic', {})['l2_ac_oid'] = int(m.group('l2_ac_oid'))
                continue

            # FSET Gid               : 10618
            m = p10.match(line)
            if m:
                parsed_dict['fset_gid'] = int(m.group('fset_gid'))
                continue

            # Asic[0] mcid_oid       : 9172
            m = p11.match(line)
            if m:
                parsed_dict['asic_mcid_oid'] = int(m.group('asic_mcid_oid'))
                continue

            # Hw L2 Mcg Info Asic[0] :
            m = p12.match(line)
            if m:
                parsed_dict['hw_l2_mcg_info'] = m.group('hw_l2_mcg_info')
                continue
            
            # urid:0x6000000000004c92 (l2m_grp: vlan:3300, 225.1.1.1)
            m = p13.match(line)
            if m:
                user_dict = parsed_dict.setdefault('users', {})
                urid = m.group('urid')
                user_dict[urid] = {
                    'l2m_grp': {
                        'vlan': m.group('vlan'),
                        'group_ip': m.group('group_ip')
                    }
                }
                continue
        return parsed_dict 

class ShowPlatformSoftwareFedSwitchActiveSecurityFedDhcpSnoopVlanDetailSchema(MetaParser):
    """Schema for show platform software fed switch active security-fed dhcp-snoop vlan {vlan} detail"""

    schema = {
        "vlan": int,
        Optional("multicast_group_id"): ListOf({
            "oid": int,
            "asic": int
        }),
        Optional("trusted_ports_multicast_gid"): str,
        "punject_switch_profile": str,
        Optional('no_trust_ports'): bool,
        Optional("dhcp_snoop_enable"): str,
        Optional("valid_snooping_di_handle"): str,
        Optional("trusted_ports"): ListOf({
            "interface": str,
            "interface_id": str,
            "po_id": str
        }),
        Optional("asic_specific_section"): ListOf({
            "asic": int,
            "acl_oid": int,
            "entries": ListOf({
                "position": int,
                "protocol": str,
                "src_port": int,
                "dst_port": int,
                "action": str,
                "counter_oid": int
            })
        })
    }

class ShowPlatformSoftwareFedSwitchActiveSecurityFedDhcpSnoopVlanDetail(ShowPlatformSoftwareFedSwitchActiveSecurityFedDhcpSnoopVlanDetailSchema):
    """Parser for show platform software fed switch active security-fed dhcp-snoop vlan {vlan} detail"""

    cli_command = 'show platform software fed switch {active} security-fed dhcp-snoop vlan {vlan} detail'

    def cli(self, active="",vlan="", output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(vlan=vlan,active=active))

        ret_dict = {}

        # Vlan= 20
        p0 = re.compile(r'^Vlan= +(?P<vlan>\d+)$')

        # Multicast Group with OID(4254) on ASIC(0)
        p1 = re.compile(r'^Multicast Group with OID\((?P<oid>\d+)\) on ASIC\((?P<asic>\d+)\)$')

        # Trusted ports multicast group GID:: 0x2038
        p2 = re.compile(r'^Trusted ports multicast group GID:: +(?P<gid>\S+)$')

        # Punject Switch Profile: FALSE
        p3 = re.compile(r'^Punject Switch Profile: +(?P<profile>\w+)$')

        # Port-channel12                                                    0x00000524        0x00000000
        p4 = re.compile(r'^(?P<interface>\S+)\s+(?P<interface_id>\S+)\s+(?P<po_id>\S+)$')

        # Information about ACL with OID(1438) on ASIC(0)
        p5 = re.compile(r'^Information about ACL with OID\((?P<acl_oid>\d+)\) on ASIC\((?P<asic>\d+)\)$')

        # 0        UDP      68       67       PUNT    1439
        p6 = re.compile(r'^(?P<position>\d+)\s+(?P<protocol>\S+)\s+(?P<src_port>\d+)\s+(?P<dst_port>\d+)\s+(?P<action>\S+)\s+(?P<counter_oid>\d+)$')

        # No trust ports for this vlan
        p7 = re.compile(r'^No trust ports for this vlan$')

        # DHCP SNOOP enable: FALSE
        p8 = re.compile(r'^DHCP SNOOP enable: +(?P<dhcp_snoop_enable>\w+)$')

        # Valid Snooping DI handle:none
        p9 = re.compile(r'^Valid Snooping DI handle:(?P<di_handle>\S+)$')

        multicast_group_id = []
        trusted_ports = []
        asic_specific_section = []
        acl_entries = []

        for line in output.splitlines():
            line = line.strip()

            # Vlan= 20
            m = p0.match(line)
            if m:
                ret_dict['vlan'] = int(m.group('vlan'))
                continue

            # Multicast Group with OID(4254) on ASIC(0)
            m = p1.match(line)
            if m:
                multicast_group_id.append({
                    "oid": int(m.group('oid')),
                    "asic": int(m.group('asic'))
                })
                continue

            # Trusted ports multicast group GID:: 0x2038
            m = p2.match(line)
            if m:
                ret_dict['trusted_ports_multicast_gid'] = m.group('gid')
                continue

            # Punject Switch Profile: FALSE
            m = p3.match(line)
            if m:
                ret_dict['punject_switch_profile'] = m.group('profile')
                continue

            # Port-channel12                                                    0x00000524        0x00000000
            m = p4.match(line)
            if m:
                trusted_ports.append({
                    "interface": m.group('interface'),
                    "interface_id": m.group('interface_id'),
                    "po_id": m.group('po_id')
                })
                continue

            # Information about ACL with OID(1438) on ASIC(0)
            m = p5.match(line)
            if m:
                if acl_entries:
                    asic_specific_section.append({
                        "asic": current_asic,
                        "acl_oid": current_acl_oid,
                        "entries": acl_entries
                    })
                    acl_entries = []
                current_acl_oid = int(m.group('acl_oid'))
                current_asic = int(m.group('asic'))
                continue

            # 0        UDP      68       67       PUNT    1439
            m = p6.match(line)
            if m:
                acl_entries.append({
                    "position": int(m.group('position')),
                    "protocol": m.group('protocol'),
                    "src_port": int(m.group('src_port')),
                    "dst_port": int(m.group('dst_port')),
                    "action": m.group('action'),
                    "counter_oid": int(m.group('counter_oid'))
                })
                continue

            # No trust ports for this vlan
            m = p7.match(line)
            if m:
                ret_dict['no_trust_ports'] = True
                continue

            # DHCP SNOOP enable: FALSE
            m = p8.match(line)
            if m:
                group= m.groupdict()
                ret_dict['dhcp_snoop_enable'] = group['dhcp_snoop_enable']
                continue

            # Valid Snooping DI handle:none
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ret_dict['valid_snooping_di_handle'] = group['di_handle']
                continue

        if acl_entries:
            asic_specific_section.append({
                "asic": current_asic,
                "acl_oid": current_acl_oid,
                "entries": acl_entries
            })

        if multicast_group_id:
            ret_dict['multicast_group_id'] = multicast_group_id

        if trusted_ports:
            ret_dict['trusted_ports'] = trusted_ports

        if asic_specific_section:
            ret_dict['asic_specific_section'] = asic_specific_section

        return ret_dict

class ShowPlatformDhcpSnoopingClientStatsSchema(MetaParser):
    """Schema for show platform dhcpsnooping client stats {mac_address}"""

    schema = {
        'client_mac': str,
        'packet_trace': ListOf({
            'timestamp': str,
            'destination_mac': str,
            'destination_ip': str,
            'vlan': int,
            'message': str,
            'handler_action': str
        })
    }

class ShowPlatformDhcpSnoopingClientStats(ShowPlatformDhcpSnoopingClientStatsSchema):
    """Parser for show platform dhcpsnooping client stats {mac_address}"""

    cli_command = 'show platform dhcpsnooping client stats {mac_address}'

    def cli(self, mac_address, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(mac_address=mac_address))

        ret_dict = {}

        # Packet Trace for client MAC 44AE.25D3.6006:
        p0 = re.compile(r'^Packet Trace for client MAC\s+(?P<client_mac>[\da-fA-F.]+):$')

        # Timestamp                Destination MAC  Destination Ip  VLAN  Message      Handler:Action
        # ------------------------ ---------------- --------------- ----  ------------ ----------------
        # 2025/03/19 11:08:53.012  FFFF.FFFF.FFFF   255.255.255.255 100  DHCPDISCOVER(B) PUNT:RECEIVED
        p1 = re.compile(
            r'^(?P<timestamp>\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}\.\d{3})\s+'
            r'(?P<destination_mac>[0-9A-Fa-f\.]+)\s+'
            r'(?P<destination_ip>[0-9\.\:]+)\s+'
            r'(?P<vlan>\d+)\s+'
            r'(?P<message>\S+)\s+'
            r'(?P<handler_action>\S+:\S+)$'
        )

        packet_trace = []
        for line in output.splitlines():
            line = line.strip()

            # Packet Trace for client MAC 44AE.25D3.6006:
            m = p0.match(line)
            if m:
                ret_dict['client_mac'] = m.group('client_mac')

            # Match the packet trace lines
            m = p1.match(line)
            if m:
                ret_dict['packet_trace']=packet_trace
                ret_dict['packet_trace'].append({
                    'timestamp': m.group('timestamp'),
                    'destination_mac': m.group('destination_mac'),
                    'destination_ip': m.group('destination_ip'),
                    'vlan': int(m.group('vlan')),
                    'message': m.group('message'),
                    'handler_action': m.group('handler_action')
                })

        return ret_dict

class ShowPlatformSoftwareFedSwitchActiveEtherchannelLoadBalanceMacAddrSchema(MetaParser):
    """Schema for:
        * 'show platform software fed switch active etherchannel <eth_channel_id> load-balance mac-addr <src> <dst>'
    """
    schema = {
        'dest_port': str
    }

class ShowPlatformSoftwareFedSwitchActiveEtherchannelLoadBalanceMacAddr(ShowPlatformSoftwareFedSwitchActiveEtherchannelLoadBalanceMacAddrSchema):
    """Parser for:
        * 'show platform software fed switch active etherchannel <eth_channel_id> load-balance mac-addr <src> <dst>'
    """

    cli_command = [
        'show platform software fed {switch} {switch_type} etherchannel {eth_channel_id} load-balance mac-addr {src} {dst}',
        'show platform software fed {switch_type} etherchannel {eth_channel_id} load-balance mac-addr {src} {dst}'
    ]

    def cli(self, switch_type, eth_channel_id, src, dst, switch=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(switch=switch, switch_type=switch_type, eth_channel_id=eth_channel_id, src=src, dst=dst)
            else:
                cmd = self.cli_command[1].format(switch_type=switch_type, eth_channel_id=eth_channel_id, src=src, dst=dst)
            output = self.device.execute(cmd)

        # Initialize the parsed dictionary
        ret_dict = {}

        # Matching Pattern
        # Dest Port: : HundredGigE1/3/0/13
        p1 = re.compile(r'^Dest Port: : (?P<dest_port>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # HundredGigE1/3/0/13
            m = p1.match(line)
            if m:
                ret_dict['dest_port'] = m.group('dest_port')
                continue

        return ret_dict

# =============================================
# Schema for 'show platform software fed active sdm feature'
# =============================================

class ShowPlatformSoftwareFedActiveSdmFeatureSchema(MetaParser):
    """ Schema for show platform software fed active sdm feature """
    schema = {
        'entries': {
            Any(): {  
                Any(): {  
                    'reserved': int,
                    'used': int,
                    'percent_used': int,
                    'max': int,
                    'alloc_fail': int,
                    'capped_max': int,
                    'asic': int,
                    'slice': int
                }
            }
        }
    }

class ShowPlatformSoftwareFedActiveSdmFeature(ShowPlatformSoftwareFedActiveSdmFeatureSchema):
    """ Parser for show platform software fed active sdm feature """
    cli_command = 'show platform software fed active sdm feature'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        entry_dict = ret_dict.setdefault('entries', {})
        
        # QOS ACL IN            1024        0           0      0           0           5120        2      1
        # QOS ACL IN            1024        16          1      16          0           5120        3      1
        # QOS ACL OUT           1024        0           0      0           0           5120        0      0
        # QOS ACL OUT           1024        0           0      0           0           5120        1      0
        p0 = re.compile(
            r'^(?P<feature>[A-Za-z0-9\/\-\s]+?)\s{2,}'
            r'(?P<reserved>\d+)\s+'
            r'(?P<used>\d+)\s+'
            r'(?P<percent_used>\d+)\s+'
            r'(?P<max>\d+)\s+'
            r'(?P<alloc_fail>\d+)\s+'
            r'(?P<capped_max>\d+)\s+'
            r'(?P<asic>\d+)\s+'
            r'(?P<slice>\d+)$'
        )

        for line in output.splitlines():
            line = line.strip()
            if not line or line.startswith('Feature Name') or line.startswith('-') or line.startswith('NPI SDM Feature Table'):
                continue

            # QOS ACL IN            1024        0           0      0           0           5120        2      1
            # QOS ACL IN            1024        16          1      16          0           5120        3      1
            # QOS ACL OUT           1024        0           0      0           0           5120        0      0
            # QOS ACL OUT           1024        0           0      0           0           5120        1      0
            m = p0.match(line)
            if m:
                group = m.groupdict()
                feature = group['feature'].strip()
                index = f"{group['asic']}"

                feature_dict = entry_dict.setdefault(feature, {})
                feature_dict[index] = {
                    'reserved': int(group['reserved']),
                    'used': int(group['used']),
                    'percent_used': int(group['percent_used']),
                    'max': int(group['max']),
                    'alloc_fail': int(group['alloc_fail']),
                    'capped_max': int(group['capped_max']),
                    'asic': int(group['asic']),
                    'slice': int(group['slice']),
                }

        return ret_dict
    
class ShowPlatformSoftwareFedSwitchAclBindDbInterfaceFeatureDirDetailAsicSchema(MetaParser):
    """Schema for
       * show platform software fed {switch} {state} acl bind db interface {interface} feature {feature} dir {dir} detail asic {asic}
    """
    schema = {
        'interface_name': str,
        'direction': str,
        'feature': str,
        'protocol': str,
        'cg_id': int,
        'cg_name': str,
        'status': str,
        'src_og_lkup_hdl': int,
        'dst_og_lkup_hdl': int,
    }


class ShowPlatformSoftwareFedSwitchAclBindDbInterfaceFeatureDirDetailAsic(ShowPlatformSoftwareFedSwitchAclBindDbInterfaceFeatureDirDetailAsicSchema):
    """Parser for
       * show platform software fed {switch} {state} acl bind db interface {interface} feature {feature} dir {dir} detail asic {asic}
    """

    cli_command = 'show platform software fed {switch} {state} acl bind db interface {interface} feature {feature} dir {dir} detail asic {asic}'

    def cli(self, switch, state, interface, feature, dir, asic, output=None):
        if output is None:
            cmd = self.cli_command.format(switch=switch, state=state, interface=interface, feature=feature, dir=dir, asic=asic)
            output = self.device.execute(cmd)

        # Initialize the parsed dictionary
        ret_dict = {}

        # Interface Name: Vl300
        p1 = re.compile(r'^Interface Name:\s+(?P<interface_name>\S+)$')

        # Direction: Ingress
        p2 = re.compile(r'^Direction:\s+(?P<direction>\S+)$')

        # Feature         : Racl
        p3 = re.compile(r'^Feature\s+:\s+(?P<feature>\S+)$')

        # Protocol        : IPv4
        p4 = re.compile(r'^Protocol\s+:\s+(?P<protocol>\S+)$')

        # CG ID           : 11
        p5 = re.compile(r'^CG ID\s+:\s+(?P<cg_id>\d+)$')

        # CG Name         : aclscale-30
        p6 = re.compile(r'^CG Name\s+:\s+(?P<cg_name>\S+)$')

        # Status          : Success
        p7 = re.compile(r'^Status\s+:\s+(?P<status>\S+)$')

        # Src_og_lkup_hdl : 0
        p8 = re.compile(r'^Src_og_lkup_hdl\s+:\s+(?P<src_og_lkup_hdl>\d+)$')

        # Dst_og_lkup_hdl : 0
        p9 = re.compile(r'^Dst_og_lkup_hdl\s+:\s+(?P<dst_og_lkup_hdl>\d+)$')

        # Parse each line of the output
        for line in output.splitlines():
            line = line.strip()

            # Interface Name: Vl300
            m = p1.match(line)
            if m:
                ret_dict['interface_name'] = m.group('interface_name')
                continue

            # Direction: Ingress
            m = p2.match(line)
            if m:
                ret_dict['direction'] = m.group('direction')
                continue

            # Feature         : Racl
            m = p3.match(line)
            if m:
                ret_dict['feature'] = m.group('feature')
                continue

            # Protocol        : IPv4
            m = p4.match(line)
            if m:
                ret_dict['protocol'] = m.group('protocol')
                continue

            # CG ID           : 11
            m = p5.match(line)
            if m:
                ret_dict['cg_id'] = int(m.group('cg_id'))
                continue

            # CG Name         : aclscale-30
            m = p6.match(line)
            if m:
                ret_dict['cg_name'] = m.group('cg_name')
                continue

            # Status          : Success
            m = p7.match(line)
            if m:
                ret_dict['status'] = m.group('status')
                continue

            # Src_og_lkup_hdl : 0
            m = p8.match(line)
            if m:
                ret_dict['src_og_lkup_hdl'] = int(m.group('src_og_lkup_hdl'))
                continue

            # Dst_og_lkup_hdl : 0
            m = p9.match(line)
            if m:
                ret_dict['dst_og_lkup_hdl'] = int(m.group('dst_og_lkup_hdl'))
                continue

        return ret_dict 

class ShowPlatformSoftwareFedSwitchAclManKeyProfileEgressAllSchema(MetaParser):
    """Schema for 'show platform software fed {switch} {mode} acl man key-profile egress all'"""

    schema = {
        'egress_key_profiles': {
            Any(): {  # Profile name (e.g., OGBIN_SRC, OGBIN_DST, RACL)
                'index': int,
                Optional('type'): str,
                Optional('oid'): ListOf(int),
                Optional('hw_merge_idx'): int,
                Optional('hw_merge_grp'): int,
                Optional('pkp_idx'): int,
                Optional('label'): str,
                Optional('no_of_fields'): int,
                Optional('fields'): ListOf(str),
            }
        }
    }


class ShowPlatformSoftwareFedSwitchAclManKeyProfileEgressAll(ShowPlatformSoftwareFedSwitchAclManKeyProfileEgressAllSchema):
    """Parser for 'show platform software fed {switch} {mode} acl man key-profile egress all'"""

    cli_command = 'show platform software fed {switch} {mode} acl man key-profile egress all'

    def cli(self, switch='',mode='', output=None):
        if output is None:
            cmd = self.cli_command.format(switch=switch, mode=mode)
            output = self.device.execute(cmd)

        ret_dict = {}
        current_profile = None
        current_type = None

        # [Egress Key Profile: OGBIN_SRC, Idx: 0]
        p1 = re.compile(r'^\[Egress Key Profile: (?P<profile_name>\S+), Idx: (?P<index>\d+)\]$')

        # IPV4 or IPV6
        p2 = re.compile(r'^\s*(?P<type>IPV4|IPV6)$')

        # OID: [  528   450   450   450 ]
        p3 = re.compile(r'^\s*OID: \[\s*(?P<oid>[\d\s]+)\]$')

        #  Idx: 0    HW Merge Grp: 0    PKP Idx: 1    Label: LIF7
        p4 = re.compile(r'^\s*HW Merge Idx: (?P<hw_merge_idx>\d+)\s+HW Merge Grp: (?P<hw_merge_grp>\d+)\s+PKP Idx: (?P<pkp_idx>\d+)\s+Label: (?P<label>\S+)$')
        
        # No of fields: 13 [ 0x14 0x15 0x7 0x11 0xa 0xf 0x1c 0x1d 0x20 0x1e 0x1f 0x3a 0x3c ]
        p5 = re.compile(r'^\s*No of fields: (?P<no_of_fields>\d+)\s+\[\s*(?P<fields>[\w\s]+)\]$')

        for line in output.splitlines():
            line = line.strip()

            # [Egress Key Profile: OGBIN_SRC, Idx: 0]
            m = p1.match(line)
            if m:
                group = m.groupdict()
                current_profile = group['profile_name']
                ret_dict.setdefault('egress_key_profiles', {})[current_profile] = {
                    'index': int(group['index']),
                }
                continue

            # type :IPV4 or IPV6
            m = p2.match(line)
            if m and current_profile:
                current_type = m.group('type')
                ret_dict['egress_key_profiles'][current_profile]['type'] = current_type
                continue

            # OID: [  528   450   450   450 ]
            m = p3.match(line)
            if m and current_profile:
                oid_list = list(map(int, m.group('oid').split()))
                ret_dict['egress_key_profiles'][current_profile]['oid'] = oid_list
                continue

            # HW Merge Idx: 0    HW Merge Grp: 0    PKP Idx: 1    Label: LIF7
            m = p4.match(line)
            if m and current_profile:
                group = m.groupdict()
                ret_dict['egress_key_profiles'][current_profile].update({
                    'hw_merge_idx': int(group['hw_merge_idx']),
                    'hw_merge_grp': int(group['hw_merge_grp']),
                    'pkp_idx': int(group['pkp_idx']),
                    'label': group['label'],
                })
                continue

            # No of fields: 13 [ 0x14 0x15 0x7 0x11 0xa 0xf 0x1c 0x1d 0x20 0x1e 0x1f 0x3a 0x3c ]
            m = p5.match(line)
            if m and current_profile:
                group = m.groupdict()
                fields_list = group['fields'].split()
                ret_dict['egress_key_profiles'][current_profile].update({
                    'no_of_fields': int(group['no_of_fields']),
                    'fields': fields_list,
                })
                continue

        return ret_dict

class ShowPlatformSoftwareFedOifsetL2mSchema(MetaParser):
    """Schema for:
        * 'show platform software fed {switch} {module} oifset l2m'
        * 'show platform software fed {switch} {module} oifset l2m hash <hash_data>'
    """
    schema = {
        'oifsets': {
            Any(): {
                'type': str,
                'state': str,
                'md5': str,
                'fset_urid': str,
                'parent_urid': str,
                'remote_port_count': int,
                'users_count': int,
                'vp_oif_count': int,
                Optional('fset_gid'): int,
                Optional('asic_mcid_oid'): int,
                Optional('fset_svl_link'): {
                    'idx': str,
                    'port': str,
                    'gid': int,
                },
                Optional('hw_l2_mcg_info_asic'): ListOf(str),
                Optional('users'): ListOf(dict),
                Optional('vp_interfaces'): ListOf(dict),
            }
        }
    }

class ShowPlatformSoftwareFedOifsetL2m(ShowPlatformSoftwareFedOifsetL2mSchema):
    """Parser for:
        * 'show platform software fed {switch} {module} oifset l2m'
        * 'show platform software fed {switch} {module} oifset l2m hash <hash_data>'
    """

    cli_command = [
        'show platform software fed {switch} {module} oifset l2m',
        'show platform software fed {switch} {module} oifset l2m hash {hash_data}'
    ]

    def cli(self, switch='', module='', hash_data='', output=None):
        if output is None:
            if hash_data:
                cmd = self.cli_command[1].format(switch=switch, module=module, hash_data=hash_data)
            else:
                cmd = self.cli_command[0].format(switch=switch, module=module)
            output = self.device.execute(cmd)

        # Initialize the return dictionary 
        ret_dict = {}

        # Matching patterns
        # "Type: vlan_group           State: allocated       MD5:(d7cc48995242c698:167e8ad0954671bd)"
        p1 = re.compile(r'^Type:\s+(?P<type>\S+)\s+State:\s+(?P<state>\S+)\s+MD5:\((?P<md5>[\w:]+)\)$')

        # Fset Urid              : 0x2000000000000002
        p2 = re.compile(r'^Fset Urid\s+:\s+(?P<fset_urid>\S+)$')

        # Parent URID            : 0x0
        p3 = re.compile(r'^Parent URID\s+:\s+(?P<parent_urid>\S+)$')

        # Remote Port Count      : 0
        p4 = re.compile(r'^Remote Port Count\s+:\s+(?P<remote_port_count>\d+)$')

        # Users Count
        p5 = re.compile(r'^Users Count\s+:\s+(?P<users_count>\d+)$')

        # VP OIF Count
        p6 = re.compile(r'^VP OIF Count\s+:\s+(?P<vp_oif_count>\d+)$')

        # FSET Gid  
        p7 = re.compile(r'^FSET Gid\s+:\s+(?P<fset_gid>\d+)$')

        # Asic[0] mcid_oid 
        p8 = re.compile(r'^Asic\[\d+\] mcid_oid\s+:\s+(?P<asic_mcid_oid>\d+)$')

        # FSET Svl Link
        p9 = re.compile(r'^FSET Svl Link\s+:\s+Idx:\s+(?P<idx>\S+)\s+Port:\s+(?P<port>[\w/]+)\s+Gid:\s+(?P<gid>\d+)$')

        # Hw L2 Mcg Info Asic[0]
        p10 = re.compile(r'^Hw L2 Mcg Info Asic\[\d+\]\s*:\s*(?P<hw_l2_mcg_info_asic>.*)$')

        # urid:0x5000000000000002 (l2m_vlan:ipv6 vlan:1)
        p11 = re.compile(r'^urid:(?P<urid>\S+)\s+\((?P<info>.+)\)$')

        # 1. Po103_V103               Port-channel103          -------------
        p12 = re.compile(r'^\d+\.\s+(?P<vp_interface>\S+)\s+(?P<interface>\S+)\s+(?P<physical_interface>\S+)$')

        current_oifset = None

        for line in output.splitlines():
            line = line.strip()

            # Type: vlan_group           State: allocated       MD5:(d7cc48995242c698:167e8ad0954671bd)
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                current_oifset = groups['md5']
                oifset_dict = ret_dict.setdefault('oifsets', {}).setdefault(current_oifset, {})
                oifset_dict.update({
                    'type': groups['type'],
                    'state': groups['state'],
                    'md5': groups['md5']
                })
                continue

            # Fset Urid              : 0x2000000000000002
            m = p2.match(line)
            if m and current_oifset:
                ret_dict['oifsets'][current_oifset]['fset_urid'] = m.group('fset_urid')
                continue

            # Parent URID            : 0x0
            m = p3.match(line)
            if m and current_oifset:
                ret_dict['oifsets'][current_oifset]['parent_urid'] = m.group('parent_urid')
                continue

            # Remote Port Count      : 0
            m = p4.match(line)
            if m and current_oifset:
                ret_dict['oifsets'][current_oifset]['remote_port_count'] = int(m.group('remote_port_count'))
                continue

            # Users Count            : 1
            m = p5.match(line)
            if m and current_oifset:
                ret_dict['oifsets'][current_oifset]['users_count'] = int(m.group('users_count'))
                continue

            # VP OIF Count           : 0
            m = p6.match(line)
            if m and current_oifset:
                ret_dict['oifsets'][current_oifset]['vp_oif_count'] = int(m.group('vp_oif_count'))
                continue

            # FSET Gid               : 8194
            m = p7.match(line)
            if m and current_oifset:
                ret_dict['oifsets'][current_oifset]['fset_gid'] = int(m.group('fset_gid'))
                continue

            # Asic[0] mcid_oid       : 2224
            m = p8.match(line)
            if m and current_oifset:
                ret_dict['oifsets'][current_oifset]['asic_mcid_oid'] = int(m.group('asic_mcid_oid'))
                continue

            # FSET Svl Link          : Idx: 0x87 Port: HundredGigE0/13   Gid: 65534
            m = p9.match(line)
            if m and current_oifset:
                ret_dict['oifsets'][current_oifset]['fset_svl_link'] = {
                    'idx': m.group('idx'),
                    'port': m.group('port'),
                    'gid': int(m.group('gid'))
                }
                continue

            # Hw L2 Mcg Info Asic[0] :
            m = p10.match(line)
            if m and current_oifset:
                hw_l2_mcg_info_asic = m.group('hw_l2_mcg_info_asic')
                hw_l2_mcg_info_list = ret_dict['oifsets'][current_oifset].setdefault('hw_l2_mcg_info_asic', [])
                hw_l2_mcg_info_list.append(hw_l2_mcg_info_asic)
                continue

            # urid:0x5000000000000002 (l2m_vlan:ipv6 vlan:1)
            m = p11.match(line)
            if m and current_oifset:
                users_list = ret_dict['oifsets'][current_oifset].setdefault('users', [])
                users_list.append({
                    'urid': m.group('urid'),
                    'info': m.group('info')
                })
                continue

            # 1. Po103_V103               Port-channel103          -------------
            m = p12.match(line)
            if m and current_oifset:
                vp_interfaces_list = ret_dict['oifsets'][current_oifset].setdefault('vp_interfaces', [])
                vp_interfaces_list.append({
                    'vp_interface': m.group('vp_interface'),
                    'interface': m.group('interface'),
                    'physical_interface': m.group('physical_interface')
                })
                continue

        return ret_dict

class ShowPlatformSoftwareFedSwitchAclManKeyProfileIngressAllSchema(MetaParser):
    """Schema for 'show platform software fed {switch} {mode} acl man key-profile ingress all'"""

    schema = {
        'ingress_key_profiles': {
            Any(): {  
                'index': int,
                Optional('type'): str,
                'oid': ListOf(int),
                'hw_merge_idx': int,
                'hw_merge_grp': int,
                'pkp_idx': int,
                'label': str,
                'no_of_fields': int,
                Optional('fields'): ListOf(str),
            }
        }
    }


class ShowPlatformSoftwareFedSwitchAclManKeyProfileIngressAll(ShowPlatformSoftwareFedSwitchAclManKeyProfileIngressAllSchema):
    """Parser for 'show platform software fed {switch} {mode} acl man key-profile ingress all'"""

    cli_command = 'show platform software fed {switch} {mode} acl man key-profile ingress all'

    def cli(self, switch='', mode='', output=None):
        if output is None:
            cmd = self.cli_command.format(switch=switch, mode=mode)
            output = self.device.execute(cmd)

        ret_dict = {}
        current_profile = None

        # Regex for [Ingress Key Profile: ACCSEC, Idx: 0]
        p1 = re.compile(r'^\[Ingress Key Profile: (?P<profile_name>\S+), Idx: (?P<index>\d+)\]$')
        # regex for ETH
        p2 = re.compile(r'^\s*(?P<type>\S+)$')
        # regex for OID: [  472   394   394   394 ]
        p3 = re.compile(r'^\s*OID: \[\s*(?P<oid>[\d\s]+)\]$')
        # regex for HW Merge Idx: 0    HW Merge Grp: 2    PKP Idx: 0    Label: LIF7
        p4 = re.compile(r'^\s*HW Merge Idx: (?P<hw_merge_idx>\d+)\s+HW Merge Grp: (?P<hw_merge_grp>\d+)\s+PKP Idx: (?P<pkp_idx>\d+)\s+Label: (?P<label>\S+)$')
        # regx for No of fields: 5 [ 0x1 0x2 0x21 0x14 0x2f ]
        p5 = re.compile(r'^\s*No of fields: (?P<no_of_fields>\d+)\s+\[\s*(?P<fields>[\w\s]+)\]$')

        for line in output.splitlines():
            line = line.strip()

            # [Ingress Key Profile: ACCSEC, Idx: 0]
            m = p1.match(line)
            if m:
                group = m.groupdict()
                current_profile = group['profile_name']
                ret_dict.setdefault('ingress_key_profiles', {})[current_profile] = {
                    'index': int(group['index']),
                    'no_of_fields': 0
                }
                continue

            # ETH
            m = p2.match(line)
            if m and current_profile:
                ret_dict['ingress_key_profiles'][current_profile]['type'] = m.group('type')
                continue

            # OID: [  472   394   394   394 ]
            m = p3.match(line)
            if m and current_profile:
                oid_list = list(map(int, m.group('oid').split()))
                ret_dict['ingress_key_profiles'][current_profile]['oid'] = oid_list
                continue

            # HW Merge Idx: 0    HW Merge Grp: 2    PKP Idx: 0    Label: LIF7
            m = p4.match(line)
            if m and current_profile:
                group = m.groupdict()
                ret_dict['ingress_key_profiles'][current_profile].update({
                    'hw_merge_idx': int(group['hw_merge_idx']),
                    'hw_merge_grp': int(group['hw_merge_grp']),
                    'pkp_idx': int(group['pkp_idx']),
                    'label': group['label'],
                })
                continue

            # No of fields: 5 [ 0x1 0x2 0x21 0x14 0x2f ]
            m = p5.match(line)
            if m and current_profile:
                group = m.groupdict()
                fields_list = group['fields'].split()
                ret_dict['ingress_key_profiles'][current_profile].update({
                    'no_of_fields': int(group['no_of_fields']),
                    'fields': fields_list,
                })
                continue

        return ret_dict	        

class ShowPlatformSoftwareFedSwitchAclParallelKeyProfileIngressSchema(MetaParser):
    """Schema for:
       * show platform software fed {switch} {state} acl man parallel-key-profile ingress all
    """
    schema = {
        'ingress': {
            Any(): {  # Profile name
                "index": int,
                Optional("protocols"): {
                    Any(): {  # ETH, IPV4, IPV6
                        "oid": list,
                        "ref_cnt": list,
                        "e_values": {
                            Any(): list,  # E0, E1, E2, E3
                        },
                        "no_of_key_prof": int,
                        "wide": bool,
                        "rtf": bool,
                        "stage": str,
                    }
                }
            }
        }
    }


class ShowPlatformSoftwareFedSwitchAclParallelKeyProfileIngress(ShowPlatformSoftwareFedSwitchAclParallelKeyProfileIngressSchema):
    """Parser for:
       * show platform software fed {switch} {state} acl man parallel-key-profile ingress all
    """

    cli_command = "show platform software fed {switch} {state} acl man parallel-key-profile ingress all"

    def cli(self, switch, state, output=None):
        if output is None:
            cmd = self.cli_command.format(state=state, switch=switch)
            output = self.device.execute(cmd)

        ret_dict = {}
        current_profile = None
        current_protocol = None

        #  [Ingress Paralley Key Profile: ACCSEC, Idx: 0]
        p1 = re.compile(r"^\[Ingress Paralley Key Profile: (?P<profile_name>[\w\-]+), Idx: (?P<index>\d+)\]$")
        
        # ETH
        p2 = re.compile(r"^(?P<protocol>\w+)$")

        # OID:     [  554   476   476   476 ]
        p3 = re.compile(r"^OID:\s+\[\s+(?P<oid>[\d\s]+)\]$")
        
        # Ref cnt: [    0     0     0     0 ]
        p4 = re.compile(r"^Ref cnt:\s+\[\s+(?P<ref_cnt>[\d\s]+)\]$")
        
        # E0:     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0
        p5 = re.compile(r"^(?P<e_value>E\d):\s+(?P<values>[\d,\s]+)$")
        
        # No of Key Prof: 1    Wide: True    RTF: False    Stage: TERM
        p6 = re.compile(
            r"^No of Key Prof:\s+(?P<no_of_key_prof>\d+)\s+Wide:\s+(?P<wide>\w+)\s+RTF:\s+(?P<rtf>\w+)\s+Stage:\s+(?P<stage>\w+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            #  [Ingress Paralley Key Profile: ACCSEC, Idx: 0]
            m = p1.match(line)
            if m:
                profile_name = m.group("profile_name")
                index = int(m.group("index"))
                current_profile = profile_name
                ret_dict.setdefault("ingress", {}).setdefault(current_profile, {"index": index})
                continue

            # ETH
            m = p2.match(line)
            if m:
                current_protocol = m.group("protocol")
                ret_dict["ingress"][current_profile].setdefault("protocols", {})
                ret_dict["ingress"][current_profile]["protocols"][current_protocol] = {
                    "e_values": {},
                    "oid": [],
                    "ref_cnt": [],
                    "no_of_key_prof": 0,
                    "wide": False,
                    "rtf": False,
                    "stage": "",
                }
                continue

            # OID:     [  554   476   476   476 ]
            m = p3.match(line)
            if m and current_protocol:
                oid = list(map(int, m.group("oid").split()))
                ret_dict["ingress"][current_profile]["protocols"][current_protocol]["oid"] = oid
                continue

            # Ref cnt: [    0     0     0     0 ]
            m = p4.match(line)
            if m and current_protocol:
                ref_cnt = list(map(int, m.group("ref_cnt").split()))
                ret_dict["ingress"][current_profile]["protocols"][current_protocol]["ref_cnt"] = ref_cnt
                continue

            # E0:     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0
            m = p5.match(line)
            if m and current_protocol:
                e_value = m.group("e_value")
                values = list(map(int, m.group("values").replace(",", "").split()))
                ret_dict["ingress"][current_profile]["protocols"][current_protocol]["e_values"][e_value] = values
                continue

            # No of Key Prof: 1    Wide: True    RTF: False    Stage: TERM
            m = p6.match(line)
            if m and current_protocol:
                ret_dict["ingress"][current_profile]["protocols"][current_protocol].update(
                    {
                        "no_of_key_prof": int(m.group("no_of_key_prof")),
                        "wide": m.group("wide").lower() == "true",
                        "rtf": m.group("rtf").lower() == "true",
                        "stage": m.group("stage"),
                    }
                )
                continue

        return ret_dict
    
class ShowPlatformSoftwareFedSwitchAclBindSdkInterfaceFeatureDirDetailAsicSchema(MetaParser):
    """Schema for
       * show platform software fed {switch} {state} acl bind sdk interface {interface} feature {feature} dir {dir} detail asic {asic}
    """
    schema = {
        'interface_name': str,
        'direction': str,
        'feature': str,
        'protocol': str,
        'cg_id': int,
        'cg_name': str,
        'acl': {
            'oid': str,
            'no_of_aces': int,
            'entries': ListOf({
                'ipv4_src': {
                    'value': str,
                    'mask': str,
                },
                'ipv4_dst': {
                    'value': str,
                    'mask': str,
                },
                'proto': str,
                'tos': str,
                'tcp_flg': str,
                'ttl': str,
                'ipv4_flags': str,
                'src_port': str,
                'dst_port': str,
                'result_action': {
                    'punt': str,
                    'drop': str,
                    'mirror': str,
                    'counter': str,
                    'counter_value': int,
                }
            })
        }
    }


class ShowPlatformSoftwareFedSwitchAclBindSdkInterfaceFeatureDirDetailAsic(ShowPlatformSoftwareFedSwitchAclBindSdkInterfaceFeatureDirDetailAsicSchema):
    """Parser for
       * show platform software fed {switch} {state} acl bind sdk interface {interface} feature {feature} dir {dir} detail asic {asic}
    """

    cli_command = 'show platform software fed {switch} {state} acl bind sdk interface {interface} feature {feature} dir {dir} detail asic {asic}'

    def cli(self,state, switch, interface, feature, dir, asic, output=None):
        if output is None:
            cmd = self.cli_command.format(switch=switch, state=state, interface=interface, feature=feature, dir=dir, asic=asic)
            output = self.device.execute(cmd)

        # Initialize parsed dictionary
        parsed_dict = {}

        # Interface Name: Vl300
        p1 = re.compile(r'^Interface Name:\s+(?P<interface_name>\S+)$')

        # Direction: Ingress
        p2 = re.compile(r'^Direction:\s+(?P<direction>\S+)$')

        # Feature : Racl
        p3 = re.compile(r'^Feature\s+:\s+(?P<feature>\S+)$')

        # Protocol : IPv4
        p4 = re.compile(r'^Protocol\s+:\s+(?P<protocol>\S+)$')

        # CG ID : 11
        p5 = re.compile(r'^CG ID\s+:\s+(?P<cg_id>\d+)$')

        # CG Name : aclscale-30
        p6 = re.compile(r'^CG Name\s+:\s+(?P<cg_name>\S+)$')
        
        # ACL (OID: 0x453, No of ACEs: 30001)
        p7 = re.compile(r'^ACL\s+\(OID:\s+(?P<oid>\S+),\s+No of ACEs:\s+(?P<no_of_aces>\d+)\)$')

        # ipv4_src: value = 110.80.0.1 mask = 255.255.255.255
        p8 = re.compile(r'^ipv4_src:\s+value\s+=\s+(?P<value>\S+)\s+mask\s+=\s+(?P<mask>\S+)$')

        # ipv4_dst: value = 210.100.0.1 mask = 255.255.255.255
        p9 = re.compile(r'^ipv4_dst:\s+value\s+=\s+(?P<value>\S+)\s+mask\s+=\s+(?P<mask>\S+)$')

        # V:  0x0 0x0 0x0 0x0 0x0 0x0 0x0
        p10 = re.compile(r'^V:\s+(?P<proto>\S+)\s+(?P<tos>\S+)\s+(?P<tcp_flg>\S+)\s+(?P<ttl>\S+)\s+(?P<ipv4_flags>\S+)\s+(?P<src_port>\S+)\s+(?P<dst_port>\S+)$')
        
        # Punt : N Drop : N Mirror: N Counter: 0x0 (0)
        p11 = re.compile(r'^Punt\s+:\s+(?P<punt>\S+)\s+Drop\s+:\s+(?P<drop>\S+)\s+Mirror:\s+(?P<mirror>\S+)\s+Counter:\s+(?P<counter>\S+)\s+\((?P<counter_value>\d+)\)$')

        current_entry = None

        for line in output.splitlines():
            line = line.strip()

            # Interface Name: Vl300
            m = p1.match(line)
            if m:
                parsed_dict['interface_name'] = m.group('interface_name')
                continue

            # Direction: Ingress
            m = p2.match(line)
            if m:
                parsed_dict['direction'] = m.group('direction')
                continue

            # Feature : Racl
            m = p3.match(line)
            if m:
                parsed_dict['feature'] = m.group('feature')
                continue

            # Protocol : IPv4
            m = p4.match(line)
            if m:
                parsed_dict['protocol'] = m.group('protocol')
                continue

            # CG ID : 11
            m = p5.match(line)
            if m:
                parsed_dict['cg_id'] = int(m.group('cg_id'))
                continue

            # CG Name : aclscale-30
            m = p6.match(line)
            if m:
                parsed_dict['cg_name'] = m.group('cg_name')
                continue

            # ACL (OID: 0x453, No of ACEs: 30001)
            m = p7.match(line)
            if m:
                acl_dict = parsed_dict.setdefault('acl', {})
                acl_dict['oid'] = m.group('oid')
                acl_dict['no_of_aces'] = int(m.group('no_of_aces'))
                acl_dict['entries'] = []
                continue

            # ipv4_src: value = 110.80.0.1 mask = 255.255.255.255
            m = p8.match(line)
            if m:
                current_entry = {
                    'ipv4_src': {
                        'value': m.group('value'),
                        'mask': m.group('mask'),
                    }
                }
                acl_dict['entries'].append(current_entry)
                continue

            # ipv4_dst: value = 210.100.0.1 mask = 255.255.255.255
            m = p9.match(line)
            if m and current_entry:
                current_entry['ipv4_dst'] = {
                    'value': m.group('value'),
                    'mask': m.group('mask'),
                }
                continue

            # V:  0x0 0x0 0x0 0x0 0x0 0x0 0x0
            m = p10.match(line)
            if m and current_entry:
                current_entry.update({
                    'proto': m.group('proto'),
                    'tos': m.group('tos'),
                    'tcp_flg': m.group('tcp_flg'),
                    'ttl': m.group('ttl'),
                    'ipv4_flags': m.group('ipv4_flags'),
                    'src_port': m.group('src_port'),
                    'dst_port': m.group('dst_port'),
                })
                continue

            # Punt : N Drop : N Mirror: N Counter: 0x0 (0)
            m = p11.match(line)
            if m and current_entry:
                current_entry['result_action'] = {
                    'punt': m.group('punt'),
                    'drop': m.group('drop'),
                    'mirror': m.group('mirror'),
                    'counter': m.group('counter'),
                    'counter_value': int(m.group('counter_value')),
                }
                continue

        return parsed_dict    


class ShowPlatformSoftwareFedSwitchAclManagerAclGroupSchema(MetaParser):
    """Schema for:
        show platform software fed {switch} <active/stby> acl manager acl-group interface <interface>
    """

    schema = {
        'direction': str,
        'asic': int,
        'pkt_fmt': str,
        'acl_groups': {
            Any(): str,  
        }
    }

class ShowPlatformSoftwareFedSwitchAclManagerAclGroup(ShowPlatformSoftwareFedSwitchAclManagerAclGroupSchema):
    """Parser for:
       show platform software fed {switch} <active/stby> acl manager acl-group interface <interface>
    """

    cli_command = 'show platform software fed {switch} {mode} acl manager acl-group interface {interface}'

    def cli(self, switch='', mode='', interface='', output=None):
        if output is None:
            cmd = self.cli_command.format(switch=switch, mode=mode, interface=interface)
            output = self.device.execute(cmd)

        ret_dict = {}

        # Dir: Ingress  Asic: 0  PKT_FMT: ETH
        p1 = re.compile(r'^Dir:\s+(?P<direction>\S+)\s+Asic:\s+(?P<asic>\d+)\s+PKT_FMT:\s+(?P<pkt_fmt>\S+)$')

        # ACCSEC     :  0x0
        p2 = re.compile(r'^(?P<acl_group>\S+)\s+:\s+(?P<value>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # Dir: Ingress  Asic: 0  PKT_FMT: ETH
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['direction'] = group['direction']
                ret_dict['asic'] = int(group['asic'])
                ret_dict['pkt_fmt'] = group['pkt_fmt']
                continue

            # ACCSEC     :  0x0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                acl_groups = ret_dict.setdefault('acl_groups', {})
                acl_groups[group['acl_group']] = group['value']
                continue

        return ret_dict
    
class ShowPlatformSoftwareFedSwitchAclManagerAclGroupIifIdSchema(MetaParser):
    """Schema for:
       * show platform software fed {switch} acl manager acl-group iif_id <if_id_num>
    """

    schema = {
        'direction': str,
        'asic': int,
        'pkt_fmt': str,
        'acl_groups': {
            Any(): str,  
        }
    }

class ShowPlatformSoftwareFedSwitchAclManagerAclGroupIifId(ShowPlatformSoftwareFedSwitchAclManagerAclGroupIifIdSchema):
    """Parser for:
       * show platform software fed {switch} acl manager acl-group iif_id <if_id_num>
    """

    cli_command = 'show platform software fed {switch} acl manager acl-group iif_id {if_id_num}'

    def cli(self, switch='', if_id_num='', output=None):
        if output is None:
            cmd = self.cli_command.format(switch=switch, if_id_num=if_id_num)
            output = self.device.execute(cmd)

        ret_dict = {}

        # Dir: Ingress  Asic: 1  PKT_FMT: ETH
        p1 = re.compile(r'^Dir:\s+(?P<direction>\S+)\s+Asic:\s+(?P<asic>\d+)\s+PKT_FMT:\s+(?P<pkt_fmt>\S+)$')

        # ACCSEC     :  0x0
        p2 = re.compile(r'^(?P<acl_group>\S+)\s+:\s+(?P<value>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # Dir: Ingress  Asic: 1  PKT_FMT: ETH
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['direction'] = group['direction']
                ret_dict['asic'] = int(group['asic'])
                ret_dict['pkt_fmt'] = group['pkt_fmt']
                continue

            # ACCSEC     :  0x0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                acl_groups = ret_dict.setdefault('acl_groups', {})
                acl_groups[group['acl_group']] = group['value']
                continue

        return ret_dict

class ShowPlatformSoftwareFedSwitchWdavcFlowsSchema(MetaParser):
    """
    Schema for show platform software fed switch {switch_num} wdavc flows
    """
    schema = {
        "index": {
            Any(): {
                "ip1": str,
                "ip2": str,
                "port1": int,
                "port2": int,
                "l3_proto": int,
                "l4_proto": int,
                "vrf_vlan": int,
                "timeout_sec": int,
                "app_name": str,
                "tuple_type": str,
                "flow_type": str,
                "swapped": str,
                "clients": str,
                "allow_bp": bool,
                "final": bool,
                "pkts": int,
                "bypass_pkt": int
            }
        }
    }


class ShowPlatformSoftwareFedSwitchWdavcFlows(ShowPlatformSoftwareFedSwitchWdavcFlowsSchema):
    """
    Parser for show platform software fed switch {switch_num} wdavc flows
    """

    cli_command = "show platform software fed switch {switch_num} wdavc flows"

    def cli(self, switch_num="", output=None):
        if output is None:
            cmd = self.cli_command.format(switch_num=switch_num)
            output = self.device.execute(cmd)

        ret_dict = {}
        index = 1

        #IX  |IP1                                     |IP2                                     |PORT1|PORT2|L3   |L4   |VRF |TIMEOUT|APP                             |TUPLE   |FLOW     |IS FIF  |CLIENTS|BYPASS|FINAL |#PKTS |BYPASS|
            #|                                        |                                        |     |     |PROTO|PROTO|VLAN|SEC  HL|NAME                            |TYPE    |TYPE     |SWAPPED |ALLW BP|      |      |      |PKT   |
        #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #1   |10.10.1.166                             |66.220.146.224                          |52059|80   |1    |6    |0   |360  HW|facebook                        |Full    |Real Flow|No      |0x01   |True  |True  |69    |21    |
        
        p1 = re.compile(r'^(?P<ix>\d+)\s+\|(?P<ip1>[^\|]+)\|(?P<ip2>[^\|]+)\|(?P<port1>[^\|]+)\|(?P<port2>[^\|]+)\|(?P<l3_proto>[^\|]+)\|(?P<l4_proto>[^\|]+)\|(?P<vrf_vlan>[^\|]+)\|(?P<timeout_sec>\d+)\s+HW\|(?P<app_name>[^\|]+)\|(?P<tuple_type>[^\|]+)\|(?P<flow_type>[^\|]+)\|(?P<swapped>[^\|]+)\|(?P<clients>[^\|]+)\|(?P<allow_bp>[^\|]+)\|(?P<final>[^\|]+)\|(?P<pkts>[^\|]+)\|(?P<bypass_pkt>[^\|]+)\|$')

        for line in output.splitlines():
            line = line.strip()
            
            #IX  |IP1                                     |IP2                                     |PORT1|PORT2|L3   |L4   |VRF |TIMEOUT|APP                             |TUPLE   |FLOW     |IS FIF  |CLIENTS|BYPASS|FINAL |#PKTS |BYPASS|
            #|                                        |                                        |     |     |PROTO|PROTO|VLAN|SEC  HL|NAME                            |TYPE    |TYPE     |SWAPPED |ALLW BP|      |      |      |PKT   |
            #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            #1   |10.10.1.166                             |66.220.146.224                          |52059|80   |1    |6    |0   |360  HW|facebook                        |Full    |Real Flow|No      |0x01   |True  |True  |69    |21    |
            
            m = p1.match(line)
            if m:
                group = m.groupdict()
                idx = int(group.pop("ix"))

                index_dict = ret_dict.setdefault("index", {}).setdefault(idx, {})
                index_dict["ip1"] = group["ip1"].strip()
                index_dict["ip2"] = group["ip2"].strip()
                index_dict["port1"] = int(group["port1"])
                index_dict["port2"] = int(group["port2"])
                index_dict["l3_proto"] = int(group["l3_proto"])
                index_dict["l4_proto"] = int(group["l4_proto"])
                index_dict["vrf_vlan"] = int(group["vrf_vlan"])
                index_dict["timeout_sec"] = int(group["timeout_sec"])
                index_dict["app_name"] = group["app_name"].strip()
                index_dict["tuple_type"] = group["tuple_type"].strip()
                index_dict["flow_type"] = group["flow_type"].strip()
                index_dict["swapped"] = group["swapped"].strip()
                index_dict["clients"] = group["clients"].strip()
                index_dict["allow_bp"] = group["allow_bp"].strip().lower() == "true"
                index_dict["final"] = group["final"].strip().lower() == "true"
                index_dict["pkts"] = int(group["pkts"])
                index_dict["bypass_pkt"] = int(group["bypass_pkt"])

        return ret_dict

class ShowPlatformSoftwareFedSwitchWdavcFunctionFlowsSchema(MetaParser):
    """
    Schema for show platform software fed switch <switch> wdavc function wdavc_ft_show_all_flows_seg_ui
    
    """
    schema = {
    "index": {
        Any(): {
            "ip1": str,
            "ip2": str,
            "port1": int,
            "port2": int,
            "l3_proto": int,
            "l4_proto": int,
            "vrf_vlan": int,
            "timeout_sec": int,
            "timeout_hl": str,
            "app_name": str,
            "tuple_type": str,
            "flow_type": str,
            "is_swapped": str,
            "clients": str,
            "bypass_type": bool,
            "final": bool,
            "pkts": int,
            "bypass_pkt": int,
            "seg_index": {
                Any(): {
                    "if_id": int,
                    "opst_if": Or(int, str),
                    "seg_dir": str,
                    "vlan": int,
                    "fif_dir": bool,
                    "seen": bool,
                    "is_set": bool,
                    "dop_id": int,
                    "nfl_hdl_st": str,
                    "bps_pnd": int,
                    "app_pnd": int,
                    "frst_ts": int,
                    "last_ts": int,
                    "bytes": int,
                    "pkts": int,
                    "tcp_flgs": int
                },
            },
         },
    },
}


class ShowPlatformSoftwareFedSwitchWdavcFunctionFlows(ShowPlatformSoftwareFedSwitchWdavcFunctionFlowsSchema):
    """
    Parser for:
    show platform software fed switch <switch> wdavc function wdavc_ft_show_all_flows_seg_ui
    """

    cli_command = 'show platform software fed switch {switch} wdavc function wdavc_ft_show_all_flows_seg_ui'

    def cli(self, switch="", output=None):
        if output is None:
            cmd = self.cli_command.format(switch=switch)
            output = self.device.execute(cmd)

        ret_dict = {}
        current_index = None
        seg_index_counter = 0

        #IX  |IP1                                     |IP2                                     |PORT1|PORT2|L3   |L4   |VRF |TIMEOUT|APP                             |TUPLE   |FLOW     |IS FIF  |CLIENTS|BYPASS|FINAL |#PKTS |BYPASS|
        #    |                                        |                                        |     |     |PROTO|PROTO|VLAN|SEC  HL|NAME                            |TYPE    |TYPE     |SWAPPED |ALLW BP|      |      |      |PKT   |
        #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #1   |10.10.1.166                             |66.220.146.224                          |52059|80   |1    |6    |0   |360  HW|facebook                        |Full    |Real Flow|No      |0x01   |True  |True  |69    |21    |    
        
        p1 = re.compile(r'^(?P<ix>\d+)\s+\|(?P<ip1>[^\|]+)\|(?P<ip2>[^\|]+)\|(?P<port1>[^\|]+)\|(?P<port2>[^\|]+)\|(?P<l3_proto>[^\|]+)\|(?P<l4_proto>[^\|]+)\|(?P<vrf_vlan>[^\|]+)\|(?P<timeout_sec>\d+)\s+(?P<timeout_hl>\w+)\|(?P<app_name>[^\|]+)\|(?P<tuple_type>[^\|]+)\|(?P<flow_type>[^\|]+)\|(?P<is_swapped>[^\|]+)\|(?P<clients>[^\|]+)\|(?P<bypass_type>[^\|]+)\|(?P<final>[^\|]+)\|(?P<pkts>[^\|]+)\|(?P<bypass_pkt>[^\|]+)\|$'
        )

        #SEG IDX |I/F ID |OPST I/F |SEG DIR |.1Q VLAN|FIF DIR | SEEN  |Is SET |DOP ID |NFL HDL ST |BPS PND |APP PND |FRST TS |LAST TS |BYTES  |PKTS   |TCP FLGS|
            #-------------------------------------------------------------------------------------------------------------------------------------------------------
            #0       |1050   |1051     |Ingress |0       |True    |True   |True   |0      |0        VV|0       |0       |1753712193000|1753712240000|283178 |265    |0       |

        #SEG IDX |I/F ID |OPST I/F |SEG DIR |.1Q VLAN|FIF DIR | SEEN  |Is SET |DOP ID |NFL HDL ST |BPS PND |APP PND |FRST TS |LAST TS |BYTES  |PKTS   |TCP FLGS|
            #-------------------------------------------------------------------------------------------------------------------------------------------------------
            #0       |1050   |----     |Ingress |0       |True    |True   |True   |0      |4        VV|0       |0       |1758196434000|1758196529000|193824 |180    |0       |

        
        p2 = re.compile(
            r'^\s*(?P<seg_idx>\d+)\s*\|\s*(?P<if_id>\d+)\s*\|\s*(?P<opst_if>\d+|----)\s*\|\s*'
            r'(?P<seg_dir>\w+)\s*\|\s*(?P<vlan>\d+)\s*\|\s*(?P<fif_dir>\w+)\s*\|\s*'
            r'(?P<seen>\w+)\s*\|\s*(?P<is_set>\w+)\s*\|\s*(?P<dop_id>\d+)\s*\|\s*'
            r'(?P<nfl_hdl_st>[\w ]+)\s*\|\s*(?P<bps_pnd>\d+)\s*\|\s*(?P<app_pnd>\d+)\s*\|\s*'
            r'(?P<frst_ts>\d+)\s*\|\s*(?P<last_ts>\d+)\s*\|\s*(?P<bytes>\d+)\s*\|\s*(?P<pkts>\d+)\s*\|\s*(?P<tcp_flgs>\d+)'
        )

        for line in output.splitlines():
            line = line.strip()
        
            if not line or line.startswith(("IX", "---", "CurrFlows")):
                continue
            
            #IX  |IP1                                     |IP2                                     |PORT1|PORT2|L3   |L4   |VRF |TIMEOUT|APP                             |TUPLE   |FLOW     |IS FIF  |CLIENTS|BYPASS|FINAL |#PKTS |BYPASS|
            #    |                                        |                                        |     |     |PROTO|PROTO|VLAN|SEC  HL|NAME                            |TYPE    |TYPE     |SWAPPED |ALLW BP|      |      |      |PKT   |
            #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            #1   |10.10.1.166                             |66.220.146.224                          |52059|80   |1    |6    |0   |360  HW|facebook                        |Full    |Real Flow|No      |0x01   |True  |True  |69    |21    |   
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                current_index = int(group["ix"])
                seg_index_counter = 0 
                flow_dict = ret_dict.setdefault("index", {}).setdefault(current_index, {})
        
                flow_dict.update({
                    "ip1": group["ip1"].strip(),
                    "ip2": group["ip2"].strip(),
                    "port1": int(group["port1"]),
                    "port2": int(group["port2"]),
                    "l3_proto": int(group["l3_proto"]),
                    "l4_proto": int(group["l4_proto"]),
                    "vrf_vlan": int(group["vrf_vlan"]),
                    "timeout_sec": int(group["timeout_sec"]),
                    "timeout_hl": group["timeout_hl"].strip(),
                    "app_name": group["app_name"].strip(),
                    "tuple_type": group["tuple_type"].strip(),
                    "flow_type": group["flow_type"].strip(),
                    "is_swapped": group["is_swapped"].strip(),
                    "clients": group["clients"].strip(),
                    "bypass_type": group["bypass_type"].strip().lower() == "true",
                    "final": group["final"].strip().lower() == "true",
                    "pkts": int(group["pkts"]),
                    "bypass_pkt": int(group["bypass_pkt"]),
                    "seg_index": {}  
                })
                continue
            
            #SEG IDX |I/F ID |OPST I/F |SEG DIR |.1Q VLAN|FIF DIR | SEEN  |Is SET |DOP ID |NFL HDL ST |BPS PND |APP PND |FRST TS |LAST TS |BYTES  |PKTS   |TCP FLGS|
            #-------------------------------------------------------------------------------------------------------------------------------------------------------
            #0       |1050   |1051     |Ingress |0       |True    |True   |True   |0      |0        VV|0       |0       |1753712193000|1753712240000|283178 |265    |0       |
            
            #SEG IDX |I/F ID |OPST I/F |SEG DIR |.1Q VLAN|FIF DIR | SEEN  |Is SET |DOP ID |NFL HDL ST |BPS PND |APP PND |FRST TS |LAST TS |BYTES  |PKTS   |TCP FLGS|
            #-------------------------------------------------------------------------------------------------------------------------------------------------------
            #0       |1050   |----     |Ingress |0       |True    |True   |True   |0      |4        VV|0       |0       |1758196434000|1758196529000|193824 |180    |0       |
            
            m2 = p2.match(line)
            if m2 and current_index is not None:
                group = m2.groupdict()
                seg_dict = ret_dict["index"][current_index]["seg_index"].setdefault(seg_index_counter, {})
        
                # Handle opst_if which can be a number or "----"
                opst_if_value = group["opst_if"]
                if opst_if_value == "----":
                    opst_if_final = opst_if_value
                else:
                    opst_if_final = int(opst_if_value)
        
                seg_dict.update({
                    "if_id": int(group["if_id"]),
                    "opst_if": opst_if_final,
                    "seg_dir": group["seg_dir"].strip(),
                    "vlan": int(group["vlan"]),
                    "fif_dir": group["fif_dir"].lower() == "true",
                    "seen": group["seen"].lower() == "true",
                    "is_set": group["is_set"].lower() == "true",
                    "dop_id": int(group["dop_id"]),
                    "nfl_hdl_st": group["nfl_hdl_st"].strip(),
                    "bps_pnd": int(group["bps_pnd"]),
                    "app_pnd": int(group["app_pnd"]),
                    "frst_ts": int(group["frst_ts"]),
                    "last_ts": int(group["last_ts"]),
                    "bytes": int(group["bytes"]),
                    "pkts": int(group["pkts"]),
                    "tcp_flgs": int(group["tcp_flgs"]),
                })
                seg_index_counter += 1
                continue

        return ret_dict

# ========================================================================
# Schema for 'show platform software fed switch {switch_state} swc statistics'
# ========================================================================
class ShowPlatformSoftwareFedSwitchSwcStatisticsSchema(MetaParser):
    """Schema for 'show platform software fed switch {switch_state} swc statistics'"""

    schema = {
        "swc_upload_statistics": {
            "last_file_uploaded": str,
            "time_of_upload": str,
            "current_file_uploading": str,
            "files_queued_for_upload": str,
            "number_of_files_queued": int,
            "last_failed_upload": str,
            "files_failed_to_upload": int,
            "files_successfully_uploaded": int,
        },
        "swc_file_creation_statistics": {
            "last_file_created": str,
            "time_of_creation": str,
        },
        "swc_flow_statistics": {
            "number_of_flows_in_prev_file": int,
            "number_of_flows_in_curr_file": int,
            "invalid_dropped_flows": int,
            "error_dropped_flows": int,
        },
        "swc_flags": {
            "is_registered": str,
            "delete_debug": str,
            "exporter_delete_debug": str,
            "certificate_validation": str,
        }
    }

# ========================================================================
# Parser for 'show platform software fed switch {switch_state} swc statistics'
# ========================================================================
class ShowPlatformSoftwareFedSwitchSwcStatistics(ShowPlatformSoftwareFedSwitchSwcStatisticsSchema):
    """
    Parser for :
        * show platform software fed switch {switch_state} swc statistics
    """

    cli_command = [
        "show platform software fed switch {switch_state} swc statistics"
    ]

    def cli(self, switch_state="active", output=None):
        if output is None:
            cmd = self.cli_command[0].format(switch_state=switch_state)
            output = self.device.execute(cmd)

        ret_dict = {}

        # Patterns for each line
        #  1: Last file uploaded          :   
        p1 = re.compile(r"^1: Last file uploaded\s*:\s*(?P<last_file_uploaded>.*)$")
        #  2: Time of upload              :  
        p2 = re.compile(r"^2: Time of upload\s*:\s*(?P<time_of_upload>.*)$")
        #  3: Current file uploading      :  
        p3 = re.compile(r"^3: Current file uploading\s*:\s*(?P<current_file_uploading>.*)$")
        #  4: Files queued for upload     :  202510151103_2, 202510151104_3, 202510151105_2, 202510151104_2, 202510151106_2 
        p4 = re.compile(r"^4: Files queued for upload\s*:\s*(?P<files_queued_for_upload>.*)$")
        #  5: Number of files queued      :  5
        p5 = re.compile(r"^5: Number of files queued\s*:\s*(?P<number_of_files_queued>\d+)$")
        #  6: Last failed upload          :  202510151102_2 
        p6 = re.compile(r"^6: Last failed upload\s*:\s*(?P<last_failed_upload>.*)$")
        #  7: Files failed to upload      :  411 
        p7 = re.compile(r"^7: Files failed to upload\s*:\s*(?P<files_failed_to_upload>\d+)$")
        #  8: Files successfully uploaded :  0 
        p8 = re.compile(r"^8: Files successfully uploaded\s*:\s*(?P<files_successfully_uploaded>\d+)$")
        #  9: Last file created           :  202510151107_2  
        p9 = re.compile(r"^9: Last file created\s*:\s*(?P<last_file_created>.*)$")
        # 10: Time of creation            :  10/15/25 11:07:03 UTC 
        p10 = re.compile(r"^10: Time of creation\s*:\s*(?P<time_of_creation>.*)$")
        # 11: Number of flows in prev file:  64000 
        p11 = re.compile(r"^11: Number of flows in prev file:\s*(?P<number_of_flows_in_prev_file>\d+)$")
        # 12: Number of flows in curr file:  48000
        p12 = re.compile(r"^12: Number of flows in curr file:\s*(?P<number_of_flows_in_curr_file>\d+)$")
        # 13: Invalid dropped flows       :  0
        p13 = re.compile(r"^13: Invalid dropped flows\s*:\s*(?P<invalid_dropped_flows>\d+)$")
        # 14: Error dropped flows         :  0
        p14 = re.compile(r"^14: Error dropped flows\s*:\s*(?P<error_dropped_flows>\d+)$")
        # 15: Is Registered               :  Registered
        p15 = re.compile(r"^15: Is Registered\s*:\s*(?P<is_registered>\w+)$")
        # 16: Delete debug                :  Disabled 
        p16 = re.compile(r"^16: Delete debug\s*:\s*(?P<delete_debug>\w+)$")
        # 17: Exporter delete debug       :  Disabled     
        p17 = re.compile(r"^17: Exporter delete debug\s*:\s*(?P<exporter_delete_debug>\w+)$")
        # 18: Certificate Validation      :  Enabled
        p18 = re.compile(r"^18: Certificate Validation\s*:\s*(?P<certificate_validation>\w+)$")

        for line in output.splitlines():
            line = line.strip()
            #  1: Last file uploaded          :   
            m = p1.match(line)
            if m:
                ret_dict.setdefault("swc_upload_statistics", {})["last_file_uploaded"] = m.group("last_file_uploaded")
                continue
            #  2: Time of upload              :  
            m = p2.match(line)
            if m:
                ret_dict.setdefault("swc_upload_statistics", {})["time_of_upload"] = m.group("time_of_upload")
                continue
            #  3: Current file uploading      :  
            m = p3.match(line)
            if m:
                ret_dict.setdefault("swc_upload_statistics", {})["current_file_uploading"] = m.group("current_file_uploading")
                continue
            #  4: Files queued for upload     :  202510151103_2, 202510151104_3, 202510151105_2, 202510151104_2, 202510151106_2 
            m = p4.match(line)
            if m:
                ret_dict.setdefault("swc_upload_statistics", {})["files_queued_for_upload"] = m.group("files_queued_for_upload")
                continue
            #  5: Number of files queued      :  5
            m = p5.match(line)
            if m:
                ret_dict.setdefault("swc_upload_statistics", {})["number_of_files_queued"] = int(m.group("number_of_files_queued"))
                continue
            #  6: Last failed upload          :  202510151102_2 
            m = p6.match(line)
            if m:
                ret_dict.setdefault("swc_upload_statistics", {})["last_failed_upload"] = m.group("last_failed_upload")
                continue
            #  7: Files failed to upload      :  411
            m = p7.match(line)
            if m:
                ret_dict.setdefault("swc_upload_statistics", {})["files_failed_to_upload"] = int(m.group("files_failed_to_upload"))
                continue
            #  8: Files successfully uploaded :  0 
            m = p8.match(line)
            if m:
                ret_dict.setdefault("swc_upload_statistics", {})["files_successfully_uploaded"] = int(m.group("files_successfully_uploaded"))
                continue
            #  9: Last file created           :  202510151107_2    
            m = p9.match(line)
            if m:
                ret_dict.setdefault("swc_file_creation_statistics", {})["last_file_created"] = m.group("last_file_created")
                continue
            # 10: Time of creation            :  10/15/25 11:07:03 UTC     
            m = p10.match(line)
            if m:
                ret_dict.setdefault("swc_file_creation_statistics", {})["time_of_creation"] = m.group("time_of_creation")
                continue
            # 11: Number of flows in prev file:  64000 
            m = p11.match(line)
            if m:
                ret_dict.setdefault("swc_flow_statistics", {})["number_of_flows_in_prev_file"] = int(m.group("number_of_flows_in_prev_file"))
                continue
            # 12: Number of flows in curr file:  48000
            m = p12.match(line)
            if m:
                ret_dict.setdefault("swc_flow_statistics", {})["number_of_flows_in_curr_file"] = int(m.group("number_of_flows_in_curr_file"))
                continue
            # 13: Invalid dropped flows       :  0
            m = p13.match(line)
            if m:
                ret_dict.setdefault("swc_flow_statistics", {})["invalid_dropped_flows"] = int(m.group("invalid_dropped_flows"))
                continue
            # 14: Error dropped flows         :  0
            m = p14.match(line)
            if m:
                ret_dict.setdefault("swc_flow_statistics", {})["error_dropped_flows"] = int(m.group("error_dropped_flows"))
                continue
            # 15: Is Registered               :  Registered
            m = p15.match(line)
            if m:
                ret_dict.setdefault("swc_flags", {})["is_registered"] = m.group("is_registered")
                continue
            # 16: Delete debug                :  Disabled 
            m = p16.match(line)
            if m:
                ret_dict.setdefault("swc_flags", {})["delete_debug"] = m.group("delete_debug")
                continue
            # 17: Exporter delete debug       :  Disabled     
            m = p17.match(line)
            if m:
                ret_dict.setdefault("swc_flags", {})["exporter_delete_debug"] = m.group("exporter_delete_debug")
                continue
            # 18: Certificate Validation      :  Enabled
            m = p18.match(line)
            if m:
                ret_dict.setdefault("swc_flags", {})["certificate_validation"] = m.group("certificate_validation")
                continue

        return ret_dict

class ShowPlatformSoftwareFedSwitchSecurityFedIpv6sgClearSchema(MetaParser):
    """Schema for show platform software fed switch {switch_var} security-fed ipv6sg clear"""
    schema = {
        'status': str
    }

class ShowPlatformSoftwareFedSwitchSecurityFedIpv6sgClear(ShowPlatformSoftwareFedSwitchSecurityFedIpv6sgClearSchema):
    """Parser for show platform software fed switch {switch_var} security-fed ipv6sg clear"""

    cli_command = ['show platform software fed {switch} {switch_var} security-fed ipv6sg clear',
                   'show platform software fed {switch_var} security-fed ipv6sg clear']

    def cli(self, switch_var, switch=None, output=None):
        if output is None:
            if switch:
                output = self.device.execute(self.cli_command[0].format(switch=switch, switch_var=switch_var))
            else:
                output = self.device.execute(self.cli_command[1].format(switch_var=switch_var))
        
        ret_dict = {}

        # Successfully cleared counter value
        p1 = re.compile(r'^Successfully cleared counter value$')

        for line in output.splitlines():
            line = line.strip()

            # Successfully cleared counter value
            m = p1.match(line)
            if m:
                ret_dict['status'] = 'Successfully cleared counter value'
                continue

        return ret_dict

class ShowPlatformSoftwareFedSwitchSecurityFedIpsgClearSchema(MetaParser):
    """Schema for show platform software fed switch {switch_var} security-fed ipsg clear"""
    schema = {
        'status': str
    }
    
class ShowPlatformSoftwareFedSwitchSecurityFedIpsgClear(ShowPlatformSoftwareFedSwitchSecurityFedIpsgClearSchema):
    """Parser for show platform software fed switch {switch_var} security-fed ipsg clear"""

    cli_command = ['show platform software fed {switch} {switch_var} security-fed ipsg clear',
                   'show platform software fed {switch_var} security-fed ipsg clear']

    def cli(self, switch_var, switch=None, output=None):
        if output is None:
            if switch:
                output = self.device.execute(self.cli_command[0].format(switch=switch, switch_var=switch_var))
            else:
                output = self.device.execute(self.cli_command[1].format(switch_var=switch_var))
        
        ret_dict = {}

        # Successfully cleared counter value
        p1 = re.compile(r'^Successfully cleared counter value$')

        for line in output.splitlines():
            line = line.strip()

            # Successfully cleared counter value
            m = p1.match(line)
            if m:
                ret_dict['status'] = 'Successfully cleared counter value'
                continue

        return ret_dict

class ShowPlatformSoftwareFedSwitchSecurityFedIpv6sgIfIdSchema(MetaParser):
    """Schema for 'show platform software fed switch {switch} security-fed ipv6sg if-id {if-id}'"""
    schema = {
        'ipsg_entries': {
            Any(): {
                'ip': str,
                'prefix': int,
                'handle': str,
                'action': str,
                Optional('ec_state'): str,
                'vlan': int,
                'mac': str,
                'mac_handle': str,
                'counter_oid': str,
                'asic': int,
                'position': int,
                'hit_counter': int
            }
        }
    }

class ShowPlatformSoftwareFedSwitchSecurityFedIpv6sgIfId(ShowPlatformSoftwareFedSwitchSecurityFedIpv6sgIfIdSchema):
    """Parser for 'show platform software fed switch {switch} security-fed ipv6sg if-id {if-id}'"""

    cli_command = ['show platform software fed {switch} {switch_var} security-fed ipv6sg if-id {if_id}',
                   'show platform software fed {switch_var} security-fed ipv6sg if-id {if_id}']

    def cli(self, switch_var, if_id, switch=None, output=None):
        if output is None:
            if switch:
                output = self.device.execute(self.cli_command[0].format(switch=switch, switch_var=switch_var, if_id=if_id))
            else:
                output = self.device.execute(self.cli_command[1].format(switch_var=switch_var, if_id=if_id))
        
        ret_dict = {}

        # fe80::200:ff:fe22:2222                        128   1259 [0x4eb]     Permit      None       200    00:00:00:22:22:22      1259 [0x4eb]
        p1 = re.compile(r'^(?P<ip>[\da-fA-F:.]+)\s+(?P<prefix>\d+)\s+(?P<handle>\d+ \[\S+\])\s+(?P<action>\w+)\s+(?P<ec_state>\w+)\s+(?P<vlan>\d+)\s+(?P<mac>[\da-fA-F:]+)\s+(?P<mac_handle>\d+ \[\S+\])$')
    
        # Counter OID (0xcfd     ) on ASIC (0         )  Position (40015     ) Hit-Counter (16327     )
        p2 = re.compile(r'^Counter\s+OID\s+\(+(?P<counter_oid>\w+)\s+\)\s+on\s+ASIC\s+\((?P<asic>\d+)\s+\)\s+Position\s+\((?P<position>\d+)\s+\)\s+Hit-Counter\s+\((?P<hit_counter>\d+)\s+\)$')

        for line in output.splitlines():
            line = line.strip()

            # fe80::200:ff:fe22:2222                        128   1259 [0x4eb]     Permit      None       200    00:00:00:22:22:22      1259 [0x4eb]
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ipsg_dict=ret_dict.setdefault("ipsg_entries", {}).setdefault(group['ip'], {})
                ipsg_dict['ip'] = group['ip']
                ipsg_dict['prefix'] = int(group['prefix'])
                ipsg_dict['handle'] = group['handle']
                ipsg_dict['action'] = group['action']
                if group['ec_state']!='None':
                    ipsg_dict['ec_state'] = group['ec_state']
                ipsg_dict['vlan'] = int(group['vlan'])
                ipsg_dict['mac'] = group['mac']
                ipsg_dict['mac_handle'] = group['mac_handle']
                continue

            # Counter OID (0xcfd     ) on ASIC (0         )  Position (40015     ) Hit-Counter (16327     )
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ipsg_dict['counter_oid'] = group['counter_oid']
                ipsg_dict['asic'] = int(group['asic'])
                ipsg_dict['position'] = int(group['position'])
                ipsg_dict['hit_counter'] = int(group['hit_counter'])
                continue

        return ret_dict

class ShowPlatformSoftwareFedSwitchSecurityFedIpsgIfIdDetailSchema(MetaParser):
    """Schema for 'show platform software fed switch {switch} security-fed ipsg if-id {if-id} detail'"""
    schema = {
        'ipsg_entries': {
            Any(): {  
                'ip': str,
                'handle': str,
                'type': str,
                'action': str,
                Optional('ec_state'): str,
                'vlan': int,
                Optional('mac'): str,
                Optional('mac_handle'): str,
                'counter_oid': str,
                'asic': int,
                'position': int,
                'hit_counter': int,
            }
        }
    }

class ShowPlatformSoftwareFedSwitchSecurityFedIpsgIfIdDetail(ShowPlatformSoftwareFedSwitchSecurityFedIpsgIfIdDetailSchema):
    """Parser for 'show platform software fed switch {switch} security-fed ipsg if-id {if-id} detail'"""

    cli_command = ['show platform software fed {switch} {switch_var} security-fed ipsg if-id {if_id} detail',
                   'show platform software fed {switch_var} security-fed ipsg if-id {if_id} detail']

    def cli(self, switch_var, if_id, switch=None, output=None):
        if output is None:
            if switch:
                output = self.device.execute(self.cli_command[0].format(switch=switch, switch_var=switch_var, if_id=if_id))
            else:
                output = self.device.execute(self.cli_command[1].format(switch_var=switch_var, if_id=if_id))
        
        ret_dict = {}

        # 0.0.0.0            1259 [0x4eb]     Mac IP      Drop             None                0
        # 100.200.0.4        1259 [0x4eb]     Mac IP      Permit             None                200    00:00:00:22:22:22      1259 [0x4eb]
        p1 = re.compile(r'^(?P<ip>[\d\.]+)\s+(?P<handle>\d+ \[\S+\])\s+(?P<type>[\w ]+)\s+(?P<action>\w+)\s+(?P<ec_state>\w+)\s+(?P<vlan>\d+)(\s+(?P<mac>[\da-fA-F:]+)\s+(?P<mac_handle>\d+ \[\S+\]))?$')

        # Counter OID (0xc58     ) on ASIC (0         )  Position (40015     ) Hit-Counter (16337     )
        p2 = re.compile(r'^Counter\s+OID\s+\(+(?P<counter_oid>\w+)\s+\)\s+on\s+ASIC\s+\((?P<asic>\d+)\s+\)\s+Position\s+\((?P<position>\d+)\s+\)\s+Hit-Counter\s+\((?P<hit_counter>\d+)\s+\)$')

        for line in output.splitlines():
            line = line.strip()

            # 0.0.0.0            1259 [0x4eb]     Mac IP      Drop             None                0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ipsg_dict=ret_dict.setdefault("ipsg_entries", {}).setdefault(group['ip'], {})
                ipsg_dict['ip'] = group['ip']
                ipsg_dict['handle'] = group['handle']
                ipsg_dict['type'] = group['type'].strip()
                ipsg_dict['action'] = group['action']
                if group['ec_state']!='None':
                    ipsg_dict['ec_state'] = group['ec_state']
                ipsg_dict['vlan'] = int(group['vlan'])
                if group.get('mac'):
                    ipsg_dict['mac'] = group['mac']
                if group.get('mac_handle'):
                    ipsg_dict['mac_handle'] = group['mac_handle']
                continue

            # Counter OID (0xc58     ) on ASIC (0         )  Position (40015     ) Hit-Counter (16337     )
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ipsg_dict['counter_oid'] = group['counter_oid']
                ipsg_dict['asic'] = int(group['asic'])
                ipsg_dict['position'] = int(group['position'])
                ipsg_dict['hit_counter'] = int(group['hit_counter'])
                continue

        return ret_dict