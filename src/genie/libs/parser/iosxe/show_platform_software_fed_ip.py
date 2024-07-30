"""show_platform_software_fed_ip.py

    * 'show platform software fed {state} ip igmp snooping vlan {vlan}'
    * 'show platform software fed {state} ip igmp snooping groups vlan {vlan}'
    * 'show platform software fed {state} ipv6 mld snooping groups vlan {vlan}'
    * 'show platform software fed {state} ipv6 mld snooping vlan {vlan}'
    * 'show platform software fed switch active ip adj'
    * 'show platform software fed switch active ip route detail'
    * 'show platform software fed switch active ip route'
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


# ================================================================
# Parser for show Platform Software Fed ipv6 mld snooping groups'
# ================================================================
class ShowPlatformSoftwareFedIpv6MldSnoopingGroupsVlanSchema(MetaParser):
    """Schema for show Platform Software Fed ipv6 mld snooping groups"""

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


class ShowPlatformSoftwareFedIpv6MldSnoopingGroupsVlan(
    ShowPlatformSoftwareFedIpv6MldSnoopingGroupsVlanSchema
):
    """Parser for show Platform Software Fed ipv6 mld snooping groups"""

    cli_command = (
        "show platform software fed {state} ipv6 mld snooping groups vlan {vlan}"
    )

    def cli(self, state="", vlan="", output=None):
        if output is None:
            output = self.device.execute(
                self.cli_command.format(state=state, vlan=vlan)
            )
        platform_dict = {}

        # Vlan:20 Group:ff1e::50
        # ---------------------------------
        # Member ports   :
        #     TenGigabitEthernet1/0/1
        #     nve1.VNI60020(0x200000063)

        # Vlan:20 Group:ff1e::50
        p0 = re.compile(r"(^Vlan:+(?P<vlan>\d+))+\s+(Group:+(?P<group>\w.*))")

        # Member ports :
        p1 = re.compile(r"(^Member+ +ports+   :+(?P<mem_port>.*))")
        # TenGigabitEthernet1/0/1
        p1_1 = re.compile("([A-Za-z]*\d[-().]*){10,}")
        # nve1.VNI60020(0x200000063)
        p1_2 = re.compile("^[A-Za-z]+[\d\/]+$")

        # CCK_epoch : 1
        p2 = re.compile(r"(^CCK_epoch+ +:+ +(?P<cck_ep>\d.*)$)")

        # Failure Flags : 0
        p3 = re.compile(r"(^Failure+ +Flags+ +:+ +(?P<fail_flag>\d.*)$)")

        # DI handle      : 0x7f4f6eb86dd8
        p4 = re.compile(r"(^DI+ +handle+ +:+ +(?P<di_hand>\w.*)$)")

        # REP RI handle  : 0x7f4f6eb87218
        p5 = re.compile(r"(^REP+ +RI+ +handle+ +:+ +(?P<rep_ri>\w.*)$)")

        # SI handle      : 0x7f4f6eb880b8
        p6 = re.compile(r"(^SI+ +handle+ +:+ +(?P<si_hand>\w.*)$)")

        # HTM handle     : 0x7f4f6eb883c8
        p7 = re.compile(r"(^HTM+ +handle+ +:+ +(?P<htm_hand>\w.*)$)")

        member_port_flag = 0
        member_list = []
        for line in output.splitlines():
            line = line.strip()

            # Vlan:20 Group:ff1e::50
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
            # TenGigabitEthernet1/0/1
            m = p1_1.match(line)
            if m:
                if member_port_flag == 1:
                    member_list.append(m.group(0))
            # nve1.VNI60020(0x200000063)
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

            # DI handle      : 0x7f4f6eb86dd8
            m = p4.match(line)
            if m:
                mac_dict["di_hand"] = m.groupdict()["di_hand"]
                continue

            # REP RI handle  : 0x7f4f6eb87218
            m = p5.match(line)
            if m:
                mac_dict["rep_ri"] = m.groupdict()["rep_ri"]
                continue

            # SI handle      : 0x7f4f6eb880b8
            m = p6.match(line)
            if m:
                mac_dict["si_hand"] = m.groupdict()["si_hand"]
                continue

            # HTM handle     : 0x7f4f6eb883c8
            m = p7.match(line)
            if m:
                mac_dict["htm_hand"] = m.groupdict()["htm_hand"]
                continue

        return platform_dict


# ======================================================================
# Parser for show Platform Software Fed active ipv6 mld snooping vlan'
# ======================================================================
class ShowPlatformSoftwareFedActiveIpv6MldSnoopingVlanSchema(MetaParser):
    """Schema for show Platform Software Fed active ipv6 mld snooping vlan"""

    schema = {
        "vlan": {
            Any(): {
                Optional("mldsn_en"): str,
                Optional("pimsn_en"): str,
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


class ShowPlatformSoftwareFedActiveIpv6MldSnoopingVlan(
    ShowPlatformSoftwareFedActiveIpv6MldSnoopingVlanSchema
):
    """Parser for show Platform Software Fed active ipv6 mld snooping vlan"""

    cli_command = "show platform software fed {state} ipv6 mld snooping vlan {vlan}"

    def cli(self, state="", vlan="", output=None):
        if output is None:
            output = self.device.execute(
                self.cli_command.format(state=state, vlan=vlan)
            )
        platform_dict = {}

        # Vlan 20
        # ---------
        # MLDSN Enabled : On
        # PIMSN Enabled : Off

        # Vlan 20
        p0 = re.compile(r"^Vlan\s+(?P<vlan>\d+)$")
        # MLDSN Enabled : On
        p1 = re.compile("MLDSN+  +Enabled  +: +(?P<mldsn_en>\w+)")

        # PIMSN Enabled : Off
        p2 = re.compile("PIMSN+ +Enabled+   +:+ +(?P<pimsn_en>\w+)")

        # Flood Mode : Off
        p3 = re.compile("Flood+ +Mode+      +:+(?P<flood_md>.*)")

        # Oper State : Up
        p4 = re.compile("Oper+ +State+    +:+ +(?P<op_state>\w+)")

        # STP TCN Flood : Off
        p5 = re.compile("STP+ +TCN+ +Flood+   +:+ +(?P<stp_tcn_flood>\w+)")

        # Routing Enabled : On
        p6 = re.compile("Routing+ +Enabled+ +:+ +(?P<route_en>\w+)")

        # PIM Enabled : On
        p7 = re.compile("PIM+ +Enabled+ +:+ +(?P<pim_en>\w+)")

        # PVLAN : No
        p8 = re.compile("PVLAN+ +:+ +(?P<pvlan>\w+)")

        # In Retry : 0x0
        p9 = re.compile("In+ +Retry+ +:+ +(?P<in_retry>\w+)")

        # CCK Epoch : 0x17
        p10 = re.compile("CCK+ +Epoch+ +:+ +(?P<cck_ep>\w+)")

        # IOSD Flood Mode : Off
        p11 = re.compile("IOSD+ +Flood+ +Mode+ :+ +(?P<iosd_md>\w+)")

        # EVPN Proxy Enabled : On
        p12 = re.compile("EVPN+ +Proxy+ +Enabled+ :+ +(?P<evpn_en>\w+)")

        # L3mcast Adj :
        p13 = re.compile("L3mcast+ +Adj+      :+(?P<l3m_adj>.*)")

        # Mrouter PortQ :
        p14 = re.compile("^Mrouter\s+PortQ\s+:\s*")
        # TenGigabitEthernet7/0/13
        p14_1 = re.compile("([A-Za-z]*\d[-().]*){10,}")

        # Flood PortQ :
        p15 = re.compile("^Flood PortQ\s+:\s*")
        # TenGigabitEthernet7/0/13
        # FiveGigabitEthernet1/0/2
        # GigabitEthernet2/0/31
        p15_1 = re.compile("^[A-Za-z]+[\d\/]+$")

        # REP RI handle : 0x0
        p16 = re.compile("REP+ +RI+ +handle+   :+(?P<rep_han>.*)")

        mroute_port_flag = 0
        mroute_list = []
        floodport_flag = 0
        floodport_list = []
        for line in output.splitlines():
            line = line.strip()
            # Vlan 20
            m = p0.match(line)
            if m:
                vlan = m.groupdict()["vlan"]
                mac_dict = platform_dict.setdefault("vlan", {}).setdefault(vlan, {})

            # MLDSN Enabled : On
            m = p1.match(line)
            if m:
                mac_dict["mldsn_en"] = m.groupdict()["mldsn_en"]
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
                # mac_dict['flood_port'] = p15
                continue

            # Mrouter PortQ :
            m = p14.match(line)
            if m:
                mac_dict["mroute_port"] = mroute_list
                mroute_port_flag = 1
                continue

            # TenGigabitEthernet7/0/13
            m = p14_1.match(line)
            if m:
                if mroute_port_flag == 1:
                    mroute_list.append(m.group(0))
                elif floodport_flag == 1:
                    floodport_list.append(m.group(0))

            # Flood PortQ :
            m = p15_1.match(line)
            if m:
                if mroute_port_flag == 1:
                    mroute_list.append(m.group(0))
                elif floodport_flag == 1:
                    floodport_list.append(m.group(0))

            # TenGigabitEthernet7/0/13
            # FiveGigabitEthernet1/0/2
            # GigabitEthernet2/0/31
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


class ShowPlatformSoftwareFedSwitchActiveIpRouteDetailSchema(MetaParser):
    """Schema for :
    * 'show platform software fed {switch} {mode} ip route {ip_add}'
    * 'show platform software fed {switch} {mode} ip route {ip_add} {detail}'
    """

    schema = {
        "ipv4_add": {
            Any(): {
                Optional("ipv4route_id"): str,
                Optional("obj_name"): str,
                Optional("obj_id"): str,
                Optional("tblid"): int,
                Optional("da"): int,
                Optional("state"): str,
                Optional("mac_addr"): str,
                Optional("adj"): {
                    Optional("objid"): str,
                    Optional("nh_type"): str,
                    Optional("ipv4_addr"): str,
                    Optional("iif_id"): str,
                    Optional("ether_type"): str,
                    Optional("srcmac"): str,
                    Optional("dstmac"): str,
                },
                Optional("npd"): {
                    Optional("child_device"): int,
                    Optional("nh_gid"): int,
                    Optional("nh_oid"): str,
                    Optional("old_gid"): int,
                    Optional("old_oid"): str,
                    Optional("parent_oid"): str,
                },
            },
        },
    }


class ShowPlatformSoftwareFedSwitchActiveIpRouteDetail(
    ShowPlatformSoftwareFedSwitchActiveIpRouteDetailSchema
):
    """Parser for
    * 'show platform software fed {switch} {mode} ip route {ip_add}'
    * 'show platform software fed {switch} {mode} ip route {ip_add} detail'
    """

    cli_command = [
        "show platform software fed {switch} {mode} ip route {ip_add}",
        "show platform software fed {switch} {mode} ip route {ip_add} {detail}",
    ]

    def cli(self, switch="", mode="", ip_add="", detail="", output=None):
        if output is None:
            if ip_add and detail:
                output = self.device.execute(
                    self.cli_command[1].format(
                        switch=switch, mode=mode, ip_add=ip_add, detail=detail
                    )
                )
            else:
                output = self.device.execute(
                    self.cli_command[0].format(switch=switch, mode=mode, ip_add=ip_add)
                )

        # Init vars
        ret_dict = {}
        ipv4_add_dict = {}

        # IPV4ROUTE_ID:id:0x5a4d1cf0f4d8 nobj:(IPNEXTHOP_ID,0x40) 2.2.2.3/32 tblid:0 DA:1
        p0 = re.compile(
            r"^IPV4ROUTE_ID:id:(?P<ipv4route_id>\w+)(?:\s+)nobj:\((?P<obj_name>\w+)(?:,)"
            r"(?P<obj_id>\w+)\)(?:\s+)(?P<ipv4_add>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})"
            r"(?:\s+)tblid:(?P<tblid>\d+)(?:\s+)DA:(?P<da>\d+)$"
        )

        # State:(0) success
        p1 = re.compile(r"^State:\(0\)\s+(?P<state>\w+)$")

        # Mac address of Host:00a7.429b.db7f
        p2 = re.compile(r"^Mac address of Host:(?P<mac_addr>\S+)$")

        # ADJ:objid:0x40 (IPv4: 2.2.2.3)  nh_type:NHADJ_NORMAL iif_id:0x553 ether_type:0x8 #child:2
        p3 = re.compile(
            r"^ADJ:objid:(?P<objid>\w+)\s+\(IPv4:\s+(?P<ipv4_addr>\S+)\)\s+nh_type:(?P<nh_type>\w+)\s+"
            r"iif_id:(?P<iif_id>\w+)\s+ether_type:(?P<ether_type>\w+)\s+#child:\d+$"
        )

        # srcmac:40b5.c1ff.d902 dstmac:00a7.429b.db7f
        p4 = re.compile(
            r"^srcmac:(?P<srcmac>([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4})\s+dstmac:(?P<dstmac>([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4})$"
        )

        # NPD: device:0 nh_gid/oid:8/0x466 old_gid/oid:0/0x0 parent_oid:0x6e6
        p5 = re.compile(
            r"^NPD:\s+device:(?P<child_device>\d+)\s+nh_gid\/oid:(?P<nh_gid>\d+)\/(?P<nh_oid>\w+)\s+"
            r"old_gid\/oid:(?P<old_gid>\d+)\/(?P<old_oid>\w+)\s+parent_oid:(?P<parent_oid>\w+)$"
        )

        for line in output.splitlines():
            line = line.strip()
            # IPV4ROUTE_ID:id:0x5b36201d0608 nobj:(PUSH_COUNTER,418) 20.1.1.123/32 tblid:2 DA:0
            m = p0.match(line)
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
                        "obj_id": str(groups["obj_id"]),
                        "tblid": int(groups["tblid"]),
                        "da": int(groups["da"]),
                    }
                )
                continue

            # Mac address of Host:00a7.429b.db7f
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                ipv4_add_dict.update(
                    {
                        "state": str(groups["state"]),
                    }
                )
                continue

            # Mac address of Host:00a7.429b.db7f
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                ipv4_add_dict.update(
                    {
                        "mac_addr": str(groups["mac_addr"]),
                    }
                )
                continue

            # ADJ:objid:0x40 (IPv4: 2.2.2.3)  nh_type:NHADJ_NORMAL iif_id:0x553 ether_type:0x8 #child:2
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                adj_dict = ipv4_add_dict.setdefault("adj", {})
                adj_dict.update(
                    {
                        "objid": str(groups["objid"]),
                        "nh_type": str(groups["nh_type"]),
                        "ipv4_addr": str(groups["ipv4_addr"]),
                        "iif_id": str(groups["iif_id"]),
                        "ether_type": str(groups["ether_type"]),
                    }
                )
                continue

            # srcmac:40b5.c1ff.d902 dstmac:00a7.429b.db7f
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                adj_dict = ipv4_add_dict.setdefault("adj", {})
                adj_dict.update(
                    {
                        "srcmac": str(groups["srcmac"]),
                        "dstmac": str(groups["dstmac"]),
                    }
                )
                continue

            # NPD: device:0 nh_gid/oid:8/0x466 old_gid/oid:0/0x0 parent_oid:0x6e6
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                npd_dict = ipv4_add_dict.setdefault("npd", {})
                npd_dict.update(
                    {
                        "child_device": int(groups["child_device"]),
                        "nh_gid": int(groups["nh_gid"]),
                        "nh_oid": str(groups["nh_oid"]),
                        "old_gid": int(groups["old_gid"]),
                        "old_oid": str(groups["old_oid"]),
                        "parent_oid": str(groups["parent_oid"]),
                    }
                )
                continue

        return ret_dict


class ShowPlatformSoftwareFedSwitchActiveIpRouteSchema(MetaParser):
    """
    Schema for show platform software fed switch active ip route
    """

    schema = {
        "index": {
            Any(): {
                "object_id": str,
                "ipv4_addr": str,
                "mask_len": int,
                "parent_type": str,
                "parent_object_id": str,
            },
        },
        "number_of_npi_ipv4route_entries": int,
    }


class ShowPlatformSoftwareFedSwitchActiveIpRoute(
    ShowPlatformSoftwareFedSwitchActiveIpRouteSchema
):
    """
    show platform software fed switch active ip route
    """

    cli_command = ["show platform software fed {switch} {mode} ip route"]

    def cli(self, switch=None, mode=None, output=None):
        if output is None:
            if switch and mode:
                cmd = self.cli_command[0].format(switch=switch, mode=mode)

            output = self.device.execute(cmd)

        ret_dict = {}
        index = 1
        index_dict = {}

        # Object ID           IPv4 Address        Mask Length         Parent Type         Parent ObjectID
        # 0x564ecc0889e8      127.0.0.0           8                   DROP                0x0
        p0 = re.compile(
            r"^(?P<object_id>\w+)\s+(?P<ipv4_addr>\S+)\s+(?P<mask_len>\S+)\s+(?P<parent_type>\S+)\s+(?P<parent_object_id>\S+)$"
        )

        # Number of npi_ipv4route entries = 6
        p1 = re.compile(
            r"^Number of npi_ipv4route entries = +(?P<number_of_npi_ipv4route_entries>\d+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # Object ID           IPv4 Address        Mask Length         Parent Type         Parent ObjectID
            # 0x564ecc0889e8      127.0.0.0           8                   DROP                0x0
            m = p0.match(line)
            if m:
                group = m.groupdict()
                index_dict = ret_dict.setdefault("index", {}).setdefault(index, {})
                index_dict.update(
                    {
                        "object_id": group["object_id"],
                        "ipv4_addr": group["ipv4_addr"],
                        "mask_len": int(group["mask_len"]),
                        "parent_type": group["parent_type"],
                        "parent_object_id": group["parent_object_id"],
                    }
                )
                index += 1
                continue

            # Number of npi_ipv4route entries = 6
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict["number_of_npi_ipv4route_entries"] = int(
                    group["number_of_npi_ipv4route_entries"]
                )
                continue

        return ret_dict


class ShowPlatformSoftwareFedSwitchActiveIpAdjSchema(MetaParser):
    """
    Schema for show platform software fed switch active ip adj
    """

    schema = {
        "index": {
            Any(): {
                "adjacency_id": str,
                "adjacency_ip_addr": str,
                "dest_mac": str,
                "nexthop_type": str,
                "interface": str,
            },
        },
        "number_of_adjacency_entries": int,
    }


class ShowPlatformSoftwareFedSwitchActiveIpAdj(
    ShowPlatformSoftwareFedSwitchActiveIpAdjSchema
):
    """
    show platform software fed switch active ip adj
    """

    cli_command = [
        "show platform software fed {switch} {mode} ip adj",
        "show platform software fed {switch} {mode} ip adj {ip_addr}",
        "show platform software fed {switch} {mode} ip adj {ip_addr} {detail}",
    ]

    def cli(self, switch=None, mode=None, ip_addr=None, detail=None, output=None):
        if output is None:
            if switch and mode and ip_addr and detail:
                cmd = self.cli_command[2].format(
                    switch=switch, mode=mode, ip_addr=ip_addr, detail=detail
                )
            elif switch and mode and ip_addr:
                cmd = self.cli_command[1].format(
                    switch=switch, mode=mode, ip_addr=ip_addr
                )
            else:
                cmd = self.cli_command[0].format(switch=switch, mode=mode)
            output = self.device.execute(cmd)

        ret_dict = {}
        index = 1
        index_dict = {}

        # Adjacency ID        Adjacency IPAddress                     Dest MacAddr        Nexthop Type        Interface
        # 0xb                 10.1.1.2                                8024.8f24.4902      NORMAL              Port-channel241
        p0 = re.compile(
            r"^(?P<adjacency_id>\w+)\s+(?P<adjacency_ip_addr>\S+)\s+(?P<dest_mac>\S+)\s+(?P<nexthop_type>\S+)\s+(?P<interface>\S+)$"
        )

        # Number of IPv4 Adjacency entries: 1
        p1 = re.compile(
            r"^Number of IPv4 Adjacency entries: +(?P<number_of_adjacency_entries>\d+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # Adjacency ID        Adjacency IPAddress                     Dest MacAddr        Nexthop Type        Interface
            # 0xb                 10.1.1.2                                8024.8f24.4902      NORMAL              Port-channel241
            m = p0.match(line)
            if m:
                group = m.groupdict()
                index_dict = ret_dict.setdefault("index", {}).setdefault(index, {})
                index_dict["adjacency_id"] = group["adjacency_id"]
                index_dict["adjacency_ip_addr"] = group["adjacency_ip_addr"]
                index_dict["dest_mac"] = group["dest_mac"]
                index_dict["nexthop_type"] = group["nexthop_type"]
                index_dict["interface"] = group["interface"]
                index += 1
                continue

            # Number of IPv4 Adjacency entries: 1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict["number_of_adjacency_entries"] = int(
                    group["number_of_adjacency_entries"]
                )
                continue

        return ret_dict


