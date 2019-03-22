# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_bfd import ShowBfdNeighborsDetails,\
											 ShowBfdNeighborsClientOSPFDetails

# ============================================
# Parser for 'show bfd neighbors details
# ============================================
class test_show_bfd(unittest.TestCase):
		
		device = Device(name='aDevice')
		empty_output = {'execute.return_value': ''}
		
		golden_parsed_output =  {
      'bfd_neighbors': {
					'106.162.197.93': {
            '106.162.197.94': {
                        'ld_rd': '4097/4097',
                        'rh_rs': '1',
                        'holddown_mult': '0 (3 )',
                        'state': 'Up',
                        'interface': 'Gi0/0/0',
                        'session': {
                            'state': 'UP',
                            'function_used': 'echo',
                                 'interval_in_ms': 500
                                 },
                       'session_host': 'Software',
                       'handle': 1,
                       'local_diag': 0,
                       'demand_mode': 0,
                       'poll_bit': 0,
                       'min_tx_interface': 1000000,
                       'min_rx_interface': 1000000,
                       'multiplier': 6,
                       'received_min_rx_interface': 1000000,
                     'received_multiplier': 6,
                     'holddown_hits': '0(0)',
                     'hello_hits': '1000(1939)',
                     'rx': {'rx_count': 1916,
                            'rx_min_interval_in_ms': 1,
                            'rx_max_interval_in_ms': 1003,
                            'rx_avg_interval_in_ms': 878,
                            'rx_last_interval_in_ms': 207},
                      'tx': {'tx_count': 1916,
                            'tx_min_interval_in_ms': 1,
                            'tx_max_interval_in_ms': 1003,
                            'tx_avg_interval_in_ms': 878,
                            'tx_last_interval_in_ms': 767},
                     
                     'elapsed_time_watermarks': '0 0',
                     'elapsed_time_watermarks_last': 0,
                          
                      'registered_protocols': 'OSPF CEF',
     
                     'up_time': '00:28:03', 
                      'last_packet': {'c_bit': 0,
                                     'demand_bit': 0,
                                     'diagnostic': 0,
                                     'final_bit': 0,
                                     'length': 24,
                                     'min_echo_interval': 3000000,
                                     'min_rx_interval': 1000000,
                                     'min_tx_interval': 1000000,
                                     'multiplier': 6,
                                     'my_discr': 4097,
                                     'poll_bit': 0,
                                     'state_bit': 'Up',
                                     'version': 1,
                                     'your_discr': 4097}
                }
        }       
      }      
    }


		golden_output = {'execute.return_value': '''
      IPv4 Sessions
      OurAddr NeighAddr   LD/RD   RH/RS Holdown(mult) State   Int
			106.162.197.93 106.162.197.94 4097/4097	1  0 (3 )	Up	Gi0/0/0
      Session state is UP and using echo function with 500 ms interval.
			Session Host: Software
			Handle: 1
			Local Diag: 0, Demand mode: 0, Poll bit: 0
			MinTxInt: 1000000, MinRxInt: 1000000, Multiplier: 6
			Received MinRxInt: 1000000, Received Multiplier: 6
			Holddown (hits): 0(0), Hello (hits): 1000(1939)
			Rx Count: 1916, Rx Interval (ms) min/max/avg: 1/1003/878 last: 207 ms ago
			Tx Count: 1916, Tx Interval (ms) min/max/avg: 1/1003/878 last: 767 ms ago
			Elapsed time watermarks: 0 0 (last: 0)
			Registered protocols: OSPF CEF
			Uptime: 00:28:03
			Last packet: 	Version: 1			- Diagnostic: 0
							State bit: Up       - Demand bit: 0
							Poll bit: 0			- Final bit: 0
							C bit: 0
							Multiplier: 6		- Length: 24
							My Discr.: 4097		- Your Discr.: 4097
							Min tx interval: 1000000	- Min rx interval: 1000000
							Min Echo interval: 3000000
		'''}


		golden_parsed_output_client_osf_details =  {
      'bfd_neighbors': {
          '106.162.197.93': {
            '106.162.197.94': {
                        'ld_rd': '4097/4097',
                        'rh_rs': '1',
                        'holddown_mult': '0 (3 )',
                        'state': 'Up',
                        'interface': 'Gi0/0/0',
                        'session': {
                            'state': 'UP',
                            'function_used': 'echo',
                                 'interval_in_ms': 500
                                 },
                       'session_host': 'Software',
                       'handle': 1,
                       'local_diag': 0,
                       'demand_mode': 0,
                       'poll_bit': 0,
                       'min_tx_interface': 1000000,
                       'min_rx_interface': 1000000,
                       'multiplier': 6,
                       'received_min_rx_interface': 1000000,
                     'received_multiplier': 6,
                     'holddown_hits': '0(0)',
                     'hello_hits': '1000(1939)',
                     'rx': {'rx_count': 1916,
                            'rx_min_interval_in_ms': 1,
                            'rx_max_interval_in_ms': 1003,
                            'rx_avg_interval_in_ms': 878,
                            'rx_last_interval_in_ms': 207},
                      'tx': {'tx_count': 1916,
                            'tx_min_interval_in_ms': 1,
                            'tx_max_interval_in_ms': 1003,
                            'tx_avg_interval_in_ms': 878,
                            'tx_last_interval_in_ms': 767},
                     
                     'elapsed_time_watermarks': '0 0',
                     'elapsed_time_watermarks_last': 0,
                          
                      'registered_protocols': 'OSPF CEF',
     
                     'up_time': '00:28:03', 
                      'last_packet': {'c_bit': 0,
                                     'demand_bit': 0,
                                     'diagnostic': 0,
                                     'final_bit': 0,
                                     'length': 24,
                                     'min_echo_interval': 3000000,
                                     'min_rx_interval': 1000000,
                                     'min_tx_interval': 1000000,
                                     'multiplier': 6,
                                     'my_discr': 4097,
                                     'poll_bit': 0,
                                     'state_bit': 'Up',
                                     'version': 1,
                                     'your_discr': 4097}
                }
        }       
      }      
    }
		golden_output_client_osf_details = {'execute.return_value': '''
      IPv4 Sessions
      OurAddr NeighAddr   
      LD/RD   RH/RS Holdown(mult)  State   Int
      106.162.197.93 106.162.197.94 
      4097/4097  1 0 (3 )  Up  Gi0/0/0
      Session state is UP and using echo function with 500 ms interval.
      Session Host: Software
      Handle: 1
      Local Diag: 0, Demand mode: 0, Poll bit: 0
      MinTxInt: 1000000, MinRxInt: 1000000, Multiplier: 6
      Received MinRxInt: 1000000, Received Multiplier: 6
      Holddown (hits): 0(0), Hello (hits): 1000(1939)
      Rx Count: 1916, Rx Interval (ms) min/max/avg: 1/1003/878 last: 207 ms ago
      Tx Count: 1916, Tx Interval (ms) min/max/avg: 1/1003/878 last: 767 ms ago
      Elapsed time watermarks: 0 0 (last: 0)
      Registered protocols: OSPF CEF
      Uptime: 00:28:03
      Last packet:  Version: 1      - Diagnostic: 0
              State bit: Up       - Demand bit: 0
              Poll bit: 0     - Final bit: 0
              C bit: 0
              Multiplier: 6   - Length: 24
              My Discr.: 4097   - Your Discr.: 4097
              Min tx interval: 1000000  - Min rx interval: 1000000
              Min Echo interval: 3000000
    '''}


		def test_empty(self):
			self.device = Mock(**self.empty_output)
			obj = ShowBfdNeighborsDetails(device=self.device)
			with self.assertRaises(SchemaEmptyParserError):
				parsed_output = obj.parse()

		def test_golden(self):
			self.device = Mock(**self.golden_output)
			obj = ShowBfdNeighborsDetails(device=self.device)
			parsed_output = obj.parse()
			self.assertEqual(parsed_output,self.golden_parsed_output)

		def test_empty_osf_details(self):
			self.device = Mock(**self.empty_output)
			obj = ShowBfdNeighborsClientOSPFDetails(device=self.device)
			with self.assertRaises(SchemaEmptyParserError):
				parsed_output = obj.parse()

		def test_golden_osf_details(self):
			self.device = Mock(**self.golden_output_client_osf_details)
			obj = ShowBfdNeighborsClientOSPFDetails(device=self.device)
			parsed_output = obj.parse()
			self.assertEqual(parsed_output,self.golden_parsed_output_client_osf_details)


if __name__ == '__main__':
		unittest.main()
