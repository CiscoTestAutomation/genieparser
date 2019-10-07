"""
show_isis.py

IOSXR parsers for the following show commands:
    * show isis adjacency
    * show isis neighbors

"""

# Python
import re
from netaddr import IPAddress, IPNetwork

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional
from genie.libs.parser.utils.common import Common


#==================================
# Schema for 'show isis adjacency'
#==================================
class ShowIsisAdjacencySchema(MetaParser):
    """Schema for show run isis adjacency"""

    schema = {
        'isis': {
            Any(): {
                'vrf': {
                    Any(): {
                        'level': {
                            Any(): {
                                Optional('total_adjacency_count'): int,
                                Optional('interfaces'): {
                                    Any(): {
                                        'system_id': {
                                            Any(): {
                                                'interface': str,
                                                'snpa': str,
                                                'state': str,
                                                'hold': str,
                                                'changed': str,
                                                Optional('nsf'): str,
                                                Optional('bfd'): str,
                                                Optional('ipv4_bfd'): str,
                                                Optional('ipv6_bfd'): str,
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


class ShowIsisAdjacency(ShowIsisAdjacencySchema):
    """Parser for show isis adjacency"""
    
    cli_command = 'show isis adjacency'
    
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        ret_dict = {}
        vrf = 'default'

        # IS-IS p Level-1 adjacencies:
        p1 = re.compile(r'^IS-IS +(?P<isis_name>\w+) +(?P<level_name>\S+) adjacencies:$')

        # 12a4           PO0/1/0/1        *PtoP*         Up    23       00:00:06 Capable  None
        p2 = re.compile(r'^(?P<system_id>\S+) +(?P<interface>\S+) +(?P<snpa>\S+) +(?P<state>(Up|Down|None)) +(?P<hold>\S+) '
                         '+(?P<changed>\S+) +(?P<nsf>\S+) +(?P<bfd>(Up|Down|None|Init))$')

        # Total adjacency count: 1
        p3 = re.compile(r'^Total +adjacency +count: +(?P<adjacency_count>(\d+))$')

        # R1_xe          Gi0/0/0/0.115    fa16.3eab.a39d Up    26   22:30:26 Yes None None
        p4 = re.compile(r'^(?P<system_id>\S+) +(?P<interface>\S+) +(?P<snpa>\S+) +(?P<state>(Up|Down|None)) +(?P<hold>\S+) '
                         '+(?P<changed>\S+) +(?P<nsf>\S+) +(?P<ipv4_bfd>([\s\w]+)) +(?P<ipv6_bfd>([\w\s]+))$')

        for line in out.splitlines():
            line = line.strip()

            # IS-IS p Level-1 adjacencies:
            m = p1.match(line)
            if m:
                isis_name = m.groupdict()['isis_name']
                level_name = m.groupdict()['level_name']
                isis_adjacency_dict = ret_dict.setdefault('isis', {}).\
                                               setdefault(isis_name, {}).\
                                               setdefault('vrf', {}).\
                                               setdefault(vrf, {})

                level_dict = isis_adjacency_dict.setdefault('level', {}).setdefault(level_name, {})
                continue

            # 12a4           PO0/1/0/1        *PtoP*         Up    23       00:00:06 Capable  None
            m = p2.match(line)
            if m:
                system_id = m.groupdict()['system_id']
                interface = m.groupdict()['interface']
                interface_name = Common.convert_intf_name(m.groupdict()['interface'])
                snpa = m.groupdict()['snpa']
                state = m.groupdict()['state']
                hold = m.groupdict()['hold']
                changed = m.groupdict()['changed']
                nsf = m.groupdict()['nsf']
                bfd = m.groupdict()['bfd']
                interface_dict = level_dict.setdefault('interfaces', {}).setdefault(interface, {})
                system_dict = interface_dict.setdefault('system_id', {}).setdefault(system_id, {})
                system_dict['interface'] = interface_name
                system_dict['snpa'] = snpa
                system_dict['state'] = state
                system_dict['hold'] = hold
                system_dict['changed'] = changed
                system_dict['nsf'] = nsf
                system_dict['bfd'] = bfd
                continue

            # Total adjacency count: 1
            m = p3.match(line)
            if m:
                level_dict['total_adjacency_count'] = int(m.groupdict()['adjacency_count'])
                continue

            # R1_xe          Gi0/0/0/0.115    fa16.3eab.a39d Up    26   22:30:26 Yes None None
            m = p4.match(line)
            if m:
                system_id = m.groupdict()['system_id']
                interface = m.groupdict()['interface']
                interface_name = Common.convert_intf_name(m.groupdict()['interface'])
                snpa = m.groupdict()['snpa']
                state = m.groupdict()['state']
                hold = m.groupdict()['hold']
                changed = m.groupdict()['changed']
                nsf = m.groupdict()['nsf']
                ipv4_bfd = m.groupdict()['ipv4_bfd']
                ipv6_bfd = m.groupdict()['ipv6_bfd']
                interface_dict = level_dict.setdefault('interfaces', {}).setdefault(interface, {})
                system_dict = interface_dict.setdefault('system_id', {}).setdefault(system_id, {})
                system_dict['interface'] = interface_name
                system_dict['snpa'] = snpa
                system_dict['state'] = state
                system_dict['hold'] = hold
                system_dict['changed'] = changed
                system_dict['nsf'] = nsf
                system_dict['ipv4_bfd'] = ipv4_bfd
                system_dict['ipv6_bfd'] = ipv6_bfd
                continue

        return ret_dict


#======================================
# Schema for 'show isis neighbors'
#======================================
class ShowIsisNeighborsSchema(MetaParser):
    """Schema for show run isis neighbors"""

    schema = {
        'isis': {
            Any(): {
                'vrf': {
                    Any(): {
                        Optional('total_neighbor_count'): int,
                        Optional('interfaces'): {
                            Any(): {
                                'neighbors': {
                                    Any(): {
                                        'snpa': str,
                                        'state': str,
                                        'holdtime': str,
                                        'type': str,
                                        Optional('ietf_nsf'): str,
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }


class ShowIsisNeighbors(ShowIsisNeighborsSchema):
    """Parser for show isis neighbors"""
    
    cli_command = 'show isis neighbors'
    
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        isis_neighbors_dict = {}
        vrf = 'default'

        # IS-IS 4445 neighbors:
        p1 = re.compile(r'^IS-IS\s+(?P<isis_name>\S+)\s*neighbors:$')

        # R1_xe          Gi0/0/0/0.115    fa16.3eab.a39d Up    24       L1L2 Capable
        p2 = re.compile(r'^(?P<system_id>\S+) +(?P<interface>\S+) +(?P<snpa>\S+) +(?P<state>(Up|Down|None)+) +(?P<holdtime>\S+) '
                         '+(?P<type>\S+) +(?P<ietf_nsf>\S+)$')

        # Total neighbor count: 1
        p3 = re.compile(r'^Total\sneighbor\scount:\s+(?P<neighbor_count>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # IS-IS 4445 neighbors:
            m = p1.match(line)
            if m:
                isis_name = m.groupdict()['isis_name']
                vrf_dict = isis_neighbors_dict.setdefault('isis', {}).\
                                               setdefault(isis_name, {}).\
                                               setdefault('vrf', {}).\
                                               setdefault(vrf, {})
                continue

            # R1_xe          Gi0/0/0/0.115    fa16.3eab.a39d Up    24       L1L2 Capable
            m = p2.match(line)
            if m:
                system_id = m.groupdict()['system_id']
                interface_name = Common.convert_intf_name(m.groupdict()['interface'])
                snpa = m.groupdict()['snpa']
                state = m.groupdict()['state']
                holdtime = m.groupdict()['holdtime']
                type = m.groupdict()['type']
                ietf_nsf = m.groupdict()['ietf_nsf']

                interface_dict = vrf_dict.setdefault('interfaces', {}).setdefault(interface_name, {})
                system_dict = interface_dict.setdefault('neighbors', {}).setdefault(system_id, {})
                system_dict['snpa'] = snpa
                system_dict['state'] = state
                system_dict['holdtime'] = holdtime
                system_dict['type'] = type
                system_dict['ietf_nsf'] = ietf_nsf

                continue
            
            # Total neighbor count: 1
            m = p3.match(line)
            if m:
                vrf_dict['total_neighbor_count'] = int(m.groupdict()['neighbor_count'])
                continue

        return isis_neighbors_dict


# ======================================================
#  Schema for 'show isis segment-routing label table'
# ======================================================
class ShowIsisSegmentRoutingLabelTableSchema(MetaParser):
    """Schema for show isis segment-routing label table"""

    schema = {
        'instance': {
            'SR': {
                'label': {
                    Any(): {
                        'prefix_interface': str,
                    },
                }
            }
        }
    }


class ShowIsisSegmentRoutingLabelTable(ShowIsisSegmentRoutingLabelTableSchema):
    """Parser for show isis segment-routing label table"""
    
    cli_command = ['show isis segment-routing label table']
    
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output
        
        isis_dict = {}

        # IS-IS SR IS Label Table
        p1 = re.compile(r'^IS-IS\s+(?P<instance>\S+)\s+IS\s+Label\s+Table$')

        # Label         Prefix/Interface
        # ----------    ----------------
        # 16001         Loopback0
        # 16002         10.2.2.2/32
        p2 = re.compile(r'^(?P<label>\d+)\s+(?P<prefix_interface>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # IS-IS SR IS Label Table
            m = p1.match(line)
            if m:
                instance = m.groupdict()['instance']
                final_dict = isis_dict.setdefault('instance', {}).\
                    setdefault(instance, {})
                continue

            # Label         Prefix/Interface
            # ----------    ----------------
            # 16001         Loopback0
            # 16002         10.2.2.2/32
            m = p2.match(line)
            if m:
                label = int(m.groupdict()['label'])
                prefix_interface = m.groupdict()['prefix_interface']
                final_dict.setdefault('label', {}).setdefault(
                    label, {}).update(
                    {'prefix_interface': prefix_interface})
                continue

        return isis_dict

class ShowIsisInterfaceSchema(MetaParser):
    ''' Schema for commands:
        * show isis interface
    '''

    schema = {
        'instance': {
            Any(): {
                'interface': {
                    Any(): {
                        'state': str,
                        'adjacency_formation': str,
                        'prefix_advertisement': str,
                        'ipv6_bfd': bool,
                        'ipv4_bfd': bool,
                        'bfd_min_interval': int,
                        'bfd_multiplier': int,
                        'bandwidth': int,
                        'circuit_type': str,
                        'media_type': str,
                        'circuit_number': int,
                        'lsp': {
                            'transmit_timer_expires_ms': int,
                            'transmission_state': str,
                            'lsp_transmit_back_to_back_limit': int,
                            'lsp_transmit_back_to_back_limit_window_msec': int,
                        },
                        'level': {
                            Any(): {
                                'adjacency_count':int,
                                Optional('lsp_pacing_interval_ms'): int,
                                'psnp_entry_queue_size': int,
                                Optional('next_lan_iih_sec'): int,
                                Optional('lan_id'): str,
                                Optional('hello_interval_sec'): int,
                                'hello_multiplier': int,
                                Optional('priority'): {
                                    'local': str,
                                    'dis': str
                                }
                            },
                        },
                        'clns_io': {
                            'protocol_state': str,
                            'mtu': int,
                            Optional('snpa'): str,
                            Optional('layer2_mcast_groups_membership'): {
                                'all_level_1_iss': str,
                                'all_level_2_iss': str,
                            },
                        },
                        'topology': {
                            Any(): {
                                'adjacency_formation': str,
                                'state': str,
                                'prefix_advertisement': str,
                                'metric': {
                                    'level': {
                                        Any(): int
                                    }
                                },
                                'weight': {
                                    'level': {
                                        Any(): int
                                    }
                                },
                                'mpls': {
                                    'mpls_max_label_stack': str,
                                    'ldp_sync': {
                                        'level': {
                                            Any(): str,
                                        }
                                    },
                                },
                                'frr': {
                                    'level': {
                                        Any(): {
                                            'state': str,
                                            'type': str,
                                        },
                                    },
                                },

                            },
                        },
                        'address_family': {
                            Any(): {
                                'state': str,
                                'forwarding_address': str,
                                'global_prefix': str,
                            },
                        }
                    }
                },
            }
        }
    }


class ShowIsisInterface(ShowIsisInterfaceSchema):
    ''' Parser for commands:
        * show isis interface
    '''

    cli_command = ['show isis interface {interface}',
                   'show isis interface']

    def cli(self, interface=None, output=None):

        if output is None:
            if interface:
                command = self.cli_command[0].format(interface=interface)
            else:
                command = self.cli_command[1]
            output = self.device.execute(command)

        # IS-IS test Interfaces
        r1 = re.compile(r'IS\-IS\s+(?P<instance>.+)\s+Interfaces')

        # Loopback0                   Enabled
        # GigabitEthernet0/0/0/0      Enabled
        r2 = re.compile(r'^(?P<interface>\w+[\d+\/]+)\s+(?P<interface_state>\w+)$')

        # Adjacency Formation:    Running
        # Adjacency Formation:      Enabled
        r3 = re.compile(r'Adjacency\s+Formation\s*:\s*'
                         '(?P<adjacency_formation_state>\w+)')

        # Prefix Advertisement:     Enabled
        # Prefix Advertisement:   Running
        r4 = re.compile(r'Prefix\s+Advertisement\s*:\s*'
                         '(?P<prefix_advertisement_state>.+)')

        # IPv4 BFD:                 Disabled
        # IPv6 BFD:                 Disabled
        r5 = re.compile(r'(?P<address_family>IPv4|IPv6)\s+BFD\s*:\s*'
                         '(?P<ip_bfd_state>\w+)')

        # BFD Min Interval:         150
        r6 = re.compile(r'BFD\s+Min\s+Interval\s*:\s*(?P<bfd_min_interval>\d+)')

        # BFD Multiplier:           3
        r7 = re.compile(r'BFD\s+Multiplier\s*:\s*(?P<bfd_multiplier>\d+)')

        # Bandwidth:                0
        # Bandwidth:                1000000
        r8 = re.compile(r'Bandwidth\s*:\s*(?P<bandwidth>\d+)')

        # Circuit Type:             level-1-2
        r9 = re.compile(r'Circuit\s+Type\s*:\s*(?P<circuit_type>\S+)')

        # Media Type:               LAN
        # Media Type:               Loop
        r10 = re.compile(r'Media\s+Type\s*:\s*(?P<media_type>\S+)')

        # Circuit Number:           0
        r11 = re.compile(r'Circuit\s+Number\s*:\s*(?P<circuit_number>\d+)')

        # Level-1
        # Level-2
        r12 = re.compile(r'^Level\-(?P<level>\d+)')

        # Adjacency Count:        0
        r13 = re.compile(r'Adjacency\s+Count\s*:\s*(?P<adjacency_count>\d+)')

        # LSP Pacing Interval:    33 ms
        r14 = re.compile(r'LSP\s+Pacing\s+Interval\s*:\s*'
                          '(?P<lsp_pacing_interval>\d+)\s+ms')

        # PSNP Entry Queue Size:  0
        r15 = re.compile(r'PSNP\s+Entry\s+Queue\s+Size\s*:\s*'
                          '(?P<psnp_entry_queue_size>\d+)')

        # Hello Interval:         10 s
        r16 = re.compile(r'Hello\s+Interval\s*:\s*(?P<hello_interval>\d+)\s*s')

        # Hello Multiplier:       3
        r17 = re.compile(r'Hello\s+Multiplier\a*:\s*(?P<hello_multiplier>\d+)')

        # CLNS I/O
        r18 = re.compile(r'CLNS\s+I\/O')

        # Protocol State:         Up
        r19 = re.compile(r'Protocol\s+State\s*:\s*(?P<protocol_state>\w+)')

        # MTU:                    1500
        r20 = re.compile(r'MTU\s*:\s*(?P<mtu>\d+)')

        # IPv4 Unicast Topology:    Enabled
        # IPv6 Unicast Topology:    Enabled
        r21 = re.compile(r'(?P<topology>(IPv4|IPv6)[\s\w]+)\s+Topology\s*:'
                           '\s*(?P<topology_state>\w+)')

        # Metric (L1/L2):         10/10
        r22 = re.compile(r'Metric\s+\(L(?P<level_1>\d+)/L(?P<level_2>\d+)\)\s*'
                          ':\s*(?P<metric_level_1>\d+)\/(?P<metric_level_2>\d+)')

        # Weight (L1/L2):         0/0
        r23 = re.compile(r'Weight\s+\(L(?P<level_1>\d+)/L(?P<level_2>\d+)\)\s*:'
                          '\s*(?P<weight_level_1>\d+)\/(?P<weight_level_2>\d+)')

        # MPLS Max Label Stack:   1/3/10 (PRI/BKP/SRTE)
        r24 = re.compile(r'MPLS\s+Max\s+Label\s+Stack\s*:\s*(?P<mpls_max_label_stack>.+)')

        # MPLS LDP Sync (L1/L2):  Disabled/Disabled
        r25 = re.compile(r'MPLS\s+LDP\s+Sync\s+\(L(?P<level_1>\d+)/L'
                          '(?P<level_2>\d+)\)\s*:\s*(?P<state_level_1>\w+)\/(?P<state_level_2>\w+)')

        # FRR (L1/L2):            L1 Not Enabled     L2 Not Enabled
        r26 = re.compile(r'FRR\s+\(L\d+\/L\d+\)\s*:\s*L(?P<level_1>\d+)\s+'
                         '(?P<level_1_state>[\w\s]+)\s+L(?P<level_2>\d+)\s+(?P<level_2_state>[\w\s]+)')

        # FRR Type:             None               None
        r27 = re.compile(r'FRR\s+Type\s*:\s*(?P<frr_type_level_1>\S+)\s*'
                          '(?P<frr_type_level_2>\S+)')

        # IPv4 Address Family:      Enabled
        # IPv6 Address Family:      Enabled
        r28 = re.compile(r'(?P<address_family>IPv4|IPv6)\s+Address\s+Family\s*:'
                          '\s*(?P<address_family_state>\w+)')

        # Forwarding Address(es): 0.0.0.0
        # Forwarding Address(es): ::
        r29 = re.compile(r'Forwarding\s+Address\(es\)\s*:\s*'
                          '(?P<forwarding_address>\S+)')

        # Global Prefix(es):      3.3.3.0/24
        # Global Prefix(es):      2001:db8:3:3:3::3/128
        r30 = re.compile(r'Global\s+Prefix\(es\)\s*:\s*(?P<global_prefix>\S+).*')

        # LSP transmit timer expires in 0 ms
        r31 = re.compile(r'LSP\s+transmit\s+timer\s+expires\s+in\s+'
                          '(?P<lsp_timer>\d+)\s+ms')

        # LSP transmission is idle
        r32 = re.compile(r'LSP\s+transmission\s+is\s+'
                          '(?P<lsp_transmission_state>\w+)')

        # Can send up to 10 back-to-back LSPs in the next 0 ms
        r33 = re.compile(r'Can\s+send\s+up\s+to\s+(?P<number_lsp_send>\d+)'
                          '\s+back\-to\-back\s+LSPs\s+in\s+the\s+next\s+'
                          '(?P<time_to_sent>\d+)\s+ms')       

        # LAN ID:                 R3.07
        r34 = re.compile(r'LAN\s+ID\s*:\s*(?P<lan_id>\S+)')

        # Priority (Local/DIS):   64/none (no DIS elected)
        # Priority (Local/DIS):   64/64
        r35 = re.compile(r'Priority\s*\(Local/DIS\)\s*:\s*'
                          '(?P<priority_local>\S+)/(?P<priority_dis>.+)')

        # Next LAN IIH in:        5 s
        # Next LAN IIH in:        3 s 
        r36 = re.compile(r'Next\s+LAN\s+IIH\s+in\s*:\s*'
                          '(?P<next_lan_iih>\d+)\s*s')

        # SNPA:                   fa16.3eb0.d50f
        r37 = re.compile(r'SNPA\s*:\s*(?P<snpa>\S+)')

        # Layer-2 MCast Groups Membership:
        r38 = re.compile(r'Layer\-(?P<layer>\d+)\s*MCast\s+Groups\s+Membership:')

        # All Level-1 ISs:      Yes
        # All Level-2 ISs:      Yes
        r39 = re.compile(r'All\s+Level\-(?P<level>\d+)\s+ISs\s*:\s*'
                          '(?P<iss_state>\S+)')

        # All ISs:              Yes
        r40 = re.compile(r'All\s+ISs\s*:\s*(?P<all_iss>(Yes|No))')

        parsed_output = {}
        interface_flag = False
        clns_flag = False

        for line in output.splitlines():
            line = line.strip()

            # IS-IS test Interfaces
            result = r1.match(line)
            if result:
                group = result.groupdict()
                instance = group['instance']
                instance_dict = parsed_output\
                    .setdefault('instance', {})\
                    .setdefault(instance, {})

                continue

            # Loopback0                   Enabled
            # GigabitEthernet0/0/0/0      Enabled            
            result = r2.match(line)
            if result:
                group = result.groupdict()
                interface = group['interface']
                interface_state = group['interface_state']
                interface_dict = instance_dict\
                    .setdefault('interface', {})\
                    .setdefault(interface, {})
                interface_dict['state'] = interface_state

                interface_flag = True
                    
                continue

            # Adjacency Formation:    Running
            # Adjacency Formation:      Enabled
            result = r3.match(line)
            if result:
                group = result.groupdict()
                adjacency_formation_state = group['adjacency_formation_state']

                if interface_flag:
                    interface_dict['adjacency_formation'] = adjacency_formation_state
                else:
                    topology_dict['adjacency_formation'] = adjacency_formation_state

                continue

            # Prefix Advertisement:     Enabled
            # Prefix Advertisement:   Running
            result = r4.match(line)
            if result:
                group = result.groupdict()
                prefix_advertisement_state = group['prefix_advertisement_state'].strip()
                if interface_flag:
                    interface_dict['prefix_advertisement'] = prefix_advertisement_state
                else:
                    topology_dict['prefix_advertisement'] = prefix_advertisement_state

                continue

            # IPv4 BFD:                 Disabled
            # IPv6 BFD:                 Disabled
            result = r5.match(line)
            if result:
                group = result.groupdict()
                address_family = group['address_family'].lower()
                ip_bfd_state = False
                if group['ip_bfd_state'].lower() == 'enabled':
                    ip_bfd_state = True
                interface_dict['{address_family}_bfd'\
                    .format(address_family=address_family)] = ip_bfd_state

                continue

            # BFD Min Interval:         150
            result = r6.match(line)
            if result:
                group = result.groupdict()
                bfd_min_interval = int(group['bfd_min_interval'])
                interface_dict['bfd_min_interval'] = bfd_min_interval

                continue

            # BFD Multiplier:           3            
            result = r7.match(line)
            if result:
                group = result.groupdict()
                bfd_multiplier = int(group['bfd_multiplier'])
                interface_dict['bfd_multiplier'] = bfd_multiplier

                continue

            # Bandwidth:                0
            # Bandwidth:                1000000
            result = r8.match(line)
            if result:
                group = result.groupdict()
                bandwidth = int(group['bandwidth'])
                interface_dict['bandwidth'] = bandwidth

                continue

            # Circuit Type:             level-1-2
            result = r9.match(line)
            if result:
                group = result.groupdict()
                circuit_type = group['circuit_type']
                interface_dict['circuit_type'] = circuit_type

                continue

            # Media Type:               LAN
            # Media Type:               Loop
            result = r10.match(line)
            if result:
                group = result.groupdict()
                media_type = group['media_type']
                interface_dict['media_type'] = media_type
                continue

            # Circuit Number:           0
            result = r11.match(line)
            if result:
                group = result.groupdict()
                circuit_number = int(group['circuit_number'])
                interface_dict['circuit_number'] = circuit_number
                continue

            # Level-1
            # Level-2
            result = r12.match(line)
            if result:
                group = result.groupdict()
                level = int(group['level'])
                level_dict = interface_dict\
                    .setdefault('level', {})\
                    .setdefault(level, {})

                continue

            # Adjacency Count:        0
            result = r13.match(line)
            if result:
                group = result.groupdict()
                adjacency_count = int(group['adjacency_count'])
                level_dict['adjacency_count'] = adjacency_count
                continue

            # LSP Pacing Interval:    33 ms
            result = r14.match(line)
            if result:                
                group = result.groupdict()
                lsp_pacing_interval = int(group['lsp_pacing_interval'])
                level_dict['lsp_pacing_interval_ms'] = lsp_pacing_interval

                continue

            # PSNP Entry Queue Size:  0
            result = r15.match(line)
            if result:                
                group = result.groupdict()
                psnp_entry_queue_size = int(group['psnp_entry_queue_size'])
                level_dict['psnp_entry_queue_size'] = psnp_entry_queue_size

                continue

            # Hello Interval:         10 s
            result = r16.match(line)
            if result:
                group = result.groupdict()
                hello_interval = int(group['hello_interval'])
                level_dict['hello_interval_sec'] = hello_interval

                continue

            # Hello Multiplier:       3
            result = r17.match(line)
            if result:
                group = result.groupdict()
                hello_multiplier = int(group['hello_multiplier'])
                level_dict['hello_multiplier'] = hello_multiplier
                continue

            # CLNS I/O
            r18 = re.compile(r'CLNS\s+I\/O')
            result = r18.match(line)
            if result:
                clns_dict = interface_dict.setdefault('clns_io', {})
                clns_flag = True
                continue

            # Protocol State:         Up
            result = r19.match(line)
            if result:                
                group = result.groupdict()
                protocol_state = group['protocol_state']
                if clns_flag:
                    clns_dict['protocol_state'] = protocol_state
                else:
                    address_family_dict['protocol_state'] = protocol_state

                continue

            # MTU:                    1500
            result = r20.match(line)
            if result:
                group = result.groupdict()
                mtu = int(group['mtu'])
                clns_dict['mtu'] = mtu

                continue

            # IPv4 Unicast Topology:    Enabled
            # IPv6 Unicast Topology:    Enabled
            result = r21.match(line)
            if result:
                group = result.groupdict()
                topology = group['topology'].lower()
                topology_state = group['topology_state']
                topology_dict = interface_dict\
                    .setdefault('topology', {})\
                    .setdefault(topology, {})
                topology_dict['state'] = topology_state
                interface_flag = False

                continue

            # Metric (L1/L2):         10/10
            result = r22.match(line)
            if result:
                group = result.groupdict()
                level_1 = int(group['level_1'])
                level_2 = int(group['level_2'])
                metric_level_1 = int(group['metric_level_1'])
                metric_level_2 = int(group['metric_level_2'])
                metric_dict = topology_dict\
                    .setdefault('metric', {})\
                    .setdefault('level', {})
                metric_dict[level_1] = metric_level_1
                metric_dict[level_2] = metric_level_2

                continue

            # Weight (L1/L2):         0/0
            result = r23.match(line)
            if result:
                group = result.groupdict()
                level_1 = int(group['level_1'])
                level_2 = int(group['level_2'])
                weight_level_1 = int(group['weight_level_1'])
                weight_level_2 = int(group['weight_level_2'])
                weight_dict = topology_dict\
                    .setdefault('weight', {})\
                    .setdefault('level', {})
                weight_dict[level_1] = weight_level_1
                weight_dict[level_2] = weight_level_2

                continue

            # MPLS Max Label Stack:   1/3/10 (PRI/BKP/SRTE)
            result = r24.match(line)            
            if result:
                group = result.groupdict()
                mpls_stack = group['mpls_max_label_stack'].strip()
                mpls_dict = topology_dict.setdefault('mpls', {})                
                mpls_dict['mpls_max_label_stack'] = mpls_stack

                continue

            # MPLS LDP Sync (L1/L2):  Disabled/Disabled
            result = r25.match(line)
            if result:
                group = result.groupdict()
                level_1 = int(group['level_1'])
                level_2 = int(group['level_2'])
                state_level_1 = group['state_level_1']
                state_level_2 = group['state_level_2']
                sync_level_dict = mpls_dict\
                    .setdefault('ldp_sync', {})\
                    .setdefault('level', {})

                sync_level_dict[level_1] = state_level_1
                sync_level_dict[level_2] = state_level_2

                continue

            # FRR (L1/L2):            L1 Not Enabled     L2 Not Enabled
            result = r26.match(line)
            if result:
                group = result.groupdict()
                level_1 = int(group['level_1'])
                level_1_state = group['level_1_state'].strip()
                level_2 = int(group['level_2'])
                level_2_state = group['level_2_state'].strip()
                frr_dict = topology_dict\
                    .setdefault('frr', {})\
                    .setdefault('level', {})
                frr_dict.setdefault(level_1, {})\
                    .setdefault('state', level_1_state)
                frr_dict.setdefault(level_2, {})\
                    .setdefault('state', level_2_state)

                continue

            # FRR Type:             None               None
            result = r27.match(line)
            if result:
                group = result.groupdict()
                frr_type_level_1 = group['frr_type_level_1']
                frr_type_level_2 = group['frr_type_level_2']
                frr_dict.setdefault(level_1, {})\
                    .setdefault('type', frr_type_level_1)
                frr_dict.setdefault(level_2, {})\
                    .setdefault('type', frr_type_level_2)                

                continue

            # IPv4 Address Family:      Enabled
            # IPv6 Address Family:      Enabled
            result = r28.match(line)
            if result:
                group = result.groupdict()
                address_family = group['address_family']
                address_family_state = group['address_family_state']
                address_family_dict = interface_dict\
                    .setdefault('address_family', {})\
                    .setdefault(address_family, {})
                address_family_dict['state'] = address_family_state
                continue

            # Forwarding Address(es): 0.0.0.0
            # Forwarding Address(es): ::
            result = r29.match(line)
            if result:
                group = result.groupdict()
                forwarding_address = group['forwarding_address']
                address_family_dict['forwarding_address'] = forwarding_address
                continue

            # Global Prefix(es):      3.3.3.0/24
            # Global Prefix(es):      2001:db8:3:3:3::3/128
            result = r30.match(line)
            if result:
                group = result.groupdict()
                global_prefix = group['global_prefix']
                address_family_dict['global_prefix'] = global_prefix
                continue

            # LSP transmit timer expires in 0 ms
            result = r31.match(line)
            if result:
                group = result.groupdict()
                lsp_timer = int(group['lsp_timer'])
                lsp_dict = interface_dict\
                    .setdefault('lsp', {})
                lsp_dict['transmit_timer_expires_ms'] = lsp_timer

                continue

            # LSP transmission is idle
            result = r32.match(line)
            if result:
                group = result.groupdict()
                lsp_transmission_state = group['lsp_transmission_state']
                lsp_dict['transmission_state'] = lsp_transmission_state

                continue

            # Can send up to 10 back-to-back LSPs in the next 0 ms
            result = r33.match(line)
            if result:
                group = result.groupdict()
                number_lsp_send = int(group['number_lsp_send'])
                time_to_sent = int(group['time_to_sent'])
                lsp_dict['lsp_transmit_back_to_back_limit_window_msec'] = time_to_sent
                lsp_dict['lsp_transmit_back_to_back_limit'] = number_lsp_send
                continue

            # LAN ID:                 R3.07
            result = r34.match(line)
            if result:
                group = result.groupdict()
                lan_id = group['lan_id']
                level_dict['lan_id'] = lan_id
                continue

            # Priority (Local/DIS):   64/none (no DIS elected)
            # Priority (Local/DIS):   64/64
            result = r35.match(line)
            if result:
                group = result.groupdict()
                priority_local = group['priority_local']
                priority_dis = group['priority_dis']
                level_dict['priority'] = {
                    'local': priority_local,
                    'dis': priority_dis,
                }

                continue

            # Next LAN IIH in:        5 s
            # Next LAN IIH in:        3 s
            result = r36.match(line)
            if result:
                group = result.groupdict()
                next_lan_iih = int(group['next_lan_iih'])
                level_dict['next_lan_iih_sec'] = next_lan_iih

                continue

            # SNPA:                   fa16.3eb0.d50f
            result = r37.match(line)
            if result:
                group = result.groupdict()
                snpa = group['snpa']
                clns_dict['snpa'] = snpa

                continue

            # Layer-2 MCast Groups Membership:
            result = r38.match(line)
            if result:
                group = result.groupdict()
                layer = int(group['layer'])
                layer_dict = clns_dict\
                    .setdefault('layer2_mcast_groups_membership', {})         

                continue

            # All Level-1 ISs:      Yes
            # All Level-2 ISs:      Yes
            result = r39.match(line)
            if result:
                group = result.groupdict()
                level = int(group['level'])
                iss_state = group['iss_state']
                layer_dict['all_level_{level}_iss'\
                    .format(level=level)] = iss_state
                    
                continue

            # All ISs:              Yes
            result = r40.match(line)
            if result:
                group = result.groupdict()
                all_iss = group['all_iss']
                layer_dict['all_level_1_iss'] = all_iss
                layer_dict['all_level_2_iss'] = all_iss

                continue

        return parsed_output