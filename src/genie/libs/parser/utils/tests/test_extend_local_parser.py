import os
import sys
import unittest
from genie.libs.parser.utils.common import _load_parser_json
from genie.libs.parser.utils.tests.dummy_parser import package_path

class TestExtendParser(unittest.TestCase):

    def setUp(self):
        if package_path not in sys.path:
            sys.path.append(package_path)

    def test_extend_api(self):
        os.environ['PYATS_LIBS_EXTERNAL_PARSER'] = 'genie.libs.parser.utils.tests.dummy_parser'
        parser_data = _load_parser_json()
        self.maxDiff = None

        show_inv = parser_data.pop('show inventory', {}).get('iosxe', {}).get('c9300')
        show_clock = parser_data.pop('show clock', {})

        # remove urls as they have dynamic line numbers
        show_inv.pop('url')
        show_clock['ios'].pop('url')
        show_clock['iosxe'].pop('url')

        data = {
            'show inventory': {'iosxe': {'c9300': show_inv}},
            'show clock': show_clock
        }

        expected = {
            "show inventory": {
                "iosxe": {
                    "c9300": {
                        "class": "ShowInventory",
                        "doc": "\n    Parser for :\n        * show inventory\n    ",
                        "module_name": "show_platform",
                        "package": "genie.libs.parser.utils.tests.dummy_parser",
                        "schema": "{\n'index': {\n  Any  (str) *: {\n    'name': <class 'str'>,\n    'descr': <class 'str'>,\n    Optional  (str) pid: <class 'str'>,\n    Optional  (str) vid: <class 'str'>,\n    Optional  (str) sn: <class 'str'>,\n    },\n  },\n}",
                        "uid": "show_inventory"
                    }
                }
            },
            "show clock": {
                "ios": {
                    "class": "ShowClock",
                    "doc": "Parser for show clock",
                    "module_name": "show_system",
                    "package": "genie.libs.parser",
                    "schema": "{\n'timezone': <class 'str'>,\n'day': <class 'str'>,\n'day_of_week': <class 'str'>,\n'month': <class 'str'>,\n'year': <class 'str'>,\n'time': <class 'str'>,\n}",
                    "uid": "show_clock"
                },
                "iosxe": {
                    "class": "ShowClock",
                    "doc": "Parser for show clock",
                    "module_name": "show_clock",
                    "package": "genie.libs.parser.utils.tests.dummy_parser",
                    "schema": "{\n'timezone': <class 'str'>,\n'day': <class 'str'>,\n'day_of_week': <class 'str'>,\n'month': <class 'str'>,\n'year': <class 'str'>,\n'time': <class 'str'>,\n}",
                    "uid": "show_clock"
                },
                "iosxr": {
                    "module_name": "show_clock",
                    "package": "genie.libs.parser.utils.tests.dummy_parser",
                    "class": "ShowClock",
                    "doc": "Parser for show clock",
                    "uid": "show_clock"
                }
            }
        }

        self.assertEqual(data, expected)


if __name__ == '__main__':
    unittest.main()
