# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_mrib
from genie.libs.parser.iosxr.show_l2route import (ShowL2routeTopology, ShowL2routeEvpnMacAll)


# ===========================================
#  Unit test for 'show l2route topology'
# ===========================================
class TestShowL2RouteTopology(unittest.TestCase):
    """Unit test for 'show l2route topology'"""

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    expected_output = {
        'topology 1': {
            'topo_id': {
                '0': {
                    'topo_name': {
                        'EVPN-Multicast-BTV': {
                            'topo_type': 'L2VRF'}}}}
        },
        'topology 2': {
            'topo_id': {
                '4294967294': {
                    'topo_name': {
                        'GLOBAL': {
                            'topo_type': 'N/A'}}}}
        },
        'topology 3': {
            'topo_id': {
                '4294967295': {
                    'topo_name': {
                        'ALL': {
                            'topo_type': 'N/A'}}}}
        }
    }

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

    # expected_output =

    device_output = {'execute.return_value': '''
        Topo ID  Mac Address    Producer    Next Hop(s)                             
        -------- -------------- ----------- ----------------------------------------
        0        0012.0100.0001 L2VPN       172.16.2.89/100001/ME                   
        0        0012.0100.0002 L2VPN       172.16.2.89/100001/ME                   
        0        0012.0100.0003 L2VPN       172.16.2.89/100001/ME                   
        0        0012.0100.0004 L2VPN       172.16.2.89/100001/ME                   
        0        0012.0100.0005 L2VPN       172.16.2.89/100001/ME                   
        0        0012.0100.0006 L2VPN       172.16.2.89/100001/ME                   
        0        0012.0100.0007 L2VPN       172.16.2.89/100001/ME                   
        0        0012.0100.0008 L2VPN       172.16.2.89/100001/ME                   
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

        import pprint
        pprint.pprint(parsed_output)
        import pdb
        pdb.set_trace()

        self.assertEqual(parsed_output, self.expected_output)

if __name__ == '__main__':
    unittest.main()
