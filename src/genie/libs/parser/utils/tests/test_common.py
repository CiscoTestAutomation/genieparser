import unittest

from genie.libs.parser.utils.common import Common
from  genie.libs.parser.utils.common import check_for_duplicate
from genie.abstract.package import AbstractTree, DEFAULT_ABSTRACT_ORDER
PARSER_MODULE_NAME = 'genie.libs.parser'

internal = {
    'show clock': {
        'folders': {
            'iosxe': {
                'class':
                'ShowClock',
                'doc':
                'Parser for show clock',
                'module_name':
                'iosxe.show_clock',
                'package':
                'genie.libs.parser.utils.tests.dummy_parser',
                'schema':
                '{\n'
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
                'uid':
                'show_clock',
                'url':
                'https://github.com/CiscoTestAutomation/genieparser/tree/master/src/iosxe/show_clock.py#L25'
            },
            'iosxr': {
                'class':
                'ShowClock',
                'doc':
                'Parser for show clock',
                'module_name':
                'iosxr.show_clock',
                'package':
                'genie.libs.parser.utils.tests.dummy_parser',
                'schema':
                '{\n'
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
                'uid':
                'show_clock',
                'url':
                'https://github.com/CiscoTestAutomation/genieparser/tree/master/src/iosxr/show_clock.py#L26'
            }
        }
    },
    'show inventory': {
        'folders': {
            'iosxe': {
                'folders': {
                    'c9300': {
                        'class':
                        'ShowInventory',
                        'doc':
                        '\n'
                        '    Parser for :\n'
                        '        * show inventory\n'
                        '    ',
                        'module_name':
                        'iosxe.c9300.show_platform',
                        'package':
                        'genie.libs.parser.utils.tests.dummy_parser',
                        'schema':
                        '{\n'
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
                        'uid':
                        'show_inventory',
                        'url':
                        'https://github.com/CiscoTestAutomation/genieparser/tree/master/src/iosxe/c9300/show_platform.py#L30'
                    }
                },
                'tokens': {
                    'os': 'iosxe'
                }
            }
        }
    },
    'show vrf': {
        'folders': {
            'ios': {
                'class':
                'ShowVrf',
                'doc':
                'Parser for show vrf',
                'module_name':
                'ios.show_vrf',
                'package':
                'genie.libs.parser',
                'schema':
                '{\n'
                "    'vrf': {\n"
                "        Any('*'): {\n"
                "            Optional('route_distinguisher'): "
                'str,\n'
                '            '
                "Optional('route_distinguisher_auto'): bool,\n"
                "            Optional('protocols'): list,\n"
                "            Optional('interfaces'): list,\n"
                "            Optional('being_deleted'): bool,\n"
                '        },\n'
                '    },\n'
                '}',
                'tokens': {
                    'os': 'ios'
                },
                'uid':
                'show_vrf',
                'url':
                'https://github.com/CiscoTestAutomation/genieparser/tree/master/src/genie/libs/parser/ios/show_vrf.py#L22'
            },
            'iosxe': {
                'class':
                'ShowVrf',
                'doc':
                ' Parser for:\n'
                '            show vrf\n'
                '            show vrf {vrf}\n'
                '    ',
                'module_name':
                'iosxe.show_vrf',
                'package':
                'genie.libs.parser',
                'schema':
                '{\n'
                "    'vrf': {\n"
                "        Any('*'): {\n"
                "            Optional('route_distinguisher'): "
                'str,\n'
                '            '
                "Optional('route_distinguisher_auto'): bool,\n"
                "            Optional('protocols'): list,\n"
                "            Optional('interfaces'): list,\n"
                "            Optional('being_deleted'): "
                'bool,\n'
                '        },\n'
                '    },\n'
                '}',
                'tokens': {
                    'os': 'iosxe'
                },
                'uid':
                'show_vrf',
                'url':
                'https://github.com/CiscoTestAutomation/genieparser/tree/master/src/genie/libs/parser/iosxe/show_vrf.py#L44'
            },
            'nxos': {
                'class':
                'ShowVrf',
                'doc':
                'Parser for show vrf',
                'module_name':
                'nxos.show_vrf',
                'package':
                'genie.libs.parser',
                'schema':
                '{\n'
                "    'vrfs': {\n"
                "        Any('*'): {\n"
                "            'vrf_id': int,\n"
                "            'vrf_state': str,\n"
                "            'reason': str,\n"
                '        },\n'
                '    },\n'
                '}',
                'tokens': {
                    'os': 'nxos'
                },
                'uid':
                'show_vrf',
                'url':
                'https://github.com/CiscoTestAutomation/genieparser/tree/master/src/genie/libs/parser/nxos/show_vrf.py#L35'
            }
        }
    },
    'tokens': {
        'os': ['iosxe', 'iosxr', 'nxos', 'ios'],
        'platform': ['c9300']
    },
    'token_order': [
        'origin', 'os', 'platform', 'model', 'submodel', 'pid', 'version',
        'os_flavor', 'revision'
    ]
}

external = {
    'show vrf': {
        'folders': {
            'external_parser': {
                'folders': {
                    'iosxe': {
                        'class':
                        'ShowVrf',
                        'doc':
                        ' Parser for:\n'
                        '            '
                        'show vrf\n'
                        '            '
                        'show vrf {vrf}\n'
                        '    ',
                        'module_name':
                        'iosxe.show_vrf',
                        'package':
                        'external_parser',
                        'schema':
                        '{\n'
                        "    'vrf': "
                        '{\n'
                        '        '
                        "Any('*'): {\n"
                        '            '
                        "Optional('route_distinguisher'): "
                        'str,\n'
                        '            '
                        "Optional('route_distinguisher_auto'): "
                        'bool,\n'
                        '            '
                        "Optional('protocols'): "
                        'list,\n'
                        '            '
                        "Optional('interfaces'): "
                        'list,\n'
                        '            '
                        "Optional('being_deleted'): "
                        'bool,\n'
                        '        },\n'
                        '    },\n'
                        '}',
                        'tokens': {
                            'os': 'iosxe'
                        },
                        'uid':
                        'show_vrf',
                        'url':
                        'https://github.com/CiscoTestAutomation/genieparser/tree/master/src/iosxe/show_vrf.py#L60'
                    }
                },
                'tokens': {
                    'origin': 'external'
                }
            }
        }
    },
    'tokens': {
        'os': ['iosxe'],
    },
    'token_order': [
        'origin', 'os', 'platform', 'model', 'submodel', 'pid', 'version',
        'os_flavor', 'revision'
    ],
}
class TestCommon(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_interface_converter(self):
        name = self.common.convert_intf_name('Fa1')
        self.assertEqual(name, 'FastEthernet1')

    def test_interface_converter_ignore_case(self):
        name = self.common.convert_intf_name('fa1', ignore_case=True)
        self.assertEqual(name, 'FastEthernet1')


class TestDuplicate(unittest.TestCase):
    def test_check_for_duplicate(self):

        internal_data = AbstractTree.from_json(internal,
                                                package=PARSER_MODULE_NAME,
                                                feature='parser')
        external_data = AbstractTree.from_json(external,
                                                package=PARSER_MODULE_NAME,
                                                feature='parser')

        internal_data.update(external_data)
        
        duplicates = check_for_duplicate(internal_data)
        self.assertIn('show vrf', duplicates)
