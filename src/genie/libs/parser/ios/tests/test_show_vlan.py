import re
import unittest
from unittest.mock import Mock

from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.ios.show_vlan import ShowVlan, \
                                          ShowVlanMtu, \
                                          ShowVlanAccessMap, \
                                          ShowVlanRemoteSpan, \
                                          ShowVlanFilter
from genie.libs.parser.iosxe.tests.test_show_vlan import test_show_vlan as test_show_vlan_iosxe,\
                                                         test_show_vlan_mtu as test_show_vlan_mtu_iosxe,\
                                                         test_show_vlan_remote_span as test_show_vlan_remote_span_iosxe,\
                                                         test_show_vlan_access_map as test_show_vlan_access_map_iosxe,\
                                                         test_show_vlan_filter as test_show_vlan_filter_iosxe

# ============================================
# unit test for 'show vlan'
# =============================================
class test_show_vlan(test_show_vlan_iosxe):

    device = Device(name='aDevice')

    def test_empty_1(self):
        self.device = Mock(**self.empty_output)
        obj = ShowVlan(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_vlan_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_vlan_1)
        obj = ShowVlan(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_vlan_1)

class test_show_vlan_mtu(test_show_vlan_mtu_iosxe):

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        vlan_obj = ShowVlanMtu(device=self.device)
        parsed_output = vlan_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        vlan_obj = ShowVlanMtu(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = vlan_obj.parse()

    def test_missing_parsed_key(self):
        self.device = Mock(**self.silver_output)
        vlan_obj = ShowVlanMtu(device=self.device)
        with self.assertRaises(Exception):
            parsed_output = vlan_obj.parse()

class test_show_vlan_remote_span(test_show_vlan_remote_span_iosxe):

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        vlan_obj = ShowVlanRemoteSpan(device=self.device)
        parsed_output = vlan_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        vlan_obj = ShowVlanRemoteSpan(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = vlan_obj.parse()

class test_show_vlan_access_map(test_show_vlan_access_map_iosxe):

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        vlan_obj = ShowVlanAccessMap(device=self.device)
        parsed_output = vlan_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        vlan_obj = ShowVlanAccessMap(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = vlan_obj.parse()

class test_show_vlan_filter(test_show_vlan_filter_iosxe):
    def test_golden(self):
        self.device = Mock(**self.golden_output)
        vlan_obj = ShowVlanFilter(device=self.device)
        parsed_output = vlan_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        vlan_obj = ShowVlanFilter(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = vlan_obj.parse()


if __name__ == '__main__':
    unittest.main()