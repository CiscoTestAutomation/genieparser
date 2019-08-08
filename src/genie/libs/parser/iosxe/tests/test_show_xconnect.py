# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_mrib
from genie.libs.parser.iosxe.show_xconnect import ShowXconnectAll


# ==================================================
#  Unit test for 'show xconnect all'
# ==================================================

class test_show_xconnect_all(unittest.TestCase):
    '''Unit test for 'show xconnect all'''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'segment_1': {
            'ac   Et0/0(Ethernet)': {
                'segment_2': {
                    'mpls 10.55.55.2:1000': {
                        's2': 'UP',
                        'xc': 'UP',
                        'st': 'pri'},
                    'mpls 10.55.55.3:1001': {
                        's2': 'DN',
                        'xc': 'IA',
                        'st': 'sec'}},
                's1': 'UP'}}}

    golden_output1 = {'execute.return_value': '''
        Router# show xconnect all
        Legend: XC ST=Xconnect State, S1=Segment1 State, S2=Segment2 State
        UP=Up, DN=Down, AD=Admin Down, IA=Inactive, NH=No Hardware
        XC ST  Segment 1                         S1 Segment 2                         S2
        ------+---------------------------------+--+---------------------------------+--
        UP pri ac   Et0/0(Ethernet)              UP mpls 10.55.55.2:1000              UP
        IA sec ac   Et0/0(Ethernet)              UP mpls 10.55.55.3:1001              DN
        
        '''}

    golden_parsed_output2 = {
        'segment_1': {
            'ac   Se6/0:150(FR DLCI)': {
                'segment_2': {
                    'ac   Se8/0:150(FR DLCI)': {
                        's2': 'UP',
                        'xc': 'UP',
                        'st': 'pri'},
                    'mpls 10.55.55.3:7151': {
                        's2': 'DN',
                        'xc': 'IA',
                        'st': 'sec'}},
                's1': 'UP'}}}

    golden_output2 = {'execute.return_value': '''
        Router# show xconnect all
        Legend: XC ST=Xconnect State, S1=Segment1 State, S2=Segment2 State
        UP=Up, DN=Down, AD=Admin Down, IA=Inactive, NH=No Hardware
        XC ST  Segment 1                         S1 Segment 2                         S2
        ------+---------------------------------+--+---------------------------------+--
        UP pri ac   Se6/0:150(FR DLCI)           UP ac   Se8/0:150(FR DLCI)           UP
        IA sec ac   Se6/0:150(FR DLCI)           UP mpls 10.55.55.3:7151              DN
    '''}

    def test_show_xconnect_all_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowXconnectAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_xconnect_all_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowXconnectAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_xconnect_all_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowXconnectAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)


if __name__ == '__main__':
    unittest.main()