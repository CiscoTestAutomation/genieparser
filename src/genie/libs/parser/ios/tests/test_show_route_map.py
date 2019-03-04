import unittest
from unittest.mock import Mock

from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError

from genie.libs.parser.ios.show_route_map import ShowRouteMapAll
from genie.libs.parser.iosxe.tests.test_show_route_map import test_show_route_map as test_show_route_map_iosxe

class test_show_route_map(test_show_route_map_iosxe):

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        route_map_obj = ShowRouteMapAll(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = route_map_obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        route_map_obj = ShowRouteMapAll(device=self.device)
        parsed_output = route_map_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()
