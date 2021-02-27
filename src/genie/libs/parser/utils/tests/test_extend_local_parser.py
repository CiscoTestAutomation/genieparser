import os
import unittest
from genie.libs.parser.utils.extension import ExtendParsers
from genie.libs.parser.utils.tests.dummy_parser import package_path

class TestExtendParser(unittest.TestCase):

    def setUp(self):
        python_path = os.environ.get('PYTHONPATH', None)
        if python_path:
            os.environ['PYTHONPATH'] += package_path + ':'
        else:
            os.environ['PYTHONPATH'] = package_path + ':'

    def test_extend_api(self):
        ext = ExtendParsers('genie.libs.parser.utils.tests.dummy_parser')
        ext.extend()
        ext.output.pop('tokens')
        ext.output.pop('extend_info')

        self.assertEqual(ext.output, 
            {
                'show inventory': {
                    'iosxe': {
                        'c9300': {
                            'module_name': 'show_platform', 
                            'package': 'genie.libs.parser.utils.tests.dummy_parser', 
                            'class': 'ShowInventory', 
                            'doc': '\n    Parser for :\n        * show inventory\n    ', 
                            'uid': 'show_inventory'
                        }
                    }
                }, 
                'show clock': {
                    'iosxe': {
                        'module_name': 'show_clock', 
                        'package': 'genie.libs.parser.utils.tests.dummy_parser', 
                        'class': 'ShowClock', 
                        'doc': 'Parser for show clock',
                        'uid': 'show_clock'
                    },
                    'iosxr': {
                        'module_name': 'show_clock', 
                        'package': 'genie.libs.parser.utils.tests.dummy_parser', 
                        'class': 'ShowClock', 
                        'doc': 'Parser for show clock', 
                        'uid': 'show_clock'
                    }
                }
            })


if __name__ == '__main__':
    unittest.main()
