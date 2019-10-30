# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_mcast import ShowIpMroute,\
                                    ShowIpv6Mroute, \
                                    ShowIpMrouteStatic, \
                                    ShowIpMulticast


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
                                               "expire": "stopped",
                                               "rp": "10.4.1.1",
                                               "flags": "SPF",
                                               'msdp_learned': False,
                                               'rp_bit': False,
                                               "uptime": "00:00:03",
                                               "rpf_nbr": "0.0.0.0",
                                          },
                                          "10.4.1.1": {
                                               "expire": "00:02:57",
                                               "flags": "PFT",
                                               'msdp_learned': False,
                                               'rp_bit': False,
                                               "uptime": "00:00:03",
                                               "rpf_info": "registering",
                                               "rpf_nbr": "0.0.0.0",
                                               "incoming_interface_list": {
                                                    "Loopback0": {
                                                         "rpf_info": "registering",
                                                         "rpf_nbr": "0.0.0.0"
                                                    }
                                               }
                                          },
                                          "10.1.3.1": {
                                               "expire": "00:02:57",
                                               "flags": "PFT",
                                               'msdp_learned': False,
                                               'rp_bit': False,
                                               "uptime": "00:00:03",
                                               "rpf_info": "registering",
                                               "rpf_nbr": "0.0.0.0",
                                               "incoming_interface_list": {
                                                    "GigabitEthernet2": {
                                                         "rpf_info": "registering",
                                                         "rpf_nbr": "0.0.0.0"
                                                    }
                                               }
                                          }
                                     }
                                },
                                "224.0.1.40": {
                                     "source_address": {
                                          "*": {
                                               "expire": "00:02:56",
                                               "outgoing_interface_list": {
                                                    "Loopback0": {
                                                         "expire": "00:02:56",
                                                         "uptime": "2d09h",
                                                         "state_mode": "forward/sparse"
                                                    }
                                               },
                                               "flags": "SCL",
                                               'msdp_learned': False,
                                               'rp_bit': False,
                                               "rp": "10.16.2.2",
                                               "uptime": "2d09h",
                                               "rpf_nbr": "0.0.0.0",
                                          }
                                     }
                                },
                                "224.1.1.1": {
                                     "source_address": {
                                          "*": {
                                               "expire": "00:02:54",
                                               "outgoing_interface_list": {
                                                    "ATM0/0": {
                                                         "expire": "00:02:53",
                                                         "uptime": "00:03:57",
                                                         "vcd": "14",
                                                         "state_mode": "forward/sparse"
                                                    }
                                               },
                                               "flags": "SJ",
                                               'msdp_learned': False,
                                               'rp_bit': False,
                                               "rp": "172.16.0.0",
                                               "uptime": "00:03:57",
                                               "rpf_nbr": "224.0.0.0224.0.0.0"}}}}}}}}}

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

        (*, 239.1.1.1), 00:00:03/stopped, RP 10.4.1.1, flags: SPF
          Incoming interface: Null, RPF nbr 0.0.0.0
          Outgoing interface list: Null

        (10.4.1.1, 239.1.1.1), 00:00:03/00:02:57, flags: PFT
          Incoming interface: Loopback0, RPF nbr 0.0.0.0, Registering
          Outgoing interface list: Null

        (10.1.3.1, 239.1.1.1), 00:00:03/00:02:57, flags: PFT
          Incoming interface: GigabitEthernet2, RPF nbr 0.0.0.0, Registering
          Outgoing interface list: Null

        (*, 224.0.1.40), 2d09h/00:02:56, RP 10.16.2.2, flags: SCL
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
                                          "10.229.11.11": {
                                               "expire": "00:02:55",
                                               "uptime": "00:00:04",
                                               "flags": "PFT",
                                               'msdp_learned': False,
                                               'rp_bit': False,
                                               "rpf_info": "registering",
                                               "rpf_nbr": "0.0.0.0",
                                               "incoming_interface_list": {
                                                    "Loopback1": {
                                                         "rpf_info": "registering",
                                                         "rpf_nbr": "0.0.0.0"
                                                    }
                                               }
                                          },
                                          "*": {
                                               "expire": "stopped",
                                               "uptime": "00:00:04",
                                               "flags": "SPF",
                                               'msdp_learned': False,
                                               'rp_bit': False,
                                               "rp": "10.229.11.11",
                                               "rpf_nbr": "0.0.0.0",
                                          }
                                     }
                                },
                                "224.0.1.40": {
                                     "source_address": {
                                          "*": {
                                               "expire": "00:02:52",
                                               "uptime": "00:08:58",
                                               "rpf_nbr": "0.0.0.0",
                                               "outgoing_interface_list": {
                                                    "Loopback1": {
                                                         "state_mode": "forward/sparse",
                                                         "uptime": "00:08:58",
                                                         "expire": "00:02:52"
                                                    }
                                               },
                                               "flags": "SJCL",
                                               'msdp_learned': False,
                                               'rp_bit': False,
                                               "rp": "10.229.11.11"}}}}}}}}}

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

        (*, 239.1.1.1), 00:00:04/stopped, RP 10.229.11.11, flags: SPF
          Incoming interface: Null, RPF nbr 0.0.0.0
          Outgoing interface list: Null

        (10.229.11.11, 239.1.1.1), 00:00:04/00:02:55, flags: PFT
          Incoming interface: Loopback1, RPF nbr 0.0.0.0, Registering
          Outgoing interface list: Null

        (*, 224.0.1.40), 00:08:58/00:02:52, RP 10.229.11.11, flags: SJCL
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
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_vrf_non_default(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowIpMroute(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output2)



# =======================================
# Unit test for 'show ipv6 mroute'
# Unit test for 'show ipv6 mroute vrf xxx'
# =======================================
class test_show_ipv6_mroute(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "vrf": {
            "default": {
                 "address_family": {
                      "ipv6": {
                           "multicast_group": {
                                "FF07::1": {
                                     "source_address": {
                                          "2001:DB8:999::99": {
                                               "outgoing_interface_list": {
                                                    "POS4/0": {
                                                         "state_mode": "forward",
                                                         "uptime": "00:02:06",
                                                         "expire": "00:03:27"
                                                    }
                                               },
                                               "incoming_interface_list": {
                                                    "POS1/0": {
                                                         "rpf_nbr": "2001:DB8:999::99"
                                                    }
                                               },
                                               "uptime": "00:02:06",
                                               "flags": "SFT",
                                               'rp_bit': False,
                                               'msdp_learned': False,
                                               "rpf_nbr": "2001:DB8:999::99",
                                               "expire": "00:01:23"
                                          },
                                          "*": {
                                               "outgoing_interface_list": {
                                                    "POS4/0": {
                                                         "state_mode": "forward",
                                                         "uptime": "00:04:45",
                                                         "expire": "00:02:47"
                                                    }
                                               },
                                               "incoming_interface_list": {
                                                    "Tunnel5": {
                                                         "rpf_nbr": "2001:db8:90:24::6"
                                                    }
                                               },
                                               "uptime": "00:04:45",
                                               "rp": "2001:DB8:6::6",
                                               "flags": "S",
                                               'msdp_learned': False,
                                               'rp_bit': False,
                                               "rpf_nbr": "2001:db8:90:24::6",
                                               "expire": "00:02:47"
                                          }}}}}}}}}

    golden_output = {'execute.return_value': '''\
        Multicast Routing Table
        Flags:D - Dense, S - Sparse, B - Bidir Group, s - SSM Group, 
               C - Connected, L - Local, I - Received Source Specific Host Report,
               P - Pruned, R - RP-bit set, F - Register flag, T - SPT-bit set,
               J - Join SPT 
        Timers:Uptime/Expires
        Interface state:Interface, State
        (*, FF07::1), 00:04:45/00:02:47, RP 2001:DB8:6::6, flags:S
          Incoming interface:Tunnel5
          RPF nbr:2001:db8:90:24::6
          Outgoing interface list:
            POS4/0, Forward, 00:04:45/00:02:47
        (2001:DB8:999::99, FF07::1), 00:02:06/00:01:23, flags:SFT
          Incoming interface:POS1/0
          RPF nbr:2001:DB8:999::99
          Outgoing interface list:
            POS4/0, Forward, 00:02:06/00:03:27
    '''}

    golden_parsed_output2 = {
        "vrf": {
            "VRF1": {
                 "address_family": {
                      "ipv6": {
                           "multicast_group": {
                                "FF07::1": {
                                     "source_address": {
                                          "2001:DB8:999::99": {
                                               "outgoing_interface_list": {
                                                    "POS4/0": {
                                                         "state_mode": "forward",
                                                         "uptime": "00:02:06",
                                                         "expire": "00:03:27"
                                                    }
                                               },
                                               "incoming_interface_list": {
                                                    "POS1/0": {
                                                         "rpf_nbr": "2001:DB8:999::99"
                                                    }
                                               },
                                               "uptime": "00:02:06",
                                               "flags": "SFT",
                                               'msdp_learned': False,
                                               'rp_bit': False,
                                               "rpf_nbr": "2001:DB8:999::99",
                                               "expire": "00:01:23"
                                          },
                                          "*": {
                                               "outgoing_interface_list": {
                                                    "POS4/0": {
                                                         "state_mode": "forward",
                                                         "uptime": "00:04:45",
                                                         "expire": "00:02:47"
                                                    }
                                               },
                                               "incoming_interface_list": {
                                                    "Tunnel5": {
                                                         "rpf_nbr": "2001:db8:90:24::6"
                                                    }
                                               },
                                               "uptime": "00:04:45",
                                               "rp": "2001:DB8:6::6",
                                               "flags": "S",
                                               'msdp_learned': False,
                                               'rp_bit': False,
                                               "rpf_nbr": "2001:db8:90:24::6",
                                               "expire": "00:02:47"
                                          }}}}}}}}}

    golden_output2 = {'execute.return_value': '''\
        Multicast Routing Table
        Flags:D - Dense, S - Sparse, B - Bidir Group, s - SSM Group, 
               C - Connected, L - Local, I - Received Source Specific Host Report,
               P - Pruned, R - RP-bit set, F - Register flag, T - SPT-bit set,
               J - Join SPT 
        Timers:Uptime/Expires
        Interface state:Interface, State
        (*, FF07::1), 00:04:45/00:02:47, RP 2001:DB8:6::6, flags:S
          Incoming interface:Tunnel5
          RPF nbr:2001:db8:90:24::6
          Outgoing interface list:
            POS4/0, Forward, 00:04:45/00:02:47
        (2001:DB8:999::99, FF07::1), 00:02:06/00:01:23, flags:SFT
          Incoming interface:POS1/0
          RPF nbr:2001:DB8:999::99
          Outgoing interface list:
            POS4/0, Forward, 00:02:06/00:03:27
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpv6Mroute(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_vrf_default(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6Mroute(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_vrf_non_default(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowIpv6Mroute(device=self.device)
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
                      "10.1.77.77/32": {
                           "path": {
                                "10.12.12.13 1": {
                                     "neighbor_address": "10.12.12.13",
                                     "admin_distance": "1"
                                }}}}}}}

    golden_output2 = {'execute.return_value': '''\
        Mroute: 10.1.77.77/32, RPF neighbor: 10.12.12.13, distance: 1
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


# =============================================
# Unit test for 'show ip multicast'
# Unit test for 'show ip multicast vrf xxx'
# =============================================
class test_show_ip_multicast(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "vrf": {
            "default": {
                 "enable": True,
                 "route_limit": "no limit",
                 "multipath": True,
                 "mo_frr": False,
                 "fallback_group_mode": "sparse",
                 "multicast_bound_with_filter_autorp": 0
            }}}

    golden_output = {'execute.return_value': '''\
        Multicast Routing: enabled
        Multicast Multipath: enabled
        Multicast Route limit: No limit
        Multicast Fallback group mode: Sparse
        Number of multicast boundaries configured with filter-autorp option: 0
        MoFRR: Disabled
    '''}

    golden_parsed_output2 = {
        "vrf": {
            "VRF1": {
                 "enable": True,
                 "route_limit": "no limit",
                 "multipath": False,
                 "mo_frr": False,
                 "fallback_group_mode": "sparse",
                 "multicast_bound_with_filter_autorp": 0
            }}}

    golden_output2 = {'execute.return_value': '''\
          Multicast Routing: enabled
          Multicast Multipath: disabled
          Multicast Route limit: No limit
          Multicast Fallback group mode: Sparse
          Number of multicast boundaries configured with filter-autorp option: 0
          MoFRR: Disabled

    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpMulticast(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_vrf_default(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpMulticast(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_vrf_non_default(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowIpMulticast(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output,self.golden_parsed_output2)


if __name__ == '__main__':
    unittest.main()