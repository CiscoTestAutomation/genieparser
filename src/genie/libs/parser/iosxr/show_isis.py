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
                        Optional('manual_area_address'): list,
                        Optional('routing_area_address'): list,
                        'non_stop_forwarding': str,
                        'most_recent_startup_mode': str,
                        'te_connection_status': str,
                        Optional('srlb'): {
                            'start': int,
                            'end': int,
                        },
                        Optional('srgb'): {
                            'start': int,
                            'end': int,
                        },
                        Optional('interfaces'): {
                            Any(): {
                                'running_state': str,
                                'configuration_state': str,
                            }
                        },
                        Optional('topology'): {
                            Any(): {
                                'vrf': {
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

        # VRF context: VRF1
        r2 = re.compile(r'VRF\s+context\s*:\s*(?P<vrf>.+)')

        # System Id: 3333.3333.3333
        r3 = re.compile(r'System\s+Id\s*:\s*(?P<system_id>\S+)')

        # Instance Id: 0
        r4 = re.compile(r'Instance\s+Id\s*:\s*(?P<instance_id>\S+)')

        # IS Levels: level-1-2
        # IS Levels: level-2-only
        # IS Levels: level-1-only
        r5 = re.compile(r'IS\s+Levels\s*:\s*'
                         '(?P<is_levels>level-1-2|level-(1|2)-only)')

        # Manual area address(es):
        r6 = re.compile(r'Manual\s+area\s+address\(es\):')

        # Routing for area address(es):
        r7 = re.compile(r'Routing\s+for\s+area\s+address\(es\):')

        # 49.0002
        r8 = re.compile(r'(?P<area_address>\d+\.\d+)')

        # Non-stop forwarding: Disabled
        r9 = re.compile(r'Non\-stop\s+forwarding\s*:\s*(?P<non_stop_forwarding>\w+)')

        # Most recent startup mode: Cold Restart
        r10 = re.compile(r'Most\s+recent\s+startup\s+mode\s*:\s*(?P<most_recent_startup_mode>.+)')

        # TE connection status: Down
        r11 = re.compile(r'TE\s+connection\s+status\s*:\s*(?P<te_connection_status>.+)')

        # Topologies supported by IS-IS:
        r12 = re.compile(r'Topologies\s+supported\s+by\s+IS\-IS:')

        # IPv4 Unicast
        # IPv6 Unicast
        # IPv4 Unicast VRF VRF1
        r13 = re.compile(r'(?P<topology>(IPv6|IPv4)\s+Unicast)'
                          '(\s*VRF\s*(?P<topology_vrf>\S+))?')

        # Level-1
        # Level-2
        r14 = re.compile(r'Level\-(?P<level>\d+)')

        # Metric style (generate/accept): Wide/Wide
        r15 = re.compile(r'Metric\s+style\s*\(generate\/accept\)\s*:\s*'
                          '(?P<generate_style>\w+)\/(?P<accept_style>\w+)')

        # Metric: 10
        r16 = re.compile(r'Metric\s*:\s*(?P<metric>\d+)')

        # ISPF status: Disabled
        r17 = re.compile(r'ISPF\s+status\s*:\s*(?P<ispf_status>\w+)')

        # No protocols redistributed
        r18 = re.compile(r'No\s+protocols\s+redistributed')

        # Distance: 115
        r19 = re.compile(r'Distance\s*:\s*(?P<distance>\d+)')

        # Advertise Passive Interface Prefixes Only: No
        r20 = re.compile(r'Advertise\s+Passive\s+Interface\s+Prefixes\s+Only'
                          '\s*:\s*(?P<adv_passive_only>\S+)')

        # SRLB not allocated
        # SRLB allocated: 15000 - 15999
        r21 = re.compile(r'SRLB\s*(?P<srlb>[\w\s]+)'
                          '(\:\s*(?P<start>\d+)\s*\-\s*(?P<end>\d+))?')

        # SRGB allocated: 16000 - 81534
        # SRGB not allocated
        r22 = re.compile(r'SRGB\s*(?P<srgb>[\w\s]+)'
                          '(\:\s*(?P<start>\d+)\s*\-\s*(?P<end>\d+))?')

        # Loopback0 is running actively (active in configuration)
        # GigabitEthernet0/0/0/0 is running actively (active in configuration)
        r23 = re.compile(r'(?P<interface>\S+)\s+is\s+(?P<running_state>[\s\w]+)'
                          '\s+\((?P<configuration_state>[\w\s]+)\)')

        parsed_output = {}
        vrf = 'default'
        topology_vrf = 'default'

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
            
            # VRF context: VRF1     
            result = r2.match(line)
            if result:
                group = result.groupdict()
                vrf = group['vrf']

                continue

            # System Id: 3333.3333.3333
            result = r3.match(line)
            if result:
                group = result.groupdict()
                system_id = group['system_id']

                continue

            # Instance Id: 0
            result = r4.match(line)
            if result:
                group = result.groupdict()
                instance_id = group['instance_id']
                instance_dict['instance'] = instance_id
                vrf_dict = instance_dict\
                    .setdefault('vrf', {})\
                    .setdefault(vrf, {})
                vrf_dict['system_id'] = system_id
                vrf = 'default'

                continue

            # IS Levels: level-1-2
            result = r5.match(line)
            if result:
                group = result.groupdict()
                is_levels = group['is_levels']
                vrf_dict['is_levels'] = is_levels

                continue

            # Manual area address(es):
            result = r6.match(line)
            if result:
                area_address_field = 'manual_area_address'

                continue

            # Routing for area address(es):
            result = r7.match(line)
            if result:
                area_address_field = 'routing_area_address'

                continue

            # 49.0002
            result = r8.match(line)
            if result:
                group = result.groupdict()
                area_address = group['area_address']
                area_address_list = vrf_dict.get(area_address_field, [])
                area_address_list.append(area_address)
                vrf_dict[area_address_field] = area_address_list

                continue

            # Non-stop forwarding: Disabled
            result = r9.match(line)
            if result:
                group = result.groupdict()
                non_stop_forwarding = group['non_stop_forwarding']
                vrf_dict['non_stop_forwarding'] = non_stop_forwarding

                continue

            # Most recent startup mode: Cold Restart
            result = r10.match(line)
            if result:
                group = result.groupdict()
                most_recent_startup_mode = group['most_recent_startup_mode']
                vrf_dict['most_recent_startup_mode'] = most_recent_startup_mode

                continue

            # TE connection status: Down
            result = r11.match(line)
            if result:
                group = result.groupdict()
                te_connection_status = group['te_connection_status']
                vrf_dict['te_connection_status'] = te_connection_status

                continue

            # Topologies supported by IS-IS:
            result = r12.match(line)
            if result:
                topology_dict = vrf_dict.setdefault('topology', {})

                continue

            if line == 'none':
                del(vrf_dict['topology'])

                continue

            # IPv4 Unicast
            # IPv6 Unicast
            # IPv4 Unicast VRF VRF1
            result = r13.match(line)
            if result:
                group = result.groupdict()
                topology = group['topology']
                if group['topology_vrf']:
                    topology_vrf = group['topology_vrf']
                address_family_dict = topology_dict\
                    .setdefault(topology, {})\
                    .setdefault('vrf', {})\
                    .setdefault(topology_vrf, {})
                topology_vrf = 'default'

                continue

            # Level-1
            # Level-2
            result = r14.match(line)
            if result:
                group = result.groupdict()
                level = int(group['level'])
                level_dict = address_family_dict\
                    .setdefault('level', {})\
                    .setdefault(level, {})

                continue

            # Metric style (generate/accept): Wide/Wide
            result = r15.match(line)
            if result:
                group = result.groupdict()
                generate_style = group['generate_style']
                accept_style = group['accept_style']
                level_dict['generate_style'] = generate_style
                level_dict['accept_style'] = accept_style

                continue

            # Metric: 10
            result = r16.match(line)
            if result:
                group = result.groupdict()
                metric = int(group['metric'])
                level_dict['metric'] = metric

                continue

            # ISPF status: Disabled
            result = r17.match(line)
            if result:
                group = result.groupdict()
                ispf_status = group['ispf_status']
                level_dict['ispf_status'] = ispf_status

                continue

            # No protocols redistributed
            result = r18.match(line)
            if result:
                address_family_dict['protocols_redistributed'] = False

                continue

            # Distance: 115
            result = r19.match(line)
            if result:
                group = result.groupdict()
                distance = int(group['distance'])
                address_family_dict['distance'] = distance

                continue

            # Advertise Passive Interface Prefixes Only: No
            result = r20.match(line)
            if result:
                group = result.groupdict()
                if group['adv_passive_only'] == 'No':
                    adv_passive_only = False
                else:
                    adv_passive_only = True
                address_family_dict['adv_passive_only'] = adv_passive_only

                continue

            # SRLB not allocated
            # SRLB allocated: 15000 - 15999
            result = r21.match(line)
            if result:
                group = result.groupdict()
                start = group['start']
                end = group['end']
                if start and end:
                    srlb_dict = vrf_dict.setdefault('srlb', {})
                    srlb_dict['start'] = int(start)
                    srlb_dict['end'] = int(end)

                continue
            
            # SRGB allocated: 16000 - 81534
            # SRGB not allocated
            result = r22.match(line)
            if result:
                group = result.groupdict()
                start = group['start']
                end = group['end']
                if start and end:
                    srlb_dict = vrf_dict.setdefault('srgb', {})
                    srlb_dict['start'] = int(start)
                    srlb_dict['end'] = int(end) 

                continue

            # Loopback0 is running actively (active in configuration)
            # GigabitEthernet0/0/0/0 is running actively (active in configuration)
            result = r23.match(line)
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


class ShowIsisProtocol(ShowIsis):
    ''' Parser for commands:
        * show isis protocol
    '''
    cli_command = 'show isis protocol'

    def cli(self, output=None):
        if not output:
            output = self.device.execute(self.cli_command)

        return super().cli(output=output)
        