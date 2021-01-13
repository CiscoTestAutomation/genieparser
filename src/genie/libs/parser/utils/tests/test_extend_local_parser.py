import os
import unittest
from genie.libs.parser.utils.extension import ExtendParsers
from genie.libs.parser.utils.tests.dummy_parser import package_path

class TestExtendParser(unittest.TestCase):

    def setUp(self):
        os.environ['PYTHONPATH'] += package_path + ':'

    def test_extend_api(self):
        ext = ExtendParsers('dummy_parser')
        ext.extend()
        self.assertEqual(ext.output, 
            {
                'tokens': ['iosxe', 'c9300', 'iosxr'],
                'show inventory': {
                    'iosxe': {
                        'c9300': {
                            'module_name': 'show_platform', 
                            'package': 'dummy_parser', 
                            'class': 'ShowInventory', 
                            'doc': '\n    Parser for :\n        * show inventory\n    ', 
                            'uid': 'show_inventory'
                        }
                    }
                }, 
                'show clock': {
                    'iosxe': {
                        'module_name': 'show_clock', 
                        'package': 'dummy_parser', 
                        'class': 'ShowClock', 
                        'doc': 'Parser for show clock',
                        'uid': 'show_clock'
                    },
                    'iosxr': {
                        'module_name': 'show_clock', 
                        'package': 'dummy_parser', 
                        'class': 'ShowClock', 
                        'doc': 'Parser for show clock', 
                        'uid': 'show_clock'
                    }
                }
            })


if __name__ == '__main__':
    unittest.main()
