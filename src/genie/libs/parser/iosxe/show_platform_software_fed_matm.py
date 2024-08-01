"""show_platform_software_fed_matm.py

    * 'show platform software fed {state} matm macTable vlan {vlan}'
    * 'show platform software fed switch active matm adjacencies vlan {vlan_id}'
    * 'show platform software fed switch active matm adjacencies adjkey {adj_key}'
    * 'show platform software fed switch active matm adjacencies'
    * 'show platform software fed active matm stats'
    * 'show platform software fed switch {mode} matm stats'
    * 'show platform software fed switch active matm macTable vlan {vlan} mac {dynamic_mac} detail'
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

# =======================================================
# Parser for 'Show Platform Software Fed Matm MacTable'
# =======================================================
class ShowPlatformSoftwareFedMatmMacTableSchema(MetaParser):
    """Schema for show Platform Software Fed matm MacTable"""

    schema = {
        "mac": {
            Any(): {
                Optional("mac"): str,
                Optional("vlanport"): int,
                Optional("type"): str,
                Optional("sequence"): int,
                Optional("ecbi"): int,
                Optional("flag"): int,
                Optional("machandle"): str,
                Optional("sihandle"): str,
                Optional("rihandle"): str,
                Optional("dihandle"): str,
                Optional("atime"): int,
                Optional("etime"): int,
                Optional("port"): str,
                Optional("con"): str,
            }
        }
    }


class ShowPlatformSoftwareFedMatmMacTable(ShowPlatformSoftwareFedMatmMacTableSchema):
    """Parser for show Platform Software Fed matm mactable"""

    cli_command = "show platform software fed {state} matm macTable vlan {vlan}"

    def cli(self, state="", vlan="", output=None):
        if output is None:
            output = self.device.execute(
                self.cli_command.format(state=state, vlan=vlan)
            )
        platform_dict = {}

        # VLAN   MAC                  Type  Seq#    EC_Bi  Flags  machandle           siHandle            riHandle            diHandle              *a_time  *e_time  ports                                                         Con
        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # 10     3c57.3104.6b42  0x5000001       0      0     64  0x7f61dd192978      0x7f61dcfb58a8      0x7f61dd1259e8      0x0                         0      798  VTEP 40.40.40.40 adj_id 1011                                  No

        p = re.compile(
            r"(?P<vlanport>\d+) +(?P<mac>[\w\.]+) + "
            r"(?P<type>\w+) +(?P<sequence>\d+) +"
            r"(?P<ecbi>\d+) +(?P<flag>\d+) +"
            r"(?P<machandle>\w+) +(?P<sihandle>\w+) +"
            r"(?P<rihandle>\w+) +(?P<dihandle>\w+) +"
            r"(?P<atime>\d+) + (?P<etime>[\d\s]+) +"
            r"(?P<port>[\w\.\_\/\s\s]+) + (?P<con>[\s\w\s]+)$"
        )

        for line in output.splitlines():
            line = line.strip()
            m = p.match(line)
            if m:
                mac = m.groupdict()["mac"]
                mac_dict = platform_dict.setdefault("mac", {}).setdefault(mac, {})
                value = [
                    "mac",
                    "type",
                    "machandle",
                    "sihandle",
                    "rihandle",
                    "dihandle",
                    "port",
                    "con",
                ]
                mac_dict.update(
                    {
                        k: v.replace(" ", "") if k in value else int(v)
                        for (k, v) in m.groupdict().items()
                    }
                )

        return platform_dict


# ======================================================
# Parser for 'show platform software fed switch active matm adjacencies vlan {vlan_id} '
# ======================================================


class ShowPlatformSoftwareFedSwitchActiveMatmAdjacenciesVlanSchema(MetaParser):
    """Schema for show platform software fed switch active matm adjacencies vlan {vlan_id}"""

    schema = {
        "adj_id": {
            Any(): {
                "vlan_id": int,
                "adj_key": str,
                "encap": str,
                "link_type": str,
                "si_handle": str,
                "ri_handle": str,
                "l3_mri_handle": str,
                "di_handle": str,
                "obj_type": str,
                "shared": str,
            },
        },
    }


class ShowPlatformSoftwareFedSwitchActiveMatmAdjacenciesVlan(
    ShowPlatformSoftwareFedSwitchActiveMatmAdjacenciesVlanSchema
):
    """Parser for show platform software fed switch active matm adjacencies vlan {vlan_id}"""

    cli_command = [
        "show platform software fed {switch} active matm adjacencies vlan {vlan_id}",
        "show platform software fed active matm adjacencies vlan {vlan_id}",
    ]

    def cli(self, vlan_id, switch=None, output=None):
        if output is None:
            if switch:
                output = self.device.execute(
                    self.cli_command[0].format(switch=switch, vlan_id=vlan_id)
                )
            else:
                output = self.device.execute(
                    self.cli_command[1].format(vlan_id=vlan_id)
                )

        # v99     966         0x3000003c6      VXLAN  V4     0x0              0x0              0x0              0x0              UC         No
        p1 = re.compile(
            r"^(?P<vlan_id>\d+)\s+(?P<adj_id>\d+)\s+(?P<adj_key>\S+)\s+(?P<encap>\S+)\s+(?P<link_type>\w+)\s+(?P<si_handle>\w+)\s+(?P<ri_handle>\w+)\s+(?P<l3_mri_handle>\S+)\s+(?P<di_handle>\w+)\s+(?P<obj_type>\S+)\s+(?P<shared>\w+)$"
        )
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # V99     966         0x3000003c6      VXLAN  V4     0x0              0x0              0x0              0x0              UC         No
            m = p1.match(line)
            if m:
                group = m.groupdict()
                adj_id = int(group["adj_id"])
                matm_adj_dict = ret_dict.setdefault("adj_id", {})
                adj_id_dict = matm_adj_dict.setdefault(adj_id, {})
                adj_id_dict["vlan_id"] = int(group["vlan_id"])
                adj_id_dict["adj_key"] = group["adj_key"]
                adj_id_dict["encap"] = group["encap"]
                adj_id_dict["link_type"] = group["link_type"]
                adj_id_dict["si_handle"] = group["si_handle"]
                adj_id_dict["ri_handle"] = group["ri_handle"]
                adj_id_dict["l3_mri_handle"] = group["l3_mri_handle"]
                adj_id_dict["di_handle"] = group["di_handle"]
                adj_id_dict["obj_type"] = group["obj_type"]
                adj_id_dict["shared"] = group["shared"]
                continue

        return ret_dict


# ======================================================
# Parser for 'show platform software fed switch active matm adjacencies adjkey {adj_key} '
# ======================================================


class ShowPlatformSoftwareFedSwitchActiveMatmAdjacenciesAdjkeySchema(MetaParser):
    """Schema for show platform software fed switch active matm adjacencies adjkey {adj_key}"""

    schema = {
        "adj_id": {
            Any(): {
                "if_number": str,
                "vni_id": int,
                "len": int,
                "vlan_id": int,
                "encap": str,
                "link_type": str,
                "source_ip": str,
                "destination_ip": str,
                "si_handle": str,
                "ri_handle": str,
                "l3_mri_handle": str,
                "di_handle": str,
                "object_type": str,
            },
        },
        "created_time": str,
        "last_modified": str,
        "current_time": str,
        Optional("asic_instance"): {
            Any(): {
                Optional("ri"): int,
                Optional("rewrite_type"): str,
                Optional("mapped_ri"): str,
                Optional("src_ip"): str,
                Optional("dst_ip"): str,
                Optional("dst_mac"): str,
                Optional("src_mac"): str,
                Optional("ipv4_ttl"): int,
                Optional("iid_present"): int,
                Optional("lisp_iid"): int,
                Optional("lisp_flags"): int,
                Optional("dst_port"): int,
                Optional("update_l3if"): int,
                Optional("is_ttl_prop"): int,
                Optional("l3if_le"): str,
                Optional("port_le"): str,
                Optional("vlan_le"): str,
            },
        },
    }


class ShowPlatformSoftwareFedSwitchActiveMatmAdjacenciesAdjkey(
    ShowPlatformSoftwareFedSwitchActiveMatmAdjacenciesAdjkeySchema
):
    """Parser for show platform software fed switch active matm adjacencies adjkey {adj_key}"""

    cli_command = [
        "show platform software fed {switch} active matm adjacencies adjkey {adj_key}",
        "show platform software fed active matm adjacencies adjkey {adj_key}",
    ]

    def cli(self, adj_key, switch=None, output=None):
        if output is None:
            if switch:
                output = self.device.execute(
                    self.cli_command[0].format(switch=switch, adj_key=adj_key)
                )
            else:
                output = self.device.execute(
                    self.cli_command[1].format(adj_key=adj_key)
                )

        # 3849        0x420065   200199     60     99     VXLAN  V4     172.11.1.1        172.11.1.22       0x7f95815d74d8       0x7f95815a4528       0x0              0x0          UC
        p1 = re.compile(
            r"^(?P<adj_id>\d+)\s+(?P<if_number>\S+)\s+(?P<vni_id>\d+)\s+(?P<len>\d+)\s+(?P<vlan_id>\d+)\s+(?P<encap>\w+)\s+(?P<link_type>\S+)\s+(?P<source_ip>(\d{1,3}\.){3}\d{1,3})\s+(?P<destination_ip>(\d{1,3}\.){3}\d{1,3})\s+(?P<si_handle>\S+)\s+(?P<ri_handle>\S+)\s+(?P<l3_mri_handle>\S+)\s+(?P<di_handle>\S+)\s+(?P<object_type>\w+)$"
        )

        # Created Time       : 2023/01/24 05:25:43.658
        p2 = re.compile(r"^Created\s+Time\s+:\s+(?P<created_time>.*)$")

        # Last Modified Time : 2023/01/24 05:25:43.658
        p3 = re.compile(r"^Last\s+Modified\s+Time\s+:\s+(?P<last_modified>.*)$")

        # Current Time       : 2023/01/24 07:52:27.709
        p4 = re.compile(r"^Current\s+Time\s+:\s+(?P<current_time>.*)$")

        # ASIC#:0 RI:226 Rewrite_type:AL_RRM_REWRITE_LVX_IPV4_L2_PAYLOAD_ENCAP_EPG(116) Mapped_rii:LVX_L3_ENCAP_L2_PAYLOAD_EPG(135)
        p5 = re.compile(
            r"^ASIC#:+(?P<asic_instance>\d+)\s+RI:+(?P<ri>\d+)+\s+Rewrite_type:+(?P<rewrite_type>\S+)\s+Mapped_rii:+(?P<mapped_ri>\S+)$"
        )

        # Src IP:    172.11.1.1
        p6 = re.compile(r"^Src\s+IP:\s+(?P<src_ip>\S+)$")

        # Dst IP:    172.11.1.22
        p7 = re.compile(r"^Dst\s+IP:\s+(?P<dst_ip>\S+)$")

        # iVxlan dstMac:     0x9f:0x00:0x00
        p8 = re.compile(r"^iVxlan\s+dstMac:\s+(?P<dst_mac>\S+)$")

        # iVxlan srcMac:     0x00:0x00:0x00
        p9 = re.compile(r"^iVxlan\s+srcMac:\s+(?P<src_mac>\S+)$")

        # IPv4 TTL:  0
        p10 = re.compile(r"^IPv4\s+TTL:\s+(?P<ipv4_ttl>\d+)$")

        # iid present:   0
        p11 = re.compile(r"^iid\s+present:\s+(?P<iid_present>\d+)$")

        # lisp iid:  200199
        p12 = re.compile(r"^lisp\s+iid:\s+(?P<lisp_iid>\d+)$")

        # lisp flags:    0
        p13 = re.compile(r"^lisp\s+flags:\s+(?P<lisp_flags>\d+)$")

        # dst Port:  4789
        p14 = re.compile(r"^dst\s+Port:\s+(?P<dst_port>\d+)$")

        # update only l3if:  0
        p15 = re.compile(r"^update\s+only\s+l3if:\s+(?P<update_l3if>\d+)$")

        # is Sgt:    0
        p16 = re.compile(r"^is\s+sgt:\s+(?P<is_sgt>\d+)$")

        # is TTL Prop:   0
        p17 = re.compile(r"^is\s+TTL\s+Prop:\s+(?P<is_ttl_prop>\d+)$")

        # L3if LE:   126 (0)
        p18 = re.compile(r"^L3if\s+LE:\s+(?P<l3if_le>.*)$")

        # Port LE:   318 (0)
        p19 = re.compile(r"^Port\s+LE:\s+(?P<port_le>.*)$")

        # Vlan LE:   68 (0)
        p20 = re.compile(r"^Vlan\s+LE:\s+(?P<vlan_le>.*)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # 3849        0x420065   200199     60     99     VXLAN  V4     172.11.1.1        172.11.1.22       0x7f95815d74d8       0x7f95815a4528       0x0              0x0          UC
            m = p1.match(line)
            if m:
                group = m.groupdict()
                adj_id = int(group["adj_id"])
                matm_adj_dict = ret_dict.setdefault("adj_id", {})
                adj_id_dict = matm_adj_dict.setdefault(adj_id, {})
                adj_id_dict["if_number"] = group["if_number"]
                adj_id_dict["vni_id"] = int(group["vni_id"])
                adj_id_dict["len"] = int(group["len"])
                adj_id_dict["vlan_id"] = int(group["vlan_id"])
                adj_id_dict["encap"] = group["encap"]
                adj_id_dict["link_type"] = group["link_type"]
                adj_id_dict["source_ip"] = group["source_ip"]
                adj_id_dict["destination_ip"] = group["destination_ip"]
                adj_id_dict["si_handle"] = group["si_handle"]
                adj_id_dict["ri_handle"] = group["ri_handle"]
                adj_id_dict["l3_mri_handle"] = group["l3_mri_handle"]
                adj_id_dict["di_handle"] = group["di_handle"]
                adj_id_dict["object_type"] = group["object_type"]

            # Created Time       : 2023/01/24 05:25:43.658
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict["created_time"] = group["created_time"]
                continue

            # Last Modified Time : 2023/01/24 05:25:43.658
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict["last_modified"] = group["last_modified"]
                continue

            # Current Time       : 2023/01/24 07:52:27.709
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict["current_time"] = group["current_time"]
                continue

            # ASIC#:0 RI:226 Rewrite_type:AL_RRM_REWRITE_LVX_IPV4_L2_PAYLOAD_ENCAP_EPG(116) Mapped_rii:LVX_L3_ENCAP_L2_PAYLOAD_EPG(135)
            m = p5.match(line)
            if m:
                group = m.groupdict()
                asic_instance = int(group["asic_instance"])
                asic_dict = ret_dict.setdefault("asic_instance", {})
                res_info_dict = asic_dict.setdefault(asic_instance, {})
                res_info_dict["ri"] = int(group["ri"])
                res_info_dict["rewrite_type"] = group["rewrite_type"]
                res_info_dict["mapped_ri"] = group["mapped_ri"]
                continue

            # Src IP:    172.11.1.1
            m = p6.match(line)
            if m:
                group = m.groupdict()
                res_info_dict["src_ip"] = group["src_ip"]
                continue

            # Dst IP:    172.11.1.22
            m = p7.match(line)
            if m:
                group = m.groupdict()
                res_info_dict["dst_ip"] = group["dst_ip"]
                continue

            # iVxlan dstMac:     0x9f:0x00:0x00
            m = p8.match(line)
            if m:
                group = m.groupdict()
                res_info_dict["dst_mac"] = group["dst_mac"]
                continue

            # iVxlan srcMac:     0x00:0x00:0x00
            m = p9.match(line)
            if m:
                group = m.groupdict()
                res_info_dict["src_mac"] = group["src_mac"]
                continue

            # IPv4 TTL:  0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                res_info_dict["ipv4_ttl"] = int(group["ipv4_ttl"])
                continue

            # iid present:   0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                res_info_dict["iid_present"] = int(group["iid_present"])
                continue

            # lisp iid:  200199
            m = p12.match(line)
            if m:
                group = m.groupdict()
                res_info_dict["lisp_iid"] = int(group["lisp_iid"])
                continue

            # lisp flags:    0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                res_info_dict["lisp_flags"] = int(group["lisp_flags"])
                continue

            # dst Port:  4789
            m = p14.match(line)
            if m:
                group = m.groupdict()
                res_info_dict["dst_port"] = int(group["dst_port"])
                continue

            # update only l3if:  0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                res_info_dict["update_l3if"] = int(group["update_l3if"])
                continue

            # is Sgt:    0
            m = p16.match(line)
            if m:
                group = m.groupdict()
                res_info_dict["is_sgt"] = int(group["is_sgt"])
                continue

            # is TTL Prop:   0
            m = p17.match(line)
            if m:
                group = m.groupdict()
                res_info_dict["is_ttl_prop"] = int(group["is_ttl_prop"])
                continue

            # L3if LE:   126 (0)
            m = p18.match(line)
            if m:
                group = m.groupdict()
                res_info_dict["l3if_le"] = group["l3if_le"]
                continue

            # Port LE:   318 (0)
            m = p19.match(line)
            if m:
                group = m.groupdict()
                res_info_dict["port_le"] = group["port_le"]
                continue

            # Vlan LE:   68 (0)
            m = p20.match(line)
            if m:
                group = m.groupdict()
                res_info_dict["vlan_le"] = group["vlan_le"]
                continue

        return ret_dict


# ======================================================
# Parser for 'show platform software fed switch active matm adjacencies '
# ======================================================
class ShowPlatformSoftwareFedSwitchActiveMatmAdjacenciesSchema(MetaParser):
    """Schema for show platform software fed switch active matm adjacencies"""

    schema = {
        "adjacencies": {
            Any(): {
                "adj_id": int,
                "adj_key": str,
                "encap": str,
                "link": str,
                "sihandle": str,
                "rihandle": str,
                "dihandle": str,
                "obj_type": str,
            },
        },
    }


class ShowPlatformSoftwareFedSwitchActiveMatmAdjacencies(
    ShowPlatformSoftwareFedSwitchActiveMatmAdjacenciesSchema
):
    """Parser for show platform software fed switch active matm adjacencies"""

    cli_command = "show platform software fed switch active matm adjacencies"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # 201    89          0x100000059      VXLAN  V4     0x7fd728bf1be8   0x7fd728bf17a8   0x0              CP

        # 201    89          0x100000059      VXLAN  V4     0x7fd728bf1be8   0x7fd728bf17a8   0x0              CP
        p2 = re.compile(
            r"^(?P<vlan>\d+)\s+(?P<adj_id>\d+)\s+(?P<adj_key>\S+)\s+(?P<encap>\w+)\s+(?P<link>\S+)\s+(?P<sihandle>\S+)\s+(?P<rihandle>\S+)\s+(?P<dihandle>\S+)\s+(?P<obj_type>\w+)$"
        )

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            # 201    89          0x100000059      VXLAN  V4     0x7fd728bf1be8   0x7fd728bf17a8   0x0              CP
            m = p2.match(line)
            if m:
                dict_val = m.groupdict()
                adjacencies = ret_dict.setdefault("adjacencies", {})
                vlan_id = int(dict_val["vlan"])
                index_adjacencies = ret_dict["adjacencies"].setdefault(vlan_id, {})
                index_adjacencies["adj_id"] = int(dict_val["adj_id"])
                index_adjacencies["adj_key"] = dict_val["adj_key"]
                index_adjacencies["encap"] = dict_val["encap"]
                index_adjacencies["link"] = dict_val["link"]
                index_adjacencies["sihandle"] = dict_val["sihandle"]
                index_adjacencies["rihandle"] = dict_val["rihandle"]
                index_adjacencies["dihandle"] = dict_val["dihandle"]
                index_adjacencies["obj_type"] = dict_val["obj_type"]
                continue

        return ret_dict


# ======================================================
# Schema for 'show platform software fed switch {mode} matm stats'
# ======================================================
class ShowPlatformSoftwareFedSwitchMatmStatsSchema(MetaParser):
    """Schema for 'show platform software fed switch {mode} matm stats'"""

    schema = {
        "matm_counters": {Any(): int},
    }


# ======================================================
# Parser for 'show platform software fed switch {mode} matm stats'
# ======================================================
class ShowPlatformSoftwareFedSwitchMatmStats(
    ShowPlatformSoftwareFedSwitchMatmStatsSchema
):
    """Parser for 'show platform software fed switch {mode} matm stats'"""

    cli_command = [
        "show platform software fed active matm stats",
        "show platform software fed switch {mode} matm stats",
        "show platform software fed {act_mode} matm stats",
    ]

    def cli(self, mode=None, act_mode=None, output=None):
        if output is None:
            if mode:
                cmd = self.cli_command[1].format(mode=mode)
            elif act_mode:
                cmd = self.cli_command[2].format(act_mode=act_mode)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        #   Total non-cpu mac entries       : 3
        #   Mac Learn SPI Msg Count         : 0
        #   Mac Learn SPI Err Count         : 0
        p = re.compile(r"^(?P<key>[\S\s]+)\s+:\s+(?P<count>\d+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            #   Total non-cpu mac entries       : 3
            #   Mac Learn SPI Msg Count         : 0
            #   Mac Learn SPI Err Count         : 0
            m = p.match(line)
            if m:
                group = m.groupdict()
                key = (
                    group["key"]
                    .lower()
                    .strip()
                    .replace(" ", "_")
                    .replace("-", "_")
                    .replace("/", "_")
                )
                matm_dict = ret_dict.setdefault("matm_counters", {})
                matm_dict[key] = int(group["count"])
                continue

        return ret_dict


# ======================================================
# Parser for 'show platform software fed switch active matm adjacencies '
# ======================================================


class ShowPlatformSoftwareFedSwitchActiveMatmAdjacenciesSchema(MetaParser):
    """Schema for show platform software fed switch active matm adjacencies"""

    schema = {
        "adjacencies": {
            Any(): {
                "adj_id": int,
                "adj_key": str,
                "encap": str,
                "link": str,
                "sihandle": str,
                "rihandle": str,
                "dihandle": str,
                "obj_type": str,
            },
        },
    }


class ShowPlatformSoftwareFedSwitchActiveMatmAdjacencies(
    ShowPlatformSoftwareFedSwitchActiveMatmAdjacenciesSchema
):
    """Parser for show platform software fed switch active matm adjacencies"""

    cli_command = "show platform software fed switch active matm adjacencies"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # 201    89          0x100000059      VXLAN  V4     0x7fd728bf1be8   0x7fd728bf17a8   0x0              CP
        p2 = re.compile(
            r"^(?P<vlan>\d+)\s+(?P<adj_id>\d+)\s+(?P<adj_key>\S+)\s+(?P<encap>\w+)\s+(?P<link>\S+)\s+(?P<sihandle>\S+)\s+(?P<rihandle>\S+)\s+(?P<dihandle>\S+)\s+(?P<obj_type>\w+)$"
        )

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            # 201    89          0x100000059      VXLAN  V4     0x7fd728bf1be8   0x7fd728bf17a8   0x0              CP
            m = p2.match(line)
            if m:
                dict_val = m.groupdict()
                adjacencies = ret_dict.setdefault("adjacencies", {})
                vlan_id = int(dict_val["vlan"])
                index_adjacencies = ret_dict["adjacencies"].setdefault(vlan_id, {})
                index_adjacencies["adj_id"] = int(dict_val["adj_id"])
                index_adjacencies["adj_key"] = dict_val["adj_key"]
                index_adjacencies["encap"] = dict_val["encap"]
                index_adjacencies["link"] = dict_val["link"]
                index_adjacencies["sihandle"] = dict_val["sihandle"]
                index_adjacencies["rihandle"] = dict_val["rihandle"]
                index_adjacencies["dihandle"] = dict_val["dihandle"]
                index_adjacencies["obj_type"] = dict_val["obj_type"]
                continue

        return ret_dict


class ShowPlatformSoftwareFedSwitchActiveMatmMacTableVlanMacSchema(MetaParser):
    """
    Schema for
        * 'show platform software fed {switch} {active} matm macTable vlan {vlan} mac {mac}'
    """

    schema = {
        "vlan": {
            Any(): {
                "mac": str,
                "type": str,
                "seq": int,
                "ec_bi": int,
                "flags": int,
                "machandle": str,
                "siHandle": str,
                "riHandle": str,
                "diHandle": str,
                "a_time": int,
                "e_time": int,
                "port": str,
                "con": str,
            }
        },
        "platform_details": {
            "asic": {
                Any(): {
                    Optional("htmhandle"): str,
                    Optional("mvid"): int,
                    Optional("gpn"): int,
                    Optional("si"): str,
                    Optional("ri"): str,
                    Optional("di"): str,
                    Optional("pmap"): str,
                    Optional("pmap_intf"): str,
                }
            }
        },
    }


class ShowPlatformSoftwareFedSwitchActiveMatmMacTableVlanMac(
    ShowPlatformSoftwareFedSwitchActiveMatmMacTableVlanMacSchema
):
    """
    Parser for
        * 'show platform software fed {switch} {active} matm macTable vlan {vlan} mac {mac}'
    """

    cli_command = [
        "show platform software fed {state} matm macTable vlan {vlan} mac {mac}",
        "show platform software fed {switch} {state} matm macTable vlan {vlan} mac {mac}",
    ]

    def cli(self, vlan, mac, state, switch=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[1].format(
                    switch=switch, state=state, vlan=vlan, mac=mac
                )
            else:
                cmd = self.cli_command[0].format(state=state, vlan=vlan, mac=mac)
            output = self.device.execute(cmd)

        # VLAN   MAC                  Type  Seq#    EC_Bi  Flags  machandle           siHandle            riHandle            diHandle              *a_time  *e_time  ports                                                         Con
        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # 1      2200.0000.0001        0x1  125648      0      0  0x7429b62dc7c8      0x742904fc2428      0x0                 0x7429b53219d8            300       90  TwoGigabitEthernet1/0/13                                      Yes
        p1 = re.compile(
            r"^(?P<vlan>\d+)\s+(?P<mac>\S+)\s+(?P<type>\S+)\s+(?P<seq>\d+)\s+(?P<ec_bi>\d+)\s+(?P<flags>\d+)\s+(?P<machandle>\S+)\s+(?P<siHandle>\S+)\s+(?P<riHandle>\S+)\s+(?P<diHandle>\S+)\s+(?P<a_time>\d+)\s+(?P<e_time>\d+)\s+(?P<port>\S+)\s+(?P<con>\w+)$"
        )

        # Asic: 0
        p2 = re.compile(r"^Asic\:\s+(?P<asic>\S+)$")

        # htm-handle = 0x7429b56aaa48 MVID = 4 gpn = 1
        p3 = re.compile(
            r"^htm-handle\s+=\s+(?P<htmhandle>\S+)\s+MVID\s+=\s+(?P<mvid>\d+)\s+gpn\s+=\s+(?P<gpn>\d+)$"
        )

        # SI = 0xad RI = 0x2 DI = 0x5415
        p4 = re.compile(
            r"^SI\s+=\s+(?P<si>\S+)\s+RI\s+=\s+(?P<ri>\S+)\s+DI\s+=\s+(?P<di>\S+)$"
        )

        # DI = 0x5415 pmap = 0x00000000 0x00000000 pmap_intf : [TwoGigabitEthernet1/0/13]
        p5 = re.compile(
            r"^DI\s+=\s+(?P<di>\S+)\s+pmap\s+=\s+(?P<pmap>\S+\s+\S+)(\s+pmap_intf\s+:\s+\[(?P<pmap_intf>\S+)\])?$"
        )

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            # VLAN   MAC                  Type  Seq#    EC_Bi  Flags  machandle           siHandle            riHandle            diHandle              *a_time  *e_time  ports                                                         Con
            # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            # 1      2200.0000.0001        0x1  125648      0      0  0x7429b62dc7c8      0x742904fc2428      0x0                 0x7429b53219d8            300       90  TwoGigabitEthernet1/0/13                                      Yes
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vlan_id = group["vlan"]
                vlan_dict = ret_dict.setdefault("vlan", {}).setdefault(vlan_id, {})
                vlan_dict.update(
                    {
                        "mac": group["mac"],
                        "type": group["type"],
                        "seq": int(group["seq"]),
                        "ec_bi": int(group["ec_bi"]),
                        "flags": int(group["flags"]),
                        "machandle": group["machandle"],
                        "siHandle": group["siHandle"],
                        "riHandle": group["riHandle"],
                        "diHandle": group["diHandle"],
                        "a_time": int(group["a_time"]),
                        "e_time": int(group["e_time"]),
                        "port": Common.convert_intf_name(group["port"]),
                        "con": group["con"],
                    }
                )
                continue

            # Asic: 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                asic = group["asic"]
                asic_dict = (
                    ret_dict.setdefault("platform_details", {})
                    .setdefault("asic", {})
                    .setdefault(asic, {})
                )
                continue

            # htm-handle = 0x7429b56aaa48 MVID = 4 gpn = 1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                asic_dict["htmhandle"] = group["htmhandle"]
                asic_dict["mvid"] = int(group["mvid"])
                asic_dict["gpn"] = int(group["gpn"])
                continue

            # SI = 0xad RI = 0x2 DI
            m = p4.match(line)
            if m:
                group = m.groupdict()
                asic_dict["si"] = group["si"]
                asic_dict["ri"] = group["ri"]
                continue

            # DI = 0x5415 pmap = 0x00000000 0x00000000 pmap_intf : [TwoGigabitEthernet1/0/13]
            m = p5.match(line)
            if m:
                group = m.groupdict()
                asic_dict["di"] = group["di"]
                asic_dict["pmap"] = group["pmap"]
                if group["pmap_intf"]:
                    asic_dict["pmap_intf"] = Common.convert_intf_name(
                        group["pmap_intf"]
                    )
                continue

        return ret_dict


# ======================================================
# Schema for 'show platform software fed switch active matm macTable'
# ======================================================
class ShowPlatformSoftwareFedSwitchActiveMatmMactableSchema(MetaParser):
    """Schema for show platform software fed switch active matm macTable"""

    schema = {
        "vlan": {
            Any(): {
                "mac": {
                    Any(): {
                        "type": str,
                        "seq": int,
                        "ecbi": int,
                        "flags": int,
                        "machandle": str,
                        "sihandle": str,
                        "rihandle": str,
                        "dihandle": str,
                        "atime": int,
                        "etime": int,
                        "ports": str,
                        "con": str,
                    },
                },
            },
        },
        "number_of_address": int,
        "number_of_secure_address": int,
        "number_of_drop_address": int,
        "number_of_local_lisp_address": int,
        "number_of_remote_lisp_address": int,
    }


# ======================================================
# Parser for 'show platform software fed switch active matm macTable'
# ======================================================
class ShowPlatformSoftwareFedSwitchActiveMatmMactable(
    ShowPlatformSoftwareFedSwitchActiveMatmMactableSchema
):
    """Parser for show platform software fed switch active matm macTable"""

    cli_command = ["show platform software fed switch active matm macTable"]

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # VLAN    MAC               Type      Seq#    EC_Bi    Flags    machandle         siHandle          riHandle    diHandle    *a_time    *e_time      ports    Con
        # ---------------------------------------------------------------------------------------------------------------------------------------------------------------
        # 1       7061.7bb8.c3e7    0x8002    0       0        64       0x71450c35a508    0x71450c355218    0x0         0x0          0          0           Vlan1    Yes
        p1 = re.compile(
            r"^(?P<vlan>[\d\-\,]+)\s+(?P<mac>([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4})+\s+(?P<type>0x[\w]+)\s+(?P<seq>\d+)\s+(?P<ecbi>\d+)\s+(?P<flags>\d+)\s+(?P<machandle>0x[\w]+)\s+(?P<sihandle>0x[\w]+)\s+(?P<rihandle>0x[\w]+)\s+(?P<dihandle>0x[\w]+)\s+(?P<atime>\d+)\s+(?P<etime>\d+)\s+(?P<ports>[\w\/\.\-\:]+)\s+(?P<con>\w+)$"
        )

        # Total Mac number of addresses:: 4
        p2 = re.compile(
            r"^Total Mac number of addresses:: (?P<number_of_address>(\d+))?"
        )

        # Total number of secure addresses:: 0
        p3 = re.compile(
            r"^Total number of secure addresses:: (?P<number_of_secure_address>(\d+))?"
        )

        # Total number of drop addresses:: 0
        p4 = re.compile(
            r"^Total number of drop addresses:: (?P<number_of_drop_address>(\d+))?"
        )

        # Total number of lisp local addresses:: 0
        p5 = re.compile(
            r"^Total number of lisp local addresses:: (?P<number_of_local_lisp_address>(\d+))?"
        )

        # Total number of lisp remote addresses:: 0
        p6 = re.compile(
            r"^Total number of lisp remote addresses:: (?P<number_of_remote_lisp_address>(\d+))?"
        )

        for line in output.splitlines():
            # Removes any trailing or leading spaces
            line = line.strip()

            # Checks for the table data
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vlan_dict = (
                    ret_dict.setdefault("vlan", {})
                    .setdefault(group["vlan"], {})
                    .setdefault("mac", {})
                    .setdefault(group["mac"], {})
                )
                vlan_dict.update(
                    {
                        "type": group["type"],
                        "seq": int(group["seq"]),
                        "ecbi": int(group["ecbi"]),
                        "flags": int(group["flags"]),
                        "machandle": group["machandle"],
                        "sihandle": group["sihandle"],
                        "rihandle": group["rihandle"],
                        "dihandle": group["dihandle"],
                        "atime": int(group["atime"]),
                        "etime": int(group["etime"]),
                        "ports": group["ports"],
                        "con": group["con"],
                    }
                )
                continue

            # Total Mac number of addresses:: 4
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict["number_of_address"] = int(group["number_of_address"])
                continue

            # Total number of secure addresses:: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict["number_of_secure_address"] = int(
                    group["number_of_secure_address"]
                )
                continue

            # Total number of drop addresses:: 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict["number_of_drop_address"] = int(
                    group["number_of_drop_address"]
                )
                continue

            # Total number of lisp local addresses:: 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict["number_of_local_lisp_address"] = int(
                    group["number_of_local_lisp_address"]
                )
                continue

            # Total number of lisp remote addresses:: 0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict["number_of_remote_lisp_address"] = int(
                    group["number_of_remote_lisp_address"]
                )
                continue

        return ret_dict

class ShowPlatformSoftwareFedActiveMatmMacTableVlanMacDetailSchema(MetaParser):
    """
    Schema for show platform software fed switch active matm macTable vlan {vlan} mac {dynamic_mac} detail
    """
    schema = {
        Optional('vlan_dict'):{
              Optional('vlan'): int,                          
              Optional('mac'): str,
              Optional('type'): str,
              Optional('seq'): int,  
              Optional('ec_bi'): int,
              Optional('flags'): int,
              Optional('mac_handle'): str,
              Optional('si_handle'): str,
              Optional('ri_handle'): str,
              Optional('di_handle'): str,
              Optional('a_time'): int,
              Optional('e_time'): int,
              Optional('ports'): str,
              Optional('con'): str,                   
            },
        Optional('plat_software'):{
            Optional('l2_port_details'):{
                Optional('l2_service_port_oid'): int,
                Optional('l2_service_port_gid'): int,
             },
        },
        Optional('plat_hardware'):{
            Optional('l2_port_details'):{
               Optional('l2_service_port_oid'): int,
                Optional('l2_service_port_gid'): int,
            },
            Optional('l2_port_oid_details'): {
            Optional('ether_port_oid'): int,
            Optional('port_type'): str,
            Optional('spa_port_gid'): int,
            Optional('spa_port_oid'): int,
            Optional('stp_type'): str,
            Optional('vlan_bd_gid'): int,
            Optional('vlan_bd_oid'): int,
            },
        }, 
        Optional('npl_hardware_info'): {
            Optional('dest_id'): int,
            Optional('intf_details'): str,
            Optional('mac_addr'): str,
            Optional('relay_id'): int,
            Optional('tag_type'): str
         }, 
    }

class ShowPlatformSoftwareFedActiveMatmMacTableVlanMacDetail(ShowPlatformSoftwareFedActiveMatmMacTableVlanMacDetailSchema):
    """
    show platform software fed switch active matm macTable vlan {vlan} mac {dynamic_mac} detail
    """
          
    cli_command = ['show platform software fed {mode} matm macTable vlan {vlan_id} mac {dynamic_mac} detail',
                   'show platform software fed {switch} {mode} matm macTable vlan {vlan_id} mac {dynamic_mac} detail'
                  ]

    def cli(self, vlan_id, dynamic_mac, mode, switch=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[1].format(switch=switch, mode=mode, vlan_id=vlan_id, dynamic_mac=dynamic_mac)
            else:
                cmd = self.cli_command[0].format(mode=mode, vlan_id=vlan_id, dynamic_mac=dynamic_mac)
            output = self.device.execute(cmd)
            
        ret_dict = {}
        
        # VLAN  MAC             Type Seq#    EC_Bi Flags  machandle  siHandle  riHandle  diHandle  *a_time  *e_time   ports  Con   
        # --------------------------------------------------------------------------------------------------------------------------------------------
        # 300   0030.8200.21e7  0x1  166464  2     8      0x0        0x0       0x0       0x0       300      191227           No   
        p0 = re.compile(r'^(?P<vlan>\d+)\s+(?P<mac>\S+)\s+(?P<type>\S+)\s+(?P<seq>\d+)\s+(?P<ec_bi>\d+)\s+(?P<flags>\d+)\s+(?P<mac_handle>\S+)\s+(?P<si_handle>\S+)\s+(?P<ri_handle>\S+)\s+(?P<di_handle>\S+)\s+(?P<a_time>\d+)\s+(?P<e_time>\d+)\s+(?P<ports>\d+|\s+)\s+(?P<con>\w+)$')
        
        # ======platform software details ======
        p1 = re.compile(r'^======platform software details ======$')

        # L2 Service Port OID.........[9333]
        p2 = re.compile(r'^L2 Service Port OID\.*\[(?P<l2_service_port_oid>\d+)\]$')
        
        # L2 Service Port GID.........[4266]
        p3 = re.compile(r'^L2 Service Port GID\.*\[(?P<l2_service_port_gid>\d+)\]$')
        
        # ======platform hardware details ======
        p4 = re.compile(r'^======platform hardware details ======$')
        
        # Age Value...................[60]
        p5 = re.compile(r'^\s+Age Value\.*\[(?P<age_value>\d+)\]$')
        
        # Age Remaining...............[0]
        p6 = re.compile(r'^\s+Age Remaining\.*\[(?P<age_remaining>\d+)\]$')
        
        # -------- L2 Service port OID Info --------
        p7 = re.compile(r'^-------- L2 Service port OID Info --------$')
        
        # Port Type: AC Port
        p8 = re.compile(r'^Port Type:\s+(?P<port_type>(.*))$')
        
        # STP Type: Forwarding      
        p9 = re.compile(r'^STP Type:\s+(?P<stp_type>\S+)$')
        
        # VLAN(BD) OID................[1270]
        p10 = re.compile(r'^VLAN\(BD\) OID\.*\[(?P<vlan_bd_oid>\d+)\]$')
        
        # VLAN(BD) GID................[300]
        p11 = re.compile(r'^VLAN\(BD\) GID\.*\[(?P<vlan_bd_gid>\d+)\]$')
        
        # Ethernet Port OID...........[11059]
        p12 = re.compile(r'^Ethernet Port OID\.*\[(?P<ether_port_oid>\d+)\]$')
        
        # SPA Port OID................[11058]
        p13 = re.compile(r'^SPA Port OID\.*\[(?P<spa_port_oid>\d+)\]$')
        
        # SPA Port GID................[310]
        p14 = re.compile(r'^SPA Port GID\.*\[(?P<spa_port_gid>\d+)\]$')
        
        # ====== NPL Hardware Information ======
        p15 = re.compile(r'^====== NPL Hardware Information ======$')
        
        # MAC address: 00a7.429b.dae3
        p16 = re.compile(r'^MAC address:\s+(?P<mac_addr>\S+)$')
        
        # Relay ID: 100
        p17 = re.compile(r'^Relay ID:\s+(?P<relay_id>\d+)$')
        
        # Tag Type: L2 DLP, Destination ID 4266       
        p18 = re.compile(r'^Tag Type:\s+(?P<tag_type>(.*))\,\s+Destination ID\s+(?P<dest_id>\d+)$')
        
        # Interface Details: Port-channel111
        p19 = re.compile(r'^Interface Details:\s+(?P<intf_details>\S+)$')
       
        for line in output.splitlines(): 
            line = line.strip()   

            # VLAN  MAC             Type Seq#    EC_Bi Flags  machandle  siHandle  riHandle  diHandle  *a_time  *e_time   ports  Con   
            # ----------------------------------------------------------------------------------------------------------------------------------------
            # 300   0030.8200.21e7  0x1  166464  2     8      0x0        0x0       0x0       0x0       300      191227           No
            m = p0.match(line)
            if m:
                group = m.groupdict()
                vlan_dict = ret_dict.setdefault('vlan_dict', {})
                vlan_dict.update({
                    'vlan': int(group['vlan']),
                    'mac': group['mac'],
                    'type': group['type'],
                    'seq': int(group['seq']),
                    'ec_bi': int(group['ec_bi']),
                    'flags': int(group['flags']),
                    'mac_handle': group['mac_handle'],
                    'si_handle': group['si_handle'],
                    'ri_handle': group['ri_handle'],
                    'di_handle': group['di_handle'],
                    'a_time': int(group['a_time']),
                    'e_time': int(group['e_time']),
                    'ports': group['ports'],
                    'con': group['con'],
                })
                continue
            
            # ======platform software details ======    
            m = p1.match(line)
            if m:
                group = m.groupdict()
                plat_software = ret_dict.setdefault('plat_software', {})
                l2_port_details = plat_software.setdefault('l2_port_details', {})
                continue

            # L2 Service Port OID.........[9333]
            m = p2.match(line)
            if m:
                group = m.groupdict()
                l2_port_details.update({
                'l2_service_port_oid': int(group['l2_service_port_oid']),
                })
                continue
            
            # L2 Service Port GID.........[4266]
            m = p3.match(line)
            if m:
                group = m.groupdict()
                l2_port_details['l2_service_port_gid'] = int(group['l2_service_port_gid'])
                continue
            
            # ======platform hardware details ======    
            m = p4.match(line)
            if m:
                group = m.groupdict()
                plat_hardware = ret_dict.setdefault('plat_hardware', {})
                l2_port_details = plat_hardware.setdefault('l2_port_details', {})
                continue
            
            # Age Value...................[60]
            m = p5.match(line)
            if m:
                group = m.groupdict()
                plat_hardware['age_value'] = int(group['age_value'])
                continue
            
            # Age Remaining...............[0]
            m = p6.match(line)
            if m:
                group = m.groupdict()
                plat_hardware['age_remaining'] = int(group['age_remaining'])
                continue
            
            # -------- L2 Service port OID Info --------    
            m = p7.match(line)
            if m:
                group = m.groupdict()
                plat_hardware = ret_dict.setdefault('plat_hardware', {})
                l2_port_oid_details = plat_hardware.setdefault('l2_port_oid_details', {})
                continue  
            
            # Port Type: AC Port    
            m = p8.match(line)
            if m:
                group = m.groupdict()
                l2_port_oid_details['port_type'] = group['port_type']
                continue  
             
            # STP Type: Forwarding     
            m = p9.match(line)
            if m:
                group = m.groupdict()
                l2_port_oid_details['stp_type'] = group['stp_type']
                continue  
            
            # VLAN(BD) OID................[1270]    
            m = p10.match(line)
            if m:
                group = m.groupdict()
                l2_port_oid_details['vlan_bd_oid'] = int(group['vlan_bd_oid'])
                continue  
            
            # VLAN(BD) GID................[300]    
            m = p11.match(line)
            if m:
                group = m.groupdict()
                l2_port_oid_details['vlan_bd_gid'] = int(group['vlan_bd_gid'])
                continue  
            
            # Ethernet Port OID...........[11059]    
            m = p12.match(line)
            if m:
                group = m.groupdict()
                l2_port_oid_details['ether_port_oid'] = int(group['ether_port_oid'])
                continue  
            
            # SPA Port OID................[11058]    
            m = p13.match(line)
            if m:
                group = m.groupdict()
                l2_port_oid_details['spa_port_oid'] = int(group['spa_port_oid'])
                continue  
            
            # SPA Port GID................[310]    
            m = p14.match(line)
            if m:
                group = m.groupdict()
                l2_port_oid_details['spa_port_gid'] = int(group['spa_port_gid'])
                continue  
           
            # ====== NPL Hardware Information ======
            m = p15.match(line)
            if m:
                group = m.groupdict()
                npl_hardware_info = ret_dict.setdefault('npl_hardware_info', {})
                continue 
            
            # MAC address: 00a7.429b.dae3    
            m = p16.match(line)
            if m:
                group = m.groupdict()
                npl_hardware_info['mac_addr'] = group['mac_addr']
                continue  
                
            # Relay ID: 100
            m = p17.match(line)
            if m:
                group = m.groupdict()
                npl_hardware_info['relay_id'] = int(group['relay_id'])
                continue  
            
            # Tag Type: L2 DLP, Destination ID 4266    
            m = p18.match(line)
            if m:
                group = m.groupdict()
                npl_hardware_info['tag_type'] = group['tag_type']
                npl_hardware_info['dest_id'] = int(group['dest_id'])
                continue  
             
            # Interface Details: Port-channel111   
            m = p19.match(line)
            if m:
                group = m.groupdict()
                npl_hardware_info['intf_details'] = group['intf_details']
                continue
                
        return ret_dict