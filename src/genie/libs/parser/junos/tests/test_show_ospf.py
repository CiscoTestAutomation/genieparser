
# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

# junos show_ospf
from genie.libs.parser.junos.show_ospf import ShowOspfInterfaceBrief


# ============================
# Unit test for 'show ospf interface brief'
# ============================
class test_show_ospf(unittest.TestCase):

    '''Unit test for "show ospf interface brief" '''

    device = Device(name='aDevice')
    
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
    show ospf interface brief                              
    Interface           State   Area            DR ID           BDR ID          Nbrs
    ge-0/0/2.0          BDR     0.0.0.1         2.2.2.2         4.4.4.4            5
    '''}

    golden_parsed_output = {
        'interfaces': {
            'ge-0/0/2.0': {
                'state': 'BDR',
                'area': '0.0.0.1',
                'dr_id': '2.2.2.2',
                'bdr_id': '4.4.4.4',
                'nbrs': 5,
                },
            },
        }
    def test_show_ospf_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowOspfInterfaceBrief(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_ospf_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowOspfInterfaceBrief(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
