''' show_ospf.py

IOSXR parsers for the following show commands:

    * show ospf vrf all-inclusive interface
    * show ospf vrf all-inclusive neighbor detail
    * show ospf vrf all-inclusive

    * show ospf mpls traffic-eng link
    * show ospf vrf all-inclusive sham-links
    * show ospf vrf all-inclusive virtual-links

    * show ospf vrf all-inclusive database router
    * show ospf vrf all-inclusive database network
    * show ospf vrf all-inclusive database summary
    * show ospf vrf all-inclusive database external
    * show ospf vrf all-inclusive database opaque-area
    * show ospf vrf all-inclusive database opaque-as
    * show ospf vrf all-inclusive database opaque-link
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
                                                'process_id': str,
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
            p4 = re.compile(r'^Process +ID +(?P<pid>(\S+))'
                             '(?:, +VRF +(?P<vrf>(\S+)))?'
                             ', +Router +ID +(?P<router_id>(\S+))'
                             ', +Network +Type +(?P<intf_type>(\S+))'
                             '(?:, +Cost: +(?P<cost>(\d+)))?$')
            m = p4.match(line)
            if m:
                sub_dict['process_id'] = str(m.groupdict()['pid'])
                sub_dict['router_id'] = str(m.groupdict()['router_id'])
                sub_dict['interface_type'] = str(m.groupdict()['intf_type'])
                if m.groupdict()['cost']:
                    sub_dict['cost'] = int(m.groupdict()['cost'])
                continue

            # Transmit Delay is 1 sec, State DR, Priority 1, MTU 1500, MaxPktSz 1500
            p5 = re.compile(r'^Transmit +Delay is +(?P<delay>(\d+)) +sec,'
                             ' +State +(?P<state>(\S+)),'
                             '(?: +Priority +(?P<priority>(\d+)),)?'
                             ' +MTU +(?P<mtu>(\d+)),'
                             ' +MaxPktSz +(?P<max_pkt_sz>(\d+))$')
            m = p5.match(line)
            if m:
                sub_dict['transmit_delay'] = int(m.groupdict()['delay'])
                sub_dict['state'] = str(m.groupdict()['state'])
                sub_dict['mtu'] = int(m.groupdict()['mtu'])
                sub_dict['max_pkt_sz'] = int(m.groupdict()['max_pkt_sz'])
                if m.groupdict()['priority']:
                    sub_dict['priority'] = int(m.groupdict()['priority'])
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


# ========================================
# Schema for 'show ospf vrf all-inclusive'
# ========================================
class ShowOspfVrfAllInclusiveSchema(MetaParser):

    ''' Schema for "show ospf vrf all-inclusive" '''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {'router_id': str,
                                'role': str,
                                'nsr': 
                                    {'enable': bool},
                                'stub_router': 
                                    {Optional('always'): 
                                        {'always': bool,
                                        'include_stub': bool,
                                        'summary_lsa': bool,
                                        'external_lsa': bool,
                                        Optional('duration'): int,
                                        Optional('state'): str},
                                    Optional('on_startup'): 
                                        {'on_startup': bool,
                                        'include_stub': bool,
                                        'summary_lsa': bool,
                                        'external_lsa':bool,
                                        Optional('duration'): int,
                                        Optional('state'): str},
                                    Optional('on_switchover'): 
                                        {'on_switchover': bool,
                                        'include_stub': bool,
                                        'summary_lsa': bool,
                                        'external_lsa': bool,
                                        Optional('duration'): int,
                                        Optional('state'): str},
                                    },
                                'spf_control': 
                                    {Optional('paths'): str,
                                    'throttle': 
                                        {'spf': 
                                            {'start': int,
                                            'hold': int,
                                            'maximum': int},
                                        'lsa': 
                                            {'start': int,
                                            'hold': int,
                                            'maximum': int,
                                            'interval': int,
                                            'arrival': int,
                                            'refresh_interval': int},
                                        },
                                    },
                                Optional('flood_pacing_interval'): int,
                                Optional('retransmission_interval'): int,
                                Optional('adjacency_stagger'): 
                                    {'disable': bool,
                                    'initial_number': int,
                                    'maximum_number': int},
                                Optional('numbers'): 
                                    {Optional('nbrs_forming'): int,
                                    Optional('nbrs_full'): int,
                                    Optional('configured_interfaces'): int,
                                    Optional('external_lsa'): int,
                                    Optional('external_lsa_checksum'): str,
                                    Optional('opaque_as_lsa'): int,
                                    Optional('opaque_as_lsa_checksum'): str,
                                    Optional('dc_bitless'): int,
                                    Optional('do_not_age'): int},
                                Optional('external_flood_list_length'): int,
                                Optional('snmp_trap'): bool,
                                Optional('lsd_state'): str,
                                Optional('lsd_revision'): int,
                                Optional('segment_routing_global_block_default'): str,
                                Optional('strict_spf_capability'): bool,
                                Optional('areas'): 
                                    {Any(): 
                                        {Optional('area_type'): str,
                                        Optional('rrr_enabled'): bool,
                                        Optional('topology_version'): int,
                                        Optional('statistics'): 
                                            {Optional('interfaces_count'): int,
                                            Optional('spf_runs_count'): int,
                                            Optional('area_scope_lsa_count'): int,
                                            Optional('area_scope_lsa_cksum_sum'): str,
                                            Optional('area_scope_opaque_lsa_count'): int,
                                            Optional('area_scope_opaque_lsa_cksum_sum'): str,
                                            Optional('dcbitless_lsa_count'): int,
                                            Optional('indication_lsa_count'): int,
                                            Optional('donotage_lsa_count'): int,
                                            Optional('flood_list_length'): int,
                                            Optional('lfa_interface_count'): int,
                                            Optional('lfa_revision'): int,
                                            Optional('lfa_per_prefix_interface_count'): int,
                                            Optional('nbrs_staggered_mode'): int,
                                            Optional('nbrs_full'): int},
                                        },
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

    ''' Parser for "show ospf vrf all-inclusive" '''

    def cli(self):

        # Execute command on device
        out = self.device.execute('show ospf vrf all-inclusive')

        # Init vars
        ret_dict = {}
        af = 'ipv4' # this is ospf - always ipv4

        for line in out.splitlines():
            line = line.strip()

            # Routing Process "ospf 1" with ID 3.3.3.3
            # VRF VRF1 in Routing Process "ospf 1" with ID 3.3.3.3
            p1 = re.compile(r'(?:^VRF +(?P<vrf>(\S+)) +in +)?Routing +Process'
                             ' +\"(?P<instance>([a-zA-Z0-9\s]+))\" +with +ID'
                             ' +(?P<router_id>(\S+))$')
            m = p1.match(line)
            if m:
                instance = str(m.groupdict()['instance'])
                router_id = str(m.groupdict()['router_id'])
                if m.groupdict()['vrf']:
                    vrf = str(m.groupdict()['vrf'])
                else:
                    vrf = 'default'

                # Set structure
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

                # Set sub_dict
                sub_dict = ret_dict['vrf'][vrf]['address_family'][af]\
                            ['instance'][instance]
                sub_dict['router_id'] = router_id
                continue

            # Role: Primary Active
            p2 = re.compile(r'^Role *: +(?P<role>([a-zA-z0-9\s]+))$')
            m = p2.match(line)
            if m:
                sub_dict['role'] = str(m.groupdict()['role']).lower()
                continue

            # NSR (Non-stop routing) is Enabled
            p3 = re.compile(r'^NSR +\(Non-stop routing\) +is +(?P<nsr>(\S+))$')
            m = p3.match(line)
            if m:
                nsr = str(m.groupdict()['nsr']).lower()
                if 'nsr' not in sub_dict:
                    sub_dict['nsr'] = {}
                if nsr == 'enabled':
                    sub_dict['nsr']['enable'] = True
                else:
                    sub_dict['nsr']['enable'] = False
                    continue

            # Supports only single TOS(TOS0) routes
            p3 = re.compile(r'^Supports +only +single +TOS(TOS0) routes$')
            m = p3.match(line)
            if m:
                # Not sure what the key is
                continue

            # Supports opaque LSA
            p4 = re.compile(r'^Supports +opaque +LSA$')
            m = p4.match(line)
            if m:
                # Not sure what the key is
                continue

            # It is an area border and autonomous system boundary router
            p5_0 = re.compile(r'^It +is +an +area +border +and +autonomous'
                               ' +system +boundary +router$')
            m = p5_0.match(line)
            if m:
                # Not sure whast the key is
                continue

            # Router is not originating router-LSAs with maximum metric
            p5_1 = re.compile(r'^Router +is +not +originating +router-LSAs'
                               ' +with +maximum +metric$')
            m = p5_1.match(line)
            if m:
                if 'stub_router' not in sub_dict:
                    sub_dict['stub_router'] = {}
                if 'always' not in sub_dict['stub_router']:
                    sub_dict['stub_router']['always'] = {}
                # Set values
                sub_dict['stub_router']['always']['always'] = False
                sub_dict['stub_router']['always']['include_stub'] = False
                sub_dict['stub_router']['always']['summary_lsa'] = False
                sub_dict['stub_router']['always']['external_lsa'] = False
                continue

            # Originating router-LSAs with maximum metric
            p5_2 = re.compile(r'^Originating +router-LSAs +with +maximum'
                               ' +metric$')
            m = p5_2.match(line)
            if m:
                if 'stub_router' not in sub_dict:
                    sub_dict['stub_router'] = {}
                    continue

            # Condition: always State: active
            # Condition: on switch-over for 10 seconds, State: inactive
            # Condition: on start-up for 5 seconds, State: inactive
            p5_3 = re.compile(r'^Condition:(?: +on)?'
                               ' +(?P<condition>([a-zA-Z\-]+))'
                               '(?: +for +(?P<seconds>(\d+)) +seconds,)?'
                               ' +State: +(?P<state>(\S+))$')
            m = p5_3.match(line)
            if m:
                condition = str(m.groupdict()['condition']).lower()
                if condition != 'always':
                    condition = "on_" + condition.replace("-", "")
                # Set keys
                if condition not in sub_dict['stub_router']:
                    sub_dict['stub_router'][condition] = {}
                sub_dict['stub_router'][condition][condition] = True
                if m.groupdict()['seconds']:
                    sub_dict['stub_router'][condition]['duration'] = \
                        int(m.groupdict()['seconds'])
                if m.groupdict()['state']:
                    sub_dict['stub_router'][condition]['state'] = \
                        str(m.groupdict()['state']).lower()
                continue

            # Advertise stub links with maximum metric in router-LSAs
            p5_4 = re.compile(r'^Advertise +stub +links +with +maximum +metric'
                               ' +in +router\-LSAs$')
            m = p5_4.match(line)
            if m:
                sub_dict['stub_router'][condition]['include_stub'] = True
                continue

            # Advertise summary-LSAs with metric 16711680
            p5_5 = re.compile(r'^Advertise +summary\-LSAs +with +metric'
                               ' +(?P<metric>(\d+))$')
            m = p5_5.match(line)
            if m:
                sub_dict['stub_router'][condition]['summary_lsa'] = True
                continue

            # Advertise external-LSAs with metric 16711680
            p5_6 = re.compile(r'^^Advertise +external\-LSAs +with +metric'
                               ' +(?P<metric>(\d+))$')
            m = p5_6.match(line)
            if m:
                sub_dict['stub_router'][condition]['external_lsa'] = True
                continue

            # Initial SPF schedule delay 50 msecs
            p6 = re.compile(r'^Initial +SPF +schedule +delay +(?P<time>(\S+))'
                             ' +msecs$')
            m = p6.match(line)
            if m:
                start = int(float(m.groupdict()['time']))
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'spf' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['spf'] = {}
                sub_dict['spf_control']['throttle']['spf']['start'] = start
                continue

            # Minimum hold time between two consecutive SPFs 200 msecs
            p7 = re.compile(r'^Minimum +hold +time +between +two +consecutive'
                             ' +SPFs +(?P<time>(\S+)) +msecs$')
            m = p7.match(line)
            if m:
                hold = int(float(m.groupdict()['time']))
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'spf' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['spf'] = {}
                sub_dict['spf_control']['throttle']['spf']['hold'] = hold
                continue

            # Maximum wait time between two consecutive SPFs 5000 msecs
            p8 = re.compile(r'^Maximum +wait +time +between +two +consecutive'
                             ' +SPFs +(?P<time>(\S+)) +msecs$')
            m = p8.match(line)
            if m:
                maximum = int(float(m.groupdict()['time']))
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'spf' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['spf'] = {}
                sub_dict['spf_control']['throttle']['spf']['maximum'] = maximum
                continue

            # Initial LSA throttle delay 50 msecs
            p9 = re.compile(r'^Initial +LSA +throttle +delay +(?P<time>(\S+))'
                             ' +msecs$')
            m = p9.match(line)
            if m:
                start = int(float(m.groupdict()['time']))
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'lsa' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['lsa'] = {}
                sub_dict['spf_control']['throttle']['lsa']['start'] = start
                continue

            # Minimum hold time for LSA throttle 200 msecs
            p10 = re.compile(r'^Minimum +hold +time +for +LSA +throttle'
                              ' +(?P<time>(\S+)) +msecs$')
            m = p10.match(line)
            if m:
                hold = int(float(m.groupdict()['time']))
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'lsa' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['lsa'] = {}
                sub_dict['spf_control']['throttle']['lsa']['hold'] = hold
                continue

            # Maximum wait time for LSA throttle 5000 msecs
            p11 = re.compile(r'^Maximum +wait +time +for +LSA +throttle'
                              ' +(?P<time>(\S+)) +msecs$')
            m = p11.match(line)
            if m:
                maximum = int(float(m.groupdict()['time']))
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'lsa' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['lsa'] = {}
                sub_dict['spf_control']['throttle']['lsa']['maximum'] = maximum
                continue

            # Minimum LSA interval 200 msecs. Minimum LSA arrival 100 msecs
            # Minimum LSA interval 200 msecs. Minimum LSA arrival 100 msecs
            p12 = re.compile(r'^Minimum +LSA +interval +(?P<interval>(\S+))'
                              ' +msecs. +Minimum +LSA +arrival'
                              ' +(?P<arrival>(\S+)) +msecs$')
            m = p12.match(line)
            if m:
                sub_dict['spf_control']['throttle']['lsa']['interval'] = \
                    int(float(m.groupdict()['interval']))
                sub_dict['spf_control']['throttle']['lsa']['arrival'] = \
                    int(float(m.groupdict()['arrival']))
                continue

            # LSA refresh interval 1800 seconds
            p13 = re.compile(r'^LSA +refresh +interval +(?P<refresh>(\S+))'
                              ' +seconds$')
            m = p13.match(line)
            if m:
                sub_dict['spf_control']['throttle']['lsa']\
                    ['refresh_interval'] = int(float(m.groupdict()['refresh']))
                continue

            # Flood pacing interval 33 msecs. Retransmission pacing interval 66 msecs
            p14 = re.compile(r'^Flood +pacing +interval +(?P<flood>(\d+))'
                              ' +msecs\. +Retransmission +pacing +interval'
                              ' +(?P<retransmission>(\d+)) +msecs$')
            m = p14.match(line)
            if m:
                sub_dict['flood_pacing_interval'] = \
                    int(float(m.groupdict()['flood']))
                sub_dict['retransmission_interval'] = \
                    int(float(m.groupdict()['retransmission']))
                continue

            # Adjacency stagger enabled; initial (per area): 2, maximum: 64
            p15 = re.compile(r'^Adjacency +stagger +(?P<adj>(\S+)); +initial'
                              ' +\(per +area\): +(?P<init>(\d+)),'
                              ' +maximum: +(?P<max>(\d+))$')
            m = p15.match(line)
            if m:
                if 'adjacency_stagger' not in sub_dict:
                    sub_dict['adjacency_stagger'] = {}
                if 'enable' in m.groupdict()['adj']:
                    sub_dict['adjacency_stagger']['disable'] = False
                else:
                    sub_dict['adjacency_stagger']['disable'] = True
                sub_dict['adjacency_stagger']['initial_number'] = \
                    int(m.groupdict()['init'])
                sub_dict['adjacency_stagger']['maximum_number'] = \
                    int(m.groupdict()['max'])
                continue

            # Number of neighbors forming: 0, 2 full
            p16 = re.compile(r'^Number +of +neighbors +forming:'
                              ' +(?P<form>(\d+)), +(?P<full>(\d+)) +full$')
            m = p16.match(line)
            if m:
                if 'numbers' not in sub_dict:
                    sub_dict['numbers'] = {}
                sub_dict['numbers']['nbrs_forming'] = int(m.groupdict()['form'])
                sub_dict['numbers']['nbrs_full'] = int(m.groupdict()['full'])
                continue

            # Maximum number of configured interfaces 1024
            p17 = re.compile(r'^Maximum +number +of +configured +interfaces'
                              ' +(?P<cfgd>(\d+))$')
            m = p17.match(line)
            if m:
                if 'numbers' not in sub_dict:
                    sub_dict['numbers'] = {}
                sub_dict['numbers']['configured_interfaces'] = \
                    int(m.groupdict()['cfgd'])
                continue

            # Number of external LSA 1. Checksum Sum 0x00607f
            p18 = re.compile(r'^Number +of +external +LSA +(?P<ext>(\d+))\.'
                              ' +Checksum +Sum +(?P<checksum>(\S+))$')
            m = p18.match(line)
            if m:
                if 'numbers' not in sub_dict:
                    sub_dict['numbers'] = {}
                sub_dict['numbers']['external_lsa'] = int(m.groupdict()['ext'])
                sub_dict['numbers']['external_lsa_checksum'] = \
                    str(m.groupdict()['checksum'])
                continue

            # Number of opaque AS LSA 0. Checksum Sum 00000000
            p19 = re.compile(r'^Number +of +opaque +AS +LSA +(?P<opq>(\d+))\.'
                              ' +Checksum +Sum +(?P<checksum>(\S+))$')
            m = p19.match(line)
            if m:
                if 'numbers' not in sub_dict:
                    sub_dict['numbers'] = {}
                sub_dict['numbers']['opaque_as_lsa'] = int(m.groupdict()['opq'])
                sub_dict['numbers']['opaque_as_lsa_checksum'] = \
                    str(m.groupdict()['checksum'])
                continue

            # Number of DCbitless external and opaque AS LSA 0
            p20 = re.compile(r'^Number +of +DCbitless +external +and +opaque'
                              ' +AS +LSA +(?P<num>(\d+))$')
            m = p20.match(line)
            if m:
                if 'numbers' not in sub_dict:
                    sub_dict['numbers'] = {}
                sub_dict['numbers']['dc_bitless'] = int(m.groupdict()['num'])
                continue

            # Number of DoNotAge external and opaque AS LSA 0
            p21 = re.compile(r'^Number +of +DoNotAge +external +and +opaque'
                              ' +AS +LSA +(?P<num>(\d+))$')
            m = p21.match(line)
            if m:
                if 'numbers' not in sub_dict:
                    sub_dict['numbers'] = {}
                sub_dict['numbers']['do_not_age'] = int(m.groupdict()['num'])
                continue

            # Number of areas in this router is 1. 1 normal 0 stub 0 nssa
            p22 = re.compile(r'^Number +of +areas +in +this +router +is'
                              ' +(?P<num_areas>(\d+))\. +(?P<normal>(\d+))'
                              ' +normal +(?P<stub>(\d+)) +stub +(?P<nssa>(\d+))'
                              ' +nssa$')
            m = p22.match(line)
            if m:
                num_areas = int(m.groupdict()['num_areas'])
                normal = int(m.groupdict()['normal'])
                stub = int(m.groupdict()['stub'])
                nssa = int(m.groupdict()['nssa'])
                if normal == 1:
                    area_type = 'normal'
                elif stub == 1:
                    area_type = 'stub'
                elif nssa == 1:
                    area_type = 'nssa'
                continue

            # External flood list length 0
            p23 = re.compile(r'^External +flood +list +length +(?P<num>(\d+))$')
            m = p23.match(line)
            if m:
                sub_dict['external_flood_list_length'] = int(m.groupdict()['num'])
                continue

            # SNMP trap is enabled
            p24 = re.compile(r'^SNMP +trap +is +(?P<snmp>(\S+))$')
            m = p24.match(line)
            if m:
                if 'enabled' in m.groupdict()['snmp']:
                    sub_dict['snmp_trap'] = True
                else:
                    sub_dict['snmp_trap'] = False
                continue

            # LSD connected, registered, bound, revision 1
            p25 = re.compile(r'^LSD +(?P<lsd>([a-zA-Z\,\s]+)), +revision'
                              ' +(?P<revision>(\d+))$')
            m = p25.match(line)
            if m:
                sub_dict['lsd_state'] = str(m.groupdict()['lsd'])
                sub_dict['lsd_revision'] = int(m.groupdict()['revision'])
                continue

            # Segment Routing Global Block default (16000-23999), not allocated
            p26 = re.compile(r'^Segment +Routing +Global +Block +default'
                              ' +\((?P<sr_block>([0-9\-]+))\), +not +allocated$')
            m = p26.match(line)
            if m:
                sub_dict['segment_routing_global_block_default'] = \
                    str(m.groupdict()['sr_block'])
                continue

            # Strict-SPF capability is enabled
            p27 = re.compile(r'^Strict-SPF +capability +is +(?P<state>(\S+))$')
            m = p27.match(line)
            if m:
                if 'enabled' in m.groupdict()['state']:
                    sub_dict['strict_spf_capability'] = True
                else:
                    sub_dict['strict_spf_capability'] = False
                continue

            # Area BACKBONE(0)
            p28 = re.compile(r'^Area +(?P<area>(\S+))$')
            m = p28.match(line)
            if m:
                area = str(m.groupdict()['area'])
                if 'areas' not in sub_dict:
                    sub_dict['areas'] = {}
                if area not in sub_dict['areas']:
                    sub_dict['areas'][area] = {}
                try:
                    sub_dict['areas'][area]['area_type'] = area_type
                except:
                    pass

            # Number of interfaces in this area is 3
            p29 = re.compile(r'^Number +of +interfaces +in +this +area +is'
                              ' +(?P<num_intf>(\d+))$')
            m = p29.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']['interfaces_count'] =\
                    int(m.groupdict()['num_intf'])
                continue

            # Area has RRR enabled, topology version 15
            p30 = re.compile(r'^Area +has +RRR +enabled, +topology +version'
                              ' +(?P<topo_version>(\d+))$')
            m = p30.match(line)
            if m:
                sub_dict['areas'][area]['rrr_enabled'] = True
                sub_dict['areas'][area]['topology_version'] = \
                    int(m.groupdict()['topo_version'])
                continue

            # SPF algorithm executed 26 times
            p31 = re.compile(r'^SPF +algorithm +executed +(?P<count>(\d+))'
                              ' +times$')
            m = p31.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']['spf_runs_count'] = \
                    int(m.groupdict()['count'])
                continue

            # Number of LSA 19.  Checksum Sum 0x0a2fb5
            p32 = re.compile(r'^Number +of +LSA +(?P<lsa_count>(\d+))\.'
                              ' +Checksum +Sum +(?P<checksum_sum>(\S+))$')
            m = p32.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']['area_scope_lsa_count'] =\
                    int(m.groupdict()['lsa_count'])
                sub_dict['areas'][area]['statistics']\
                    ['area_scope_lsa_cksum_sum'] = \
                        str(m.groupdict()['checksum_sum'])
                continue

            # Number of opaque link LSA 0.  Checksum Sum 00000000
            p33 = re.compile(r'^Number +of opaque +link +LSA'
                              ' +(?P<opaque_count>(\d+))\. +Checksum +Sum'
                              ' +(?P<checksum_sum>(\S+))$')
            m = p33.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']\
                    ['area_scope_opaque_lsa_count'] = \
                        int(m.groupdict()['opaque_count'])
                sub_dict['areas'][area]['statistics']\
                    ['area_scope_opaque_lsa_cksum_sum'] = \
                        str(m.groupdict()['checksum_sum'])
                continue

            # Number of DCbitless LSA 5
            p34 = re.compile(r'^Number +of +DCbitless +LSA +(?P<count>(\d+))$')
            m = p34.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']['dcbitless_lsa_count'] = \
                    int(m.groupdict()['count'])
                continue

            # Number of indication LSA 0
            p35 = re.compile(r'^Number +of +indication +LSA +(?P<count>(\d+))$')
            m = p35.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']['indication_lsa_count'] =\
                    int(m.groupdict()['count'])
                continue

            # Number of DoNotAge LSA 0
            p36 = re.compile(r'^Number +of +DoNotAge +LSA +(?P<count>(\d+))$')
            m = p36.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']['donotage_lsa_count'] = \
                    int(m.groupdict()['count'])
                continue

            # Flood list length 0
            p37 = re.compile(r'^Flood +list +length +(?P<len>(\d+))$')
            m = p37.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']['flood_list_length'] = \
                    int(m.groupdict()['len'])
                continue

            # Number of LFA enabled interfaces 0, LFA revision 0
            p38 = re.compile(r'^Number +of +LFA +enabled +interfaces'
                              ' +(?P<count>(\d+)), +LFA +revision'
                              ' +(?P<revision>(\d+))$')
            m = p38.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']['lfa_interface_count'] = \
                    int(m.groupdict()['count'])
                sub_dict['areas'][area]['statistics']['lfa_revision'] = \
                    int(m.groupdict()['revision'])
                continue

            # Number of Per Prefix LFA enabled interfaces 0
            p39 = re.compile(r'^Number +of +Per +Prefix +LFA +enabled'
                              ' +interfaces +(?P<count>(\d+))$')
            m = p39.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']\
                    ['lfa_per_prefix_interface_count'] = \
                        int(m.groupdict()['count'])
                continue

            # Number of neighbors forming in staggered mode 0, 2 full
            p40 = re.compile(r'^Number +of +neighbors +forming +in +staggered'
                              ' +mode +(?P<mode>(\d+)), +(?P<full>(\d+)) +full$')
            m = p40.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']['nbrs_staggered_mode'] = \
                    int(m.groupdict()['mode'])
                sub_dict['areas'][area]['statistics']['nbrs_full'] = \
                    int(m.groupdict()['full'])
                continue

        return ret_dict


# ============================================
# Schema for 'show ospf mpls traffic-eng link'
# ============================================
class ShowOspfMplsTrafficEngLinkSchema(MetaParser):

    ''' Schema for 'show ospf mpls traffic-eng link' '''

    schema = {}


# ============================================
# Parser for 'show ospf mpls traffic-eng link'
# ============================================
class ShowOspfMplsTrafficEngLink(ShowOspfMplsTrafficEngLinkSchema):

    ''' Parser for 'show ospf mpls traffic-eng link' '''

    pass


# ======================================================
# Schema for 'show ospf vrf all-inclusive virtual-links'
# ======================================================
class ShowOspfVrfAllInclusiveVirtualLinksSchema(MetaParser):

    ''' Schema for 'show ospf vrf all-inclusive virtual-links' '''

    schema = {}


# ======================================================
# Parser for 'show ospf vrf all-inclusive virtual-links'
# ======================================================
class ShowOspfVrfAllInclusiveVirtualLinks(ShowOspfVrfAllInclusiveVirtualLinksSchema):

    ''' Parser for 'show ospf vrf all-inclusive virtual-links' '''

    pass


# ===================================================
# Schema for 'show ospf vrf all-inclusive sham-links'
# ===================================================
class ShowOspfVrfAllInclusiveShamLinksSchema(MetaParser):

    ''' Schema for 'show ospf vrf all-inclusive sham-links' '''

    schema = {}


# ======================================================
# Parser for 'show ospf vrf all-inclusive sham-links'
# ======================================================
class ShowOspfVrfAllInclusiveShamLinks(ShowOspfVrfAllInclusiveShamLinksSchema):

    ''' Parser for 'show ospf vrf all-inclusive sham-links' '''

    pass


# ========================================================
# Schema for 'show ospf vrf all-inclusive database router'
# ========================================================
class ShowOspfVrfAllInclusiveDatabaseRouterSchema(MetaParser):

    ''' Schema for 'show ospf vrf all-inclusive database router' '''

    schema = {}


# ========================================================
# Parser for 'show ospf vrf all-inclusive database router'
# ========================================================
class ShowOspfVrfAllInclusiveDatabaseRouter(ShowOspfVrfAllInclusiveDatabaseRouterSchema):

    ''' Parser for 'show ospf vrf all-inclusive database router' '''

    pass

# =========================================================
# Schema for 'show ospf vrf all-inclusive database network'
# =========================================================
class ShowOspfVrfAllInclusiveDatabaseNetworkSchema(MetaParser):

    ''' Schema for 'show ospf vrf all-inclusive database network' '''

    schema = {}


# =========================================================
# Parser for 'show ospf vrf all-inclusive database network'
# =========================================================
class ShowOspfVrfAllInclusiveDatabaseNetwork(ShowOspfVrfAllInclusiveDatabaseNetworkSchema):

    ''' Parser for 'show ospf vrf all-inclusive database network' '''

    pass


# =========================================================
# Schema for 'show ospf vrf all-inclusive database summary'
# =========================================================
class ShowOspfVrfAllInclusiveDatabaseSummarySchema(MetaParser):

    ''' Schema for 'show ospf vrf all-inclusive database summary' '''

    schema = {}


# =========================================================
# Parser for 'show ospf vrf all-inclusive database summary'
# =========================================================
class ShowOspfVrfAllInclusiveDatabaseSummary(ShowOspfVrfAllInclusiveDatabaseSummarySchema):

    ''' Parser for 'show ospf vrf all-inclusive database summary' '''

    pass


# ==========================================================
# Schema for 'show ospf vrf all-inclusive database external'
# ==========================================================
class ShowOspfVrfAllInclusiveDatabaseExternalSchema(MetaParser):

    ''' Schema for 'show ospf vrf all-inclusive database external' '''

    schema = {}


# ==========================================================
# Parser for 'show ospf vrf all-inclusive database external'
# ==========================================================
class ShowOspfVrfAllInclusiveDatabaseExternal(ShowOspfVrfAllInclusiveDatabaseExternalSchema):

    ''' Parser for 'show ospf vrf all-inclusive database external' '''

    pass


# =============================================================
# Schema for 'show ospf vrf all-inclusive database opaque-area'
# =============================================================
class ShowOspfVrfAllInclusiveDatabaseOpaqueAreaSchema(MetaParser):

    ''' Schema for 'show ospf vrf all-inclusive database opaque-area' '''

    schema = {}


# =============================================================
# Parser for 'show ospf vrf all-inclusive database opaque-area'
# =============================================================
class ShowOspfVrfAllInclusiveDatabaseOpaqueArea(ShowOspfVrfAllInclusiveDatabaseOpaqueAreaSchema):

    ''' Parser for 'show ospf vrf all-inclusive database opaque-area' '''

    pass


# ===========================================================
# Schema for 'show ospf vrf all-inclusive database opaque-as'
# ===========================================================
class ShowOspfVrfAllInclusiveDatabaseOpaqueAsSchema(MetaParser):

    ''' Schema for 'show ospf vrf all-inclusive database opaque-as' '''

    schema = {}


# ===========================================================
# Parser for 'show ospf vrf all-inclusive database opaque-as'
# ===========================================================
class ShowOspfVrfAllInclusiveDatabaseOpaqueAs(ShowOspfVrfAllInclusiveDatabaseOpaqueAsSchema):

    ''' Parser for 'show ospf vrf all-inclusive database opaque-as' '''

    pass


# =============================================================
# Schema for 'show ospf vrf all-inclusive database opaque-link'
# =============================================================
class ShowOspfVrfAllInclusiveDatabaseOpaqueLinkSchema(MetaParser):

    ''' Schema for 'show ospf vrf all-inclusive database opaque-link' '''

    schema = {}


# =============================================================
# Parser for 'show ospf vrf all-inclusive database opaque-link'
# =============================================================
class ShowOspfVrfAllInclusiveDatabaseOpaqueLink(ShowOspfVrfAllInclusiveDatabaseOpaqueLinkSchema):

    ''' Parser for 'show ospf vrf all-inclusive database opaque-link' '''

    pass