"""show_platform_software_fed_ip.py

    * 'show platform software fed {state} ip igmp snooping vlan {vlan}'
    * 'show platform software fed {state} ip igmp snooping groups vlan {vlan}'
    * 'show platform software fed {state} ipv6 mld snooping groups vlan {vlan}'
    * 'show platform software fed {state} ipv6 mld snooping vlan {vlan}'
    * 'show platform software fed switch active ip adj'
    * 'show platform software fed switch active ip route detail'
    * 'show platform software fed switch active ip route'
    * 'show platform software fed {switch_var} {state} ipv6 mld snooping vlan {vlan}'
    * 'show platform software fed {state} ipv6 mld snooping vlan {vlan} detail'
    * 'show platform software fed {switch_var} {state} ipv6 mld snooping vlan {vlan} detail'
    * 'show platform software fed {switch_var} {state} ipv6 mfib count'
    * 'show platform software fed {state} ipv6 mfib count'
    * 'show platform software fed {switch_var} {state} ipv6 mfib summary'
    * 'show platform software fed {state} ipv6 mfib summary'
    * 'show platform software fed {switch_var} {state} ipv6 mld snooping summary'
    * 'show platform software fed {state} ipv6 mld snooping summary'
    * 'show platform software fed {switch_var} {state} ip mfib vrf {vrf_name} count'
    * 'show platform software fed {state} ip mfib vrf {vrf_name} count'
    * 'show platform software fed {switch_var} {state} ip igmp snooping summary'
    * 'show platform software fed {state} ip igmp snooping summary'
    * 'show ipv6 mld snooping address vlan {vlan} {group} summary'
    * 'show platform software fed {switch} {state} ip mfib count'
    * 'show platform software fed {state} ip mfib count'
    * 'show platform software fed {switch} {state} ip mfib summary'
    * 'show platform software fed {state} ip mfib summary'
    * 'show platform software fed {switch} {state} ip igmp snooping groups count'
    * 'show platform software fed {state} ip igmp snooping groups count'
    * 'show platform software fed switch {mode} ipv6 route'
    *'show platform software fed {switch} {module} ip igmp snooping group vlan {vlan_id} {group}',
    *'show platform software fed {switch} {module} ip igmp snooping group vlan {vlan_id} {group} detail'
"""
# Python
import re
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, ListOf

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
        p1_1 = re.compile(r"([A-Za-z]*\d[-().]*){10,}")
        # nve1.VNI60020(0x200000063)
        p1_2 = re.compile(r"^[A-Za-z]+[\d\/]+$")

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
                Optional("protocol"): str,
                Optional("snoop_state"): str,
                Optional("secondary_vlan"): str,
                Optional("vlan_urid"): str,
                Optional("d_users_count"): str,
            }
        }
    }

class ShowPlatformSoftwareFedActiveIpv6MldSnoopingVlan(
    ShowPlatformSoftwareFedActiveIpv6MldSnoopingVlanSchema
):
    """Parser for show Platform Software Fed active ipv6 mld snooping vlan"""

    cli_command = [
        "show platform software fed {switch_var} {state} ipv6 mld snooping vlan {vlan}",
        "show platform software fed {state} ipv6 mld snooping vlan {vlan}",
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
        # MLDSN Enabled : On
        # PIMSN Enabled : Off

        # Vlan 20
        p0 = re.compile(r"^Vlan\s+(?P<vlan>\d+)$")

        # (ipv6, vlan: 13)
        p0_1 = re.compile(r'\(+(?P<protocol>\S+)+\,+\s+vlan\: +(?P<vlan>\d+)+\)')

        # Vlan: 13
        p0_2 = re.compile(r"^Vlan:\s+(?P<vlan>\d+)$")

        # MLDSN Enabled : On
        p1 = re.compile(r"MLDSN+  +Enabled  +: +(?P<mldsn_en>\w+)")

        # PIMSN Enabled : Off
        p2 = re.compile(r"PIMSN+ +Enabled+   +:+ +(?P<pimsn_en>\w+)")

        # Flood Mode : Off
        p3 = re.compile(r"Flood+ +Mode+      +:+(?P<flood_md>.*)")

        # Flood Mode              : OFF
        p3_1 = re.compile(r'^Flood\s+Mode\s+:\s+(?P<flood_md>[\s\w\s]+)$')

        # Oper State : Up
        p4 = re.compile(r"Oper+ +State+    +:+ +(?P<op_state>\w+)")

        # STP TCN Flood : Off
        p5 = re.compile(r"STP+ +TCN+ +Flood+   +:+ +(?P<stp_tcn_flood>\w+)")

        # STP TCN State           : OFF
        p5_1 = re.compile(r'^STP\s+TCN\s+(Flood|State)\s+:\s+(?P<stp_tcn_flood>[\s\w\s]+)$')

        # Routing Enabled : On
        p6 = re.compile(r"Routing+ +Enabled+ +:+ +(?P<route_en>\w+)")

        # PIM Enabled : On
        p7 = re.compile(r"PIM+ +Enabled+ +:+ +(?P<pim_en>\w+)")

        # Pim state               : ON
        p7_1 = re.compile(r'^Pim\s+state\s+:\s+(?P<pim_en>[\s\w\s]+)$')

        # PVLAN : No
        p8 = re.compile(r"PVLAN+ +:+ +(?P<pvlan>\w+)")

        # In Retry : 0x0
        p9 = re.compile(r"In+ +Retry+ +:+ +(?P<in_retry>\w+)")

        # CCK Epoch : 0x17
        p10 = re.compile(r"CCK+ +Epoch+ +:+ +(?P<cck_ep>\w+)")

        # IOSD Flood Mode : Off
        p11 = re.compile(r"IOSD+ +Flood+ +Mode+ :+ +(?P<iosd_md>\w+)")

        # IOS Flood Mode          : OFF
        p11_1 = re.compile(r'^IOS\s+Flood\s+Mode\s+:\s+(?P<iosd_md>[\s\w\s]+)$')

        # EVPN Proxy Enabled : On
        p12 = re.compile(r"EVPN+ +Proxy+ +Enabled+ :+ +(?P<evpn_en>\w+)")

        # Evpn Proxy              : OFF
        p12_1 = re.compile(r'^Evpn\s+Proxy\s+:\s+(?P<evpn_en>[\s\w\s]+)$')

        # L3mcast Adj :
        p13 = re.compile(r"L3mcast+ +Adj+      :+(?P<l3m_adj>.*)")

        # Mrouter PortQ :
        p14 = re.compile(r"^Mrouter\s+PortQ\s+:\s*")
        # TenGigabitEthernet7/0/13
        p14_1 = re.compile(r"([A-Za-z]*\d[-().]*){10,}")

        # Flood PortQ :
        p15 = re.compile(r"^Flood PortQ\s+:\s*")
        # TenGigabitEthernet7/0/13
        # FiveGigabitEthernet1/0/2
        # GigabitEthernet2/0/31
        p15_1 = re.compile(r"^[A-Za-z]+[\d\/]+$")

        # REP RI handle : 0x0
        p16 = re.compile(r"REP+ +RI+ +handle+   :+(?P<rep_han>.*)")

        # Snoop State             : ON
        p17 = re.compile(r'^Snoop\s+State\s+:\s+(?P<snoop_state>[\w\s]+)$')

        # Secondary Vlan          : NO
        p18 = re.compile(r'^Secondary\s+Vlan\s+:\s+(?P<secondary_vlan>[\s\w\s]+)$')

        # Vlan Urid               : 0x5000000000000008
        p19 = re.compile(r'^Vlan\s+Urid\s+:\s+(?P<vlan_urid>[\s\w\s]+)$')

        # Dependant users count   : 0
        p20 = re.compile(r'^Dependant\s+users\s+count\s+:\s+(?P<d_users_count>[\s\w\s]+)$')

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
                continue

            m = p0_1.match(line)
            if m:
                vlan = int(m.groupdict()['vlan'])
                mac_dict = platform_dict.setdefault('vlan', {}).setdefault(vlan, {})
                mac_dict['protocol'] = m.groupdict()['protocol']
                continue

            # Vlan: 13
            m = p0_2.match(line)
            if m:
                vlan = m.groupdict()["vlan"]
                mac_dict = platform_dict.setdefault("vlan", {}).setdefault(vlan, {})
                continue

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

            # Flood Mode              : OFF
            m = p3_1.match(line)
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

            # STP TCN State           : OFF
            m = p5_1.match(line)
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

            # Snoop State     : ON
            m = p17.match(line)
            if m:
                mac_dict['snoop_state'] = m.groupdict()['snoop_state']
                continue

            # Secondary Vlan          : NO
            m = p18.match(line)
            if m:
                mac_dict['secondary_vlan'] = m.groupdict()['secondary_vlan']
                continue

            # Vlan Urid               : 0x5000000000000008
            m = p19.match(line)
            if m:
                mac_dict['vlan_urid'] = m.groupdict()['vlan_urid']
                continue

            # Dependant users count   : 0
            m = p20.match(line)
            if m:
                mac_dict['d_users_count'] = m.groupdict()['d_users_count']
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
                Optional("device"): int,
                Optional("lspa_rec"): int,
                Optional("api_type"): int,
                Optional("state"): str,
                Optional("mac_addr"): str,
                Optional("l3port_oid"): str,
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
                    Optional("fec_oid"): int,
                    Optional("was_nor_nh"): int,
                    Optional("cr_def"): int,
                    Optional("stale"): int,
                    Optional("l3port_valid"): int,
                    Optional("child_device"): int,
                    Optional("nh_gid"): int,
                    Optional("nh_oid"): str,
                    Optional("old_gid"): int,
                    Optional("old_oid"): str,
                    Optional("parent_oid"): str,
                },
                Optional("cla_nhtype"): int,
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

        # NPD: device:0 lspa_rec:0 api_type:host(1)
        p2 = re.compile(r'NPD:\sdevice:(?P<device>\d+)\slspa_rec:(?P<lspa_rec>\d+)\sapi_type:route\((?P<api_type>\d+)\)$')

        # Mac address of Host:00a7.429b.db7f
        p3 = re.compile(r"^Mac address of Host:(?P<mac_addr>\S+)$")

        # Host L3Port OID:0x460
        p4 = re.compile(r"^Host L3Port OID:(?P<l3port_oid>\S+)$")

        # ADJ:objid:0x40 (IPv4: 2.2.2.3)  nh_type:NHADJ_NORMAL iif_id:0x553 ether_type:0x8 #child:2
        p5 = re.compile(
            r"^ADJ:objid:(?P<objid>\w+)\s+\(IPv4:\s+(?P<ipv4_addr>\S+)\)\s+nh_type:(?P<nh_type>\w+)\s+"
            r"iif_id:(?P<iif_id>\w+)\s+ether_type:(?P<ether_type>\w+)\s+#child:\d+$"
        )

        # srcmac:40b5.c1ff.d902 dstmac:00a7.429b.db7f
        p6 = re.compile(
            r"^srcmac:(?P<srcmac>([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4})\s+dstmac:(?P<dstmac>([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4})$"
        )
        # NPD: fec_oid:0 was_nor_nh:1 cr_def:0 stale:0 l3port_valid:1
        p7 = re.compile(r'NPD:\sfec_oid:(?P<fec_oid>\d+)\s+was_nor_nh:(?P<was_nor_nh>\d+)\s+cr_def:(?P<cr_def>\d+)\s+stale:(?P<stale>\d+)\s+l3port_valid:(?P<l3port_valid>\d+)$')



        # NPD: device:0 nh_gid/oid:8/0x466 old_gid/oid:0/0x0 parent_oid:0x6e6
        p8 = re.compile(
            r"^NPD:\s+device:(?P<child_device>\d+)\s+nh_gid\/oid:(?P<nh_gid>\d+)\/(?P<nh_oid>\w+)\s+"
            r"old_gid\/oid:(?P<old_gid>\d+)\/(?P<old_oid>\w+)\s+parent_oid:(?P<parent_oid>\w+)$"
        )

        #      SDK: cla_nhtype:0
        p9 = re.compile(r'SDK:\s+cla_nhtype:(?P<cla_nhtype>\d+)$')


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

            # State:(0) success
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                ipv4_add_dict.update(
                    {
                        "state": str(groups["state"]),
                    }
                )
                continue

            # NPD: device:0 lspa_rec:0 api_type:host(1)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ipv4_add_dict.update({
                    'device': int(group['device']),
                    'lspa_rec': int(group['lspa_rec']),
                    'api_type': int(group['api_type']),
                })
                continue

            # Mac address of Host:00a7.429b.db7f
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                ipv4_add_dict.update(
                    {
                        "mac_addr": str(groups["mac_addr"]),
                    }
                )
                continue

            # Host L3Port OID:0x460
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                ipv4_add_dict["l3port_oid"] = groups["l3port_oid"]
                continue

            # ADJ:objid:0x40 (IPv4: 2.2.2.3)  nh_type:NHADJ_NORMAL iif_id:0x553 ether_type:0x8 #child:2
            m = p5.match(line)
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
            m = p6.match(line)
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

            # NPD: fec_oid:0 was_nor_nh:1 cr_def:0 stale:0 l3port_valid:1
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                npd_dict = ipv4_add_dict.setdefault("npd", {})
                npd_dict.update(
                    {
                        "fec_oid": int(groups["fec_oid"]),
                        "was_nor_nh": int(groups["was_nor_nh"]),
                        "cr_def": int(groups["cr_def"]),
                        "stale": int(groups["stale"]),
                        "l3port_valid": int(groups["l3port_valid"]),
                    }
                )
                continue

            # NPD: device:0 nh_gid/oid:8/0x466 old_gid/oid:0/0x0 parent_oid:0x6e6
            m = p8.match(line)
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

            # SDK: cla_nhtype:0
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                ipv4_add_dict["cla_nhtype"] = int(groups["cla_nhtype"])

        return ret_dict


class ShowPlatformSoftwareFedSwitchActiveIpRouteSchema(MetaParser):
    """
    Schema for
    show platform software fed switch active ip route
    show platform software fed switch active ip route vrf {vrf_name}
    """

    schema = {
        "index": {
            Any(): {
                Optional("object_id"): str,
                "ipv4_addr": str,
                "mask_len": int,
                Optional("parent_type"): str,
                Optional("parent_object_id"): str,
                Optional("sgt"): int,
                Optional("vrf"): int,
                Optional("mpls"): int,
                Optional("htm"): str,
                Optional("flags"): str,
                Optional("dgid"): int,
                Optional("last_modified_year"): int,
                Optional("month"): int,
                Optional("date"): int,
                Optional("hours"): int,
                Optional("minutes"): int,
                Optional("seconds"): int,
                Optional("millseconds"): int,
                Optional("secssincehit"): int,
            },
        },
        Optional("number_of_npi_ipv4route_entries"): int,
    }


class ShowPlatformSoftwareFedSwitchActiveIpRoute(
    ShowPlatformSoftwareFedSwitchActiveIpRouteSchema
):
    """
    parser for
    show platform software fed switch active ip route
    show platform software fed switch active ip route vrf {vrf_name}
    """

    cli_command = ["show platform software fed {switch} {mode} ip route","show platform software fed {switch} {mode} ip route vrf {vrf_name}"]

    def cli(self, switch='', mode='', vrf_name='', output=None):
        if output is None:
            if vrf_name:
                cmd = self.cli_command[1].format(switch=switch, mode=mode, vrf_name=vrf_name)
            else:
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

        #Object ID           IPv4 Address        Mask Length         Parent Type         Parent ObjectID     SGT
        #0x5bb0d60dd878      100.60.2.200        32                  IPNEXTHOP_ID        0x5f                0
        p0_1 = re.compile(
            r"^(?P<object_id>\w+)\s+(?P<ipv4_addr>\S+)\s+(?P<mask_len>\d+)\s+(?P<parent_type>\S+)\s+(?P<parent_object_id>\S+)\s+(?P<sgt>\d+)$"
        )

        # Number of npi_ipv4route entries = 6
        p1 = re.compile(
            r"^Number of npi_ipv4route entries = +(?P<number_of_npi_ipv4route_entries>\d+)$"
        )

        # 0     0.0.0.0/0                                     0x71aa2521a8e8 0x0     0     0         2025/11/16 20:09:44.619            9
        p2 = re.compile(
            r"^(?P<vrf>\d+)\s+(?P<ipv4_addr>[\d\.]+)/(?P<mask_len>\d+)\s+(?P<htm>\w+)\s+(?P<flags>\w+)\s+(?P<sgt>\d+)\s+(?P<dgid>\d+)\s+(?P<mpls>\w+)?\s+"+
            r"(?P<last_modified_year>\d+)/(?P<month>\d+)/(?P<date>\d+) (?P<hours>\d+):(?P<minutes>\d+):(?P<seconds>\d+).(?P<millseconds>\d+)\s+(?P<secssincehit>\d+)$"
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

            #Object ID           IPv4 Address        Mask Length         Parent Type         Parent ObjectID     SGT
            #0x5bb0d60dd878      100.60.2.200        32                  IPNEXTHOP_ID        0x5f                0
            m = p0_1.match(line)
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
                        "sgt": int(group["sgt"]),
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

            # 0     0.0.0.0/0       0x71aa2521a8e8 0x0     0     0         2025/11/16 20:09:44.619            9
            m = p2.match(line)
            if m:
                group = m.groupdict()
                index_dict = ret_dict.setdefault("index", {}).setdefault(index, {})
                index_dict.update(
                    {
                        "ipv4_addr": group["ipv4_addr"],
                        "mask_len": int(group["mask_len"]),
                        "vrf": int(group["vrf"]),
                        "htm": group["htm"],
                        "flags": group["flags"],
                        "sgt": int(group["sgt"]),
                        "dgid": int(group["dgid"]),
                        "last_modified_year": int(group["last_modified_year"]),
                        "month": int(group["month"]),
                        "date": int(group["date"]),
                        "hours": int(group["hours"]),
                        "minutes": int(group["minutes"]),
                        "seconds": int(group["seconds"]),
                        "millseconds": int(group["millseconds"]),
                        "secssincehit": int(group["secssincehit"]),
                    }
                )
                if "mpls" in group and group["mpls"] is not None:
                    index_dict["mpls"] = group["mpls"]
                index += 1
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

# ======================================================================
# Parser for show Platform Software Fed active ipv6 mld snooping vlan detail'
# ======================================================================
class ShowPlatformSoftwareFedActiveIpv6MldSnoopingVlanDetailSchema(MetaParser):
    """Schema for show Platform Software Fed active ipv6 mld snooping vlan detail"""

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
                Optional("protocol"): str,
                Optional("snoop_state"): str,
                Optional("secondary_vlan"): str,
                Optional("vlan_urid"): str,
                Optional("d_users_count"): str,
                Optional('fset_urid'): {
					Optional('urid'): str,
					Optional('hash'): str           
                },
                Optional('fset_aux_urid'): str,
                Optional('mrouter_ports'): ListOf(str),
                Optional('flood_ports'): ListOf(str),
                Optional('gid'): int,
                Optional('mcid_asic'): int,
                Optional('hw_info_asic'): {
                Optional('hw_vlan_mcid_oid'): {
                    Optional('oid'): int,
                    Optional('cookie'): str
                },
                Optional('multicast_state'): str
                    }    
                }
        }
    }

class ShowPlatformSoftwareFedActiveIpv6MldSnoopingVlanDetail(
    ShowPlatformSoftwareFedActiveIpv6MldSnoopingVlanDetailSchema
):
    """Parser for show Platform Software Fed active ipv6 mld snooping vlan detail"""

    cli_command = [
        "show platform software fed {switch_var} {state} ipv6 mld snooping vlan {vlan} detail",
        "show platform software fed {state} ipv6 mld snooping vlan {vlan} detail",
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
        # MLDSN Enabled : On
        # PIMSN Enabled : Off

        # Vlan 20
        p0 = re.compile(r"^Vlan\s+(?P<vlan>\d+)$")

        # (ipv6, vlan: 13)
        p0_1 = re.compile(r'^\(+(?P<protocol>\S+)+\,+\s+vlan\:\s+(?P<vlan>\d+)+\)$')

        # Vlan: 13
        p0_2 = re.compile(r"^Vlan:\s+(?P<vlan>\d+)$")

        # MLDSN Enabled : On
        p1 = re.compile(r"^MLDSN+\s+Enabled+\s+:\s+(?P<mldsn_en>\w+)$")

        # PIMSN Enabled : Off
        p2 = re.compile(r"^PIMSN+\s+Enabled+\s+:+\s+(?P<pimsn_en>\w+)$")

        # Flood Mode : Off
        p3 = re.compile(r"^Flood+\s+Mode+\s+:+(?P<flood_md>.*)$")

        # Flood Mode              : OFF
        p3_1 = re.compile(r'^Flood\s+Mode\s+:\s+(?P<flood_md>[\s\w\s]+)$')

        # Oper State : Up
        p4 = re.compile(r"^Oper+\s+State+\s+:+\s+(?P<op_state>\w+)$")

        # STP TCN Flood : Off
        p5 = re.compile(r"^STP+\s+TCN+\s+Flood+\s+:+\s+(?P<stp_tcn_flood>\w+)$")

        # STP TCN State           : OFF
        p5_1 = re.compile(r'^STP\s+TCN\s+(Flood|State)\s+:\s+(?P<stp_tcn_flood>[\s\w\s]+)$')

        # Routing Enabled : On
        p6 = re.compile(r"^Routing+\s+Enabled+\s+:+\s+(?P<route_en>\w+)$")

        # PIM Enabled : On
        p7 = re.compile(r"PIM+\s+Enabled+\s+:+\s+(?P<pim_en>\w+)$")

        # Pim state               : ON
        p7_1 = re.compile(r'^Pim\s+state\s+:\s+(?P<pim_en>[\s\w\s]+)$')

        # PVLAN : No
        p8 = re.compile(r"^PVLAN+\s+:+\s+(?P<pvlan>\w+)$")

        # In Retry : 0x0
        p9 = re.compile(r"^In+\s+Retry+\s+:+\s+(?P<in_retry>\w+)$")

        # CCK Epoch : 0x17
        p10 = re.compile(r"^CCK+\s+Epoch+\s+:+\s+(?P<cck_ep>\w+)$")

        # IOSD Flood Mode : Off
        p11 = re.compile(r"^IOSD+\s+Flood+\s+Mode+\s+:+\s+(?P<iosd_md>\w+)$")

        # IOS Flood Mode          : OFF
        p11_1 = re.compile(r'^IOS\s+Flood\s+Mode\s+:\s+(?P<iosd_md>[\s\w\s]+)$')

        # EVPN Proxy Enabled : On
        p12 = re.compile(r"^EVPN+\s+Proxy+\s+Enabled+\s:+\s+(?P<evpn_en>\w+)$")

        # Evpn Proxy              : OFF
        p12_1 = re.compile(r'^Evpn\s+Proxy\s+:\s+(?P<evpn_en>[\s\w\s]+)$')

        # L3mcast Adj :
        p13 = re.compile(r"^L3mcast+\s+Adj+\s+:+(?P<l3m_adj>.*)$")

        # Mrouter PortQ :
        p14 = re.compile(r"^Mrouter\s+PortQ\s+:\s*")
        # TenGigabitEthernet7/0/13
        p14_1 = re.compile(r"^([A-Za-z]*\d[-().]*){10,}$")

        # Flood PortQ :
        p15 = re.compile(r"^Flood PortQ\s+:\s*$")
        # TenGigabitEthernet7/0/13
        # FiveGigabitEthernet1/0/2
        # GigabitEthernet2/0/31
        p15_1 = re.compile(r"^[A-Za-z]+[\d\/]+$")

        # REP RI handle : 0x0
        p16 = re.compile(r"^REP+\s+RI+\s+handle+\s+:+(?P<rep_han>.*)$")

        # Snoop State             : ON
        p17 = re.compile(r'^Snoop\s+State\s+:\s+(?P<snoop_state>[\w\s]+)$')

        # Secondary Vlan          : NO
        p18 = re.compile(r'^Secondary\s+Vlan\s+:\s+(?P<secondary_vlan>[\s\w\s]+)$')

        # Vlan Urid               : 0x5000000000000008
        p19 = re.compile(r'^Vlan\s+Urid\s+:\s+(?P<vlan_urid>[\s\w\s]+)$')

        # Dependant users count   : 0
        p20 = re.compile(r'^Dependant\s+users\s+count\s+:\s+(?P<d_users_count>[\s\w\s]+)$')

        # Fset Urid ( hash )      : 0x200000000000000a ( 701ec04e )
        p21 = re.compile(r'^Fset +Urid +\( +hash +\) *: *(?P<urid>\S+) +\( +(?P<hash>\S+) +\)$')

        # Fset Aux Urid           : 0x0
        p22 = re.compile(r'^Fset +Aux +Urid *: *(?P<fset_aux_urid>\S+)$')

        # Mrouter ports           : 1
        p23 = re.compile(r'^Mrouter +ports *: *(?P<mrouter_count>\d+)$')

        # GigabitEthernet4/0/12
        p24 = re.compile(r'^(?P<mrouter_port>^\s*([^\s]+)\s*\(Port:([^\)]+)\)\s*)$')

        # Flood ports             :
        p25 = re.compile(r'^Flood +ports *:$')

        # GigabitEthernet1/0/46
        p26 = re.compile(r'^(?P<flood_port>\S+)$')

        # Gid                     : 8204
        p27 = re.compile(r'^Gid *: *(?P<gid>\d+)$')

        # Mcid Asic[0]            : 2872
        p28 = re.compile(r'^Mcid +Asic\[0\] *: *(?P<mcid_asic>\d+)$')

        # Hw Vlan Mcid Oid    : 2872 (cookie:urid:0x20::a)
        p29 = re.compile(r'^Hw +Vlan +Mcid +Oid *: *(?P<oid>\d+) +\(cookie:urid:(?P<cookie>\S+)\)$')

        # Multicast state     : enabled
        p30 = re.compile(r'^Multicast +state *: *(?P<multicast_state>\S+)$')

        # Parsing logic
        flood_ports_flag = False
        mrouter_ports_flag = False
    
        port_list = None
        mroute_list = []
        floodport_list = []
        for line in output.splitlines():
            line = line.strip()
            # Vlan 20
            m = p0.match(line)
            if m:
                vlan = m.groupdict()["vlan"]
                mac_dict = platform_dict.setdefault("vlan", {}).setdefault(vlan, {})

            # (ipv6, vlan: 13)
            m = p0_1.match(line)
            if m:
                vlan = int(m.groupdict()['vlan'])
                mac_dict = platform_dict.setdefault('vlan', {}).setdefault(vlan, {})
                mac_dict['protocol'] = m.groupdict()['protocol']

            # Vlan: 13
            m = p0_2.match(line)
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

            # Flood Mode              : OFF
            m = p3_1.match(line)
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

            # STP TCN State           : OFF
            m = p5_1.match(line)
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

            # TenGigabitEthernet7/0/13
            m = p14_1.match(line)
            if m and port_list is not None:
                port_list.append(m.group(0))

            # TenGigabitEthernet7/0/13
            # FiveGigabitEthernet1/0/2
            # GigabitEthernet2/0/31
            m = p15.match(line)
            if m:
                port_list = floodport_list
                mac_dict["flood_port"] = floodport_list
                continue
        
            # Flood PortQ :
            m = p15_1.match(line)
            if m and port_list is not None:
                port_list.append(m.group(0))
    

            # REP RI handle : 0x0
            m = p16.match(line)
            if m:
                mac_dict["rep_han"] = m.groupdict()["rep_han"]
                continue

            # Snoop State     : ON
            m = p17.match(line)
            if m:
                mac_dict['snoop_state'] = m.groupdict()['snoop_state']
                continue

            # Secondary Vlan          : NO
            m = p18.match(line)
            if m:
                mac_dict['secondary_vlan'] = m.groupdict()['secondary_vlan']
                continue

            # Vlan Urid               : 0x5000000000000008
            m = p19.match(line)
            if m:
                mac_dict['vlan_urid'] = m.groupdict()['vlan_urid']
                continue

            # Dependant users count   : 0
            m = p20.match(line)
            if m:
                mac_dict['d_users_count'] = m.groupdict()['d_users_count']
                continue
    
            # Fset Urid ( hash )      : 0x200000000000000a ( 701ec04e )
            m = p21.match(line)
            if m:
                fset_urid_dict = mac_dict.setdefault('fset_urid', {})
                fset_urid_dict['urid'] = m.group('urid')
                fset_urid_dict['hash'] = m.group('hash')
                continue

            # Fset Aux Urid           : 0x0
            m = p22.match(line)
            if m:
                mac_dict['fset_aux_urid'] = m.group('fset_aux_urid')
                continue

            # Mrouter ports           : 1
            m = p23.match(line)
            if m:
                mrouter_ports_flag = True
                flood_ports_flag = False  
                mac_dict['mrouter_ports'] = []
                continue

            # GigabitEthernet4/0/12 (Mrouter Port)
            m = p24.match(line)
            if m and mrouter_ports_flag:
                mac_dict['mrouter_ports'].append(m.group('mrouter_port'))
                continue

            # Flood ports             :
            m = p25.match(line)
            if m:
                flood_ports_flag = True
                mrouter_ports_flag = False  
                mac_dict['flood_ports'] = []
                continue

            # GigabitEthernet1/0/46 (Flood Port)
            m = p26.match(line)
            if m and flood_ports_flag:
                mac_dict['flood_ports'].append(m.group('flood_port'))
                continue

            # Gid                     : 8204
            m = p27.match(line)
            if m:
                mac_dict['gid'] = int(m.group('gid'))
                continue

            # Mcid Asic[0]            : 2872
            m = p28.match(line)
            if m:
                mac_dict['mcid_asic'] = int(m.group('mcid_asic'))
                continue

            # Hw Vlan Mcid Oid    : 2872 (cookie:urid:0x20::a)
            m = p29.match(line)
            if m:
                hw_info_asic = mac_dict.setdefault('hw_info_asic', {})
                hw_vlan_mcid_oid = hw_info_asic.setdefault('hw_vlan_mcid_oid', {})
                hw_vlan_mcid_oid['oid'] = int(m.group('oid'))
                hw_vlan_mcid_oid['cookie'] = m.group('cookie')
                continue

            # Multicast state     : enabled
            m = p30.match(line)
            if m:
                mac_dict.setdefault('hw_info_asic', {})['multicast_state'] = m.group('multicast_state')
                continue

        return platform_dict

# ===================================================================
# Parser for show platform software fed switch active ipv6 mfib count'
# ===================================================================
class ShowPlatformSoftwareFedIpv6MfibCountSchema(MetaParser):
    """Schema for show platform software fed switch active ipv6 mfib count"""
    schema = {
        'mfib_count': {
            'number_of_entries': int
            }
        }

class ShowPlatformSoftwareFedIpv6MfibCount(ShowPlatformSoftwareFedIpv6MfibCountSchema):
    """Parser for show platform software fed switch active ipv6 mfib count"""

    cli_command = ['show platform software fed {switch_var} {state} ipv6 mfib count',
        'show platform software fed {state} ipv6 mfib count']

    def cli(self, state='', switch_var=None, output=None):
        if output is None:
            if switch_var:
                cmd = self.cli_command[0].format(state=state, switch_var=switch_var)
            else:
                cmd = self.cli_command[1].format(state=state)
            output = self.device.execute(cmd)
        ret_dict = {}

        # Number of entries = 8000
        p0 = re.compile(r'(Number of entries +\= +(?P<number_of_entries>\d+))')

        for line in output.splitlines():
            line = line.strip()

            # Number of entries = 8000
            m = p0.match(line)
            if m:
                group = m.groupdict()
                id_dict = ret_dict.setdefault('mfib_count', {})
                id_dict['number_of_entries'] = int(group['number_of_entries'])
                continue

        return ret_dict


# ===================================================================
# Parser for show platform software fed switch active ipv6 mfib summary'
# ===================================================================
class ShowPlatformSoftwareFedIpv6MfibSummarySchema(MetaParser):
    """Schema for show platform software fed switch active ipv6 mfib summary"""
    schema = {
        'mfib_v6_summary': {
            Optional('last_used_mlist_urid'): int,
            'mcast_current_count_reached': int,
            'mcast_max_count_reached': int,
            'mcast_vrf_count': int,
            'oifs_current_count_reached': int,
            'oifs_current_max_reached': int,
            's_g_current_count': int,
            's_g_retryq_count': int,
            's_gm_retryq_count': int,
            'star_g_current_count': int,
            'star_g_retryq_count': int
        }
    }

class ShowPlatformSoftwareFedIpv6MfibSummary(ShowPlatformSoftwareFedIpv6MfibSummarySchema):
    """Parser for show platform software fed switch active ip mfib summary"""

    cli_command = ['show platform software fed {switch_var} {state} ipv6 mfib summary',
        'show platform software fed {state} ipv6 mfib summary']

    def cli(self, state='', switch_var=None, output=None):
        if output is None:
            if switch_var:
                cmd = self.cli_command[0].format(state=state, switch_var=switch_var)
            else:
                cmd = self.cli_command[1].format(state=state)
            output = self.device.execute(cmd)

        ret_dict = {}

        # Multicast Vrf Current Count              : 2
        p0 = re.compile(r'(Multicast Vrf Current Count +\: +(?P<mcast_vrf_count>\d+))')

        # Mroute Current Count/Max Reached         : 7830/10118
        p1 = re.compile(r'(Mroute Current .* +Reached +\: +(?P<mcast_current_count_reached>\d+)\/(?P<mcast_max_count_reached>\d+))')

        # (*,G) Current Count                      : 4001
        p2 = re.compile(r'(\(+\*+\,+G\) +Current Count +\: +(?P<star_g_current_count>\d+))')

        # (S,G) Current Count                      : 3829
        p3 = re.compile(r'(\(+\S+\,+G\) +Current Count +\: +(?P<s_g_current_count>\d+))')

        #  (*,G/m) RetryQ Count                     : 0
        p4 = re.compile(r'(\(+\*+\,+G\/m\) +RetryQ Count +\: +(?P<s_gm_retryq_count>\d+))')

        # (*,G) RetryQ Count                       : 0
        p5 = re.compile(r'(\(+\*+\,+G\) +RetryQ Count +\: +(?P<star_g_retryq_count>\d+))')

        #   (S,G) RetryQ Count                       : 0
        p6 = re.compile(r'(\(+\S+\,+G\) +RetryQ Count +\: +(?P<s_g_retryq_count>\d+))')

        # Oifs Current Count/Max Reached           : 16126/18354
        p7 = re.compile(r'(Oifs Current Count.* +Reached +\: +(?P<oifs_current_count_reached>\d+)\/(?P<oifs_current_max_reached>\d+))')

        # Last used Mlist Urid                     : 0x100000000000d3a
        p8 = re.compile(r'(Last used Mlist Urid  +\: +(?P<last_used_mlist_urid>\d+))')

        for line in output.splitlines():
            line = line.strip()

            # Multicast Vrf Current Count              : 2
            m = p0.match(line)
            if m:
                group = m.groupdict()
                id_dict = ret_dict.setdefault('mfib_v6_summary', {})
                id_dict['mcast_vrf_count'] = int(group['mcast_vrf_count'])
                continue

            # Mroute Current Count/Max Reached         : 7830/10118
            m = p1.match(line)
            if m:
                group = m.groupdict()
                id_dict['mcast_current_count_reached'] = int(group['mcast_current_count_reached'])
                id_dict['mcast_max_count_reached'] = int(group['mcast_max_count_reached'])
                continue

            # (*,G) Current Count                      : 4001
            m = p2.match(line)
            if m:
                group = m.groupdict()
                id_dict['star_g_current_count'] = int(group['star_g_current_count'])
                continue

            # (S,G) Current Count                      : 3829
            m = p3.match(line)
            if m:
                group = m.groupdict()
                id_dict['s_g_current_count'] = int(group['s_g_current_count'])
                continue

            #  (*,G/m) RetryQ Count                     : 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                id_dict['s_gm_retryq_count'] = int(group['s_gm_retryq_count'])
                continue

            # (*,G) RetryQ Count                       : 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                id_dict['star_g_retryq_count'] = int(group['star_g_retryq_count'])
                continue

            #   (S,G) RetryQ Count                       : 0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                id_dict['s_g_retryq_count'] = int(group['s_g_retryq_count'])
                continue

            # Oifs Current Count/Max Reached           : 16126/18354
            m = p7.match(line)
            if m:
                group = m.groupdict()
                id_dict['oifs_current_count_reached'] = int(group['oifs_current_count_reached'])
                id_dict['oifs_current_max_reached'] = int(group['oifs_current_max_reached'])
                continue

            # Last used Mlist Urid                     : 0x100000000000d3a
            m = p8.match(line)
            if m:
                group = m.groupdict()
                id_dict['last_used_mlist_urid'] = int(group['last_used_mlist_urid'])
                continue

        return ret_dict

# ===================================================================
# Parser for show platform software fed switch active ipv6 mld snooping summary'
# ===================================================================
class ShowPlatformSoftwareFedIpv6MldSnoopingSummarySchema(MetaParser):
    """Schema for show platform software fed switch active ipv6 mld snooping summary"""
    schema = {
        'mld_snooping_summary': {
            'group_current_count': int,
            'group_max_count': int,
            'last_used_group_urid': str,
            'last_used_vlan_urid': str,
            'port_current_count': int,
            'port_max_count': int,
            'vlan_current_count': int,
            'vlan_max_count': int
        }
    }

class ShowPlatformSoftwareFedIpv6MldSnoopingSummary(ShowPlatformSoftwareFedIpv6MldSnoopingSummarySchema):
    """Parser for show platform software fed switch active ipv6 mld snooping summary"""

    cli_command = ['show platform software fed {switch_var} {state} ipv6 mld snooping summary',
        'show platform software fed {state} ipv6 mld snooping summary']

    def cli(self, state='', switch_var=None, output=None):
        if output is None:
            if switch_var:
                cmd = self.cli_command[0].format(state=state, switch_var=switch_var)
            else:
                cmd = self.cli_command[1].format(state=state)
            output = self.device.execute(cmd)

        ret_dict = {}

        # Vlan Current Count/Max Reached    : 3/3
        p0 = re.compile(r'(Vlan Current Count/Max Reached +\: +(?P<vlan_current_count>\d+)\/+(?P<vlan_max_count>\d+))')

        # Group Current Count/Max Reached   : 0/0
        p1 = re.compile(r'(Group Current Count/Max Reached +\: +(?P<group_current_count>\d+)\/+(?P<group_max_count>\d+))')

        # Port Current Count/Max Reached    : 2001/2057
        p2 = re.compile(r'(Port Current Count/Max Reached +\: +(?P<port_current_count>\d+)\/+(?P<port_max_count>\d+))')

        # Last used Vlan Urid               : 0x4000000000000006
        p3 = re.compile(r'(Last used Vlan Urid +\: +(?P<last_used_vlan_urid>\S+))')

        # Last Used Group Urid              : 0x600000000000575c
        p4 = re.compile(r'(Last Used Group Urid  +\: +(?P<last_used_group_urid>\S+))')

        for line in output.splitlines():
            line = line.strip()

            # Vlan Current Count/Max Reached    : 3/3             : 2
            m = p0.match(line)
            if m:
                group = m.groupdict()
                id_dict = ret_dict.setdefault('mld_snooping_summary', {})
                id_dict['vlan_current_count'] = int(group['vlan_current_count'])
                id_dict['vlan_max_count'] = int(group['vlan_max_count'])
                continue

            # Group Current Count/Max Reached   : 0/0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                id_dict['group_current_count'] = int(group['group_current_count'])
                id_dict['group_max_count'] = int(group['group_max_count'])
                continue

            # Port Current Count/Max Reached    : 2001/2057
            m = p2.match(line)
            if m:
                group = m.groupdict()
                id_dict['port_current_count'] = int(group['port_current_count'])
                id_dict['port_max_count'] = int(group['port_max_count'])
                continue

            # Last used Vlan Urid               : 0x4000000000000006
            m = p3.match(line)
            if m:
                group = m.groupdict()
                id_dict['last_used_vlan_urid'] = group['last_used_vlan_urid']
                continue

            # Last Used Group Urid              : 0x600000000000575c                    : 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                id_dict['last_used_group_urid'] = group['last_used_group_urid']
                continue

        return ret_dict

# ===================================================================
# Parser for show platform software fed switch active ip mfib count'
# ===================================================================
class ShowPlatformSoftwareFedIpMfibCountSchema(MetaParser):
    """Schema for show platform software fed switch active ip mfib count"""
    schema = {
        'mfib_count': {
            'number_of_entries': int
        }
    }

class ShowPlatformSoftwareFedIpMfibCount(ShowPlatformSoftwareFedIpMfibCountSchema):
    """Parser for show platform software fed switch active ip mfib count"""

    cli_command = ['show platform software fed {switch} {state} ip mfib count',
                   'show platform software fed {state} ip mfib count']

    def cli(self, state, switch=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(state=state, switch=switch)
            else:
                cmd = self.cli_command[1].format(state=state)
            output = self.device.execute(cmd)

        ret_dict = {}

        # Number of entries = 7896
        p0 = re.compile(r'(Number of entries +\= +(?P<number_of_entries>\d+))')

        for line in output.splitlines():
            line = line.strip()

            # Number of entries = 7896
            m = p0.match(line)
            if m:
                group = m.groupdict()
                id_dict = ret_dict.setdefault('mfib_count', {})
                id_dict['number_of_entries'] = int(group['number_of_entries'])
                continue

        return ret_dict


# ===================================================================
# Parser for show platform software fed switch active ip mfib summary'
# ===================================================================
class ShowPlatformSoftwareFedIpMfibSummarySchema(MetaParser):
    """Schema for show platform software fed switch active ip mfib summary"""
    schema = {
        'mfib_v4_summary': {
            Optional('last_used_mlist_urid'): int,
            'mcast_count_mac_reached': str,
            'mcast_vrf_count': int,
            'oifs_current_count_reached': str,
            's_g_current_count': int,
            's_g_retryq_count': int,
            's_gm_retryq_count': int,
            'star_g_current_count': int,
            'star_g_retryq_count': int
        }
    }


class ShowPlatformSoftwareFedIpMfibSummary(ShowPlatformSoftwareFedIpMfibSummarySchema):
    """Parser for show platform software fed switch active ip mfib summary"""

    cli_command = ['show platform software fed {switch} {state} ip mfib summary',
                   'show platform software fed {state} ip mfib summary']

    def cli(self, state, switch=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(state=state, switch=switch)
            else:
                cmd = self.cli_command[1].format(state=state)
            output = self.device.execute(cmd)

        ret_dict = {}

        # Multicast Vrf Current Count              : 2
        p0 = re.compile(r'(Multicast Vrf Current Count +\: +(?P<mcast_vrf_count>\d+))')

        # Mroute Current Count/Max Reached         : 7830/10118
        p1 = re.compile(r'(Mroute Current .* +Reached +\: +(?P<mcast_count_mac_reached>\d+.+))')

        # (*,G) Current Count                      : 4001
        p2 = re.compile(r'(\(+\*+\,+G\) +Current Count +\: +(?P<star_g_current_count>\d+))')

        # (S,G) Current Count                      : 3829
        p3 = re.compile(r'(\(+\S+\,+G\) +Current Count +\: +(?P<s_g_current_count>\d+))')

        #  (*,G/m) RetryQ Count                     : 0
        p4 = re.compile(r'(\(+\*+\,+G\/m\) +RetryQ Count +\: +(?P<s_gm_retryq_count>\d+))')

        # (*,G) RetryQ Count                       : 0
        p5 = re.compile(r'(\(+\*+\,+G\) +RetryQ Count +\: +(?P<star_g_retryq_count>\d+))')

        #   (S,G) RetryQ Count                       : 0
        p6 = re.compile(r'(\(+\S+\,+G\) +RetryQ Count +\: +(?P<s_g_retryq_count>\d+))')

        # Oifs Current Count/Max Reached           : 16126/18354
        p7 = re.compile(r'(Oifs Current Count.* +Reached +\: +(?P<oifs_current_count_reached>\d+.+))')

        # Last used Mlist Urid                     : 0x100000000000d3a
        p8 = re.compile(r'(Last used Mlist Urid  +\: +(?P<last_used_mlist_urid>\d+))')

        for line in output.splitlines():
            line = line.strip()

            # Multicast Vrf Current Count              : 2
            m = p0.match(line)
            if m:
                group = m.groupdict()
                id_dict = ret_dict.setdefault('mfib_v4_summary', {})
                id_dict['mcast_vrf_count'] = int(group['mcast_vrf_count'])
                continue

            # Mroute Current Count/Max Reached         : 7830/10118
            m = p1.match(line)
            if m:
                group = m.groupdict()
                id_dict['mcast_count_mac_reached'] = group['mcast_count_mac_reached']
                continue

            # (*,G) Current Count                      : 4001
            m = p2.match(line)
            if m:
                group = m.groupdict()
                id_dict['star_g_current_count'] = int(group['star_g_current_count'])
                continue

            # (S,G) Current Count                      : 3829
            m = p3.match(line)
            if m:
                group = m.groupdict()
                id_dict['s_g_current_count'] = int(group['s_g_current_count'])
                continue

            #  (*,G/m) RetryQ Count                     : 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                id_dict['s_gm_retryq_count'] = int(group['s_gm_retryq_count'])
                continue

            # (*,G) RetryQ Count                       : 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                id_dict['star_g_retryq_count'] = int(group['star_g_retryq_count'])
                continue

            #   (S,G) RetryQ Count                       : 0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                id_dict['s_g_retryq_count'] = int(group['s_g_retryq_count'])
                continue

            # Oifs Current Count/Max Reached           : 16126/18354
            m = p7.match(line)
            if m:
                group = m.groupdict()
                id_dict['oifs_current_count_reached'] = group['oifs_current_count_reached']
                continue

            # Last used Mlist Urid                     : 0x100000000000d3a
            m = p8.match(line)
            if m:
                group = m.groupdict()
                id_dict['last_used_mlist_urid'] = int(group['last_used_mlist_urid'])
                continue

        return ret_dict


# ========================================================
# Parser for 'show Platform Software Fed ip igmp snooping groups count'
# ========================================================
class ShowPlatformSoftwareIgmpSnoopingGroupsCountSchema(MetaParser):
    """Schema for show Platform Software Fed ip igmp snooping groups count """
    schema = {
        Optional('ip_igmp_snooping_entries'): int,
        Optional('total_group_count'): int,
        Optional('total_stub_group_count'): int
    }


class ShowPlatformSoftwareIgmpSnoopingGroupsCount(ShowPlatformSoftwareIgmpSnoopingGroupsCountSchema):

    cli_command = ['show platform software fed {switch} {state} ip igmp snooping groups count',
                   'show platform software fed {state} ip igmp snooping groups count']

    def cli(self, state, switch=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(switch=switch, state=state)
            else:
                cmd = self.cli_command[1].format(state=state)
            output = self.device.execute(cmd)

        ret_dict = {}

        # Total number of entries:8000
        p1 = re.compile(r'^Total\s+number\s+of\s+entries\:(?P<ip_igmp_snooping_entries>\d+)$')

        # Total Group Count       : 9789
        p2 = re.compile(r'(Total Group Count +\: +(?P<total_group_count>\d+))')

        # Total Stub Group Count  : 9787
        p3 = re.compile(r'(Total Stub Group Count +\: +(?P<total_stub_group_count>\d+))')

        for line in output.splitlines():
            line = line.strip()

            # Number of lines which match regexp = 240
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                count = int(groups['ip_igmp_snooping_entries'])
                ret_dict['ip_igmp_snooping_entries'] = count

            # Total Group Count       : 9789
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['total_group_count'] = int(group['total_group_count'])
                continue

            # Total Stub Group Count  : 9787
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict['total_stub_group_count'] = int(group['total_stub_group_count'])
                continue

        return ret_dict

# ================================================================================
# Parser for show platform software fed switch active ip mfib vrf {vrf_name} count'
# ================================================================================
class ShowPlatformSoftwareFedIpMfibVrfCountSchema(MetaParser):
    """Schema for show platform software fed switch active ipv6 mfib count"""
    schema = {
        'mfib_count': {
            'number_of_entries': int
            }
        }

class ShowPlatformSoftwareFedIpMfibVrfCount(ShowPlatformSoftwareFedIpMfibVrfCountSchema):
    """Parser for show platform software fed switch active ip mfib vrf {vrf_name} count"""

    cli_command = ['show platform software fed {switch_var} {state} ip mfib vrf {vrf_name} count',
        'show platform software fed {state} ip mfib vrf {vrf_name} count']

    def cli(self, state='', vrf_name='',switch_var=None, output=None):
        if output is None:
            if switch_var:
                cmd = self.cli_command[0].format(state=state, vrf_name=vrf_name, switch_var=switch_var)
            else:
                cmd = self.cli_command[1].format(state=state, vrf_name=vrf_name)
            output = self.device.execute(cmd)
        ret_dict = {}

        # Number of entries = 32001
        p0 = re.compile(r'(Number of entries +\= +(?P<number_of_entries>\d+))')

        for line in output.splitlines():
            line = line.strip()

            # Number of entries = 32001
            m = p0.match(line)
            if m:
                group = m.groupdict()
                id_dict = ret_dict.setdefault('mfib_count', {})
                id_dict['number_of_entries'] = int(group['number_of_entries'])
                continue

        return ret_dict

# ===================================================================
# Parser for show platform software fed switch active ip igmp snooping summary'
# ===================================================================
class ShowPlatformSoftwareFedIpIgmpSnoopingSummarySchema(MetaParser):
    """Schema for show platform software fed switch active ip igmp snooping summary"""
    schema = {
        'igmp_snooping_summary': {
            'group_current_count': int,
            'group_max_count': int,
            'last_used_group_urid': str,
            'last_used_vlan_urid': str,
            'port_current_count': int,
            'port_max_count': int,
            'vlan_current_count': int,
            'vlan_max_count': int
        }
    }

class ShowPlatformSoftwareFedIpIgmpSnoopingSummary(ShowPlatformSoftwareFedIpIgmpSnoopingSummarySchema):
    """Parser for show platform software fed switch active ip igmp snooping summary"""

    cli_command = ['show platform software fed {switch_var} {state} ip igmp snooping summary',
        'show platform software fed {state} ip igmp snooping summary']

    def cli(self, state='', switch_var=None, output=None):
        if output is None:
            if switch_var:
                cmd = self.cli_command[0].format(state=state, switch_var=switch_var)
            else:
                cmd = self.cli_command[1].format(state=state)
            output = self.device.execute(cmd)

        ret_dict = {}

        # Vlan Current Count/Max Reached    : 3/3
        p0 = re.compile(r'(Vlan Current Count/Max Reached +\: +(?P<vlan_current_count>\d+)\/+(?P<vlan_max_count>\d+))')

        # Group Current Count/Max Reached   : 0/0
        p1 = re.compile(r'(Group Current Count/Max Reached +\: +(?P<group_current_count>\d+)\/+(?P<group_max_count>\d+))')

        # Port Current Count/Max Reached    : 2001/2057
        p2 = re.compile(r'(Port Current Count/Max Reached +\: +(?P<port_current_count>\d+)\/+(?P<port_max_count>\d+))')

        # Last used Vlan Urid               : 0x4000000000000006
        p3 = re.compile(r'(Last used Vlan Urid +\: +(?P<last_used_vlan_urid>\S+))')

        # Last Used Group Urid              : 0x600000000000575c
        p4 = re.compile(r'(Last Used Group Urid  +\: +(?P<last_used_group_urid>\S+))')

        for line in output.splitlines():
            line = line.strip()

            # Vlan Current Count/Max Reached    : 3/3             : 2
            m = p0.match(line)
            if m:
                group = m.groupdict()
                id_dict = ret_dict.setdefault('igmp_snooping_summary', {})
                id_dict['vlan_current_count'] = int(group['vlan_current_count'])
                id_dict['vlan_max_count'] = int(group['vlan_max_count'])
                continue

            # Group Current Count/Max Reached   : 0/0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                id_dict['group_current_count'] = int(group['group_current_count'])
                id_dict['group_max_count'] = int(group['group_max_count'])
                continue

            # Port Current Count/Max Reached    : 2001/2057
            m = p2.match(line)
            if m:
                group = m.groupdict()
                id_dict['port_current_count'] = int(group['port_current_count'])
                id_dict['port_max_count'] = int(group['port_max_count'])
                continue

            # Last used Vlan Urid               : 0x4000000000000006
            m = p3.match(line)
            if m:
                group = m.groupdict()
                id_dict['last_used_vlan_urid'] = group['last_used_vlan_urid']
                continue

            # Last Used Group Urid              : 0x600000000000575c                    : 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                id_dict['last_used_group_urid'] = group['last_used_group_urid']
                continue

        return ret_dict

# ===================================================================
# Parser for show ipv6 mld snooping address vlan {vlan} {group} summary
# ===================================================================
class ShowPlatformSoftwareFedMldSnoopingIpv6GroupsCountSchema(MetaParser):
    """Schema for show ipv6 mld snooping address vlan {vlan} {group} summary """
    schema = {
    'mld_snooping_summary':
        {
            Optional('group_address'): str,
            Optional('interface'): str,
            Optional('host_type'): str,
            Optional('member_ports'): str
        }
    }

class ShowPlatformSoftwareFedMldSnoopingIpv6GroupsCount(ShowPlatformSoftwareFedMldSnoopingIpv6GroupsCountSchema):
    """Parser for show Platform Software fed ipv6 mld snooping groups count"""

    cli_command = ['show ipv6 mld snooping address vlan {vlan} {group} summary']

    def cli(self, vlan='', group='', output=None):
        if output is None:
            cmd = self.cli_command[0].format(vlan=vlan,group=group)
            output = self.device.execute(cmd)
        ret_dict = {}

        # Group Address (Vlan 11)        : FF13::1
        p0 = re.compile(r'(Group\s+Address\s+\(+(?P<interface>.*)\) +\: +(?P<group_address>[\w\:\.\/]+))')
        # Host type                      : v1
        p1 = re.compile(r'(Host\s+type\s+\:\s+(?P<host_type>\S+))')

        # Member Ports                   : Po92
        p2 = re.compile(r'(Member\s+Ports  +\: +(?P<member_ports>\S+))')

        for line in output.splitlines():
            line = line.strip()

            # Group Address (Vlan 11)        : FF13::1
            m = p0.match(line)
            if m:
                group = m.groupdict()
                mld_dict = ret_dict.setdefault('mld_snooping_summary', {})
                mld_dict['group_address'] = group['group_address']
                mld_dict['interface'] = group['interface']
                continue

            # Host type                      : v1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                mld_dict['host_type'] = group['host_type']
                continue

            # Member Ports                   : Po92
            m = p2.match(line)
            if m:
                group = m.groupdict()
                mld_dict['member_ports'] = group['member_ports']
                continue

        return ret_dict

class ShowPlatformSoftwareFedSwitchActiveIpv6RouteSchema(MetaParser):
    """
    Schema for show platform software fed switch active ipv6 route
    """

    schema = {
        "index": {
            Any(): {
                Optional("object_id"): str,
                "ipv6_addr": str,
                "mask_len": int,
                Optional("parent_type"): str,
                Optional("parent_object_id"): str,
                Optional("sgt"): int,
                Optional("vrf"): int,
                Optional("mpls"): int,
                Optional("htm"): str,
                Optional("flags"): str,
                Optional("dgid"): int,
                Optional("last_modified_year"): int,
                Optional("month"): int,
                Optional("date"): int,
                Optional("hours"): int,
                Optional("minutes"): int,
                Optional("seconds"): int,
                Optional("millseconds"): int,
                Optional("secssincehit"): int,
            },
        },
        Optional("number_of_npi_ipv6route_entries"): int,
    }


class ShowPlatformSoftwareFedSwitchActiveIpv6Route(
    ShowPlatformSoftwareFedSwitchActiveIpv6RouteSchema
):
    """
    show platform software fed switch active ipv6 route
    show platform software fed switch active ipv6 route vrf {vrf_name}
    """

    cli_command = [
        "show platform software fed switch {mode} ipv6 route",
        "show platform software fed switch {mode} ipv6 route vrf {vrf_name}"
    ]

    def cli(self, mode='', vrf_name='', output=None):
        if output is None:
            if mode and vrf_name:
                cmd = self.cli_command[1].format(mode=mode, vrf_name=vrf_name)
            else:
                cmd = self.cli_command[0].format(mode=mode)

            output = self.device.execute(cmd)
        ret_dict = {}
        index = 1
        index_dict = {}

        # Object ID           IPv6 Address                            Mask Length         Parent Type         Parent ObjectID     SGT
        # 0x5c292bc04268      fe80::                                  10                  RECV                0x0                 0

        p0 = re.compile(
            r"^(?P<object_id>\w+)\s+(?P<ipv6_addr>\S+)\s+(?P<mask_len>\d+)\s+(?P<parent_type>\S+)\s+(?P<parent_object_id>\S+)\s+(?P<sgt>\d+)$"
        )

        # Number of npi_ipv6route entries = 6
        p1 = re.compile(
            r"^Number of npi_ipv6route entries = +(?P<number_of_npi_ipv6route_entries>\d+)$"
        )

        # 0     0000:0000:0000:0000:0000:0000:0000:0000/0       0x71aa2521a8e8 0x0     0     0         2025/11/16 20:09:44.619            9
        p2 = re.compile(
            r"^(?P<vrf>\d+)\s+(?P<ipv6_addr>[\da-fA-F:]+)/(?P<mask_len>\d+)\s+(?P<htm>\w+)\s+(?P<flags>\w+)\s+(?P<sgt>\d+)\s+(?P<dgid>\d+)\s+(?P<mpls>\w+)?\s+"+
            r"(?P<last_modified_year>\d+)/(?P<month>\d+)/(?P<date>\d+) (?P<hours>\d+):(?P<minutes>\d+):(?P<seconds>\d+).(?P<millseconds>\d+)\s+(?P<secssincehit>\d+)$"
        )

        for line in output.splitlines():
            line = line.strip()

        # Object ID           IPv6 Address                            Mask Length         Parent Type         Parent ObjectID     SGT
        # 0x5c292bc04268      fe80::                                  10                  RECV                0x0                 0
            m = p0.match(line)
            if m:
                group = m.groupdict()
                index_dict = ret_dict.setdefault("index", {}).setdefault(index, {})
                index_dict.update(
                    {
                        "object_id": group["object_id"],
                        "ipv6_addr": group["ipv6_addr"],
                        "mask_len": int(group["mask_len"]),
                        "parent_type": group["parent_type"],
                        "parent_object_id": group["parent_object_id"],
                        "sgt": int(group["sgt"]),
                    }
                )
                index += 1
                continue

            # Number of npi_ipv6route entries = 6
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict["number_of_npi_ipv6route_entries"] = int(
                    group["number_of_npi_ipv6route_entries"]
                )
                continue

            # 0     0000:0000:0000:0000:0000:0000:0000:0000/0       0x71aa2521a8e8 0x0     0     0         2025/11/16 20:09:44.619            9
            m = p2.match(line)
            if m:
                group = m.groupdict()
                index_dict = ret_dict.setdefault("index", {}).setdefault(index, {})
                index_dict.update(
                    {
                        "ipv6_addr": group["ipv6_addr"],
                        "mask_len": int(group["mask_len"]),
                        "vrf": int(group["vrf"]),
                        "htm": group["htm"],
                        "flags": group["flags"],
                        "sgt": int(group["sgt"]),
                        "dgid": int(group["dgid"]),
                        "last_modified_year": int(group["last_modified_year"]),
                        "month": int(group["month"]),
                        "date": int(group["date"]),
                        "hours": int(group["hours"]),
                        "minutes": int(group["minutes"]),
                        "seconds": int(group["seconds"]),
                        "millseconds": int(group["millseconds"]),
                        "secssincehit": int(group["secssincehit"]),
                    }
                )
                if "mpls" in group and group["mpls"] is not None:
                    index_dict["mpls"] = group["mpls"]
                index += 1
                continue

        return ret_dict

class ShowPlatformSoftwareFedActiveIpMfibVrfSchema(MetaParser):
    """
    Schema for show platform software fed {switch} {active} ip mfib vrf {vrf_name} {group} {source}
    """

    schema = {
        'mfib': {
            int : {
                'mvrf': int,
                'group': str,
                'source': str,
                'attrs': {
                    'hw_flag': str,
                    'mlist_flags': str,
                    'mlist_hndl_id': str,
                    'mlist_urid': str,
                    'fset_urid_hash': str,
                    Optional('fset_aux_urid'): str,
                    'rpf_adjacency_id': str,
                    'cpu_credit': int,
                    Optional('total_packets'): int,
                    Optional('ec_seed'): int,
                    Optional('npi_mroute_ent'): str,
                    Optional('svi_fwd_ifs'): int,
                    Optional('ios_f_ifs'): int,
                    Optional('mlist_f_ifs'): int,
                    Optional('pps_approx'): int,
                    'oif_count': int,
                    'oif_details': list,
                    'gid': int,
                    'asic': {
                        int: {
                            'mcid_oid_asic': int,
                        },
                    },
                    Optional('hw_asic_info'): {
                        int: {
                            Optional('ip_mcid_oid'): int,
                            Optional('cookie'): str,
                            Optional('rpf_port_oid'): int,
                            Optional('rpfid'): int,
                            Optional('use_rpfid'): int,
                            Optional('punt_and_forward'): int,
                            Optional('punt_on_rpf_fail'): int,
                            Optional('enable_rpf_check'): int,
                            }
                        }
                    }
                }
            }
        }

class ShowPlatformSoftwareFedActiveIpMfibVrf(ShowPlatformSoftwareFedActiveIpMfibVrfSchema):
    """
    Parser for show platform software fed {switch} {active} ip mfib vrf {vrf_name} {group} {source}
    """

    cli_command = [
        'show platform software fed {switch} {active} ip mfib vrf {vrf_name} {group} {source}',
        'show platform software fed {active} ip mfib vrf {vrf_name} {group} {source}',
        'show platform software fed {switch} {active} ip mfib {group} {source}',
        'show platform software fed {active} ip mfib {group} {source}'
    ]

    def cli(self, switch='', active='', vrf_name='', group='', source='', output=None):
        if output is None:
            if vrf_name:
                if switch:
                    cmd = self.cli_command[0].format(switch=switch, active=active, vrf_name=vrf_name, group=group, source=source)
                else:
                    cmd = self.cli_command[1].format(active=active, vrf_name=vrf_name, group=group, source=source)
            else:
                if switch:
                    cmd = self.cli_command[2].format(switch=switch, active=active, group=group, source=source)
                else:
                    cmd = self.cli_command[3].format(active=active, group=group, source=source)
            output = self.device.execute(cmd)

        ret_dict = {}

        # Mvrf: 3  ( 40::2, ff1e::1 ) Attrs:
        p0 = re.compile(r'^Mvrf: +(?P<mvrf>\d+) +\( +(?P<source>[\w\:\.\/\*]+), +(?P<group>[\w\:\.\/]+) +\) +Attrs:( C)?$')

        # Hw Flag                 : InHw
        # Hw Flag                 : InHw  EntryActive
        p1 = re.compile(r'^Hw Flag +: +(?P<hw_flag>[\w\s]+)$')

        # Mlist Flags             : None
        p2 = re.compile(r'^Mlist Flags +: +(?P<mlist_flags>\w+)$')

        # Mlist_hndl (Id)         : 0x11889275ea0 ( 0xc823 )
        p3 = re.compile(r'^Mlist_hndl \(Id\) +: +(?P<mlist_hndl_id>[\w\(\)\s]+)$')

        # Mlist Urid              : 0x10000000003238e8
        p4 = re.compile(r'^Mlist Urid +: +(?P<mlist_urid>[\w]+)$')

        # Fset Urid (Hash)        : 0x300000000031f715 ( 68af2994 )
        p5 = re.compile(r'^Fset Urid \(Hash\) +: +(?P<fset_urid_hash>[\w\(\)\s]+)$')

        # Fset Aux Urid           : 0x0
        p5_1 = re.compile(r'^Fset Aux Urid +: +(?P<fset_aux_urid>[\w]+)$')

        # RPF Adjacency ID        : 0xf80059d2
        p6 = re.compile(r'^RPF Adjacency ID +: +(?P<rpf_adjacency_id>[\w]+)$')

        # CPU Credit              : 0
        p7 = re.compile(r'^CPU Credit +: +(?P<cpu_credit>\d+)$')

        # Total Packets           : 4643 ( 9 pps approx.)
        p8 = re.compile(r'^Total Packets +: +(?P<total_packets>\d+) +\( +(?P<pps_approx>\d+) pps approx\.\)$')

        # OIF Count               : 3
        p9 = re.compile(r'^OIF Count +: +(?P<oif_count>\d+)$')

        # OIF Details:
        p10 = re.compile(r'^OIF Details:$')

        # AdjID          Interface          ParentIf        HwFlag      Flags
        # 0xc851         Tu315              --------         ---        F NS
        # AdjID          Interface          ParentIf        HwFlag      Flags      IntfType       MsgType
        # 0xf80053e6     Tu1                --------         Cpu        A          HW_UNSUPP      NORMAL        
        p11 = re.compile(r'^(?P<adjid>[\w]+) +(?P<interface>[\w\/]+) +(?P<parentif>[\w\-]+) +(?P<hwflag>[\w\-]+) +(?P<flags>[a-zA-Z ]+)( +(?P<intf_type>[\w]+) +(?P<msg_type>[\w]+))?$')

        # GID                   : 8631
        p12 = re.compile(r'^GID +: +(?P<gid>\d+)$')

        # MCID OID Asic[0]      : 1346
        p13 = re.compile(r'^MCID OID Asic\[(?P<asic>[\d]+)] +: +(?P<mcid_oid_asic>\d+)$')

        # Hardware Info ASIC[0] :
        p14 = re.compile(r'^Hardware Info ASIC\[(?P<asic_number>[\d]+)] +:$')

        # IP MCID OID         :3272 (cookie:urid:0x30::1b6)
        p15 = re.compile(r'^IP MCID OID +:(?P<ip_mcid_oid>\d+) +\(cookie:urid:(?P<cookie>[\w\:\.\/]+)\)$')

        # RPF PORT OID        :1493
        p16 = re.compile(r'^RPF PORT OID +:(?P<rpf_port_oid>\d+)$')

        # punt_on_rpf_fail    :1
        p17 = re.compile(r'^punt_on_rpf_fail +:(?P<punt_on_rpf_fail>\d+)$')

        # punt_and_forward    :1
        p18 = re.compile(r'^punt_and_forward +:(?P<punt_and_forward>\d+)$')

        # use_rpfid           :0
        p19 = re.compile(r'^use_rpfid +:(?P<use_rpfid>\d+)$')

        # rpfid               :0
        p20 = re.compile(r'^rpfid +:(?P<rpfid>\d+)$')

        # enable_rpf_check    :1
        p21 = re.compile(r'^enable_rpf_check +:(?P<enable_rpf_check>\d+)$')

        # Ec_seed                 : 6
        p22 = re.compile(r'^Ec_seed +: +(?P<ec_seed>\d+)$')

        # npi_mroute_ent          : 0x118812c5e20
        p23 = re.compile(r'^npi_mroute_ent +: +(?P<npi_mroute_ent>[\w]+)$')

        # svi_fwd_ifs             : 2
        p24 = re.compile(r'^svi_fwd_ifs +: +(?P<svi_fwd_ifs>\d+)$')

        # ios_f_ifs/mlist_f_ifs   : 1/1
        p25 = re.compile(r'^ios_f_ifs/mlist_f_ifs +: +(?P<ios_f_ifs>\d+)/(?P<mlist_f_ifs>\d+)$')

        index = 1
        oif_details = []
        for line in output.splitlines():
            line = line.strip()

            # Mvrf: 3  ( 40::2, ff1e::1 ) Attrs:
            m = p0.match(line)
            if m:
                group = m.groupdict()
                mfib_dict = ret_dict.setdefault("mfib", {}).setdefault(index, {})
                mfib_dict['mvrf'] = int(group['mvrf'])
                mfib_dict['group'] = group['group']
                mfib_dict['source'] = group['source']
                attrs_dict = mfib_dict.setdefault('attrs', {})
                index += 1
                continue

            # Hw Flag                 : InHw
            m = p1.match(line)
            if m:
                attrs_dict['hw_flag'] = m.groupdict()['hw_flag']
                continue

            # Mlist Flags             : None
            m = p2.match(line)
            if m:
                attrs_dict['mlist_flags'] = m.groupdict()['mlist_flags']
                continue

            # Mlist_hndl (Id)         : 0x11889275ea0 ( 0xc823 )
            m = p3.match(line)
            if m:
                attrs_dict['mlist_hndl_id'] = m.groupdict()['mlist_hndl_id']
                continue

            # Mlist Urid              : 0x10000000003238e8
            m = p4.match(line)
            if m:
                attrs_dict['mlist_urid'] = m.groupdict()['mlist_urid']
                continue

            # Fset Urid (Hash)        : 0x300000000031f715 ( 68af2994 )
            m = p5.match(line)
            if m:
                attrs_dict['fset_urid_hash'] = m.groupdict()['fset_urid_hash']
                continue

            # Fset Aux Urid           : 0x0
            m = p5_1.match(line)
            if m:
                attrs_dict['fset_aux_urid'] = m.groupdict()['fset_aux_urid']
                continue

            # RPF Adjacency ID        : 0xf80059d2
            m = p6.match(line)
            if m:
                attrs_dict['rpf_adjacency_id'] = m.groupdict()['rpf_adjacency_id']
                continue

            # CPU Credit              : 0
            m = p7.match(line)
            if m:
                attrs_dict['cpu_credit'] = int(m.groupdict()['cpu_credit'])
                continue

            # Total Packets           : 4643 ( 9 pps approx.)
            m = p8.match(line)
            if m:
                attrs_dict['total_packets'] = int(m.groupdict()['total_packets'])
                attrs_dict['pps_approx'] = int(m.groupdict()['pps_approx'])
                continue

            # OIF Count               : 3
            m = p9.match(line)
            if m:
                attrs_dict['oif_count'] = int(m.groupdict()['oif_count'])
                continue

            # OIF Details:
            m = p10.match(line)
            if m:
                attrs_dict['oif_details'] = oif_details
                continue

            # AdjID          Interface          ParentIf        HwFlag      Flags
            # 0xc851         Tu315              --------         ---        F NS
            m = p11.match(line)
            if m:
                oif_details.append(m.groupdict())
                continue

            # GID                   : 8631
            m = p12.match(line)
            if m:
                attrs_dict['gid'] = int(m.groupdict()['gid'])
                continue

            # MCID OID Asic[0]      : 1346
            m = p13.match(line)
            if m:
                group = m.groupdict()
                asic_dict = attrs_dict.setdefault('asic', {}).setdefault(int(group['asic']), {})            
                asic_dict['mcid_oid_asic'] = int(group['mcid_oid_asic'])
                continue

            # Hardware Info ASIC[0] :
            m = p14.match(line)
            if m:
                group = m.groupdict()
                hw_dict = attrs_dict.setdefault('hw_asic_info', {}).setdefault(int(group['asic_number']), {})            
                continue

            # IP MCID OID         :3272 (cookie:urid:0x30::1b6)
            m = p15.match(line)
            if m:
                group = m.groupdict()
                hw_dict['ip_mcid_oid'] = int(group['ip_mcid_oid'])
                hw_dict['cookie'] = group['cookie']
                continue

            # RPF PORT OID        :1493
            m = p16.match(line)
            if m:
                hw_dict['rpf_port_oid'] = int(m.groupdict()['rpf_port_oid'])
                continue

            # punt_on_rpf_fail    :1
            m = p17.match(line)
            if m:
                hw_dict['punt_on_rpf_fail'] = int(m.groupdict()['punt_on_rpf_fail'])
                continue

            # punt_and_forward    :1
            m = p18.match(line)
            if m:
                hw_dict['punt_and_forward'] = int(m.groupdict()['punt_and_forward'])
                continue

            # use_rpfid           :0
            m = p19.match(line)
            if m:
                hw_dict['use_rpfid'] = int(m.groupdict()['use_rpfid'])
                continue

            # rpfid               :0
            m = p20.match(line)
            if m:
                hw_dict['rpfid'] = int(m.groupdict()['rpfid'])
                continue

            # enable_rpf_check    :1
            m = p21.match(line)
            if m:
                hw_dict['enable_rpf_check'] = int(m.groupdict()['enable_rpf_check'])
                continue

            # Ec_seed                 : 6
            m = p22.match(line)
            if m:
                attrs_dict['ec_seed'] = int(m.groupdict()['ec_seed'])
                continue

            # npi_mroute_ent          : 0x118812c5e20
            m = p23.match(line)
            if m:
                attrs_dict['npi_mroute_ent'] = m.groupdict()['npi_mroute_ent']
                continue

            # svi_fwd_ifs             : 2
            m = p24.match(line)
            if m:
                attrs_dict['svi_fwd_ifs'] = int(m.groupdict()['svi_fwd_ifs'])
                continue

            # ios_f_ifs/mlist_f_ifs   : 1/1
            m = p25.match(line)
            if m:
                attrs_dict['ios_f_ifs'] = int(m.groupdict()['ios_f_ifs'])
                attrs_dict['mlist_f_ifs'] = int(m.groupdict()['mlist_f_ifs'])
                continue

        return ret_dict


class ShowPlatformSoftwareFedSwitchActiveIpMfibVrfSchema(MetaParser):
    """Schema for show platform software fed switch active ipv6 mfib vrf {vrf_name} {group} {source}"""
    schema = {
        'mfib': {
            'mvrf': int,
            'group': str,
            'source': str,
            'attrs': {
                'hw_flag': str,
                'mlist_flags': str,
                'mlist_hndl_id': str,
                'mlist_urid': str,
                'fset_urid_hash': str,
                'rpf_adjacency_id': str,
                'cpu_credit': int,
                'total_packets': int,
                'pps_approx': int,
                'oif_count': int,
                'oif_details': list,
                'gid': int,
                'mcid_oid_asic': int,
            }
        }
    }

class ShowPlatformSoftwareFedSwitchActiveIpMfibVrf(ShowPlatformSoftwareFedSwitchActiveIpMfibVrfSchema):
    """Parser for show platform software fed switch active ipv6 mfib vrf {vrf_name} {group} {source}"""

    cli_command = [
        'show platform software fed {switch} {active} ipv6 mfib vrf {vrf_name} {group} {source}',
        'show platform software fed {switch} {active} ipv6 mfib {group} {source}',
        'show platform software fed {active} ipv6 mfib vrf {vrf_name} {group} {source}',
        'show platform software fed {active} ipv6 mfib {group} {source}'
    ]

    def cli(self, switch='', active='', vrf_name='', group='', source='', output=None):
        if output is None:
            if vrf_name:
                if switch:
                    cmd = self.cli_command[0].format(switch=switch, active=active, vrf_name=vrf_name, group=group, source=source)
                else:
                    cmd = self.cli_command[2].format(active=active, vrf_name=vrf_name, group=group, source=source)
            else:
                if switch:
                    cmd = self.cli_command[1].format(switch=switch, active=active, group=group, source=source)
                else:
                    cmd = self.cli_command[3].format(active=active, group=group, source=source)
            output = self.device.execute(cmd)

        ret_dict = {}

        # Mvrf: 3  ( 40::2, ff1e::1 ) Attrs:
        p0 = re.compile(r'^Mvrf: +(?P<mvrf>\d+) +\( +(?P<source>[\w\:\.\/]+), +(?P<group>[\w\:\.\/]+) +\) +Attrs:$')

        # Hw Flag                 : InHw
        # Hw Flag                 : InHw  EntryActive
        p1 = re.compile(r'^Hw Flag +: +(?P<hw_flag>[\w\s]+)$')        

        # Mlist Flags             : None
        p2 = re.compile(r'^Mlist Flags +: +(?P<mlist_flags>\w+)$')

        # Mlist_hndl (Id)         : 0x11889275ea0 ( 0xc823 )
        p3 = re.compile(r'^Mlist_hndl \(Id\) +: +(?P<mlist_hndl_id>[\w\(\)\s]+)$')

        # Mlist Urid              : 0x10000000003238e8
        p4 = re.compile(r'^Mlist Urid +: +(?P<mlist_urid>[\w]+)$')

        # Fset Urid (Hash)        : 0x300000000031f715 ( 68af2994 )
        p5 = re.compile(r'^Fset Urid \(Hash\) +: +(?P<fset_urid_hash>[\w\(\)\s]+)$')

        # RPF Adjacency ID        : 0xf80059d2
        p6 = re.compile(r'^RPF Adjacency ID +: +(?P<rpf_adjacency_id>[\w]+)$')

        # CPU Credit              : 0
        p7 = re.compile(r'^CPU Credit +: +(?P<cpu_credit>\d+)$')

        # Total Packets           : 4643 ( 9 pps approx.)
        p8 = re.compile(r'^Total Packets +: +(?P<total_packets>\d+) +\( +(?P<pps_approx>\d+) pps approx\.\)$')

        # OIF Count               : 3
        p9 = re.compile(r'^OIF Count +: +(?P<oif_count>\d+)$')

        # OIF Details:
        p10 = re.compile(r'^OIF Details:$')

        # AdjID          Interface          ParentIf        HwFlag      Flags
        # 0xc851         Tu315              --------         ---        F NS
        p11 = re.compile(r'^(?P<adjid>[\w]+) +(?P<interface>[\w\/]+) +(?P<parentif>[\w\-]+) +(?P<hwflag>[\w\-]+) +(?P<flags>[\w\s]+)$')

        # GID                   : 8631
        p12 = re.compile(r'^GID +: +(?P<gid>\d+)$')

        # MCID OID Asic[0]      : 1346
        p13 = re.compile(r'^MCID OID Asic\[0\] +: +(?P<mcid_oid_asic>\d+)$')

        oif_details = []
        for line in output.splitlines():
            line = line.strip()

            # Mvrf: 3  ( 40::2, ff1e::1 ) Attrs:
            m = p0.match(line)
            if m:
                group = m.groupdict()
                mfib_dict = ret_dict.setdefault('mfib', {})
                mfib_dict['mvrf'] = int(group['mvrf'])
                mfib_dict['group'] = group['group']
                mfib_dict['source'] = group['source']
                attrs_dict = mfib_dict.setdefault('attrs', {})
                continue

            # Hw Flag                 : InHw
            m = p1.match(line)
            if m:
                attrs_dict['hw_flag'] = m.groupdict()['hw_flag']
                continue

            # Mlist Flags             : None
            m = p2.match(line)
            if m:
                attrs_dict['mlist_flags'] = m.groupdict()['mlist_flags']
                continue

            # Mlist_hndl (Id)         : 0x11889275ea0 ( 0xc823 )
            m = p3.match(line)
            if m:
                attrs_dict['mlist_hndl_id'] = m.groupdict()['mlist_hndl_id']
                continue

            # Mlist Urid              : 0x10000000003238e8
            m = p4.match(line)
            if m:
                attrs_dict['mlist_urid'] = m.groupdict()['mlist_urid']
                continue

            # Fset Urid (Hash)        : 0x300000000031f715 ( 68af2994 )
            m = p5.match(line)
            if m:
                attrs_dict['fset_urid_hash'] = m.groupdict()['fset_urid_hash']
                continue

            # RPF Adjacency ID        : 0xf80059d2
            m = p6.match(line)
            if m:
                attrs_dict['rpf_adjacency_id'] = m.groupdict()['rpf_adjacency_id']
                continue

            # CPU Credit              : 0
            m = p7.match(line)
            if m:
                attrs_dict['cpu_credit'] = int(m.groupdict()['cpu_credit'])
                continue

            # Total Packets           : 4643 ( 9 pps approx.)
            m = p8.match(line)
            if m:
                attrs_dict['total_packets'] = int(m.groupdict()['total_packets'])
                attrs_dict['pps_approx'] = int(m.groupdict()['pps_approx'])
                continue

            # OIF Count               : 3
            m = p9.match(line)
            if m:
                attrs_dict['oif_count'] = int(m.groupdict()['oif_count'])
                continue

            # OIF Details:
            m = p10.match(line)
            if m:
                attrs_dict['oif_details'] = oif_details
                continue

            # AdjID          Interface          ParentIf        HwFlag      Flags
            # 0xc851         Tu315              --------         ---        F NS
            m = p11.match(line)
            if m:
                oif_details.append(m.groupdict())
                continue

            # GID                   : 8631
            m = p12.match(line)
            if m:
                attrs_dict['gid'] = int(m.groupdict()['gid'])
                continue

            # MCID OID Asic[0]      : 1346
            m = p13.match(line)
            if m:
                attrs_dict['mcid_oid_asic'] = int(m.groupdict()['mcid_oid_asic'])
                continue

        return ret_dict

class ShowPlatformSoftwareFedIpIgmpSnoopingGroupVlanSchema(MetaParser):
    """Schema for show platform software fed [switch] [module] ip igmp snooping group vlan <vlan-id> <group>"""
    schema = {
        'vlan': int,
        'group': str,
        'member_ports': ListOf({
            'port_channel': str,
            'port': str
        }),
        'dependent_users_count': int,
        'group_urid': str,
        'fset_urid_hash': str,
        'layer_3_stub_entry': str,
        'gid': int,
        'mcid_asic': int,
        Optional('hw_group_entry_asic'): ListOf({
            'hw_mcid_oid': int
        })
    }

class ShowPlatformSoftwareFedIpIgmpSnoopingGroupVlan(ShowPlatformSoftwareFedIpIgmpSnoopingGroupVlanSchema):
    """Parser for show platform software fed [switch] [module] ip igmp snooping group vlan <vlan-id> <group>"""

    cli_command = [
        'show platform software fed {switch} {module} ip igmp snooping group vlan {vlan_id} {group}',
        'show platform software fed {switch} {module} ip igmp snooping group vlan {vlan_id} {group} detail'
    ]

    def cli(self, switch='', module='', vlan_id='', group='', detail=False, output=None):
        if output is None:
            if detail:
                cmd = self.cli_command[1].format(switch=switch, module=module, vlan_id=vlan_id, group=group)
            else:
                cmd = self.cli_command[0].format(switch=switch, module=module, vlan_id=vlan_id, group=group)
            output = self.device.execute(cmd)

        ret_dict = {}

        # (Vlan: 10, 225.0.0.1)
        p0 = re.compile(r'^\(Vlan: +(?P<vlan>\d+), +(?P<group>[\d\.]+)\)$')

        # Port-channel2 (Port:HundredGigE1/1/0/21)
        p1 = re.compile(r'^(?P<port_channel>Port-channel\d+) +\(Port:(?P<port>[\w\/]+)\)$')

        # Dependent Users Count   : 2
        p2 = re.compile(r'^Dependent Users Count +: +(?P<dependent_users_count>\d+)$')

        # Group Urid              : 0x6000000000000001
        p3 = re.compile(r'^Group Urid +: +(?P<group_urid>[\w]+)$')

        # Fset Urid ( Hash )      : 0x2000000000000011 \( (?P<fset_urid_hash>[\w]+) \)
        p4 = re.compile(r'^Fset Urid \( Hash \) +: +(?P<fset_urid>[\w]+) +\( +(?P<fset_urid_hash>[\w]+) +\)$')

        # Layer 3 Stub Entry      : No
        p5 = re.compile(r'^Layer 3 Stub Entry +: +(?P<layer_3_stub_entry>\w+)$')

        # Gid                     : 8212
        p6 = re.compile(r'^Gid +: +(?P<gid>\d+)$')

        # Mcid Asic[0]            : 1549
        p7 = re.compile(r'^Mcid Asic\[0\] +: +(?P<mcid_asic>\d+)$')

        # Hw Group Entry Asic[0]:
        p8 = re.compile(r'^Hw Group Entry Asic\[0\]:$')

        # Hw Mcid Oid[0]      : 1549
        p9 = re.compile(r'^Hw Mcid Oid\[0\] +: +(?P<hw_mcid_oid>\d+)$')

        member_ports = []
        hw_group_entry_asic = []
        for line in output.splitlines():
            line = line.strip()

            # (Vlan: 10, 225.0.0.1)
            m = p0.match(line)
            if m:
                group = m.groupdict()
                ret_dict['vlan'] = int(group['vlan'])
                ret_dict['group'] = group['group']
                continue

            # Port-channel2 (Port:HundredGigE1/1/0/21)
            m = p1.match(line)
            if m:
                member_ports.append(m.groupdict())
                continue

            # Dependent Users Count   : 2
            m = p2.match(line)
            if m:
                ret_dict['dependent_users_count'] = int(m.groupdict()['dependent_users_count'])
                continue

            # Group Urid              : 0x6000000000000001
            m = p3.match(line)
            if m:
                ret_dict['group_urid'] = m.groupdict()['group_urid']
                continue

            # Fset Urid ( Hash )      : 0x2000000000000011 ( 134439a0 )
            m = p4.match(line)
            if m:
                ret_dict['fset_urid_hash'] = m.groupdict()['fset_urid_hash']
                continue

            # Layer 3 Stub Entry      : No
            m = p5.match(line)
            if m:
                ret_dict['layer_3_stub_entry'] = m.groupdict()['layer_3_stub_entry']
                continue

            # Gid                     : 8212
            m = p6.match(line)
            if m:
                ret_dict['gid'] = int(m.groupdict()['gid'])
                continue

            # Mcid Asic[0]            : 1549
            m = p7.match(line)
            if m:
                ret_dict['mcid_asic'] = int(m.groupdict()['mcid_asic'])
                continue

            # Hw Group Entry Asic[0]:
            m = p8.match(line)
            if m:
                continue

            # Hw Mcid Oid[0]      : 1549
            m = p9.match(line)
            if m:
                hw_group_entry_asic.append({'hw_mcid_oid': int(m.groupdict()['hw_mcid_oid'])})
                continue

        if member_ports:
            ret_dict['member_ports'] = member_ports

        if hw_group_entry_asic:
            ret_dict['hw_group_entry_asic'] = hw_group_entry_asic

        return ret_dict


class ShowPlatformSoftwareFedIpIgmpSnoopingGroupSchema(MetaParser):
    """Schema for show platform software fed [switch] [module] ip igmp snooping group"""
    schema = {
        Optional('number_of_group_entries'): int,
        'groups': ListOf({
            'vlan': int,
            'group': str,
            'member_ports': ListOf(str),
            'dependent_users_count': int,
            'group_urid': str,
            'fset_urid_hash': str,
            'layer_3_stub_entry': str,
            'group_flags': str,
            'gid': int,
            'mcid_asic': int
        })
    }

class ShowPlatformSoftwareFedIpIgmpSnoopingGroup(ShowPlatformSoftwareFedIpIgmpSnoopingGroupSchema):
    """Parser for show platform software fed [switch] [module] ip igmp snooping group"""

    cli_command = 'show platform software fed {switch} {module} ip igmp snooping group'

    def cli(self, switch='', module='', output=None):
        if output is None:
            cmd = self.cli_command.format(switch=switch, module=module)
            output = self.device.execute(cmd)

        ret_dict = {}
        groups = []

        # Regex patterns
        # Number of Group entries: 1
        p0 = re.compile(r'^Number of Group entries: +(?P<number_of_group_entries>\d+)$')

        # (Vlan: 104, 232.0.31.64)
        p1 = re.compile(r'^\(Vlan: +(?P<vlan>\d+), +(?P<group>[\d\.]+)\)$')
        # Member ports           : Port-channel2
        p2 = re.compile(r'^Member ports +: +(?P<member_ports_count>\d+)$')
        # Member ports
        p3 = re.compile(r'^(?P<member_port>[\w\/]+)$')
        # Dependent Users Count
        p4 = re.compile(r'^Dependent Users Count +: +(?P<dependent_users_count>\d+)$')
        # Group Urid
        p5 = re.compile(r'^Group Urid +: +(?P<group_urid>[\w]+)$')
        # Fset Urid ( Hash )
        p6 = re.compile(r'^Fset Urid \( Hash \) +: +[\w]+ \( (?P<fset_urid_hash>[\w]+) \)$')
        # Layer 3 Stub Entry
        p7 = re.compile(r'^Layer 3 Stub Entry +: +(?P<layer_3_stub_entry>\w+)$')
        # Group Flags
        p8 = re.compile(r'^Group Flags +: +(?P<group_flags>\w+)$')
        # Gid
        p9 = re.compile(r'^Gid +: +(?P<gid>\d+)$')
        # Mcid Asic[0]
        p10 = re.compile(r'^Mcid Asic\[0\] +: +(?P<mcid_asic>\d+)$')

        current_group = None
        member_ports = []

        for line in output.splitlines():
            line = line.strip().rstrip('\\')

            # Match Number of Group entries
            m = p0.match(line)
            if m:
                ret_dict['number_of_group_entries'] = int(m.group('number_of_group_entries'))
                continue

            # Match (Vlan: 104, 232.0.31.64)
            m = p1.match(line)
            if m:
                # Save the previous group if it exists
                if current_group:
                    current_group['member_ports'] = member_ports
                    groups.append(current_group)
                # Start a new group
                current_group = {
                    'vlan': int(m.group('vlan')),
                    'group': m.group('group')
                }
                member_ports = []
                continue

            # Match Member ports
            m = p2.match(line)
            if m:
                continue

            # Match individual member ports
            m = p3.match(line)
            if m:
                member_ports.append(m.group('member_port'))
                continue

            # Match Dependent Users Count   : 2
            m = p4.match(line)
            if m:
                current_group['dependent_users_count'] = int(m.group('dependent_users_count'))
                continue

            # Match Group Urid              : 0x600000000003dd64
            m = p5.match(line)
            if m:
                current_group['group_urid'] = m.group('group_urid')
                continue

            # Match Fset Urid ( Hash )      : 0x2000000000002154 ( f2e2a15a )
            m = p6.match(line)
            if m:
                current_group['fset_urid_hash'] = m.group('fset_urid_hash')
                continue

            # Match Layer 3 Stub Entry      : No
            m = p7.match(line)
            if m:
                current_group['layer_3_stub_entry'] = m.group('layer_3_stub_entry')
                continue

            # Match Group Flags             : None
            m = p8.match(line)
            if m:
                current_group['group_flags'] = m.group('group_flags')
                continue

            # Match Gid                     : 32377
            m = p9.match(line)
            if m:
                current_group['gid'] = int(m.group('gid'))
                continue

            # Match Mcid Asic[0]            : 2645
            m = p10.match(line)
            if m:
                current_group['mcid_asic'] = int(m.group('mcid_asic'))
                continue

        # Add the last group
        if current_group:
            current_group['member_ports'] = member_ports
            groups.append(current_group)

        # Add groups to the final dictionary
        ret_dict['groups'] = groups
        return ret_dict

class ShowPlatformSoftwareFedActiveIpTypeMfibGroupSchema(MetaParser):
    """
    Schema for show platform software fed {switch} {switch_var} ip mfib {group}
    """
    schema = {
        'mfib': {
            int : {
                'mvrf': int,
                'group': str,
                'source': str,
                'attrs': {
                    'hw_flag': str,
                    'mlist_flags': str,
                    'mlist_hndl_id': str,
                    'mlist_urid': str,
                    'fset_urid_hash': str,
                    'rpf_adjacency_id': str,
                    'cpu_credit': int,
                    Optional('total_packets'): int,
                    Optional('pps_approx'): int,
                    'oif_count': int,
                    'oif_details': list,
                    'gid': int,
                    'asic': {
                        int: {
                            'mcid_oid_asic': int,
                        },
                    }
                }
            }
        }
    }

class ShowPlatformSoftwareFedActiveIpTypeMfibGroup(ShowPlatformSoftwareFedActiveIpTypeMfibGroupSchema):
    """
    Parser for show platform software fed {switch} {switch_var} {ip_type} mfib {group}
    """

    cli_command = [
        'show platform software fed {switch} {switch_var} {ip_type} mfib {group}',
        'show platform software fed {switch_var} {ip_type} mfib {group}'
    ]

    def cli(self, switch='', switch_var='', group='', ip_type='', output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(switch=switch, switch_var=switch_var, group=group, ip_type=ip_type)
            else:
                cmd = self.cli_command[1].format(switch_var=switch_var, group=group, ip_type=ip_type)
            output = self.device.execute(cmd)

        ret_dict = {}

        # Mvrf: 3  ( 40::2, ff1e::1 ) Attrs:
        # Mvrf: 0  ( *, ff13::1 ) Attrs: C
        p0 = re.compile(r'^Mvrf: +(?P<mvrf>\d+) +\( +(?P<source>[\w\:\.\/\*]+), +(?P<group>[\w\:\.\/]+) +\) +Attrs:( C)?$')

        # Hw Flag                 : InHw
        # Hw Flag                 : InHw  EntryActive
        p1 = re.compile(r'^Hw Flag +: +(?P<hw_flag>[\w\s]+)$')        

        # Mlist Flags             : None
        p2 = re.compile(r'^Mlist Flags +: +(?P<mlist_flags>\w+)$')

        # Mlist_hndl (Id)         : 0x11889275ea0 ( 0xc823 )
        p3 = re.compile(r'^Mlist_hndl \(Id\) +: +(?P<mlist_hndl_id>[\w\(\)\s]+)$')

        # Mlist Urid              : 0x10000000003238e8
        p4 = re.compile(r'^Mlist Urid +: +(?P<mlist_urid>[\w]+)$')

        # Fset Urid (Hash)        : 0x300000000031f715 ( 68af2994 )
        p5 = re.compile(r'^Fset Urid \(Hash\) +: +(?P<fset_urid_hash>[\w\(\)\s]+)$')

        # RPF Adjacency ID        : 0xf80059d2
        p6 = re.compile(r'^RPF Adjacency ID +: +(?P<rpf_adjacency_id>[\w]+)$')

        # CPU Credit              : 0
        p7 = re.compile(r'^CPU Credit +: +(?P<cpu_credit>\d+)$')

        # Total Packets           : 4643 ( 9 pps approx.)
        p8 = re.compile(r'^Total Packets +: +(?P<total_packets>\d+) +\( +(?P<pps_approx>\d+) pps approx\.\)$')

        # OIF Count               : 3
        p9 = re.compile(r'^OIF Count +: +(?P<oif_count>\d+)$')

        # OIF Details:
        p10 = re.compile(r'^OIF Details:$')

        # AdjID          Interface          ParentIf        HwFlag      Flags
        # 0xc851         Tu315              --------         ---        F NS
        p11 = re.compile(r'^(?P<adjid>[\w]+) +(?P<interface>[\w\/]+) +(?P<parentif>[\w\-]+) +(?P<hwflag>[\w\-]+) +(?P<flags>[\w\s]+)$')

        # GID                   : 8631
        p12 = re.compile(r'^GID +: +(?P<gid>\d+)$')

        # MCID OID Asic[0]      : 1346
        p13 = re.compile(r'^MCID OID Asic\[(?P<asic>[\d]+)] +: +(?P<mcid_oid_asic>\d+)$')

        index = 1
        oif_details = []
        for line in output.splitlines():
            line = line.strip()

            # Mvrf: 3  ( 40::2, ff1e::1 ) Attrs:
            m = p0.match(line)
            if m:
                group = m.groupdict()
                mfib_dict = ret_dict.setdefault("mfib", {}).setdefault(index, {})
                mfib_dict['mvrf'] = int(group['mvrf'])
                mfib_dict['group'] = group['group']
                mfib_dict['source'] = group['source']
                attrs_dict = mfib_dict.setdefault('attrs', {})
                index += 1
                continue

            # Hw Flag                 : InHw
            m = p1.match(line)
            if m:
                attrs_dict['hw_flag'] = m.groupdict()['hw_flag']
                continue

            # Mlist Flags             : None
            m = p2.match(line)
            if m:
                attrs_dict['mlist_flags'] = m.groupdict()['mlist_flags']
                continue

            # Mlist_hndl (Id)         : 0x11889275ea0 ( 0xc823 )
            m = p3.match(line)
            if m:
                attrs_dict['mlist_hndl_id'] = m.groupdict()['mlist_hndl_id']
                continue

            # Mlist Urid              : 0x10000000003238e8
            m = p4.match(line)
            if m:
                attrs_dict['mlist_urid'] = m.groupdict()['mlist_urid']
                continue

            # Fset Urid (Hash)        : 0x300000000031f715 ( 68af2994 )
            m = p5.match(line)
            if m:
                attrs_dict['fset_urid_hash'] = m.groupdict()['fset_urid_hash']
                continue

            # RPF Adjacency ID        : 0xf80059d2
            m = p6.match(line)
            if m:
                attrs_dict['rpf_adjacency_id'] = m.groupdict()['rpf_adjacency_id']
                continue

            # CPU Credit              : 0
            m = p7.match(line)
            if m:
                attrs_dict['cpu_credit'] = int(m.groupdict()['cpu_credit'])
                continue

            # Total Packets           : 4643 ( 9 pps approx.)
            m = p8.match(line)
            if m:
                attrs_dict['total_packets'] = int(m.groupdict()['total_packets'])
                attrs_dict['pps_approx'] = int(m.groupdict()['pps_approx'])
                continue

            # OIF Count               : 3
            m = p9.match(line)
            if m:
                attrs_dict['oif_count'] = int(m.groupdict()['oif_count'])
                continue

            # OIF Details:
            m = p10.match(line)
            if m:
                attrs_dict['oif_details'] = oif_details
                continue

            # AdjID          Interface          ParentIf        HwFlag      Flags
            # 0xc851         Tu315              --------         ---        F NS
            m = p11.match(line)
            if m:
                oif_details.append(m.groupdict())
                continue

            # GID                   : 8631
            m = p12.match(line)
            if m:
                attrs_dict['gid'] = int(m.groupdict()['gid'])
                continue

            # MCID OID Asic[0]      : 1346
            m = p13.match(line)
            if m:
                group = m.groupdict()
                asic_dict = attrs_dict.setdefault('asic', {}).setdefault(int(group['asic']), {})            
                asic_dict['mcid_oid_asic'] = int(group['mcid_oid_asic'])
                continue

        return ret_dict
    
class ShowPlatformSoftwareFedSwitchIpv6MldSnoopingGroupSchema(MetaParser):
    """Schema for show platform software fed {switch} {state} ipv6 mld snooping group"""
    schema = {
        "number_of_group_entries": int,
        "groups": {
            Any(): {
                "vlan": int,
                "member_ports": int,
                "dependent_users_count": int,
                "group_urid": str,
                "fset_urid": str,
                "fset_hash": str,
                "layer_3_stub_entry": str,
                "group_flags": str,
                "gid": int,
                "mcid_asic": int,
                Optional("member_port_details"): list,
            }
        }
    }

class ShowPlatformSoftwareFedSwitchIpv6MldSnoopingGroup(ShowPlatformSoftwareFedSwitchIpv6MldSnoopingGroupSchema):
    """Parser for show platform software fed {switch} {state} ipv6 mld snooping group"""

    cli_command = "show platform software fed {switch} {state} ipv6 mld snooping group"

    def cli(self, switch, state, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch=switch, state=state))

        ret_dict = {}
        group_dict = None

        # Number of Group entries: 80
        p1 = re.compile(r"^Number of Group entries: (?P<number_of_group_entries>\d+)$")

        # (Vlan: 13, ff13::2:14)
        p2 = re.compile(r"^\(Vlan: (?P<vlan>\d+), (?P<group>[\w:]+)\)$")

        # Member ports            : 0
        p3 = re.compile(r"^Member ports\s+:\s+(?P<member_ports>\d+)$")

        # Dependent Users Count   : 2
        p4 = re.compile(r"^Dependent Users Count\s+:\s+(?P<dependent_users_count>\d+)$")

        # Group Urid              : 0x70000000000003c6
        p5 = re.compile(r"^Group Urid\s+:\s+(?P<group_urid>\S+)$")

        # Fset Urid ( Hash )      : 0x2000000000007d82 \( (?P<fset_hash>\w+) \)
        p6 = re.compile(r"^Fset Urid \( Hash \)\s+:\s+(?P<fset_urid>\S+) \(\s+(?P<fset_hash>\w+)\s+\)$")

        # Layer 3 Stub Entry      : Yes
        p7 = re.compile(r"^Layer 3 Stub Entry\s+:\s+(?P<layer_3_stub_entry>\w+)$")

        # Group Flags             : None
        p8 = re.compile(r"^Group Flags\s+:\s+(?P<group_flags>\w+)$")

        # Gid                     : 8198
        p9 = re.compile(r"^Gid\s+:\s+(?P<gid>\d+)$")

        # Mcid Asic[0]            : 0
        p10 = re.compile(r"^Mcid Asic\[0\]\s+:\s+(?P<mcid_asic>\d+)$")

        # Port-channel92 (Port:HundredGigE1/0/6)
        p11 = re.compile(r"^(?P<member_port_details>[\w\-\/\(\):]+)$")

        for line in output.splitlines():
            line = line.strip()

            # Number of Group entries: 80
            m = p1.match(line)
            if m:
                ret_dict["number_of_group_entries"] = int(m.group("number_of_group_entries"))
                continue

            # (Vlan: 13, ff13::2:14)
            m = p2.match(line)
            if m:
                group = m.group("group")
                group_dict = ret_dict.setdefault("groups", {}).setdefault(group, {})
                group_dict["vlan"] = int(m.group("vlan"))
                continue

            # Member ports            : 0
            m = p3.match(line)
            if m:
                group_dict["member_ports"] = int(m.group("member_ports"))
                continue

            # Dependent Users Count   : 2
            m = p4.match(line)
            if m:
                group_dict["dependent_users_count"] = int(m.group("dependent_users_count"))
                continue

            # Group Urid              : 0x70000000000003c6
            m = p5.match(line)
            if m:
                group_dict["group_urid"] = m.group("group_urid")
                continue

            # Fset Urid ( Hash )      : 0x2000000000007d82 ( 7839ab25 )
            m = p6.match(line)
            if m:
                group_dict["fset_urid"] = m.group("fset_urid")
                group_dict["fset_hash"] = m.group("fset_hash")
                continue

            # Layer 3 Stub Entry      : Yes
            m = p7.match(line)
            if m:
                group_dict["layer_3_stub_entry"] = m.group("layer_3_stub_entry")
                continue

            # Group Flags             : None
            m = p8.match(line)
            if m:
                group_dict["group_flags"] = m.group("group_flags")
                continue

            # Gid                     : 8198
            m = p9.match(line)
            if m:
                group_dict["gid"] = int(m.group("gid"))
                continue

            # Mcid Asic[0]            : 0
            m = p10.match(line)
            if m:
                group_dict["mcid_asic"] = int(m.group("mcid_asic"))
                continue

            # Port-channel92 (Port:HundredGigE1/0/6)
            m = p11.match(line)
            if m:
                member_port_details = group_dict.setdefault("member_port_details", [])
                member_port_details.append(m.group("member_port_details"))
                continue

        return ret_dict

class ShowPlatformSoftwareFedSecurityArpSnoopStatsSchema(MetaParser):
    """Schema for show platform software fed switch security-fed arp-snoop stats"""
    schema = {
        'entries': {
            Any(): {
                'oid': {
                    Any(): {
                        'packets_hits': int
                    }
                }
            }
        }
    }

class ShowPlatformSoftwareFedSecurityArpSnoopStats(ShowPlatformSoftwareFedSecurityArpSnoopStatsSchema):
    """Parser for show platform software fed switch security-fed arp-snoop stats"""

    cli_command = ['show platform software fed switch {switch_var} security-fed arp-snoop statistics',
                   'show platform software fed switch {switch_var} security-fed arp-snoop statistics {clear}']

    def cli(self, switch_var='',clear='', output=None):
        if output is None:
            if clear:
                cmd = self.cli_command[1].format(switch_var=switch_var, clear=clear)
            else:
                cmd = self.cli_command[0].format(switch_var=switch_var)
            output = self.device.execute(cmd)

        ret_dict = {}

        # ARP Snoop Port                    1442      75
        p0 = re.compile(r'^(?P<name>[\w\s]+)\s+(?P<oid>\d+)\s+(?P<packets_hits>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # ARP Snoop VLAN Unconditional      1444      5
            m = p0.match(line)
            if m:
                group = m.groupdict()
                entry_name = group['name'].strip()
                entry_dict = ret_dict.setdefault('entries', {}).setdefault(entry_name, {})
                oid_dict = entry_dict.setdefault('oid', {}).setdefault(int(group['oid']), {})
                oid_dict['packets_hits'] = int(group['packets_hits'])

        return ret_dict

class ShowPlatformSoftwareFedSecurityArpSnoopVlanSchema(MetaParser):
    """Schema for show platform software fed switch security-fed arp-snoop vlan {vlan}"""
    schema = {
        'vlan': int,
        'punject_switch_profile': str,
        'arp_snoop_enable': str,
        Optional('acls'): ListOf({
            'oid': int,
            'asic': int,
            'position': int,
            'action': str,
            'counter_oid': int
        })
    }

class ShowPlatformSoftwareFedSecurityArpSnoopVlan(ShowPlatformSoftwareFedSecurityArpSnoopVlanSchema):
    """Parser for show platform software fed switch security-fed arp-snoop vlan {vlan}"""

    cli_command = 'show platform software fed switch {switch_var} security-fed arp-snoop vlan {vlan}'

    def cli(self, switch_var='', vlan='', output=None):
        if output is None:
            cmd = self.cli_command.format(switch_var=switch_var, vlan=vlan)
            output = self.device.execute(cmd)

        ret_dict = {}

        # Vlan= 50
        p0 = re.compile(r'^Vlan= +(?P<vlan>\d+)$')

        # Punject Switch Profile: FALSE
        p1 = re.compile(r'^Punject Switch Profile: +(?P<punject_switch_profile>\w+)$')

        # ARP SNOOP enable: TRUE
        p2 = re.compile(r'^ARP SNOOP enable: +(?P<arp_snoop_enable>\w+)$')

        # Information about ACL with OID(1443) on ASIC(0)
        p3 = re.compile(r'^Information about ACL with OID\((?P<oid>\d+)\) on ASIC\((?P<asic>\d+)\)$')

        # Position Action  Counter OID
        # ----------------------------
        # 0        PUNT    1444
        p4 = re.compile(r'^(?P<position>\d+)\s+(?P<action>\w+)\s+(?P<counter_oid>\d+)$')

        acls = []
        current_acl = None

        for line in output.splitlines():
            line = line.strip()

            # Vlan= 50
            m = p0.match(line)
            if m:
                ret_dict['vlan'] = int(m.group('vlan'))
                continue

            # Punject Switch Profile: FALSE
            m = p1.match(line)
            if m:
                ret_dict['punject_switch_profile'] = m.group('punject_switch_profile')
                continue

            # ARP SNOOP enable: TRUE
            m = p2.match(line)
            if m:
                ret_dict['arp_snoop_enable'] = m.group('arp_snoop_enable')
                continue

            # Information about ACL with OID(1443) on ASIC(0)
            m = p3.match(line)
            if m:
                current_acl = {
                    'oid': int(m.group('oid')),
                    'asic': int(m.group('asic'))
                }
                continue

            # 0        PUNT    1444
            m = p4.match(line)
            if m and current_acl:
                current_acl.update({
                    'position': int(m.group('position')),
                    'action': m.group('action'),
                    'counter_oid': int(m.group('counter_oid'))
                })
                acls.append(current_acl)
                current_acl = None
                continue

        if acls:
            ret_dict['acls'] = acls

        return ret_dict   

class ShowPlatformSoftwareFedSwitchIpv6MldSnoopingGroupsVlanSchema(MetaParser):
    """Schema for show platform software fed {switch} {state} ipv6 mld snooping groups vlan {vlan-id}"""
    schema = {
        'number_of_group_entries': int,
        'groups': {
            Any(): {
                'vlan': int,
                'member_ports': int,
                'dependent_users_count': int,
                'group_urid': str,
                'fset_urid': {
                    'value': str,
                    'hash': str,
                },
                'layer_3_stub_entry': str,
                'group_flags': str,
                'gid': int,
                'mcid_asic': int,
            }
        }
    }

class ShowPlatformSoftwareFedSwitchIpv6MldSnoopingGroupsVlan(ShowPlatformSoftwareFedSwitchIpv6MldSnoopingGroupsVlanSchema):
    """Parser for show platform software fed {switch} {state} ipv6 mld snooping groups vlan {vlan-id}"""

    cli_command = 'show platform software fed {switch} {state} ipv6 mld snooping groups vlan {vlan_id}'

    def cli(self, switch, state, vlan_id, output=None):
        if output is None:
            cmd = self.cli_command.format(switch=switch, state=state, vlan_id=vlan_id)
            output = self.device.execute(cmd)

        ret_dict = {}

        # Number of Group entries: 40
        p1 = re.compile(r'^Number of Group entries:\s+(?P<number_of_group_entries>\d+)$')

        # (Vlan: 13, ff13::2:14)
        p2 = re.compile(r'^\(Vlan:\s+(?P<vlan>\d+),\s+(?P<group>[\w:]+)\)$')

        # Member ports            : 0
        p3 = re.compile(r'^Member ports\s+:\s+(?P<member_ports>\d+)$')

        # Dependent Users Count   : 2
        p4 = re.compile(r'^Dependent Users Count\s+:\s+(?P<dependent_users_count>\d+)$')

        # Group Urid              : 0x70000000000003c6
        p5 = re.compile(r'^Group Urid\s+:\s+(?P<group_urid>\S+)$')

        # Fset Urid ( Hash )      : 0x2000000000007d82 \( (?P<hash>\S+) \)
        p6 = re.compile(r'^Fset Urid \( Hash \)\s+:\s+(?P<fset_urid>\S+)\s+\(\s+(?P<hash>\S+)\s+\)$')

        # Layer 3 Stub Entry      : Yes
        p7 = re.compile(r'^Layer 3 Stub Entry\s+:\s+(?P<layer_3_stub_entry>\S+)$')

        # Group Flags             : None
        p8 = re.compile(r'^Group Flags\s+:\s+(?P<group_flags>\S+)$')

        # Gid                     : 8198
        p9 = re.compile(r'^Gid\s+:\s+(?P<gid>\d+)$')

        # Mcid Asic[0]            : 0
        p10 = re.compile(r'^Mcid Asic\[0\]\s+:\s+(?P<mcid_asic>\d+)$')

        current_group = None

        for line in output.splitlines():
            line = line.strip()

            # Number of Group entries: 40
            m = p1.match(line)
            if m:
                ret_dict['number_of_group_entries'] = int(m.group('number_of_group_entries'))
                continue

            # (Vlan: 13, ff13::2:14)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                current_group = group['group']
                group_dict = ret_dict.setdefault('groups', {}).setdefault(current_group, {})
                group_dict['vlan'] = int(group['vlan'])
                continue

            # Member ports            : 0
            m = p3.match(line)
            if m and current_group:
                ret_dict['groups'][current_group]['member_ports'] = int(m.group('member_ports'))
                continue

            # Dependent Users Count   : 2
            m = p4.match(line)
            if m and current_group:
                ret_dict['groups'][current_group]['dependent_users_count'] = int(m.group('dependent_users_count'))
                continue

            # Group Urid              : 0x70000000000003c6
            m = p5.match(line)
            if m and current_group:
                ret_dict['groups'][current_group]['group_urid'] = m.group('group_urid')
                continue

            # Fset Urid ( Hash )      : 0x2000000000007d82 ( 7839ab25 )
            m = p6.match(line)
            if m and current_group:
                fset_urid_dict = ret_dict['groups'][current_group].setdefault('fset_urid', {})
                fset_urid_dict['value'] = m.group('fset_urid')
                fset_urid_dict['hash'] = m.group('hash')
                continue

            # Layer 3 Stub Entry      : Yes
            m = p7.match(line)
            if m and current_group:
                ret_dict['groups'][current_group]['layer_3_stub_entry'] = m.group('layer_3_stub_entry')
                continue

            # Group Flags             : None
            m = p8.match(line)
            if m and current_group:
                ret_dict['groups'][current_group]['group_flags'] = m.group('group_flags')
                continue

            # Gid                     : 8198
            m = p9.match(line)
            if m and current_group:
                ret_dict['groups'][current_group]['gid'] = int(m.group('gid'))
                continue

            # Mcid Asic[0]            : 0
            m = p10.match(line)
            if m and current_group:
                ret_dict['groups'][current_group]['mcid_asic'] = int(m.group('mcid_asic'))
                continue

        return ret_dict                          

class ShowPlatformSoftwareFedSwitchActiveIpTypeMfibVrfDetailSchema(MetaParser):
    """Schema for show platform software fed switch active ipv6 mfib vrf {vrf_name} {group} {source} detail"""
    schema = {
        'mfib': {
            int : {
                'mvrf': int,
                'group': str,
                'source': str,
                'attrs': {
                    'hw_flag': str,
                    'mlist_flags': str,
                    'mlist_hndl_id': str,
                    'mlist_urid': str,
                    'fset_urid_hash': str,
                    Optional('fset_aux_urid'): str,
                    'rpf_adjacency_id': str,
                    'cpu_credit': int,
                    Optional('total_packets'): int,
                    Optional('pps_approx'): int,
                    Optional('ec_seed'): int,
                    Optional('npi_mroute_ent'): str,
                    Optional('svi_fwd_ifs'): int,
                    Optional('ios_f_ifs'): int,
                    Optional('mlist_f_ifs'): int,                    
                    'oif_count': int,
                    'oif_details': ListOf({
                        'adjid': str,
                        'interface': str,
                        Optional('parentif'): str,
                        Optional('hwflag'): str,
                        'flags': ListOf(str),
                        'intf_type': str,
                        'msg_type': str,
                        }),
                    'gid': int,
                    'asic': {
                        int: {
                            'mcid_oid_asic': int,
                        },
                    },
                    Optional('hw_asic_info'): {
                        int: {
                            Optional('ip_mcid_oid'): int,
                            Optional('cookie'): str,
                            Optional('rpf_port_oid'): int,
                            Optional('rpfid'): int,
                            Optional('use_rpfid'): int,
                            Optional('punt_and_forward'): int,
                            Optional('punt_on_rpf_fail'): int,
                            Optional('enable_rpf_check'): int,
                            }
                        }
                    }
                }
            }
        }

class ShowPlatformSoftwareFedSwitchActiveIpTypeMfibVrfDetail(ShowPlatformSoftwareFedSwitchActiveIpTypeMfibVrfDetailSchema):
    """Parser for 'show platform software fed switch active ipv6 mfib vrf {vrf_name} {group} {source} detail',
    'show platform software fed {switch} {active} {ip_type} mfib {group} {source} detail',
    'show platform software fed {active} {ip_type} mfib vrf {vrf_name} {group} {source} detail',
    'show platform software fed {active} {ip_type} mfib {group} {source} detail'
    """

    cli_command = [
        'show platform software fed {switch} {active} {ip_type} mfib vrf {vrf_name} {group} {source} detail',
        'show platform software fed {switch} {active} {ip_type} mfib {group} {source} detail',
        'show platform software fed {active} {ip_type} mfib vrf {vrf_name} {group} {source} detail',
        'show platform software fed {active} {ip_type} mfib {group} {source} detail'
    ]

    def cli(self, switch='', ip_type='', active='', vrf_name='', group='', source='', output=None):
        if output is None:
            if vrf_name:
                if switch:
                    cmd = self.cli_command[0].format(switch=switch, ip_type=ip_type, active=active, vrf_name=vrf_name, group=group, source=source)
                else:
                    cmd = self.cli_command[2].format(active=active, ip_type=ip_type, vrf_name=vrf_name, group=group, source=source)
            else:
                if switch:
                    cmd = self.cli_command[1].format(switch=switch, ip_type=ip_type, active=active, group=group, source=source)
                else:
                    cmd = self.cli_command[3].format(active=active, ip_type=ip_type, group=group, source=source)
            output = self.device.execute(cmd)

        ret_dict = {}

        # Mvrf: 3  ( 40::2, ff1e::1 ) Attrs:
        p0 = re.compile(r'^Mvrf: +(?P<mvrf>\d+) +\( +(?P<source>[\w\:\.\/\*]+), +(?P<group>[\w\:\.\/]+) +\) +Attrs:( C)?$')

        # Hw Flag                 : InHw
        # Hw Flag                 : InHw  EntryActive
        p1 = re.compile(r'^Hw Flag +: +(?P<hw_flag>[\w\s]+)$')        

        # Mlist Flags             : None
        p2 = re.compile(r'^Mlist Flags +: +(?P<mlist_flags>\w+)$')

        # Mlist_hndl (Id)         : 0x11889275ea0 ( 0xc823 )
        p3 = re.compile(r'^Mlist_hndl \(Id\) +: +(?P<mlist_hndl_id>[\w\(\)\s]+)$')

        # Mlist Urid              : 0x10000000003238e8
        p4 = re.compile(r'^Mlist Urid +: +(?P<mlist_urid>[\w]+)$')

        # Fset Urid (Hash)        : 0x300000000031f715 ( 68af2994 )
        p5 = re.compile(r'^Fset Urid \(Hash\) +: +(?P<fset_urid_hash>[\w\(\)\s]+)$')

        # Fset Aux Urid           : 0x0
        p5_1 = re.compile(r'^Fset Aux Urid +: +(?P<fset_aux_urid>[\w]+)$')

        # RPF Adjacency ID        : 0xf80059d2
        p6 = re.compile(r'^RPF Adjacency ID +: +(?P<rpf_adjacency_id>[\w]+)$')

        # CPU Credit              : 0
        p7 = re.compile(r'^CPU Credit +: +(?P<cpu_credit>\d+)$')

        # Total Packets           : 4643 ( 9 pps approx.)
        p8 = re.compile(r'^Total Packets +: +(?P<total_packets>\d+) +\( +(?P<pps_approx>\d+) pps approx\.\)$')

        # OIF Count               : 3
        p9 = re.compile(r'^OIF Count +: +(?P<oif_count>\d+)$')

        # OIF Details:
        p10 = re.compile(r'^OIF Details:$')

        # AdjID          Interface          ParentIf        HwFlag      Flags      IntfType       MsgType
        p10_1 = re.compile(r'^AdjID\s+Interface\s+ParentIf\s+HwFlag\s+Flags\s+IntfType\s+MsgType$')

        # 0xf8005442     Vl109              --------         ---        F A        SVI_IF         NORMAL
        p11 = re.compile(r'^(?P<adjid>[\w]+) +(?P<interface>[\w\/]+) +(?P<parentif>[\w\-]+) +(?P<hwflag>[\w\-]+) +(?P<flags>[A|F|NS|\s]+)\s+(?P<intf_type>[\w]+)\s+(?P<msg_type>[\w\s]+)$')

        # GID                   : 8631
        p12 = re.compile(r'^GID +: +(?P<gid>\d+)$')

        # MCID OID Asic[0]      : 1346
        p13 = re.compile(r'^MCID OID Asic\[(?P<asic>[\d]+)] +: +(?P<mcid_oid_asic>\d+)$')

        # Hardware Info ASIC[0] :
        p14 = re.compile(r'^Hardware Info ASIC\[(?P<asic_number>[\d]+)] +:$')

        # IP MCID OID         :3272 (cookie:urid:0x30::1b6)
        p15 = re.compile(r'^IP MCID OID +:(?P<ip_mcid_oid>\d+) +\(cookie:urid:(?P<cookie>[\w\:\.\/]+)\)$')

        # RPF PORT OID        :1493
        p16 = re.compile(r'^RPF PORT OID +:(?P<rpf_port_oid>\d+)$')

        # punt_on_rpf_fail    :1
        p17 = re.compile(r'^punt_on_rpf_fail +:(?P<punt_on_rpf_fail>\d+)$')

        # punt_and_forward    :1
        p18 = re.compile(r'^punt_and_forward +:(?P<punt_and_forward>\d+)$')

        # use_rpfid           :0
        p19 = re.compile(r'^use_rpfid +:(?P<use_rpfid>\d+)$')

        # rpfid               :0
        p20 = re.compile(r'^rpfid +:(?P<rpfid>\d+)$')

        # enable_rpf_check    :1
        p21 = re.compile(r'^enable_rpf_check +:(?P<enable_rpf_check>\d+)$')

        # Ec_seed                 : 6
        p22 = re.compile(r'^Ec_seed +: +(?P<ec_seed>\d+)$')

        # npi_mroute_ent          : 0x118812c5e20
        p23 = re.compile(r'^npi_mroute_ent +: +(?P<npi_mroute_ent>[\w]+)$')

        # svi_fwd_ifs             : 2
        p24 = re.compile(r'^svi_fwd_ifs +: +(?P<svi_fwd_ifs>\d+)$')

        # ios_f_ifs/mlist_f_ifs   : 1/1
        p25 = re.compile(r'^ios_f_ifs/mlist_f_ifs +: +(?P<ios_f_ifs>\d+)/(?P<mlist_f_ifs>\d+)$')

        index = 1
        for line in output.splitlines():
            line = line.strip()

            # Mvrf: 3  ( 40::2, ff1e::1 ) Attrs:
            m = p0.match(line)
            if m:
                group = m.groupdict()
                mfib_dict = ret_dict.setdefault("mfib", {}).setdefault(index, {})
                mfib_dict['mvrf'] = int(group['mvrf'])
                mfib_dict['group'] = group['group']
                mfib_dict['source'] = group['source']
                attrs_dict = mfib_dict.setdefault('attrs', {})
                index += 1
                continue

            # Hw Flag                 : InHw
            m = p1.match(line)
            if m:
                attrs_dict['hw_flag'] = m.groupdict()['hw_flag']
                continue

            # Mlist Flags             : None
            m = p2.match(line)
            if m:
                attrs_dict['mlist_flags'] = m.groupdict()['mlist_flags']
                continue

            # Mlist_hndl (Id)         : 0x11889275ea0 ( 0xc823 )
            m = p3.match(line)
            if m:
                attrs_dict['mlist_hndl_id'] = m.groupdict()['mlist_hndl_id']
                continue

            # Mlist Urid              : 0x10000000003238e8
            m = p4.match(line)
            if m:
                attrs_dict['mlist_urid'] = m.groupdict()['mlist_urid']
                continue

            # Fset Urid (Hash)        : 0x300000000031f715 ( 68af2994 )
            m = p5.match(line)
            if m:
                attrs_dict['fset_urid_hash'] = m.groupdict()['fset_urid_hash']
                continue

            # Fset Aux Urid           : 0x0
            m = p5_1.match(line)
            if m:
                attrs_dict['fset_aux_urid'] = m.groupdict()['fset_aux_urid']
                continue

            # RPF Adjacency ID        : 0xf80059d2
            m = p6.match(line)
            if m:
                attrs_dict['rpf_adjacency_id'] = m.groupdict()['rpf_adjacency_id']
                continue

            # CPU Credit              : 0
            m = p7.match(line)
            if m:
                attrs_dict['cpu_credit'] = int(m.groupdict()['cpu_credit'])
                continue

            # Total Packets           : 4643 ( 9 pps approx.)
            m = p8.match(line)
            if m:
                attrs_dict['total_packets'] = int(m.groupdict()['total_packets'])
                attrs_dict['pps_approx'] = int(m.groupdict()['pps_approx'])
                continue

            # OIF Count               : 3
            m = p9.match(line)
            if m:
                attrs_dict['oif_count'] = int(m.groupdict()['oif_count'])
                continue

            # OIF Details:
            m = p10.match(line)
            if m:
                oif_list = attrs_dict.setdefault('oif_details', [])
                continue

            # AdjID          Interface          ParentIf        HwFlag      Flags      IntfType       MsgType
            m=p10_1.match(line)
            if m:
                continue

            # 0xc851         Tu315              --------         ---        F NS
            m = p11.match(line)
            if m:
                oif_list.append({
                    'adjid': m.groupdict()['adjid'],
                    'interface': m.groupdict()['interface'],
                    'intf_type': m.groupdict()['intf_type'],
                    'msg_type': m.groupdict()['msg_type'],
                    'flags': m.groupdict()['flags'].strip().split(),
                })
                if '--' not in m.groupdict()['parentif']:
                    oif_list[-1].update({'parentif': m.groupdict()['parentif']})
                if '--' not in m.groupdict()['hwflag']:
                    oif_list[-1].update({'hwflag': m.groupdict()['hwflag']})
                continue

            # GID                   : 8631
            m = p12.match(line)
            if m:
                attrs_dict['gid'] = int(m.groupdict()['gid'])
                continue

            # MCID OID Asic[0]      : 1346
            m = p13.match(line)
            if m:
                group = m.groupdict()
                asic_dict = attrs_dict.setdefault('asic', {}).setdefault(int(group['asic']), {})            
                asic_dict['mcid_oid_asic'] = int(group['mcid_oid_asic'])
                continue

            # Hardware Info ASIC[0] :
            m = p14.match(line)
            if m:
                group = m.groupdict()
                hw_dict = attrs_dict.setdefault('hw_asic_info', {}).setdefault(int(group['asic_number']), {})            
                continue

            # IP MCID OID         :3272 (cookie:urid:0x30::1b6)
            m = p15.match(line)
            if m:
                group = m.groupdict()
                hw_dict['ip_mcid_oid'] = int(group['ip_mcid_oid'])
                hw_dict['cookie'] = group['cookie']
                continue

            # RPF PORT OID        :1493
            m = p16.match(line)
            if m:
                hw_dict['rpf_port_oid'] = int(m.groupdict()['rpf_port_oid'])
                continue

            # punt_on_rpf_fail    :1
            m = p17.match(line)
            if m:
                hw_dict['punt_on_rpf_fail'] = int(m.groupdict()['punt_on_rpf_fail'])
                continue

            # punt_and_forward    :1
            m = p18.match(line)
            if m:
                hw_dict['punt_and_forward'] = int(m.groupdict()['punt_and_forward'])
                continue

            # use_rpfid           :0
            m = p19.match(line)
            if m:
                hw_dict['use_rpfid'] = int(m.groupdict()['use_rpfid'])
                continue

            # rpfid               :0
            m = p20.match(line)
            if m:
                hw_dict['rpfid'] = int(m.groupdict()['rpfid'])
                continue

            # enable_rpf_check    :1
            m = p21.match(line)
            if m:
                hw_dict['enable_rpf_check'] = int(m.groupdict()['enable_rpf_check'])
                continue

            # Ec_seed                 : 6
            m = p22.match(line)
            if m:
                attrs_dict['ec_seed'] = int(m.groupdict()['ec_seed'])
                continue

            # npi_mroute_ent          : 0x118812c5e20
            m = p23.match(line)
            if m:
                attrs_dict['npi_mroute_ent'] = m.groupdict()['npi_mroute_ent']
                continue

            # svi_fwd_ifs             : 2
            m = p24.match(line)
            if m:
                attrs_dict['svi_fwd_ifs'] = int(m.groupdict()['svi_fwd_ifs'])
                continue

            # ios_f_ifs/mlist_f_ifs   : 1/1
            m = p25.match(line)
            if m:
                attrs_dict['ios_f_ifs'] = int(m.groupdict()['ios_f_ifs'])
                attrs_dict['mlist_f_ifs'] = int(m.groupdict()['mlist_f_ifs'])
                continue

        return ret_dict

class ShowPlatformSoftwareIgmpSnoopingGroupsVlanCountSchema(MetaParser):
    """Schema for 'show platform software fed {state} ip igmp snooping groups vlan {vlan} count'"""
    schema = {
        'total_group_count': int,
        'total_stub_group_count': int
    }

class ShowPlatformSoftwareIgmpSnoopingGroupsVlanCount(ShowPlatformSoftwareIgmpSnoopingGroupsVlanCountSchema):
    """Parser for 'show platform software fed {state} ip igmp snooping groups vlan {vlan} count'"""

    cli_command = 'show platform software fed {state} ip igmp snooping groups vlan {vlan} count'

    def cli(self, state, vlan, output=None):
        if output is None:
            cmd = self.cli_command.format(state=state, vlan=vlan)
            output = self.device.execute(cmd)

        ret_dict = {}

        # Total Group Count       : 16000
        p1 = re.compile(r'^Total Group Count\s+:\s+(?P<total_group_count>\d+)$')

        # Total Stub Group Count  : 0
        p2 = re.compile(r'^Total Stub Group Count\s+:\s+(?P<total_stub_group_count>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Total Group Count       : 16000
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['total_group_count'] = int(group['total_group_count'])
                continue

            # Total Stub Group Count  : 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['total_stub_group_count'] = int(group['total_stub_group_count'])
                continue

        return ret_dict 
