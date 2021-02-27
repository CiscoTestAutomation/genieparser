# Python 
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

from genie.libs.parser.iosxe.show_ip_nbar_version import ShowIpNbarVersion

# ==============================
# Unittest for:
#    * 'show ip nbar version'
# ==============================
class test_show_ip_nbar_version(unittest.TestCase):
    '''
    Unit test for:
    show ip nbar version
    '''

    device = Device(name = 'aDevice')
    empty_output = { 'execute.return_value': '' }

    #* define the golden_parsed_output(s) and golden_output(s) here
    golden_parsed_output_1 = {
       'creation_time': 'Wed Nov 21 08:10:34 UTC 2018',
       'file': 'flash:/pp-adv-cat9k-169.1-34-40.0.0.pack',
       'name': 'Advanced Protocol Pack',
       'nbar_engine_version': '34',
       'nbar_minimum_backward_compatible_version': '34',
       'nbar_software_version': '34',
       'publisher': 'Cisco Systems Inc.',
       'state': 'Active',
       'version': '40.0'
    }

    golden_output_1 = { 'execute.return_value': 
        '''
        NBAR software version:  34
        NBAR minimum backward compatible version:  34



        Loaded Protocol Pack(s): 


        Name:                            Advanced Protocol Pack
        Version:                         40.0
        Publisher:                       Cisco Systems Inc.
        NBAR Engine Version:             34
        Creation time:                   Wed Nov 21 08:10:34 UTC 2018
        File:                            flash:/pp-adv-cat9k-169.1-34-40.0.0.pack
        State:                           Active
        '''
    }

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpNbarVersion(device = self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpNbarVersion(device = self.device)
        parsed_output = obj.parse() #* could pass in parameters as you wish
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

if __name__ == '__main__':
    unittest.main()
