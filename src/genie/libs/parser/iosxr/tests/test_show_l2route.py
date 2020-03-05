# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_l2route
from genie.libs.parser.iosxr.show_l2route import (
    ShowL2routeTopology, ShowL2routeEvpnMacAll, ShowL2routeEvpnMacIpAll)


# ===========================================
#  Unit test for 'show l2route topology'
# ===========================================
class TestShowL2RouteTopology(unittest.TestCase):
    """Unit test for 'show l2route topology'"""

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    expected_output = {
        'topo_id': {
            '0': {
                'topo_name': {
                    'EVPN-Multicast-BTV': {
                        'topo_type': 'L2VRF'}}},
            '4294967294': {
                'topo_name': {
                    'GLOBAL': {
                        'topo_type': 'N/A'}}},
            '4294967295': {
                'topo_name': {
                    'ALL': {
                        'topo_type': 'N/A'}}}}}
    device_output = {'execute.return_value': '''
        RP/0/RP0/CPU0:router# show l2route topology

        Topology ID   Topology Name    Type
        -----------   -------------    ----
        0              EVPN-Multicast-BTV    L2VRF
        4294967294     GLOBAL           N/A
        4294967295     ALL              N/A
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowL2routeTopology(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output)
        obj = ShowL2routeTopology(device=self.device)

        parsed_output = obj.parse()

        self.assertEqual(parsed_output, self.expected_output)


# ===========================================
#  Unit test for 'show l2route evpn mac all'
# ===========================================


class TestShowL2RouteEvpnMacAll(unittest.TestCase):
    """Unit test for 'show l2route evpn mac all'"""

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    expected_output = {
        'topo_id': {
            '0': {
                'mac_address': {
                    '0012.01ff.0001': {
                        'producer': 'L2VPN',
                        'next_hop': '172.16.2.89/100001/ME'},
                    '0012.01ff.0002': {
                        'producer': 'L2VPN',
                        'next_hop': '172.16.2.89/100001/ME'},
                    '0012.01ff.0003': {
                        'producer': 'L2VPN',
                        'next_hop': '172.16.2.89/100001/ME'},
                    '0012.01ff.0004': {
                        'producer': 'L2VPN',
                        'next_hop': '172.16.2.89/100001/ME'},
                    '0012.01ff.0005': {
                        'producer': 'L2VPN',
                        'next_hop': '172.16.2.89/100001/ME'},
                    '0012.01ff.0006': {
                        'producer': 'L2VPN',
                        'next_hop': '172.16.2.89/100001/ME'},
                    '0012.01ff.0007': {
                        'producer': 'L2VPN',
                        'next_hop': '172.16.2.89/100001/ME'},
                    '0012.01ff.0008': {
                        'producer': 'L2VPN',
                        'next_hop': '172.16.2.89/100001/ME'}}}}}

    device_output = {'execute.return_value': '''
        Topo ID  Mac Address    Producer    Next Hop(s)
        -------- -------------- ----------- ----------------------------------------
        0        0012.01ff.0001 L2VPN       172.16.2.89/100001/ME
        0        0012.01ff.0002 L2VPN       172.16.2.89/100001/ME
        0        0012.01ff.0003 L2VPN       172.16.2.89/100001/ME
        0        0012.01ff.0004 L2VPN       172.16.2.89/100001/ME
        0        0012.01ff.0005 L2VPN       172.16.2.89/100001/ME
        0        0012.01ff.0006 L2VPN       172.16.2.89/100001/ME
        0        0012.01ff.0007 L2VPN       172.16.2.89/100001/ME
        0        0012.01ff.0008 L2VPN       172.16.2.89/100001/ME
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowL2routeEvpnMacAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output)
        obj = ShowL2routeEvpnMacAll(device=self.device)
        parsed_output = obj.parse()

        self.assertEqual(parsed_output, self.expected_output)


class TestShowL2routeEvpnMacIpAll(unittest.TestCase):
    """Unit test for 'show l2route evpn mac-ip all'"""

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    expected_output = {
        'topo_id': {
            '0': {
                'mac_address': {
                    '0001.00ff.0307': {
                        'ip_address': {
                            '10.1.0.250': {
                                'next_hop': 'N/A',
                                'producer': 'LOCAL'},
                            '2001:db8::250': {
                                'next_hop': 'N/A',
                                'producer': 'LOCAL'}}},
                    '0aaa.0bff.bbbb': {
                        'ip_address': {
                            '10.1.0.3': {
                                'next_hop': 'N/A',
                                'producer': 'LOCAL'}}},
                    '0aaa.0bff.bbbc': {
                        'ip_address': {
                            '10.1.0.4': {
                                'next_hop': 'N/A',
                                'producer': 'LOCAL'}}},
                    'fc00.00ff.0107': {
                        'ip_address': {
                            '192.168.166.3': {
                                'next_hop': 'Bundle-Ether1.0',
                                'producer': 'L2VPN'}}},
                    'fc00.00ff.0109': {
                        'ip_address': {
                            '192.168.49.3': {
                                'next_hop': '68101/I/ME',
                                'producer': 'L2VPN'}}}}}}}

    device_output = {'execute.return_value': '''
        Topo ID  Mac Address    IP Address      Producer    Next Hop(s)
        -------- -------------- --------------- ----------- ----------------------------------------
        0        0001.00ff.0307 10.1.0.250    LOCAL       N/A
        0        0001.00ff.0307 2001:db8::250   LOCAL       N/A
        0        0aaa.0bff.bbbb 10.1.0.3      LOCAL       N/A
        0        0aaa.0bff.bbbc 10.1.0.4      LOCAL       N/A
        0        fc00.00ff.0107 192.168.166.3   L2VPN  Bundle-Ether1.0
        0        fc00.00ff.0109 192.168.49.3    L2VPN  68101/I/ME
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowL2routeEvpnMacIpAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output)
        obj = ShowL2routeEvpnMacIpAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_output)


if __name__ == '__main__':
    unittest.main()
