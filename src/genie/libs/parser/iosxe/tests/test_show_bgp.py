
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
from genie.libs.parser.iosxe.show_bgp import ShowBgpAll,\
                                             ShowIpBgpAll,\
                                             ShowBgp,\
                                             ShowIpBgp,\
                                             ShowBgpAllDetail,\
                                             ShowIpBgpAllDetail,\
                                             ShowBgpDetail,\
                                             ShowIpBgpDetail,\
                                             ShowBgpSummary,\
                                             ShowBgpAllSummary,\
                                             ShowIpBgpSummary,\
                                             ShowIpBgpAllSummary,\
                                             ShowBgpAllNeighbors,\
                                             ShowBgpNeighbors,\
                                             ShowIpBgpAllNeighbors,\
                                             ShowIpBgpNeighbors,\
                                             ShowBgpAllNeighborsAdvertisedRoutes,\
                                             ShowBgpNeighborsAdvertisedRoutes,\
                                             ShowIpBgpAllNeighborsAdvertisedRoutes,\
                                             ShowIpBgpNeighborsAdvertisedRoutes,\
                                             ShowBgpAllNeighborsReceivedRoutes,\
                                             ShowBgpNeighborsReceivedRoutes,\
                                             ShowIpBgpAllNeighborsReceivedRoutes,\
                                             ShowIpBgpNeighborsReceivedRoutes,\
                                             ShowBgpAllNeighborsRoutes,\
                                             ShowBgpNeighborsRoutes,\
                                             ShowIpBgpAllNeighborsRoutes,\
                                             ShowIpBgpNeighborsRoutes,\
                                             ShowBgpAllClusterIds,\
                                             ShowBgpAllNeighborsPolicy,\
                                             ShowIpBgpTemplatePeerSession,\
                                             ShowIpBgpTemplatePeerPolicy,\
                                             ShowIpBgpAllDampeningParameters, \
                                             ShowIpBgpRegexp


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
#   * 'show bgp all neighbors'
#   * 'show bgp {address_family} all neighbors {neighbor}'
# =========================================================
class TestShowBgpAllNeighbors(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'list_of_neighbors': ['10.16.2.2',
                             '10.36.3.3',
                             '10.4.6.6',
                             '10.66.6.6',
                             '10.64.4.4',
                             '10.100.5.5',
                             '2001:DB8:4:6::6',
                             '2001:DB8:20:4:6::6'],
        'vrf': 
            {'VRF1': 
                {'neighbor': 
                    {'10.4.6.6': 
                        {'address_family': 
                            {'vpnv4 unicast': 
                                {'current_time': '0x530A19',
                                'last_read': '00:00:33',
                                'last_write': '00:00:30',
                                'session_state': 'Established',
                                'up_time': '01:01:59'}},
                        'bgp_event_timer': 
                            {'next': 
                                {'ackhold': '0x0',
                                'deadwait': '0x0',
                                'giveup': '0x0',
                                'keepalive': '0x0',
                                'linger': '0x0',
                                'pmtuager': '0x0',
                                'processq': '0x0',
                                'retrans': '0x0',
                                'sendwnd': '0x0',
                                'timewait': '0x0'},
                            'starts': 
                                {'ackhold': 66,
                                'deadwait': 0,
                                'giveup': 0,
                                'keepalive': 0,
                                'linger': 0,
                                'pmtuager': 0,
                                'processq': 0,
                                'retrans': 71,
                                'sendwnd': 0,
                                'timewait': 0},
                            'wakeups': 
                                {'ackhold': 64,
                                'deadwait': 0,
                                'giveup': 0,
                                'keepalive': 0,
                                'linger': 0,
                                'pmtuager': 0,
                                'processq': 0,
                                'retrans': 0,
                                'sendwnd': 0,
                                'timewait': 0}},
                        'bgp_neighbor_session': {
                        'sessions': 1,
                        },
                        'bgp_negotiated_capabilities': 
                            {'enhanced_refresh': 'advertised',
                            'four_octets_asn': 'advertised',
                            'ipv4_unicast': 'advertised '
                                            'and '
                                            'received',
                            'route_refresh': 'advertised',
                            'stateful_switchover': 'NO '
                                                   'for '
                                                   'session '
                                                   '1'},
                        'bgp_negotiated_keepalive_timers': 
                            {'hold_time': 180,
                            'keepalive_interval': 60},
                        'bgp_neighbor_counters': 
                            {'messages': 
                                {'in_queue_depth': 0,
                                'out_queue_depth': 0,
                                'received': 
                                    {'keepalives': 64,
                                    'notifications': 0,
                                    'opens': 1,
                                    'route_refresh': 0,
                                    'total': 66,
                                    'updates': 1},
                                'sent': 
                                    {'keepalives': 69,
                                    'notifications': 0,
                                    'opens': 1,
                                    'route_refresh': 0,
                                    'total': 73,
                                    'updates': 3}}},
                        'bgp_session_transport': 
                            {'ack_hold': 200,
                            'address_tracking_status': 'enabled',
                            'connection': 
                                {'dropped': 1,
                                'established': 2,
                                'last_reset': '01:02:11',
                                'reset_reason': 'Peer '
                                             'closed '
                                             'the '
                                             'session '
                                             'of '
                                             'session '
                                             '1'},
                            'connection_state': 'estab',
                            'connection_tableid': 1,
                            'datagram': 
                                {'datagram_received': 
                                    {'out_of_order': 0,
                                    'total_data': 1330,
                                    'value': 137,
                                    'with_data': 66},
                                'datagram_sent': 
                                    {'fastretransmit': 0,
                                    'partialack': 0,
                                    'retransmit': 0,
                                    'second_congestion': 0,
                                    'total_data': 1537,
                                    'value': 138,
                                    'with_data': 72}},
                            'delrcvwnd': 1330,
                            'ecn_connection': 'disabled',
                            'enqueued_packets': 
                                {'input_packet': 0,
                                'mis_ordered_packet': 0,
                                'retransmit_packet': 0},
                            'fast_lock_acquisition_failures': 0,
                            'graceful_restart': 'disabled',
                            'io_status': 1,
                            'ip_precedence_value': 6,
                            'irs': 930048172,
                            'iss': 271842,
                            'krtt': 0,
                            'lock_slow_path': 0,
                            'max_rtt': 1000,
                            'maximum_output_segment_queue_size': 50,
                            'maxrcvwnd': 16384,
                            'min_rtt': 1,
                            'min_time_between_advertisement_runs': 0,
                            'minimum_incoming_ttl': 0,
                            'option_flags': 'VRF '
                                            'id '
                                            'set, '
                                            'nagle, '
                                            'path '
                                            'mtu '
                                            'capable',
                            'outgoing_ttl': 1,
                            'packet_fast_path': 0,
                            'packet_fast_processed': 0,
                            'packet_slow_path': 0,
                            'rcv_scale': 0,
                            'rcvnxt': 930049503,
                            'rcvwnd': 15054,
                            'receive_idletime': 30999,
                            'rib_route_ip': '10.4.6.6',
                            'rtto': 1003,
                            'rtv': 3,
                            'sent_idletime': 31107,
                            'snd_scale': 0,
                            'sndnxt': 273380,
                            'snduna': 273380,
                            'sndwnd': 32000,
                            'srtt': 1000,
                            'status_flags': 'passive '
                                            'open, '
                                            'gen '
                                            'tcbs',
                            'tcp_path_mtu_discovery': 'enabled',
                            'tcp_semaphore': '0x1286E62C',
                            'tcp_semaphore_status': 'FREE',
                            'transport': 
                                {'foreign_host': '10.4.6.6',
                                'foreign_port': '11010',
                                'local_host': '10.4.6.4',
                                'local_port': '179',
                                'mss': 1460},
                            'unread_input_bytes': 0,
                            'uptime': 3720132},
                        'bgp_version': 4,
                        'link': 'external',
                        'remote_as': 300,
                        'router_id': '10.4.6.6',
                        'session_state': 'Established',
                        'shutdown': True},
                    '2001:DB8:4:6::6': 
                        {'address_family': 
                            {'vpnv6 unicast': 
                                {'current_time': '0x5315CE',
                                'last_read': '00:00:32',
                                'last_write': '00:00:06',
                                'session_state': 'Established',
                                'up_time': '01:01:58'},
                            },
                        'bgp_event_timer': 
                            {'next': 
                                {'ackhold': '0x0',
                                'deadwait': '0x0',
                                'giveup': '0x0',
                                'keepalive': '0x0',
                                'linger': '0x0',
                                'pmtuager': '0x0',
                                'processq': '0x0',
                                'retrans': '0x0',
                                'sendwnd': '0x0',
                                'timewait': '0x0'},
                            'starts': 
                                {'ackhold': 66,
                                'deadwait': 0,
                                'giveup': 0,
                                'keepalive': 0,
                                'linger': 0,
                                'pmtuager': 0,
                                'processq': 0,
                                'retrans': 72,
                                'sendwnd': 0,
                                'timewait': 0},
                            'wakeups': 
                                {'ackhold': 64,
                                'deadwait': 0,
                                'giveup': 0,
                                'keepalive': 0,
                                'linger': 0,
                                'pmtuager': 0,
                                'processq': 0,
                                'retrans': 0,
                                'sendwnd': 0,
                                'timewait': 0}},
                                'bgp_neighbor_session': {
                            'sessions': 1,
                            },
                        'bgp_negotiated_capabilities': 
                            {'enhanced_refresh': 'advertised',
                            'four_octets_asn': 'advertised',
                            'ipv6_unicast': 'advertised '
                                            'and '
                                            'received',
                            'route_refresh': 'advertised',
                            'stateful_switchover': 'NO '
                                                   'for '
                                                   'session '
                                                   '1'},
                        'bgp_negotiated_keepalive_timers': 
                            {'hold_time': 180,
                            'keepalive_interval': 60},
                        'bgp_neighbor_counters': 
                            {'messages': 
                                {'in_queue_depth': 0,
                                'out_queue_depth': 0,
                                'received': 
                                    {'keepalives': 64,
                                    'notifications': 0,
                                    'opens': 1,
                                    'route_refresh': 0,
                                    'total': 66,
                                    'updates': 1},
                                'sent': 
                                    {'keepalives': 70,
                                    'notifications': 0,
                                    'opens': 1,
                                    'route_refresh': 0,
                                    'total': 74,
                                    'updates': 3}}},
                        'bgp_session_transport': 
                            {'ack_hold': 200,
                            'address_tracking_status': 'enabled',
                            'connection': 
                                {'dropped': 1,
                                'established': 2,
                                'last_reset': '01:05:12',
                                'reset_reason': 'Active '
                                                'open '
                                                'failed'},
                            'connection_state': 'estab',
                            'connection_tableid': 503316481,
                            'datagram': 
                                {'datagram_received': 
                                    {'out_of_order': 0,
                                    'total_data': 1380,
                                    'value': 138,
                                    'with_data': 66},
                                'datagram_sent': 
                                    {'fastretransmit': 0,
                                    'partialack': 0,
                                    'retransmit': 0,
                                    'second_congestion': 0,
                                    'total_data': 7246,
                                    'value': 139,
                                    'with_data': 139}},
                            'delrcvwnd': 1380,
                            'ecn_connection': 'disabled',
                            'enqueued_packets': 
                                {'input_packet': 0,
                                'mis_ordered_packet': 0,
                                'retransmit_packet': 0},
                            'fast_lock_acquisition_failures': 0,
                            'graceful_restart': 'disabled',
                            'io_status': 1,
                            'ip_precedence_value': 6,
                            'irs': 1797203329,
                            'iss': 164676617,
                            'krtt': 0,
                            'lock_slow_path': 0,
                            'max_rtt': 1000,
                            'maximum_output_segment_queue_size': 50,
                            'maxrcvwnd': 16384,
                            'min_rtt': 1,
                            'min_time_between_advertisement_runs': 0,
                            'minimum_incoming_ttl': 0,
                            'option_flags': 'VRF '
                                            'id '
                                            'set, '
                                            'nagle, '
                                            'path '
                                            'mtu '
                                            'capable',
                            'outgoing_ttl': 1,
                            'packet_fast_path': 0,
                            'packet_fast_processed': 0,
                            'packet_slow_path': 0,
                            'rcv_scale': 0,
                            'rcvnxt': 1797204710,
                            'rcvwnd': 15004,
                            'receive_idletime': 6849,
                            'rib_route_ip': '2001:DB8:4:6::6',
                            'rtto': 1003,
                            'rtv': 3,
                            'sent_idletime': 6954,
                            'snd_scale': 0,
                            'sndnxt': 164678296,
                            'snduna': 164678296,
                            'sndwnd': 32000,
                            'srtt': 1000,
                            'status_flags': 'passive '
                                            'open, '
                                            'gen '
                                            'tcbs',
                            'tcp_path_mtu_discovery': 'enabled',
                            'tcp_semaphore': '0x1286E9AC',
                            'tcp_semaphore_status': 'FREE',
                            'transport': 
                                {'foreign_host': '2001:DB8:4:6::6',
                                'foreign_port': '11003',
                                'local_host': '2001:DB8:4:6::4',
                                'local_port': '179',
                                'mss': 1440},
                            'unread_input_bytes': 0,
                            'uptime': 3718683},
                        'bgp_version': 4,
                        'link': 'external',
                        'remote_as': 300,
                        'router_id': '10.4.6.6',
                        'session_state': 'Established',
                        'shutdown': False}}},
            'VRF2': 
                {'neighbor': 
                    {'10.66.6.6': 
                        {'address_family': 
                            {'vpnv6 unicast': {},
                            'vpnv4 unicast': 
                                {'current_time': '0x530C0D',
                                'last_read': '00:00:24',
                                'last_write': '00:00:21',
                                'session_state': 'Established',
                                'up_time': '01:01:51'}},
                        'bgp_event_timer': 
                            {'next': 
                                {'ackhold': '0x0',
                                'deadwait': '0x0',
                                'giveup': '0x0',
                                'keepalive': '0x0',
                                'linger': '0x0',
                                'pmtuager': '0x0',
                                'processq': '0x0',
                                'retrans': '0x0',
                                'sendwnd': '0x0',
                                'timewait': '0x0'},
                            'starts': 
                                {'ackhold': 66,
                                'deadwait': 0,
                                'giveup': 0,
                                'keepalive': 0,
                                'linger': 0,
                                'pmtuager': 0,
                                'processq': 0,
                                'retrans': 70,
                                'sendwnd': 0,
                                'timewait': 0},
                            'wakeups': 
                                {'ackhold': 64,
                                'deadwait': 0,
                                'giveup': 0,
                                'keepalive': 0,
                                'linger': 0,
                                'pmtuager': 0,
                                'processq': 0,
                                'retrans': 0,
                                'sendwnd': 0,
                                'timewait': 0}},
                                'bgp_neighbor_session': {
                            'sessions': 1,
                            },
                        'bgp_negotiated_capabilities': 
                            {'enhanced_refresh': 'advertised',
                            'four_octets_asn': 'advertised',
                            'ipv4_unicast': 'advertised '
                                            'and '
                                            'received',
                            'route_refresh': 'advertised',
                            'stateful_switchover': 'NO '
                                                   'for '
                                                   'session '
                                                   '1'},
                        'bgp_negotiated_keepalive_timers': 
                            {'hold_time': 180,
                            'keepalive_interval': 60},
                        'bgp_neighbor_counters': 
                            {'messages': 
                                {'in_queue_depth': 0,
                                'out_queue_depth': 0,
                                'received': 
                                    {'keepalives': 64,
                                    'notifications': 0,
                                    'opens': 1,
                                    'route_refresh': 0,
                                    'total': 66,
                                    'updates': 1},
                                'sent': 
                                    {'keepalives': 69,
                                    'notifications': 0,
                                    'opens': 1,
                                    'route_refresh': 0,
                                    'total': 71,
                                    'updates': 1}}},
                        'bgp_session_transport': 
                            {'ack_hold': 200,
                            'address_tracking_status': 'enabled',
                            'connection': 
                                {'dropped': 1,
                                'established': 2,
                                'last_reset': '01:05:09',
                                'reset_reason': 'Active '
                                                'open '
                                                'failed'},
                            'connection_state': 'estab',
                            'connection_tableid': 2,
                            'datagram': 
                                {'datagram_received': 
                                    {'out_of_order': 0,
                                    'total_data': 1330,
                                    'value': 135,
                                    'with_data': 66},
                                'datagram_sent': 
                                    {'fastretransmit': 0,
                                    'partialack': 0,
                                    'retransmit': 0,
                                    'second_congestion': 0,
                                    'total_data': 1391,
                                    'value': 137,
                                    'with_data': 71}},
                            'delrcvwnd': 1330,
                            'ecn_connection': 'disabled',
                            'enqueued_packets': 
                                {'input_packet': 0,
                                'mis_ordered_packet': 0,
                                'retransmit_packet': 0},
                            'fast_lock_acquisition_failures': 0,
                            'graceful_restart': 'disabled',
                            'io_status': 1,
                            'ip_precedence_value': 6,
                            'irs': 213294715,
                            'iss': 2048397580,
                            'krtt': 0,
                            'lock_slow_path': 0,
                            'max_rtt': 1000,
                            'maximum_output_segment_queue_size': 50,
                            'maxrcvwnd': 16384,
                            'min_rtt': 2,
                            'min_time_between_advertisement_runs': 0,
                            'minimum_incoming_ttl': 0,
                            'option_flags': 'VRF '
                                            'id '
                                            'set, '
                                            'nagle, '
                                            'path '
                                            'mtu '
                                            'capable',
                            'outgoing_ttl': 1,
                            'packet_fast_path': 0,
                            'packet_fast_processed': 0,
                            'packet_slow_path': 0,
                            'rcv_scale': 0,
                            'rcvnxt': 213296046,
                            'rcvwnd': 15054,
                            'receive_idletime': 21765,
                            'rib_route_ip': '10.66.6.6',
                            'rtto': 1003,
                            'rtv': 3,
                            'sent_idletime': 21866,
                            'snd_scale': 0,
                            'sndnxt': 2048398972,
                            'snduna': 2048398972,
                            'sndwnd': 32000,
                            'srtt': 1000,
                            'status_flags': 'passive '
                                            'open, '
                                            'gen '
                                            'tcbs',
                            'tcp_path_mtu_discovery': 'enabled',
                            'tcp_semaphore': '0x1286E8CC',
                            'tcp_semaphore_status': 'FREE',
                            'transport': 
                                {'foreign_host': '10.66.6.6',
                                'foreign_port': '11003',
                                'local_host': '10.66.6.4',
                                'local_port': '179',
                                'mss': 1460},
                            'unread_input_bytes': 0,
                            'uptime': 3712326},
                        'bgp_version': 4,
                        'link': 'external',
                        'remote_as': 400,
                        'router_id': '10.66.6.6',
                        'session_state': 'Established',
                        'shutdown': False},
                    '2001:DB8:20:4:6::6': 
                        {'address_family': 
                            {'ipv4 multicast': {},
                            'l2vpn evpn': {},
                            'mvpnv4 unicast': {},
                            'mvpnv6 unicast': {},
                            'vpnv4 multicast': {},
                            'vpnv6 multicast': {},
                            'vpnv6 unicast': 
                                {'current_time': '0x5319B5',
                                'last_read': '00:00:22',
                                'last_write': '00:00:01',
                                'session_state': 'Established',
                                'up_time': '01:01:51'}},
                                'bgp_event_timer': 
                                    {'next': 
                                        {'ackhold': '0x0',
                                        'deadwait': '0x0',
                                        'giveup': '0x0',
                                        'keepalive': '0x0',
                                        'linger': '0x0',
                                        'pmtuager': '0x0',
                                        'processq': '0x0',
                                        'retrans': '0x0',
                                        'sendwnd': '0x0',
                                        'timewait': '0x0'},
                                    'starts': 
                                        {'ackhold': 66,
                                        'deadwait': 0,
                                        'giveup': 0,
                                        'keepalive': 0,
                                        'linger': 0,
                                        'pmtuager': 0,
                                        'processq': 0,
                                        'retrans': 71,
                                        'sendwnd': 0,
                                        'timewait': 0},
                                    'wakeups': 
                                        {'ackhold': 64,
                                        'deadwait': 0,
                                        'giveup': 0,
                                        'keepalive': 0,
                                        'linger': 0,
                                        'pmtuager': 0,
                                        'processq': 0,
                                        'retrans': 0,
                                        'sendwnd': 0,
                                        'timewait': 0}},
                                        'bgp_neighbor_session': {
                                    'sessions': 1,
                                    },
                                'bgp_negotiated_capabilities': 
                                    {'enhanced_refresh': 'advertised',
                                    'four_octets_asn': 'advertised',
                                    'ipv6_unicast': 'advertised '
                                                    'and '
                                                    'received',
                                    'route_refresh': 'advertised',
                                    'stateful_switchover': 'NO '
                                                            'for '
                                                            'session '
                                                            '1'},
                                'bgp_negotiated_keepalive_timers': 
                                    {'hold_time': 180,
                                    'keepalive_interval': 60},
                                'bgp_neighbor_counters': 
                                    {'messages': 
                                        {'in_queue_depth': 0,
                                        'out_queue_depth': 0,
                                        'received': 
                                            {'keepalives': 64,
                                            'notifications': 0,
                                            'opens': 1,
                                            'route_refresh': 0,
                                            'total': 66,
                                            'updates': 1},
                                        'sent': 
                                            {'keepalives': 70,
                                            'notifications': 0,
                                            'opens': 1,
                                            'route_refresh': 0,
                                            'total': 72,
                                            'updates': 1}}},
                                'bgp_session_transport': 
                                    {'ack_hold': 200,
                                    'address_tracking_status': 'enabled',
                                    'connection': 
                                        {'dropped': 1,
                                        'established': 2,
                                        'last_reset': '01:05:13',
                                        'reset_reason': 'Active '
                                                        'open '
                                                        'failed'},
                                    'connection_state': 'estab',
                                    'connection_tableid': 503316482,
                                    'datagram': 
                                        {'datagram_received': 
                                            {'out_of_order': 0,
                                            'total_data': 1380,
                                            'value': 137,
                                            'with_data': 66},
                                        'datagram_sent': 
                                            {'fastretransmit': 0,
                                            'partialack': 0,
                                            'retransmit': 0,
                                            'second_congestion': 0,
                                            'total_data': 6944,
                                            'value': 138,
                                            'with_data': 138}},
                                    'delrcvwnd': 1380,
                                    'ecn_connection': 'disabled',
                                    'enqueued_packets': 
                                        {'input_packet': 0,
                                        'mis_ordered_packet': 0,
                                        'retransmit_packet': 0},
                                    'fast_lock_acquisition_failures': 0,
                                    'graceful_restart': 'disabled',
                                    'io_status': 1,
                                    'ip_precedence_value': 6,
                                    'irs': 693674496,
                                    'iss': 3178074389,
                                    'krtt': 0,
                                    'lock_slow_path': 0,
                                    'max_rtt': 1000,
                                    'maximum_output_segment_queue_size': 50,
                                    'maxrcvwnd': 16384,
                                    'min_rtt': 3,
                                    'min_time_between_advertisement_runs': 0,
                                    'minimum_incoming_ttl': 0,
                                    'option_flags': 'VRF '
                                                    'id '
                                                    'set, '
                                                    'nagle, '
                                                    'path '
                                                    'mtu '
                                                    'capable',
                                    'outgoing_ttl': 1,
                                    'packet_fast_path': 0,
                                    'packet_fast_processed': 0,
                                    'packet_slow_path': 0,
                                    'rcv_scale': 0,
                                    'rcvnxt': 693675877,
                                    'rcvwnd': 15004,
                                    'receive_idletime': 2277,
                                    'rib_route_ip': '2001:DB8:20:4:6::6',
                                    'rtto': 1003,
                                    'rtv': 3,
                                    'sent_idletime': 2335,
                                    'snd_scale': 0,
                                    'sndnxt': 3178075806,
                                    'snduna': 3178075806,
                                    'sndwnd': 32000,
                                    'srtt': 1000,
                                    'status_flags': 'passive '
                                                    'open, '
                                                    'gen '
                                                    'tcbs',
                                    'tcp_path_mtu_discovery': 'enabled',
                                    'tcp_semaphore': '0x1286E93C',
                                    'tcp_semaphore_status': 'FREE',
                                    'transport': 
                                        {'foreign_host': '2001:DB8:20:4:6::6',
                                        'foreign_port': '11003',
                                        'local_host': '2001:DB8:20:4:6::4',
                                        'local_port': '179',
                                        'mss': 1440},
                                    'unread_input_bytes': 0,
                                    'uptime': 3711535},
                                'bgp_version': 4,
                                'link': 'external',
                                'remote_as': 400,
                                'router_id': '10.66.6.6',
                                'session_state': 'Established',
                                'shutdown': False}}},
         'default': 
            {'neighbor': 
                {'10.16.2.2': 
                    {'address_family': 
                        {'vpnv4 unicast': 
                            {'current_time': '0x530449',
                            'last_read': '00:00:04',
                            'last_write': '00:00:09',
                            'session_state': 'Established',
                            'up_time': '01:10:35'}},
                    'bgp_event_timer': 
                        {'next': 
                            {'ackhold': '0x0',
                            'deadwait': '0x0',
                            'giveup': '0x0',
                            'keepalive': '0x0',
                            'linger': '0x0',
                            'pmtuager': '0x0',
                            'processq': '0x0',
                            'retrans': '0x0',
                            'sendwnd': '0x0',
                            'timewait': '0x0'},
                        'starts': 
                            {'ackhold': 80,
                            'deadwait': 0,
                            'giveup': 0,
                            'keepalive': 0,
                            'linger': 0,
                            'pmtuager': 1,
                            'processq': 0,
                            'retrans': 86,
                            'sendwnd': 0,
                            'timewait': 0},
                        'wakeups': 
                            {'ackhold': 72,
                            'deadwait': 0,
                            'giveup': 0,
                            'keepalive': 0,
                            'linger': 0,
                            'pmtuager': 1,
                            'processq': 0,
                            'retrans': 0,
                            'sendwnd': 0,
                            'timewait': 0}},
                            'bgp_neighbor_session': {
                            'sessions': 1,
                            },
                    'bgp_negotiated_capabilities': 
                        {'enhanced_refresh': 'advertised',
                        'four_octets_asn': 'advertised '
                                           'and '
                                           'received',
                        'graceful_restart': 'received',
                        'graceful_restart_af_advertised_by_peer': ['vpnv4 '
                                                                   'unicast',
                                                                   'vpnv6 '
                                                                   'unicast'],
                        'remote_restart_timer': 120,
                        'route_refresh': 'advertised '
                                         'and '
                                         'received(new)',
                        'stateful_switchover': 'NO '
                                               'for '
                                               'session '
                                               '1',
                        'vpnv4_unicast': 'advertised '
                                         'and '
                                         'received',
                        'vpnv6_unicast': 'advertised '
                                         'and '
                                         'received'},
                    'bgp_negotiated_keepalive_timers': 
                        {'hold_time': 180,
                        'keepalive_interval': 60},
                    'bgp_neighbor_counters': 
                        {'messages': 
                            {'in_queue_depth': 0,
                            'out_queue_depth': 0,
                            'received': 
                                {'keepalives': 74,
                                'notifications': 0,
                                'opens': 1,
                                'route_refresh': 0,
                                'total': 81,
                                'updates': 6},
                            'sent': 
                                {'keepalives': 75,
                                'notifications': 0,
                                'opens': 1,
                                'route_refresh': 0,
                                'total': 87,
                                'updates': 11}}},
                    'bgp_session_transport': 
                        {'ack_hold': 200,
                        'address_tracking_status': 'enabled',
                        'connection': 
                            {'dropped': 0,
                            'established': 1,
                            'last_reset': 'never'},
                        'connection_state': 'estab',
                        'connection_tableid': 0,
                        'datagram': 
                            {'datagram_received': 
                                {'out_of_order': 0,
                                'total_data': 2374,
                                'value': 164,
                                'with_data': 80},
                            'datagram_sent': 
                                {'fastretransmit': 0,
                                'partialack': 0,
                                'retransmit': 0,
                                'second_congestion': 0,
                                'total_data': 3303,
                                'value': 166,
                                'with_data': 87}},
                        'delrcvwnd': 57,
                        'ecn_connection': 'disabled',
                        'enqueued_packets': 
                            {'input_packet': 0,
                            'mis_ordered_packet': 0,
                            'retransmit_packet': 0},
                        'fast_lock_acquisition_failures': 0,
                        'graceful_restart': 'disabled',
                        'io_status': 1,
                        'ip_precedence_value': 6,
                        'irs': 109992783,
                        'iss': 55023811,
                        'krtt': 0,
                        'lock_slow_path': 0,
                        'max_rtt': 1000,
                        'maximum_output_segment_queue_size': 50,
                        'maxrcvwnd': 16384,
                        'min_rtt': 4,
                        'min_time_between_advertisement_runs': 0,
                        'minimum_incoming_ttl': 0,
                        'option_flags': 'nagle, '
                                        'path '
                                        'mtu '
                                        'capable',
                        'outgoing_ttl': 255,
                        'packet_fast_path': 0,
                        'packet_fast_processed': 0,
                        'packet_slow_path': 0,
                        'rcv_scale': 0,
                        'rcvnxt': 109995158,
                        'rcvwnd': 16327,
                        'receive_idletime': 4549,
                        'rib_route_ip': '10.16.2.2',
                        'rtto': 1003,
                        'rtv': 3,
                        'sent_idletime': 4349,
                        'snd_scale': 0,
                        'sndnxt': 55027115,
                        'snduna': 55027115,
                        'sndwnd': 16616,
                        'srtt': 1000,
                        'status_flags': 'active '
                                        'open',
                        'tcp_path_mtu_discovery': 'enabled',
                        'tcp_semaphore': '0x1286E7EC',
                        'tcp_semaphore_status': 'FREE',
                        'transport': {'foreign_host': '10.16.2.2',
                                      'foreign_port': '179',
                                      'local_host': '10.64.4.4',
                                      'local_port': '35281',
                                      'mss': 536},
                        'unread_input_bytes': 0,
                        'uptime': 4236258},
                    'bgp_version': 4,
                    'link': 'internal',
                    'remote_as': 100,
                    'router_id': '10.16.2.2',
                    'session_state': 'Established',
                    'shutdown': False},
                '10.64.4.4': 
                    {'address_family': 
                        {'vpnv6 unicast': 
                            {'current_time': '0x530FF5',
                            'last_read': '00:00:07',
                            'last_write': '00:00:12',
                            'session_state': 'Established',
                            'up_time': '01:10:38'}},
                    'bgp_event_timer': 
                        {'next': 
                            {'ackhold': '0x0',
                            'deadwait': '0x0',
                            'giveup': '0x0',
                            'keepalive': '0x0',
                            'linger': '0x0',
                            'pmtuager': '0x0',
                            'processq': '0x0',
                            'retrans': '0x0',
                            'sendwnd': '0x0',
                            'timewait': '0x0'},
                        'starts': 
                            {'ackhold': 80,
                            'deadwait': 0,
                            'giveup': 0,
                            'keepalive': 0,
                            'linger': 0,
                            'pmtuager': 1,
                            'processq': 0,
                            'retrans': 86,
                            'sendwnd': 0,
                            'timewait': 0},
                        'wakeups': 
                            {'ackhold': 72,
                            'deadwait': 0,
                            'giveup': 0,
                            'keepalive': 0,
                            'linger': 0,
                            'pmtuager': 1,
                            'processq': 0,
                            'retrans': 0,
                            'sendwnd': 0,
                            'timewait': 0}},
                            'bgp_neighbor_session': {
                            'sessions': 1,
                            },
                    'bgp_negotiated_capabilities': 
                        {'enhanced_refresh': 'advertised',
                        'four_octets_asn': 'advertised '
                                            'and '
                                            'received',
                        'graceful_restart': 'received',
                        'graceful_restart_af_advertised_by_peer': ['vpnv4 '
                                                                  'unicast',
                                                                  'vpnv6 '
                                                                  'unicast'],
                        'remote_restart_timer': 120,
                        'route_refresh': 'advertised '
                                         'and '
                                         'received(new)',
                        'stateful_switchover': 'NO '
                                               'for '
                                               'session '
                                               '1',
                        'vpnv4_unicast': 'advertised '
                                         'and '
                                         'received',
                        'vpnv6_unicast': 'advertised '
                                         'and '
                                         'received'},
                    'bgp_negotiated_keepalive_timers': 
                        {'hold_time': 180,
                        'keepalive_interval': 60},
                    'bgp_neighbor_counters': 
                        {'messages': 
                            {'in_queue_depth': 0,
                            'out_queue_depth': 0,
                            'received': 
                                {'keepalives': 74,
                                'notifications': 0,
                                'opens': 1,
                                'route_refresh': 0,
                                'total': 81,
                                'updates': 6},
                            'sent': 
                                {'keepalives': 75,
                                'notifications': 0,
                                'opens': 1,
                                'route_refresh': 0,
                                'total': 87,
                                'updates': 11}}},
                    'bgp_session_transport': 
                        {'ack_hold': 200,
                        'address_tracking_status': 'enabled',
                        'connection': 
                            {'dropped': 0,
                            'established': 1,
                            'last_reset': 'never'},
                        'connection_state': 'estab',
                        'connection_tableid': 0,
                        'datagram': 
                            {'datagram_received': 
                                {'out_of_order': 0,
                                'total_data': 2374,
                                'value': 164,
                                'with_data': 80},
                            'datagram_sent': 
                                {'fastretransmit': 0,
                                'partialack': 0,
                                'retransmit': 0,
                                'second_congestion': 0,
                                'total_data': 3303,
                                'value': 166,
                                'with_data': 87}},
                        'delrcvwnd': 57,
                        'ecn_connection': 'disabled',
                        'enqueued_packets': 
                            {'input_packet': 0,
                            'mis_ordered_packet': 0,
                            'retransmit_packet': 0},
                        'fast_lock_acquisition_failures': 0,
                        'graceful_restart': 'disabled',
                        'io_status': 1,
                        'ip_precedence_value': 6,
                        'irs': 109992783,
                        'iss': 55023811,
                        'krtt': 0,
                        'lock_slow_path': 0,
                        'max_rtt': 1000,
                        'maximum_output_segment_queue_size': 50,
                        'maxrcvwnd': 16384,
                        'min_rtt': 4,
                        'min_time_between_advertisement_runs': 0,
                        'minimum_incoming_ttl': 0,
                        'option_flags': 'nagle, '
                                        'path '
                                        'mtu '
                                        'capable',
                        'outgoing_ttl': 255,
                        'packet_fast_path': 0,
                        'packet_fast_processed': 0,
                        'packet_slow_path': 0,
                        'rcv_scale': 0,
                        'rcvnxt': 109995158,
                        'rcvwnd': 16327,
                        'receive_idletime': 8032,
                        'rib_route_ip': '10.16.2.2',
                        'rtto': 1003,
                        'rtv': 3,
                        'sent_idletime': 7832,
                        'snd_scale': 0,
                        'sndnxt': 55027115,
                        'snduna': 55027115,
                        'sndwnd': 16616,
                        'srtt': 1000,
                        'status_flags': 'active '
                                        'open',
                        'tcp_path_mtu_discovery': 'enabled',
                        'tcp_semaphore': '0x1286E7EC',
                        'tcp_semaphore_status': 'FREE',
                        'transport': 
                            {'foreign_host': '10.16.2.2',
                            'foreign_port': '179',
                            'local_host': '10.64.4.4',
                            'local_port': '35281',
                            'mss': 536},
                        'unread_input_bytes': 0,
                        'uptime': 4239741},
                    'bgp_version': 4,
                    'description': 'router2222222',
                    'link': 'internal',
                    'remote_as': 100,
                    'router_id': '10.64.4.4',
                    'session_state': 'Established',
                    'shutdown': False},
                '10.100.5.5': 
                    {'address_family': 
                        {'vpnv6 unicast': 
                            {'current_time': '0x5313D8',
                            'last_read': '00:00:08',
                            'last_write': '00:00:47',
                            'session_state': 'Established',
                            'up_time': '01:10:44'}},
                    'bgp_event_timer': 
                        {'next': 
                            {'ackhold': '0x0',
                            'deadwait': '0x0',
                            'giveup': '0x0',
                            'keepalive': '0x0',
                            'linger': '0x0',
                            'pmtuager': '0x0',
                            'processq': '0x0',
                            'retrans': '0x0',
                            'sendwnd': '0x0',
                            'timewait': '0x0'},
                        'starts': 
                            {'ackhold': 80,
                            'deadwait': 0,
                            'giveup': 0,
                            'keepalive': 0,
                            'linger': 0,
                            'pmtuager': 1,
                            'processq': 0,
                            'retrans': 86,
                            'sendwnd': 0,
                            'timewait': 0},
                        'wakeups': 
                            {'ackhold': 73,
                            'deadwait': 0,
                            'giveup': 0,
                            'keepalive': 0,
                            'linger': 0,
                            'pmtuager': 1,
                            'processq': 0,
                            'retrans': 0,
                            'sendwnd': 0,
                            'timewait': 0}},
                            'bgp_neighbor_session': {
                            'sessions': 1,
                            },
                    'bgp_negotiated_capabilities': 
                        {'enhanced_refresh': 'advertised',
                        'four_octets_asn': 'advertised '
                                           'and '
                                           'received',
                        'graceful_restart': 'received',
                        'graceful_restart_af_advertised_by_peer': ['vpnv4 '
                                                                  'unicast',
                                                                  'vpnv6 '
                                                                  'unicast'],
                        'remote_restart_timer': 120,
                        'route_refresh': 'advertised '
                                         'and '
                                         'received(new)',
                        'stateful_switchover': 'NO '
                                               'for '
                                               'session '
                                               '1',
                        'vpnv4_unicast': 'advertised '
                                         'and '
                                         'received',
                        'vpnv6_unicast': 'advertised '
                                         'and '
                                         'received'},
                    'bgp_negotiated_keepalive_timers': 
                        {'hold_time': 180,
                        'keepalive_interval': 60},
                    'bgp_neighbor_counters': 
                        {'messages': 
                            {'in_queue_depth': 0,
                            'out_queue_depth': 0,
                            'received': 
                                {'keepalives': 74,
                                'notifications': 0,
                                'opens': 1,
                                'route_refresh': 0,
                                'total': 81,
                                'updates': 6},
                            'sent': 
                                {'keepalives': 75,
                                'notifications': 0,
                                'opens': 1,
                                'route_refresh': 0,
                                'total': 87,
                                'updates': 11}}},
                    'bgp_session_transport': 
                        {'ack_hold': 200,
                        'address_tracking_status': 'enabled',
                        'connection': 
                            {'dropped': 0,
                            'established': 1,
                            'last_reset': 'never'},
                        'connection_state': 'estab',
                        'connection_tableid': 0,
                        'datagram': 
                            {'datagram_received': 
                                {'out_of_order': 0,
                                'total_data': 2374,
                                'value': 165,
                                'with_data': 80},
                            'datagram_sent': 
                                {'fastretransmit': 0,
                                'partialack': 0,
                                'retransmit': 0,
                                'second_congestion': 0,
                                'total_data': 3303,
                                'value': 167,
                                'with_data': 87}},
                        'delrcvwnd': 57,
                        'ecn_connection': 'disabled',
                        'enqueued_packets': 
                            {'input_packet': 0,
                            'mis_ordered_packet': 0,
                            'retransmit_packet': 0},
                        'fast_lock_acquisition_failures': 0,
                        'graceful_restart': 'disabled',
                        'io_status': 1,
                        'ip_precedence_value': 6,
                        'irs': 4033842748,
                        'iss': 2116369173,
                        'krtt': 0,
                        'lock_slow_path': 0,
                        'max_rtt': 1000,
                        'maximum_output_segment_queue_size': 50,
                        'maxrcvwnd': 16384,
                        'min_rtt': 3,
                        'min_time_between_advertisement_runs': 0,
                        'minimum_incoming_ttl': 0,
                        'option_flags': 'nagle, '
                                        'path '
                                        'mtu '
                                        'capable',
                        'outgoing_ttl': 255,
                        'packet_fast_path': 0,
                        'packet_fast_processed': 0,
                        'packet_slow_path': 0,
                        'rcv_scale': 0,
                        'rcvnxt': 4033845123,
                        'rcvwnd': 16327,
                        'receive_idletime': 8567,
                        'rib_route_ip': '10.36.3.3',
                        'rtto': 1003,
                        'rtv': 3,
                        'sent_idletime': 8367,
                        'snd_scale': 0,
                        'sndnxt': 2116372477,
                        'snduna': 2116372477,
                        'sndwnd': 16616,
                        'srtt': 1000,
                        'status_flags': 'active '
                                        'open',
                        'tcp_path_mtu_discovery': 'enabled',
                        'tcp_semaphore': '0x1286E85C',
                        'tcp_semaphore_status': 'FREE',
                        'transport': 
                            {'foreign_host': '10.36.3.3',
                            'foreign_port': '179',
                            'local_host': '10.64.4.4',
                            'local_port': '56031',
                            'mss': 536},
                        'unread_input_bytes': 0,
                        'uptime': 4246385},
                   'bgp_version': 4,
                   'link': 'internal',
                   'remote_as': 100,
                   'router_id': '10.100.5.5',
                   'session_state': 'Established',
                   'shutdown': False},
                '10.36.3.3': 
                    {'address_family': 
                        {'vpnv4 unicast': 
                            {'current_time': '0x530638',
                            'last_read': '00:00:04',
                            'last_write': '00:00:43',
                            'session_state': 'Established',
                            'up_time': '01:10:41'}},
                    'bgp_event_timer': 
                        {'next': 
                            {'ackhold': '0x0',
                            'deadwait': '0x0',
                            'giveup': '0x0',
                            'keepalive': '0x0',
                            'linger': '0x0',
                            'pmtuager': '0x0',
                            'processq': '0x0',
                            'retrans': '0x0',
                            'sendwnd': '0x0',
                            'timewait': '0x0'},
                        'starts': 
                            {'ackhold': 80,
                            'deadwait': 0,
                            'giveup': 0,
                            'keepalive': 0,
                            'linger': 0,
                            'pmtuager': 1,
                            'processq': 0,
                            'retrans': 86,
                            'sendwnd': 0,
                            'timewait': 0},
                        'wakeups': 
                            {'ackhold': 73,
                            'deadwait': 0,
                            'giveup': 0,
                            'keepalive': 0,
                            'linger': 0,
                            'pmtuager': 1,
                            'processq': 0,
                            'retrans': 0,
                            'sendwnd': 0,
                            'timewait': 0}},
                            'bgp_neighbor_session': {
                            'sessions': 1,
                            },
                    'bgp_negotiated_capabilities': 
                        {'enhanced_refresh': 'advertised',
                        'four_octets_asn': 'advertised '
                                         'and '
                                         'received',
                        'graceful_restart': 'received',
                        'graceful_restart_af_advertised_by_peer': ['vpnv4 '
                                                                   'unicast',
                                                                   'vpnv6 '
                                                                   'unicast'],
                        'remote_restart_timer': 120,
                        'route_refresh': 'advertised '
                                         'and '
                                         'received(new)',
                        'stateful_switchover': 'NO '
                                               'for '
                                               'session '
                                               '1',
                        'vpnv4_unicast': 'advertised '
                                         'and ' 
                                         'received',
                        'vpnv6_unicast': 'advertised '
                                         'and '
                                         'received'},
                    'bgp_negotiated_keepalive_timers': 
                        {'hold_time': 180,
                        'keepalive_interval': 60},
                    'bgp_neighbor_counters': 
                        {'messages': 
                            {'in_queue_depth': 0,
                            'out_queue_depth': 0,
                            'received': 
                                {'keepalives': 74,
                                'notifications': 0,
                                'opens': 1,
                                'route_refresh': 0,
                                'total': 81,
                                'updates': 6},
                            'sent': 
                                {'keepalives': 75,
                                'notifications': 0,
                                'opens': 1,
                                'route_refresh': 0,
                                'total': 87,
                                'updates': 11}}},
                    'bgp_session_transport': 
                        {'ack_hold': 200,
                        'address_tracking_status': 'enabled',
                        'connection': 
                            {'dropped': 0,
                            'established': 1,
                            'last_reset': 'never'},
                        'connection_state': 'estab',
                        'connection_tableid': 0,
                        'datagram': 
                            {'datagram_received': 
                                {'out_of_order': 0,
                                'total_data': 2374,
                                'value': 165,
                                'with_data': 80},
                            'datagram_sent': 
                                {'fastretransmit': 0,
                                'partialack': 0,
                                'retransmit': 0,
                                'second_congestion': 0,
                                'total_data': 3303,
                                'value': 167,
                                'with_data': 87}},
                        'delrcvwnd': 57,
                        'ecn_connection': 'disabled',
                        'enqueued_packets': 
                            {'input_packet': 0,
                            'mis_ordered_packet': 0,
                            'retransmit_packet': 0},
                        'fast_lock_acquisition_failures': 0,
                        'graceful_restart': 'disabled',
                        'io_status': 1,
                        'ip_precedence_value': 6,
                        'irs': 4033842748,
                        'iss': 2116369173,
                        'krtt': 0,
                        'lock_slow_path': 0,
                        'max_rtt': 1000,
                        'maximum_output_segment_queue_size': 50,
                        'maxrcvwnd': 16384,
                        'min_rtt': 3,
                        'min_time_between_advertisement_runs': 0,
                        'minimum_incoming_ttl': 0,
                        'option_flags': 'nagle, '
                                        'path '
                                        'mtu '
                                        'capable',
                        'outgoing_ttl': 255,
                        'packet_fast_path': 0,
                        'packet_fast_processed': 0,
                        'packet_slow_path': 0,
                        'rcv_scale': 0,
                        'rcvnxt': 4033845123,
                        'rcvwnd': 16327,
                        'receive_idletime': 5575,
                        'rib_route_ip': '10.36.3.3',
                        'rtto': 1003,
                        'rtv': 3,
                        'sent_idletime': 5375,
                        'snd_scale': 0,
                        'sndnxt': 2116372477,
                        'snduna': 2116372477,
                        'sndwnd': 16616,
                        'srtt': 1000,
                        'status_flags': 'active '
                                        'open',
                        'tcp_path_mtu_discovery': 'enabled',
                        'tcp_semaphore': '0x1286E85C',
                        'tcp_semaphore_status': 'FREE',
                        'transport': 
                            {'foreign_host': '10.36.3.3',
                            'foreign_port': '179',
                            'local_host': '10.64.4.4',
                            'local_port': '56031',
                            'mss': 536},
                        'unread_input_bytes': 0,
                        'uptime': 4243393},
                    'bgp_version': 4,
                    'link': 'internal',
                    'remote_as': 100,
                    'router_id': '10.36.3.3',
                    'session_state': 'Established',
                    'shutdown': False}}}}}

    golden_output1 = {'execute.return_value': '''
        router# show bgp all neighbors

        For address family: IPv4 Unicast

        For address family: IPv6 Unicast

        For address family: VPNv4 Unicast
        BGP neighbor is 10.16.2.2,  remote AS 100, internal link
          BGP version 4, remote router ID 10.16.2.2
          BGP state = Established, up for 01:10:35
          Last read 00:00:04, last write 00:00:09, hold time is 180, keepalive interval is 60 seconds
          Neighbor sessions:
            1 active, is not multisession capable (disabled)
          Neighbor capabilities:
            Route refresh: advertised and received(new)
            Four-octets ASN Capability: advertised and received
            Address family VPNv4 Unicast: advertised and received
            Address family VPNv6 Unicast: advertised and received
            Graceful Restart Capability: received
              Remote Restart timer is 120 seconds
              Address families advertised by peer:
                VPNv4 Unicast (was not preserved, VPNv6 Unicast (was not preserved
            Enhanced Refresh Capability: advertised
            Multisession Capability:
            Stateful switchover support enabled: NO for session 1
          Message statistics:
            InQ depth is 0
            OutQ depth is 0

                                 Sent       Rcvd
            Opens:                  1          1
            Notifications:          0          0
            Updates:               11          6
            Keepalives:            75         74
            Route Refresh:          0          0
            Total:                 87         81
          Default minimum time between advertisement runs is 0 seconds

          Address tracking is enabled, the RIB does have a route to 10.16.2.2
          Connections established 1; dropped 0
          Last reset never
          Transport(tcp) path-mtu-discovery is enabled
          Graceful-Restart is disabled
        Connection state is ESTAB, I/O status: 1, unread input bytes: 0
        Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 255
        Local host: 10.64.4.4, Local port: 35281
        Foreign host: 10.16.2.2, Foreign port: 179
        Connection tableid (VRF): 0
        Maximum output segment queue size: 50

        Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

        Event Timers (current time is 0x530449):
        Timer          Starts    Wakeups            Next
        Retrans            86          0             0x0
        TimeWait            0          0             0x0
        AckHold            80         72             0x0
        SendWnd             0          0             0x0
        KeepAlive           0          0             0x0
        GiveUp              0          0             0x0
        PmtuAger            1          1             0x0
        DeadWait            0          0             0x0
        Linger              0          0             0x0
        ProcessQ            0          0             0x0

        iss:   55023811  snduna:   55027115  sndnxt:   55027115
        irs:  109992783  rcvnxt:  109995158

        sndwnd:  16616  scale:      0  maxrcvwnd:  16384
        rcvwnd:  16327  scale:      0  delrcvwnd:     57

        SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
        minRTT: 4 ms, maxRTT: 1000 ms, ACK hold: 200 ms
        uptime: 4236258 ms, Sent idletime: 4349 ms, Receive idletime: 4549 ms
        Status Flags: active open
        Option Flags: nagle, path mtu capable
        IP Precedence value : 6

        Datagrams (max data segment is 536 bytes):
        Rcvd: 164 (out of order: 0), with data: 80, total data bytes: 2374
        Sent: 166 (retransmit: 0, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 87, total data bytes: 3303

         Packets received in fast path: 0, fast processed: 0, slow path: 0
         fast lock acquisition failures: 0, slow path: 0
        TCP Semaphore      0x1286E7EC  FREE

        BGP neighbor is 10.36.3.3,  remote AS 100, internal link
          BGP version 4, remote router ID 10.36.3.3
          BGP state = Established, up for 01:10:41
          Last read 00:00:04, last write 00:00:43, hold time is 180, keepalive interval is 60 seconds
          Neighbor sessions:
            1 active, is not multisession capable (disabled)
          Neighbor capabilities:
            Route refresh: advertised and received(new)
            Four-octets ASN Capability: advertised and received
            Address family VPNv4 Unicast: advertised and received
            Address family VPNv6 Unicast: advertised and received
            Graceful Restart Capability: received
              Remote Restart timer is 120 seconds
              Address families advertised by peer:
                VPNv4 Unicast (was not preserved, VPNv6 Unicast (was not preserved
            Enhanced Refresh Capability: advertised
            Multisession Capability:
            Stateful switchover support enabled: NO for session 1
          Message statistics:
            InQ depth is 0
            OutQ depth is 0

                                 Sent       Rcvd
            Opens:                  1          1
            Notifications:          0          0
            Updates:               11          6
            Keepalives:            75         74
            Route Refresh:          0          0
            Total:                 87         81
          Default minimum time between advertisement runs is 0 seconds

          Address tracking is enabled, the RIB does have a route to 10.36.3.3
          Connections established 1; dropped 0
          Last reset never
          Transport(tcp) path-mtu-discovery is enabled
          Graceful-Restart is disabled
        Connection state is ESTAB, I/O status: 1, unread input bytes: 0
        Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 255
        Local host: 10.64.4.4, Local port: 56031
        Foreign host: 10.36.3.3, Foreign port: 179
        Connection tableid (VRF): 0
        Maximum output segment queue size: 50

        Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

        Event Timers (current time is 0x530638):
        Timer          Starts    Wakeups            Next
        Retrans            86          0             0x0
        TimeWait            0          0             0x0
        AckHold            80         73             0x0
        SendWnd             0          0             0x0
        KeepAlive           0          0             0x0
        GiveUp              0          0             0x0
        PmtuAger            1          1             0x0
        DeadWait            0          0             0x0
        Linger              0          0             0x0
        ProcessQ            0          0             0x0

        iss: 2116369173  snduna: 2116372477  sndnxt: 2116372477
        irs: 4033842748  rcvnxt: 4033845123

        sndwnd:  16616  scale:      0  maxrcvwnd:  16384
        rcvwnd:  16327  scale:      0  delrcvwnd:     57

        SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
        minRTT: 3 ms, maxRTT: 1000 ms, ACK hold: 200 ms
        uptime: 4243393 ms, Sent idletime: 5375 ms, Receive idletime: 5575 ms
        Status Flags: active open
        Option Flags: nagle, path mtu capable
        IP Precedence value : 6

        Datagrams (max data segment is 536 bytes):
        Rcvd: 165 (out of order: 0), with data: 80, total data bytes: 2374
        Sent: 167 (retransmit: 0, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 87, total data bytes: 3303

         Packets received in fast path: 0, fast processed: 0, slow path: 0
         fast lock acquisition failures: 0, slow path: 0
        TCP Semaphore      0x1286E85C  FREE

        BGP neighbor is 10.4.6.6,  vrf VRF1,  remote AS 300, external link
          Administratively shut down
          BGP version 4, remote router ID 10.4.6.6
          BGP state = Established, up for 01:01:59
          Last read 00:00:33, last write 00:00:30, hold time is 180, keepalive interval is 60 seconds
          Neighbor sessions:
            1 active, is not multisession capable (disabled)
          Neighbor capabilities:
            Route refresh: advertised
            Four-octets ASN Capability: advertised
            Address family IPv4 Unicast: advertised and received
            Enhanced Refresh Capability: advertised
            Multisession Capability:
            Stateful switchover support enabled: NO for session 1
          Message statistics:
            InQ depth is 0
            OutQ depth is 0

                                 Sent       Rcvd
            Opens:                  1          1
            Notifications:          0          0
            Updates:                3          1
            Keepalives:            69         64
            Route Refresh:          0          0
            Total:                 73         66
          Default minimum time between advertisement runs is 0 seconds

          Address tracking is enabled, the RIB does have a route to 10.4.6.6
          Connections established 2; dropped 1
          Last reset 01:02:11, due to Peer closed the session of session 1
          Transport(tcp) path-mtu-discovery is enabled
          Graceful-Restart is disabled
        Connection state is ESTAB, I/O status: 1, unread input bytes: 0
        Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 1
        Local host: 10.4.6.4, Local port: 179
        Foreign host: 10.4.6.6, Foreign port: 11010
        Connection tableid (VRF): 1
        Maximum output segment queue size: 50

        Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

        Event Timers (current time is 0x530A19):
        Timer          Starts    Wakeups            Next
        Retrans            71          0             0x0
        TimeWait            0          0             0x0
        AckHold            66         64             0x0
        SendWnd             0          0             0x0
        KeepAlive           0          0             0x0
        GiveUp              0          0             0x0
        PmtuAger            0          0             0x0
        DeadWait            0          0             0x0
        Linger              0          0             0x0
        ProcessQ            0          0             0x0

        iss:     271842  snduna:     273380  sndnxt:     273380
        irs:  930048172  rcvnxt:  930049503

        sndwnd:  32000  scale:      0  maxrcvwnd:  16384
        rcvwnd:  15054  scale:      0  delrcvwnd:   1330

        SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
        minRTT: 1 ms, maxRTT: 1000 ms, ACK hold: 200 ms
        uptime: 3720132 ms, Sent idletime: 31107 ms, Receive idletime: 30999 ms
        Status Flags: passive open, gen tcbs
        Option Flags: VRF id set, nagle, path mtu capable
        IP Precedence value : 6

        Datagrams (max data segment is 1460 bytes):
        Rcvd: 137 (out of order: 0), with data: 66, total data bytes: 1330
        Sent: 138 (retransmit: 0, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 72, total data bytes: 1537

         Packets received in fast path: 0, fast processed: 0, slow path: 0
         fast lock acquisition failures: 0, slow path: 0
        TCP Semaphore      0x1286E62C  FREE

        BGP neighbor is 10.66.6.6,  vrf VRF2,  remote AS 400, external link
          BGP version 4, remote router ID 10.66.6.6
          BGP state = Established, up for 01:01:51
          Last read 00:00:24, last write 00:00:21, hold time is 180, keepalive interval is 60 seconds
          Neighbor sessions:
            1 active, is not multisession capable (disabled)
          Neighbor capabilities:
            Route refresh: advertised
            Four-octets ASN Capability: advertised
            Address family IPv4 Unicast: advertised and received
            Enhanced Refresh Capability: advertised
            Multisession Capability:
            Stateful switchover support enabled: NO for session 1
          Message statistics:
            InQ depth is 0
            OutQ depth is 0

                                 Sent       Rcvd
            Opens:                  1          1
            Notifications:          0          0
            Updates:                1          1
            Keepalives:            69         64
            Route Refresh:          0          0
            Total:                 71         66
          Default minimum time between advertisement runs is 0 seconds

          Address tracking is enabled, the RIB does have a route to 10.66.6.6
          Connections established 2; dropped 1
          Last reset 01:05:09, due to Active open failed
          Transport(tcp) path-mtu-discovery is enabled
          Graceful-Restart is disabled
        Connection state is ESTAB, I/O status: 1, unread input bytes: 0
        Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 1
        Local host: 10.66.6.4, Local port: 179
        Foreign host: 10.66.6.6, Foreign port: 11003
        Connection tableid (VRF): 2
        Maximum output segment queue size: 50

        Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

        Event Timers (current time is 0x530C0D):
        Timer          Starts    Wakeups            Next
        Retrans            70          0             0x0
        TimeWait            0          0             0x0
        AckHold            66         64             0x0
        SendWnd             0          0             0x0
        KeepAlive           0          0             0x0
        GiveUp              0          0             0x0
        PmtuAger            0          0             0x0
        DeadWait            0          0             0x0
        Linger              0          0             0x0
        ProcessQ            0          0             0x0

        iss: 2048397580  snduna: 2048398972  sndnxt: 2048398972
        irs:  213294715  rcvnxt:  213296046

        sndwnd:  32000  scale:      0  maxrcvwnd:  16384
        rcvwnd:  15054  scale:      0  delrcvwnd:   1330

        SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
        minRTT: 2 ms, maxRTT: 1000 ms, ACK hold: 200 ms
        uptime: 3712326 ms, Sent idletime: 21866 ms, Receive idletime: 21765 ms
        Status Flags: passive open, gen tcbs
        Option Flags: VRF id set, nagle, path mtu capable
        IP Precedence value : 6

        Datagrams (max data segment is 1460 bytes):
        Rcvd: 135 (out of order: 0), with data: 66, total data bytes: 1330
        Sent: 137 (retransmit: 0, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 71, total data bytes: 1391

         Packets received in fast path: 0, fast processed: 0, slow path: 0
         fast lock acquisition failures: 0, slow path: 0
        TCP Semaphore      0x1286E8CC  FREE


        For address family: VPNv6 Unicast
        BGP neighbor is 10.64.4.4,  remote AS 100, internal link
          Description: router2222222
          BGP version 4, remote router ID 10.64.4.4
          BGP state = Established, up for 01:10:38
          Last read 00:00:07, last write 00:00:12, hold time is 180, keepalive interval is 60 seconds
          Neighbor sessions:
            1 active, is not multisession capable (disabled)
          Neighbor capabilities:
            Route refresh: advertised and received(new)
            Four-octets ASN Capability: advertised and received
            Address family VPNv4 Unicast: advertised and received
            Address family VPNv6 Unicast: advertised and received
            Graceful Restart Capability: received
              Remote Restart timer is 120 seconds
              Address families advertised by peer:
                VPNv4 Unicast (was not preserved, VPNv6 Unicast (was not preserved
            Enhanced Refresh Capability: advertised
            Multisession Capability:
            Stateful switchover support enabled: NO for session 1
          Message statistics:
            InQ depth is 0
            OutQ depth is 0

                                 Sent       Rcvd
            Opens:                  1          1
            Notifications:          0          0
            Updates:               11          6
            Keepalives:            75         74
            Route Refresh:          0          0
            Total:                 87         81
          Default minimum time between advertisement runs is 0 seconds

          Address tracking is enabled, the RIB does have a route to 10.16.2.2
          Connections established 1; dropped 0
          Last reset never
          Transport(tcp) path-mtu-discovery is enabled
          Graceful-Restart is disabled
        Connection state is ESTAB, I/O status: 1, unread input bytes: 0
        Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 255
        Local host: 10.64.4.4, Local port: 35281
        Foreign host: 10.16.2.2, Foreign port: 179
        Connection tableid (VRF): 0
        Maximum output segment queue size: 50

        Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

        Event Timers (current time is 0x530FF5):
        Timer          Starts    Wakeups            Next
        Retrans            86          0             0x0
        TimeWait            0          0             0x0
        AckHold            80         72             0x0
        SendWnd             0          0             0x0
        KeepAlive           0          0             0x0
        GiveUp              0          0             0x0
        PmtuAger            1          1             0x0
        DeadWait            0          0             0x0
        Linger              0          0             0x0
        ProcessQ            0          0             0x0

        iss:   55023811  snduna:   55027115  sndnxt:   55027115
        irs:  109992783  rcvnxt:  109995158

        sndwnd:  16616  scale:      0  maxrcvwnd:  16384
        rcvwnd:  16327  scale:      0  delrcvwnd:     57

        SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
        minRTT: 4 ms, maxRTT: 1000 ms, ACK hold: 200 ms
        uptime: 4239741 ms, Sent idletime: 7832 ms, Receive idletime: 8032 ms
        Status Flags: active open
        Option Flags: nagle, path mtu capable
        IP Precedence value : 6

        Datagrams (max data segment is 536 bytes):
        Rcvd: 164 (out of order: 0), with data: 80, total data bytes: 2374
        Sent: 166 (retransmit: 0, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 87, total data bytes: 3303

         Packets received in fast path: 0, fast processed: 0, slow path: 0
         fast lock acquisition failures: 0, slow path: 0
        TCP Semaphore      0x1286E7EC  FREE

        BGP neighbor is 10.100.5.5,  remote AS 100, internal link
          BGP version 4, remote router ID 10.100.5.5
          BGP state = Established, up for 01:10:44
          Last read 00:00:08, last write 00:00:47, hold time is 180, keepalive interval is 60 seconds
          Neighbor sessions:
            1 active, is not multisession capable (disabled)
          Neighbor capabilities:
            Route refresh: advertised and received(new)
            Four-octets ASN Capability: advertised and received
            Address family VPNv4 Unicast: advertised and received
            Address family VPNv6 Unicast: advertised and received
            Graceful Restart Capability: received
              Remote Restart timer is 120 seconds
              Address families advertised by peer:
                VPNv4 Unicast (was not preserved, VPNv6 Unicast (was not preserved
            Enhanced Refresh Capability: advertised
            Multisession Capability:
            Stateful switchover support enabled: NO for session 1
          Message statistics:
            InQ depth is 0
            OutQ depth is 0

                                 Sent       Rcvd
            Opens:                  1          1
            Notifications:          0          0
            Updates:               11          6
            Keepalives:            75         74
            Route Refresh:          0          0
            Total:                 87         81
          Default minimum time between advertisement runs is 0 seconds

          Address tracking is enabled, the RIB does have a route to 10.36.3.3
          Connections established 1; dropped 0
          Last reset never
          Transport(tcp) path-mtu-discovery is enabled
          Graceful-Restart is disabled
        Connection state is ESTAB, I/O status: 1, unread input bytes: 0
        Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 255
        Local host: 10.64.4.4, Local port: 56031
        Foreign host: 10.36.3.3, Foreign port: 179
        Connection tableid (VRF): 0
        Maximum output segment queue size: 50

        Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

        Event Timers (current time is 0x5313D8):
        Timer          Starts    Wakeups            Next
        Retrans            86          0             0x0
        TimeWait            0          0             0x0
        AckHold            80         73             0x0
        SendWnd             0          0             0x0
        KeepAlive           0          0             0x0
        GiveUp              0          0             0x0
        PmtuAger            1          1             0x0
        DeadWait            0          0             0x0
        Linger              0          0             0x0
        ProcessQ            0          0             0x0

        iss: 2116369173  snduna: 2116372477  sndnxt: 2116372477
        irs: 4033842748  rcvnxt: 4033845123

        sndwnd:  16616  scale:      0  maxrcvwnd:  16384
        rcvwnd:  16327  scale:      0  delrcvwnd:     57

        SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
        minRTT: 3 ms, maxRTT: 1000 ms, ACK hold: 200 ms
        uptime: 4246385 ms, Sent idletime: 8367 ms, Receive idletime: 8567 ms
        Status Flags: active open
        Option Flags: nagle, path mtu capable
        IP Precedence value : 6

        Datagrams (max data segment is 536 bytes):
        Rcvd: 165 (out of order: 0), with data: 80, total data bytes: 2374
        Sent: 167 (retransmit: 0, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 87, total data bytes: 3303

         Packets received in fast path: 0, fast processed: 0, slow path: 0
         fast lock acquisition failures: 0, slow path: 0
        TCP Semaphore      0x1286E85C  FREE

        BGP neighbor is 2001:DB8:4:6::6,  vrf VRF1,  remote AS 300, external link
          BGP version 4, remote router ID 10.4.6.6
          BGP state = Established, up for 01:01:58
          Last read 00:00:32, last write 00:00:06, hold time is 180, keepalive interval is 60 seconds
          Neighbor sessions:
            1 active, is not multisession capable (disabled)
          Neighbor capabilities:
            Route refresh: advertised
            Four-octets ASN Capability: advertised
            Address family IPv6 Unicast: advertised and received
            Enhanced Refresh Capability: advertised
            Multisession Capability:
            Stateful switchover support enabled: NO for session 1
          Message statistics:
            InQ depth is 0
            OutQ depth is 0

                                 Sent       Rcvd
            Opens:                  1          1
            Notifications:          0          0
            Updates:                3          1
            Keepalives:            70         64
            Route Refresh:          0          0
            Total:                 74         66
          Default minimum time between advertisement runs is 0 seconds

          Address tracking is enabled, the RIB does have a route to 2001:DB8:4:6::6
          Connections established 2; dropped 1
          Last reset 01:05:12, due to Active open failed
          Transport(tcp) path-mtu-discovery is enabled
          Graceful-Restart is disabled
        Connection state is ESTAB, I/O status: 1, unread input bytes: 0
        Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 1
        Local host: 2001:DB8:4:6::4, Local port: 179
        Foreign host: 2001:DB8:4:6::6, Foreign port: 11003
        Connection tableid (VRF): 503316481
        Maximum output segment queue size: 50

        Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

        Event Timers (current time is 0x5315CE):
        Timer          Starts    Wakeups            Next
        Retrans            72          0             0x0
        TimeWait            0          0             0x0
        AckHold            66         64             0x0
        SendWnd             0          0             0x0
        KeepAlive           0          0             0x0
        GiveUp              0          0             0x0
        PmtuAger            0          0             0x0
        DeadWait            0          0             0x0
        Linger              0          0             0x0
        ProcessQ            0          0             0x0

        iss:  164676617  snduna:  164678296  sndnxt:  164678296
        irs: 1797203329  rcvnxt: 1797204710

        sndwnd:  32000  scale:      0  maxrcvwnd:  16384
        rcvwnd:  15004  scale:      0  delrcvwnd:   1380

        SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
        minRTT: 1 ms, maxRTT: 1000 ms, ACK hold: 200 ms
        uptime: 3718683 ms, Sent idletime: 6954 ms, Receive idletime: 6849 ms
        Status Flags: passive open, gen tcbs
        Option Flags: VRF id set, nagle, path mtu capable
        IP Precedence value : 6

        Datagrams (max data segment is 1440 bytes):
        Rcvd: 138 (out of order: 0), with data: 66, total data bytes: 1380
        Sent: 139 (retransmit: 0, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 139, total data bytes: 7246

         Packets received in fast path: 0, fast processed: 0, slow path: 0
         fast lock acquisition failures: 0, slow path: 0
        TCP Semaphore      0x1286E9AC  FREE

        BGP neighbor is 2001:DB8:20:4:6::6,  vrf VRF2,  remote AS 400, external link
          BGP version 4, remote router ID 10.66.6.6
          BGP state = Established, up for 01:01:51
          Last read 00:00:22, last write 00:00:01, hold time is 180, keepalive interval is 60 seconds
          Neighbor sessions:
            1 active, is not multisession capable (disabled)
          Neighbor capabilities:
            Route refresh: advertised
            Four-octets ASN Capability: advertised
            Address family IPv6 Unicast: advertised and received
            Enhanced Refresh Capability: advertised
            Multisession Capability:
            Stateful switchover support enabled: NO for session 1
          Message statistics:
            InQ depth is 0
            OutQ depth is 0

                                 Sent       Rcvd
            Opens:                  1          1
            Notifications:          0          0
            Updates:                1          1
            Keepalives:            70         64
            Route Refresh:          0          0
            Total:                 72         66
          Default minimum time between advertisement runs is 0 seconds

          Address tracking is enabled, the RIB does have a route to 2001:DB8:20:4:6::6
          Connections established 2; dropped 1
          Last reset 01:05:13, due to Active open failed
          Transport(tcp) path-mtu-discovery is enabled
          Graceful-Restart is disabled
        Connection state is ESTAB, I/O status: 1, unread input bytes: 0
        Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 1
        Local host: 2001:DB8:20:4:6::4, Local port: 179
        Foreign host: 2001:DB8:20:4:6::6, Foreign port: 11003
        Connection tableid (VRF): 503316482
        Maximum output segment queue size: 50

        Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

        Event Timers (current time is 0x5319B5):
        Timer          Starts    Wakeups            Next
        Retrans            71          0             0x0
        TimeWait            0          0             0x0
        AckHold            66         64             0x0
        SendWnd             0          0             0x0
        KeepAlive           0          0             0x0
        GiveUp              0          0             0x0
        PmtuAger            0          0             0x0
        DeadWait            0          0             0x0
        Linger              0          0             0x0
        ProcessQ            0          0             0x0

        iss: 3178074389  snduna: 3178075806  sndnxt: 3178075806
        irs:  693674496  rcvnxt:  693675877

        sndwnd:  32000  scale:      0  maxrcvwnd:  16384
        rcvwnd:  15004  scale:      0  delrcvwnd:   1380

        SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
        minRTT: 3 ms, maxRTT: 1000 ms, ACK hold: 200 ms
        uptime: 3711535 ms, Sent idletime: 2335 ms, Receive idletime: 2277 ms
        Status Flags: passive open, gen tcbs
        Option Flags: VRF id set, nagle, path mtu capable
        IP Precedence value : 6

        Datagrams (max data segment is 1440 bytes):
        Rcvd: 137 (out of order: 0), with data: 66, total data bytes: 1380
        Sent: 138 (retransmit: 0, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 138, total data bytes: 6944

         Packets received in fast path: 0, fast processed: 0, slow path: 0
         fast lock acquisition failures: 0, slow path: 0
        TCP Semaphore      0x1286E93C  FREE


        For address family: IPv4 Multicast

        For address family: L2VPN E-VPN

        For address family: VPNv4 Multicast

        For address family: MVPNv4 Unicast

        For address family: MVPNv6 Unicast

        For address family: VPNv6 Multicast
        '''}

    golden_parsed_output2 = {
        'list_of_neighbors': ['192.168.165.120'],
        'vrf': 
            {'default': 
                {'neighbor': 
                    {'192.168.165.120': 
                        {'address_family': 
                            {'l2vpn vpls': 
                                {'advertise_bit': 0,
                                'bgp_table_version': 403,
                                'current_time': '0x233AE79E',
                                'dynamic_slow_peer_recovered': 'never',
                                'extended_community_attribute_sent': True,
                                'index': 4,
                                'last_detected_dynamic_slow_peer': 'never',
                                'last_received_refresh_end_of_rib': '21:35:12',
                                'last_received_refresh_start_of_rib': '21:35:12',
                                'last_sent_refresh_end_of_rib': '04:52:14',
                                'last_sent_refresh_start_of_rib': '04:52:14',
                                'local_policy_denied_prefixes_counters': 
                                    {'inbound': 
                                        {'bestpath_from_this_peer': 'n/a',
                                        'originator_loop': 1608,
                                        'total': 1608},
                                    'outbound': 
                                        {'bestpath_from_this_peer': 1407,
                                        'originator_loop': 'n/a',
                                        'total': 1407}},
                                'max_nlri': 1,
                                'min_nlri': 0,
                                'neighbor_version': '403/0',
                                'output_queue_size': 0,
                                'prefix_activity_counters': 
                                    {'received': 
                                        {'explicit_withdraw': 0,
                                        'implicit_withdraw': 1407,
                                        'prefixes_total': 1608,
                                        'used_as_bestpath': 0,
                                        'used_as_multipath': 0},
                                    'sent': 
                                        {'explicit_withdraw': 0,
                                        'implicit_withdraw': 1608,
                                        'prefixes_total': 1809,
                                        'used_as_bestpath': 'n/a',
                                        'used_as_multipath': 'n/a'}},
                                'refresh_activity_counters': 
                                    {'received': 
                                        {'refresh_end_of_rib': 8,
                                        'refresh_start_of_rib': 8},
                                    'sent': 
                                        {'refresh_end_of_rib': 6,
                                        'refresh_start_of_rib': 6}},
                                'refresh_epoch': 9,
                                'refresh_in': 0,
                                'refresh_out': 0,
                                'slow_peer_detection': False,
                                'slow_peer_split_update_group_dynamic': False,
                                'suppress_ldp_signaling': True,
                                'update_group_member': 4},
                            'vpnv4 unicast': 
                                {'advertise_bit': 0,
                                'bgp_table_version': 33086714,
                                'community_attribute_sent': True,
                                'dynamic_slow_peer_recovered': 'never',
                                'extended_community_attribute_sent': True,
                                'index': 1954,
                                'last_detected_dynamic_slow_peer': 'never',
                                'last_received_refresh_end_of_rib': '21:34:57',
                                'last_received_refresh_start_of_rib': '21:35:12',
                                'last_sent_refresh_end_of_rib': '04:51:02',
                                'last_sent_refresh_start_of_rib': '04:52:14',
                                'local_policy_denied_prefixes_counters': 
                                    {'inbound': 
                                        {'af_permit_check': 'n/a',
                                        'af_update_check': 'n/a',
                                        'bestpath_from_ibgp_peer': 'n/a',
                                        'bestpath_from_this_peer': 'n/a',
                                        'originator_loop': 191399,
                                        'total': 191399},
                                    'outbound': 
                                        {'af_permit_check': 84090,
                                        'af_update_check': 11509,
                                        'bestpath_from_ibgp_peer': 3488082,
                                        'bestpath_from_this_peer': 10473918,
                                        'originator_loop': 'n/a',
                                        'total': 14057599}},
                                'max_nlri': 270,
                                'min_nlri': 0,
                                'neighbor_version': '33086714/0',
                                'output_queue_size': 0,
                                'prefix_activity_counters': 
                                    {'received': 
                                        {'explicit_withdraw': 4059067,
                                        'implicit_withdraw': 12437988,
                                        'prefixes_total': 18498954,
                                        'used_as_bestpath': 0,
                                        'used_as_multipath': 0},
                                    'sent': 
                                        {'explicit_withdraw': 2045210,
                                        'implicit_withdraw': 81710,
                                        'prefixes_total': 131522,
                                        'used_as_bestpath': 'n/a',
                                        'used_as_multipath': 'n/a'}},
                                'refresh_activity_counters': 
                                    {'received': 
                                        {'refresh_end_of_rib': 7,
                                        'refresh_start_of_rib': 8},
                                    'sent': 
                                        {'refresh_end_of_rib': 7,
                                        'refresh_start_of_rib': 7}},
                                'refresh_epoch': 9,
                                'refresh_in': 15,
                                'refresh_out': 72,
                                'slow_peer_detection': False,
                                'slow_peer_split_update_group_dynamic': False,
                                'update_group_member': 1954}},
                        'bgp_event_timer': 
                            {'next': 
                                {'ackhold': '0x0',
                                'deadwait': '0x0',
                                'giveup': '0x0',
                                'keepalive': '0x0',
                                'linger': '0x0',
                                'pmtuager': '0x0',
                                'processq': '0x0',
                                'retrans': '0x0',
                                'sendwnd': '0x0',
                                'timewait': '0x0'},
                            'starts': 
                                {'ackhold': 153946,
                                'deadwait': 0,
                                'giveup': 0,
                                'keepalive': 0,
                                'linger': 0,
                                'pmtuager': 1,
                                'processq': 0,
                                'retrans': 35475,
                                'sendwnd': 0,
                                'timewait': 0},
                            'wakeups': 
                                {'ackhold': 6831,
                                'deadwait': 0,
                                'giveup': 0,
                                'keepalive': 0,
                                'linger': 0,
                                'pmtuager': 1,
                                'processq': 0,
                                'retrans': 3,
                                'sendwnd': 0,
                                'timewait': 0}},
                                'bgp_neighbor_session': {
                            'sessions': 1,
                            },
                        'bgp_negotiated_capabilities': 
                            {'enhanced_refresh': 'advertised '
                                                 'and '
                                                 'received',
                            'four_octets_asn': 'advertised '
                                               'and '
                                               'received',
                            'graceful_restart': 'advertised '
                                                'and '
                                                'received',
                            'graceful_restart_af_advertised_by_peer': ['vpnv4 '
                                                                       'unicast',
                                                                     'l2vpn '
                                                                       'vpls'],
                            'l2vpn_vpls': 'advertised '
                                          'and '
                                          'received',
                            'remote_restart_timer': 120,
                            'route_refresh': 'advertised '
                                             'and '
                                             'received(new)',
                            'stateful_switchover': 'NO '
                                                   'for '
                                                   'session '
                                                   '1',
                            'vpnv4_unicast': 'advertised '
                                             'and '
                                             'received'},
                        'bgp_negotiated_keepalive_timers': 
                            {'hold_time': 90,
                            'keepalive_interval': 30,
                            'min_holdtime': 15},
                        'bgp_neighbor_counters': 
                            {'messages': 
                                {'in_queue_depth': 0,
                                'out_queue_depth': 0,
                                'received': 
                                    {'keepalives': 4659,
                                    'notifications': 0,
                                    'opens': 1,
                                    'route_refresh': 6,
                                    'total': 140627,
                                    'updates': 135930},
                                'sent': 
                                    {'keepalives': 5187,
                                    'notifications': 0,
                                    'opens': 1,
                                    'route_refresh': 10,
                                    'total': 39192,
                                    'updates': 33968}}},
                        'bgp_session_transport': 
                            {'ack_hold': 200,
                            'address_tracking_status': 'enabled',
                            'connection': 
                                {'dropped': 3,
                                'established': 4,
                                'last_reset': '1d16h',
                                'reset_reason': 'Neighbor '
                                                'reset'},
                            'connection_state': 'estab',
                            'connection_tableid': 0,
                            'datagram': 
                                {'datagram_received': 
                                    {'out_of_order': 0,
                                    'total_data': 356569101,
                                    'value': 363804,
                                    'with_data': 281016},
                                'datagram_sent': 
                                    {'fastretransmit': 1,
                                    'partialack': 0,
                                    'retransmit': 3,
                                    'second_congestion': 0,
                                    'total_data': 76361745,
                                    'value': 423496,
                                    'with_data': 62849}},
                            'delrcvwnd': 323,
                            'ecn_connection': 'disabled',
                            'enqueued_packets': 
                                {'input_packet': 0,
                                'mis_ordered_packet': 0,
                                'retransmit_packet': 0},
                            'fast_lock_acquisition_failures': 0,
                            'gr_restart_time': 120,
                            'gr_stalepath_time': 360,
                            'graceful_restart': 'enabled',
                            'io_status': 1,
                            'ip_precedence_value': 6,
                            'irs': 3910340259,
                            'iss': 673876598,
                            'krtt': 0,
                            'lock_slow_path': 0,
                            'max_rtt': 1344,
                            'maximum_output_segment_queue_size': 50,
                            'maxrcvwnd': 16384,
                            'min_rtt': 0,
                            'min_time_between_advertisement_runs': 0,
                            'minimum_incoming_ttl': 0,
                            'option_flags': 'nagle, '
                                            'path '
                                            'mtu '
                                            'capable',
                            'outgoing_ttl': 255,
                            'packet_fast_path': 0,
                            'packet_fast_processed': 0,
                            'packet_slow_path': 0,
                            'rcv_scale': 0,
                            'rcvnxt': 4266909361,
                            'rcvwnd': 16061,
                            'receive_idletime': 9542,
                            'rib_route_ip': '192.168.165.120',
                            'rtto': 1003,
                            'rtv': 3,
                            'sent_idletime': 9744,
                            'snd_scale': 0,
                            'sndnxt': 750238254,
                            'snduna': 750238254,
                            'sndwnd': 15567,
                            'srtt': 1000,
                            'sso': False,
                            'status_flags': 'active '
                                            'open',
                            'tcp_path_mtu_discovery': 'enabled',
                            'tcp_semaphore': '0x7FDED5D66E70',
                            'tcp_semaphore_status': 'FREE',
                            'transport': 
                                {'foreign_host': '192.168.165.120',
                                'foreign_port': '179',
                                'local_host': '10.169.197.254',
                                'local_port': '13949',
                                'mss': 1400},
                            'unread_input_bytes': 0,
                            'uptime': 144455028},
                        'bgp_version': 4,
                        'link': 'internal',
                        'remote_as': 5918,
                        'router_id': '192.168.165.120',
                        'session_state': 'Established',
                        'shutdown': False}}}}}

    golden_output2 = {'execute.return_value': '''
        Router#show bgp l2vpn vpls all neighbors 192.168.165.120
        Load for five secs: 29%/0%; one minute: 7%; five minutes: 5%
        Time source is NTP, 16:31:15.088 EST Tue Jun 8 2016

        BGP neighbor is 192.168.165.120,  remote AS 5918, internal link
          BGP version 4, remote router ID 192.168.165.120
          BGP state = Established, up for 1d16h
          Last read 00:00:26, last write 00:00:09, hold time is 90, keepalive interval is 30 seconds
          Configured hold time is 90, keepalive interval is 30 seconds
          Minimum holdtime from neighbor is 15 seconds
          Neighbor sessions:
            1 active, is not multisession capable (disabled)
          Neighbor capabilities:
            Route refresh: advertised and received(new)
            Four-octets ASN Capability: advertised and received
            Address family VPNv4 Unicast: advertised and received
            Address family L2VPN Vpls: advertised and received
            Graceful Restart Capability: advertised and received
              Remote Restart timer is 120 seconds
              Address families advertised by peer:
                VPNv4 Unicast (was not preserved, L2VPN Vpls (was not preserved
            Enhanced Refresh Capability: advertised and received
            Multisession Capability: 
            Stateful switchover support enabled: NO for session 1
          Message statistics:
            InQ depth is 0
            OutQ depth is 0
            
                                 Sent       Rcvd
            Opens:                  1          1
            Notifications:          0          0
            Updates:            33968     135930
            Keepalives:          5187       4659
            Route Refresh:         10          6
            Total:              39192     140627
          Do log neighbor state changes (via global configuration)
          Default minimum time between advertisement runs is 0 seconds

         For address family: VPNv4 Unicast
          BGP diverse-paths computation is enabled 
          Session: 192.168.165.120
          BGP table version 33086714, neighbor version 33086714/0
          Output queue size : 0
          Index 1954, Advertise bit 0
          1954 update-group member
          Community attribute sent to this neighbor
          Extended-community attribute sent to this neighbor
          Slow-peer detection is disabled
          Slow-peer split-update-group dynamic is disabled
                                         Sent       Rcvd
          Prefix activity:               ----       ----
            Prefixes Current:           10202    2001899 (Consumes 240227880 bytes)
            Prefixes Total:            131522   18498954
            Implicit Withdraw:          81710   12437988
            Explicit Withdraw:        2045210    4059067
            Used as bestpath:             n/a          0
            Used as multipath:            n/a          0

                                           Outbound    Inbound
          Local Policy Denied Prefixes:    --------    -------
            ORIGINATOR loop:                    n/a     191399
            Bestpath from this peer:       10473918        n/a
            Bestpath from iBGP peer:        3488082        n/a
            AF Permit Check:                  84090        n/a
            AF Update Check:                  11509        n/a
            Total:                         14057599     191399
          Number of NLRIs in the update sent: max 270, min 0
          Last detected as dynamic slow peer: never
          Dynamic slow peer recovered: never
          Refresh Epoch: 9
          Last Sent Refresh Start-of-rib: 04:52:14
          Last Sent Refresh End-of-rib: 04:51:02
          Refresh-Out took 72 seconds
          Last Received Refresh Start-of-rib: 21:35:12
          Last Received Refresh End-of-rib: 21:34:57
          Refresh-In took 15 seconds
                               Sent   Rcvd
            Refresh activity:          ----   ----
              Refresh Start-of-RIB          7          8
              Refresh End-of-RIB            7          7

        For address family: L2VPN Vpls
          Session: 192.168.165.120
          BGP table version 403, neighbor version 403/0
          Output queue size : 0
          Index 4, Advertise bit 0
          4 update-group member
          Extended-community attribute sent to this neighbor
          Suppress LDP signaling protocol
          Slow-peer detection is disabled
          Slow-peer split-update-group dynamic is disabled
                                         Sent       Rcvd
          Prefix activity:               ----       ----
            Prefixes Current:             201        201 (Consumes 27336 bytes)
            Prefixes Total:              1809       1608
            Implicit Withdraw:           1608       1407
            Explicit Withdraw:              0          0
            Used as bestpath:             n/a          0
            Used as multipath:            n/a          0

                                           Outbound    Inbound
          Local Policy Denied Prefixes:    --------    -------
            ORIGINATOR loop:                    n/a       1608
            Bestpath from this peer:           1407        n/a
            Total:                             1407       1608
          Number of NLRIs in the update sent: max 1, min 0
          Last detected as dynamic slow peer: never
          Dynamic slow peer recovered: never
          Refresh Epoch: 9
          Last Sent Refresh Start-of-rib: 04:52:14
          Last Sent Refresh End-of-rib: 04:52:14
          Refresh-Out took 0 seconds
          Last Received Refresh Start-of-rib: 21:35:12
          Last Received Refresh End-of-rib: 21:35:12
          Refresh-In took 0 seconds
                               Sent   Rcvd
            Refresh activity:          ----   ----
              Refresh Start-of-RIB          6          8
              Refresh End-of-RIB            6          8

          Address tracking is enabled, the RIB does have a route to 192.168.165.120
          Connections established 4; dropped 3
          Last reset 1d16h, due to Neighbor reset
          Interface associated: (none) (peering address NOT in same link)
          Transport(tcp) path-mtu-discovery is enabled
          Graceful-Restart is enabled, restart-time 120 seconds, stalepath-time 360 seconds
          SSO is disabled
        Connection state is ESTAB, I/O status: 1, unread input bytes: 0            
        Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 255
        Local host: 10.169.197.254, Local port: 13949
        Foreign host: 192.168.165.120, Foreign port: 179
        Connection tableid (VRF): 0
        Maximum output segment queue size: 50

        Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

        Event Timers (current time is 0x233AE79E):
        Timer          Starts    Wakeups            Next
        Retrans         35475          3             0x0
        TimeWait            0          0             0x0
        AckHold        153946       6831             0x0
        SendWnd             0          0             0x0
        KeepAlive           0          0             0x0
        GiveUp              0          0             0x0
        PmtuAger            1          1             0x0
        DeadWait            0          0             0x0
        Linger              0          0             0x0
        ProcessQ            0          0             0x0

        iss:  673876598  snduna:  750238254  sndnxt:  750238254
        irs: 3910340259  rcvnxt: 4266909361

        sndwnd:  15567  scale:      0  maxrcvwnd:  16384
        rcvwnd:  16061  scale:      0  delrcvwnd:    323

        SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
        minRTT: 0 ms, maxRTT: 1344 ms, ACK hold: 200 ms
        uptime: 144455028 ms, Sent idletime: 9744 ms, Receive idletime: 9542 ms 
        Status Flags: active open
        Option Flags: nagle, path mtu capable
        IP Precedence value : 6

        Datagrams (max data segment is 1400 bytes):
        Rcvd: 363804 (out of order: 0), with data: 281016, total data bytes: 356569101
        Sent: 423496 (retransmit: 3, fastretransmit: 1, partialack: 0, Second Congestion: 0), with data: 62849, total data bytes: 76361745

         Packets received in fast path: 0, fast processed: 0, slow path: 0
         fast lock acquisition failures: 0, slow path: 0
        TCP Semaphore      0x7FDED5D66E70  FREE 
        Router#
        '''}

    golden_parsed_output3 = {
        'list_of_neighbors': ['192.168.165.119'],
        'vrf': {'default': {'neighbor': {'192.168.165.119': {'address_family': {'l2vpn vpls': {'advertise_bit': 0,
                                                                                        'bgp_table_version': 403,
                                                                                        'current_time': '0x233AE2F9',
                                                                                        'dynamic_slow_peer_recovered': 'never',
                                                                                        'extended_community_attribute_sent': True,
                                                                                        'index': 4,
                                                                                        'last_detected_dynamic_slow_peer': 'never',
                                                                                        'last_received_refresh_end_of_rib': '21:35:10',
                                                                                        'last_received_refresh_start_of_rib': '21:35:11',
                                                                                        'last_sent_refresh_end_of_rib': '04:52:13',
                                                                                        'last_sent_refresh_start_of_rib': '04:52:13',
                                                                                        'local_policy_denied_prefixes_counters': {'inbound': {'bestpath_from_this_peer': 'n/a',
                                                                                                                                              'originator_loop': 1206,
                                                                                                                                              'total': 1206},
                                                                                                                                  'outbound': {'bestpath_from_this_peer': 1407,
                                                                                                                                               'originator_loop': 'n/a',
                                                                                                                                               'total': 1407}},
                                                                                        'max_nlri': 1,
                                                                                        'min_nlri': 0,
                                                                                        'neighbor_version': '403/0',
                                                                                        'output_queue_size': 0,
                                                                                        'prefix_activity_counters': {'received': {'explicit_withdraw': 0,
                                                                                                                                  'implicit_withdraw': 1005,
                                                                                                                                  'prefixes_total': 1206,
                                                                                                                                  'used_as_bestpath': 201,
                                                                                                                                  'used_as_multipath': 0},
                                                                                                                     'sent': {'explicit_withdraw': 0,
                                                                                                                              'implicit_withdraw': 1608,
                                                                                                                              'prefixes_total': 1809,
                                                                                                                              'used_as_bestpath': 'n/a',
                                                                                                                              'used_as_multipath': 'n/a'}},
                                                                                        'refresh_activity_counters': {'received': {'refresh_end_of_rib': 6,
                                                                                                                                   'refresh_start_of_rib': 6},
                                                                                                                      'sent': {'refresh_end_of_rib': 2,
                                                                                                                               'refresh_start_of_rib': 2}},
                                                                                        'refresh_epoch': 7,
                                                                                        'refresh_in': 1,
                                                                                        'refresh_out': 0,
                                                                                        'slow_peer_detection': False,
                                                                                        'slow_peer_split_update_group_dynamic': False,
                                                                                        'suppress_ldp_signaling': True,
                                                                                        'update_group_member': 4},
                                                                         'vpnv4 unicast': {'advertise_bit': 0,
                                                                                           'bgp_table_version': 33086714,
                                                                                           'community_attribute_sent': True,
                                                                                           'dynamic_slow_peer_recovered': 'never',
                                                                                           'extended_community_attribute_sent': True,
                                                                                           'index': 1954,
                                                                                           'last_detected_dynamic_slow_peer': 'never',
                                                                                           'last_received_refresh_end_of_rib': '21:34:52',
                                                                                           'last_received_refresh_start_of_rib': '21:35:11',
                                                                                           'last_sent_refresh_end_of_rib': '04:51:01',
                                                                                           'last_sent_refresh_start_of_rib': '04:52:13',
                                                                                           'local_policy_denied_prefixes_counters': {'inbound': {'af_permit_check': 'n/a',
                                                                                                                                                 'af_update_check': 'n/a',
                                                                                                                                                 'bestpath_from_ibgp_peer': 'n/a',
                                                                                                                                                 'bestpath_from_this_peer': 'n/a',
                                                                                                                                                 'originator_loop': 151495,
                                                                                                                                                 'total': 151495},
                                                                                                                                     'outbound': {'af_permit_check': 84090,
                                                                                                                                                  'af_update_check': 11509,
                                                                                                                                                  'bestpath_from_ibgp_peer': 3488082,
                                                                                                                                                  'bestpath_from_this_peer': 10473918,
                                                                                                                                                  'originator_loop': 'n/a',
                                                                                                                                                  'total': 14057599}},
                                                                                           'max_nlri': 270,
                                                                                           'min_nlri': 0,
                                                                                           'neighbor_version': '33086714/0',
                                                                                           'output_queue_size': 0,
                                                                                           'prefix_activity_counters': {'received': {'explicit_withdraw': 4059067,
                                                                                                                                     'implicit_withdraw': 10255632,
                                                                                                                                     'prefixes_total': 16316598,
                                                                                                                                     'used_as_bestpath': 2005600,
                                                                                                                                     'used_as_multipath': 0},
                                                                                                                        'sent': {'explicit_withdraw': 2045210,
                                                                                                                                 'implicit_withdraw': 81710,
                                                                                                                                 'prefixes_total': 131522,
                                                                                                                                 'used_as_bestpath': 'n/a',
                                                                                                                                 'used_as_multipath': 'n/a'}},
                                                                                           'refresh_activity_counters': {'received': {'refresh_end_of_rib': 6,
                                                                                                                                      'refresh_start_of_rib': 6},
                                                                                                                         'sent': {'refresh_end_of_rib': 4,
                                                                                                                                  'refresh_start_of_rib': 4}},
                                                                                           'refresh_epoch': 7,
                                                                                           'refresh_in': 19,
                                                                                           'refresh_out': 72,
                                                                                           'slow_peer_detection': False,
                                                                                           'slow_peer_split_update_group_dynamic': False,
                                                                                           'update_group_member': 1954}},
                                                      'bgp_event_timer': {'next': {'ackhold': '0x0',
                                                                                   'deadwait': '0x0',
                                                                                   'giveup': '0x0',
                                                                                   'keepalive': '0x0',
                                                                                   'linger': '0x0',
                                                                                   'pmtuager': '0x0',
                                                                                   'processq': '0x0',
                                                                                   'retrans': '0x0',
                                                                                   'sendwnd': '0x0',
                                                                                   'timewait': '0x0'},
                                                                          'starts': {'ackhold': 137871,
                                                                                     'deadwait': 0,
                                                                                     'giveup': 0,
                                                                                     'keepalive': 0,
                                                                                     'linger': 0,
                                                                                     'pmtuager': 1,
                                                                                     'processq': 0,
                                                                                     'retrans': 55014,
                                                                                     'sendwnd': 8,
                                                                                     'timewait': 0},
                                                                          'wakeups': {'ackhold': 6940,
                                                                                      'deadwait': 0,
                                                                                      'giveup': 0,
                                                                                      'keepalive': 0,
                                                                                      'linger': 0,
                                                                                      'pmtuager': 1,
                                                                                      'processq': 0,
                                                                                      'retrans': 14,
                                                                                      'sendwnd': 0,
                                                                                      'timewait': 0}},
                                                                                      'bgp_neighbor_session': {
                                                                                        'sessions': 1,
                                                                                        },
                                                      'bgp_negotiated_capabilities': {'enhanced_refresh': 'advertised '
                                                                                                          'and '
                                                                                                          'received',
                                                                                      'four_octets_asn': 'advertised '
                                                                                                         'and '
                                                                                                         'received',
                                                                                      'graceful_restart': 'advertised '
                                                                                                          'and '
                                                                                                          'received',
                                                                                      'graceful_restart_af_advertised_by_peer': ['vpnv4 '
                                                                                                                                 'unicast',
                                                                                                                                 'l2vpn '
                                                                                                                                 'vpls'],
                                                                                      'l2vpn_vpls': 'advertised '
                                                                                                    'and '
                                                                                                    'received',
                                                                                      'remote_restart_timer': 120,
                                                                                      'route_refresh': 'advertised '
                                                                                                       'and '
                                                                                                       'received(new)',
                                                                                      'stateful_switchover': 'NO '
                                                                                                             'for '
                                                                                                             'session '
                                                                                                             '1',
                                                                                      'vpnv4_unicast': 'advertised '
                                                                                                       'and '
                                                                                                       'received'},
                                                      'bgp_negotiated_keepalive_timers': {'hold_time': 90,
                                                                                          'keepalive_interval': 30,
                                                                                          'min_holdtime': 15},
                                                      'bgp_neighbor_counters': {'messages': {'in_queue_depth': 0,
                                                                                             'out_queue_depth': 0,
                                                                                             'received': {'keepalives': 4709,
                                                                                                          'notifications': 0,
                                                                                                          'opens': 1,
                                                                                                          'route_refresh': 0,
                                                                                                          'total': 127376,
                                                                                                          'updates': 122642},
                                                                                             'sent': {'keepalives': 5188,
                                                                                                      'notifications': 0,
                                                                                                      'opens': 1,
                                                                                                      'route_refresh': 10,
                                                                                                      'total': 55036,
                                                                                                      'updates': 49825}}},
                                                      'bgp_session_transport': {'ack_hold': 200,
                                                                                'address_tracking_status': 'enabled',
                                                                                'connection': {'dropped': 3,
                                                                                               'established': 4,
                                                                                               'last_reset': '1d16h',
                                                                                               'reset_reason': 'Neighbor '
                                                                                                               'reset'},
                                                                                'connection_state': 'estab',
                                                                                'connection_tableid': 0,
                                                                                'datagram': {'datagram_received': {'out_of_order': 0,
                                                                                                                   'total_data': 322194190,
                                                                                                                   'value': 392625,
                                                                                                                   'with_data': 254123},
                                                                                             'datagram_sent': {'fastretransmit': 1992,
                                                                                                               'partialack': 1067,
                                                                                                               'retransmit': 22,
                                                                                                               'second_congestion': 0,
                                                                                                               'total_data': 131166632,
                                                                                                               'value': 434376,
                                                                                                               'with_data': 102975}},
                                                                                'delrcvwnd': 741,
                                                                                'ecn_connection': 'disabled',
                                                                                'enqueued_packets': {'input_packet': 0,
                                                                                                     'mis_ordered_packet': 0,
                                                                                                     'retransmit_packet': 0},
                                                                                'fast_lock_acquisition_failures': 0,
                                                                                'gr_restart_time': 120,
                                                                                'gr_stalepath_time': 360,
                                                                                'graceful_restart': 'enabled',
                                                                                'io_status': 1,
                                                                                'ip_precedence_value': 6,
                                                                                'irs': 3539951191,
                                                                                'iss': 61822047,
                                                                                'krtt': 0,
                                                                                'lock_slow_path': 0,
                                                                                'max_rtt': 1019,
                                                                                'maximum_output_segment_queue_size': 50,
                                                                                'maxrcvwnd': 16384,
                                                                                'min_rtt': 0,
                                                                                'min_time_between_advertisement_runs': 0,
                                                                                'minimum_incoming_ttl': 0,
                                                                                'option_flags': 'nagle, '
                                                                                                'path '
                                                                                                'mtu '
                                                                                                'capable',
                                                                                'outgoing_ttl': 255,
                                                                                'packet_fast_path': 0,
                                                                                'packet_fast_processed': 0,
                                                                                'packet_slow_path': 0,
                                                                                'rcv_scale': 0,
                                                                                'rcvnxt': 3862145382,
                                                                                'rcvwnd': 15643,
                                                                                'receive_idletime': 15525,
                                                                                'rib_route_ip': '192.168.165.119',
                                                                                'rtto': 1003,
                                                                                'rtv': 3,
                                                                                'sent_idletime': 15727,
                                                                                'snd_scale': 0,
                                                                                'sndnxt': 190308893,
                                                                                'snduna': 190308893,
                                                                                'sndwnd': 15510,
                                                                                'srtt': 1000,
                                                                                'sso': False,
                                                                                'status_flags': 'active '
                                                                                                'open',
                                                                                'tcp_path_mtu_discovery': 'enabled',
                                                                                'tcp_semaphore': '0x7FDE7F22E108',
                                                                                'tcp_semaphore_status': 'FREE',
                                                                                'transport': {'foreign_host': '192.168.165.119',
                                                                                              'foreign_port': '179',
                                                                                              'local_host': '10.169.197.254',
                                                                                              'local_port': '13427',
                                                                                              'mss': 1400},
                                                                                'unread_input_bytes': 0,
                                                                                'uptime': 144452788},
                                                      'bgp_version': 4,
                                                      'link': 'internal',
                                                      'remote_as': 5918,
                                                      'router_id': '192.168.165.119',
                                                      'session_state': 'Established',
                                                      'shutdown': False}}}}}

    golden_output3 = {'execute.return_value': '''
        Router#show bgp l2vpn vpls all neighbors 192.168.165.119
        Load for five secs: 4%/0%; one minute: 5%; five minutes: 4%
        Time source is NTP, 16:31:13.822 EST Tue Jun 8 2016

        BGP neighbor is 192.168.165.119,  remote AS 5918, internal link
          BGP version 4, remote router ID 192.168.165.119
          BGP state = Established, up for 1d16h
          Last read 00:00:23, last write 00:00:15, hold time is 90, keepalive interval is 30 seconds
          Configured hold time is 90, keepalive interval is 30 seconds
          Minimum holdtime from neighbor is 15 seconds
          Neighbor sessions:
            1 active, is not multisession capable (disabled)
          Neighbor capabilities:
            Route refresh: advertised and received(new)
            Four-octets ASN Capability: advertised and received
            Address family VPNv4 Unicast: advertised and received
            Address family L2VPN Vpls: advertised and received
            Graceful Restart Capability: advertised and received
              Remote Restart timer is 120 seconds
              Address families advertised by peer:
                VPNv4 Unicast (was not preserved, L2VPN Vpls (was not preserved
            Enhanced Refresh Capability: advertised and received
            Multisession Capability: 
            Stateful switchover support enabled: NO for session 1
          Message statistics:
            InQ depth is 0
            OutQ depth is 0
            
                                 Sent       Rcvd
            Opens:                  1          1
            Notifications:          0          0
            Updates:            49825     122642
            Keepalives:          5188       4709
            Route Refresh:         10          0
            Total:              55036     127376
          Do log neighbor state changes (via global configuration)
          Default minimum time between advertisement runs is 0 seconds

         For address family: VPNv4 Unicast
          BGP diverse-paths computation is enabled 
          Session: 192.168.165.119
          BGP table version 33086714, neighbor version 33086714/0
          Output queue size : 0
          Index 1954, Advertise bit 0
          1954 update-group member
          Community attribute sent to this neighbor
          Extended-community attribute sent to this neighbor
          Slow-peer detection is disabled
          Slow-peer split-update-group dynamic is disabled
                                         Sent       Rcvd
          Prefix activity:               ----       ----
            Prefixes Current:           10202    2001899 (Consumes 240672000 bytes)
            Prefixes Total:            131522   16316598
            Implicit Withdraw:          81710   10255632
            Explicit Withdraw:        2045210    4059067
            Used as bestpath:             n/a    2005600
            Used as multipath:            n/a          0

                                           Outbound    Inbound
          Local Policy Denied Prefixes:    --------    -------
            ORIGINATOR loop:                    n/a     151495
            Bestpath from this peer:       10473918        n/a
            Bestpath from iBGP peer:        3488082        n/a
            AF Permit Check:                  84090        n/a
            AF Update Check:                  11509        n/a
            Total:                         14057599     151495
          Number of NLRIs in the update sent: max 270, min 0
          Last detected as dynamic slow peer: never
          Dynamic slow peer recovered: never
          Refresh Epoch: 7
          Last Sent Refresh Start-of-rib: 04:52:13
          Last Sent Refresh End-of-rib: 04:51:01
          Refresh-Out took 72 seconds
          Last Received Refresh Start-of-rib: 21:35:11
          Last Received Refresh End-of-rib: 21:34:52
          Refresh-In took 19 seconds
                               Sent   Rcvd
            Refresh activity:          ----   ----
              Refresh Start-of-RIB          4          6
              Refresh End-of-RIB            4          6

         For address family: L2VPN Vpls
          Session: 192.168.165.119
          BGP table version 403, neighbor version 403/0
          Output queue size : 0
          Index 4, Advertise bit 0
          4 update-group member
          Extended-community attribute sent to this neighbor
          Suppress LDP signaling protocol
          Slow-peer detection is disabled
          Slow-peer split-update-group dynamic is disabled
                                         Sent       Rcvd
          Prefix activity:               ----       ----
            Prefixes Current:             201        201 (Consumes 27336 bytes)
            Prefixes Total:              1809       1206
            Implicit Withdraw:           1608       1005
            Explicit Withdraw:              0          0
            Used as bestpath:             n/a        201
            Used as multipath:            n/a          0

                                           Outbound    Inbound
          Local Policy Denied Prefixes:    --------    -------
            ORIGINATOR loop:                    n/a       1206
            Bestpath from this peer:           1407        n/a
            Total:                             1407       1206
          Number of NLRIs in the update sent: max 1, min 0
          Last detected as dynamic slow peer: never
          Dynamic slow peer recovered: never
          Refresh Epoch: 7
          Last Sent Refresh Start-of-rib: 04:52:13
          Last Sent Refresh End-of-rib: 04:52:13
          Refresh-Out took 0 seconds
          Last Received Refresh Start-of-rib: 21:35:11
          Last Received Refresh End-of-rib: 21:35:10
          Refresh-In took 1 seconds
                               Sent   Rcvd
            Refresh activity:          ----   ----
              Refresh Start-of-RIB          2          6
              Refresh End-of-RIB            2          6

          Address tracking is enabled, the RIB does have a route to 192.168.165.119
          Connections established 4; dropped 3
          Last reset 1d16h, due to Neighbor reset
          Interface associated: (none) (peering address NOT in same link)
          Transport(tcp) path-mtu-discovery is enabled
          Graceful-Restart is enabled, restart-time 120 seconds, stalepath-time 360 seconds
          SSO is disabled
        Connection state is ESTAB, I/O status: 1, unread input bytes: 0            
        Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 255
        Local host: 10.169.197.254, Local port: 13427
        Foreign host: 192.168.165.119, Foreign port: 179
        Connection tableid (VRF): 0
        Maximum output segment queue size: 50

        Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

        Event Timers (current time is 0x233AE2F9):
        Timer          Starts    Wakeups            Next
        Retrans         55014         14             0x0
        TimeWait            0          0             0x0
        AckHold        137871       6940             0x0
        SendWnd             8          0             0x0
        KeepAlive           0          0             0x0
        GiveUp              0          0             0x0
        PmtuAger            1          1             0x0
        DeadWait            0          0             0x0
        Linger              0          0             0x0
        ProcessQ            0          0             0x0

        iss:   61822047  snduna:  190308893  sndnxt:  190308893
        irs: 3539951191  rcvnxt: 3862145382

        sndwnd:  15510  scale:      0  maxrcvwnd:  16384
        rcvwnd:  15643  scale:      0  delrcvwnd:    741

        SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
        minRTT: 0 ms, maxRTT: 1019 ms, ACK hold: 200 ms
        uptime: 144452788 ms, Sent idletime: 15727 ms, Receive idletime: 15525 ms 
        Status Flags: active open
        Option Flags: nagle, path mtu capable
        IP Precedence value : 6

        Datagrams (max data segment is 1400 bytes):
        Rcvd: 392625 (out of order: 0), with data: 254123, total data bytes: 322194190
        Sent: 434376 (retransmit: 22, fastretransmit: 1992, partialack: 1067, Second Congestion: 0), with data: 102975, total data bytes: 131166632

         Packets received in fast path: 0, fast processed: 0, slow path: 0
         fast lock acquisition failures: 0, slow path: 0
        TCP Semaphore      0x7FDE7F22E108  FREE 
        Router#
        '''}

    golden_parsed_output4 = {
        'list_of_neighbors': [
            '10.16.2.2',
            '10.36.3.3',
            '10.4.6.6',
            '10.66.6.6',
            '10.64.4.4',
            '10.100.5.5',
            '2001:DB8:4:6::6',
            '2001:DB8:20:4:6::6'
        ],
        'vrf': {
            'default': {
                'neighbor': {
                    '10.16.2.2': {
                        'remote_as': 100,
                        'link': 'internal',
                        'shutdown': False,
                        'address_family': {
                            'vpnv4 unicast': {
                                'session_state': 'Established',
                                'up_time': '01:10:35',
                                'last_read': '00:00:04',
                                'last_write': '00:00:09',
                                'current_time': '0x530449'
                            }
                        },
                        'bgp_version': 4,
                        'router_id': '10.16.2.2',
                        'session_state': 'Established',
                        'bgp_negotiated_keepalive_timers': {
                            'hold_time': 180,
                            'keepalive_interval': 60
                        },
                        'bgp_neighbor_session': {
                            'sessions': 1,
                            },
                        'bgp_negotiated_capabilities': {
                            'route_refresh': 'advertised and received(new)',
                            'four_octets_asn': 'advertised and received',
                            'vpnv4_unicast': 'advertised and received',
                            'vpnv6_unicast': 'advertised and received',
                            'graceful_restart': 'received',
                            'remote_restart_timer': 120,
                            'graceful_restart_af_advertised_by_peer': [
                                'vpnv4 unicast',
                                'vpnv6 unicast'
                            ],
                            'enhanced_refresh': 'advertised',
                            'stateful_switchover': 'NO for session 1'
                        },
                        'bgp_neighbor_counters': {
                            'messages': {
                                'sent': {
                                    'opens': 1,
                                    'notifications': 0,
                                    'updates': 11,
                                    'keepalives': 75,
                                    'route_refresh': 0,
                                    'total': 87
                                },
                                'received': {
                                    'opens': 1,
                                    'notifications': 0,
                                    'updates': 6,
                                    'keepalives': 74,
                                    'route_refresh': 0,
                                    'total': 81
                                },
                                'in_queue_depth': 0,
                                'out_queue_depth': 0
                            }
                        },
                        'bgp_session_transport': {
                            'min_time_between_advertisement_runs': 0,
                            'address_tracking_status': 'enabled',
                            'rib_route_ip': '10.16.2.2',
                            'connection': {
                                'established': 1,
                                'dropped': 0,
                                'last_reset': 'never'
                            },
                            'tcp_path_mtu_discovery': 'enabled',
                            'graceful_restart': 'disabled',
                            'connection_state': 'estab',
                            'io_status': 1,
                            'unread_input_bytes': 0,
                            'ecn_connection': 'disabled',
                            'minimum_incoming_ttl': 0,
                            'outgoing_ttl': 255,
                            'transport': {
                                'local_host': '10.64.4.4',
                                'local_port': '35281',
                                'foreign_host': '10.16.2.2',
                                'foreign_port': '179',
                                'mss': 536
                            },
                            'connection_tableid': 0,
                            'maximum_output_segment_queue_size': 50,
                            'enqueued_packets': {
                                'retransmit_packet': 0,
                                'input_packet': 0,
                                'mis_ordered_packet': 0
                            },
                            'iss': 55023811,
                            'snduna': 55027115,
                            'sndnxt': 55027115,
                            'irs': 109992783,
                            'rcvnxt': 109995158,
                            'sndwnd': 16616,
                            'snd_scale': 0,
                            'maxrcvwnd': 16384,
                            'rcvwnd': 16327,
                            'rcv_scale': 0,
                            'delrcvwnd': 57,
                            'srtt': 1000,
                            'rtto': 1003,
                            'rtv': 3,
                            'krtt': 0,
                            'min_rtt': 4,
                            'max_rtt': 1000,
                            'ack_hold': 200,
                            'uptime': 4236258,
                            'sent_idletime': 4349,
                            'receive_idletime': 4549,
                            'status_flags': 'active open',
                            'option_flags': 'nagle, path mtu capable',
                            'ip_precedence_value': 6,
                            'datagram': {
                                'datagram_received': {
                                    'value': 164,
                                    'out_of_order': 0,
                                    'with_data': 80,
                                    'total_data': 2374
                                },
                                'datagram_sent': {
                                    'value': 166,
                                    'retransmit': 0,
                                    'fastretransmit': 0,
                                    'partialack': 0,
                                    'second_congestion': 0,
                                    'with_data': 87,
                                    'total_data': 3303
                                }
                            },
                            'packet_fast_path': 0,
                            'packet_fast_processed': 0,
                            'packet_slow_path': 0,
                            'fast_lock_acquisition_failures': 0,
                            'lock_slow_path': 0,
                            'tcp_semaphore': '0x1286E7EC',
                            'tcp_semaphore_status': 'FREE'
                        },
                        'bgp_event_timer': {
                            'starts': {
                                'retrans': 86,
                                'timewait': 0,
                                'ackhold': 80,
                                'sendwnd': 0,
                                'keepalive': 0,
                                'giveup': 0,
                                'pmtuager': 1,
                                'deadwait': 0,
                                'linger': 0,
                                'processq': 0
                            },
                            'wakeups': {
                                'retrans': 0,
                                'timewait': 0,
                                'ackhold': 72,
                                'sendwnd': 0,
                                'keepalive': 0,
                                'giveup': 0,
                                'pmtuager': 1,
                                'deadwait': 0,
                                'linger': 0,
                                'processq': 0
                            },
                            'next': {
                                'retrans': '0x0',
                                'timewait': '0x0',
                                'ackhold': '0x0',
                                'sendwnd': '0x0',
                                'keepalive': '0x0',
                                'giveup': '0x0',
                                'pmtuager': '0x0',
                                'deadwait': '0x0',
                                'linger': '0x0',
                                'processq': '0x0'
                            }
                        }
                    },
                    '10.36.3.3': {
                        'remote_as': 100,
                        'link': 'internal',
                        'shutdown': False,
                        'address_family': {
                            'vpnv4 unicast': {
                                'session_state': 'Established',
                                'up_time': '01:10:41',
                                'last_read': '00:00:04',
                                'last_write': '00:00:43',
                                'current_time': '0x530638'
                            }
                        },
                        'bgp_version': 4,
                        'router_id': '10.36.3.3',
                        'session_state': 'Established',
                        'bgp_negotiated_keepalive_timers': {
                            'hold_time': 180,
                            'keepalive_interval': 60
                        },
                        'bgp_neighbor_session': {
                            'sessions': 1,
                            },
                        'bgp_negotiated_capabilities': {
                            'route_refresh': 'advertised and received(new)',
                            'four_octets_asn': 'advertised and received',
                            'vpnv4_unicast': 'advertised and received',
                            'vpnv6_unicast': 'advertised and received',
                            'graceful_restart': 'received',
                            'remote_restart_timer': 120,
                            'graceful_restart_af_advertised_by_peer': [
                                'vpnv4 unicast',
                                'vpnv6 unicast'
                            ],
                            'enhanced_refresh': 'advertised',
                            'stateful_switchover': 'NO for session 1'
                        },
                        'bgp_neighbor_counters': {
                            'messages': {
                                'sent': {
                                    'opens': 1,
                                    'notifications': 0,
                                    'updates': 11,
                                    'keepalives': 75,
                                    'route_refresh': 0,
                                    'total': 87
                                },
                                'received': {
                                    'opens': 1,
                                    'notifications': 0,
                                    'updates': 6,
                                    'keepalives': 74,
                                    'route_refresh': 0,
                                    'total': 81
                                },
                                'in_queue_depth': 0,
                                'out_queue_depth': 0
                            }
                        },
                        'bgp_session_transport': {
                            'min_time_between_advertisement_runs': 0,
                            'address_tracking_status': 'enabled',
                            'rib_route_ip': '10.36.3.3',
                            'connection': {
                                'established': 1,
                                'dropped': 0,
                                'last_reset': 'never'
                            },
                            'tcp_path_mtu_discovery': 'enabled',
                            'graceful_restart': 'disabled',
                            'connection_state': 'estab',
                            'io_status': 1,
                            'unread_input_bytes': 0,
                            'ecn_connection': 'disabled',
                            'minimum_incoming_ttl': 0,
                            'outgoing_ttl': 255,
                            'transport': {
                                'local_host': '10.64.4.4',
                                'local_port': '56031',
                                'foreign_host': '10.36.3.3',
                                'foreign_port': '179',
                                'mss': 536
                            },
                            'connection_tableid': 0,
                            'maximum_output_segment_queue_size': 50,
                            'enqueued_packets': {
                                'retransmit_packet': 0,
                                'input_packet': 0,
                                'mis_ordered_packet': 0
                            },
                            'iss': 2116369173,
                            'snduna': 2116372477,
                            'sndnxt': 2116372477,
                            'irs': 4033842748,
                            'rcvnxt': 4033845123,
                            'sndwnd': 16616,
                            'snd_scale': 0,
                            'maxrcvwnd': 16384,
                            'rcvwnd': 16327,
                            'rcv_scale': 0,
                            'delrcvwnd': 57,
                            'srtt': 1000,
                            'rtto': 1003,
                            'rtv': 3,
                            'krtt': 0,
                            'min_rtt': 3,
                            'max_rtt': 1000,
                            'ack_hold': 200,
                            'uptime': 4243393,
                            'sent_idletime': 5375,
                            'receive_idletime': 5575,
                            'status_flags': 'active open',
                            'option_flags': 'nagle, path mtu capable',
                            'ip_precedence_value': 6,
                            'datagram': {
                                'datagram_received': {
                                    'value': 165,
                                    'out_of_order': 0,
                                    'with_data': 80,
                                    'total_data': 2374
                                },
                                'datagram_sent': {
                                    'value': 167,
                                    'retransmit': 0,
                                    'fastretransmit': 0,
                                    'partialack': 0,
                                    'second_congestion': 0,
                                    'with_data': 87,
                                    'total_data': 3303
                                }
                            },
                            'packet_fast_path': 0,
                            'packet_fast_processed': 0,
                            'packet_slow_path': 0,
                            'fast_lock_acquisition_failures': 0,
                            'lock_slow_path': 0,
                            'tcp_semaphore': '0x1286E85C',
                            'tcp_semaphore_status': 'FREE'
                        },
                        'bgp_event_timer': {
                            'starts': {
                                'retrans': 86,
                                'timewait': 0,
                                'ackhold': 80,
                                'sendwnd': 0,
                                'keepalive': 0,
                                'giveup': 0,
                                'pmtuager': 1,
                                'deadwait': 0,
                                'linger': 0,
                                'processq': 0
                            },
                            'wakeups': {
                                'retrans': 0,
                                'timewait': 0,
                                'ackhold': 73,
                                'sendwnd': 0,
                                'keepalive': 0,
                                'giveup': 0,
                                'pmtuager': 1,
                                'deadwait': 0,
                                'linger': 0,
                                'processq': 0
                            },
                            'next': {
                                'retrans': '0x0',
                                'timewait': '0x0',
                                'ackhold': '0x0',
                                'sendwnd': '0x0',
                                'keepalive': '0x0',
                                'giveup': '0x0',
                                'pmtuager': '0x0',
                                'deadwait': '0x0',
                                'linger': '0x0',
                                'processq': '0x0'
                            }
                        }
                    },
                    '10.64.4.4': {
                        'remote_as': 100,
                        'link': 'internal',
                        'shutdown': False,
                        'address_family': {
                            'vpnv6 unicast': {
                                'session_state': 'Established',
                                'up_time': '01:10:38',
                                'last_read': '00:00:07',
                                'last_write': '00:00:12',
                                'current_time': '0x530FF5'
                            }
                        },
                        'description': 'router2222222',
                        'bgp_version': 4,
                        'router_id': '10.64.4.4',
                        'session_state': 'Established',
                        'bgp_negotiated_keepalive_timers': {
                            'hold_time': 180,
                            'keepalive_interval': 60
                        },
                        'bgp_neighbor_session': {
                            'sessions': 1,
                            },
                        'bgp_negotiated_capabilities': {
                            'route_refresh': 'advertised and received(new)',
                            'four_octets_asn': 'advertised and received',
                            'vpnv4_unicast': 'advertised and received',
                            'vpnv6_unicast': 'advertised and received',
                            'graceful_restart': 'received',
                            'remote_restart_timer': 120,
                            'graceful_restart_af_advertised_by_peer': [
                                'vpnv4 unicast',
                                'vpnv6 unicast'
                            ],
                            'enhanced_refresh': 'advertised',
                            'stateful_switchover': 'NO for session 1'
                        },
                        'bgp_neighbor_counters': {
                            'messages': {
                                'sent': {
                                    'opens': 1,
                                    'notifications': 0,
                                    'updates': 11,
                                    'keepalives': 75,
                                    'route_refresh': 0,
                                    'total': 87
                                },
                                'received': {
                                    'opens': 1,
                                    'notifications': 0,
                                    'updates': 6,
                                    'keepalives': 74,
                                    'route_refresh': 0,
                                    'total': 81
                                },
                                'in_queue_depth': 0,
                                'out_queue_depth': 0
                            }
                        },
                        'bgp_session_transport': {
                            'min_time_between_advertisement_runs': 0,
                            'address_tracking_status': 'enabled',
                            'rib_route_ip': '10.16.2.2',
                            'connection': {
                                'established': 1,
                                'dropped': 0,
                                'last_reset': 'never'
                            },
                            'tcp_path_mtu_discovery': 'enabled',
                            'graceful_restart': 'disabled',
                            'connection_state': 'estab',
                            'io_status': 1,
                            'unread_input_bytes': 0,
                            'ecn_connection': 'disabled',
                            'minimum_incoming_ttl': 0,
                            'outgoing_ttl': 255,
                            'transport': {
                                'local_host': '10.64.4.4',
                                'local_port': '35281',
                                'foreign_host': '10.16.2.2',
                                'foreign_port': '179',
                                'mss': 536
                            },
                            'connection_tableid': 0,
                            'maximum_output_segment_queue_size': 50,
                            'enqueued_packets': {
                                'retransmit_packet': 0,
                                'input_packet': 0,
                                'mis_ordered_packet': 0
                            },
                            'iss': 55023811,
                            'snduna': 55027115,
                            'sndnxt': 55027115,
                            'irs': 109992783,
                            'rcvnxt': 109995158,
                            'sndwnd': 16616,
                            'snd_scale': 0,
                            'maxrcvwnd': 16384,
                            'rcvwnd': 16327,
                            'rcv_scale': 0,
                            'delrcvwnd': 57,
                            'srtt': 1000,
                            'rtto': 1003,
                            'rtv': 3,
                            'krtt': 0,
                            'min_rtt': 4,
                            'max_rtt': 1000,
                            'ack_hold': 200,
                            'uptime': 4239741,
                            'sent_idletime': 7832,
                            'receive_idletime': 8032,
                            'status_flags': 'active open',
                            'option_flags': 'nagle, path mtu capable',
                            'ip_precedence_value': 6,
                            'datagram': {
                                'datagram_received': {
                                    'value': 164,
                                    'out_of_order': 0,
                                    'with_data': 80,
                                    'total_data': 2374
                                },
                                'datagram_sent': {
                                    'value': 166,
                                    'retransmit': 0,
                                    'fastretransmit': 0,
                                    'partialack': 0,
                                    'second_congestion': 0,
                                    'with_data': 87,
                                    'total_data': 3303
                                }
                            },
                            'packet_fast_path': 0,
                            'packet_fast_processed': 0,
                            'packet_slow_path': 0,
                            'fast_lock_acquisition_failures': 0,
                            'lock_slow_path': 0,
                            'tcp_semaphore': '0x1286E7EC',
                            'tcp_semaphore_status': 'FREE'
                        },
                        'bgp_event_timer': {
                            'starts': {
                                'retrans': 86,
                                'timewait': 0,
                                'ackhold': 80,
                                'sendwnd': 0,
                                'keepalive': 0,
                                'giveup': 0,
                                'pmtuager': 1,
                                'deadwait': 0,
                                'linger': 0,
                                'processq': 0
                            },
                            'wakeups': {
                                'retrans': 0,
                                'timewait': 0,
                                'ackhold': 72,
                                'sendwnd': 0,
                                'keepalive': 0,
                                'giveup': 0,
                                'pmtuager': 1,
                                'deadwait': 0,
                                'linger': 0,
                                'processq': 0
                            },
                            'next': {
                                'retrans': '0x0',
                                'timewait': '0x0',
                                'ackhold': '0x0',
                                'sendwnd': '0x0',
                                'keepalive': '0x0',
                                'giveup': '0x0',
                                'pmtuager': '0x0',
                                'deadwait': '0x0',
                                'linger': '0x0',
                                'processq': '0x0'
                            }
                        }
                    },
                    '10.100.5.5': {
                        'remote_as': 100,
                        'link': 'internal',
                        'shutdown': False,
                        'address_family': {
                            'vpnv6 unicast': {
                                'session_state': 'Established',
                                'up_time': '01:10:44',
                                'last_read': '00:00:08',
                                'last_write': '00:00:47',
                                'current_time': '0x5313D8'
                            }
                        },
                        'bgp_version': 4,
                        'router_id': '10.100.5.5',
                        'session_state': 'Established',
                        'bgp_negotiated_keepalive_timers': {
                            'hold_time': 180,
                            'keepalive_interval': 60
                        },
                        'bgp_neighbor_session': {
                            'sessions': 1,
                            },
                        'bgp_negotiated_capabilities': {
                            'route_refresh': 'advertised and received(new)',
                            'four_octets_asn': 'advertised and received',
                            'vpnv4_unicast': 'advertised and received',
                            'vpnv6_unicast': 'advertised and received',
                            'graceful_restart': 'received',
                            'remote_restart_timer': 120,
                            'graceful_restart_af_advertised_by_peer': [
                                'vpnv4 unicast',
                                'vpnv6 unicast'
                            ],
                            'enhanced_refresh': 'advertised',
                            'stateful_switchover': 'NO for session 1'
                        },
                        'bgp_neighbor_counters': {
                            'messages': {
                                'sent': {
                                    'opens': 1,
                                    'notifications': 0,
                                    'updates': 11,
                                    'keepalives': 75,
                                    'route_refresh': 0,
                                    'total': 87
                                },
                                'received': {
                                    'opens': 1,
                                    'notifications': 0,
                                    'updates': 6,
                                    'keepalives': 74,
                                    'route_refresh': 0,
                                    'total': 81
                                },
                                'in_queue_depth': 0,
                                'out_queue_depth': 0
                            }
                        },
                        'bgp_session_transport': {
                            'min_time_between_advertisement_runs': 0,
                            'address_tracking_status': 'enabled',
                            'rib_route_ip': '10.36.3.3',
                            'connection': {
                                'established': 1,
                                'dropped': 0,
                                'last_reset': 'never'
                            },
                            'tcp_path_mtu_discovery': 'enabled',
                            'graceful_restart': 'disabled',
                            'connection_state': 'estab',
                            'io_status': 1,
                            'unread_input_bytes': 0,
                            'ecn_connection': 'disabled',
                            'minimum_incoming_ttl': 0,
                            'outgoing_ttl': 255,
                            'transport': {
                                'local_host': '10.64.4.4',
                                'local_port': '56031',
                                'foreign_host': '10.36.3.3',
                                'foreign_port': '179',
                                'mss': 536
                            },
                            'connection_tableid': 0,
                            'maximum_output_segment_queue_size': 50,
                            'enqueued_packets': {
                                'retransmit_packet': 0,
                                'input_packet': 0,
                                'mis_ordered_packet': 0
                            },
                            'iss': 2116369173,
                            'snduna': 2116372477,
                            'sndnxt': 2116372477,
                            'irs': 4033842748,
                            'rcvnxt': 4033845123,
                            'sndwnd': 16616,
                            'snd_scale': 0,
                            'maxrcvwnd': 16384,
                            'rcvwnd': 16327,
                            'rcv_scale': 0,
                            'delrcvwnd': 57,
                            'srtt': 1000,
                            'rtto': 1003,
                            'rtv': 3,
                            'krtt': 0,
                            'min_rtt': 3,
                            'max_rtt': 1000,
                            'ack_hold': 200,
                            'uptime': 4246385,
                            'sent_idletime': 8367,
                            'receive_idletime': 8567,
                            'status_flags': 'active open',
                            'option_flags': 'nagle, path mtu capable',
                            'ip_precedence_value': 6,
                            'datagram': {
                                'datagram_received': {
                                    'value': 165,
                                    'out_of_order': 0,
                                    'with_data': 80,
                                    'total_data': 2374
                                },
                                'datagram_sent': {
                                    'value': 167,
                                    'retransmit': 0,
                                    'fastretransmit': 0,
                                    'partialack': 0,
                                    'second_congestion': 0,
                                    'with_data': 87,
                                    'total_data': 3303
                                }
                            },
                            'packet_fast_path': 0,
                            'packet_fast_processed': 0,
                            'packet_slow_path': 0,
                            'fast_lock_acquisition_failures': 0,
                            'lock_slow_path': 0,
                            'tcp_semaphore': '0x1286E85C',
                            'tcp_semaphore_status': 'FREE'
                        },
                        'bgp_event_timer': {
                            'starts': {
                                'retrans': 86,
                                'timewait': 0,
                                'ackhold': 80,
                                'sendwnd': 0,
                                'keepalive': 0,
                                'giveup': 0,
                                'pmtuager': 1,
                                'deadwait': 0,
                                'linger': 0,
                                'processq': 0
                            },
                            'wakeups': {
                                'retrans': 0,
                                'timewait': 0,
                                'ackhold': 73,
                                'sendwnd': 0,
                                'keepalive': 0,
                                'giveup': 0,
                                'pmtuager': 1,
                                'deadwait': 0,
                                'linger': 0,
                                'processq': 0
                            },
                            'next': {
                                'retrans': '0x0',
                                'timewait': '0x0',
                                'ackhold': '0x0',
                                'sendwnd': '0x0',
                                'keepalive': '0x0',
                                'giveup': '0x0',
                                'pmtuager': '0x0',
                                'deadwait': '0x0',
                                'linger': '0x0',
                                'processq': '0x0'
                            }
                        }
                    }
                }
            },
            'VRF1': {
                'neighbor': {
                    '10.4.6.6': {
                        'remote_as': 300,
                        'link': 'external',
                        'shutdown': True,
                        'address_family': {
                            'vpnv4 unicast': {
                                'session_state': 'Established',
                                'up_time': '01:01:59',
                                'last_read': '00:00:33',
                                'last_write': '00:00:30',
                                'current_time': '0x530A19'
                            }
                        },
                        'bgp_version': 4,
                        'router_id': '10.4.6.6',
                        'session_state': 'Established',
                        'bgp_negotiated_keepalive_timers': {
                            'hold_time': 180,
                            'keepalive_interval': 60
                        },
                        'bgp_neighbor_session': {
                            'sessions': 1,
                            },
                        'bgp_negotiated_capabilities': {
                            'route_refresh': 'advertised',
                            'four_octets_asn': 'advertised',
                            'ipv4_unicast': 'advertised and received',
                            'enhanced_refresh': 'advertised',
                            'stateful_switchover': 'NO for session 1'
                        },
                        'bgp_neighbor_counters': {
                            'messages': {
                                'sent': {
                                    'opens': 1,
                                    'notifications': 0,
                                    'updates': 3,
                                    'keepalives': 69,
                                    'route_refresh': 0,
                                    'total': 73
                                },
                                'received': {
                                    'opens': 1,
                                    'notifications': 0,
                                    'updates': 1,
                                    'keepalives': 64,
                                    'route_refresh': 0,
                                    'total': 66
                                },
                                'in_queue_depth': 0,
                                'out_queue_depth': 0
                            }
                        },
                        'bgp_session_transport': {
                            'min_time_between_advertisement_runs': 0,
                            'address_tracking_status': 'enabled',
                            'rib_route_ip': '10.4.6.6',
                            'connection': {
                                'established': 2,
                                'dropped': 1,
                                'last_reset': '01:02:11',
                                'reset_reason': 'Peer closed the session of session 1'
                            },
                            'tcp_path_mtu_discovery': 'enabled',
                            'graceful_restart': 'disabled',
                            'connection_state': 'estab',
                            'io_status': 1,
                            'unread_input_bytes': 0,
                            'ecn_connection': 'disabled',
                            'minimum_incoming_ttl': 0,
                            'outgoing_ttl': 1,
                            'transport': {
                                'local_host': '10.4.6.4',
                                'local_port': '179',
                                'foreign_host': '10.4.6.6',
                                'foreign_port': '11010',
                                'mss': 1460
                            },
                            'connection_tableid': 1,
                            'maximum_output_segment_queue_size': 50,
                            'enqueued_packets': {
                                'retransmit_packet': 0,
                                'input_packet': 0,
                                'mis_ordered_packet': 0
                            },
                            'iss': 271842,
                            'snduna': 273380,
                            'sndnxt': 273380,
                            'irs': 930048172,
                            'rcvnxt': 930049503,
                            'sndwnd': 32000,
                            'snd_scale': 0,
                            'maxrcvwnd': 16384,
                            'rcvwnd': 15054,
                            'rcv_scale': 0,
                            'delrcvwnd': 1330,
                            'srtt': 1000,
                            'rtto': 1003,
                            'rtv': 3,
                            'krtt': 0,
                            'min_rtt': 1,
                            'max_rtt': 1000,
                            'ack_hold': 200,
                            'uptime': 3720132,
                            'sent_idletime': 31107,
                            'receive_idletime': 30999,
                            'status_flags': 'passive open, gen tcbs',
                            'option_flags': 'VRF id set, nagle, path mtu capable',
                            'ip_precedence_value': 6,
                            'datagram': {
                                'datagram_received': {
                                    'value': 137,
                                    'out_of_order': 0,
                                    'with_data': 66,
                                    'total_data': 1330
                                },
                                'datagram_sent': {
                                    'value': 138,
                                    'retransmit': 0,
                                    'fastretransmit': 0,
                                    'partialack': 0,
                                    'second_congestion': 0,
                                    'with_data': 72,
                                    'total_data': 1537
                                }
                            },
                            'packet_fast_path': 0,
                            'packet_fast_processed': 0,
                            'packet_slow_path': 0,
                            'fast_lock_acquisition_failures': 0,
                            'lock_slow_path': 0,
                            'tcp_semaphore': '0x1286E62C',
                            'tcp_semaphore_status': 'FREE'
                        },
                        'bgp_event_timer': {
                            'starts': {
                                'retrans': 71,
                                'timewait': 0,
                                'ackhold': 66,
                                'sendwnd': 0,
                                'keepalive': 0,
                                'giveup': 0,
                                'pmtuager': 0,
                                'deadwait': 0,
                                'linger': 0,
                                'processq': 0
                            },
                            'wakeups': {
                                'retrans': 0,
                                'timewait': 0,
                                'ackhold': 64,
                                'sendwnd': 0,
                                'keepalive': 0,
                                'giveup': 0,
                                'pmtuager': 0,
                                'deadwait': 0,
                                'linger': 0,
                                'processq': 0
                            },
                            'next': {
                                'retrans': '0x0',
                                'timewait': '0x0',
                                'ackhold': '0x0',
                                'sendwnd': '0x0',
                                'keepalive': '0x0',
                                'giveup': '0x0',
                                'pmtuager': '0x0',
                                'deadwait': '0x0',
                                'linger': '0x0',
                                'processq': '0x0'
                            }
                        }
                    },
                    '2001:DB8:4:6::6': {
                        'remote_as': 300,
                        'link': 'external',
                        'shutdown': False,
                        'address_family': {
                            'vpnv6 unicast': {
                                'session_state': 'Established',
                                'up_time': '01:01:58',
                                'last_read': '00:00:32',
                                'last_write': '00:00:06',
                                'current_time': '0x5315CE'
                            }
                        },
                        'bgp_version': 4,
                        'router_id': '10.4.6.6',
                        'session_state': 'Established',
                        'bgp_negotiated_keepalive_timers': {
                            'hold_time': 180,
                            'keepalive_interval': 60
                        },
                        'bgp_neighbor_session': {
                            'sessions': 1,
                            },
                        'bgp_negotiated_capabilities': {
                            'route_refresh': 'advertised',
                            'four_octets_asn': 'advertised',
                            'ipv6_unicast': 'advertised and received',
                            'enhanced_refresh': 'advertised',
                            'stateful_switchover': 'NO for session 1'
                        },
                        'bgp_neighbor_counters': {
                            'messages': {
                                'sent': {
                                    'opens': 1,
                                    'notifications': 0,
                                    'updates': 3,
                                    'keepalives': 70,
                                    'route_refresh': 0,
                                    'total': 74
                                },
                                'received': {
                                    'opens': 1,
                                    'notifications': 0,
                                    'updates': 1,
                                    'keepalives': 64,
                                    'route_refresh': 0,
                                    'total': 66
                                },
                                'in_queue_depth': 0,
                                'out_queue_depth': 0
                            }
                        },
                        'bgp_session_transport': {
                            'min_time_between_advertisement_runs': 0,
                            'address_tracking_status': 'enabled',
                            'rib_route_ip': '2001:DB8:4:6::6',
                            'connection': {
                                'established': 2,
                                'dropped': 1,
                                'last_reset': '01:05:12',
                                'reset_reason': 'Active open failed'
                            },
                            'tcp_path_mtu_discovery': 'enabled',
                            'graceful_restart': 'disabled',
                            'connection_state': 'estab',
                            'io_status': 1,
                            'unread_input_bytes': 0,
                            'ecn_connection': 'disabled',
                            'minimum_incoming_ttl': 0,
                            'outgoing_ttl': 1,
                            'transport': {
                                'local_host': '2001:DB8:4:6::4',
                                'local_port': '179',
                                'foreign_host': '2001:DB8:4:6::6',
                                'foreign_port': '11003',
                                'mss': 1440
                            },
                            'connection_tableid': 503316481,
                            'maximum_output_segment_queue_size': 50,
                            'enqueued_packets': {
                                'retransmit_packet': 0,
                                'input_packet': 0,
                                'mis_ordered_packet': 0
                            },
                            'iss': 164676617,
                            'snduna': 164678296,
                            'sndnxt': 164678296,
                            'irs': 1797203329,
                            'rcvnxt': 1797204710,
                            'sndwnd': 32000,
                            'snd_scale': 0,
                            'maxrcvwnd': 16384,
                            'rcvwnd': 15004,
                            'rcv_scale': 0,
                            'delrcvwnd': 1380,
                            'srtt': 1000,
                            'rtto': 1003,
                            'rtv': 3,
                            'krtt': 0,
                            'min_rtt': 1,
                            'max_rtt': 1000,
                            'ack_hold': 200,
                            'uptime': 3718683,
                            'sent_idletime': 6954,
                            'receive_idletime': 6849,
                            'status_flags': 'passive open, gen tcbs',
                            'option_flags': 'VRF id set, nagle, path mtu capable',
                            'ip_precedence_value': 6,
                            'datagram': {
                                'datagram_received': {
                                    'value': 138,
                                    'out_of_order': 0,
                                    'with_data': 66,
                                    'total_data': 1380
                                },
                                'datagram_sent': {
                                    'value': 139,
                                    'retransmit': 0,
                                    'fastretransmit': 0,
                                    'partialack': 0,
                                    'second_congestion': 0,
                                    'with_data': 139,
                                    'total_data': 7246
                                }
                            },
                            'packet_fast_path': 0,
                            'packet_fast_processed': 0,
                            'packet_slow_path': 0,
                            'fast_lock_acquisition_failures': 0,
                            'lock_slow_path': 0,
                            'tcp_semaphore': '0x1286E9AC',
                            'tcp_semaphore_status': 'FREE'
                        },
                        'bgp_event_timer': {
                            'starts': {
                                'retrans': 72,
                                'timewait': 0,
                                'ackhold': 66,
                                'sendwnd': 0,
                                'keepalive': 0,
                                'giveup': 0,
                                'pmtuager': 0,
                                'deadwait': 0,
                                'linger': 0,
                                'processq': 0
                            },
                            'wakeups': {
                                'retrans': 0,
                                'timewait': 0,
                                'ackhold': 64,
                                'sendwnd': 0,
                                'keepalive': 0,
                                'giveup': 0,
                                'pmtuager': 0,
                                'deadwait': 0,
                                'linger': 0,
                                'processq': 0
                            },
                            'next': {
                                'retrans': '0x0',
                                'timewait': '0x0',
                                'ackhold': '0x0',
                                'sendwnd': '0x0',
                                'keepalive': '0x0',
                                'giveup': '0x0',
                                'pmtuager': '0x0',
                                'deadwait': '0x0',
                                'linger': '0x0',
                                'processq': '0x0'
                            }
                        }
                    }
                }
            },
            'VRF2': {
                'neighbor': {
                    '10.66.6.6': {
                        'remote_as': 400,
                        'link': 'external',
                        'shutdown': False,
                        'address_family': {
                            'vpnv4 unicast': {
                                'session_state': 'Established',
                                'up_time': '01:01:51',
                                'last_read': '00:00:24',
                                'last_write': '00:00:21',
                                'current_time': '0x530C0D'
                            },
                            'vpnv6 unicast': {}
                        },
                        'bgp_version': 4,
                        'router_id': '10.66.6.6',
                        'session_state': 'Established',
                        'bgp_negotiated_keepalive_timers': {
                            'hold_time': 180,
                            'keepalive_interval': 60
                        },
                        'bgp_neighbor_session': {
                            'sessions': 1,
                            },
                        'bgp_negotiated_capabilities': {
                            'route_refresh': 'advertised',
                            'four_octets_asn': 'advertised',
                            'ipv4_unicast': 'advertised and received',
                            'enhanced_refresh': 'advertised',
                            'stateful_switchover': 'NO for session 1'
                        },
                        'bgp_neighbor_counters': {
                            'messages': {
                                'sent': {
                                    'opens': 1,
                                    'notifications': 0,
                                    'updates': 1,
                                    'keepalives': 69,
                                    'route_refresh': 0,
                                    'total': 71
                                },
                                'received': {
                                    'opens': 1,
                                    'notifications': 0,
                                    'updates': 1,
                                    'keepalives': 64,
                                    'route_refresh': 0,
                                    'total': 66
                                },
                                'in_queue_depth': 0,
                                'out_queue_depth': 0
                            }
                        },
                        'bgp_session_transport': {
                            'min_time_between_advertisement_runs': 0,
                            'address_tracking_status': 'enabled',
                            'rib_route_ip': '10.66.6.6',
                            'connection': {
                                'established': 2,
                                'dropped': 1,
                                'last_reset': '01:05:09',
                                'reset_reason': 'Active open failed'
                            },
                            'tcp_path_mtu_discovery': 'enabled',
                            'graceful_restart': 'disabled',
                            'connection_state': 'estab',
                            'io_status': 1,
                            'unread_input_bytes': 0,
                            'ecn_connection': 'disabled',
                            'minimum_incoming_ttl': 0,
                            'outgoing_ttl': 1,
                            'transport': {
                                'local_host': '10.66.6.4',
                                'local_port': '179',
                                'foreign_host': '10.66.6.6',
                                'foreign_port': '11003',
                                'mss': 1460
                            },
                            'connection_tableid': 2,
                            'maximum_output_segment_queue_size': 50,
                            'enqueued_packets': {
                                'retransmit_packet': 0,
                                'input_packet': 0,
                                'mis_ordered_packet': 0
                            },
                            'iss': 2048397580,
                            'snduna': 2048398972,
                            'sndnxt': 2048398972,
                            'irs': 213294715,
                            'rcvnxt': 213296046,
                            'sndwnd': 32000,
                            'snd_scale': 0,
                            'maxrcvwnd': 16384,
                            'rcvwnd': 15054,
                            'rcv_scale': 0,
                            'delrcvwnd': 1330,
                            'srtt': 1000,
                            'rtto': 1003,
                            'rtv': 3,
                            'krtt': 0,
                            'min_rtt': 2,
                            'max_rtt': 1000,
                            'ack_hold': 200,
                            'uptime': 3712326,
                            'sent_idletime': 21866,
                            'receive_idletime': 21765,
                            'status_flags': 'passive open, gen tcbs',
                            'option_flags': 'VRF id set, nagle, path mtu capable',
                            'ip_precedence_value': 6,
                            'datagram': {
                                'datagram_received': {
                                    'value': 135,
                                    'out_of_order': 0,
                                    'with_data': 66,
                                    'total_data': 1330
                                },
                                'datagram_sent': {
                                    'value': 137,
                                    'retransmit': 0,
                                    'fastretransmit': 0,
                                    'partialack': 0,
                                    'second_congestion': 0,
                                    'with_data': 71,
                                    'total_data': 1391
                                }
                            },
                            'packet_fast_path': 0,
                            'packet_fast_processed': 0,
                            'packet_slow_path': 0,
                            'fast_lock_acquisition_failures': 0,
                            'lock_slow_path': 0,
                            'tcp_semaphore': '0x1286E8CC',
                            'tcp_semaphore_status': 'FREE'
                        },
                        'bgp_event_timer': {
                            'starts': {
                                'retrans': 70,
                                'timewait': 0,
                                'ackhold': 66,
                                'sendwnd': 0,
                                'keepalive': 0,
                                'giveup': 0,
                                'pmtuager': 0,
                                'deadwait': 0,
                                'linger': 0,
                                'processq': 0
                            },
                            'wakeups': {
                                'retrans': 0,
                                'timewait': 0,
                                'ackhold': 64,
                                'sendwnd': 0,
                                'keepalive': 0,
                                'giveup': 0,
                                'pmtuager': 0,
                                'deadwait': 0,
                                'linger': 0,
                                'processq': 0
                            },
                            'next': {
                                'retrans': '0x0',
                                'timewait': '0x0',
                                'ackhold': '0x0',
                                'sendwnd': '0x0',
                                'keepalive': '0x0',
                                'giveup': '0x0',
                                'pmtuager': '0x0',
                                'deadwait': '0x0',
                                'linger': '0x0',
                                'processq': '0x0'
                            }
                        }
                    },
                    '2001:DB8:20:4:6::6': {
                        'remote_as': 400,
                        'link': 'external',
                        'shutdown': False,
                        'address_family': {
                            'vpnv6 unicast': {
                                'session_state': 'Idle',
                                'last_read': '00:00:22',
                                'last_write': '00:00:01',
                                'current_time': '0x5319B5'
                            },
                            'ipv4 multicast': {},
                            'l2vpn evpn': {},
                            'vpnv4 multicast': {},
                            'mvpnv4 unicast': {},
                            'mvpnv6 unicast': {},
                            'vpnv6 multicast': {}
                        },
                        'bgp_version': 4,
                        'router_id': '10.66.6.6',
                        'session_state': 'Idle',
                        'bgp_negotiated_keepalive_timers': {
                            'hold_time': 180,
                            'keepalive_interval': 60
                        },
                        'bgp_neighbor_session': {
                            'sessions': 1,
                            },
                        'bgp_negotiated_capabilities': {
                            'route_refresh': 'advertised',
                            'four_octets_asn': 'advertised',
                            'ipv6_unicast': 'advertised and received',
                            'enhanced_refresh': 'advertised',
                            'stateful_switchover': 'NO for session 1'
                        },
                        'bgp_neighbor_counters': {
                            'messages': {
                                'sent': {
                                    'opens': 1,
                                    'notifications': 0,
                                    'updates': 1,
                                    'keepalives': 70,
                                    'route_refresh': 0,
                                    'total': 72
                                },
                                'received': {
                                    'opens': 1,
                                    'notifications': 0,
                                    'updates': 1,
                                    'keepalives': 64,
                                    'route_refresh': 0,
                                    'total': 66
                                },
                                'in_queue_depth': 0,
                                'out_queue_depth': 0
                            }
                        },
                        'bgp_session_transport': {
                            'min_time_between_advertisement_runs': 0,
                            'address_tracking_status': 'enabled',
                            'rib_route_ip': '2001:DB8:20:4:6::6',
                            'connection': {
                                'established': 2,
                                'dropped': 1,
                                'last_reset': '01:05:13',
                                'reset_reason': 'Active open failed'
                            },
                            'tcp_path_mtu_discovery': 'enabled',
                            'graceful_restart': 'disabled',
                            'connection_state': 'estab',
                            'io_status': 1,
                            'unread_input_bytes': 0,
                            'ecn_connection': 'disabled',
                            'minimum_incoming_ttl': 0,
                            'outgoing_ttl': 1,
                            'transport': {
                                'local_host': '2001:DB8:20:4:6::4',
                                'local_port': '179',
                                'foreign_host': '2001:DB8:20:4:6::6',
                                'foreign_port': '11003',
                                'mss': 1440
                            },
                            'connection_tableid': 503316482,
                            'maximum_output_segment_queue_size': 50,
                            'enqueued_packets': {
                                'retransmit_packet': 0,
                                'input_packet': 0,
                                'mis_ordered_packet': 0
                            },
                            'iss': 3178074389,
                            'snduna': 3178075806,
                            'sndnxt': 3178075806,
                            'irs': 693674496,
                            'rcvnxt': 693675877,
                            'sndwnd': 32000,
                            'snd_scale': 0,
                            'maxrcvwnd': 16384,
                            'rcvwnd': 15004,
                            'rcv_scale': 0,
                            'delrcvwnd': 1380,
                            'srtt': 1000,
                            'rtto': 1003,
                            'rtv': 3,
                            'krtt': 0,
                            'min_rtt': 3,
                            'max_rtt': 1000,
                            'ack_hold': 200,
                            'uptime': 3711535,
                            'sent_idletime': 2335,
                            'receive_idletime': 2277,
                            'status_flags': 'passive open, gen tcbs',
                            'option_flags': 'VRF id set, nagle, path mtu capable',
                            'ip_precedence_value': 6,
                            'datagram': {
                                'datagram_received': {
                                    'value': 137,
                                    'out_of_order': 0,
                                    'with_data': 66,
                                    'total_data': 1380
                                },
                                'datagram_sent': {
                                    'value': 138,
                                    'retransmit': 0,
                                    'fastretransmit': 0,
                                    'partialack': 0,
                                    'second_congestion': 0,
                                    'with_data': 138,
                                    'total_data': 6944
                                }
                            },
                            'packet_fast_path': 0,
                            'packet_fast_processed': 0,
                            'packet_slow_path': 0,
                            'fast_lock_acquisition_failures': 0,
                            'lock_slow_path': 0,
                            'tcp_semaphore': '0x1286E93C',
                            'tcp_semaphore_status': 'FREE'
                        },
                        'bgp_event_timer': {
                            'starts': {
                                'retrans': 71,
                                'timewait': 0,
                                'ackhold': 66,
                                'sendwnd': 0,
                                'keepalive': 0,
                                'giveup': 0,
                                'pmtuager': 0,
                                'deadwait': 0,
                                'linger': 0,
                                'processq': 0
                            },
                            'wakeups': {
                                'retrans': 0,
                                'timewait': 0,
                                'ackhold': 64,
                                'sendwnd': 0,
                                'keepalive': 0,
                                'giveup': 0,
                                'pmtuager': 0,
                                'deadwait': 0,
                                'linger': 0,
                                'processq': 0
                            },
                            'next': {
                                'retrans': '0x0',
                                'timewait': '0x0',
                                'ackhold': '0x0',
                                'sendwnd': '0x0',
                                'keepalive': '0x0',
                                'giveup': '0x0',
                                'pmtuager': '0x0',
                                'deadwait': '0x0',
                                'linger': '0x0',
                                'processq': '0x0'
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output4 = {'execute.return_value': '''
        router# show bgp all neighbors

        For address family: IPv4 Unicast

        For address family: IPv6 Unicast

        For address family: VPNv4 Unicast
        BGP neighbor is 10.16.2.2,  remote AS 100, internal link
          BGP version 4, remote router ID 10.16.2.2
          BGP state = Established, up for 01:10:35
          Last read 00:00:04, last write 00:00:09, hold time is 180, keepalive interval is 60 seconds
          Neighbor sessions:
            1 active, is not multisession capable (disabled)
          Neighbor capabilities:
            Route refresh: advertised and received(new)
            Four-octets ASN Capability: advertised and received
            Address family VPNv4 Unicast: advertised and received
            Address family VPNv6 Unicast: advertised and received
            Graceful Restart Capability: received
              Remote Restart timer is 120 seconds
              Address families advertised by peer:
                VPNv4 Unicast (was not preserved, VPNv6 Unicast (was not preserved
            Enhanced Refresh Capability: advertised
            Multisession Capability:
            Stateful switchover support enabled: NO for session 1
          Message statistics:
            InQ depth is 0
            OutQ depth is 0

                                 Sent       Rcvd
            Opens:                  1          1
            Notifications:          0          0
            Updates:               11          6
            Keepalives:            75         74
            Route Refresh:          0          0
            Total:                 87         81
          Default minimum time between advertisement runs is 0 seconds

          Address tracking is enabled, the RIB does have a route to 10.16.2.2
          Connections established 1; dropped 0
          Last reset never
          Transport(tcp) path-mtu-discovery is enabled
          Graceful-Restart is disabled
        Connection state is ESTAB, I/O status: 1, unread input bytes: 0
        Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 255
        Local host: 10.64.4.4, Local port: 35281
        Foreign host: 10.16.2.2, Foreign port: 179
        Connection tableid (VRF): 0
        Maximum output segment queue size: 50

        Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

        Event Timers (current time is 0x530449):
        Timer          Starts    Wakeups            Next
        Retrans            86          0             0x0
        TimeWait            0          0             0x0
        AckHold            80         72             0x0
        SendWnd             0          0             0x0
        KeepAlive           0          0             0x0
        GiveUp              0          0             0x0
        PmtuAger            1          1             0x0
        DeadWait            0          0             0x0
        Linger              0          0             0x0
        ProcessQ            0          0             0x0

        iss:   55023811  snduna:   55027115  sndnxt:   55027115
        irs:  109992783  rcvnxt:  109995158

        sndwnd:  16616  scale:      0  maxrcvwnd:  16384
        rcvwnd:  16327  scale:      0  delrcvwnd:     57

        SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
        minRTT: 4 ms, maxRTT: 1000 ms, ACK hold: 200 ms
        uptime: 4236258 ms, Sent idletime: 4349 ms, Receive idletime: 4549 ms
        Status Flags: active open
        Option Flags: nagle, path mtu capable
        IP Precedence value : 6

        Datagrams (max data segment is 536 bytes):
        Rcvd: 164 (out of order: 0), with data: 80, total data bytes: 2374
        Sent: 166 (retransmit: 0, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 87, total data bytes: 3303

         Packets received in fast path: 0, fast processed: 0, slow path: 0
         fast lock acquisition failures: 0, slow path: 0
        TCP Semaphore      0x1286E7EC  FREE

        BGP neighbor is 10.36.3.3,  remote AS 100, internal link
          BGP version 4, remote router ID 10.36.3.3
          BGP state = Established, up for 01:10:41
          Last read 00:00:04, last write 00:00:43, hold time is 180, keepalive interval is 60 seconds
          Neighbor sessions:
            1 active, is not multisession capable (disabled)
          Neighbor capabilities:
            Route refresh: advertised and received(new)
            Four-octets ASN Capability: advertised and received
            Address family VPNv4 Unicast: advertised and received
            Address family VPNv6 Unicast: advertised and received
            Graceful Restart Capability: received
              Remote Restart timer is 120 seconds
              Address families advertised by peer:
                VPNv4 Unicast (was not preserved, VPNv6 Unicast (was not preserved
            Enhanced Refresh Capability: advertised
            Multisession Capability:
            Stateful switchover support enabled: NO for session 1
          Message statistics:
            InQ depth is 0
            OutQ depth is 0

                                 Sent       Rcvd
            Opens:                  1          1
            Notifications:          0          0
            Updates:               11          6
            Keepalives:            75         74
            Route Refresh:          0          0
            Total:                 87         81
          Default minimum time between advertisement runs is 0 seconds

          Address tracking is enabled, the RIB does have a route to 10.36.3.3
          Connections established 1; dropped 0
          Last reset never
          Transport(tcp) path-mtu-discovery is enabled
          Graceful-Restart is disabled
        Connection state is ESTAB, I/O status: 1, unread input bytes: 0
        Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 255
        Local host: 10.64.4.4, Local port: 56031
        Foreign host: 10.36.3.3, Foreign port: 179
        Connection tableid (VRF): 0
        Maximum output segment queue size: 50

        Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

        Event Timers (current time is 0x530638):
        Timer          Starts    Wakeups            Next
        Retrans            86          0             0x0
        TimeWait            0          0             0x0
        AckHold            80         73             0x0
        SendWnd             0          0             0x0
        KeepAlive           0          0             0x0
        GiveUp              0          0             0x0
        PmtuAger            1          1             0x0
        DeadWait            0          0             0x0
        Linger              0          0             0x0
        ProcessQ            0          0             0x0

        iss: 2116369173  snduna: 2116372477  sndnxt: 2116372477
        irs: 4033842748  rcvnxt: 4033845123

        sndwnd:  16616  scale:      0  maxrcvwnd:  16384
        rcvwnd:  16327  scale:      0  delrcvwnd:     57

        SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
        minRTT: 3 ms, maxRTT: 1000 ms, ACK hold: 200 ms
        uptime: 4243393 ms, Sent idletime: 5375 ms, Receive idletime: 5575 ms
        Status Flags: active open
        Option Flags: nagle, path mtu capable
        IP Precedence value : 6

        Datagrams (max data segment is 536 bytes):
        Rcvd: 165 (out of order: 0), with data: 80, total data bytes: 2374
        Sent: 167 (retransmit: 0, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 87, total data bytes: 3303

         Packets received in fast path: 0, fast processed: 0, slow path: 0
         fast lock acquisition failures: 0, slow path: 0
        TCP Semaphore      0x1286E85C  FREE

        BGP neighbor is 10.4.6.6,  vrf VRF1,  remote AS 300, external link
          Administratively shut down
          BGP version 4, remote router ID 10.4.6.6
          BGP state = Established, up for 01:01:59
          Last read 00:00:33, last write 00:00:30, hold time is 180, keepalive interval is 60 seconds
          Neighbor sessions:
            1 active, is not multisession capable (disabled)
          Neighbor capabilities:
            Route refresh: advertised
            Four-octets ASN Capability: advertised
            Address family IPv4 Unicast: advertised and received
            Enhanced Refresh Capability: advertised
            Multisession Capability:
            Stateful switchover support enabled: NO for session 1
          Message statistics:
            InQ depth is 0
            OutQ depth is 0

                                 Sent       Rcvd
            Opens:                  1          1
            Notifications:          0          0
            Updates:                3          1
            Keepalives:            69         64
            Route Refresh:          0          0
            Total:                 73         66
          Default minimum time between advertisement runs is 0 seconds

          Address tracking is enabled, the RIB does have a route to 10.4.6.6
          Connections established 2; dropped 1
          Last reset 01:02:11, due to Peer closed the session of session 1
          Transport(tcp) path-mtu-discovery is enabled
          Graceful-Restart is disabled
        Connection state is ESTAB, I/O status: 1, unread input bytes: 0
        Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 1
        Local host: 10.4.6.4, Local port: 179
        Foreign host: 10.4.6.6, Foreign port: 11010
        Connection tableid (VRF): 1
        Maximum output segment queue size: 50

        Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

        Event Timers (current time is 0x530A19):
        Timer          Starts    Wakeups            Next
        Retrans            71          0             0x0
        TimeWait            0          0             0x0
        AckHold            66         64             0x0
        SendWnd             0          0             0x0
        KeepAlive           0          0             0x0
        GiveUp              0          0             0x0
        PmtuAger            0          0             0x0
        DeadWait            0          0             0x0
        Linger              0          0             0x0
        ProcessQ            0          0             0x0

        iss:     271842  snduna:     273380  sndnxt:     273380
        irs:  930048172  rcvnxt:  930049503

        sndwnd:  32000  scale:      0  maxrcvwnd:  16384
        rcvwnd:  15054  scale:      0  delrcvwnd:   1330

        SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
        minRTT: 1 ms, maxRTT: 1000 ms, ACK hold: 200 ms
        uptime: 3720132 ms, Sent idletime: 31107 ms, Receive idletime: 30999 ms
        Status Flags: passive open, gen tcbs
        Option Flags: VRF id set, nagle, path mtu capable
        IP Precedence value : 6

        Datagrams (max data segment is 1460 bytes):
        Rcvd: 137 (out of order: 0), with data: 66, total data bytes: 1330
        Sent: 138 (retransmit: 0, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 72, total data bytes: 1537

         Packets received in fast path: 0, fast processed: 0, slow path: 0
         fast lock acquisition failures: 0, slow path: 0
        TCP Semaphore      0x1286E62C  FREE

        BGP neighbor is 10.66.6.6,  vrf VRF2,  remote AS 400, external link
          BGP version 4, remote router ID 10.66.6.6
          BGP state = Established, up for 01:01:51
          Last read 00:00:24, last write 00:00:21, hold time is 180, keepalive interval is 60 seconds
          Neighbor sessions:
            1 active, is not multisession capable (disabled)
          Neighbor capabilities:
            Route refresh: advertised
            Four-octets ASN Capability: advertised
            Address family IPv4 Unicast: advertised and received
            Enhanced Refresh Capability: advertised
            Multisession Capability:
            Stateful switchover support enabled: NO for session 1
          Message statistics:
            InQ depth is 0
            OutQ depth is 0

                                 Sent       Rcvd
            Opens:                  1          1
            Notifications:          0          0
            Updates:                1          1
            Keepalives:            69         64
            Route Refresh:          0          0
            Total:                 71         66
          Default minimum time between advertisement runs is 0 seconds

          Address tracking is enabled, the RIB does have a route to 10.66.6.6
          Connections established 2; dropped 1
          Last reset 01:05:09, due to Active open failed
          Transport(tcp) path-mtu-discovery is enabled
          Graceful-Restart is disabled
        Connection state is ESTAB, I/O status: 1, unread input bytes: 0
        Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 1
        Local host: 10.66.6.4, Local port: 179
        Foreign host: 10.66.6.6, Foreign port: 11003
        Connection tableid (VRF): 2
        Maximum output segment queue size: 50

        Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

        Event Timers (current time is 0x530C0D):
        Timer          Starts    Wakeups            Next
        Retrans            70          0             0x0
        TimeWait            0          0             0x0
        AckHold            66         64             0x0
        SendWnd             0          0             0x0
        KeepAlive           0          0             0x0
        GiveUp              0          0             0x0
        PmtuAger            0          0             0x0
        DeadWait            0          0             0x0
        Linger              0          0             0x0
        ProcessQ            0          0             0x0

        iss: 2048397580  snduna: 2048398972  sndnxt: 2048398972
        irs:  213294715  rcvnxt:  213296046

        sndwnd:  32000  scale:      0  maxrcvwnd:  16384
        rcvwnd:  15054  scale:      0  delrcvwnd:   1330

        SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
        minRTT: 2 ms, maxRTT: 1000 ms, ACK hold: 200 ms
        uptime: 3712326 ms, Sent idletime: 21866 ms, Receive idletime: 21765 ms
        Status Flags: passive open, gen tcbs
        Option Flags: VRF id set, nagle, path mtu capable
        IP Precedence value : 6

        Datagrams (max data segment is 1460 bytes):
        Rcvd: 135 (out of order: 0), with data: 66, total data bytes: 1330
        Sent: 137 (retransmit: 0, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 71, total data bytes: 1391

         Packets received in fast path: 0, fast processed: 0, slow path: 0
         fast lock acquisition failures: 0, slow path: 0
        TCP Semaphore      0x1286E8CC  FREE


        For address family: VPNv6 Unicast
        BGP neighbor is 10.64.4.4,  remote AS 100, internal link
          Description: router2222222
          BGP version 4, remote router ID 10.64.4.4
          BGP state = Established, up for 01:10:38
          Last read 00:00:07, last write 00:00:12, hold time is 180, keepalive interval is 60 seconds
          Neighbor sessions:
            1 active, is not multisession capable (disabled)
          Neighbor capabilities:
            Route refresh: advertised and received(new)
            Four-octets ASN Capability: advertised and received
            Address family VPNv4 Unicast: advertised and received
            Address family VPNv6 Unicast: advertised and received
            Graceful Restart Capability: received
              Remote Restart timer is 120 seconds
              Address families advertised by peer:
                VPNv4 Unicast (was not preserved, VPNv6 Unicast (was not preserved
            Enhanced Refresh Capability: advertised
            Multisession Capability:
            Stateful switchover support enabled: NO for session 1
          Message statistics:
            InQ depth is 0
            OutQ depth is 0

                                 Sent       Rcvd
            Opens:                  1          1
            Notifications:          0          0
            Updates:               11          6
            Keepalives:            75         74
            Route Refresh:          0          0
            Total:                 87         81
          Default minimum time between advertisement runs is 0 seconds

          Address tracking is enabled, the RIB does have a route to 10.16.2.2
          Connections established 1; dropped 0
          Last reset never
          Transport(tcp) path-mtu-discovery is enabled
          Graceful-Restart is disabled
        Connection state is ESTAB, I/O status: 1, unread input bytes: 0
        Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 255
        Local host: 10.64.4.4, Local port: 35281
        Foreign host: 10.16.2.2, Foreign port: 179
        Connection tableid (VRF): 0
        Maximum output segment queue size: 50

        Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

        Event Timers (current time is 0x530FF5):
        Timer          Starts    Wakeups            Next
        Retrans            86          0             0x0
        TimeWait            0          0             0x0
        AckHold            80         72             0x0
        SendWnd             0          0             0x0
        KeepAlive           0          0             0x0
        GiveUp              0          0             0x0
        PmtuAger            1          1             0x0
        DeadWait            0          0             0x0
        Linger              0          0             0x0
        ProcessQ            0          0             0x0

        iss:   55023811  snduna:   55027115  sndnxt:   55027115
        irs:  109992783  rcvnxt:  109995158

        sndwnd:  16616  scale:      0  maxrcvwnd:  16384
        rcvwnd:  16327  scale:      0  delrcvwnd:     57

        SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
        minRTT: 4 ms, maxRTT: 1000 ms, ACK hold: 200 ms
        uptime: 4239741 ms, Sent idletime: 7832 ms, Receive idletime: 8032 ms
        Status Flags: active open
        Option Flags: nagle, path mtu capable
        IP Precedence value : 6

        Datagrams (max data segment is 536 bytes):
        Rcvd: 164 (out of order: 0), with data: 80, total data bytes: 2374
        Sent: 166 (retransmit: 0, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 87, total data bytes: 3303

         Packets received in fast path: 0, fast processed: 0, slow path: 0
         fast lock acquisition failures: 0, slow path: 0
        TCP Semaphore      0x1286E7EC  FREE

        BGP neighbor is 10.100.5.5,  remote AS 100, internal link
          BGP version 4, remote router ID 10.100.5.5
          BGP state = Established, up for 01:10:44
          Last read 00:00:08, last write 00:00:47, hold time is 180, keepalive interval is 60 seconds
          Neighbor sessions:
            1 active, is not multisession capable (disabled)
          Neighbor capabilities:
            Route refresh: advertised and received(new)
            Four-octets ASN Capability: advertised and received
            Address family VPNv4 Unicast: advertised and received
            Address family VPNv6 Unicast: advertised and received
            Graceful Restart Capability: received
              Remote Restart timer is 120 seconds
              Address families advertised by peer:
                VPNv4 Unicast (was not preserved, VPNv6 Unicast (was not preserved
            Enhanced Refresh Capability: advertised
            Multisession Capability:
            Stateful switchover support enabled: NO for session 1
          Message statistics:
            InQ depth is 0
            OutQ depth is 0

                                 Sent       Rcvd
            Opens:                  1          1
            Notifications:          0          0
            Updates:               11          6
            Keepalives:            75         74
            Route Refresh:          0          0
            Total:                 87         81
          Default minimum time between advertisement runs is 0 seconds

          Address tracking is enabled, the RIB does have a route to 10.36.3.3
          Connections established 1; dropped 0
          Last reset never
          Transport(tcp) path-mtu-discovery is enabled
          Graceful-Restart is disabled
        Connection state is ESTAB, I/O status: 1, unread input bytes: 0
        Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 255
        Local host: 10.64.4.4, Local port: 56031
        Foreign host: 10.36.3.3, Foreign port: 179
        Connection tableid (VRF): 0
        Maximum output segment queue size: 50

        Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

        Event Timers (current time is 0x5313D8):
        Timer          Starts    Wakeups            Next
        Retrans            86          0             0x0
        TimeWait            0          0             0x0
        AckHold            80         73             0x0
        SendWnd             0          0             0x0
        KeepAlive           0          0             0x0
        GiveUp              0          0             0x0
        PmtuAger            1          1             0x0
        DeadWait            0          0             0x0
        Linger              0          0             0x0
        ProcessQ            0          0             0x0

        iss: 2116369173  snduna: 2116372477  sndnxt: 2116372477
        irs: 4033842748  rcvnxt: 4033845123

        sndwnd:  16616  scale:      0  maxrcvwnd:  16384
        rcvwnd:  16327  scale:      0  delrcvwnd:     57

        SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
        minRTT: 3 ms, maxRTT: 1000 ms, ACK hold: 200 ms
        uptime: 4246385 ms, Sent idletime: 8367 ms, Receive idletime: 8567 ms
        Status Flags: active open
        Option Flags: nagle, path mtu capable
        IP Precedence value : 6

        Datagrams (max data segment is 536 bytes):
        Rcvd: 165 (out of order: 0), with data: 80, total data bytes: 2374
        Sent: 167 (retransmit: 0, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 87, total data bytes: 3303

         Packets received in fast path: 0, fast processed: 0, slow path: 0
         fast lock acquisition failures: 0, slow path: 0
        TCP Semaphore      0x1286E85C  FREE

        BGP neighbor is 2001:DB8:4:6::6,  vrf VRF1,  remote AS 300, external link
          BGP version 4, remote router ID 10.4.6.6
          BGP state = Established, up for 01:01:58
          Last read 00:00:32, last write 00:00:06, hold time is 180, keepalive interval is 60 seconds
          Neighbor sessions:
            1 active, is not multisession capable (disabled)
          Neighbor capabilities:
            Route refresh: advertised
            Four-octets ASN Capability: advertised
            Address family IPv6 Unicast: advertised and received
            Enhanced Refresh Capability: advertised
            Multisession Capability:
            Stateful switchover support enabled: NO for session 1
          Message statistics:
            InQ depth is 0
            OutQ depth is 0

                                 Sent       Rcvd
            Opens:                  1          1
            Notifications:          0          0
            Updates:                3          1
            Keepalives:            70         64
            Route Refresh:          0          0
            Total:                 74         66
          Default minimum time between advertisement runs is 0 seconds

          Address tracking is enabled, the RIB does have a route to 2001:DB8:4:6::6
          Connections established 2; dropped 1
          Last reset 01:05:12, due to Active open failed
          Transport(tcp) path-mtu-discovery is enabled
          Graceful-Restart is disabled
        Connection state is ESTAB, I/O status: 1, unread input bytes: 0
        Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 1
        Local host: 2001:DB8:4:6::4, Local port: 179
        Foreign host: 2001:DB8:4:6::6, Foreign port: 11003
        Connection tableid (VRF): 503316481
        Maximum output segment queue size: 50

        Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

        Event Timers (current time is 0x5315CE):
        Timer          Starts    Wakeups            Next
        Retrans            72          0             0x0
        TimeWait            0          0             0x0
        AckHold            66         64             0x0
        SendWnd             0          0             0x0
        KeepAlive           0          0             0x0
        GiveUp              0          0             0x0
        PmtuAger            0          0             0x0
        DeadWait            0          0             0x0
        Linger              0          0             0x0
        ProcessQ            0          0             0x0

        iss:  164676617  snduna:  164678296  sndnxt:  164678296
        irs: 1797203329  rcvnxt: 1797204710

        sndwnd:  32000  scale:      0  maxrcvwnd:  16384
        rcvwnd:  15004  scale:      0  delrcvwnd:   1380

        SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
        minRTT: 1 ms, maxRTT: 1000 ms, ACK hold: 200 ms
        uptime: 3718683 ms, Sent idletime: 6954 ms, Receive idletime: 6849 ms
        Status Flags: passive open, gen tcbs
        Option Flags: VRF id set, nagle, path mtu capable
        IP Precedence value : 6

        Datagrams (max data segment is 1440 bytes):
        Rcvd: 138 (out of order: 0), with data: 66, total data bytes: 1380
        Sent: 139 (retransmit: 0, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 139, total data bytes: 7246

         Packets received in fast path: 0, fast processed: 0, slow path: 0
         fast lock acquisition failures: 0, slow path: 0
        TCP Semaphore      0x1286E9AC  FREE

        BGP neighbor is 2001:DB8:20:4:6::6,  vrf VRF2,  remote AS 400, external link
          BGP version 4, remote router ID 10.66.6.6
          BGP state = Idle
          Last read 00:00:22, last write 00:00:01, hold time is 180, keepalive interval is 60 seconds
          Neighbor sessions:
            1 active, is not multisession capable (disabled)
          Neighbor capabilities:
            Route refresh: advertised
            Four-octets ASN Capability: advertised
            Address family IPv6 Unicast: advertised and received
            Enhanced Refresh Capability: advertised
            Multisession Capability:
            Stateful switchover support enabled: NO for session 1
          Message statistics:
            InQ depth is 0
            OutQ depth is 0

                                 Sent       Rcvd
            Opens:                  1          1
            Notifications:          0          0
            Updates:                1          1
            Keepalives:            70         64
            Route Refresh:          0          0
            Total:                 72         66
          Default minimum time between advertisement runs is 0 seconds

          Address tracking is enabled, the RIB does have a route to 2001:DB8:20:4:6::6
          Connections established 2; dropped 1
          Last reset 01:05:13, due to Active open failed
          Transport(tcp) path-mtu-discovery is enabled
          Graceful-Restart is disabled
        Connection state is ESTAB, I/O status: 1, unread input bytes: 0
        Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 1
        Local host: 2001:DB8:20:4:6::4, Local port: 179
        Foreign host: 2001:DB8:20:4:6::6, Foreign port: 11003
        Connection tableid (VRF): 503316482
        Maximum output segment queue size: 50

        Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

        Event Timers (current time is 0x5319B5):
        Timer          Starts    Wakeups            Next
        Retrans            71          0             0x0
        TimeWait            0          0             0x0
        AckHold            66         64             0x0
        SendWnd             0          0             0x0
        KeepAlive           0          0             0x0
        GiveUp              0          0             0x0
        PmtuAger            0          0             0x0
        DeadWait            0          0             0x0
        Linger              0          0             0x0
        ProcessQ            0          0             0x0

        iss: 3178074389  snduna: 3178075806  sndnxt: 3178075806
        irs:  693674496  rcvnxt:  693675877

        sndwnd:  32000  scale:      0  maxrcvwnd:  16384
        rcvwnd:  15004  scale:      0  delrcvwnd:   1380

        SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
        minRTT: 3 ms, maxRTT: 1000 ms, ACK hold: 200 ms
        uptime: 3711535 ms, Sent idletime: 2335 ms, Receive idletime: 2277 ms
        Status Flags: passive open, gen tcbs
        Option Flags: VRF id set, nagle, path mtu capable
        IP Precedence value : 6

        Datagrams (max data segment is 1440 bytes):
        Rcvd: 137 (out of order: 0), with data: 66, total data bytes: 1380
        Sent: 138 (retransmit: 0, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 138, total data bytes: 6944

         Packets received in fast path: 0, fast processed: 0, slow path: 0
         fast lock acquisition failures: 0, slow path: 0
        TCP Semaphore      0x1286E93C  FREE


        For address family: IPv4 Multicast

        For address family: L2VPN E-VPN

        For address family: VPNv4 Multicast

        For address family: MVPNv4 Unicast

        For address family: MVPNv6 Unicast

        For address family: VPNv6 Multicast
        '''}


    golden_output5 = {'execute.return_value': '''
            For address family: IPv4 Unicast
            BGP neighbor is 10.136.199.57,  remote AS 209, external link
              BGP version 4, remote router ID 0.0.0.0
              BGP state = Idle
              Neighbor sessions:
                0 active, is multisession capable
              Default minimum time between advertisement runs is 30 seconds

              Address tracking is enabled, the RIB does not have a route to 10.136.199.57
              Connections established 0; dropped 0
              Last reset never
              External BGP neighbor not directly connected.
              Transport(tcp) path-mtu-discovery is enabled
              Graceful-Restart is disabled
              No active TCP connection

            BGP neighbor is 172.16.0.2,  remote AS 10, external link
              BGP version 4, remote router ID 192.168.0.202
              BGP state = Established, up for 08:59:32
              Last read 00:00:37, last write 00:00:55, hold time is 180, keepalive interval is 60 seconds
              Neighbor sessions:
                1 active, is multisession capable
              Neighbor capabilities:
                Route refresh: advertised and received(new)
                Four-octets ASN Capability: advertised and received
                Address family IPv4 Unicast: advertised and received
                Multisession Capability: advertised and received
              Message statistics, state Established:
                InQ depth is 0
                OutQ depth is 0

                                     Sent       Rcvd
                Opens:                  1          1
                Notifications:          0          0
                Updates:                3          1
                Keepalives:           593        589
                Route Refresh:          1          0
                Total:                598        591
              Default minimum time between advertisement runs is 30 seconds

              Address tracking is enabled, the RIB does have a route to 172.16.0.2
              Connections established 1; dropped 0
              Last reset never
              Transport(tcp) path-mtu-discovery is enabled
              Graceful-Restart is disabled
            Connection state is ESTAB, I/O status: 1, unread input bytes: 0            
            Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 1
            Local host: 172.16.0.1, Local port: 179
            Foreign host: 172.16.0.2, Foreign port: 54555
            Connection tableid (VRF): 0
            Maximum output segment queue size: 50

            Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

            Event Timers (current time is 0x51AADE68):
            Timer          Starts    Wakeups            Next
            Retrans           596          0             0x0
            TimeWait            0          0             0x0
            AckHold           590        579             0x0
            SendWnd             0          0             0x0
            KeepAlive           0          0             0x0
            GiveUp              0          0             0x0
            PmtuAger            0          0             0x0
            DeadWait            0          0             0x0
            Linger              0          0             0x0
            ProcessQ            0          0             0x0

            iss:  922302782  snduna:  922314285  sndnxt:  922314285
            irs: 2839013050  rcvnxt: 2839024323

            sndwnd:  15130  scale:      0  maxrcvwnd:  16384
            rcvwnd:  15358  scale:      0  delrcvwnd:   1026

            SRTT: 650 ms, RTTO: 653 ms, RTV: 3 ms, KRTT: 0 ms
            minRTT: 0 ms, maxRTT: 650 ms, ACK hold: 200 ms
            Status Flags: passive open, gen tcbs
            Option Flags: nagle, path mtu capable
            IP Precedence value : 6

            Datagrams (max data segment is 1460 bytes):
            Rcvd: 1186 (out of order: 0), with data: 591, total data bytes: 11272
            Sent: 1184 (retransmit: 0, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 597, total data bytes: 11502
             Packets received in fast path: 0, fast processed: 0, slow path: 0
             fast lock acquisition failures: 0, slow path: 0


            For address family: IPv4 Multicast
        '''}

    golden_parsed_output5 = {
        'list_of_neighbors': ['10.136.199.57', '172.16.0.2'],
        'vrf': {
            'default': {
                'neighbor': {
                    '172.16.0.2': {
                        'address_family': {
                            'ipv4 multicast': {
                            },
                            'ipv4 unicast': {
                                'current_time': '0x51AADE68',
                                'last_read': '00:00:37',
                                'last_write': '00:00:55',
                                'session_state': 'Established',
                                'up_time': '08:59:32',
                            },
                        },
                        'bgp_event_timer': {
                            'next': {
                                'ackhold': '0x0',
                                'deadwait': '0x0',
                                'giveup': '0x0',
                                'keepalive': '0x0',
                                'linger': '0x0',
                                'pmtuager': '0x0',
                                'processq': '0x0',
                                'retrans': '0x0',
                                'sendwnd': '0x0',
                                'timewait': '0x0',
                            },
                            'starts': {
                                'ackhold': 590,
                                'deadwait': 0,
                                'giveup': 0,
                                'keepalive': 0,
                                'linger': 0,
                                'pmtuager': 0,
                                'processq': 0,
                                'retrans': 596,
                                'sendwnd': 0,
                                'timewait': 0,
                            },
                            'wakeups': {
                                'ackhold': 579,
                                'deadwait': 0,
                                'giveup': 0,
                                'keepalive': 0,
                                'linger': 0,
                                'pmtuager': 0,
                                'processq': 0,
                                'retrans': 0,
                                'sendwnd': 0,
                                'timewait': 0,
                            },
                        },
                        'bgp_negotiated_capabilities': {
                            'four_octets_asn': 'advertised and received',
                            'ipv4_unicast': 'advertised and received',
                            'multisession': 'advertised and received',
                            'route_refresh': 'advertised and received(new)',
                        },
                        'bgp_negotiated_keepalive_timers': {
                            'hold_time': 180,
                            'keepalive_interval': 60,
                        },
                        'bgp_neighbor_counters': {
                            'messages': {
                                'in_queue_depth': 0,
                                'out_queue_depth': 0,
                                'received': {
                                    'keepalives': 589,
                                    'notifications': 0,
                                    'opens': 1,
                                    'route_refresh': 0,
                                    'total': 591,
                                    'updates': 1,
                                },
                                'sent': {
                                    'keepalives': 593,
                                    'notifications': 0,
                                    'opens': 1,
                                    'route_refresh': 1,
                                    'total': 598,
                                    'updates': 3,
                                },
                            },
                        },
                        'bgp_neighbor_session': {
                        },
                        'bgp_session_transport': {
                            'ack_hold': 200,
                            'address_tracking_status': 'enabled',
                            'connection': {
                                'dropped': 0,
                                'established': 1,
                                'last_reset': 'never',
                            },
                            'connection_state': 'estab',
                            'connection_tableid': 0,
                            'datagram': {
                                'datagram_received': {
                                    'out_of_order': 0,
                                    'total_data': 11272,
                                    'value': 1186,
                                    'with_data': 591,
                                },
                                'datagram_sent': {
                                    'fastretransmit': 0,
                                    'partialack': 0,
                                    'retransmit': 0,
                                    'second_congestion': 0,
                                    'total_data': 11502,
                                    'value': 1184,
                                    'with_data': 597,
                                },
                            },
                            'delrcvwnd': 1026,
                            'ecn_connection': 'disabled',
                            'enqueued_packets': {
                                'input_packet': 0,
                                'mis_ordered_packet': 0,
                                'retransmit_packet': 0,
                            },
                            'fast_lock_acquisition_failures': 0,
                            'graceful_restart': 'disabled',
                            'io_status': 1,
                            'ip_precedence_value': 6,
                            'irs': 2839013050,
                            'iss': 922302782,
                            'krtt': 0,
                            'lock_slow_path': 0,
                            'max_rtt': 650,
                            'maximum_output_segment_queue_size': 50,
                            'maxrcvwnd': 16384,
                            'min_rtt': 0,
                            'min_time_between_advertisement_runs': 30,
                            'minimum_incoming_ttl': 0,
                            'option_flags': 'nagle, path mtu capable',
                            'outgoing_ttl': 1,
                            'packet_fast_path': 0,
                            'packet_fast_processed': 0,
                            'packet_slow_path': 0,
                            'rcv_scale': 0,
                            'rcvnxt': 2839024323,
                            'rcvwnd': 15358,
                            'rib_route_ip': '172.16.0.2',
                            'rtto': 653,
                            'rtv': 3,
                            'snd_scale': 0,
                            'sndnxt': 922314285,
                            'snduna': 922314285,
                            'sndwnd': 15130,
                            'srtt': 650,
                            'status_flags': 'passive open, gen tcbs',
                            'tcp_path_mtu_discovery': 'enabled',
                            'transport': {
                                'foreign_host': '172.16.0.2',
                                'foreign_port': '54555',
                                'local_host': '172.16.0.1',
                                'local_port': '179',
                                'mss': 1460,
                            },
                            'unread_input_bytes': 0,
                        },
                        'bgp_version': 4,
                        'link': 'external',
                        'remote_as': 10,
                        'router_id': '192.168.0.202',
                        'session_state': 'Established',
                        'shutdown': False,
                    },
                    '10.136.199.57': {
                        'address_family': {
                            'ipv4 unicast': {
                                'session_state': 'Idle',
                            },
                        },
                        'bgp_neighbor_session': {
                        },
                        'bgp_session_transport': {
                            'address_tracking_status': 'enabled',
                            'connection': {
                                'dropped': 0,
                                'established': 0,
                                'last_reset': 'never',
                            },
                            'graceful_restart': 'disabled',
                            'min_time_between_advertisement_runs': 30,
                            'tcp_connection': False,
                            'tcp_path_mtu_discovery': 'enabled',
                        },
                        'bgp_version': 4,
                        'link': 'external',
                        'remote_as': 209,
                        'router_id': '0.0.0.0',
                        'session_state': 'Idle',
                        'shutdown': False,
                    },
                },
            },
        },
    }
        
    def test_show_bgp_all_neighbors_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpAllNeighbors(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_bgp_all_neighbors_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowBgpAllNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_bgp_all_neighbors_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowBgpAllNeighbors(device=self.device)
        parsed_output = obj.parse(address_family='l2vpn vpls', neighbor='192.168.165.120')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_bgp_all_neighbors_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowBgpAllNeighbors(device=self.device)
        parsed_output = obj.parse(address_family='l2vpn vpls', neighbor='192.168.165.119')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_bgp_all_neighbors_golden4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output4)
        obj = ShowBgpAllNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output4)


    def test_show_bgp_all_neighbors_golden5(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output5)
        obj = ShowBgpAllNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output5)


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

#-------------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
