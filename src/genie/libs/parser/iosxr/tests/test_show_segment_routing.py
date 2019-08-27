#!/bin/env python
import unittest
from unittest.mock import Mock

from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

from genie.libs.parser.iosxr.show_segment_routing import ShowSegmentRoutingPrefixSidMap

# =============================================================
# Unittest for:
#   * 'Show Segment Routing Prefix Sid Map'
# =============================================================
class test_show_routing_prefix_sid_map(unittest.TestCase):
    
    device = Device(name='DeviceA')
    dev2 = Device(name='DeviceB')



    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        RP/0/0/CPU0:router# show isis segment-routing prefix-sid-map active-policy

            IS-IS 1 active policy
        Prefix               SID Index    Range        Flags
        1.1.1.100/32         100          20          
        1.1.1.150/32         150          10          

        Number of mapping entries: 2

        RP/0/0/CPU0:router# show isis segment-routing prefix-sid-map backup-policy

        IS-IS 1 backup policy
        Prefix               SID Index    Range        Flags
        1.1.1.100/32         100          20          
        1.1.1.150/32         150          10          

        Number of mapping entries: 2

        RP/0/0/CPU0:router# show ospf segment-routing prefix-sid-map active-policy

                SRMS active policy for Process ID 1

        Prefix               SID Index    Range        Flags
        1.1.1.100/32         100          20          
        1.1.1.150/32         150          10           

        Number of mapping entries: 2

        RP/0/0/CPU0:router# show ospf segment-routing prefix-sid-map backup-policy

                SRMS backup policy for Process ID 1

        Prefix               SID Index    Range        Flags
        1.1.1.100/32         100          20          
        1.1.1.150/32         150          10          

        Number of mapping entries: 2
    '''}

    golden_parsed_output = {
        'isis': {
        'name': 'isis',
        'active': {
            'status': True,
            'isis_id': 1,
            'algorithm': {
                'prefix': '1.1.1.100/32',
                'sid_index': 100,
                'range': 20
            },
            'entries': 2
            },
            'backup': {
                'status': False,
                'isis_id': 1,
                'algorithm': {
                    'prefix': '1.1.1.100/32',
                    'sid_index': 100,
                    'range': 20
                },
                'entries': 2
            }
        },
        'ospf': {
            'name': 'ospf',
            'active': {
                'status': True,
                'algorithm': {
                    'prefix': '1.1.1.100/32',
                    'sid_index': 100,
                    'range': 20
                },
                'process_id': 1,
                'entries': 2
            },
            'backup': {
                'status': False,
                'algorithm': {
                    'prefix': '1.1.1.100/32',
                    'sid_index': 100,
                    'range': 20
                },
                'process_id': 1,
                'entries': 2
            }
        }
    }


    def test_empty_output(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowSegmentRoutingPrefixSidMap(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed = obj.parse()

    def test_golden_output(self):
        self.maxDiff = None
        self.dev2 = Mock(**self.golden_output)
        obj = ShowSegmentRoutingPrefixSidMap(device = self.dev2)
        parsed = obj.parse()
        self.assertEqual(parsed, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()