#!/bin/env python
# -*- coding: utf-8 -*-
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError
from genie.libs.parser.nxos.show_dot1x import ShowDot1xAllStatistics

class test_show_dot1x_all_statistics(unittest.TestCase):
    dev1 = Device(name='DeviceA')
    dev2 = Device(name='DeviceB')

    empty_output = {'execute.return_value' : '          '}

    parsed_output = {
        'Interfaces': {
            'Ethernet1/1': {
                'Interface': 'Ethernet1/1',
                'Statistics': {
                    'txreq': 0,
                    'rxlogoff': 0,
                    'txtotal': 3,
                    'txreqid': 0,
                    'lastrxsrcmac': '00:00:00:00:00:00',
                    'rxinvalid': 0,
                    'rxrespid': 0,
                    'rxlenerr': 0,
                    'rxversion': 0,
                    'rxstart': 0,
                    'rxresp': 0,
                    'rxtotal': 0,
                    }
                }
            }
        }

    output = {'execute.return_value': '''
        Dot1x Authenticator Port Statistics for Ethernet1/1
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0      RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0       TxReqID = 0     TxTotal = 3

        RxVersion = 0   LastRxSrcMAC = 00:00:00:00:00:00
    '''
    }

    parsed_output_2 = {
        'Interfaces': {
            'Ethernet1/1': {
                'Interface': 'Ethernet1/1',
                'Statistics': {
                    'txreq': 5,
                    'rxlogoff': 25,
                    'txtotal': 6,
                    'txreqid': 89,
                    'lastrxsrcmac': '02:45:44:55:66:78',
                    'rxinvalid': 5,
                    'rxrespid': 34,
                    'rxlenerr': 6,
                    'rxversion': 78,
                    'rxstart': 111,
                    'rxresp': 224,
                    'rxtotal': 543,
                    }
                }
            }
        }

    output_2 = {'execute.return_value': '''
        Dot1x Authenticator Port Statistics for Ethernet1/1
        --------------------------------------------
        RxStart = 111     RxLogoff = 25    RxResp = 224      RxRespID = 34
        RxInvalid = 5   RxLenErr = 6    RxTotal = 543

        TxReq = 5       TxReqID = 89     TxTotal = 6

        RxVersion = 78   LastRxSrcMAC = 02:45:44:55:66:78 
    '''
    }


    def test_output(self):
        self.maxDiff = None
        self.dev1 = Mock(**self.output)
        obj = ShowDot1xAllStatistics(device=self.dev1)
        parsed = obj.parse()
        self.assertEqual(parsed, self.parsed_output)

    def test_output_2(self):
        self.maxDiff = None
        self.dev1 = Mock(**self.output_2)
        obj = ShowDot1xAllStatistics(device=self.dev1)
        parsed = obj.parse()
        print(parsed)
    
    def test_empty_output(self):
        self.dev2 = Mock(**self.empty_output)
        obj = ShowDot1xAllStatistics(device = self.dev2)
        with self.assertRaises(SchemaEmptyParserError):
            parsed = obj.parse()


if __name__ == '__main__':
    unittest.main()