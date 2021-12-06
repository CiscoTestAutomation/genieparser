"""
show_isis.py

IOSXR parsers for the following show commands:
    * show isis
    * show isis lsp-log
    * show isis spf-log
    * show isis protocol
    * show isis hostname
    * show isis adjacency
    * show isis neighbors
    * show isis interface
    * show isis statistics
    * show isis private all
    * show isis spf-log detail
    * show isis database detail
    * show isis fast-reroute summary
    * show isis instance {instance} hostname
    * show isis segment-routing srv6 locators
    * show isis instance {instance} segment-routing srv6 locators
"""

# Python
import re
from netaddr import IPAddress, IPNetwork

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional
from genie.libs.parser.utils.common import Common

#============================================
# Schema for 'show isis fast-reroute summary'
#============================================

class ShowIsisFastRerouteSummarySchema(MetaParser):
    ''' 'Schema for 'show isis fast-reroute summary' '''

    schema = {
        'instance':{
            Any():{
                'topology':{
                    Any():{
                        'level':{
                            Any():{
                                Any():{
                                    'critical_priority': int,
                                    'high_priority': int,
                                    'medium_priority': int,
                                    'low_priority': int,
                                    'total': int,
                                },
                                'protection_coverage':{
                                    'critical_priority': str,
                                    'high_priority': str,
                                    'medium_priority': str,
                                    'low_priority': str,
                                    'total': str,
                                },
                            },
                        },
                    },
                },
            },
        },
    }

#============================================
# Parser for 'show isis fast-reroute summary'
#============================================

class ShowIsisFastRerouteSummary(ShowIsisFastRerouteSummarySchema):
    ''' 'Parser for 'show isis fast-reroute summary' '''


    cli_command = ['show isis fast-reroute summary']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        #Init vars
        ret_dict = {}
        label_list = ['critical_priority', 'high_priority', 'medium_priority', 'low_priority', 'total']


        # IS-IS SR IPv4 Unicast FRR summary
        p1 = re.compile(r'IS-IS +(?P<instance>\S+) +(?P<topology>\S+\s+\S+) +FRR +summary')

        # Prefixes reachable in L1
        p2 = re.compile(r'Prefixes +reachable +in +L(?P<level>\d+)')

        #                       Critical   High       Medium     Low        Total
        #                       Priority   Priority   Priority   Priority
        #--------------------------------------------------------------------------------
        # All paths protected     0          0          0          0          0
        # Some paths protected    0          0          0          0          0
        # Unprotected             0          0          4          6          10
        p3 = re.compile(r'(?P<name>[\S\s]+) +(?P<critical_priority>\d+) +(?P<high_priority>\d+) +(?P<medium_priority>\d+) +(?P<low_priority>\d+) +(?P<total>\d+)')

        # Protection coverage     0.00%      0.00%      0.00%      0.00%      0.00%
        p4 = re.compile(r'Protection +coverage +(?P<critical_priority>[\d\.\%]+) +(?P<high_priority>[\d\.\%]+) +(?P<medium_priority>[\d\.\%]+) +(?P<low_priority>[\d\.\%]+) +(?P<total>[\d\.\%]+)')

        for line in out.splitlines():
            line = line.strip()

            # IS-IS SR IPv4 Unicast FRR summary
            m = p1.match(line)
            if m:
                group = m.groupdict()
                instance = group ['instance']
                topology = group ['topology']
                instance_dict = ret_dict.setdefault('instance', {}).setdefault(instance, {}).\
                    setdefault('topology',{}).setdefault(topology, {})

            # Prefixes reachable in L1
            m = p2.match(line)
            if m:
               group = m.groupdict()
               frr_sum_dict = instance_dict.setdefault('level', {}).setdefault(int(group['level']), {})
               continue

            #                       Critical   High       Medium     Low        Total
            #                       Priority   Priority   Priority   Priority
            #--------------------------------------------------------------------------------
            # All paths protected     0          0          0          0          0
            # Some paths protected    0          0          0          0          0
            # Unprotected             0          0          4          6          10
            m = p3.match(line)
            if m:
               group = m.groupdict()
               label_name = group['name'].strip().lower().replace(' ','_')
               label_dict = frr_sum_dict.setdefault(label_name, {})
               for key in label_list:
                   label_dict.update({key: int(group[key])})
               continue

            # Protection coverage     0.00%      0.00%      0.00%      0.00%      0.00%
            m = p4.match(line)
            if m:
               group = m.groupdict()
               coverage_dict = frr_sum_dict.setdefault('protection_coverage', {})
               for key in label_list:
                  coverage_dict.update({key: group[key]})
               continue

        return ret_dict

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

        # R1_xe          Gi0/0/0/0.115    fa16.3eff.4f49 Up    26   22:30:26 Yes None None
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

            # R1_xe          Gi0/0/0/0.115    fa16.3eff.4f49 Up    26   22:30:26 Yes None None
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

        # R1_xe          Gi0/0/0/0.115    fa16.3eff.4f49 Up    24       L1L2 Capable
        p2 = re.compile(r'^(?P<system_id>\S+) +(?P<interface>\S+) +(?P<snpa>\S+) +(?P<state>(Up|Down|None|Init)+) +(?P<holdtime>\S+) '
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

            # R1_xe          Gi0/0/0/0.115    fa16.3eff.4f49 Up    24       L1L2 Capable
            m = p2.match(line)
            if m:
                system_id = m.groupdict()['system_id']
                interface_name = Common.convert_intf_name(m.groupdict()['interface'])
                snpa = m.groupdict()['snpa']
                state = m.groupdict()['state']
                holdtime = m.groupdict()['holdtime']
                type_ = m.groupdict()['type']
                ietf_nsf = m.groupdict()['ietf_nsf']

                interface_dict = vrf_dict.setdefault('interfaces', {}).setdefault(interface_name, {})
                system_dict = interface_dict.setdefault('neighbors', {}).setdefault(system_id, {})
                system_dict['snpa'] = snpa
                system_dict['state'] = state
                system_dict['holdtime'] = holdtime
                system_dict['type'] = type_
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
        * show isis protocol
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
                                        Optional('protocols_redistributed'): bool,
                                        'level': {
                                            Any(): {
                                                Optional('generate_style'): str,
                                                Optional('accept_style'): str,
                                                'metric': int,
                                                Optional('ispf_status'): str,
                                            }
                                        },
                                        Optional('redistributing'): list,
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
        * show isis protocol
    '''

    cli_command = 'show isis'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # IS-IS Router: test
        r1 = re.compile(r'IS\-IS\s+Router\s*:\s*(?P<isis_router>\S+)')

        # VRF context: VRF1
        r2 = re.compile(r'VRF\s+context\s*:\s*(?P<vrf>.+)')

        # System Id: 3333.33ff.6666
        r3 = re.compile(r'System\s+Id\s*:\s*(?P<system_id>\S+)')

        # Instance Id: 0
        r4 = re.compile(r'Instance\s+Id\s*:\s*(?P<instance_id>\S+)')

        # IS Levels: level-1-2
        # IS Levels: level-2-only
        # IS Levels: level-1-only
        # IS Levels: level-1
        r5 = re.compile(r'IS\s+Levels\s*:\s*(?P<is_levels>\S+)')

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

        # OSPF process 75688
        r24 = re.compile(r'^(?P<protocol>\S+) process +(?P<process>\d+)$')

        # Connected
        r25 = re.compile(r'^Connected$')

        # Static
        r26 = re.compile(r'^Static$')


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

            # System Id: 3333.33ff.6666
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

            # OSPF process 75688
            result = r24.match(line)
            if result:
                group = result.groupdict()
                redistributing_list = address_family_dict.get('redistributing', [])
                redistributing_list.append(line)
                address_family_dict.update({'redistributing': redistributing_list})
                address_family_dict['protocols_redistributed'] = True
                continue

            # Connected
            result = r25.match(line)
            if result:
                group = result.groupdict()
                redistributing_list = address_family_dict.get('redistributing', [])
                redistributing_list.append(line)
                address_family_dict.update({'redistributing': redistributing_list})
                address_family_dict['protocols_redistributed'] = True
                continue

            # Static
            result = r26.match(line)
            if result:
                group = result.groupdict()
                redistributing_list = address_family_dict.get('redistributing', [])
                redistributing_list.append(line)
                address_family_dict.update({'redistributing': redistributing_list})
                address_family_dict['protocols_redistributed'] = True
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

        # 2     1720.18ff.0254 tor-28.tenlab-cloud
        # 2     1720.18ff.0213 leaf-2.qa-site1
        # 2     1720.18ff.0250 tor-23.tenlab-cloud
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

            # 2     1720.18ff.0254 tor-28.tenlab-cloud
            # 2     1720.18ff.0213 leaf-2.qa-site1
            # 2     1720.18ff.0250 tor-23.tenlab-cloud
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
                    Optional('queue_size'): int,
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
                        Optional('level'): {
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
                        r'(?P<psnp_cach_hits>\d+)/(?P<psnp_cach_tries>\d+)')

        # Fast CSNP cache (hits/tries): 1398/1501
        r3 = re.compile(r'Fast\s+CSNP\s+cache\s*\(hits/tries\): '
                        r'(?P<csnp_cach_hits>\d+)/(?P<csnp_cach_tries>\d+)')

        # Fast CSNP cache updates: 204
        r4 = re.compile(r'Fast\s+CSNP\s+cache\s+updates\s*:\s*'
                        r'(?P<csnp_cache_updates>\d+)')

        # LSP checksum errors received: 0
        r5 = re.compile(r'LSP\s+checksum\s+errors\s+received\s*:\s*'
                        r'(?P<lsp_checksum_errors_received>\d+)')

        # LSP Dropped: 0
        r6 = re.compile(r'LSP\s+Dropped\s*:\s*(?P<lsp_dropped>\d+)')

        # SNP Dropped: 0
        r7 = re.compile(r'SNP\s+Dropped\s*:\s*(?P<snp_dropped>\d+)')

        # UPD Max Queue size: 3
        r8 = re.compile(r'UPD\s+Max\s+Queue\s+size\s*:\s*'
                        r'(?P<upd_max_queue_size>\d+)')

        # UPD Queue size: 0
        r9 = re.compile(r'UPD\s+Queue\s+size\s*:\s*(?P<upd_queue_size>\d+)')

        # Average transmit times and rate:
        r10 = re.compile(r'Average\s+transmit\s+times\s+and\s+rate\s*:')

        # Average process times and rate:
        r11 = re.compile(r'Average\s+process\s+times\s+and\s+rate\s*:')

        # Hello:          0 s,      66473 ns,         15/s
        r12 = re.compile(r'Hello\s*:\s+(?P<time_s>\d+)\s*\w+\,\s+'
                         r'(?P<time_ns>\d+)\s*\w+\,\s+(?P<rate>\d+)/\w+')

        # CSNP:           0 s,      26914 ns,          1/s
        r13 = re.compile(r'CSNP\s*:\s+(?P<time_s>\d+)\s*\w+\,\s+'
                         r'(?P<time_ns>\d+)\s*\w+\,\s+(?P<rate>\d+)/\w+')

        # PSNP:           0 s,       4113 ns,          0/s
        r14 = re.compile(r'PSNP\s*:\s+(?P<time_s>\d+)\s*\w+\,\s+'
                         r'(?P<time_ns>\d+)\s*\w+\,\s+(?P<rate>\d+)/\w+')

        # LSP:            0 s,      52706 ns,          0/s
        r15 = re.compile(r'LSP\s*:\s+(?P<time_s>\d+)\s*\w+\,\s+(?P<time_ns>'
                         r'\d+)\s*\w+\,\s+(?P<rate>\d+)/\w+')

        # Level-1:
        r16 = re.compile(r'Level\-(?P<level>\d+):')

        # LSPs sourced (new/refresh): 11/15
        # LSPs sourced (new/refresh): 13/11
        r17 = re.compile(r'LSPs\s+sourced\s*\(new/refresh\)\s*:\s*'
                         r'(?P<lsp_source_new>\d+)\/(?P<lsp_source_refresh>\d+)')

        # IPv4 Unicast
        # IPv6 Unicast
        r18 = re.compile(r'(?P<address_family>(IPv4|IPv6) Unicast)')

        # Total SPF calculations     : 23
        r19 = re.compile(r'Total\s+SPF\s+calculations\s*:\s*'
                         r'(?P<total_spf_calculation>\d+)')

        # Full SPF calculations      : 16
        r20 = re.compile(r'Full\s+SPF\s+calculations\s*:\s*'
                         r'(?P<full_spf_calculation>\d+)')

        # ISPF calculations          : 0
        r21 = re.compile(r'ISPF\s+calculations\s*:\s*'
                         r'(?P<ispf_calculation>\d+)')

        # Next Hop Calculations      : 0
        r22 = re.compile(r'Next\s+Hop\s+Calculations\s*:\s*'
                         r'(?P<next_hop_calculation>\d+)')

        # Partial Route Calculations : 2
        r23 = re.compile(r'Partial\s+Route\s+Calculations\s*:\s*'
                         r'(?P<partial_route_calculation>\d+)')

        # Periodic SPF calculations  : 3
        r24 = re.compile(r'Periodic\s+SPF\s+calculations\s*:\s*'
                         r'(?P<periodic_spf_calculation>\d+)')

        # Interface Loopback0:
        # Interface GigabitEthernet0/0/0/1:
        r25 = re.compile(r'Interface\s+(?P<interface>\S+):')

        # Level-1 LSPs (sent/rcvd)  : 0/0
        # Level-2 LSPs (sent/rcvd)  : 0/0
        r26 = re.compile(r'Level\-(?P<level>\d+)\s+LSPs\s+\(sent\/rcvd\)\s*:'
                         r'\s*(?P<lsp_sent>\d+)/(?P<lsp_received>\d+)')

        # Level-2 CSNPs (sent/rcvd) : 0/0
        # Level-1 CSNPs (sent/rcvd) : 339/0
        r27 = re.compile(r'Level\-(?P<level>\d+)\s+CSNPs\s+\(sent\/rcvd\)\s*:'
                         r'\s*(?P<csnp_sent>\d+)/(?P<csnp_received>\d+)')

        # Level-1 PSNPs (sent/rcvd) : 0/0
        r28 = re.compile(r'Level\-(?P<level>\d+)\s+PSNPs\s+\(sent/rcvd\)\s*:'
                         r'\s*(?P<psnp_sent>\d+)\/(?P<psnp_received>\d+)')

        # Level-1 LSP Flooding Duplicates     : 51
        r29 = re.compile(r'Level-(?P<level>\d+)\s+LSP\s+Flooding\s+Duplicates'
                         r'\s*:\s*(?P<lsp_flooding_duplicates>\d+)')

        # Level-1 LSPs Arrival Time Throttled : 0
        # Level-2 LSPs Arrival Time Throttled : 0
        r30 = re.compile(r'Level-(?P<level>\d+)\s+LSPs\s+Arrival\s+Time\s+'
                         r'Throttled\s*:\s*(?P<lsp_arrival_time_throttled>\d+)')

        # Level-1 Hellos (sent/rcvd): 594/593
        r31 = re.compile(r'Level-(?P<level>\d+)\s+Hellos\s+\(sent/rcvd\)\s*:'
                         r'\s*(?P<hello_sent>\d+)/(?P<hello_received>\d+)')

        # Level-1 DR Elections      : 3
        # Level-2 DR Elections      : 3
        r32 = re.compile(r'Level-(?P<level>\d+)\s+DR\s+Elections\s*:'
                         r'\s*(?P<dr_elections>\d+)')

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


class ShowIsisSpfLogSchema(MetaParser):
    ''' Schema for command
        * show isis spf-log
    '''
    schema = {
        'instance': {
            Any():{
                'address_family': {
                    Any(): {
                        'spf_log': {
                            Any(): {
                                'type': str,
                                'start_timestamp': str,
                                'time_ms': int,
                                'level': int,
                                'total_nodes': int,
                                'trigger_count': int,
                                Optional('first_trigger_lsp'): str,
                                'triggers': str,
                            }
                        }
                    }
                }
            }
        }
    }


class ShowIsisSpfLog(ShowIsisSpfLogSchema):
    ''' Parser for commands:
        * show isis spf-log
    '''

    cli_command = 'show isis spf-log'

    def cli(self, output=None):
        if not output:
            output = self.device.execute(self.cli_command)

        # IS-IS TEST Level 2 IPv4 Unicast Route Calculation Log
        r1 = re.compile(r'IS\-IS\s+(?P<instance>\S+)\s+Level\s+(?P<level>\d+)'
                         '\s+(?P<address_family>.+)\s+Route\s+Calculation\s+Log')

        # --- Mon Oct  7 2019 ---
        r2 = re.compile(r'\-\-\-\s+(?P<log_date>[\s\w]+)\s+\-\-\-')

        #                     Time Total Trig.
        # Timestamp    Type   (ms) Nodes Count First Trigger LSP    Triggers
        # ------------ ----- ----- ----- ----- -------------------- -----------------------
        # 00:00:17.514   PRC     0    64     6      bla-host1.12-34 PREFIXBAD
        # 23:42:51.522 PPFRR     0    64     1                      PERPREFIXFRR
        r3 = re.compile(r'(?P<timestamp>[0-9\:\.]+)\s+(?P<log_type>\S+)\s+(?P<time_ms>\d+)'
                         '\s+(?P<total_nodes>\d+)\s+(?P<trigger_count>\d+)\s+'
                         '(?P<first_trigger_lsp>\S*)\s+(?P<triggers>[\w\s]+)')

        parsed_output = {}
        log_index = 1

        for line in output.splitlines():
            line = line.strip()

            # IS-IS TEST Level 2 IPv4 Unicast Route Calculation Log
            result = r1.match(line)
            if result:
                group = result.groupdict()
                instance = group['instance']
                level = int(group['level'])
                address_family = group['address_family']
                instance_dict = parsed_output\
                    .setdefault('instance', {})\
                    .setdefault(instance, {})\
                    .setdefault('address_family', {})\
                    .setdefault(address_family, {})

                continue

            # --- Mon Oct  7 2019 ---
            result = r2.match(line)
            if result:
                group = result.groupdict()
                log_date = group['log_date']

                continue

            #                     Time Total Trig.
            # Timestamp    Type   (ms) Nodes Count First Trigger LSP    Triggers
            # ------------ ----- ----- ----- ----- -------------------- -----------------------
            # 00:00:17.514   PRC     0    64     6      bla-host1.12-34 PREFIXBAD
            # 23:42:51.522 PPFRR     0    64     1                      PERPREFIXFRR
            result = r3.match(line)
            if result:
                group = result.groupdict()
                timestamp = group['timestamp']
                log_type = group['log_type']
                time_ms = int(group['time_ms'])
                total_nodes = int(group['total_nodes'])
                trigger_count = int(group['trigger_count'])
                first_trigger_lsp = group['first_trigger_lsp']
                triggers = group['triggers']
                index_dict = instance_dict\
                    .setdefault('spf_log', {})\
                    .setdefault(log_index, {})
                index_dict['start_timestamp'] = "{} {}".format(log_date, timestamp)
                index_dict['level'] = level
                index_dict['type'] = log_type
                index_dict['time_ms'] = time_ms
                index_dict['total_nodes'] = total_nodes
                index_dict['trigger_count'] = trigger_count
                if first_trigger_lsp:
                    index_dict['first_trigger_lsp'] = first_trigger_lsp
                index_dict['triggers'] = triggers
                log_index += 1

                continue

        return parsed_output


class ShowIsisSpfLogDetailSchema(MetaParser):
    ''' Schema for command
        * show isis spf-log detail
    '''
    schema = {
        'instance': {
            Any(): {
                'address_family': {
                    Any(): {
                        'spf_log': {
                            Any(): {
                                'type': str,
                                'start_timestamp': str,
                                'total_nodes': int,
                                'time_ms': int,
                                'level': int,
                                Optional('first_trigger_lsp'): str,
                                'triggers': str,
                                'trigger_count': int,
                                Optional('sr_uloop'): str,
                                'delay': {
                                    'since_first_trigger_ms': int,
                                    Optional('since_end_of_last_calculation'): int,
                                },
                                Optional('trigger_prefix'): str,
                                Optional('interrupted'): str,
                                Optional('rib_batches'): {
                                    'total': str,
                                    Optional('critical'): str,
                                    Optional('high'): str,
                                    Optional('medium'): str,
                                    Optional('low'): str,
                                },
                                'spt_calculation': {
                                    'cpu_time_ms': int,
                                    'real_time_ms': int,
                                },
                                'prefix_update': {
                                    'cpu_time_ms': int,
                                    'real_time_ms': int,
                                },
                                Optional('full_calculation'):{
                                    'cpu_time_ms': int,
                                    'real_time_ms': int,
                                },
                                'new_lsp_arrivals': int,
                                'next_wait_interval_ms': int,
                                Optional('results'): {
                                    'nodes': {
                                        'reach': int,
                                        'unreach': int,
                                        'total': int,
                                    },
                                    'prefixes': {
                                        'items': {
                                            'critical_priority': {
                                                'reach': int,
                                                Optional('unreach'): int,
                                                'total': int,
                                            },
                                            'high_priority': {
                                                'reach': int,
                                                Optional('unreach'): int,
                                                'total': int,
                                            },
                                            'medium_priority': {
                                                'reach': int,
                                                Optional('unreach'): int,
                                                'total': int,
                                            },
                                            'low_priority': {
                                                'reach': int,
                                                Optional('unreach'): int,
                                                'total': int,
                                            },
                                            'all_priority': {
                                                'reach': int,
                                                Optional('unreach'): int,
                                                'total': int,
                                            },
                                        },
                                        'routes': {
                                            'critical_priority': {
                                                'reach': int,
                                                Optional('unreach'): int,
                                                'total': int,
                                            },
                                            'high_priority': {
                                                'reach': int,
                                                Optional('unreach'): int,
                                                'total': int,
                                            },
                                            'medium_priority': {
                                                'reach': int,
                                                Optional('unreach'): int,
                                                'total': int,
                                            },
                                            'low_priority': {
                                                'reach': int,
                                                Optional('unreach'): int,
                                                'total': int,
                                            },
                                            'all_priority': {
                                                'reach': int,
                                                Optional('unreach'): int,
                                                'total': int,
                                            },
                                        }
                                    },
                                }
                            }
                        }
                    }
                }
            }
        }
    }


class ShowIsisSpfLogDetail(ShowIsisSpfLogDetailSchema):
    ''' Parser for command
        * show isis spf-log detail
    '''

    cli_command = 'show isis spf-log detail'
    def cli(self, output=None):

        if not output:
            output = self.device.execute(self.cli_command)

        # ISIS isp Level 1 IPv4 Unicast Route Calculation Log
        r1 = re.compile(r'IS\-*IS\s+(?P<instance>\S+)\s+Level\s+(?P<level>\d+)'
                        r'\s+(?P<address_family>.+)\s+Route\s+Calculation\s+Log')

        #                    Time  Total Trig
        # Timestamp     Type (ms)  Nodes Count  First Trigger LSP   Triggers
        # 19:25:35.140  FSPF  1    1     1             12a5.00-00   NEWLSP0
        r2 = re.compile(r'^(?P<timestamp>[\d\:\.]+)\s+(?P<type>\w+)\s+'
                r'(?P<time_ms>\d+)\s+(?P<nodes>\d+)\s+(?P<count>\d+)'
                r'(\s+(?P<first_trigger_lsp>[\w\-\.]+))?\s+(?P<triggers>\w+)')

        # Delay:              51ms (since first trigger)
        r3 = re.compile(r'Delay\s*:\s*(?P<delay>\d+)ms\s+'
                        r'\((?P<delay_info>[\w\s]+)\)')

        # SPT Calculation
        r4 = re.compile(r'SPT\s+Calculation$')

        # SPT Calculation:         5     5
        r4_1 = re.compile(r'^SPT +Calculation: +(?P<cpu_time>\d+) +(?P<real_time>\d+)$')

        # Prefix Updates
        r5 = re.compile(r'Prefix\s+Updates')

        # Route Update:            0     0
        r5_1 = re.compile(r'^Route +Update: +(?P<cpu_time>\d+) +(?P<real_time>\d+)$')

        # Full Calculation:        0     0
        r5_2 = re.compile(r'^Full +Calculation: +(?P<cpu_time>\d+) +(?P<real_time>\d+)$')

        # CPU Time:         1ms
        # CPU Time:         0ms
        r6 = re.compile(r'CPU\s+Time\s*:\s*(?P<cpu_time>\d+)\w+')

        # Real Time:        0ms
        r7 = re.compile(r'Real\s+Time\s*:\s*(?P<real_time>\d+)\w+')

        # New LSP Arrivals:    0
        r8 = re.compile(r'New\s+LSP\s+Arrivals\s*:\s*(?P<new_lsp_arrival>\d+)')

        # Next Wait Interval: 200ms
        r9 = re.compile(r'Next\s+Wait\s+Interval\s*:\s*(?P<next_wait_interval>\d+)\w+')

        # Nodes:                   1       0     1
        r10 = re.compile(r'Nodes\s*:\s*(?P<reach>\d+)\s+(?P<unreach>\d+)\s+(?P<total>\d+)')

        # Prefixes (Items)
        # Prefixes (Routes)
        r11 = re.compile(r'Prefixes\s*\((?P<prefixes>\w+)\)')

        # Critical Priority:     0       0     0
        # Critical Priority:     0       -     0
        # High Priority:         0       0     0
        # High Priority:         0       -     0
        # Medium Priority        0       0     0
        # Medium Priority        0        -    0
        # Low Priority           0       0     0
        # Low Priority:          0        -    0
        # All Priorities         0        -    0
        # All Priorities         0       0     0
        r12 = re.compile(r'(?P<priority_level>\w+)\s+Priorit(y|ies)\s*:*\s+'
                          '(?P<reach>\d+)\s+(?P<unreach>\d+|\-)\s+'
                          '(?P<total>\d+)')

        # SR uloop:              No
        r13 = re.compile(r'^SR +uloop: +(?P<sr_uloop>\w+)$')

        # Interrupted:           No
        r14 = re.compile(r'^Interrupted: +(?P<interrupted>\w+)$')

        # RIB Batches:           0
        r15 = re.compile(r'^RIB +Batches: +(?P<total>\d+)( +\((?P<critical>\d+) '
                r'critical, +(?P<high>\d+) +high, +(?P<medium>\d+) +medium, +'
                r'(?P<low>\d+) +low\))?$')

        # 899545ms (since end of last calculation)
        r16 = re.compile(r'^(?P<since_end_of_last_calculation_ms>\d+)ms +\(since '
                r'+end +of +last +calculation\)$')
        
        # Trigger Prefix:        10.234.81.14/32 (optional field)
        r17 = re.compile(r'^Trigger +Prefix: +(?P<trigger_prefix>\S+) +\(optional +field\)$')

        # Mon Aug 16 2004
        rd = re.compile(r'(?P<timestamp_date>[\w\d\s]+)')

        parsed_dict = {}
        log_index = 1

        for line in output.splitlines():
            line = line.strip()

            # ISIS isp Level 1 IPv4 Unicast Route Calculation Log
            result = r1.match(line)
            if result:
                group = result.groupdict()
                instance = group['instance']
                level = int(group['level'])
                address_family = group['address_family']
                instance_dict = parsed_dict\
                    .setdefault('instance', {})\
                    .setdefault(instance, {})\
                    .setdefault('address_family', {})\
                    .setdefault(address_family, {})

                continue

            #                    Time  Total Trig
            # Timestamp     Type (ms)  Nodes Count  First Trigger LSP   Triggers
            # 19:25:35.140  FSPF  1    1     1             12a5.00-00   NEWLSP0
            result = r2.match(line)
            if result:
                group = result.groupdict()
                timestamp = group['timestamp']
                type_ = group['type']
                time_ms = int(group['time_ms'])
                nodes = int(group['nodes'])
                trigger_count = int(group['count'])
                first_trigger_lsp = group['first_trigger_lsp']
                triggers = group['triggers']
                spf_log_dict = instance_dict\
                    .setdefault('spf_log', {})\
                    .setdefault(log_index, {})
                spf_log_dict['type'] = type_
                spf_log_dict['time_ms'] = time_ms
                spf_log_dict['level'] = level
                spf_log_dict['total_nodes'] = nodes
                spf_log_dict['trigger_count'] = trigger_count
                if first_trigger_lsp:
                    spf_log_dict['first_trigger_lsp'] = first_trigger_lsp
                spf_log_dict['triggers'] = triggers
                spf_log_dict['start_timestamp'] = "{} {}"\
                    .format(timestamp_date, timestamp).strip()
                log_index += 1
                continue

            # Delay:              51ms (since first trigger)
            result = r3.match(line)
            if result:
                group = result.groupdict()
                delay = int(group['delay'])
                delay_dict = spf_log_dict.setdefault('delay', {})
                delay_dict['since_first_trigger_ms'] = delay
                continue

            # SPT Calculation
            result = r4.match(line)
            if result:
                spt_prefix_dict = spf_log_dict\
                    .setdefault('spt_calculation', {})

                continue

            # SPT Calculation:         5     5
            result = r4_1.match(line)
            if result:
                group = result.groupdict()
                spt_prefix_dict = spf_log_dict\
                    .setdefault('spt_calculation', {})
                cpu_time = int(group['cpu_time'])
                spt_prefix_dict['cpu_time_ms'] = cpu_time
                real_time = int(group['real_time'])
                spt_prefix_dict['real_time_ms'] = real_time
                continue

            # Prefix Updates
            result = r5.match(line)
            if result:
                spt_prefix_dict = spf_log_dict\
                    .setdefault('prefix_update', {})

                continue

            # Route Update:            0     0
            result = r5_1.match(line)
            if result:
                group = result.groupdict()
                spt_prefix_dict = spf_log_dict\
                    .setdefault('prefix_update', {})
                cpu_time = int(group['cpu_time'])
                spt_prefix_dict['cpu_time_ms'] = cpu_time
                real_time = int(group['real_time'])
                spt_prefix_dict['real_time_ms'] = real_time
                continue

            # Full Calculation:        0     0
            result = r5_2.match(line)
            if result:
                group = result.groupdict()
                spt_prefix_dict = spf_log_dict\
                    .setdefault('full_calculation', {})
                cpu_time = int(group['cpu_time'])
                spt_prefix_dict['cpu_time_ms'] = cpu_time
                real_time = int(group['real_time'])
                spt_prefix_dict['real_time_ms'] = real_time
                continue

            # CPU Time:         1ms
            # CPU Time:         0ms
            result = r6.match(line)
            if result:
                group = result.groupdict()
                cpu_time = int(group['cpu_time'])
                spt_prefix_dict['cpu_time_ms'] = cpu_time
                continue

            # Real Time:        0ms
            result = r7.match(line)
            if result:
                group = result.groupdict()
                real_time = int(group['real_time'])
                spt_prefix_dict['real_time_ms'] = real_time
                continue

            # New LSP Arrivals:    0
            result = r8.match(line)
            if result:
                group = result.groupdict()
                new_lsp_arrival = int(group['new_lsp_arrival'])
                spf_log_dict['new_lsp_arrivals'] = new_lsp_arrival
                continue

            # Next Wait Interval: 200ms
            result = r9.match(line)
            if result:
                group = result.groupdict()
                next_wait_interval = int(group['next_wait_interval'])
                spf_log_dict['next_wait_interval_ms'] = next_wait_interval
                continue

            # Results
            if line == "Results":
                results_dict = spf_log_dict.setdefault('results', {})

                continue

            #                      Reach Unreach Total
            # Nodes:                   1       0     1
            result = r10.match(line)
            if result:
                group = result.groupdict()
                reach = group['reach']
                unreach = group['unreach']
                total = group['total']
                node_dict = results_dict.setdefault('nodes', {})
                if reach.isdigit():
                    node_dict['reach'] = int(reach)
                if unreach.isdigit():
                    node_dict['unreach'] = int(unreach)
                if total.isdigit():
                    node_dict['total'] = int(total)
                continue

            # Prefixes (Items)
            # Prefixes (Routes)
            result = r11.match(line)
            if result:
                group = result.groupdict()
                prefixes = group['prefixes'].lower()
                prefixes_priority_dict = results_dict\
                    .setdefault('prefixes', {})\
                    .setdefault(prefixes, {})

                continue

            # Critical Priority:     0       0     0
            # Critical Priority:     0       -     0
            # High Priority:         0       0     0
            # High Priority:         0       -     0
            # Medium Priority        0       0     0
            # Medium Priority        0       -     0
            # Low Priority           0       0     0
            # Low Priority:          0       -     0
            # All Priorities         0       -     0
            # All Priorities         0       0     0
            result = r12.match(line)
            if result:
                group = result.groupdict()
                priority_level = group['priority_level'].lower()
                reach = group['reach']
                unreach = group['unreach']
                total = group['total']

                priority_dict = prefixes_priority_dict\
                    .setdefault('{priority_level}_priority'\
                        .format(priority_level=priority_level), {})

                if reach.isdigit():
                    priority_dict['reach'] = int(reach)
                if unreach.isdigit():
                    priority_dict['unreach'] = int(unreach)
                if total.isdigit():
                    priority_dict['total'] = int(total)

                continue

            # SR uloop:              No
            result = r13.match(line)
            if result:
                group = result.groupdict()
                sr_uloop = group['sr_uloop']
                spf_log_dict['sr_uloop'] = sr_uloop
                continue

            # Interrupted:           No
            result = r14.match(line)
            if result:
                group = result.groupdict()
                interrupted = group['interrupted']
                spf_log_dict['interrupted'] = interrupted
                continue

            # RIB Batches:           0
            result = r15.match(line)
            if result:
                group = result.groupdict()
                rib_batches_dict = spf_log_dict.setdefault('rib_batches', {})
                rib_batches_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # 899545ms (since end of last calculation)
            result = r16.match(line)
            if result:
                group = result.groupdict()
                delay = int(group['since_end_of_last_calculation_ms'])
                delay_dict = spf_log_dict.setdefault('delay', {})
                delay_dict['since_end_of_last_calculation'] = delay
                continue
            
            # Trigger Prefix:        10.234.81.14/32 (optional field)
            result = r17.match(line)
            if result:
                group = result.groupdict()
                spf_log_dict.update({'trigger_prefix': group['trigger_prefix']})
                continue

            # Mon Aug 16 2004
            result = rd.match(line)
            if result:
                group = result.groupdict()
                timestamp_date = group['timestamp_date']

                continue
        return parsed_dict


class ShowIsisLspLogSchema(MetaParser):
    ''' Schema for commands:
        * show isis lsp-log
    '''

    schema = {
        'instance': {
            Any(): {
                'lsp_log': {
                    Any(): {
                        'level': int,
                        'received_timestamp': str,
                        'count': int,
                        Optional('interface'): str,
                        Optional('triggers'): str,
                    }
                }
            }
        }
    }


class ShowIsisLspLog(ShowIsisLspLogSchema):
    ''' Parser for commands:
        * show isis lsp-log
    '''

    cli_command = 'show isis lsp-log'

    def cli(self, output=None):

        if not output:
            output = self.device.execute(self.cli_command)

        # IS-IS TEST Level 2 LSP log
        # ISIS isp Level 1 LSP log
        # Level 1 LSP log
        r1 = re.compile(r'(IS\-*IS\s+(?P<instance>.+)\s+)?Level\s+'
                         '(?P<level>\d+)\s+LSP\s+log')

        # --- Thu Sep 26 2019 ---
        # --- Mon Sep 30 2019 ---
        r2 = re.compile(r'\-\-\-\s+(?P<log_date>[\w\s]+)\s+\-\-\-')

        # 09:39:16.648     1                   IPEXT
        # 07:05:24         2                   CONFIG NEWADJ
        # 16:15:03.822     2  BE2              DELADJ
        # 00:02:36         1
        r3 = re.compile(r'(?P<timestamp>[0-9\:\.]+)\s+(?P<count>\d+)\s*'
                         '(?P<interface>[A-Z]+[a-z]*[\/*\d\.]+)?\s*'
                         '(?P<triggers>[\w*\s]*)')

        parsed_output = {}
        log_date = ''
        log_index = 1

        for line in output.splitlines():
            line = line.strip()

            # IS-IS TEST Level 2 LSP log
            # ISIS isp Level 1 LSP log
            # Level 1 LSP log
            result = r1.match(line)
            if result:
                group = result.groupdict()
                instance = group['instance']
                if instance is None:
                    instance = ""
                level = int(group['level'])
                instance_dict = parsed_output\
                    .setdefault('instance', {})\
                    .setdefault(instance, {})

                continue

            # --- Thu Sep 26 2019 ---
            # --- Mon Sep 30 2019 ---
            result = r2.match(line)
            if result:
                group = result.groupdict()
                log_date = group['log_date']

                continue

            # 09:39:16.648    1                   IPEXT
            # 07:05:24        2                   CONFIG NEWADJ
            # 16:15:03.822    2  BE2              DELADJ
            # 00:02:36        1
            result = r3.match(line)
            if result:
                group = result.groupdict()
                timestamp = group['timestamp']
                count = int(group['count'])
                interface = group['interface']
                triggers = group['triggers']
                lsp_log_dict = instance_dict\
                    .setdefault('lsp_log', {})\
                    .setdefault(log_index, {})
                lsp_log_dict['count'] = count
                lsp_log_dict['level'] = level
                if interface:
                    lsp_log_dict['interface'] = Common\
                        .convert_intf_name(interface)
                if triggers:
                    lsp_log_dict['triggers'] = triggers
                lsp_log_dict['received_timestamp'] = ('{} {}'\
                    .format(log_date, timestamp)).strip()
                log_index += 1

                continue

        return parsed_output


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
                        Optional('adjacency_formation'): str,
                        Optional('prefix_advertisement'): str,
                        Optional('ipv6_bfd'): bool,
                        Optional('ipv4_bfd'): bool,
                        Optional('bfd_min_interval'): int,
                        Optional('bfd_multiplier'): int,
                        Optional('bandwidth'): int,
                        Optional('circuit_type'): str,
                        Optional('media_type'): str,
                        Optional('circuit_number'): int,
                        Optional('rsi_srlg'): str,
                        Optional('next_p2p_iih_in'): int,
                        Optional('extended_circuit_number'): int,
                        Optional('lsp_rexmit_queue_size'): int,
                        Optional('lsp'): {
                            'transmit_timer_expires_ms': int,
                            'transmission_state': str,
                            'lsp_transmit_back_to_back_limit': int,
                            'lsp_transmit_back_to_back_limit_window_msec': int,
                        },
                        Optional('underlying_interface'):{
                            Any(): {
                                'index': str
                            }
                        },
                        Optional('level'): {
                            Any(): {
                                'adjacency_count':int,
                                Optional('lsp_pacing_interval_ms'): int,
                                'psnp_entry_queue_size': int,
                                Optional('next_lan_iih_sec'): int,
                                Optional('lan_id'): str,
                                Optional('hello_interval_sec'): int,
                                Optional('hello_multiplier'): int,
                                Optional('priority'): {
                                    'local': str,
                                    'dis': str
                                }
                            },
                        },
                        Optional('clns_io'): {
                            'protocol_state': str,
                            'mtu': int,
                            Optional('snpa'): str,
                            Optional('layer2_mcast_groups_membership'): {
                                Optional('all_level_1_iss'): str,
                                Optional('all_level_2_iss'): str,
                            },
                        },
                        Optional('topology'): {
                            Any(): {
                                'adjacency_formation': str,
                                'state': str,
                                'prefix_advertisement': str,
                                Optional('protocol_state'): str,
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
                                Optional('frr'): {
                                    'level': {
                                        Any(): {
                                            'state': str,
                                            'type': str,
                                            Optional(Any()): {
                                                Optional('state'): str,
                                                Optional('tie_breaker'): str,
                                                Optional('line_card_disjoint'): str,
                                                Optional('lowest_backup_metric'): str,
                                                Optional('node_protecting'): str,
                                                Optional('primary_path'): str,
                                                Optional('link_protecting'): str,
                                                Optional('srlg_disjoint'): str,
                                            }
                                        },
                                    },
                                },
                            },
                        },
                        Optional('address_family'): {
                            Any(): {
                                'state': str,
                                'forwarding_address': list,
                                'global_prefix': list,
                                Optional('protocol_state'): str,
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
        # TenGigE0/0/0/0/0            Disabled (No topologies cfg on the intf)
        r2 = re.compile(r'^(?P<interface>[\w\-\d+\/\.]+)\s+(?P<interface_state>Enabled|Disabled)( +[\S ]+)?$')

        # Adjacency Formation:    Running
        # Adjacency Formation:      Enabled
        r3 = re.compile(r'Adjacency\s+Formation\s*:\s*'
                        r'(?P<adjacency_formation_state>\w+)')

        # Prefix Advertisement:     Enabled
        # Prefix Advertisement:   Running
        r4 = re.compile(r'Prefix\s+Advertisement\s*:\s*'
                        r'(?P<prefix_advertisement_state>.+)')

        # IPv4 BFD:                 Disabled
        # IPv6 BFD:                 Disabled
        r5 = re.compile(r'(?P<address_family>IPv4|IPv6)\s+BFD\s*:\s*'
                        r'(?P<ip_bfd_state>\w+)')

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
                         r'(?P<lsp_pacing_interval>\d+)\s+ms')

        # PSNP Entry Queue Size:  0
        r15 = re.compile(r'PSNP\s+Entry\s+Queue\s+Size\s*:\s*'
                         r'(?P<psnp_entry_queue_size>\d+)')

        # Hello Interval:         10 s
        r16 = re.compile(r'Hello\s+Interval\s*:\s*(?P<hello_interval>\d+)\s*s')

        # Hello Multiplier:       3
        r17 = re.compile(r'Hello\s+Multiplier\a*:\s*(?P<hello_multiplier>\d+)')

        # CLNS I/O
        r18 = re.compile(r'CLNS\s+I\/O')

        # Protocol State:         Up
        # Protocol State:         Down (Intf not up in CLNS proto stack)
        r19 = re.compile(r'Protocol\s+State\s*:\s*(?P<protocol_state>[\S\s]+)')

        # MTU:                    1500
        r20 = re.compile(r'MTU\s*:\s*(?P<mtu>\S+)')

        # IPv4 Unicast Topology:    Enabled
        # IPv6 Unicast Topology:    Enabled
        r21 = re.compile(r'(?P<topology>(IPv4|IPv6)[\s\w]+)\s+Topology\s*:'
                         r'\s*(?P<topology_state>\w+)')

        # Metric (L1/L2):         10/10
        r22 = re.compile(r'Metric\s+\(L(?P<level_1>\d+)/L(?P<level_2>\d+)\)\s*'
                         r':\s*(?P<metric_level_1>\d+)\/(?P<metric_level_2>\d+)')

        # Weight (L1/L2):         0/0
        r23 = re.compile(r'Weight\s+\(L(?P<level_1>\d+)/L(?P<level_2>\d+)\)\s*:'
                         r'\s*(?P<weight_level_1>\d+)\/(?P<weight_level_2>\d+)')

        # MPLS Max Label Stack:   1/3/10 (PRI/BKP/SRTE)
        # MPLS Max Label Stack(PRI/BKP/SRTE):2/2/10
        r24 = re.compile(r'MPLS\s+Max\s+Label\s+Stack(?P<mpls_max_label_stack>.+)')

        # MPLS LDP Sync (L1/L2):  Disabled/Disabled
        r25 = re.compile(r'MPLS\s+LDP\s+Sync\s+\(L(?P<level_1>\d+)/L'
                         r'(?P<level_2>\d+)\)\s*:\s*(?P<state_level_1>\w+)\/(?P<state_level_2>\w+)')

        # FRR (L1/L2):            L1 Not Enabled     L2 Not Enabled
        r26 = re.compile(r'FRR\s+\(L\d+\/L\d+\)\s*:\s*L(?P<level_1>\d+)\s+'
                         r'(?P<level_1_state>[\w\s]+)\s+L(?P<level_2>\d+)\s+(?P<level_2_state>[\w\s]+)')

        # FRR Type:             None               None
        r27 = re.compile(r'FRR\s+Type\s*:\s*(?P<frr_type_level_1>\S+)\s*'
                         r'(?P<frr_type_level_2>\S+)')

        # IPv4 Address Family:      Enabled
        # IPv6 Address Family:      Enabled
        r28 = re.compile(r'(?P<address_family>IPv4|IPv6)\s+Address\s+Family\s*:'
                         r'\s*(?P<address_family_state>\w+)')

        # Forwarding Address(es): 0.0.0.0
        # Forwarding Address(es): ::
        r29 = re.compile(r'Forwarding\s+Address\(es\)\s*:\s*'
                         r'(?P<forwarding_address>\S+)')

        # Global Prefix(es):      10.36.3.0/24
        # Global Prefix(es):      2001:db8:3:3:3::3/128
        # Global Prefix(es):      None (No global addresses are configured)
        r30 = re.compile(r'Global\s+Prefix\(es\)\s*:\s*(?P<global_prefix>.+)')

        # LSP transmit timer expires in 0 ms
        r31 = re.compile(r'LSP\s+transmit\s+timer\s+expires\s+in\s+'
                         r'(?P<lsp_timer>\d+)\s+ms')

        # LSP transmission is idle
        r32 = re.compile(r'LSP\s+transmission\s+is\s+'
                         r'(?P<lsp_transmission_state>\w+)')

        # Can send up to 10 back-to-back LSPs in the next 0 ms
        r33 = re.compile(r'Can\s+send\s+up\s+to\s+(?P<number_lsp_send>\d+)'
                         r'\s+back\-to\-back\s+LSPs\s+in\s+the\s+next\s+'
                         r'(?P<time_to_sent>\d+)\s+ms')

        # LAN ID:                 R3.07
        r34 = re.compile(r'LAN\s+ID\s*:\s*(?P<lan_id>\S+)')

        # Priority (Local/DIS):   64/none (no DIS elected)
        # Priority (Local/DIS):   64/64
        r35 = re.compile(r'Priority\s*\(Local/DIS\)\s*:\s*'
                         r'(?P<priority_local>\S+)/(?P<priority_dis>.+)')

        # Next LAN IIH in:        5 s
        # Next LAN IIH in:        3 s
        r36 = re.compile(r'Next\s+LAN\s+IIH\s+in\s*:\s*'
                         r'(?P<next_lan_iih>\d+)\s*s')

        # SNPA:                   fa16.3eff.86bf
        r37 = re.compile(r'SNPA\s*:\s*(?P<snpa>\S+)')

        # Layer-2 MCast Groups Membership:
        r38 = re.compile(r'Layer\-(?P<layer>\d+)\s*MCast\s+Groups\s+Membership:')

        # All Level-1 ISs:      Yes
        # All Level-2 ISs:      Yes
        r39 = re.compile(r'All\s+Level\-(?P<level>\d+)\s+ISs\s*:\s*'
                         r'(?P<iss_state>\S+)')

        # All ISs:              Yes
        r40 = re.compile(r'All\s+ISs\s*:\s*(?P<all_iss>(Yes|No))')

        # Extended Circuit Number:  20
        r41 = re.compile(r'^Extended +Circuit +Number: +(?P<extended_circuit_number>\d+)$')

        # Next P2P IIH in:          3 s
        r42 = re.compile(r'^Next +P2P +IIH +in: +(?P<next_p2p_iih_in>\d+) +m?s$')

        # LSP Rexmit Queue Size:    0
        r43 = re.compile(r'^LSP +Rexmit +Queue +Size: +(?P<lsp_rexmit_queue_size>\d+)$')

        # RSI SRLG:                 Registered
        r44 = re.compile(r'^RSI +SRLG: +(?P<rsi_srlg>\S+)$')

        # Direct LFA:           Enabled            Enabled
        r45 = re.compile(r'^Direct +LFA: +(?P<level_1>\w+) +(?P<level_2>\w+)$')

        # Remote LFA:           Not Enabled        Not Enabled
        r46 = re.compile(r'^Remote +LFA: +(?P<level_1>(Not +)?Enabled) +(?P<level_2>(Not +)?Enabled)$')

        # Tie Breaker          Default            Default
        r47 = re.compile(r'^Tie +Breaker +(?P<level_1>\w+) +(?P<level_2>\w+)$')

        # Line-card disjoint   30                 30
        r48 = re.compile(r'^Line-card +disjoint +(?P<level_1>\w+) +(?P<level_2>\w+)$')

        # Lowest backup metric 20                 20
        r49 = re.compile(r'^Lowest +backup +metric +(?P<level_1>\w+) +(?P<level_2>\w+)$')

        # Node protecting      40                 40
        r50 = re.compile(r'^Node +protecting +(?P<level_1>\w+) +(?P<level_2>\w+)$')

        # Primary path         10                 10
        r51 = re.compile(r'^Primary +path +(?P<level_1>\w+) +(?P<level_2>\w+)$')

        # TI LFA:               Enabled            Enabled
        r52 = re.compile(r'^TI +LFA: +(?P<level_1>\w+) +(?P<level_2>\w+)$')

        # Link Protecting      Enabled            Enabled
        r53 = re.compile(r'^Link +Protecting +(?P<level_1>\w+) +(?P<level_2>\w+)$')

        # SRLG disjoint        0                  0
        r54 = re.compile(r'^SRLG +disjoint +(?P<level_1>\w+) +(?P<level_2>\w+)$')

        # IfName: Hu0/0/0/1 IfIndex: 0x55
        r55 = re.compile(r'^IfName: +(?P<if_name>\S+) +IfIndex: +(?P<if_index>\S+)$')

        parsed_output = {}
        interface_flag = False
        clns_flag = False
        topology_flag = False
        instance = None

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

                if not instance:
                    instance_dict = parsed_output\
                    .setdefault('instance', {})\
                    .setdefault('default', {})

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
                elif topology_flag:
                    topology_dict['protocol_state'] = protocol_state
                else:
                    address_family_dict['protocol_state'] = protocol_state
                continue

            # MTU:                    1500
            result = r20.match(line)
            if result:
                group = result.groupdict()
                if group['mtu'].isnumeric() is True:
                    mtu = int(group['mtu'])
                else:
                    mtu = int(-1)
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
                clns_flag = False
                topology_flag = True
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
            # MPLS Max Label Stack(PRI/BKP/SRTE):2/2/10
            result = r24.match(line)
            if result:
                group = result.groupdict()
                mpls_stack = group['mpls_max_label_stack'].replace(':', ' ').strip()
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
                lfa_type = 'frr'
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
                topology_flag = False
                continue

            # Forwarding Address(es): 0.0.0.0
            # Forwarding Address(es): ::
            result = r29.match(line)
            if result:
                group = result.groupdict()
                forwarding_address = group['forwarding_address']
                forwarding_address_list = address_family_dict\
                    .get('forwarding_address', [])
                forwarding_address_list.append(forwarding_address)
                address_family_dict['forwarding_address'] = forwarding_address_list
                continue

            # Global Prefix(es):      10.36.3.0/24
            # Global Prefix(es):      2001:db8:3:3:3::3/128
            result = r30.match(line)
            if result:
                group = result.groupdict()
                global_prefix = group['global_prefix']
                global_prefix_list = address_family_dict\
                    .get('global_prefix', [])
                global_prefix_list.append(global_prefix)
                address_family_dict['global_prefix'] = global_prefix_list
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

            # SNPA:                   fa16.3eff.86bf
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
            # Extended Circuit Number:  20
            result = r41.match(line)
            if result:
                group = result.groupdict()
                extended_circuit_number = int(group['extended_circuit_number'])
                if interface_flag:
                    interface_dict['extended_circuit_number'] = extended_circuit_number
                else:
                    topology_dict['extended_circuit_number'] = extended_circuit_number
                continue

            # Next P2P IIH in:          3 s
            result = r42.match(line)
            if result:
                group = result.groupdict()
                next_p2p_iih_in = int(group['next_p2p_iih_in'])
                if interface_flag:
                    interface_dict['next_p2p_iih_in'] = next_p2p_iih_in
                else:
                    topology_dict['next_p2p_iih_in'] = next_p2p_iih_in
                continue

            # LSP Rexmit Queue Size:    0
            result = r43.match(line)
            if result:
                group = result.groupdict()
                lsp_rexmit_queue_size = int(group['lsp_rexmit_queue_size'])
                if interface_flag:
                    interface_dict['lsp_rexmit_queue_size'] = lsp_rexmit_queue_size
                else:
                    topology_dict['lsp_rexmit_queue_size'] = lsp_rexmit_queue_size
                continue

            # RSI SRLG:                 Registered
            result = r44.match(line)
            if result:
                group = result.groupdict()
                rsi_srlg = group['rsi_srlg']
                if interface_flag:
                    interface_dict['rsi_srlg'] = rsi_srlg
                else:
                    topology_dict['rsi_srlg'] = rsi_srlg
                continue

            # Direct LFA:           Enabled            Enabled
            result = r45.match(line)
            if result:
                lfa_type = 'direct_lfa'
                group = result.groupdict()
                direct_lfa_level_1 = group['level_1']
                direct_lfa_level_2 = group['level_2']
                direct_lfa_dict_1 = frr_dict.setdefault(level_1, {}). \
                    setdefault('direct_lfa', {})
                direct_lfa_dict_1.update({'state': direct_lfa_level_1})
                direct_lfa_dict_2 = frr_dict.setdefault(level_2, {}). \
                    setdefault('direct_lfa', {})
                direct_lfa_dict_2.update({'state': direct_lfa_level_2})
                continue
            # Remote LFA:           Not Enabled        Not Enabled
            result = r46.match(line)
            if result:
                lfa_type = 'remote_lfa'
                group = result.groupdict()
                remote_lfa_level_1 = group['level_1']
                remote_lfa_level_2 = group['level_2']
                remote_lfa_dict_1 = frr_dict.setdefault(level_1, {}). \
                    setdefault('remote_lfa', {})
                remote_lfa_dict_1.update({'state': remote_lfa_level_1})
                remote_lfa_dict_2 = frr_dict.setdefault(level_2, {}). \
                    setdefault('remote_lfa', {})
                remote_lfa_dict_2.update({'state': remote_lfa_level_2})
                continue

            # Tie Breaker          Default            Default
            result = r47.match(line)
            if result:
                group = result.groupdict()
                tie_breaker_level_1 = group['level_1']
                tie_breaker_level_2 = group['level_2']
                if lfa_type == 'direct_lfa':
                    current_lfa_dict_1 = direct_lfa_dict_2
                    current_lfa_dict_2 = direct_lfa_dict_2
                elif lfa_type == 'remote_lfa':
                    current_lfa_dict_1 = remote_lfa_dict_1
                    current_lfa_dict_2 = remote_lfa_dict_2
                else:
                    current_lfa_dict_1 = ti_lfa_dict_1
                    current_lfa_dict_2 = ti_lfa_dict_2

                current_lfa_dict_1.update({'tie_breaker': tie_breaker_level_1})
                current_lfa_dict_2.update({'tie_breaker': tie_breaker_level_2})
                continue

            # Line-card disjoint   30                 30
            result = r48.match(line)
            if result:
                group = result.groupdict()
                line_card_disjoint_level_1 = group['level_1']
                line_card_disjoint_level_2 = group['level_2']
                if lfa_type == 'direct_lfa':
                    current_lfa_dict_1 = direct_lfa_dict_2
                    current_lfa_dict_2 = direct_lfa_dict_2
                elif lfa_type == 'remote_lfa':
                    current_lfa_dict_1 = remote_lfa_dict_1
                    current_lfa_dict_2 = remote_lfa_dict_2
                else:
                    current_lfa_dict_1 = ti_lfa_dict_1
                    current_lfa_dict_2 = ti_lfa_dict_2

                current_lfa_dict_1.update({'line_card_disjoint': line_card_disjoint_level_1})
                current_lfa_dict_2.update({'line_card_disjoint': line_card_disjoint_level_2})
                continue

            # Lowest backup metric 20                 20
            result = r49.match(line)
            if result:
                group = result.groupdict()
                lowest_backup_metric_level_1 = group['level_1']
                lowest_backup_metric_level_2 = group['level_2']
                if lfa_type == 'direct_lfa':
                    current_lfa_dict_1 = direct_lfa_dict_2
                    current_lfa_dict_2 = direct_lfa_dict_2
                elif lfa_type == 'remote_lfa':
                    current_lfa_dict_1 = remote_lfa_dict_1
                    current_lfa_dict_2 = remote_lfa_dict_2
                else:
                    current_lfa_dict_1 = ti_lfa_dict_1
                    current_lfa_dict_2 = ti_lfa_dict_2

                current_lfa_dict_1.update({'lowest_backup_metric': lowest_backup_metric_level_1})
                current_lfa_dict_2.update({'lowest_backup_metric': lowest_backup_metric_level_2})
                continue

            # Node protecting      40                 40
            result = r50.match(line)
            if result:
                group = result.groupdict()
                node_protecting_level_1 = group['level_1']
                node_protecting_level_2 = group['level_2']
                if lfa_type == 'direct_lfa':
                    current_lfa_dict_1 = direct_lfa_dict_2
                    current_lfa_dict_2 = direct_lfa_dict_2
                elif lfa_type == 'remote_lfa':
                    current_lfa_dict_1 = remote_lfa_dict_1
                    current_lfa_dict_2 = remote_lfa_dict_2
                else:
                    current_lfa_dict_1 = ti_lfa_dict_1
                    current_lfa_dict_2 = ti_lfa_dict_2

                current_lfa_dict_1.update({'node_protecting': node_protecting_level_1})
                current_lfa_dict_2.update({'node_protecting': node_protecting_level_2})
                continue

            # Primary path         10                 10
            result = r51.match(line)
            if result:
                group = result.groupdict()
                primary_path_level_1 = group['level_1']
                primary_path_level_2 = group['level_2']
                if lfa_type == 'direct_lfa':
                    current_lfa_dict_1 = direct_lfa_dict_2
                    current_lfa_dict_2 = direct_lfa_dict_2
                elif lfa_type == 'remote_lfa':
                    current_lfa_dict_1 = remote_lfa_dict_1
                    current_lfa_dict_2 = remote_lfa_dict_2
                else:
                    current_lfa_dict_1 = ti_lfa_dict_1
                    current_lfa_dict_2 = ti_lfa_dict_2

                current_lfa_dict_1.update({'primary_path': primary_path_level_1})
                current_lfa_dict_2.update({'primary_path': primary_path_level_2})
                continue

            # TI LFA:               Enabled            Enabled
            result = r52.match(line)
            if result:
                lfa_type = 'ti_lfa'
                group = result.groupdict()
                ti_lfa_level_1 = group['level_1']
                ti_lfa_level_2 = group['level_2']
                ti_lfa_dict_1 = frr_dict.setdefault(level_1, {}). \
                    setdefault('ti_lfa', {})
                ti_lfa_dict_1.update({'state': ti_lfa_level_1})
                ti_lfa_dict_2 = frr_dict.setdefault(level_2, {}). \
                    setdefault('ti_lfa', {})
                ti_lfa_dict_2.update({'state': ti_lfa_level_2})
                continue

            # Link Protecting      Enabled            Enabled
            result = r53.match(line)
            if result:
                group = result.groupdict()
                link_protecting_level_1 = group['level_1']
                link_protecting_level_2 = group['level_2']
                if lfa_type == 'direct_lfa':
                    current_lfa_dict_1 = direct_lfa_dict_2
                    current_lfa_dict_2 = direct_lfa_dict_2
                elif lfa_type == 'remote_lfa':
                    current_lfa_dict_1 = remote_lfa_dict_1
                    current_lfa_dict_2 = remote_lfa_dict_2
                else:
                    current_lfa_dict_1 = ti_lfa_dict_1
                    current_lfa_dict_2 = ti_lfa_dict_2

                current_lfa_dict_1.update({'link_protecting': link_protecting_level_1})
                current_lfa_dict_2.update({'link_protecting': link_protecting_level_1})
                continue

            # SRLG disjoint        0                  0
            result = r54.match(line)
            if result:
                group = result.groupdict()
                srlg_disjoint_level_1 = group['level_1']
                srlg_disjoint_level_2 = group['level_2']
                if lfa_type == 'direct_lfa':
                    current_lfa_dict_1 = direct_lfa_dict_2
                    current_lfa_dict_2 = direct_lfa_dict_2
                elif lfa_type == 'remote_lfa':
                    current_lfa_dict_1 = remote_lfa_dict_1
                    current_lfa_dict_2 = remote_lfa_dict_2
                else:
                    current_lfa_dict_1 = ti_lfa_dict_1
                    current_lfa_dict_2 = ti_lfa_dict_2

                current_lfa_dict_1.update({'srlg_disjoint': srlg_disjoint_level_1})
                current_lfa_dict_2.update({'srlg_disjoint': srlg_disjoint_level_2})
                continue

            # IfName: Hu0/0/0/1 IfIndex: 0x55
            result = r55.match(line)
            if result:
                group = result.groupdict()
                if_name = Common.convert_intf_name(group['if_name'])
                if_index = group['if_index']
                underlying_interface = interface_dict.setdefault('underlying_interface', {}). \
                    setdefault(if_name, {})
                underlying_interface.update({'index': if_index})

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
                                Optional('router_cap'): str,
                                Optional('area_address'): str,
                                Optional('nlpid'): list,
                                Optional('ip_address'): str,
                                Optional('ipv6_address'): str,
                                Optional('hostname'): str,
                                Optional('topology'): list,
                                Optional('tlv'): int,
                                Optional('tlv_length'): int,
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
        # 0000.0CFF.0C35.00-00  0x0000000C    0x5696        325                0/0/0
        # 0000.0CFF.40AF.00-00* 0x00000009    0x8452        608                1/0/0
        r2 = re.compile(r'^(?P<lspid>[\w\-\.]+)( *(?P<local_router>\*))? +'
                r'(?P<lsp_seq_num>\w+) +(?P<lsp_checksum>\w+) +(?P<lsp_holdtime>\d+|\*)'
                r'( *\/(?P<lsp_rcvd>\d+|\*))? +(?P<attach_bit>\d+)\/(?P<p_bit>\d+)\/'
                r'(?P<overload_bit>\d+)$')

        # Area Address:   49.0002
        r3 = re.compile(r'Area\s+Address\s*:\s*(?P<area_address>\S+)')

        # NLPID: 0xcc
        # NLPID: 0xCC 0x8E
        r4 = re.compile(r'NLPID\s*:\s*(?P<nlpid>[\w\s]+)')

        # IP Address:     10.36.3.3
        r5 = re.compile(r'IP\s*Address\s*:\s*(?P<ip_address>\S+)')

        # Metric: 10         IP-Extended 10.36.3.0/24
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

        # Router ID:      10.144.6.6
        # Router ID:      10.196.7.7
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

        # Metric: 10   IS 0000.0CFF.62E6.03
        r18 = re.compile(r'Metric\s*:\s*(?P<metric>\d+)\s+IS\s+'
                         r'(?P<is_neighbor>[\w\.\-]+)')

        # Metric: 0    ES 0000.0CFF.0C35
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

        # Metric: 0          IP 172.16.115.0/24
        r22 = re.compile(r'Metric\s*:\s*(?P<metric>\d+)\s+IP\s+'
                         r'(?P<ip_address>[\d\.\/]+)')

        # Router Cap:     172.19.1.2 D:0 S:0
        r23 = re.compile(r'^Router +Cap: +(?P<router_cap>[\S ]+)$')

        # TLV 14:         Length: 2
        r24 = re.compile(r'^TLV +(?P<tlv>\d+): +Length: +(?P<length>\d+)$')

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
                instance = instance if instance else ''
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

            # IP Address:     10.36.3.3
            result = r5.match(line)
            if result:
                group = result.groupdict()
                ip_address = group['ip_address']
                lspid_dict['ip_address'] = ip_address

                continue

            # Metric: 10         IP-Extended 10.36.3.0/24
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

            # Router ID:      10.144.6.6
            # Router ID:      10.196.7.7
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
                    .setdefault(ipv6_interarea, {})\
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

            # Metric: 10   IS 0000.0CFF.62E6.03
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

            # Metric: 0    ES 0000.0CFF.0C35
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

            # Metric: 0          IP 172.16.115.0/24
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

            # Router Cap:     172.19.1.2 D:0 S:0
            result = r23.match(line)
            if result:
                group = result.groupdict()
                router_cap = group['router_cap']
                lspid_dict['router_cap'] = router_cap
                continue

            # TLV 14:         Length: 2
            result = r24.match(line)
            if result:
                group = result.groupdict()
                tlv = int(group['tlv'])
                length = int(group['length'])
                lspid_dict['tlv'] = tlv
                lspid_dict['tlv_length'] = length
                continue

        return parsed_output


class ShowIsisPrivateAllSchema(MetaParser):
    ''' Schema for commands:
       * show isis private all
    '''
    schema = {
        'instance': {
            Any(): {
                'cfg_refcount': int,
                'isis_is_level': str,
                'ignore_cksum_errs': bool,
                'cfg_log_drops': bool,
                'nsf_cfg_purgetime': int,
                'nsf2_t1_delay': int,
                'nsf2_t1_max_num_exp': int,
                'nsf_cfg_interval': int,
                'address_family_table': {
                    Any():{
                        'ref_count': int,
                    },
                },
                'link_topology_table': {
                    Any(): {
                        'ref_count': int,
                        'index': int,
                        'is_running': bool,
                        'list_linkage': {
                            'next':str,
                            'previous': str,
                        },
                    },
                },
                'topology_table': {
                    Any(): {
                        'configuration': {
                            'check_adjacencies': str,
                            'attached_bit': str,
                            'max_paths': str,
                            'is_mcast_intact_set': bool,
                            'mcast_intact': bool,
                            'is_igp_intact_set': bool,
                            'igp_intact': bool,
                            'is_first_hop_source_set': bool,
                            'first_hop_source': bool,
                        },
                        'index': int,
                        'ref_count': int,
                        'ltopo_index': int,
                        'list_linkage': {
                            'next':str,
                            'previous': str,
                        },
                    },
                },
                'area_configuration_table': {
                    Any(): {
                        'is_lsp_gen_interval_set': bool,
                        'lsp_gen_interval': {
                            'initial_wait_msecs': int,
                            'secondary_wait_msecs': int,
                            'maximum_wait_msecs': int,
                        },
                        'is_lsp_arrivaltime_parameter_set': bool,
                        'lsp_arrivaltime_parameter': {
                            'backoff_cfg': {
                                'initial_wait_msecs': int,
                                'secondary_wait_msecs': int,
                                'maximum_wait_msecs': int,
                            },
                            'max_count': int,
                            'max_window_size_msec': int,
                        },
                        'is_lsp_checksum_interval_set': bool,
                        'lsp_checksum_interval_secs': int,
                        'is_lsp_refresh_interval_set': bool,
                        'lsp_refresh_interval_secs': int,
                        'is_lsp_lifetime_set': bool,
                        'lsp_lifetime_secs': int,
                        'is_lsp_mtu_set': bool,
                        'lsp_mtu': int,
                        'is_auth_cfg_ctx_set': bool,
                        'auth_cfg_ctx': {
                            'alg': str,
                            'failure_mode': str,
                            'password':  str,
                            'accept_password': str,
                        },
                        'is_snp_authentication_options_set': bool,
                        'snp_authentication_options': int,
                        'is_overload_set': bool,
                        'overload_mode': int,
                        'overload_on_startup_secs': int,
                        'per_topo': {
                            Any(): {
                                'is_metric_style_set': bool,
                                'generate_metric_mask': int,
                                'accept_metric_mask': int,
                                'summary_table': str,
                                'metric': Any(),
                                'is_spf_interval_set': bool,
                                'spf_interval': {
                                    'initial_wait_msecs': int,
                                    'secondary_wait_msecs': int,
                                    'maximum_wait_msecs': int,
                                },
                                'spf_periodic_interval_secs': str,
                                'ispf_state': str,
                                'max_redist_prefixes': str,
                                'topo_index': {
                                    Any(): {
                                        'is_spf_prefix_priority_acl_names_set': bool,
                                        'spf_prefix_priority_acl_names': str,
                                        'is_spf_prefix_priority_tags_set': bool,
                                        'spf_prefix_priority_tags': int,
                                    },
                                },
                            },
                        },
                    },
                },
                'area_tables': {
                    Any(): {
                        'index': int,
                        'nsf_ietf_csnp_rcvd': bool,
                        'overload_bit_on_startup_timer': str,
                        'overload_bit_trigger_expired': bool,
                        Optional('overload_bit_forced_reasons'): str,
                        'upd_periodic_timer': str,
                        'checksum_ptimer': {
                            'tv_sec': int,
                            'tv_nsec': int,
                        },
                        'idb_list': {
                            'sll_head': str,
                            'sll_tail': str,
                            'sll_count': int,
                            'sll_maximum': int,
                        },
                        'list_linkage': {
                            'next': str,
                            'previous': str,
                        },
                        'adj_db': str,
                        'adj_log': str,
                        'uni_db_log': str,
                        'upd_db': {
                            'area': str,
                            'log': str,
                            'name': str,
                            'lock': {
                                'description': str,
                                'rwlock': {
                                    'active': int,
                                    'spare': str,
                                    'blockedwriters': int,
                                    'blockedreaders': int,
                                    'heavy': int,
                                    'owner': int,
                                    Optional('lock'): {
                                        'count': int,
                                        'owner': int,
                                    },
                                },
                            },
                            'tree': {
                                'root': str,
                                'key_size': int,
                                'size': int,
                                'node_alloc_data': str,
                                'node_alloc_fn': str,
                                'node_free_fn': str,
                                'data_to_str_fn': str,
                            },
                            'tree_node_chunks': {
                                'name': str,
                                'size': int,
                                'flags': int,
                                'chunk': str,
                                'num_allocated_elements': int
                            },
                        },
                        'dec_db': {
                            'area': str,
                            'log': str,
                            'name': str,
                            'lock': {
                                'description': str,
                                'rwlock': {
                                    'active': int,
                                    'spare': str,
                                    'blockedwriters': int,
                                    'blockedreaders': int,
                                    'heavy': int,
                                    'lock': {
                                        'count': int,
                                        'owner': int,
                                    },
                                    'owner': int,
                                }
                            },
                            'tree': {
                                'root': str,
                                'key_size':  int,
                                'size': int,
                                'node_alloc_data': str,
                                'node_alloc_fn': str,
                                'node_free_fn': str,
                                'data_to_str_fn': str,
                            },
                            'tree_node_chunks': {
                                'name': str,
                                'size': int,
                                'flags': int,
                                'chunk': str,
                                'num_allocated_elements': int,
                            },
                        },
                        'node_db': {
                            'node_created_fn': str,
                            'node_destroyed_fn': str,
                            'node_ltopo_created_fn': str,
                            'node_ltopo_destroyed_fn': str,
                            'node_topo_created_fn': str,
                            'node_topo_destroyed_fn': str,
                            'callback_context': str,
                            'root_element': str,
                            'num_nodes': int,
                        },
                        'stats': {
                            'ta_lsp_build': int,
                            'ta_lsp_refresh': int,
                        },
                        'trap_stats': {
                            'corr_lsps': int,
                            'auth_type_fails': int,
                            'auth_fails': int,
                            'lsp_dbase_oloads': int,
                            'man_addr_drop_from_areas': int,
                            'attmpt_to_ex_max_seq_nums': int,
                            'seq_num_skips': int,
                            'own_lsp_purges': int,
                            'id_field_len_mismatches': int,
                            'lsp_errors': int,
                        },
                        'per_ltopo': {
                            Any(): {
                                'area': str,
                                'ltopo_index': str,
                                'spf_periodic_timer': str,
                                'reachable_area_addresses': str,
                                'stats': {
                                    'num_spfs': int,
                                    'num_ispfs': int,
                                    'num_nhcs': int,
                                    'num_prcs': int,
                                    'num_periodic_spfs': int,
                                },
                                'paths':{
                                    'classification': int,
                                    'is_sorted': bool,
                                    'array': str,
                                    'num_elements': int,
                                },
                                'unreached': {
                                    'classification': int,
                                    'is_sorted': bool,
                                    'array': str,
                                    'num_elements': int,
                                },
                                'firsthopchanged': {
                                    'classification': int,
                                    'is_sorted': bool,
                                    'array': str,
                                    'num_elements': int,
                                },
                                'linkchanged': {
                                    'classification': int,
                                    'is_sorted': bool,
                                    'array': str,
                                    'num_elements': int,
                                },
                                'roca_event': {
                                    'log': str,
                                    'class': str,
                                    'mutex': {
                                        'mutex': {
                                            'count': int,
                                            'owner': int,
                                        },
                                        'description': str,
                                    },
                                    'timer': {
                                        'timer': str,
                                        'num_execution_events': int,
                                        'is_pending': bool,
                                        'is_executing': bool,
                                        'postponed_schedule_time': {
                                            'tv_sec': int,
                                            'tv_nsec': int,
                                        },
                                        'last_execution_time': {
                                            'tv_sec': int,
                                            'tv_nsec': int,
                                        },
                                    },
                                }
                            },
                        },
                        'per_topo': {
                            Any(): {
                                'area': str,
                                'topo_index': str,
                                'te': {
                                    'link_holddown_timer': str,
                                    'purge_link_info_timer': str,
                                    'log': str,
                                    'tunnel_table': str,
                                    'info_from_te': str,
                                    'pce_info_from_te': str,
                                    'is_pce_ready': bool,
                                },
                                'overloaded_count': int,
                                'overload_bit_trigger_running': bool,
                                'bgp_converged_notify_h': str,
                                'added_first_hops': str,
                                'deleted_first_hops': str,
                                'postponed_added_first_hops': str,
                                'postponed_deleted_first_hops': str,
                                'prefixeschanged': str,
                                'nodechanged': str,
                                'prefix_priority_acl': {
                                    'critical': str,
                                    'high': str,
                                    'medium': str,
                                    'low': str,
                                },
                                'num_redist_prefixes': int,
                                'max_redist_prefixes_exceeded': bool,
                                'max_redist_prefixes_alarm_on': bool,
                                'has_prefix_policy_changed': bool,
                            },
                        },
                        'per_af': {
                            Any(): {
                                'router_id': str,
                            },
                        },
                    },
                },
                Optional('interfaces'): {
                    Any(): {
                        'im_handle': str,
                        'name': str,
                        'ref_count': int,
                        'index': int,
                        'snmp_index': int,
                        'chkpt': {
                            'objid': str,
                        },
                        Optional('ltopos_ready_active'): str,
                        'nsf_waiting_for_running': bool,
                        'nsf_ietf_waiting_for_sent_rr': bool,
                        'is_media_ready': bool,
                        'im_base_caps_exist_registered': bool,
                        'tmrs_active': bool,
                        'lsp_pacing_timer': str,
                        'lsp_sent_last_id': str,
                        'lsp_sent_last_area': int,
                        'lsp_send_b2b_limit':int,
                        'lsp_send_b2b_limit_window_end': {
                            'tv_sec': int,
                            'tv_nsec': int,
                        },
                        'mesh_group': str,
                        'lsp_send_requested': bool,
                        'lsp_send_in_progress': bool,
                        Optional('topos_enabled_passive'): str,
                        Optional('topos_enabled_active'): str,
                        'pri_label_stack_limit': Or(int, str),
                        'bkp_label_stack_limit': Or(int, str),
                        'srte_label_stack_limit': Or(int, str),
                        'srat_label_stack_limit': Or(int, str),
                        'bandwidth': Or(int, str),
                        'is_pme_delay_loss_set': bool,
                        'pme_avg_delay': str,
                        'pme_min_delay': str,
                        'pme_max_delay': str,
                        'pme_delay_var': str,
                        'pme_loss': str,
                        'pme_total_bw': str,
                        'pme_rsvp_te_bw': str,
                        'rsvp_max_res_bw': str,
                        'rsvp_unres_prio_7': str,
                        'cfg': {
                            'refcount': int,
                            'is_p2p': bool,
                            'enabled_mode': str,
                            'circuit_type': str,
                            'ipv4_bfd_enabled': bool,
                            'ipv6_bfd_enabled': bool,
                            'bfd_interval': int,
                            'bfd_multiplier': int,
                            'topos': str,
                            'cross_levels': {
                                'per_topo': {
                                    Any(): {
                                        'metric': Or(int, str),
                                        'weight': str,
                                        'ldp_sync_cfg': str,
                                        'admin_tag': str,
                                        'frr_type': str,
                                        'is_lkgp_set': int,
                                    },
                                },
                                'is_auth_cfg_ctx_set': bool,
                                'auth_cfg_ctx': {
                                    'alg': str,
                                    'failure_mode': str,
                                    'password': str,
                                    'accept_password': str,
                                },
                                'hello_interval_msecs': str,
                                'hello_multiplier': str,
                                'csnp_interval_secs': str,
                                'lsp_pacing_interval_msecs': str,
                                'lsp_fast_flood_threshold': str,
                                'lsp_rexmit_interval_secs': str,
                                'min_lsp_rexmit_interval_msecs': str,
                                'dr_priority': str,
                                'is_hello_padding_set': bool,
                                'hello_padding': str,
                            },
                            'per_level': {
                                Any(): {
                                    'per_topo': {
                                        Any(): {
                                            'metric': str,
                                            'weight': str,
                                            'ldp_sync_cfg': str,
                                            'admin_tag': str,
                                            'frr_type': str,
                                            'is_lkgp_set': int,
                                        },
                                    },
                                    'is_auth_cfg_ctx_set': bool,
                                    'auth_cfg_ctx': {
                                        'alg': str,
                                        'failure_mode': str,
                                        'password': str,
                                        'accept_password': str,
                                    },
                                    'hello_interval_msecs': str,
                                    'hello_multiplier': str,
                                    'csnp_interval_secs': str,
                                    'lsp_pacing_interval_msecs': str,
                                    'lsp_fast_flood_threshold': str,
                                    'lsp_rexmit_interval_secs': str,
                                    'min_lsp_rexmit_interval_msecs': str,
                                    'dr_priority': str,
                                    'is_hello_padding_set': bool,
                                    'hello_padding': str,
                                },
                            },
                        },
                        Optional('per_area'): {
                            Any(): {
                                'area_linkage': str,
                                'idb': str,
                                'area': str,
                                'adj_filter': str,
                                'csnp_control': {
                                    'timer': str,
                                    'next_lsp_id': str,
                                    'building_packets': bool,
                                },
                                'psnp_timer': str,
                                'nsf_ietf': {
                                    'full_csnp_set_rcvd': bool,
                                    'csnp_set_rcvd': {
                                        'list_head': str,
                                        'list_size': int,
                                    },
                                },
                                'adj_up_count': int,
                                'lan_adj_up_count': int,
                                'adj_list': str,
                                'per_ltopo': {
                                    Any(): {
                                        'num_requested_adjs': int,
                                        'num_adjs': int,
                                    },
                                },
                                'tmrs_active': bool,
                                'adj_filter_match_all': bool,
                                'lsp_count': {
                                    'in': int,
                                    'out': int,
                                },
                                'csnp_count': {
                                    'in': int,
                                    'out': int,
                                },
                                'psnp_count': {
                                    'in': int,
                                    'out': int,
                                },
                                'lsp_flooding_dup_count': int,
                                'lsp_drop_count': int,
                            },
                        },
                        'media': {
                            Any():{
                                Optional('caps_id'): int,
                                Optional('media_class'):  str,
                                Optional('encaps_overhead'): int,
                            },
                        },
                        Optional('media_specific'): {
                            Any(): {
                                'hello_timer': str,
                                'last_hello': {
                                    'tv_sec': int,
                                    'tv_nsec': int,
                                },
                                'recent_hello_send_count': int,
                                'adj_state': int,
                                'do_ietf_3way': bool,
                                'received_ietf_3way': bool,
                                'neighbor_extended_circuit_number': int,
                                'neighbor_system_id': str,
                                'lsp_rexmit_timer': str,
                                'mib_counters': {
                                    'circuit_type': int,
                                    'adj_changes': int,
                                    'num_adj': int,
                                    'init_fails': int,
                                    'rej_adjs': int,
                                    'id_field_len_mismatches': int,
                                    'max_area_addr_mismatches': int,
                                    'auth_type_fails': int,
                                    'auth_fails': int,
                                    'lan_des_is_canges': int,
                                    'index':int,
                                },
                                'init_csnp_wait': {
                                    'tv_sec': int,
                                    'tv_nsec': int,
                                },
                                'lsp_rexmit_queue': {
                                    'sll_head': str,
                                    'sll_tail': str,
                                    'sll_count': int,
                                    'sll_maximum': int,
                                },
                                'stats': {
                                    'iih_count': {
                                        'in': int,
                                        'out': int,
                                    },
                                    'iih_nomem': int,
                                    'lsp_retransmits': int,
                                },
                                'nsf_ietf': {
                                    't1_timer': str,
                                    'num_t1_expiries': int,
                                    'first_t1_expiry_seen': bool,
                                    'rr_sent': bool,
                                    'ra_rcvd': bool,
                                    'all_ra_seen': bool,
                                    'ra_required_nbr_count': int,
                                    Optional('ra_expected_neighbor_list'): list,
                                },
                                'p2p_over_lan': {
                                    'mcast_state': {
                                        'is_mcast_group_member': bool,
                                        'mcast_join_reason':  int,
                                    },
                                    'snpa_info': {
                                        'im_attr_macaddr_notify_handle':  str,
                                        'snpa': str,
                                        'is_snpa_ok': bool,
                                    },
                                },
                            },
                        },
                        'clns': {
                            'im_node': {
                                'exist_registered': bool,
                                'node_exists': bool,
                                'state_registered': bool,
                                'node_up': bool,
                            },
                            'mtu': int,
                        },
                        'per_af': {
                            Any(): {
                                'im_node': {
                                    'exist_registered': bool,
                                    'node_exists': bool,
                                    'state_registered': bool,
                                    'node_up': bool,
                                },
                                'local_address': str,
                                'is_nexthop_addr_registered': bool,
                                'is_global_prefix_registered': bool,
                                'is_running_passive': bool,
                            },
                        },
                        'per_topo': {
                            Any(): {
                                'refcount': int,
                            },
                        },
                        'mpls_ldp_sync': {
                            'im_attr_ldp_sync_info_notify_handle': Or(int, str),
                            'ldp_sync_info': bool,
                            'is_ldp_sync_info_ok': int,
                        },
                        'mpls_ldpv6_sync': {
                            'im_attr_ldp_sync_info_notify_handle': Or(int, str),
                            'ldp_sync_info': bool,
                            'is_ldp_sync_info_ok': int,
                        },
                        'stats': {
                            'ish_recv_count': int,
                            'esh_recv_count': int,
                            'unk_recv_count': int,
                        },

                    },
                },
            },
        },
    }


class ShowIsisPrivateAll(ShowIsisPrivateAllSchema):
    ''' Parser for commands:
       * show isis private all
    '''

    priority_level = {
        'ISIS_PREFIX_PRIORITY_CRITICAL': 'critical',
        'ISIS_PREFIX_PRIORITY_HIGH': 'high',
        'ISIS_PREFIX_PRIORITY_MED': 'medium',
        'ISIS_PREFIX_PRIORITY_LOW': 'low',
    }

    trap_stats_field = {
        'isisSysStatCorrLSPs': 'corr_lsps',
        'isisSysStatAuthTypeFails': 'auth_type_fails',
        'isisSysStatAuthFails':'auth_fails',
        'isisSysStatLSPDbaseOloads':'lsp_dbase_oloads',
        'isisSysStatManAddrDropFromAreas':'man_addr_drop_from_areas',
        'isisSysStatAttmptToExMaxSeqNums':'attmpt_to_ex_max_seq_nums',
        'isisSysStatSeqNumSkips':'seq_num_skips',
        'isisSysStatOwnLSPPurges':'own_lsp_purges',
        'isisSysStatIDFieldLenMismatches':'id_field_len_mismatches',
        'isisSysStatLSPErrors':'lsp_errors',
    }

    mib_counters_field = {
        'isisCircuitType': 'circuit_type',
        'isisCircAdjChanges': 'adj_changes',
        'isisCircNumAdj': 'num_adj',
        'isisCircInitFails': 'init_fails',
        'isisCircRejAdjs': 'rej_adjs',
        'isisCircIDFieldLenMismatches': 'id_field_len_mismatches',
        'isisCircMaxAreaAddrMismatches': 'max_area_addr_mismatches',
        'isisCircAuthTypeFails': 'auth_type_fails',
        'isisCircAuthFails': 'auth_fails',
        'isisCircLANDesISChanges': 'lan_des_is_canges',
        'isisCircIndex': 'index',
    }

    cli_command = 'show isis private all'

    def cli(self, output=None):

        if not output:
            output = self.device.execute(self.cli_command)

        # initial variables
        result_dict = {}
        indent_map = {}
        area_table_flag = False

        def get_parent_dict(indent):
            while indent > 0:
                indent -= 1
                parent = indent_map.get(indent)
                if parent is not None:
                    return parent

        def clear_indent_map(indent):
            for idx in list(indent_map):
                if idx >= indent:
                    indent_map.pop(idx)

        def get_key(key):
            if key.startswith('__'):
                return key.replace('__', '')

            if key in self.priority_level:
                return self.priority_level[key]

            if key in self.trap_stats_field:
                return self.trap_stats_field[key]

            if key in self.mib_counters_field:
                return self.mib_counters_field[key]

            return key

        def get_value(value):
            if not value:
                return None

            try:
                return int(value)
            except Exception:
                pass

            if value.lower() == 'true':
                return True

            if value.lower() == 'false':
                return False

            return value

        # +++++++++++++++++++++++ IS-IS TEST Global Private Data ++++++++++++++++++++++++

        # ISIS Test private data:
        r1 = re.compile(r'^(?P<indent>\s*)ISIS +(?P<instance>\w+) +private +data:$')

        # Address Family Table
        r2 = re.compile(r'^(?P<indent>\s*)Address +Family +Table$')

        # IPv4
        # IPv6
        r3 = re.compile(r'^(?P<indent>\s*)IPv(4|6)$')

        # Link Topology Table
        r4 = re.compile(r'^(?P<indent>\s*)Link +Topology +Table$')

        # Standard (IPv4 Unicast)
        r5 = re.compile(r'^(?P<indent>\s*)Standard +\(IPv4 +Unicast\)$')

        # Topology Table
        r6 = re.compile(r'^(?P<indent>\s*)Topology +Table$')

        # IPv4 Unicast
        # IPv4 Unicast VRF VRF1
        r7 = re.compile(r'^(?P<indent>\s*)IPv(4|6) +Unicast( +VRF +\S+)?$')

        # Configuration:
        r8 = re.compile(r'^(?P<indent>\s*)Configuration:$')

        # Area Configuration Table
        r9 = re.compile(r'^(?P<indent>\s*)Area +Configuration +Table$')

        # Cross Levels
        r10 = re.compile(r'^(?P<indent>\s*)Cross +Levels$')

        # Level-1
        r11 = re.compile(r'^(?P<indent>\s*)Level\-(?P<level>\d+)$')

        # Area Table
        r12 = re.compile(r'^(?P<indent>\s*)Area +Table$')

        # per_af[IPv4]
        # per_topo[IPv4 Unicast]   :
        # prefix_priority_acl[ISIS_PREFIX_PRIORITY_CRITICAL]: 0x0
        r13 = re.compile(r'^(?P<indent>\s*)(?P<key>\w+)\[(?P<type>.+)\]( *:)?'
                         r'( +(?P<value>.*))?$')

        # [000] is_spf_prefix_priority_acl_names_set : FALSE
        r14 = re.compile(r'^(?P<indent>\s*)\[(?P<idx>\d+)\] +(?P<key>\w+) *: +'
                         r'(?P<value>.*)$')


        # ++++++++++++++++++++++ IS-IS Test Interface Private Data ++++++++++++++++++++++

        # Interface TenGigE0/0/1/2
        r15 = re.compile(r'^(?P<indent>\s*)Interface +(?P<interface>\S+)$')

        #   media             : 0x440cc90
        r16 = re.compile(r'^(?P<indent>\s*)media *: +(?P<media>\S+)$')

        # cfg.cross_levels   :
        # cfg.per_level[Level-1]    :
        # cfg.per_level[Level-2]    :
        r17 = re.compile(r'^(?P<indent>\s*)(?P<key>cfg\.(cross_levels|per_level\[.*\])) +:$')

        # media_specific.p2p.nsf_ietf
        # media_specific.p2p.p2p_over_lan
        r18 = re.compile(r'^(?P<indent>\s*)(?P<key>[\w]+\.[\S]+)$')

        #   lsp_arrivaltime_parameter.backoff_cfg.secondary_wait_msecs: 200
        r99 = re.compile(r'^(?P<indent>\s*)(?P<key>[\w\.]+) *: +(?P<value>.*)$')

        for line in output.splitlines():
            line = line.rstrip()
            if not line:
                continue

            # ISIS TEST private data:
            m = r1.match(line)
            if m:
                group = m.groupdict()
                indent = len(group['indent'])
                instance = group['instance']
                inst_dict = result_dict.setdefault('instance', {}).setdefault(instance, {})
                indent_map.update({indent: inst_dict})
                area_table_flag = False
                continue

            # Address Family Table
            m = r2.match(line)
            if m:
                group = m.groupdict()
                indent = len(group['indent'])
                af_dict = inst_dict.setdefault('address_family_table', {})
                clear_indent_map(indent)
                indent_map.update({indent: af_dict})
                continue

            # IPv4
            # IPv6
            m = r3.match(line)
            if m:
                group = m.groupdict()
                indent = len(group['indent'])
                ip = line.strip()
                ip_dict = af_dict.setdefault(ip, {})
                clear_indent_map(indent)
                indent_map.update({indent: ip_dict})
                continue

            # Link Topology Table
            m = r4.match(line)
            if m:
                group = m.groupdict()
                indent = len(group['indent'])
                link_dict = inst_dict.setdefault('link_topology_table', {})
                clear_indent_map(indent)
                indent_map.update({indent: link_dict})
                continue

            # Standard (IPv4 unicast)
            m = r5.match(line)
            if m:
                group = m.groupdict()
                indent = len(group['indent'])
                key = line.strip()
                parent = get_parent_dict(indent)
                sub_dict = parent.setdefault(key, {})
                clear_indent_map(indent)
                indent_map.update({indent: sub_dict})
                continue

            # Topology Table
            m = r6.match(line)
            if m:
                group = m.groupdict()
                indent = len(group['indent'])
                topo_dict = inst_dict.setdefault('topology_table', {})
                clear_indent_map(indent)
                indent_map.update({indent: topo_dict})
                continue

            # IPv4 Unicast
            m = r7.match(line)
            if m:
                group = m.groupdict()
                indent = len(group['indent'])
                key = line.strip()
                parent = get_parent_dict(indent)
                sub_dict = parent.setdefault(key, {})
                clear_indent_map(indent)
                indent_map.update({indent: sub_dict})
                continue

            # Configuration:
            m = r8.match(line)
            if m:
                group = m.groupdict()
                indent = len(group['indent'])
                parent = get_parent_dict(indent)
                sub_dict = parent.setdefault('configuration', {})
                clear_indent_map(indent)
                indent_map.update({indent: sub_dict})
                continue

            # Area Configuration Table
            m = r9.match(line)
            if m:
                group = m.groupdict()
                indent = len(group['indent'])
                config_dict = inst_dict.setdefault('area_configuration_table', {})
                clear_indent_map(indent)
                indent_map.update({indent: config_dict})
                continue

            # Cross Levels
            m = r10.match(line)
            if m:
                group = m.groupdict()
                indent = len(group['indent'])
                parent = get_parent_dict(indent)
                sub_dict = parent.setdefault('cross_level', {})
                clear_indent_map(indent)
                indent_map.update({indent: sub_dict})
                continue

            # Level-1
            m = r11.match(line)
            if m:
                group = m.groupdict()
                indent = len(group['indent'])
                level = group['level']
                if area_table_flag:
                    parent = area_dict
                else:
                    parent = config_dict

                sub_dict = parent.setdefault('level-' + level, {})
                clear_indent_map(indent)
                indent_map.update({indent: sub_dict})
                continue

            # Area Table
            m = r12.match(line)
            if m:
                group = m.groupdict()
                indent = len(group['indent'])
                area_dict = inst_dict.setdefault('area_tables', {})
                clear_indent_map(indent)
                indent_map.update({indent: area_dict})
                area_table_flag = True
                continue

            # per_topo[IPv4 Unicast]   :
            # prefix_priority_acl[ISIS_PREFIX_PRIORITY_CRITICAL]: 0x0
            m = r13.match(line)
            if m:
                group = m.groupdict()
                indent = len(group['indent'])
                key = group['key']
                stype = get_key(group['type'])
                value = get_value(group['value'])
                parent = get_parent_dict(indent)

                if value:
                    sub = parent.setdefault(key, {})
                    sub.update({stype: value})
                else:
                    sub = parent.setdefault(key, {}).setdefault(stype, {})
                    clear_indent_map(indent)
                    indent_map.update({indent: sub})
                continue

            # [000] is_spf_prefix_priority_acl_names_set : FALSE
            m = r14.match(line)
            if m:
                group = m.groupdict()
                indent = len(group['indent'])
                idx = int(group['idx'])
                key = group['key']
                value = get_value(group['value'])
                parent = get_parent_dict(indent)

                sub = parent.setdefault('topo_index', {}).setdefault(idx, {})
                sub.update({key: value})
                continue

            # Interface TenGigE0/0/1/2
            m = r15.match(line)
            if m:
                group = m.groupdict()
                indent = len(group['indent'])
                interface = group['interface']
                intf_dict = inst_dict.setdefault('interfaces', {}).\
                                      setdefault(interface, {})

                clear_indent_map(indent)
                indent_map.update({indent: intf_dict})
                continue

            #   media             : 0x440cc90
            m = r16.match(line)
            if m:
                group = m.groupdict()
                indent = len(group['indent'])
                media = group['media']
                parent = get_parent_dict(indent)
                sub_dict = parent.setdefault('media', {}).setdefault(media, {})
                clear_indent_map(indent)
                indent_map.update({indent: sub_dict})
                continue

            # cfg.cross_levels   :
            # cfg.per_level[Level-1]    :
            # cfg.per_level[Level-2]    :
            m = r17.match(line)
            if m:
                group = m.groupdict()
                indent = len(group['indent'])
                keys = group['key'].replace('[','.').replace(']','').split('.')
                parent = get_parent_dict(indent)
                sub_dict = parent
                for key in keys:
                    sub_dict = sub_dict.setdefault(key, {})
                clear_indent_map(indent)
                indent_map.update({indent: sub_dict})
                continue

            # media_specific.p2p.nsf_ietf
            # media_specific.p2p.p2p_over_lan
            m = r18.match(line)
            if m:
                group = m.groupdict()
                indent = len(group['indent'])
                keys = group['key'].split('.')
                parent = get_parent_dict(indent)
                sub_dict = parent
                for key in keys:
                    sub_dict = sub_dict.setdefault(key, {})
                clear_indent_map(indent)
                indent_map.update({indent: sub_dict})
                continue

            #   lsp_arrivaltime_parameter.backoff_cfg.secondary_wait_msecs: 200
            m = r99.match(line)
            if m:
                group = m.groupdict()
                indent = len(group['indent'])
                keys = group['key'].split('.')
                value = get_value(group['value'])
                parent = get_parent_dict(indent)

                if len(keys) == 1:
                    parent.update({keys[0]: value})
                else:
                    sub = parent
                    for key in keys[:-1]:
                        key = get_key(key)
                        sub = sub.setdefault(key, {})
                    sub.update({get_key(keys[-1]): value})
                continue

        return result_dict

class ShowIsisSegmentRoutingSrv6LocatorsSchema(MetaParser):
    """Schema for:
        * show isis segment-routing srv6 locators
        * show isis instance {instance} segment-routing srv6 locators
    """
    schema = {
        'instance': {
            Any(): {
                'locators': {
                    Any(): {
                        'id': int,
                        'algo': int,
                        'prefix': str,
                        'status': str
                    },
                }
            }
        }
    }

# ==============================================
# Parser for 'show isis segment-routing srv6 locators'
# ==============================================

class ShowIsisSegmentRoutingSrv6Locators(ShowIsisSegmentRoutingSrv6LocatorsSchema):
    """Parser for:
    * show isis segment-routing srv6 locators
    * show isis instance {instance} segment-routing srv6 locators
    """
    cli_command = ['show isis segment-routing srv6 locators',
                   'show isis instance {instance} segment-routing srv6 locators']

    def cli(self, instance=None, output=None):

        if output is None:
            if instance:
                out = self.device.execute(self.cli_command[1].format(instance=instance))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        isis_dict = {}
        # IS-IS 1 SRv6 Locators
        p0 =  re.compile(r'^IS-IS\s+(?P<instance>\S+)\s+SRv6\s+Locators$')

        # Name                  ID       Algo  Prefix                    Status
        # ------                ----     ----  ------                    ------
        # ALGO_0                1        0     cafe:0:100::/48           Active
        # ALGO_128              2        128   cafe:0:128::/48           Active
        # ALGO_129              3        129   cafe:0:129::/48           Active

        p1 = re.compile(r'^(?P<name>\w+)\s+(?P<id>\d+)\s+(?P<algo>\d+) +'
                        r'\s+(?P<prefix>[a-fA-F\d\:]+\/\d{1,3}) +'
                        r'\s+(?P<status>\w+)$')

        for line in out.splitlines():
            line = line.strip()

            # IS-IS 1 SRv6 Locators
            m = p0.match(line)
            if m:
                instance = m.groupdict()['instance']
                final_dict = isis_dict.setdefault('instance', {}).\
                    setdefault(instance, {})
                continue

            # Name                  ID       Algo  Prefix                    Status
            # ------                ----     ----  ------                    ------
            # ALGO_0                1        0     cafe:0:100::/48           Active
            # ALGO_128              2        128   cafe:0:128::/48           Active
            # ALGO_129              3        129   cafe:0:129::/48           Active
            m = p1.match(line)
            if m:
                group = m.groupdict()
                final_dict.setdefault('locators', {}).setdefault(group['name'], {})\
                    .update({
                        'id': int(group['id']),
                        'algo': int(group['algo']),
                        'prefix': group['prefix'],
                        'status': group['status']
                    })
                continue

        return isis_dict
