# Python
import unittest
from unittest.mock import Mock

# PyATS
from pyats.topology import (Device)

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# junos show_arp
from genie.libs.parser.junos.show_class_of_service import ShowClassOfService


class TestShowClassOfService(unittest.TestCase):
    """ Unit tests for:
            * show class-of-service interface {interface}
    """

    device = Device(name='aDevice')
    maxDiff = None
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show class-of-service interface ge-0/0/2
        Physical interface: ge-0/0/2, Index: 150
        Maximum usable queues: 8, Queues in use: 4
        Exclude aggregate overhead bytes: disabled
        Logical interface aggregate statistics: disabled
        Shaping rate: 1000000 bps
        Scheduler map: <default>, Index: 2
        Congestion-notification: Disabled

        Logical interface: ge-0/0/2.0, Index: 335
        Object                  Name                   Type                    Index
        Classifier              dscp-ipv6-compatibility dscp-ipv6                  9
        Classifier              ipprec-compatibility   ip                         13
    '''}
    
    golden_parsed_output = {
        "cos-interface-information": {
            "interface-map": {
                "i-logical-map": {
                    "cos-objects": {
                        "cos-object-index": [
                            "9",
                            "13"
                        ],
                        "cos-object-name": [
                            "dscp-ipv6-compatibility",
                            "ipprec-compatibility"
                        ],
                        "cos-object-subtype": [
                            "dscp-ipv6",
                            "ip"
                        ],
                        "cos-object-type": [
                            "Classifier",
                            "Classifier"
                        ]
                    },
                    "i-logical-index": "335",
                    "i-logical-name": "ge-0/0/2.0"
                },
                "interface-congestion-notification-map": "Disabled",
                "interface-exclude-queue-overhead-bytes": "disabled",
                "interface-index": "150",
                "interface-logical-interface-aggregate-statistics": "disabled",
                "interface-name": "ge-0/0/2",
                "interface-queues-in-use": "4",
                "interface-queues-supported": "8",
                "interface-shaping-rate": "1000000",
                "scheduler-map-index": "2",
                "scheduler-map-name": "<default>"
            }
        }
    }

    golden_output_2 = {'execute.return_value': '''
        show class-of-service interface xe-0/1/7 
        Physical interface: xe-0/1/7, Index: 184
        Queues supported: 8, Queues in use: 4
        Scheduler map: <default>, Index: 2
        Congestion-notification: Disabled
        Logical interface: xe-0/1/7.0, Index: 430
        Object                  Name                   Type                    Index
        Classifier              dscp-ipv6-compatibility dscp-ipv6                  9
        Classifier              ipprec-compatibility   ip                         13
    '''}

    golden_parsed_output_2 = {
        'cos-interface-information': {
            'interface-map': {
                'i-logical-map': {
                    'cos-objects': {
                        'cos-object-index': ['9', '13'],
                        'cos-object-name': ['dscp-ipv6-compatibility', 'ipprec-compatibility'],
                        'cos-object-subtype': ['dscp-ipv6', 'ip'],
                        'cos-object-type': ['Classifier', 'Classifier'],
                    },
                    'i-logical-index': '430',
                    'i-logical-name': 'xe-0/1/7.0',
                },
                'interface-congestion-notification-map': 'Disabled',
                'interface-index': '184',
                'interface-name': 'xe-0/1/7',
                'interface-queues-in-use': '4',
                'interface-queues-supported': '8',
                'scheduler-map-index': '2',
                'scheduler-map-name': '<default>',
            },
        },
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowClassOfService(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse(interface='ge-0/0/2')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowClassOfService(device=self.device)
        parsed_output = obj.parse(interface='ge-0/0/2')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowClassOfService(device=self.device)
        parsed_output = obj.parse(interface='xe-0/1/7')
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

if __name__ == '__main__':
    unittest.main()