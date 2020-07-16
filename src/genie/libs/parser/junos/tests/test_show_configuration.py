# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import (
    SchemaEmptyParserError,
    SchemaMissingKeyError,
)

# Parser
from genie.libs.parser.junos.show_configuration import (
    ShowConfigurationProtocolsMplsLabelSwitchedPath,
)

class TestShowConfigurationProtocolsMplsLabelSwitchedPath(unittest.TestCase):

    device = Device(name="aDevice")

    maxDiff = None
    empty_output = {"execute.return_value": ""}

    golden_parsed_output_1 = {
        'configuration': {
            'protocols': {
                'mpls': {
                    'label-switched-path': {
                        'to': '10.0.0.1',
                        'revert-timer': '0',
                        'no-cspf': True,
                        'setup-priority': '3',
                        'reservation-priority': '3',
                        'record': True,
                        'inter-domain': True,
                        'primary': {
                            'name': 'test_data'
                        }
                    }
                }
            }
        }
    }

    golden_output_1 = {
        "execute.return_value":
        """
            show configuration protocols mpls label-switched-path test_data
            to 10.0.0.1;
            revert-timer 0;
            no-cspf;
            priority 3 3;
            record;
            inter-domain;
            primary test_data;
    """
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowConfigurationProtocolsMplsLabelSwitchedPath(
            device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(path='test_data')

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowConfigurationProtocolsMplsLabelSwitchedPath(
            device=self.device)
        parsed_output = obj.parse(path='test_data')
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

if __name__ == '__main__':
    unittest.main()
