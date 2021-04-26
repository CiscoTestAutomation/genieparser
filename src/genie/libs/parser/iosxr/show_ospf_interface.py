"""
    show_ospf_interface.py
    IOSXR parsers for the following show commands:
         * show ospf interface
         * show ospf interface <interface_name>
         * show ospf <process_name> interface
         * show ospf <process_name> interface <interface_name>
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# ======================================================
# schema for:
#       * show ospf interface
#       * show ospf interface <interface_name>
#       * show ospf <process_name> interface
#       * show ospf <process_name> interface <interface_name>
#       * show ospf vrf all-inclusive interface <interface_name>
# ======================================================
from genie.libs.parser.iosxr.show_ospf import ShowOspfVrfAllInclusiveInterfaceSchema

# ======================================================
# parser schema for:
#          * show ospf interface
#          * show ospf interface <interface_name>
#          * show ospf <process_name> interface
#          * show ospf <process_name> interface <interface_name>
# ======================================================
class ShowOspfInterfaceSchema(MetaParser):
    schema = {
        "vrf": {
            Any(): {  # VRF information, if no, assign "default"
                "address_family": {
                    Any(): {  # IPv4 as initial value
                        "instance": {
                            Any(): {  # here is ospf name
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
                                        Optional("forward_ref_No"): {
                                            "unnumbered": bool,
                                            "bandwidth": int
                                        },
                                        Optional("nsf"): {
                                            "enabled": bool,
                                        },
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
                                        Optional("neighbors"): list
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
                    self.cli_command[3].format(process_name=process_name, interface_name=interface_name)
                )
            elif interface_name:
                out = self.device.execute(
                    self.cli_command[1].format(interface_name=interface_name)
                )
            elif process_name:
                out = self.device.execute(
                    self.cli_command[2].format(process_name=process_name)
                )
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        ret_dict = {}

        # initialization
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
                        r'Network +Type +(?P<interface_type>\w+), +Cost: +(?P<cost>\d+)')

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
        p17_1 = re.compile(
            r'^Adjacent +with +neighbor +(?P<neighbors_dr_router_id>(\S+)) +\((D|d)esignated +(R|r)outer\)$')
        # Adjacent with neighbor 10.16.2.2  (Backup Designated Router)
        p17_2 = re.compile(
            r'Adjacent +with +neighbor +(?P<neighbors_bdr_router_id>(\S+)) +\((D|d)esignated +(R|r)outer\)$')

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
        p21 = re.compile(
            r'Forward +reference No, +Unnumbered +(?P<unnumbered_bool>\w+), +Bandwidth +(?P<bandwidth>\d+)$')


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
        p27 = re.compile(
            r"^DoNotAge +LSA +not +allowed +\(Number +of"
            " +DCbitless +LSA +is +(?P<num>(\d+))\)\.$"
        )

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
                else: # if there is no vrf information following ospf instance, assign it to default vrf dict
                    vrf_dict = vrfs_dict.setdefault('default', {})

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

                interface_dict['enable'] = True if interface_enable == 'up' else False

                interface_dict['line_protocol'] = True if line_protocol == 'up' else False

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

            # Forward reference No, Unnumbered no,  Bandwidth 1000000
            m = p21.match(line)
            if m:
                unnumbered_bool = m.groupdict()['unnumbered_bool']
                bandwidth = m.groupdict()['bandwidth']

                forward_reference_no_dict = interface_dict.setdefault('forward_ref_No', {})

                forward_reference_no_dict['unnumbered'] = True if unnumbered_bool == 'yes' else False
                forward_reference_no_dict['bandwidth'] = int(bandwidth)




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

            # Designated Router (ID) 10.64.4.4, Interface address 10.3.4.4
            # p7 = re.compile(
            #     r'^Designated +(R|r)outer +\(ID\) +(?P<dr_router_id>(\S+)), +(I|i)nterface +(A|a)ddress +'
            #     r'(?P<dr_ip_addr>(\S+))$')
            #
            m = p7.match(line)
            if m:
                dr_router_id = m.groupdict()['dr_router_id']
                dr_ip_addr = m.groupdict()['dr_ip_addr']

                interface_dict['dr_router_id'] = dr_router_id
                interface_dict['dr_ip_addr'] = dr_ip_addr


            # Backup Designated router (ID) 10.36.3.3, Interface address 10.3.4.3
            # p8 = re.compile(
            #     r'^Backup +(D|d)esignated +(R|r)outer +\(ID\) +(?P<bdr_router_id>(\S+)), +(I|i)nterface +'
            #     r'(A|a)ddress +(?P<bdr_ip_addr>(\S+))$')

            m = p7.match(line)
            if m:
                bdr_router_id = m.groupdict()['bdr_router_id']
                bdr_ip_addr = m.groupdict()['bdr_ip_addr']

                interface_dict['bdr_router_id'] = bdr_router_id
                interface_dict['bdr_ip_addr'] = bdr_ip_addr






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


            # Non-Stop Forwarding (NSF) enabled
            # p23 = re.compile(r'^Non-Stop +Forwarding +\(NSF\) +(?P<nsf_status>\w+)$')
            m = p23.match(line)
            if m:
                nsf_status = m.groupdict()['nsf_status']

                interface_dict.setdefault('nsf', {})['enabled'] = True if nsf_status == 'enabled' else False

            # Hello due in 00:00:07:171
            # p10_1 = re.compile(r'^Hello +due +in +(?P<hello_timer>(\S+))$')


            m = p10_1.match(line)
            if m:
                hello_timer = m.groupdict()['hello_timer']


                interface_dict['hello_timer'] = hello_timer







            # No Hellos (Passive interface)
            # p10_2 = re.compile(r"^No +Hellos +\(Passive +interface\)$")
            m = p10_2.match(line)
            if m:
                interface_dict['passive'] = True

            # Index 1/1, flood queue length 0
            # p11 = re.compile(r'^Index +(?P<index>(\S+)), +flood +queue +length +(?P<length>(\d+))$')
            m = p11.match(line)
            if m:
                index = m.groupdict()['index']
                flood_queue_length = m.groupdict()['length']
                interface_dict['index'] = index
                interface_dict['flood_queue_length'] = int(flood_queue_length)


            # Next 0(0)/0(0)
            # p12 = re.compile(r'^Next +(?P<next>(\S+))$')
            m = p12.match(line)
            if m:
                next_ = m.groupdict()['next']
                interface_dict['next'] = next_

            # Last flood scan length is 1, maximum is 7
            # Last flood scan length is 1, maximum is 3
            # p13 = re.compile(r'^Last +flood +scan +length +is +(?P<num>(\d+)), +maximum +is +(?P<max>(\d+))$')
            m = p13.match(line)
            if m:
                last_flood_scan_length = m.groupdict()['num']
                max_flood_scan_length = m.groupdict()['max']

                interface_dict['last_flood_scan_length'] = int(last_flood_scan_length)
                interface_dict['max_flood_scan_length'] = int(max_flood_scan_length)


            # Last flood scan time is 0 msec, maximum is 0 msec
            # p14 = re.compile(
            #     r'^Last +flood +scan +time +is +(?P<time1>(\d+)) +msec, +maximum +is +(?P<time2>(\d+)) +msec$')
            m = p14.match(line)

            if m:
                last_flood_scan_time_msec = m.groupdict()['time1']
                max_flood_scan_time_msec = m.groupdict()['time2']

                interface_dict['last_flood_scan_time_msec'] = int(last_flood_scan_time_msec)
                interface_dict['max_flood_scan_time_msec'] = int(max_flood_scan_time_msec)


            # LS Ack List: current length 0, high water mark 5
            #         p15 = re.compile(
            #             r'^LS +Ack +List: +(?P<ls_ack_list>(\S+)) +length +(?P<num>(\d+)), +high +water +mark +(?P<num2>(\d+))$')

            m = p15.match(line)
            if m:
                ls_ack_list = m.groupdict()['ls_ack_list']
                ls_ack_list_length = m.groupdict()['num']
                high_water_mark = m.groupdict()['num2']
                interface_dict['ls_ack_list'] = ls_ack_list
                interface_dict['ls_ack_list_length'] = int(ls_ack_list_length)
                interface_dict['high_water_mark'] = int(high_water_mark)

            # Neighbor Count is 1, Adjacent neighbor count is 1
            # Neighbor Count is 1, Adjacent neighbor count is 1
            # p16 = re.compile(
            #     r'^Neighbor +Count +is +(?P<nbr_count>(\d+)), +Adjacent +neighbor +count +is +(?P<adj_nbr_count>(\d+))$')
            m = p16.match(line)
            if m:
                nbr_count = m.groupdict()['nbr_count']
                adj_nbr_count = m.groupdict()['adj_nbr_count']

                statistic_dict = interface_dict.setdefault('statistics',{})
                statistic_dict['nbr_count'] = int(nbr_count)
                statistic_dict['adj_nbr_count'] = int(adj_nbr_count)


                neighbors = interface_dict.setdefault('neighbors', [])

            # Adjacent with neighbor 10.64.4.4  (Designated Router)
            # Adjacent with neighbor 10.16.2.2  (Backup Designated Router)
            # Adjacent with neighbor 101.3.3.3
            m = p17.match(line)
            if m:
                neighbor_id = m.groupdict()['neighbors_router_id']
                neighbors.append(neighbor_id)


            # Suppress hello for 0 neighbor(s)
            # p18 = re.compile(r'^Suppress +hello +for +(?P<sup>(\d+)) +neighbor\(s\)$')
            m = p18.match(line)
            if m:
                num_nbrs_suppress_hello = m.groupdict()['sup']
                statistic_dict['num_nbrs_suppress_hello'] = int(num_nbrs_suppress_hello)


            # Multi-area interface Count is 0
            # Multi-area interface Count is 0
            # p19 = re.compile(r'^Multi-area +interface +Count +is +(?P<count>(\d+))$')
            m = p19.match(line)
            if m:
                multi_area_intf_count = m.groupdict()['count']
                statistic_dict['multi_area_intf_count'] = int(multi_area_intf_count)

            # # Configured as demand circuit
            # p25 = re.compile(r'^Configured as demand circuit$')
            #

            m = p25.match(line)
            if m:
                interface_dict['demand_circuit'] = True



            # Run as demand circuit.
            # p26 = re.compile(r"^Run as demand circuit\.$")
            #
            m = p26.match(line)
            if m:
                interface_dict['demand_circuit'] = True


            # DoNotAge LSA not allowed (Number of DCbitless LSA is 1).
            # p27 = re.compile(
            #     r"^DoNotAge +LSA +not +allowed +\(Number +of"
            #     " +DCbitless +LSA +is +(?P<num>(\d+))\)\.$"
            # )

            m = p27.match(line)
            if m:
                interface_dict['donotage_lsa'] = False
                interface_dict['total_dcbitless_lsa'] = int(m.groupdict()['num'])

            # if there is no 'default' vrf in the output, remove its initial empty dict
            if 'default' in ret_dict['vrf'] and not ret_dict['vrf']['default']:
                ret_dict['vrf'].pop('default', None)

        return ret_dict
