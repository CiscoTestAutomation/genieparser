
# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_pim
from genie.libs.parser.iosxr.show_ethernet import (ShowEthernetCfmMeps)


# ===================================================
#  Unit test for 'show ethernet cfm peer meps'
# ===================================================

class test_show_pim_vrf_mstatic(unittest.TestCase):

    '''Unit test for 'show ethernet cfm peer meps'''
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'domain': {
            'dom3': {
                'level': 5,
                'service': 'ser3',
                'mep_type': {
                    'down': {
                        'interface': {
                            'GigabitEthernet0/0/0/0': {
                                'mep_id': 1,
                                'id': {
                                    10: {
                                        'mac_address': {
                                            '0001.02ff.0706': {
                                                'st': 'V',
                                                'port': 'Up',
                                                'up_down_time': '00:01:35',
                                                'ccm_rcvd': 2,
                                                'seq_err': 0,
                                                'rdi': 0,
                                                'error': 2,
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
            'dom4': {
                'level': 2,
                'service': 'ser4',
                'mep_type': {
                    'down': {
                        'interface': {
                            'GigabitEthernet0/0/0/0': {
                                'mep_id': 1,
                                'id': {
                                    20: {
                                        'mac_address': {
                                            '0001.02ff.0705': {
                                                'st': '>',
                                                'port': 'Up',
                                                'up_down_time': '00:00:03',
                                                'ccm_rcvd': 4,
                                                'seq_err': 1,
                                                'rdi': 0,
                                                'error': 0,
                                            },
                                        },
                                    },
                                    21: {
                                        'mac_address': {
                                            '0001.02ff.0706': {
                                                'st': '>',
                                                'port': 'Up',
                                                'up_down_time': '00:00:04',
                                                'ccm_rcvd': 3,
                                                'seq_err': 0,
                                                'rdi': 0,
                                                'error': 0,
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
            'dom5': {
                'level': 2,
                'service': 'dom5',
            },
        },
    }

    golden_output1 = {'execute.return_value': '''
        RP/0/0/CPU0:router# show ethernet cfm peer meps 

        Flags:
        > - Ok                          I - Wrong interval
        R - Remote Defect received      V - Wrong level
        L - Loop (our MAC received)     T - Timed out
        C - Config (our ID received)    M - Missing (cross-check)
        X - Cross-connect (wrong MAID)  U - Unexpected (cross-check)
        * - Multiple errors received

        Domain dom3 (level 5), Service ser3
        Down MEP on GigabitEthernet0/0/0/0 MEP-ID 1
        ================================================================================
        St    ID MAC Address    Port    Up/Downtime   CcmRcvd SeqErr   RDI Error
        -- ----- -------------- ------- ----------- --------- ------ ----- -----
        V     10 0001.02ff.0706 Up      00:01:35            2      0     0     2

        Domain dom4 (level 2), Service ser4
        Down MEP on GigabitEthernet0/0/0/0 MEP-ID 1
        ================================================================================
        St    ID MAC Address    Port    Up/Downtime   CcmRcvd SeqErr   RDI Error
        -- ----- -------------- ------- ----------- --------- ------ ----- -----
        >    20 0001.02ff.0705 Up      00:00:03            4      1     0     0
        >    21 0001.02ff.0706 Up      00:00:04            3      0     0     0

        Domain dom5 (level 2), Service dom5
        '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowEthernetCfmMeps(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowEthernetCfmMeps(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output1)

if __name__ == '__main__':
    unittest.main()