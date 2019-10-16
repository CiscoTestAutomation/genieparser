"""
show_isis.py

IOSXR parsers for the following show commands:
    * show isis adjacency
    * show isis neighbors
    * show isis

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
            Any(): {
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

class ShowIsisSchema(MetaParser):
    ''' Schema for commands:
        * show isis
    '''
    schema = {
        'instance': {
            Any(): {
                'process_id': str,
                'instance': str,
                'vrf': {
                    Any(): {
                        'system_id': str,
                        'is_levels': str,
                        'manual_area_address': list,
                        'routing_area_address': list,
                        'non_stop_forwarding': str,
                        'most_recent_startup_mode': str,
                        'te_connection_status': str,
                        'srlb': str,
                        'srgb': str,
                        'interfaces': {
                            Any(): {
                                'running_state': str,
                                'configuration_state': str,
                            }
                        },
                        'topology': {
                            Any(): {
                                'distance': int,
                                'adv_passive_only': bool,
                                'protocols_redistributed': bool,
                                'level': {
                                    Any(): {
                                        Optional('generate_style'): str,
                                        Optional('accept_style'): str,
                                        'metric': int,
                                        'ispf_status': str,
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    
    

class ShowIsis(ShowIsisSchema):
    ''' Parser for commands:
        * show isis
    '''

    cli_command = 'show isis'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # IS-IS Router: test
        r1 = re.compile(r'IS\-IS\s+Router\s*:\s*(?P<isis_router>\S+)')

        # System Id: 3333.3333.3333
        r2 = re.compile(r'System\s+Id\s*:\s*(?P<system_id>\S+)')

        # Instance Id: 0
        r3 = re.compile(r'Instance\s+Id\s*:\s*(?P<instance_id>\S+)')

        # IS Levels: level-1-2
        r4 = re.compile(r'IS\s+Levels\s*:\s*(?P<is_levels>level-1-2)')

        # Manual area address(es):
        r5 = re.compile(r'Manual\s+area\s+address\(es\):')

        # Routing for area address(es):
        r6 = re.compile(r'Routing\s+for\s+area\s+address\(es\):')

        # 49.0002
        r7 = re.compile(r'(?P<area_address>\d+\.\d+)')

        # Non-stop forwarding: Disabled
        r8 = re.compile(r'Non\-stop\s+forwarding\s*:\s*(?P<non_stop_forwarding>\w+)')

        # Most recent startup mode: Cold Restart
        r9 = re.compile(r'Most\s+recent\s+startup\s+mode\s*:\s*(?P<most_recent_startup_mode>.+)')

        # TE connection status: Down
        r10 = re.compile(r'TE\s+connection\s+status\s*:\s*(?P<te_connection_status>.+)')

        # Topologies supported by IS-IS:
        r11 = re.compile(r'Topologies\s+supported\s+by\s+IS\-IS:')

        # IPv4 Unicast
        # IPv6 Unicast
        r12 = re.compile(r'(?P<topology>(IPv6|IPv4)\s+Unicast)')

        # Level-1
        # Level-2
        r13 = re.compile(r'Level\-(?P<level>\d+)')

        # Metric style (generate/accept): Wide/Wide
        r14 = re.compile(r'Metric\s+style\s*\(generate\/accept\)\s*:\s*'
                          '(?P<generate_style>\w+)\/(?P<accept_style>\w+)')

        # Metric: 10
        r15 = re.compile(r'Metric\s*:\s*(?P<metric>\d+)')

        # ISPF status: Disabled
        r16 = re.compile(r'ISPF\s+status\s*:\s*(?P<ispf_status>\w+)')
        r17 = re.compile(r'No\s+protocols\s+redistributed')

        # Distance: 115
        r18 = re.compile(r'Distance\s*:\s*(?P<distance>\d+)')

        # Advertise Passive Interface Prefixes Only: No
        r19 = re.compile(r'Advertise\s+Passive\s+Interface\s+Prefixes\s+Only'
                          '\s*:\s*(?P<adv_passive_only>\S+)')

        # SRLB not allocated
        r20 = re.compile(r'SRLB\s*(?P<srlb>[\w\s]+)')


        # SRGB not allocated
        r21 = re.compile(r'SRGB\s*(?P<srgb>[\w\s]+)')

        # Loopback0 is running actively (active in configuration)
        # GigabitEthernet0/0/0/0 is running actively (active in configuration)
        r22 = re.compile(r'(?P<interface>\S+)\s+is\s+(?P<running_state>[\s\w]+)'
                          '\s+\((?P<configuration_state>[\w\s]+)\)')

        parsed_output = {}
        vrf = 'default'

        for line in output.splitlines():
            line = line.strip()

            # IS-IS Router: test
            result = r1.match(line)
            if result:
                group = result.groupdict()
                isis_router = group['isis_router']
                instance_dict = parsed_output\
                    .setdefault('instance', {})\
                    .setdefault(isis_router, {})
                instance_dict['process_id'] = isis_router
                    
                continue

            # System Id: 3333.3333.3333
            result = r2.match(line)
            if result:
                group = result.groupdict()
                system_id = group['system_id']

                continue

            # Instance Id: 0
            result = r3.match(line)
            if result:
                group = result.groupdict()
                instance_id = group['instance_id']
                instance_dict['instance'] = instance_id
                vrf_dict = instance_dict\
                    .setdefault('vrf', {})\
                    .setdefault(vrf, {})
                vrf_dict['system_id'] = system_id

                continue

            # IS Levels: level-1-2
            result = r4.match(line)
            if result:
                group = result.groupdict()
                is_levels = group['is_levels']
                vrf_dict['is_levels'] = is_levels

                continue

            # Manual area address(es):
            result = r5.match(line)
            if result:
                area_address_field = 'manual_area_address'

                continue

            # Routing for area address(es):
            result = r6.match(line)
            if result:
                area_address_field = 'routing_area_address'

                continue

            # 49.0002
            result = r7.match(line)
            if result:
                group = result.groupdict()
                area_address = group['area_address']
                area_address_list = vrf_dict.get(area_address_field, [])
                area_address_list.append(area_address)
                vrf_dict[area_address_field] = area_address_list

                continue

            # Non-stop forwarding: Disabled
            result = r8.match(line)
            if result:
                group = result.groupdict()
                non_stop_forwarding = group['non_stop_forwarding']
                vrf_dict['non_stop_forwarding'] = non_stop_forwarding

                continue

            # Most recent startup mode: Cold Restart
            result = r9.match(line)
            if result:
                group = result.groupdict()
                most_recent_startup_mode = group['most_recent_startup_mode']
                vrf_dict['most_recent_startup_mode'] = most_recent_startup_mode

                continue

            # TE connection status: Down
            result = r10.match(line)
            if result:
                group = result.groupdict()
                te_connection_status = group['te_connection_status']
                vrf_dict['te_connection_status'] = te_connection_status

                continue

            # Topologies supported by IS-IS:
            result = r11.match(line)
            if result:
                topology_dict = vrf_dict.setdefault('topology', {})

                continue

            # IPv4 Unicast
            # IPv6 Unicast
            result = r12.match(line)
            if result:
                group = result.groupdict()
                topology = group['topology']
                address_family_dict = topology_dict.setdefault(topology, {})

                continue

            # Level-1
            # Level-2
            result = r13.match(line)
            if result:
                group = result.groupdict()
                level = int(group['level'])
                level_dict = address_family_dict\
                    .setdefault('level', {})\
                    .setdefault(level, {})

                continue

            # Metric style (generate/accept): Wide/Wide
            result = r14.match(line)
            if result:
                group = result.groupdict()
                generate_style = group['generate_style']
                accept_style = group['accept_style']
                level_dict['generate_style'] = generate_style
                level_dict['accept_style'] = accept_style

                continue

            # Metric: 10
            result = r15.match(line)
            if result:
                group = result.groupdict()
                metric = int(group['metric'])
                level_dict['metric'] = metric

                continue

            # ISPF status: Disabled
            result = r16.match(line)
            if result:
                group = result.groupdict()
                ispf_status = group['ispf_status']
                level_dict['ispf_status'] = ispf_status

                continue

            # No protocols redistributed
            result = r17.match(line)
            if result:
                address_family_dict['protocols_redistributed'] = False

                continue

            # Distance: 115
            result = r18.match(line)
            if result:
                group = result.groupdict()
                distance = int(group['distance'])
                address_family_dict['distance'] = distance

                continue

            # Advertise Passive Interface Prefixes Only: No
            result = r19.match(line)
            if result:
                group = result.groupdict()
                if group['adv_passive_only'] == 'No':
                    adv_passive_only = False
                else:
                    adv_passive_only = True
                address_family_dict['adv_passive_only'] = adv_passive_only

                continue

            # SRLB not allocated
            result = r20.match(line)
            if result:
                group = result.groupdict()
                srlb = group['srlb']
                vrf_dict['srlb'] = srlb   

                continue

            # SRGB not allocated
            result = r21.match(line)
            if result:
                group = result.groupdict()
                srgb = group['srgb']
                vrf_dict['srgb'] = srgb

                continue

            # Loopback0 is running actively (active in configuration)
            # GigabitEthernet0/0/0/0 is running actively (active in configuration)
            result = r22.match(line)
            if result:
                group = result.groupdict()
                interface = group['interface']
                running_state = group['running_state']
                configuration_state = group['configuration_state']
                interfaces_dict = vrf_dict\
                    .setdefault('interfaces', {})\
                    .setdefault(interface, {})
                interfaces_dict['running_state'] = running_state
                interfaces_dict['configuration_state'] = configuration_state

                continue

        return parsed_output


class ShowIsisDatabaseDetailSchema(MetaParser):
    ''' Schema for commands:
        * show isis database detail
    '''

    schema = {
        'instance': {
            Any(): {
                'level': {
                    Any(): {
                        'lspid': {
                            Any(): {
                                'lsp': {
                                    'seq_num': str,
                                    Optional('local_router'): bool,
                                    'checksum': str,
                                    'holdtime': int,
                                    Optional('received'): int,
                                    'attach_bit': int,
                                    'p_bit': int,
                                    'overload_bit': int,
                                },
                                Optional('router_id'): str,
                                Optional('area_address'): str,
                                Optional('nlpid'): list,
                                Optional('ip_address'): str,
                                Optional('ipv6_address'): str,
                                Optional('hostname'): str,
                                Optional('topology'): list,
                                Optional('extended_ipv4_reachability'): {
                                    Any(): {
                                        'ip_prefix': str,
                                        'prefix_length': str,
                                        'metric': int,
                                    }
                                },
                                Optional('ip_interarea'): {
                                    Any(): {
                                        'address_family': {
                                            Any(): {
                                                'metric': int,
                                            }
                                        }
                                    }
                                },
                                Optional('mt_is_neighbor'): {
                                    Any(): {
                                        'mt_id': str,
                                        'metric': int,
                                    }
                                },
                                Optional('is_neighbor'): {
                                    Any(): {
                                        'metric': int,
                                    }
                                },
                                Optional('ip_neighbor'): {
                                    Any(): {
                                        'ip_prefix': str,
                                        'prefix_length': str,
                                        'metric': int,
                                    }
                                },
                                Optional('es_neighbor'): {
                                    Any(): {
                                        'metric': int,
                                    }
                                },
                                Optional('extended_is_neighbor'): {
                                    Any(): {
                                        'metric': int,
                                    }
                                },
                                Optional('mt_ipv4_reachability'): {
                                    Any(): {
                                        'ip_prefix': str,
                                        Optional('prefix_length'): str,
                                        'metric': str,
                                    }
                                },
                                Optional('ipv4_reachability'): {
                                    Any(): {
                                        'ip_prefix': str,
                                        Optional('prefix_length'): str,
                                        'metric': str,
                                    }
                                },
                                Optional('mt_ipv6_reachability'): {
                                    Any(): {
                                        'ip_prefix': str,
                                        Optional('prefix_length'): str,
                                        'metric': int,
                                    }
                                },
                                Optional('ipv6_reachability'): {
                                    Any(): {
                                        'ip_prefix': str,
                                        Optional('prefix_length'): str,
                                        'metric': str,
                                    }
                                },
                                Optional('mt_entries'): {
                                    Any(): {
                                        Optional('attach_bit'): int,
                                        Optional('p_bit'): int,
                                        Optional('overload_bit'): int,
                                    }
                                }
                            }
                        },
                        Optional('total_lsp_count'): int,
                        Optional('local_lsp_count'): int,
                    }
                }
            }
        }
    }

class ShowIsisDatabaseDetail(ShowIsisDatabaseDetailSchema):
    ''' Parser for commands:
       * show isis database detail 
    '''

    cli_command = 'show isis database detail'

    def cli(self, output=None):

        if not output:
            output = self.device.execute(self.cli_command)

        # IS-IS test (Level-1) Link State Database
        # IS-IS test (Level-2) Link State Database
        # IS-IS Level-1 Link State Database
        r1 = re.compile(r'IS\-IS\s+(?P<instance>\S+)?\s*\(*Level\-'
                        r'(?P<level>\d+)\)*\s+Link\s+State\s+Database')

        # LSPID                 LSP Seq Num   LSP Checksum  LSP Holdtime/Rcvd  ATT/P/OL
        # R3.00-00            * 0x0000000d    0x0476        578  /*            1/0/0
        # R3.03-00              0x00000007    0x8145        988  /*            0/0/0
        # router-5.00-00        0x00000005 0x807997c        457                0/0/0
        # 0000.0C00.0C35.00-00  0x0000000C    0x5696        325                0/0/0
        # 0000.0C00.40AF.00-00* 0x00000009    0x8452        608                1/0/0 
        r2 = re.compile(r'(?P<lspid>[\w\-\.]+)\s*(?P<local_router>\**)\s+(?P<lsp_seq_num>\S+)\s+(?P<lsp_checksum>\S+)\s+(?P<lsp_holdtime>\d+|\*)\s+(/*(?P<lsp_rcvd>\d*|\*)?)\s+(?P<attach_bit>\d+)/(?P<p_bit>\d+)/(?P<overload_bit>\d+)')

        # Area Address:   49.0002
        r3 = re.compile(r'Area\s+Address\s*:\s*(?P<area_address>\S+)')

        # NLPID: 0xcc
        # NLPID: 0xCC 0x8E
        r4 = re.compile(r'NLPID\s*:\s*(?P<nlpid>[\w\s]+)')

        # IP Address:     3.3.3.3
        r5 = re.compile(r'IP\s*Address\s*:\s*(?P<ip_address>\S+)')

        # Metric: 10         IP-Extended 3.3.3.0/24
        # Metric: 10         IP-Extended 10.2.3.0/24
        r6 = re.compile(r'Metric\s*:\s*(?P<metric>\d+)\s+IP\-Extended\s+'
                        r'(?P<ip_address>[\d\.\/]+)')

        # Hostname:       R3
        r7 = re.compile(r'Hostname\s*:\s+(?P<hostname>\S+)')

        # IPv6 Address:   2001:db8:3:3:3::3
        r8 = re.compile(r'IPv6\s+Address\s*:\s*(?P<ipv6_address>\S+)')

        # Metric: 10         MT (IPv6 Unicast) IPv6 2001:db8:3:3:3::3/128
        # Metric: 10         MT (IPv6 Unicast) IPv6 2001:db8:10:2::/64
        r9 = re.compile(r'Metric\s*:\s*(?P<metric>\d+)\s+MT\s*\(IPv(4|6)\s+'
                        r'\w+\)\s*(?P<ip_version>IPv(4|6))\s+(?P<ip_address>\S+)')
        
        # Metric: 10   IPv6 (MT-IPv6) 2001:0DB8::/64
        # Metric: 10         IPv6 2001:2:2:2::2/128
        r9_2 = re.compile(r'Metric\s*:\s*(?P<metric>\d+)\s+(?P<ip_version>'
                          r'IPv(4|6))\s+(\(MT-IPv6\))?\s*(?P<ip_address>'
                          r'[\w\:\/]+)')

        # MT:             Standard (IPv4 Unicast)
        # MT:             Standard (IPv6 Unicast)
        r10 = re.compile(r'MT\s*:\s*(?P<mt>\w+\s+\(IPv(4|6)\s*\w+\))\s*'
                         r'(:?(?P<attach_bit>\d+)\/(?P<p_bit>\d+)\/'
                         r'(?P<overload_bit>\d+))?')

        # MT:             IPv6 Unicast                                 1/0/0
        # MT:             IPv4 Unicast                                 0/0/0
        r11 = re.compile(r'MT\s*:\s*(?P<mt>IPv(4|6)\s+\w+)\s+'
                         r'(?P<attach_bit>\d+)/(?P<p_bit>\d+)/'
                         r'(?P<overload_bit>\d+)')

        # Metric: 10         IS-Extended R3.03
        # Metric: 10         IS-Extended R5.01
        r12 = re.compile(r'Metric\s*:\s*(?P<metric>\d+)\s+IS\-Extended\s+'
                         r'(?P<is_extended>\S+)')

        # Metric: 10         MT (IPv6 Unicast) IS-Extended R3.03
        # Metric: 10         MT (IPv6 Unicast) IS-Extended R5.01
        r13 = re.compile(r'Metric\s*:\s*(?P<metric>\d+)\s+'
                         r'(?P<mt_id>[\w\(\)\s]+)\s+IS-Extended\s+'
                         r'(?P<is_extended>\S+)')

        # Router ID:      6.6.6.6
        # Router ID:      7.7.7.7
        r14 = re.compile(r'Router\s+ID\s*:\s*(?P<router_id>\S+)')

        # Metric: 40         IP-Extended-Interarea 10.7.8.0/24
        r15 = re.compile(r'Metric\s*:\s*(?P<metric>\d+)\s+IP\-Extended\-'
                          'Interarea\s+(?P<ip_interarea>\S+)')

        # Metric: 40         MT (IPv6 Unicast) IPv6-Interarea 2001:db8:10:7::/64
        r16 = re.compile(r'Metric\s*:\s*(?P<metric>\d+)\s+MT\s+\('
                         r'(?P<address_family>.+)\)\s+IPv6-Interarea\s+'
                         r'(?P<ipv6_interarea>\S+)')

        # Total Level-1 LSP count: 11     Local Level-1 LSP count: 1
        # Total Level-2 LSP count: 11     Local Level-2 LSP count: 1
        r17 = re.compile(r'Total\s+Level\-(?P<total_level>\d+)\s+LSP\s+count\s*:'
                         r'\s*(?P<total_lsp_count>\d+)\s+Local\s*Level-'
                         r'(?P<local_level>\d+)\s+LSP\s+count\s*:\s*'
                         r'(?P<local_lsp_count>\d+)')

        # Total LSP count: 3 (L1: 0, L2 3, local L1: 0, local L2 2)
        r17_2 = re.compile(r'Total\s*LSP\s+count\s*:\s*(?P<total_lsp_count>\d+)'
                           r'\s*\(L1\s*:\s*(?P<total_l1>\d+)\s*,\s*L2\s*'
                           r'(?P<total_l2>\d+)\s*,\s*local\s*L1\s*:\s*'
                           r'(?P<local_l1>\d+),\s*local\s*L2\s*'
                           r'(?P<local_l2>\d+)\)')

        # Metric: 10   IS 0000.0C00.62E6.03 
        r18 = re.compile(r'Metric\s*:\s*(?P<metric>\d+)\s+IS\s+'
                         r'(?P<is_neighbor>[\w\.\-]+)')

        # Metric: 0    ES 0000.0C00.0C35
        r19 = re.compile(r'Metric\s*:\s*(?P<metric>\d+)\s+ES\s+'
                         r'(?P<es_neighbor>[\w\.]+)')

        # Topology: IPv4 (0x0) IPv6 (0x2)
        # Topology: IPv4 (0x0)
        # Topology: IPv6 (0x0)
        r20 = re.compile(r'Topology\s*:\s*(?P<topology_1>IPv(4|6)\s+\(0x0\))'
                         r'\s*(?P<topology_2>IPv(4|6)\s+\(0x2\))?')

        # Metric: 10    IS (MT-IPv6) cisco.03
        r21 = re.compile(r'Metric\s*:\s*(?P<metric>\d+)\s*IS\s+\(MT-IPv(4|6)\)'
                         r'\s+(?P<is_neighbor>[\w\.]+)')

        # Metric: 0          IP 172.3.55.0/24
        r22 = re.compile(r'Metric\s*:\s*(?P<metric>\d+)\s+IP\s+'
                         r'(?P<ip_address>[\d\.\/]+)')

        parsed_output = {}


        for line in output.splitlines():
            line = line.strip()

            # IS-IS test (Level-1) Link State Database
            # IS-IS test (Level-2) Link State Database
            result = r1.match(line)
            if result:
                group = result.groupdict()
                level = int(group['level'])
                instance = group['instance']
                level_dict = parsed_output\
                    .setdefault('instance', {})\
                    .setdefault(instance, {})\
                    .setdefault('level', {})\
                    .setdefault(level, {})

                continue

            # LSPID                 LSP Seq Num  LSP Checksum  LSP Holdtime/Rcvd  ATT/P/OL
            # R3.00-00            * 0x0000000d   0x0476        578  /*            1/0/0
            # R3.03-00              0x00000007   0x8145        988  /*            0/0/0
            result = r2.match(line)
            if result:
                group = result.groupdict()
                lspid = group['lspid']
                local_router = group['local_router']
                lsp_seq_num = group['lsp_seq_num']
                lsp_checksum = group['lsp_checksum']
                lsp_holdtime = group['lsp_holdtime']
                lsp_rcvd = group['lsp_rcvd']
                attach_bit = int(group['attach_bit'])
                p_bit = int(group['p_bit'])
                overload_bit = int(group['overload_bit'])
                lspid_dict = level_dict\
                    .setdefault('lspid', {})\
                    .setdefault(lspid, {})

                lsp_dict = lspid_dict.setdefault('lsp', {})
                lsp_dict['seq_num'] = lsp_seq_num
                lsp_dict['checksum'] = lsp_checksum
                lsp_dict['local_router'] = bool(local_router)
                lsp_dict['holdtime'] = int(lsp_holdtime)
                if lsp_rcvd and '*' not in lsp_rcvd:
                    lsp_dict['received'] = int(lsp_rcvd)
                lsp_dict['attach_bit'] = attach_bit
                lsp_dict['p_bit'] = p_bit
                lsp_dict['overload_bit'] = overload_bit

                continue

            # Area Address:   49.0002
            result = r3.match(line)
            if result:
                group = result.groupdict()
                area_address = group['area_address']
                lspid_dict['area_address'] = area_address
                continue

            # NLPID: 0xcc
            # NLPID: 0xCC 0x8E
            result = r4.match(line)
            if result:
                group = result.groupdict()
                parsed_nlpid = group['nlpid'].split()
                for nlpid in parsed_nlpid:
                    nlpid_list = lspid_dict.get('nlpid', [])
                    nlpid_list.append(nlpid)
                lspid_dict['nlpid'] = nlpid_list

                continue

            # IP Address:     3.3.3.3
            result = r5.match(line)
            if result:
                group = result.groupdict()
                ip_address = group['ip_address']
                lspid_dict['ip_address'] = ip_address

                continue

            # Metric: 10         IP-Extended 3.3.3.0/24
            # Metric: 10         IP-Extended 10.2.3.0/24
            result = r6.match(line)
            if result:
                group = result.groupdict()
                metric = int(group['metric'])
                ip_address = group['ip_address']
                ip_extended_dict = lspid_dict\
                    .setdefault('extended_ipv4_reachability', {})\
                    .setdefault(ip_address, {})
                ip_len_list = ip_address.split('/')
                ip_extended_dict['ip_prefix'] = ip_len_list[0]
                if len(ip_len_list) > 1:
                    ip_extended_dict['prefix_length'] = ip_len_list[1]
                ip_extended_dict['metric'] = metric

                continue

            # Hostname:       R3
            result = r7.match(line)
            if result:
                group = result.groupdict()
                hostname = group['hostname']
                lspid_dict['hostname'] = hostname

                continue

            # IPv6 Address:   2001:db8:3:3:3::3
            result = r8.match(line)
            if result:
                group = result.groupdict()
                ipv6_address = group['ipv6_address']
                lspid_dict['ipv6_address'] = ipv6_address

                continue

            # Metric: 10         MT (IPv6 Unicast) IPv6 2001:db8:3:3:3::3/128
            # Metric: 10         MT (IPv4 Unicast) IPv4 192.168.1.1/12
            result = r9.match(line)
            if result:
                group = result.groupdict()
                metric = int(group['metric'])
                ip_address = group['ip_address']
                ip_version = group['ip_version'].lower()
                mt_dict = lspid_dict\
                    .setdefault('mt_{ip_version}_reachability'\
                        .format(ip_version=ip_version), {})\
                    .setdefault(ip_address, {})
                ip_prefix_list = ip_address.split('/')
                mt_dict['ip_prefix'] = ip_prefix_list[0]
                if len(ip_prefix_list) > 1:
                    mt_dict['prefix_length'] = ip_prefix_list[1]
                mt_dict['metric'] = metric

                continue

            # Metric: 10         IPv6 2001:2:2:2::2/128
            # Metric: 10   IPv6 (MT-IPv6) 2001:0DB8::/64
            result = r9_2.match(line)
            if result:
                group = result.groupdict()
                metric = group['metric']
                ip_address = group['ip_address']
                ip_version = group['ip_version'].lower()
                mt_dict = lspid_dict\
                    .setdefault('{ip_version}_reachability'\
                        .format(ip_version=ip_version), {})\
                    .setdefault(ip_address, {})
                ip_prefix_list = ip_address.split('/')
                mt_dict['ip_prefix'] = ip_prefix_list[0]
                if len(ip_prefix_list) > 1:
                    mt_dict['prefix_length'] = ip_prefix_list[1]
                mt_dict['metric'] = metric

                continue

            # MT:             Standard (IPv4 Unicast)
            result = r10.match(line)
            if result:
                group = result.groupdict()
                mt_entry = group['mt']
                attach_bit = group['attach_bit']
                p_bit = group['p_bit']
                overload_bit = group['overload_bit']
                topology_dict = lspid_dict\
                    .setdefault('mt_entries', {})\
                    .setdefault(mt_entry, {})
                if attach_bit:
                    topology_dict['attach_bit'] = int(attach_bit)
                if p_bit:
                    topology_dict['p_bit'] = int(p_bit)
                if overload_bit:
                    topology_dict['overload_bit'] = int(overload_bit)

                continue

            # MT:    IPv6 Unicast                1/0/0
            # MT:    IPv6 Unicast                0/0/0
            result = r11.match(line)
            if result:
                group = result.groupdict()
                mt_entry = group['mt']
                attach_bit = group['attach_bit']
                p_bit = group['p_bit']
                overload_bit = group['overload_bit']
                topology_dict = lspid_dict\
                    .setdefault('mt_entries', {})\
                    .setdefault(mt_entry, {})                
                if attach_bit:
                    topology_dict['attach_bit'] = int(attach_bit)
                if p_bit:
                    topology_dict['p_bit'] = int(p_bit)
                if overload_bit:
                    topology_dict['overload_bit'] = int(overload_bit)

                continue

            # Metric: 10         IS-Extended R3.03
            # Metric: 10         IS-Extended R5.01
            result = r12.match(line)
            if result:
                group = result.groupdict()
                metric = int(group['metric'])
                is_extended = group['is_extended']
                is_extended_dict =  lspid_dict\
                    .setdefault('extended_is_neighbor', {})\
                    .setdefault(is_extended, {})
                is_extended_dict['metric'] = metric

                continue

            # Metric: 10         MT (IPv6 Unicast) IS-Extended R3.03
            # Metric: 10         MT (IPv6 Unicast) IS-Extended R5.01
            result = r13.match(line)
            if result:
                group = result.groupdict()
                metric = int(group['metric'])
                mt_id = group['mt_id']
                is_extended = group['is_extended']
                is_extended_dict =  lspid_dict\
                    .setdefault('mt_is_neighbor', {})\
                    .setdefault(is_extended, {})
                is_extended_dict['metric'] = metric
                is_extended_dict['mt_id'] = mt_id

                continue

            # Router ID:      6.6.6.6
            # Router ID:      7.7.7.7
            result = r14.match(line)
            if result:
                group = result.groupdict()
                router_id = group['router_id']
                lspid_dict['router_id'] = router_id
                continue

            # Metric: 40         IP-Extended-Interarea 10.7.8.0/24
            result = r15.match(line)
            if result:
                group = result.groupdict()
                metric = int(group['metric'])
                ip_extended_interarea = group['ip_interarea']
                ip_interarea_dict = lspid_dict\
                    .setdefault('ip_interarea', {})\
                    .setdefault(ip_extended_interarea, {})\
                    .setdefault('address_family', {})\
                    .setdefault('ipv4 unicast', {})
                ip_interarea_dict['metric'] = metric

                continue

            # Metric: 40         MT (IPv6 Unicast) IPv6-Interarea 2001:db8:10:7::/64
            result = r16.match(line)
            if result:
                group = result.groupdict()
                address_family = group['address_family']
                metric = int(group['metric'])
                ipv6_interarea = group['ipv6_interarea']
                ip_interarea_dict = lspid_dict\
                    .setdefault('ip_interarea', {})\
                    .setdefault(ip_extended_interarea, {})\
                    .setdefault('address_family', {})\
                    .setdefault(address_family, {})
                ip_interarea_dict['metric'] = metric

                continue

            # Total Level-1 LSP count: 11     Local Level-1 LSP count: 1
            # Total Level-2 LSP count: 11     Local Level-2 LSP count: 1
            result = r17.match(line)
            if result:
                group = result.groupdict()
                total_lsp_count = int(group['total_lsp_count'])
                local_lsp_count = int(group['local_lsp_count'])
                level_dict['total_lsp_count'] = total_lsp_count
                level_dict['local_lsp_count'] = local_lsp_count
                
                continue

            # Total LSP count: 3 (L1: 0, L2 3, local L1: 0, local L2 2)
            result = r17_2.match(line)
            if result:
                group = result.groupdict()
                total_lsp_count = int(group['total_lsp_count'])
                local_l1 = int(group['local_l1'])
                local_l2 = int(group['local_l2'])
                local_lsp_count = sum((local_l1, local_l2))

                level_dict['total_lsp_count'] = total_lsp_count
                level_dict['local_lsp_count'] = local_lsp_count

                continue

            # Metric: 10   IS 0000.0C00.62E6.03 
            result = r18.match(line)
            if result:
                group = result.groupdict()
                metric = int(group['metric'])
                is_neighbor = group['is_neighbor']
                is_neighbor_dict = lspid_dict\
                    .setdefault('is_neighbor', {})\
                    .setdefault(is_neighbor, {})
                is_neighbor_dict['metric'] = metric

                continue
            
            # Metric: 0    ES 0000.0C00.0C35
            result = r19.match(line)
            if result:        
                group = result.groupdict()
                metric = int(group['metric'])
                es_neighbor = group['es_neighbor']
                es_neighbor_dict = lspid_dict\
                    .setdefault('es_neighbor', {})\
                    .setdefault(es_neighbor, {})
                es_neighbor_dict['metric'] = metric

                continue

            # Topology: IPv4 (0x0) IPv6 (0x2)
            # Topology: IPv4 (0x0)
            # Topology: IPv6 (0x0)
            result = r20.match(line)
            if result:
                group = result.groupdict()
                topology_1 = group['topology_1']
                topology_2 = group['topology_2']
                topology_list = lspid_dict\
                    .setdefault('topology', [])
                topology_list.append(topology_1)
                if topology_2:
                    topology_list.append(topology_2)

                continue

            # Metric: 10    IS (MT-IPv6) cisco.03
            result = r21.match(line)
            if result:
                group = result.groupdict()
                metric = int(group['metric'])
                is_neighbor = group['is_neighbor']
                is_neighbor_dict = lspid_dict\
                    .setdefault('is_neighbor', {})\
                    .setdefault(is_neighbor, {})
                is_neighbor_dict['metric'] = metric

                continue

            # Metric: 0          IP 172.3.55.0/24
            result = r22.match(line)
            if result:
                group = result.groupdict()
                metric = int(group['metric'])
                ip_address = group['ip_address']
                ip_prefix_list = ip_address.split('/')
                ip_dict = lspid_dict\
                    .setdefault('ip_neighbor', {})\
                    .setdefault(ip_address, {})
                ip_dict['ip_prefix'] = ip_prefix_list[0]
                if len(ip_prefix_list) > 1:
                    ip_dict['prefix_length'] = ip_prefix_list[1]
                ip_dict['metric'] = metric

                continue

        return parsed_output