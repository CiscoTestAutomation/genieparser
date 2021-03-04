import unittest
from unittest.mock import Mock

from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.iosxr.show_bfd import ShowBfdSessionDestinationDetails


class TestShowBfdSessionDestinationDetailss(unittest.TestCase):

    device = Device(name='aDevice')

    empty_device_output = {'execute.return_value': '''
      '''}

    expected_parsed_output = {
         "src":{
            "10.4.1.2":{
               "dest":{
                  "10.4.1.1":{
                     "interface":"GigabitEthernet0/0/0/0",
                     "location":"0/0/CPU0",
                     "session":{
                        "state":"UP",
                        "duration":"0d:0h:5m:50s",
                        "num_of_times_up":1,
                        "type":"PR/V4/SH",
                        "owner_info":{
                              "ipv4_static":{
                                 "desired_interval_ms":500,
                                 "desired_multiplier":6,
                                 "adjusted_interval_ms":500,
                                 "adjusted_multiplier":6
                              }
                           }
                        },
                     "received_parameters":{
                        "version":1,
                        "desired_tx_interval_ms":500,
                        "required_rx_interval_ms":500,
                        "required_echo_rx_interval_ms":0,
                        "multiplier":6,
                        "diag":"None",
                        "demand_bit":0,
                        "final_bit":0,
                        "poll_bit":0,
                        "control_bit":1,
                        "authentication_bit":0,
                        "my_discr":18,
                        "your_discr":2148532226,
                        "state":"UP"
                     },
                     "transmitted_parameters":{
                        "version":1,
                        "desired_tx_interval_ms":500,
                        "required_rx_interval_ms":500,
                        "required_echo_rx_interval_ms":1,
                        "multiplier":6,
                        "diag":"None",
                        "demand_bit":0,
                        "final_bit":0,
                        "poll_bit":0,
                        "control_bit":1,
                        "authentication_bit":0,
                        "my_discr":2148532226,
                        "your_discr":18,
                        "state":"UP"
                     },
                     "timer_vals":{
                        "local_async_tx_interval_ms":500,
                        "remote_async_tx_interval_ms":500,
                        "desired_echo_tx_interval_ms":500,
                        "local_echo_tax_interval_ms":0,
                        "echo_detection_time_ms":0,
                        "async_detection_time_ms":3000
                     },
                     "local_stats":{
                        "interval_async_packets":{
                           "Tx":{
                              "num_intervals":100,
                              "min_ms":1,
                              "max_ms":500,
                              "avg_ms":229,
                              "last_packet_transmitted_ms_ago":48
                           },
                           "Rx":{
                              "num_intervals":100,
                              "min_ms":490,
                              "max_ms":513,
                              "avg_ms":500,
                              "last_packet_received_ms_ago":304
                           }
                        },
                        "interval_echo_packets":{
                           "Tx":{
                              "num_intervals":0,
                              "min_ms":0,
                              "max_ms":0,
                              "avg_ms":0,
                              "last_packet_transmitted_ms_ago":0
                           },
                           "Rx":{
                              "num_intervals":0,
                              "min_ms":0,
                              "max_ms":0,
                              "avg_ms":0,
                              "last_packet_received_ms_ago":0
                           }
                        },
                        "latency_of_echo_packets":{
                           "num_of_packets":0,
                           "min_ms":0,
                           "max_ms":0,
                           "avg_ms":0
                        }
                     }
                  }
               }
            }
         }
      }

    device_output = {'execute.return_value': '''
        I/f: GigabitEthernet0/0/0/0, Location: 0/0/CPU0
        Dest: 10.4.1.1
        Src: 10.4.1.2
         State: UP for 0d:0h:5m:50s, number of times UP: 1
         Session type: PR/V4/SH
        Received parameters:
         Version: 1, desired tx interval: 500 ms, required rx interval: 500 ms
         Required echo rx interval: 0 ms, multiplier: 6, diag: None
         My discr: 18, your discr: 2148532226, state UP, D/F/P/C/A: 0/0/0/1/0
        Transmitted parameters:
         Version: 1, desired tx interval: 500 ms, required rx interval: 500 ms
         Required echo rx interval: 1 ms, multiplier: 6, diag: None
         My discr: 2148532226, your discr: 18, state UP, D/F/P/C/A: 0/0/0/1/0
        Timer Values:
         Local negotiated async tx interval: 500 ms
         Remote negotiated async tx interval: 500 ms
         Desired echo tx interval: 500 ms, local negotiated echo tx interval: 0 ms
         Echo detection time: 0 ms(0 ms*6), async detection time: 3 s(500 ms*6)
        Local Stats:
         Intervals between async packets:
           Tx: Number of intervals=100, min=1 ms, max=500 ms, avg=229 ms
               Last packet transmitted 48 ms ago
           Rx: Number of intervals=100, min=490 ms, max=513 ms, avg=500 ms
               Last packet received 304 ms ago
         Intervals between echo packets:
           Tx: Number of intervals=0, min=0 s, max=0 s, avg=0 s
               Last packet transmitted 0 s ago
           Rx: Number of intervals=0, min=0 s, max=0 s, avg=0 s
               Last packet received 0 s ago
         Latency of echo packets (time between tx and rx):
           Number of packets: 0, min=0 ms, max=0 ms, avg=0 ms 
        Session owner information:
                                    Desired               Adjusted
          Client               Interval   Multiplier Interval   Multiplier
          -------------------- --------------------- ---------------------
          ipv4_static          500 ms     6          500 ms     6
    '''}

    device_output_ipv6 = {'execute.return_value': '''
        I/f: GigabitEthernet0/0/0/0, Location: 0/0/CPU0
        Dest: 2001:31::1
        Src: 2001:31::2
         State: UP for 0d:0h:7m:8s, number of times UP: 1
         Session type: PR/V6/SH
        Received parameters:
         Version: 1, desired tx interval: 500 ms, required rx interval: 500 ms
         Required echo rx interval: 0 ms, multiplier: 6, diag: None
         My discr: 19, your discr: 2148532225, state UP, D/F/P/C/A: 0/0/0/1/0
        Transmitted parameters:
         Version: 1, desired tx interval: 500 ms, required rx interval: 500 ms
         Required echo rx interval: 0 ms, multiplier: 6, diag: None
         My discr: 2148532225, your discr: 19, state UP, D/F/P/C/A: 0/0/0/1/0
        Timer Values:
         Local negotiated async tx interval: 500 ms
         Remote negotiated async tx interval: 500 ms
         Desired echo tx interval: 0 s, local negotiated echo tx interval: 0 ms
         Echo detection time: 0 ms(0 ms*6), async detection time: 3 s(500 ms*6)
        Local Stats:
         Intervals between async packets:
           Tx: Number of intervals=100, min=1 ms, max=498 ms, avg=226 ms
               Last packet transmitted 169 ms ago
           Rx: Number of intervals=100, min=490 ms, max=507 ms, avg=500 ms
               Last packet received 198 ms ago
         Intervals between echo packets:
           Tx: Number of intervals=0, min=0 s, max=0 s, avg=0 s
               Last packet transmitted 0 s ago
           Rx: Number of intervals=0, min=0 s, max=0 s, avg=0 s
               Last packet received 0 s ago
         Latency of echo packets (time between tx and rx):
           Number of packets: 0, min=0 ms, max=0 ms, avg=0 ms
        Session owner information:
                                    Desired               Adjusted
          Client               Interval   Multiplier Interval   Multiplier
          -------------------- --------------------- ---------------------
          ipv6_static          500 ms     6          500 ms     6
    '''}

    expected_parsed_output_ipv6 = {
         "src":{
            "2001:31::2":{
               "dest":{
                  "2001:31::1":{
                     "interface":"GigabitEthernet0/0/0/0",
                     "location":"0/0/CPU0",
                     "session":{
                        "state":"UP",
                        "duration":"0d:0h:7m:8s",
                        "num_of_times_up":1,
                        "type":"PR/V6/SH",
                        "owner_info":{
                              "ipv6_static":{
                                 "desired_interval_ms":500,
                                 "desired_multiplier":6,
                                 "adjusted_interval_ms":500,
                                 "adjusted_multiplier":6
                              }
                           }
                        },
                     "received_parameters":{
                        "version":1,
                        "desired_tx_interval_ms":500,
                        "required_rx_interval_ms":500,
                        "required_echo_rx_interval_ms":0,
                        "multiplier":6,
                        "diag":"None",
                        "demand_bit":0,
                        "final_bit":0,
                        "poll_bit":0,
                        "control_bit":1,
                        "authentication_bit":0,
                        "my_discr":19,
                        "your_discr":2148532225,
                        "state":"UP"
                     },
                     "transmitted_parameters":{
                        "version":1,
                        "desired_tx_interval_ms":500,
                        "required_rx_interval_ms":500,
                        "required_echo_rx_interval_ms":0,
                        "multiplier":6,
                        "diag":"None",
                        "demand_bit":0,
                        "final_bit":0,
                        "poll_bit":0,
                        "control_bit":1,
                        "authentication_bit":0,
                        "my_discr":2148532225,
                        "your_discr":19,
                        "state":"UP"
                     },
                     "timer_vals":{
                        "local_async_tx_interval_ms":500,
                        "remote_async_tx_interval_ms":500,
                        "desired_echo_tx_interval_ms":0,
                        "local_echo_tax_interval_ms":0,
                        "echo_detection_time_ms":0,
                        "async_detection_time_ms":3000
                     },
                     "local_stats":{
                        "interval_async_packets":{
                           "Tx":{
                              "num_intervals":100,
                              "min_ms":1,
                              "max_ms":498,
                              "avg_ms":226,
                              "last_packet_transmitted_ms_ago":169
                           },
                           "Rx":{
                              "num_intervals":100,
                              "min_ms":490,
                              "max_ms":507,
                              "avg_ms":500,
                              "last_packet_received_ms_ago":198
                           }
                        },
                        "interval_echo_packets":{
                           "Tx":{
                              "num_intervals":0,
                              "min_ms":0,
                              "max_ms":0,
                              "avg_ms":0,
                              "last_packet_transmitted_ms_ago":0
                           },
                           "Rx":{
                              "num_intervals":0,
                              "min_ms":0,
                              "max_ms":0,
                              "avg_ms":0,
                              "last_packet_received_ms_ago":0
                           }
                        },
                        "latency_of_echo_packets":{
                           "num_of_packets":0,
                           "min_ms":0,
                           "max_ms":0,
                           "avg_ms":0
                        }
                     }
                  }
               }
            }
         }
      }

    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None

    def test_show_bfd_destination_details_1(self):

        self.device = Mock(**self.device_output)
        obj = ShowBfdSessionDestinationDetails(device=self.device)
        parsed_output = obj.parse(ip_address='10.4.1.1')
        self.assertEqual(parsed_output, self.expected_parsed_output)

    def test_show_bfd_destination_details_2(self):

        self.device = Mock(**self.device_output_ipv6)
        obj = ShowBfdSessionDestinationDetails(device=self.device)
        parsed_output = obj.parse(ipv6='ipv6', ip_address='2001:31::1')
        self.assertEqual(parsed_output, self.expected_parsed_output_ipv6)

    def test_show_bfd_destination_details_empty_output(self):

        self.device = Mock(**self.empty_device_output)
        obj = ShowBfdSessionDestinationDetails(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(ip_address=None)

if __name__ == '__main__':
    unittest.main()
