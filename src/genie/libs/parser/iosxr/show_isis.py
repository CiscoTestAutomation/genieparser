"""
show_isis.py

IOSXR parsers for the following show commands:
    * show isis adjacency
    * show isis neighbors
    * show isis
    * show isis hostname
    * show isis instance {instance} hostname
    * show isis statistics

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

class ShowIsisHostnameSchema(MetaParser):
    ''' Schema for commands:
        * 'show isis hostname'
        * 'show isis instance {instance} hostname'
    '''

    schema = {
        'isis': {
            Any(): {
                'vrf': {
                    Any(): {
                        'level': {
                            Any(): {
                                'system_id': {
                                    Any(): {
                                        'dynamic_hostname': str,
                                        Optional('local_router'): bool
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }    

class ShowIsisHostname(ShowIsisHostnameSchema):
    ''' Parser for commands:
        * 'show isis hostname'
        * 'show isis instance {instance} hostname'
    '''

    cli_command = ['show isis instance {instance} hostname',
                   'show isis hostname']

    def cli(self, instance=None, output=None):

        if output is None:
            if instance:
                command = self.cli_command[0].format(instance=instance)
            else:
                command = self.cli_command[1]
            output = self.device.execute(command)

        # IS-IS TEST1 hostnames
        r1 = re.compile(r'IS\-IS\s(?P<isis>.+)\s+hostnames')

        # 2     1720.1800.0254 tor-28.tenlab-cloud
        # 2     1720.1800.0213 leaf-2.qa-site1
        # 2     1720.1800.0250 tor-23.tenlab-cloud
        r2 = re.compile(r'(?P<level>[\d\,]+)\s+(?P<local_router>\**)\s+'
                         '(?P<system_id>\S+)\s+(?P<dynamic_hostname>\S+)')

        parsed_output = {}
        vrf = 'default'

        for line in output.splitlines():
            line = line.strip()
            
            # IS-IS TEST1 hostnames            
            result = r1.match(line)
            if result:                
                group = result.groupdict()
                isis = group['isis']

                isis_dict = parsed_output\
                    .setdefault('isis', {})\
                    .setdefault(isis, {})\
                    .setdefault('vrf', {})\
                    .setdefault(vrf, {})                    

                continue

            # 2     1720.1800.0254 tor-28.tenlab-cloud
            # 2     1720.1800.0213 leaf-2.qa-site1
            # 2     1720.1800.0250 tor-23.tenlab-cloud            
            result = r2.match(line)
            if result:
                group = result.groupdict()

                levels = group['level']
                system_id = group['system_id']
                local_router = group.get('local_router', None)
                dynamic_hostname = group['dynamic_hostname']

                for level in levels.split(','):
                    hostname_dict = isis_dict\
                        .setdefault('level', {})\
                        .setdefault(int(level), {})\
                        .setdefault('system_id', {})\
                        .setdefault(system_id, {})

                    hostname_dict['dynamic_hostname'] = dynamic_hostname
                    if local_router:
                        hostname_dict['local_router'] = True

                continue

        return parsed_output

class ShowIsisStatisticsSchema(MetaParser):
    ''' Schema for commands:
        * show isis statistics
    '''
    schema = {
        'isis': {
            Any(): {
                
                'psnp_cache': {
                    'hits': int,
                    'tries': int,
                },
                'csnp_cache': {
                    'hits': int,
                    'tries': int,
                    'updates': int,
                },
                'lsp': {
                    'checksum_errors_received': int,
                    'dropped': int,
                },
                'upd': {
                    'max_queue_size': int,
                    'queue_size': int,
                },
                'snp': {
                    'dropped': int
                },
                'transmit_time': {
                    'hello': {
                        'rate_per_sec': int,
                        'average_transmit_time_sec': int,
                        'average_transmit_time_nsec': int,
                    },
                    'csnp': {
                        'rate_per_sec': int,
                        'average_transmit_time_sec': int,
                        'average_transmit_time_nsec': int,
                    },
                    'psnp': {
                        'rate_per_sec': int,
                        'average_transmit_time_sec': int,
                        'average_transmit_time_nsec': int,
                    },
                    'lsp': {
                        'rate_per_sec': int,
                        'average_transmit_time_sec': int,
                        'average_transmit_time_nsec': int,
                    },
                },
                'process_time': {
                    'hello': {
                        'rate_per_sec': int,
                        'average_process_time_sec': int,
                        'average_process_time_nsec': int,
                    },
                    'csnp': {
                        'rate_per_sec': int,
                        'average_process_time_sec': int,
                        'average_process_time_nsec': int,
                    },
                    'psnp': {
                        'rate_per_sec': int,
                        'average_process_time_sec': int,
                        'average_process_time_nsec': int,
                    },
                    'lsp': {
                        'rate_per_sec': int,
                        'average_process_time_sec': int,
                        'average_process_time_nsec': int,
                    },
                },
                'level': {
                    Any(): {
                        'lsp': {
                            'new': int,
                            'refresh': int,
                        },
                        'address_family': {
                            Any(): {
                                'total_spf_calculation': int,
                                'full_spf_calculation': int,
                                'ispf_calculation': int,
                                'next_hop_calculation': int,
                                'partial_route_calculation': int,
                                'periodic_spf_calculation': int,
                            }
                        }
                    }
                },
                'interface': {
                    Any(): {
                        'level': {
                            Any(): {
                                Optional('lsps_sourced'): {
                                    'sent': int,
                                    'received': int,
                                    'arrival_time_throttled': int,
                                    'flooding_duplicates': int,
                                },
                                Optional('csnp'):  {
                                    'sent': int,
                                    'received': int,
                                },
                                Optional('psnp'): {
                                    'sent': int,
                                    'received': int,
                                },
                                Optional('dr'): {
                                    'elections': int
                                },
                                Optional('hello'): {
                                    'sent': int,
                                    'received': int,
                                }
                            }
                        }
                    }
                }
            }
        }
    }


class ShowIsisStatistics(ShowIsisStatisticsSchema):
    ''' Parser for commands:
        * show isis statistics
    '''

    cli_command = 'show isis statistics'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # IS-IS test statistics:
        r1 = re.compile(r'IS\-IS\s+(?P<isis>.+)\s+statistics\:')

        # Fast PSNP cache (hits/tries): 21/118
        r2 = re.compile(r'Fast\s+PSNP\s+cache\s*\(hits/tries\): '
                         '(?P<psnp_cach_hits>\d+)/(?P<psnp_cach_tries>\d+)')

        # Fast CSNP cache (hits/tries): 1398/1501
        r3 = re.compile(r'Fast\s+CSNP\s+cache\s*\(hits/tries\): '
                         '(?P<csnp_cach_hits>\d+)/(?P<csnp_cach_tries>\d+)')

        # Fast CSNP cache updates: 204
        r4 = re.compile(r'Fast\s+CSNP\s+cache\s+updates\s*:\s*'
                         '(?P<csnp_cache_updates>\d+)')

        # LSP checksum errors received: 0
        r5 = re.compile(r'LSP\s+checksum\s+errors\s+received\s*:\s*'
                         '(?P<lsp_checksum_errors_received>\d+)')

        # LSP Dropped: 0
        r6 = re.compile(r'LSP\s+Dropped\s*:\s*(?P<lsp_dropped>\d+)')

        # SNP Dropped: 0
        r7 = re.compile(r'SNP\s+Dropped\s*:\s*(?P<snp_dropped>\d+)')

        # UPD Max Queue size: 3
        r8 = re.compile(r'UPD\s+Max\s+Queue\s+size\s*:\s*'
                         '(?P<upd_max_queue_size>\d+)')

        # UPD Queue size: 0
        r9 = re.compile(r'UPD\s+Queue\s+size\s*:\s*(?P<upd_queue_size>\d+)')

        # Average transmit times and rate:
        r10 = re.compile(r'Average\s+transmit\s+times\s+and\s+rate\s*:')
        
        # Average process times and rate:
        r11 = re.compile(r'Average\s+process\s+times\s+and\s+rate\s*:')

        # Hello:          0 s,      66473 ns,         15/s
        r12 = re.compile(r'Hello\s*:\s+(?P<time_s>\d+)\s*\w+\,\s+'
                          '(?P<time_ns>\d+)\s*\w+\,\s+(?P<rate>\d+)/\w+')

        # CSNP:           0 s,      26914 ns,          1/s
        r13 = re.compile(r'CSNP\s*:\s+(?P<time_s>\d+)\s*\w+\,\s+'
                          '(?P<time_ns>\d+)\s*\w+\,\s+(?P<rate>\d+)/\w+')

        # PSNP:           0 s,       4113 ns,          0/s
        r14 = re.compile(r'PSNP\s*:\s+(?P<time_s>\d+)\s*\w+\,\s+'
                          '(?P<time_ns>\d+)\s*\w+\,\s+(?P<rate>\d+)/\w+')

        # LSP:            0 s,      52706 ns,          0/s
        r15 = re.compile(r'LSP\s*:\s+(?P<time_s>\d+)\s*\w+\,\s+(?P<time_ns>'
                          '\d+)\s*\w+\,\s+(?P<rate>\d+)/\w+')

        # Level-1:
        r16 = re.compile(r'Level\-(?P<level>\d+):')

        # LSPs sourced (new/refresh): 11/15
        # LSPs sourced (new/refresh): 13/11
        r17 = re.compile(r'LSPs\s+sourced\s*\(new/refresh\)\s*:\s*'
                          '(?P<lsp_source_new>\d+)\/(?P<lsp_source_refresh>\d+)')

        # IPv4 Unicast
        # IPv6 Unicast
        r18 = re.compile(r'(?P<address_family>(IPv4|IPv6) Unicast)')

        # Total SPF calculations     : 23
        r19 = re.compile(r'Total\s+SPF\s+calculations\s*:\s*'
                          '(?P<total_spf_calculation>\d+)')

        # Full SPF calculations      : 16
        r20 = re.compile(r'Full\s+SPF\s+calculations\s*:\s*'
                          '(?P<full_spf_calculation>\d+)')

        # ISPF calculations          : 0
        r21 = re.compile(r'ISPF\s+calculations\s*:\s*'
                          '(?P<ispf_calculation>\d+)')

        # Next Hop Calculations      : 0
        r22 = re.compile(r'Next\s+Hop\s+Calculations\s*:\s*'
                          '(?P<next_hop_calculation>\d+)')

        # Partial Route Calculations : 2
        r23 = re.compile(r'Partial\s+Route\s+Calculations\s*:\s*'
                          '(?P<partial_route_calculation>\d+)')

        # Periodic SPF calculations  : 3
        r24 = re.compile(r'Periodic\s+SPF\s+calculations\s*:\s*'
                          '(?P<periodic_spf_calculation>\d+)')
        
        # Interface Loopback0:
        # Interface GigabitEthernet0/0/0/1:
        r25 = re.compile(r'Interface\s+(?P<interface>\S+):')

        # Level-1 LSPs (sent/rcvd)  : 0/0
        # Level-2 LSPs (sent/rcvd)  : 0/0
        r26 = re.compile(r'Level\-(?P<level>\d+)\s+LSPs\s+\(sent\/rcvd\)\s*:'
                          '\s*(?P<lsp_sent>\d+)/(?P<lsp_received>\d+)')

        # Level-2 CSNPs (sent/rcvd) : 0/0
        # Level-1 CSNPs (sent/rcvd) : 339/0
        r27 = re.compile(r'Level\-(?P<level>\d+)\s+CSNPs\s+\(sent\/rcvd\)\s*:'
                          '\s*(?P<csnp_sent>\d+)/(?P<csnp_received>\d+)')

        # Level-1 PSNPs (sent/rcvd) : 0/0
        r28 = re.compile(r'Level\-(?P<level>\d+)\s+PSNPs\s+\(sent/rcvd\)\s*:'
                          '\s*(?P<psnp_sent>\d+)\/(?P<psnp_received>\d+)')

        # Level-1 LSP Flooding Duplicates     : 51
        r29 = re.compile(r'Level-(?P<level>\d+)\s+LSP\s+Flooding\s+Duplicates'
                          '\s*:\s*(?P<lsp_flooding_duplicates>\d+)')

        # Level-1 LSPs Arrival Time Throttled : 0
        # Level-2 LSPs Arrival Time Throttled : 0
        r30 = re.compile(r'Level-(?P<level>\d+)\s+LSPs\s+Arrival\s+Time\s+'
                          'Throttled\s*:\s*(?P<lsp_arrival_time_throttled>\d+)')

        # Level-1 Hellos (sent/rcvd): 594/593
        r31 = re.compile(r'Level-(?P<level>\d+)\s+Hellos\s+\(sent/rcvd\)\s*:'
                          '\s*(?P<hello_sent>\d+)/(?P<hello_received>\d+)')

        # Level-1 DR Elections      : 3
        # Level-2 DR Elections      : 3
        r32 = re.compile(r'Level-(?P<level>\d+)\s+DR\s+Elections\s*:'
                          '\s*(?P<dr_elections>\d+)')

        parsed_dict = {}
        vrf = 'default'

        for line in output.splitlines():
            line = line.strip()

            # IS-IS test statistics:            
            result = r1.match(line)
            if result:
                group = result.groupdict()
                isis = group['isis']
                isis_dict = parsed_dict\
                    .setdefault('isis', {})\
                    .setdefault(isis, {})

                continue

            # Fast PSNP cache (hits/tries): 21/118
            result = r2.match(line)
            if result:
                group = result.groupdict()
                psnp_cach_hits = int(group['psnp_cach_hits'])
                psnp_cach_tries = int(group['psnp_cach_tries'])
                psnp_cache = isis_dict.setdefault('psnp_cache', {})
                psnp_cache['hits'] = psnp_cach_hits
                psnp_cache['tries'] = psnp_cach_tries

                continue

            # Fast CSNP cache (hits/tries): 1398/1501
            result = r3.match(line)
            if result:
                group = result.groupdict()
                csnp_cach_hits = int(group['csnp_cach_hits'])
                csnp_cach_tries = int(group['csnp_cach_tries'])
                csnp_cache_dict = isis_dict.setdefault('csnp_cache', {})
                csnp_cache_dict['hits'] = csnp_cach_hits
                csnp_cache_dict['tries'] = csnp_cach_tries

                continue

            # Fast CSNP cache updates: 204
            result = r4.match(line)
            if result:
                group = result.groupdict()
                csnp_cache_updates = int(group['csnp_cache_updates'])
                csnp_cache_dict['updates'] = csnp_cache_updates

                continue

            # LSP checksum errors received: 0
            result = r5.match(line)
            if result:
                group = result.groupdict()
                lsp_checksum_errors_received = int(group['lsp_checksum_errors_received'])
                lsp_dict = isis_dict.setdefault('lsp', {})
                lsp_dict['checksum_errors_received'] = lsp_checksum_errors_received

                continue

            # LSP Dropped: 0
            result = r6.match(line)
            if result:
                group = result.groupdict()
                lsp_dropped = int(group['lsp_dropped'])
                lsp_dict['dropped'] = lsp_dropped

                continue

            # SNP Dropped: 0
            result = r7.match(line)
            if result:
                group = result.groupdict()
                snp_dropped = int(group['snp_dropped'])
                snp_dict = isis_dict.setdefault('snp', {})
                snp_dict['dropped'] = snp_dropped

                continue

            # UPD Max Queue size: 3
            result = r8.match(line)
            if result:
                group = result.groupdict()
                upd_max_queue_size = int(group['upd_max_queue_size'])
                upd_dict = isis_dict.setdefault('upd', {})
                upd_dict['max_queue_size'] = upd_max_queue_size

                continue

            # UPD Queue size: 0
            result = r9.match(line)
            if result:
                group = result.groupdict()
                upd_queue_size = int(group['upd_queue_size'])
                upd_dict['queue_size'] = upd_queue_size

                continue

            # Average transmit times and rate:
            result = r10.match(line)
            if result:
                process_transmit_time_dict = isis_dict\
                    .setdefault('transmit_time', {})
                average_time_key_name_sec = 'average_transmit_time_sec'
                average_time_key_name_nsec = 'average_transmit_time_nsec'

                continue
            
            # Average process times and rate:
            result = r11.match(line)
            if result:
                process_transmit_time_dict = isis_dict\
                    .setdefault('process_time', {})
                average_time_key_name_sec = 'average_process_time_sec'
                average_time_key_name_nsec = 'average_process_time_nsec'

                continue

            # Hello:          0 s,      66473 ns,         15/s
            result = r12.match(line)
            if result:
                group = result.groupdict()
                time1 = int(group['time_s'])
                time2 = int(group['time_ns'])
                rate = int(group['rate'])
                hello_dict = process_transmit_time_dict.setdefault('hello', {})
                hello_dict[average_time_key_name_sec] = time1
                hello_dict[average_time_key_name_nsec] = time2
                hello_dict['rate_per_sec'] = rate

                continue

            # CSNP:           0 s,      26914 ns,          1/s
            result = r13.match(line)
            if result:
                group = result.groupdict()
                time1 = int(group['time_s'])
                time2 = int(group['time_ns'])
                rate = int(group['rate'])
                csnp_dict = process_transmit_time_dict.setdefault('csnp', {})
                csnp_dict[average_time_key_name_sec] = time1
                csnp_dict[average_time_key_name_nsec] = time2
                csnp_dict['rate_per_sec'] = rate

                continue

            # PSNP:           0 s,       4113 ns,          0/s
            result = r14.match(line)
            if result:
                group = result.groupdict()
                time1 = int(group['time_s'])
                time2 = int(group['time_ns'])
                rate = int(group['rate'])
                psnp_dict = process_transmit_time_dict.setdefault('psnp', {})
                psnp_dict[average_time_key_name_sec] = time1
                psnp_dict[average_time_key_name_nsec] = time2
                psnp_dict['rate_per_sec'] = rate

                continue

            # LSP:            0 s,      52706 ns,          0/s
            result = r15.match(line)
            if result:
                group = result.groupdict()
                time1 = int(group['time_s'])
                time2 = int(group['time_ns'])
                rate = int(group['rate'])
                lsp_dict = process_transmit_time_dict.setdefault('lsp', {})
                lsp_dict[average_time_key_name_sec] = time1
                lsp_dict[average_time_key_name_nsec] = time2
                lsp_dict['rate_per_sec'] = rate

                continue

            # Level-1:
            result = r16.match(line)
            if result:
                group = result.groupdict()
                level = int(group['level'])
                level_dict = isis_dict.setdefault('level', {}).setdefault(level, {})

                continue

            # LSPs sourced (new/refresh): 11/15
            # LSPs sourced (new/refresh): 13/11
            result = r17.match(line)
            if result:
                group = result.groupdict()
                lsp_source_new = int(group['lsp_source_new'])
                lsp_source_refresh = int(group['lsp_source_refresh'])
                lsp_level_dict = level_dict.setdefault('lsp', {})
                lsp_level_dict['new'] = lsp_source_new
                lsp_level_dict['refresh'] = lsp_source_refresh

                continue

            # IPv4 Unicast
            # IPv6 Unicast
            result = r18.match(line)
            if result:
                group = result.groupdict()
                address_family = group['address_family']
                address_family_dict = level_dict\
                    .setdefault('address_family', {})\
                    .setdefault(address_family, {})

                continue

            # Total SPF calculations     : 23
            result = r19.match(line)
            if result:
                group = result.groupdict()
                total_spf_calculation = int(group['total_spf_calculation'])
                address_family_dict['total_spf_calculation'] = total_spf_calculation

                continue

            # Full SPF calculations      : 16
            result = r20.match(line)
            if result:
                group = result.groupdict()
                full_spf_calculation = int(group['full_spf_calculation'])
                address_family_dict['full_spf_calculation'] = full_spf_calculation

                continue

            # ISPF calculations          : 0
            result = r21.match(line)
            if result:
                group = result.groupdict()
                ispf_calculation = int(group['ispf_calculation'])
                address_family_dict['ispf_calculation'] = ispf_calculation

                continue

            # Next Hop Calculations      : 0
            result = r22.match(line)
            if result:
                group = result.groupdict()
                next_hop_calculation = int(group['next_hop_calculation'])
                address_family_dict['next_hop_calculation'] = next_hop_calculation

                continue

            # Partial Route Calculations : 2
            result = r23.match(line)
            if result:
                group = result.groupdict()
                partial_route_calculation = int(group['partial_route_calculation'])
                address_family_dict['partial_route_calculation'] = partial_route_calculation

                continue

            # Periodic SPF calculations  : 3
            result = r24.match(line)
            if result:
                group = result.groupdict()
                periodic_spf_calculation = int(group['periodic_spf_calculation'])
                address_family_dict['periodic_spf_calculation'] = periodic_spf_calculation

                continue
            
            # Interface Loopback0:
            # Interface GigabitEthernet0/0/0/1:
            result = r25.match(line)
            if result:
                group = result.groupdict()
                interface = group['interface']
                interface_dict = isis_dict\
                    .setdefault('interface', {})\
                    .setdefault(interface, {})
                continue

            # Level-1 LSPs (sent/rcvd)  : 0/0
            # Level-2 LSPs (sent/rcvd)  : 0/0            
            result = r26.match(line)
            if result:
                group = result.groupdict()
                level = int(group['level'])
                lsp_sent = int(group['lsp_sent'])
                lsp_received = int(group['lsp_received'])
                lsp_interface_dict = interface_dict\
                    .setdefault('level', {})\
                    .setdefault(level, {})\
                    .setdefault('lsps_sourced', {})
                lsp_interface_dict['sent'] = lsp_sent
                lsp_interface_dict['received'] = lsp_received

                continue

            # Level-2 CSNPs (sent/rcvd) : 0/0
            # Level-1 CSNPs (sent/rcvd) : 339/0
            result = r27.match(line)
            if result:
                group = result.groupdict()
                level = int(group['level'])
                csnp_sent = int(group['csnp_sent'])
                csnp_received = int(group['csnp_received'])
                csnp_interface_dict = interface_dict\
                    .setdefault('level', {})\
                    .setdefault(level, {})\
                    .setdefault('csnp', {})
                csnp_interface_dict['sent'] = csnp_sent
                csnp_interface_dict['received'] = csnp_received

                continue

            # Level-1 PSNPs (sent/rcvd) : 0/0
            result = r28.match(line)
            if result:
                group = result.groupdict()
                level = int(group['level'])
                psnp_sent = int(group['psnp_sent'])
                psnp_received = int(group['psnp_received'])
                psnp_interface_dict = interface_dict\
                    .setdefault('level', {})\
                    .setdefault(level, {})\
                    .setdefault('psnp', {})

                psnp_interface_dict['sent'] = psnp_sent
                psnp_interface_dict['received'] = psnp_received

                continue

            # Level-1 LSP Flooding Duplicates     : 51
            result = r29.match(line)
            if result:
                group = result.groupdict()
                level = int(group['level'])
                lsp_flooding_duplicates = int(group['lsp_flooding_duplicates'])
                lsp_interface_dict = interface_dict\
                    .setdefault('level', {})\
                    .setdefault(level, {})\
                    .setdefault('lsps_sourced', {})
                lsp_interface_dict['flooding_duplicates'] = lsp_flooding_duplicates

                continue

            # Level-1 LSPs Arrival Time Throttled : 0
            # Level-2 LSPs Arrival Time Throttled : 0
            result = r30.match(line)
            if result:
                group = result.groupdict()
                level = int(group['level'])
                lsp_arrival_time_throttled = int(group['lsp_arrival_time_throttled'])
                lsp_interface_dict = interface_dict\
                    .setdefault('level', {})\
                    .setdefault(level, {})\
                    .setdefault('lsps_sourced', {})
                lsp_interface_dict['arrival_time_throttled'] = lsp_arrival_time_throttled

                continue

            # Level-1 Hellos (sent/rcvd): 594/593
            result = r31.match(line)
            if result:
                group = result.groupdict()
                level = int(group['level'])
                hello_sent = int(group['hello_sent'])
                hello_received = int(group['hello_received'])
                hello_interface_dict = interface_dict\
                    .setdefault('level', {})\
                    .setdefault(level, {})\
                    .setdefault('hello', {})
                hello_interface_dict['received'] = hello_sent
                hello_interface_dict['sent'] = hello_received

                continue

            # Level-1 DR Elections      : 3
            # Level-2 DR Elections      : 3
            result = r32.match(line)
            if result:
                group = result.groupdict()
                level = int(group['level'])
                dr_elections = int(group['dr_elections'])
                dr_dict = interface_dict\
                    .setdefault('level', {})\
                    .setdefault(level, {})\
                    .setdefault('dr', {})
                dr_dict['elections'] = dr_elections

                continue

        return parsed_dict