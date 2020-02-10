# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
											 SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxr.show_arp import ShowArpDetail, \
											 ShowArpTrafficDetail


# ============================================
# Parser for 'show arp detail'
# ============================================
class test_show_arp_detail(unittest.TestCase):
		
		device = Device(name='aDevice')
		empty_output = {'execute.return_value': ''}
		
		golden_parsed_output = {
			'interfaces': {
				'GigabitEthernet0/0/0/0': {
					'ipv4': {
						'neighbors': {
							'10.1.2.1': {
								'age': '02:55:43',
								'ip': '10.1.2.1',
								'link_layer_address': 'fa16.3eff.06af',
								'origin': 'dynamic',
								'type': 'ARPA'},
							'10.1.2.2': {
								'age': '-',
								'ip': '10.1.2.2',
								'link_layer_address': 'fa16.3eff.f847',
								'origin': 'static',
								'type': 'ARPA'}
						}
					}
				},
				'GigabitEthernet0/0/0/1': {
					'ipv4': {
						'neighbors': {
							'10.2.3.2': {
								'age': '-',
								'ip': '10.2.3.2',
								'link_layer_address': 'fa16.3eff.c3f7',
								'origin': 'static',
								'type': 'ARPA'},
							'10.2.3.3': {
								'age': '00:13:12',
								'ip': '10.2.3.3',
								'link_layer_address': '5e00.80ff.0209',
								'origin': 'dynamic',
								'type': 'ARPA'}
						}
					}
				}
			}
		}

		golden_output = {'execute.return_value': '''\
			RP/0/RP0/CPU0:R2_xrv9000#show arp detail
			Wed Mar 21 02:12:48.613 UTC

			-------------------------------------------------------------------------------
			0/0/CPU0
			-------------------------------------------------------------------------------
			Address         Age         Hardware Addr   State      Flag      Type  Interface
			10.1.2.1        02:55:43   fa16.3eff.06af  Dynamic    Dynamic ARPA GigabitEthernet0/0/0/0
			10.1.2.2        -          fa16.3eff.f847  Interface  Unknown ARPA GigabitEthernet0/0/0/0
			10.2.3.2        -          fa16.3eff.c3f7  Interface  Unknown ARPA GigabitEthernet0/0/0/1
			10.2.3.3        00:13:12   5e00.80ff.0209  Dynamic    Dynamic ARPA GigabitEthernet0/0/0/1
		'''}


		golden_parsed_output_1 = {
			'interfaces': {
				'GigabitEthernet0/0/0/0': {
					'ipv4': {
						'neighbors': {
							'10.1.2.1': {
								'age': '02:56:20',
								'ip': '10.1.2.1',
								'link_layer_address': 'fa16.3eff.06af',
								'origin': 'dynamic',
								'type': 'ARPA'},
							'10.1.2.2': {
								'age': '-',
								'ip': '10.1.2.2',
								'link_layer_address': 'fa16.3eff.f847',
								'origin': 'static',
								'type': 'ARPA'}
						}
					}
				},
				'GigabitEthernet0/0/0/1': {
					'ipv4': {
						'neighbors': {
							'10.2.3.2': {
								'age': '-',
								'ip': '10.2.3.2',
								'link_layer_address': 'fa16.3eff.c3f7',
								'origin': 'static',
								'type': 'ARPA'},
							'10.2.3.3': {'age': '00:13:49',
								'ip': '10.2.3.3',
								'link_layer_address': '5e00.80ff.0209',
								'origin': 'dynamic',
								'type': 'ARPA'}
						}
					}
				}
			}
		}

		golden_output_1 = {'execute.return_value': '''\
			RP/0/RP0/CPU0:R2_xrv9000#show arp vrf default detail
			Wed Mar 21 02:13:24.990 UTC

			-------------------------------------------------------------------------------
			0/0/CPU0
			-------------------------------------------------------------------------------
			Address         Age         Hardware Addr   State      Flag      Type  Interface
			10.1.2.1        02:56:20   fa16.3eff.06af  Dynamic    Dynamic ARPA GigabitEthernet0/0/0/0
			10.1.2.2        -          fa16.3eff.f847  Interface  Unknown ARPA GigabitEthernet0/0/0/0
			10.2.3.2        -          fa16.3eff.c3f7  Interface  Unknown ARPA GigabitEthernet0/0/0/1
			10.2.3.3        00:13:49   5e00.80ff.0209  Dynamic    Dynamic ARPA GigabitEthernet0/0/0/1
		'''}

		def test_empty(self):
				self.device1 = Mock(**self.empty_output)
				obj = ShowArpDetail(device=self.device1)
				with self.assertRaises(SchemaEmptyParserError):
						parsed_output = obj.parse()

		def test_golden(self):
				self.device = Mock(**self.golden_output)
				obj = ShowArpDetail(device=self.device)
				parsed_output = obj.parse()
				self.assertEqual(parsed_output,self.golden_parsed_output)

		def test_golden_1(self):
				self.device = Mock(**self.golden_output_1)
				obj = ShowArpDetail(device=self.device)
				parsed_output = obj.parse(vrf='default')
				self.assertEqual(parsed_output,self.golden_parsed_output_1)

# ============================================
# Parser for 'show arp traffic detail'
# ============================================
class test_show_arp_traffic_detail(unittest.TestCase):
		
		device = Device(name='aDevice')
		empty_output = {'execute.return_value': ''}
		
		golden_parsed_output = {
			'0/0/CPU0': {
				'cache': {
					'alias': 0,
					'dhcp': 0,
					'dynamic': 2,
					'interface': 2,
					'ip_packet_drop_count': 0,
					'standby': 0,
					'static': 0,
					'total_arp_entries': 4,
					'total_arp_idb': 2},
				'statistics': {
					'in_replies_pkts': 8,
					'in_requests_pkts': 108,
					'no_buffers_errors': 0,
					'out_gratuitous_pkts': 2,
					'out_local_proxy': 0,
					'out_of_memory_errors': 0,
					'out_of_subnet_errors': 0,
					'out_proxy': 0,
					'out_replies_pkts': 108,
					'out_requests_pkts': 8,
					'resolve_dropped_requests': 0,
					'resolve_rcvd_requests': 0,
					'subscriber_intf_gratuitous': 0,
					'subscriber_intf_replies': 0,
					'subscriber_intf_requests': 0}},
			'0/RP0/CPU0': {
				'cache': {
					'alias': 0,
					'dhcp': 0,
					'dynamic': 0,
					'interface': 0,
					'ip_packet_drop_count': 0,
					'standby': 0,
					'static': 0,
					'total_arp_entries': 0,
					'total_arp_idb': 0},
				'statistics': {
					'in_replies_pkts': 0,
					'in_requests_pkts': 0,
					'no_buffers_errors': 0,
					'out_gratuitous_pkts': 0,
					'out_local_proxy': 0,
					'out_of_memory_errors': 0,
					'out_of_subnet_errors': 0,
					'out_proxy': 0,
					'out_replies_pkts': 0,
					'out_requests_pkts': 0,
					'resolve_dropped_requests': 0,
					'resolve_rcvd_requests': 0,
					'subscriber_intf_gratuitous': 0,
					'subscriber_intf_replies': 0,
					'subscriber_intf_requests': 0}
			}
		}

		golden_output = {'execute.return_value': '''\
			RP/0/RP0/CPU0:R2_xrv9000#show arp traffic detail 
			Wed Mar 21 02:14:05.935 UTC

			-------------------------------------------------------------------------------
			0/0/CPU0
			-------------------------------------------------------------------------------

			ARP statistics:
			  Recv: 108 requests, 8 replies
			  Sent: 8 requests, 108 replies (0 proxy, 0 local proxy, 2 gratuitous)
			  Subscriber Interface: 
					 0 requests recv, 0 replies sent, 0 gratuitous replies sent
			  Resolve requests rcvd: 0
			  Resolve requests dropped: 0
			  Errors: 0 out of memory, 0 no buffers, 0 out of subnet

			ARP cache:
			  Total ARP entries in cache: 4
			  Dynamic: 2, Interface: 2, Standby: 0
			  Alias: 0,   Static: 0,    DHCP: 0

			  IP Packet drop count for node 0/0/CPU0: 0

			  Total ARP-IDB:2


			-------------------------------------------------------------------------------
			0/RP0/CPU0
			-------------------------------------------------------------------------------

			ARP statistics:
			  Recv: 0 requests, 0 replies
			  Sent: 0 requests, 0 replies (0 proxy, 0 local proxy, 0 gratuitous)
			  Subscriber Interface: 
					 0 requests recv, 0 replies sent, 0 gratuitous replies sent
			  Resolve requests rcvd: 0
			  Resolve requests dropped: 0
			  Errors: 0 out of memory, 0 no buffers, 0 out of subnet

			ARP cache:
			  Total ARP entries in cache: 0
			  Dynamic: 0, Interface: 0, Standby: 0
			  Alias: 0,   Static: 0,    DHCP: 0

			  IP Packet drop count for node 0/RP0/CPU0: 0

			  Total ARP-IDB:0
		'''}

		def test_empty(self):
				self.device1 = Mock(**self.empty_output)
				obj = ShowArpTrafficDetail(device=self.device1)
				with self.assertRaises(SchemaEmptyParserError):
						parsed_output = obj.parse()

		def test_golden(self):
				self.device = Mock(**self.golden_output)
				obj = ShowArpTrafficDetail(device=self.device)
				parsed_output = obj.parse()
				self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
		unittest.main()