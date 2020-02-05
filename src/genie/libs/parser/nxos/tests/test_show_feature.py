
# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Parser
from genie.libs.parser.nxos.show_feature import ShowFeature, ShowFeatureSet

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

 
# =========================
#  Unit test for 'show feature'
# =========================

class test_show_feature(unittest.TestCase):

    '''Unit test for show feature'''
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'feature':
            {'bash-shell':
                {'instance':
                    {'1':
                        {'state': 'disabled',}}},
            'bgp':
                {'instance':
                    {'1':
                        {'state': 'enabled',}}},
            'eigrp':
                {'instance':
                    {'1':
                        {'state': 'enabled',},
                    '2':
                        {'state': 'enabled',
                         'running': 'no',},
                    '3':
                        {'state': 'enabled',
                         'running': 'no',},
                    '4':
                        {'state': 'enabled',
                         'running': 'no',}, }}}}

    golden_output = {'execute.return_value': '''
       Feature Name          Instance  State   
        --------------------  --------  --------
        bash-shell             1          disabled
        bgp                    1          enabled 
        eigrp                  1          enabled 
        eigrp                  2          enabled(not-running)
        eigrp                  3          enabled(not-running)
        eigrp                  4          enabled(not-running)
        '''}

    def test_show_feature_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowFeature(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_feature_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowFeature(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_feature_set_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowFeatureSet(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_feature_set_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowFeatureSet(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

if __name__ == '__main__':
    unittest.main()


# vim: ft=python et sw=4
