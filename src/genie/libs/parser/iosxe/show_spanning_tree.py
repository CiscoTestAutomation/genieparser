"""show_spanning_tree.py
   supported commands:
     *  show spanning-tree detail
     *  show spanning-tree mst detail
     *  show spanning-tree summary
     *  show errdisable recovery
     *  show spanning-tree
     *  show spanning-tree mst <WORD>
     *  show spanning-tree vlan <WORD>
     *  show spanning-tree mst configuration

"""
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use

# import parser utils
from genie.libs.parser.utils.common import Common


class ShowSpanningTreeSummarySchema(MetaParser):
    """Schema for show spanning-tree summary"""
    schema = {
        Optional('etherchannel_misconfig_guard'): bool,
        Optional('extended_system_id'): bool,
        Optional('portfast_default'): bool,
        'bpdu_guard': bool,
        Optional('bpdu_filter'): bool,
        Optional('bridge_assurance'): bool,
        Optional('loop_guard'): bool,
        Optional('uplink_fast'): bool,
        Optional('backbone_fast'): bool,
        Optional('root_bridge_for'): str,
        Optional('pvst_simulation'): bool,
        Optional('pvst_simulation_status'): str,
        Optional('platform_pvst_simulation'): bool,
        Optional("configured_pathcost"): {
            'method': str,
            Optional('operational_value'): str,
        },
        Optional('mode'): {
            Any(): {  # mstp, pvst, rapid_pvst
                Any(): {  # <mst_domain>,  <pvst_id>
                    'blocking': int,
                    'listening': int,
                    'learning': int,
                    'forwarding': int,
                    'stp_active': int,
                }
            }
        },
        'total_statistics': {
            'blockings': int,
            'listenings': int,
            'learnings': int,
            'forwardings': int,
            'stp_actives': int,
            Optional('num_of_msts'): int,
            Optional('num_of_vlans'): int,
        }
    }
class ShowSpanningTreeSummary(ShowSpanningTreeSummarySchema):
    """Parser for show show spanning-tree summary"""

    cli_command = 'show spanning-tree summary'

    def cli(self,output=None):
        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^Switch +is +in +(?P<mode>[\w\-]+) +mode( *\(IEEE +Standard\))?$')
        p2 = re.compile(r'^Root +bridge +for: +(?P<root_bridge_for>[\w\-\,\s]+).?$')
        #p3 = re.compile(r'^(?P<name>\w+(?: \S+){,5}?) +is '
        #                 '+(?P<value>disabled|enabled)(?: +but +inactive +in (?P<simulation_value>\S+) +mode)?$')
        p3 = re.compile(r'^(?P<name>\w+(?: \S+){,5}?) +is +(?P<value>disable|disabled|enabled)'
                        r'(?: +but (?P<simulation_value>active|inactive) +in +rapid-pvst +mode)?$')

        p4 = re.compile(r'^(?P<id>(?!Total)\w+) +(?P<blocking>\d+) +(?P<listening>\d+)'
                        r' +(?P<learning>\d+) +(?P<forwarding>\d+) +(?P<stp_active>\d+)$')
        p5 = re.compile(r'^(?P<num>\d+) +(msts?|vlans?) +(?P<blockings>\d+) +(?P<listenings>\d+)'
                        r' +(?P<learnings>\d+) +(?P<forwardings>\d+) +(?P<stp_actives>\d+)$')

        p6 = re.compile(r'^(?:Configured +)?Pathcost +method +used +is '
                        r'+(?P<method>\w+)(?: +\(Operational +value +is +(?P<operational_value>\w+)\))?$')

        p7 = re.compile(r'Total +(?P<blockings>\d+) +(?P<listenings>\d+)'
                        r' +(?P<learnings>\d+) +(?P<forwardings>\d+) +(?P<stp_actives>\d+)$')

        p8 = re.compile(r'^(?P<root_bridge_for>(?:(?:[\w-]+, +)+)?[\w-]+)$')

        key_map = {'EtherChannel misconfig guard': 'etherchannel_misconfig_guard',
                   'Extended system ID': 'extended_system_id',
                   'Portfast Default': 'portfast_default',
                   'PortFast BPDU Guard': 'bpdu_guard',
                   'PortFast BPDU Guard Default': 'bpdu_guard',
                   'Portfast Edge BPDU Guard Default': 'bpdu_guard',
                   'Portfast BPDU Filter Default': 'bpdu_filter',
                   'Portfast Edge BPDU Filter Default': 'bpdu_filter',
                   'Loopguard Default': 'loop_guard',
                   'UplinkFast': 'uplink_fast',
                   'Bridge Assurance': 'bridge_assurance',
                   'BackboneFast': 'backbone_fast',
                   'PVST Simulation': 'pvst_simulation',
                   'Platform PVST Simulation': 'platform_pvst_simulation'}

        for line in out.splitlines():
            line = line.strip()

            # Switch is in mst mode (IEEE Standard)
            m = p1.match(line)
            if m:
                mode = m.groupdict()['mode'].replace('-', '_')
                continue
            
            # Root bridge for: MST0, MST100
            m = p2.match(line)
            if m:
                ret_dict['root_bridge_for'] = m.groupdict()['root_bridge_for']
                continue
            
            # VLAN0780, VLAN0801-VLAN0803, VLAN0806, VLAN0808-VLAN0818, VLAN0821-VLAN0822
            m = p8.match(line)
            if m:
                ret_dict['root_bridge_for'] += ', {}'.format(m.groupdict()['root_bridge_for'])

            # EtherChannel misconfig guard is disabled
            # Extended system ID           is enabled
            # Portfast Default             is disabled
            # PortFast BPDU Guard Default  is disabled  or  Portfast Edge BPDU Guard Default
            # Portfast BPDU Filter Default is disabled  or  Portfast Edge BPDU Filter Default
            # Loopguard Default            is disabled
            # UplinkFast                   is disabled
            # BackboneFast                 is disabled
            # PVST Simulation              is enabled
            # PVST Simulation Default                 is enabled but inactive in rapid-pvst mode
            # Platform PVST Simulation is enabled
            m = p3.match(line)
            if m:
                group = m.groupdict()
                if 'PVST Simulation Default' in group['name']:
                    group['name'] = 'PVST Simulation'

                if 'enabled' in group['value'].lower():
                    if group['simulation_value']:
                        ret_dict[key_map[group['name'].strip()]] = True
                        ret_dict['pvst_simulation_status'] = group['simulation_value']
                    else:
                        ret_dict[key_map[group['name'].strip()]] = True
                else:
                    ret_dict[key_map[group['name'].strip()]] = False
                
                continue

            # VLAN0100                     0         1        0          0          1
            m = p4.match(line)
            if m:
                group = m.groupdict()
                mode_id = group.pop('id')
                mode_dict = ret_dict.setdefault('mode', {})\
                    .setdefault(mode, {}).setdefault(mode_id, {})
                mode_dict.update({k:int(v) for k, v in group.items()})
                continue

            # 5 vlans                      0         5        0          0          5
            # 2 msts                       6         0        0         10         16
            m = p5.match(line)
            if m:
                group = m.groupdict()
                if 'mst' in line:
                    key = 'num_of_msts'
                elif 'vlan' in line:
                    key = 'num_of_vlans'
                ret_dict.setdefault('total_statistics', {})\
                    .setdefault(key, int(group.pop('num')))
                ret_dict.setdefault('total_statistics', {})\
                    .update({k:int(v) for k, v in group.items()})
                continue

            # Configured Pathcost method used is short
            # Configured Pathcost method used is short (Operational value is long)
            # Pathcost method used                     is long
            m = p6.match(line)
            if m:
                group = m.groupdict()
                
                ret_dict.setdefault('configured_pathcost', {})\
                    .update({k:v for k, v in group.items() if v})
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_statistics', {}) \
                     .update({k: int(v) for k, v in group.items()})
                continue

        return ret_dict


class ShowSpanningTreeDetailSchema(MetaParser):
    """Schema for show spanning-tree detail"""
    schema = {
        Any(): {     # mstp, pvst, rapid_pvst
            Optional('domain'): str,
            Optional('pvst_id'): str,
            Optional('name'): str,
            Optional('revision'): int,
            Optional('max_hop'): int,
            'hello_time': int,
            'max_age': int,
            'forwarding_delay': int,
            Optional('hold_count'): int,
            Any(): {   # mst_instances, vlans
                Any(): {
                    Optional('mst_id'): int,
                    Optional('vlan'): str,
                    Optional('vlan_id'): int,
                    Optional('hello_time'): int,
                    Optional('max_age'): int,
                    Optional('forwarding_delay'): int,
                    Optional('hold_count'): int,
                    'bridge_priority': int,
                    'bridge_sysid': int,
                    'bridge_address': str,
                    Optional('root_of_spanning_tree'): bool,
                    'topology_change_flag': bool,
                    'topology_detected_flag': bool,
                    'hold_time': int,
                    'topology_changes': int,
                    'time_since_topology_change': str,
                    Optional('topology_from_port'): str,
                    'hello_time': int,
                    'max_age': int,
                    'forwarding_delay': int,
                    'hold_time': int,
                    'topology_change_times': int,
                    'notification_times': int,
                    'hello_timer': int,
                    'topology_change_timer': int,
                    'notification_timer': int,
                    Optional('aging_timer'): int,
                    Optional('interfaces'): {
                        Any(): {
                            'status': str,
                            'name': str,
                            'cost': int,
                            'port_priority': int,
                            'port_num': int,
                            'port_identifier': str,
                            'designated_root_priority': int,
                            'designated_root_address': str,
                            'designated_path_cost': int,
                            'designated_port_id': str,
                            'designated_bridge_priority': int,
                            'designated_bridge_address': str,
                            'number_of_forward_transitions': int,
                            'message_age': int,
                            'forward_delay': int,
                            'hold': int,
                            'link_type': str,
                            Optional('internal'): bool,
                            Optional('boundary'): str,
                            Optional('peer'): str,
                            Optional('loop_guard'): bool,
                            'counters': {
                                'bpdu_sent': int,
                                'bpdu_received': int,
                            }
                        }
                    }
                },
            },
        }
    }


class ShowSpanningTreeDetail(ShowSpanningTreeDetailSchema):
    """Parser for show spanning-tree detail"""
    MODE_NAME_MAP = {'mstp': 'mstp',
                     'ieee': 'pvst',
                     'rstp': 'rapid_pvst'}
    MODE_INST_MAP = {'mstp': 'mst_instances',
                     'ieee': 'vlans',
                     'rstp': 'vlans'}
    MODE_KEY_MAP = {'mstp': 'mst_id',
                     'ieee': 'vlan_id',
                     'rstp': 'vlan_id'}
    cli_command = 'show spanning-tree detail'

    def cli(self, output=None):
        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command)
        else:
            out = output
        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        # MST0 is executing the mstp compatible Spanning Tree protocol
        p1 = re.compile(r'^(MST|VLAN)?(?P<inst>\w+) +is +executing +the +(?P<mode>[\w\-]+) +'
                        r'compatible +Spanning +Tree +protocol$')

        # Bridge Identifier has priority 8192, sysid 0, address 5897.bdff.3b3a 
        p2 = re.compile(r'^Bridge +Identifier +has +priority +(?P<bridge_priority>\d+), +'
                        r'sysid +(?P<bridge_sysid>\d+), +'
                        r'address +(?P<bridge_address>[\w\.]+)$')

        # Configured hello time 2, max age 20, forward delay 15, transmit hold-count 6 
        p3 = re.compile(r'^Configured +hello +time +(?P<hello_time>\d+), +'
                        r'max +age +(?P<max_age>\d+), +forward +delay +(?P<forwarding_delay>\d+)(, +'
                        r'(transmit|tranmsit) +hold\-count +(?P<hold_count>\d+))?$')

        # We are the root of the spanning tree 
        p4 = re.compile(r'^We +are +the +root +of +the +spanning +tree$')

        # Topology change flag not set, detected flag not set 
        p5 = re.compile(r'^Topology +change +flag +(?P<topology_change_flag>[\w\s]+), +'
                        r'detected +flag +(?P<topology_detected_flag>[\w\s]+)$')

        # Number of topology changes 471 last change occurred 16:02:38 ago 
        p6 = re.compile(r'^Number +of +topology +changes +(?P<topology_changes>\d+) +'
                        r'last +change +occurred +(?P<time_since_topology_change>[\w\.\:]+)( +ago)?$')

        # from TenGigabitEthernet2/3 
        p7 = re.compile(r'^from +(?P<topology_from_port>[\w\.\/\-]+)$')

        # Times:  hold 1, topology change 35, notification 2
        p8 = re.compile(r'^Times: +hold +(?P<hold_time>\d+), +'
                        r'topology +change +(?P<topology_change_times>\d+), +'
                        r'notification +(?P<notification_times>\d+)$')

        # hello 2, max age 20, forward delay 15 
        p9 = re.compile(r'^hello +(?P<hello_time>\d+), '
                        r'max +age +(?P<max_age>\d+), '
                        r'+forward +delay +(?P<forwarding_delay>\d+)$')

        # Timers: hello 0, topology change 0, notification 0
        p10 = re.compile(r'^Timers: +hello +(?P<hello_timer>\d+), +'
                         r'topology +change +(?P<topology_change_timer>\d+), +'
                         r'notification +(?P<notification_timer>\d+)'
                         r'(, +aging +(?P<aging_timer>\d+))?$')

        # Port 2 (GigabitEthernet1/2) of MST0 is designated forwarding
        p11 = re.compile(r'^Port +(?P<port_num>\d+) *\((?P<name>[\w\/\-\.]+)\) +'
                         r'of +(?P<inst>\w+) +is +(?P<status>.*)$')

        # Port path cost 20000, Port priority 128, Port Identifier 128.2. 
        p12 = re.compile(r'^Port +path +cost +(?P<cost>\d+), +'
                         r'Port +priority +(?P<port_priority>\d+), +'
                         r'Port +Identifier +(?P<port_identifier>[\w\.]+)$')

        # Designated root has priority 8192, address 5897.bdff.3b3a 
        p13 = re.compile(r'^Designated +root +has +priority +(?P<designated_root_priority>\d+), +'
                         r'address +(?P<designated_root_address>[\w\.]+)$')

        # Designated bridge has priority 8192, address 5897.bdff.3b3a 
        p14 = re.compile(r'^Designated +bridge +has +priority +(?P<designated_bridge_priority>\d+), +'
                         r'address +(?P<designated_bridge_address>[\w\.]+)$')

        # Designated port id is 128.2, designated path cost 0 
        p15 = re.compile(r'^Designated +port +id +is +(?P<designated_port_id>[\w\.]+), +'
                         r'designated +path +cost +(?P<designated_path_cost>\d+)'
                         r'( +[\w\s\,]+)?$')

        # Timers: message age 0, forward delay 0, hold 0 
        p16 = re.compile(r'^Timers: +message +age +(?P<message_age>\d+), +'
                         r'forward +delay +(?P<forward_delay>\d+), +hold +(?P<hold>\d+)$')

        # Number of transitions to forwarding state: 0 
        p17 = re.compile(r'^Number +of +transitions +to +forwarding +'
                         r'state: +(?P<number_of_forward_transitions>\d+)$')

        # Link type is point-to-point by default, Internal
        # Link type is point-to-point by default, Internal Pre-STD
        # Link type is point-to-point by default, Boundary PVST
        p18 = re.compile(r'^Link +type +is +(?P<link_type>[\w\-]+) +by +default'
                         r'(, *(Boundary +(?P<boundary>\w+)|Peer +is +(?P<peer>\w+)))?'
                         r'(?:, +(?P<internal>Internal( +\S+)?))?$')

        # Loop guard is enabled by default on the port
        p19 = re.compile(r'^Loop +guard +is +(?P<loop_guard>\w+) +by +default +on +the +port$')

        # BPDU: sent 2349185, received 0
        p20 = re.compile(r'^BPDU: +sent +(?P<bpdu_sent>\d+), +'
                         r'received +(?P<bpdu_received>\d+)$')

        for line in out.splitlines():
            line = line.strip()
            
            # MST0 is executing the mstp compatible Spanning Tree protocol
            m = p1.match(line)
            if m:
                group = m.groupdict()
                mode = group['mode']
                mode_dict = ret_dict.setdefault(self.MODE_NAME_MAP[mode], {})
                inst_dict = mode_dict.setdefault(self.MODE_INST_MAP[mode], {}).\
                    setdefault(int(group['inst']), {})
                inst_dict[self.MODE_KEY_MAP[mode]] = int(group['inst'])
                continue

            # Bridge Identifier has priority 32768, sysid 0, address d8b1.90ff.c889
            m = p2.match(line)
            if m:
                group = m.groupdict()
                inst_dict['bridge_address'] = group.pop('bridge_address')
                inst_dict.update({k:int(v) for k, v in group.items()})
                continue

            # Configured hello time 10, max age 40, forward delay 30, transmit hold-count 20
            # Configured hello time 2, max age 20, forward delay 15, tranmsit hold-count 6
            m = p3.match(line)
            if m:
                group = m.groupdict()
                update_dict = {k:int(v) for k, v in group.items() if v}
                mode_dict.update(update_dict)
                inst_dict.update(update_dict)
                continue

            # We are the root of the spanning tree
            m = p4.match(line)
            if m:
                inst_dict['root_of_spanning_tree'] = True
                continue

            # Topology change flag not set, detected flag not set
            m = p5.match(line)
            if m:
                group = m.groupdict()
                inst_dict['topology_change_flag'] = False if 'not' in group['topology_change_flag'] else True
                inst_dict['topology_detected_flag'] = False if 'not' in group['topology_detected_flag'] else True
                continue

            # Number of topology changes 3 last change occurred 03:09:48 ago
            m = p6.match(line)
            if m:
                group = m.groupdict()
                inst_dict['topology_changes'] = int(group['topology_changes'])
                inst_dict['time_since_topology_change'] = group['time_since_topology_change']
                continue

            #       from Port-channel24
            m = p7.match(line)
            if m:
                inst_dict['topology_from_port'] = m.groupdict()['topology_from_port']
                continue

            # Times:  hold 1, topology change 70, notification 10
            m = p8.match(line)
            if m:
                group = m.groupdict()
                inst_dict.update({k:int(v) for k, v in group.items()})
                continue

            #       hello 10, max age 40, forward delay 30 
            m = p9.match(line)
            if m:
                group = m.groupdict()
                inst_dict.update({k:int(v) for k, v in group.items()})
                continue

            # Timers: hello 0, topology change 0, notification 0
            # hello 0, topology change 0, notification 0, aging 300
            m = p10.match(line)
            if m:
                group = m.groupdict()
                inst_dict.update({k:int(v) for k, v in group.items() if v})
                continue

            # Port 2390 (Port-channel14) of MST0 is broken  (PVST Sim. Inconsistent)
            # Port 2400 (Port-channel24) of MST0 is designated forwarding 
            m = p11.match(line)
            if m:
                group = m.groupdict()
                intf_dict = inst_dict.setdefault('interfaces', {}).setdefault(group['name'], {})
                intf_dict['port_num'] = int(group['port_num'])
                intf_dict['name'] = group['name']
                intf_dict['status'] = group['status']
                continue

            # Port path cost 6660, Port priority 128, Port Identifier 128.2390.
            m = p12.match(line)
            if m:
                group = m.groupdict()
                intf_dict['port_identifier'] = group.pop('port_identifier')
                intf_dict.update({k:int(v) for k, v in group.items()})
                continue

            # Designated root has priority 32768, address d8b1.90ff.c889
            m = p13.match(line)
            if m:
                group = m.groupdict()
                intf_dict['designated_root_priority'] = int(group['designated_root_priority'])
                intf_dict['designated_root_address'] = group['designated_root_address']
                continue

            # Designated bridge has priority 32768, address d8b1.90ff.c889
            m = p14.match(line)
            if m:
                group = m.groupdict()
                intf_dict['designated_bridge_priority'] = int(group['designated_bridge_priority'])
                intf_dict['designated_bridge_address'] = group['designated_bridge_address']
                continue

            # Designated port id is 128.2390, designated path cost 0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                intf_dict['designated_path_cost'] = int(group['designated_path_cost'])
                intf_dict['designated_port_id'] = group['designated_port_id']
                continue

            # Timers: message age 0, forward delay 0, hold 0
            m = p16.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({k:int(v) for k, v in group.items()})
                continue

            # Number of transitions to forwarding state: 0
            m = p17.match(line)
            if m:
                intf_dict['number_of_forward_transitions'] = \
                    int(m.groupdict()['number_of_forward_transitions'])
                continue

            # Link type is point-to-point by default, Boundary PVST
            # Link type is point-to-point by default, Internal
            # Link type is point-to-point by default, Internal Pre-STD
            m = p18.match(line)
            if m:
                group = m.groupdict()
                internal = group.pop('internal', None)
                if internal:
                    internal_bool = True
                    intf_dict['internal'] = internal_bool

                intf_dict.update({k:v for k, v in group.items() if v})
                continue

            # Loop guard is enabled by default on the port
            m = p19.match(line)
            if m:
                group = m.groupdict()
                intf_dict['loop_guard'] = True if 'enabled' in m.groupdict()['loop_guard'].lower() \
                    else False
                continue

            # BPDU: sent 138231, received 167393
            m = p20.match(line)
            if m:
                group = m.groupdict()
                intf_dict.setdefault('counters', {}).update({k:int(v) for k, v in group.items()})
                continue

        return ret_dict


class ShowSpanningTreeMstDetailSchema(MetaParser):
    """Schema for show spanning-tree mst detail"""
    schema = {
        'mst_instances': {
            Any(): {
                'mst_id': int,
                Optional('vlan'): str,
                'bridge_address': str,
                'bridge_priority': int,
                'sysid': int,
                Optional('root'): str,
                Optional('root_address'): str,
                Optional('root_priority'): int,
                Optional('operational'): {
                    'hello_time': int,
                    'forward_delay': int,
                    'max_age': int,
                    'tx_hold_count': int
                },
                Optional('configured'): {
                    'hello_time': int,
                    'forward_delay': int,
                    'max_age': int,
                    'max_hops': int
                },
                'interfaces': {
                    Any(): {
                        'status': str,
                        Optional('broken_reason'): str,
                        'name': str,
                        'port_id': str,
                        'cost': int,
                        'port_priority': int,
                        'designated_root_priority': int,
                        'designated_root_address': str,
                        'designated_root_cost': int,
                        Optional('designated_regional_root_cost'): int,
                        Optional('designated_regional_root_priority'): int,
                        Optional('designated_regional_root_address'): str,
                        'designated_bridge_priority': int,
                        'designated_bridge_address': str,
                        'designated_bridge_port_id': str,
                        'forward_transitions': int,
                        'message_expires': int,
                        'forward_delay': int,
                        'counters': {
                            'bpdu_sent': int,
                            'bpdu_received': int,
                        }
                    }
                }
            },
        }
    }


class ShowSpanningTreeMstDetail(ShowSpanningTreeMstDetailSchema):
    """Parser for show spanning-tree mst detail"""

    cli_command = 'show spanning-tree mst detail'

    def cli(self, output=None):
        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^\#+ +MST(?P<inst>\d+) +'
                        r'vlans +mapped: +(?P<vlan>[\d\-\,\s]+)$')

        p2 = re.compile(r'^Bridge +address +(?P<bridge_address>[\w\.]+) +'
                        r'priority +(?P<bridge_priority>\d+) +'
                        r'\((\d+) +sysid +(?P<sysid>\d+)\)$')
        
        p3 = re.compile(r'^Root +this +switch +for +(the +)?(?P<root>[\w\.\s]+)$')

        # Root          address 58ac.78ff.c3f5  priority      8198  (8192 sysid 6)
        p3_1 = re.compile(r'^Root +address +(?P<root_address>[\w\.]+) +'
                          r'priority +(?P<root_priority>\d+) +'
                          r'\((\d+) +sysid +(?P<sysid>\d+)\)$')
        
        p4 = re.compile(r'^Operational +hello +time +(?P<hello_time>\d+), +'
                        r'forward +delay +(?P<forward_delay>\d+), +'
                        r'max +age +(?P<max_age>\d+), +'
                        r'txholdcount +(?P<tx_hold_count>\d+)$')
        
        p5 = re.compile(r'^Configured +hello +time +(?P<hello_time>\d+), +'
                        r'forward +delay +(?P<forward_delay>\d+), +'
                        r'max +age +(?P<max_age>\d+), +'
                        r'max +hops +(?P<max_hops>\d+)$')
        
        p6 = re.compile(r'^(?P<name>[\w\-\.\/]+) +of +'
                        r'MST(\d+) +is +(?P<status>[\w\s]+)'
                        r'( +\((?P<broken_reason>.*)\))?$')
        
        p7 = re.compile(r'^Port +info +port +id +'
                        r'(?P<port_id>[\d\.]+) +'
                        r'priority +(?P<port_priority>\d+) +'
                        r'cost +(?P<cost>\d+)$')
        
        p8 = re.compile(r'^Designated +root +address +'
                        r'(?P<designated_root_address>[\w\.]+) +'
                        r'priority +(?P<designated_root_priority>\d+) +'
                        r'cost +(?P<designated_root_cost>\d+)$')
        
        p9 = re.compile(r'^Design\. +regional +root +address +'
                        r'(?P<designated_regional_root_address>[\w\.]+) +'
                        r'priority +(?P<designated_regional_root_priority>\d+) +'
                        r'cost +(?P<designated_regional_root_cost>\d+)$')
        
        p10 = re.compile(r'^Designated +bridge +address +'
                         r'(?P<designated_bridge_address>[\w\.]+) +'
                         r'priority +(?P<designated_bridge_priority>\d+) +'
                         r'port +id +(?P<designated_bridge_port_id>[\d\.]+)$')
        
        p11 = re.compile(r'^Timers: +message +expires +in +(?P<message_expires>\d+) +sec, +'
                         r'forward +delay +(?P<forward_delay>\d+), '
                         r'forward +transitions +(?P<forward_transitions>\d+)$')
        
        p12 = re.compile(r'^Bpdus +(\(\w+\) *)?'
                         r'sent +(?P<bpdu_sent>\d+), +'
                         r'received +(?P<bpdu_received>\d+)')


        for line in out.splitlines():
            line = line.strip()
            
            # ##### MST0    vlans mapped:   1-9,11-99,101-4094
            m = p1.match(line)
            if m:
                group = m.groupdict()
                inst = int(group['inst'])
                inst_dict = ret_dict.setdefault('mst_instances', {}).setdefault(inst, {})
                inst_dict['mst_id'] = inst
                inst_dict['vlan'] = group['vlan']
                continue

            # Bridge        address d8b1.90ff.c889  priority      32768 (32768 sysid 0)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                inst_dict['bridge_address'] = group.pop('bridge_address')
                inst_dict.update({k:int(v) for k, v in group.items()})
                continue
            
            # Root          this switch for the CIST
            m = p3.match(line)
            if m:
                inst_dict['root'] = m.groupdict()['root']
                continue

            # Root          address 58ac.78ff.c3f5  priority      8198  (8192 sysid 6)
            m = p3_1.match(line)
            if m:
                group = m.groupdict()
                inst_dict['root_address'] = group.pop('root_address')
                inst_dict.update({k:int(v) for k, v in group.items()})
                continue
            
            # Operational   hello time 10, forward delay 30, max age 40, txholdcount 20
            m = p4.match(line)
            if m:
                inst_dict.setdefault('operational', {}).update(
                    {k:int(v) for k, v in m.groupdict().items()})
                continue
            
            # Configured    hello time 10, forward delay 30, max age 40, max hops    255
            m = p5.match(line)
            if m:
                inst_dict.setdefault('configured', {}).update(
                    {k:int(v) for k, v in m.groupdict().items()})
                continue
            
            # Port-channel14 of MST0 is broken (PVST Sim. Inconsistent)
            m = p6.match(line)
            if m:
                group = m.groupdict()
                intf = group['name']
                intf_dict = inst_dict.setdefault('interfaces', {}).setdefault(intf, {})
                intf_dict.update({k:v for k,v in group.items() if v})
                continue
            
            # Port info             port id         128.23  priority    128  cost       20000
            m = p7.match(line)
            if m:
                group = m.groupdict()
                intf_dict['port_id'] = group.pop('port_id')
                intf_dict.update({k:int(v) for k,v in group.items()})
                continue
            
            # Designated root       address 3820.56ff.e15b  priority  32768  cost           0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                intf_dict['designated_root_address'] = group.pop('designated_root_address')
                intf_dict.update({k:int(v) for k,v in group.items()})
                continue
            
            # Design. regional root address 3820.56ff.e15b  priority  32768  cost           0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                intf_dict['designated_regional_root_address'] = \
                    group.pop('designated_regional_root_address')
                intf_dict.update({k:int(v) for k,v in group.items()})
                continue
            
            # Designated bridge     address 3820.56ff.e15b  priority  32768  port id   128.23
            m = p10.match(line)
            if m:
                group = m.groupdict()
                intf_dict['designated_bridge_priority'] = \
                    int(group.pop('designated_bridge_priority'))
                intf_dict.update({k:v for k,v in group.items()})
                continue
            
            # Timers: message expires in 0 sec, forward delay 0, forward transitions 1
            m = p11.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({k:int(v) for k,v in group.items()})
                continue
            
            # Bpdus (MRecords) sent 493, received 0
            # Bpdus sent 493, received 0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                intf_dict.setdefault('counters', {}).update({k:int(v) for k,v in group.items()})
                continue

        return ret_dict


class ShowErrdisableRecoverySchema(MetaParser):
    """Schema for show errdisable recovery"""
    schema = {
        'timer_status': {
            Any(): bool,
        },
        'bpduguard_timeout_recovery': int,
        Optional('interfaces'): {
            Any(): {
                'interface': str,
                'errdisable_reason': str,
                'time_left': int,
            },
        }
    }


class ShowErrdisableRecovery(ShowErrdisableRecoverySchema):
    """Parser for show errdisable recovery"""

    cli_command = 'show errdisable recovery'

    def cli(self, output=None):
        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^Timer +interval: +(?P<interval>\d+) +seconds$')
        p2 = re.compile(r'^(?P<name>[\w\-\s\(\)\"\:"]+) +'
                         '(?P<status>(Disabled|Enabled)+)$')
        p3 = re.compile(r'^(?P<interface>[\w\-\/\.]+) +'
                         '(?P<errdisable_reason>\w+) +'
                         '(?P<time_left>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # Timer interval: 333 seconds
            m = p1.match(line)
            if m:
                ret_dict['bpduguard_timeout_recovery'] = int(m.groupdict()['interval'])
                continue
            
            # channel-misconfig (STP)      Disabled
            m = p2.match(line)
            if m:
                group = m.groupdict()
                status_dict = ret_dict.setdefault('timer_status', {})
                status_dict[group['name'].strip()] = False if 'disabled' in group['status'].lower() else True
                continue

            # Fa2/4                bpduguard          273
            m = p3.match(line)
            if m:
                group = m.groupdict()
                intf = Common.convert_intf_name(group.pop('interface'))
                intf_dict = ret_dict.setdefault('interfaces', {}).setdefault(intf, {})
                intf_dict['interface'] = intf
                intf_dict['time_left'] = int(group.pop('time_left'))
                intf_dict.update({k:v for k,v in group.items()})
                continue

        return ret_dict


class ShowSpanningTreeSchema(MetaParser):
    """Schema for show spanning-tree [mst|vlan <WORD>]"""
    schema = {
        Any(): {     # mstp, pvst, rapid_pvst
            Any(): {   # mst_instances, vlans
                Any(): {
                    Any(): { # root, bridge
                        'priority':  int,
                        'address': str,
                        Optional('cost'): int,
                        Optional('port'): int,
                        Optional('interface'): str,
                        Optional('configured_bridge_priority'): int,
                        Optional('sys_id_ext'): int,
                        'hello_time': int,
                        'max_age': int,
                        'forward_delay': int,
                        Optional('aging_time'):  int,
                    },
                    'interfaces': {
                        Any(): {
                            'role': str,
                            'port_state': str,
                            'cost': int,
                            'port_priority': int,
                            'port_num': int,
                            'type': str,
                            Optional('peer'): str,
                            Optional('bound'): str,
                        }
                    }
                }
            }
        }        
    }


class ShowSpanningTree(ShowSpanningTreeSchema):
    """Parser for show spanning-tree [mst|vlan <WORD>]"""

    MODE_NAME_MAP = {'mstp': 'mstp',
                     'ieee': 'pvst',
                     'rstp': 'rapid_pvst'}
    MODE_INST_MAP = {'mstp': 'mst_instances',
                     'ieee': 'vlans',
                     'rstp': 'vlans'}
    PORT_STATE_MAP = {'FWD': 'forwarding',
                     'BLK': 'blocking',
                     'DIS': 'disabled',
                     'LRN': 'learning',
                     'LIS': 'listensing',
                     'BKN*': 'broken'}
    ROLE_MAP = {'Mstr': 'master ',
                'Desg': 'designated',
                'Root': 'root',
                'BLK': 'blocking',
                'Altn': 'alternate',
                'Back': 'backup'}
    cli_command = ['show spanning-tree vlan {vlan}','show spanning-tree mst {mst}','show spanning-tree']

    def cli(self, mst='', vlan='',output=None):
        if output is None:
            # get output from device
            if vlan:
                cmd = self.cli_command[0].format(vlan=vlan)
            elif mst:
                cmd = self.cli_command[1].format(mst=mst)
            else:
                cmd = self.cli_command[2]

            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^(MST|VLAN)(?P<inst>\d+)$')
        p2 = re.compile(r'^Spanning +tree +enabled p+rotocol +(?P<mode>\w+)$')
        p3 = re.compile(r'^Root +ID +Priority +(?P<priority>\d+)$')
        p4 = re.compile(r'^Bridge +ID +Priority +(?P<priority>\d+)'
                         '( *\(priority +(?P<configured_bridge_priority>\d+) +'
                         'sys\-id\-ext +(?P<sys_id_ext>\d+)\))?$')
        p5 = re.compile(r'^Address +(?P<address>[\w\.]+)$')
        p6 = re.compile(r'^Cost +(?P<cost>\d+)$')
        p7 = re.compile(r'^Port +(?P<port>\d+) +\((?P<interface>[\w\-\/\.]+)\)$')
        p8 = re.compile(r'Hello +Time +(?P<hello_time>\d+) +sec +'
                         'Max +Age +(?P<max_age>\d+) +sec +'
                         'Forward +Delay +(?P<forward_delay>\d+) +sec$')
        p9 = re.compile(r'^Aging +Time +(?P<aging_time>\d+) +sec$')
        p10 = re.compile(r'^(?P<interface>[\w\-\/\.]+) +'
                          '(?P<role>[\w\*]+) +(?P<port_state>[A-Z\*]+) *'
                          '(?P<cost>\d+) +(?P<port_priority>\d+)\.'
                          '(?P<port_num>\d+) +(?P<type>\w+)'
                          '( +(Bound\((?P<bound>\w+)\)|Peer\((?P<peer>\w+)\)))?'
                          '( +\*\S+)?$')

        for line in out.splitlines():
            line = line.strip()

            # VLAN0200
            # MST10
            m = p1.match(line)
            if m:
                inst = int(m.groupdict()['inst'])
                continue
            
            # Spanning tree enabled protocol rstp
            m = p2.match(line)
            if m:
                mode_dict = ret_dict.setdefault(self.MODE_NAME_MAP[m.groupdict()['mode']], {})
                inst_dict = mode_dict.setdefault(self.MODE_INST_MAP[m.groupdict()['mode']], {}).\
                    setdefault(inst, {})
                continue
            
            # Root ID    Priority    24776
            m = p3.match(line)
            if m:
                role_dict = inst_dict.setdefault('root', {})
                role_dict['priority'] = int(m.groupdict()['priority'])
                continue

            # Address     58bf.eaff.e5b6
            m = p5.match(line)
            if m:
                role_dict['address'] = m.groupdict()['address']
                continue

            # Cost        3
            m = p6.match(line)
            if m:
                role_dict['cost'] = int(m.groupdict()['cost'])
                continue

            # Port        2390 (Port-channel14)
            m = p7.match(line)
            if m:
                group = m.groupdict()
                role_dict['port'] = int(group['port'])
                role_dict['interface'] = group['interface']
                continue

            # Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
            m = p8.match(line)
            if m:
                role_dict.update({k:int(v) for k,v in m.groupdict().items()})
                continue

            # Bridge ID  Priority    28872  (priority 28672 sys-id-ext 200)
            m = p4.match(line)
            if m:
                role_dict = inst_dict.setdefault('bridge', {})
                role_dict.update({k:int(v) for k,v in m.groupdict().items() if v})
                continue

            # Aging Time  300 sec
            m = p9.match(line)
            if m:
                role_dict['aging_time'] = int(m.groupdict()['aging_time'])
                continue

            # Gi1/0/5             Desg FWD 4         128.5    P2p Peer(STP)
            # Gi1/0/5             Mstr FWD 20000     128.5    P2p Bound(RSTP) 
            # Po14                Desg BKN*6660      128.2390 P2p Bound(PVST) *PVST_Inc
            m = p10.match(line)
            if m:
                group = m.groupdict()
                intf = Common.convert_intf_name(group.pop('interface'))
                intf_dict = inst_dict.setdefault('interfaces', {}).setdefault(intf, {})
                intf_dict['cost'] = int(group.pop('cost'))
                intf_dict['port_priority'] = int(group.pop('port_priority'))
                intf_dict['port_num'] = int(group.pop('port_num'))
                intf_dict['role'] = self.ROLE_MAP[group.pop('role')]
                intf_dict['port_state'] = self.PORT_STATE_MAP[group.pop('port_state')]
                intf_dict.update({k:v for k,v in group.items() if v})
                continue
        return ret_dict


class ShowSpanningTreeMstConfigurationSchema(MetaParser):
    """Schema for show spanning-tree mst configuration"""
    schema = {
        'mstp': {
            'name': str,
            'revision': int,
            'instances_configured': int,
            'mst_instances': {
                Any(): {
                    'vlan_mapped': str,
                }
            }
        }
    }


class ShowSpanningTreeMstConfiguration(ShowSpanningTreeMstConfigurationSchema):
    """Parser for show spanning-tree mst configuration"""

    cli_command = 'show spanning-tree mst configuration'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^Name +\[(?P<name>.*)\]$')
        p2 = re.compile(r'^Revision +(?P<revision>\d+) +'
                         'Instances +configured +(?P<instances_configured>\d+)$')
        p3 = re.compile(r'^(?P<inst>\d+) +(?P<vlan_mapped>[\d\,\s\-]+)$')

        for line in out.splitlines():
            line = line.strip()

            # Name      [mst]
            m = p1.match(line)
            if m:
                ret_dict['name'] = m.groupdict()['name']
                continue
            
            # Revision  111   Instances configured 2
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({k:int(v) for k, v in group.items()})
                continue

            # 0         1-99,201-4094
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('mst_instances', {}).setdefault(int(group['inst']), {}).update({
                    'vlan_mapped': group['vlan_mapped']})
                continue

        return {'mstp': ret_dict} if ret_dict else ret_dict