#!/bin/env python
import unittest
from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from genie.libs.parser.ios.show_spanning_tree import ShowSpanningTreeDetail, \
                                    ShowSpanningTreeMstDetail, \
                                    ShowSpanningTreeSummary, \
                                    ShowErrdisableRecovery, \
                                    ShowSpanningTree, \
                                    ShowSpanningTreeMstConfiguration

class test_show_spanning_tree_summary(unittest.TestCase):   

    device = Device(name='aDevice')

    golden_parsed_output_ios = {
        "total_statistics": {
            "forwardings": 0,
            "listenings": 0,
            "stp_actives": 0,
            "learnings": 0,
            "blockings": 0
        },
        "root_bridge_for": "none",
        "bpdu_guard": False,
        "uplink_fast": False,
        "backbone_fast": False,
    }
    golden_output_ios = {'execute.return_value': '''\
        Root bridge for: none.
        PortFast BPDU Guard is disabled
        UplinkFast is disabled
        BackboneFast is disabled

        Name                 Blocking Listening Learning Forwarding STP Active
        -------------------- -------- --------- -------- ---------- ----------
                       Total 0        0         0        0          0
            '''
                         }

    def test_golden_ios(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_ios)
        obj = ShowSpanningTreeSummary(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_ios)


class test_show_spanning_tree(unittest.TestCase):
    device = Device(name='aDevice')
    golden_parsed_output_vlan = {
        "mstp": {
            "mst_instances": {
                3: {
                    "root": {
                        "max_age": 20,
                        "interface": "GigabitEthernet3/8",
                        "forward_delay": 15,
                        "priority": 32771,
                        "cost": 20000,
                        "port": 136,
                        "address": "0050.14ff.1cbb",
                        "hello_time": 2
                    },
                    "bridge": {
                        "max_age": 20,
                        "priority": 32771,
                        "forward_delay": 15,
                        "configured_bridge_priority": 32768,
                        "sys_id_ext": 3,
                        "address": "00d0.00ff.c73f",
                        "hello_time": 2
                    },
                    "interfaces": {
                        "GigabitEthernet3/8": {
                            "port_num": 136,
                            "role": "root",
                            "port_state": "forwarding",
                            "type": "P2p",
                            "port_priority": 128,
                            "cost": 20000
                        },
                        "Port-channel1": {
                            "port_num": 833,
                            "role": "designated",
                            "port_state": "forwarding",
                            "type": "P2p",
                            "port_priority": 128,
                            "cost": 20000
                        }
                    }
                }
            }
        }
    }
    golden_output_vlan = {'execute.return_value': '''
        cat# show spanning-tree vlan 333

        MST03
          Spanning tree enabled protocol mstp
          Root ID    Priority    32771
                     Address     0050.14ff.1cbb
                     Cost        20000
                     Port        136 (GigabitEthernet3/8)
                     Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

          Bridge ID  Priority    32771  (priority 32768 sys-id-ext 3)
                     Address     00d0.00ff.c73f
                     Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

        Interface        Role Sts Cost      Prio.Nbr Status
        ---------------- ---- --- --------- -------- ------------------------
        Gi3/8            Root FWD 20000     128.136  P2p
        Po1              Desg FWD 20000     128.833  P2p
        '''}

    def test_golden_vlan(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_vlan)
        obj = ShowSpanningTree(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_vlan)

if __name__ == '__main__':
    unittest.main()

