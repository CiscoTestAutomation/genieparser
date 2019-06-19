#!/bin/env python
# -*- coding: utf-8 -*-
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError
from genie.libs.parser.nxos.show_spanning_tree import ShowSpanningTreeMst

class test_Show_Spanning_Tree_details(unittest.TestCase):
    dev1 = Device(name = 'deviceA')
    dev2 = Device(name = 'deviceB')

    output_1 = {'execute.return_value' : 
        '''
                ##### MST0    vlans mapped:   1-399,501-4094
            Bridge        address 0023.04ee.be14  priority      32768 (32768 sysid 0)
            Root          this switch for the CIST
            Regional Root this switch
            Operational   hello time 10, forward delay 30, max age 40, txholdcount 6 
            Configured    hello time 10, forward delay 30, max age 40, max hops    255


            Po30 of MST0 is broken (Bridge Assurance Inconsistent, VPC Peer-link Inconsisten
            t)
            Port info             port id       128.4125  priority    128  cost   500      
            Designated root       address 0023.04ee.be14  priority  32768  cost   0        
            Design. regional root address 0023.04ee.be14  priority  32768  cost   0        
            Designated bridge     address 4055.3926.d8c1  priority  61440  port id 128.4125
            Timers: message expires in 0 sec, forward delay 0, forward transitions 0
            Bpdus sent 113, received 0
        '''}

    parsed_output_1 = {
            'mstp': {
                'mst_intances': {
                    0: {
                        'mst_id': 0,
                        'vlan': '1-399,501-4094',
                        'bridge_address': '0023.04ee.be14',
                        'bridge_priority': 32768,
                        'sys_id': 0,
                        'root': 'CIST',
                        'interfaces': {
                            'Po30': {
                                'name': 'po30',
                                'port_state': 'broken',
                                'port_num': 128.4125,
                                'port_priority': 128,
                                'cost': 500,
                                'designated_root_address': '0023.04ee.be14',
                                'designated_root_priority': 32768,
                                'designated_cost': 0,
                                'designated_bridge_address': '4055.3926.d8c1',
                                'designated_bridge_priority': 61440,
                                'designated_bridge_port_id': '128.4125',
                                'timers': {
                                    'message_expires_in': 0,
                                    'forward_delay': 0,
                                    'forward_transitions': 0
                                },
                                'counters': {
                                    'bpdu_sent': 113,
                                    'bpdu_recieved': 0
                                }
                            }
                        }
                    }
                },
                'operational': {
                    'domain': 'operational',
                    'hello_time': 10,
                    'forwarding_delay': 30,
                    'max_age': 40,
                    'hold_count': 6
                },
                'configured': {
                    'domain': 'configured',
                    'hello_time': 10,
                    'forwarding_delay': 30,
                    'max_age': 40,
                    'max_hop': 255
                }
            }
        }


    output_2 = {'execute.return_value' : 
        '''
                ##### MST0    vlans mapped:   1-399,501-4094
            Bridge        address 0023.04ee.be14  priority      32768 (32768 sysid 0)
            Root          this switch for the CIST
            Operational   hello time 5, forward delay 20, max age 30, txholdcount 12
            Configured    hello time 10, forward delay 30, max age 40, max hops    255


            Po25 of MST0 is broken (Bridge Assurance Inconsistent, VPC Peer-link Inconsisten
            t)
            Port info             port id       128.4125  priority    128  cost   500      
            Designated root       address 0023.04ee.be14  priority  32768  cost   0        
            Design. regional root address 0023.04ee.be14  priority  32768  cost   0        
            Designated bridge     address 4055.3926.d8c1  priority  61440  port id 128.4125
            Timers: message expires in 0 sec, forward delay 0, forward transitions 0
            Bpdus sent 113, received 0
        '''}

    parsed_output_2 = {
            'mstp': {
                'mst_intances': {
                    0: {
                        'mst_id': 0,
                        'vlan': '1-399,501-4094',
                        'bridge_address': '0023.04ee.be14',
                        'bridge_priority': 32768,
                        'sys_id': 0,
                        'root': 'CIST',
                        'interfaces': {
                            'Po25': {
                                'name': 'po25',
                                'port_state': 'broken',
                                'port_num': 128.4125,
                                'port_priority': 128,
                                'cost': 500,
                                'designated_root_address': '0023.04ee.be14',
                                'designated_root_priority': 32768,
                                'designated_cost': 0,
                                'designated_bridge_address': '4055.3926.d8c1',
                                'designated_bridge_priority': 61440,
                                'designated_bridge_port_id': '128.4125',
                                'timers': {
                                    'message_expires_in': 0,
                                    'forward_delay': 0,
                                    'forward_transitions': 0
                                },
                                'counters': {
                                    'bpdu_sent': 113,
                                    'bpdu_recieved': 0
                                }
                            }
                        }
                    }
                },
                'operational': {
                    'domain': 'operational',
                    'hello_time': 5,
                    'forwarding_delay': 20,
                    'max_age': 30,
                    'hold_count': 12
                },
                'configured': {
                    'domain': 'configured',
                    'hello_time': 10,
                    'forwarding_delay': 30,
                    'max_age': 40,
                    'max_hop': 255
                }
            }
        }
    
    empty_output = {'execute.return_value': '           '}

    def test_output_1(self):
        self.maxDiff = None
        self.dev1 = Mock(**self.output_1)
        obj = ShowSpanningTreeMst(device = self.dev1)
        parsed = obj.parse()
        self.assertEqual(parsed, self.parsed_output_1)
    
    def test_output_2(self):
        self.maxDiff = None
        self.dev1 = Mock(**self.output_2)
        obj = ShowSpanningTreeMst(device = self.dev1)
        parsed = obj.parse()
        self.assertEqual(parsed, self.parsed_output_2)

    def test_empty_output(self):
        self.dev2 = Mock(**self.empty_output)
        obj = ShowSpanningTreeMst(device = self.dev2)
        with self.assertRaises(SchemaEmptyParserError):
            parsed = obj.parse()


if __name__ == '__main__':
    unittest.main()