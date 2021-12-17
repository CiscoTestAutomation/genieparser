'''show_spanning_tree.py

NXOS parsers for the following show commands:
    * show spanning-tree detail
    * show spanning-tree mst detail
    * show spanning-tree summary
    * show spanning-tree issu-impact
'''


# -*- coding: utf-8 -*-
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional
from genie.libs.parser.utils.common import Common

#   ============================================    #
#                    mst detail                     #
#   ============================================    #

class ShowSpanningTreeMstSchema(MetaParser):
    '''Schema for:
            show spanning-tree mst detail
    '''
    
    schema = {
        'mstp' : {
            'mst_intances': {
                Any() : { 
                    'mst_id' : int,
                    'vlans_mapped' : str,
                    'bridge_priority': int,
                    'bridge_address': str,
                    Optional('sys_id'): int,
                    Optional('root_for_cist'): str,
                    Optional('regional_root'): str,
                    Optional('hold_time'): int,
                    Optional('topology_changes'): int,
                    Optional('time_since_topology_change'): str,
                    'interfaces': {
                        Any () :{
                            'name': str,
                            'port_cost': int,
                            'port_priority' : int,
                            'port_id': str,
                            'port_state' : str,
                            'bridge_assurance_inconsistent': bool,
                            'vpc_peer_link_inconsistent' : bool,
                            'designated_root_priority': int,
                            'designated_root_address': str,
                            'designated_root_cost': int,
                            'designated_bridge_priority': int,
                            'designated_bridge_address': str,
                            'designated_bridge_port_id': str,
                            'designated_regional_root_cost': int,
                            'designated_regional_root_priority': int,
                            'designated_regional_root_address': str,
                            Optional('broken_reason'): str,
                            Optional('designated_port_num'): str,
                            Optional('timers') :{
                                'forward_transitions': int,
                                'forward_delay': int,
                                'message_expires_in': int,
                            },
                            Optional('counters') : {
                                'bpdu_sent': int,
                                'bpdu_recieved' : int,
                            }
                        }
                    },
                    Any() : { 
                        'domain': str,
                        'hello_time': int,
                        'max_age': int,
                        'forwarding_delay': int,
                        Optional('name'): str,
                        Optional('max_hop'): int,
                        Optional('hold_count'): int,
                    },
                }
            }
        }
    }


class ShowSpanningTreeMst(ShowSpanningTreeMstSchema):
    '''Parser for:
            show spanning-tree mst detail
    '''
    cli_command = 'show spanning-tree mst detail'

    def cli(self, output = None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
        p1_1 = re.compile(r'^##### MST(?P<mst_id>\d+) +\s+vlans\s+mapped: '
                          r'+\s+(?P<vlan>\w+\-\w+,\w+\-\w+)$')
            
        p2_1 = re.compile(r'^Bridge +\saddress\s+(?P<b_address>\w+\.\w+.\w+)'
                          r' +\spriority +\s(?P<b_priority>\d+)\s+\(\d+\s+sysid'
                          r'\s+(?P<b_sysid>\d+)\)$')

        p3_1 = re.compile(r'^Root +\s(?P<switch>\w+\s+\w+)\s+for\s+the\s+(?P<root>\w+)$')
        
        p3_2= re.compile(r'^Regional\s+Root\s(?P<switch>\w+\s+\w+)$')

        p4_1 = re.compile(r'^(?P<mst_domain>\w+) +\shello\s+time\s+'
                          r'(?P<hello_time>\d+),\s+forward\s+delay\s+'
                          r'(?P<forward_delay>\d+),\s+max\s+age\s+(?P<max_age>\d+), '
                          r'((txholdcount|max hops))\ *\s(?P<holdcount_or_maxhops>\d+)$')

        p5_1 = re.compile(r'^(?P<port_channel>\w+)\sof\s+\w+\s+is\s+(?P<port_state>\w+)\s+'
                          r'\(Bridge Assurance\s+(?P<bridge_assurance_inconsistent>\w+), '
                          r'VPC Peer-link\s+(?P<vpc_peer_link_inconsistent>\w+)$')

        p6_1 = re.compile(r'^Port\s+info +\sport\s+id +\s(?P<port_id>\d+\.*\d+)'
                          r' +\spriority +\s(?P<port_priority>\d+)'
                          r' +\scost +\s(?P<port_cost>\d+)$')
            
        p7_1 = re.compile(r'^Designated\s+root +\saddress\s+(?P<d_root_address>'
                          r'\w+\.\w+\.\w+) +\spriority +\s(?P<d_priority>\d+)'
                          r' +\scost +\s(?P<d_cost>\d+)$')

        p7_2 = re.compile(r'Design.\s+regional\s+root\s+address\s+(?P<designated_regional_root_address>\w+\.\w+\.\w+) '
                          r'+\spriority +\s(?P<designated_regional_root_priority>\d+) +\scost +\s(?P<designated_regional_root_cost>\d+)')

        p8_1 = re.compile(r'^Designated\s+bridge +\saddress\s+(?P<d_bridge_address>'
                          r'\w+\.\w+\.\w+) +\spriority +\s(?P<d_bridge_priority>\d+)'
                          r' +\sport\s+id\s+(?P<d_bridge_port_id>\d+(\.\d+)*)$')
            
        p9_1 = re.compile(r'^Timers\:\s+message\s+expires\s+in\s+'
                          r'(?P<message_expires_in>\d+)\s+sec,\s+forward'
                          r'\s+delay\s+(?P<forward_delay>\d+),\s+forward'
                          r'\s+transitions\s+(?P<forward_transitions>\d+)$')

        p10_1 = re.compile(r'^Bpdus\s+sent\s+(?P<bpdus_sent>\d+),'
                           r'\s+received\s+(?P<bpdus_received>\d+)$')

        for line in out.splitlines():
            line = line.strip()


            ##### MST0    vlans mapped:   1-399,501-4094
            m = p1_1.match(line)
            if m:
                mst_id = m.groupdict()['mst_id']
                instances_dict = ret_dict.setdefault('mstp', {}).setdefault('mst_intances', {})\
                    .setdefault(int(mst_id), {})
                instances_dict['mst_id'] = int(mst_id)
                instances_dict['vlans_mapped'] = m.groupdict()['vlan']
                continue

            # Bridge        address 0023.04ff.ad03  priority      32768 (32768 sysid 0) 
            m = p2_1.match(line)
            if m:
                instances_dict['bridge_address'] = m.groupdict()['b_address']
                instances_dict['bridge_priority'] = int(m.groupdict()['b_priority'])
                instances_dict['sys_id'] = int(m.groupdict()['b_sysid'])
                continue

            # Root          this switch for the CIST
            m = p3_1.match(line)
            if m:
                instances_dict['root_for_cist'] = m.groupdict()['switch']
                continue

            # Regional Root this switch
            m = p3_2.match(line)
            if m:
                instances_dict['regional_root'] = m.groupdict()['switch']
                continue

            # Operational   hello time 10, forward delay 30, max age 40, txholdcount 6 
            # Configured    hello time 10, forward delay 30, max age 40, max hops    255
            m = p4_1.match(line)
            if m:
                domain = m.groupdict()['mst_domain']
                domain_dict = instances_dict.setdefault(domain.lower(), {})
                domain_dict['domain'] = domain.lower()
                domain_dict['hello_time'] = int(m.groupdict()['hello_time'])
                domain_dict['forwarding_delay'] = int(m.groupdict()['forward_delay'])
                domain_dict['max_age'] = int(m.groupdict()['max_age'])

                if 'txholdcount' in line:
                    domain_dict['hold_count'] = int(m.groupdict()['holdcount_or_maxhops'])
                elif 'max hops' in line:
                    domain_dict['max_hop'] = int(m.groupdict()['holdcount_or_maxhops'])
                continue

            # Po30 of MST0 is broken (Bridge Assurance Inconsistent, VPC Peer-link Inconsistent)str
            m = p5_1.match(line)
            if m:
                intf = Common.convert_intf_name(m.groupdict()['port_channel'])
                intf_dict = instances_dict.setdefault('interfaces', {}).setdefault(intf, {})
                intf_dict['name'] = intf
                intf_dict['port_state'] = m.groupdict()['port_state']

                bridge_consistency = True if 'inconsistent' in m.groupdict()['bridge_assurance_inconsistent'].lower() else False
                intf_dict['bridge_assurance_inconsistent'] = bridge_consistency
                bridge_consistency = True if 'inconsisten' in m.groupdict()['vpc_peer_link_inconsistent'].lower() else False
                intf_dict['vpc_peer_link_inconsistent'] = bridge_consistency

                continue

            # Port info             port id       128.4125  priority    128  cost   500      
            m = p6_1.match(line)
            if m:
                intf_dict['port_id'] = m.groupdict()['port_id']
                intf_dict['port_priority'] = int(m.groupdict()['port_priority'])
                intf_dict['port_cost'] = int(m.groupdict()['port_cost'])
                continue

            # Designated root       address 0023.04ff.ad03  priority  32768  cost   0        
            m = p7_1.match(line)
            if m:
                intf_dict['designated_root_address'] = m.groupdict()['d_root_address']
                intf_dict['designated_root_priority'] = int(m.groupdict()['d_priority'])
                intf_dict['designated_root_cost'] = int(m.groupdict()['d_cost'])
                continue

            m = p7_2.match(line)
            if m:
                intf_dict['designated_regional_root_address'] = m.groupdict()['designated_regional_root_address']
                intf_dict['designated_regional_root_priority'] = int(m.groupdict()['designated_regional_root_priority'])
                intf_dict['designated_regional_root_cost'] = int(m.groupdict()['designated_regional_root_cost'])
                continue

            # Designated bridge     address 4055.39ff.fee7  priority  61440  port id 128.4125
            m = p8_1.match(line)
            if m:
                intf_dict['designated_bridge_address'] = m.groupdict()['d_bridge_address']
                intf_dict['designated_bridge_priority'] = int(m.groupdict()['d_bridge_priority'])
                intf_dict['designated_bridge_port_id'] = m.groupdict()['d_bridge_port_id']
                continue

            # Timers: message expires in 0 sec, forward delay 0, forward transitions 0
            m = p9_1.match(line)
            if m:
                timer_dict = intf_dict.setdefault('timers', {})
                group = m.groupdict()
                timer_dict.update({k: int(v) for k,v in group.items()})
                continue
            
            # Bpdus sent 113, received 0
            m = p10_1.match(line)
            if m:
                counters_dict = intf_dict.setdefault('counters', {})
                counters_dict['bpdu_sent'] = int(m.groupdict()['bpdus_sent'])
                counters_dict['bpdu_recieved'] = int(m.groupdict()['bpdus_received'])
                continue

        return ret_dict

#   ============================================    #
#                     summary                       #
#   ============================================    #

class ShowSpanningTreeSummarySchema(MetaParser):
    '''Schema for:
            show spanning-tree summary
    '''

    schema = {
        Optional('root_bridge_for'): str,
        Optional('mst_type'): str,
        'port_type_default': bool,
        'bpdu_guard':bool,
        'bpdu_filter': bool,
        'bridge_assurance': bool,
        'loop_guard': bool,
        'path_cost_method': str,
        Optional('pvst_simulation'): bool,
        Optional('vpc_peer_switch'): bool,
        Optional('vpc_peer_switch_status'): str,
        'stp_lite': bool,
        Optional('portfast_default'): bool,
        Optional('uplink_fast'): bool,
        Optional('backbone_fast'): bool,
        'mode': {
            Any() : {
                Any() : {
                'blocking':int,
                'listening': int,
                'learning': int,
                'forwarding': int,
                'stp_active': int,
                },
            },
        },
        Optional('total_statistics'): {
            'blockings': int,
            'listenings': int,
            'learnings': int,
            'forwardings': int,
            'stp_actives': int,
            Optional('num_of_msts'): int,
            Optional('num_of_vlans'):int,
        },
    }

class ShowSpanningTreeSummary(ShowSpanningTreeSummarySchema):
    '''Parser class for:
            show spanning-tree summary
    '''

    cli_command = 'show spanning-tree summary'

    def cli(self, output = None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        p1 = re.compile(r'^Switch +is +in +(?P<mode>[\S]+) +mode(?: +\((?P<mst_type>[\w\s]+)\))?$')
        p2 = re.compile(r'^Root +bridge +for: +(?P<root_bridge_for>[\S, ]+)$')
        p3 = re.compile(r'^Port +Type +Default\s+is +(?P<port_type_default>\w+)$')
        p4 = re.compile(r'^Edge\s+Port\s+\[PortFast\]\s+BPDU\s+(?P<port_type>\w+)'
                        r'\s+Default\s+is\s+(?P<bpdu_bool>\w+)$')
        p5 = re.compile(r'^Bridge +Assurance\s+is +(?P<bridge_assurance>\w+)$')
        p6 = re.compile(r'^Loopguard +Default\s+is +(?P<loop_guard>\w+)$')
        p7 = re.compile(r'^(?:Configured +)?Pathcost +method +used\s+is '
                        r'+(?P<path_cost_method>\w+)(?: +\(Operational +value +is +(?P<operational_value>\w+)\))?$')
        p8 = re.compile(r'^PVST\s+Simulation +\s+is\s+(?P<pvst_simulation>\w+)$')
        p9 = re.compile(r'^vPC +peer-switch\s+is +(?P<vpc_peer_switch>\w+)(?: +\((?P<vpc_peer_switch_status>[\S]+)?\))$')
        p10 = re.compile(r'^STP-Lite\s+is +(?P<stp_lite>\w+)$')
        p11 = re.compile(r'^(?P<mode_name>\w+) *\s+(?P<blocking>\d+) '
                         r'*\s+(?P<listening>\d+) *\s+(?P<learning>\d+) '
                         r'*\s+(?P<forwarding>\d+) *\s+(?P<stp_active>\d+)$')
        p12 = re.compile(r'^\d+\s+\w+ *\s+(?P<blockings>\d+) '
                         r'*\s+(?P<listenings>\d+) *\s+(?P<learnings>\d+) '
                         r'*\s+(?P<forwardings>\d+) *\s+(?P<stp_actives>\d+)$')

        p13 = re.compile(r'^(?P<root_bridge_for>(?:(?:[\w-]+, +)+)?[\w-]+)$')

        for line in out.splitlines():
            line = line.strip()

            # Switch is in rapid-pvst mode
            # Switch is in mst mode (IEEE Standard)
            m = p1.match(line)
            if m:
                mode = m.groupdict()['mode']
                mode_dict = ret_dict.setdefault('mode', {}).setdefault(mode, {})
                if m.groupdict()['mst_type']:
                    ret_dict['mst_type'] = m.groupdict()['mst_type']

                continue

            # Root bridge for: MST0000
            # Root bridge for: VLAN0002
            # Root bridge for: VLAN0109-VLAN0110, VLAN0122, VLAN0202-VLAN0205
            m = p2.match(line)
            if m:
                ret_dict['root_bridge_for'] = m.groupdict()['root_bridge_for']
                continue

            # VLAN0207-VLAN0209, VLAN0212-VLAN0215, VLAN0222-VLAN0224, VLAN0232-VLAN0234
            # VLAN0242, VLAN0244, VLAN0253-VLAN0254, VLAN0264, VLAN0274, VLAN0280-VLAN028
            m = p13.match(line)
            if m:
                ret_dict['root_bridge_for'] += ', {}'.format(m.groupdict()['root_bridge_for'])
                continue

            # Port Type Default                        is disable
            m = p3.match(line)
            if m:
                availability = True if 'enabled' in line.lower() else False
                ret_dict['port_type_default'] = availability
                continue

            # Edge Port [PortFast] BPDU Guard Default  is disabled
            # Edge Port [PortFast] BPDU Filter Default is disabled
            m = p4.match(line)
            if m:
                bpdu_type = m.groupdict()['bpdu_bool'].lower()
                if 'guard' in line.lower():
                    availability = True if 'enabled' in bpdu_type else False
                    ret_dict['bpdu_guard'] = availability
            
                bpdu_type = m.groupdict()['bpdu_bool'].lower()
                if 'filter' in line.lower():
                    availability = True if 'enabled' in bpdu_type else False
                    ret_dict['bpdu_filter'] = availability
                continue

            # Bridge Assurance                         is enabled
            m = p5.match(line)
            if m:
                bridge_assurance = m.groupdict()['bridge_assurance']
                availability = True if 'enabled' in bridge_assurance else False
                ret_dict['bridge_assurance'] = availability
                continue

            # Loopguard Default                        is disabled
            m = p6.match(line)
            if m:
                loop_guard = m.groupdict()['loop_guard']
                availability = True if 'enabled' in loop_guard else False
                ret_dict['loop_guard'] = availability
                continue

            # Configured Pathcost method used is short (Operational value is long)
            # Pathcost method used                     is short
            m = p7.match(line)
            if m:
                ret_dict['path_cost_method'] = m.groupdict()['path_cost_method']
                continue

            # PVST Simulation              is enabled
            # PVST Simulation Default                 is enabled but inactive in rapid-pvst mode
            m = p8.match(line)
            if m:
                pvst_simulation = m.groupdict()['pvst_simulation']
                availability = True if 'enabled' in line else False
                ret_dict['pvst_simulation'] = availability
                continue

            # vPC peer-switch                          is enabled (non-operational)
            # vPC peer-switch                          is enabled (operational)
            m = p9.match(line)
            if m:
                availability = True if 'enabled' in line else False
                ret_dict['vpc_peer_switch'] = availability
                ret_dict['vpc_peer_switch_status'] = m.groupdict()['vpc_peer_switch_status']
                continue

            # STP-Lite                                 is enabled
            m = p10.match(line)
            if m:
                stp_lite = m.groupdict()['stp_lite']
                availability = True if 'enabled' in line else False
                ret_dict['stp_lite'] = availability
                continue

            # VLAN0109                     0         0        0          3          3
            # VLAN0110                     0         0        0          2          2
            m = p11.match(line)
            if m:
                mode_name_dict = mode_dict.setdefault(m.groupdict()['mode_name'], {})
                group = m.groupdict()
                mode_name_dict.update({k: int(v) for k,v in group.items() if 'mode_name' not in k})
                continue

            # 1 mst                        1         0        0          0          1   
            m = p12.match(line)
            if m:
                stats_dict = ret_dict.setdefault('total_statistics', {})
                group = m.groupdict()
                stats_dict.update({k: int(v) for k, v in group.items()})
                continue

        return ret_dict


#   ============================================    #
#                      detail                       #
#   ============================================    #



class ShowSpanningTreeDetailSchema(MetaParser):
    '''Schema for:
            show spanning-tree detail
    '''
    schema = {
        Any(): {     # mstp, pvst, rapid_pvst
            Optional('domain'): str,
            Optional('pvst_id'): str,
            Optional('name'): str,
            Optional('revision'): int,
            Optional('max_hop'): int,
            'hello_time': int,
            Optional('fex_hello_time'): int,
            'max_age': int,
            'forwarding_delay': int,
            Optional('hold_count'): int,
            Any(): {   # mst_instances, vlans
                Any(): {
                    'bridge_priority': int,
                    'bridge_sysid': int,
                    'bridge_address': str,
                    'topology_change_flag': bool,
                    'topology_detected_flag': bool,
                    'topology_changes': int,
                    'time_since_topology_change': str,
                    'times': {
                        'hold': int,
                        'topology_change': int,
                        'notification': int,
                        'max_age': int,
                        'hello': int,
                        'forwarding_delay': int,
                    },
                    'timers' : {
                        'hello': int,
                        'topology_change': int,
                        'notification': int,
                    },
                    Optional('mst_id'): int,
                    Optional('vlan'): str,
                    Optional('vlan_id'): int,
                    Optional('root_of_the_spanning_tree'): bool,
                    Optional('topology_from_port'): str,
                    Optional('aging_timer'): int,
                    'interfaces': {
                        Any(): {
                            'status': str,
                            'name': str,
                            Optional('bridge_assurance_inconsistent'): bool,
                            Optional('vpc_peer_link_inconsistent'): bool,
                            Optional('topology_change'): bool,
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
                            'timers' : {
                                'message_age': int,
                                'forward_delay': int,
                                'hold': int,
                            },
                            Optional('port_type'): str,
                            'link_type': str,
                            Optional('internal'): bool,
                            Optional('peer_type'): str,
                            Optional('root_guard'): bool,
                            Optional('pvst_simulation'): bool,
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
    '''Parser for:
            show spanning-tree detail
    '''
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

    def cli(self, output = None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        p1 = re.compile(r'^(MST|VLAN)?(?P<inst>\w+)\s+is\s+executing\s'
                        r'+the\s+(?P<mode>\w+)\s+compatible\s+Spanning\s+'
                        r'Tree\s+protocol$')

        # Bridge Identifier has priority 12345, sysid 0, address aa00.aaff.aa00
        p2 = re.compile(r'^Bridge\s+Identifier\s+has\s+priority\s+'
                        r'(?P<bridge_priority>\d+),\s+sysid\s+'
                        r'(?P<bridge_sysid>\d+),\s+address\s+'
                        r'(?P<bridge_address>\w+\.\w+\.\w+)$')

        p3 = re.compile(r'^Configured\s+hello\s+time\s+(?P<hello_time>\d+)'
                        r'(?:, +fex +hello +time +(?P<fex_hello_time>\d+))?'
                        r',\s+max\s+age\s+(?P<max_age>\d+),\s+forward\s+delay'
                        r'\s+(?P<forwarding_delay>\d+)$')

        p3_1 = re.compile(r'^We\s+(?P<root_of_the_spanning_tree>\w+[\'\w+]*)\s+the\s+'
                          r'root\s+of\s+the\s+spanning\s+tree$')

        p4 = re.compile(r'^Topology\s+change\s+flag\s+(?P<topology_change_flag>'
                        r'[\w\s]+),\s+detected\s+flag\s+(?P<topology_detected_flag>[\w\s]+)$')

        p5 = re.compile(r'^Number\s+of\s+topology\s+changes\s+(?P<topology_changes>\d+)'
                        r'\s+last\s+change\s+occurred\s+(?P<time_since_topology_change>'
                        r'[\w\.\:]+)(\s+ago)?$')

        p6 = re.compile(r'^Times\:\s+hold\s+(?P<hold>\d+),\s+topology'
                        r'\s+change\s+(?P<topology_change>\d+),'
                        r'\s+notification\s+(?P<notification>\d+)$')

        p7 = re.compile(r'^hello +(?P<hello>\d+), +max +age +(?P<max_age>\d+),'
                        r' +forward +delay +(?P<forwarding_delay>[\d]+)')

        p8 = re.compile(r'^Timers:\s+hello\s+(?P<hello>\d+),'
                        r'\s+topology\s+change\s+(?P<topology_change>\d+)'
                        r',\s+notification\s+(?P<notification>\d+)'
                        r'(,\s+aging\s+(?P<aging>\d+))?$')

        p9 = re.compile(r'^Port +(?P<port_num>\d+) +\((?P<name>[\S]+)'
                        r'(?:(, +[\w\s\-]+))?\) +of +(?P<inst>\w+) +is +(?P<status>\w+)')

        p9_1 = re.compile(r'^ce (?P<bridge_assurance_inconsistent>\w+)\,\s+VPC\sPeer'
                          r'\-link\s+(?P<vpc_peer_link_inconsistent>\w+)\)$')

        p10 = re.compile(r'^Port\s+path\s+cost\s+(?P<cost>\d+),'
                         r'\s+Port\s+priority\s+(?P<port_priority>\d+),'
                         r'\s+Port\s+Identifier\s+(?P<port_identifier>[\w\.]+)$')

        p11 = re.compile(r'Designated\s+root\s+has\s+priority\s+'
                         r'(?P<designated_root_priority>\d+),'
                         r'\s+address\s+(?P<designated_root_address>[\w\.]+)')

        p12 = re.compile(r'^Designated\s+bridge\s+has\s+priority\s+'
                         r'(?P<designated_bridge_priority>\d+),\s+'
                         r'address\s+(?P<designated_bridge_address>[\w\.]+)$')

        p13 = re.compile(r'^Designated\s+port\s+id\s+is\s+'
                         r'(?P<designated_port_id>[\w\.]+),\s+designated'
                         r'\s+path\s+cost\s+(?P<designated_path_cost>\d+)'
                         r'(, +(?P<topology_change>Topology +change +is +set))?$')

        p14 = re.compile(r'^Timers:\s+message\s+age\s+(?P<message_age>\-?\d+),'
                         r'\s+forward\s+delay\s+(?P<forward_delay>\d+),'
                         r'\s+hold\s+(?P<hold>\d+)$')

        p15 = re.compile(r'^Number\s+of\s+transitions\s+to\s+forwarding'
                         r'\s+state:\s+(?P<number_of_forward_transitions>\d+)$')

        p15_1 = re.compile(r'^The +port +type +is +(?P<port_type>[\S]+)$')

        p16 = re.compile(r'^Link +type +is +(?P<link_type>[\w\-]+) ?(by default)?'
                         r',? ?(?P<internal>[I|i]nternal)?'
                         r',? ?(Peer is (?P<peer_type>\S+))?$')

        p17 = re.compile(r'^PVST\s+Simulation\s+is\s+'
                         r'(?P<pvst_simulation>\w+)\s+by\s+default$')

        p18 = re.compile(r'^BPDU:\s+sent\s+(?P<bpdu_sent>\d+),'
                         r'\s+received\s+(?P<bpdu_received>\d+)$')

        p19 = re.compile(r'^from +(?P<topology_from_port>[\w\.\/\-]+)$')

        p20 = re.compile(r'^Root +guard +is (?P<root_guard>\S+)$')

        for line in out.splitlines():
            line = line.strip()


        #  MST0000 is executing the mstp compatible Spanning Tree protocol
        # VLAN0109 is executing the rstp compatible Spanning Tree protocol
            m = p1.match(line)
            if m:
                group = m.groupdict()
                mode = group['mode']
                domain_dict = ret_dict.setdefault(self.MODE_NAME_MAP[mode], {})
                inst_dict = domain_dict.setdefault(self.MODE_INST_MAP[mode], {}).\
                    setdefault(int(group['inst']), {})
                inst_dict[self.MODE_KEY_MAP[mode]] = int(group['inst'])
                continue

            #   Bridge Identifier has priority 32768, sysid 0, address 0023.04ff.ad03
            m = p2.match(line)
            if m:
                group = m.groupdict()
                inst_dict['bridge_address'] = group.pop('bridge_address')
                inst_dict.update({k:int(v) for k, v in group.items()})
                continue

            #   Configured hello time 10, max age 40, forward delay 30
            #   Configured hello time 10, fex hello time 10, max age 40, forward delay 30
            m = p3.match(line)
            if m:
                group = m.groupdict()
                domain_dict.update({k: int(v) for k, v in group.items() if v})
                continue

            # We are the root of the spanning tree
            m = p3_1.match(line)
            if m:
                root_bool = True if m.groupdict()['root_of_the_spanning_tree'] == 'are' else False
                inst_dict['root_of_the_spanning_tree'] = root_bool
                continue

            # Topology change flag not set, detected flag not set
            m = p4.match(line)
            if m:
                availability = False if 'topology change flag not set' in line.lower() else True
                inst_dict['topology_change_flag'] =  availability
                availability = False if 'detected flag not set' in line.lower() else True
                inst_dict['topology_detected_flag'] = availability
                continue

            # Number of topology changes 0 last change occurred 142:22:13 ago
            m = p5.match(line)
            if m:
                inst_dict['topology_changes']  = int(m.groupdict()['topology_changes'])
                inst_dict['time_since_topology_change'] = m.groupdict()['time_since_topology_change']
                continue

            #       from Port-channel24
            m = p19.match(line)
            if m:
                inst_dict['topology_from_port'] = m.groupdict()['topology_from_port']
                continue

            # Times:  hold 1, topology change 70, notification 10
            m = p6.match(line)
            if m:
                time_dict = inst_dict.setdefault('times', {})
                time_dict['hold'] = int(m.groupdict()['hold'])
                time_dict['topology_change'] = int(m.groupdict()['topology_change'])
                time_dict['notification'] = int(m.groupdict()['notification'])
                continue

            # hello 10, max age 40, forward delay 30
            m = p7.match(line)
            if m:
                time_dict['hello'] = int(m.groupdict()['hello'])
                time_dict['max_age'] = int(m.groupdict()['max_age'])
                time_dict['forwarding_delay'] = int(m.groupdict()['forwarding_delay'])
                continue

            # Timers: hello 0, topology change 0, notification 0
            m = p8.match(line)
            if m:
                timer_dict = inst_dict.setdefault('timers', {})
                timer_dict['hello'] = int(m.groupdict()['hello'])
                timer_dict['topology_change'] = int(m.groupdict()['topology_change'])
                timer_dict['notification'] = int(m.groupdict()['notification'])
                continue

            # Port 4125 (port-channel30, vPC Peer-link) of MST0000 is broken
            m = p9.match(line)
            if m:
                port_name = Common.convert_intf_name(m.groupdict()['name'])
                intf_dict = inst_dict.setdefault('interfaces', {}).setdefault(port_name, {})
                intf_dict['name'] = port_name
                intf_dict['port_num'] = int(m.groupdict()['port_num'])
                intf_dict['status'] = m.groupdict()['status']
                continue

            #ce Inconsistent, VPC Peer-link Inconsistent)
            m = p9_1.match(line)
            if m:
                consistency_bool = True if 'inconsistent' in m.groupdict()\
                                            ['bridge_assurance_inconsistent'].lower() else False
                intf_dict['bridge_assurance_inconsistent'] = consistency_bool
                consistency_bool = True if 'inconsistent' in m.groupdict()\
                                            ['vpc_peer_link_inconsistent'].lower() else False
                intf_dict['vpc_peer_link_inconsistent'] = consistency_bool
                continue

            # Port path cost 500, Port priority 128, Port Identifier 128.4125
            m = p10.match(line)
            if m:
                intf_dict['cost'] = int(m.groupdict()['cost'])
                intf_dict['port_priority'] = int(m.groupdict()['port_priority'])
                intf_dict['port_identifier'] = m.groupdict()['port_identifier']
                continue

            # Designated root has priority 32768, address 0023.04ff.ad03
            m = p11.match(line)
            if m:
                intf_dict['designated_root_priority'] = int(m.groupdict()['designated_root_priority'])
                intf_dict['designated_root_address'] = m.groupdict()['designated_root_address']
                continue

            # Designated bridge has priority 61440, address 4055.3926.d8c
            m = p12.match(line)
            if m:
                intf_dict['designated_bridge_priority'] = int(m.groupdict()['designated_bridge_priority'])
                intf_dict['designated_bridge_address'] = m.groupdict()['designated_bridge_address']
                continue

            # Designated port id is 128.4125, designated path cost 0
            m = p13.match(line)
            if m:
                intf_dict['designated_port_id'] = m.groupdict()['designated_port_id']
                intf_dict['designated_path_cost'] = int(m.groupdict()['designated_path_cost'])
                if m.groupdict()['topology_change']:
                    intf_dict['topology_change'] = True
                continue

            # Timers: message age 0, forward delay 0, hold 0
            # Timers: message age -38, forward delay 0, hold 0
            m = p14.match(line)
            if m:
                timers_dict = intf_dict.setdefault('timers', {})
                timers_dict['message_age'] = int(m.groupdict()['message_age'])
                timers_dict['forward_delay'] = int(m.groupdict()['forward_delay'])
                timers_dict['hold'] = int(m.groupdict()['hold'])
                continue

            # Number of transitions to forwarding state: 0
            m = p15.match(line)
            if m:
                intf_dict['number_of_forward_transitions'] = int(m.groupdict()\
                    ['number_of_forward_transitions'])
                continue

            # The port type is network
            m = p15_1.match(line)
            if m:
                intf_dict['port_type'] = m.groupdict()['port_type']
                continue

            # Link type is point-to-point by default
            # Link type is point-to-point by default, Internal
            m = p16.match(line)
            if m:
                intf_dict['link_type'] = m.groupdict()['link_type']
                if m.groupdict()['internal'] == None:
                    internal_bool = False
                else:
                    internal_bool = True

                intf_dict['internal'] = internal_bool

                if m.groupdict()['peer_type']:
                    peer_type = m.groupdict()['peer_type']
                    intf_dict['peer_type'] = peer_type
                continue

            # Root guard is enabled
            m = p20.match(line)
            if m:
                group = m.groupdict()
                intf_dict['root_guard'] = True if 'enabled' in m.groupdict()['root_guard'].lower() \
                    else False
                continue

            # PVST Simulation is enabled by default
            m = p17.match(line)
            if m:
                availability = True if 'enabled' in line.lower() else False
                intf_dict['pvst_simulation'] = availability
                continue

            # BPDU: sent 110, received 0
            m = p18.match(line)
            if m:
                counters_dict = intf_dict.setdefault('counters', {})
                counters_dict['bpdu_sent'] = int(m.groupdict()['bpdu_sent'])
                counters_dict['bpdu_received'] = int(m.groupdict()['bpdu_received'])
                continue

        return ret_dict


class ShowErrdisableRecoverySchema(MetaParser):
    """Schema for show errdisable recovery"""
    schema = {
        'errdisable_reason': {
            Any(): bool,
        },
        'timer_interval': int,
    }


class ShowErrdisableRecovery(ShowErrdisableRecoverySchema):
    """Parser for show errdisable recovery"""

    cli_command = ['show errdisable recovery']

    def cli(self, output=None):
        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # initial return dictionary
        ret_dict = {}


        # link-flap                       disabled
        # udld                            disabled
        # CMM miscabling                  disabled
        p1 = re.compile(r'^(?P<name>[\w\s\-]+) '
                        r'+(?P<status>[D|d]isabled|[e|E]nabled)$')
        # Timer interval: 300
        p2 = re.compile(r'^Timer +interval\: +(?P<interval>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # link-flap                       disabled
            # udld                            disabled
            # CMM miscabling                  disabled
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                name = group['name'].strip()
                status = group['status'].lower()
                status_dict = ret_dict.setdefault('errdisable_reason', {})
                status_dict[name] = False if 'disabled' in status else True
                continue

            # Timer interval: 300
            m2 = p2.match(line)
            if m2:
                ret_dict['timer_interval'] = int(m2.groupdict()['interval'])

                continue

        return ret_dict

class ShowSpanningTreeIssuImpactSchema(MetaParser):
    """Schema for show spanning-tree issu-impact"""
    schema = {
        'criteria1': {
            'value': str,
            'status': str,
        },
        'criteria2': {
            'value': str,
            'status': str,
        },
        'criteria3': {
            'value': str,
            'status': str,
            Optional('non_edge_port'): {
                Any(): {
                    'vlan': int,
                    'role': str,
                    'sts': str,
                    'tree_type': str,
                    'instance': str,
                },
            },
        },
        'issu_proceed_status': str
    }

class ShowSpanningTreeIssuImpact(ShowSpanningTreeIssuImpactSchema):
    """Schema for show spanning-tree issu-impact."""

    cli_command = [
        'show spanning-tree issu-impact'
    ]

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0])

        parsed_dict = {}

        # 1. No Topology change must be active in any STP instance
        p1_a = re.compile(r'^1. (?P<value1>No Topology change must be active in any STP instance)$')

        # Criteria 1 PASSED !!
        p1_b = re.compile(r'^Criteria 1 (?P<status1>[\w]+)')

        # 2. Bridge assurance(BA) should not be active on any port (except MCT)
        p2_a = re.compile(r'^2. (?P<value2>Bridge assurance\(BA\) should not be active on any port).*$')

        # Criteria 2 PASSED !!
        p2_b = re.compile(r'^Criteria 2 (?P<status2>[\w]+)')

        # 3. There should not be any Non Edge Designated Forwarding port (except MCT)
        p3_a = re.compile(r'^3. (?P<value3>There should not be any Non Edge Designated Forwarding port).*$')

        # Criteria 3 FAILED
        p3_b = re.compile(r'^Criteria 3 (?P<status3>[\w]+)')

        # Ethernet1/21        1 Desg FWD  MST           0
        # Ethernet1/20        1 Desg FWD  MST           0
        p4 = re.compile(
            r'^(?P<port>[\w]+\/\d+)\s+(?P<vlan>[\d]+)\s+(?P<role>[\w]+)\s+(?P<sts>[\w]+)\s+(?P<tree_type>[\w]+)\s+(?P<instance>[\d]+)$')

        # ISSU Cannot Proceed! Change the above Config
        p5 = re.compile(r'^(?P<proceed>ISSU [\w\s]+).*$')

        for line in out.splitlines():
            line_strip = line.strip()
            m = p1_a.match(line_strip)
            if m:
                group = m.groupdict()
                criteria1 = parsed_dict.setdefault('criteria1', {})
                criteria1['value'] = group['value1']
                continue

            m = p1_b.match(line_strip)
            if m:
                group = m.groupdict()
                criteria1['status'] = group['status1']
                continue

            m = p2_a.match(line_strip)
            if m:
                group = m.groupdict()
                criteria2 = parsed_dict.setdefault('criteria2', {})
                criteria2['value'] = group['value2']
                continue

            m = p2_b.match(line_strip)
            if m:
                group = m.groupdict()
                criteria2['status'] = group['status2']
                continue

            m = p3_a.match(line_strip)
            if m:
                group = m.groupdict()
                criteria3 = parsed_dict.setdefault('criteria3', {})
                criteria3['value'] = group['value3']
                continue

            m = p3_b.match(line_strip)
            if m:
                group = m.groupdict()
                criteria3['status'] = group['status3']
                continue

            m = p4.match(line_strip)
            if m:
                group = m.groupdict()
                portedge = group['port']
                result_dict = criteria3.setdefault('non_edge_port', {}).setdefault(portedge, {})
                result_dict['vlan'] = int(group['vlan'])
                result_dict['role'] = group['role']
                result_dict['sts'] = group['sts']
                result_dict['tree_type'] = group['tree_type']
                result_dict['instance'] = group['instance']
                continue

            m = p5.match(line_strip)
            if m:
                group = m.groupdict()
                parsed_dict['issu_proceed_status'] = group['proceed']
                continue

        return parsed_dict

