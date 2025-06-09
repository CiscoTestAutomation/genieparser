"""show_platform_software_fed_mpls.py

    * 'show platform software fed switch {switch_type} mpls rlist'
    * 'show platform software fed switch active mpls rlist | sect RLIST id:'
    * 'show platform software fed switch active mpls forwarding label {label} detail'
    * 'show platform software fed active mpls forwarding label {label} detail'
    * 'show platform software fed {switchvirtualstate} mpls lspa all | c {mode}'
    * 'show platform software fed {switchvirtualstate} mpls lspa all'
    * 'show platform software fed {switch} active mpls ipv4 vrf-name {vn_name} {ip_add}'
    * 'show platform software fed active mpls ipv4 vrf-name {vn_name} {ip_add}'
    * 'show platform software fed {switchvirtualstate} mpls lspa all | c {mode}'
    * 'show platform software fed {switchvirtualstate} mpls lspa all'
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


# ======================================================================================
# Schema for :
#   * 'show platform software fed {switch} active mpls ipv4 vrf-name {vn_name} {ip_add}'
#   * 'show platform software fed active mpls ipv4 vrf-name {vn_name} {ip_add}'
# ======================================================================================
class ShowPlatformSofwareFedActiveMplsIpv4VrfNameIpAddSchema(MetaParser):

    """Schema for :
    * 'show platform software fed {switch} active mpls ipv4 vrf-name {vn_name} {ip_add}'
    * 'show platform software fed active mpls ipv4 vrf-name {vn_name} {ip_add}'
    """

    schema = {
        "ipv4_add": {
            Any(): {
                "ipv4route_id": str,
                "obj_name": str,
                "obj_id": int,
                "tblid": int,
                "da": int,
                Optional("child"): {
                    Optional("child_adj"): {
                        Optional("objid"): int,
                        Optional("nh_type"): str,
                        Optional("iif_id"): str,
                        Optional("ether_type"): str,
                        Optional("srcmac"): str,
                        Optional("dstmac"): str,
                    },
                    Optional("child_npd"): {
                        Optional("child_device"): int,
                        Optional("nh_gid"): int,
                        Optional("nh_oid"): int,
                        Optional("old_gid"): int,
                        Optional("old_oid"): int,
                        Optional("parent_oid"): int,
                        Optional("child_fec_oid"): int,
                        Optional("was_nor_nh"): int,
                        Optional("cr_def"): int,
                        Optional("stale"): int,
                        Optional("l3port_valid"): int,
                    },
                    Optional("child_sdk"): {
                        Optional("cla_nhtype"): int,
                    },
                },
                Optional("sdk_fec_dest"): {
                    Optional("sdk_oid"): int,
                    Optional("sdk_dev"): int,
                    Optional("dest_type"): str,
                },
                Optional("npd"): {
                    Optional("device"): int,
                    Optional("lspa_rec"): int,
                    Optional("api_type"): str,
                    Optional("sdk_oid"): int,
                    Optional("devid"): int,
                    Optional("asic"): int,
                },
                Optional("sdk"): {
                    Optional("is_host"): int,
                    Optional("l3_dest_id"): str,
                    Optional("l3_dest_name"): str,
                    Optional("vrf_gid"): int,
                    Optional("vrf_oid"): int,
                },
                Optional("object_type"): str,
                Optional("sdk_nexthop"): {
                    Optional("oid"): int,
                    Optional("dev"): int,
                    Optional("gid"): str,
                    Optional("macaddr"): str,
                    Optional("nh_type"): str,
                },
                Optional("sdk_outgoing_port"): {
                    Optional("out_oid"): int,
                    Optional("porttype"): str,
                },
                Optional("forus_destination"): {
                    Any(): {
                        Optional("forus_obj_id"): int,
                    }
                },
                Optional("subnet_present_l3port_oid"): int,
                Optional(Any()): {
                    Optional("ipnexthop_obj_id"): int,
                },
            }
        }
    }


# ======================================================================================
# Parser for:
#   * 'show platform software fed {switch} active mpls ipv4 vrf-name {vn_name} {ip_add}'
#   * 'show platform software fed active mpls ipv4 vrf-name {vn_name} {ip_add}'
# ======================================================================================
class ShowPlatformSofwareFedActiveMplsIpv4VrfNameIpAdd(
    ShowPlatformSofwareFedActiveMplsIpv4VrfNameIpAddSchema
):
    """Parser for
    * 'show platform software fed {switch} active mpls ipv4 vrf-name {vn_name} {ip_add}'
    * 'show platform software fed active mpls ipv4 vrf-name {vn_name} {ip_add}'
    """

    cli_command = [
        "show platform software fed {switch} active mpls ipv4 vrf-name {vn_name} {ip_address}",
        "show platform software fed active mpls ipv4 vrf-name {vn_name} {ip_address}",
    ]

    def cli(self, switch="", vn_name="", ip_address="", output=None):
        if output is None:
            if vn_name and ip_address:
                if switch:
                    output = self.device.execute(
                        self.cli_command[0].format(
                            switch=switch, vn_name=vn_name, ip_address=ip_address
                        )
                    )
                else:
                    output = self.device.execute(
                        self.cli_command[1].format(
                            vn_name=vn_name, ip_address=ip_address
                        )
                    )

        # Init vars
        ret_dict = {}
        ipv4_add_dict = {}

        # IPV4ROUTE_ID:id:0x5b36201d0608 nobj:(PUSH_COUNTER,418) 20.1.1.123/32 tblid:2 DA:0
        p1 = re.compile(
            r"^IPV4ROUTE_ID:id:(?P<ipv4route_id>\w+)(?:\s+)nobj:\((?P<obj_name>\w+)(?:,)"
            r"(?P<obj_id>\d+)\)(?:\s+)(?P<ipv4_add>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})"
            r"(?:\s+)tblid:(?P<tblid>\d+)(?:\s+)DA:(?P<da>\d+)$"
        )

        # NPD: device:0 lspa_rec:0 api_type:route(3)
        p2 = re.compile(
            r"^NPD:\s+device:(?P<device>\d+)(?:\s+)lspa_rec:(?P<lspa_rec>\d+)(?:\s+)api_type:(?P<api_type>\S+)$"
        )

        # NPD: SDK oid 534, devid:0, asic:0
        p3 = re.compile(
            r"^NPD:\sSDK\soid\s(?P<sdk_oid>\d+)(?:,\s+)devid:(?P<devid>\d+)(?:,\s+)asic:(?P<asic>\d+)$"
        )

        # SDK: is_host:0 l3_dest:0x62faa7b0fca0 l3_dest:la_vxlan_next_hop_base(oid=2113) vrf(gid/oid):2/697
        p4 = re.compile(
            r"^SDK:(?:\s+)is_host:(?P<is_host>\d+)(?:\s+)"
            r"l3_dest:(?P<l3_dest_id>\w+)(?:\s+)"
            r"l3_dest:(?P<l3_dest_name>\S+)(?:\s+)"
            r"vrf\(gid\/oid\):(?P<vrf_gid>\d+)\/(?P<vrf_oid>\d+)$"
        )

        # object type: vxlan_next_hop
        p5 = re.compile(r"^object type:\s+(?P<object_type>\w+)$")

        # sdk nexthop oid:1449,dev:0, gid:0xa,macaddr:a0f8.4910.ab57, nh_type:normal(0)
        p6 = re.compile(
            r"^sdk nexthop oid:(?P<oid>\d+),dev:(?P<dev>\d+),\s+gid:(?P<gid>\w+)"
            r",macaddr:(?P<macaddr>([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}),\s+nh_type:(?P<nh_type>\S+)$"
        )

        # sdk outgoing port oid 2143, porttype:svi(104)
        p7 = re.compile(
            r"^sdk outgoing port oid\s+(?P<out_oid>\d+),\s+porttype:(?P<porttype>\S+)$"
        )

        # forus_destination  SPECIAL_IPNEXTHOP_ID:obj_id:0
        p8 = re.compile(
            r"^forus_destination\s+(?P<forus_name>\w+):obj_id:(?P<forus_obj_id>\d+)$"
        )

        # Subnet Present in SDK for L3Port OID:2143
        p9 = re.compile(
            r"^Subnet Present in SDK for L3Port OID:(?P<subnet_present_l3port_oid>\d+)$"
        )

        # SPECIAL_IPNEXTHOP_ID:obj_id:0
        p10 = re.compile(r"^(?P<ipnexthop_name>\w+):obj_id:(?P<ipnexthop_obj_id>\d+)$")

        # sdk fec destination oid:1449,dev:0, destination_type:4b
        p11 = re.compile(
            r"^sdk fec destination oid:(?P<sdk_oid>\d+),dev:(?P<sdk_dev>\d+),\s+destination_type:(?P<dest_type>\S+)$"
        )

        # ADJ:objid:101 nh_type:NHADJ_NORMAL iif_id:0x553 ether_type:0x8 #child:2
        p12 = re.compile(
            r"^ADJ:objid:(?P<objid>\d+)\s+nh_type:(?P<nh_type>\w+)\s+"
            r"iif_id:(?P<iif_id>\w+)\s+ether_type:(?P<ether_type>\w+)\s+#child:\d+$"
        )

        # srcmac:f87a.4125.2f02 dstmac:a0f8.4910.ab57
        p13 = re.compile(
            r"^srcmac:(?P<srcmac>([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4})\s+dstmac:(?P<dstmac>([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4})$"
        )

        # NPD: device:0 nh_gid/oid:10/1449 old_gid/oid:0/0 parent_oid:2143
        p14 = re.compile(
            r"^NPD:\s+device:(?P<child_device>\d+)\s+nh_gid\/oid:(?P<nh_gid>\d+)\/(?P<nh_oid>\d+)\s+"
            r"old_gid\/oid:(?P<old_gid>\d+)\/(?P<old_oid>\d+)\s+parent_oid:(?P<parent_oid>\d+)$"
        )

        # fec_oid:1454 was_nor_nh:1 cr_def:0 stale:0 l3port_valid:1
        p15 = re.compile(
            r"^fec_oid:(?P<child_fec_oid>\d+)\s+was_nor_nh:(?P<was_nor_nh>\d+)\s+cr_def:(?P<cr_def>\d+)"
            r"\s+stale:(?P<stale>\d+)\s+l3port_valid:(?P<l3port_valid>\d+)$"
        )

        # SDK: cla_nhtype:0
        p16 = re.compile(r"^SDK:\s+cla_nhtype:(?P<cla_nhtype>\d+)$")

        for line in output.splitlines():
            line = line.strip()
            # IPV4ROUTE_ID:id:0x5b36201d0608 nobj:(PUSH_COUNTER,418) 20.1.1.123/32 tblid:2 DA:0
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                ipv4_add = m.groupdict()["ipv4_add"]
                ipv4_add_dict = ret_dict.setdefault("ipv4_add", {}).setdefault(
                    ipv4_add, {}
                )
                ipv4_add_dict.update(
                    {
                        "ipv4route_id": str(groups["ipv4route_id"]),
                        "obj_name": str(groups["obj_name"]),
                        "obj_id": int(groups["obj_id"]),
                        "tblid": int(groups["tblid"]),
                        "da": int(groups["da"]),
                    }
                )
                continue

            # NPD: device:0 lspa_rec:0 api_type:route(3)
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                npd_dict = ipv4_add_dict.setdefault("npd", {})
                npd_dict.update(
                    {
                        "device": int(groups["device"]),
                        "lspa_rec": int(groups["lspa_rec"]),
                        "api_type": str(groups["api_type"]),
                    }
                )
                continue

            # NPD: SDK oid 534, devid:0, asic:0
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                npd_dict.update(
                    {
                        "sdk_oid": int(groups["sdk_oid"]),
                        "devid": int(groups["devid"]),
                        "asic": int(groups["asic"]),
                    }
                )
                continue

            # SDK: is_host:0 l3_dest:0x62faa7b0fca0 l3_dest:la_vxlan_next_hop_base(oid=2113) vrf(gid/oid):2/697
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                sdk_dict = ipv4_add_dict.setdefault("sdk", {})
                sdk_dict.update(
                    {
                        "is_host": int(groups["is_host"]),
                        "l3_dest_id": str(groups["l3_dest_id"]),
                        "l3_dest_name": str(groups["l3_dest_name"]),
                        "vrf_gid": int(groups["vrf_gid"]),
                        "vrf_oid": int(groups["vrf_oid"]),
                    }
                )
                continue
            # object type: vxlan_next_hop
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                ipv4_add_dict.update(
                    {
                        "object_type": str(groups["object_type"]),
                    }
                )
                continue

            # sdk nexthop oid:1449,dev:0, gid:0xa,macaddr:a0f8.4910.ab57, nh_type:normal(0)
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                sdk_nexthop_dict = ipv4_add_dict.setdefault("sdk_nexthop", {})
                sdk_nexthop_dict.update(
                    {
                        "oid": int(groups["oid"]),
                        "dev": int(groups["dev"]),
                        "gid": str(groups["gid"]),
                        "macaddr": str(groups["macaddr"]),
                        "nh_type": str(groups["nh_type"]),
                    }
                )
                continue

            # sdk outgoing port oid 2143, porttype:svi(104)
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                sdk_outgoing_port_dict = ipv4_add_dict.setdefault(
                    "sdk_outgoing_port", {}
                )
                sdk_outgoing_port_dict.update(
                    {
                        "out_oid": int(groups["out_oid"]),
                        "porttype": str(groups["porttype"]),
                    }
                )
                continue

            # forus_destination  SPECIAL_IPNEXTHOP_ID:obj_id:0
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                forus_name = m.groupdict()["forus_name"]
                forus_destination_dict = ipv4_add_dict.setdefault(
                    "forus_destination", {}
                )
                forus_name_dict = forus_destination_dict.setdefault(forus_name, {})
                forus_name_dict.update(
                    {
                        "forus_obj_id": int(groups["forus_obj_id"]),
                    }
                )
                continue

            # Subnet Present in SDK for L3Port OID:2143
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                ipv4_add_dict.update(
                    {
                        "subnet_present_l3port_oid": int(
                            groups["subnet_present_l3port_oid"]
                        ),
                    }
                )
                continue

            # SPECIAL_IPNEXTHOP_ID:obj_id:0
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                ipnexthop_name = m.groupdict()["ipnexthop_name"]
                ipnexthop_name_dict = ipv4_add_dict.setdefault(ipnexthop_name, {})
                ipnexthop_name_dict.update(
                    {
                        "ipnexthop_obj_id": int(groups["ipnexthop_obj_id"]),
                    }
                )
                continue

            # sdk fec destination oid:1449,dev:0, destination_type:4b
            m = p11.match(line)
            if m:
                sdk_fec_dest = m.groupdict()
                sdk_fec_dest_dict = ipv4_add_dict.setdefault("sdk_fec_dest", {})
                sdk_fec_dest_dict.update(
                    {
                        "sdk_oid": int(sdk_fec_dest["sdk_oid"]),
                        "sdk_dev": int(sdk_fec_dest["sdk_dev"]),
                        "dest_type": str(sdk_fec_dest["dest_type"]),
                    }
                )
                continue

            # ADJ:objid:101 nh_type:NHADJ_NORMAL iif_id:0x553 ether_type:0x8 #child:2
            m = p12.match(line)
            if m:
                child_adj = m.groupdict()
                ipv4_add_dict.setdefault("child", {}).setdefault("child_adj", {})
                child_adj_dict = ipv4_add_dict.setdefault("child", {}).setdefault(
                    "child_adj", {}
                )
                child_adj_dict.update(
                    {
                        "objid": int(child_adj["objid"]),
                        "nh_type": str(child_adj["nh_type"]),
                        "iif_id": str(child_adj["iif_id"]),
                        "ether_type": str(child_adj["ether_type"]),
                    }
                )
                continue

            # srcmac:f87a.4125.2f02 dstmac:a0f8.4910.ab57
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                child_adj_dict.update(
                    {
                        "srcmac": str(groups["srcmac"]),
                        "dstmac": str(groups["dstmac"]),
                    }
                )
                continue

            # NPD: device:0 nh_gid/oid:10/1449 old_gid/oid:0/0 parent_oid:2143
            m = p14.match(line)
            if m:
                child_npd = m.groupdict()
                child_npd_dict = ipv4_add_dict.setdefault("child", {}).setdefault(
                    "child_npd", {}
                )
                child_npd_dict.update(
                    {
                        "child_device": int(child_npd["child_device"]),
                        "nh_gid": int(child_npd["nh_gid"]),
                        "nh_oid": int(child_npd["nh_oid"]),
                        "old_gid": int(child_npd["old_gid"]),
                        "old_oid": int(child_npd["old_oid"]),
                        "parent_oid": int(child_npd["parent_oid"]),
                    }
                )
                continue

            # fec_oid:1454 was_nor_nh:1 cr_def:0 stale:0 l3port_valid:1
            m = p15.match(line)
            if m:
                child_npd = m.groupdict()
                child_npd_dict.update(
                    {
                        "child_fec_oid": int(child_npd["child_fec_oid"]),
                        "was_nor_nh": int(child_npd["was_nor_nh"]),
                        "cr_def": int(child_npd["cr_def"]),
                        "stale": int(child_npd["stale"]),
                        "l3port_valid": int(child_npd["l3port_valid"]),
                    }
                )
                continue

            # SDK: cla_nhtype:0
            m = p16.match(line)
            if m:
                child_sdk = m.groupdict()
                child_sdk_dict = ipv4_add_dict.setdefault("child", {}).setdefault(
                    "child_sdk", {}
                )
                child_sdk_dict.update(
                    {
                        "cla_nhtype": int(child_sdk["cla_nhtype"]),
                    }
                )
                continue

        return ret_dict


class showPlatformMplsRlistIdSchema(MetaParser):
    """
    Schema for show environment status
    """

    schema = {
        "rlist_id": {
            Any(): {
                "state": int,
                "status": str,
                "flags": str,
                "remote_ifs": int,
                "packets": int,
                "pps": int,
            },
        },
    }


class ShowPlatformMplsRlistId(showPlatformMplsRlistIdSchema):
    """Parser for:
    show platform software fed switch <switch_type> mpls rlist | in RLIST id:
    """

    cli_command = (
        "show platform software fed switch {switch_type} mpls rlist | in RLIST id:"
    )

    def cli(self, switch_type="", output=None):
        if output is None:
            output = self.device.execute(
                self.cli_command.format(switch_type=switch_type)
            )

        ret_dict = {}

        ###RLIST id: 0xf0001aeb State: 1 {OK} Flags: 0x0 remote_ifs: 0 packets: 0 (0 pps approx.)
        p1 = re.compile(
            r"^RLIST\s+id:\s+(?P<rlist_id>\S+)\s+State:\s+(?P<state>\d+)\s+\{(?P<status>\S+)\}\s+Flags:\s+(?P<flags>\S+)\s+[A-Z\{\} ]*\s*remote_ifs:\s+(?P<remote_ifs>\d+)\s+packets:\s+(?P<packets>\d+)\s+\((?P<pps>\d+).*$"
        )

        for line in output.splitlines():
            line = line.strip()

            ##RLIST id: 0xf0001aeb State: 1 {OK} Flags: 0x0 remote_ifs: 0 packets: 0 (0 pps approx.)
            m1 = p1.match(line)
            if m1:
                r = m1.groupdict()
                res = ret_dict.setdefault("rlist_id", {}).setdefault(r["rlist_id"], {})
                r.pop("rlist_id")
                for key, value in r.items():
                    res[key] = int(value) if value.isdigit() else value
        return ret_dict


class ShowPlatformMplsRlistSummarySchema(MetaParser):
    """
    Schema for show platform software fed switch <switch_type> mpls rlist summary
    """

    schema = {
        "mpls_rlist_summary": {
            "current_count": {"rlist": int, "rentry": int},
            "maximum_reached": {"rlist": int, "rentry": int},
            "total_retry_count": {"rlist": int, "rentry": int},
            "current_lspvif_adj_count": int,
            "max_lspvif_adj": int,
            "current_lspvif_adj_label_count": int,
            "max_lspvif_adj_label_info": int,
            "total_lspvif_adj_label_count": int,
        },
    }


class ShowPlatformMplsRlistSummary(ShowPlatformMplsRlistSummarySchema):
    """Parser for:
    show platform software fed switch <switch_type> mpls rlist
    """

    cli_command = "show platform software fed switch {switch_type} mpls rlist summary"

    def cli(self, switch_type, output=None):
        if output is None:
            output = self.device.execute(
                self.cli_command.format(switch_type=switch_type)
            )

        # Current Count (RLIST/RENTRY) : 4 / 2
        p1 = re.compile(
            r"Current\s+Count\s+\(RLIST\/RENTRY\)\s+\:\s+(?P<rlist>\d+)\s+\/\s+(?P<rentry>\d+)"
        )

        # Maximum Reached (RLIST/RENTRY) : 24 / 48
        p2 = re.compile(
            r"Maximum\s+Reached\s+\(RLIST\/RENTRY\)\s+\:\s+(?P<rlist>\d+)\s+\/\s+(?P<rentry>\d+)"
        )

        # Total Retry Count (RLIST/RENTRY) : 0 / 0
        p3 = re.compile(
            r"Total\s+Retry\s+Count\s+\(RLIST\/RENTRY\)\s+\:\s+(?P<rlist>\d+)\s+\/\s+(?P<rentry>\d+)"
        )

        # Current Lspvif Adjacency's Count : 5
        p4 = re.compile(
            r"Current\s+Lspvif\s+Adjacency's\s+Count\s+\:\s+(?P<current_lspvif_adj_count>\d+)"
        )

        # Max reached Lspvif Adjacency's : 40
        p5 = re.compile(
            r"Max\s+reached\s+Lspvif\s+Adjacency's\s+\:\s+(?P<max_lspvif_adj>\d+)"
        )

        # Current Lspvif Adj label info Count : 1
        p6 = re.compile(
            r"Current\s+Lspvif\s+Adj\s+label\s+info\s+Count\s+\:\s+(?P<current_lspvif_adj_label_count>\d+)"
        )

        # Max reached Lspvif Adj label info : 11
        p7 = re.compile(
            r"Max\s+reached\s+Lspvif\s+Adj\s+label\s+info\s+\:\s+(?P<max_lspvif_adj_label_info>\d+)"
        )

        # Total Retry Lspvif Adj label info Count : 0
        p8 = re.compile(
            r"Total\s+Retry\s+Lspvif\s+Adj\s+label\s+info\s+Count\s+\:\s+(?P<total_lspvif_adj_label_count>\d+)"
        )

        mpls_rlist_summary = dict()
        for line in output.splitlines():
            line = line.strip()

            # Current Count (RLIST/RENTRY) : 4 / 2
            m = p1.match(line)
            if m:
                mpls_rlist_summary_dict = mpls_rlist_summary.setdefault(
                    "mpls_rlist_summary", {}
                )
                current_count_dict = mpls_rlist_summary_dict.setdefault(
                    "current_count", {}
                )
                for item, value in m.groupdict().items():
                    current_count_dict.update({item: int(value)})

            # Maximum Reached (RLIST/RENTRY) : 24 / 48
            m = p2.match(line)
            if m:
                max_reached_dict = mpls_rlist_summary_dict.setdefault(
                    "maximum_reached", {}
                )
                for item, value in m.groupdict().items():
                    max_reached_dict.update({item: int(value)})

            # Total Retry Count (RLIST/RENTRY) : 0 / 0
            m = p3.match(line)
            if m:
                total_retry_count_dict = mpls_rlist_summary_dict.setdefault(
                    "total_retry_count", {}
                )
                for item, value in m.groupdict().items():
                    total_retry_count_dict.update({item: int(value)})

            # Current Lspvif Adjacency's Count : 5
            m = p4.match(line)
            if m:
                mpls_rlist_summary_dict.update(
                    {
                        "current_lspvif_adj_count": int(
                            m.groupdict()["current_lspvif_adj_count"]
                        )
                    }
                )

            # Max reached Lspvif Adjacency's : 40
            m = p5.match(line)
            if m:
                mpls_rlist_summary_dict.update(
                    {"max_lspvif_adj": int(m.groupdict()["max_lspvif_adj"])}
                )

            # Current Lspvif Adj label info Count : 1
            m = p6.match(line)
            if m:
                mpls_rlist_summary_dict.update(
                    {
                        "current_lspvif_adj_label_count": int(
                            m.groupdict()["current_lspvif_adj_label_count"]
                        )
                    }
                )

            # Max reached Lspvif Adj label info : 11
            m = p7.match(line)
            if m:
                mpls_rlist_summary_dict.update(
                    {
                        "max_lspvif_adj_label_info": int(
                            m.groupdict()["max_lspvif_adj_label_info"]
                        )
                    }
                )

            # Total Retry Lspvif Adj label info Count : 0
            m = p8.match(line)
            if m:
                mpls_rlist_summary_dict.update(
                    {
                        "total_lspvif_adj_label_count": int(
                            m.groupdict()["total_lspvif_adj_label_count"]
                        )
                    }
                )

        return mpls_rlist_summary


# =============================================
# Schema for 'show platform software fed switch active mpls forwarding label <label> detail'
# Schema for 'show platform software fed active mpls forwarding label <label> detail'
# =============================================
class ShowPlatformSoftwareFedSchema(MetaParser):
    """Schema for:
    *show platform software fed {switch} active mpls forwarding label {label} detail
    *show platform software fed active mpls forwarding label {label} detail
    """

    schema = {
        "lentry_label": {
            Any(): {
                "nobj": list,
                "lentry_hdl": str,
                "modify_cnt": int,
                "backwalk_cnt": int,
                "lspa_handle": str,
                "aal": {
                    "id": int,
                    "lbl": int,
                    "eos0": {
                        "adj_hdl": str,
                        "hw_hdl": str,
                    },
                    "eos1": {
                        "adj_hdl": str,
                        "hw_hdl": str,
                    },
                    "deagg_vrf_id": int,
                    "lspa_handle": str,
                },
                Optional("eos"): {
                    "objid": int,
                    "local_label": int,
                    "flags": str,
                    "pdflags": str,
                    "nobj0": list,
                    "nobj1": list,
                    "modify": int,
                    "bwalk": int,
                },
                Optional("label"): {
                    Any(): {
                        "link_type": str,
                        "local_label": int,
                        "outlabel": str,
                        "flags": {
                            Any(): list,
                        },
                        "pdflags": {
                            Any(): list,
                        },
                        "adj_handle": str,
                        "unsupported_recursion": int,
                        "olbl_changed": int,
                        "local_adj": int,
                        "modify_cnt": int,
                        "bwalk_cnt": int,
                        "subwalk_cnt": int,
                        "collapsed_oce": int,
                        Optional("label_aal"): {
                            Any(): {
                                "lbl": int,
                                "smac": str,
                                "dmac": str,
                                "sub_type": int,
                                "link_type": int,
                                "adj_flags": str,
                                "label_type": int,
                                "rewrite_type": str,
                                "vlan_id": int,
                                "vrf_id": int,
                                "ri": str,
                                "ri_id": str,
                                "phdl": str,
                                "ref_cnt": int,
                                "si": str,
                                "si_id": str,
                                "di_id": str,
                            },
                        },
                    },
                },
                Optional("adj"): {
                    Any(): {
                        "link_type": str,
                        "ifnum": str,
                        "adj": str,
                        "si": str,
                        Optional("IPv4"): str,
                    },
                },
                Optional("objid"): {
                    Any(): {
                        "SPECIAL": str,
                    },
                },
                Optional("lb"): {
                    Any(): {
                        "ecr_map_objid": int,
                        "link_type": str,
                        "num_choices": int,
                        "flags": str,
                        "mpls_ecr": int,
                        "local_label": int,
                        "path_inhw": int,
                        "ecrh": str,
                        "old_ecrh": str,
                        "modify_cnt": int,
                        "bwalk_cnt": int,
                        "subwalk_cnt": int,
                        "finish_cnt": int,
                        Optional("bwalk"): {
                            "req": int,
                            "in_prog": int,
                            "nested": int,
                        },
                        Optional("aal"): {
                            "ecr_id": int,
                            "af": int,
                            "ecr_type": str,
                            "ref": int,
                            "ecrh": str,
                            "hwhdl": str,
                        },
                    },
                },
                Optional("sw_enh_ecr_scale"): {
                    Any(): {
                        "llabel": int,
                        "eos": int,
                        "adjs": int,
                        "mixed_adj": str,
                        "reprogram_hw": str,
                        "ecrhdl": str,
                        "ecr_hwhdl": str,
                        "mod_cnt": int,
                        "prev_npath": int,
                        "pmismatch": int,
                        "pordermatch": int,
                        Optional("ecr_adj"): {
                            Any(): {
                                Optional("is_mpls_adj"): int,
                                Optional("l3adj_flags"): str,
                                Optional("recirc_adj_id"): int,
                                "sih": str,
                                "di_id": int,
                                "rih": str,
                                Optional("adj_lentry"): str,
                            },
                        },
                    },
                },
            }
        }
    }


# ================================================================
# Parser for:
#   * 'show platform software fed '
# ================================================================
class ShowPlatformSoftwareFed(ShowPlatformSoftwareFedSchema):
    """Parser for:
    ' show platform software fed {switch} active mpls forwarding label {label} detail'
    ' show platform software fed active mpls forwarding label {label} detail '
    """

    cli_command = [
        "show platform software fed active mpls forwarding label {label} detail",
        "show platform software fed {switch} active mpls forwarding label {label} detail",
    ]

    def cli(self, label="", switch="", output=None):
        """cli for:
        ' show platform software fed {switch} active mpls forwarding label {label} detail '
        ' show platform software fed active mpls forwarding label {label} detail '
        """
        if output is None:
            # Build command
            if not switch:
                cmd = self.cli_command[0].format(label=label)
            else:
                cmd = self.cli_command[1].format(switch=switch, label=label)
            # Execute command
            out = self.device.execute(cmd)
        else:
            out = output

        # LENTRY:label:22 nobj:(EOS, 142) lentry_hdl:0xde00000a
        p1 = re.compile(
            r"^LENTRY:label:+(?P<label>\d+)\s+nobj:\(+"
            r"(?P<nobj>[\w\, ]+)+\)\s+lentry_hdl:+(?P<lentry_hdl>\S+)$"
        )

        # modify_cnt:1 backwalk_cnt:2
        p2 = re.compile(
            r"^modify_cnt:+(?P<modify_cnt>\d+)\s+"
            r"backwalk_cnt:+(?P<backwalk_cnt>\d+)$"
        )

        # lspa_handle:0
        p3 = re.compile(r"^lspa_handle:+(?P<lspa_handle>\w+)$")

        # AAL: id:3724541962 lbl:22
        p4 = re.compile(r"^AAL:\s+id:+(?P<id>\d+)\s+lbl:+(?P<lbl>\d+)$")

        # eos0:[adj_hdl:0x83000039, hw_hdl:0x7f02737c6628]
        p5 = re.compile(
            r"^eos0:\[+adj_hdl:+(?P<adj_hdl>\w+)+,\s+hw_hdl:+(?P<hw_hdl>\w+)+\]+$"
        )

        # eos1:[adj_hdl:0x3d000038, hw_hdl:0x7f02737c6478]
        p6 = re.compile(
            r"^eos1:\[+adj_hdl:+(?P<adj_hdl>\w+)+,\s+hw_hdl:+" r"(?P<hw_hdl>\w+)+\]+$"
        )

        # deagg_vrf_id = 0 lspa_handle:0
        p7 = re.compile(
            r"^deagg_vrf_id\s+=\s+(?P<deagg_vrf_id>\d+)+\s+lspa_handle:+"
            r"(?P<lspa_handle>\w+)+$"
        )

        # EOS:objid:142 local_label:0 flags:0:() pdflags:0
        p8 = re.compile(
            r"^EOS:+objid:+(?P<objid>\d+)\s+local_label:+"
            r"(?P<local_label>\d+)\s+flags:+\S:+"
            r"(?P<flags>[\S\s]+)\s+pdflags:+"
            r"(?P<pdflags>\S+)$"
        )

        # nobj0:(LABEL, 143), nobj1:(LABEL, 141) modify:1 bwalk:0
        p9 = re.compile(
            r"^nobj0:\(+(?P<nobj0>[\w\,\s]+)+\)+\,\s+nobj1:\(+"
            r"(?P<nobj1>[\w\,\s]+)+\)\s+modify:+(?P<modify>\d+)\s+bwalk:+(?P<bwalk>\d+)$"
        )

        # LABEL:objid:143 link_type:MPLS local_label:22 outlabel:(3, 0)
        p10 = re.compile(
            r"LABEL:+objid:+(?P<objid>\d+)\s+link_type:+"
            r"(?P<link_type>\w+)\s+local_label:+"
            r"(?P<local_label>\d+)\s+outlabel:+(?P<outlabel>[\S\s]+)$"
        )

        # flags:0x18:(POP,PHP,) pdflags:0:(INSTALL_HW_OK,) adj_handle:0x83000039
        p11 = re.compile(
            r"flags:+(?P<flagid>\w+)+:\(+(?P<flagstr>\S+)+\,+\)+\s+pdflags:+"
            r"(?P<pdflagid>\w+)+:\(+(?P<pdflagstr>\S+)+\,+\)+\s+adj_handle:+(?P<adj_handle>\w+)$"
        )

        # unsupported recursion:0 olbl_changed 0 local_adj:0 modify_cnt:0
        p12 = re.compile(
            r"^unsupported\s+recursion:+(?P<unsupported_recursion>\d+)\s+olbl_changed\s+"
            r"(?P<olbl_changed>\d+)\s+local_adj:+"
            r"(?P<local_adj>\d+)\s+modify_cnt:+(?P<modify_cnt>\d+)$"
        )

        # bwalk_cnt:0 subwalk_cnt:0 collapsed_oce:0
        p13 = re.compile(
            r"^bwalk_cnt:+(?P<bwalk_cnt>\d+)\s+subwalk_cnt:+"
            r"(?P<subwalk_cnt>\d+)\s+collapsed_oce:+(?P<collapsed_oce>\d+)$"
        )

        # AAL: id:2197815353 lbl:0 smac:00a7.42d6.c41f dmac:0027.90bf.2ee7
        p14 = re.compile(
            r"^AAL:\s+id:+(?P<id>\d+)\s+lbl:+(?P<lbl>\d+)\s+smac:+"
            r"(?P<smac>\S+)\s+dmac:+(?P<dmac>\S+)$"
        )

        # sub_type:0 link_type:2 adj_flags:0 label_type:1 rewrite_type:POP2MPLS(138)
        p15 = re.compile(
            r"^sub_type:+(?P<sub_type>\d+)\s+link_type:+"
            r"(?P<link_type>\d+)\s+adj_flags:+(?P<adj_flags>\w+)\s+label_type:+"
            r"(?P<label_type>\d+)\s+rewrite_type:+(?P<rewrite_type>\S+)$"
        )

        # vlan_id:0 vrf_id:0 ri:0x7f02737cc1e8, ri_id:0x3e phdl:0xab000447, ref_cnt:1
        p16 = re.compile(
            r"^vlan_id:+(?P<vlan_id>\d+)\s+vrf_id:+(?P<vrf_id>\d+)\s+ri:+"
            r"(?P<ri>\w+)+,\s+ri_id:+(?P<ri_id>\w+)\s+phdl:+"
            r"(?P<phdl>\w+)+,\s+ref_cnt:+(?P<ref_cnt>\d+)$"
        )

        # si:0x7f02737cc6b8, si_id:0x4027, di_id:0x526d
        p17 = re.compile(
            r"^si:+(?P<si>\w+)+,\s+si_id:+(?P<si_id>\w+)+,\s+di_id:+(?P<di_id>\w+)$"
        )

        # ADJ:objid:139 {link_type:MPLS ifnum:0x36, adj:0x5c000037, si: 0x7f02737a2348  }
        p18 = re.compile(
            r"ADJ:objid:+(?P<objid>\d+) +{link_type:(?P<link_type>\w+) +ifnum:(?P<ifnum>\w+), +adj:(?P<adj>\w+), +si: +(?P<si>\w+) +}$"
        )

        # ADJ:objid:137 {link_type:IP ifnum:0x36, adj:0x63000036, si: 0x7f02737a2348  IPv4:     172.16.25.2 }
        p19 = re.compile(
            r"ADJ:objid:+(?P<objid>\d+) +{link_type:(?P<link_type>\w+) +ifnum:(?P<ifnum>\w+), +adj:(?P<adj>\w+), +si: +(?P<si>\w+) +IPv4: +(?P<IPv4>[\d\.]+) +}$"
        )

        # LENTRY:label:75 not found...
        p20 = re.compile(r"^LENTRY:label:+(?P<label>\d+)\snot +found\S+$")

        # AAL: Handle not found:0
        p21 = re.compile(r"^AAL:\s+Handle\ not\ found:\S$")

        # LB:obj_id:38 ecr_map_objid:0 link_type:IP num_choices:2 Flags:0
        p22 = re.compile(
            r"LB:+obj_id:+(?P<obj_id>\d+)\s+ecr_map_objid:+"
            r"(?P<ecr_map_objid>\d+)\s+link_type:+"
            r"(?P<link_type>\w+)\s+num_choices:+"
            r"(?P<num_choices>\d+)\s+Flags:+(?P<flags>\w+)$"
        )

        # mpls_ecr:1 local_label:24 path_inhw:2 ecrh:0xf9000002 old_ecrh:0
        p23 = re.compile(
            r"mpls_ecr:+(?P<mpls_ecr>\d+)\s+local_label:+"
            r"(?P<local_label>\d+)\s+path_inhw:+"
            r"(?P<path_inhw>\d+)\s+ecrh:+"
            r"(?P<ecrh>\w+)\s+old_ecrh:+(?P<old_ecrh>\w+)$"
        )

        # modify_cnt:0 bwalk_cnt:0 subwalk_cnt:0 finish_cnt:0
        p24 = re.compile(
            r"modify_cnt:+(?P<modify_cnt>\d+)\s+bwalk_cnt:+"
            r"(?P<bwalk_cnt>\d+)\s+subwalk_cnt:+"
            r"(?P<subwalk_cnt>\d+)\s+finish_cnt:+" + r"(?P<finish_cnt>\d+)$"
        )

        # bwalk:[req:0 in_prog:0 nested:0]
        p25 = re.compile(
            r"bwalk:\[+req:+(?P<req>\d+)\s+in_prog:+"
            r"(?P<in_prog>\d+)\s+nested:+(?P<nested>\d+)+\]+$"
        )

        # AAL: ecr:id:4177526786 af:0 ecr_type:0 ref:3 ecrh:0x7f02737e49f8(28:2)
        p26 = re.compile(
            r"AAL:\s+ecr:id:+(?P<ecr_id>\d+)\s+af:(?P<af>\d+)\s+ecr_type:+"
            r"(?P<ecr_type>\w+)\s+ref:+(?P<ref>\d+)\s+ecrh:+(?P<ecrh>\S+)+$"
        )

        # hwhdl:1937656312 ::0x7f02737e11c8,0x7f02737e2728,0x7f02737e11c8,0x7f02737e2728
        p27 = re.compile(r"hwhdl+(?P<hwhdl>[\S\s]+)$")

        # Sw Enh ECR scale: objid:38 llabel:24 eos:1 #adjs:2 mixed_adj:0
        p28 = re.compile(
            r"Sw +Enh +ECR +scale:\s+objid:+(?P<objid>\d+)\s+llabel:+"
            r"(?P<llabel>\d+)\s+eos:+(?P<eos>\d+)\s+\#adjs:+"
            r"(?P<adjs>\d+)\s+mixed_adj:+(?P<mixed_adj>\w+)$"
        )

        # reprogram_hw:0 ecrhdl:0xf9000002 ecr_hwhdl:0x7f02737e49f8
        p29 = re.compile(
            r"reprogram_hw:+(?P<reprogram_hw>\w+)\s+ecrhdl:+"
            r"(?P<ecrhdl>\w+)\s+ecr_hwhdl:+(?P<ecr_hwhdl>\w+)$"
        )

        # mod_cnt:0 prev_npath:0 pmismatch:0 pordermatch:0
        p30 = re.compile(
            r"mod_cnt:+(?P<mod_cnt>\d+)\s+prev_npath:+"
            r"(?P<prev_npath>\d+)\s+pmismatch:+(?P<pmismatch>\d+)\s+pordermatch:+"
            r"(?P<pordermatch>\d+)$"
        )

        # ecr_adj: id:1644167265 is_mpls_adj:1 l3adj_flags:0x100000
        p31 = re.compile(
            r"(?P<ecr_adj>\S+):\s+id:+(?P<id>\d+)\s+is_mpls_adj:+"
            r"(?P<is_mpls_adj>\d+)\s+l3adj_flags:+(?P<l3adj_flags>\w+)$"
        )

        # recirc_adj_id:3120562239
        p32 = re.compile(r"recirc_adj_id:+(?P<recirc_adj_id>\d+)$")

        # sih:0x7f02737e11c8(182) di_id:20499 rih:0x7f02737e0bf8(74)
        p33 = re.compile(
            r"sih:+(?P<sih>\S+)\s+di_id:(?P<di_id>\d+)\s+rih:+(?P<rih>\S+)$"
        )

        # adj_lentry [eos0:0x7f02734123b8 eos1:0x7f02737ec5e8]
        p34 = re.compile(r"adj_lentry\s+(?P<adj_lentry>[\S\s]+)$")

        # ecr_prefix_adj: id:2483028067 (ref:1)
        p35 = re.compile(r"(?P<ecr_prefix_adj>\S+):\s+id:+(?P<id>\d+)\s+\S+$")

        # objid:ADJ SPECIAL:0
        p36 = re.compile(r"objid:+(?P<objid>\S+)\s+SPECIAL:+(?P<SPECIAL>\w+)$")

        # Init vars
        ret_dict = {}
        for line in out.splitlines():
            line = line.strip()
            eos_dict = {}

            # LENTRY:label:22 nobj:(EOS, 142) lentry_hdl:0xde00000a
            m = p1.match(line)
            if m:
                group = m.groupdict()
                label_id = int(group["label"])
                lentry_dict = ret_dict.setdefault("lentry_label", {}).setdefault(
                    label_id, {}
                )
                lentry_dict["nobj"] = list(str(group["nobj"]).split(","))
                lentry_dict["lentry_hdl"] = group["lentry_hdl"]
                continue

            # modify_cnt:1 backwalk_cnt:2
            m = p2.match(line)
            if m:
                group = m.groupdict()
                lentry_dict["modify_cnt"] = int(group["modify_cnt"])
                lentry_dict["backwalk_cnt"] = int(group["backwalk_cnt"])
                continue

            # lspa_handle:0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                lentry_dict["lspa_handle"] = str(group["lspa_handle"])
                continue

            # AAL: id:3724541962 lbl:22
            m = p4.match(line)
            if m:
                group = m.groupdict()
                aal_dict = ret_dict["lentry_label"][label_id].setdefault("aal", {})
                aal_dict["id"] = int(group["id"])
                aal_dict["lbl"] = int(group["lbl"])
                continue

            # eos0:[adj_hdl:0x83000039, hw_hdl:0x7f02737c6628]
            m = p5.match(line)
            if m:
                group = m.groupdict()
                eos0_dict = ret_dict["lentry_label"][label_id]["aal"].setdefault(
                    "eos0", {}
                )
                eos0_dict["adj_hdl"] = str(group["adj_hdl"])
                eos0_dict["hw_hdl"] = str(group["hw_hdl"])
                continue

            # eos1:[adj_hdl:0x3d000038, hw_hdl:0x7f02737c6478]
            m = p6.match(line)
            if m:
                group = m.groupdict()
                eos1_dict = ret_dict["lentry_label"][label_id]["aal"].setdefault(
                    "eos1", {}
                )
                eos1_dict["adj_hdl"] = str(group["adj_hdl"])
                eos1_dict["hw_hdl"] = str(group["hw_hdl"])
                continue

            # deagg_vrf_id = 0 lspa_handle:0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                aal_dict["deagg_vrf_id"] = int(group["deagg_vrf_id"])
                aal_dict["lspa_handle"] = str(group["lspa_handle"])
                continue

            # EOS:objid:142 local_label:0 flags:0:() pdflags:0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                eos_dict = ret_dict["lentry_label"][label_id].setdefault("eos", {})
                eos_dict["objid"] = int(group["objid"])
                eos_dict["local_label"] = int(group["local_label"])
                eos_dict["flags"] = str(group["flags"])
                eos_dict["pdflags"] = str(group["pdflags"])
                continue

            # nobj0:(LABEL, 143), nobj1:(LABEL, 141) modify:1 bwalk:0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ret_dict["lentry_label"][label_id]["eos"]["nobj0"] = list(
                    str(group["nobj0"]).split(", ")
                )
                ret_dict["lentry_label"][label_id]["eos"]["nobj1"] = list(
                    str(group["nobj1"]).split(", ")
                )
                ret_dict["lentry_label"][label_id]["eos"]["modify"] = int(
                    group["modify"]
                )
                ret_dict["lentry_label"][label_id]["eos"]["bwalk"] = int(group["bwalk"])
                continue

            # LABEL:objid:143 link_type:MPLS local_label:22 outlabel:(3, 0)
            m = p10.match(line)
            if m:
                group = m.groupdict()
                objid = int(group["objid"])
                label_dict = (
                    ret_dict["lentry_label"][label_id]
                    .setdefault("label", {})
                    .setdefault(objid, {})
                )
                label_dict["link_type"] = str(group["link_type"])
                label_dict["local_label"] = int(group["local_label"])
                label_dict["outlabel"] = str(group["outlabel"])
                continue

            # flags:0x18:(POP,PHP,) pdflags:0:(INSTALL_HW_OK,) adj_handle:0x83000039
            m = p11.match(line)
            if m:
                group = m.groupdict()
                label_dict["flags"] = {}
                flagid = str(group["flagid"])
                flagstr = str(group["flagstr"])
                flaglist = list(flagstr.split(","))
                label_dict["flags"][flagid] = flaglist
                label_dict["pdflags"] = {}
                flagid = str(group["pdflagid"])
                flagstr = str(group["pdflagstr"])
                flaglist = list(flagstr.split(","))
                label_dict["pdflags"][flagid] = flaglist
                label_dict["adj_handle"] = str(group["adj_handle"])
                continue

            # unsupported recursion:0 olbl_changed 0 local_adj:0 modify_cnt:0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                label_dict["unsupported_recursion"] = int(
                    group["unsupported_recursion"]
                )
                label_dict["olbl_changed"] = int(group["olbl_changed"])
                label_dict["local_adj"] = int(group["local_adj"])
                label_dict["modify_cnt"] = int(group["modify_cnt"])
                continue

            # bwalk_cnt:0 subwalk_cnt:0 collapsed_oce:0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                label_dict["bwalk_cnt"] = int(group["bwalk_cnt"])
                label_dict["subwalk_cnt"] = int(group["subwalk_cnt"])
                label_dict["collapsed_oce"] = int(group["collapsed_oce"])
                continue

            # AAL: id:2197815353 lbl:0 smac:00a7.42d6.c41f dmac:0027.90bf.2ee7
            m = p14.match(line)
            if m:
                group = m.groupdict()
                id = int(group["id"])
                labelaal_dict = (
                    ret_dict["lentry_label"][label_id]["label"][objid]
                    .setdefault("label_aal", {})
                    .setdefault(id, {})
                )
                labelaal_dict["lbl"] = int(group["lbl"])
                labelaal_dict["smac"] = str(group["smac"])
                labelaal_dict["dmac"] = str(group["dmac"])
                continue

            # sub_type:0 link_type:2 adj_flags:0 label_type:1 rewrite_type:POP2MPLS(138)
            m = p15.match(line)
            if m:
                group = m.groupdict()
                labelaal_dict["sub_type"] = int(group["sub_type"])
                labelaal_dict["link_type"] = int(group["link_type"])
                labelaal_dict["adj_flags"] = str(group["adj_flags"])
                labelaal_dict["label_type"] = int(group["label_type"])
                labelaal_dict["rewrite_type"] = str(group["rewrite_type"])
                continue

            # vlan_id:0 vrf_id:0 ri:0x7f02737cc1e8, ri_id:0x3e phdl:0xab000447, ref_cnt:1
            m = p16.match(line)
            if m:
                group = m.groupdict()
                labelaal_dict["vlan_id"] = int(group["vlan_id"])
                labelaal_dict["vrf_id"] = int(group["vrf_id"])
                labelaal_dict["ri"] = str(group["ri"])
                labelaal_dict["ri_id"] = str(group["ri_id"])
                labelaal_dict["phdl"] = str(group["phdl"])
                labelaal_dict["ref_cnt"] = int(group["ref_cnt"])
                continue

            # si:0x7f02737cc6b8, si_id:0x4027, di_id:0x526d
            m = p17.match(line)
            if m:
                group = m.groupdict()
                labelaal_dict["si"] = str(group["si"])
                labelaal_dict["si_id"] = str(group["si_id"])
                labelaal_dict["di_id"] = str(group["di_id"])
                continue

            # ADJ:objid:71 {link_type:MPLS ifnum:0x7c, adj:0x53000020, si: 0x7ff791190278
            m = p18.match(line)
            if m:
                group = m.groupdict()
                objid = int(group["objid"])
                adj_dict = (
                    ret_dict["lentry_label"][label_id]
                    .setdefault("adj", {})
                    .setdefault(objid, {})
                )
                adj_dict["link_type"] = str(group["link_type"])
                adj_dict["ifnum"] = str(group["ifnum"])
                adj_dict["adj"] = str(group["adj"])
                adj_dict["si"] = str(group["si"])
                continue

            # ADJ:objid:139 {link_type:MPLS ifnum:0x36, adj:0x5c000037, si: 0x7f02737a2348  }
            m = p19.match(line)
            if m:
                group = m.groupdict()
                objid = int(group["objid"])
                adj_dict = (
                    ret_dict["lentry_label"][label_id]
                    .setdefault("adj", {})
                    .setdefault(objid, {})
                )
                adj_dict["link_type"] = str(group["link_type"])
                adj_dict["ifnum"] = str(group["ifnum"])
                adj_dict["adj"] = str(group["adj"])
                adj_dict["si"] = str(group["si"])
                adj_dict["IPv4"] = str(group["IPv4"])
                continue

            # LENTRY:label:75 not found...
            m = p20.match(line)
            if m:
                group = m.groupdict()
                label_id = int(group["label"])
                lentry_dict = ret_dict.setdefault("lentry_label", {}).setdefault(
                    label_id, {}
                )
                lentry_dict["label"] = int(group["label"])
                continue

            # AAL: Handle not found:0
            m = p21.match(line)
            if m:
                group = m.groupdict()
                labelaal_dict = ret_dict["lentry_label"][label_id].setdefault("aal", {})
                continue

            # LB:obj_id:38 ecr_map_objid:0 link_type:IP num_choices:2 Flags:0
            m = p22.match(line)
            if m:
                group = m.groupdict()
                objid1 = int(group["obj_id"])
                lb_dict = (
                    ret_dict["lentry_label"][label_id]
                    .setdefault("lb", {})
                    .setdefault(objid1, {})
                )
                lb_dict["ecr_map_objid"] = int(group["ecr_map_objid"])
                lb_dict["link_type"] = str(group["link_type"])
                lb_dict["num_choices"] = int(group["num_choices"])
                lb_dict["flags"] = str(group["flags"])
                continue

            # mpls_ecr:1 local_label:24 path_inhw:2 ecrh:0xf9000002 old_ecrh:0
            m = p23.match(line)
            if m:
                group = m.groupdict()
                lb_dict["mpls_ecr"] = int(group["mpls_ecr"])
                lb_dict["local_label"] = int(group["local_label"])
                lb_dict["path_inhw"] = int(group["path_inhw"])
                lb_dict["ecrh"] = str(group["ecrh"])
                lb_dict["old_ecrh"] = str(group["old_ecrh"])
                continue

            # modify_cnt:0 bwalk_cnt:0 subwalk_cnt:0 finish_cnt:0
            m = p24.match(line)
            if m:
                group = m.groupdict()
                lb_dict["modify_cnt"] = int(group["modify_cnt"])
                lb_dict["bwalk_cnt"] = int(group["bwalk_cnt"])
                lb_dict["subwalk_cnt"] = int(group["subwalk_cnt"])
                lb_dict["finish_cnt"] = int(group["finish_cnt"])
                lb_dict["aal"] = {}
                lb_dict["bwalk"] = {}
                continue

            # bwalk:[req:0 in_prog:0 nested:0]
            m = p25.match(line)
            if m:
                group = m.groupdict()
                lb_dict["bwalk"]["req"] = int(group["req"])
                lb_dict["bwalk"]["in_prog"] = int(group["in_prog"])
                lb_dict["bwalk"]["nested"] = int(group["nested"])
                continue

            # AAL: ecr:id:4177526786 af:0 ecr_type:0 ref:3 ecrh:0x7f02737e49f8(28:2)
            m = p26.match(line)
            if m:
                group = m.groupdict()
                lb_dict["aal"]["ecr_id"] = int(group["ecr_id"])
                lb_dict["aal"]["af"] = int(group["af"])
                lb_dict["aal"]["ecr_type"] = str(group["ecr_type"])
                lb_dict["aal"]["ref"] = int(group["ref"])
                lb_dict["aal"]["ecrh"] = str(group["ecrh"])
                continue

            # hwhdl:1937656312 ::0x7f02737e11c8,0x7f02737e2728,0x7f02737e11c8,0x7f02737e2728
            m = p27.match(line)
            if m:
                group = m.groupdict()
                lb_dict["aal"]["hwhdl"] = str(group["hwhdl"])
                continue

            # Sw Enh ECR scale: objid:38 llabel:24 eos:1 #adjs:2 mixed_adj:0
            m = p28.match(line)
            if m:
                group = m.groupdict()
                objid = int(group["objid"])
                ecr_dict = (
                    ret_dict["lentry_label"][label_id]
                    .setdefault("sw_enh_ecr_scale", {})
                    .setdefault(objid, {})
                )
                ecr_dict["llabel"] = int(group["llabel"])
                ecr_dict["eos"] = int(group["eos"])
                ecr_dict["adjs"] = int(group["adjs"])
                ecr_dict["mixed_adj"] = str(group["mixed_adj"])
                continue

            # reprogram_hw:0 ecrhdl:0xf9000002 ecr_hwhdl:0x7f02737e49f8
            m = p29.match(line)
            if m:
                group = m.groupdict()
                ecr_dict["reprogram_hw"] = str(group["reprogram_hw"])
                ecr_dict["ecrhdl"] = str(group["ecrhdl"])
                ecr_dict["ecr_hwhdl"] = str(group["ecr_hwhdl"])
                continue

            # mod_cnt:0 prev_npath:0 pmismatch:0 pordermatch:0
            m = p30.match(line)
            if m:
                group = m.groupdict()
                ecr_dict["mod_cnt"] = int(group["mod_cnt"])
                ecr_dict["prev_npath"] = int(group["prev_npath"])
                ecr_dict["pmismatch"] = int(group["pmismatch"])
                ecr_dict["pordermatch"] = int(group["pordermatch"])
                ecr_dict["ecr_adj"] = {}
                continue

            # ecr_adj: id:1644167265 is_mpls_adj:1 l3adj_flags:0x100000
            m = p31.match(line)
            if m:
                group = m.groupdict()
                id1 = int(group["id"])
                ecr_dict["ecr_adj"][id1] = {}
                ecr_dict["ecr_adj"][id1]["is_mpls_adj"] = int(group["is_mpls_adj"])
                ecr_dict["ecr_adj"][id1]["l3adj_flags"] = str(group["l3adj_flags"])
                continue

            # recirc_adj_id:3120562239
            m = p32.match(line)
            if m:
                group = m.groupdict()
                ecr_dict["ecr_adj"][id1]["recirc_adj_id"] = int(group["recirc_adj_id"])
                continue

            # sih:0x7f02737e11c8(182) di_id:20499 rih:0x7f02737e0bf8(74)
            m = p33.match(line)
            if m:
                group = m.groupdict()
                ecr_dict["ecr_adj"][id1]["sih"] = str(group["sih"])
                ecr_dict["ecr_adj"][id1]["di_id"] = int(group["di_id"])
                ecr_dict["ecr_adj"][id1]["rih"] = str(group["rih"])
                continue

            # adj_lentry [eos0:0x7f02734123b8 eos1:0x7f02737ec5e8]
            m = p34.match(line)
            if m:
                group = m.groupdict()
                ecr_dict["ecr_adj"][id1]["adj_lentry"] = str(group["adj_lentry"])
                continue

            # ecr_prefix_adj: id:2483028067 (ref:1)
            m = p35.match(line)
            if m:
                group = m.groupdict()
                id1 = int(group["id"])
                ecr_dict["ecr_adj"][id1] = {}
                continue

            # objid:ADJ SPECIAL:0
            m = p36.match(line)
            if m:
                group = m.groupdict()
                lentry_dict["objid"] = {}
                id2 = str(group["objid"])
                lentry_dict["objid"][id2] = {}
                lentry_dict["objid"][id2]["SPECIAL"] = str(group["SPECIAL"])
                continue

        return ret_dict


# ==================================================
# Parser for 'show platform software fed mode count'
# ==================================================
class ShowPlatformSoftwareFedLspaAllPermodeSchema(MetaParser):

    """Schema for "show Platform software fed mode count" """

    schema = {"lspa_mode_count": int}


# ==================================================
# Parser for 'show platform software fed mode count'
# ==================================================
class ShowPlatformSoftwareFedLspaAllPermode(
    ShowPlatformSoftwareFedLspaAllPermodeSchema
):
    """Parser for
    "show platform software fed {switchvirtualstate} mpls lspa all | c {mode}"
    """

    cli_command = [
        "show platform software fed {switchvirtualstate} mpls lspa all | c {mode}"
    ]

    def cli(self, switchvirtualstate="", mode="", output=None):
        if output is None:
            cmd = self.cli_command[0].format(
                switchvirtualstate=switchvirtualstate, mode=mode
            )
            output = self.device.execute(cmd)

        # Init vars
        ret_dict = {}

        # Number of lines which match regexp = 0
        p1 = re.compile(
            r"^Number +of +lines +which +match +regexp+\s+\W+\s+(?P<lspa_mode_count>(\d+))$"
        )

        for line in output.splitlines():
            line = line.strip()

            # Number of lines which match regexp = 0
            m = p1.match(line)
            if m:
                lspa_mode_count = int(m.groupdict()["lspa_mode_count"])
                ret_dict["lspa_mode_count"] = lspa_mode_count
                continue
        return ret_dict


# =======================================
# Parser for 'show platform software fed'
# =======================================
class ShowPlatformSoftwareFedLspaAllSchema(MetaParser):

    """Schema for "show Platform software fed" """

    schema = {
        "lspa_info": {
            Optional("total_lspa_entries"): int,
            Optional("lspa_record"): {
                Any(): {Optional("mode"): str, Optional("ref_cnt"): int}
            },
        }
    }


# =======================================
# Parser for 'show platform software fed'
# =======================================
class ShowPlatformSoftwareFedLspaAll(ShowPlatformSoftwareFedLspaAllSchema):
    """Parser for
    "show platform software fed {switchvirtualstate} mpls lspa all"
    """

    cli_command = ["show platform software fed {switchvirtualstate} mpls lspa all"]

    def cli(self, switchvirtualstate="", output=None):
        if output is None:
            cmd = self.cli_command[0].format(switchvirtualstate=switchvirtualstate)
            output = self.device.execute(cmd)

        # Init vars
        ret_dict = {}

        # Detailed LSPA info for all LSPA: (# of entries:2)
        p1 = re.compile(
            r"^Detailed +LSPA +info +for +all +LSPA+\W+of +entries\W+(?P<total_lspa_entries>\d+)\)$"
        )
        # LSPA:NPD:lspa_rec:0x118804cdfb8 lspa:0x118804ce108 rm_hdl:0 mode:PER_VRF ref_cnt:11
        #       lspakey[pfx1_gid,vpnlbl]:[1010,22][0,0] mode:1
        #       lspa:[vrf_id:6 vpn_encap_gid:0 l3nh_oid:1501 paths:1 dst_oid:1495]
        #    SDK: fec:oid:1501 l3_fec_st:1495, type:la_prefix_object_base(oid=1495)
        p2 = re.compile(
            r"^\S+lspa_rec\W+(?P<lspa_rec>(\S+))+\s+\S+\s+\S+\s+mode\W+(?P<mode>(\S+))+\s+ref_cnt\W+(?P<ref_cnt>(\d+))$"
        )

        for line in output.splitlines():
            line = line.strip()

            # Detailed LSPA info for all LSPA: (# of entries:2)
            m = p1.match(line)
            if m:
                lspa_dict = ret_dict.setdefault("lspa_info", {})
                total_lspa_entries = int(m.groupdict()["total_lspa_entries"])
                lspa_dict["total_lspa_entries"] = total_lspa_entries
                continue

            m = p2.match(line)
            if m:
                lspa_rec_dict = lspa_dict.setdefault("lspa_record", {})
                rec_id = m.groupdict()["lspa_rec"]
                lspa_rec = lspa_rec_dict.setdefault(rec_id, {})
                mode = m.groupdict()["mode"]
                ref_cnt = int(m.groupdict()["ref_cnt"])
                lspa_rec["mode"] = mode
                lspa_rec["ref_cnt"] = ref_cnt
                continue

        return ret_dict