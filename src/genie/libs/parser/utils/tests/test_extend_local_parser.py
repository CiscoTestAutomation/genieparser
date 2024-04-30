import os
import sys
import unittest
from genie.libs.parser.utils.common import _load_parser_json, ExtendParsers
from genie.libs.parser.utils.tests.dummy_parser import package_path

class TestExtendParser(unittest.TestCase):

    def setUp(self):
        if package_path not in sys.path:
            sys.path.append(package_path)

    def test_extend_api(self):
        ext = ExtendParsers('genie.libs.parser.utils.tests.dummy_parser')
        ext.extend()
        ext.output.pop('extend_info')

        self.assertEqual(ext.output,
            {
                'show clock': {
                    'folders': {
                        'iosxe': {
                            'class': 'ShowClock',
                            'doc': 'Parser for show clock',
                            'module_name': 'iosxe.show_clock',
                            'package': 'genie.libs.parser.utils.tests.dummy_parser',
                            'schema': '{\n'
                                    "    'timezone': str,\n"
                                    "    'day': str,\n"
                                    "    'day_of_week': str,\n"
                                    "    'month': str,\n"
                                    "    'year': str,\n"
                                    "    'time': str,\n"
                                    '}',
                            'tokens': {
                                'os': 'iosxe'
                            },
                            'uid': 'show_clock',
                            'url': 'https://github.com/CiscoTestAutomation/genieparser/tree/master/src/iosxe/show_clock.py#L25'
                        },
                        'iosxr': {
                            'class': 'ShowClock',
                            'doc': 'Parser for show clock',
                            'module_name': 'iosxr.show_clock',
                            'package': 'genie.libs.parser.utils.tests.dummy_parser',
                            'schema': '{\n'
                                    "    'timezone': str,\n"
                                    "    'day': str,\n"
                                    "    'day_of_week': str,\n"
                                    "    'month': str,\n"
                                    "    'year': str,\n"
                                    "    'time': str,\n"
                                    '}',
                            'tokens': {
                                'os': 'iosxr'
                            },
                            'uid': 'show_clock',
                            'url': 'https://github.com/CiscoTestAutomation/genieparser/tree/master/src/iosxr/show_clock.py#L26'
                        }
                    }
                },
                'show inventory': {
                    'folders': {
                        'iosxe': {
                            'folders': {
                                'c9300': {
                                    'class': 'ShowInventory',
                                    'doc': '\n'
                                        '    Parser for :\n'
                                        '        * show inventory\n'
                                        '    ',
                                    'module_name': 'iosxe.c9300.show_platform',
                                    'package': 'genie.libs.parser.utils.tests.dummy_parser',
                                    'schema': '{\n'
                                            "    'index': {\n"
                                            "        Any('*'): {\n"
                                            "            'name': str,\n"
                                            "            'descr': str,\n"
                                            "            Optional('pid'): str,\n"
                                            "            Optional('vid'): str,\n"
                                            "            Optional('sn'): str,\n"
                                            "        },\n"
                                            "    },\n"
                                            "}",
                                    'tokens': {
                                        'platform': 'c9300'
                                    },
                                    'uid': 'show_inventory',
                                    'url': 'https://github.com/CiscoTestAutomation/genieparser/tree/master/src/iosxe/c9300/show_platform.py#L30'
                                }
                            },
                            'tokens': {
                                'os': 'iosxe'
                            }
                        }
                    }
                },
                'tokens': {
                    'os': ['iosxe', 'iosxr'],
                    'platform': ['c9300']
                },
                'token_order': [
                    'origin',
                    'os',
                    'platform',
                    'model',
                    'submodel',
                    'pid',
                    'version',
                    'os_flavor',
                    'revision'
                ]
            })

if __name__ == '__main__':
    unittest.main()
