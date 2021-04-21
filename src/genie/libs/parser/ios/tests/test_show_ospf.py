
# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# iosxe show_ospf
from genie.libs.parser.ios.show_ospf import ShowIpOspf,\
                                   ShowIpOspfInterface,\
                                   ShowIpOspfNeighborDetail,\
                                   ShowIpOspfShamLinks,\
                                   ShowIpOspfVirtualLinks

from genie.libs.parser.iosxe.tests.test_show_ospf import test_show_ip_ospf_interface as test_show_ip_ospf_interface_iosxe,\
 test_show_ip_ospf_neighbor_detail as test_show_ip_ospf_neighbor_detail_iosxe,\
 test_show_ip_ospf_sham_links as test_show_ip_ospf_sham_links_iosxe,\
 test_show_ip_ospf_virtual_links as test_show_ip_ospf_virtual_links_iosxe


# ======================================
# Unit test for 'show ip ospf interface'
# ======================================
class test_show_ip_ospf_interface(test_show_ip_ospf_interface_iosxe):

    def test_show_ip_ospf_interface_full1(self):
        super().test_show_ip_ospf_interface_full1()

        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper

        obj = ShowIpOspfInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_interface_full2(self):
        super().test_show_ip_ospf_interface_full2()

        self.maxDiff = None
        def mapper(key):
            return self.outputs[key]

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper

        obj = ShowIpOspfInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_ip_ospf_interface_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ============================================
# Unit test for 'show ip ospf neighbor detail'
#============================================
class test_show_ip_ospf_neighbor_detail(test_show_ip_ospf_neighbor_detail_iosxe):

    def test_show_ip_ospf_neighbor_detail_full1(self):
        super().test_show_ip_ospf_neighbor_detail_full1()
        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]


        self.device.execute = Mock()
        self.device.execute.side_effect = mapper

        obj = ShowIpOspfNeighborDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_neighbor_detail_full2(self):
        super().test_show_ip_ospf_neighbor_detail_full2()

        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper

        obj = ShowIpOspfNeighborDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_ip_ospf_neighbor_detail_full3(self):
        super().test_show_ip_ospf_neighbor_detail_full3()

        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]


        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        obj = ShowIpOspfNeighborDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_ip_ospf_neighbor_detail_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfNeighborDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# =======================================
# Unit test for 'show ip ospf sham-links'
# =======================================
class test_show_ip_ospf_sham_links(test_show_ip_ospf_sham_links_iosxe):

    def test_show_ip_ospf_sham_links_full1(self):
        super().test_show_ip_ospf_sham_links_full1()
        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper

        obj = ShowIpOspfShamLinks(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_sham_links_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfShamLinks(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ==========================================
# Unit test for 'show ip ospf virtual-links'
# ==========================================
class test_show_ip_ospf_virtual_links(test_show_ip_ospf_virtual_links_iosxe):

    golden_parsed_output1 = {
        'vrf': 
            {'VRF1': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'2': 
                                {'areas': 
                                    {'0.0.0.1': 
                                        {'virtual_links': 
                                            {'0.0.0.1 10.36.3.3': 
                                                {'adjacency_state': 'full',
                                                'dcbitless_lsa_count': 7,
                                                'dead_interval': 40,
                                                'demand_circuit': True,
                                                'donotage_lsa': 'not allowed',
                                                'first': '0x0(0)/0x0(0)',
                                                'hello_interval': 10,
                                                'hello_timer': '00:00:08',
                                                'index': '1/3',
                                                'interface': 'GigabitEthernet0/1',
                                                'last_retransmission_max_length': 0,
                                                'last_retransmission_max_scan': 0,
                                                'last_retransmission_scan_length': 0,
                                                'last_retransmission_scan_time': 0,
                                                'link_state': 'up',
                                                'name': 'VL0',
                                                'next': '0x0(0)/0x0(0)',
                                                'retrans_qlen': 0,
                                                'retransmit_interval': 5,
                                                'router_id': '10.36.3.3',
                                                'state': 'point-to-point,',
                                                'topology': 
                                                    {0: 
                                                        {'cost': 1,
                                                        'disabled': False,
                                                        'name': 'Base',
                                                        'shutdown': False}},
                                                'total_retransmission': 0,
                                                'transit_area_id': '0.0.0.1',
                                                'transmit_delay': 1,
                                                'wait_interval': 40}}}}}}}}}}}

    def test_show_ip_ospf_virtual_links_full1(self):
        super().test_show_ip_ospf_virtual_links_full1()
        
        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        
        obj = ShowIpOspfVirtualLinks(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_sham_links_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfVirtualLinks(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

if __name__ == '__main__':
    unittest.main()
