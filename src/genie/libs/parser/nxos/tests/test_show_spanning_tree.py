#!/bin/env python
# -*- coding: utf-8 -*-
import unittest
from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError
from genie.libs.parser.nxos.show_spanning_tree import (ShowSpanningTreeMst,
                                                      ShowSpanningTreeSummary,
                                                      ShowSpanningTreeDetail,
                                                      ShowErrdisableRecovery)

class TestShowSpanningTreeMst(unittest.TestCase):
    dev1 = Device(name = 'deviceA')
    dev2 = Device(name = 'deviceB')

    output_1 = {'execute.return_value' : 
        '''
           P1# show spanning-tree mst detail  

                ##### MST0    vlans mapped:   1-399,501-4094
            Bridge        address 0023.04ff.ad03  priority      32768 (32768 sysid 0)
            Root          this switch for the CIST
            Regional Root this switch
            Operational   hello time 10, forward delay 30, max age 40, txholdcount 6 
            Configured    hello time 10, forward delay 30, max age 40, max hops    255


            Po30 of MST0 is broken (Bridge Assurance Inconsistent, VPC Peer-link Inconsisten
            t)
            Port info             port id       128.4125  priority    128  cost   500      
            Designated root       address 0023.04ff.ad03  priority  32768  cost   0        
            Design. regional root address 0023.04ff.ad03  priority  32768  cost   0        
            Designated bridge     address 4055.39ff.fee7  priority  61440  port id 128.4125
            Timers: message expires in 0 sec, forward delay 0, forward transitions 0
            Bpdus sent 113, received 0
        '''}

    parsed_output_1 = {
            'mstp': {
                'mst_intances': {
                    0: {
                        'mst_id': 0,
                        'vlans_mapped': '1-399,501-4094',
                        'bridge_address': '0023.04ff.ad03',
                        'bridge_priority': 32768,
                        'sys_id': 0,
                        'root_for_cist' : 'this switch',
                        'regional_root': 'this switch',
                        'interfaces': {
                            'Port-channel30': {
                                'name': 'Port-channel30',
                                'port_state': 'broken',
                                'port_id': '128.4125',
                                'port_priority': 128,
                                'port_cost': 500,
                                'bridge_assurance_inconsistent': True,
                                'vpc_peer_link_inconsistent': True,
                                'designated_root_address': '0023.04ff.ad03',
                                'designated_root_priority': 32768,
                                'designated_root_cost': 0,
                                'designated_regional_root_address': '0023.04ff.ad03',
                                'designated_regional_root_priority': 32768,
                                'designated_regional_root_cost': 0,
                                'designated_bridge_address': '4055.39ff.fee7',
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

                ##### MST0    vlans mapped:   1-399,501-4094
            Bridge        address 0023.04ff.ad03  priority      32768 (32768 sysid 0)
            Root          this switch for the CIST
            Operational   hello time 5, forward delay 20, max age 30, txholdcount 12
            Configured    hello time 10, forward delay 30, max age 40, max hops    255


            Po25 of MST0 is broken (Bridge Assurance Inconsistent, VPC Peer-link Inconsisten
            t)
            Port info             port id       128.4125  priority    128  cost   500      
            Designated root       address 0023.04ff.ad03  priority  32768  cost   0        
            Design. regional root address 0023.04ff.ad03  priority  32768  cost   0        
            Designated bridge     address 4055.39ff.fee7  priority  61440  port id 128.4125
            Timers: message expires in 0 sec, forward delay 0, forward transitions 0
            Bpdus sent 113, received 0
        '''}

    parsed_output_2 = {
            'mstp': {
                'mst_intances': {
                    0: {
                        'mst_id': 0,
                        'vlans_mapped': '1-399,501-4094',
                        'bridge_address': '0023.04ff.ad03',
                        'bridge_priority': 32768,
                        'sys_id': 0,
                        'root_for_cist' : 'this switch',
                        'interfaces': {
                            'Port-channel25': {
                                'name': 'Port-channel25',
                                'port_state': 'broken',
                                'port_id': '128.4125',
                                'port_priority': 128,
                                'port_cost': 500,
                                'bridge_assurance_inconsistent': True,
                                'vpc_peer_link_inconsistent': True,
                                'designated_root_address': '0023.04ff.ad03',
                                'designated_root_priority': 32768,
                                'designated_root_cost': 0,
                                'designated_regional_root_address': '0023.04ff.ad03',
                                'designated_regional_root_priority': 32768,
                                'designated_regional_root_cost': 0,
                                'designated_bridge_address': '4055.39ff.fee7',
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


class TestShowSpanningTreeSummary(unittest.TestCase):
    dev_c3850 = Device(name = 'deviceA')
    dev2 = Device(name = 'deviceB')

    golden_output_mstp = {'execute.return_value' : '''
        P1# show spanning-tree summary 

        Switch is in mst mode (IEEE Standard)
        Root bridge for: MST0000
        Port Type Default                        is disable
        Edge Port [PortFast] BPDU Guard Default  is disabled
        Edge Port [PortFast] BPDU Filter Default is disabled
        Bridge Assurance                         is enabled
        Loopguard Default                        is disabled
        Pathcost method used                     is long
        PVST Simulation                          is enabled
        vPC peer-switch                          is enabled (non-operational)
        STP-Lite                                 is enabled

        Name                   Blocking Listening Learning Forwarding STP Active
        ---------------------- -------- --------- -------- ---------- ----------
        MST0000                      1         0        0          0          1
        ---------------------- -------- --------- -------- ---------- ----------
        1 mst                        1         0        0          0          1
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
        Port Type Default                        is disable
        Edge Port [PortFast] BPDU Guard Default  is enabled
        Edge Port [PortFast] BPDU Filter Default is enabled
        Bridge Assurance                         is enabled
        Loopguard Default                        is disabled
        Pathcost method used                     is long
        PVST Simulation                          is disabled
        vPC peer-switch                          is enabled (non-operational)
        STP-Lite                                 is enabled

        Name                   Blocking Listening Learning Forwarding STP Active
        ---------------------- -------- --------- -------- ---------- ----------
        MST0                         3         0        0          9         12
        MST100                       3         0        0          1          4
        ---------------------- -------- --------- -------- ---------- ----------
        1 mst                        1         0        0          0          1
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

    golden_output_1 = {'execute.return_value': '''\
        S1-R101# show spann sum
        Switch is in rapid-pvst mode 
        Root bridge for: VLAN0109-VLAN0110, VLAN0122, VLAN0202-VLAN0205
          VLAN0207-VLAN0209, VLAN0212-VLAN0215, VLAN0222-VLAN0224, VLAN0232-VLAN0234
          VLAN0242, VLAN0244, VLAN0253-VLAN0254, VLAN0264, VLAN0274, VLAN0280

        Port Type Default                        is disable
        Edge Port [PortFast] BPDU Guard Default  is disabled
        Edge Port [PortFast] BPDU Filter Default is disabled
        Bridge Assurance                         is enabled
        Loopguard Default                        is disabled
        Pathcost method used                     is short
        STP-Lite                                 is enabled

        Name                   Blocking Listening Learning Forwarding STP Active
        ---------------------- -------- --------- -------- ---------- ----------
        VLAN0109                     0         0        0          3          3
        VLAN0110                     0         0        0          2          2
        VLAN0122                     0         0        0          2          2
        VLAN0202                     0         0        0          2          2
        VLAN0203                     0         0        0          1          1
        VLAN0204                     0         0        0          2          2
        VLAN0205                     0         0        0          2          2
        VLAN0207                     0         0        0          2          2
        VLAN0208                     0         0        0          2          2
        ---------------------- -------- --------- -------- ---------- ----------
        117 vlans                    0         0        0        280        280
        DS1-R101#        exit
    '''
    }

    golden_parsed_output_1 = {
        'bpdu_filter': False,
        'bpdu_guard': False,
        'bridge_assurance': True,
        'loop_guard': False,
        'mode': {
            'rapid-pvst': {
                'VLAN0109': {
                    'blocking': 0,
                    'forwarding': 3,
                    'learning': 0,
                    'listening': 0,
                    'stp_active': 3
                },
                'VLAN0110': {
                    'blocking': 0,
                    'forwarding': 2,
                    'learning': 0,
                    'listening': 0,
                    'stp_active': 2
                },
                'VLAN0122': {
                    'blocking': 0,
                    'forwarding': 2,
                    'learning': 0,
                    'listening': 0,
                    'stp_active': 2
                },
                'VLAN0202': {
                    'blocking': 0,
                    'forwarding': 2,
                    'learning': 0,
                    'listening': 0,
                    'stp_active': 2
                },
                'VLAN0203': {
                    'blocking': 0,
                    'forwarding': 1,
                    'learning': 0,
                    'listening': 0,
                    'stp_active': 1
                },
                'VLAN0204': {
                    'blocking': 0,
                    'forwarding': 2,
                    'learning': 0,
                    'listening': 0,
                    'stp_active': 2
                },
                'VLAN0205': {
                    'blocking': 0,
                    'forwarding': 2,
                    'learning': 0,
                    'listening': 0,
                    'stp_active': 2
                },
                'VLAN0207': {
                    'blocking': 0,
                    'forwarding': 2,
                    'learning': 0,
                    'listening': 0,
                    'stp_active': 2
                },
                'VLAN0208': {
                    'blocking': 0,
                    'forwarding': 2,
                    'learning': 0,
                    'listening': 0,
                    'stp_active': 2
                },
            }
        },
        'path_cost_method': 'short',
        'port_type_default': False,
        'root_bridge_for': 'VLAN0109-VLAN0110, VLAN0122, VLAN0202-VLAN0205, '
                            'VLAN0207-VLAN0209, VLAN0212-VLAN0215, VLAN0222-VLAN0224, '
                            'VLAN0232-VLAN0234, VLAN0242, VLAN0244, VLAN0253-VLAN0254, '
                            'VLAN0264, VLAN0274, VLAN0280',
        'stp_lite': True,
        'total_statistics': {
            'blockings': 0,
            'forwardings': 280,
            'learnings': 0,
            'listenings': 0,
            'stp_actives': 280
        }
    }

    golden_output_2 = {'execute.return_value': '''
    show spann sum
    Switch is in rapid-pvst mode 

    Port Type Default                        is disable
    Edge Port [PortFast] BPDU Guard Default  is disabled
    Edge Port [PortFast] BPDU Filter Default is disabled
    Bridge Assurance                         is enabled
    Loopguard Default                        is disabled
    Pathcost method used                     is short
    STP-Lite                                 is enabled
    '''}

    golden_parsed_output_2 = {
        'bpdu_filter': False,
        'bpdu_guard': False,
        'bridge_assurance': True,
        'loop_guard': False,
        'mode': {
            'rapid-pvst': {
            }
        },
        'path_cost_method': 'short',
        'port_type_default': False,
        'stp_lite': True,
    }

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

    def test_golden_1(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_1)
        obj = ShowSpanningTreeSummary(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_1)

    def test_golden_2(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_2)
        obj = ShowSpanningTreeSummary(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

class TestShowSpanningTreeDetail(unittest.TestCase):
    dev_c3850 = Device(name = 'c3850')
    dev2 = Device(name = 'empty')

    empty_output = {'execute.return_value' : '          '}

    golden_output_1 = {'execute.return_value': '''
        P1# show spanning-tree detail

         MST0000 is executing the mstp compatible Spanning Tree protocol
      Bridge Identifier has priority 32768, sysid 0, address 00e3.04ff.ad03
      Configured hello time 10, max age 40, forward delay 30
      We are the root of the spanning tree
      Topology change flag not set, detected flag not set
      Number of topology changes 0 last change occurred 142:22:13 ago
      Times:  hold 1, topology change 70, notification 10
              hello 10, max age 40, forward delay 30 
      Timers: hello 0, topology change 0, notification 0

     Port 4125 (port-channel30, vPC Peer-link) of MST0000 is broken  (Bridge Assuran
    ce Inconsistent, VPC Peer-link Inconsistent)
       Port path cost 500, Port priority 128, Port Identifier 128.4125
       Designated root has priority 32768, address 0023.04ff.ad03
       Designated bridge has priority 61440, address 4055.39ff.fee7
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
                    'bridge_address': '00e3.04ff.ad03',
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
                        'Port-channel30': {
                            'name': 'Port-channel30',
                            'bridge_assurance_inconsistent': True,
                            'vpc_peer_link_inconsistent': True,
                            'port_num': 4125,
                            'status': 'broken',
                            'cost': 500,
                            'port_priority': 128,
                            'port_identifier': '128.4125',
                            'designated_root_priority': 32768,
                            'designated_root_address': '0023.04ff.ad03',
                            'designated_bridge_priority': 61440,
                            'designated_bridge_address': '4055.39ff.fee7',
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
      Bridge Identifier has priority 32768, sysid 0, address 0023.04ff.ad03
      Configured hello time 10, fex hello time 10, max age 40, forward delay 30
      We are the root of the spanning tree
      Topology change flag not set, detected flag not set
      Number of topology changes 0 last change occurred 142:22:13 ago
      Times:  hold 1, topology change 70, notification 10
              hello 10, max age 40, forward delay 30 
      Timers: hello 0, topology change 0, notification 0

     Port 4125 (port-channel30, vPC Peer-link) of MST0000 is broken  (Bridge Assuran
    ce Inconsistent, VPC Peer-link Inconsistent)
       Port path cost 500, Port priority 128, Port Identifier 128.4125
       Designated root has priority 32768, address 0023.04ff.ad03
       Designated bridge has priority 61440, address 4055.39ff.fee7
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
        Designated root has priority 32768, address d8b1.90ff.c889
        Designated bridge has priority 32768, address d8b1.90ff.c889
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
                    'bridge_address': '0023.04ff.ad03',
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
                        'Port-channel30': {
                            'name': 'Port-channel30',
                            'bridge_assurance_inconsistent': True,
                            'vpc_peer_link_inconsistent': True,
                            'port_num': 4125,
                            'status': 'broken',
                            'cost': 500,
                            'port_priority': 128,
                            'port_identifier': '128.4125',
                            'designated_root_priority': 32768,
                            'designated_root_address': '0023.04ff.ad03',
                            'designated_bridge_priority': 61440,
                            'designated_bridge_address': '4055.39ff.fee7',
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
                            'designated_root_address': 'd8b1.90ff.c889',
                            'designated_bridge_priority': 32768,
                            'designated_bridge_address': 'd8b1.90ff.c889',
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
            'fex_hello_time': 10,
            'max_age': 40,
            'forwarding_delay': 30
        }
    }

    golden_output_3 = {'execute.return_value': '''\
DS1-R101# sh spanning-tree detail 

 VLAN0109 is executing the rstp compatible Spanning Tree protocol
  Bridge Identifier has priority 20480, sysid 109, address 0023.04ff.ad0e
  Configured hello time 2, max age 20, forward delay 15
  We are the root of the spanning tree
  Topology change flag not set, detected flag not set
  Number of topology changes 8 last change occurred 126:41:16 ago
          from port-channel31
  Times:  hold 1, topology change 35, notification 2
          hello 2, max age 20, forward delay 15 
  Timers: hello 0, topology change 0, notification 0

 Port 4126 (port-channel31, vPC Peer-link) of VLAN0109 is root forwarding 
   Port path cost 2, Port priority 128, Port Identifier 128.4126
   Designated root has priority 20589, address 0023.04ff.ad0e
   Designated bridge has priority 0, address 0026.98ff.e460
   Designated port id is 128.4126, designated path cost 0
   Timers: message age 3, forward delay 0, hold 0
   Number of transitions to forwarding state: 1
   The port type is network
   Link type is point-to-point by default
   BPDU: sent 3245614, received 3245744

 Port 4194 (port-channel99, vPC) of VLAN0109 is designated forwarding 
   Port path cost 1, Port priority 128, Port Identifier 128.4194
   Designated root has priority 20589, address 0023.04ff.ad0e
   Designated bridge has priority 20589, address 0026.98ff.e460
   Designated port id is 128.4194, designated path cost 0
   Timers: message age 0, forward delay 0, hold 0
   Number of transitions to forwarding state: 0
   Link type is point-to-point by default
   Root guard is enabled
   BPDU: sent 2725887, received 0

 Port 4196 (port-channel101, vPC) of VLAN0109 is designated forwarding 
   Port path cost 1, Port priority 128, Port Identifier 128.4196
   Designated root has priority 20589, address 0023.04ff.ad0e
   Designated bridge has priority 20589, address 0026.98ff.e460
   Designated port id is 128.4196, designated path cost 0
   Timers: message age 0, forward delay 0, hold 0
   Number of transitions to forwarding state: 0
   Link type is shared
   BPDU: sent 231106, received 0


 VLAN0110 is executing the rstp compatible Spanning Tree protocol
  Bridge Identifier has priority 20480, sysid 110, address 0023.04ff.ad0e
  Configured hello time 2, max age 20, forward delay 15
  We are the root of the spanning tree
  Topology change flag not set, detected flag not set
  Number of topology changes 9 last change occurred 123:32:30 ago
          from port-channel31
  Times:  hold 1, topology change 35, notification 2
          hello 2, max age 20, forward delay 15 
  Timers: hello 0, topology change 0, notification 0

 Port 4126 (port-channel31, vPC Peer-link) of VLAN0110 is root forwarding 
   Port path cost 2, Port priority 128, Port Identifier 128.4126
   Designated root has priority 20590, address 0023.04ff.ad0e
   Designated bridge has priority 0, address 0026.98ff.e460
   Designated port id is 128.4126, designated path cost 0
   Timers: message age 3, forward delay 0, hold 0
   Number of transitions to forwarding state: 1
   The port type is network
   Link type is point-to-point by default
   BPDU: sent 3245614, received 3245745

 Port 4194 (port-channel99, vPC) of VLAN0110 is designated forwarding 
   Port path cost 1, Port priority 128, Port Identifier 128.4194
   Designated root has priority 20590, address 0023.04ff.ad0e
   Designated bridge has priority 20590, address 0026.98ff.e460
   Designated port id is 128.4194, designated path cost 0
   Timers: message age 0, forward delay 0, hold 0
   Number of transitions to forwarding state: 0
   Link type is point-to-point by default
   Root guard is enabled
   BPDU: sent 2725886, received 0


 VLAN0122 is executing the rstp compatible Spanning Tree protocol
  Bridge Identifier has priority 20480, sysid 122, address 0023.04ff.ad0e
  Configured hello time 2, max age 20, forward delay 15
  Topology change flag not set, detected flag not set
  Number of topology changes 9 last change occurred 123:10:02 ago
          from port-channel31
  Times:  hold 1, topology change 35, notification 2
          hello 2, max age 20, forward delay 15 
  Timers: hello 0, topology change 0, notification 0

 Port 4126 (port-channel31, vPC Peer-link) of VLAN0122 is root forwarding 
   Port path cost 2, Port priority 128, Port Identifier 128.4126
   Designated root has priority 20602, address 0023.04ff.ad0e
   Designated bridge has priority 0, address 0026.98ff.e460
   Designated port id is 128.4126, designated path cost 0
   Timers: message age 3, forward delay 0, hold 0
   Number of transitions to forwarding state: 1
   The port type is network
   Link type is point-to-point by default
   BPDU: sent 3245614, received 3245745

 Port 4194 (port-channel99, vPC) of VLAN0122 is designated forwarding 
   Port path cost 1, Port priority 128, Port Identifier 128.4194
   Designated root has priority 20602, address 0023.04ff.ad0e
   Designated bridge has priority 20602, address 0026.98ff.e460
   Designated port id is 128.4194, designated path cost 0, Topology change is set
   Timers: message age 0, forward delay 0, hold 0
   Number of transitions to forwarding state: 0
   Link type is point-to-point by default
   Root guard is enabled
   BPDU: sent 2725887, received 0

    '''
    }

    golden_parsed_output_3 = {
        'rapid_pvst': {
            'forwarding_delay': 15,
            'hello_time': 2,
            'max_age': 20,
            'vlans': {
                109: {
                    'bridge_address': '0023.04ff.ad0e',
                    'bridge_priority': 20480,
                    'bridge_sysid': 109,
                    'interfaces': {
                        'Port-channel101': {
                            'cost': 1,
                            'counters': {
                                'bpdu_received': 0,
                                'bpdu_sent': 231106
                            },
                            'designated_bridge_address': '0026.98ff.e460',
                            'designated_bridge_priority': 20589,
                            'designated_path_cost': 0,
                            'designated_port_id': '128.4196',
                            'designated_root_address': '0023.04ff.ad0e',
                            'designated_root_priority': 20589,
                            'internal': False,
                            'link_type': 'shared',
                            'name': 'Port-channel101',
                            'number_of_forward_transitions': 0,
                            'port_identifier': '128.4196',
                            'port_num': 4196,
                            'port_priority': 128,
                            'status': 'designated',
                            'timers': {
                                'forward_delay': 0,
                                'hold': 0,
                                'message_age': 0
                            }
                        },
                        'Port-channel31': {
                            'cost': 2,
                            'counters': {
                                'bpdu_received': 3245744,
                                'bpdu_sent': 3245614
                            },
                            'designated_bridge_address': '0026.98ff.e460',
                            'designated_bridge_priority': 0,
                            'designated_path_cost': 0,
                            'designated_port_id': '128.4126',
                            'designated_root_address': '0023.04ff.ad0e',
                            'designated_root_priority': 20589,
                            'internal': False,
                            'link_type': 'point-to-point',
                            'name': 'Port-channel31',
                            'number_of_forward_transitions': 1,
                            'port_identifier': '128.4126',
                            'port_num': 4126,
                            'port_priority': 128,
                            'port_type': 'network',
                            'status': 'root',
                            'timers': {
                                'forward_delay': 0,
                                'hold': 0,
                                'message_age': 3
                            }
                        },
                       'Port-channel99': {
                            'cost': 1,
                            'counters': {
                                'bpdu_received': 0,
                                'bpdu_sent': 2725887
                            },
                            'designated_bridge_address': '0026.98ff.e460',
                            'designated_bridge_priority': 20589,
                            'designated_path_cost': 0,
                            'designated_port_id': '128.4194',
                            'designated_root_address': '0023.04ff.ad0e',
                            'designated_root_priority': 20589,
                            'internal': False,
                            'link_type': 'point-to-point',
                            'name': 'Port-channel99',
                            'number_of_forward_transitions': 0,
                            'port_identifier': '128.4194',
                            'port_num': 4194,
                            'port_priority': 128,
                            'root_guard': True,
                            'status': 'designated',
                            'timers': {
                                'forward_delay': 0,
                                'hold': 0,
                                'message_age': 0
                            }
                        }
                    },
                    'root_of_the_spanning_tree': True,
                    'time_since_topology_change': '126:41:16',
                    'timers': {
                        'hello': 0,
                        'notification': 0,
                        'topology_change': 0
                    },
                    'times': {
                        'forwarding_delay': 15,
                        'hello': 2,
                        'hold': 1,
                        'max_age': 20,
                        'notification': 2,
                        'topology_change': 35
                    },
                    'topology_change_flag': False,
                    'topology_changes': 8,
                    'topology_detected_flag': False,
                    'topology_from_port': 'port-channel31',
                    'vlan_id': 109
                },
                110: {
                    'bridge_address': '0023.04ff.ad0e',
                    'bridge_priority': 20480,
                    'bridge_sysid': 110,
                    'interfaces': {
                        'Port-channel31': {
                        'cost': 2,
                        'counters': {
                            'bpdu_received': 3245745,
                            'bpdu_sent': 3245614
                        },
                        'designated_bridge_address': '0026.98ff.e460',
                        'designated_bridge_priority': 0,
                        'designated_path_cost': 0,
                        'designated_port_id': '128.4126',
                        'designated_root_address': '0023.04ff.ad0e',
                        'designated_root_priority': 20590,
                        'internal': False,
                        'link_type': 'point-to-point',
                        'name': 'Port-channel31',
                        'number_of_forward_transitions': 1,
                        'port_identifier': '128.4126',
                        'port_num': 4126,
                        'port_priority': 128,
                        'port_type': 'network',
                        'status': 'root',
                        'timers': {
                            'forward_delay': 0,
                            'hold': 0,
                            'message_age': 3
                            }
                        },
                       'Port-channel99': {
                            'cost': 1,
                            'counters': {
                                'bpdu_received': 0,
                                'bpdu_sent': 2725886
                            },
                            'designated_bridge_address': '0026.98ff.e460',
                            'designated_bridge_priority': 20590,
                            'designated_path_cost': 0,
                            'designated_port_id': '128.4194',
                            'designated_root_address': '0023.04ff.ad0e',
                            'designated_root_priority': 20590,
                            'internal': False,
                            'link_type': 'point-to-point',
                            'name': 'Port-channel99',
                            'number_of_forward_transitions': 0,
                            'port_identifier': '128.4194',
                            'port_num': 4194,
                            'port_priority': 128,
                            'root_guard': True,
                            'status': 'designated',
                            'timers': {
                                'forward_delay': 0,
                                'hold': 0,
                                'message_age': 0
                            }
                        }
                    },
                    'root_of_the_spanning_tree': True,
                    'time_since_topology_change': '123:32:30',
                    'timers': {
                        'hello': 0,
                        'notification': 0,
                        'topology_change': 0
                    },
                    'times': {
                        'forwarding_delay': 15,
                        'hello': 2,
                        'hold': 1,
                        'max_age': 20,
                        'notification': 2,
                        'topology_change': 35
                    },
                    'topology_change_flag': False,
                    'topology_changes': 9,
                    'topology_detected_flag': False,
                    'topology_from_port': 'port-channel31',
                    'vlan_id': 110
                },
                122: {
                    'bridge_address': '0023.04ff.ad0e',
                    'bridge_priority': 20480,
                    'bridge_sysid': 122,
                    'interfaces': {
                        'Port-channel31': {
                            'cost': 2,
                            'counters': {  
                                'bpdu_received': 3245745,
                                'bpdu_sent': 3245614
                            },
                            'designated_bridge_address': '0026.98ff.e460',
                            'designated_bridge_priority': 0,
                            'designated_path_cost': 0,
                            'designated_port_id': '128.4126',
                            'designated_root_address': '0023.04ff.ad0e',
                            'designated_root_priority': 20602,
                            'internal': False,
                            'link_type': 'point-to-point',
                            'name': 'Port-channel31',
                            'number_of_forward_transitions': 1,
                            'port_identifier': '128.4126',
                            'port_num': 4126,
                            'port_priority': 128,
                            'port_type': 'network',
                            'status': 'root',
                            'timers': {
                                'forward_delay': 0,
                                'hold': 0,
                                'message_age': 3
                            }
                        },
                        'Port-channel99': {
                            'cost': 1,
                            'counters': {
                                'bpdu_received': 0,
                                'bpdu_sent': 2725887
                            },
                            'topology_change': True,
                            'designated_bridge_address': '0026.98ff.e460',
                            'designated_bridge_priority': 20602,
                            'designated_path_cost': 0,
                            'designated_port_id': '128.4194',
                            'designated_root_address': '0023.04ff.ad0e',
                            'designated_root_priority': 20602,
                            'internal': False,
                            'link_type': 'point-to-point',
                            'name': 'Port-channel99',
                            'number_of_forward_transitions': 0,
                            'port_identifier': '128.4194',
                            'port_num': 4194,
                            'port_priority': 128,
                            'root_guard': True,
                            'status': 'designated',
                            'timers': {
                                'forward_delay': 0,
                                'hold': 0,
                                'message_age': 0
                            }
                        }
                    },
                    'time_since_topology_change': '123:10:02',
                    'timers': {
                        'hello': 0,
                        'notification': 0,
                        'topology_change': 0
                    },
                    'times': {
                        'forwarding_delay': 15,
                        'hello': 2,
                        'hold': 1,
                        'max_age': 20,
                        'notification': 2,
                        'topology_change': 35
                    },
                    'topology_change_flag': False,
                    'topology_changes': 9,
                    'topology_detected_flag': False,
                    'topology_from_port': 'port-channel31',
                    'vlan_id': 122
                }
            }
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

    def test_detail_output_3(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_3)
        obj = ShowSpanningTreeDetail(device = self.dev_c3850)
        parsed = obj.parse()
        self.assertEqual(parsed, self.golden_parsed_output_3)   


class TestShowErrdisabledRecovery(unittest.TestCase):
    dev_n7k = Device(name='n7000')
    dev2 = Device(name = 'empty')

    empty_output = {'execute.return_value' : '          '}

    golden_output = {'execute.return_value': '''
        PE1# sh errdisable recovery                                                                                                                                                                                                                                                                                                                 
        ErrDisable Reason               Timer Status                                                                                                                                                                                                                                                                                                
        -----------------               ------------                                                                                                                                                                                                                                                                                                
        link-flap                       disabled                                                                                                                                                                                                                                                                                                    
        udld                            disabled                                                                                                                                                                                                                                                                                                    
        bpduguard                       disabled                                                                                                                                                                                                                                                                                                    
        loopback                        disabled                                                                                                                                                                                                                                                                                                    
        storm-ctrl                      disabled                                                                                                                                                                                                                                                                                                    
        sec-violation                   disabled                                                                                                                                                                                                                                                                                                    
        psec-violation                  disabled                                                                                                                                                                                                                                                                                                    
        vpc-peerlink                    disabled                                                                                                                                                                                                                                                                                                    
        failed-port-state               disabled                                                                                                                                                                                                                                                                                                    
        event-debug                     disabled                                                                                                                                                                                                                                                                                                    
        event-debug1                    disabled                                                                                                                                                                                                                                                                                                    
        event-debug2                    disabled                                                                                                                                                                                                                                                                                                    
        event-debug3                    disabled                                                                                                                                                                                                                                                                                                    
        event-debug4                    disabled                                                                                                                                                                                                                                                                                                    
        miscabling                      disabled                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                    
                Timer interval: 300                                                                                                                                                                                                                                                                                                                 
        PE1# 
    '''}

    golden_parsed_output = {
        'timer_interval': 300,
        'errdisable_reason': {
            'bpduguard': False,
            'event-debug': False,
            'event-debug1': False,
            'event-debug2': False,
            'event-debug3': False,
            'event-debug4': False,
            'failed-port-state': False,
            'link-flap': False,
            'loopback': False,
            'miscabling': False,
            'psec-violation': False,
            'sec-violation': False,
            'storm-ctrl': False,
            'udld': False,
            'vpc-peerlink': False
        }
    }

    golden_output_2 = {'execute.return_value': '''
        N95_2# sh errdisable recovery                                                                                                                                                                                                                                                                                                               
        ErrDisable Reason               Timer Status                                                                                                                                                                                                                                                                                                
        -----------------               ------------                                                                                                                                                                                                                                                                                                
        link-flap                       disabled                                                                                                                                                                                                                                                                                                    
        udld                            disabled                                                                                                                                                                                                                                                                                                    
        bpduguard                       disabled                                                                                                                                                                                                                                                                                                    
        loopback                        disabled                                                                                                                                                                                                                                                                                                    
        storm-ctrl                      disabled                                                                                                                                                                                                                                                                                                    
        dhcp-rate-lim                   disabled                                                                                                                                                                                                                                                                                                    
        arp-inspection                  disabled                                                                                                                                                                                                                                                                                                    
        sec-violation                   disabled                                                                                                                                                                                                                                                                                                    
        psec-violation                  disabled                                                                                                                                                                                                                                                                                                    
        vpc-peerlink                    disabled                                                                                                                                                                                                                                                                                                    
        port-state-failed               disabled                                                                                                                                                                                                                                                                                                    
        event-debug                     disabled                                                                                                                                                                                                                                                                                                    
        event-debug1                    disabled                                                                                                                                                                                                                                                                                                    
        event-debug2                    disabled                                                                                                                                                                                                                                                                                                    
        event-debug3                    disabled                                                                                                                                                                                                                                                                                                    
        event-debug4                    disabled                                                                                                                                                                                                                                                                                                    
        ip-addr-conflict                disabled                                                                                                                                                                                                                                                                                                    
        ipqos-mgr-error                 disabled                                                                                                                                                                                                                                                                                                    
        ethpm                           disabled                                                                                                                                                                                                                                                                                                    
        ipqos-compat-failure            disabled                                                                                                                                                                                                                                                                                                    
        syserr based                    disabled                                                                                                                                                                                                                                                                                                    
        CMM miscabling                  disabled                                                                                                                                                                                                                                                                                                    
        md-mismatch                     disabled                                                                                                                                                                                                                                                                                                    
        hw-res-exhaustion               disabled                                                                                                                                                                                                                                                                                                    
        reinit-no-flap                  disabled                                                                                                                                                                                                                                                                                                    
        dcbx-error                      disabled                                                                                                                                                                                                                                                                                                    
        vlan-membership-erro            disabled                                                                                                                                                                                                                                                                                                    
        pause-rate-limit                disabled                                                                                                                                                                                                                                                                                                    
        inline-power                    disabled                                                                                                                                                                                                                                                                                                    
        sw-failure                      disabled                                                                                                                                                                                                                                                                                                    
        elo-session-down                disabled                                                                                                                                                                                                                                                                                                    
        elo-discovery-timeou            disabled                                                                                                                                                                                                                                                                                                    
        elo-capabilties-conf            disabled                                                                                                                                                                                                                                                                                                    
        elo-miswired                    disabled                                                                                                                                                                                                                                                                                                    
        elo-link-fault                  disabled                                                                                                                                                                                                                                                                                                    
        elo-dying-gasp                  disabled                                                                                                                                                                                                                                                                                                    
        elo-critical-event              disabled                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                    
                Timer interval: 300                                                                                                                                                                                                                                                                                                                 
        N95_2#  
    '''}

    golden_parsed_output_2 = {
        'timer_interval': 300,
        'errdisable_reason': {
            'CMM miscabling': False,
            'arp-inspection': False,
            'bpduguard': False,
            'dcbx-error': False,
            'dhcp-rate-lim': False,
            'elo-capabilties-conf': False,
            'elo-critical-event': False,
            'elo-discovery-timeou': False,
            'elo-dying-gasp': False,
            'elo-link-fault': False,
            'elo-miswired': False,
            'elo-session-down': False,
            'ethpm': False,
            'event-debug': False,
            'event-debug1': False,
            'event-debug2': False,
            'event-debug3': False,
            'event-debug4': False,
            'hw-res-exhaustion': False,
            'inline-power': False,
            'ip-addr-conflict': False,
            'ipqos-compat-failure': False,
            'ipqos-mgr-error': False,
            'link-flap': False,
            'loopback': False,
            'md-mismatch': False,
            'pause-rate-limit': False,
            'port-state-failed': False,
            'psec-violation': False,
            'reinit-no-flap': False,
            'sec-violation': False,
            'storm-ctrl': False,
            'sw-failure': False,
            'syserr based': False,
            'udld': False,
            'vlan-membership-erro': False,
            'vpc-peerlink': False
        }
    }

    def test_output_empty(self):
        self.dev2 = Mock(**self.empty_output)
        obj = ShowErrdisableRecovery(device=self.dev2)
        with self.assertRaises(SchemaEmptyParserError):
            parsed = obj.parse()

    def test_golden_output_1(self):
        self.maxDiff = None
        self.dev_n7k = Mock(**self.golden_output)
        obj = ShowErrdisableRecovery(device=self.dev_n7k)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_output_2(self):
        self.maxDiff = None
        self.dev_n7k = Mock(**self.golden_output_2)
        obj = ShowErrdisableRecovery(device=self.dev_n7k)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)


if __name__ == '__main__':
    unittest.main()
