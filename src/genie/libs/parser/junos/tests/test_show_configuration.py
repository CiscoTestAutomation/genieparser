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
    ShowConfigurationProtocolsMplsPath,
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


class TestShowConfigurationProtocolsMplsPath(unittest.TestCase):

    device = Device(name="aDevice")

    maxDiff = None
    empty_output = {"execute.return_value": ""}

    golden_parsed_output_1 = {
        'configuration': {
            'protocols': {
                'mpls': {
                    'path': {
                        'path-list': [{
                            'name': '10.49.194.2',
                            'type': 'strict'
                        }, {
                            'name': '10.49.194.1',
                            'type': 'strict'
                        }, {
                            'name': '10.169.14.157',
                            'type': 'strict'
                        }, {
                            'name': '10.169.14.158',
                            'type': 'strict'
                        }, {
                            'name': '192.168.145.217',
                            'type': 'strict'
                        }, {
                            'name': '192.168.145.218',
                            'type': 'strict'
                        }, {
                            'name': '10.49.194.65',
                            'type': 'strict'
                        }, {
                            'name': '10.49.194.66',
                            'type': 'strict'
                        }]
                    }
                }
            }
        }
    }

    golden_output_1 = {
        "execute.return_value":
        """
            show configuration protocols mpls path test_data
            10.49.194.2 strict;
            10.49.194.1 strict;
            10.169.14.157 strict;
            10.169.14.158 strict;
            192.168.145.217 strict;
            192.168.145.218 strict;
            10.49.194.65 strict;
            10.49.194.66 strict;
    """
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowConfigurationProtocolsMplsPath(
            device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(path='test_data')

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowConfigurationProtocolsMplsPath(
            device=self.device)
        parsed_output = obj.parse(path='test_data')
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

if __name__ == '__main__':
    unittest.main()
