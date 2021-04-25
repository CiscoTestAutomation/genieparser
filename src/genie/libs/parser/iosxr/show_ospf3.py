"""show_ospf3.py

IOSXR parsers for the following show commands:
    * show ospfv3 interface
    * show ospfv3 interface <interface_name>
    * show ospfv3 <process_name> interface
    * show ospfv3 <process_name> interface <interface_name>
    * show ospfv3 vrf all-inclusive interface
    * show ospfv3 vrf all-inclusive interface <interface_name>
"""

# Python
import re
from netaddr import IPAddress, IPNetwork

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional


# ==================================
# Schema for 'show ospfv3 interface'
# ==================================
class ShowOspfv3InterfaceSchema(MetaParser):
    """Schema for show ospfv3 interface"""

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
                                                Optional("last_flood_scan_time_msec"): int,
                                                Optional("max_flood_scan_time_msec"): int,
                                                Optional("ls_ack_list"): str,
                                                Optional("ls_ack_list_length"): int,
                                                Optional("high_water_mark"): int,
                                                Optional("total_dcbitless_lsa"): int,
                                                Optional("donotage_lsa"): bool,
                                                Optional("statistics"): {
                                                    Optional("adj_nbr_count"): int,
                                                    Optional("nbr_count"): int,
                                                    Optional("num_nbrs_suppress_hello"): int,
                                                    Optional("multi_area_intf_count"): int,
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

# ==================================
# Parser for 'show ospfv3 interface'
# ==================================
class ShowOspfv3Interface(ShowOspfv3InterfaceSchema):
    """Parser for show ospfv3 interface"""

    cli_command = [
        "show ospfv3 interface",
        "show ospfv3 interface {interface_name}",
        "show ospfv3 {process_name} interface",
        "show ospfv3 {process_name} interface {interface_name}",
        "show ospfv3 vrf all-inclusive interface",
        "show ospfv3 vrf all-inclusive interface {interface_name}",
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
                    out = self.device.execute(self.cli_command[2].format(interface=interface, vrf=vrf))
                else:
                    out = self.device.execute(self.cli_command[1].format(interface=interface))
            else:
                if vrf:
                    out = self.device.execute(self.cli_command[3].format(vrf=vrf))
                else:
                    out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # Init vars
        ret_dict = {}

        # Address Family for ospfv3 is always ipv6
        af = "ipv6"  

        # set instance
        instance = ""
        
        # Mapping dict
        bool_dict = {"up": True, "down": False, "unknown": False}

        # p1 = re.compile(
        #     r"^Interfaces +for +OSPF +(?P<instance>(\S+))"
        #     "(?:, +VRF +(?P<vrf>(\S+)))?$")

        # GigabitEthernet0/0/0/0 is up, line protocol is up
        p2 = re.compile(
            r"^(?P<interface>(\S+)) +is( +administratively)?"
            " +(?P<enable>(unknown|up|down)), +line +protocol +is"
            " +(?P<line_protocol>(up|down))$")

        # Link Local address fe80:100:10::1, Interface ID 7
        p3 = re.compile(
            r"^Link +Local +address +(?P<address>(\S+)),"
            " +Interface ID +(?P<interface_id>(\S+))$")

        # Area 0, Process ID mpls1, Instance ID 0, Router ID 25.97.1.1
        p4 = re.compile(
            r"^Area +(?P<area>(\S+))"
            ", +Process +ID +(?P<pid>(\S+))"
            ", +Instance +ID +(?P<instance>(\S+))"
            ", +Router +ID +(?P<router_id>(\S+))$")

        # Network Type POINT_TO_POINT, Cost: 1
        p4_1 = re.compile(
            r"^Network +Type +(?P<interface_type>(\S+))"
            ", +Cost: +(?P<cost>(\S+))$") 

        # BFD enabled, interval 150 msec, multiplier 3, mode Default
        p21 = re.compile(
            r"^BFD enabled"
            "(?:, +interval +(?P<interval>(\d+)) +msec)?"
            "(?:, +multiplier +(?P<multi>(\d+)))?"
            "(?:, +mode +(?P<mode>(\S+)))?$")

        # Transmit Delay is 1 sec, State POINT_TO_POINT,
        p5 = re.compile(
            r"^Transmit +Delay is +(?P<delay>(\d+)) +sec"
            ", +sec, +State +(?P<state>(\w)+),$")

        # Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
        p8 = re.compile(
            r"^Timer +intervals +configured"
            ", +Hello +(?P<hello>(\d+))"
            ", +Dead +(?P<dead>(\d+))"
            ", +Wait +(?P<wait>(\d+))"
            ", +Retransmit +(?P<retransmit>(\d+))$")

        # p6 = re.compile(
        #     r"^Designated +(R|r)outer +\(ID\)"
        #     " +(?P<dr_router_id>(\S+)), +(I|i)nterface"
        #     " +(A|a)ddress +(?P<dr_ip_addr>(\S+))$")

        # p7 = re.compile(
        #     r"^Backup +(D|d)esignated +(R|r)outer +\(ID\)"
        #     " +(?P<bdr_router_id>(\S+)), +(I|i)nterface"
        #     " +(A|a)ddress +(?P<bdr_ip_addr>(\S+))$")

        # Hello due in 00:00:08
        p9_1 = re.compile(r"^Hello +due +in +(?P<hello_timer>(\S+))$")

        # p9_2 = re.compile(r"^No +Hellos +\(Passive +interface\)$")

        # Index 1/1/1, flood queue length 0
        p10 = re.compile(r"^Index +(?P<index>(\S+)), +flood +queue +length +(?P<length>(\d+))$")

        # Next 0(0)/0(0)/0(0)
        p22 = re.compile(r"^Next +(?P<next>(\S+))$")
        
        # Last flood scan length is 1, maximum is 4
        p11 = re.compile(r"^Last +flood +scan +length +is +(?P<num>(\d+))"
            ", +maximum +is +(?P<max>(\d+))$")

        # Last flood scan time is 0 msec, maximum is 0 msec
        p12 = re.compile(
            r"^Last +flood +scan +time +is +(?P<time1>(\d+))"
            " +msec, +maximum +is +(?P<time2>(\d+)) +msec$")


        # p13 = re.compile(
        #     r"^LS +Ack +List: +(?P<ls_ack_list>(\S+)) +length"
        #     " +(?P<num>(\d+)), +high +water +mark"
        #     " +(?P<num2>(\d+))$")

        # Neighbor Count is 1, Adjacent neighbor count is 1
        p14 = re.compile(
            r"^Neighbor +Count +is +(?P<nbr_count>(\d+))"
            ", +Adjacent +neighbor +count +is"
            " +(?P<adj_nbr_count>(\d+))$")

        # Adjacent with neighbor 100.100.100.100
        p15_1 = re.compile(
            r"^Adjacent +with +neighbor +(?P<nbr>(\S+))$")

            
        # p15_2 = re.compile(
        #     r"^Adjacent +with +neighbor +(?P<nbr>(\S+))"
        #     " +\((D|d)esignated +(R|r)outer\)$")
        # p15_3 = re.compile(
        #     r"^Adjacent +with +neighbor +(?P<nbr>(\S+))" " +\(Hello suppressed\)$")

        # Suppress hello for 0 neighbor(s)
        p16 = re.compile(r"^Suppress +hello +for +(?P<sup>(\d+)) +neighbor\(s\)$")

        # Reference count is 6
        p17 = re.compile(r"^Reference +Count +is +(?P<count>(\d+))$")


        # p18 = re.compile(r"^Configured as demand circuit\.$")
        # p19 = re.compile(r"^Run as demand circuit\.$")
        # p20 = re.compile(
        #     r"^DoNotAge +LSA +not +allowed +\(Number +of"
        #     " +DCbitless +LSA +is +(?P<num>(\d+))\)\.$")

        p21 = re.compile(r"^Loopback interface is treated as a stub Host\.$")

        


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
                if (instance not in ret_dict["vrf"][vrf]["address_family"][af]["instance"]):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance] = {}
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
                if (instance not in ret_dict["vrf"][vrf]["address_family"][af]["instance"]):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance] = {}
                    
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
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][pid] = ret_dict["vrf"][vrf]["address_family"][af]["instance"].pop(instance)
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
                            for vl_inst in vl_out["vrf"][vl_vrf]["address_family"][vl_af]["instance"]:
                                for vl_area in vl_out["vrf"][vl_vrf]["address_family"][vl_af]["instance"][vl_inst]["areas"]:
                                    for vl in vl_out["vrf"][vl_vrf]["address_family"][vl_af]["instance"][vl_inst]["areas"][vl_area]["virtual_links"]:
                                        vl_name = vl_out["vrf"][vl_vrf]["address_family"][vl_af]["instance"][vl_inst]["areas"][vl_area]["virtual_links"][vl]["name"]
                                        if vl_name == name:
                                            vl_transit_area_id = vl_out["vrf"][vl_vrf]["address_family"][vl_af]["instance"][vl_inst]["areas"][vl_area]["virtual_links"][vl]["transit_area_id"]
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
                if ("areas" not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance]):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance]["areas"] = {}
                if (area not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance]["areas"]):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance]["areas"][area] = {}
                if (intf_type not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance]["areas"][area]):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance]["areas"][area][intf_type] = {}
                if (intf_name not in ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance]["areas"][area][intf_type]):
                    ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance]["areas"][area][intf_type][intf_name] = {}

                # Set sub_dict
                sub_dict = ret_dict["vrf"][vrf]["address_family"][af]["instance"][instance]["areas"][area][intf_type][intf_name]

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
                sub_dict["statistics"]["num_nbrs_suppress_hello"] = int(m.groupdict()["sup"])
                continue

            # Multi-area interface Count is 0
            m = p17.match(line)
            if m:
                if "statistics" not in sub_dict:
                    sub_dict["statistics"] = {}
                sub_dict["statistics"]["multi_area_intf_count"] = int( m.groupdict()["count"])
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
