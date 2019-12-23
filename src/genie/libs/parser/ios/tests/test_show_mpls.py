# Python
import unittest
from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

from genie.libs.parser.ios.show_mpls import ShowMplsLdpParameters,\
                                            ShowMplsLdpNsrStatistics,\
                                            ShowMplsLdpNeighbor,\
                                            ShowMplsLdpNeighborDetail,\
                                            ShowMplsLdpBindings,\
                                            ShowMplsLdpCapabilities,\
                                            ShowMplsLdpDiscovery,\
                                            ShowMplsLdpIgpSync,\
                                            ShowMplsForwardingTable,\
                                            ShowMplsInterface,\
                                            ShowMplsL2TransportDetail, \
                                            ShowMplsL2TransportVC

# iosxe tests/test_show_mpls
from genie.libs.parser.iosxe.tests.test_show_mpls import \
                            test_show_mpls_ldp_parameters as test_show_mpls_ldp_parameters_iosxe,\
                            test_show_mpls_ldp_nsr_statistics as test_show_mpls_ldp_nsr_statistics_iosxe,\
                            test_show_mpls_ldp_neighbor as test_show_mpls_ldp_neighbor_iosxe,\
                            test_show_mpls_ldp_neighbor_detail as test_show_mpls_ldp_neighbor_detail_iosxe,\
                            test_show_mpls_ldp_bindings as test_show_mpls_ldp_bindings_iosxe,\
                            test_show_mpls_ldp_capabilities as test_show_mpls_ldp_capabilities_iosxe,\
                            test_show_mpls_ldp_discovery as test_show_mpls_ldp_discovery_iosxe,\
                            test_show_mpls_ldp_igp_sync as test_show_mpls_ldp_igp_sync_iosxe,\
                            TestShowMplsForwardingTable as test_show_mpls_forwarding_table_iosxe,\
                            test_show_mpls_interface as test_show_mpls_interface_iosxe, \
                            test_show_mpls_l2transport_vc as test_show_mpls_l2transport_vc_iosxe


class test_show_mpls_ldp_parameters(test_show_mpls_ldp_parameters_iosxe):
    
    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowMplsLdpParameters(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowMplsLdpParameters(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


class test_show_mpls_ldp_nsr_statistics(test_show_mpls_ldp_nsr_statistics_iosxe):
    
    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowMplsLdpParameters(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowMplsLdpNsrStatistics(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class test_show_mpls_ldp_neighbor(test_show_mpls_ldp_neighbor_iosxe):
    
    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowMplsLdpNeighbor(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowMplsLdpNeighbor(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_vrf(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_vrf)
        obj = ShowMplsLdpNeighbor(device=self.dev)
        parsed_output = obj.parse(vrf="vpn10")
        self.assertEqual(parsed_output,self.golden_parsed_output_vrf)


class test_show_mpls_ldp_neighbor_detail(test_show_mpls_ldp_neighbor_detail_iosxe):

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowMplsLdpNeighborDetail(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowMplsLdpNeighborDetail(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


class test_show_mpls_ldp_bindings(test_show_mpls_ldp_bindings_iosxe):
    
    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowMplsLdpBindings(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowMplsLdpBindings(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_all_detail(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_all_detail)
        obj = ShowMplsLdpBindings(device=self.dev)
        parsed_output = obj.parse(all='all',detail="detail")
        self.assertEqual(parsed_output, self.golden_parsed_output_all_detail)

    def test_golden_all(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_all)
        obj = ShowMplsLdpBindings(device=self.dev)
        parsed_output = obj.parse(all='all')
        self.assertEqual(parsed_output, self.golden_parsed_output_all)


class test_show_mpls_ldp_capabilities(test_show_mpls_ldp_capabilities_iosxe):
    
    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowMplsLdpCapabilities(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_all)
        obj = ShowMplsLdpCapabilities(device=self.dev)
        parsed_output = obj.parse(all="all")
        self.assertEqual(parsed_output, self.golden_parsed_output_all)

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowMplsLdpCapabilities(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class test_show_mpls_ldp_discovery(test_show_mpls_ldp_discovery_iosxe):

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowMplsLdpDiscovery(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_all_detail(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_all_detail)
        obj = ShowMplsLdpDiscovery(device=self.dev)
        parsed_output = obj.parse(all="all", detail="detail")
        self.assertEqual(parsed_output, self.golden_parsed_output_all_detail)

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowMplsLdpDiscovery(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_all(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_all)
        obj = ShowMplsLdpDiscovery(device=self.dev)
        parsed_output = obj.parse(all='all')
        self.assertEqual(parsed_output, self.golden_parsed_output_all)


class test_show_mpls_ldp_igp_sync(test_show_mpls_ldp_igp_sync_iosxe):

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowMplsLdpIgpSync(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_all(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_all)
        obj = ShowMplsLdpIgpSync(device=self.dev)
        parsed_output = obj.parse(all='all')
        self.assertEqual(parsed_output, self.golden_parsed_output_all)

    def test_golden_interface(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowMplsLdpIgpSync(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class test_show_mpls_forwarding_table(test_show_mpls_forwarding_table_iosxe):
    
    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowMplsForwardingTable(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowMplsForwardingTable(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_2(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_2)
        obj = ShowMplsForwardingTable(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_3(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_3)
        obj = ShowMplsForwardingTable(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_3)

    def test_golden_4(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_4)
        obj = ShowMplsForwardingTable(device=self.dev)
        parsed_output = obj.parse(prefix='10.16.2.2')
        self.assertEqual(parsed_output, self.golden_parsed_output_4)


class test_show_mpls_interface(test_show_mpls_interface_iosxe):

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowMplsInterface(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_detail(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_detail)
        obj = ShowMplsInterface(device=self.dev)
        parsed_output = obj.parse(detail='detail')
        self.assertEqual(parsed_output, self.golden_parsed_output_detail)

    def test_golden_all(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_all)
        obj = ShowMplsInterface(device=self.dev)
        parsed_output = obj.parse(all='all')
        self.assertEqual(parsed_output, self.golden_parsed_output_all)


class test_show_mpls_l2transport_vc_detail(unittest.TestCase):
    dev = Device(name='dev1')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        'interface': {
            'VFI TEST VFI': {
                'status': 'up',
                'destination_address': {
                    '10.1.1.1': {
                        'vc_id': {
                            '1000': {
                                'vc_status': 'up',
                                },
                            },
                        'output_interface': 'Serial2/0',
                        'imposed_label_stack': '{17}',
                        'preferred_path': 'not configured',
                        'default_path': 'active',
                        'next_hop': 'point2point',
                        },
                    },
                'create_time': '00:04:34',
                'last_status_change_time': '00:04:15',
                'signaling_protocol': {
                    'LDP': {
                        'peer_id': '10.1.1.1:0',
                        'peer_state': 'up',
                        'targeted_hello_ip': '10.1.1.1',
                        'id': '10.1.1.1',
                        'mpls_vc_labels': {
                            'local': '16',
                            'remote': '17',
                            },
                        'group_id': {
                            'local': '0',
                            'remote': '0',
                            },
                        'mtu': {
                            'local': '1500',
                            'remote': '1500',
                            },
                        'mac_withdraw': {
                            'sent': 5,
                            'received': 3,
                            },
                        },
                    },
                'sequencing': {
                    'received': 'disabled',
                    'sent': 'disabled',
                    },
                'statistics': {
                    'packets': {
                        'received': 0,
                        'sent': 0,
                        },
                    'bytes': {
                        'received': 0,
                        'sent': 0,
                        },
                    'packets_drop': {
                        'received': 0,
                        'sent': 0,
                        },
                    },
                },
            },
        }

    golden_output = {'execute.return_value': '''\
        Local interface: VFI TEST VFI up
          MPLS VC type is VFI, interworking type is Ethernet
          Destination address: 10.1.1.1, VC ID: 1000, VC status: up
            Output interface: Se2/0, imposed label stack {17}
            Preferred path: not configured
            Default path: active
            Next hop: point2point
          Create time: 00:04:34, last status change time: 00:04:15
          Signaling protocol: LDP, peer 10.1.1.1:0 up
            Targeted Hello: 10.1.1.1(LDP Id) -> 10.1.1.1
            MPLS VC labels: local 16, remote 17
            Group ID: local 0, remote 0
            MTU: local 1500, remote 1500    
            Remote interface description:
            MAC Withdraw: sent 5, received 3
          Sequencing: receive disabled, send disabled
          VC statistics:
            packet totals: receive 0, send 0
            byte totals:   receive 0, send 0
            packet drops:  receive 0, send 0
    '''}


    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowMplsL2TransportDetail(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowMplsL2TransportDetail(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


# ============================================
# unit test for 'show mpls l2transport vc'
# ============================================
class test_show_mpls_l2transport_vc(test_show_mpls_l2transport_vc_iosxe):

    def test_empty(self):
            self.device = Mock(**self.empty_output)
            obj = ShowMplsL2TransportVC(device=self.device)
            with self.assertRaises(SchemaEmptyParserError):
                parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowMplsL2TransportVC(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowMplsL2TransportVC(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_2)

    def test_golden_3(self):
        self.device = Mock(**self.golden_output_3)
        obj = ShowMplsL2TransportVC(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_3)

if __name__ == '__main__':
    unittest.main()
