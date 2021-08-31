"""show_ospf.py

IOSXR parsers for the following show commands:
    * show ospf vrf all-inclusive interface
    * show ospf vrf all-inclusive neighbor detail
    * show ospf vrf all-inclusive
    * show ospf vrf all-inclusive sham-links
    * show ospf vrf all-inclusive virtual-links
    * show ospf mpls traffic-eng link
    * show ospf vrf all-inclusive database router
    * show ospf vrf all-inclusive database network
    * show ospf vrf all-inclusive database summary
    * show ospf vrf all-inclusive database external
    * show ospf vrf all-inclusive database opaque-area
    * show ospf database
    * show ospf mpls1 database
    * show ospf {process_id} database router
    * show ospf all-inclusive database router
    * show ospf interface brief
"""

# Python
import re
from netaddr import IPAddress, IPNetwork

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional


# ==================================================
# Schema for 'show ospf vrf all-inclusive interface'
# ==================================================
class ShowOspfVrfAllInclusiveInterfaceSchema(MetaParser):
    """Schema for show ospf vrf all-inclusive interface"""

    schema = {
        "vrf": {
            Any(): {
                "address_family": {
                    Any(): {
                        "instance": {
                            Any(): {
                                "areas": {
                                    Any(): {
                                        Optional("interfaces"): {
                                            Any(): {
                                                "name": str,
                                                "enable": bool,
                                                "line_protocol": bool,
                                                "ip_address": str,
                                                "demand_circuit": bool,
                                                "process_id": str,
                                                "router_id": str,
                                                "interface_type": str,
                                                "bfd": {
                                                    "enable": bool,
                                                    Optional("interval"): int,
                                                    Optional("min_interval"): int,
                                                    Optional("multiplier"): int,
                                                    Optional("mode"): str,
                                                },
                                                Optional("cost"): int,
                                                Optional("transmit_delay"): int,
                                                Optional("state"): str,
                                                Optional("priority"): int,
                                                Optional("mtu"): int,
                                                Optional("max_pkt_sz"): int,
                                                Optional("dr_router_id"): str,
                                                Optional("dr_ip_addr"): str,
                                                Optional("bdr_router_id"): str,
                                                Optional("bdr_ip_addr"): str,
                                                Optional("hello_interval"): int,
                                                Optional("dead_interval"): int,
                                                Optional("wait_interval"): int,
                                                Optional("retransmit_interval"): int,
                                                Optional("passive"): bool,
                                                Optional("hello_timer"): str,
                                                Optional("index"): str,
                                                Optional("flood_queue_length"): int,
                                                Optional("next"): str,
                                                Optional("last_flood_scan_length"): int,
                                                Optional("max_flood_scan_length"): int,
                                                Optional(
                                                    "last_flood_scan_time_msec"
                                                ): int,
                                                Optional(
                                                    "max_flood_scan_time_msec"
                                                ): int,
                                                Optional("ls_ack_list"): str,
                                                Optional("ls_ack_list_length"): int,
                                                Optional("high_water_mark"): int,
                                                Optional("total_dcbitless_lsa"): int,
                                                Optional("donotage_lsa"): bool,
                                                Optional("statistics"): {
                                                    Optional("adj_nbr_count"): int,
                                                    Optional("nbr_count"): int,
                                                    Optional(
                                                        "num_nbrs_suppress_hello"
                                                    ): int,
                                                    Optional(
                                                        "multi_area_intf_count"
                                                    ): int,
                                                },
                                                Optional("neighbors"): {
                                                    Any(): {
                                                        Optional("dr_router_id"): str,
                                                        Optional("bdr_router_id"): str,
                                                    },
                                                },
                                            },
                                        },
                                        Optional("virtual_links"): {
                                            Any(): {
                                                "name": str,
                                                "enable": bool,
                                                "line_protocol": bool,
                                                "ip_address": str,
                                                "demand_circuit": bool,
                                                "process_id": str,
                                                "router_id": str,
                                                "interface_type": str,
                                                "bfd": {
                                                    "enable": bool,
                                                    Optional("interval"): int,
                                                    Optional("min_interval"): int,
                                                    Optional("multiplier"): int,
                                                    Optional("mode"): str,
                                                },
                                                Optional("cost"): int,
                                                Optional("transmit_delay"): int,
                                                Optional("state"): str,
                                                Optional("priority"): int,
                                                Optional("mtu"): int,
                                                Optional("max_pkt_sz"): int,
                                                Optional("dr_router_id"): str,
                                                Optional("dr_ip_addr"): str,
                                                Optional("bdr_router_id"): str,
                                                Optional("bdr_ip_addr"): str,
                                                Optional("hello_interval"): int,
                                                Optional("dead_interval"): int,
                                                Optional("wait_interval"): int,
                                                Optional("retransmit_interval"): int,
                                                Optional("passive"): bool,
                                                Optional("hello_timer"): str,
                                                Optional("index"): str,
                                                Optional("flood_queue_length"): int,
                                                Optional("next"): str,
                                                Optional("last_flood_scan_length"): int,
                                                Optional("max_flood_scan_length"): int,
                                                Optional(
                                                    "last_flood_scan_time_msec"
                                                ): int,
                                                Optional(
                                                    "max_flood_scan_time_msec"
                                                ): int,
                                                Optional("ls_ack_list"): str,
                                                Optional("ls_ack_list_length"): int,
                                                Optional("high_water_mark"): int,
                                                Optional("total_dcbitless_lsa"): int,
                                                Optional("donotage_lsa"): bool,
                                                Optional("statistics"): {
                                                    Optional("adj_nbr_count"): int,
                                                    Optional("nbr_count"): int,
                                                    Optional(
                                                        "num_nbrs_suppress_hello"
                                                    ): int,
                                                    Optional(
                                                        "multi_area_intf_count"
                                                    ): int,
                                                },
                                                Optional("neighbors"): {
                                                    Any(): {
                                                        Optional("dr_router_id"): str,
                                                        Optional("bdr_router_id"): str,
                                                    },
                                                },
                                            },
                                        },
                                        Optional("sham_links"): {
                                            Any(): {
                                                "name": str,
                                                "enable": bool,
                                                "line_protocol": bool,
                                                "ip_address": str,
                                                "demand_circuit": bool,
                                                "process_id": str,
                                                "router_id": str,
                                                "interface_type": str,
                                                "bfd": {
                                                    "enable": bool,
                                                    Optional("interval"): int,
                                                    Optional("min_interval"): int,
                                                    Optional("multiplier"): int,
                                                    Optional("mode"): str,
                                                },
                                                Optional("cost"): int,
                                                Optional("transmit_delay"): int,
                                                Optional("state"): str,
                                                Optional("priority"): int,
                                                Optional("mtu"): int,
                                                Optional("max_pkt_sz"): int,
                                                Optional("dr_router_id"): str,
                                                Optional("dr_ip_addr"): str,
                                                Optional("bdr_router_id"): str,
                                                Optional("bdr_ip_addr"): str,
                                                Optional("hello_interval"): int,
                                                Optional("dead_interval"): int,
                                                Optional("wait_interval"): int,
                                                Optional("retransmit_interval"): int,
                                                Optional("passive"): bool,
                                                Optional("hello_timer"): str,
                                                Optional("index"): str,
                                                Optional("flood_queue_length"): int,
                                                Optional("next"): str,
                                                Optional("last_flood_scan_length"): int,
                                                Optional("max_flood_scan_length"): int,
                                                Optional(
                                                    "last_flood_scan_time_msec"
                                                ): int,
                                                Optional(
                                                    "max_flood_scan_time_msec"
                                                ): int,
                                                Optional("ls_ack_list"): str,
                                                Optional("ls_ack_list_length"): int,
                                                Optional("high_water_mark"): int,
                                                Optional("total_dcbitless_lsa"): int,
                                                Optional("donotage_lsa"): bool,
                                                Optional("statistics"): {
                                                    Optional("adj_nbr_count"): int,
                                                    Optional("nbr_count"): int,
                                                    Optional(
                                                        "num_nbrs_suppress_hello"
                                                    ): int,
                                                    Optional(
                                                        "multi_area_intf_count"
                                                    ): int,
                                                },
                                                Optional("neighbors"): {
                                                    Any(): {
                                                        Optional("dr_router_id"): str,
                                                        Optional("bdr_router_id"): str,
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }


# ==================================================
# Parser for 'show ospf vrf all-inclusive interface'
# ==================================================
class ShowOspfVrfAllInclusiveInterface(ShowOspfVrfAllInclusiveInterfaceSchema):
    """Parser for show ospf vrf all-inclusive interface"""

    cli_command = [
        "show ospf vrf all-inclusive interface",
        "show ospf vrf all-inclusive interface {interface}",
        "show ospf vrf {vrf} interface {interface}",
        "show ospf vrf {vrf} interface",
    ]
    exclude = [
        "dead_timer",
        "hello_timer",
        "last_flood_scan_length",
        "max_flood_scan_length",
        "high_water_mark",
    ]

    def cli(self, vrf="", interface="", output=None):
        if output is None:
            if interface:
                if vrf:
                    out = self.device.execute(
                        self.cli_command[2].format(interface=interface, vrf=vrf)
                    )
                else:
                    out = self.device.execute(
                        self.cli_command[1].format(interface=interface)
                    )
            else:
                if vrf:
                    out = self.device.execute(self.cli_command[3].format(vrf=vrf))
                else:
                    out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # Init vars
        ret_dict = {}
        af = "ipv4"  # this is ospf - always ipv4
        instance = ""
        # Mapping dict
        bool_dict = {"up": True, "down": False, "unknown": False}

        p1 = re.compile(
            r"^Interfaces +for +OSPF +(?P<instance>(\S+))"
            "(?:, +VRF +(?P<vrf>(\S+)))?$"
        )
        p2 = re.compile(
            r"^(?P<interface>(\S+)) +is( +administratively)?"
            " +(?P<enable>(unknown|up|down)), +line +protocol"
            " +is +(?P<line_protocol>(up|down))$"
        )
        p3 = re.compile(
            r"^Internet +Address +(?P<address>(\S+)),"
            " +Area +(?P<area>(\S+))"
            "(, +(?P<dummy>.+))?$"
        )
        p4 = re.compile(
            r"^Process +ID +(?P<pid>(\S+))"
            "(?:, +VRF +(?P<vrf>(\S+)))?"
            ", +Router +ID +(?P<router_id>(\S+))"
            ", +Network +Type +(?P<interface_type>(\S+))"
            "(?:, +Cost: +(?P<cost>(\d+))( \([A-Z\-]+\))?)?$"
        )
        p5 = re.compile(
            r"^Transmit +Delay is +(?P<delay>(\d+)) +sec,"
            " +State +(?P<state>(\S+)),"
            "(?: +Priority +(?P<priority>(\d+)),)?"
            " +MTU +(?P<mtu>(\d+)),"
            " +MaxPktSz +(?P<max_pkt_sz>(\d+))$"
        )
        p6 = re.compile(
            r"^Designated +(R|r)outer +\(ID\)"
            " +(?P<dr_router_id>(\S+)), +(I|i)nterface"
            " +(A|a)ddress +(?P<dr_ip_addr>(\S+))$"
        )
        p7 = re.compile(
            r"^Backup +(D|d)esignated +(R|r)outer +\(ID\)"
            " +(?P<bdr_router_id>(\S+)), +(I|i)nterface"
            " +(A|a)ddress +(?P<bdr_ip_addr>(\S+))$"
        )
        p8 = re.compile(
            r"^Timer +intervals +configured,"
            " +Hello +(?P<hello>(\d+)),"
            " +Dead +(?P<dead>(\d+)),"
            " +Wait +(?P<wait>(\d+)),"
            " +Retransmit +(?P<retransmit>(\d+))$"
        )
        p9_1 = re.compile(r"^Hello +due +in +(?P<hello_timer>(\S+))$")
        p9_2 = re.compile(r"^No +Hellos +\(Passive +interface\)$")
        p10 = re.compile(
            r"^Index +(?P<index>(\S+))," " +flood +queue +length +(?P<length>(\d+))$"
        )
        p22 = re.compile(r"^Next +(?P<next>(\S+))$")
        p11 = re.compile(
            r"^Last +flood +scan +length +is +(?P<num>(\d+)),"
            " +maximum +is +(?P<max>(\d+))$"
        )
        p12 = re.compile(
            r"^Last +flood +scan +time +is +(?P<time1>(\d+))"
            " +msec, +maximum +is +(?P<time2>(\d+)) +msec$"
        )
        p13 = re.compile(
            r"^LS +Ack +List: +(?P<ls_ack_list>(\S+)) +length"
            " +(?P<num>(\d+)), +high +water +mark"
            " +(?P<num2>(\d+))$"
        )
        p14 = re.compile(
            r"^Neighbor +Count +is +(?P<nbr_count>(\d+)),"
            " +Adjacent +neighbor +count +is"
            " +(?P<adj_nbr_count>(\d+))$"
        )
        p15_1 = re.compile(
            r"^Adjacent +with +neighbor +(?P<nbr>(\S+))"
            " +\((B|b)ackup +(D|d)esignated +(R|r)outer\)$"
        )
        p15_2 = re.compile(
            r"^Adjacent +with +neighbor +(?P<nbr>(\S+))"
            " +\((D|d)esignated +(R|r)outer\)$"
        )
        p15_3 = re.compile(
            r"^Adjacent +with +neighbor +(?P<nbr>(\S+))" " +\(Hello suppressed\)$"
        )
        p16 = re.compile(r"^Suppress +hello +for +(?P<sup>(\d+))" " +neighbor\(s\)$")
        p17 = re.compile(r"^Multi-area +interface +Count +is" " +(?P<count>(\d+))$")
        p18 = re.compile(r"^Configured as demand circuit\.$")
        p19 = re.compile(r"^Run as demand circuit\.$")
        p20 = re.compile(
            r"^DoNotAge +LSA +not +allowed +\(Number +of"
            " +DCbitless +LSA +is +(?P<num>(\d+))\)\.$"
        )
        p21 = re.compile(
            r"^BFD enabled"
            "(?:, +BFD +interval +(?P<interval>(\d+)) +msec)?"
            "(?:, +BFD +multiplier +(?P<multi>(\d+)))?"
            "(?:, +Mode: +(?P<mode>(\S+)))?$"
        )

        for line in out.splitlines():
            line = line.strip()

            # Interfaces for OSPF 1, VRF VRF1
            m = p1.match(line)
            if m:
                instance = str(m.groupdict()["instance"])
                if m.groupdict()["vrf"]:
                    vrf = str(m.groupdict()["vrf"])
                else:
                    vrf = "default"
                if "vrf" not in ret_dict:
                    ret_dict["vrf"] = {}
                if vrf not in ret_dict["vrf"]:
                    ret_dict["vrf"][vrf] = {}
                if "address_family" not in ret_dict["vrf"][vrf]:
                    ret_dict["vrf"][vrf]["address_family"] = {}
                if af not in ret_dict["vrf"][vrf]["address_family"]:
                    ret_dict["vrf"][vrf]["address_family"][af] = {}
                if "instance" not in ret_dict["vrf"][vrf]["address_family"][af]:
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"] = {}
                if (
                    instance
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ] = {}
                    continue

            # GigabitEthernet0/0/0/2 is up, line protocol is up
            # Loopback1 is administratively down, line protocol is down
            # OSPF_SL0 is unknown, line protocol is up
            # OSPF_VL0 is unknown, line protocol is up
            m = p2.match(line)
            if m:
                if "vrf" not in ret_dict:
                    ret_dict["vrf"] = {}
                if vrf not in ret_dict["vrf"]:
                    ret_dict["vrf"][vrf] = {}
                if "address_family" not in ret_dict["vrf"][vrf]:
                    ret_dict["vrf"][vrf]["address_family"] = {}
                if af not in ret_dict["vrf"][vrf]["address_family"]:
                    ret_dict["vrf"][vrf]["address_family"][af] = {}
                if "instance" not in ret_dict["vrf"][vrf]["address_family"][af]:
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"] = {}
                if (
                    instance
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ] = {}
                interface = str(m.groupdict()["interface"])
                enable = str(m.groupdict()["enable"])
                line_protocol = str(m.groupdict()["line_protocol"])

                # Determine if 'interface' or 'sham_link' or 'virtual_link'
                if re.search("SL", interface):
                    n = re.match("(?P<ignore>\S+)_SL(?P<num>(\d+))", interface)
                    if n:
                        intf_type = "sham_links"
                        name = "SL" + str(n.groupdict()["num"])
                elif re.search("VL", interface):
                    n = re.match("(?P<ignore>\S+)_VL(?P<num>(\d+))", interface)
                    if n:
                        intf_type = "virtual_links"
                        name = "VL" + str(n.groupdict()["num"])
                else:
                    intf_type = "interfaces"
                    name = interface
                    continue

            # Internet Address 10.2.3.3/24, Area 0
            # Internet Address 192.168.205.1/32, Area 1, SID 0, Strict-SPF SID 0
            m = p3.match(line)
            if m:
                ip_address = str(m.groupdict()["address"])
                area = str(m.groupdict()["area"])
                if area.isdigit():
                    area = str(IPAddress(area))
                continue

            # Process ID 1, Router ID 10.36.3.3, Network Type POINT_TO_POINT
            # Process ID 1, Router ID 10.36.3.3, Network Type BROADCAST, Cost: 1
            # Process ID 1, VRF VRF1, Router ID 10.36.3.3, Network Type SHAM_LINK, Cost: 111
            # Process ID 1, VRF VRF501, Router ID 192.168.111.1, Network Type BROADCAST, Cost: 1 (RSVP-TE)
            m = p4.match(line)
            if m:
                pid = str(m.groupdict()["pid"])
                router_id = str(m.groupdict()["router_id"])
                interface_type = str(m.groupdict()["interface_type"]).lower()
                interface_type = interface_type.replace("_", "-")
                if not instance:
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        pid
                    ] = ret_dict["vrf"][vrf]["address_family"][af]["instance"].pop(
                        instance
                    )
                    instance = pid
                # Get interface values
                if intf_type == "interfaces":
                    intf_name = interface
                elif intf_type == "virtual_links":
                    # Init
                    vl_transit_area_id = None

                    # Execute 'show ospf vrf all-inclusive virtual-links' to get the vl_transit_area_id
                    obj = ShowOspfVrfAllInclusiveVirtualLinks(device=self.device)
                    vl_out = obj.parse()

                    for vl_vrf in vl_out["vrf"]:
                        for vl_af in vl_out["vrf"][vl_vrf]["address_family"]:
                            for vl_inst in vl_out["vrf"][vl_vrf]["address_family"][
                                vl_af
                            ]["instance"]:
                                for vl_area in vl_out["vrf"][vl_vrf]["address_family"][
                                    vl_af
                                ]["instance"][vl_inst]["areas"]:
                                    for vl in vl_out["vrf"][vl_vrf]["address_family"][
                                        vl_af
                                    ]["instance"][vl_inst]["areas"][vl_area][
                                        "virtual_links"
                                    ]:
                                        vl_name = vl_out["vrf"][vl_vrf][
                                            "address_family"
                                        ][vl_af]["instance"][vl_inst]["areas"][vl_area][
                                            "virtual_links"
                                        ][
                                            vl
                                        ][
                                            "name"
                                        ]
                                        if vl_name == name:
                                            vl_transit_area_id = vl_out["vrf"][vl_vrf][
                                                "address_family"
                                            ][vl_af]["instance"][vl_inst]["areas"][
                                                vl_area
                                            ][
                                                "virtual_links"
                                            ][
                                                vl
                                            ][
                                                "transit_area_id"
                                            ]
                                            break

                    if vl_transit_area_id is not None:
                        intf_name = vl_transit_area_id + " " + router_id
                        area = vl_transit_area_id
                elif intf_type == "sham_links":
                    # Init
                    sl_local_id = None
                    sl_remote_id = None

                    # Execute command to get sham-link remote_id
                    cmd = "show ospf vrf all-inclusive sham-links | i {interface}".format(
                        interface=interface
                    )
                    out = self.device.execute(cmd)

                    for line in out.splitlines():
                        line = line.rstrip()
                        # Sham Link OSPF_SL0 to address 10.151.22.22 is up
                        p = re.search(
                            "Sham +Link +(?P<intf>(\S+)) +to +address"
                            " +(?P<remote>(\S+)) +is +up",
                            line,
                        )
                        if p:
                            if interface == str(p.groupdict()["intf"]):
                                sl_remote_id = str(p.groupdict()["remote"])
                                break

                    # Execute command to get sham-link local_id
                    if sl_remote_id is not None:
                        cmd = "show run formal router ospf | i sham | i {remote}".format(
                            remote=sl_remote_id
                        )
                        out = self.device.execute(cmd)

                        for line in out.splitlines():
                            line = line.rstrip()
                            # router ospf 1 vrf VRF1 area 1 sham-link 10.21.33.33 10.151.22.22
                            q = re.search(
                                "router +ospf +(?P<q_inst>(\d+))(?: +vrf"
                                " +(?P<q_vrf>(\S+)))? +area"
                                " +(?P<q_area>(\S+)) +sham-link"
                                " +(?P<local_id>(\S+))"
                                " +(?P<remote_id>(\S+))",
                                line,
                            )
                            if q:
                                if q.groupdict()["q_vrf"]:
                                    q_vrf = str(q.groupdict()["q_vrf"])
                                else:
                                    q_vrf = "default"
                                q_inst = str(q.groupdict()["q_inst"])
                                q_area = str(q.groupdict()["q_area"])
                                if q_area.isdigit():
                                    q_area = str(IPAddress(q_area))
                                remote_id = str(q.groupdict()["remote_id"])

                                # Check parameters match
                                if (
                                    q_inst == instance
                                    and q_vrf == vrf
                                    and q_area == area
                                    and remote_id == sl_remote_id
                                ):
                                    sl_local_id = str(q.groupdict()["local_id"])
                                    break

                    if sl_local_id is not None:
                        intf_name = sl_local_id + " " + sl_remote_id

                # Build dictionary
                if (
                    "areas"
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance][
                        "areas"
                    ] = {}
                if (
                    area
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ]["areas"]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance][
                        "areas"
                    ][area] = {}
                if (
                    intf_type
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ]["areas"][area]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance][
                        "areas"
                    ][area][intf_type] = {}
                if (
                    intf_name
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ]["areas"][area][intf_type]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance][
                        "areas"
                    ][area][intf_type][intf_name] = {}
                # Set sub_dict
                sub_dict = ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                    instance
                ]["areas"][area][intf_type][intf_name]
                # Set keys
                sub_dict["demand_circuit"] = False
                if "bfd" not in sub_dict:
                    sub_dict["bfd"] = {}
                sub_dict["bfd"]["enable"] = False
                try:
                    sub_dict["name"] = name
                    sub_dict["ip_address"] = ip_address
                    sub_dict["enable"] = bool_dict[enable]
                    sub_dict["line_protocol"] = bool_dict[line_protocol]
                except Exception:
                    pass

                sub_dict["process_id"] = pid
                sub_dict["router_id"] = router_id
                sub_dict["interface_type"] = interface_type
                if m.groupdict()["cost"]:
                    sub_dict["cost"] = int(m.groupdict()["cost"])
                continue

            # Transmit Delay is 1 sec, State DR, Priority 1, MTU 1500, MaxPktSz 1500
            m = p5.match(line)
            if m:
                sub_dict["transmit_delay"] = int(m.groupdict()["delay"])
                state = str(m.groupdict()["state"]).lower()
                state = state.replace("_", "-")
                sub_dict["state"] = state
                sub_dict["mtu"] = int(m.groupdict()["mtu"])
                sub_dict["max_pkt_sz"] = int(m.groupdict()["max_pkt_sz"])
                if m.groupdict()["priority"]:
                    sub_dict["priority"] = int(m.groupdict()["priority"])
                continue

            # Designated Router (ID) 10.36.3.3, Interface address 10.2.3.3
            m = p6.match(line)
            if m:
                sub_dict["dr_router_id"] = str(m.groupdict()["dr_router_id"])
                sub_dict["dr_ip_addr"] = str(m.groupdict()["dr_ip_addr"])
                continue

            # Backup Designated router (ID) 10.16.2.2, Interface address 10.2.3.2
            m = p7.match(line)
            if m:
                sub_dict["bdr_router_id"] = str(m.groupdict()["bdr_router_id"])
                sub_dict["bdr_ip_addr"] = str(m.groupdict()["bdr_ip_addr"])
                continue

            # Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
            m = p8.match(line)
            if m:
                sub_dict["hello_interval"] = int(m.groupdict()["hello"])
                sub_dict["dead_interval"] = int(m.groupdict()["dead"])
                sub_dict["wait_interval"] = int(m.groupdict()["wait"])
                sub_dict["retransmit_interval"] = int(m.groupdict()["retransmit"])
                continue

            # Hello due in 00:00:07:587
            m = p9_1.match(line)
            if m:
                sub_dict["passive"] = False
                sub_dict["hello_timer"] = str(m.groupdict()["hello_timer"])
                continue

            # No Hellos (Passive interface)
            m = p9_2.match(line)
            if m:
                sub_dict["passive"] = True
                continue

            # Index 2/2, flood queue length 0
            m = p10.match(line)
            if m:
                sub_dict["index"] = str(m.groupdict()["index"])
                sub_dict["flood_queue_length"] = int(m.groupdict()["length"])
                continue

            # Next 0(0)/0(0)
            m = p22.match(line)
            if m:
                sub_dict["next"] = str(m.groupdict()["next"])
                continue

            # Last flood scan length is 1, maximum is 3
            m = p11.match(line)
            if m:
                sub_dict["last_flood_scan_length"] = int(m.groupdict()["num"])
                sub_dict["max_flood_scan_length"] = int(m.groupdict()["max"])
                continue

            # Last flood scan time is 0 msec, maximum is 0 msec
            m = p12.match(line)
            if m:
                sub_dict["last_flood_scan_time_msec"] = int(m.groupdict()["time1"])
                sub_dict["max_flood_scan_time_msec"] = int(m.groupdict()["time2"])
                continue

            # LS Ack List: current length 0, high water mark 7
            m = p13.match(line)
            if m:
                sub_dict["ls_ack_list"] = str(m.groupdict()["ls_ack_list"])
                sub_dict["ls_ack_list_length"] = int(m.groupdict()["num"])
                sub_dict["high_water_mark"] = int(m.groupdict()["num2"])
                continue

            # Neighbor Count is 1, Adjacent neighbor count is 1
            m = p14.match(line)
            if m:
                if "statistics" not in sub_dict:
                    sub_dict["statistics"] = {}
                sub_dict["statistics"]["nbr_count"] = int(m.groupdict()["nbr_count"])
                sub_dict["statistics"]["adj_nbr_count"] = int(
                    m.groupdict()["adj_nbr_count"]
                )
                continue

            # Adjacent with neighbor 10.16.2.2  (Backup Designated Router)
            m = p15_1.match(line)
            if m:
                neighbor = str(m.groupdict()["nbr"])
                if "neighbors" not in sub_dict:
                    sub_dict["neighbors"] = {}
                if neighbor not in sub_dict["neighbors"]:
                    sub_dict["neighbors"][neighbor] = {}
                sub_dict["neighbors"][neighbor]["bdr_router_id"] = neighbor
                continue

            # Adjacent with neighbor 10.36.3.3  (Designated Router)
            m = p15_2.match(line)
            if m:
                neighbor = str(m.groupdict()["nbr"])
                if "neighbors" not in sub_dict:
                    sub_dict["neighbors"] = {}
                if neighbor not in sub_dict["neighbors"]:
                    sub_dict["neighbors"][neighbor] = {}
                sub_dict["neighbors"][neighbor]["dr_router_id"] = neighbor
                continue

            # Adjacent with neighbor 10.64.4.4  (Hello suppressed)
            m = p15_3.match(line)
            if m:
                neighbor = str(m.groupdict()["nbr"])
                if "neighbors" not in sub_dict:
                    sub_dict["neighbors"] = {}
                if neighbor not in sub_dict["neighbors"]:
                    sub_dict["neighbors"][neighbor] = {}
                continue

            # Suppress hello for 0 neighbor(s)
            m = p16.match(line)
            if m:
                if "statistics" not in sub_dict:
                    sub_dict["statistics"] = {}
                sub_dict["statistics"]["num_nbrs_suppress_hello"] = int(
                    m.groupdict()["sup"]
                )
                continue

            # Multi-area interface Count is 0
            m = p17.match(line)
            if m:
                if "statistics" not in sub_dict:
                    sub_dict["statistics"] = {}
                sub_dict["statistics"]["multi_area_intf_count"] = int(
                    m.groupdict()["count"]
                )
                continue

            # Configured as demand circuit.
            m = p18.match(line)
            if m:
                sub_dict["demand_circuit"] = True
                continue

            # Run as demand circuit.
            m = p19.match(line)
            if m:
                sub_dict["demand_circuit"] = True
                continue

            # DoNotAge LSA not allowed (Number of DCbitless LSA is 1).
            m = p20.match(line)
            if m:
                sub_dict["donotage_lsa"] = False
                sub_dict["total_dcbitless_lsa"] = int(m.groupdict()["num"])
                continue

            # BFD enabled, BFD interval 12345 msec, BFD multiplier 50, Mode: Default
            m = p21.match(line)
            if m:
                sub_dict["bfd"]["enable"] = True
                if m.groupdict()["interval"]:
                    sub_dict["bfd"]["interval"] = int(m.groupdict()["interval"])
                if m.groupdict()["multi"]:
                    sub_dict["bfd"]["multiplier"] = int(m.groupdict()["multi"])
                if m.groupdict()["mode"]:
                    sub_dict["bfd"]["mode"] = str(m.groupdict()["mode"]).lower()
                    continue

        return ret_dict


# ========================================================
# Schema for 'show ospf vrf all-inclusive neighbor detail'
# ========================================================
class ShowOspfVrfAllInclusiveNeighborDetailSchema(MetaParser):
    """Schema for show ospf vrf all-inclusive neighbor detail"""

    schema = {
        "vrf": {
            Any(): {
                "address_family": {
                    Any(): {
                        "instance": {
                            Any(): {
                                Optional("total_neighbor_count"): int,
                                "areas": {
                                    Any(): {
                                        Optional("interfaces"): {
                                            Any(): {
                                                "neighbors": {
                                                    Any(): {
                                                        "neighbor_router_id": str,
                                                        Optional("bfd_enable"): bool,
                                                        Optional("bfd_mode"): str,
                                                        "address": str,
                                                        "priority": int,
                                                        "state": str,
                                                        "dr_ip_addr": str,
                                                        "bdr_ip_addr": str,
                                                        Optional("options"): str,
                                                        Optional("lls_options"): str,
                                                        Optional("dead_timer"): str,
                                                        Optional(
                                                            "neighbor_uptime"
                                                        ): str,
                                                        Optional("index"): str,
                                                        Optional("first"): str,
                                                        Optional("next"): str,
                                                        Optional("ls_ack_list"): str,
                                                        Optional(
                                                            "ls_ack_list_pending"
                                                        ): int,
                                                        Optional(
                                                            "high_water_mark"
                                                        ): int,
                                                        Optional("statistics"): {
                                                            Optional(
                                                                "total_dbd_retrans"
                                                            ): int,
                                                            Optional(
                                                                "nbr_event_count"
                                                            ): int,
                                                            Optional(
                                                                "nbr_retrans_qlen"
                                                            ): int,
                                                            Optional(
                                                                "total_retransmission"
                                                            ): int,
                                                            Optional(
                                                                "last_retrans_scan_length"
                                                            ): int,
                                                            Optional(
                                                                "last_retrans_max_scan_length"
                                                            ): int,
                                                            Optional(
                                                                "last_retrans_scan_time_msec"
                                                            ): int,
                                                            Optional(
                                                                "last_retrans_max_scan_time_msec"
                                                            ): int,
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        Optional("virtual_links"): {
                                            Any(): {
                                                "neighbors": {
                                                    Any(): {
                                                        "neighbor_router_id": str,
                                                        "address": str,
                                                        "priority": int,
                                                        "state": str,
                                                        "dr_ip_addr": str,
                                                        "bdr_ip_addr": str,
                                                        Optional("options"): str,
                                                        Optional("lls_options"): str,
                                                        Optional("dead_timer"): str,
                                                        Optional(
                                                            "neighbor_uptime"
                                                        ): str,
                                                        Optional("index"): str,
                                                        Optional("first"): str,
                                                        Optional("next"): str,
                                                        Optional("ls_ack_list"): str,
                                                        Optional(
                                                            "ls_ack_list_pending"
                                                        ): int,
                                                        Optional(
                                                            "high_water_mark"
                                                        ): int,
                                                        Optional("statistics"): {
                                                            Optional(
                                                                "total_dbd_retrans"
                                                            ): int,
                                                            Optional(
                                                                "nbr_event_count"
                                                            ): int,
                                                            Optional(
                                                                "nbr_retrans_qlen"
                                                            ): int,
                                                            Optional(
                                                                "total_retransmission"
                                                            ): int,
                                                            Optional(
                                                                "last_retrans_scan_length"
                                                            ): int,
                                                            Optional(
                                                                "last_retrans_max_scan_length"
                                                            ): int,
                                                            Optional(
                                                                "last_retrans_scan_time_msec"
                                                            ): int,
                                                            Optional(
                                                                "last_retrans_max_scan_time_msec"
                                                            ): int,
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }


# ========================================================
# Parser for 'show ospf vrf all-inclusive neighbor detail'
# ========================================================
class ShowOspfVrfAllInclusiveNeighborDetail(
    ShowOspfVrfAllInclusiveNeighborDetailSchema
):
    """Parser for show ospf vrf all-inclusive neighbor detail"""

    cli_command = [
        "show ospf vrf all-inclusive neighbor detail",
        "show ospf vrf all-inclusive neighbor detail {interface}",
        "show ospf vrf all-inclusive neighbor {neighbor} detail",
        "show ospf vrf all-inclusive neighbor {neighbor} detail {interface}",
        "show ospf vrf {vrf} neighbor detail",
        "show ospf vrf {vrf} neighbor detail {interface}",
        "show ospf vrf {vrf} neighbor {neighbor} detail",
        "show ospf vrf {vrf} neighbor {neighbor} detail {interface}",
    ]

    exclude = ["dead_timer", "neighbor_uptime", "hello_timer", "total_dbd_retrans"]

    def cli(self, vrf="", neighbor="", interface="", output=None):
        if output is None:
            if vrf:
                if neighbor:
                    if interface:
                        cmd = self.cli_command[7].format(
                            vrf=vrf, interface=interface, neighbor=neighbor
                        )
                    else:
                        cmd = self.cli_command[6].format(vrf=vrf, neighbor=neighbor)
                else:
                    if interface:
                        cmd = self.cli_command[5].format(vrf=vrf, interface=interface)
                    else:
                        cmd = self.cli_command[4].format(vrf=vrf)
            else:
                if neighbor:
                    if interface:
                        cmd = self.cli_command[3].format(
                            interface=interface, neighbor=neighbor
                        )
                    else:
                        cmd = self.cli_command[2].format(neighbor=neighbor)
                else:
                    if interface:
                        cmd = self.cli_command[1].format(interface=interface)
                    else:
                        cmd = self.cli_command[0]

            out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        ret_dict = {}
        af = "ipv4"  # this is ospf - always ipv4

        p1 = re.compile(
            r"^Neighbors +for +OSPF +(?P<instance>(\S+))" "(?:, +VRF +(?P<vrf>(\S+)))?$"
        )
        p2 = re.compile(
            r"^Neighbor +(?P<neighbor>(\S+)), +interface"
            " +address +(?P<address>(\S+))$"
        )
        p3 = re.compile(
            r"^In +the +area +(?P<area>\S+) +via +interface"
            " +(?P<interface>\S+)( +, +BFD +(?P<bfd_status>\w+), +Mode: (?P<mode>\w+))?$"
        )
        p4 = re.compile(
            r"^Neighbor +priority +is +(?P<priority>(\d+)),"
            " +State +is +(?P<state>(\S+)),"
            " +(?P<num>(\d+)) +state +changes$"
        )
        p5 = re.compile(
            r"^DR +is +(?P<dr_ip_addr>(\S+))" " +BDR +is +(?P<bdr_ip_addr>(\S+))$"
        )
        p6_1 = re.compile(r"^Options +is +(?P<options>(\S+))$")
        p6_2 = re.compile(r"^LLS +Options +is +(?P<lls_options>(.*))$")
        p7 = re.compile(r"^Dead +timer +due +in +(?P<dead_timer>(\S+))$")
        p8 = re.compile(r"^Neighbor +is +up +for +(?P<uptime>(\S+))$")
        p9 = re.compile(
            r"^Number +of +DBD +retrans +during +last"
            " +exchange +(?P<dbd_retrans>(\d+))$"
        )
        p10 = re.compile(
            r"^Index +(?P<index>(\S+)) +retransmission +queue"
            " +length +(?P<ql>(\d+)), +number +of"
            " +retransmission +(?P<num_retrans>(\d+))$"
        )
        p11 = re.compile(r"^First +(?P<first>(\S+)) +Next +(?P<next>(\S+))$")
        p12 = re.compile(
            r"^Last +retransmission +scan +length +is"
            " +(?P<num1>(\d+)), +maximum +is"
            " +(?P<num2>(\d+))$"
        )
        p13 = re.compile(
            r"^Last +retransmission +scan +time +is"
            " +(?P<num1>(\d+)) +msec, +maximum +is"
            " +(?P<num2>(\d+)) +msec$"
        )
        p14 = re.compile(
            r"^LS +Ack +list: +(?P<ls_ack_list>(\S+))"
            " +pending +(?P<pending>(\d+)), +high +water"
            " +mark +(?P<mark>(\d+))$"
        )
        p15 = re.compile(r"^Total +neighbor +count: +(?P<num>(\d+))$")

        for line in out.splitlines():
            line = line.strip()

            # Neighbors for OSPF 1
            # Neighbors for OSPF 1, VRF VRF1
            m = p1.match(line)
            if m:
                instance = str(m.groupdict()["instance"])
                if m.groupdict()["vrf"]:
                    vrf = str(m.groupdict()["vrf"])
                else:
                    vrf = "default"
                if "vrf" not in ret_dict:
                    ret_dict["vrf"] = {}
                if vrf not in ret_dict["vrf"]:
                    ret_dict["vrf"][vrf] = {}
                if "address_family" not in ret_dict["vrf"][vrf]:
                    ret_dict["vrf"][vrf]["address_family"] = {}
                if af not in ret_dict["vrf"][vrf]["address_family"]:
                    ret_dict["vrf"][vrf]["address_family"][af] = {}
                if "instance" not in ret_dict["vrf"][vrf]["address_family"][af]:
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"] = {}
                if (
                    instance
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ] = {}
                    continue

            # Neighbor 10.16.2.2, interface address 10.2.3.2
            m = p2.match(line)
            if m:
                neighbor = str(m.groupdict()["neighbor"])
                address = str(m.groupdict()["address"])
                continue

            # In the area 0 via interface GigabitEthernet0/0/0/2
            # In the area 0.0.0.0 via interface GigabitEthernet0/0/0/0 , BFD enabled, Mode: Default
            m = p3.match(line)
            if m:
                area = str(m.groupdict()["area"])
                if area.isdigit():
                    area = str(IPAddress(area))
                interface = str(m.groupdict()["interface"])

                # Determine if 'interface' or 'virtual_link'
                # Note: This show command does not have output for 'sham-links'
                if re.search("VL", interface):
                    # Set values for dict
                    intf_type = "virtual_links"
                    vl_transit_area_id = None

                    # Get interface name
                    n = re.match("(?P<ignore>\S+)_VL(?P<num>(\d+))", interface)
                    if n:
                        intf_type = "virtual_links"
                        name = "VL" + str(n.groupdict()["num"])

                    # Execute 'show ospf vrf all-inclusive virtual-links' to get the vl_transit_area_id
                    obj = ShowOspfVrfAllInclusiveVirtualLinks(device=self.device)
                    vl_out = obj.parse()

                    for vl_vrf in vl_out["vrf"]:
                        for vl_af in vl_out["vrf"][vl_vrf]["address_family"]:
                            for vl_inst in vl_out["vrf"][vl_vrf]["address_family"][
                                vl_af
                            ]["instance"]:
                                for vl_area in vl_out["vrf"][vl_vrf]["address_family"][
                                    vl_af
                                ]["instance"][vl_inst]["areas"]:
                                    for vl in vl_out["vrf"][vl_vrf]["address_family"][
                                        vl_af
                                    ]["instance"][vl_inst]["areas"][vl_area][
                                        "virtual_links"
                                    ]:
                                        vl_name = vl_out["vrf"][vl_vrf][
                                            "address_family"
                                        ][vl_af]["instance"][vl_inst]["areas"][vl_area][
                                            "virtual_links"
                                        ][
                                            vl
                                        ][
                                            "name"
                                        ]
                                        if vl_name == name:
                                            vl_transit_area_id = vl_out["vrf"][vl_vrf][
                                                "address_family"
                                            ][vl_af]["instance"][vl_inst]["areas"][
                                                vl_area
                                            ][
                                                "virtual_links"
                                            ][
                                                vl
                                            ][
                                                "transit_area_id"
                                            ]
                                            break

                    # Change the area to transit_area_id
                    if vl_transit_area_id is not None:
                        area = vl_transit_area_id
                        intf_name = area + " " + neighbor

                else:
                    # Set values for dict
                    intf_type = "interfaces"
                    intf_name = interface

                if (
                    "areas"
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance][
                        "areas"
                    ] = {}
                if (
                    area
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ]["areas"]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance][
                        "areas"
                    ][area] = {}
                if (
                    intf_type
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ]["areas"][area]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance][
                        "areas"
                    ][area][intf_type] = {}
                if (
                    intf_name
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ]["areas"][area][intf_type]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance][
                        "areas"
                    ][area][intf_type][intf_name] = {}
                if (
                    "neighbors"
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ]["areas"][area][intf_type][intf_name]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance][
                        "areas"
                    ][area][intf_type][intf_name]["neighbors"] = {}
                if (
                    neighbor
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ]["areas"][area][intf_type][intf_name]["neighbors"]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance][
                        "areas"
                    ][area][intf_type][intf_name]["neighbors"][neighbor] = {}
                    neighbor_dict = ret_dict["vrf"][vrf]["address_family"][af][
                        "instance"
                    ][instance]["areas"][area][intf_type][intf_name]["neighbors"][
                        neighbor
                    ]

                if m.groupdict()["bfd_status"]:
                    neighbor_dict.update({"bfd_enable": True})
                if m.groupdict()["mode"]:
                    neighbor_dict.update({"bfd_mode": m.groupdict()["mode"]})
                # Set sub_dict
                sub_dict = ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                    instance
                ]["areas"][area][intf_type][intf_name]["neighbors"][neighbor]
                sub_dict["neighbor_router_id"] = neighbor
                sub_dict["address"] = address
                continue

            # Neighbor priority is 1, State is FULL, 6 state changes
            m = p4.match(line)
            if m:
                sub_dict["priority"] = int(m.groupdict()["priority"])
                state = str(m.groupdict()["state"]).lower()
                state = state.replace("_", "-")
                sub_dict["state"] = state
                if "statistics" not in sub_dict:
                    sub_dict["statistics"] = {}
                sub_dict["statistics"]["nbr_event_count"] = int(m.groupdict()["num"])
                continue

            # DR is 10.2.3.3 BDR is 10.2.3.2
            m = p5.match(line)
            if m:
                sub_dict["dr_ip_addr"] = str(m.groupdict()["dr_ip_addr"])
                sub_dict["bdr_ip_addr"] = str(m.groupdict()["bdr_ip_addr"])
                continue

            # Options is 0x42
            m = p6_1.match(line)
            if m:
                sub_dict["options"] = str(m.groupdict()["options"])
                continue

            # LLS Options is 0x1 (LR)
            m = p6_2.match(line)
            if m:
                sub_dict["lls_options"] = str(m.groupdict()["lls_options"])
                continue

            # Dead timer due in 00:00:38
            m = p7.match(line)
            if m:
                sub_dict["dead_timer"] = str(m.groupdict()["dead_timer"])
                continue

            # Neighbor is up for 08:22:07
            m = p8.match(line)
            if m:
                sub_dict["neighbor_uptime"] = str(m.groupdict()["uptime"])
                continue

            # Number of DBD retrans during last exchange 0
            m = p9.match(line)
            if m:
                if "statistics" not in sub_dict:
                    sub_dict["statistics"] = {}
                sub_dict["statistics"]["total_dbd_retrans"] = int(
                    m.groupdict()["dbd_retrans"]
                )
                continue

            # Index 1/1, retransmission queue length 0, number of retransmission 0
            m = p10.match(line)
            if m:
                sub_dict["index"] = str(m.groupdict()["index"])
                if "statistics" not in sub_dict:
                    sub_dict["statistics"] = {}
                sub_dict["statistics"]["nbr_retrans_qlen"] = int(m.groupdict()["ql"])
                sub_dict["statistics"]["total_retransmission"] = int(
                    m.groupdict()["num_retrans"]
                )
                continue

            # First 0(0)/0(0) Next 0(0)/0(0)
            m = p11.match(line)
            if m:
                sub_dict["first"] = str(m.groupdict()["first"])
                sub_dict["next"] = str(m.groupdict()["next"])
                continue

            # Last retransmission scan length is 0, maximum is 0
            m = p12.match(line)
            if m:
                if "statistics" not in sub_dict:
                    sub_dict["statistics"] = {}
                sub_dict["statistics"]["last_retrans_scan_length"] = int(
                    m.groupdict()["num1"]
                )
                sub_dict["statistics"]["last_retrans_max_scan_length"] = int(
                    m.groupdict()["num2"]
                )
                continue

            # Last retransmission scan time is 0 msec, maximum is 0 msec
            m = p13.match(line)
            if m:
                if "statistics" not in sub_dict:
                    sub_dict["statistics"] = {}
                sub_dict["statistics"]["last_retrans_scan_time_msec"] = int(
                    m.groupdict()["num1"]
                )
                sub_dict["statistics"]["last_retrans_max_scan_time_msec"] = int(
                    m.groupdict()["num2"]
                )
                continue

            # LS Ack list: NSR-sync pending 0, high water mark 0
            m = p14.match(line)
            if m:
                sub_dict["ls_ack_list"] = str(m.groupdict()["ls_ack_list"])
                sub_dict["ls_ack_list_pending"] = int(m.groupdict()["pending"])
                sub_dict["high_water_mark"] = int(m.groupdict()["mark"])
                continue

            # Total neighbor count: 2
            m = p15.match(line)
            if m:
                ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance][
                    "total_neighbor_count"
                ] = int(m.groupdict()["num"])

        return ret_dict


# ========================================
# Schema for 'show ospf vrf all-inclusive'
# ========================================
class ShowOspfVrfAllInclusiveSchema(MetaParser):
    """Schema for show ospf vrf all-inclusive"""

    schema = {
        "vrf": {
            Any(): {
                "address_family": {
                    Any(): {
                        "instance": {
                            Any(): {
                                "router_id": str,
                                "role": str,
                                "nsr": {"enable": bool},
                                Optional("maximum_interfaces"): int,
                                Optional("redistribution"): {
                                    Optional("max_prefix"): {
                                        Optional("num_of_prefix"): int,
                                        Optional("prefix_thld"): int,
                                        Optional("warn_only"): bool,
                                    },
                                    Optional("connected"): {
                                        "enabled": bool,
                                        Optional("metric"): int,
                                    },
                                    Optional("static"): {
                                        "enabled": bool,
                                        Optional("metric"): int,
                                    },
                                    Optional("bgp"): {
                                        "bgp_id": int,
                                        Optional("metric"): int,
                                    },
                                    Optional("isis"): {
                                        "isis_pid": str,
                                        Optional("metric"): int,
                                    },
                                },
                                Optional("database_control"): {"max_lsa": int},
                                Optional("stub_router"): {
                                    Optional("always"): {
                                        Optional("always"): bool,
                                        Optional("include_stub"): bool,
                                        Optional("summary_lsa"): bool,
                                        Optional("external_lsa"): bool,
                                        Optional("summary_lsa_metric"): int,
                                        Optional("external_lsa_metric"): int,
                                        Optional("state"): str,
                                    },
                                    Optional("on_startup"): {
                                        Optional("on_startup"): int,
                                        Optional("include_stub"): bool,
                                        Optional("summary_lsa"): bool,
                                        Optional("summary_lsa_metric"): int,
                                        Optional("external_lsa"): bool,
                                        Optional("external_lsa_metric"): int,
                                        "state": str,
                                    },
                                    Optional("on_switchover"): {
                                        Optional("on_switchover"): int,
                                        Optional("include_stub"): bool,
                                        Optional("summary_lsa"): bool,
                                        Optional("summary_lsa_metric"): int,
                                        Optional("external_lsa"): bool,
                                        Optional("external_lsa_metric"): int,
                                        Optional("state"): str,
                                    },
                                    Optional("on_procrestart"): {
                                        Optional("on_procrestart"): int,
                                        Optional("include_stub"): bool,
                                        Optional("summary_lsa"): bool,
                                        Optional("summary_lsa_metric"): int,
                                        Optional("external_lsa"): bool,
                                        Optional("external_lsa_metric"): int,
                                        "state": str,
                                    },
                                },
                                Optional("spf_control"): {
                                    Optional("paths"): str,
                                    "throttle": {
                                        "spf": {
                                            "start": int,
                                            "hold": int,
                                            "maximum": int,
                                        },
                                        "lsa": {
                                            "start": int,
                                            "hold": int,
                                            "maximum": int,
                                            "interval": int,
                                            "arrival": int,
                                            "refresh_interval": int,
                                        },
                                    },
                                },
                                Optional("mpls"): {
                                    "ldp": {
                                        "ldp_igp_sync": bool,
                                        "ldp_sync_status": str,
                                    }
                                },
                                Optional("adjacency_stagger"): {
                                    "disable": bool,
                                    "initial_number": int,
                                    "maximum_number": int,
                                    "nbrs_forming": int,
                                    "nbrs_full": int,
                                },
                                Optional("graceful_restart"): {
                                    Any(): {"enable": bool, "type": str}
                                },
                                Optional("numbers"): {
                                    Optional("external_lsa"): int,
                                    Optional("external_lsa_checksum"): str,
                                    Optional("opaque_as_lsa"): int,
                                    Optional("opaque_as_lsa_checksum"): str,
                                    Optional("dc_bitless"): int,
                                    Optional("do_not_age"): int,
                                },
                                Optional("total_areas"): int,
                                Optional("total_normal_areas"): int,
                                Optional("total_stub_areas"): int,
                                Optional("total_nssa_areas"): int,
                                Optional("flood_pacing_interval_msec"): int,
                                Optional("retransmission_pacing_interval"): int,
                                Optional("external_flood_list_length"): int,
                                Optional("snmp_trap"): bool,
                                Optional("lsd_state"): str,
                                Optional("lsd_revision"): int,
                                Optional("segment_routing_global_block_default"): str,
                                Optional("segment_routing_global_block_status"): str,
                                Optional("strict_spf"): bool,
                                Optional("flags"): {
                                    Optional("abr"): bool,
                                    Optional("asbr"): bool,
                                },
                                Optional("areas"): {
                                    Any(): {
                                        "area_id": str,
                                        "area_type": str,
                                        Optional("summary"): bool,
                                        Optional("default_cost"): int,
                                        Optional("lsa_translation"): str,
                                        Optional("ranges"): {
                                            Any(): {"prefix": str, "advertise": bool}
                                        },
                                        Optional("rrr_enabled"): bool,
                                        Optional("topology_version"): int,
                                        Optional("statistics"): {
                                            Optional("spf_runs_count"): int,
                                            Optional("interfaces_count"): int,
                                            Optional("area_scope_lsa_count"): int,
                                            Optional("area_scope_lsa_cksum_sum"): str,
                                            Optional(
                                                "area_scope_opaque_lsa_count"
                                            ): int,
                                            Optional(
                                                "area_scope_opaque_lsa_cksum_sum"
                                            ): str,
                                            Optional("dcbitless_lsa_count"): int,
                                            Optional("indication_lsa_count"): int,
                                            Optional("donotage_lsa_count"): int,
                                            Optional("flood_list_length"): int,
                                            Optional("lfa_interface_count"): int,
                                            Optional("lfa_revision"): int,
                                            Optional(
                                                "lfa_per_prefix_interface_count"
                                            ): int,
                                            Optional("nbrs_staggered_mode"): int,
                                            Optional("nbrs_full"): int,
                                        },
                                    },
                                },
                                Optional("ipfrr_per_prefix_tiebreakers"): {
                                    Optional("name"): str,
                                    Optional("no_tunnel"): str,
                                    Optional("node_protection"): str,
                                    Optional("line_card_disjoint"): str,
                                    Optional("lowest_metric"): str,
                                    Optional("primary_path"): str,
                                    Optional("downstream"): str,
                                    Optional("secondary_path"): str,
                                    Optional("srlg_disjoint"): str,
                                    Optional("post_convergence_path"): str,
                                },
                            },
                        },
                    },
                },
            },
        },
    }


# ========================================
# Parser for 'show ospf vrf all-inclusive'
# ========================================
class ShowOspfVrfAllInclusive(ShowOspfVrfAllInclusiveSchema):
    """Parser for show ospf vrf all-inclusive"""

    cli_command = ["show ospf vrf all-inclusive", "show ospf vrf {vrf}"]
    exclude = [
        "area_scope_lsa_cksum_sum",
        "topology_version",
        "spf_runs_count",
        "external_lsa_checksum",
    ]

    def cli(self, vrf="", output=None):
        if output is None:
            if vrf:
                out = self.device.execute(self.cli_command[1].format(vrf=vrf))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # Init vars
        ret_dict = {}
        af = "ipv4"  # this is ospf - always ipv4
        condition = "always"
        p1 = re.compile(
            r"(?:^VRF +(?P<vrf>(\S+)) +in +)?Routing +Process"
            ' +"(?:ospf)? +(?P<instance>([a-zA-Z0-9\s]+))"'
            " +with +ID +(?P<router_id>(\S+))$"
        )
        p2 = re.compile(r"^Role *: +(?P<role>([a-zA-z0-9\s]+))$")
        p3 = re.compile(r"^NSR +\(Non-stop routing\) +is +(?P<nsr>(\S+))$")
        p3_1 = re.compile(r"^Supports +only +single +TOS(TOS0) routes$")
        p3_2 = re.compile(r"^Supports +opaque +LSA$")
        p4 = re.compile(r"^Redistributing +External +Routes +from,$")
        p4_1 = re.compile(
            r"^(?P<type>(connected|static))(?: +with +metric"
            " +mapped +to +(?P<metric>(\d+)))?$"
        )
        p4_2 = re.compile(
            r"^(?P<prot>(bgp|isis)) +(?P<pid>(\d+))(?: +with"
            " +metric +mapped +to +(?P<metric>(\d+)))?$"
        )
        p4_3 = re.compile(
            r"^Maximum +number +of +redistributed +prefixes"
            " +(?P<num_prefix>(\d+))"
            "(?: +\((?P<warn>(warning-only))\))?"
        )
        p4_4 = re.compile(r"^Threshold +for +warning +message" " +(?P<thld>(\d+))\%$")
        p5_0 = re.compile(
            r"^It +is +an"
            "(?: +(?P<abr>(area border)))?"
            "(?: +and)?"
            "(?: +(?P<asbr>(autonomous system boundary)))?"
            " +router$"
        )
        p5_1 = re.compile(
            r"^Router +is +not +originating +router-LSAs" " +with +maximum +metric$"
        )
        p5_2 = re.compile(r"^Originating +router-LSAs +with +maximum" " +metric$")
        p5_3 = re.compile(
            r"^Condition:"
            " +(?P<condition>(always|on switch-over|on start-up|on proc-restart))"
            "(?: +for +(?P<seconds>(\d+)) +seconds,)?"
            " +State: +(?P<state>(\S+))$"
        )
        p5_4 = re.compile(
            r"^Advertise +stub +links +with +maximum +metric" " +in +router\-LSAs$"
        )
        p5_5 = re.compile(
            r"^Advertise +summary\-LSAs +with +metric" " +(?P<metric>(\d+))$"
        )
        p5_6 = re.compile(
            r"^^Advertise +external\-LSAs +with +metric" " +(?P<metric>(\d+))$"
        )
        p6 = re.compile(r"^Initial +SPF +schedule +delay +(?P<time>(\S+))" " +msecs$")
        p7 = re.compile(
            r"^Minimum +hold +time +between +two +consecutive"
            " +SPFs +(?P<time>(\S+)) +msecs$"
        )
        p8 = re.compile(
            r"^Maximum +wait +time +between +two +consecutive"
            " +SPFs +(?P<time>(\S+)) +msecs$"
        )
        p9 = re.compile(r"^Initial +LSA +throttle +delay +(?P<time>(\S+))" " +msecs$")
        p10 = re.compile(
            r"^Minimum +hold +time +for +LSA +throttle" " +(?P<time>(\S+)) +msecs$"
        )
        p11 = re.compile(
            r"^Maximum +wait +time +for +LSA +throttle" " +(?P<time>(\S+)) +msecs$"
        )
        p12 = re.compile(
            r"^Minimum +LSA +interval +(?P<interval>(\S+))"
            " +msecs. +Minimum +LSA +arrival"
            " +(?P<arrival>(\S+)) +msecs$"
        )
        p13 = re.compile(r"^LSA +refresh +interval +(?P<refresh>(\S+))" " +seconds$")
        p14 = re.compile(
            r"^Flood +pacing +interval +(?P<flood>(\d+))"
            " +msecs\. +Retransmission +pacing +interval"
            " +(?P<retransmission>(\d+)) +msecs$"
        )
        p15 = re.compile(
            r"^Adjacency +stagger +(?P<adj>(\S+)); +initial"
            " +\(per +area\): +(?P<init>(\d+)),"
            " +maximum: +(?P<max>(\d+))$"
        )
        p16 = re.compile(
            r"^Number +of +neighbors +forming:"
            " +(?P<form>(\d+)), +(?P<full>(\d+)) +full$"
        )
        p17 = re.compile(
            r"^Maximum +number +of +configured +interfaces" " +(?P<max>(\d+))$"
        )
        p18 = re.compile(
            r"^Number +of +external +LSA +(?P<ext>(\d+))\."
            " +Checksum +Sum +(?P<checksum>(\S+))$"
        )
        p19 = re.compile(
            r"^Number +of +opaque +AS +LSA +(?P<opq>(\d+))\."
            " +Checksum +Sum +(?P<checksum>(\S+))$"
        )
        p20 = re.compile(
            r"^Number +of +DCbitless +external +and +opaque"
            " +AS +LSA +(?P<num>(\d+))$"
        )
        p21 = re.compile(
            r"^Number +of +DoNotAge +external +and +opaque" " +AS +LSA +(?P<num>(\d+))$"
        )
        p22 = re.compile(
            r"^Number +of +areas +in +this +router +is"
            " +(?P<total_areas>(\d+))\. +(?P<normal>(\d+))"
            " +normal +(?P<stub>(\d+)) +stub +(?P<nssa>(\d+))"
            " +nssa$"
        )
        p23 = re.compile(r"^External +flood +list +length +(?P<num>(\d+))$")
        p43 = re.compile(
            r"^LDP +Sync +(?P<sync>(Enabled|Disabled)),"
            " +Sync +Status: +(?P<status>(.*))$"
        )
        p25 = re.compile(
            r"^LSD +(?P<lsd>([a-zA-Z\,\s]+)), +revision" " +(?P<revision>(\d+))$"
        )
        p26 = re.compile(
            r"^Segment +Routing +Global +Block +default"
            " +\((?P<sr_block>([0-9\-]+))\),"
            " +(?P<status>(.*))$"
        )
        p27 = re.compile(r"^Strict-SPF +capability +is +(?P<state>(\S+))$")
        p28_1 = re.compile(r"^Area +(?P<area>(\S+))(?: +(inactive|\(Inactive\)))?$")
        p28_2 = re.compile(
            r"^It +is +a +(?P<area_type>(\S+)) +area"
            "(?:, +(?P<summary>(no +summary +LSA +in +this"
            " +area)))?$"
        )
        p28_3 = re.compile(
            r"^generates +stub +default +route +with +cost" " +(?P<default_cost>(\d+))$"
        )
        p28_4 = re.compile(r"^Perform +(?P<trans>(\S+)) +LSA +translation$")
        p28_5 = re.compile(r"^Area ranges are$")
        p28_6 = re.compile(
            r"^(?P<prefix>([0-9\.\/]+)) +Passive"
            " +(?P<advertise>(Advertise|DoNotAdvertise))$"
        )
        p29 = re.compile(
            r"^Number +of +interfaces +in +this +area +is" " +(?P<num_intf>(\d+))$"
        )
        p30 = re.compile(
            r"^Area +has +RRR +enabled, +topology +version" " +(?P<topo_version>(\d+))$"
        )
        p31 = re.compile(r"^SPF +algorithm +executed +(?P<count>(\d+))" " +times$")
        p32 = re.compile(
            r"^Number +of +LSA +(?P<lsa_count>(\d+))\."
            " +Checksum +Sum +(?P<checksum_sum>(\S+))$"
        )
        p33 = re.compile(
            r"^Number +of opaque +link +LSA"
            " +(?P<opaque_count>(\d+))\. +Checksum +Sum"
            " +(?P<checksum_sum>(\S+))$"
        )
        p34 = re.compile(r"^Number +of +DCbitless +LSA +(?P<count>(\d+))$")
        p35 = re.compile(r"^Number +of +indication +LSA +(?P<count>(\d+))$")
        p36 = re.compile(r"^Number +of +DoNotAge +LSA +(?P<count>(\d+))$")
        p37 = re.compile(r"^Flood +list +length +(?P<len>(\d+))$")
        p38 = re.compile(
            r"^Number +of +LFA +enabled +interfaces"
            " +(?P<count>(\d+)), +LFA +revision"
            " +(?P<revision>(\d+))$"
        )
        p39 = re.compile(
            r"^Number +of +Per +Prefix +LFA +enabled" " +interfaces +(?P<count>(\d+))$"
        )
        p40 = re.compile(
            r"^Number +of +neighbors +forming +in +staggered"
            " +mode +(?P<mode>(\d+)), +(?P<full>(\d+)) +full$"
        )
        p41 = re.compile(
            r"^Maximum +number +of +non +self-generated +LSA"
            " +allowed +(?P<max_lsa>(\d+))$"
        )
        p42 = re.compile(r"^Non-Stop +Forwarding +enabled$")
        #  IPFRR per-prefix tiebreakers:
        p43_2 = re.compile(
            r"^(?P<per_prefix_tiebreakers>\S+) +per-prefix +tiebreakers:$"
        )
        # Name                    Index
        p44 = re.compile(r"^Name +(?P<name>\S+)$")
        # No Tunnel (Implicit)    255
        p45 = re.compile(r"^No +Tunnel +\(Implicit\) +(?P<no_tunnel>\S+)$")
        # Node Protection         40
        p46 = re.compile(r"^Node +Protection +(?P<node_protection>\S+)$")
        # Line-card Disjoint      30
        p47 = re.compile(r"^Line-card +Disjoint +(?P<line_card_disjoint>\S+)$")
        # Lowest Metric           20
        p48 = re.compile(r"^Lowest +Metric +(?P<lowest_metric>\S+)$")
        # Primary Path            10
        p49 = re.compile(r"^Primary +Path +(?P<primary_path>\S+)$")
        # Downstream              0
        p50 = re.compile(r"^Downstream +(?P<downstream>\S+)$")
        # Secondary Path          0
        p51 = re.compile(r"^Secondary +Path +(?P<secondary_path>\S+)$")
        # SRLG Disjoint           0
        p52 = re.compile(r"^SRLG +Disjoint +(?P<srlg_disjoint>\S+)$")
        # Post Convergence Path   0
        p53 = re.compile(r"^Post +Convergence +Path +(?P<post_convergence_path>\S+)$")

        for line in out.splitlines():
            line = line.strip()

            # Routing Process "ospf 1" with ID 10.36.3.3
            # VRF VRF1 in Routing Process "ospf 1" with ID 10.36.3.3
            m = p1.match(line)
            if m:
                instance = str(m.groupdict()["instance"])
                router_id = str(m.groupdict()["router_id"])
                if m.groupdict()["vrf"]:
                    vrf = str(m.groupdict()["vrf"])
                else:
                    vrf = "default"

                # Set structure
                if "vrf" not in ret_dict:
                    ret_dict["vrf"] = {}
                if vrf not in ret_dict["vrf"]:
                    ret_dict["vrf"][vrf] = {}
                if "address_family" not in ret_dict["vrf"][vrf]:
                    ret_dict["vrf"][vrf]["address_family"] = {}
                if af not in ret_dict["vrf"][vrf]["address_family"]:
                    ret_dict["vrf"][vrf]["address_family"][af] = {}
                if "instance" not in ret_dict["vrf"][vrf]["address_family"][af]:
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"] = {}
                if (
                    instance
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ] = {}

                # Set sub_dict
                sub_dict = ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                    instance
                ]
                sub_dict["router_id"] = router_id
                continue

            # Role: Primary Active
            m = p2.match(line)
            if m:
                sub_dict["role"] = str(m.groupdict()["role"]).lower()
                continue

            # NSR (Non-stop routing) is Enabled
            m = p3.match(line)
            if m:
                nsr = str(m.groupdict()["nsr"]).lower()
                if "nsr" not in sub_dict:
                    sub_dict["nsr"] = {}
                if nsr == "enabled":
                    sub_dict["nsr"]["enable"] = True
                else:
                    sub_dict["nsr"]["enable"] = False
                    continue

            # Supports only single TOS(TOS0) routes
            m = p3_1.match(line)
            if m:
                # Not sure what the key is
                continue

            # Supports opaque LSA
            m = p3_2.match(line)
            if m:
                # Not sure what the key is
                continue

            # Redistributing External Routes from,
            m = p4.match(line)
            if m:
                if "redistribution" not in sub_dict:
                    sub_dict["redistribution"] = {}
                    continue

            # connected
            # connected with metric mapped to 10
            # static
            # static with metric mapped to 10
            m = p4_1.match(line)
            if m:
                the_type = str(m.groupdict()["type"])
                if the_type not in sub_dict["redistribution"]:
                    sub_dict["redistribution"][the_type] = {}
                sub_dict["redistribution"][the_type]["enabled"] = True
                if m.groupdict()["metric"]:
                    sub_dict["redistribution"][the_type]["metric"] = int(
                        m.groupdict()["metric"]
                    )
                    continue

            # bgp 100 with metric mapped to 111
            # isis 10 with metric mapped to 3333
            m = p4_2.match(line)
            if m:
                prot = str(m.groupdict()["prot"])
                if prot not in sub_dict["redistribution"]:
                    sub_dict["redistribution"][prot] = {}
                if prot == "bgp":
                    sub_dict["redistribution"][prot]["bgp_id"] = int(
                        m.groupdict()["pid"]
                    )
                else:
                    sub_dict["redistribution"][prot]["isis_pid"] = str(
                        m.groupdict()["pid"]
                    )
                if m.groupdict()["metric"]:
                    sub_dict["redistribution"][prot]["metric"] = int(
                        m.groupdict()["metric"]
                    )
                continue

            # Maximum number of redistributed prefixes 4000
            # Maximum number of redistributed prefixes 3000 (warning-only)
            m = p4_3.match(line)
            if m:
                if "max_prefix" not in sub_dict["redistribution"]:
                    sub_dict["redistribution"]["max_prefix"] = {}
                sub_dict["redistribution"]["max_prefix"]["num_of_prefix"] = int(
                    m.groupdict()["num_prefix"]
                )
                if m.groupdict()["warn"]:
                    sub_dict["redistribution"]["max_prefix"]["warn_only"] = True
                else:
                    sub_dict["redistribution"]["max_prefix"]["warn_only"] = False
                    continue

            # Threshold for warning message 70%
            m = p4_4.match(line)
            if m:
                if "max_prefix" not in sub_dict["redistribution"]:
                    sub_dict["redistribution"]["max_prefix"] = {}
                sub_dict["redistribution"]["max_prefix"]["prefix_thld"] = int(
                    m.groupdict()["thld"]
                )
                continue

            # It is an area border router
            # It is an autonomous system boundary router
            # It is an area border and autonomous system boundary router
            m = p5_0.match(line)
            if m:
                if "flags" not in sub_dict:
                    sub_dict["flags"] = {}
                if m.groupdict()["abr"]:
                    sub_dict["flags"]["abr"] = True
                if m.groupdict()["asbr"]:
                    sub_dict["flags"]["asbr"] = True
                continue

            # Router is not originating router-LSAs with maximum metric
            m = p5_1.match(line)
            if m:
                if "stub_router" not in sub_dict:
                    sub_dict["stub_router"] = {}
                if "always" not in sub_dict["stub_router"]:
                    sub_dict["stub_router"]["always"] = {}
                # Set values
                sub_dict["stub_router"]["always"]["always"] = False
                sub_dict["stub_router"]["always"]["include_stub"] = False
                sub_dict["stub_router"]["always"]["summary_lsa"] = False
                sub_dict["stub_router"]["always"]["external_lsa"] = False
                continue

            # Originating router-LSAs with maximum metric
            m = p5_2.match(line)
            if m:
                if "stub_router" not in sub_dict:
                    sub_dict["stub_router"] = {}
                    continue

            # Condition: always State: active
            # Condition: on switch-over for 10 seconds, State: inactive
            # Condition: on start-up for 5 seconds, State: inactive
            # Condition: on proc-restart for 900 seconds, State: inactive
            m = p5_3.match(line)
            if m:
                condition = str(m.groupdict()["condition"]).lower().replace("-", "")
                condition = condition.replace(" ", "_")
                if "stub_router" not in sub_dict:
                    sub_dict["stub_router"] = {}
                if condition not in sub_dict["stub_router"]:
                    sub_dict["stub_router"][condition] = {}
                sub_dict["stub_router"][condition]["state"] = str(
                    m.groupdict()["state"]
                ).lower()
                # Set 'condition' key
                if condition == "always":
                    sub_dict["stub_router"][condition][condition] = True
                else:
                    sub_dict["stub_router"][condition][condition] = int(
                        m.groupdict()["seconds"]
                    )
                continue

            # Advertise stub links with maximum metric in router-LSAs
            m = p5_4.match(line)
            if m:
                sub_dict.setdefault("stub_router", {}).setdefault(condition, {})
                sub_dict["stub_router"][condition]["include_stub"] = True
                continue

            # Advertise summary-LSAs with metric 16711680
            m = p5_5.match(line)
            if m:
                sub_dict["stub_router"][condition]["summary_lsa"] = True
                sub_dict["stub_router"][condition]["summary_lsa_metric"] = int(
                    m.groupdict()["metric"]
                )
                continue

            # Advertise external-LSAs with metric 16711680
            m = p5_6.match(line)
            if m:
                sub_dict["stub_router"][condition]["external_lsa"] = True
                sub_dict["stub_router"][condition]["external_lsa_metric"] = int(
                    m.groupdict()["metric"]
                )
                continue

            # Initial SPF schedule delay 50 msecs
            m = p6.match(line)
            if m:
                start = int(float(m.groupdict()["time"]))
                if "spf_control" not in sub_dict:
                    sub_dict["spf_control"] = {}
                if "throttle" not in sub_dict["spf_control"]:
                    sub_dict["spf_control"]["throttle"] = {}
                if "spf" not in sub_dict["spf_control"]["throttle"]:
                    sub_dict["spf_control"]["throttle"]["spf"] = {}
                sub_dict["spf_control"]["throttle"]["spf"]["start"] = start
                continue

            # Minimum hold time between two consecutive SPFs 200 msecs
            m = p7.match(line)
            if m:
                hold = int(float(m.groupdict()["time"]))
                if "spf_control" not in sub_dict:
                    sub_dict["spf_control"] = {}
                if "throttle" not in sub_dict["spf_control"]:
                    sub_dict["spf_control"]["throttle"] = {}
                if "spf" not in sub_dict["spf_control"]["throttle"]:
                    sub_dict["spf_control"]["throttle"]["spf"] = {}
                sub_dict["spf_control"]["throttle"]["spf"]["hold"] = hold
                continue

            # Maximum wait time between two consecutive SPFs 5000 msecs
            m = p8.match(line)
            if m:
                maximum = int(float(m.groupdict()["time"]))
                if "spf_control" not in sub_dict:
                    sub_dict["spf_control"] = {}
                if "throttle" not in sub_dict["spf_control"]:
                    sub_dict["spf_control"]["throttle"] = {}
                if "spf" not in sub_dict["spf_control"]["throttle"]:
                    sub_dict["spf_control"]["throttle"]["spf"] = {}
                sub_dict["spf_control"]["throttle"]["spf"]["maximum"] = maximum
                continue

            # Initial LSA throttle delay 50 msecs
            m = p9.match(line)
            if m:
                start = int(float(m.groupdict()["time"]))
                if "spf_control" not in sub_dict:
                    sub_dict["spf_control"] = {}
                if "throttle" not in sub_dict["spf_control"]:
                    sub_dict["spf_control"]["throttle"] = {}
                if "lsa" not in sub_dict["spf_control"]["throttle"]:
                    sub_dict["spf_control"]["throttle"]["lsa"] = {}
                sub_dict["spf_control"]["throttle"]["lsa"]["start"] = start
                continue

            # Minimum hold time for LSA throttle 200 msecs
            m = p10.match(line)
            if m:
                hold = int(float(m.groupdict()["time"]))
                if "spf_control" not in sub_dict:
                    sub_dict["spf_control"] = {}
                if "throttle" not in sub_dict["spf_control"]:
                    sub_dict["spf_control"]["throttle"] = {}
                if "lsa" not in sub_dict["spf_control"]["throttle"]:
                    sub_dict["spf_control"]["throttle"]["lsa"] = {}
                sub_dict["spf_control"]["throttle"]["lsa"]["hold"] = hold
                continue

            # Maximum wait time for LSA throttle 5000 msecs
            m = p11.match(line)
            if m:
                maximum = int(float(m.groupdict()["time"]))
                if "spf_control" not in sub_dict:
                    sub_dict["spf_control"] = {}
                if "throttle" not in sub_dict["spf_control"]:
                    sub_dict["spf_control"]["throttle"] = {}
                if "lsa" not in sub_dict["spf_control"]["throttle"]:
                    sub_dict["spf_control"]["throttle"]["lsa"] = {}
                sub_dict["spf_control"]["throttle"]["lsa"]["maximum"] = maximum
                continue

            # Minimum LSA interval 200 msecs. Minimum LSA arrival 100 msecs
            m = p12.match(line)
            if m:
                sub_dict["spf_control"]["throttle"]["lsa"]["interval"] = int(
                    float(m.groupdict()["interval"])
                )
                sub_dict["spf_control"]["throttle"]["lsa"]["arrival"] = int(
                    float(m.groupdict()["arrival"])
                )
                continue

            # LSA refresh interval 1800 seconds
            m = p13.match(line)
            if m:
                sub_dict["spf_control"]["throttle"]["lsa"]["refresh_interval"] = int(
                    float(m.groupdict()["refresh"])
                )
                continue

            # Flood pacing interval 33 msecs. Retransmission pacing interval 66 msecs
            m = p14.match(line)
            if m:
                sub_dict["flood_pacing_interval_msec"] = int(
                    float(m.groupdict()["flood"])
                )
                sub_dict["retransmission_pacing_interval"] = int(
                    float(m.groupdict()["retransmission"])
                )
                continue

            # Adjacency stagger enabled; initial (per area): 2, maximum: 64
            m = p15.match(line)
            if m:
                if "adjacency_stagger" not in sub_dict:
                    sub_dict["adjacency_stagger"] = {}
                if "enable" in m.groupdict()["adj"]:
                    sub_dict["adjacency_stagger"]["disable"] = False
                else:
                    sub_dict["adjacency_stagger"]["disable"] = True
                sub_dict["adjacency_stagger"]["initial_number"] = int(
                    m.groupdict()["init"]
                )
                sub_dict["adjacency_stagger"]["maximum_number"] = int(
                    m.groupdict()["max"]
                )
                continue

            # Number of neighbors forming: 0, 2 full
            m = p16.match(line)
            if m:
                if "adjacency_stagger" not in sub_dict:
                    sub_dict["adjacency_stagger"] = {}
                sub_dict["adjacency_stagger"]["nbrs_forming"] = int(
                    m.groupdict()["form"]
                )
                sub_dict["adjacency_stagger"]["nbrs_full"] = int(m.groupdict()["full"])
                continue

            # Maximum number of configured interfaces 1024
            m = p17.match(line)
            if m:
                sub_dict["maximum_interfaces"] = int(m.groupdict()["max"])
                continue

            # Number of external LSA 1. Checksum Sum 0x00607f
            m = p18.match(line)
            if m:
                if "numbers" not in sub_dict:
                    sub_dict["numbers"] = {}
                sub_dict["numbers"]["external_lsa"] = int(m.groupdict()["ext"])
                sub_dict["numbers"]["external_lsa_checksum"] = str(
                    m.groupdict()["checksum"]
                )
                continue

            # Number of opaque AS LSA 0. Checksum Sum 00000000
            m = p19.match(line)
            if m:
                if "numbers" not in sub_dict:
                    sub_dict["numbers"] = {}
                sub_dict["numbers"]["opaque_as_lsa"] = int(m.groupdict()["opq"])
                sub_dict["numbers"]["opaque_as_lsa_checksum"] = str(
                    m.groupdict()["checksum"]
                )
                continue

            # Number of DCbitless external and opaque AS LSA 0
            m = p20.match(line)
            if m:
                if "numbers" not in sub_dict:
                    sub_dict["numbers"] = {}
                sub_dict["numbers"]["dc_bitless"] = int(m.groupdict()["num"])
                continue

            # Number of DoNotAge external and opaque AS LSA 0
            m = p21.match(line)
            if m:
                if "numbers" not in sub_dict:
                    sub_dict["numbers"] = {}
                sub_dict["numbers"]["do_not_age"] = int(m.groupdict()["num"])
                continue

            # Number of areas in this router is 1. 1 normal 0 stub 0 nssa
            m = p22.match(line)
            if m:
                sub_dict["total_areas"] = int(m.groupdict()["total_areas"])
                sub_dict["total_normal_areas"] = int(m.groupdict()["normal"])
                sub_dict["total_stub_areas"] = int(m.groupdict()["stub"])
                sub_dict["total_nssa_areas"] = int(m.groupdict()["nssa"])
                continue

            # External flood list length 0
            m = p23.match(line)
            if m:
                sub_dict["external_flood_list_length"] = int(m.groupdict()["num"])
                continue

            # SNMP trap is enabled
            p24 = re.compile(r"^SNMP +trap +is +(?P<snmp>(\S+))$")
            m = p24.match(line)
            if m:
                if "enabled" in m.groupdict()["snmp"]:
                    sub_dict["snmp_trap"] = True
                else:
                    sub_dict["snmp_trap"] = False
                continue

            # LDP Sync Enabled, Sync Status: Not Achieved
            m = p43.match(line)
            if m:
                if "mpls" not in sub_dict:
                    sub_dict["mpls"] = {}
                if "ldp" not in sub_dict["mpls"]:
                    sub_dict["mpls"]["ldp"] = {}
                if "Enabled" in m.groupdict()["sync"]:
                    sub_dict["mpls"]["ldp"]["ldp_igp_sync"] = True
                else:
                    sub_dict["mpls"]["ldp"]["ldp_igp_sync"] = False
                sub_dict["mpls"]["ldp"]["ldp_sync_status"] = str(
                    m.groupdict()["status"]
                ).lower()
                continue

            # LSD connected, registered, bound, revision 1
            m = p25.match(line)
            if m:
                sub_dict["lsd_state"] = str(m.groupdict()["lsd"])
                sub_dict["lsd_revision"] = int(m.groupdict()["revision"])
                continue

            # Segment Routing Global Block default (16000-23999), not allocated
            m = p26.match(line)
            if m:
                sub_dict["segment_routing_global_block_default"] = str(
                    m.groupdict()["sr_block"]
                )
                sub_dict["segment_routing_global_block_status"] = str(
                    m.groupdict()["status"]
                )
                continue

            # Strict-SPF capability is enabled
            m = p27.match(line)
            if m:
                if "enabled" in m.groupdict()["state"]:
                    sub_dict["strict_spf"] = True
                else:
                    sub_dict["strict_spf"] = False
                continue

            # Area BACKBONE(0)
            # Area 1
            # Area BACKBONE(0) (Inactive)
            m = p28_1.match(line)
            if m:
                parsed_area = str(m.groupdict()["area"])
                n = re.match("BACKBONE\((?P<area_num>(\S+))\)", parsed_area)
                if n:
                    area = str(n.groupdict()["area_num"])
                    if area.isdigit():
                        area = str(IPAddress(area))
                else:
                    area = str(m.groupdict()["area"])
                    if area.isdigit():
                        area = str(IPAddress(area))

                # Create dict
                if "areas" not in sub_dict:
                    sub_dict["areas"] = {}
                if area not in sub_dict["areas"]:
                    sub_dict["areas"][area] = {}

                # Set default values
                sub_dict["areas"][area]["area_id"] = area
                sub_dict["areas"][area]["area_type"] = "normal"
                continue

            # It is a stub area
            # It is a stub area, no summary LSA in this area
            # It is a NSSA area
            m = p28_2.match(line)
            if m:
                area_type = str(m.groupdict()["area_type"]).lower()
                sub_dict["areas"][area]["area_type"] = area_type
                if area_type == "stub":
                    if m.groupdict()["summary"]:
                        sub_dict["areas"][area]["summary"] = False
                    else:
                        sub_dict["areas"][area]["summary"] = True
                        continue

            # generates stub default route with cost 111
            # generates stub default route with cost 222
            m = p28_3.match(line)
            if m:
                sub_dict["areas"][area]["default_cost"] = int(
                    m.groupdict()["default_cost"]
                )
                continue

            # Perform type-7/type-5 LSA translation
            m = p28_4.match(line)
            if m:
                sub_dict["areas"][area]["lsa_translation"] = str(m.groupdict()["trans"])
                continue

            # Area ranges are
            m = p28_5.match(line)
            if m:
                if "ranges" not in sub_dict["areas"][area]:
                    sub_dict["areas"][area]["ranges"] = {}
                    continue

            # 10.16.2.0/24 Passive Advertise
            # 10.4.0.0/16 Passive DoNotAdvertise
            m = p28_6.match(line)
            if m:
                prefix = str(m.groupdict()["prefix"])
                if "ranges" not in sub_dict["areas"][area]:
                    sub_dict["areas"][area]["ranges"] = {}
                if prefix not in sub_dict["areas"][area]["ranges"]:
                    sub_dict["areas"][area]["ranges"][prefix] = {}
                sub_dict["areas"][area]["ranges"][prefix]["prefix"] = prefix
                if "Advertise" in m.groupdict()["advertise"]:
                    sub_dict["areas"][area]["ranges"][prefix]["advertise"] = True
                else:
                    sub_dict["areas"][area]["ranges"][prefix]["advertise"] = False
                    continue

            # Number of interfaces in this area is 3
            m = p29.match(line)
            if m:
                if "statistics" not in sub_dict["areas"][area]:
                    sub_dict["areas"][area]["statistics"] = {}
                sub_dict["areas"][area]["statistics"]["interfaces_count"] = int(
                    m.groupdict()["num_intf"]
                )
                continue

            # Area has RRR enabled, topology version 15
            m = p30.match(line)
            if m:
                sub_dict["areas"][area]["rrr_enabled"] = True
                sub_dict["areas"][area]["topology_version"] = int(
                    m.groupdict()["topo_version"]
                )
                continue

            # SPF algorithm executed 26 times
            m = p31.match(line)
            if m:
                if "statistics" not in sub_dict["areas"][area]:
                    sub_dict["areas"][area]["statistics"] = {}
                sub_dict["areas"][area]["statistics"]["spf_runs_count"] = int(
                    m.groupdict()["count"]
                )
                continue

            # Number of LSA 19.  Checksum Sum 0x0a2fb5
            m = p32.match(line)
            if m:
                if "statistics" not in sub_dict["areas"][area]:
                    sub_dict["areas"][area]["statistics"] = {}
                sub_dict["areas"][area]["statistics"]["area_scope_lsa_count"] = int(
                    m.groupdict()["lsa_count"]
                )
                sub_dict["areas"][area]["statistics"]["area_scope_lsa_cksum_sum"] = str(
                    m.groupdict()["checksum_sum"]
                )
                continue

            # Number of opaque link LSA 0.  Checksum Sum 00000000
            m = p33.match(line)
            if m:
                if "statistics" not in sub_dict["areas"][area]:
                    sub_dict["areas"][area]["statistics"] = {}
                sub_dict["areas"][area]["statistics"][
                    "area_scope_opaque_lsa_count"
                ] = int(m.groupdict()["opaque_count"])
                sub_dict["areas"][area]["statistics"][
                    "area_scope_opaque_lsa_cksum_sum"
                ] = str(m.groupdict()["checksum_sum"])
                continue

            # Number of DCbitless LSA 5
            m = p34.match(line)
            if m:
                if "statistics" not in sub_dict["areas"][area]:
                    sub_dict["areas"][area]["statistics"] = {}
                sub_dict["areas"][area]["statistics"]["dcbitless_lsa_count"] = int(
                    m.groupdict()["count"]
                )
                continue

            # Number of indication LSA 0
            m = p35.match(line)
            if m:
                if "statistics" not in sub_dict["areas"][area]:
                    sub_dict["areas"][area]["statistics"] = {}
                sub_dict["areas"][area]["statistics"]["indication_lsa_count"] = int(
                    m.groupdict()["count"]
                )
                continue

            # Number of DoNotAge LSA 0
            m = p36.match(line)
            if m:
                if "statistics" not in sub_dict["areas"][area]:
                    sub_dict["areas"][area]["statistics"] = {}
                sub_dict["areas"][area]["statistics"]["donotage_lsa_count"] = int(
                    m.groupdict()["count"]
                )
                continue

            # Flood list length 0
            m = p37.match(line)
            if m:
                if "statistics" not in sub_dict["areas"][area]:
                    sub_dict["areas"][area]["statistics"] = {}
                sub_dict["areas"][area]["statistics"]["flood_list_length"] = int(
                    m.groupdict()["len"]
                )
                continue

            # Number of LFA enabled interfaces 0, LFA revision 0
            m = p38.match(line)
            if m:
                if "statistics" not in sub_dict["areas"][area]:
                    sub_dict["areas"][area]["statistics"] = {}
                sub_dict["areas"][area]["statistics"]["lfa_interface_count"] = int(
                    m.groupdict()["count"]
                )
                sub_dict["areas"][area]["statistics"]["lfa_revision"] = int(
                    m.groupdict()["revision"]
                )
                continue

            # Number of Per Prefix LFA enabled interfaces 0
            m = p39.match(line)
            if m:
                if "statistics" not in sub_dict["areas"][area]:
                    sub_dict["areas"][area]["statistics"] = {}
                sub_dict["areas"][area]["statistics"][
                    "lfa_per_prefix_interface_count"
                ] = int(m.groupdict()["count"])
                continue

            # Number of neighbors forming in staggered mode 0, 2 full
            m = p40.match(line)
            if m:
                if "statistics" not in sub_dict["areas"][area]:
                    sub_dict["areas"][area]["statistics"] = {}
                sub_dict["areas"][area]["statistics"]["nbrs_staggered_mode"] = int(
                    m.groupdict()["mode"]
                )
                sub_dict["areas"][area]["statistics"]["nbrs_full"] = int(
                    m.groupdict()["full"]
                )
                continue

            # Maximum number of non self-generated LSA allowed 123
            m = p41.match(line)
            if m:
                if "database_control" not in sub_dict:
                    sub_dict["database_control"] = {}
                sub_dict["database_control"]["max_lsa"] = int(m.groupdict()["max_lsa"])
                continue

            # Non-Stop Forwarding enabled
            m = p42.match(line)
            if m:
                # Execute command on device
                out = self.device.execute("show run formal router ospf | i nsf")

                # router ospf 1 vrf VRF1 nsf ietf
                for line in out.splitlines():
                    line = line.rstrip()
                    # router ospf 1 vrf VRF1 nsf ietf
                    # router ospf 1 nsf ietf
                    p = re.search(
                        "router +ospf +(?P<new_inst>(\d+))(?: +vrf"
                        " +(?P<new_vrf>(\S+)))? +nsf"
                        " +(?P<gr_type>(\S+))",
                        line,
                    )
                    if p:
                        new_inst = str(p.groupdict()["new_inst"])
                        if p.groupdict()["new_vrf"]:
                            new_vrf = str(p.groupdict()["new_vrf"])
                        else:
                            new_vrf = "default"
                        gr_type = str(p.groupdict()["gr_type"])
                        if new_vrf == vrf and new_inst == instance:
                            if "graceful_restart" not in sub_dict:
                                sub_dict["graceful_restart"] = {}
                            if gr_type not in sub_dict["graceful_restart"]:
                                sub_dict["graceful_restart"][gr_type] = {}
                            # Set keys
                            sub_dict["graceful_restart"][gr_type]["enable"] = True
                            sub_dict["graceful_restart"][gr_type]["type"] = gr_type
                            continue

            #  IPFRR per-prefix tiebreakers:
            m = p43_2.match(line)
            if m:
                group = m.groupdict()
                sub_dict.setdefault("ipfrr_per_prefix_tiebreakers", {})
                continue

            # Name                    Index
            m = p44.match(line)
            if m:
                group = m.groupdict()
                sub_dict.setdefault("ipfrr_per_prefix_tiebreakers", {})["name"] = group[
                    "name"
                ]
                continue

            # No Tunnel (Implicit)    255
            m = p45.match(line)
            if m:
                group = m.groupdict()
                sub_dict.setdefault("ipfrr_per_prefix_tiebreakers", {})[
                    "no_tunnel"
                ] = group["no_tunnel"]
                continue

            # Node Protection         40
            m = p46.match(line)
            if m:
                group = m.groupdict()
                sub_dict.setdefault("ipfrr_per_prefix_tiebreakers", {})[
                    "node_protection"
                ] = group["node_protection"]
                continue

            # Line-card Disjoint      30
            m = p47.match(line)
            if m:
                group = m.groupdict()
                sub_dict.setdefault("ipfrr_per_prefix_tiebreakers", {})[
                    "line_card_disjoint"
                ] = group["line_card_disjoint"]
                continue

            # Lowest Metric           20
            m = p48.match(line)
            if m:
                group = m.groupdict()
                sub_dict.setdefault("ipfrr_per_prefix_tiebreakers", {})[
                    "lowest_metric"
                ] = group["lowest_metric"]
                continue

            # Primary Path            10
            m = p49.match(line)
            if m:
                group = m.groupdict()
                sub_dict.setdefault("ipfrr_per_prefix_tiebreakers", {})[
                    "primary_path"
                ] = group["primary_path"]
                continue

            # Downstream              0
            m = p50.match(line)
            if m:
                group = m.groupdict()
                sub_dict.setdefault("ipfrr_per_prefix_tiebreakers", {})[
                    "downstream"
                ] = group["downstream"]
                continue

            # Secondary Path          0
            m = p51.match(line)
            if m:
                group = m.groupdict()
                sub_dict.setdefault("ipfrr_per_prefix_tiebreakers", {})[
                    "secondary_path"
                ] = group["secondary_path"]
                continue

            # SRLG Disjoint           0m = p40.match(line)
            m = p52.match(line)
            if m:
                group = m.groupdict()
                sub_dict.setdefault("ipfrr_per_prefix_tiebreakers", {})[
                    "srlg_disjoint"
                ] = group["srlg_disjoint"]
                continue

            # Post Convergence Path   0
            m = p53.match(line)
            if m:
                group = m.groupdict()
                sub_dict.setdefault("ipfrr_per_prefix_tiebreakers", {})[
                    "post_convergence_path"
                ] = group["post_convergence_path"]
                continue

        return ret_dict


# ===========================================================
# Super parser for 'show ospf vrf all-inclusive <link_type>-links'
# ===========================================================
class ShowOspfVrfAllInclusiveLinksParser(MetaParser):

    """Parser for "show ip ospf vrf all-inclusive <link_type>-links"""

    def cli(self, cmd, link_type, output=None):

        assert link_type in ["virtual_links", "sham_links"]
        if output is None:
            # Execute command on device
            out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        ret_dict = {}
        af = "ipv4"

        # crypo_algorithm dict
        crypto_dict = {"message digest": "md5", "clear text": "simple"}

        for line in out.splitlines():
            line = line.strip()

            # Virtual Links for OSPF 1
            # Sham Links for OSPF 1, VRF VRF1
            p1 = re.compile(
                r"^(Virtual|Sham) +Links +for +OSPF"
                " +(?P<instance>([a-zA-Z0-9\s]+))"
                "(?:, +VRF +(?P<vrf>(\S+)))?$"
            )
            m = p1.match(line)
            if m:
                instance = str(m.groupdict()["instance"])
                if m.groupdict()["vrf"]:
                    vrf = str(m.groupdict()["vrf"])
                else:
                    vrf = "default"

                # Build dict
                if "vrf" not in ret_dict:
                    ret_dict["vrf"] = {}
                if vrf not in ret_dict["vrf"]:
                    ret_dict["vrf"][vrf] = {}
                if "address_family" not in ret_dict["vrf"][vrf]:
                    ret_dict["vrf"][vrf]["address_family"] = {}
                if af not in ret_dict["vrf"][vrf]["address_family"]:
                    ret_dict["vrf"][vrf]["address_family"][af] = {}
                if "instance" not in ret_dict["vrf"][vrf]["address_family"][af]:
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"] = {}
                if (
                    instance
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ] = {}
                    continue

            # Sham Link OSPF_SL0 to address 10.151.22.22 is up
            # Virtual Link OSPF_VL0 to router 10.64.4.4 is up
            p2 = re.compile(
                r"^(Virtual|Sham) +Link +(?P<link>(\S+)) +to"
                " +(address|router) +(?P<address>(\S+)) +is"
                " +(?P<link_state>(up|down))$"
            )
            m = p2.match(line)
            if m:
                address = str(m.groupdict()["address"])
                sl_remote_id = vl_router_id = address
                link = str(m.groupdict()["link"])
                link_state = str(m.groupdict()["link_state"])
                n = re.match("(?P<ignore>\S+)_(?P<name>(S|V)L(\d+))", link)
                if n:
                    real_link_name = str(n.groupdict()["name"])
                else:
                    real_link_name = link
                    continue

            # Area 1, source address 10.21.33.33
            p3_1 = re.compile(
                r"^Area +(?P<area>(\S+)), +source +address"
                " +(?P<source_address>(\S+))$"
            )
            m = p3_1.match(line)
            if m:
                area = str(m.groupdict()["area"])
                if area.isdigit():
                    area = str(IPAddress(area))
                source_address = str(m.groupdict()["source_address"])

                # Set link_name for sham_link
                link_name = source_address + " " + sl_remote_id

                # Create dict
                if (
                    "areas"
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance][
                        "areas"
                    ] = {}
                if (
                    area
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ]["areas"]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance][
                        "areas"
                    ][area] = {}
                if (
                    link_type
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ]["areas"][area]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance][
                        "areas"
                    ][area][link_type] = {}
                if (
                    link_name
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ]["areas"][area][link_type]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance][
                        "areas"
                    ][area][link_type][link_name] = {}

                # Set sub_dict
                sub_dict = ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                    instance
                ]["areas"][area][link_type][link_name]

                # Set values
                sub_dict["transit_area_id"] = area
                sub_dict["local_id"] = source_address
                sub_dict["demand_circuit"] = False

                # Set previously parsed values
                try:
                    sub_dict["name"] = real_link_name
                    sub_dict["remote_id"] = sl_remote_id
                    sub_dict["link_state"] = link_state
                except Exception:
                    pass
                continue

            # Transit area 1, via interface GigabitEthernet0/0/0/3, Cost of using 65535
            p3_2 = re.compile(
                r"^Transit +area +(?P<area>(\S+)),"
                "(?: +via +interface +(?P<intf>(\S+)),)?"
                " +Cost +of +using +(?P<cost>(\d+))$"
            )
            m = p3_2.match(line)
            if m:
                area = str(m.groupdict()["area"])
                if area.isdigit():
                    area = str(IPAddress(area))

                # Set link_name for virtual_link
                link_name = area + " " + vl_router_id

                # Create dict
                if (
                    "areas"
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance][
                        "areas"
                    ] = {}
                if (
                    area
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ]["areas"]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance][
                        "areas"
                    ][area] = {}
                if (
                    link_type
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ]["areas"][area]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance][
                        "areas"
                    ][area][link_type] = {}
                if (
                    link_name
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ]["areas"][area][link_type]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance][
                        "areas"
                    ][area][link_type][link_name] = {}

                # Set sub_dict
                sub_dict = ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                    instance
                ]["areas"][area][link_type][link_name]

                # Set values
                sub_dict["transit_area_id"] = area
                sub_dict["demand_circuit"] = False
                sub_dict["cost"] = int(m.groupdict()["cost"])
                if m.groupdict()["intf"]:
                    sub_dict["interface"] = str(m.groupdict()["intf"])

                # Set previously parsed values
                try:
                    sub_dict["name"] = real_link_name
                    sub_dict["router_id"] = vl_router_id
                    sub_dict["dcbitless_lsa_count"] = dcbitless_lsa_count
                    sub_dict["donotage_lsa"] = donotage_lsa
                    sub_dict["demand_circuit"] = demand_circuit
                    sub_dict["link_state"] = link_state
                except Exception:
                    pass
                continue

            # IfIndex = 2
            p4 = re.compile(r"^IfIndex += +(?P<if_index>(\d+))$")
            m = p4.match(line)
            if m:
                sub_dict["if_index"] = int(m.groupdict()["if_index"])
                continue

            # Run as demand circuit
            p5 = re.compile(r"^Run +as +demand +circuit$")
            m = p5.match(line)
            if m:
                if link_type == "sham_links":
                    sub_dict["demand_circuit"] = True
                else:
                    demand_circuit = True
                continue

            # DoNotAge LSA not allowed (Number of DCbitless LSA is 1)., Cost of using 111
            # DoNotAge LSA not allowed Run as demand circuit (Number of DCbitless LSA is 1).
            p6 = re.compile(
                r"^DoNotAge +LSA +not +allowed"
                "(?: +(?P<demand>(Run +as +demand +circuit)))?"
                " +\(Number +of +DCbitless +LSA +is +(?P<dcbitless>(\d+))\).,?"
                "(?: +Cost +of +using +(?P<cost>(\d+)))?$"
            )
            m = p6.match(line)
            if m:
                dcbitless_lsa_count = int(m.groupdict()["dcbitless"])
                donotage_lsa = "not allowed"
                if m.groupdict()["demand"]:
                    demand_circuit = True
                # Set values for sham_links
                if link_type == "sham_links":
                    sub_dict["dcbitless_lsa_count"] = dcbitless_lsa_count
                    sub_dict["donotage_lsa"] = donotage_lsa
                    if m.groupdict()["cost"]:
                        sub_dict["cost"] = int(m.groupdict()["cost"])
                        continue

            # Transmit Delay is 7 sec, State POINT_TO_POINT,
            # Transmit Delay is 5 sec, State POINT_TO_POINT,
            p7 = re.compile(
                r"^Transmit +Delay +is +(?P<transmit_delay>(\d+))"
                " +sec, +State +(?P<state>(\S+)),?$"
            )
            m = p7.match(line)
            if m:
                sub_dict["transmit_delay"] = int(m.groupdict()["transmit_delay"])
                state = str(m.groupdict()["state"]).lower()
                state = state.replace("_", "-")
                sub_dict["state"] = state
                continue

            # Timer intervals configured, Hello 3, Dead 13, Wait 13, Retransmit 5
            # Timer intervals configured, Hello 4, Dead 16, Wait 16, Retransmit 44
            p8 = re.compile(
                r"^Timer +intervals +configured,"
                " +Hello +(?P<hello>(\d+)),"
                " +Dead +(?P<dead>(\d+)),"
                " +Wait +(?P<wait>(\d+)),"
                " +Retransmit +(?P<retransmit>(\d+))$"
            )
            m = p8.match(line)
            if m:
                sub_dict["hello_interval"] = int(m.groupdict()["hello"])
                sub_dict["dead_interval"] = int(m.groupdict()["dead"])
                sub_dict["wait_interval"] = int(m.groupdict()["wait"])
                sub_dict["retransmit_interval"] = int(m.groupdict()["retransmit"])
                continue

            # Hello due in 00:00:00:772
            # Hello due in 00:00:03:179
            p9 = re.compile(r"^Hello +due +in +(?P<hello_timer>(\S+))$")
            m = p9.match(line)
            if m:
                sub_dict["hello_timer"] = str(m.groupdict()["hello_timer"])
                continue

            # Non-Stop Forwarding (NSF) enabled, last NSF restart 00:18:16 ago
            p10 = re.compile(
                r"^Non-Stop +Forwarding +\(NSF\)"
                " +(?P<state>(enabled|disabled)), +last +NSF"
                " +restart +(?P<restart>(\S+)) +ago$"
            )
            m = p10.match(line)
            if m:
                if "nsf" not in sub_dict:
                    sub_dict["nsf"] = {}
                if "enabled" in m.groupdict()["state"]:
                    sub_dict["nsf"]["enable"] = True
                else:
                    sub_dict["nsf"]["enable"] = False
                sub_dict["nsf"]["last_restart"] = str(m.groupdict()["restart"])
                continue

            # Clear text authentication enabled
            # Message digest authentication enabled
            p11 = re.compile(r"^(?P<auth>([a-zA-Z\s]+)) +authentication +enabled$")
            m = p11.match(line)
            if m:
                auth = str(m.groupdict()["auth"]).lower()
                if "authentication" not in sub_dict:
                    sub_dict["authentication"] = {}
                if "auth_trailer_key" not in sub_dict["authentication"]:
                    sub_dict["authentication"]["auth_trailer_key"] = {}
                sub_dict["authentication"]["auth_trailer_key"][
                    "crypto_algorithm"
                ] = crypto_dict[auth]
                continue

            # Youngest key id is 1
            p12 = re.compile(r"^Youngest +key +id +is +(?P<young>(\d+))$")
            m = p12.match(line)
            if m:
                if "authentication" not in sub_dict:
                    sub_dict["authentication"] = {}
                if "auth_trailer_key" not in sub_dict["authentication"]:
                    sub_dict["authentication"]["auth_trailer_key"] = {}
                sub_dict["authentication"]["auth_trailer_key"]["youngest_key_id"] = int(
                    m.groupdict()["young"]
                )
                continue

        return ret_dict


# ===================================================
# Schema for 'show ospf vrf all-inclusive sham-links'
# ===================================================
class ShowOspfVrfAllInclusiveShamLinksSchema(MetaParser):
    """Schema for show ospf vrf all-inclusive sham-links"""

    schema = {
        "vrf": {
            Any(): {
                "address_family": {
                    Any(): {
                        "instance": {
                            Any(): {
                                "areas": {
                                    Any(): {
                                        "sham_links": {
                                            Any(): {
                                                "name": str,
                                                "link_state": str,
                                                "local_id": str,
                                                "remote_id": str,
                                                "transit_area_id": str,
                                                "hello_interval": int,
                                                "dead_interval": int,
                                                "wait_interval": int,
                                                "retransmit_interval": int,
                                                "transmit_delay": int,
                                                "cost": int,
                                                "state": str,
                                                "hello_timer": str,
                                                "demand_circuit": bool,
                                                "if_index": int,
                                                Optional("dcbitless_lsa_count"): int,
                                                Optional("donotage_lsa"): str,
                                                Optional("nsf"): {
                                                    "enable": bool,
                                                    "last_restart": str,
                                                },
                                                Optional("authentication"): {
                                                    "auth_trailer_key": {
                                                        "crypto_algorithm": str,
                                                        Optional(
                                                            "youngest_key_id"
                                                        ): int,
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }


# ===================================================
# Parser for 'show ospf vrf all-inclusive sham-links'
# ===================================================
class ShowOspfVrfAllInclusiveShamLinks(
    ShowOspfVrfAllInclusiveShamLinksSchema, ShowOspfVrfAllInclusiveLinksParser
):

    """Parser for show ospf vrf all-inclusive sham-links"""

    cli_command = [
        "show ospf vrf all-inclusive sham-links",
        "show ospf vrf {vrf} sham-links",
    ]

    def cli(self, vrf="", output=None):
        if vrf:
            cmd = self.cli_command[1].format(vrf=vrf)
        else:
            cmd = self.cli_command[0]
        return super().cli(cmd=cmd, link_type="sham_links", output=output)


# ======================================================
# Schema for 'show ospf vrf all-inclusive virtual-links'
# ======================================================
class ShowOspfVrfAllInclusiveVirtualLinksSchema(MetaParser):
    """Schema for show ospf vrf all-inclusive virtual-links"""

    schema = {
        "vrf": {
            Any(): {
                "address_family": {
                    Any(): {
                        "instance": {
                            Any(): {
                                "areas": {
                                    Any(): {
                                        "virtual_links": {
                                            Any(): {
                                                "name": str,
                                                "link_state": str,
                                                "router_id": str,
                                                "transit_area_id": str,
                                                "hello_interval": int,
                                                "dead_interval": int,
                                                "wait_interval": int,
                                                "retransmit_interval": int,
                                                "transmit_delay": int,
                                                "cost": int,
                                                "state": str,
                                                "demand_circuit": bool,
                                                Optional("hello_timer"): str,
                                                Optional("interface"): str,
                                                Optional("dcbitless_lsa_count"): int,
                                                Optional("donotage_lsa"): str,
                                                Optional("nsf"): {
                                                    "enable": bool,
                                                    "last_restart": str,
                                                },
                                                Optional("authentication"): {
                                                    "auth_trailer_key": {
                                                        "crypto_algorithm": str,
                                                        Optional(
                                                            "youngest_key_id"
                                                        ): int,
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }


# ======================================================
# Parser for 'show ospf vrf all-inclusive virtual-links'
# ======================================================
class ShowOspfVrfAllInclusiveVirtualLinks(
    ShowOspfVrfAllInclusiveVirtualLinksSchema, ShowOspfVrfAllInclusiveLinksParser
):

    """Parser for show ospf vrf all-inclusive virtual-links"""

    cli_command = [
        "show ospf vrf all-inclusive virtual-links",
        "show ospf vrf {vrf} virtual-links",
    ]

    def cli(self, vrf="", output=None):
        if vrf:
            cmd = self.cli_command[1].format(vrf=vrf)
        else:
            cmd = self.cli_command[0]
        return super().cli(cmd=cmd, link_type="virtual_links", output=output)


# ============================================
# Schema for 'show ospf mpls traffic-eng link'
# ============================================
class ShowOspfMplsTrafficEngLinkSchema(MetaParser):
    """Schema for show ospf mpls traffic-eng link"""

    schema = {
        "vrf": {
            Any(): {
                "address_family": {
                    Any(): {
                        "instance": {
                            Any(): {
                                "mpls": {"te": {"router_id": str},},
                                "areas": {
                                    Any(): {
                                        "mpls": {
                                            "te": {
                                                "enable": bool,
                                                Optional("total_links"): int,
                                                Optional("area_instance"): int,
                                                Optional("link_fragments"): {
                                                    Any(): {
                                                        "link_instance": int,
                                                        "network_type": str,
                                                        "link_id": str,
                                                        "interface_address": str,
                                                        "te_admin_metric": int,
                                                        "maximum_bandwidth": int,
                                                        "maximum_reservable_bandwidth": int,
                                                        "total_priority": int,
                                                        "out_interface_id": int,
                                                        "affinity_bit": str,
                                                        "total_extended_admin_group": int,
                                                        "unreserved_bandwidths": {
                                                            Any(): {
                                                                "priority": int,
                                                                "unreserved_bandwidth": int,
                                                            },
                                                        },
                                                        "extended_admin_groups": {
                                                            Any(): {"value": int,},
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }


# ============================================
# Parser for 'show ospf mpls traffic-eng link'
# ============================================
class ShowOspfMplsTrafficEngLink(ShowOspfMplsTrafficEngLinkSchema):
    """Parser for show ospf mpls traffic-eng link"""

    cli_command = "show ospf mpls traffic-eng link"
    exclude = ["area_instance"]

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        ret_dict = {}
        af = "ipv4"

        p1 = re.compile(
            r"^OSPF +Router +with +ID +\((?P<router_id>(\S+))\)"
            " +\(Process +ID +(?P<instance>(\S+))\)$"
        )
        p2_1 = re.compile(
            r"^Area +(?P<area>(\S+)) +has"
            " +(?P<total_links>(\d+)) +MPLS +TE links\."
            " +Area +instance +is +(?P<instance>(\d+))\.$"
        )
        p2_2 = re.compile(r"^Area +(?P<area>(\S+)) +MPLS +TE +not" " +initialized$")
        p3 = re.compile(
            r"^Link +is +associated +with +fragment"
            " +(?P<fragment>(\d+))\. +Link +instance +is"
            " +(?P<link_instance>(\d+))$"
        )
        p4 = re.compile(r"^Link +connected +to +(?P<net>(\S+)) +network$")
        p5 = re.compile(r"^Link +ID *: +(?P<link_id>(\S+))$")
        p6 = re.compile(r"^Interface +Address *: +(?P<address>(\S+))$")
        p7 = re.compile(r"^Admin +Metric *: +TE *: +(?P<metric>(\d+))$")
        p8 = re.compile(r"^Maximum +bandwidth *: +(?P<max_band>(\d+))$")
        p9 = re.compile(
            r"^Maximum +global +pool +reservable +bandwidth *:"
            " +(?P<max_reserve_band>(\d+))$"
        )
        p15 = re.compile(r"^Number +of +Priority *: +(?P<priority>(\d+))$")
        p10 = re.compile(
            r"^Priority +(?P<priority1>(\d+)) *: +(?P<band1>(\d+))"
            " *Priority +(?P<priority2>(\d+)) *: +(?P<band2>(\d+))$"
        )
        p11 = re.compile(r"^Out +Interface +ID *: +(?P<out_id>(\d+))$")
        p12 = re.compile(r"^Affinity +Bit *: +(?P<affinity>(\S+))$")
        p13 = re.compile(r"^Extended +Admin +Group *: +(?P<eag>(\d+))$")
        p14 = re.compile(r"^EAG\[(?P<group_num>(\d+))\]:" " +(?P<value>(\d+))$")

        for line in out.splitlines():
            line = line.strip()

            # OSPF Router with ID (10.36.3.3) (Process ID 1)
            m = p1.match(line)
            if m:
                vrf = "default"
                instance = str(m.groupdict()["instance"])
                if "vrf" not in ret_dict:
                    ret_dict["vrf"] = {}
                if vrf not in ret_dict["vrf"]:
                    ret_dict["vrf"][vrf] = {}
                if "address_family" not in ret_dict["vrf"][vrf]:
                    ret_dict["vrf"][vrf]["address_family"] = {}
                if af not in ret_dict["vrf"][vrf]["address_family"]:
                    ret_dict["vrf"][vrf]["address_family"][af] = {}
                if "instance" not in ret_dict["vrf"][vrf]["address_family"][af]:
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"] = {}
                if (
                    instance
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ] = {}
                if (
                    "mpls"
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance][
                        "mpls"
                    ] = {}
                if (
                    "te"
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ]["mpls"]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance][
                        "mpls"
                    ]["te"] = {}
                # Set keys
                ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance][
                    "mpls"
                ]["te"]["router_id"] = str(m.groupdict()["router_id"])
                continue

            # Area 0 has 2 MPLS TE links. Area instance is 2.
            m = p2_1.match(line)
            if m:
                area = str(m.groupdict()["area"])
                if area.isdigit():
                    area = str(IPAddress(area))
                if (
                    "areas"
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance][
                        "areas"
                    ] = {}
                if (
                    area
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ]["areas"]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance][
                        "areas"
                    ][area] = {}
                if (
                    "mpls"
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ]["areas"][area]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance][
                        "areas"
                    ][area]["mpls"] = {}
                if (
                    "te"
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ]["areas"][area]["mpls"]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance][
                        "areas"
                    ][area]["mpls"]["te"] = {}

                # Set sub_dict
                sub_dict = ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                    instance
                ]["areas"][area]["mpls"]["te"]

                # Set values
                sub_dict["enable"] = True
                sub_dict["total_links"] = int(m.groupdict()["total_links"])
                sub_dict["area_instance"] = int(m.groupdict()["instance"])
                continue

            # Area 1 MPLS TE not initialized
            # Area 0.0.0.0 MPLS TE not initialized
            m = p2_2.match(line)
            if m:
                area = str(m.groupdict()["area"])
                if area.isdigit():
                    area = str(IPAddress(area))
                if (
                    "areas"
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance][
                        "areas"
                    ] = {}
                if (
                    area
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ]["areas"]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance][
                        "areas"
                    ][area] = {}
                if (
                    "mpls"
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ]["areas"][area]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance][
                        "areas"
                    ][area]["mpls"] = {}
                if (
                    "te"
                    not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                        instance
                    ]["areas"][area]["mpls"]
                ):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance][
                        "areas"
                    ][area]["mpls"]["te"] = {}

                # Set sub_dict
                sub_dict = ret_dict["vrf"][vrf]["address_family"][af]["instance"][
                    instance
                ]["areas"][area]["mpls"]["te"]

                # Set values
                sub_dict["enable"] = False
                continue

            # Link is associated with fragment 1. Link instance is 2
            m = p3.match(line)
            if m:
                fragment = int(m.groupdict()["fragment"])
                if "link_fragments" not in sub_dict:
                    sub_dict["link_fragments"] = {}
                if fragment not in sub_dict["link_fragments"]:
                    sub_dict["link_fragments"][fragment] = {}

                # Create link_dict
                link_dict = sub_dict["link_fragments"][fragment]

                # Set values
                link_dict["link_instance"] = int(m.groupdict()["link_instance"])
                continue

            # Link connected to Broadcast network
            m = p4.match(line)
            if m:
                link_dict["network_type"] = str(m.groupdict()["net"]).lower()
                continue

            # Link ID : 10.3.4.4
            m = p5.match(line)
            if m:
                link_dict["link_id"] = str(m.groupdict()["link_id"])
                continue

            # Interface Address : 10.3.4.3
            m = p6.match(line)
            if m:
                link_dict["interface_address"] = str(m.groupdict()["address"])
                continue

            # Admin Metric : TE: 1
            m = p7.match(line)
            if m:
                link_dict["te_admin_metric"] = int(m.groupdict()["metric"])
                continue

            # (all bandwidths in bytes/sec)

            # Maximum bandwidth : 125000000
            m = p8.match(line)
            if m:
                link_dict["maximum_bandwidth"] = int(m.groupdict()["max_band"])
                continue

            # Maximum global pool reservable bandwidth : 93750000
            m = p9.match(line)
            if m:
                link_dict["maximum_reservable_bandwidth"] = int(
                    m.groupdict()["max_reserve_band"]
                )
                continue

            # Number of Priority : 8
            m = p15.match(line)
            if m:
                link_dict["total_priority"] = int(m.groupdict()["priority"])
                continue

            # Global pool unreserved BW

            # Priority 0 :             93750000  Priority 1 :           93750000
            # Priority 2 :             93750000  Priority 3 :           93750000
            # Priority 4 :             93750000  Priority 5 :           93750000
            # Priority 6 :             93750000  Priority 7 :           93750000
            m = p10.match(line)
            if m:
                priority1 = str(m.groupdict()["priority1"])
                priority2 = str(m.groupdict()["priority2"])
                band1 = str(m.groupdict()["band1"])
                band2 = str(m.groupdict()["band2"])
                value1 = priority1 + " " + band1
                value2 = priority2 + " " + band2
                if "unreserved_bandwidths" not in link_dict:
                    link_dict["unreserved_bandwidths"] = {}
                # Set keys for first parsed value
                if value1 not in link_dict["unreserved_bandwidths"]:
                    link_dict["unreserved_bandwidths"][value1] = {}
                link_dict["unreserved_bandwidths"][value1]["priority"] = int(priority1)
                link_dict["unreserved_bandwidths"][value1][
                    "unreserved_bandwidth"
                ] = int(band1)
                # Set keys for second parsed value
                if value2 not in link_dict["unreserved_bandwidths"]:
                    link_dict["unreserved_bandwidths"][value2] = {}
                link_dict["unreserved_bandwidths"][value2]["priority"] = int(priority2)
                link_dict["unreserved_bandwidths"][value2][
                    "unreserved_bandwidth"
                ] = int(band2)
                continue

            # Out Interface ID : 4
            m = p11.match(line)
            if m:
                link_dict["out_interface_id"] = int(m.groupdict()["out_id"])
                continue

            # Affinity Bit : 0
            # Affinity Bit : 0x100000
            m = p12.match(line)
            if m:
                link_dict["affinity_bit"] = m.groupdict()["affinity"]
                continue

            # Extended Admin Group : 8
            m = p13.match(line)
            if m:
                link_dict["total_extended_admin_group"] = int(m.groupdict()["eag"])
                continue

            # EAG[0]: 0
            # EAG[1]: 0
            m = p14.match(line)
            if m:
                group_num = int(m.groupdict()["group_num"])
                if "extended_admin_groups" not in link_dict:
                    link_dict["extended_admin_groups"] = {}
                if group_num not in link_dict["extended_admin_groups"]:
                    link_dict["extended_admin_groups"][group_num] = {}
                link_dict["extended_admin_groups"][group_num]["value"] = int(
                    m.groupdict()["value"]
                )
                continue

        return ret_dict


# ==============================================================
# Super parser for 'show ospf vrf all-inclusive database <db_type>'
# ==============================================================
class ShowOspfVrfAllInclusiveDatabaseParser(MetaParser):
    """Parser for show ospf vrf all-inclusive database <db_type>"""

    def cli(self, cmd, db_type, output=None):

        assert db_type in ["external", "network", "summary", "router", "opaque"]

        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        ret_dict = {}
        af = "ipv4"
        mt_id = 0

        # Router
        # Network Link
        # Summary Network
        # Opaque Area
        # Type-5 AS External
        lsa_type_mapping = {
            "router": 1,
            "network": 2,
            "summary": 3,
            "external": 5,
            "opaque": 10,
        }

        p1 = re.compile(
            r"^OSPF +Router +with +ID +\((?P<router_id>(\S+))\)"
            " +\(Process +ID +(?P<instance>(\S+))"
            "(?:, +VRF +(?P<vrf>(\S+)))?\)$"
        )
        p2 = re.compile(
            r"^(?P<lsa_type_name>(.*)) +Link +States"
            "(?: +\(Area +(?P<area>(\S+))\))?$"
        )
        p3_1 = re.compile(r"^Routing +Bit +Set +on +this +LSA$")
        p3_2 = re.compile(r"^LS +age: +(?P<age>(\d+))$")
        p4 = re.compile(
            r"^Options:(?: +(?P<option>([a-zA-Z0-9]+)))?"
            "(?: *\((?P<option_desc>(.*))\))?$"
        )
        p5_1 = re.compile(r"^LS +Type: +(?P<lsa_type>(.*))$")
        p5_2 = re.compile(r"^Link +State +ID: +(?P<lsa_id>(\S+))" "(?: +\(.*\))?$")
        p6 = re.compile(r"^Advertising +Router: +(?P<adv_router>(\S+))$")
        p7 = re.compile(r"^LS +Seq +Number: +(?P<ls_seq_num>(\S+))$")
        p8 = re.compile(r"^Checksum: +(?P<checksum>(\S+))$")
        p9 = re.compile(r"^Length: +(?P<length>(\d+))$")
        p10 = re.compile(r"^Network +Mask: +\/(?P<net_mask>(\S+))$")
        p11_1 = re.compile(r"^Metric +Type: +2 +\(.*\)$")
        p11_2 = re.compile(r"^Metric +Type: +1 +\(.*\)$")
        p12 = re.compile(
            r"^TOS:? +(?P<tos>(\d+))(?:(\s+|\t+)Metric(?:s)?:" " +(?P<metric>(\d+)))?$"
        )
        p13 = re.compile(r"^Metric: +(?P<metric>(\d+))$")
        p14 = re.compile(r"^Forward +Address: +(?P<addr>(\S+))$")
        p15 = re.compile(r"^External +Route +Tag: +(?P<tag>(\d+))$")
        p16 = re.compile(r"^Attached +Router: +(?P<att_router>(\S+))$")

        # Number of Links : 1
        # Number of Links: 3
        p17 = re.compile(r"^Number +of +(l|L)inks *: +(?P<num>(\d+))$")
        p18 = re.compile(r"^Link +connected +to: +a +(?P<type>(.*))$")
        p18_1 = re.compile(r"^Link +connected +to: +(?P<type>(.*))$")
        p19_1 = re.compile(
            r"^\(Link +ID\) +Network\/(s|S)ubnet +(n|N)umber:" " +(?P<link_id>(\S+))$"
        )
        p19_2 = re.compile(
            r"^\(Link +ID\) +(D|d)esignated +(R|r)outer"
            " +(a|A)ddress: +(?P<link_id>(\S+))$"
        )
        p19_3 = re.compile(
            r"^\(Link +ID\) +(N|n)eighboring +(R|r)outer"
            " +(I|d)D: +(?P<link_id>(\S+))$"
        )
        p20_1 = re.compile(r"^\(Link +Data\) +Network +Mask:" " +(?P<link_data>(\S+))$")
        p20_2 = re.compile(
            r"^\(Link +Data\) +Router +Interface +address:" " +(?P<link_data>(\S+))$"
        )
        p21 = re.compile(r"^Number +of +TOS +metrics: +(?P<num>(\d+))$")
        p22 = re.compile(r"^Opaque +Type: +(?P<type>(\d+))$")
        p23 = re.compile(r"^Opaque +ID: +(?P<id>(\d+))$")
        p24 = re.compile(r"^Fragment +number: +(?P<num>(\d+))$")
        p25 = re.compile(r"^MPLS +TE +router +ID *: +(?P<mpls>(\S+))$")
        p26_1 = re.compile(r"^AS +Boundary +Router$")
        p26_2 = re.compile(r"^Area +Border +Router$")
        p27 = re.compile(r"^Link +connected +to +(?P<link>(.*))$")
        p28 = re.compile(r"^Link +ID *: +(?P<id>(\S+))$")
        p29 = re.compile(r"^Interface +Address *: +(?P<addr>(\S+))$")
        p30 = re.compile(r"^Admin +Metric *: +(?P<te_metric>(\d+))$")
        p31 = re.compile(r"^Maximum +(B|b)andwidth *:" " +(?P<max_band>(\d+))$")
        p32 = re.compile(
            r"^Maximum +(R|r)eservable +(B|b)andwidth"
            "(?: +global)? *: +(?P<max_res_band>(\d+))$"
        )
        p33 = re.compile(r"^Affinity +Bit *: +(?P<admin_group>(\S+))$")
        p33_1 = re.compile(r"^IGP +Metric *: +(?P<igp_metric>(\d+))$")
        p33_2 = re.compile(r"^Number +of +Priority *: +(?P<num>(\d+))$")
        p34 = re.compile(
            r"^Priority +(?P<num1>(\d+)) *:"
            " +(?P<band1>(\d+))(?: +Priority +(?P<num2>(\d+))"
            " *: +(?P<band2>(\d+)))?$"
        )
        p35 = re.compile(
            r"^Unknown +Sub-TLV *: +Type += +(?P<type>(\d+)),"
            " +Length += +(?P<length>(\d+))"
            " +Value += +(?P<value>(.*))$"
        )
        p36 = re.compile(
            r"^Extended +Administrative +Group *: +Length *:" " +(?P<eag_length>(\d+))$"
        )
        p37 = re.compile(r"^EAG\[(?P<group_num>(\d+))\]: +(?P<val>(\d+))$")

        # --regex for opaque-- #
        # Router Information TLV: Length: 4
        p38 = re.compile(r"^Router +Information +TLV: +Length: +(?P<length>\d+)$")

        # Capabilities:
        #   Graceful Restart Helper Capable
        p39 = re.compile(r"^Graceful +Restart +Helper +Capable$")

        #   Stub Router Capable
        p40 = re.compile(r"^Stub +Router +Capable$")

        #   All capability bits: 0x60000000
        p41 = re.compile(r"^All +capability +bits: +(?P<bits>\w+)$")

        # Segment Routing Algorithm TLV: Length: 2
        p42 = re.compile(
            r"^Segment +Routing +Algorithm +TLV: +Length: +(?P<length>\d+)$"
        )

        #   Algorithm: 0
        #   Algorithm: 1
        p43 = re.compile(r"^Algorithm: +(?P<algo>\d+)$")

        # Segment Routing Range TLV: Length: 12
        p44 = re.compile(r"^Segment +Routing +Range +TLV: +Length: +(?P<length>\d+)$")

        #   Range Size: 65535
        p45 = re.compile(r"^Range +Size: +(?P<range_size>\d+)$")

        #     SID sub-TLV: Length 3
        #     SID sub-TLV: Length: 8
        p46 = re.compile(r"^(?P<type>[\S\s]+) +sub-TLV: +Length:? +(?P<length>\d+)$")

        #      Label: 16000
        p47 = re.compile(r"^Label *: +(?P<label>\d+)$")

        # Node MSD TLV: Length: 2
        p48 = re.compile(r"^Node MSD TLV: +Length: +(?P<length>\d+)$")

        #     Type: 1, Value 10
        p49 = re.compile(r"^Type: +(?P<type>\d+), +Value +(?P<value>\d+)$")

        # Segment Routing Local Block TLV: Length: 12
        p50 = re.compile(
            r"^Segment +Routing +Local +Block +TLV: +Length: +(?P<length>\d+)$"
        )

        # Extended Prefix Range TLV: Length: 24
        # Extended Prefix TLV: Length: 24
        p51 = re.compile(r"^Extended +Prefix +(Range +)?TLV: +Length: +(?P<length>\d+)$")

        #   AF        : 0
        p52 = re.compile(r"^AF *: +(?P<af>\d+)$")

        #   Prefix    : 10.246.254.0/32
        p53 = re.compile(r"^Prefix *: +(?P<prefix>\S+)$")

        #   Flags     : 0x0
        p54 = re.compile(r"^Flags *: +(?P<flags>\S+)$")

        #     MTID      : 0
        p55 = re.compile(r"^MTID *: +(?P<mt_id>\d+)$")

        #     Algo      : 0
        p56 = re.compile(r"^Algo *: +(?P<algo>\d+)$")

        #     SID Index : 1028
        p57 = re.compile(r"^SID +Index *: +(?P<sid_index>\d+)$")

        # Extended Link TLV: Length: 76
        p58 = re.compile(r"^Extended +Link +TLV: +Length: +(?P<length>\d+)$")

        #   Link-type : 1
        p59 = re.compile(r"^Link-type *: +(?P<link_type>\d+)$")

        #   Link Data : 172.16.0.91
        p60 = re.compile(r"^Link +Data *: +(?P<link_data>\S+)$")

        #     Weight    : 0
        p61 = re.compile(r"^Weight *: +(?P<weight>\d+)$")

        #     Local Interface ID: 78
        p62 = re.compile(r"^Local +Interface +ID *: +(?P<local_id>\d+)$")

        #     Remote Interface ID: 76
        p63 = re.compile(r"^Remote +Interface +ID *: +(?P<remote_id>\d+)$")

        #     Neighbor Address: 172.16.0.90
        p64 = re.compile(r"^Neighbor +Address *: +(?P<nbr_addr>\S+)$")

        for line in out.splitlines():
            line = line.strip()

            # OSPF Router with ID (10.36.3.3) (Process ID 1)
            # OSPF Router with ID (10.36.3.3) (Process ID 1, VRF VRF1)
            # OSPF Router with ID (10.4.1.1) (Process ID mpls1)
            m = p1.match(line)
            if m:
                router_id = str(m.groupdict()["router_id"])
                instance = str(m.groupdict()["instance"])
                if m.groupdict()["vrf"]:
                    vrf = str(m.groupdict()["vrf"])
                else:
                    vrf = "default"

                inst_dict = (
                    ret_dict.setdefault("vrf", {})
                    .setdefault(vrf, {})
                    .setdefault("address_family", {})
                    .setdefault(af, {})
                    .setdefault("instance", {})
                    .setdefault(instance, {})
                )
                continue

            # Router Link States (Area 0)
            # Net Link States (Area 1)
            # Net Link States (Area 0.0.0.0)
            # Summary Net Link States (Area 0.0.0.0)
            # Type-5 AS External Link States
            # Type-10 Opaque Link Area Link States (Area 0)
            m = p2.match(line)
            if m:
                lsa_type = lsa_type_mapping[db_type]

                # Set area
                if m.groupdict()["area"]:
                    try:
                        int(m.groupdict()["area"])
                        area = str(IPAddress(str(m.groupdict()["area"])))
                    except Exception:
                        area = str(m.groupdict()["area"])
                else:
                    area = "0.0.0.0"

                # Create dict structure
                type_dict = (
                    inst_dict.setdefault("areas", {})
                    .setdefault(area, {})
                    .setdefault("database", {})
                    .setdefault("lsa_types", {})
                    .setdefault(lsa_type, {})
                )

                # Set lsa_type
                type_dict["lsa_type"] = lsa_type
                continue

            # Routing Bit Set on this LSA
            m = p3_1.match(line)
            if m:
                routing_bit_enable = True
                continue

            # LS age: 1565
            m = p3_2.match(line)
            if m:
                age = int(m.groupdict()["age"])
                continue

            # Options: 0x20 (No TOS-capability, DC)
            # Options: (No TOS-capability, DC)
            m = p4.match(line)
            if m:
                option = str(m.groupdict()["option"])
                option_desc = str(m.groupdict()["option_desc"])
                continue

            # LS Type: Type-5 AS-External
            m = p5_1.match(line)
            if m:
                lsa_type = lsa_type_mapping[db_type]
                continue

            # Link State ID: 10.4.1.1
            # Link State ID: 10.94.44.44 (Network address)
            # Link State ID: 10.1.2.1 (Designated Router address)
            # Link State ID: 10.1.2.1 (address of Designated Router)
            m = p5_2.match(line)
            if m:
                lsa_id = str(m.groupdict()["lsa_id"])
                continue

            # Advertising Router: 10.64.4.4
            m = p6.match(line)
            if m:
                adv_router = str(m.groupdict()["adv_router"])
                lsa = lsa_id + " " + adv_router

                # Reset counters for this lsa
                tlv_idx = 0
                unknown_tlvs_counter = 0

                # Create schema structure
                lsa_dict = type_dict.setdefault("lsas", {}).setdefault(lsa, {})

                # Set keys under 'lsa'
                lsa_dict["adv_router"] = adv_router
                try:
                    lsa_dict["lsa_id"] = lsa_id
                except Exception:
                    pass

                # Set header dict
                header_dict = lsa_dict.setdefault("ospfv2", {}).setdefault("header", {})

                # Set db_dict
                db_dict = (
                    lsa_dict.setdefault("ospfv2", {})
                    .setdefault("body", {})
                    .setdefault(db_type, {})
                )

                # Create 'topologies' sub_dict if 'summary' or 'database'
                if db_type in ["summary", "external"]:
                    db_topo_dict = db_dict.setdefault("topologies", {}).setdefault(
                        mt_id, {}
                    )
                    db_topo_dict["mt_id"] = mt_id

                # Set previously parsed values
                try:
                    header_dict["routing_bit_enable"] = routing_bit_enable
                    del routing_bit_enable
                except Exception:
                    pass
                try:
                    header_dict["age"] = age
                    del age
                except Exception:
                    pass
                try:
                    header_dict["option"] = option
                    del option
                except Exception:
                    pass
                try:
                    header_dict["option_desc"] = option_desc
                    del option_desc
                except Exception:
                    pass
                try:
                    header_dict["type"] = lsa_type
                    del lsa_type
                except Exception:
                    pass
                try:
                    header_dict["lsa_id"] = lsa_id
                    del lsa_id
                except Exception:
                    pass
                try:
                    header_dict["adv_router"] = adv_router
                    del adv_router
                except Exception:
                    pass
                try:
                    header_dict["opaque_type"] = opaque_type
                    del opaque_type
                except Exception:
                    pass
                try:
                    header_dict["opaque_id"] = opaque_id
                    del opaque_id
                except Exception:
                    pass

            # LS Seq Number: 0x80000002
            m = p7.match(line)
            if m:
                header_dict["seq_num"] = str(m.groupdict()["ls_seq_num"])
                continue

            # Checksum: 0x7d61
            m = p8.match(line)
            if m:
                header_dict["checksum"] = str(m.groupdict()["checksum"])
                continue

            # Length: 36
            m = p9.match(line)
            if m:
                header_dict["length"] = int(m.groupdict()["length"])
                continue

            # Network Mask: /32
            m = p10.match(line)
            if m:
                dummy = "{}/{}".format("0.0.0.0", m.groupdict()["net_mask"])
                db_dict["network_mask"] = str(IPNetwork(dummy).netmask)
                continue

            # Metric Type: 2 (Larger than any link state path)
            # Metric Type: 2 (Larger than any link state path)
            m = p11_1.match(line)
            if m:
                db_topo_dict["flags"] = "E"
                continue

            # Metric Type: 1 (Comparable directly to link state metric)
            m = p11_2.match(line)
            if m:
                # Do nothing
                continue

            # TOS: 0
            # TOS: 0 Metric: 1
            m = p12.match(line)
            if m:
                if db_type == "router":
                    if m.groupdict()["tos"]:
                        db_dict["links"][link_id]["topologies"][mt_id]["tos"] = int(
                            m.groupdict()["tos"]
                        )
                    if m.groupdict()["metric"]:
                        db_dict["links"][link_id]["topologies"][mt_id]["metric"] = int(
                            m.groupdict()["metric"]
                        )
                        continue
                else:
                    db_topo_dict["tos"] = int(m.groupdict()["tos"])
                    if m.groupdict()["metric"]:
                        db_topo_dict["metric"] = int(m.groupdict()["metric"])
                        continue

            # Metric: 20
            m = p13.match(line)
            if m:
                db_topo_dict["metric"] = int(m.groupdict()["metric"])
                continue

            # Forward Address: 0.0.0.0
            m = p14.match(line)
            if m:
                db_topo_dict["forwarding_address"] = str(m.groupdict()["addr"])
                continue

            # External Route Tag: 0
            m = p15.match(line)
            if m:
                db_topo_dict["external_route_tag"] = int(m.groupdict()["tag"])
                continue

            # Attached Router: 10.84.66.66
            m = p16.match(line)
            if m:
                attached_router = str(m.groupdict()["att_router"])
                if "attached_routers" not in db_dict:
                    db_dict["attached_routers"] = {}
                if attached_router not in db_dict["attached_routers"]:
                    db_dict["attached_routers"][attached_router] = {}
                    continue

            # Number of Links: 3
            m = p17.match(line)
            if m:
                db_dict["num_of_links"] = int(m.groupdict()["num"])
                continue

            # Link connected to: a Stub Network
            m = p18.match(line)
            if m:
                link_type = str(m.groupdict()["type"]).lower()
                continue

            # Link connected to: another Router (point-to-point)
            m = p18_1.match(line)
            if m:
                link_type = str(m.groupdict()["type"]).lower()
                continue

            # (Link ID) Network/subnet number: 10.4.1.1
            m = p19_1.match(line)
            if m:
                link_id = str(m.groupdict()["link_id"])

                # Create dict structures
                if "links" not in db_dict:
                    db_dict["links"] = {}
                if link_id not in db_dict["links"]:
                    db_dict["links"][link_id] = {}
                db_dict["links"][link_id]["link_id"] = link_id

                # Set previously parsed values
                try:
                    db_dict["links"][link_id]["type"] = link_type
                except Exception:
                    pass

                # Create topology dict under link_id
                if "topologies" not in db_dict["links"][link_id]:
                    db_dict["links"][link_id]["topologies"] = {}
                if mt_id not in db_dict["links"][link_id]["topologies"]:
                    db_dict["links"][link_id]["topologies"][mt_id] = {}
                db_dict["links"][link_id]["topologies"][mt_id]["mt_id"] = mt_id
                continue

            # (Link ID) Designated Router address: 10.166.7.6
            m = p19_2.match(line)
            if m:
                link_id = str(m.groupdict()["link_id"])

                # Create dict structures
                if "links" not in db_dict:
                    db_dict["links"] = {}
                if link_id not in db_dict["links"]:
                    db_dict["links"][link_id] = {}
                db_dict["links"][link_id]["link_id"] = link_id

                # Set previously parsed values
                try:
                    db_dict["links"][link_id]["type"] = link_type
                except Exception:
                    pass

                # Create topology dict under link_id
                if "topologies" not in db_dict["links"][link_id]:
                    db_dict["links"][link_id]["topologies"] = {}
                if mt_id not in db_dict["links"][link_id]["topologies"]:
                    db_dict["links"][link_id]["topologies"][mt_id] = {}
                db_dict["links"][link_id]["topologies"][mt_id]["mt_id"] = mt_id
                continue

            # (Link ID) Neighboring Router ID: 10.151.22.22
            m = p19_3.match(line)
            if m:
                link_id = str(m.groupdict()["link_id"])

                # Create dict structures
                if "links" not in db_dict:
                    db_dict["links"] = {}
                if link_id not in db_dict["links"]:
                    db_dict["links"][link_id] = {}
                db_dict["links"][link_id]["link_id"] = link_id

                # Set previously parsed values
                try:
                    db_dict["links"][link_id]["type"] = link_type
                except Exception:
                    pass

                # Create topology dict under link_id
                if "topologies" not in db_dict["links"][link_id]:
                    db_dict["links"][link_id]["topologies"] = {}
                if mt_id not in db_dict["links"][link_id]["topologies"]:
                    db_dict["links"][link_id]["topologies"][mt_id] = {}
                db_dict["links"][link_id]["topologies"][mt_id]["mt_id"] = mt_id
                continue

            # (Link Data) Network Mask: 255.255.255.255
            m = p20_1.match(line)
            if m:
                db_dict["links"][link_id]["link_data"] = str(m.groupdict()["link_data"])
                continue

            # (Link Data) Router Interface address: 10.166.7.6
            m = p20_2.match(line)
            if m:
                db_dict["links"][link_id]["link_data"] = str(m.groupdict()["link_data"])
                continue

            # Number of TOS metrics: 0
            m = p21.match(line)
            if m:
                db_dict["links"][link_id]["num_tos_metrics"] = int(m.groupdict()["num"])
                continue

            # Opaque Type: 1
            m = p22.match(line)
            if m:
                opaque_type = int(m.groupdict()["type"])
                continue

            # Opaque ID: 38
            m = p23.match(line)
            if m:
                opaque_id = int(m.groupdict()["id"])
                continue

            # Fragment number: 0
            m = p24.match(line)
            if m:
                header_dict["fragment_number"] = int(m.groupdict()["num"])
                continue

            # MPLS TE router ID : 10.4.1.1
            m = p25.match(line)
            if m:
                header_dict["mpls_te_router_id"] = str(m.groupdict()["mpls"])
                continue

            # AS Boundary Router
            m = p26_1.match(line)
            if m:
                header_dict["as_boundary_router"] = True
                continue

            # Area Border Router
            m = p26_2.match(line)
            if m:
                header_dict["area_border_router"] = True
                continue

            # Link connected to Broadcast network
            m = p27.match(line)
            if m:
                tlv_idx = len(db_dict.get("link_tlvs", {})) + 1
                tlv_dict = db_dict.setdefault("link_tlvs", {}).setdefault(tlv_idx, {})

                # Set link type
                opaque_link = m.groupdict()["link"].lower()
                if opaque_link == "broadcast network":
                    opaque_link_type = 2
                else:
                    opaque_link_type = 1
                tlv_dict["link_type"] = opaque_link_type
                tlv_dict["link_name"] = opaque_link

                # Set remote_if_ipv4_addrs (if needed)
                if opaque_link_type == 2:
                    if_dict = tlv_dict.setdefault("remote_if_ipv4_addrs", {})
                    if_dict["remote_if_ipv4_addr"] = "0.0.0.0"

                # Reset index for sub_tlv
                is_sub_tlv = False
                sub_tlv_idx = 0
                continue

            # Link ID : 10.1.4.4
            m = p28.match(line)
            if m:
                tlv_dict["link_id"] = m.groupdict()["id"]
                continue

            # Interface Address : 10.1.4.1
            m = p29.match(line)
            if m:
                addr = m.groupdict()["addr"]
                tlv_dict.setdefault("local_if_ipv4_addrs", {}).setdefault(addr, {})
                continue

            # Admin Metric : 1
            m = p30.match(line)
            if m:
                tlv_dict["te_metric"] = int(m.groupdict()["te_metric"])
                continue

            # Maximum Bandwidth : 125000000
            # Maximum bandwidth : 125000000
            m = p31.match(line)
            if m:
                tlv_dict["max_bandwidth"] = int(m.groupdict()["max_band"])
                continue

            # Maximum reservable bandwidth : 93750000
            # Maximum reservable bandwidth global: 93750000
            m = p32.match(line)
            if m:
                tlv_dict["max_reservable_bandwidth"] = int(
                    m.groupdict()["max_res_band"]
                )
                continue

            # Affinity Bit : 0x0
            m = p33.match(line)
            if m:
                tlv_dict["admin_group"] = m.groupdict()["admin_group"]
                continue

            # IGP Metric : 1
            m = p33_1.match(line)
            if m:
                tlv_dict["igp_metric"] = int(m.groupdict()["igp_metric"])
                continue

            # Number of Priority : 8
            m = p33_2.match(line)
            if m:
                tlv_dict["total_priority"] = int(m.groupdict()["num"])
                continue

            # Priority 0 : 93750000    Priority 1 : 93750000
            m = p34.match(line)
            if m:
                value1 = m.groupdict()["num1"] + " " + m.groupdict()["band1"]
                value2 = m.groupdict()["num2"] + " " + m.groupdict()["band2"]
                unres_dict = tlv_dict.setdefault("unreserved_bandwidths", {})

                v1_dict = unres_dict.setdefault(value1, {})
                v1_dict["priority"] = int(m.groupdict()["num1"])
                v1_dict["unreserved_bandwidth"] = int(m.groupdict()["band1"])

                v2_dict = unres_dict.setdefault(value2, {})
                v2_dict["priority"] = int(m.groupdict()["num2"])
                v2_dict["unreserved_bandwidth"] = int(m.groupdict()["band2"])
                continue

            # Unknown Sub-TLV   :  Type = 32770, Length = 4 Value = 00 00 00 01
            m = p35.match(line)
            if m:
                unknown_tlvs_counter += 1
                unknown_dict = tlv_dict.setdefault("unknown_tlvs", {}).setdefault(
                    unknown_tlvs_counter, {}
                )

                unknown_dict["type"] = int(m.groupdict()["type"])
                unknown_dict["length"] = int(m.groupdict()["length"])
                unknown_dict["value"] = m.groupdict()["value"]
                continue

            # Extended Administrative Group : Length: 8
            m = p36.match(line)
            if m:
                ext_dict = tlv_dict.setdefault("extended_admin_group", {})
                ext_dict["length"] = int(m.groupdict()["eag_length"])
                continue

            # EAG[0]: 0
            m = p37.match(line)
            if m:
                group_num = int(m.groupdict()["group_num"])
                gr_dict = ext_dict.setdefault("groups", {}).setdefault(group_num, {})
                gr_dict["value"] = int(m.groupdict()["val"])
                continue

            # Router Information TLV: Length: 4
            m = p38.match(line)
            if m:
                tlv_idx = len(db_dict.get("router_capabilities_tlv", {})) + 1
                tlv_dict = db_dict.setdefault("router_capabilities_tlv", {}).setdefault(
                    tlv_idx, {}
                )
                tlv_dict["length"] = int(m.groupdict()["length"])

                # Reset index for sub_tlv
                is_sub_tlv = False
                sub_tlv_idx = 0
                continue

            # Capabilities:
            #   Graceful Restart Helper Capable
            m = p39.match(line)
            if m:
                info_dict = tlv_dict.setdefault("information_capabilities", {})
                info_dict["graceful_restart_helper"] = True
                continue

            #   Stub Router Capable
            m = p40.match(line)
            if m:
                info_dict = tlv_dict.setdefault("information_capabilities", {})
                info_dict["stub_router"] = True
                continue

            #   All capability bits: 0x60000000
            m = p41.match(line)
            if m:
                info_dict = tlv_dict.setdefault("information_capabilities", {})
                info_dict["capability_bits"] = m.groupdict()["bits"]
                continue

            # Segment Routing Algorithm TLV: Length: 2
            m = p42.match(line)
            if m:
                tlv_idx = len(db_dict.get("sr_algorithm_tlv", {})) + 1
                tlv_dict = db_dict.setdefault("sr_algorithm_tlv", {}).setdefault(
                    tlv_idx, {}
                )
                tlv_dict["length"] = int(m.groupdict()["length"])

                # Reset index for sub_tlv
                is_sub_tlv = False
                sub_tlv_idx = 0
                continue

            #   Algorithm: 0
            #   Algorithm: 1
            m = p43.match(line)
            if m:
                algo = tlv_dict.setdefault("algorithm", {})
                algo.update({m.groupdict()["algo"]: True})
                continue

            # Segment Routing Range TLV: Length: 12
            m = p44.match(line)
            if m:
                tlv_idx = len(db_dict.get("sid_range_tlvs", {})) + 1
                tlv_dict = db_dict.setdefault("sid_range_tlvs", {}).setdefault(
                    tlv_idx, {}
                )
                tlv_dict["length"] = int(m.groupdict()["length"])
                tlv_dict["tlv_type"] = "Segment Routing Range"

                # Reset index for sub_tlv
                is_sub_tlv = False
                sub_tlv_idx = 0
                continue

            #   Range Size: 65535
            m = p45.match(line)
            if m:
                tlv_dict["range_size"] = int(m.groupdict()["range_size"])
                continue

            #     SID sub-TLV: Length 3
            #     SID sub-TLV: Length: 8
            m = p46.match(line)
            if m:
                group = m.groupdict()
                sub_tlv_idx += 1
                sub_tlv_dict = tlv_dict.setdefault("sub_tlvs", {}).setdefault(
                    sub_tlv_idx, {}
                )

                is_sub_tlv = True
                sub_tlv_dict["length"] = int(group["length"])
                sub_tlv_dict["type"] = group["type"]
                continue

            #      Label: 16000
            m = p47.match(line)
            if m:
                if is_sub_tlv:
                    tmp = sub_tlv_dict
                else:
                    tmp = tlv_dict

                tmp["label"] = int(m.groupdict()["label"])
                continue

            # Node MSD TLV: Length: 2
            m = p48.match(line)
            if m:
                tlv_idx = len(db_dict.get("node_msd_tlvs", {})) + 1
                tlv_dict = db_dict.setdefault("node_msd_tlvs", {}).setdefault(
                    tlv_idx, {}
                )
                tlv_dict["length"] = int(m.groupdict()["length"])

                # Reset index for sub_tlv
                is_sub_tlv = False
                sub_tlv_idx = 0
                continue

            #     Type: 1, Value 10
            m = p49.match(line)
            if m:
                # check if is sub_tlv
                if is_sub_tlv:
                    tmp = sub_tlv_dict
                else:
                    tmp = tlv_dict

                tmp["node_type"] = int(m.groupdict()["type"])
                tmp["value"] = int(m.groupdict()["value"])
                continue

            # Segment Routing Local Block TLV: Length: 12
            m = p50.match(line)
            if m:
                tlv_idx = len(db_dict.get("local_block_tlvs", {})) + 1
                tlv_dict = db_dict.setdefault("local_block_tlvs", {}).setdefault(
                    tlv_idx, {}
                )
                tlv_dict["length"] = int(m.groupdict()["length"])

                # Reset index for sub_tlv
                is_sub_tlv = False
                sub_tlv_idx = 0
                continue

            # Extended Prefix Range TLV: Length: 24
            # Extended Prefix TLV: Length: 24
            m = p51.match(line)
            if m:
                tlv_idx = len(db_dict.get("extended_prefix_tlvs", {})) + 1
                tlv_dict = db_dict.setdefault("extended_prefix_tlvs", {}).setdefault(
                    tlv_idx, {}
                )
                tlv_dict["length"] = int(m.groupdict()["length"])

                # Reset index for sub_tlv
                is_sub_tlv = False
                sub_tlv_idx = 0
                continue

            #   AF   : 0
            m = p52.match(line)
            if m:
                tlv_dict["af"] = int(m.groupdict()["af"])
                continue

            #   Prefix    : 10.246.254.0/32
            m = p53.match(line)
            if m:
                tlv_dict["prefix"] = m.groupdict()["prefix"]
                continue

            #   Flags     : 0x0
            m = p54.match(line)
            if m:
                # check if is sub_tlv
                if is_sub_tlv:
                    tmp = sub_tlv_dict
                else:
                    tmp = tlv_dict

                tmp["flags"] = m.groupdict()["flags"]
                continue

            #     MTID      : 0
            m = p55.match(line)
            if m:
                sub_tlv_dict["mt_id"] = m.groupdict()["mt_id"]
                continue

            #     Algo      : 0
            m = p56.match(line)
            if m:
                # check if is sub_tlv
                sub_tlv_dict["algo"] = int(m.groupdict()["algo"])
                continue

            #     SID Index : 1028
            m = p57.match(line)
            if m:
                sub_tlv_dict["sid"] = int(m.groupdict()["sid_index"])
                continue

            # Extended Link TLV: Length: 76
            m = p58.match(line)
            if m:
                tlv_idx = len(db_dict.get("extended_link_tlvs", {})) + 1
                tlv_dict = db_dict.setdefault("extended_link_tlvs", {}).setdefault(
                    tlv_idx, {}
                )
                tlv_dict["length"] = int(m.groupdict()["length"])

                # Reset index for sub_tlv
                is_sub_tlv = False
                sub_tlv_idx = 0
                continue

            #   Link-type : 1
            m = p59.match(line)
            if m:
                tlv_dict["link_type"] = int(m.groupdict()["link_type"])
                continue

            #   Link Data : 172.16.0.91
            m = p60.match(line)
            if m:
                tlv_dict["link_data"] = m.groupdict()["link_data"]
                continue

            #     Weight    : 0
            m = p61.match(line)
            if m:
                sub_tlv_dict["weight"] = int(m.groupdict()["weight"])
                continue

            #     Local Interface ID: 78
            m = p62.match(line)
            if m:
                sub_tlv_dict["local_interface_id"] = int(m.groupdict()["local_id"])
                continue

            #     Remote Interface ID: 76
            m = p63.match(line)
            if m:
                sub_tlv_dict["remote_interface_id"] = int(m.groupdict()["remote_id"])
                continue

            #     Neighbor Address: 172.16.0.90
            m = p64.match(line)
            if m:
                if is_sub_tlv:
                    tmp = sub_tlv_dict
                else:
                    tmp = tlv_dict
                tmp["neighbor_address"] = m.groupdict()["nbr_addr"]
                continue

        return ret_dict


# ========================================================
# Schema for 'show ospf vrf all-inclusive database router'
# ========================================================
class ShowOspfVrfAllInclusiveDatabaseRouterSchema(MetaParser):
    """Schema for show ospf vrf all-inclusive database router"""

    schema = {
        "vrf": {
            Any(): {
                "address_family": {
                    Any(): {
                        "instance": {
                            Any(): {
                                Optional("areas"): {
                                    Any(): {
                                        "database": {
                                            "lsa_types": {
                                                Any(): {
                                                    "lsa_type": int,
                                                    "lsas": {
                                                        Any(): {
                                                            "lsa_id": str,
                                                            "adv_router": str,
                                                            "ospfv2": {
                                                                "header": {
                                                                    "option": str,
                                                                    "option_desc": str,
                                                                    "lsa_id": str,
                                                                    "age": int,
                                                                    "type": int,
                                                                    "adv_router": str,
                                                                    "seq_num": str,
                                                                    "checksum": str,
                                                                    "length": int,
                                                                    Optional(
                                                                        "routing_bit_enable"
                                                                    ): bool,
                                                                    Optional(
                                                                        "as_boundary_router"
                                                                    ): bool,
                                                                    Optional(
                                                                        "area_border_router"
                                                                    ): bool,
                                                                },
                                                                "body": {
                                                                    "router": {
                                                                        Optional(
                                                                            "flags"
                                                                        ): str,
                                                                        "num_of_links": int,
                                                                        "links": {
                                                                            Any(): {
                                                                                "link_id": str,
                                                                                "link_data": str,
                                                                                "type": str,
                                                                                "num_tos_metrics": int,
                                                                                "topologies": {
                                                                                    Any(): {
                                                                                        "mt_id": int,
                                                                                        Optional(
                                                                                            "metric"
                                                                                        ): int,
                                                                                        Optional(
                                                                                            "tos"
                                                                                        ): int,
                                                                                    },
                                                                                },
                                                                            },
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }


# ========================================================
# Parser for 'show ospf vrf all-inclusive database router'
# ========================================================
class ShowOspfVrfAllInclusiveDatabaseRouter(
    ShowOspfVrfAllInclusiveDatabaseRouterSchema, ShowOspfVrfAllInclusiveDatabaseParser
):
    """
    Parser for show ospf vrf all-inclusive database router
    For checking any output with the parser ,below mandatory key(s) are needed and have to be in cli command.

    - db_type
    """

    cli_command = [
        "show ospf vrf all-inclusive database router",
        "show ospf vrf {vrf} database router",
    ]
    exclude = ["age"]

    def cli(self, vrf="", output=None):
        if vrf:
            cmd = self.cli_command[1].format(vrf=vrf)
        else:
            cmd = self.cli_command[0]
        return super().cli(cmd=cmd, db_type="router", output=output)


# ==========================================================
# Schema for 'show ospf vrf all-inclusive database external'
# ==========================================================
class ShowOspfVrfAllInclusiveDatabaseExternalSchema(MetaParser):
    """Schema for show ospf vrf all-inclusive database external"""

    schema = {
        "vrf": {
            Any(): {
                "address_family": {
                    Any(): {
                        "instance": {
                            Any(): {
                                Optional("areas"): {
                                    Any(): {
                                        "database": {
                                            "lsa_types": {
                                                Any(): {
                                                    "lsa_type": int,
                                                    "lsas": {
                                                        Any(): {
                                                            "lsa_id": str,
                                                            "adv_router": str,
                                                            "ospfv2": {
                                                                "header": {
                                                                    "option": str,
                                                                    "option_desc": str,
                                                                    "lsa_id": str,
                                                                    "age": int,
                                                                    "type": int,
                                                                    "adv_router": str,
                                                                    "seq_num": str,
                                                                    "checksum": str,
                                                                    "length": int,
                                                                    Optional(
                                                                        "routing_bit_enable"
                                                                    ): bool,
                                                                },
                                                                "body": {
                                                                    "external": {
                                                                        "network_mask": str,
                                                                        "topologies": {
                                                                            Any(): {
                                                                                "mt_id": int,
                                                                                "tos": int,
                                                                                Optional(
                                                                                    "flags"
                                                                                ): str,
                                                                                "metric": int,
                                                                                "forwarding_address": str,
                                                                                "external_route_tag": int,
                                                                            },
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }


# ==========================================================
# Parser for 'show ospf vrf all-inclusive database external'
# ==========================================================
class ShowOspfVrfAllInclusiveDatabaseExternal(
    ShowOspfVrfAllInclusiveDatabaseExternalSchema, ShowOspfVrfAllInclusiveDatabaseParser
):
    """
    Parser for show ospf vrf all-inclusive database external
    For checking any output with the parser ,below mandatory key(s) are needed and have to be in cli command.

    - db_type
    """

    cli_command = [
        "show ospf vrf all-inclusive database external",
        "show ospf vrf {vrf} database external",
    ]
    exclude = ["age", "checksum", "seq_num"]

    def cli(self, vrf="", output=None):
        if vrf:
            cmd = self.cli_command[1].format(vrf=vrf)
        else:
            cmd = self.cli_command[0]
        return super().cli(cmd=cmd, db_type="external", output=output)


# =========================================================
# Schema for 'show ospf vrf all-inclusive database network'
# =========================================================
class ShowOspfVrfAllInclusiveDatabaseNetworkSchema(MetaParser):
    """Schema for show ospf vrf all-inclusive database network"""

    schema = {
        "vrf": {
            Any(): {
                "address_family": {
                    Any(): {
                        "instance": {
                            Any(): {
                                Optional("areas"): {
                                    Any(): {
                                        "database": {
                                            "lsa_types": {
                                                Any(): {
                                                    "lsa_type": int,
                                                    "lsas": {
                                                        Any(): {
                                                            "lsa_id": str,
                                                            "adv_router": str,
                                                            "ospfv2": {
                                                                "header": {
                                                                    "option": str,
                                                                    "option_desc": str,
                                                                    "lsa_id": str,
                                                                    "age": int,
                                                                    "type": int,
                                                                    "adv_router": str,
                                                                    "seq_num": str,
                                                                    "checksum": str,
                                                                    "length": int,
                                                                    Optional(
                                                                        "routing_bit_enable"
                                                                    ): bool,
                                                                },
                                                                "body": {
                                                                    "network": {
                                                                        "network_mask": str,
                                                                        "attached_routers": {
                                                                            Any(): {},
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }


# ==========================================================
# Parser for 'show ospf vrf all-inclusive database network'
# ==========================================================
class ShowOspfVrfAllInclusiveDatabaseNetwork(
    ShowOspfVrfAllInclusiveDatabaseNetworkSchema, ShowOspfVrfAllInclusiveDatabaseParser
):
    """
    Parser for show ospf vrf all-inclusive database network
    For checking any output with the parser ,below mandatory key(s) are needed and have to be in cli command.

    - db_type
    """

    cli_command = [
        "show ospf vrf all-inclusive database network",
        "show ospf vrf {vrf} database network",
    ]
    exclude = ["age", "checksum", "seq_num"]

    def cli(self, vrf="", output=None):
        if vrf:
            cmd = self.cli_command[1].format(vrf=vrf)
        else:
            cmd = self.cli_command[0]
        return super().cli(cmd=cmd, db_type="network", output=output)


# =========================================================
# Schema for 'show ospf vrf all-inclusive database summary'
# =========================================================
class ShowOspfVrfAllInclusiveDatabaseSummarySchema(MetaParser):
    """Schema for show ospf vrf all-inclusive database summary"""

    schema = {
        "vrf": {
            Any(): {
                "address_family": {
                    Any(): {
                        "instance": {
                            Any(): {
                                Optional("areas"): {
                                    Any(): {
                                        "database": {
                                            "lsa_types": {
                                                Any(): {
                                                    "lsa_type": int,
                                                    "lsas": {
                                                        Any(): {
                                                            "lsa_id": str,
                                                            "adv_router": str,
                                                            "ospfv2": {
                                                                "header": {
                                                                    "option": str,
                                                                    "option_desc": str,
                                                                    "lsa_id": str,
                                                                    "age": int,
                                                                    "type": int,
                                                                    "adv_router": str,
                                                                    "seq_num": str,
                                                                    "checksum": str,
                                                                    "length": int,
                                                                    Optional(
                                                                        "routing_bit_enable"
                                                                    ): bool,
                                                                },
                                                                "body": {
                                                                    "summary": {
                                                                        "network_mask": str,
                                                                        "topologies": {
                                                                            Any(): {
                                                                                "mt_id": int,
                                                                                "tos": int,
                                                                                "metric": int,
                                                                            },
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }


# =========================================================
# Parser for 'show ospf vrf all-inclusive database summary'
# =========================================================
class ShowOspfVrfAllInclusiveDatabaseSummary(
    ShowOspfVrfAllInclusiveDatabaseSummarySchema, ShowOspfVrfAllInclusiveDatabaseParser
):
    """
    Parser for show ospf vrf all-inclusive database summary
    For checking any output with the parser ,below mandatory key(s) are needed and have to be in cli command.

    - db_type
    """

    cli_command = [
        "show ospf vrf all-inclusive database summary",
        "show ospf vrf {vrf} database summary",
    ]
    exclude = ["age", "checksum", "seq_num"]

    def cli(self, vrf="", output=None):
        if vrf:
            cmd = self.cli_command[1].format(vrf=vrf)
        else:
            cmd = self.cli_command[0]
        return super().cli(cmd=cmd, db_type="summary", output=output)


# =============================================================
# Schema for 'show ospf vrf all-inclusive database opaque-area'
# =============================================================
class ShowOspfVrfAllInclusiveDatabaseOpaqueAreaSchema(MetaParser):
    """Schema for show ospf vrf all-inclusive database opaque-area"""

    schema = {
        "vrf": {
            Any(): {
                "address_family": {
                    Any(): {
                        "instance": {
                            Any(): {
                                Optional("areas"): {
                                    Any(): {
                                        "database": {
                                            "lsa_types": {
                                                Any(): {
                                                    "lsa_type": int,
                                                    "lsas": {
                                                        Any(): {
                                                            "lsa_id": str,
                                                            "adv_router": str,
                                                            "ospfv2": {
                                                                "header": {
                                                                    "option": str,
                                                                    "option_desc": str,
                                                                    "lsa_id": str,
                                                                    "age": int,
                                                                    "type": int,
                                                                    "adv_router": str,
                                                                    "seq_num": str,
                                                                    "checksum": str,
                                                                    "length": int,
                                                                    "opaque_type": int,
                                                                    "opaque_id": int,
                                                                    Optional(
                                                                        "fragment_number"
                                                                    ): int,
                                                                    Optional(
                                                                        "mpls_te_router_id"
                                                                    ): str,
                                                                    Optional(
                                                                        "num_links"
                                                                    ): int,
                                                                },
                                                                "body": {
                                                                    "opaque": {
                                                                        Optional(
                                                                            "num_of_links"
                                                                        ): int,
                                                                        Optional(
                                                                            "link_tlvs"
                                                                        ): {
                                                                            Any(): {
                                                                                "link_type": int,
                                                                                "link_name": str,
                                                                                "link_id": str,
                                                                                "te_metric": int,
                                                                                "max_bandwidth": int,
                                                                                Optional(
                                                                                    "max_reservable_bandwidth"
                                                                                ): int,
                                                                                Optional(
                                                                                    "admin_group"
                                                                                ): str,
                                                                                Optional(
                                                                                    "igp_metric"
                                                                                ): int,
                                                                                Optional(
                                                                                    "total_priority"
                                                                                ): int,
                                                                                Optional(
                                                                                    "neighbor_address"
                                                                                ): str,
                                                                                Optional(
                                                                                    "local_if_ipv4_addrs"
                                                                                ): {
                                                                                    Any(): {}
                                                                                },
                                                                                Optional(
                                                                                    "remote_if_ipv4_addrs"
                                                                                ): {
                                                                                    Optional(
                                                                                        "remote_if_ipv4_addr"
                                                                                    ): Or(
                                                                                        str,
                                                                                        {},
                                                                                    )
                                                                                },
                                                                                Optional(
                                                                                    "unreserved_bandwidths"
                                                                                ): {
                                                                                    Any(): {
                                                                                        "priority": int,
                                                                                        "unreserved_bandwidth": int,
                                                                                    },
                                                                                },
                                                                                Optional(
                                                                                    "unknown_tlvs"
                                                                                ): {
                                                                                    Any(): {
                                                                                        "type": int,
                                                                                        "length": int,
                                                                                        "value": str,
                                                                                    },
                                                                                },
                                                                                Optional(
                                                                                    "extended_admin_group"
                                                                                ): {
                                                                                    "length": int,
                                                                                    Optional(
                                                                                        "groups"
                                                                                    ): {
                                                                                        Any(): {
                                                                                            "value": int,
                                                                                        },
                                                                                    },
                                                                                },
                                                                            },
                                                                        },
                                                                        Optional(
                                                                            "extended_link_tlvs"
                                                                        ): {
                                                                            Any(): {
                                                                                "length": int,
                                                                                "link_type": int,
                                                                                "link_id": str,
                                                                                "link_data": str,
                                                                                Optional(
                                                                                    "sub_tlvs"
                                                                                ): {
                                                                                    Any(): {
                                                                                        "length": int,
                                                                                        "type": str,
                                                                                        Optional(
                                                                                            "flags"
                                                                                        ): str,
                                                                                        Optional(
                                                                                            "mt_id"
                                                                                        ): str,
                                                                                        Optional(
                                                                                            "weight"
                                                                                        ): int,
                                                                                        Optional(
                                                                                            "label"
                                                                                        ): int,
                                                                                        Optional(
                                                                                            "local_interface_id"
                                                                                        ): int,
                                                                                        Optional(
                                                                                            "remote_interface_id"
                                                                                        ): int,
                                                                                        Optional(
                                                                                            "neighbor_address"
                                                                                        ): str,
                                                                                        Optional(
                                                                                            "node_type"
                                                                                        ): int,
                                                                                        Optional(
                                                                                            "value"
                                                                                        ): int,
                                                                                    },
                                                                                },
                                                                            },
                                                                        },
                                                                        Optional(
                                                                            "extended_prefix_tlvs"
                                                                        ): {
                                                                            Any(): {
                                                                                "length": int,
                                                                                Optional(
                                                                                    "af"
                                                                                ): int,
                                                                                Optional(
                                                                                    "prefix"
                                                                                ): str,
                                                                                Optional(
                                                                                    "range_size"
                                                                                ): int,
                                                                                Optional(
                                                                                    "flags"
                                                                                ): str,
                                                                                Optional(
                                                                                    "sub_tlvs"
                                                                                ): {
                                                                                    Any(): {
                                                                                        "length": int,
                                                                                        "type": str,
                                                                                        Optional(
                                                                                            "flags"
                                                                                        ): str,
                                                                                        Optional(
                                                                                            "mt_id"
                                                                                        ): str,
                                                                                        Optional(
                                                                                            "algo"
                                                                                        ): int,
                                                                                        Optional(
                                                                                            "sid"
                                                                                        ): int,
                                                                                    },
                                                                                },
                                                                            },
                                                                        },
                                                                        Optional(
                                                                            "router_capabilities_tlv"
                                                                        ): {
                                                                            Any(): {
                                                                                "length": int,
                                                                                Optional(
                                                                                    "information_capabilities"
                                                                                ): {
                                                                                    Optional(
                                                                                        "graceful_restart_helper"
                                                                                    ): bool,
                                                                                    Optional(
                                                                                        "stub_router"
                                                                                    ): bool,
                                                                                    Optional(
                                                                                        "capability_bits"
                                                                                    ): str,
                                                                                },
                                                                            },
                                                                        },
                                                                        Optional(
                                                                            "sr_algorithm_tlv"
                                                                        ): {
                                                                            Any(): {
                                                                                "length": int,
                                                                                Optional(
                                                                                    "algorithm"
                                                                                ): {
                                                                                    Any(): bool,
                                                                                },
                                                                            },
                                                                        },
                                                                        Optional(
                                                                            "sid_range_tlvs"
                                                                        ): {
                                                                            Any(): {
                                                                                "length": int,
                                                                                "tlv_type": str,
                                                                                "range_size": int,
                                                                                Optional(
                                                                                    "sub_tlvs"
                                                                                ): {
                                                                                    Any(): {
                                                                                        "length": int,
                                                                                        "type": str,
                                                                                        Optional(
                                                                                            "label"
                                                                                        ): int,
                                                                                    },
                                                                                },
                                                                            },
                                                                        },
                                                                        Optional(
                                                                            "node_msd_tlvs"
                                                                        ): {
                                                                            Any(): {
                                                                                "length": int,
                                                                                Optional(
                                                                                    "node_type"
                                                                                ): int,
                                                                                Optional(
                                                                                    "value"
                                                                                ): int,
                                                                            },
                                                                        },
                                                                        Optional(
                                                                            "local_block_tlvs"
                                                                        ): {
                                                                            Any(): {
                                                                                "length": int,
                                                                                Optional(
                                                                                    "range_size"
                                                                                ): int,
                                                                                Optional(
                                                                                    "sub_tlvs"
                                                                                ): {
                                                                                    Any(): {
                                                                                        "length": int,
                                                                                        "type": str,
                                                                                        Optional(
                                                                                            "label"
                                                                                        ): int,
                                                                                    },
                                                                                },
                                                                            },
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }


# =============================================================
# Parser for 'show ospf vrf all-inclusive database opaque-area'
# =============================================================
class ShowOspfVrfAllInclusiveDatabaseOpaqueArea(
    ShowOspfVrfAllInclusiveDatabaseOpaqueAreaSchema,
    ShowOspfVrfAllInclusiveDatabaseParser,
):
    """
    Parser for show ospf vrf all-inclusive database opaque-area
    For checking any output with the parser ,below mandatory key(s) are needed and have to be in cli command.

    - db_type

    """

    cli_command = [
        "show ospf vrf all-inclusive database opaque-area",
        "show ospf vrf {vrf} database opaque-area",
    ]
    exclude = ["age", "checksum", "seq_num"]

    def cli(self, vrf="", output=None):
        if vrf:
            cmd = self.cli_command[1].format(vrf=vrf)
        else:
            cmd = self.cli_command[0]
        return super().cli(cmd=cmd, db_type="opaque", output=output)


# =============================================================
# Schema for 'show ospf database', 'show ospf <process_id> database'
# =============================================================
class ShowOspfDatabaseSchema(MetaParser):
    """Schema for show ospf database, show ospf <process_id> database
    """
    schema = {
    'vrf': {
        Any(): {
            'address_family': {
                Any(): {
                    'instance': {
                        Any(): {
                            "router_id": str,
                            Optional('area'): {
                                Any(): {
                                    "area_id": int,
                                    'database': {
                                        'lsa_types': {
                                            Any(): {
                                                'lsa_type': int,
                                                'lsas': {
                                                    Any(): {
                                                        'adv_router': str,
                                                        'link_id': str,
                                                        'ospf': {
                                                            'header': {
                                                                'age': int,
                                                                'seq_num': str,
                                                                'checksum': str,
                                                                Optional('link_count'): int,
                                                                Optional('opaque_id'): int
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}


# =============================================================
#  Parser for 'show ospf database', 'show ospf <process_id> database'
# =============================================================
class ShowOspfDatabase(ShowOspfDatabaseSchema):
    """ Parser for show ospf database, show ospf <process_id> database
    """
    cli_command = ['show ospf database', 'show ospf {process_id} database']

    def cli(self, process_id=None, output=None):
        if not output:
            if process_id:
                output = self.device.execute(self.cli_command[1].format(process_id=process_id))
            else:
                output = self.device.execute(self.cli_command[0])


        # Init vars
        ret_dict = {}
        address_family = 'ipv4'

        #Lsa Types
        # 1: Router
        # 2: Network Link
        # 3: Summary
        # 3: Summary Network
        # 3: Summary Net
        # 4: Summary ASB
        # 5: Type-5 AS External
        # 8: Link (Type-8)
        # 9: Intra Area Prefix'
        # 10: Opaque Area

        lsa_type_mapping = {
            'router': 1,
            'net': 2,
            'summary': 3,
            'summary net': 3,
            'summary asb': 4,
            'external': 5,
            'link (type-8)': 8,
            'intra area prefix': 9,
            'type-10 opaque link area': 10
        }

        # Initializes the Python dictionary variable
        parsed_dict = {}

        #OSPF Router with ID (10.94.1.1) (Process ID mpls1)
        p1 = re.compile(r'^OSPF +Router +with +ID +\((?P<router_id>(\S+))\) '
                        r'+\(Process +ID +(?P<instance>(\S+))(?:, +VRF +(?P<vrf>(\S+)))?\)$')

        #Router Link States (Area 0)
        #Type-10 Opaque Link Area Link States (Area 0)
        p2 = re.compile(r'^(?P<lsa_type>([a-zA-Z0-9\s\D]+)) +Link +States +\(Area'
                        ' +(?P<area>(\S+))\)$')

        #10.94.1.1       10.94.1.1       86          0x800080ff 0x0043de 5
        p3 = re.compile(
            "^(?P<link_id>[\w\.]+)\s+(?P<adv_router>[\w\.]+)\s+(?P<age>[\w]+)\s+"
            "(?P<seq_num>[\w]+)\s+(?P<checksum>[\w]+)\s(?P<link_count>[\w]+)$")

        #10.1.0.0         10.94.1.1       54          0x8003b136     0x009cb2        0
        p4 = re.compile(
            "^(?P<link_id>[\w\.]+)\s+(?P<adv_router>[\w\.]+)\s+(?P<age>[\w]+)"
            "\s+(?P<seq_num>[\w]+)\s+(?P<checksum>[\w]+)\s+(?P<opaque_id>[\w]+)$")


        for line in output.splitlines():
            line = line.strip()

            # OSPF Router with ID (10.94.1.1) (Process ID mpls1)
            m = p1.match(line)

            if m:
                group = m.groupdict()
                router_id = group['router_id']
                instance = group['instance']
                if group['vrf']:
                    vrf = group['vrf']
                else:
                    vrf = 'default'

                # Create dict
                ospf_dict = ret_dict.setdefault('vrf', {}). \
                    setdefault(vrf, {}). \
                    setdefault('address_family', {}). \
                    setdefault(address_family, {}). \
                    setdefault('instance', {}). \
                    setdefault(instance, {})
                continue


            # Router Link States (Area 0)
            # Type-10 Opaque Link Area Link States (Area 0)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                lsa_type_key = group['lsa_type'].lower()
                if lsa_type_key in lsa_type_mapping:
                    lsa_type = lsa_type_mapping[lsa_type_key]
                else:
                    continue

                # Set area
                if group['area']:
                    try:
                        int(group['area'])
                        area = str(IPAddress(str(group['area'])))
                    except Exception:
                        area = str(group['area'])
                else:
                    area = '0.0.0.0'

                ospf_dict['router_id'] = router_id
                area_dict = ospf_dict.setdefault('area', {}). \
                    setdefault(area, {})
                area_dict['area_id'] = int(group['area'])

                lsa_type_dict = area_dict.setdefault('database', {}). \
                    setdefault('lsa_types', {}). \
                    setdefault(lsa_type, {})

                # Set lsa_type
                lsa_type_dict['lsa_type'] = lsa_type
                continue


            #To process the router link states
            # 10.94.1.1       10.94.1.1       86          0x800080ff 0x0043de 5
            m = p3.match(line)
            if m:
                group = m.groupdict()
                link_id = group['link_id']
                adv_router = group['adv_router']
                age = int(group['age'])
                seq = group['seq_num']
                checksum = group['checksum']
                link_count = group['link_count']
                linkid_advrouter = link_id + " " + adv_router

                # Create lsas dict
                lsas_dict = lsa_type_dict.setdefault('lsas', {}). \
                    setdefault(linkid_advrouter, {})
                lsas_dict['adv_router'] = adv_router
                lsas_dict['link_id'] = link_id

                # osfpv2 dict
                ospfv2_dict = lsas_dict.setdefault('ospf', {}). \
                    setdefault('header', {})
                ospfv2_dict['age'] = age
                ospfv2_dict['seq_num'] = seq
                ospfv2_dict['checksum'] = group['checksum']
                ospfv2_dict['link_count'] = int(group['link_count'])
                continue

            # To process the type_10_opaque_link_states
            # 10.1.0.0         10.94.1.1       54          0x8003b136 0x009cb2        0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                link_id = group['link_id']
                adv_router = group['adv_router']
                age = int(group['age'])
                seq = group['seq_num']
                checksum = group['checksum']
                link_count = group['opaque_id']
                linkid_advrouter = link_id + " " + adv_router

                # Create lsas dict
                lsas_dict = lsa_type_dict.setdefault('lsas', {}). \
                    setdefault(linkid_advrouter, {})
                lsas_dict['adv_router'] = adv_router
                lsas_dict['link_id'] = link_id

                # osfpv2 dict
                ospfv2_dict = lsas_dict.setdefault('ospf', {}). \
                    setdefault('header', {})
                ospfv2_dict['age'] = age
                ospfv2_dict['seq_num'] = seq
                ospfv2_dict['checksum'] = group['checksum']
                ospfv2_dict['opaque_id'] = int(group['opaque_id'])
                continue

        return ret_dict


class ShowOspfDatabaseRouter(ShowOspfVrfAllInclusiveDatabaseParser, ShowOspfVrfAllInclusiveDatabaseRouterSchema):
    """Parser for show ospf database router"""
    cli_command = ['show ospf {process_id} database router', 'show ospf all-inclusive database router']

    def cli(self, process_id=None, output=None):
        if process_id:
            output = self.device.execute(self.cli_command[0].format(process_id=process_id))
        else:
            output = self.device.execute(self.cli_command[1])

        ret_dict = super().cli(cmd=output, db_type="router", output=None)

        return ret_dict


# ======================================================
# schema for:
#   * show ospf neighbor
#   * show ospf {process_name} neighbor
#   * show ospf vrf {vrf} neighbor
#   * show ospf {process} vrf {vrf} neighbor
# ======================================================
class ShowOspfNeighborSchema(MetaParser):
    """Schema detail for:
          * show ospf neighbor
          * show ospf {process_name} neighbor
          * show ospf vrf {vrf} neighbor
          * show ospf {process} vrf {vrf} neighbor
     """
    schema = {
        Optional('process_name'): str,
        'vrfs': {
            Any(): {
                'neighbors': {
                    Optional(Any()): {  # neighbor_id
                        'priority': str,
                        'state': str,
                        'dead_time': str,
                        'address': str,
                        'interface': str,
                        'up_time': str
                    }
                },
                Optional('total_neighbor_count'): int
            }
        }
    }


# ======================================================
# parser for:
#   * show ospf neighbor
#   * show ospf {process_name} neighbor
#   * show ospf vrf {vrf} neighbor
#   * show ospf {process} vrf {vrf} neighbor
# ======================================================
class ShowOspfNeighbor(ShowOspfNeighborSchema):
    """parser details for:
        * show ospf neighbor
        * show ospf {process_name} neighbor
        * show ospf vrf {vrf} neighbor
        * show ospf {process} vrf {vrf} neighbor
    """

    cli_command = ['show ospf neighbor', 'show ospf {process_name} neighbor',
                   'show ospf vrf {vrf} neighbor', 'show ospf {process_name} vrf {vrf} neighbor']

    def cli(self, process_name='', vrf='', output=None):
        if output is None:
            if process_name and vrf:
                out = self.device.execute(
                    self.cli_command[3].format(process_name=process_name, vrf=vrf))
            elif process_name:
                out = self.device.execute(
                    self.cli_command[1].format(process_name=process_name))
            elif vrf:
                out = self.device.execute(
                    self.cli_command[2].format(vrf=vrf))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        ret_dict = {}


        # Neighbors for OSPF
        p1 = re.compile(r'^Neighbors +for +OSPF')
        # Neighbors for OSPFv3 mpls1
        p1_1 = re.compile(r'^Neighbors +for +OSPF\w* +(?P<process_name>\w+)$')
        # Neighbors for OSPFv3 mpls1, VRF 1
        p1_2 = re.compile(r'Neighbors +for +OSPF\w* +(?P<process_name>\w+), VRF +(?P<vrf>\S+)')

        # Neighbor ID     Pri   State           Dead Time   Address         Interface
        # 100.100.100.100 1     FULL/  -        00:00:38    100.10.0.2      GigabitEthernet0/0/0/0
        # 95.95.95.95     1     FULL/  -        00:00:38    100.20.0.2      GigabitEthernet0/0/0/1
        # 192.168.199.137 1    FULL/DR       0:00:31    172.31.80.37      GigabitEthernet 0/3/0/2
        p2 = re.compile(r'^(?P<neighbor_id>\S+)\s+(?P<priority>\d+) +(?P<state>[A-Z]+/\s*[A-Z-]*)'
                        r' +(?P<dead_time>(\d+:){2}\d+) +(?P<address>[\d\.\/]+) +(?P<interface>\w+\s*\S+)$')

        # Neighbor is up for 2d18h
        p3 = re.compile(r'^Neighbor +is +up +for +(?P<up_time>\S+)$')

        # Total neighbor count: 2
        p4 = re.compile(r'^Total +neighbor +count: +(?P<total_neighbor_count>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # Neighbors for OSPF
            m = p1.match(line)
            if m:
                # Neighbors for OSPFv3 mpls1
                m = p1_1.match(line)
                if m:
                    process_name = m.groupdict()['process_name']

                    ret_dict['process_name'] = process_name
                    vrfs_dict = ret_dict.setdefault('vrfs', {})

                    vrf_dict = vrfs_dict.setdefault('default', {})
                    neighbors_dict = vrf_dict.setdefault('neighbors', {})
                    continue

                # Neighbors for OSPFv3 mpls1, VRF 1
                m = p1_2.match(line)
                if m:
                    process_name = m.groupdict()['process_name']
                    vrf_name = m.groupdict()['vrf']

                    ret_dict['process_name'] = process_name
                    vrfs_dict = ret_dict.setdefault('vrfs', {})

                    vrf_dict = vrfs_dict.setdefault(vrf_name, {})
                    neighbors_dict = vrf_dict.setdefault('neighbors', {})
                    continue

                # Neighbors for OSPF
                vrfs_dict = ret_dict.setdefault('vrfs', {})
                if vrf:
                    vrf_dict = vrfs_dict.setdefault(vrf, {})
                else:
                    vrf_dict = vrfs_dict.setdefault('default', {})
                neighbors_dict = vrf_dict.setdefault('neighbors', {})

                continue

            # Neighbor ID     Pri   State           Dead Time   Address         Interface
            # 100.100.100.100 1     FULL/  -        00:00:38    100.10.0.2      GigabitEthernet0/0/0/0
            # 95.95.95.95     1     FULL/  -        00:00:38    100.20.0.2      GigabitEthernet0/0/0/1
            # 192.168.199.137 1    FULL/DR       0:00:31    172.31.80.37      GigabitEthernet 0/3/0/2
            m = p2.match(line)
            if m:
                neighbor_id = m.groupdict()['neighbor_id']
                priority = m.groupdict()['priority']
                state = m.groupdict()['state']
                dead_time = m.groupdict()['dead_time']
                address = m.groupdict()['address']
                interface = m.groupdict()['interface']

                neighbor_dict = neighbors_dict.setdefault(neighbor_id, {})

                neighbor_dict['priority'] = priority
                neighbor_dict['state'] = state
                neighbor_dict['dead_time'] = dead_time
                neighbor_dict['address'] = address
                neighbor_dict['interface'] = interface

                continue

            # Neighbor is up for 2d18h
            m = p3.match(line)
            if m:
                up_time = m.groupdict()['up_time']
                neighbor_dict['up_time'] = up_time

                continue

            # Total neighbor count: 2
            m = p4.match(line)
            if m:
                total_neighbor_count = m.groupdict()['total_neighbor_count']
                vrf_dict['total_neighbor_count'] = int(total_neighbor_count)

        return ret_dict


# ======================================================
# parser schema for:
#          * show ospf interface brief
# ======================================================
class ShowOspfInterfaceBriefSchema(MetaParser):
    """Schema details for:
          * show ospf interface  brief
    """
    schema = {
        'instance': {
            Any(): {
                'areas': {
                    Any(): {
                        'interfaces': {
                            Any(): {
                                "name": str,
                                "ip_address": str,
                                "process_id": str,
                                "state": str,
                                "area": str,
                                "cost": int,
                                "nbrs_f": int,
                                "nbrs_count": int
                            }
                        }
                    }
                }
            }
        }
    }

# ======================================================
# parser for:
#          * show ospf interface brief
# ======================================================
class ShowOspfInterfaceBrief(ShowOspfInterfaceBriefSchema):
    """parser details for:
         * show ospf interface brief
    """

    cli_command = ['show ospf interface brief']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        ret_dict = {}

        # Lo0                mpls1 0               17.17.17.17/32     1     LOOP  0/0
        p1 = re.compile(r'^(?P<interface>\S+) +(?P<pid>\S+) +(?P<area>\S+) +'
            r'(?P<ip_addr>\S+) +(?P<cost>[0-9]+) +(?P<state>\S+) +(?P<nbrs_count>[0-9]+)\/(?P<nbrs_f>[0-9]+).*$')

        for line in out.splitlines():
            
            # Lo0                mpls1 0               17.17.17.17/32     1     LOOP  0/0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                area = group['area']
                interface = group['interface']
                interface_dict = ret_dict.setdefault('instance', {}).\
                    setdefault('default', {}).\
                    setdefault('areas', {}).\
                    setdefault(area, {}).\
                    setdefault('interfaces', {}).\
                    setdefault(interface, {})
                interface_dict.update({
                    'name': interface,
                    'process_id': group['pid'],
                    'area': group['area'],
                    'ip_address': group['ip_addr'],
                    'state': group['state'],
                    'cost': int(group['cost']),
                    'nbrs_f': int(group['nbrs_f']),
                    'nbrs_count': int(group['nbrs_count'])
                })

        return ret_dict


# ======================================================
# parser schema for:
#          * show ospf interface
#          * show ospf interface <interface_name>
#          * show ospf <process_name> interface
#          * show ospf <process_name> interface <interface_name>
# ======================================================
class ShowOspfInterfaceSchema(MetaParser):
    """Schema details for:
          * show ospf interface
          * show ospf interface <interface_name>
          * show ospf <process_name> interface
          * show ospf <process_name> interface <interface_name>
    """
    schema = {
        "vrf": {
            Any(): {
                "address_family": {
                    Any(): {
                        "instance": {
                            Any(): {
                                Optional("interfaces"): {
                                    Any(): {
                                        "name": str,
                                        "enable": bool,
                                        "line_protocol": bool,
                                        "ip_address": str,
                                        "demand_circuit": bool,
                                        "process_id": str,
                                        "router_id": str,
                                        "interface_type": str,
                                        "area": str,
                                        "bfd": {
                                            "enable": bool,
                                            Optional("interval"): int,
                                            Optional("min_interval"): int,
                                            Optional("multiplier"): int,
                                            Optional("mode"): str,
                                        },
                                        Optional("label_stack"): {
                                            "primary_label": str,
                                            "backup_label": str,
                                            "srte_label": str,
                                        },
                                        Optional("forward_reference"): str,
                                        Optional("unnumbered"): bool,
                                        Optional("bandwidth"): int,
                                        Optional("nsf_enabled"): bool,
                                        Optional("treated_as_stub_host"): bool,
                                        Optional("sid"): str,
                                        Optional("strict_spf_sid"): str,
                                        Optional("cost"): int,
                                        Optional("transmit_delay"): int,
                                        Optional("state"): str,
                                        Optional("priority"): int,
                                        Optional("mtu"): int,
                                        Optional("max_pkt_sz"): int,
                                        Optional("dr_router_id"): str,
                                        Optional("dr_ip_addr"): str,
                                        Optional("bdr_router_id"): str,
                                        Optional("bdr_ip_addr"): str,
                                        Optional("hello_interval"): int,
                                        Optional("dead_interval"): int,
                                        Optional("wait_interval"): int,
                                        Optional("retransmit_interval"): int,
                                        Optional("passive"): bool,
                                        Optional("hello_timer"): str,
                                        Optional("index"): str,
                                        Optional("flood_queue_length"): int,
                                        Optional("next"): str,
                                        Optional("last_flood_scan_length"): int,
                                        Optional("max_flood_scan_length"): int,
                                        Optional(
                                            "last_flood_scan_time_msec"
                                        ): int,
                                        Optional(
                                            "max_flood_scan_time_msec"
                                        ): int,
                                        Optional("ls_ack_list"): str,
                                        Optional("ls_ack_list_length"): int,
                                        Optional("high_water_mark"): int,
                                        Optional("total_dcbitless_lsa"): int,
                                        Optional("donotage_lsa"): bool,
                                        Optional("statistics"): {
                                            Optional("adj_nbr_count"): int,
                                            Optional("nbr_count"): int,
                                            Optional(
                                                "num_nbrs_suppress_hello"
                                            ): int,
                                            Optional(
                                                "multi_area_intf_count"
                                            ): int,
                                        },
                                        Optional("neighbors"): {
                                            Any(): {
                                                Optional('bdr_router_id'): str,
                                                Optional('dr_router_id'): str,
                                                Optional('router_id'): str,
                                            }
                                        }
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }


# ======================================================
# parser for:
#          * show ospf interface
#          * show ospf interface <interface_name>
#          * show ospf <process_name> interface
#          * show ospf <process_name> interface <interface_name>
# ======================================================
class ShowOspfInterface(ShowOspfInterfaceSchema):
    """parser details for:
         * show ospf interface
         * show ospf interface <interface_name>
         * show ospf <process_name> interface
         * show ospf <process_name> interface <interface_name>
    """

    cli_command = ['show ospf interface',
                   'show ospf interface {interface_name}',
                   'show ospf {process_name} interface',
                   'show ospf {process_name} interface {interface_name}']

    def cli(self, process_name='', interface_name='', output=None):
        if output is None:
            if process_name and interface_name:
                out = self.device.execute(
                    self.cli_command[3].format(process_name=process_name, 
                                               interface_name=interface_name))
            elif interface_name:
                out = self.device.execute(
                    self.cli_command[1].format(interface_name=interface_name))
            elif process_name:
                out = self.device.execute(
                    self.cli_command[2].format(process_name=process_name))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        ret_dict = {}

        # initialization of vrf dict
        if out:
            vrfs_dict = ret_dict.setdefault('vrf', {})

        # Interfaces for OSPF mpls1
        p1 = re.compile(r'^Interfaces +for +OSPF +(?P<ospf_instance>\S+)$')

        # Interfaces for OSPF 1, VRF VRF1
        p2 = re.compile(r'^Interfaces +for +OSPF +(?P<ospf_instance>\S+), +VRF +(?P<vrf_name>\S+)$')

        # Loopback0 is up, line protocol is up
        p3 = re.compile(r'^(?P<interface>\S+) +is +(?P<interface_enable>unknown|up|down), +line +protocol +is +'
                        r'(?P<line_protocol>up|down)$')

        # Internet Address 10.36.3.3/32, Area 0
        p4 = re.compile(r'^Internet +Address +(?P<ip_address>(\d+.){3}\d+/\d+), +Area +(?P<area>\w+)')
        
        # Internet Address 25.97.1.1/32, Area 0, SID 0, Strict-SPF SID 0
        p4_1 = re.compile(r'^Internet +Address +(?P<ip_address>(\d+.){3}\d+/\d+), +Area +(?P<area>\w+), +SID +'
                          r'(?P<sid>\d+), +Strict-SPF +SID +(?P<strict_spf_sid>\d+)$')

        # Process ID 1, Router ID 10.36.3.3, Network Type LOOPBACK, Cost: 1
        p5 = re.compile(r'^Process +ID +(?P<process_id>\w+), +Router +ID +(?P<router_id>(\d+.){3}\d+), +'
                        r'Network +Type +(?P<interface_type>\w+), +Cost: +(?P<cost>\d+)$')

        # Transmit Delay is 1 sec, State BDR, Priority 1, MTU 1500, MaxPktSz 1500
        # Transmit Delay is 1 sec, State POINT_TO_POINT, MTU 1500, MaxPktSz 1500
        # Transmit Delay is 1 sec, State POINT_TO_POINT,
        p6 = re.compile(r'Transmit +Delay +is +(?P<transmit_delay>\d+) +sec, +State +(?P<state>\S+),'
                        r'((( +(Priority +(?P<priority>\w+),)|) +MTU +(?P<mtu>\d+), +MaxPktSz +(?P<max_pkt_sz>\d+))|)$')

        # Designated Router (ID) 10.64.4.4, Interface address 10.3.4.4
        p7 = re.compile(r'^Designated +(R|r)outer +\(ID\) +(?P<dr_router_id>(\S+)), +(I|i)nterface +(A|a)ddress +'
                        r'(?P<dr_ip_addr>(\S+))$')

        # Backup Designated router (ID) 10.36.3.3, Interface address 10.3.4.3
        p8 = re.compile(r'^Backup +(D|d)esignated +(R|r)outer +\(ID\) +(?P<bdr_router_id>(\S+)), +(I|i)nterface +'
                        r'(A|a)ddress +(?P<bdr_ip_addr>(\S+))$')

        # Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
        p9 = re.compile(r'^Timer +intervals +configured, +Hello +(?P<hello>(\d+)), +Dead +(?P<dead>(\d+)), +Wait +'
                        r'(?P<wait>(\d+)), +Retransmit +(?P<retransmit>(\d+))$')

        # Hello due in 00:00:07:171
        p10_1 = re.compile(r'^Hello +due +in +(?P<hello_timer>(\S+))$')
        
        # No Hellos (Passive interface)
        p10_2 = re.compile(r"^No +Hellos +\(Passive +interface\)$")

        # Index 1/1, flood queue length 0
        p11 = re.compile(r'^Index +(?P<index>(\S+)), +flood +queue +length +(?P<length>(\d+))$')

        # Next 0(0)/0(0)
        p12 = re.compile(r'^Next +(?P<next>(\S+))$')

        # Last flood scan length is 1, maximum is 3
        p13 = re.compile(r'^Last +flood +scan +length +is +(?P<num>(\d+)), +maximum +is +(?P<max>(\d+))$')

        # Last flood scan time is 0 msec, maximum is 0 msec
        p14 = re.compile(
            r'^Last +flood +scan +time +is +(?P<time1>(\d+)) +msec, +maximum +is +(?P<time2>(\d+)) +msec$')

        # LS Ack List: current length 0, high water mark 5
        p15 = re.compile(
            r'^LS +Ack +List: +(?P<ls_ack_list>(\S+)) +length +(?P<num>(\d+)), +high +water +mark +(?P<num2>(\d+))$')

        # Neighbor Count is 1, Adjacent neighbor count is 1
        p16 = re.compile(
            r'^Neighbor +Count +is +(?P<nbr_count>(\d+)), +Adjacent +neighbor +count +is +(?P<adj_nbr_count>(\d+))$')

        # Adjacent with neighbor 10.64.4.4  (Designated Router)
        # Adjacent with neighbor 10.16.2.2  (Backup Designated Router)
        # Adjacent with neighbor 101.3.3.3
        p17 = re.compile(r'^Adjacent +with +neighbor +(?P<neighbors_router_id>(\S+))')

        # Suppress hello for 0 neighbor(s)
        p18 = re.compile(r'^Suppress +hello +for +(?P<sup>(\d+)) +neighbor\(s\)$')

        # Multi-area interface Count is 0
        p19 = re.compile(r'^Multi-area +interface +Count +is +(?P<count>(\d+))$')

        # Label stack Primary label 0 Backup label 0 SRTE label 0
        p20 = re.compile(r'^Label stack +Primary +label +(?P<primary_label>\d+) +Backup +label +'
                         r'(?P<backup_label>\d+) +SRTE +label +(?P<srte_label>\d+)$')

        # Forward reference No, Unnumbered no,  Bandwidth 1000000
        p21 = re.compile(r'^Forward +reference +(?P<forward_reference>\w+), +Unnumbered +'
                         r'(?P<unnumbered_bool>\w+), +Bandwidth +(?P<bandwidth>\S+)$')

        # BFD enabled, BFD interval 150 msec, BFD multiplier 3, Mode: Default
        p22 = re.compile(r'^BFD enabled(?:, +BFD +interval +(?P<interval>(\d+)) +msec)?(?:, +BFD +multiplier +('
                         r'?P<multi>(\d+)))?(?:, +Mode: +(?P<mode>(\S+)))?$')

        # Non-Stop Forwarding (NSF) enabled
        p23 = re.compile(r'^Non-Stop +Forwarding +\(NSF\) +(?P<nsf_status>\w+)$')

        # Adjacent with neighbor 100.100.100.100
        p24 = re.compile(r'^Adjacent +with +neighbor +(?P<neighbors_dr_router_id>(\S+))$')

        # Configured as demand circuit
        p25 = re.compile(r'^Configured as demand circuit$')

        # Run as demand circuit.
        p26 = re.compile(r"^Run as demand circuit\.$")

        # DoNotAge LSA not allowed (Number of DCbitless LSA is 1).
        p27 = re.compile(r"^DoNotAge +LSA +not +allowed +\(Number +of +DCbitless +LSA +is +(?P<num>(\d+))\)\.$")

        # Loopback interface is treated as a stub Host
        p28 = re.compile(r'^Loopback +interface +is +treated +as +a +stub +Host$')

        for line in out.splitlines():
            line = line.strip()

            # Interfaces for OSPF mpls1
            m = p1.match(line)
            if m:
                ospf_instance = m.groupdict()['ospf_instance']

                # Interfaces for OSPF 1, VRF VRF1
                m_sub = p2.match(line)
                if m_sub:
                    vrf_name = m_sub.groupdict()['vrf_name']
                    vrf_dict = vrfs_dict.setdefault(vrf_name, {})
                else:  # if there is no vrf information following ospf instance, assign it to default vrf dict
                    vrf_dict = vrfs_dict.setdefault('default', {})

                # initialize vrf dict
                instance_dict = vrf_dict \
                    .setdefault('address_family', {}) \
                    .setdefault('ipv4', {}) \
                    .setdefault('instance', {})

                ospf_dict = instance_dict.setdefault(ospf_instance, {})
                continue

            # Loopback0 is up, line protocol is up
            m = p3.match(line)
            if m:
                interface = m.groupdict()['interface']
                interface_enable = m.groupdict()['interface_enable']
                line_protocol = m.groupdict()['line_protocol']

                interfaces_dict = ospf_dict.setdefault('interfaces', {})
                interface_dict = interfaces_dict.setdefault(interface, {})

                # initializing some keys
                interface_dict['name'] = interface
                interface_dict['demand_circuit'] = False
                interface_dict['enable'] = \
                    True if interface_enable == 'up' else False
                interface_dict['line_protocol'] = \
                    True if line_protocol == 'up' else False

                # initialize bfd state
                interface_dict.setdefault('bfd', {}).setdefault('enable', False)
                continue

            # Internet Address 10.36.3.3/32, Area 0
            m = p4.match(line)
            if m:
                ip_address = m.groupdict()['ip_address']
                area = m.groupdict()['area']

                interface_dict['ip_address'] = ip_address
                interface_dict['area'] = area

                # Internet Address 25.97.1.1/32, Area 0, SID 0, Strict-SPF SID 0
                m_sub = p4_1.match(line)
                if m_sub:
                    sid = m_sub.groupdict()['sid']
                    strict_spf_sid = m_sub.groupdict()['sid']

                    interface_dict['sid'] = sid
                    interface_dict['strict_spf_sid'] = strict_spf_sid
                continue

            # Process ID mpls1, Router ID 25.97.1.1, Network Type LOOPBACK, Cost: 1
            m = p5.match(line)
            if m:
                process_id = m.groupdict()['process_id']
                router_id = m.groupdict()['router_id']
                interface_type = m.groupdict()['interface_type']
                cost = m.groupdict()['cost']

                interface_dict['process_id'] = process_id
                interface_dict['router_id'] = router_id
                interface_dict['interface_type'] = interface_type
                interface_dict['process_id'] = process_id
                interface_dict['cost'] = int(cost)
                continue

            # Transmit Delay is 1 sec, State POINT_TO_POINT, MTU 1500, MaxPktSz 1500
            # Transmit Delay is 1 sec, State BDR, Priority 1, MTU 1500, MaxPktSz 1500
            # Transmit Delay is 1 sec, State POINT_TO_POINT,
            m = p6.match(line)
            if m:
                transmit_delay = m.groupdict()['transmit_delay']
                state = m.groupdict()['state']
                priority = m.groupdict().get('priority')
                mtu = m.groupdict()['mtu']
                max_pkt_sz = m.groupdict()['max_pkt_sz']

                interface_dict['transmit_delay'] = int(transmit_delay)
                interface_dict['state'] = state
                if priority:
                    interface_dict['priority'] = int(priority)
                if mtu:
                    interface_dict['mtu'] = int(mtu)
                if max_pkt_sz:
                    interface_dict['max_pkt_sz'] = int(max_pkt_sz)
                continue

            # Designated Router (ID) 10.64.4.4, Interface address 10.3.4.4
            m = p7.match(line)
            if m:
                dr_router_id = m.groupdict()['dr_router_id']
                dr_ip_addr = m.groupdict()['dr_ip_addr']

                interface_dict['dr_router_id'] = dr_router_id
                interface_dict['dr_ip_addr'] = dr_ip_addr
                continue

            # Backup Designated router (ID) 10.36.3.3, Interface address 10.3.4.3
            m = p7.match(line)
            if m:
                bdr_router_id = m.groupdict()['bdr_router_id']
                bdr_ip_addr = m.groupdict()['bdr_ip_addr']

                interface_dict['bdr_router_id'] = bdr_router_id
                interface_dict['bdr_ip_addr'] = bdr_ip_addr
                continue

            # Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
            m = p9.match(line)
            if m:
                hello_interval = m.groupdict()['hello']
                dead_interval = m.groupdict()['dead']
                wait_interval = m.groupdict()['wait']
                retransmit_interval = m.groupdict()['retransmit']

                interface_dict['hello_interval'] = int(hello_interval)
                interface_dict['dead_interval'] = int(dead_interval)
                interface_dict['wait_interval'] = int(wait_interval)
                interface_dict['retransmit_interval'] = int(retransmit_interval)
                continue

            # Hello due in 00:00:07:171
            m = p10_1.match(line)
            if m:
                hello_timer = m.groupdict()['hello_timer']
                interface_dict['hello_timer'] = hello_timer
                continue

            # No Hellos (Passive interface)
            m = p10_2.match(line)
            if m:
                interface_dict['passive'] = True
                continue

            # Index 1/1, flood queue length 0
            m = p11.match(line)
            if m:
                index = m.groupdict()['index']
                flood_queue_length = m.groupdict()['length']
                interface_dict['index'] = index
                interface_dict['flood_queue_length'] = int(flood_queue_length)
                continue

            # Next 0(0)/0(0)
            m = p12.match(line)
            if m:
                next_ = m.groupdict()['next']
                interface_dict['next'] = next_
                continue

            # Last flood scan length is 1, maximum is 7
            m = p13.match(line)
            if m:
                last_flood_scan_length = m.groupdict()['num']
                max_flood_scan_length = m.groupdict()['max']

                interface_dict['last_flood_scan_length'] = \
                    int(last_flood_scan_length)
                interface_dict['max_flood_scan_length'] = \
                    int(max_flood_scan_length)
                continue

            # Last flood scan time is 0 msec, maximum is 0 msec
            m = p14.match(line)
            if m:
                last_flood_scan_time_msec = m.groupdict()['time1']
                max_flood_scan_time_msec = m.groupdict()['time2']

                interface_dict['last_flood_scan_time_msec'] = \
                    int(last_flood_scan_time_msec)
                interface_dict['max_flood_scan_time_msec'] = \
                    int(max_flood_scan_time_msec)
                continue

            # LS Ack List: current length 0, high water mark 5
            m = p15.match(line)
            if m:
                ls_ack_list = m.groupdict()['ls_ack_list']
                ls_ack_list_length = m.groupdict()['num']
                high_water_mark = m.groupdict()['num2']

                interface_dict['ls_ack_list'] = ls_ack_list
                interface_dict['ls_ack_list_length'] = int(ls_ack_list_length)
                interface_dict['high_water_mark'] = int(high_water_mark)
                continue

            # Neighbor Count is 1, Adjacent neighbor count is 1
            m = p16.match(line)
            if m:
                nbr_count = m.groupdict()['nbr_count']
                adj_nbr_count = m.groupdict()['adj_nbr_count']

                statistic_dict = interface_dict.setdefault('statistics', {})
                statistic_dict['nbr_count'] = int(nbr_count)
                statistic_dict['adj_nbr_count'] = int(adj_nbr_count)

                # initialize 'neighbors'
                neighbors = interface_dict.setdefault('neighbors', {})
                continue

            # Adjacent with neighbor 10.64.4.4  (Designated Router)
            # Adjacent with neighbor 10.16.2.2  (Backup Designated Router)
            # Adjacent with neighbor 101.3.3.3
            m = p17.match(line)
            if m:
                neighbor_id = m.groupdict()['neighbors_router_id']
                inner_neighbor_dict = neighbors.setdefault(neighbor_id, {})
                if "Designated" in line:
                    inner_neighbor_dict['dr_router_id'] = neighbor_id
                elif "Backup" in line:
                    inner_neighbor_dict['bdr_router_id'] = neighbor_id
                else:
                    inner_neighbor_dict['router_id'] = neighbor_id
                continue

            # Suppress hello for 0 neighbor(s)
            m = p18.match(line)
            if m:
                num_nbrs_suppress_hello = m.groupdict()['sup']
                statistic_dict['num_nbrs_suppress_hello'] = \
                    int(num_nbrs_suppress_hello)
                continue

            # Multi-area interface Count is 0
            # Multi-area interface Count is 0
            m = p19.match(line)
            if m:
                multi_area_intf_count = m.groupdict()['count']
                statistic_dict['multi_area_intf_count'] = \
                    int(multi_area_intf_count)
                continue

            # Label stack Primary label 0 Backup label 0 SRTE label 0
            m = p20.match(line)
            if m:
                primary_label = m.groupdict()['primary_label']
                backup_label = m.groupdict()['backup_label']
                srte_label = m.groupdict()['srte_label']

                label_stack_dict = interface_dict.setdefault('label_stack', {})
                label_stack_dict['primary_label'] = primary_label
                label_stack_dict['backup_label'] = backup_label
                label_stack_dict['srte_label'] = srte_label
                continue

            # Forward reference No, Unnumbered no,  Bandwidth 1000000
            m = p21.match(line)
            if m:
                forward_reference = m.groupdict()['forward_reference']
                unnumbered_bool = m.groupdict()['unnumbered_bool']
                bandwidth = m.groupdict()['bandwidth']

                interface_dict['forward_reference'] = forward_reference
                interface_dict['unnumbered'] = \
                    False if unnumbered_bool == 'no' else True
                interface_dict['bandwidth'] = int(bandwidth)
                continue

            # BFD enabled, BFD interval 150 msec, BFD multiplier 3, Mode: Default
            m = p22.match(line)
            if m:
                interval = m.groupdict()['interval']
                multiplier = m.groupdict()['multi']
                mode = m.groupdict()['mode']

                interface_dict['bfd']['enable'] = True
                interface_dict['bfd']['interval'] = int(interval)
                interface_dict['bfd']['multiplier'] = int(multiplier)
                if mode:
                    interface_dict['bfd']['mode'] = mode
                continue

            # Non-Stop Forwarding (NSF) enabled
            m = p23.match(line)
            if m:
                nsf_status = m.groupdict()['nsf_status']
                interface_dict['nsf_enabled'] = \
                    True if nsf_status == 'enabled' else False
                continue

            # # Configured as demand circuit
            m = p25.match(line)
            if m:
                interface_dict['demand_circuit'] = True
                continue

            # Run as demand circuit.
            m = p26.match(line)
            if m:
                interface_dict['demand_circuit'] = True
                continue

            # DoNotAge LSA not allowed (Number of DCbitless LSA is 1).
            m = p27.match(line)
            if m:
                interface_dict['donotage_lsa'] = False
                interface_dict['total_dcbitless_lsa'] = \
                    int(m.groupdict()['num'])
                continue

            # Loopback interface is treated as a stub Host
            m = p28.match(line)
            if m:
                interface_dict['treated_as_stub_host'] = True
                continue

            # if there is no 'default' vrf in the output, remove its initial empty dict
            if 'default' in ret_dict['vrf'] and not ret_dict['vrf']['default']:
                ret_dict['vrf'].pop('default', None)

        return ret_dict
