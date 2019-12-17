# Import the Python mock functionality
import unittest
from unittest.mock import Mock

# pyATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# nxos show_fabricpath
from genie.libs.parser.nxos.show_fabricpath import ShowFabricpathIsisAdjacency

# =================================
# Unit test for 'show fabricpath isis adjacency'
# =================================
class test_show_fabricpath_isis_adjacency(unittest.TestCase):

    '''Unit test for "show fabricpath isis adjacency"'''

    empty_output = {'execute.return_value': ''}

    # Specify the expected result for the parsed output
    golden_parsed_output1 = {'domain': {'default': {'interfaces': {'Port-channel1': {'hold_time': '00:00:28',
                                                         'level': 1,
                                                         'snpa': 'N/A',
                                                         'state': 'UP',
                                                         'system_id': 'Switch-A'},
                                       'Port-channel326': {'hold_time': '00:00:32',
                                                           'level': 1,
                                                           'snpa': 'N/A',
                                                           'state': 'UP',
                                                           'system_id': 'Switch-B'}}}}}

    # Specify the expected unparsed output
    golden_output1 = {'execute.return_value': '''
    204-MSMR#show fabricpath isis adjacency
    Fabricpath IS-IS domain: default Fabricpath IS-IS adjacency database:
    System ID       SNPA            Level  State  Hold Time  Interface
    Switch-A        N/A             1      UP     00:00:28   port-channel1
    Switch-B        N/A             1      UP     00:00:32   port-channel326
                '''}

    def test_show_fabricpath_isis_adjacency_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowFabricpathIsisAdjacency(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_fabricpath_isis_adjacency_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowFabricpathIsisAdjacency(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

if __name__ == '__main__':
    unittest.main()