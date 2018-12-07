# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

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
			'global_static_table': {
				'10.1.2.1': {
					'age': '02:55:43',
                    'encap_type': 'ARPA',
                    'flag': 'Dynamic',
                    'interface': 'GigabitEthernet0/0/0/0',
                    'ip_address': '10.1.2.1',
                    'mac_address': 'fa16.3e4c.b963',
                    'state': 'Dynamic'},
                '10.1.2.2': {
                	'age': '-',
                    'encap_type': 'ARPA',
                    'flag': 'Unknown',
                    'interface': 'GigabitEthernet0/0/0/0',
                    'ip_address': '10.1.2.2',
                    'mac_address': 'fa16.3ee4.1462',
                    'state': 'Interface'},
                '10.2.3.2': {
                	'age': '-',
                    'encap_type': 'ARPA',
                    'flag': 'Unknown',
                    'interface': 'GigabitEthernet0/0/0/1',
                    'ip_address': '10.2.3.2',
                    'mac_address': 'fa16.3e8f.3468',
                    'state': 'Interface'},
                '10.2.3.3': {
                	'age': '00:13:12',
                    'encap_type': 'ARPA',
                    'flag': 'Dynamic',
                    'interface': 'GigabitEthernet0/0/0/1',
                    'ip_address': '10.2.3.3',
                    'mac_address': '5e00.8002.0007',
                    'state': 'Dynamic'}
            }
        }

		golden_output = {'execute.return_value': '''\
			RP/0/RP0/CPU0:R2_xrv9000#show arp detail
			Wed Mar 21 02:12:48.613 UTC

			-------------------------------------------------------------------------------
			0/0/CPU0
			-------------------------------------------------------------------------------
			Address         Age         Hardware Addr   State      Flag      Type  Interface
			10.1.2.1        02:55:43   fa16.3e4c.b963  Dynamic    Dynamic ARPA GigabitEthernet0/0/0/0
			10.1.2.2        -          fa16.3ee4.1462  Interface  Unknown ARPA GigabitEthernet0/0/0/0
			10.2.3.2        -          fa16.3e8f.3468  Interface  Unknown ARPA GigabitEthernet0/0/0/1
			10.2.3.3        00:13:12   5e00.8002.0007  Dynamic    Dynamic ARPA GigabitEthernet0/0/0/1
		'''}


		golden_parsed_output_1 = {
			'global_static_table': {
				'10.1.2.1': {
					'age': '02:56:20',
                    'encap_type': 'ARPA',
                    'flag': 'Dynamic',
                    'interface': 'GigabitEthernet0/0/0/0',
                    'ip_address': '10.1.2.1',
                    'mac_address': 'fa16.3e4c.b963',
                    'state': 'Dynamic'},
                '10.1.2.2': {
                	'age': '-',
                    'encap_type': 'ARPA',
                    'flag': 'Unknown',
                    'interface': 'GigabitEthernet0/0/0/0',
                    'ip_address': '10.1.2.2',
                    'mac_address': 'fa16.3ee4.1462',
                    'state': 'Interface'},
                '10.2.3.2': {
                	'age': '-',
                    'encap_type': 'ARPA',
                    'flag': 'Unknown',
                    'interface': 'GigabitEthernet0/0/0/1',
                    'ip_address': '10.2.3.2',
                    'mac_address': 'fa16.3e8f.3468',
                    'state': 'Interface'},
                '10.2.3.3': {
                	'age': '00:13:49',
                    'encap_type': 'ARPA',
                    'flag': 'Dynamic',
                    'interface': 'GigabitEthernet0/0/0/1',
                    'ip_address': '10.2.3.3',
                    'mac_address': '5e00.8002.0007',
                    'state': 'Dynamic'}
            }
        }

		golden_output_1 = {'execute.return_value': '''\
			RP/0/RP0/CPU0:R2_xrv9000#show arp vrf default detail
			Wed Mar 21 02:13:24.990 UTC

			-------------------------------------------------------------------------------
			0/0/CPU0
			-------------------------------------------------------------------------------
			Address         Age         Hardware Addr   State      Flag      Type  Interface
			10.1.2.1        02:56:20   fa16.3e4c.b963  Dynamic    Dynamic ARPA GigabitEthernet0/0/0/0
			10.1.2.2        -          fa16.3ee4.1462  Interface  Unknown ARPA GigabitEthernet0/0/0/0
			10.2.3.2        -          fa16.3e8f.3468  Interface  Unknown ARPA GigabitEthernet0/0/0/1
			10.2.3.3        00:13:49   5e00.8002.0007  Dynamic    Dynamic ARPA GigabitEthernet0/0/0/1
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
		
		golden_parsed_output = {}

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
			  Errors: 0 out of memory, 0 no buffers, 0 out of sunbet

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
			  Errors: 0 out of memory, 0 no buffers, 0 out of sunbet

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
				import pdb; pdb.set_trace()
				self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
		unittest.main()