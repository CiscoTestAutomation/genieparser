# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_mrib
from genie.libs.parser.iosxr.show_isis import ShowIsisAdjacency, \
                                              ShowIsisNeighbors


# ==================================================
#  Unit test for 'show isis adjacency'
# ==================================================

class test_show_isis_adjacency(unittest.TestCase):
    '''Unit test for 'show isis adjacency'''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'isis': {
            'p': {
                'level': {
                    'Level-2': {
                        'system_id': {
                            '12a4': {
                                'interface': 'GigabitEthernet0/6/0/2',
                                'snpa': '0004.2893.f2f6',
                                'state': 'Up',
                                'hold': '26',
                                'changed': '00:00:13',
                                'nsf': 'CapableInit'}},
                        'total_adjacency_count': 2}}}}}

    golden_output1 = {'execute.return_value': '''
        RP/0/RP0/CPU0:router# show isis adjacency

        IS-IS p Level-1 adjacencies:
        System Id      Interface        SNPA           State Hold Changed NSFBFD
        12a4           PO0/1/0/1        *PtoP*         Up    23       00:00:06 Capable Init
        12a4           Gi0/6/0/2        0004.2893.f2f6 Up    56       00:04:01 Capable Up
      
        Total adjacency count: 2
      
        IS-IS p Level-2 adjacencies:
        System Id      Interface        SNPA           State Hold Changed NSFBFD
        12a4           PO0/1/0/1        *PtoP*         Up    23       00:00:06 CapableNone
        12a4           Gi0/6/0/2        0004.2893.f2f6 Up    26       00:00:13 CapableInit
      
        Total adjacency count: 2
    '''}

    def test_show_isis_adjacency_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIsisAdjacency(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_isis_adjacency_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIsisAdjacency(device=self.device)
        parsed_output = obj.parse()
        import pdb;pdb.set_trace()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

# ====================================
#  Unit test for 'show isis neighbors'
# ====================================

class test_show_isis_neighbors(unittest.TestCase):
    '''Unit test for "show isis neighbors"'''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {}

    golden_output1 = {'execute.return_value': '''
    '''}

    def test_show_isis_neighbors_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIsisNeighbors(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_isis_neighbors_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIsisNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)


if __name__ == '__main__':
    unittest.main()