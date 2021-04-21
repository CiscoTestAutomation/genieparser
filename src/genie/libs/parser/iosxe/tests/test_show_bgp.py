
# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

# iosxe show_bgp
from genie.libs.parser.iosxe.show_bgp import ShowIpBgpSummary,\
                                             ShowIpBgpAllSummary,\
                                             ShowIpBgpNeighborsAdvertisedRoutes,\
                                             ShowBgpSummary


# ==============================
# Unit test for
#   * 'show ip bgp all summary'
# ==============================
class TestShowIpBgpAllSummary(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'bgp_id': 5918,
        'vrf': 
            {'default': 
                {'neighbor': 
                    {'192.168.10.253': 
                        {'address_family': 
                            {'vpnv4 unicast': 
                                {'activity_paths': '5564772/1540171',
                                'activity_prefixes': '2722567/700066',
                                'as': 60103,
                                'attribute_entries': '5098/4898',
                                'bgp_table_version': 9370482,
                                'cache_entries': 
                                    {'filter-list': 
                                        {'memory_usage': 0,
                                        'total_entries': 0},
                                    'route-map': 
                                        {'memory_usage': 0,
                                        'total_entries': 0}},
                                'community_entries': 
                                    {'memory_usage': 60056,
                                    'total_entries': 2301},
                                'entries': 
                                    {'AS-PATH': 
                                        {'memory_usage': 4824,
                                        'total_entries': 201},
                                    'rrinfo': 
                                        {'memory_usage': 20080,
                                        'total_entries': 502}},
                                'input_queue': 0,
                                'local_as': 5918,
                                'msg_rcvd': 0,
                                'msg_sent': 0,
                                'output_queue': 0,
                                'path': 
                                    {'memory_usage': 482879760,
                                    'total_entries': 4023998},
                                'prefixes': 
                                    {'memory_usage': 517657344,
                                    'total_entries': 2022099},
                                'route_identifier': '10.169.197.254',
                                'routing_table_version': 9370482,
                                'scan_interval': 60,
                                'state_pfxrcd': 'Idle',
                                'tbl_ver': 1,
                                'total_memory': 1001967936,
                                'up_down': 'never',
                                'version': 4}}}}}}}

    golden_output1 = {'execute.return_value': '''
        Router#show ip bgp all summary
        Load for five secs: 2%/0%; one minute: 10%; five minutes: 9%
        Time source is NTP, 20:34:39.724 EST Wed Jun 2 2016
        For address family: VPNv4 Unicast
        BGP router identifier 10.169.197.254, local AS number 5918
        BGP table version is 9370482, main routing table version 9370482
        2022099 network entries using 517657344 bytes of memory
        4023998 path entries using 482879760 bytes of memory
        5098/4898 BGP path/bestpath attribute entries using 1345872 bytes of memory
        502 BGP rrinfo entries using 20080 bytes of memory
        201 BGP AS-PATH entries using 4824 bytes of memory
        2301 BGP extended community entries using 60056 bytes of memory
        0 BGP route-map cache entries using 0 bytes of memory
        0 BGP filter-list cache entries using 0 bytes of memory
        BGP using 1001967936 total bytes of memory
        BGP activity 2722567/700066 prefixes, 5564772/1540171 paths, scan interval 60 secs

        Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        192.168.10.253  4        65555     299     332  9370482    0    0 02:27:39      100
        192.168.10.253  4        60001     299     333  9370482    0    0 02:27:46      100
        192.168.10.253  4        60002     299     333  9370482    0    0 02:27:45      100
        192.168.10.253  4        60003     299     331  9370482    0    0 02:27:40      100
        192.168.10.253  4        60004     299     334  9370482    0    0 02:27:39      100
        192.168.10.253  4        60005     299     334  9370482    0    0 02:27:41      100
        192.168.10.253  4        60006     299     333  9370482    0    0 02:27:43      100
        192.168.10.253  4        60007     299     332  9370482    0    0 02:27:41      100
        192.168.10.253  4        60100       0       0        1    0    0 never    Idle
        192.168.10.253  4        60101       0       0        1    0    0 never    Idle
        192.168.10.253  4        60102       0       0        1    0    0 never    Idle
        192.168.10.253  4        60103       0       0        1    0    0 never    Idle
        '''}

    golden_parsed_output2 = {
        "bgp_id": 65109,
        "vrf": {
            "VRF1": {
                "neighbor": {
                    "192.168.10.253": {
                        "address_family": {
                            "vpnv4": {
                                "version": 4,
                                "as": 65555,
                                "msg_rcvd": 10112,
                                "msg_sent": 10107,
                                "tbl_ver": 263,
                                "input_queue": 0,
                                "output_queue": 0,
                                "up_down": "3d05h",
                                "state_pfxrcd": "13",
                                "route_identifier": "10.169.197.254",
                                "local_as": 65109,
                                "bgp_table_version": 263,
                                "routing_table_version": 263,
                                "attribute_entries": "106/104",
                                "prefixes": {
                                    "total_entries": 126,
                                    "memory_usage": 32256
                                },
                                "path": {
                                    "total_entries": 189,
                                    "memory_usage": 25704
                                },
                                "total_memory": 92688,
                                "activity_prefixes": "226/0",
                                "activity_paths": "4035/3696",
                                "scan_interval": 60,
                                "cache_entries": {
                                    "route-map": {
                                        "total_entries": 0,
                                        "memory_usage": 0
                                    },
                                    "filter-list": {
                                        "total_entries": 0,
                                        "memory_usage": 0
                                    }
                                },
                                "entries": {
                                    "rrinfo": {
                                        "total_entries": 1,
                                        "memory_usage": 40
                                    },
                                    "AS-PATH": {
                                        "total_entries": 2,
                                        "memory_usage": 64
                                    }
                                },
                                "community_entries": {
                                    "total_entries": 102,
                                    "memory_usage": 3248
                                }
                            }
                        }
                    }
                }
            },
            "default": {
                "neighbor": {
                    "192.168.10.253": {
                        "address_family": {
                            "vpnv4": {
                                "version": 4,
                                "as": 65555,
                                "msg_rcvd": 0,
                                "msg_sent": 0,
                                "tbl_ver": 1,
                                "input_queue": 0,
                                "output_queue": 0,
                                "up_down": "never",
                                "state_pfxrcd": "Idle",
                                "route_identifier": "10.169.197.254",
                                "local_as": 65109,
                                "bgp_table_version": 263,
                                "routing_table_version": 263,
                                "attribute_entries": "106/104",
                                "prefixes": {
                                    "total_entries": 126,
                                    "memory_usage": 32256
                                },
                                "path": {
                                    "total_entries": 189,
                                    "memory_usage": 25704
                                },
                                "total_memory": 92688,
                                "activity_prefixes": "226/0",
                                "activity_paths": "4035/3696",
                                "scan_interval": 60,
                                "cache_entries": {
                                    "route-map": {
                                        "total_entries": 0,
                                        "memory_usage": 0
                                    },
                                    "filter-list": {
                                        "total_entries": 0,
                                        "memory_usage": 0
                                    }
                                },
                                "entries": {
                                    "rrinfo": {
                                        "total_entries": 1,
                                        "memory_usage": 40
                                    },
                                    "AS-PATH": {
                                        "total_entries": 2,
                                        "memory_usage": 64
                                    }
                                },
                                "community_entries": {
                                    "total_entries": 102,
                                    "memory_usage": 3248
                                }
                            }
                        }
                    },
                    "192.168.36.119": {
                        "address_family": {
                            "vpnv4": {
                                "version": 4,
                                "as": 65109,
                                "msg_rcvd": 10293,
                                "msg_sent": 10213,
                                "tbl_ver": 263,
                                "input_queue": 0,
                                "output_queue": 0,
                                "up_down": "3d05h",
                                "state_pfxrcd": "62",
                                "route_identifier": "10.169.197.254",
                                "local_as": 65109,
                                "bgp_table_version": 263,
                                "routing_table_version": 263,
                                "attribute_entries": "106/104",
                                "prefixes": {
                                    "total_entries": 126,
                                    "memory_usage": 32256
                                },
                                "path": {
                                    "total_entries": 189,
                                    "memory_usage": 25704
                                },
                                "total_memory": 92688,
                                "activity_prefixes": "226/0",
                                "activity_paths": "4035/3696",
                                "scan_interval": 60,
                                "cache_entries": {
                                    "route-map": {
                                        "total_entries": 0,
                                        "memory_usage": 0
                                    },
                                    "filter-list": {
                                        "total_entries": 0,
                                        "memory_usage": 0
                                    }
                                },
                                "entries": {
                                    "rrinfo": {
                                        "total_entries": 1,
                                        "memory_usage": 40
                                    },
                                    "AS-PATH": {
                                        "total_entries": 2,
                                        "memory_usage": 64
                                    }
                                },
                                "community_entries": {
                                    "total_entries": 102,
                                    "memory_usage": 3248
                                }
                            }
                        }
                    },
                    "192.168.36.120": {
                        "address_family": {
                            "vpnv4": {
                                "version": 4,
                                "as": 65109,
                                "msg_rcvd": 9930,
                                "msg_sent": 9826,
                                "tbl_ver": 263,
                                "input_queue": 0,
                                "output_queue": 0,
                                "up_down": "3d02h",
                                "state_pfxrcd": "62",
                                "route_identifier": "10.169.197.254",
                                "local_as": 65109,
                                "bgp_table_version": 263,
                                "routing_table_version": 263,
                                "attribute_entries": "106/104",
                                "prefixes": {
                                    "total_entries": 126,
                                    "memory_usage": 32256
                                },
                                "path": {
                                    "total_entries": 189,
                                    "memory_usage": 25704
                                },
                                "total_memory": 92688,
                                "activity_prefixes": "226/0",
                                "activity_paths": "4035/3696",
                                "scan_interval": 60,
                                "cache_entries": {
                                    "route-map": {
                                        "total_entries": 0,
                                        "memory_usage": 0
                                    },
                                    "filter-list": {
                                        "total_entries": 0,
                                        "memory_usage": 0
                                    }
                                },
                                "entries": {
                                    "rrinfo": {
                                        "total_entries": 1,
                                        "memory_usage": 40
                                    },
                                    "AS-PATH": {
                                        "total_entries": 2,
                                        "memory_usage": 64
                                    }
                                },
                                "community_entries": {
                                    "total_entries": 102,
                                    "memory_usage": 3248
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    def test_show_ip_bgp_all_summary_empty(self):
        self.device1 = Mock(**self.empty_output)
        bgp_summary_obj = ShowIpBgpAllSummary(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = bgp_summary_obj.parse()

    def test_show_ip_bgp_all_summary_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpBgpAllSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_bgp_all_summary_golden2(self):

        def mapper(key):
            return self.outputs[key]

        raw1 = '''\
         address-family ipv4 vrf VRF1
          bgp router-id 192.168.10.254
          redistribute connected
          redistribute static
          neighbor 192.168.10.253 remote-as 65555
          neighbor 192.168.10.253 timers 30 90 15
          neighbor 192.168.10.253 activate
          neighbor 192.168.10.253 as-override
          neighbor 192.168.10.253 route-map prepend in         
        '''

        golden_output2 = '''\
            PE1#show ip bgp vpnv4 all summary
            Load for five secs: 1%/0%; one minute: 1%; five minutes: 1%
            Time source is NTP, 05:46:49.882 EST Tue May 28 2019
            BGP router identifier 10.169.197.254, local AS number 65109
            BGP table version is 263, main routing table version 263
            126 network entries using 32256 bytes of memory
            189 path entries using 25704 bytes of memory
            106/104 BGP path/bestpath attribute entries using 31376 bytes of memory
            1 BGP rrinfo entries using 40 bytes of memory
            2 BGP AS-PATH entries using 64 bytes of memory
            102 BGP extended community entries using 3248 bytes of memory
            0 BGP route-map cache entries using 0 bytes of memory
            0 BGP filter-list cache entries using 0 bytes of memory
            BGP using 92688 total bytes of memory
            BGP activity 226/0 prefixes, 4035/3696 paths, scan interval 60 secs

            Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
            192.168.10.253  4        65555   10112   10107      263    0    0 3d05h          13
            192.168.10.253  4        65555       0       0        1    0    0 never    Idle           
            192.168.36.119 4         65109   10293   10213      263    0    0 3d05h          62
            192.168.36.120 4         65109    9930    9826      263    0    0 3d02h          62
        '''

        self.outputs = {}
        self.maxDiff = None 
        self.outputs['show ip bgp vpnv4 all summary'] = golden_output2
        self.outputs['show run | sec address-family ipv4 vrf'] = raw1
        self.outputs['show run | sec address-family ipv6 vrf'] = ''

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper

        obj = ShowIpBgpAllSummary(device=self.device)
        parsed_output = obj.parse(address_family='vpnv4')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_ip_bgp_all_summary_golden3(self):

        def mapper(key):
            return self.outputs[key]
        
        raw1 = '''
            [2019-06-05 09:46:16,345] +++ R1_xe: executing command 'show ip bgp all summary' +++
            show ip bgp all summary
            For address family: IPv4 Unicast
            BGP router identifier 10.4.1.1, local AS number 65000
            BGP table version is 4, main routing table version 4
            3 network entries using 744 bytes of memory
            3 path entries using 408 bytes of memory
            3/3 BGP path/bestpath attribute entries using 840 bytes of memory
            2 BGP extended community entries using 500 bytes of memory
            0 BGP route-map cache entries using 0 bytes of memory
            0 BGP filter-list cache entries using 0 bytes of memory
            BGP using 2492 total bytes of memory
            BGP activity 12/0 prefixes, 12/0 paths, scan interval 60 secs

            Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
            10.16.2.2         4        65000   30178   33211        4    0    0 2w6d            1
            10.36.3.3         4        65000   30182   33227        4    0    0 2w6d            1

            For address family: IPv6 Unicast
            BGP router identifier 10.4.1.1, local AS number 65000
            BGP table version is 5, main routing table version 5
            3 network entries using 816 bytes of memory
            3 path entries using 456 bytes of memory
            3/3 BGP path/bestpath attribute entries using 840 bytes of memory
            2 BGP extended community entries using 500 bytes of memory
            0 BGP route-map cache entries using 0 bytes of memory
            0 BGP filter-list cache entries using 0 bytes of memory
            BGP using 2612 total bytes of memory
            BGP activity 12/0 prefixes, 12/0 paths, scan interval 60 secs

            Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
            2001:2:2:2::2   4        65000   30178   33214        5    0    0 2w6d            1
            2001:3:3:3::3   4        65000   30182   33196        5    0    0 2w6d            1

            For address family: VPNv4 Unicast
            BGP router identifier 10.4.1.1, local AS number 65000
            BGP table version is 4, main routing table version 4
            3 network entries using 768 bytes of memory
            3 path entries using 408 bytes of memory
            3/3 BGP path/bestpath attribute entries using 888 bytes of memory
            2 BGP extended community entries using 500 bytes of memory
            0 BGP route-map cache entries using 0 bytes of memory
            0 BGP filter-list cache entries using 0 bytes of memory
            BGP using 2564 total bytes of memory
            BGP activity 12/0 prefixes, 12/0 paths, scan interval 60 secs

            Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
            10.16.2.2         4        65000   30178   33215        4    0    0 2w6d            1
            10.36.3.3         4        65000   30182   33221        4    0    0 2w6d            1

            For address family: VPNv6 Unicast
            BGP router identifier 10.4.1.1, local AS number 65000
            BGP table version is 5, main routing table version 5
            3 network entries using 840 bytes of memory
            3 path entries using 468 bytes of memory
            3/3 BGP path/bestpath attribute entries using 888 bytes of memory
            2 BGP extended community entries using 500 bytes of memory
            0 BGP route-map cache entries using 0 bytes of memory
            0 BGP filter-list cache entries using 0 bytes of memory
            BGP using 2696 total bytes of memory
            BGP activity 12/0 prefixes, 12/0 paths, scan interval 60 secs

            Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
            2001:2:2:2::2   4        65000   30178   33203        5    0    0 2w6d            1
            2001:3:3:3::3   4        65000   30183   33216        5    0    0 2w6d            1
        '''

        raw2 = '''
            [2019-06-05 09:46:59,306] +++ R1_xe: executing command 'show run | sec address-family ipv4 vrf' +++
            show run | sec address-family ipv4 vrf
             address-family ipv4 vrf VRF1
              network 10.1.0.0
              network 10.0.0.0
              no auto-summary
             address-family ipv4 vrf VRF1
              network 10.4.1.1 mask 255.255.255.255
              neighbor 10.16.2.2 remote-as 65000
              neighbor 10.16.2.2 update-source Loopback300
              neighbor 10.16.2.2 activate
              neighbor 10.36.3.3 remote-as 65000
              neighbor 10.36.3.3 update-source Loopback300
              neighbor 10.36.3.3 activate
        '''

        raw3 = '''
            [2019-06-05 09:47:19,474] +++ R1_xe: executing command 'show run | sec address-family ipv6 vrf' +++
            show run | sec address-family ipv6 vrf
             address-family ipv6 vrf VRF1
              network 2001:1:1:1::1/128
              neighbor 2001:2:2:2::2 remote-as 65000
              neighbor 2001:2:2:2::2 update-source Loopback300
              neighbor 2001:2:2:2::2 activate
              neighbor 2001:3:3:3::3 remote-as 65000
              neighbor 2001:3:3:3::3 update-source Loopback300
              neighbor 2001:3:3:3::3 activate
             address-family ipv6 vrf VRF1
        '''

        parsed_output3 = {
            "bgp_id": 65000,
            "vrf": {
                "VRF1": {
                    "neighbor": {
                        "10.16.2.2": {
                            "address_family": {
                                "vpnv4 unicast": {
                                    "activity_paths": "12/0",
                                    "activity_prefixes": "12/0",
                                    "as": 65000,
                                    "attribute_entries": "3/3",
                                    "bgp_table_version": 4,
                                    "cache_entries": {
                                        "filter-list": {
                                            "memory_usage": 0,
                                            "total_entries": 0
                                        },
                                        "route-map": {
                                            "memory_usage": 0,
                                            "total_entries": 0
                                        }
                                    },
                                    "community_entries": {
                                        "memory_usage": 500,
                                        "total_entries": 2
                                    },
                                    "input_queue": 0,
                                    "local_as": 65000,
                                    "msg_rcvd": 30178,
                                    "msg_sent": 33215,
                                    "output_queue": 0,
                                    "path": {
                                        "memory_usage": 408,
                                        "total_entries": 3
                                    },
                                    "prefixes": {
                                        "memory_usage": 768,
                                        "total_entries": 3
                                    },
                                    "route_identifier": "10.4.1.1",
                                    "routing_table_version": 4,
                                    "scan_interval": 60,
                                    "state_pfxrcd": "1",
                                    "tbl_ver": 4,
                                    "total_memory": 2564,
                                    "up_down": "2w6d",
                                    "version": 4
                                }
                            }
                        },
                        "2001:2:2:2::2": {
                            "address_family": {
                                "vpnv6 unicast": {
                                    "activity_paths": "12/0",
                                    "activity_prefixes": "12/0",
                                    "as": 65000,
                                    "attribute_entries": "3/3",
                                    "bgp_table_version": 5,
                                    "cache_entries": {
                                        "filter-list": {
                                            "memory_usage": 0,
                                            "total_entries": 0
                                        },
                                        "route-map": {
                                            "memory_usage": 0,
                                            "total_entries": 0
                                        }
                                    },
                                    "community_entries": {
                                        "memory_usage": 500,
                                        "total_entries": 2
                                    },
                                    "input_queue": 0,
                                    "local_as": 65000,
                                    "msg_rcvd": 30178,
                                    "msg_sent": 33203,
                                    "output_queue": 0,
                                    "path": {
                                        "memory_usage": 468,
                                        "total_entries": 3
                                    },
                                    "prefixes": {
                                        "memory_usage": 840,
                                        "total_entries": 3
                                    },
                                    "route_identifier": "10.4.1.1",
                                    "routing_table_version": 5,
                                    "scan_interval": 60,
                                    "state_pfxrcd": "1",
                                    "tbl_ver": 5,
                                    "total_memory": 2696,
                                    "up_down": "2w6d",
                                    "version": 4
                                }
                            }
                        },
                        "2001:3:3:3::3": {
                            "address_family": {
                                "vpnv6 unicast": {
                                    "activity_paths": "12/0",
                                    "activity_prefixes": "12/0",
                                    "as": 65000,
                                    "attribute_entries": "3/3",
                                    "bgp_table_version": 5,
                                    "cache_entries": {
                                        "filter-list": {
                                            "memory_usage": 0,
                                            "total_entries": 0
                                        },
                                        "route-map": {
                                            "memory_usage": 0,
                                            "total_entries": 0
                                        }
                                    },
                                    "community_entries": {
                                        "memory_usage": 500,
                                        "total_entries": 2
                                    },
                                    "input_queue": 0,
                                    "local_as": 65000,
                                    "msg_rcvd": 30183,
                                    "msg_sent": 33216,
                                    "output_queue": 0,
                                    "path": {
                                        "memory_usage": 468,
                                        "total_entries": 3
                                    },
                                    "prefixes": {
                                        "memory_usage": 840,
                                        "total_entries": 3
                                    },
                                    "route_identifier": "10.4.1.1",
                                    "routing_table_version": 5,
                                    "scan_interval": 60,
                                    "state_pfxrcd": "1",
                                    "tbl_ver": 5,
                                    "total_memory": 2696,
                                    "up_down": "2w6d",
                                    "version": 4
                                }
                            }
                        },
                        "10.36.3.3": {
                            "address_family": {
                                "vpnv4 unicast": {
                                    "activity_paths": "12/0",
                                    "activity_prefixes": "12/0",
                                    "as": 65000,
                                    "attribute_entries": "3/3",
                                    "bgp_table_version": 4,
                                    "cache_entries": {
                                        "filter-list": {
                                            "memory_usage": 0,
                                            "total_entries": 0
                                        },
                                        "route-map": {
                                            "memory_usage": 0,
                                            "total_entries": 0
                                        }
                                    },
                                    "community_entries": {
                                        "memory_usage": 500,
                                        "total_entries": 2
                                    },
                                    "input_queue": 0,
                                    "local_as": 65000,
                                    "msg_rcvd": 30182,
                                    "msg_sent": 33221,
                                    "output_queue": 0,
                                    "path": {
                                        "memory_usage": 408,
                                        "total_entries": 3
                                    },
                                    "prefixes": {
                                        "memory_usage": 768,
                                        "total_entries": 3
                                    },
                                    "route_identifier": "10.4.1.1",
                                    "routing_table_version": 4,
                                    "scan_interval": 60,
                                    "state_pfxrcd": "1",
                                    "tbl_ver": 4,
                                    "total_memory": 2564,
                                    "up_down": "2w6d",
                                    "version": 4
                                }
                            }
                        }
                    }
                },
                "default": {
                    "neighbor": {
                        "10.16.2.2": {
                            "address_family": {
                                "ipv4 unicast": {
                                    "activity_paths": "12/0",
                                    "activity_prefixes": "12/0",
                                    "as": 65000,
                                    "attribute_entries": "3/3",
                                    "bgp_table_version": 4,
                                    "cache_entries": {
                                        "filter-list": {
                                            "memory_usage": 0,
                                            "total_entries": 0
                                        },
                                        "route-map": {
                                            "memory_usage": 0,
                                            "total_entries": 0
                                        }
                                    },
                                    "community_entries": {
                                        "memory_usage": 500,
                                        "total_entries": 2
                                    },
                                    "input_queue": 0,
                                    "local_as": 65000,
                                    "msg_rcvd": 30178,
                                    "msg_sent": 33211,
                                    "output_queue": 0,
                                    "path": {
                                        "memory_usage": 408,
                                        "total_entries": 3
                                    },
                                    "prefixes": {
                                        "memory_usage": 744,
                                        "total_entries": 3
                                    },
                                    "route_identifier": "10.4.1.1",
                                    "routing_table_version": 4,
                                    "scan_interval": 60,
                                    "state_pfxrcd": "1",
                                    "tbl_ver": 4,
                                    "total_memory": 2492,
                                    "up_down": "2w6d",
                                    "version": 4
                                }
                            }
                        },
                        "2001:2:2:2::2": {
                            "address_family": {
                                "ipv6 unicast": {
                                    "activity_paths": "12/0",
                                    "activity_prefixes": "12/0",
                                    "as": 65000,
                                    "attribute_entries": "3/3",
                                    "bgp_table_version": 5,
                                    "cache_entries": {
                                        "filter-list": {
                                            "memory_usage": 0,
                                            "total_entries": 0
                                        },
                                        "route-map": {
                                            "memory_usage": 0,
                                            "total_entries": 0
                                        }
                                    },
                                    "community_entries": {
                                        "memory_usage": 500,
                                        "total_entries": 2
                                    },
                                    "input_queue": 0,
                                    "local_as": 65000,
                                    "msg_rcvd": 30178,
                                    "msg_sent": 33214,
                                    "output_queue": 0,
                                    "path": {
                                        "memory_usage": 456,
                                        "total_entries": 3
                                    },
                                    "prefixes": {
                                        "memory_usage": 816,
                                        "total_entries": 3
                                    },
                                    "route_identifier": "10.4.1.1",
                                    "routing_table_version": 5,
                                    "scan_interval": 60,
                                    "state_pfxrcd": "1",
                                    "tbl_ver": 5,
                                    "total_memory": 2612,
                                    "up_down": "2w6d",
                                    "version": 4
                                }
                            }
                        },
                        "2001:3:3:3::3": {
                            "address_family": {
                                "ipv6 unicast": {
                                    "activity_paths": "12/0",
                                    "activity_prefixes": "12/0",
                                    "as": 65000,
                                    "attribute_entries": "3/3",
                                    "bgp_table_version": 5,
                                    "cache_entries": {
                                        "filter-list": {
                                            "memory_usage": 0,
                                            "total_entries": 0
                                        },
                                        "route-map": {
                                            "memory_usage": 0,
                                            "total_entries": 0
                                        }
                                    },
                                    "community_entries": {
                                        "memory_usage": 500,
                                        "total_entries": 2
                                    },
                                    "input_queue": 0,
                                    "local_as": 65000,
                                    "msg_rcvd": 30182,
                                    "msg_sent": 33196,
                                    "output_queue": 0,
                                    "path": {
                                        "memory_usage": 456,
                                        "total_entries": 3
                                    },
                                    "prefixes": {
                                        "memory_usage": 816,
                                        "total_entries": 3
                                    },
                                    "route_identifier": "10.4.1.1",
                                    "routing_table_version": 5,
                                    "scan_interval": 60,
                                    "state_pfxrcd": "1",
                                    "tbl_ver": 5,
                                    "total_memory": 2612,
                                    "up_down": "2w6d",
                                    "version": 4
                                }
                            }
                        },
                        "10.36.3.3": {
                            "address_family": {
                                "ipv4 unicast": {
                                    "activity_paths": "12/0",
                                    "activity_prefixes": "12/0",
                                    "as": 65000,
                                    "attribute_entries": "3/3",
                                    "bgp_table_version": 4,
                                    "cache_entries": {
                                        "filter-list": {
                                            "memory_usage": 0,
                                            "total_entries": 0
                                        },
                                        "route-map": {
                                            "memory_usage": 0,
                                            "total_entries": 0
                                        }
                                    },
                                    "community_entries": {
                                        "memory_usage": 500,
                                        "total_entries": 2
                                    },
                                    "input_queue": 0,
                                    "local_as": 65000,
                                    "msg_rcvd": 30182,
                                    "msg_sent": 33227,
                                    "output_queue": 0,
                                    "path": {
                                        "memory_usage": 408,
                                        "total_entries": 3
                                    },
                                    "prefixes": {
                                        "memory_usage": 744,
                                        "total_entries": 3
                                    },
                                    "route_identifier": "10.4.1.1",
                                    "routing_table_version": 4,
                                    "scan_interval": 60,
                                    "state_pfxrcd": "1",
                                    "tbl_ver": 4,
                                    "total_memory": 2492,
                                    "up_down": "2w6d",
                                    "version": 4
                                }
                            }
                        }
                    }
                }
            }
        }

        self.outputs = {}
        self.maxDiff = None 
        self.outputs['show ip bgp all summary'] = raw1
        self.outputs['show run | sec address-family ipv4 vrf'] = raw2
        self.outputs['show run | sec address-family ipv6 vrf'] = raw3

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper

        obj = ShowIpBgpAllSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, parsed_output3)



# ====================================================
# Unit test for
#   * 'show ip bgp {address_family} vrf {vrf} summary
# ====================================================
class TestShowIpBgpSummary(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'bgp_id': 5918,
        'vrf': 
            {'L3VPN-1151': 
                {'neighbor': 
                    {'192.168.10.253': 
                        {'address_family': 
                            {'vpnv4': 
                                {'activity_paths': '5564978/1540171',
                                'activity_prefixes': '2722671/700066',
                                'as': 61100,
                                'attribute_entries': '5101/4901',
                                'bgp_table_version': 9370786,
                                'cache_entries': 
                                    {'filter-list': 
                                        {'memory_usage': 0,
                                        'total_entries': 0},
                                    'route-map': 
                                        {'memory_usage': 0,
                                        'total_entries': 0}},
                                'community_entries': 
                                    {'memory_usage': 60120,
                                    'total_entries': 2303},
                                'entries': 
                                    {'AS-PATH': 
                                        {'memory_usage': 4824,
                                        'total_entries': 201},
                                    'rrinfo': 
                                        {'memory_usage': 20080,
                                        'total_entries': 502}},
                                'input_queue': 0,
                                'local_as': 5918,
                                'msg_rcvd': 0,
                                'msg_sent': 0,
                                'output_queue': 0,
                                'path': 
                                    {'memory_usage': 24360,
                                    'total_entries': 203},
                                'prefixes': 
                                    {'memory_usage': 26112,
                                    'total_entries': 102},
                                'route_identifier': '192.168.10.254',
                                'routing_table_version': 9370786,
                                'scan_interval': 60,
                                'state_pfxrcd': 'Idle',
                                'tbl_ver': 1,
                                'total_memory': 1482160,
                                'up_down': 'never',
                                'version': 4}}}}}}}

    golden_output1 = {'execute.return_value': '''
        Router#show ip bgp vpnv4 vrf L3VPN-1151 summary
        Load for five secs: 1%/0%; one minute: 57%; five minutes: 26%
        Time source is NTP, 20:39:33.145 EST Wed Jun 2 2016
        BGP router identifier 192.168.10.254, local AS number 5918
        BGP table version is 9370786, main routing table version 9370786
        102 network entries using 26112 bytes of memory
        203 path entries using 24360 bytes of memory
        5101/4901 BGP path/bestpath attribute entries using 1346664 bytes of memory
        502 BGP rrinfo entries using 20080 bytes of memory
        201 BGP AS-PATH entries using 4824 bytes of memory
        2303 BGP extended community entries using 60120 bytes of memory
        0 BGP route-map cache entries using 0 bytes of memory
        0 BGP filter-list cache entries using 0 bytes of memory
        BGP using 1482160 total bytes of memory
        BGP activity 2722671/700066 prefixes, 5564978/1540171 paths, scan interval 60 secs

        Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        192.168.10.253  4        61100       0       0        1    0    0 never    Idle
        '''}

    golden_parsed_output2 = {
        'bgp_id': 65109, 
        'vrf': {
            'VRF1': {
                'neighbor': {
                    '192.168.10.253': {
                        'address_family': {
                            'vpnv4': {
                                'version': 4, 
                                'as': 65555, 
                                'msg_rcvd': 9586, 
                                'msg_sent': 9590, 
                                'tbl_ver': 250, 
                                'input_queue': 0, 
                                'output_queue': 0, 
                                'up_down': '3d01h', 
                                'state_pfxrcd': '13', 
                                'route_identifier': '192.168.10.254', 
                                'local_as': 65109, 
                                'bgp_table_version': 250, 
                                'routing_table_version': 250, 
                                'attribute_entries': '105/104', 
                                'prefixes': {
                                    'total_entries': 25, 
                                    'memory_usage': 6400}, 
                                'path': {
                                    'total_entries': 38, 
                                    'memory_usage': 5168}, 
                                'total_memory': 45960, 
                                'activity_prefixes': '226/0', 
                                'activity_paths': '787/448', 
                                'scan_interval': 60, 
                                'cache_entries': {
                                    'route-map': {
                                        'total_entries': 0, 
                                        'memory_usage': 0}, 
                                    'filter-list': {
                                        'total_entries': 0, 
                                        'memory_usage': 0}}, 
                                'entries': {
                                    'rrinfo': {
                                        'total_entries': 1, 'memory_usage': 40}, 
                                    'AS-PATH': {
                                        'total_entries': 1, 
                                        'memory_usage': 24}}, 
                                    'community_entries': {
                                        'total_entries': 102, 
                                        'memory_usage': 3248}}}}}}}}

    golden_parsed_output3 = {
        'bgp_id': 65109,
        'vrf': {
            'VRF1': {
                'neighbor': {
                    '192.168.10.253': {
                        'address_family': {
                            'vpnv4 unicast': {
                                'activity_paths': '787/448',
                                'activity_prefixes': '226/0',
                                'as': 65555,
                                'attribute_entries': '105/104',
                                'bgp_table_version': 250,
                                'cache_entries': {
                                    'filter-list': {
                                    'memory_usage': 0,
                                    'total_entries': 0},
                                'route-map': {
                                    'memory_usage': 0,
                                    'total_entries': 0}},
                                'community_entries': {
                                    'memory_usage': 3248,
                                    'total_entries': 102},
                                'entries': {
                                    'AS-PATH': {
                                        'memory_usage': 24,
                                        'total_entries': 1},
                                    'rrinfo': {
                                        'memory_usage': 40,
                                        'total_entries': 1}},
                                'input_queue': 0,
                                'local_as': 65109,
                                'msg_rcvd': 9694,
                                'msg_sent': 9698,
                                'output_queue': 0,
                                'path': {
                                    'memory_usage': 5168,
                                    'total_entries': 38},
                                'prefixes': {
                                    'memory_usage': 6400,
                                    'total_entries': 25},
                                'route_identifier': '192.168.10.254',
                                'routing_table_version': 250,
                                'scan_interval': 60,
                                'state_pfxrcd': '13',
                                'tbl_ver': 250,
                                'total_memory': 45960,
                                'up_down': '3d02h',
                                'version': 4}}}}}}}

    def test_show_ip_bgp_summary_empty(self):
        self.device1 = Mock(**self.empty_output)
        bgp_summary_obj = ShowIpBgpSummary(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = bgp_summary_obj.parse()

    def test_show_ip_bgp_summary_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpBgpSummary(device=self.device)
        parsed_output = obj.parse(address_family='vpnv4', vrf='L3VPN-1151')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_bgp_summary_golden2(self):
        def mapper(key):
            return self.outputs[key]

        raw1 = '''/
            PE1#show ip bgp vpnv4 rd 65109:4093 summary 
            Load for five secs: 1%/0%; one minute: 1%; five minutes: 1%
            Time source is NTP, 23:18:11.225 EST Mon Jun 3 2019
            BGP router identifier 192.168.10.254, local AS number 65109
            BGP table version is 250, main routing table version 250
            25 network entries using 6400 bytes of memory
            38 path entries using 5168 bytes of memory
            105/104 BGP path/bestpath attribute entries using 31080 bytes of memory
            1 BGP rrinfo entries using 40 bytes of memory
            1 BGP AS-PATH entries using 24 bytes of memory
            102 BGP extended community entries using 3248 bytes of memory
            0 BGP route-map cache entries using 0 bytes of memory
            0 BGP filter-list cache entries using 0 bytes of memory
            BGP using 45960 total bytes of memory
            BGP activity 226/0 prefixes, 787/448 paths, scan interval 60 secs

            Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
            192.168.10.253  4        65555    9586    9590      250    0    0 3d01h          13
        '''

        raw2 = '''
            show vrf
            Load for five secs: 1%/0%; one minute: 1%; five minutes: 1%
            Time source is NTP, 23:19:19.766 EST Mon Jun 3 2019

              Name                             Default RD            Protocols   Interfaces
              VRF1                          65109:4093             ipv4        Gi8.4093              
        '''

        self.outputs = {}
        self.maxDiff = None
        self.outputs['show vrf'] = raw2
        self.outputs['show ip bgp vpnv4 rd 65109:4093 summary'] = raw1

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        obj = ShowIpBgpSummary(device=self.device)
        parsed_output = obj.parse(address_family='vpnv4', rd='65109:4093')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_ip_bgp_summary_golden3(self):
        def mapper(key):
            return self.outputs[key]

        raw1 = '''/
            PE1#show bgp vpnv4 unicast rd 65109:4093 summary
            Load for five secs: 1%/0%; one minute: 1%; five minutes: 1%
            Time source is NTP, 00:07:47.856 EST Tue Jun 4 2019
            BGP router identifier 192.168.10.254, local AS number 65109
            BGP table version is 250, main routing table version 250
            25 network entries using 6400 bytes of memory
            38 path entries using 5168 bytes of memory
            105/104 BGP path/bestpath attribute entries using 31080 bytes of memory
            1 BGP rrinfo entries using 40 bytes of memory
            1 BGP AS-PATH entries using 24 bytes of memory
            102 BGP extended community entries using 3248 bytes of memory
            0 BGP route-map cache entries using 0 bytes of memory
            0 BGP filter-list cache entries using 0 bytes of memory
            BGP using 45960 total bytes of memory
            BGP activity 226/0 prefixes, 787/448 paths, scan interval 60 secs

            Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
            192.168.10.253  4        65555    9694    9698      250    0    0 3d02h          13
        '''

        raw2 = '''
            show vrf
            Load for five secs: 1%/0%; one minute: 1%; five minutes: 1%
            Time source is NTP, 23:19:19.766 EST Mon Jun 3 2019

              Name                             Default RD            Protocols   Interfaces
              VRF1                          65109:4093             ipv4        Gi8.4093              
        '''

        self.outputs = {}
        self.maxDiff = None
        self.outputs['show vrf'] = raw2
        self.outputs['show bgp vpnv4 unicast rd 65109:4093 summary'] = raw1

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        obj = ShowBgpSummary(device=self.device)
        parsed_output = obj.parse(address_family='vpnv4 unicast', rd='65109:4093')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

# =========================================================
# Unit test for:
#   * 'show ip bgp neighbors {neighbor} advertised-routes'
# =========================================================
class TestShowIpBgpNeighborsAdvertisedRoutes(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': 
            {'default': 
                {'neighbor': 
                    {'10.169.197.252': 
                        {'address_family': 
                            {'': 
                                {'advertised': 
                                    {'10.69.9.9/32': 
                                        {'index': 
                                            {1: 
                                                {'status_codes': '*>',
                                                'next_hop': '192.168.36.119',
                                                'origin_codes': '?',
                                                'weight': 0,
                                                'metric': 0,
                                                'path': '5918'},
                                            2:
                                                {'status_codes': '*b',
                                                'path_type': 'a',
                                                'next_hop': '192.168.36.120',
                                                'origin_codes': '?',
                                                'weight': 0,
                                                'metric': 0,
                                                'path': '5918'}}}},
                                'bgp_table_version': 2,
                                'local_router_id': '10.169.197.254'}}}}}}}

    golden_output1 = {'execute.return_value': '''
        Router#show ip bgp neighbors 10.169.197.252 advertised-routes
        Load for five secs: 38%/0%; one minute: 11%; five minutes: 13%
        Time source is NTP, 17:40:07.943 EST Sat Jun 12 2016

        BGP table version is 2, local router ID is 10.169.197.254
        Status codes: s suppressed, d damped, h history, * valid, > best, i - internal, 
                      r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter, 
                      x best-external, a additional-path, c RIB-compressed, 
        Origin codes: i - IGP, e - EGP, ? - incomplete
        RPKI validation codes: V valid, I invalid, N Not found

             Network          Next Hop            Metric LocPrf Weight Path
         *>  10.69.9.9/32       192.168.36.119          0             0 5918 ?
         *b a10.69.9.9/32       192.168.36.120          0             0 5918 ?
        '''}

    golden_output2 = {'execute.return_value' : '''
    BGP table version is 166, local router ID is 172.16.1.1

    Status codes: s suppressed, d damped, h history, * valid, > best, i - internal, 

                  r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter, 

                  x best-external, a additional-path, c RIB-compressed, 

                  t secondary path, L long-lived-stale,

    Origin codes: i - IGP, e - EGP, ? - incomplete

    RPKI validation codes: V valid, I invalid, N Not found



         Network          Next Hop            Metric LocPrf Weight Path

    Route Distinguisher: 65000:100 (default for vrf TEST-VPN) VRF Router ID 172.16.1.1

     *>   192.168.1.0      0.0.0.0                  0         32768 ?

    '''}
    golden_parsed_output2 = {
        'vrf': {
            'default': {
                'neighbor': {
                    '172.16.1.1': {
                        'address_family': {
                            'vpnv4': {
                                'advertised': {
                                    },
                                'bgp_table_version': 166,
                                'local_router_id': '172.16.1.1',
                                },
                            'vpnv4 RD 65000:100': {
                                'bgp_table_version': 166,
                                'local_router_id': '172.16.1.1',
                                'route_distinguisher': '65000:100',
                                'default_vrf': 'TEST-VPN',
                                'advertised': {
                                    '192.168.1.0': {
                                        'index': {
                                            1: {
                                                'status_codes': '*>',
                                                'next_hop': '0.0.0.0',
                                                'origin_codes': '?',
                                                'weight': 32768,
                                                'localprf': 0,
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }
    def test_show_ip_bgp_neighbors_advertised_routes_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpBgpNeighborsAdvertisedRoutes(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(neighbor='10.4.6.6')

    def test_show_ip_bgp_neighbors_advertised_routes_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpBgpNeighborsAdvertisedRoutes(device=self.device)
        parsed_output = obj.parse(neighbor='10.169.197.252')
        self.assertEqual(parsed_output,self.golden_parsed_output1)

    def test_show_ip_bgp_rd_neighbors_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowIpBgpNeighborsAdvertisedRoutes(device=self.device)
        parsed_output = obj.parse(address_family='vpnv4',
                rd='65000:100', neighbor='172.16.1.1')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_golden(self):
        def mapper(key):
            return self.outputs[key]

        raw1 = '''\
            show bgp all neighbors | i BGP neighbor
            BGP neighbor is 10.120.202.189,  remote AS 65109, internal link
            BGP neighbor is 192.168.0.6,  remote AS 2516, external link
            BGP neighbor is 10.225.10.253,  vrf CE1test,  remote AS 60000, external link
            External BGP neighbor configured for connected checks (single-hop no-disable-connected-check)
            BGP neighbor is 192.168.0.254,  vrf L3VPN_1001,  remote AS 60001, external link
            External BGP neighbor configured for connected checks (single-hop no-disable-connected-check)
            BGP neighbor is 192.168.1.254,  vrf L3VPN_1002,  remote AS 60002, external link
            External BGP neighbor configured for connected checks (single-hop no-disable-connected-check)
        '''

        golden_output = '''\
            show ip bgp vpnv4 vrf L3VPN_1001 neighbors 192.168.0.254 advertised-routes
            Load for five secs: 100%/4%; one minute: 80%; five minutes: 75%
            Time source is NTP, 21:20:51.739 EST Wed Oct 16 2019

            BGP table version is 6173717, local router ID is 192.168.0.253
            Status codes: s suppressed, d damped, h history, * valid, > best, i - internal, 
                        r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter, 
                        x best-external, a additional-path, c RIB-compressed, 
                        t secondary path, L long-lived-stale,
            Origin codes: i - IGP, e - EGP, ? - incomplete
            RPKI validation codes: V valid, I invalid, N Not found

                Network          Next Hop            Metric LocPrf Weight Path
            Route Distinguisher: 65109:1001 (default for vrf L3VPN_1001) VRF Router ID 192.168.0.253
            *>i  10.1.0.0/24     10.19.198.238            0    100      0 65000 i
            *>i  10.1.1.0/24     10.19.198.238            0    100      0 65000 i
            *>i  10.1.2.0/24     10.19.198.238            0    100      0 65000 i
            *>i  10.1.3.0/24     10.19.198.238            0    100      0 65000 i
            *>i  10.1.4.0/24     10.19.198.238            0    100      0 65000 i

            Total number of prefixes 5
        '''

        golden_parsed_output = {
            'vrf': {
                'L3VPN_1001': {
                    'neighbor': {
                        '192.168.0.254': {
                            'address_family': {
                                'vpnv4': {
                                    'advertised': {
                                    },
                                    'bgp_table_version': 6173717,
                                    'local_router_id': '192.168.0.253',
                                },
                                'vpnv4 RD 65109:1001': {
                                    'bgp_table_version': 6173717,
                                    'local_router_id': '192.168.0.253',
                                    'route_distinguisher': '65109:1001',
                                    'default_vrf': 'L3VPN_1001',
                                    'advertised': {
                                        '10.1.0.0/24': {
                                            'index': {
                                                1: {
                                                    'status_codes': '*>',
                                                    'path_type': 'i',
                                                    'next_hop': '10.19.198.238',
                                                    'origin_codes': 'i',
                                                    'metric': 0,
                                                    'localprf': 100,
                                                    'weight': 0,
                                                    'path': '65000',
                                                },
                                            },
                                        },
                                        '10.1.1.0/24': {
                                            'index': {
                                                1: {
                                                    'status_codes': '*>',
                                                    'path_type': 'i',
                                                    'next_hop': '10.19.198.238',
                                                    'origin_codes': 'i',
                                                    'metric': 0,
                                                    'localprf': 100,
                                                    'weight': 0,
                                                    'path': '65000',
                                                },
                                            },
                                        },
                                        '10.1.2.0/24': {
                                            'index': {
                                                1: {
                                                    'status_codes': '*>',
                                                    'path_type': 'i',
                                                    'next_hop': '10.19.198.238',
                                                    'origin_codes': 'i',
                                                    'metric': 0,
                                                    'localprf': 100,
                                                    'weight': 0,
                                                    'path': '65000',
                                                },
                                            },
                                        },
                                        '10.1.3.0/24': {
                                            'index': {
                                                1: {
                                                    'status_codes': '*>',
                                                    'path_type': 'i',
                                                    'next_hop': '10.19.198.238',
                                                    'origin_codes': 'i',
                                                    'metric': 0,
                                                    'localprf': 100,
                                                    'weight': 0,
                                                    'path': '65000',
                                                },
                                            },
                                        },
                                        '10.1.4.0/24': {
                                            'index': {
                                                1: {
                                                    'status_codes': '*>',
                                                    'path_type': 'i',
                                                    'next_hop': '10.19.198.238',
                                                    'origin_codes': 'i',
                                                    'metric': 0,
                                                    'localprf': 100,
                                                    'weight': 0,
                                                    'path': '65000',
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }

        self.outputs = {}
        self.maxDiff = None 
        self.outputs['show ip bgp vpnv4 vrf L3VPN_1001 neighbors 192.168.0.254 advertised-routes'] = golden_output
        self.outputs['show bgp all neighbors | i BGP neighbor'] = raw1

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper

        obj = ShowIpBgpNeighborsAdvertisedRoutes(device=self.device)
        parsed_output = obj.parse(address_family='vpnv4', vrf='L3VPN_1001', neighbor='192.168.0.254')
        self.assertEqual(parsed_output, golden_parsed_output)


if __name__ == '__main__':
    unittest.main()