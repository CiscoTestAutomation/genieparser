# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.junos.show_lldp import ShowLldp


# =================================
# Unit test for 'show lldp'
# =================================
class TestShowLldp(unittest.TestCase):
    '''unit test for "show lldp'''
    device = Device(name='aDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'lldp-global-status': 'Disabled',
        'lldp-advertisement-interval': '30',
        'lldp-transmit-delay-interval': '0',
        'lldp-hold-time-interval': '120',
        'lldp-notification-interval': '5',
        'ptopo-configuration-trap-interval': '0',
        'ptopo-maximum-hold-time': '300',
        'lldp-med-global-status': 'Disabled',
        'lldp-port-id-subtype': 'locally-assigned',
        'lldp-port-description-type': 'interface-alias (ifAlias)',
    }

    golden_output = {
        'execute.return_value':
        '''
        LLDP                      : Disabled
        Advertisement interval    : 30 seconds
        Transmit delay            : 0 seconds
        Hold timer                : 120 seconds
        Notification interval     : 5 Second(s)
        Config Trap Interval      : 0 seconds
        Connection Hold timer     : 300 seconds

        LLDP MED                  : Disabled
        Port ID TLV subtype       : locally-assigned
        Port Description TLV type : interface-alias (ifAlias)
        '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLldp(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowLldp(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()
