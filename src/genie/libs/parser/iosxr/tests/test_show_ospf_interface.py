# Python
import unittest
from unittest.mock import Mock

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError
# iosxr show ospf neighbor
from pyats.topology import Device

from genie.libs.parser.iosxr.show_ospf_neighbor import ShowOspfNeighbor


# =================================
# Unit test for:
#   * show ospf neighbor
#   * show ospf {process_name} neighbor
# =================================
class TestShowOspfNeighbor(unittest.TestCase):
    """Unit test for:
     * show ospf neighbor
     * show ospf {process_name} neighbor
    """

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output1 = {'execute.return_value': '''
        Mon Apr 12 11:10:38.799 JST
        
        * Indicates MADJ interface
        # Indicates Neighbor awaiting BFD session up
        
        Neighbors for OSPF mpls1
        
        Neighbor ID     Pri   State           Dead Time   Address         Interface
        100.100.100.100 1     FULL/  -        00:00:38    100.10.0.2      GigabitEthernet0/0/0/0
            Neighbor is up for 2d18h
        95.95.95.95     1     FULL/  -        00:00:38    100.20.0.2      GigabitEthernet0/0/0/1
            Neighbor is up for 2d18h
        
        Total neighbor count: 2
    '''}

    golden_output2 = {'execute.return_value': '''
        Mon Apr 12 11:10:38.799 JST

        * Indicates MADJ interface
        # Indicates Neighbor awaiting BFD session up
        
        Neighbors for OSPF mpls1
        
        Neighbor ID     Pri   State           Dead Time   Address         Interface
        100.100.100.100 1     FULL/  -        00:00:38    100.10.0.2      GigabitEthernet0/0/0/0
            Neighbor is up for 2d18h
        95.95.95.95     1     FULL/  -        00:00:38    100.20.0.2      GigabitEthernet0/0/0/1
            Neighbor is up for 2d18h
        
        Total neighbor count: 2
    '''}

    golden_output3 = {'execute.return_value': '''
        Neighbors for OSPF
        
        Neighbor ID     Pri  State         Dead Time  Address           Interface
        192.168.199.137 1    FULL/DR       0:00:31    172.31.80.37      GigabitEthernet 0/3/0/2
          Neighbor is up for 18:45:22
        192.168.48.1     1    FULL/DROTHER  0:00:33    192.168.48.1       GigabitEthernet 0/3/0/3
          Neighbor is up for 18:45:30
        192.168.48.200   1    FULL/DROTHER  0:00:33    192.168.48.200     GigabitEthernet 0/3/0/3
          Neighbor is up for 18:45:25
        192.168.199.137 5    FULL/DR       0:00:33    192.168.48.189     GigabitEthernet 0/3/0/3
          Neighbor is up for 18:45:27
    '''}

    golden_output4 = {'execute.return_value': '''
        Mon Apr 12 11:10:38.799 JST
        
        * Indicates MADJ interface
        # Indicates Neighbor awaiting BFD session up
        
        Neighbors for OSPF
        
        Neighbor ID     Pri   State           Dead Time   Address         Interface
        100.100.100.100 1     FULL/  -        00:00:38    100.10.0.2      GigabitEthernet0/0/0/0
            Neighbor is up for 2d18h
        95.95.95.95     1     FULL/  -        00:00:38    100.20.0.2      GigabitEthernet0/0/0/1
            Neighbor is up for 2d18h
        
        Total neighbor count: 2
    '''}

    # From folder based test case import expected parsed output
    from genie.libs.parser.iosxr.tests.ShowOspfNeighbor.cli.equal.golden_output1_expected \
        import expected_output as golden_parsed_output1
    from genie.libs.parser.iosxr.tests.ShowOspfNeighbor.cli.equal.golden_output2_expected \
        import expected_output as golden_parsed_output2
    from genie.libs.parser.iosxr.tests.ShowOspfNeighbor.cli.equal.golden_output3_expected \
        import expected_output as golden_parsed_output3
    from genie.libs.parser.iosxr.tests.ShowOspfNeighbor.cli.equal.golden_output4_expected \
        import expected_output as golden_parsed_output4

    # =============================================================
    # Test case for `show ospf neighbor`, output has `process_name`
    # =============================================================
    def test_show_ospf_neighbor_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowOspfNeighbor(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    # =============================================================
    # Test case for `show ospf {process_name} neighbor`, output has
    # `process_name`
    # =============================================================
    def test_show_ospf_neighbor_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowOspfNeighbor(device=self.device)
        parsed_output = obj.parse(process_name='mpls1')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    # =============================================================
    # Test case for `show ospf neighbor`, input has identical neighbor_id
    # output dose not have `process_name` and `total_neighbor_count`
    #
    # This test case idea is from `https://www.cisco.com/c/en/us/td/docs
    # /routers/xr12000/software/xr12k_r4-0/routing/command/reference
    # /rr40xr12kbook_chapter4.html#wp962813110
    # =============================================================
    def test_show_ospf_neighbor_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowOspfNeighbor(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    # =============================================================
    # Test case for `show ospf {process_name} neighbor`, output does not
    # has `process_name`.
    # =============================================================
    def test_show_ospf_neighbor_full4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output4)
        obj = ShowOspfNeighbor(device=self.device)
        parsed_output = obj.parse(process_name='mpls1')
        self.assertEqual(parsed_output, self.golden_parsed_output4)

    # =============================================================
    # Test case for `show ospf {process_name} neighbor`, output is
    # empty
    # =============================================================
    def test_show_ospf_neighbor_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowOspfNeighbor(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
