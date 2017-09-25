# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from parser.iosxe.show_mcast import ShowIpMroute,\
                                    ShowIpv6Mroute, \
                                    ShowIpMrouteStatic


# =======================================
# Unit test for 'show ip mroute'
# Unit test for 'show ip mroute vrf xxx'
# =======================================
class test_show_ip_mroute(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "vrf": {
            "default": {
                 "address_family": {
                      "ipv4": {
                           "multicast_group": {
                                "239.1.1.1": {
                                     "source_address": {
                                          "*": {
                                               "expires": "stopped",
                                               "rp": "1.1.1.1",
                                               "flags": "SPF",
                                               "uptime": "00:00:03",
                                               "incoming_interface_list": {
                                                    "Null": {
                                                         "rpf_nbr": "0.0.0.0"
                                                    }
                                               }
                                          },
                                          "1.1.1.1": {
                                               "expires": "00:02:57",
                                               "flags": "PFT",
                                               "uptime": "00:00:03",
                                               "incoming_interface_list": {
                                                    "Loopback0": {
                                                         "rpf_info": "Registering",
                                                         "rpf_nbr": "0.0.0.0"
                                                    }
                                               }
                                          },
                                          "10.1.3.1": {
                                               "expires": "00:02:57",
                                               "flags": "PFT",
                                               "uptime": "00:00:03",
                                               "incoming_interface_list": {
                                                    "GigabitEthernet2": {
                                                         "rpf_info": "Registering",
                                                         "rpf_nbr": "0.0.0.0"
                                                    }
                                               }
                                          }
                                     }
                                },
                                "224.0.1.40": {
                                     "source_address": {
                                          "*": {
                                               "expires": "00:02:56",
                                               "outgoing_interface_list": {
                                                    "Loopback0": {
                                                         "expire": "00:02:56",
                                                         "uptime": "2d09h",
                                                         "state_mode": "Forward/Sparse"
                                                    }
                                               },
                                               "flags": "SCL",
                                               "rp": "2.2.2.2",
                                               "uptime": "2d09h",
                                               "incoming_interface_list": {
                                                    "Null": {
                                                         "rpf_nbr": "0.0.0.0"
                                                    }
                                               }
                                          }
                                     }
                                },
                                "224.1.1.1": {
                                     "source_address": {
                                          "*": {
                                               "expires": "00:02:54",
                                               "outgoing_interface_list": {
                                                    "ATM0/0": {
                                                         "expire": "00:02:53",
                                                         "uptime": "00:03:57",
                                                         "vcd": "14",
                                                         "state_mode": "Forward/Sparse"
                                                    }
                                               },
                                               "flags": "SJ",
                                               "rp": "172.16.0.0",
                                               "uptime": "00:03:57",
                                               "incoming_interface_list": {
                                                    "Null": {
                                                         "rpf_nbr": "224.0.0.0224.0.0.0"
                                                    }}}}}}}}}}}

    golden_output = {'execute.return_value': '''\
        IP Multicast Routing Table
        Flags: D - Dense, S - Sparse, B - Bidir Group, s - SSM Group, C - Connected,
               L - Local, P - Pruned, R - RP-bit set, F - Register flag,
               T - SPT-bit set, J - Join SPT, M - MSDP created entry, E - Extranet,
               X - Proxy Join Timer Running, A - Candidate for MSDP Advertisement,
               U - URD, I - Received Source Specific Host Report, 
               Z - Multicast Tunnel, z - MDT-data group sender, 
               Y - Joined MDT-data group, y - Sending to MDT-data group, 
               G - Received BGP C-Mroute, g - Sent BGP C-Mroute, 
               N - Received BGP Shared-Tree Prune, n - BGP C-Mroute suppressed, 
               Q - Received BGP S-A Route, q - Sent BGP S-A Route, 
               V - RD & Vector, v - Vector, p - PIM Joins on route, 
               x - VxLAN group
        Outgoing interface flags: H - Hardware switched, A - Assert winner, p - PIM Join
         Timers: Uptime/Expires
         Interface state: Interface, Next-Hop or VCD, State/Mode

        (*, 239.1.1.1), 00:00:03/stopped, RP 1.1.1.1, flags: SPF
          Incoming interface: Null, RPF nbr 0.0.0.0
          Outgoing interface list: Null

        (1.1.1.1, 239.1.1.1), 00:00:03/00:02:57, flags: PFT
          Incoming interface: Loopback0, RPF nbr 0.0.0.0, Registering
          Outgoing interface list: Null

        (10.1.3.1, 239.1.1.1), 00:00:03/00:02:57, flags: PFT
          Incoming interface: GigabitEthernet2, RPF nbr 0.0.0.0, Registering
          Outgoing interface list: Null

        (*, 224.0.1.40), 2d09h/00:02:56, RP 2.2.2.2, flags: SCL
          Incoming interface: Null, RPF nbr 0.0.0.0
          Outgoing interface list:
            Loopback0, Forward/Sparse, 2d09h/00:02:56

        (*, 224.1.1.1), 00:03:57/00:02:54, RP 172.16.0.0, flags: SJ
          Incoming interface: Null, RPF nbr 224.0.0.0224.0.0.0
          Outgoing interface list:
            ATM0/0, VCD 14, Forward/Sparse, 00:03:57/00:02:53
    '''}

    golden_parsed_output2 = {
        "vrf": {
            "VRF1": {
                 "address_family": {
                      "ipv4": {
                           "multicast_group": {
                                "239.1.1.1": {
                                     "source_address": {
                                          "11.11.11.11": {
                                               "expires": "00:02:55",
                                               "uptime": "00:00:04",
                                               "flags": "PFT",
                                               "incoming_interface_list": {
                                                    "Loopback1": {
                                                         "rpf_info": "Registering",
                                                         "rpf_nbr": "0.0.0.0"
                                                    }
                                               }
                                          },
                                          "*": {
                                               "expires": "stopped",
                                               "uptime": "00:00:04",
                                               "flags": "SPF",
                                               "rp": "11.11.11.11",
                                               "incoming_interface_list": {
                                                    "Null": {
                                                         "rpf_nbr": "0.0.0.0"
                                                    }
                                               }
                                          }
                                     }
                                },
                                "224.0.1.40": {
                                     "source_address": {
                                          "*": {
                                               "expires": "00:02:52",
                                               "uptime": "00:08:58",
                                               "incoming_interface_list": {
                                                    "Null": {
                                                         "rpf_nbr": "0.0.0.0"
                                                    }
                                               },
                                               "outgoing_interface_list": {
                                                    "Loopback1": {
                                                         "state_mode": "Forward/Sparse",
                                                         "uptime": "00:08:58",
                                                         "expire": "00:02:52"
                                                    }
                                               },
                                               "flags": "SJCL",
                                               "rp": "11.11.11.11"}}}}}}}}}

    golden_output2 = {'execute.return_value': '''\
        IP Multicast Routing Table
        Flags: D - Dense, S - Sparse, B - Bidir Group, s - SSM Group, C - Connected,
               L - Local, P - Pruned, R - RP-bit set, F - Register flag,
               T - SPT-bit set, J - Join SPT, M - MSDP created entry, E - Extranet,
               X - Proxy Join Timer Running, A - Candidate for MSDP Advertisement,
               U - URD, I - Received Source Specific Host Report, 
               Z - Multicast Tunnel, z - MDT-data group sender, 
               Y - Joined MDT-data group, y - Sending to MDT-data group, 
               G - Received BGP C-Mroute, g - Sent BGP C-Mroute, 
               N - Received BGP Shared-Tree Prune, n - BGP C-Mroute suppressed, 
               Q - Received BGP S-A Route, q - Sent BGP S-A Route, 
               V - RD & Vector, v - Vector, p - PIM Joins on route, 
               x - VxLAN group
        Outgoing interface flags: H - Hardware switched, A - Assert winner, p - PIM Join
         Timers: Uptime/Expires
         Interface state: Interface, Next-Hop or VCD, State/Mode

        (*, 239.1.1.1), 00:00:04/stopped, RP 11.11.11.11, flags: SPF
          Incoming interface: Null, RPF nbr 0.0.0.0
          Outgoing interface list: Null

        (11.11.11.11, 239.1.1.1), 00:00:04/00:02:55, flags: PFT
          Incoming interface: Loopback1, RPF nbr 0.0.0.0, Registering
          Outgoing interface list: Null

        (*, 224.0.1.40), 00:08:58/00:02:52, RP 11.11.11.11, flags: SJCL
          Incoming interface: Null, RPF nbr 0.0.0.0
          Outgoing interface list:
            Loopback1, Forward/Sparse, 00:08:58/00:02:52
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpMroute(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_vrf_default(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpMroute(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_vrf_non_default(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowIpMroute(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output,self.golden_parsed_output2)


# =============================================
# Unit test for 'show ip mroute static'
# Unit test for 'show ip mroute vrf xxx static'
# =============================================
class test_show_ip_mroute_static(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "vrf": {
            "default": {
                 "mroute": {
                      "172.16.0.0/16": {
                           "path": {
                                "172.30.10.13 1": {
                                     "neighbor_address": "172.30.10.13",
                                     "admin_distance": "1"
                                }
                           }
                      },
                      "172.16.1.0/24": {
                           "path": {
                                "172.30.10.13 1": {
                                     "neighbor_address": "172.30.10.13",
                                     "admin_distance": "1"
                                }}}}}}}

    golden_output = {'execute.return_value': '''\
        Mroute: 172.16.0.0/16, RPF neighbor: 172.30.10.13, distance: 1
        Mroute: 172.16.1.0/24, RPF neighbor: 172.30.10.13, distance: 1
    '''}

    golden_parsed_output2 = {
        "vrf": {
            "VRF1": {
                 "mroute": {
                      "77.77.77.77/32": {
                           "path": {
                                "10.12.12.13 1": {
                                     "neighbor_address": "10.12.12.13",
                                     "admin_distance": "1"
                                }}}}}}}

    golden_output2 = {'execute.return_value': '''\
        Mroute: 77.77.77.77/32, RPF neighbor: 10.12.12.13, distance: 1
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpMrouteStatic(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_vrf_default(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpMrouteStatic(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_vrf_non_default(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowIpMrouteStatic(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output,self.golden_parsed_output2)



if __name__ == '__main__':
    unittest.main()