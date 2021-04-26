# Python
import unittest
from unittest.mock import Mock

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError
# iosxr show ospf neighbor
from pyats.topology import Device

from genie.libs.parser.iosxr.show_ospf_interface import ShowOspfInterface


# =================================
# Unit test for:
#   * show ospf neighbor
#   * show ospf {process_name} neighbor
# =================================
class TestShowOspfInterface(unittest.TestCase):
    """Unit test for:
     * show ospf neighbor
     * show ospf {process_name} neighbor
    """

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output1 = {'execute.return_value': '''
        RP/0/RP0/CPU0:R1#show ospf interface
        Mon Apr 12 11:05:23.351 JST
        
        Interfaces for OSPF mpls1
        
        Loopback0 is up, line protocol is up
          Internet Address 25.97.1.1/32, Area 0, SID 0, Strict-SPF SID 0
          Label stack Primary label 0 Backup label 0 SRTE label 0
          Process ID mpls1, Router ID 25.97.1.1, Network Type LOOPBACK, Cost: 1
          Loopback interface is treated as a stub Host
        GigabitEthernet0/0/0/0 is up, line protocol is up
          Internet Address 100.10.0.1/30, Area 0, SID 0, Strict-SPF SID 0
          Label stack Primary label 1 Backup label 3 SRTE label 10
          Process ID mpls1, Router ID 25.97.1.1, Network Type POINT_TO_POINT, Cost: 1
          Transmit Delay is 1 sec, State POINT_TO_POINT, MTU 1500, MaxPktSz 1500
          Forward reference No, Unnumbered no,  Bandwidth 1000000
          BFD enabled, BFD interval 150 msec, BFD multiplier 3, Mode: Default
          Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
          Non-Stop Forwarding (NSF) enabled
            Hello due in 00:00:04:702
          Index 1/1, flood queue length 0
          Next 0(0)/0(0)
          Last flood scan length is 1, maximum is 7
          Last flood scan time is 0 msec, maximum is 1 msec
          LS Ack List: current length 0, high water mark 19
          Neighbor Count is 1, Adjacent neighbor count is 1
            Adjacent with neighbor 100.100.100.100
          Suppress hello for 0 neighbor(s)
          Multi-area interface Count is 0
        GigabitEthernet0/0/0/1 is up, line protocol is up
          Internet Address 100.20.0.1/30, Area 0, SID 0, Strict-SPF SID 0
          Label stack Primary label 1 Backup label 3 SRTE label 10
          Process ID mpls1, Router ID 25.97.1.1, Network Type POINT_TO_POINT, Cost: 1
          Transmit Delay is 1 sec, State POINT_TO_POINT, MTU 1500, MaxPktSz 1500
          Forward reference No, Unnumbered no,  Bandwidth 1000000
          BFD enabled, BFD interval 150 msec, BFD multiplier 3, Mode: Default
          Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
          Non-Stop Forwarding (NSF) enabled
            Hello due in 00:00:08:508
          Index 2/2, flood queue length 0
          Next 0(0)/0(0)
          Last flood scan length is 3, maximum is 9
          Last flood scan time is 0 msec, maximum is 1 msec
          LS Ack List: current length 0, high water mark 14
          Neighbor Count is 1, Adjacent neighbor count is 1
            Adjacent with neighbor 95.95.95.95
          Suppress hello for 0 neighbor(s)
          Multi-area interface Count is 0
    '''}

    golden_output2 = {'execute.return_value': '''
        Interfaces for OSPF 1
        GigabitEthernet0/2/0/1 is up, line protocol is up
            Internet Address 121.10.10.2/24, Area 2
            Process ID 1, Router ID 200.2.2.2, Network Type POINT_TO_POINT, Cost: 1
            Transmit Delay is 1 sec, State POINT_TO_POINT,
            Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
              Hello due in 00:00:04
            Index 1/3, flood queue length 0
            Next 0(0)/0(0)
            Last flood scan length is 3, maximum is 10
            Last flood scan time is 0 msec, maximum is 0 msec
            Neighbor Count is 1, Adjacent neighbor count is 1
              Adjacent with neighbor 101.3.3.3
            Suppress hello for 0 neighbor(s)
            Multi-area interface Count is 1
              Multi-Area interface exist in area 1 Neighbor Count is 1
          GigabitEthernet0/3/0/0 is up, line protocol is up
            Internet Address 145.10.10.2/16, Area 3
            Process ID 1, Router ID 200.2.2.2, Network Type POINT_TO_POINT, Cost: 1
            Transmit Delay is 1 sec, State POINT_TO_POINT,
            BFD enabled, BFD interval 15 msec, BFD multiplier 3
            Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
            Index 1/5, flood queue length 0
            Next 0(0)/0(0)
            Last flood scan length is 3, maximum is 11
            Last flood scan time is 0 msec, maximum is 1 msec
            Neighbor Count is 1, Adjacent neighbor count is 1
              Adjacent with neighbor 101.3.3.3
            Suppress hello for 0 neighbor(s)
            Message digest authentication enabled
              Youngest key id is 1
            Multi-area interface Count is 0
    '''}


    # From folder based test case import expected parsed output
    from genie.libs.parser.iosxr.tests.ShowOspfInterface.cli.equal.golden_output1_expected \
        import expected_output as golden_parsed_output1
    from genie.libs.parser.iosxr.tests.ShowOspfInterface.cli.equal.golden_output2_expected \
        import expected_output as golden_parsed_output2

    # =============================================================
    # Test case for `show ospf neighbor`, output has `process_name`
    # =============================================================
    def test_show_ospf_interface_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowOspfInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    # =============================================================
    # Test case for `show ospf {process_name} neighbor`, output has
    # `process_name`
    # =============================================================
    def test_show_ospf_interface_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowOspfInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)


    # =============================================================
    # Test case for `show ospf {process_name} neighbor`, output is
    # empty
    # =============================================================
    def test_show_ospf_neighbor_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowOspfInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

if __name__ == '__main__':
    unittest.main()
