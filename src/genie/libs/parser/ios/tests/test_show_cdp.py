# Python
import unittest
from unittest.mock import Mock
# iosxe tests/test_show_cdp
from genie.libs.parser.iosxe.tests.test_show_cdp import test_show_cdp_neighbors as test_show_cdp_neighbors_iosxe,\
 test_show_cdp_neighbors_detail as test_show_cdp_neighbors_detail_iosxe

# Parser
from genie.libs.parser.ios.show_cdp import ShowCdpNeighbors, \
                                           ShowCdpNeighborsDetail


# ==================================
# Unit test for 'show cdp neighbors'
# ==================================
from genie.metaparser import SchemaEmptyParserError


class TestShowCdpNeighbors(test_show_cdp_neighbors_iosxe):

    @classmethod
    def setUpClass(cls) -> None:
        cls.maxDiff = None

    def test_show_cdp_neighbors_1(self):

        self.device = Mock(**self.device_output_1)
        obj = ShowCdpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_1)

    def test_show_cdp_neighbors_2(self):

        self.device = Mock(**self.device_output_2)
        obj = ShowCdpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_2)

    def test_show_cdp_neighbors_3(self):

        self.device = Mock(**self.device_output_3)
        obj = ShowCdpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_3)

    def test_show_cdp_neighbors_4(self):

        self.device = Mock(**self.device_output_4)
        obj = ShowCdpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_4)

    def test_show_cdp_neighbors_5(self):

        self.device = Mock(**self.device_output_5)
        obj = ShowCdpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_5)

class TestShowCdpNeighborsDetail(test_show_cdp_neighbors_detail_iosxe):

    @classmethod
    def setUpClass(cls) -> None:
        cls.maxDiff = None

    def test_show_cdp_neighbors_detail_1(self):

        self.device = Mock(**self.device_output_1)
        obj = ShowCdpNeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_1)

    def test_show_cdp_neighbors_detail_2(self):

        self.device = Mock(**self.device_output_2)
        obj = ShowCdpNeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_2)

    def test_show_cdp_neighbors_detail_3(self):

        self.device = Mock(**self.device_output_3)
        obj = ShowCdpNeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_3)

    def test_show_cdp_neighbors_detail_empty(self):

        self.device = Mock(**self.device_output_4_empty)
        obj = ShowCdpNeighborsDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_cdp_neighbors_detail_4(self):

        self.device = Mock(**self.device_output_5)
        obj = ShowCdpNeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_5)


if __name__ == '__main__':
    unittest.main()
