"""show_platform_software_fed.py

    * 'show platform software fed switch {switch_var} access-security table usage'

"""
# Python
import re
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use, And, ListOf
from genie.libs.parser.utils.common import Common

log = logging.getLogger(__name__)

class ShowPlatformSoftwareFedSwitchActiveAccessSecurityTableUsageSchema(MetaParser):
    """Schema for 'show platform software fed switch {switch_var} access-security table usage'"""

    schema = {
        'feature': {
            str: {
                'asic': {
                    int: ListOf({
                        'mask': str,
                        'maximum': int,
                        'in_use': int,
                        'total_allocated': int,
                        'total_freed': int
                    })
                }
            }
        }
    }
                                
class ShowPlatformSoftwareFedSwitchActiveAccessSecurityTableUsage(ShowPlatformSoftwareFedSwitchActiveAccessSecurityTableUsageSchema):
    """Parser for 'show platform software fed switch {switch_var} access-security table usage'"""

    cli_command = 'show platform software fed switch {switch_var} access-security table usage'

    def cli(self, switch_var, output=None):
        if output is None:
            cmd = self.cli_command.format(switch_var=switch_var)

        output = self.device.execute(cmd)

        # Initialize parsed dictionary
        ret_dict = {}

        # Dot1x-MAC-Drop    Port-VLAN-MAC       0     4096      0  0       0
        p1 = re.compile(
            r'^(?P<feature>[\w\-]+)\s+(?P<mask>[\w\-]+)\s+(?P<asic>\d+)\s+'
            r'(?P<maximum>\d+)\s+(?P<in_use>\d+)\s+(?P<total_allocated>\d+)\s+'
            r'(?P<total_freed>\d+)$'
        )

        for line in output.splitlines():
            line = line.strip()
            # Dot1x-MAC-Drop    Port-VLAN-MAC       0     4096      0  0       0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                feature_dict = ret_dict.setdefault('feature', {}).setdefault(group['feature'], {})
                asic_dict = feature_dict.setdefault('asic', {}).setdefault(int(group['asic']), [])
                asic_dict.append({
                    'mask': group['mask'],
                    'maximum': int(group['maximum']),
                    'in_use': int(group['in_use']),
                    'total_allocated': int(group['total_allocated']),
                    'total_freed': int(group['total_freed'])
                })

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
                    Any(): ListOf({
                        "protocol": str,
                        "status": str,
                        "cg_id": int,
                        "direction": str,
                    })
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
            if switch:
                if feature_name:
                    cmd = self.cli_command[3].format(switch=switch, switch_var=switch_var,feature_name=feature_name)
                else:
                    cmd = self.cli_command[0].format(switch_var=switch_var,switch=switch)
            else:
                if feature_name:
                    cmd = self.cli_command[2].format(switch_var=switch_var,feature_name=feature_name)
                else:
                    cmd = self.cli_command[1].format(switch_var=switch_var)
            output = self.device.execute(cmd)

        # initial return dictionary
        ret_dict = {}

        # Gi1/0/26.11  Racl          IPv4          Egress      13           Success
        # Gi1/0/25    Racl          IPv4          Ingress     17           Success
        p1 = re.compile(
            r"^(?P<interface>[\w\-\.\/]+)\s+(?P<feature>\w+)\s+(?P<protocol>\w+)?\s+(?P<direction>\w+)\s+(?P<cg_id>\d+)\s+(?P<status>\w+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # Gi1/0/26.11  Racl          IPv4          Egress      13           Success
            # Gi1/0/25    Racl          IPv4          Ingress     17           Success
            m = p1.match(line)
            if m:
                group = m.groupdict()
                feature_dict = ret_dict.setdefault('interface', {}).setdefault(Common.convert_intf_name(group['interface']), {})
                acl_dict = feature_dict.setdefault('feature', {}).setdefault(group['feature'], [])
                acl_dict.append({
                    'cg_id': int(group['cg_id']),
                    'protocol': group['protocol'],
                    'direction': group['direction'],
                    'status': group['status']
                })
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
                            Any(): ListOf({
                                "protocol": str,
                                "cg_id": int,
                                "cg_name": str,
                                "status": str,
                                "src_og_lkup_hdl": int,
                                "dst_og_lkup_hdl": int,
                            }),
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
        p1 = re.compile(r"^Interface Name:\s+(?P<interface>[\w\/\.\-]+)$")

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
                int_dict = ret_dict.setdefault("interface", {}).setdefault(Common.convert_intf_name(group["interface"]), {})
                continue

            # Direction: Egress
            m = p2.match(line)
            if m:
                direction = m.groupdict()["direction"]
                dir_dict = int_dict.setdefault("direction", {}).setdefault(direction, {})
                continue

            # Feature         : Pbr
            m = p3.match(line)
            if m:
                group = m.groupdict()
                direction_list = dir_dict.setdefault("feature", {}).setdefault(group["feature"], [])
                continue

            # Protocol        : IPv4
            m = p4.match(line)
            if m:
                dict_val = m.groupdict()
                direction_list.append({"protocol": dict_val["protocol"]})
                continue

            # CG ID           : 1
            m = p5.match(line)
            if m:
                dict_val = m.groupdict()
                direction_list[-1].update({"cg_id": int(dict_val["cg_id"])})
                continue

            # CG Name         : v4_rmap2
            m = p6.match(line)
            if m:
                dict_val = m.groupdict()
                direction_list[-1].update({"cg_name": dict_val["cg_name"]})
                continue

            # Status          : Success
            m = p7.match(line)
            if m:
                dict_val = m.groupdict()
                direction_list[-1].update({"status": dict_val["status"]})
                continue

            # Src_og_lkup_hdl : 0
            m = p8.match(line)
            if m:
                dict_val = m.groupdict()
                direction_list[-1].update({"src_og_lkup_hdl": int(dict_val["src_og_lkup_hdl"])})
                continue

            # Dst_og_lkup_hdl : 0
            m = p9.match(line)
            if m:
                dict_val = m.groupdict()
                direction_list[-1].update({"dst_og_lkup_hdl": int(dict_val["dst_og_lkup_hdl"])})
                continue

        return ret_dict

class ShowPlatformSoftwareFedSwitchIfmInterfaceNameSchema(MetaParser):
    """Schema for show platform software fed switch {switch} ifm interface_name {interface}"""

    schema = {
        'interface_if_id': str,
        'interface_name': str,
        'interface_block_pointer': str,
        'interface_block_state': str,
        'interface_state': str,
        Optional('interface_admin_mode'): str,
        'interface_status': str,
        'interface_ref_cnt': int,
        'interface_type': {
            str : {
                Optional('port_type'): str,
                Optional('port_location'): str,
                Optional('slot'): int,
                Optional('unit'): int,
                Optional('slot_unit'): int,
                'snmp_if_index': int,
                Optional('gpn'): int,
                Optional('ec_channel'): int,
                Optional('ec_index'): int,
                Optional('mtu'): int,
                Optional('qos_trust_type'): str,
                Optional('vlan_id'): int,
                Optional('ipv4_mtu'): int,
                Optional('ipv6_mtu'): int,
                Optional('ipv4_vrf_id'): str,
                Optional('ipv6_vrf_id'): str,
                Optional('protocol_flags'): str,
                Optional('protocols'): list,
                Optional('misc_flags'): str,
                Optional('misc_flags_list'): list,
                Optional('icmpv4_flags'): str,
                Optional('icmpv4_flags_list'): list,
                Optional('icmpv6_flags'): str,
                Optional('icmpv6_flags_list'): list,
                Optional('mac_address'): str,
            },
        },
        'ref_count': int,
        Optional('feature_reference_count'): str,
        Optional('port_physical_subblock'): {
            'affinity': str,
            'lpn': int,
            'gpn': int,
            'speed': str,
            'type': str,
            'mtu': int,
            'ac_profile': str,
        },
        Optional('port_subblock'): {
            int : {
                Optional('mac_port_oid'): str,
                Optional('mpp_port_oid'): str,
                'system_port_oid': str,
                'system_port_gid': int,
                'ethernet_port_oid': str,
                Optional('port_mode'): str,
                Optional('dense_mode_service_port_gid'): str,
                Optional('dense_mode_service_port_oid'): str,
                Optional('dense_mode_port_vid'): int,
                'voq_oid': str,
            },
        },
        Optional('platform_subblock'): {
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
            'context_id': int,
        },
        Optional('port_l2_subblock'): {
            'l2_port_mode': str,
            'l2_port_mode_set': str,
            'ethertype': int,
            Optional('port_vlan'): int,
            Optional('native_vlan_trunk'): int,
            Optional('untagged_port_bd_vlan_access'): int,
            Optional('default_vlan_dot1q_tunnel'): int,
            Optional('native_vlan_tagging'): str,
            'status': int,
            'ac_profile': str,
        },
        Optional('port_cts_subblock'): {
            'disable_sgacl': str,
            'trust': str,
            'propagate': str,
            'port_sgt': str,
        },
        Optional('events_log'): list,
        Optional('port_cts_subblock_null_if_id'): str,
        Optional('l3_port_tcp_mss_subblock'): {
            'ipv4_tcp_mss_adjust': str,
            'ipv6_tcp_mss_adjust': str,
            'ipv4_maximum_mss_value': int,
            'ipv6_maximum_mss_value': int,
            'acl_asic_oid': {
                int: {
                    'acl_asic_type': list,
                    'acl_oid_asic_id': list,
                },
            },
        },        
        Optional('port_l3_subblock'): {
            'vrf_id': str,
            'ipv4_routing_enabled': str,
            'ipv6_routing_enabled': str,
            'mpls_enabled': str,
            'pimv4_enabled': str,
            'pimv6_enabled': str,
            'ipv4_mtu': int,
            'ipv6_mtu': int,
            'l3_srv_port_gid': int,
            'l3_srv_port_asic_id': {
                int: {
                    'l3_srv_port_oid': str,
                },
            },
        },
    }

class ShowPlatformSoftwareFedSwitchIfmInterfaceName(ShowPlatformSoftwareFedSwitchIfmInterfaceNameSchema):
    """Parser for show platform software fed switch {switch} ifm interface_name {interface}"""

    cli_command = ['show platform software fed {switch} {switch_var} ifm interface_name {interface}',
                    'show platform software fed {switch_var} ifm interface_name {interface}']

    def cli(self, switch=None, switch_var=None, interface=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(switch=switch, switch_var=switch_var, interface=interface)
            else:
                cmd = self.cli_command[1].format(switch_var=switch_var, interface=interface)

            output = self.device.execute(cmd)

        ret_dict = {}

        # Interface IF_ID         : 0x0000000000000441
        p1 = re.compile(r'^Interface IF_ID\s+:\s+(?P<interface_if_id>\S+)$')

        # Interface Name          : FiftyGigE1/1/2
        p2 = re.compile(r'^Interface Name\s+:\s+(?P<interface_name>\S+)$')

        # Interface Block Pointer : 0x71d2ee756398
        p3 = re.compile(r'^Interface Block Pointer\s+:\s+(?P<interface_block_pointer>\S+)$')

        # Interface Block State   : Ready
        p4 = re.compile(r'^Interface Block State\s+:\s+(?P<interface_block_state>\S+)$')

        # Interface State         : Disabled
        p5 = re.compile(r'^Interface State\s+:\s+(?P<interface_state>\S+)$')

        # Interface Admin mode    : Admin Up
        p5_1 = re.compile(r'^Interface Admin mode\s+:\s+(?P<interface_admin_mode>.+)$')

        # Interface Status        : STP-BLOCK-SET
        p6 = re.compile(r'^Interface Status\s+:\s+(?P<interface_status>[\S\s]+)$')

        # Interface Ref-Cnt       : 1
        p7 = re.compile(r'^Interface Ref-Cnt\s+:\s+(?P<interface_ref_cnt>\d+)$')

        # Interface Type          : ETHER
        p8 = re.compile(r'^Interface Type\s+:\s+(?P<interface_type>\S+)$')

        # Port Type         : SWITCH PORT
        p9 = re.compile(r'^Port Type\s+:\s+(?P<port_type>.+)$')

        # Port Location     : LOCAL
        p10 = re.compile(r'^Port Location\s+:\s+(?P<port_location>\S+)$')

        # Slot              : 3
        p11 = re.compile(r'^Slot\s+:\s+(?P<slot>\d+)$')

        # Unit              : 0
        p12 = re.compile(r'^Unit\s+:\s+(?P<unit>\d+)$')

        # Slot Unit         : 58
        p13 = re.compile(r'^Slot Unit\s+:\s+(?P<slot_unit>\d+)$')

        # Vlan id        : 20
        p13_1 = re.compile(r'^Vlan id\s+:\s+(?P<vlan_id>\d+)$')

        # IPv4 MTU       : 1500
        p13_2 = re.compile(r'^IPv4 MTU\s+:\s+(?P<ipv4_mtu>\d+)$')

        # IPv6 MTU       : 1500
        p13_3 = re.compile(r'^IPv6 MTU\s+:\s+(?P<ipv6_mtu>\d+)$')

        # IPv4 VRF ID    : 0x0
        p13_4 = re.compile(r'^IPv4 VRF ID\s+:\s+(?P<ipv4_vrf_id>\S+)$')

        # IPv6 VRF ID    : 0x0
        p13_5 = re.compile(r'^IPv6 VRF ID\s+:\s+(?P<ipv6_vrf_id>\S+)$')

        # Protocol flags : 0x0003 [ ipv4 ipv6 ]
        p13_6 = re.compile(r'^Protocol flags\s+:\s+(?P<protocol_flags>\S+)\s+\[\s*(?P<protocols>[\w\s]+)\s*\]$')

        # Misc flags     : 0x0043 [ ipv4 ipv6 --- ]
        p13_7 = re.compile(r'^Misc flags\s+:\s+(?P<misc_flags>\S+)\s+\[\s*(?P<misc_flags_list>[\w\s\-]+)\s*\]$')

        # ICMPv4 flags   : 0x03 [ unreachable redirect ]
        p13_8 = re.compile(r'^ICMPv4 flags\s+:\s+(?P<icmpv4_flags>\S+)\s+\[\s*(?P<icmpv4_flags_list>[\w\s\-]+)\s*\]$')

        # ICMPv6 flags   : 0x03 [ unreachable redirect ]
        p13_9 = re.compile(r'^ICMPv6 flags\s+:\s+(?P<icmpv6_flags>\S+)\s+\[\s*(?P<icmpv6_flags_list>[\w\s\-]+)\s*\]$')

        # Mac Address    : dc:d8:3b:6a:f1:d6
        p13_10 = re.compile(r'^Mac Address\s+:\s+(?P<mac_address>\S+)$')

        # SNMP IF Index     : 58
        p14 = re.compile(r'^SNMP IF Index\s+:\s+(?P<snmp_if_index>\d+)$')

        # GPN               : 58
        p15 = re.compile(r'^GPN\s+:\s+(?P<gpn>\d+)$')

        # EC Channel        : 0
        p16 = re.compile(r'^EC Channel\s+:\s+(?P<ec_channel>\d+)$')

        # EC Index          : 0
        p17 = re.compile(r'^EC Index\s+:\s+(?P<ec_index>\d+)$')

        # MTU               : 1500
        p18 = re.compile(r'^MTU\s+:\s+(?P<mtu>\d+)$')

        # QoS Trust Type    : 3 (DSCP)
        p19 = re.compile(r'^QoS Trust Type\s+:\s+(?P<qos_trust_type>.+)$')

        # Ref Count : 1 (feature Ref Counts + 1)
        p20 = re.compile(r'^Ref Count\s+:\s+(?P<ref_count>\d+)')

        # No Feature Reference count Present
        p21 = re.compile(r'^(?P<feature_reference_count>\w+)\s+Feature Reference count Present$')

        # Affinity .......... [local]
        p22 = re.compile(r'^Affinity\s+\.+\s+\[(?P<affinity>\w+)\]$')

        # LPN ............... [58]
        p23 = re.compile(r'^LPN\s+\.+\s+\[(?P<lpn>\d+)\]$')

        # GPN ............... [58]
        p24 = re.compile(r'^GPN\s+\.+\s+\[(?P<gpn>\d+)\]$')

        # Speed ............. [10GB]
        # Speed ............. [100GB ]
        p25 = re.compile(r'^Speed\s+\.+\s+\[(?P<speed>\S+)\s*\]$')

        # type .............. [IFM_PORT_TYPE_L2]
        p26 = re.compile(r'^type\s+\.+\s+\[(?P<type>\S+)\]$')

        # MTU ............... [1518]
        p27 = re.compile(r'^MTU\s+\.+\s+\[(?P<mtu>\d+)\]$')

        # ac profile ........ [IFM_AC_PROFILE_L2_DEFAULT]
        p28 = re.compile(r'^ac profile\s+\.+\s+\[(?P<ac_profile>\S+)\]$')

        # Mac port oid................... [0xba8(2984)]
        p29 = re.compile(r'^Mac port oid[\s+]?\.+\s+\[(?P<mac_port_oid>\S+)\]$')

        # Mpp port oid................... [0x761(1889)]
        p29_1 = re.compile(r'^Mpp port oid[\s+]?\.+\s+\[(?P<mpp_port_oid>\S+)\]$')

        # System port oid................ [0xbac(2988)]
        p30 = re.compile(r'^System port oid[\s+]?\.+\s+\[(?P<system_port_oid>\S+)\]$')

        # System port gid................ [100]
        p31 = re.compile(r'^System port gid[\s+]?\.+\s+\[(?P<system_port_gid>\d+)\]$')

        # Ethernet port oid.............. [0xbb2(2994)]
        p32 = re.compile(r'^Ethernet port oid[\s+]?\.+\s+\[(?P<ethernet_port_oid>\S+)\]$')

        # Port mode...................... [Dense Mode]
        p33 = re.compile(r'^Port mode[\s+]?\.+\s+\[(?P<port_mode>.+)\]$')

        # Dense mode service port gid.... [0x1e065(122981)]
        p34 = re.compile(r'^Dense mode service port gid[\s+]?\.+\s+\[(?P<dense_mode_service_port_gid>\S+)\]$')

        # Dense mode service port oid.... [0xbba(3002)]
        p35 = re.compile(r'^Dense mode service port oid[\s+]?\.+\s+\[(?P<dense_mode_service_port_oid>\S+)\]$')

        # Dense mode port vid............ [100]
        p36 = re.compile(r'^Dense mode port vid[\s+]?\.+\s+\[(?P<dense_mode_port_vid>\d+)\]$')

        # Voq oid........................ [0xbaa(2986)]
        p37 = re.compile(r'^Voq oid[\s+]?\.+\s+\[(?P<voq_oid>\S+)\]$')

        # Asic.............. [0]
        p38 = re.compile(r'^Asic[\s+]?\.+\s+\[(?P<asic>\d+)\]$')

        # Core.............. [0]
        p39 = re.compile(r'^Core[\s+]?\.+\s+\[(?P<core>\d+)\]$')

        # Asic Port......... [0]
        p40 = re.compile(r'^Asic Port[\s+]?\.+\s+\[(?P<asic_port>\d+)\]$')

        # Asic Sub Port..... [65535]
        p41 = re.compile(r'^Asic Sub Port[\s+]?\.+\s+\[(?P<asic_sub_port>\d+)\]$')

        # Ifg Id............ [0]
        p42 = re.compile(r'^Ifg Id[\s+]?\.+\s+\[(?P<ifg_id>\d+)\]$')

        # Mac Num........... [58]
        p43 = re.compile(r'^Mac Num[\s+]?\.+\s+\[(?P<mac_num>\d+)\]$')

        # First Serdes...... [41]
        p44 = re.compile(r'^First Serdes[\s+]?\.+\s+\[(?P<first_serdes>\d+)\]$')

        # Last Serdes....... [41]
        p45 = re.compile(r'^Last Serdes[\s+]?\.+\s+\[(?P<last_serdes>\d+)\]$')

        # FC Mode........... [0]
        p46 = re.compile(r'^FC Mode[\s+]?\.+\s+\[(?P<fc_mode>\d+)\]$')

        # FEC Mode.......... [0]
        p47 = re.compile(r'^FEC Mode[\s+]?\.+\s+\[(?P<fec_mode>\d+)\]$')

        # Context Id........ [0]
        p48 = re.compile(r'^Context Id[\s+]?\.+\s+\[(?P<context_id>\d+)\]$')

        # L2 Port Mode ................ [port_mode_access]
        p49 = re.compile(r'^L2 Port Mode\s+\.+\s+\[(?P<l2_port_mode>\S+)\]$')

        # L2 Port Mode set............. [Yes]
        p50 = re.compile(r'^L2 Port Mode set[\s+]?\.+\s+\[(?P<l2_port_mode_set>\S+)\]$')

        # Ethertype.................... [8100]
        p51 = re.compile(r'^Ethertype[\s+]?\.+\s+\[(?P<ethertype>\d+)\]$')

        # Port vlan  .................. [100]
        p52 = re.compile(r'^Port vlan\s+\.+\s+\[(?P<port_vlan>\d+)\]$')

        # Native vlan (trunk) .............. [1]
        p53 = re.compile(r'^Native vlan \(trunk\)\s+\.+\s+\[(?P<native_vlan_trunk>\d+)\]$')

        # Untagged port bd vlan (access) ... [100]
        p54 = re.compile(r'^Untagged port bd vlan \(access\)\s+\.+\s+\[(?P<untagged_port_bd_vlan_access>\d+)\]$')

        # Default vlan (dot1q tunnel) ...... [0]
        p55 = re.compile(r'^Default vlan \(dot1q tunnel\)\s+\.+\s+\[(?P<default_vlan_dot1q_tunnel>\d+)\]$')

        # Native Vlan Tagging.......... [Native Vlan UnTagged]
        p56 = re.compile(r'^Native Vlan Tagging[\s+]?\.+\s+\[(?P<native_vlan_tagging>.+)\]$')

        # status....................... [0]
        p57 = re.compile(r'^status[\s+]?\.+\s+\[(?P<status>\d+)\]$')

        # ac profile .................. [IFM_AC_PROFILE_L2_DEFAULT]
        p58 = re.compile(r'^ac profile\s+\.+\s+\[(?P<ac_profile>\S+)\]$')

        # Disable SGACL .................... [0x0]
        p59 = re.compile(r'^Disable SGACL\s+\.+\s+\[(?P<disable_sgacl>\S+)\]$')

        # Trust ............................ [0x0]
        p60 = re.compile(r'^Trust\s+\.+\s+\[(?P<trust>\S+)\]$')

        # Propagate ........................ [0x0]
        p61 = re.compile(r'^Propagate\s+\.+\s+\[(?P<propagate>\S+)\]$')

        # Port SGT ......................... [0xffff]
        p62 = re.compile(r'^Port SGT\s+\.+\s+\[(?P<port_sgt>\S+)\]$')

        # [2026/02/12 06:41:27.524] Mode None
        p63 = re.compile(r'^\[(?P<timestamp>[\d/: .]+)\]\s+(?P<event>.+)$')

        # Port CTS Subblock is NULL if_id = 0x441
        p64 = re.compile(r'^Port CTS Subblock is NULL if_id = (?P<port_cts_subblock_null_if_id>\S+)$')

        # VRF ID .................. [0]
        p65 = re.compile(r'^VRF ID\s+\.+\s+\[(?P<vrf_id>\S+)\]$')

        # IPv4 Routing Enabled .... [Yes]
        p66 = re.compile(r'^IPv4 Routing Enabled\s+\.+\s+\[(?P<ipv4_routing_enabled>\S+)\]$')

        # IPv6 Routing Enabled .... [Yes]
        p67 = re.compile(r'^IPv6 Routing Enabled\s+\.+\s+\[(?P<ipv6_routing_enabled>\S+)\]$')

        # MPLS Enabled ............ [No]
        p68 = re.compile(r'^MPLS Enabled\s+\.+\s+\[(?P<mpls_enabled>\S+)\]$')

        # Pimv4 Enabled ........... [No]
        p69 = re.compile(r'^Pimv4 Enabled\s+\.+\s+\[(?P<pimv4_enabled>\S+)\]$')

        # Pimv6 Enabled ........... [No]
        p70 = re.compile(r'^Pimv6 Enabled\s+\.+\s+\[(?P<pimv6_enabled>\S+)\]$')

        # IPv4 MTU ................ [1500]
        p71 = re.compile(r'^IPv4 MTU\s+\.+\s+\[(?P<ipv4_mtu>\d+)\]$')
        
        # IPv6 MTU ................ [1500]
        p72 = re.compile(r'^IPv6 MTU\s+\.+\s+\[(?P<ipv6_mtu>\d+)\]$')

        # L3 srv port gid ......... [20]
        p73 = re.compile(r'^L3 srv port gid\s+\.+\s+\[(?P<l3_srv_port_gid>\d+)\]$')

        # L3 srv port oid for Asic[0] ......... [0xa85(2693)]
        p74 = re.compile(r'^L3 srv port oid for Asic\[(?P<l3_srv_port_asic_id>\d+)\]\s+\.+\s+\[(?P<l3_srv_port_oid>\S+)\]$')

        # IPv4 Tcp/Mss Adjust.......... [OFF]
        p75 = re.compile(r'^IPv4 Tcp/Mss Adjust[\s+]?\.+\s+\[(?P<ipv4_tcp_mss_adjust>\S+)\]$')

        # IPv4 Maximum Mss Value..... [0]
        p76 = re.compile(r'^IPv4 Maximum Mss Value[\s+]?\.+\s+\[(?P<ipv4_maximum_mss_value>\d+)\]$')

        # IPv6 Tcp/Mss Adjust.......... [OFF]
        p77 = re.compile(r'^IPv6 Tcp/Mss Adjust[\s+]?\.+\s+\[(?P<ipv6_tcp_mss_adjust>\S+)\]$')

        # IPv6 Maximum Mss Value..... [0]
        p78 = re.compile(r'^IPv6 Maximum Mss Value[\s+]?\.+\s+\[(?P<ipv6_maximum_mss_value>\d+)\]$')

        # ACL_oid Asic[0] [eth:ipv4:ipv6]..... [0(0x0):0(0x0):0(0x0)]
        p79 = re.compile(r'^ACL_oid Asic\[(?P<acl_asic_oid>\d+)\] \[(?P<acl_asic_type>.+)\][\s+]?\.+\s+\[(?P<acl_oid_asic_id>\S+)\]$')

        # Port Subblock [0]
        p80 = re.compile(r'^Port Subblock \[(?P<port_subblock>\d+)\]$')

        events_log = []
        port_physical_subblock_active = False
        port_subblock_active = False
        platform_subblock_active = False
        port_l2_subblock_active = False
        port_cts_subblock_active = False
        port_l3_subblock_active = False
        l3_port_tcp_mss_subblock_active = False

        for line in output.splitlines():
            line = line.strip()

            # Interface IF_ID         : 0x0000000000000441
            m = p1.match(line)
            if m:
                ret_dict['interface_if_id'] = m.group('interface_if_id')
                continue

            # Interface Name          : FiftyGigE1/1/2
            m = p2.match(line)
            if m:
                ret_dict['interface_name'] = m.group('interface_name')
                continue

            # Interface Block Pointer : 0x71d2ee756398
            m = p3.match(line)
            if m:
                ret_dict['interface_block_pointer'] = m.group('interface_block_pointer')
                continue

            # Interface Block State   : Ready
            m = p4.match(line)
            if m:
                ret_dict['interface_block_state'] = m.group('interface_block_state')
                continue

            # Interface State         : Disabled
            m = p5.match(line)
            if m:
                ret_dict['interface_state'] = m.group('interface_state')
                continue

            # Interface Admin mode    : Admin Up
            m = p5_1.match(line)
            if m:
                ret_dict['interface_admin_mode'] = m.group('interface_admin_mode')
                continue

            # Interface Status        : STP-BLOCK-SET
            m = p6.match(line)
            if m:
                ret_dict['interface_status'] = m.group('interface_status').strip()
                continue

            # Interface Ref-Cnt       : 1
            m = p7.match(line)
            if m:
                ret_dict['interface_ref_cnt'] = int(m.group('interface_ref_cnt'))
                continue

            # Interface Type          : ETHER
            m = p8.match(line)
            if m:
                intf_dict = ret_dict.setdefault('interface_type', {}).setdefault(m.group('interface_type'), {}) 
                continue

            # Port Type         : SWITCH PORT
            m = p9.match(line)
            if m:
                intf_dict['port_type'] = m.group('port_type').strip()
                continue

            # Port Location     : LOCAL
            m = p10.match(line)
            if m:
                intf_dict['port_location'] = m.group('port_location')
                continue

            # Slot              : 3
            m = p11.match(line)
            if m:
                intf_dict['slot'] = int(m.group('slot'))
                continue

            # Unit              : 0
            m = p12.match(line)
            if m:
                intf_dict['unit'] = int(m.group('unit'))
                continue

            # Slot Unit         : 58
            m = p13.match(line)
            if m:
                intf_dict['slot_unit'] = int(m.group('slot_unit'))
                continue

            # Vlan id        : 20
            m = p13_1.match(line)
            if m:
                intf_dict['vlan_id'] = int(m.group('vlan_id'))
                continue

            # IPv4 MTU       : 1500
            m = p13_2.match(line)
            if m:
                intf_dict['ipv4_mtu'] = int(m.group('ipv4_mtu'))
                continue

            # IPv6 MTU       : 1500
            m = p13_3.match(line)
            if m:
                intf_dict['ipv6_mtu'] = int(m.group('ipv6_mtu'))
                continue

            # IPv4 VRF ID    : 0x0
            m = p13_4.match(line)
            if m:
                intf_dict['ipv4_vrf_id'] = m.group('ipv4_vrf_id')
                continue

            # IPv6 VRF ID    : 0x0
            m = p13_5.match(line)
            if m:
                intf_dict['ipv6_vrf_id'] = m.group('ipv6_vrf_id')
                continue

            # Protocol flags : 0x0003 [ ipv4 ipv6 ]
            m = p13_6.match(line)
            if m:
                intf_dict['protocol_flags'] = m.group('protocol_flags')
                intf_dict['protocols'] = m.group('protocols').split()
                continue

            # Misc flags     : 0x0043 [ ipv4 ipv6 --- ]
            m = p13_7.match(line)
            if m:
                intf_dict['misc_flags'] = m.group('misc_flags')
                intf_dict['misc_flags_list'] = m.group('misc_flags_list').split()
                continue

            # ICMPv4 flags   : 0x03 [ unreachable redirect ]
            m = p13_8.match(line)
            if m:
                intf_dict['icmpv4_flags'] = m.group('icmpv4_flags')
                intf_dict['icmpv4_flags_list'] = m.group('icmpv4_flags_list').split()
                continue    

            # ICMPv6 flags   : 0x03 [ unreachable redirect ]
            m = p13_9.match(line)
            if m:
                intf_dict['icmpv6_flags'] = m.group('icmpv6_flags')
                intf_dict['icmpv6_flags_list'] = m.group('icmpv6_flags_list').split()
                continue

            # Mac Address    : dc:d8:3b:6a:f1:d6
            m = p13_10.match(line)
            if m:
                intf_dict['mac_address'] = m.group('mac_address')
                continue

            # SNMP IF Index     : 58
            m = p14.match(line)
            if m:
                intf_dict['snmp_if_index'] = int(m.group('snmp_if_index'))
                continue

            # GPN               : 58
            m = p15.match(line)
            if m:
                intf_dict['gpn'] = int(m.group('gpn'))
                continue

            # EC Channel        : 0
            m = p16.match(line)
            if m:
                intf_dict['ec_channel'] = int(m.group('ec_channel'))
                continue

            # EC Index          : 0
            m = p17.match(line)
            if m:
                intf_dict['ec_index'] = int(m.group('ec_index'))
                continue

            # MTU               : 1500
            m = p18.match(line)
            if m:
                intf_dict['mtu'] = int(m.group('mtu'))
                continue

            # QoS Trust Type    : 3 (DSCP)
            m = p19.match(line)
            if m:
                intf_dict['qos_trust_type'] = m.group('qos_trust_type')
                continue

            # Ref Count : 1 (feature Ref Counts + 1)
            m = p20.match(line)
            if m:
                ret_dict['ref_count'] = int(m.group('ref_count'))
                continue

            # No Feature Reference count Present
            m = p21.match(line)
            if m:
                ret_dict['feature_reference_count'] = m.group('feature_reference_count')
                continue

            # Port Physical Subblock
            if 'Port Physical Subblock' in line:
                port_physical_subblock_active = True
                port_subblock_active = False
                platform_subblock_active = False
                port_l2_subblock_active = False
                port_cts_subblock_active = False
                port_l3_subblock_active = False
                l3_port_tcp_mss_subblock_active = False
                ret_dict['port_physical_subblock'] = {}
                continue

            # Port Subblock [0]
            if 'Port Subblock' in line:
                port_subblock_active = True
                port_physical_subblock_active = False
                platform_subblock_active = False
                port_l2_subblock_active = False
                port_cts_subblock_active = False
                port_l3_subblock_active = False
                l3_port_tcp_mss_subblock_active = False
                port_block_dict=ret_dict.setdefault('port_subblock', {}).setdefault(int(p80.match(line).group('port_subblock')), {})
                continue

            # Platform Subblock
            if 'Platform Subblock' in line:
                platform_subblock_active = True
                port_physical_subblock_active = False
                port_subblock_active = False
                port_l2_subblock_active = False
                port_cts_subblock_active = False
                port_l3_subblock_active = False
                l3_port_tcp_mss_subblock_active = False
                ret_dict['platform_subblock'] = {}
                continue

            # Port L2 Subblock
            if 'Port L2 Subblock' in line:
                port_l2_subblock_active = True
                port_physical_subblock_active = False
                port_subblock_active = False
                platform_subblock_active = False
                port_cts_subblock_active = False
                port_l3_subblock_active = False
                l3_port_tcp_mss_subblock_active = False
                ret_dict['port_l2_subblock'] = {}
                continue

            # Port CTS Subblock
            if 'Port CTS Subblock' in line and 'is NULL' not in line:
                port_cts_subblock_active = True
                port_physical_subblock_active = False
                port_subblock_active = False
                platform_subblock_active = False
                port_l2_subblock_active = False
                port_l3_subblock_active = False
                l3_port_tcp_mss_subblock_active = False
                ret_dict['port_cts_subblock'] = {}
                continue

            # Port L3 Subblock
            if 'Port L3 Subblock' in line:
                port_l3_subblock_active = True
                port_physical_subblock_active = False
                port_subblock_active = False
                platform_subblock_active = False
                port_l2_subblock_active = False
                port_cts_subblock_active = False
                l3_port_tcp_mss_subblock_active = False
                ret_dict['port_l3_subblock'] = {}
                continue

            # L3 Port Tcp MSS Subblock
            if 'L3 Port Tcp MSS Subblock' in line:
                l3_port_tcp_mss_subblock_active = True
                port_l3_subblock_active = False
                port_physical_subblock_active = False
                port_subblock_active = False
                platform_subblock_active = False
                port_l2_subblock_active = False
                port_cts_subblock_active = False
                ret_dict['l3_port_tcp_mss_subblock'] = {}
                continue

            # Events Log
            if 'Events Log' in line:
                port_physical_subblock_active = False
                port_l3_subblock_active = False
                l3_port_tcp_mss_subblock_active = False
                port_subblock_active = False
                platform_subblock_active = False
                port_l2_subblock_active = False
                port_cts_subblock_active = False
                continue

            if port_physical_subblock_active:
                # Affinity .......... [local]
                m = p22.match(line)
                if m:
                    ret_dict['port_physical_subblock']['affinity'] = m.group('affinity')
                    continue

                # LPN ............... [58]
                m = p23.match(line)
                if m:
                    ret_dict['port_physical_subblock']['lpn'] = int(m.group('lpn'))
                    continue

                # GPN ............... [58]
                m = p24.match(line)
                if m:
                    ret_dict['port_physical_subblock']['gpn'] = int(m.group('gpn'))
                    continue

                # Speed ............. [10GB]
                m = p25.match(line)
                if m:
                    ret_dict['port_physical_subblock']['speed'] = m.group('speed')
                    continue

                # type .............. [IFM_PORT_TYPE_L2]
                m = p26.match(line)
                if m:
                    ret_dict['port_physical_subblock']['type'] = m.group('type')
                    continue

                # MTU ............... [1518]
                m = p27.match(line)
                if m:
                    ret_dict['port_physical_subblock']['mtu'] = int(m.group('mtu'))
                    continue

                # ac profile ........ [IFM_AC_PROFILE_L2_DEFAULT]
                m = p28.match(line)
                if m:
                    ret_dict['port_physical_subblock']['ac_profile'] = m.group('ac_profile')
                    continue

            if port_subblock_active:
                # Mac port oid................... [0xba8(2984)]
                m = p29.match(line)
                if m:
                    port_block_dict['mac_port_oid'] = m.group('mac_port_oid')
                    continue

                # Mpp port oid................... [0x761(1889)]
                m = p29_1.match(line)
                if m:
                    port_block_dict['mpp_port_oid'] = m.group('mpp_port_oid')
                    continue

                # System port oid................ [0xbac(2988)]
                m = p30.match(line)
                if m:
                    port_block_dict['system_port_oid'] = m.group('system_port_oid')
                    continue

                # System port gid................ [100]
                m = p31.match(line)
                if m:
                    port_block_dict['system_port_gid'] = int(m.group('system_port_gid'))
                    continue

                # Ethernet port oid.............. [0xbb2(2994)]
                m = p32.match(line)
                if m:
                    port_block_dict['ethernet_port_oid'] = m.group('ethernet_port_oid')
                    continue

                # Port mode...................... [Dense Mode]
                m = p33.match(line)
                if m:
                    port_block_dict['port_mode'] = m.group('port_mode')
                    continue

                # Dense mode service port gid.... [0x1e065(122981)]
                m = p34.match(line)
                if m:
                    port_block_dict['dense_mode_service_port_gid'] = m.group('dense_mode_service_port_gid')
                    continue

                # Dense mode service port oid.... [0xbba(3002)]
                m = p35.match(line)
                if m:
                    port_block_dict['dense_mode_service_port_oid'] = m.group('dense_mode_service_port_oid')
                    continue

                # Dense mode port vid............ [100]
                m = p36.match(line)
                if m:
                    port_block_dict['dense_mode_port_vid'] = int(m.group('dense_mode_port_vid'))
                    continue

                # Voq oid........................ [0xbaa(2986)]
                m = p37.match(line)
                if m:
                    port_block_dict['voq_oid'] = m.group('voq_oid')
                    continue

            if platform_subblock_active:
                # Asic.............. [0]
                m = p38.match(line)
                if m:
                    ret_dict['platform_subblock']['asic'] = int(m.group('asic'))
                    continue

                # Core.............. [0]
                m = p39.match(line)
                if m:
                    ret_dict['platform_subblock']['core'] = int(m.group('core'))
                    continue

                # Asic Port......... [0]
                m = p40.match(line)
                if m:
                    ret_dict['platform_subblock']['asic_port'] = int(m.group('asic_port'))
                    continue

                # Asic Sub Port..... [65535]
                m = p41.match(line)
                if m:
                    ret_dict['platform_subblock']['asic_sub_port'] = int(m.group('asic_sub_port'))
                    continue

                # Ifg Id............ [0]
                m = p42.match(line)
                if m:
                    ret_dict['platform_subblock']['ifg_id'] = int(m.group('ifg_id'))
                    continue

                # Mac Num........... [58]
                m = p43.match(line)
                if m:
                    ret_dict['platform_subblock']['mac_num'] = int(m.group('mac_num'))
                    continue

                # First Serdes...... [41]
                m = p44.match(line)
                if m:
                    ret_dict['platform_subblock']['first_serdes'] = int(m.group('first_serdes'))
                    continue

                # Last Serdes....... [41]
                m = p45.match(line)
                if m:
                    ret_dict['platform_subblock']['last_serdes'] = int(m.group('last_serdes'))
                    continue

                # FC Mode........... [0]
                m = p46.match(line)
                if m:
                    ret_dict['platform_subblock']['fc_mode'] = int(m.group('fc_mode'))
                    continue

                # FEC Mode.......... [0]
                m = p47.match(line)
                if m:
                    ret_dict['platform_subblock']['fec_mode'] = int(m.group('fec_mode'))
                    continue

                # Context Id........ [0]
                m = p48.match(line)
                if m:
                    ret_dict['platform_subblock']['context_id'] = int(m.group('context_id'))
                    continue

            if port_l2_subblock_active:
                # L2 Port Mode ................ [port_mode_access]
                m = p49.match(line)
                if m:
                    ret_dict['port_l2_subblock']['l2_port_mode'] = m.group('l2_port_mode')
                    continue

                # L2 Port Mode set............. [Yes]
                m = p50.match(line)
                if m:
                    ret_dict['port_l2_subblock']['l2_port_mode_set'] = m.group('l2_port_mode_set')
                    continue

                # Ethertype.................... [8100]
                m = p51.match(line)
                if m:
                    ret_dict['port_l2_subblock']['ethertype'] = int(m.group('ethertype'))
                    continue

                # Port vlan  .................. [100]
                m = p52.match(line)
                if m:
                    ret_dict['port_l2_subblock']['port_vlan'] = int(m.group('port_vlan'))
                    continue

                # Native vlan (trunk) .............. [1]
                m = p53.match(line)
                if m:
                    ret_dict['port_l2_subblock']['native_vlan_trunk'] = int(m.group('native_vlan_trunk'))
                    continue

                # Untagged port bd vlan (access) ... [100]
                m = p54.match(line)
                if m:
                    ret_dict['port_l2_subblock']['untagged_port_bd_vlan_access'] = int(m.group('untagged_port_bd_vlan_access'))
                    continue

                # Default vlan (dot1q tunnel) ...... [0]
                m = p55.match(line)
                if m:
                    ret_dict['port_l2_subblock']['default_vlan_dot1q_tunnel'] = int(m.group('default_vlan_dot1q_tunnel'))
                    continue

                # Native Vlan Tagging.......... [Native Vlan UnTagged]
                m = p56.match(line)
                if m:
                    ret_dict['port_l2_subblock']['native_vlan_tagging'] = m.group('native_vlan_tagging')
                    continue

                # status....................... [0]
                m = p57.match(line)
                if m:
                    ret_dict['port_l2_subblock']['status'] = int(m.group('status'))
                    continue

                # ac profile .................. [IFM_AC_PROFILE_L2_DEFAULT]
                m = p58.match(line)
                if m:
                    ret_dict['port_l2_subblock']['ac_profile'] = m.group('ac_profile')
                    continue

            if port_cts_subblock_active:
                # Disable SGACL .................... [0x0]
                m = p59.match(line)
                if m:
                    ret_dict['port_cts_subblock']['disable_sgacl'] = m.group('disable_sgacl')
                    continue

                # Trust ............................ [0x0]
                m = p60.match(line)
                if m:
                    ret_dict['port_cts_subblock']['trust'] = m.group('trust')
                    continue

                # Propagate ........................ [0x0]
                m = p61.match(line)
                if m:
                    ret_dict['port_cts_subblock']['propagate'] = m.group('propagate')
                    continue

                # Port SGT ......................... [0xffff]
                m = p62.match(line)
                if m:
                    ret_dict['port_cts_subblock']['port_sgt'] = m.group('port_sgt')
                    continue

            # [2026/02/12 06:41:27.524] Mode None
            m = p63.match(line)
            if m:
                events_log.append({
                    'timestamp': m.group('timestamp'),
                    'event': m.group('event')
                })
                continue

            # Port CTS Subblock is NULL if_id = 0x441
            m = p64.match(line)
            if m:
                ret_dict['port_cts_subblock_null_if_id'] = m.group('port_cts_subblock_null_if_id')
                continue

            if port_l3_subblock_active:
                # VRF ID .................. [0]
                m = p65.match(line)
                if m:
                    ret_dict['port_l3_subblock']['vrf_id'] = m.group('vrf_id')
                    continue

                # IPv4 Routing Enabled .... [Yes]
                m = p66.match(line)
                if m:
                    ret_dict['port_l3_subblock']['ipv4_routing_enabled'] = m.group('ipv4_routing_enabled')
                    continue

                # IPv6 Routing Enabled .... [Yes]
                m = p67.match(line)
                if m:
                    ret_dict['port_l3_subblock']['ipv6_routing_enabled'] = m.group('ipv6_routing_enabled')
                    continue

                # MPLS Enabled ............ [No]
                m = p68.match(line)
                if m:
                    ret_dict['port_l3_subblock']['mpls_enabled'] = m.group('mpls_enabled')
                    continue

                # Pimv4 Enabled ........... [No]
                m = p69.match(line)
                if m:
                    ret_dict['port_l3_subblock']['pimv4_enabled'] = m.group('pimv4_enabled')
                    continue

                # Pimv6 Enabled ........... [No]
                m = p70.match(line)
                if m:
                    ret_dict['port_l3_subblock']['pimv6_enabled'] = m.group('pimv6_enabled')
                    continue

                # IPv4 MTU ................ [1500]
                m = p71.match(line)
                if m:
                    ret_dict['port_l3_subblock']['ipv4_mtu'] = int(m.group('ipv4_mtu'))
                    continue

                # IPv6 MTU ................ [1500]
                m = p72.match(line)
                if m:
                    ret_dict['port_l3_subblock']['ipv6_mtu'] = int(m.group('ipv6_mtu'))
                    continue

                # L3 srv port gid ......... [20]
                m = p73.match(line)
                if m:
                    ret_dict['port_l3_subblock']['l3_srv_port_gid'] = int(m.group('l3_srv_port_gid'))
                    continue

                # L3 srv port oid for Asic[0] ......... [0xa85(2693)]
                m = p74.match(line)
                if m:
                    l3_srv_port_oid_for_asic_dict = ret_dict['port_l3_subblock'].setdefault('l3_srv_port_asic_id', {}).setdefault(int(m.group('l3_srv_port_asic_id')), {})
                    l3_srv_port_oid_for_asic_dict['l3_srv_port_oid'] = m.group('l3_srv_port_oid')
                    continue


            if l3_port_tcp_mss_subblock_active:
                # IPv4 Tcp/Mss Adjust.......... [OFF]
                m = p75.match(line)
                if m:
                    ret_dict['l3_port_tcp_mss_subblock']['ipv4_tcp_mss_adjust'] = m.group('ipv4_tcp_mss_adjust')
                    continue

                # IPv4 Maximum Mss Value..... [0]
                m = p76.match(line)
                if m:
                    ret_dict['l3_port_tcp_mss_subblock']['ipv4_maximum_mss_value'] = int(m.group('ipv4_maximum_mss_value'))
                    continue

                # IPv6 Tcp/Mss Adjust.......... [OFF]
                m = p77.match(line)
                if m:
                    ret_dict['l3_port_tcp_mss_subblock']['ipv6_tcp_mss_adjust'] = m.group('ipv6_tcp_mss_adjust')
                    continue

                # IPv6 Maximum Mss Value..... [0]
                m = p78.match(line)
                if m:
                    ret_dict['l3_port_tcp_mss_subblock']['ipv6_maximum_mss_value'] = int(m.group('ipv6_maximum_mss_value'))
                    continue
                
                # ACL_oid Asic[0] [eth:ipv4:ipv6]..... [0(0x0):0(0x0):0(0x0)]
                m = p79.match(line)
                if m:
                    asic_oid_dict = ret_dict['l3_port_tcp_mss_subblock'].setdefault('acl_asic_oid', {}).setdefault(int(m.group('acl_asic_oid')), {})
                    asic_oid_dict['acl_asic_type'] = m.group('acl_asic_type').split(':')
                    asic_oid_dict['acl_oid_asic_id'] = m.group('acl_oid_asic_id').split(':')
                    continue

        if events_log:
            ret_dict['events_log'] = events_log

        return ret_dict
