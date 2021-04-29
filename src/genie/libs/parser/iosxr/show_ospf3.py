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
            Any(): {    #default
                "address_family": {
                    Any(): {    #ipv6
                        "instance": {
                            Any(): {    # p3-- group[pid] --mpls1
                                "instance_id": {
                                    Any(): {    # p3-- int(group[instance])   --0
                                        "areas": {
                                            Any(): {    # p3-- int(group[area]) --0
                                                Optional("interfaces"): {
                                                    Any(): {    # p1-- group[interface] -- GigabitEthernet0/0/0/0
                                                        "name": str,
                                                        "enable": bool,
                                                        "line_protocol": bool,
                                                        "link_local_address": str,
                                                        "process_id": str,
                                                        "router_id": str,
                                                        "interface_type": str,
                                                        Optional("bfd"): {
                                                            Optional("bfd_status"): str,
                                                            Optional("interval"): int,
                                                            Optional("multiplier"): int,
                                                            Optional("mode"): str,
                                                        },
                                                        Optional("cost"): int,
                                                        Optional("transmit_delay"): int,
                                                        Optional("state"): str,
                                                        Optional("hello_interval"): int,
                                                        Optional("dead_interval"): int,
                                                        Optional("wait_interval"): int,
                                                        Optional("retransmit_interval"): int,
                                                        Optional("hello_timer"): str,
                                                        Optional("index"): str,
                                                        Optional("flood_queue_length"): int,
                                                        Optional("next"): str,
                                                        Optional("last_flood_scan_length"): int,
                                                        Optional("max_flood_scan_length"): int,
                                                        Optional("last_flood_scan_time_msec"): int,
                                                        Optional("max_flood_scan_time_msec"): int,
                                                        Optional("statistics"): {
                                                            Optional("nbr_count"): int,                                                            
                                                            Optional("adj_nbr_count"): int,
                                                            Optional("num_nbrs_suppress_hello"): int,
                                                            Optional("refrence_count"): int,
                                                        },
                                                        Optional("neighbors"): {    
                                                            Any(): {    #100.100.100.100
                                                                Optional("nbr_count"): str,
                                                                Optional("adj_nbr_count"): str,
                                                            },
                                                        },
                                                       Optional("loobpack_txt"): str, 
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
        interface_dict = {}

        # Address Family for ospfv3 is always ipv6
        af = "ipv6"  

        # Mapping dict
        bool_dict = {"up": True, "down": False, "unknown": False}


        # GigabitEthernet0/0/0/0 is up, line protocol is up
        p1 = re.compile(
            r"^(?P<interface>(\S+)) +is( +administratively)?"
            " +(?P<enable>(unknown|up|down)), +line +protocol +is"
            " +(?P<line_protocol>(up|down))$")

        # Link Local address fe80:100:10::1, Interface ID 7
        p2 = re.compile(
            r"^Link +Local +address +(?P<link_local_address>(\S+)),"
            " +Interface ID +(?P<interface_id>(\S+))$")

        # Area 0, Process ID mpls1, Instance ID 0, Router ID 25.97.1.1
        p3 = re.compile(
            r"^Area +(?P<area>(\S+))"
            ", +Process +ID +(?P<pid>(\S+))"
            ", +Instance +ID +(?P<instance>(\S+))"
            ", +Router +ID +(?P<router_id>(\S+))$")

        # Network Type POINT_TO_POINT, Cost: 1
        p4 = re.compile(
            r"^Network +Type +(?P<interface_type>(\S+))"
            ", +Cost: +(?P<cost>(\S+))$") 

        # BFD enabled, interval 150 msec, multiplier 3, mode Default
        p5 = re.compile(
            r"^BFD +(?P<bfd_status>(\S+))"
            "(?:, +interval +(?P<interval>(\d+)) +msec)?"
            "(?:, +multiplier +(?P<multi>(\d+)))?"
            "(?:, +mode +(?P<mode>(\S+)))?$")

        # Transmit Delay is 1 sec, State POINT_TO_POINT,
        p6 = re.compile(
            r"^Transmit +Delay is +(?P<delay>(\d+)) +sec"
            ", +State +(?P<state>(\w)+),$")

        # Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
        p7 = re.compile(
            r"^Timer +intervals +configured"
            ", +Hello +(?P<hello>(\d+))"
            ", +Dead +(?P<dead>(\d+))"
            ", +Wait +(?P<wait>(\d+))"
            ", +Retransmit +(?P<retransmit>(\d+))$")

        # Hello due in 00:00:08
        p8 = re.compile(r"^Hello +due +in +(?P<hello_timer>(\S+))$")

        # Index 1/1/1, flood queue length 0
        p9 = re.compile(r"^Index +(?P<index>(\S+)), +flood +queue +length +(?P<flood_queue_length>(\d+))$")

        # Next 0(0)/0(0)/0(0)
        p10 = re.compile(r"^Next +(?P<next>(\S+))$")
        
        # Last flood scan length is 1, maximum is 4
        p11 = re.compile(r"^Last +flood +scan +length +is +(?P<last_flood_scan_length>(\d+))"
            ", +maximum +is +(?P<max_flood_scan_length>(\d+))$")

        # Last flood scan time is 0 msec, maximum is 0 msec
        p12 = re.compile(
            r"^Last +flood +scan +time +is +(?P<last_flood_scan_time_msec>(\d+))"
            " +msec, +maximum +is +(?P<max_flood_scan_time_msec>(\d+)) +msec$")

        # Neighbor Count is 1, Adjacent neighbor count is 1
        p13 = re.compile(
            r"^Neighbor +Count +is +(?P<nbr_count>(\d+))"
            ", +Adjacent +neighbor +count +is"
            " +(?P<adj_nbr_count>(\d+))$")

        # Adjacent with neighbor 100.100.100.100
        p14 = re.compile(
            r"^Adjacent +with +neighbor +(?P<adj_with_nbr>(\S+))$")

        # Suppress hello for 0 neighbor(s)
        p15 = re.compile(r"^Suppress +hello +for +(?P<num_nbrs_suppress_hello>(\d+)) +neighbor\(s\)$")

        # Reference count is 6
        p16 = re.compile(r"^Reference +count +is +(?P<refrence_count>(\d+))$")

        # Loopback interface is treated as a stub Host
        p17 = re.compile(r"^(?P<loobpack_txt>Loopback interface is treated as a stub Host)$")

        

        for line in out.splitlines():
            line = line.strip()

            # GigabitEthernet0/0/0/0 is up, line protocol is up
            m = p1.match(line)
            if m:
                group = m.groupdict()

                #define vrf_dict dictionary and set to 'vrf'
                vrf_dict = ret_dict.setdefault('vrf', {}).\
                                    setdefault('default',{})
                
                #define af_dict dictionary and set to 'address_family'
                af_dict = vrf_dict.setdefault('address_family',{}).\
                                   setdefault(af,{})

                interface_name = group['interface']
                interface_dict.update({'interface':interface_name})
                interface_dict.update({'enable':bool_dict[group['enable']]})
                interface_dict.update({'line_protocol':bool_dict[group['line_protocol']]})
                continue

            # Link Local address fe80:100:10::1, Interface ID 7
            m = p2.match(line)
            if m:
                group = m.groupdict()

                interface_dict.update({'link_local_address':group['link_local_address']})
                interface_dict.update({'interface_id':int(group['interface_id'])})
                continue
            
            # Area 0, Process ID mpls1, Instance ID 0, Router ID 25.97.1.1
            m = p3.match(line)
            if m:
                group = m.groupdict()

                interface_dict.update({'router_id':group['router_id']})


                # af_dict.setdefault('instance',{}).setdefault(group['pid'],{}).\
                #                 setdefault('instance_id',{}).setdefault(int(group['instance']),{}).\
                #                 setdefault('areas',{}).setdefault(int(group['area']),{}).\
                #                 setdefault('interfaces',{}).setdefault(interface_name,{})

                instance_dict= af_dict.setdefault('instance',{}).setdefault(group['pid'],{})
                instance_id_dict = instance_dict.setdefault('instance_id',{}).setdefault(int(group['instance']),{})
                areas_dict = instance_id_dict.setdefault('areas',{}).setdefault(int(group['area']),{})
                interfaces_dict= areas_dict.setdefault('interfaces',{}).setdefault(interface_name,{})
                        
                continue

            # Network Type POINT_TO_POINT, Cost: 1
            m = p4.match(line)
            if m:
                group = m.groupdict()

                interface_dict.update({'interface_type':group['interface_type']})
                interface_dict.update({'cost':int(group['cost'])})
                continue

            # BFD enabled, interval 150 msec, multiplier 3, mode Default
            m = p5.match(line)
            if m:
                group = m.groupdict()

                bdf_dict = interface_dict.setdefault('bdf',{})

                bdf_dict.update({'bfd_status':group['bfd_status']})
                bdf_dict.update({'interval':int(group['interval'])})
                bdf_dict.update({'multi':int(group['multi'])})
                bdf_dict.update({'mode':group['mode']})
                continue
            
            # Transmit Delay is 1 sec, State POINT_TO_POINT,
            m = p6.match(line)
            if m:
                group = m.groupdict()

                interface_dict.update({'transmit_delay':int(group['delay'])})
                interface_dict.update({'state':group['state']})
                continue

            # Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
            m = p7.match(line)
            if m:
                group = m.groupdict()

                interface_dict.update({'hello_interval':int(group['hello'])})
                interface_dict.update({'dead_interval':int(group['dead'])})
                interface_dict.update({'wait_interval':int(group['wait'])})
                interface_dict.update({'retransmit_interval':int(group['retransmit'])})
                continue


            # Hello due in 00:00:07:587
            m = p8.match(line)
            if m:
                group = m.groupdict()

                interface_dict.update({'hello_timer':group['hello_timer']})
                continue

            # Index 1/1/1, flood queue length 0
            m = p9.match(line)
            if m:
                group = m.groupdict()

                interface_dict.update({'index':group['index']})
                interface_dict.update({'flood_queue_length':int(group['flood_queue_length'])})
                continue

            # Next 0(0)/0(0)
            m = p10.match(line)
            if m:
                group = m.groupdict()

                interface_dict.update({'next':group['next']})
                continue

            # Last flood scan length is 1, maximum is 3
            m = p11.match(line)
            if m:
                group = m.groupdict()

                interface_dict.update({'last_flood_scan_length':int(group['last_flood_scan_length'])})
                interface_dict.update({'max_flood_scan_length':int(group['max_flood_scan_length'])})
                continue

            # Last flood scan time is 0 msec, maximum is 0 msec
            m = p12.match(line)
            if m:
                group = m.groupdict()

                interface_dict.update({'last_flood_scan_time_msec':int(group['last_flood_scan_time_msec'])})
                interface_dict.update({'max_flood_scan_time_msec':int(group['max_flood_scan_time_msec'])})
                continue

            
            # Neighbor Count is 1, Adjacent neighbor count is 1
            m = p13.match(line)
            if m:
                group = m.groupdict()

                neighbor_stats_dict = interface_dict.setdefault('statistics',{})
                nbr_count = int(group['nbr_count'])
                adj_nbr_count = int(group['adj_nbr_count'])

                neighbor_stats_dict.update({'nbr_count':nbr_count})
                neighbor_stats_dict.update({'adj_nbr_count':adj_nbr_count})
                continue

            # Adjacent with neighbor 100.100.100.100
            m = p14.match(line)
            if m:
                group = m.groupdict()
                adj_nbr = group['adj_with_nbr']

                neighbor_stats_dict.update({'neighbor':adj_nbr})
                continue

            # Suppress hello for 0 neighbor(s)
            m = p15.match(line)
            if m:
                group = m.groupdict()

                neighbor_stats_dict.update({'num_nbrs_suppress_hello':int(group['num_nbrs_suppress_hello'])})                
                continue
            import pdb; pdb.set_trace()
            # Reference count is 6
            m = p16.match(line)
            if m:
                group = m.groupdict()

                neighbor_stats_dict.update({'refrence_count':int(group['refrence_count'])})

                neighbor_dict = interface_dict.setdefault('neighbors',{}).\
                                                setdefault(adj_nbr,{})

                neighbor_dict.update({'nbr_count':nbr_count})
                neighbor_dict.update({'adj_nbr_count':adj_nbr_count})
                interfaces_dict.update(interface_dict)

                continue
            
            m = p17.match(line)
            if m:
                group = m.groupdict()

                interface_dict.update({'loobpack_txt':group['loobpack_txt']})
                continue
            
        return ret_dict
