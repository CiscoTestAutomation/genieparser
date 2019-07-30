
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
    ge-0/0/2.0          BDR     0.0.0.1         10.16.2.2         10.64.4.4            5
    '''}
    
    golden_output_master = {'execute.return_value': '''
    show ospf interface brief instance master
    Interface           State   Area            DR ID           BDR ID          Nbrs
    ge-0/0/4.0          BDR     0.0.0.4         10.64.4.4         192.168.10.22    2
    ge-0/0/5.0          BDR     0.0.0.4         10.16.2.2         10.16.2.2          3
    ge-0/0/6.0          DR      0.0.0.4         10.64.4.4         192.168.10.22    4
    lo1.0               DR      0.0.0.4         10.16.2.2         0.0.0.0          0
    '''}
    
    golden_parsed_output = {
    'instance': {
        'master': {
            'areas': {
                '0.0.0.1': {
                    'interfaces': {
                        'ge-0/0/2.0': {
                            'state': 'BDR',
                            'dr_id': '10.16.2.2',
                            'bdr_id': '10.64.4.4',
                            'nbrs_count': 5,
                            },
                        },
                    },
                },
            },
        },
    }

    golden_parsed_output_master = {
    'instance': {
        'master': {
            'areas': {
                '0.0.0.4': {
                    'interfaces': {
                        'ge-0/0/4.0': {
                            'state': 'BDR',
                            'dr_id': '10.64.4.4',
                            'bdr_id': '192.168.10.22',
                            'nbrs_count': 2,
                            },
                        'ge-0/0/5.0': {
                            'state': 'BDR',
                            'dr_id': '10.16.2.2',
                            'bdr_id': '10.16.2.2',
                            'nbrs_count': 3,
                            },
                        'ge-0/0/6.0': {
                            'state': 'DR',
                            'dr_id': '10.64.4.4',
                            'bdr_id': '192.168.10.22',
                            'nbrs_count': 4,
                            },
                        'lo1.0': {
                            'state': 'DR',
                            'dr_id': '10.16.2.2',
                            'bdr_id': '0.0.0.0',
                            'nbrs_count': 0,
                            },
                        },
                    },
                },
            },
        },
    }


    def test_show_ospf_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowOspfInterfaceBrief(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ospf(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowOspfInterfaceBrief(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_ospf_master(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_master)
        obj = ShowOspfInterfaceBrief(device=self.device)
        parsed_output = obj.parse(instance='master')
        self.assertEqual(parsed_output, self.golden_parsed_output_master)

if __name__ == '__main__':
    unittest.main()
