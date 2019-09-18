
# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_evpn
from genie.libs.parser.iosxr.show_evpn import (ShowEvpnInternalLabel)

# ===================================================
#  Unit test for 'show evpn internal-label'
# ===================================================

class test_show_evpn_internal_label(unittest.TestCase):

    '''Unit test for 'show evpn internal-label'''
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output1 = {
        'evi': {
            1000: {
                'ethernet_segment_id': {
                    '0000.0102.0304.0506.07aa': {
                        'index': {
                            1: {
                                'ether_tag': '0',
                                'label': 'None',
                            },
                            2: {
                                'ether_tag': '200',
                                'label': '24011',
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output1 = {'execute.return_value': '''
        EVI     Ethernet    Segment Id                 EtherTag Label
        ----- --------------------------------------- -------- --------
        1000    0000.0102.0304.0506.07aa                0       None
        1000    0000.0102.0304.0506.07aa                200     24011
        '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowEvpnInternalLabel(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowEvpnInternalLabel(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output1)

if __name__ == '__main__':
    unittest.main()