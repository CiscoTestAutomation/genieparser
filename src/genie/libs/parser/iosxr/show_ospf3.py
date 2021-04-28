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
                                "instance_id": {
                                    Any(): {
                                        "areas": {
                                            Any(): {
                                                Optional("interfaces"): {
                                                    Any(): {
                                                        "name": str,
                                                        "enable": bool,
                                                        "line_protocol": bool,
                                                        "link_local_address": str,
                                                        "interface_id": int,
                                                        "router_id": str,
                                                        "interface_type": str,
                                                        Optional("cost"): int,
                                                        "bfd": {
                                                            "enable": bool,
                                                            Optional("interval"): int,
                                                            Optional("multiplier"): int,
                                                            Optional("mode"): str,
                                                        },
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
                                                        Optional("neighbors_statistics"): {
                                                            Optional("neighbor_count"): int,
                                                            Optional("adjacent_neighbor_count"): int,
                                                            Optional("adjacent_with_neighbor"): int,
                                                            Optional("num_nbrs_suppress_hello"): int,
                                                            Optional("refrence_count"): int,
                                                        },
                                                        Optional("neighbors"): {
                                                            Any(): {
                                                                Optional("nbr_count"): str,
                                                                Optional("adj_nbr_count"): str,
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
        # instance_dict = {}

        # Address Family for ospfv3 is always ipv6
        af = "ipv6"  
        
        # Mapping dict
        bool_dict = {"up": True, "down": False, "unknown": False}

        # GigabitEthernet0/0/0/0 is up, line protocol is up
        p1 = re.compile(
            r"^(?P<name>(\S+)) +is( +administratively)?"
            " +(?P<enable>(unknown|up|down)), +line +protocol +is"
            " +(?P<line_protocol>(up|down))$")

        # Link Local address fe80:100:10::1, Interface ID 7
        p2 = re.compile(
            r"^Link +Local +address +(?P<link_local_address>(\S+)),"
            " +Interface ID +(?P<interface_id>(\S+))$")

        # Area 0, Process ID mpls1, Instance ID 0, Router ID 25.97.1.1
        p3 = re.compile(
            r"^Area +(?P<area>(\S+))"
            ", +Process +ID +(?P<process_id>(\S+))"
            ", +Instance +ID +(?P<instance_id>(\S+))"
            ", +Router +ID +(?P<router_id>(\S+))$")

        # Network Type POINT_TO_POINT, Cost: 1
        p4 = re.compile(
            r"^Network +Type +(?P<interface_type>(\S+))"
            ", +Cost: +(?P<cost>(\S+))$") 

        # BFD enabled, interval 150 msec, multiplier 3, mode Default
        p5 = re.compile(
            r"^BFD +(?P<enable>(\S+))"
            "(?:, +interval +(?P<interval>(\d+)) +msec)?"
            "(?:, +multiplier +(?P<multi>(\d+)))?"
            "(?:, +mode +(?P<mode>(\S+)))?$")

        # Transmit Delay is 1 sec, State POINT_TO_POINT,
        p6 = re.compile(
            r"^Transmit +Delay is +(?P<transmit_delay>(\d+)) +sec"
            ", +State +(?P<state>(\w)+),$")

        # Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
        p7 = re.compile(
            r"^Timer +intervals +configured"
            ", +Hello +(?P<hello_interval>(\d+))"
            ", +Dead +(?P<dead_interval>(\d+))"
            ", +Wait +(?P<wait_interval>(\d+))"
            ", +Retransmit +(?P<retransmit_interval>(\d+))$")

        # Hello due in 00:00:08
        p8 = re.compile(r"^Hello +due +in +(?P<hello_timer>(\S+))$")

        # Index 1/1/1, flood queue length 0
        p9 = re.compile(r"^Index +(?P<index>(\S+)), +flood +queue +length +(?P<length>(\d+))$")        

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
            r"^Neighbor +Count +is +(?P<neighbor_count>(\d+))"
            ", +Adjacent +neighbor +count +is"
            " +(?P<adjacent_neighbor_count>(\d+))$")

        # Adjacent with neighbor 100.100.100.100
        p14 = re.compile(
            r"^Adjacent +with +neighbor +(?P<adjacent_with_neighbor>(\S+))$")

        # Suppress hello for 0 neighbor(s)
        p15 = re.compile(r"^Suppress +hello +for +(?P<num_nbrs_suppress_hello>(\d+)) +neighbor\(s\)$")

        # Reference count is 6
        p16 = re.compile(r"^Reference +Count +is +(?P<refrence_count>(\d+))$")

        # Loopback interface is treated as a stub Host
        p17 = re.compile(r"^(?P<loopback>Loopback interface is treated as a stub Host)$")

        
        
        for line in out.splitlines():
            line = line.strip()

            # GigabitEthernet0/0/0/2 is up, line protocol is up
            # Loopback1 is administratively down, line protocol is down
            # Loopback0 is up, line protocol is up
            m = p1.match(line)
            if m:
                group = m.groupdict()

                #define vrf_dict dictionary and set to 'vrf'
                vrf_dict = ret_dict.setdefault('vrf', {})

                #define def_dict dictionary and assigned to 'default'
                def_dict = vrf_dict.setdefault('default',{})                

                #define af_dict dictionary and set to 'address_family'
                af_dict = def_dict.setdefault('address_family',{})

                #define ipv6_dict dictionary and set to 'ipv6'
                ipv6_dict = af_dict.setdefault(af,{})

                #define instance_dict dictionary and set to 'instance'
                instance_dict = ipv6_dict.setdefault('instance',{})
          
                #update interface_dict
                interface_dict.update({'name': group['name']})
                interface_dict.update({'enable': group['enable']})
                continue

            # Link Local address fe80:100:10::1, Interface ID 7
            m = p2.match(line)
            if m:
                group = m.groupdict()

                #update interface_dict
                interface_dict.update({'link_local_address': group['link_local_address']})
                interface_dict.update({'interface_id': group['interface_id']})
                continue

            # Area 0, Process ID mpls1, Instance ID 0, Router ID 25.97.1.1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                
                #update interface_dict
                interface_dict.update({'router_id': group['router_id']})

                #define process_dict dictionary and set to 'process_id' 
                process_dict = instance_dict.setdefault(group['process_id'],{})
                
                #define instance_id_dict dictionary and set to 'instance_id'
                instance_id_dict = process_dict.setdefault('instance_id',{}).setdefault(group['instance_id'],{})

                #define areas_dict dictionary and set to 'area'
                areas_dict = instance_id_dict.setdefault('areas',{}).setdefault(group['area'],{})

                #define int_dict dictionary and set to interfaces_dict
                interfaces_dict = areas_dict.setdefault('interfaces', {}).setdefault(interface_dict['name'],{})
                
                # update int_dict
                interfaces_dict.update(interface_dict)
                continue
            

            # Network Type POINT_TO_POINT, Cost: 1
            m = p4.match(line)
            if m:
                group = m.groupdict()
                
                # update interface_dict
                interface_dict.update({'interface_type': group['interface_type']})
                interface_dict.update({'cost': group['cost']})

                # # update interfaces_dict
                interfaces_dict.update(interface_dict)                
                continue

            # Transmit Delay is 1 sec, State DR, Priority 1, MTU 1500, MaxPktSz 1500
            m = p5.match(line)
            if m:
                group = m.groupdict()

                #define bdf_dict dictionary and set to 'bdf'
                bdf_dict = interface_dict.setdefault('bdf',{})

                #update bdf_dict
                bdf_dict.update({'enable': group['enable']})
                bdf_dict.update({'interval': group['interval']})
                bdf_dict.update({'multi': group['multi']})
                bdf_dict.update({'mode': group['mode']})

                # # update interfaces_dict
                interfaces_dict.update(interface_dict)
                continue

            # Transmit Delay is 1 sec, State POINT_TO_POINT,
            m = p6.match(line)
            if m:
                group = m.groupdict()

                # update interface_dict
                interface_dict.update({'transmit_delay': group['transmit_delay']})
                interface_dict.update({'state': group['state']})

                # # update interfaces_dict
                interfaces_dict.update(interface_dict)
                continue

            # Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
            m = p7.match(line)
            if m:
                group = m.groupdict()

                # update interface_dict
                interface_dict.update({'hello_interval': group['hello_interval']})
                interface_dict.update({'dead_interval': group['dead_interval']})
                interface_dict.update({'wait_interval': group['wait_interval']})
                interface_dict.update({'retransmit_interval': group['retransmit_interval']})

                # # update interfaces_dict
                interfaces_dict.update(interface_dict)
                continue

            # Hello due in 00:00:08
            m = p8.match(line)
            if m:
                group = m.groupdict()

                # update interface_dict
                interface_dict.update({'hello_timer': group['hello_timer']})

                # update interfaces_dict
                interfaces_dict.update(interface_dict)
                continue

            # Index 1/1/1, flood queue length 0
            m = p9.match(line)
            if m:
                group = m.groupdict()

                # update interface_dict
                interface_dict.update({'index': group['index']})
                interface_dict.update({'length': group['length']})

                # update interfaces_dict
                interfaces_dict.update(interface_dict)
                continue

            # Next 0(0)/0(0)/0(0
            m = p10.match(line)
            if m:
                group = m.groupdict()

                # update interface_dict
                interface_dict.update({'next': group['next']})

                # update interfaces_dict
                interfaces_dict.update(interface_dict)
                continue

            # Last flood scan length is 1, maximum is 4
            m = p11.match(line)
            if m:
                group = m.groupdict()

                # update interface_dict
                interface_dict.update({'last_flood_scan_length': group['last_flood_scan_length']})
                interface_dict.update({'max_flood_scan_length': group['max_flood_scan_length']})

                # update interfaces_dict
                interfaces_dict.update(interface_dict)
                continue
            
            # Last flood scan time is 0 msec, maximum is 0 msec
            m = p12.match(line)
            if m:
                group = m.groupdict()

                # update interface_dict
                interface_dict.update({'last_flood_scan_time_msec': group['last_flood_scan_time_msec']})
                interface_dict.update({'max_flood_scan_time_msec': group['max_flood_scan_time_msec']})

                # update interfaces_dict
                interfaces_dict.update(interface_dict)
                continue

            # Neighbor Count is 1, Adjacent neighbor count is 1
            m = p13.match(line)
            if m:
                group = m.groupdict()

                #define neighbor_statistics_dict dictionary and set to 'neighbors_statistics'
                neighbor_statistics_dict = interface_dict.setdefault('neighbors_statistics',{})

                #update neighbor_statistics_dict
                neighbor_statistics_dict.update({'neighbor_count': group['neighbor_count']})
                neighbor_statistics_dict.update({'adjacent_neighbor_count': group['adjacent_neighbor_count']})

                #update interfaces_dict
                interfaces_dict.update(interface_dict)
                continue

            # Adjacent with neighbor 100.100.100.100
            m = p14.match(line)
            if m:
                group = m.groupdict()

                #update neighbor_statistics_dict
                neighbor_statistics_dict.update({'adjacent_with_neighbor': group['adjacent_with_neighbor']})

                #update interfaces_dict
                interfaces_dict.update(interface_dict)                
                continue

            # Suppress hello for 0 neighbor(s)
            m = p15.match(line)
            if m:
                group = m.groupdict()

                #update neighbor_statistics_dict
                neighbor_statistics_dict.update({'num_nbrs_suppress_hello': group['num_nbrs_suppress_hello']})

                #update interfaces_dict
                interfaces_dict.update(interface_dict)                
                continue
            import pdb; pdb.set_trace()
            # Reference count is 6
            m = p16.match(line)
            if m:
                group = m.groupdict()

                #update neighbor_statistics_dict
                neighbor_statistics_dict.update({'refrence_count': group['refrence_count']})

                #update interfaces_dict
                interfaces_dict.update(interface_dict)    
                continue
            
            # Loopback interface is treated as a stub Host
            m = p17.match(line)
            if m:
                group = m.groupdict()

                # update interface_dict
                interface_dict.update({'loopback': group['loopback']})

                # update interfaces_dict
                interfaces_dict.update(interface_dict)
                continue

        return ret_dict
