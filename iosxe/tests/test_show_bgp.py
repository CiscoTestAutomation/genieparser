import re
import unittest
from unittest.mock import Mock

from ats.topology import Device

from metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from parser.iosxe.show_bgp import ShowIpBgpSummary

class test_show_ip_bgp_summary(unittest.TestCase):
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        'bgp_summary': 
            {'identifier':
                {'200.0.1.1':
                    {'autonomous_system_number': '100',
                     'table_version': '1',
                     'version': '1'}},
             'neighbor':
                {'200.0.2.1':
                    {'asn': '100',
                    'inq': '0',
                    'msgr': '1352',
                    'msgs': '1355',
                    'outq': '0',
                    'state_pfxrcd': '0',
                    'tblv': '1',
                    'up_down': '20:26:15',
                    'ver': '4'},
                 '201.0.14.4':
                    {'asn': '200',
                     'inq': '0',
                     'msgr': '0',
                     'msgs': '0',
                     'outq': '0',
                     'state_pfxrcd': 'Idle',
                     'tblv': '1',
                     'up_down': 'never',
                     'ver': '4'}}}}


    golden_parsed_output_1 = {
        'bgp_summary': 
            {'identifier':
                {'200.0.1.1':
                    {'autonomous_system_number': '100',
                     'table_version': '1',
                     'version': '1'}},
             'neighbor':
                {'200.0.2.1':
                    {'asn': '100',
                    'inq': '0',
                    'msgr': '1352',
                    'msgs': '1355',
                    'outq': '0',
                    'state_pfxrcd': '0',
                    'tblv': '1',
                    'up_down': '20:26:15',
                    'ver': '4'},
                 '201.0.14.4':
                    {'asn': '200',
                     'msgr': '0',
                     'msgs': '0',                 
                     'ver': '4'}}}}

          
    golden_output = {'execute.return_value': '''
        BGP router identifier 200.0.1.1, local AS number 100
        BGP table version is 1, main routing table version 1

        Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        200.0.2.1       4          100    1352    1355        1    0    0 20:26:15        0
        201.0.14.4      4          200       0       0        1    0    0 never    Idle
        '''}

    golden_output_1 = {'execute.return_value': '''
        BGP router identifier 200.0.1.1, local AS number 100
        BGP table version is 1, main routing table version 1

        Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        200.0.2.1       4          100    1352    1355        
        201.0.14.4      4          200       0       0        
        '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        bgp_summary_obj = ShowIpBgpSummary(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = bgp_summary_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        bgp_summary_obj = ShowIpBgpSummary(device=self.device)
        #import pprint ; import pdb ; pdb.set_trace()
        parsed_output = bgp_summary_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        bgp_summary_obj = ShowIpBgpSummary(device=self.device)
        #Unitest for incompete data
        with self.assertRaises(SchemaMissingKeyError):
            parsed_output = bgp_summary_obj.parse()

if __name__ == '__main__':
    unittest.main()
