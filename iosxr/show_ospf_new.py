''' show_ospf.py

IOSXR parsers for the following show commands:

Completed:
    * show ospf vrf all-inclusive interface
    * show ospf vrf all-inclusive neighbor detail
'''

# Python
import re
import xmltodict

# Metaparser
from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, Any, Or, Optional
from parser.utils.common import Common


# ==================================================
# Schema for 'show ospf vrf all-inclusive interface'
# ==================================================
class ShowOspfVrfAllInclusiveInterfaceSchema(MetaParser):

    ''' Schema for "show ospf vrf all-inclusive interface" '''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {'areas': 
                                    {Any(): 
                                        {'interfaces': 
                                            {Any(): 
                                                {'name': str,
                                                'enable': bool,
                                                'line_protocol': bool,
                                                'ip_address': str,
                                                'demand_circuit': bool,
                                                'process_id': int,
                                                'router_id': str,
                                                'interface_type': str,
                                                'bfd': 
                                                    {'enable': bool,
                                                    Optional('interval'): int,
                                                    Optional('min_interval'): int,
                                                    Optional('multiplier'): int,
                                                    Optional('mode'): str,
                                                    },
                                                Optional('cost'): int,
                                                Optional('transmit_delay'): int,
                                                Optional('state'): str,
                                                Optional('priority'): int,
                                                Optional('mtu'): int,
                                                Optional('max_pkt_sz'): int,
                                                Optional('dr_router_id'): str,
                                                Optional('dr_ip_addr'): str,
                                                Optional('bdr_router_id'): str,
                                                Optional('bdr_ip_addr'): str,
                                                Optional('hello_interval'): int,
                                                Optional('dead_interval'): int,
                                                Optional('wait_interval'): int,
                                                Optional('retransmit_interval'): int,
                                                Optional('passive'): bool,
                                                Optional('hello_due_in'): str,
                                                Optional('index'): str,
                                                Optional('flood_queue_length'): int,
                                                Optional('next'): str,
                                                Optional('last_flood_scan_length'): int,
                                                Optional('max_flood_scan_length'): int,
                                                Optional('last_flood_scan_time_msec'): int,
                                                Optional('max_flood_scan_time_msec'): int,
                                                Optional('ls_ack_list'): str,
                                                Optional('ls_ack_list_length'): int,
                                                Optional('high_water_mark'): int,
                                                Optional('nbr_count'): int,
                                                Optional('adj_nbr_count'): int,
                                                Optional('adj_nbr'): str,
                                                Optional('num_nbrs_suppress_hello'): int,
                                                Optional('multi_area_intf_count'): int,
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

    ''' Parser for "show ospf vrf all-inclusive interface" '''

    def cli(self):

        # Execute command on device
        out = self.device.execute('show ospf vrf all-inclusive interface')

        # Init vars
        ret_dict = {}
        af = 'ipv4' # this is ospf - always ipv4

        # Mapping dict
        bool_dict = {'up': True, 'down': False, 'unknown': False}

        for line in out.splitlines():
            line = line.strip()

            # Interfaces for OSPF 1, VRF VRF1
            p1 = re.compile(r'^Interfaces +for +OSPF +(?P<instance>(\S+))'
                             '(?:, +VRF +(?P<vrf>(\S+)))?$')
            m = p1.match(line)
            if m:
                instance = str(m.groupdict()['instance'])
                if m.groupdict()['vrf']:
                    vrf = str(m.groupdict()['vrf'])
                else:
                    vrf = 'default'
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}
                if 'address_family' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['address_family'] = {}
                if af not in ret_dict['vrf'][vrf]['address_family']:
                    ret_dict['vrf'][vrf]['address_family'][af] = {}
                if 'instance' not in ret_dict['vrf'][vrf]['address_family'][af]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance'] = {}
                if instance not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance] = {}
                    continue

            # GigabitEthernet0/0/0/2 is up, line protocol is up
            p2 = re.compile(r'^(?P<interface>(\S+)) +is'
                             ' +(?P<enable>(unknown|up|down)), +line +protocol'
                             ' +is +(?P<line_protocol>(up|down))$')
            m = p2.match(line)
            if m:
                interface = str(m.groupdict()['interface'])
                enable = str(m.groupdict()['enable'])
                line_protocol = str(m.groupdict()['line_protocol'])
                continue

            # Internet Address 10.2.3.3/24, Area 0
            p3 = re.compile(r'^Internet +Address +(?P<address>(\S+)),'
                             ' +Area +(?P<area>(\S+))$')
            m = p3.match(line)
            if m:
                area = str(m.groupdict()['area'])
                if 'areas' not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'] = {}
                if area not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area] = {}
                if 'interfaces' not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]['areas'][area]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['interfaces'] = {}
                if interface not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area]['interfaces']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['interfaces'][interface] = {}
                # Set sub_dict
                sub_dict = ret_dict['vrf'][vrf]['address_family'][af]\
                            ['instance'][instance]['areas'][area]\
                            ['interfaces'][interface]
                # Set keys
                sub_dict['ip_address'] = str(m.groupdict()['address'])
                sub_dict['demand_circuit'] = False
                if 'bfd' not in sub_dict:
                    sub_dict['bfd'] = {}
                sub_dict['bfd']['enable'] = False
                try:
                    sub_dict['name'] = interface
                    sub_dict['enable'] = bool_dict[enable]
                    sub_dict['line_protocol'] = bool_dict[line_protocol]
                except:
                    pass

            # Process ID 1, Router ID 3.3.3.3, Network Type POINT_TO_POINT
            # Process ID 1, Router ID 3.3.3.3, Network Type BROADCAST, Cost: 1
            # Process ID 1, VRF VRF1, Router ID 3.3.3.3, Network Type SHAM_LINK, Cost: 111
            p4 = re.compile(r'^Process +ID +(?P<pid>(\d+))'
                             '(?:, +VRF +(?P<vrf>(\S+)))?'
                             ', +Router +ID +(?P<router_id>(\S+))'
                             ', +Network +Type +(?P<intf_type>(\S+))'
                             '(?:, +Cost: +(?P<cost>(\d+)))?$')
            m = p4.match(line)
            if m:
                sub_dict['process_id'] = int(m.groupdict()['pid'])
                sub_dict['router_id'] = str(m.groupdict()['router_id'])
                sub_dict['interface_type'] = str(m.groupdict()['intf_type'])
                if m.groupdict()['cost']:
                    sub_dict['cost'] = int(m.groupdict()['cost'])
                continue

            # Transmit Delay is 1 sec, State DR, Priority 1, MTU 1500, MaxPktSz 1500
            p5 = re.compile(r'^Transmit +Delay is +(?P<delay>(\d+))'
                             ' +sec, +State +(?P<state>(\S+)), +Priority'
                             ' +(?P<priority>(\d+)), +MTU +(?P<mtu>(\d+)),'
                             ' +MaxPktSz +(?P<max_pkt_sz>(\d+))$')
            m = p5.match(line)
            if m:
                sub_dict['transmit_delay'] = int(m.groupdict()['delay'])
                sub_dict['state'] = str(m.groupdict()['state'])
                sub_dict['priority'] = int(m.groupdict()['priority'])
                sub_dict['mtu'] = int(m.groupdict()['mtu'])
                sub_dict['max_pkt_sz'] = int(m.groupdict()['max_pkt_sz'])
                continue

            # Designated Router (ID) 3.3.3.3, Interface address 10.2.3.3
            p6 = re.compile(r'^Designated +Router +\(ID\)'
                             ' +(?P<dr_router_id>(\S+)), +Interface +address'
                             ' +(?P<dr_ip_addr>(\S+))$')
            m = p6.match(line)
            if m:
                sub_dict['dr_router_id'] = str(m.groupdict()['dr_router_id'])
                sub_dict['dr_ip_addr'] = str(m.groupdict()['dr_ip_addr'])
                continue

            # Backup Designated router (ID) 2.2.2.2, Interface address 10.2.3.2
            p7 = re.compile(r'^Backup +Designated +Router +\(ID\)'
                             ' +(?P<bdr_router_id>(\S+)), +Interface +address'
                             ' +(?P<bdr_ip_addr>(\S+))$')
            m = p7.match(line)
            if m:
                sub_dict['bdr_router_id'] = str(m.groupdict()['bdr_router_id'])
                sub_dict['bdr_ip_addr'] = str(m.groupdict()['bdr_ip_addr'])
                continue

            # Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
            p8 = re.compile(r'^Timer +intervals +configured,'
                             ' +Hello +(?P<hello>(\d+)),'
                             ' +Dead +(?P<dead>(\d+)),'
                             ' +Wait +(?P<wait>(\d+)),'
                             ' +Retransmit +(?P<retransmit>(\d+))$')
            m = p8.match(line)
            if m:
                sub_dict['hello_interval'] = int(m.groupdict()['hello'])
                sub_dict['dead_interval'] = int(m.groupdict()['dead'])
                sub_dict['wait_interval'] = int(m.groupdict()['wait'])
                sub_dict['retransmit_interval'] = int(m.groupdict()['retransmit'])
                continue

            # Hello due in 00:00:07:587
            p9_1 = re.compile(r'^Hello +due +in +(?P<hello_due>(\S+))$')
            m = p9_1.match(line)
            if m:
                sub_dict['passive'] = False
                sub_dict['hello_due_in'] = str(m.groupdict()['hello_due'])
                continue

            # No Hellos (Passive interface)
            p9_2 = re.compile(r'^No +Hellos +\(Passive +interface\)$')
            m = p9_2.match(line)
            if m:
                sub_dict['passive'] = True
                continue

            # Index 2/2, flood queue length 0
            p10 = re.compile(r'^Index +(?P<index>(\S+)),'
                               ' +flood +queue +length +(?P<length>(\d+))$')
            m = p10.match(line)
            if m:
                sub_dict['index'] = str(m.groupdict()['index'])
                sub_dict['flood_queue_length'] = int(m.groupdict()['length'])
                continue

            # Next 0(0)/0(0)
            p11 = re.compile(r'^Next +(?P<next>(\S+))$')
            m = p11.match(line)
            if m:
                sub_dict['next'] = str(m.groupdict()['next'])
                continue

            # Last flood scan length is 1, maximum is 3
            p11 = re.compile(r'^Last +flood +scan +length +is +(?P<num>(\d+)),'
                              ' +maximum +is +(?P<max>(\d+))$')
            m = p11.match(line)
            if m:
                sub_dict['last_flood_scan_length'] = int(m.groupdict()['num'])
                sub_dict['max_flood_scan_length'] = int(m.groupdict()['max'])
                continue

            # Last flood scan time is 0 msec, maximum is 0 msec
            p12 = re.compile(r'^Last +flood +scan +time +is +(?P<time1>(\d+))'
                              ' +msec, +maximum +is +(?P<time2>(\d+)) +msec$')
            m = p12.match(line)
            if m:
                sub_dict['last_flood_scan_time_msec'] = \
                    int(m.groupdict()['time1'])
                sub_dict['max_flood_scan_time_msec'] = \
                    int(m.groupdict()['time2'])
                continue

            # LS Ack List: current length 0, high water mark 7
            p13 = re.compile(r'^LS +Ack +List: +(?P<ls_ack_list>(\S+)) +length'
                              ' +(?P<num>(\d+)), +high +water +mark'
                              ' +(?P<num2>(\d+))$')
            m = p13.match(line)
            if m:
                sub_dict['ls_ack_list'] = str(m.groupdict()['ls_ack_list'])
                sub_dict['ls_ack_list_length'] = int(m.groupdict()['num'])
                sub_dict['high_water_mark'] = int(m.groupdict()['num2'])
                continue

            # Neighbor Count is 1, Adjacent neighbor count is 1
            p14 = re.compile(r'^Neighbor +Count +is +(?P<nbr_count>(\d+)),'
                              ' +Adjacent +neighbor +count +is'
                              ' +(?P<adj_nbr_count>(\d+))$')
            m = p14.match(line)
            if m:
                sub_dict['nbr_count'] = int(m.groupdict()['nbr_count'])
                sub_dict['adj_nbr_count'] = int(m.groupdict()['adj_nbr_count'])
                continue

            # Adjacent with neighbor 2.2.2.2  (Backup Designated Router)
            p15 = re.compile(r'^Adjacent +with +neighbor +(?P<adj_nbr>(\S+))'
                              ' +\(.*\)$')
            m = p15.match(line)
            if m:
                sub_dict['adj_nbr'] = str(m.groupdict()['adj_nbr'])
                continue

            # Suppress hello for 0 neighbor(s)
            p16 = re.compile(r'^Suppress +hello +for +(?P<sup>(\d+))'
                              ' +neighbor\(s\)$')
            m = p16.match(line)
            if m:
                sub_dict['num_nbrs_suppress_hello'] = int(m.groupdict()['sup'])
                continue

            # Multi-area interface Count is 0
            p17 = re.compile(r'^Multi-area +interface +Count +is'
                              ' +(?P<count>(\d+))$')
            m = p17.match(line)
            if m:
                sub_dict['multi_area_intf_count'] = int(m.groupdict()['count'])
                continue

            # Configured as demand circuit.
            p18 = re.compile(r'^Configured as demand circuit\.$')
            m = p18.match(line)
            if m:
                sub_dict['demand_circuit'] = True
                continue

            # Run as demand circuit.
            p19 = re.compile(r'^Run as demand circuit\.$')
            m = p19.match(line)
            if m:
                sub_dict['demand_circuit'] = True

            # DoNotAge LSA not allowed (Number of DCbitless LSA is 1).
            p20 = re.compile(r'^DoNotAge LSA not allowed \(.*\)\.$')
            m = p20.match(line)
            if m:
                sub_dict['demand_circuit'] = True

            # BFD enabled, BFD interval 12345 msec, BFD multiplier 50, Mode: Default
            p21 = re.compile(r'^BFD enabled'
                              '(?:, +BFD +interval +(?P<interval>(\d+)) +msec)?'
                              '(?:, +BFD +multiplier +(?P<multi>(\d+)))?'
                              '(?:, +Mode: +(?P<mode>(\S+)))?$')
            m = p21.match(line)
            if m:
                sub_dict['bfd']['enable'] = True
                if m.groupdict()['interval']:
                    sub_dict['bfd']['interval'] = int(m.groupdict()['interval'])
                if m.groupdict()['multi']:
                    sub_dict['bfd']['multiplier'] = int(m.groupdict()['multi'])
                if m.groupdict()['mode']:
                    sub_dict['bfd']['mode'] = str(m.groupdict()['mode'])
                    continue

        return ret_dict


# ========================================================
# Schema for 'show ospf vrf all-inclusive neighbor detail'
# ========================================================
class ShowOspfVrfAllInclusiveNeighborDetailSchema(MetaParser):

    ''' Schema for "show ospf vrf all-inclusive neighbor detail" '''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {'total_neighbor_count': int,
                                'areas': 
                                    {Any(): 
                                        {'interfaces': 
                                            {Any(): 
                                                {'neighbors': 
                                                    {Any(): 
                                                        {'neighbor_router_id': str,
                                                        'address': str,
                                                        'priority': int,
                                                        'state': str,
                                                        'num_state_changes': int,
                                                        'dr_ip_addr': str,
                                                        'bdr_ip_addr': str,
                                                        Optional('options'): str,
                                                        Optional('lls_options'): str,
                                                        Optional('dead_timer'): str,
                                                        Optional('neighbor_uptime'): str,
                                                        Optional('dbd_retrans'): int,
                                                        Optional('index'): str,
                                                        Optional('retransmission_queue_length'): int,
                                                        Optional('num_retransmission'): int,
                                                        Optional('first'): str,
                                                        Optional('next'): str,
                                                        Optional('last_retrans_scan_length'): int,
                                                        Optional('last_retrans_max_scan_length'): int,
                                                        Optional('last_retrans_scan_time_msec'): int,
                                                        Optional('last_retrans_max_scan_time_msec'): int,
                                                        Optional('ls_ack_list'): str,
                                                        Optional('ls_ack_list_pending'): int,
                                                        Optional('high_water_mark'): int,
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
class ShowOspfVrfAllInclusiveNeighborDetail(ShowOspfVrfAllInclusiveNeighborDetailSchema):

    ''' Parser for "show ospf vrf all-inclusive neighbor detail" '''

    def cli(self):

        # Execute command on device
        out = self.device.execute('show ospf vrf all-inclusive neighbor detail')

        # Init vars
        ret_dict = {}
        af = 'ipv4' # this is ospf - always ipv4

        for line in out.splitlines():
            line = line.strip()

            # Neighbors for OSPF 1
            # Neighbors for OSPF 1, VRF VRF1
            p1 = re.compile(r'^Neighbors +for +OSPF +(?P<instance>(\S+))'
                             '(?:, +VRF +(?P<vrf>(\S+)))?$')
            m = p1.match(line)
            if m:
                instance = str(m.groupdict()['instance'])
                if m.groupdict()['vrf']:
                    vrf = str(m.groupdict()['vrf'])
                else:
                    vrf = 'default'
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}
                if 'address_family' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['address_family'] = {}
                if af not in ret_dict['vrf'][vrf]['address_family']:
                    ret_dict['vrf'][vrf]['address_family'][af] = {}
                if 'instance' not in ret_dict['vrf'][vrf]['address_family'][af]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance'] = {}
                if instance not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance] = {}
                    continue

            # Neighbor 2.2.2.2, interface address 10.2.3.2
            p2 = re.compile(r'^Neighbor +(?P<neighbor>(\S+)), +interface'
                             ' +address +(?P<address>(\S+))$')
            m = p2.match(line)
            if m:
                neighbor = str(m.groupdict()['neighbor'])
                address = str(m.groupdict()['address'])
                continue

            # In the area 0 via interface GigabitEthernet0/0/0/2 
            p3 = re.compile(r'^In +the +area +(?P<area>(\S+)) +via +interface'
                             ' +(?P<intf>(\S+))$')
            m = p3.match(line)
            if m:
                area = str(m.groupdict()['area'])
                interface = str(m.groupdict()['intf'])
                if 'areas' not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'] = {}
                if area not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area] = {}
                if 'interfaces' not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]['areas'][area]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['interfaces'] = {}
                if interface not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area]['interfaces']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['interfaces'][interface] = {}
                if 'neighbors' not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]['areas'][area]['interfaces']\
                        [interface]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['interfaces'][interface]\
                        ['neighbors'] = {}
                if neighbor not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]['areas'][area]['interfaces']\
                        [interface]['neighbors']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['interfaces'][interface]\
                        ['neighbors'][neighbor] = {}
                # Set sub_dict
                sub_dict = ret_dict['vrf'][vrf]['address_family'][af]\
                            ['instance'][instance]['areas'][area]['interfaces']\
                            [interface]['neighbors'][neighbor]
                sub_dict['neighbor_router_id'] = neighbor
                sub_dict['address'] = address
                continue

            # Neighbor priority is 1, State is FULL, 6 state changes
            p4 = re.compile(r'^Neighbor +priority +is +(?P<priority>(\d+)),'
                             ' +State +is +(?P<state>(\S+)),'
                             ' +(?P<num>(\d+)) +state +changes$')
            m = p4.match(line)
            if m:
                sub_dict['priority'] = int(m.groupdict()['priority'])
                sub_dict['state'] = str(m.groupdict()['state'])
                sub_dict['num_state_changes'] = int(m.groupdict()['num'])
                continue

            # DR is 10.2.3.3 BDR is 10.2.3.2
            p5 = re.compile(r'^DR +is +(?P<dr_ip_addr>(\S+))'
                             ' +BDR +is +(?P<bdr_ip_addr>(\S+))$')
            m = p5.match(line)
            if m:
                sub_dict['dr_ip_addr'] = str(m.groupdict()['dr_ip_addr'])
                sub_dict['bdr_ip_addr'] = str(m.groupdict()['bdr_ip_addr'])
                continue

            # Options is 0x42
            p6_1 = re.compile(r'^Options +is +(?P<options>(\S+))$')
            m = p6_1.match(line)
            if m:
                sub_dict['options'] = str(m.groupdict()['options'])
                continue

            # LLS Options is 0x1 (LR)
            p6_2 = re.compile(r'^LLS +Options +is +(?P<lls_options>(.*))$')
            m = p6_2.match(line)
            if m:
                sub_dict['lls_options'] = str(m.groupdict()['lls_options'])
                continue

            # Dead timer due in 00:00:38
            p7 = re.compile(r'^Dead +timer +due +in +(?P<dead_timer>(\S+))$')
            m = p7.match(line)
            if m:
                sub_dict['dead_timer'] = str(m.groupdict()['dead_timer'])
                continue

            # Neighbor is up for 08:22:07
            p8 = re.compile(r'^Neighbor +is +up +for +(?P<uptime>(\S+))$')
            m = p8.match(line)
            if m:
                sub_dict['neighbor_uptime'] = str(m.groupdict()['uptime'])
                continue

            # Number of DBD retrans during last exchange 0
            p9 = re.compile(r'^Number +of +DBD +retrans +during +last'
                             ' +exchange +(?P<dbd_retrans>(\d+))$')
            m = p9.match(line)
            if m:
                sub_dict['dbd_retrans'] = int(m.groupdict()['dbd_retrans'])
                continue

            # Index 1/1, retransmission queue length 0, number of retransmission 0
            p10 = re.compile(r'^Index +(?P<index>(\S+)) +retransmission +queue'
                             ' +length +(?P<ql>(\d+)), +number +of'
                             ' +retransmission +(?P<num_retrans>(\d+))$')
            m = p10.match(line)
            if m:
                sub_dict['index'] = str(m.groupdict()['index'])
                sub_dict['retransmission_queue_length'] = \
                    int(m.groupdict()['ql'])
                sub_dict['num_retransmission'] = \
                    int(m.groupdict()['num_retrans'])
                continue

            # First 0(0)/0(0) Next 0(0)/0(0)
            p11 = re.compile(r'^First +(?P<first>(\S+)) +Next +(?P<next>(\S+))$')
            m = p11.match(line)
            if m:
                sub_dict['first'] = str(m.groupdict()['first'])
                sub_dict['next'] = str(m.groupdict()['next'])
                continue

            # Last retransmission scan length is 0, maximum is 0
            p12 = re.compile(r'^Last +retransmission +scan +length +is'
                              ' +(?P<num1>(\d+)), +maximum +is'
                              ' +(?P<num2>(\d+))$')
            m = p12.match(line)
            if m:
                sub_dict['last_retrans_scan_length'] = \
                    int(m.groupdict()['num1'])
                sub_dict['last_retrans_max_scan_length'] = \
                    int(m.groupdict()['num2'])
                continue

            # Last retransmission scan time is 0 msec, maximum is 0 msec
            p13 = re.compile(r'^Last +retransmission +scan +time +is'
                              ' +(?P<num1>(\d+)) +msec, +maximum +is'
                              ' +(?P<num2>(\d+)) +msec$')
            m = p13.match(line)
            if m:
                sub_dict['last_retrans_scan_time_msec'] = \
                    int(m.groupdict()['num1'])
                sub_dict['last_retrans_max_scan_time_msec'] = \
                    int(m.groupdict()['num2'])
                continue

            # LS Ack list: NSR-sync pending 0, high water mark 0
            p14 = re.compile(r'^LS +Ack +list: +(?P<ls_ack_list>(\S+))'
                              ' +pending +(?P<pending>(\d+)), +high +water'
                              ' +mark +(?P<mark>(\d+))$')
            m = p14.match(line)
            if m:
                sub_dict['ls_ack_list'] = str(m.groupdict()['ls_ack_list'])
                sub_dict['ls_ack_list_pending'] = int(m.groupdict()['pending'])
                sub_dict['high_water_mark'] = int(m.groupdict()['mark'])
                continue

            # Total neighbor count: 2
            p15 = re.compile(r'^Total +neighbor +count: +(?P<num>(\d+))$')
            m = p15.match(line)
            if m:
                ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                    [instance]['total_neighbor_count'] = \
                        int(m.groupdict()['num'])

        return ret_dict
