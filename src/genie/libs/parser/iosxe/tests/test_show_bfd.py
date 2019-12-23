# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_bfd import ShowBfdNeighborsDetails

# ============================================
# Parser for the following commands
#   * 'show bfd neighbors details'
#   * 'show bfd neighbors client {client} details'
# ============================================
class test_show_bfd(unittest.TestCase):
  device = Device(name='aDevice')
  empty_output = {'execute.return_value' : ''}

  golden_parsed_output = {
    'our_address': {
  	  '10.169.197.93': {
        'neighbor_address':{
          '10.169.197.94': {
            'ld_rd': '4097/4097',
            'rh_rs': '1',
            'holdown_timer': 0,
            'holdown_timer_multiplier': 3,
            'state': 'Up',
            'interface': 'GigabitEthernet0/0/0',
            'session': {
              'state': 'UP',
              'echo_function': True,
              'echo_interval_ms': 500
            },
            'session_host': 'Software',
            'handle': 1,
            'local_diag': 0,
            'demand_mode': 0,
            'poll_bit': 0,
            'min_tx_int': 1000000,
            'min_rx_int': 1000000,
            'multiplier': 6,
            'received_min_rx_int': 1000000,
            'received_multiplier': 6,
            'holddown': 0,
            'holddown_hits': 0,
            'hello': 1000,
            'hello_hits': 1939,
            'rx': {
              'count': 1916,
              'min_int_ms': 1,
              'max_int_ms': 1003,
              'avg_int_ms': 878,
              'last_ms_ago': 207
            },
            'tx': {
              'count': 1916,
              'min_int_ms': 1,
              'max_int_ms': 1003,
              'avg_int_ms': 878,
              'last_ms_ago': 767
            },
            'elapsed_time_watermarks': '0 0',
            'elapsed_time_watermarks_last': 0,                        
            'registered_protocols': [
              'OSPF', 
              'CEF'
            ],
            'up_time': '00:28:03', 
            'last_packet': {
              'c_bit': 0,
              'demand_bit': 0,
              'diagnostic': 0,
              'final_bit': 0,
              'length': 24,
              'min_echo_int': 3000000,
              'min_rx_int': 1000000,
              'min_tx_int': 1000000,
              'multiplier': 6,
              'my_discr': 4097,
              'poll_bit': 0,
              'state_bit': 'Up',
              'version': 1,
              'your_discr': 4097
            }
          }
        }
      }
    }       
  }

  golden_output = {'execute.return_value': '''
    IPv4 Sessions
    OurAddr NeighAddr   LD/RD   RH/RS Holdown(mult) State   Int
		10.169.197.93 10.169.197.94 4097/4097	1  0 (3 )	Up	Gi0/0/0
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

  golden_parsed_output_client_osf_details = {
    'our_address': {
      '10.169.197.93': {
          'neighbor_address': {
              '10.169.197.94': {
                  'ld_rd': '4097/4097',
                  'rh_rs': 'Up',
                  'state': 'Up',
                  'interface': 'GigabitEthernet0/0/0',
                  'session': {
                      'state': 'UP',
                      'echo_function': True,
                      'echo_interval_ms': 500,
                      },
                  'session_host': 'Software',
                  'handle': 1,
                  'local_diag': 0,
                  'demand_mode': 0,
                  'poll_bit': 0,
                  'min_tx_int': 1000000,
                  'min_rx_int': 1000000,
                  'multiplier': 6,
                  'received_min_rx_int': 1000000,
                  'received_multiplier': 6,
                  'holddown': 0,
                  'holddown_hits': 0,
                  'hello': 1000,
                  'hello_hits': 1912,
                  'rx': {
                      'count': 1914,
                      'min_int_ms': 1,
                      'max_int_ms': 1017,
                      'avg_int_ms': 878,
                      'last_ms_ago': 668,
                      },
                  'tx': {
                      'count': 1914,
                      'min_int_ms': 1,
                      'max_int_ms': 1003,
                      'avg_int_ms': 878,
                      'last_ms_ago': 69,
                      },
                  'elapsed_time_watermarks': '0 0',
                  'elapsed_time_watermarks_last': 0,
                  'registered_protocols': ['OSPF', 'CEF'],
                  'up_time': '00:28:01',
                  'last_packet': {
                      'version': 1,
                      'diagnostic': 0,
                      'state_bit': 'Up',
                      'demand_bit': 0,
                      'poll_bit': 0,
                      'final_bit': 0,
                      'c_bit': 0,
                      'multiplier': 6,
                      'length': 24,
                      'my_discr': 4097,
                      'your_discr': 4097,
                      'min_tx_int': 1000000,
                      'min_rx_int': 1000000,
                      'min_echo_int': 300000,
                      },
                  },
              },
          },
      },
    }
    
  golden_output_client_osf_details = {'execute.return_value': '''
    1006#show bfd neighbors client ospf details
		Load for five secs: 0%/0%; one minute: 0%; five minutes: 0%
		Time source is NTP, 20:25:57.866 EST Sat Nov 12 2016


		IPv4 Sessions
		NeighAddr                              LD/RD         RH/RS     State     Int
		10.169.197.94                        4097/4097       Up        Up        Gi0/0/0
		Session state is UP and using echo function with 500 ms interval.
		Session Host: Software
		OurAddr: 10.169.197.93 
		Handle: 1
		Local Diag: 0, Demand mode: 0, Poll bit: 0
		MinTxInt: 1000000, MinRxInt: 1000000, Multiplier: 6
		Received MinRxInt: 1000000, Received Multiplier: 6
		Holddown (hits): 0(0), Hello (hits): 1000(1912)
		Rx Count: 1914, Rx Interval (ms) min/max/avg: 1/1017/878 last: 668 ms ago
		Tx Count: 1914, Tx Interval (ms) min/max/avg: 1/1003/878 last: 69 ms ago
		Elapsed time watermarks: 0 0 (last: 0)
		Registered protocols: OSPF CEF 
		Uptime: 00:28:01
		Last packet: Version: 1                  - Diagnostic: 0
			     State bit: Up               - Demand bit: 0
			     Poll bit: 0                 - Final bit: 0
			     C bit: 0                                   
			     Multiplier: 6               - Length: 24
			     My Discr.: 4097             - Your Discr.: 4097
			     Min tx interval: 1000000    - Min rx interval: 1000000
			     Min Echo interval: 300000  
    '''
    }
  
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
    obj = ShowBfdNeighborsDetails(device=self.device)
    with self.assertRaises(SchemaEmptyParserError):
      parsed_output = obj.parse(client='ospf')
  
  def test_golden_osf_details(self):
    self.device = Mock(**self.golden_output_client_osf_details)
    obj = ShowBfdNeighborsDetails(device=self.device)
    parsed_output = obj.parse(client='ospf')
    self.assertEqual(parsed_output,self.golden_parsed_output_client_osf_details)

  def test_golden_interface_details(self):
    self.device = Mock(**self.golden_output)
    obj = ShowBfdNeighborsDetails(device=self.device)
    parsed_output = obj.parse(interface='GigabitEthernet0/0/0')
    self.assertEqual(parsed_output,self.golden_parsed_output)



if __name__ == '__main__':
		unittest.main()
