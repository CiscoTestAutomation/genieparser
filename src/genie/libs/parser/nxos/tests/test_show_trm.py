# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Parser
from genie.libs.parser.nxos.show_trm import ShowRunningConfigTrm

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# ==========================================================================
#  Unit test for 'show running-config | sec '^advertise evpn multicast'"
# ==========================================================================
class test_show_running_config_trm(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'advertise_evpn_multicast': True,
    }

    golden_output = {'execute.return_value': '''
R2# show running-config | sec '^advertise evpn multicast'
advertise evpn multicast
        '''}

    def test_show_running_config_trm(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowRunningConfigTrm(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


    def test_show_running_config_trm_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowRunningConfigTrm(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

if __name__ == '__main__':
    unittest.main()