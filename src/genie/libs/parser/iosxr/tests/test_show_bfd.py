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
           "interface":{
              "GigabitEthernet0/0/0/0":{
                 "location":"0/0/CPU0",
                 "dest":"31.1.1.1",
                 "src":"31.1.1.2",
                 "session":{
                    "state":"UP",
                    "duration":"0d:0h:5m:50s",
                    "num_of_times_up":1,
                    "type":"PR/V4/SH",
                    "owner_info":{
                       "desired":{
                          "client":{
                             "ipv4_static":{
                                "interval":500,
                                "interval_unit":"ms",
                                "multiplier":6
                             }
                          }
                       },
                       "adjusted":{
                          "client":{
                             "ipv4_static":{
                                "interval":500,
                                "interval_unit":"ms",
                                "multiplier":6
                             }
                          }
                       }
                    }
                 },
                 "received_parameters":{
                    "version":1,
                    "desired_tx_interval":500,
                    "desired_tx_interval_unit":"ms",
                    "required_rx_interval":500,
                    "required_rx_interval_unit":"ms",
                    "required_echo_rx_interval":0,
                    "required_echo_rx_interval_unit":"ms",
                    "multiplier":6,
                    "diag":"None",
                    "demand":False,
                    "final":False,
                    "poll":False,
                    "control":True,
                    "authentication":False,
                    "my_discr":18,
                    "your_discr":2148532226,
                    "state":"UP"
                 },
                 "transmitted_parameters":{
                    "version":1,
                    "desired_tx_interval":500,
                    "desired_tx_interval_unit":"ms",
                    "required_rx_interval":500,
                    "required_rx_interval_unit":"ms",
                    "required_echo_rx_interval":1,
                    "required_echo_rx_interval_unit":"ms",
                    "multiplier":6,
                    "diag":"None",
                    "demand":False,
                    "final":False,
                    "poll":False,
                    "control":True,
                    "authentication":False,
                    "my_discr":2148532226,
                    "your_discr":18,
                    "state":"UP"
                 },
                 "timer_vals":{
                    "local_async_tx_interval":500,
                    "local_async_tx_interval_unit":"ms",
                    "remote_async_tx_interval":500,
                    "remote_async_tx_interval_unit":"ms",
                    "desired_echo_tx_interval":500,
                    "desired_echo_tx_interval_unit":"ms",
                    "local_echo_tax_interval":0,
                    "local_echo_tax_interval_unit":"ms",
                    "echo_detection_time":0,
                    "echo_detection_time_unit":"ms",
                    "async_detection_time":3,
                    "async_detection_time_unit":"s"
                 },
                 "local_stats":{
                    "interval_async_packets":{
                       "Tx":{
                          "num_intervals":100,
                          "min":1,
                          "min_unit":"ms",
                          "max":500,
                          "max_unit":"ms",
                          "avg": 229,
                          "avg_unit": "ms", 
                          "last_packet_transmitted_ago":48,
                          "last_packet_transmitted_unit_ago":"ms"
                       },
                       "Rx":{
                          "num_intervals":100,
                          "min":490,
                          "min_unit":"ms",
                          "max":513,
                          "max_unit":"ms",
                          "avg": 500,
                          "avg_unit": "ms",
                          "last_packet_received_ago":304,
                          "last_packet_received_unit_ago":"ms"
                       }
                    },
                    "interval_echo_packets":{
                       "Tx":{
                          "num_intervals":0,
                          "min":0,
                          "min_unit":"s",
                          "max":0,
                          "max_unit":"s",
                          "avg": 0,
                          "avg_unit": "s",
                          "last_packet_transmitted_ago":0,
                          "last_packet_transmitted_unit_ago":"s"
                       },
                       "Rx":{
                          "num_intervals":0,
                          "min":0,
                          "min_unit":"s",
                          "max":0,
                          "max_unit":"s",
                          "avg": 0,
                          "avg_unit": "s",
                          "last_packet_received_ago":0,
                          "last_packet_received_unit_ago":"s"
                       }
                    },
                    "latency_of_echo_packets":{
                       "num_of_packets":0,
                       "min":0,
                       "min_unit":"ms",
                       "max":0,
                       "max_unit":"ms",
                       "avg": 0,
                       "avg_unit": "ms"
                    }
                 }
              }
           }
        }

    device_output = {'execute.return_value': '''
        RP/0/RP0/CPU0:P12-XR#show bfd session destination 31.1.1.1 detail
        Wed Nov 18 15:14:26.344 JST
        I/f: GigabitEthernet0/0/0/0, Location: 0/0/CPU0
        Dest: 31.1.1.1
        Src: 31.1.1.2
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
        RP/0/RP0/CPU0:P12-XR#show bfd ipv6 session destination 2001:31::1 detail
        Wed Nov 18 15:15:44.241 JST
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
       "interface":{
          "GigabitEthernet0/0/0/0":{
             "location":"0/0/CPU0",
             "dest":"2001:31::1",
             "src":"2001:31::2",
             "session":{
                "state":"UP",
                "duration":"0d:0h:7m:8s",
                "num_of_times_up":1,
                "type":"PR/V6/SH",
                "owner_info":{
                   "desired":{
                      "client":{
                         "ipv6_static":{
                            "interval":500,
                            "interval_unit":"ms",
                            "multiplier":6
                         }
                      }
                   },
                   "adjusted":{
                      "client":{
                         "ipv6_static":{
                            "interval":500,
                            "interval_unit":"ms",
                            "multiplier":6
                         }
                      }
                   }
                }
             },
             "received_parameters":{
                "version":1,
                "desired_tx_interval":500,
                "desired_tx_interval_unit":"ms",
                "required_rx_interval":500,
                "required_rx_interval_unit":"ms",
                "required_echo_rx_interval":0,
                "required_echo_rx_interval_unit":"ms",
                "multiplier":6,
                "diag":"None",
                "demand":False,
                "final":False,
                "poll":False,
                "control":True,
                "authentication":False,
                "my_discr":19,
                "your_discr":2148532225,
                "state":"UP"
             },
             "transmitted_parameters":{
                "version":1,
                "desired_tx_interval":500,
                "desired_tx_interval_unit":"ms",
                "required_rx_interval":500,
                "required_rx_interval_unit":"ms",
                "required_echo_rx_interval":0,
                "required_echo_rx_interval_unit":"ms",
                "multiplier":6,
                "diag":"None",
                "demand":False,
                "final":False,
                "poll":False,
                "control":True,
                "authentication":False,
                "my_discr":2148532225,
                "your_discr":19,
                "state":"UP"
             },
             "timer_vals":{
                "local_async_tx_interval":500,
                "local_async_tx_interval_unit":"ms",
                "remote_async_tx_interval":500,
                "remote_async_tx_interval_unit":"ms",
                "desired_echo_tx_interval":0,
                "desired_echo_tx_interval_unit":"s",
                "local_echo_tax_interval":0,
                "local_echo_tax_interval_unit":"ms",
                "echo_detection_time":0,
                "echo_detection_time_unit":"ms",
                "async_detection_time":3,
                "async_detection_time_unit":"s"
             },
             "local_stats":{
                "interval_async_packets":{
                   "Tx":{
                      "num_intervals":100,
                      "min":1,
                      "min_unit":"ms",
                      "max":498,
                      "max_unit":"ms",
                      "avg":226,
                      "avg_unit":"ms",
                      "last_packet_transmitted_ago":169,
                      "last_packet_transmitted_unit_ago":"ms"
                   },
                   "Rx":{
                      "num_intervals":100,
                      "min":490,
                      "min_unit":"ms",
                      "max":507,
                      "max_unit":"ms",
                      "avg":500,
                      "avg_unit":"ms",
                      "last_packet_received_ago":198,
                      "last_packet_received_unit_ago":"ms"
                   }
                },
                "interval_echo_packets":{
                   "Tx":{
                      "num_intervals":0,
                      "min":0,
                      "min_unit":"s",
                      "max":0,
                      "max_unit":"s",
                      "avg":0,
                      "avg_unit":"s",
                      "last_packet_transmitted_ago":0,
                      "last_packet_transmitted_unit_ago":"s"
                   },
                   "Rx":{
                      "num_intervals":0,
                      "min":0,
                      "min_unit":"s",
                      "max":0,
                      "max_unit":"s",
                      "avg":0,
                      "avg_unit":"s",
                      "last_packet_received_ago":0,
                      "last_packet_received_unit_ago":"s"
                   }
                },
                "latency_of_echo_packets":{
                   "num_of_packets":0,
                   "min":0,
                   "min_unit":"ms",
                   "max":0,
                   "max_unit":"ms",
                   "avg":0,
                   "avg_unit":"ms"
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
        parsed_output = obj.parse(ip_address='31.1.1.1')
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
