# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
    SchemaMissingKeyError

# iosxe show_lisp
from genie.libs.parser.nxos.show_lag import ShowFeature


# =================================
# Unit test for 'show feature'
# =================================
class test_show_feature(unittest.TestCase):
    """unit test for show feature"""
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        Feature Name          Instance  State
    --------------------  --------  --------
    bash-shell             1          disabled
    eigrp                  1          disabled
    eigrp                  2          disabled
    lacp                   1          enabled
    '''
                     }
    golden_parsed_output = {'features': {
        'bash-shell': {
            'instances': {
                '1': False
            }
        },
        'eigrp': {
            'instances': {
                '1': False,
                '2': False
            }
        },
        'lacp': {
            'instances': {
                '1': True
            }
        }
    }
    }

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowFeature(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowFeature(device=self.device)
        parsed_output = obj.parse()

        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()
