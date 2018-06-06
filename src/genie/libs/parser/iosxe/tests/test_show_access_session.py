#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError

from genie.libs.parser.iosxe.show_access_session import ShowAccessSession


class test_show_access_session(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        'session_count': 1,
        'interfaces': {
            'GigabitEthernet1/0/1': {
                'interface': 'GigabitEthernet1/0/1',
                'client': {
                    'f4cf.beef.acc1': {
                        'client': 'f4cf.beef.acc1',
                        'method': 'dot1x',
                        'domain': 'DATA',
                        'status': 'authenticator',
                        'session': {
                            '000000000000000BB6FC9EAF': {
                                'session_id': '000000000000000BB6FC9EAF',
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        Interface                MAC Address    Method  Domain  Status Fg  Session ID
        --------------------------------------------------------------------------------------------
        Gi1/0/1                  f4cf.beef.acc1 dot1x   DATA    Auth        000000000000000BB6FC9EAF

        Session count = 1
    '''
    }
    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowAccessSession(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowAccessSession(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()

