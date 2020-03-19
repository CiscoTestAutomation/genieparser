import unittest
from unittest.mock import Mock

# pyATS
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.asa.show_resource import ShowResourceUsage


# ============================================
# unit test for 'show resource usage'
# =============================================
class TestShowResourceUsage(unittest.TestCase):
    """    unit test for
            * show resource usage
    """
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    # show resource usage
    golden_output = {'execute.return_value': '''
    Resource              Current         Peak      Limit        Denied Context
    SSH                         1            5          5             0 System
    ASDM                        1            1          5             0 System
    Syslogs [rate]             18          861        N/A             0 System
    Conns                  176981      1999939    2000000      16815496 System
    Xlates                   9873        70234        N/A             0 System
    Hosts                   56874      1996513        N/A             0 System
    Conns [rate]             1227       103095        N/A             0 System
    Inspects [rate]           435        88557        N/A             0 System
    '''}

    golden_parsed_output = {
        'context': {
            'System': {
                'resource': {
                    'ASDM': {
                        'current': 1,
                        'denied': 0,
                        'limit': 5,
                        'peak': 1,
                    },
                    'Conns': {
                        'current': 176981,
                        'denied': 16815496,
                        'limit': 2000000,
                        'peak': 1999939,
                    },
                    'Conns [rate]': {
                        'current': 1227,
                        'denied': 0,
                        'peak': 103095,
                    },
                    'Hosts': {
                        'current': 56874,
                        'denied': 0,
                        'peak': 1996513,
                    },
                    'Inspects [rate]': {
                        'current': 435,
                        'denied': 0,
                        'peak': 88557,
                    },
                    'SSH': {
                        'current': 1,
                        'denied': 0,
                        'limit': 5,
                        'peak': 5,
                    },
                    'Syslogs [rate]': {
                        'current': 18,
                        'denied': 0,
                        'peak': 861,
                    },
                    'Xlates': {
                        'current': 9873,
                        'denied': 0,
                        'peak': 70234,
                    },
                },
            },
        },
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowResourceUsage(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj_context = ShowResourceUsage(device=self.device)
        parsed_output = obj_context.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()