# Python
import unittest
from unittest.mock import Mock

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError
# iosxr show_ospf_vrf_neighbor
from pyats.topology import Device

from genie.libs.parser.iosxr.show_ospf_neighbor import ShowOspfNeighbor


# =================================
# Unit test for 'show ospf vrf {vrf} neighbor'
# =================================
class TestShowOspfVrfNeighbor(unittest.TestCase):
    """Unit test for "show ospf vrf {vrf} neighbor"""

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

    # import expected ouput from folder based test cases
    from genie.libs.parser.iosxr.tests.ShowOspfVrfNeighbor.cli.equal.golden_output1_expected import \
        expected_output as golden_parsed_output1

    def test_show_lisp_session_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowOspfNeighbor(device=self.device)
        parsed_output = obj.parse(vrf='all-inclusive')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_session_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowOspfNeighbor(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
