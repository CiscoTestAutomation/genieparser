# -*- coding: utf-8 -*-
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

class ShowSpanningTreeMstSchema(MetaParser):
    '''Schema for:
            show show spanning tree mst details
    '''
    
    schema = {
        'mstp' : {
            'mst_intances': {
                Any() : { 
                    'mst_id' : int,
                    'vlan' : str,
                    'bridge_priority': int,
                    'bridge_address': str,
                    Optional('sys_id'): int,
                    Optional('root'): str,
                    Optional('hold_time'): int,
                    Optional('topology_changes'): int,
                    Optional('time_since_topology_change'): str,
                    'interfaces': {
                        Any () :{
                            'name': str,
                            'cost': int,
                            'port_priority' : int,
                            'port_num': float,
                            'port_state' : str,
                            Optional('designated_root_priority'): int,
                            Optional('designated_root_address'): str,
                            Optional('designated_cost'): int,
                            Optional('designated_bridge_priority'): int,
                            Optional('designated_bridge_address'): str,
                            Optional('designated_bridge_port_id'): str,
                            Optional('designated_port_num'): int,
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
                    }
                }
            },
            Any() : { 
                'domain': str,
                Optional('name'): str,
                Optional('max_hop'): int,
                Optional('hello_time'): int,
                Optional('max_age'): int,
                Optional('forwarding_delay'): int,
                Optional('hold_count'): int,
            }
        }
    }




class ShowSpanningTreeMst(ShowSpanningTreeMstSchema):
    '''Parser for:
            show spanning tree mst details
    '''
    cli_command = 'show spanning tree'

    def cli(self, output = None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = cli_command

        ret_dict = {}
        p1_1 = re.compile(r'##### MST(?P<mst_id>\d+)    '
            'vlans mapped:   (?P<vlan>\w+\-\w+,\w+\-\w+)')
            
        p2_1 = re.compile(r'Bridge        address '
            '(?P<b_address>\w+\.\w+.\w+)  priority      '
            '(?P<b_priority>\d+) .32768 sysid (?P<b_sysid>\d+).')

        p3_1 = re.compile(r'Root          this switch for the '
            '(?P<root>\w+)')

        p4_1 = re.compile(r'(?P<mst_domain>\w+)((   )|(    ))'
            'hello time (?P<hello_time>\d+), forward delay '
            '(?P<forward_delay>\d+), max age (?P<max_age>\d+), '
            '((txholdcount|max hops))(( )|(    ))'
            '(?P<holdcount_or_maxhops>\d+)')

        p5_1 = re.compile(r'(?P<port_channel>\w+) of \w+ is '
            '(?P<port_state>\w+)')

        p6_1 = re.compile(r'Port info             '
            'port id       (?P<port_id>\d+\.*\d+)  '
            'priority    (?P<port_priority>\d+)  '
            'cost   (?P<port_cost>\d+)')
            
        p7_1 = re.compile(r'Designated root       '
            'address (?P<d_root_address>\w+\.\w+\.\w+)  '
            'priority  (?P<d_priority>\d+)  cost   '
            '(?P<d_cost>\d+)')

        p8_1 = re.compile(r'Designated bridge     '
            'address (?P<d_bridge_address>\w+\.\w+\.\w+)  '
            'priority  (?P<d_bridge_priority>\d+)  '
            'port id (?P<d_bridge_port_id>\d+(\.\d+)*)')
            
        p9_1 = re.compile(r'Timers\: message expires in '
            '(?P<expire_message_time>\d+) sec, forward '
            'delay (?P<forward_delay>\d+), forward '
            'transitions (?P<forward_transitions>\d+)')

        p10_1 = re.compile(r'Bpdus sent (?P<bpdus_sent>\d+), '
            'received (?P<bpdus_received>\d+)')

        for line in out.splitlines():
            line = line.strip()


            ##### MST0    vlans mapped:   1-399,501-4094
            m = p1_1.match(line)
            if m:
                mst_id = m.groupdict()['mst_id']
                instances_dict = ret_dict.setdefault('mstp', {}).setdefault('mst_intances', {}).setdefault(int(mst_id), {})
                instances_dict.setdefault('mst_id', int(mst_id))
                instances_dict.setdefault('vlan', m.groupdict()['vlan'])
                continue

            # Bridge        address 0023.04ee.be14  priority      32768 (32768 sysid 0) 
            m = p2_1.match(line)
            if m:
                instances_dict.setdefault('bridge_address', m.groupdict()['b_address'])
                instances_dict.setdefault('bridge_priority', int(m.groupdict()['b_priority']))
                instances_dict.setdefault('sys_id', int(m.groupdict()['b_sysid']))
                continue

            # Root          this switch for the CIST
            m = p3_1.match(line)
            if m:
                instances_dict.setdefault('root', m.groupdict()['root'])
                continue

            # Operational   hello time 10, forward delay 30, max age 40, txholdcount 6 
            # Configured    hello time 10, forward delay 30, max age 40, max hops    255
            m = p4_1.match(line)
            if m:
                domain = m.groupdict()['mst_domain']
                domain_dict = ret_dict.setdefault('mstp', {}).setdefault(domain.lower(), {})
                domain_dict.setdefault('domain', domain.lower())
                domain_dict.setdefault('hello_time', int(m.groupdict()['hello_time']))
                domain_dict.setdefault('forwarding_delay', int(m.groupdict()['forward_delay']))
                domain_dict.setdefault('max_age', int(m.groupdict()['max_age']))
                if 'txholdcount' in line:
                    domain_dict.setdefault('hold_count', int(m.groupdict()['holdcount_or_maxhops']))
                elif 'max hops' in line:
                    domain_dict.setdefault('max_hop', int(m.groupdict()['holdcount_or_maxhops']))
                continue

            # Po30 of MST0 is broken (Bridge Assurance Inconsistent, VPC Peer-link Inconsistent)str
            m = p5_1.match(line)
            if m:
                intf = m.groupdict()['port_channel']
                intf_dict = instances_dict.setdefault('interfaces', {}).setdefault(intf, {})
                intf_dict.setdefault('name', m.groupdict()['port_channel'].lower())
                intf_dict.setdefault('port_state', m.groupdict()['port_state'])
                continue

            # Port info             port id       128.4125  priority    128  cost   500      
            m = p6_1.match(line)
            if m:
                intf_dict.setdefault('port_num', float(m.groupdict()['port_id']))
                intf_dict.setdefault('port_priority', int(m.groupdict()['port_priority']))
                intf_dict.setdefault('cost', int(m.groupdict()['port_cost']))
                continue

            # Designated root       address 0023.04ee.be14  priority  32768  cost   0        
            m = p7_1.match(line)
            if m:
                intf_dict.setdefault('designated_root_address', m.groupdict()['d_root_address'])
                intf_dict.setdefault('designated_root_priority', int(m.groupdict()['d_priority']))
                intf_dict.setdefault('designated_cost', int(m.groupdict()['d_cost']))
                continue

            # Designated bridge     address 4055.3926.d8c1  priority  61440  port id 128.4125
            m = p8_1.match(line)
            if m:
                intf_dict.setdefault('designated_bridge_address', m.groupdict()['d_bridge_address'])
                intf_dict.setdefault('designated_bridge_priority', int(m.groupdict()['d_bridge_priority']))
                intf_dict.setdefault('designated_bridge_port_id', m.groupdict()['d_bridge_port_id'])
                continue

            # Timers: message expires in 0 sec, forward delay 0, forward transitions 0
            m = p9_1.match(line)
            if m:
                timer_dict = intf_dict.setdefault('timers', {})
                timer_dict.setdefault('message_expires_in', int(m.groupdict()['expire_message_time']))
                timer_dict.setdefault('forward_delay', int(m.groupdict()['forward_delay']))
                timer_dict.setdefault('forward_transitions', int(m.groupdict()['forward_transitions']))
                continue
            
            # Bpdus sent 113, received 0
            m = p10_1.match(line)
            if m:
                counters_dict = intf_dict.setdefault('counters', {})
                counters_dict.setdefault('bpdu_sent', int(m.groupdict()['bpdus_sent']))
                counters_dict.setdefault('bpdu_recieved', int(m.groupdict()['bpdus_received']))
                continue

        return ret_dict