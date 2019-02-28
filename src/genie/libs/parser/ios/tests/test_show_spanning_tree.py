#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from genie.libs.parser.ios.show_spanning_tree import ShowSpanningTreeDetail, \
                                    ShowSpanningTreeMstDetail, \
                                    ShowSpanningTreeSummary, \
                                    ShowErrdisableRecovery, \
                                    ShowSpanningTree, \
                                    ShowSpanningTreeMstConfiguration

from genie.libs.parser.iosxe.tests.test_show_spanning_tree import \
    test_show_spanning_tree_summary as test_show_spanning_tree_summary_iosxe,\
    test_show_spanning_tree_mst_configuration as test_show_spanning_tree_mst_configuration_iosxe,\
    test_show_spanning_tree_detail as test_show_spanning_tree_detail_iosxe,\
    test_show_spanning_tree_mst_detail as test_show_spanning_tree_mst_detail_iosxe,\
    test_show_errdisable_recovery as test_show_errdisable_recovery_iosxe,\
    test_show_spanning_tree as test_show_spanning_tree_iosxe


class test_show_spanning_tree_summary(test_show_spanning_tree_summary_iosxe):

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
    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowSpanningTreeSummary(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_mst(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_mstp)
        obj = ShowSpanningTreeSummary(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_mstp)

    def test_golden_ios(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_ios)
        obj = ShowSpanningTreeSummary(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_ios)

    def test_golden_single_mst(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_mstp_single_mst)
        obj = ShowSpanningTreeSummary(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_mstp_single_mst)

    def test_golden_pvst(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_pvst)
        obj = ShowSpanningTreeSummary(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_pvst)

    def test_golden_rpvst(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_rpvst)
        obj = ShowSpanningTreeSummary(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_rpvst)

class test_show_spanning_tree_detail(test_show_spanning_tree_detail_iosxe):

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowSpanningTreeDetail(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_mstp(self):
        self.dev_c3850 = Mock(**self.golden_output_mstp)
        obj = ShowSpanningTreeDetail(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_mstp)

    def test_golden_pvst(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_pvst)
        obj = ShowSpanningTreeDetail(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_pvst)

    def test_golden_rapid_pvst(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_rapid_pvst)
        obj = ShowSpanningTreeDetail(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_rapid_pvst)


class test_show_spanning_tree_mst_detail(test_show_spanning_tree_mst_detail_iosxe):

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowSpanningTreeMstDetail(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowSpanningTreeMstDetail(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


class test_show_errdisable_recovery(test_show_errdisable_recovery_iosxe):

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowErrdisableRecovery(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowErrdisableRecovery(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


class test_show_spanning_tree(test_show_spanning_tree_iosxe):
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
                        "address": "0050.14bb.6000",
                        "hello_time": 2
                    },
                    "bridge": {
                        "max_age": 20,
                        "priority": 32771,
                        "forward_delay": 15,
                        "configured_bridge_priority": 32768,
                        "sys_id_ext": 3,
                        "address": "00d0.003f.8800",
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
                     Address     0050.14bb.6000
                     Cost        20000
                     Port        136 (GigabitEthernet3/8)
                     Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

          Bridge ID  Priority    32771  (priority 32768 sys-id-ext 3)
                     Address     00d0.003f.8800
                     Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

        Interface        Role Sts Cost      Prio.Nbr Status
        ---------------- ---- --- --------- -------- ------------------------
        Gi3/8            Root FWD 20000     128.136  P2p
        Po1              Desg FWD 20000     128.833  P2p
        '''}
    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowSpanningTree(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_mst(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_mstp)
        obj = ShowSpanningTree(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_mstp)

    def test_golden_rstp(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_rstp)
        obj = ShowSpanningTree(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_rstp)

    def test_golden_vlan(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_vlan)
        obj = ShowSpanningTree(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_vlan)

class test_show_spanning_tree_mst_configuration(test_show_spanning_tree_mst_configuration_iosxe):

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowSpanningTreeMstConfiguration(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowSpanningTreeMstConfiguration(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()

