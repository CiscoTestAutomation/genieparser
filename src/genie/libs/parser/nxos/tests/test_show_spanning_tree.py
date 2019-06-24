#!/bin/env python
# -*- coding: utf-8 -*-
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError
from genie.libs.parser.nxos.show_spanning_tree import ShowSpanningTreeMst,\
                                                        ShowSpanningTreeSummary,\
                                                            ShowSpanningTreeDetail

class testShowSpanningTreeMst(unittest.TestCase):
    dev1 = Device(name = 'deviceA')
    dev2 = Device(name = 'deviceB')

    output_1 = {'execute.return_value' : 
        '''
           P1# show spanning-tree mst detail  

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
                        'vlans_mapped': '1-399,501-4094',
                        'bridge_address': '0023.04ee.be14',
                        'bridge_priority': 32768,
                        'sys_id': 0,
                        'root_for_cist' : 'this switch',
                        'regional_root': 'this switch',
                        'interfaces': {
                            'port-channel30': {
                                'name': 'port-channel30',
                                'port_state': 'broken',
                                'port_id': '128.4125',
                                'port_priority': 128,
                                'port_cost': 500,
                                'bridge_assurance_inconsistent': True,
                                'vpc_peer_link_inconsistent': True,
                                'designated_root_address': '0023.04ee.be14',
                                'designated_root_priority': 32768,
                                'designated_root_cost': 0,
                                'designated_regional_root_address': '0023.04ee.be14',
                                'designated_regional_root_priority': 32768,
                                'designated_regional_root_cost': 0,
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
            }
        }


    output_2 = {'execute.return_value' : 
        '''
            P1# show spanning-tree mst detail 

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
                        'vlans_mapped': '1-399,501-4094',
                        'bridge_address': '0023.04ee.be14',
                        'bridge_priority': 32768,
                        'sys_id': 0,
                        'root_for_cist' : 'this switch',
                        'interfaces': {
                            'port-channel25': {
                                'name': 'port-channel25',
                                'port_state': 'broken',
                                'port_id': '128.4125',
                                'port_priority': 128,
                                'port_cost': 500,
                                'bridge_assurance_inconsistent': True,
                                'vpc_peer_link_inconsistent': True,
                                'designated_root_address': '0023.04ee.be14',
                                'designated_root_priority': 32768,
                                'designated_root_cost': 0,
                                'designated_regional_root_address': '0023.04ee.be14',
                                'designated_regional_root_priority': 32768,
                                'designated_regional_root_cost': 0,
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


class testShowSpanningTreeSummary(unittest.TestCase):
    dev_c3850 = Device(name = 'deviceA')
    dev2 = Device(name = 'deviceB')

    golden_output_mstp = {'execute.return_value' : '''
        P1# show spanning-tree summary 

        Switch is in mst mode (IEEE Standard)
        Root bridge for: MST0000
        Port Type Default                        is disable
        Edge Port [PortFast] BPDU Guard Default  is disabled
        Edge Port [PortFast] BPDU Filter Default is disabled
        Bridge Assurance                         is enabled
        Loopguard Default                        is disabled
        Pathcost method used                     is long
        PVST Simulation                          is enabled
        vPC peer-switch                          is enabled (non-operational)
        STP-Lite                                 is enabled

        Name                   Blocking Listening Learning Forwarding STP Active
        ---------------------- -------- --------- -------- ---------- ----------
        MST0000                      1         0        0          0          1
        ---------------------- -------- --------- -------- ---------- ----------
        1 mst                        1         0        0          0          1
    '''}

    golden_parsed_output_mstp = {
        'mode': {
            'mst': {
                'MST0000': {
                    'blocking': 1,
                    'listening': 0,
                    'learning': 0,
                    'forwarding': 0,
                    'stp_active': 1
                }
            }
        },
        'root_bridge_for': 'MST0000',
        'mst_type': 'IEEE Standard',
        'port_type_default': False,
        'bpdu_guard': False,
        'bpdu_filter': False,
        'bridge_assurance': True,
        'loop_guard': False,
        'path_cost_method': 'long',
        'pvst_simulation': True,
        'vpc_peer_switch': True,
        'vpc_peer_switch_status': 'non-operational',
        'stp_lite': True,
        'total_statistics': {
            'blockings': 1,
            'listenings': 0,
            'learnings': 0,
            'forwardings': 0,
            'stp_actives': 1
        }
    }

    golden_output_mstp_2 = {'execute.return_value' : '''
        P1# show spanning-tree summary 

        Switch is in mst mode (IEEE Standard)
        Root bridge for: MST0000
        Port Type Default                        is disable
        Edge Port [PortFast] BPDU Guard Default  is enabled
        Edge Port [PortFast] BPDU Filter Default is enabled
        Bridge Assurance                         is enabled
        Loopguard Default                        is disabled
        Pathcost method used                     is long
        PVST Simulation                          is disabled
        vPC peer-switch                          is enabled (non-operational)
        STP-Lite                                 is enabled

        Name                   Blocking Listening Learning Forwarding STP Active
        ---------------------- -------- --------- -------- ---------- ----------
        MST0                         3         0        0          9         12
        MST100                       3         0        0          1          4
        ---------------------- -------- --------- -------- ---------- ----------
        1 mst                        1         0        0          0          1
    '''}

    golden_parsed_output_mstp_2 = {
        'mode': {
            'mst': {
                'MST0': {
                    'blocking': 3,
                    'listening': 0,
                    'learning': 0,
                    'forwarding': 9,
                    'stp_active': 12
                },
                'MST100': {
                    'blocking': 3,
                    'listening': 0,
                    'learning': 0,
                    'forwarding': 1,
                    'stp_active': 4
                }
            }
        },
        'root_bridge_for': 'MST0000',
        'mst_type': 'IEEE Standard',
        'port_type_default': False,
        'bpdu_guard': True,
        'bpdu_filter': True,
        'bridge_assurance': True,
        'loop_guard': False,
        'path_cost_method': 'long',
        'pvst_simulation': False,
        'vpc_peer_switch': True,
        'vpc_peer_switch_status': 'non-operational',
        'stp_lite': True,
        'total_statistics': {
            'blockings': 1,
            'listenings': 0,
            'learnings': 0,
            'forwardings': 0,
            'stp_actives': 1
        }
    }

    empty_output = {'execute.return_value': '       '}
    
    def test_empty(self):
        self.dev2 = Mock(**self.empty_output)
        obj = ShowSpanningTreeSummary(device=self.dev2)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_mst(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_mstp)
        obj = ShowSpanningTreeSummary(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_mstp)
    
    def test_golden_mst_2(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_mstp_2)
        obj = ShowSpanningTreeSummary(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_mstp_2)


class TestShowSpanningTreeDetail(unittest.TestCase):
    dev_c3850 = Device(name = 'c3850')
    dev2 = Device(name = 'empty')

    empty_output = {'execute.return_value' : '          '}

    golden_output_1 = {'execute.return_value': '''
        P1# show spanning-tree detail

         MST0000 is executing the mstp compatible Spanning Tree protocol
      Bridge Identifier has priority 32768, sysid 0, address 0023.04ee.be14
      Configured hello time 10, max age 40, forward delay 30
      We are the root of the spanning tree
      Topology change flag not set, detected flag not set
      Number of topology changes 0 last change occurred 142:22:13 ago
      Times:  hold 1, topology change 70, notification 10
              hello 10, max age 40, forward delay 30 
      Timers: hello 0, topology change 0, notification 0

     Port 4125 (port-channel30, vPC Peer-link) of MST0000 is broken  (Bridge Assuran
    ce Inconsistent, VPC Peer-link Inconsistent)
       Port path cost 500, Port priority 128, Port Identifier 128.4125
       Designated root has priority 32768, address 0023.04ee.be14
       Designated bridge has priority 61440, address 4055.3926.d8c1
       Designated port id is 128.4125, designated path cost 0
       Timers: message age 0, forward delay 0, hold 0
       Number of transitions to forwarding state: 0
       The port type is network
       Link type is point-to-point by default, Internal
       PVST Simulation is enabled by default
       BPDU: sent 110, received 0
        '''}

    golden_parsed_output_1 = {
        'mstp': {
            'mst_instances': {
                0: {
                    'mst_id': 0,
                    'bridge_priority': 32768,
                    'bridge_sysid': 0,
                    'bridge_address': '0023.04ee.be14',
                    'topology_change_flag': False,
                    'topology_detected_flag': False,
                    'topology_changes': 0,
                    'time_since_topology_change': '142:22:13',
                    'times': {
                        'hold': 1,
                        'topology_change': 70,
                        'notification': 10,
                        'max_age': 40,
                        'hello': 10,
                        'forwarding_delay': 30,
                    },
                    'timers' : {
                        'hello': 0,
                        'topology_change': 0,
                        'notification': 0,
                    },
                    'root_of_the_spanning_tree': True,
                    'interfaces': {
                        'port-channel30': {
                            'name': 'port-channel30',
                            'bridge_assurance_inconsistent': True,
                            'vpc_peer_link_inconsistent': True,
                            'port_num': 4125,
                            'status': 'broken',
                            'cost': 500,
                            'port_priority': 128,
                            'port_identifier': '128.4125',
                            'designated_root_priority': 32768,
                            'designated_root_address': '0023.04ee.be14',
                            'designated_bridge_priority': 61440,
                            'designated_bridge_address': '4055.3926.d8c1',
                            'designated_port_id': '128.4125',
                            'designated_path_cost': 0,
                            'timers': {
                                'message_age': 0,
                                'forward_delay': 0,
                                'hold': 0,
                            },
                            'port_type' : 'network',
                            'number_of_forward_transitions': 0,
                            'link_type': 'point-to-point',
                            'internal': True,
                            'pvst_simulation': True,
                            'counters': {
                                'bpdu_sent': 110,
                                'bpdu_received': 0
                            }
                        }
                    }
                }
            },
            'hello_time': 10,
            'max_age': 40,
            'forwarding_delay': 30
        }
    }
    
    golden_output_2 = {'execute.return_value' : '''
        P1# show spanning-tree detail

         MST0000 is executing the mstp compatible Spanning Tree protocol
      Bridge Identifier has priority 32768, sysid 0, address 0023.04ee.be14
      Configured hello time 10, max age 40, forward delay 30
      We are the root of the spanning tree
      Topology change flag not set, detected flag not set
      Number of topology changes 0 last change occurred 142:22:13 ago
      Times:  hold 1, topology change 70, notification 10
              hello 10, max age 40, forward delay 30 
      Timers: hello 0, topology change 0, notification 0

     Port 4125 (port-channel30, vPC Peer-link) of MST0000 is broken  (Bridge Assuran
    ce Inconsistent, VPC Peer-link Inconsistent)
       Port path cost 500, Port priority 128, Port Identifier 128.4125
       Designated root has priority 32768, address 0023.04ee.be14
       Designated bridge has priority 61440, address 4055.3926.d8c1
       Designated port id is 128.4125, designated path cost 0
       Timers: message age 0, forward delay 0, hold 0
       Number of transitions to forwarding state: 0
       The port type is network
       Link type is point-to-point by default, Internal
       PVST Simulation is enabled by default
       BPDU: sent 110, received 0

        Port 2390 (Port-channel14) of MST0 is broken   (Bridge Assuran
        ce Inconsistent, VPC Peer-link Inconsistent)
        Port path cost 6660, Port priority 128, Port Identifier 128.2390.
        Designated root has priority 32768, address d8b1.9009.bf80
        Designated bridge has priority 32768, address d8b1.9009.bf80
        Designated port id is 128.2390, designated path cost 0
        Timers: message age 0, forward delay 0, hold 0
        Number of transitions to forwarding state: 0
        The port type is network
        Link type is point-to-point by default, Internal
       PVST Simulation is enabled by default
        BPDU: sent 138231, received 167393
    '''}

    golden_parsed_output_2 = {
        'mstp': {
            'mst_instances': {
                0: {
                    'mst_id': 0,
                    'bridge_priority': 32768,
                    'bridge_sysid': 0,
                    'bridge_address': '0023.04ee.be14',
                    'topology_change_flag': False,
                    'topology_detected_flag': False,
                    'time_since_topology_change': '142:22:13',
                    'topology_changes': 0,
                    'times': {
                        'hold': 1,
                        'topology_change': 70,
                        'notification': 10,
                        'max_age': 40,
                        'hello': 10,
                        'forwarding_delay': 30,
                    },
                    'timers' : {
                        'hello': 0,
                        'topology_change': 0,
                        'notification': 0,
                    },
                    'root_of_the_spanning_tree': True,
                    'interfaces': {
                        'port-channel30': {
                            'name': 'port-channel30',
                            'bridge_assurance_inconsistent': True,
                            'vpc_peer_link_inconsistent': True,
                            'port_num': 4125,
                            'status': 'broken',
                            'cost': 500,
                            'port_priority': 128,
                            'port_identifier': '128.4125',
                            'designated_root_priority': 32768,
                            'designated_root_address': '0023.04ee.be14',
                            'designated_bridge_priority': 61440,
                            'designated_bridge_address': '4055.3926.d8c1',
                            'designated_port_id': '128.4125',
                            'designated_path_cost': 0,
                            'timers': {
                                'message_age': 0,
                                'forward_delay': 0,
                                'hold': 0,
                            },
                            'port_type' : 'network',
                            'number_of_forward_transitions': 0,
                            'link_type': 'point-to-point',
                            'internal': True,
                            'pvst_simulation': True,
                            'counters': {
                                'bpdu_sent': 110,
                                'bpdu_received': 0
                            }
                        },
                        'Port-channel14': {
                            'name': 'Port-channel14',
                            'bridge_assurance_inconsistent': True,
                            'vpc_peer_link_inconsistent': True,
                            'port_num': 2390,
                            'status': 'broken',
                            'cost': 6660,
                            'port_priority': 128,
                            'port_identifier': '128.2390.',
                            'designated_root_priority': 32768,
                            'designated_root_address': 'd8b1.9009.bf80',
                            'designated_bridge_priority': 32768,
                            'designated_bridge_address': 'd8b1.9009.bf80',
                            'designated_port_id': '128.2390',
                            'designated_path_cost': 0,
                            'timers': {
                                'message_age': 0,
                                'forward_delay': 0,
                                'hold': 0,
                            },
                            'port_type' : 'network',
                            'number_of_forward_transitions': 0,
                            'link_type': 'point-to-point',
                            'internal': True,
                            'pvst_simulation': True,
                            'counters': {
                                'bpdu_sent': 138231,
                                'bpdu_received': 167393
                            }
                        }
                    }
                }
            },
            'hello_time': 10,
            'max_age': 40,
            'forwarding_delay': 30
        }
    }

    def test_detail_output_1(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_1)
        obj = ShowSpanningTreeDetail(device = self.dev_c3850)
        parsed = obj.parse()
        self.assertEqual(parsed, self.golden_parsed_output_1)

    def test_detail_output_2(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_2)
        obj = ShowSpanningTreeDetail(device = self.dev_c3850)
        parsed = obj.parse()
        self.assertEqual(parsed, self.golden_parsed_output_2)


    def test_detail_output_empty(self):
        self.dev2 = Mock(**self.empty_output)
        obj = ShowSpanningTreeDetail(device = self.dev2)
        with self.assertRaises(SchemaEmptyParserError):
            parsed = obj.parse()
        

if __name__ == '__main__':
    unittest.main()