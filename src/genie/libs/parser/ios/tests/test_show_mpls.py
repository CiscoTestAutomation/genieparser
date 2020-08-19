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


if __name__ == '__main__':
    unittest.main()
