import re
import unittest
from unittest.mock import Mock

from ats.topology import Device

from metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from parser.iosxe.show_bgp import ShowBgpAllSummary, ShowBgpAllClusterIds,\
                                  ShowBgpAllNeighbors

"""
class test_show_bgp_all_summary(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        'vrf':
            {'default':
                 {'neighbor':
                      {'200.0.1.1':
                           {'address_family':
                                {'ipv4 unicast':
                                     {'as': 100,
                                      'attribute_entries': '1/1',
                                      'bgp_table_version': 28,
                                      'input_queue': 0,
                                      'local_as': 100,
                                      'msg_rcvd': 0,
                                      'msg_sent': 0,
                                      'output_queue': 0,
                                      'path': {'memory_usage': 3672,
                                               'total_entries': 27},
                                      'prefixes':
                                          {'memory_usage': 6696,
                                           'total_entries': 27},
                                      'cache_entries':
                                          {
                                              'route-map':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  },
                                              'filter-list':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  }
                                          },
                                      'total_memory': 10648,
                                      'activity_prefixes': '47/20',
                                      'activity_paths': '66/39',
                                      'scan_interval': 60,
                                      'route_identifier': '200.0.1.1',
                                      'routing_table_version': 28,
                                      'state_pfxrcd': 'Idle',
                                      'tbl_ver': 1,
                                      'up_down': '01:07:38',
                                      'version': 4}}},
                      '200.0.2.1':
                           {'address_family':
                                {'ipv4 unicast':
                                     {'as': 100,
                                      'attribute_entries': '1/1',
                                      'bgp_table_version': 28,
                                      'input_queue': 0,
                                      'local_as': 100,
                                      'msg_rcvd': 0,
                                      'msg_sent': 0,
                                      'output_queue': 0,
                                      'path': {'memory_usage': 3672,
                                               'total_entries': 27},
                                      'prefixes':
                                          {'memory_usage': 6696,
                                           'total_entries': 27},
                                      'cache_entries':
                                          {
                                              'route-map':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  },
                                              'filter-list':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  }
                                          },
                                      'total_memory': 10648,
                                      'activity_prefixes': '47/20',
                                      'activity_paths': '66/39',
                                      'scan_interval': 60,
                                      'route_identifier': '200.0.1.1',
                                      'routing_table_version': 28,
                                      'state_pfxrcd': 'Idle',
                                      'tbl_ver': 1,
                                      'up_down': 'never',
                                      'version': 4}}},
                      '200.0.4.1':
                           {'address_family':
                                {'ipv4 unicast':
                                     {'as': 100,
                                      'attribute_entries': '1/1',
                                      'bgp_table_version': 28,
                                      'input_queue': 0,
                                      'local_as': 100,
                                      'msg_rcvd': 0,
                                      'msg_sent': 0,
                                      'output_queue': 0,
                                      'path': {'memory_usage': 3672,
                                               'total_entries': 27},
                                      'prefixes':
                                          {'memory_usage': 6696,
                                           'total_entries': 27},
                                      'cache_entries':
                                          {
                                              'route-map':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  },
                                              'filter-list':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  }
                                          },
                                      'total_memory': 10648,
                                      'activity_prefixes': '47/20',
                                      'activity_paths': '66/39',
                                      'scan_interval': 60,
                                      'route_identifier': '200.0.1.1',
                                      'routing_table_version': 28,
                                      'state_pfxrcd': 'Idle',
                                      'tbl_ver': 1,
                                      'up_down': '01:07:38',
                                      'version': 4}}},
                      '201.0.14.4':
                           {'address_family':
                                {'ipv4 unicast':
                                     {'as': 200,
                                      'attribute_entries': '1/1',
                                      'bgp_table_version': 28,
                                      'input_queue': 0,
                                      'local_as': 100,
                                      'msg_rcvd': 0,
                                      'msg_sent': 0,
                                      'output_queue': 0,
                                      'path': {'memory_usage': 3672,
                                               'total_entries': 27},
                                      'prefixes':
                                          {'memory_usage': 6696,
                                           'total_entries': 27},
                                      'cache_entries':
                                          {
                                              'route-map':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  },
                                              'filter-list':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  }
                                          },
                                      'total_memory': 10648,
                                      'activity_prefixes': '47/20',
                                      'activity_paths': '66/39',
                                      'scan_interval': 60,
                                      'route_identifier': '200.0.1.1',
                                      'routing_table_version': 28,
                                      'state_pfxrcd': 'Idle',
                                      'tbl_ver': 1,
                                      'up_down': 'never',
                                      'version': 4}}},
                      '201.0.26.2':
                           {'address_family':
                                {'ipv4 unicast':
                                     {'as': 300,
                                      'attribute_entries': '1/1',
                                      'bgp_table_version': 28,
                                      'input_queue': 0,
                                      'local_as': 100,
                                      'msg_rcvd': 0,
                                      'msg_sent': 0,
                                      'output_queue': 0,
                                      'path': {'memory_usage': 3672,
                                               'total_entries': 27},
                                      'prefixes':
                                          {'memory_usage': 6696,
                                           'total_entries': 27},
                                      'cache_entries':
                                          {
                                              'route-map':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  },
                                              'filter-list':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  }
                                          },
                                      'total_memory': 10648,
                                      'activity_prefixes': '47/20',
                                      'activity_paths': '66/39',
                                      'scan_interval': 60,
                                      'route_identifier': '200.0.1.1',
                                      'routing_table_version': 28,
                                      'state_pfxrcd': 'Idle',
                                      'tbl_ver': 1,
                                      'up_down': '01:07:38',
                                      'version': 4}}},
                       '2000::1:1': {'address_family': {'ipv6 unicast': {'as': 100,
                                                                         'bgp_table_version': 1,
                                                                         'input_queue': 0,
                                                                         'local_as': 100,
                                                                         'msg_rcvd': 0,
                                                                         'msg_sent': 0,
                                                                         'output_queue': 0,
                                                                         'route_identifier': '200.0.1.1',
                                                                         'routing_table_version': 1,
                                                                         'state_pfxrcd': 'Idle',
                                                                         'tbl_ver': 1,
                                                                         'up_down': '01:07:38',
                                                                         'version': 4}}},
                       '2000::4:1': {'address_family': {'ipv6 unicast': {'as': 100,
                                                                         'bgp_table_version': 1,
                                                                         'input_queue': 0,
                                                                         'local_as': 100,
                                                                         'msg_rcvd': 0,
                                                                         'msg_sent': 0,
                                                                         'output_queue': 0,
                                                                         'route_identifier': '200.0.1.1',
                                                                         'routing_table_version': 1,
                                                                         'state_pfxrcd': 'Idle',
                                                                         'tbl_ver': 1,
                                                                         'up_down': '01:07:38',
                                                                         'version': 4}}},
                       '2001::14:4': {'address_family': {'ipv6 unicast': {'as': 200,
                                                                          'bgp_table_version': 1,
                                                                          'input_queue': 0,
                                                                          'local_as': 100,
                                                                          'msg_rcvd': 0,
                                                                          'msg_sent': 0,
                                                                          'output_queue': 0,
                                                                          'route_identifier': '200.0.1.1',
                                                                          'routing_table_version': 1,
                                                                          'state_pfxrcd': 'Idle',
                                                                          'tbl_ver': 1,
                                                                          'up_down': 'never',
                                                                          'version': 4}}},
                       '2001::26:2': {'address_family': {'ipv6 unicast': {'as': 300,
                                                                          'bgp_table_version': 1,
                                                                          'input_queue': 0,
                                                                          'local_as': 100,
                                                                          'msg_rcvd': 0,
                                                                          'msg_sent': 0,
                                                                          'output_queue': 0,
                                                                          'route_identifier': '200.0.1.1',
                                                                          'routing_table_version': 1,
                                                                          'state_pfxrcd': 'Idle',
                                                                          'tbl_ver': 1,
                                                                          'up_down': '01:07:38',
                                                                          'version': 4}}},
                       '3.3.3.3': {'address_family':
                                       {'vpnv4 unicast':
                                            {'as': 100,
                                             'bgp_table_version': 1,
                                             'input_queue': 0,
                                             'local_as': 100,
                                             'msg_rcvd': 0,
                                             'msg_sent': 0,
                                             'output_queue': 0,
                                             'route_identifier': '200.0.1.1',
                                             'routing_table_version': 1,
                                             'state_pfxrcd': 'Idle',
                                             'tbl_ver': 1,
                                             'up_down': 'never',
                                             'version': 4},
                                        'vpnv6 unicast':
                                            {'as': 100,
                                             'bgp_table_version': 1,
                                             'input_queue': 0,
                                             'local_as': 100,
                                             'msg_rcvd': 0,
                                             'msg_sent': 0,
                                             'output_queue': 0,
                                             'route_identifier': '200.0.1.1',
                                             'routing_table_version': 1,
                                             'state_pfxrcd': 'Idle',
                                             'tbl_ver': 1,
                                             'up_down': 'never',
                                             'version': 4}
                                        }
                                   }
                       }
                  }
             }
    }


    golden_output = {'execute.return_value': '''
        For address family: IPv4 Unicast
        BGP router identifier 200.0.1.1, local AS number 100
        BGP table version is 28, main routing table version 28
        27 network entries using 6696 bytes of memory
        27 path entries using 3672 bytes of memory
        1/1 BGP path/bestpath attribute entries using 280 bytes of memory
        0 BGP route-map cache entries using 0 bytes of memory
        0 BGP filter-list cache entries using 0 bytes of memory
        BGP using 10648 total bytes of memory
        BGP activity 47/20 prefixes, 66/39 paths, scan interval 60 secs

        Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        200.0.1.1       4          100       0       0        1    0    0 01:07:38 Idle
        200.0.2.1       4          100       0       0        1    0    0 never    Idle
        200.0.4.1       4          100       0       0        1    0    0 01:07:38 Idle
        201.0.14.4      4          200       0       0        1    0    0 never    Idle
        201.0.26.2      4          300       0       0        1    0    0 01:07:38 Idle

        For address family: IPv6 Unicast
        BGP router identifier 200.0.1.1, local AS number 100
        BGP table version is 1, main routing table version 1

        Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        2000::1:1       4          100       0       0        1    0    0 01:07:38 Idle
        2000::4:1       4          100       0       0        1    0    0 01:07:38 Idle
        2001::14:4      4          200       0       0        1    0    0 never    Idle
        2001::26:2      4          300       0       0        1    0    0 01:07:38 Idle

        For address family: VPNv4 Unicast
        BGP router identifier 200.0.1.1, local AS number 100
        BGP table version is 1, main routing table version 1

        Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        3.3.3.3         4          100       0       0        1    0    0 never    Idle

        For address family: VPNv6 Unicast
        BGP router identifier 200.0.1.1, local AS number 100
        BGP table version is 1, main routing table version 1

        Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        3.3.3.3         4          100       0       0        1    0    0 never    Idle

        '''}

    golden_parsed_output_2 = {
        'vrf':
            {'default':
                 {'neighbor':
                      {'2.2.2.2':
                           {'address_family':
                                {'vpnv4 unicast':
                                     {'as': 100,
                                      'attribute_entries': '6/4',
                                      'bgp_table_version': 56,
                                      'input_queue': 0,
                                      'local_as': 100,
                                      'msg_rcvd': 82,
                                      'msg_sent': 88,
                                      'output_queue': 0,
                                      'path': {'memory_usage': 3600,
                                               'total_entries': 45},
                                      'prefixes':
                                          {'memory_usage': 4560,
                                           'total_entries': 30},
                                      'cache_entries':
                                          {
                                              'route-map':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  },
                                              'filter-list':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  }
                                          },
                                      'entries':
                                          {
                                              'AS-PATH':
                                                  {
                                                      'total_entries': 3,
                                                      'memory_usage': 120
                                                  },
                                              'rrinfo':
                                                  {
                                                      'total_entries': 2,
                                                      'memory_usage': 48
                                                  }
                                          },
                                      'community_entries':
                                          {'total_entries': 4,
                                           'memory_usage': 96,
                                           },
                                      'total_memory': 9384,
                                      'activity_prefixes': '85/25',
                                      'activity_paths': '120/30',
                                      'scan_interval': 60,
                                      'route_identifier': '4.4.4.4',
                                      'routing_table_version': 56,
                                      'state_pfxrcd': '10',
                                      'tbl_ver': 56,
                                      'up_down': '01:12:00',
                                      'version': 4},
                                'vpnv6 unicast':
                                    {'as': 100,
                                      'attribute_entries': '6/4',
                                      'bgp_table_version': 66,
                                      'input_queue': 0,
                                      'local_as': 100,
                                      'msg_rcvd': 82,
                                      'msg_sent': 88,
                                      'output_queue': 0,
                                      'path': {'memory_usage': 4860,
                                               'total_entries': 45},
                                      'prefixes':
                                          {'memory_usage': 5280,
                                           'total_entries': 30},
                                      'cache_entries':
                                          {
                                              'route-map':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  },
                                              'filter-list':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  }
                                          },
                                      'entries':
                                          {
                                              'AS-PATH':
                                                  {
                                                      'total_entries': 3,
                                                      'memory_usage': 120
                                                  },
                                              'rrinfo':
                                                  {
                                                      'total_entries': 2,
                                                      'memory_usage': 48
                                                  }
                                          },
                                      'community_entries':
                                          {'total_entries': 4,
                                           'memory_usage': 96,
                                           },
                                      'total_memory': 11364,
                                      'activity_prefixes': '85/25',
                                      'activity_paths': '120/30',
                                      'scan_interval': 60,
                                      'route_identifier': '4.4.4.4',
                                      'routing_table_version': 66,
                                      'state_pfxrcd': '10',
                                      'tbl_ver': 66,
                                      'up_down': '01:12:00',
                                      'version': 4}
                                }
                           },
                      '3.3.3.3':
                           {'address_family':
                                {'vpnv4 unicast':
                                     {'as': 100,
                                      'attribute_entries': '6/4',
                                      'bgp_table_version': 56,
                                      'input_queue': 0,
                                      'local_as': 100,
                                      'msg_rcvd': 82,
                                      'msg_sent': 89,
                                      'output_queue': 0,
                                      'path': {'memory_usage': 3600,
                                               'total_entries': 45},
                                      'prefixes':
                                          {'memory_usage': 4560,
                                           'total_entries': 30},
                                      'cache_entries':
                                          {
                                              'route-map':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  },
                                              'filter-list':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  }
                                          },
                                      'entries':
                                          {
                                              'AS-PATH':
                                                  {
                                                      'total_entries': 3,
                                                      'memory_usage': 120
                                                  },
                                              'rrinfo':
                                                  {
                                                      'total_entries': 2,
                                                      'memory_usage': 48
                                                  }
                                          },
                                      'community_entries':
                                          {'total_entries': 4,
                                           'memory_usage': 96,
                                           },
                                      'total_memory': 9384,
                                      'activity_prefixes': '85/25',
                                      'activity_paths': '120/30',
                                      'scan_interval': 60,
                                      'route_identifier': '4.4.4.4',
                                      'routing_table_version': 56,
                                      'state_pfxrcd': '10',
                                      'tbl_ver': 56,
                                      'up_down': '01:12:06',
                                      'version': 4},
                                 'vpnv6 unicast':
                                     {'as': 100,
                                      'attribute_entries': '6/4',
                                      'bgp_table_version': 66,
                                      'input_queue': 0,
                                      'local_as': 100,
                                      'msg_rcvd': 82,
                                      'msg_sent': 89,
                                      'output_queue': 0,
                                      'path': {'memory_usage': 4860,
                                               'total_entries': 45},
                                      'prefixes':
                                          {'memory_usage': 5280,
                                           'total_entries': 30},
                                      'cache_entries':
                                          {
                                              'route-map':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  },
                                              'filter-list':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  }
                                          },
                                      'entries':
                                          {
                                              'AS-PATH':
                                                  {
                                                      'total_entries': 3,
                                                      'memory_usage': 120
                                                  },
                                              'rrinfo':
                                                  {
                                                      'total_entries': 2,
                                                      'memory_usage': 48
                                                  }
                                          },
                                      'community_entries':
                                          {'total_entries': 4,
                                           'memory_usage': 96,
                                           },
                                      'total_memory': 11364,
                                      'activity_prefixes': '85/25',
                                      'activity_paths': '120/30',
                                      'scan_interval': 60,
                                      'route_identifier': '4.4.4.4',
                                      'routing_table_version': 66,
                                      'state_pfxrcd': '10',
                                      'tbl_ver': 66,
                                      'up_down': '01:12:06',
                                      'version': 4}
                                 }},
                      '10.4.6.6':
                           {'address_family':
                                {'vpnv4 unicast':
                                     {'as': 300,
                                      'attribute_entries': '6/4',
                                      'bgp_table_version': 56,
                                      'input_queue': 0,
                                      'local_as': 100,
                                      'msg_rcvd': 68,
                                      'msg_sent': 75,
                                      'output_queue': 0,
                                      'path': {'memory_usage': 3600,
                                               'total_entries': 45},
                                      'prefixes':
                                          {'memory_usage': 4560,
                                           'total_entries': 30},
                                      'cache_entries':
                                          {
                                              'route-map':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  },
                                              'filter-list':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  }
                                          },
                                      'entries':
                                          {
                                              'AS-PATH':
                                                  {
                                                      'total_entries': 3,
                                                      'memory_usage': 120
                                                  },
                                              'rrinfo':
                                                  {
                                                      'total_entries': 2,
                                                      'memory_usage': 48
                                                  }
                                          },
                                      'community_entries':
                                          {'total_entries': 4,
                                           'memory_usage': 96,
                                           },
                                      'total_memory': 9384,
                                      'activity_prefixes': '85/25',
                                      'activity_paths': '120/30',
                                      'scan_interval': 60,
                                      'route_identifier': '4.4.4.4',
                                      'routing_table_version': 56,
                                      'state_pfxrcd': '5',
                                      'tbl_ver': 56,
                                      'up_down': '01:03:23',
                                      'version': 4}}},
                      '20.4.6.6':
                           {'address_family':
                                {'vpnv4 unicast':
                                     {'as': 400,
                                      'attribute_entries': '6/4',
                                      'bgp_table_version': 56,
                                      'input_queue': 0,
                                      'local_as': 100,
                                      'msg_rcvd': 67,
                                      'msg_sent': 72,
                                      'output_queue': 0,
                                      'path': {'memory_usage': 3600,
                                               'total_entries': 45},
                                      'prefixes':
                                          {'memory_usage': 4560,
                                           'total_entries': 30},
                                      'cache_entries':
                                          {
                                              'route-map':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  },
                                              'filter-list':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  }
                                          },
                                      'entries':
                                          {
                                              'AS-PATH':
                                                  {
                                                      'total_entries': 3,
                                                      'memory_usage': 120
                                                  },
                                              'rrinfo':
                                                  {
                                                      'total_entries': 2,
                                                      'memory_usage': 48
                                                  }
                                          },
                                      'community_entries':
                                          {'total_entries': 4,
                                           'memory_usage': 96,
                                           },
                                      'total_memory': 9384,
                                      'activity_prefixes': '85/25',
                                      'activity_paths': '120/30',
                                      'scan_interval': 60,
                                      'route_identifier': '4.4.4.4',
                                      'routing_table_version': 56,
                                      'state_pfxrcd': '5',
                                      'tbl_ver': 56,
                                      'up_down': '01:03:14',
                                      'version': 4}}},
                      '2001:DB8:4:6::6':
                           {'address_family':
                                {'vpnv6 unicast':
                                     {'as': 300,
                                      'attribute_entries': '6/4',
                                      'bgp_table_version': 66,
                                      'input_queue': 0,
                                      'local_as': 100,
                                      'msg_rcvd': 67,
                                      'msg_sent': 75,
                                      'output_queue': 0,
                                      'path': {'memory_usage': 4860,
                                               'total_entries': 45},
                                      'prefixes':
                                          {'memory_usage': 5280,
                                           'total_entries': 30},
                                      'cache_entries':
                                          {
                                              'route-map':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  },
                                              'filter-list':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  }
                                          },
                                      'entries':
                                          {
                                              'AS-PATH':
                                                  {
                                                      'total_entries': 3,
                                                      'memory_usage': 120
                                                  },
                                              'rrinfo':
                                                  {
                                                      'total_entries': 2,
                                                      'memory_usage': 48
                                                  }
                                          },
                                      'community_entries':
                                          {'total_entries': 4,
                                           'memory_usage': 96,
                                           },
                                      'total_memory': 11364,
                                      'activity_prefixes': '85/25',
                                      'activity_paths': '120/30',
                                      'scan_interval': 60,
                                      'route_identifier': '4.4.4.4',
                                      'routing_table_version': 66,
                                      'state_pfxrcd': '5',
                                      'tbl_ver': 66,
                                      'up_down': '01:03:19',
                                      'version': 4}
                                 }},
                      '2001:DB8:20:4:6::6':
                           {'address_family':
                                {'vpnv6 unicast':
                                     {'as': 400,
                                      'attribute_entries': '6/4',
                                      'bgp_table_version': 66,
                                      'input_queue': 0,
                                      'local_as': 100,
                                      'msg_rcvd': 67,
                                      'msg_sent': 73,
                                      'output_queue': 0,
                                      'path': {'memory_usage': 4860,
                                               'total_entries': 45},
                                      'prefixes':
                                          {'memory_usage': 5280,
                                           'total_entries': 30},
                                      'cache_entries':
                                          {
                                              'route-map':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  },
                                              'filter-list':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  }
                                          },
                                      'entries':
                                          {
                                              'AS-PATH':
                                                  {
                                                      'total_entries': 3,
                                                      'memory_usage': 120
                                                  },
                                              'rrinfo':
                                                  {
                                                      'total_entries': 2,
                                                      'memory_usage': 48
                                                  }
                                          },
                                      'community_entries':
                                          {'total_entries': 4,
                                           'memory_usage': 96,
                                           },
                                      'total_memory': 11364,
                                      'activity_prefixes': '85/25',
                                      'activity_paths': '120/30',
                                      'scan_interval': 60,
                                      'route_identifier': '4.4.4.4',
                                      'routing_table_version': 66,
                                      'state_pfxrcd': '5',
                                      'tbl_ver': 66,
                                      'up_down': '01:03:11',
                                      'version': 4}
                                 }
                           }

                      }
                 }
            }
        }

    golden_output_2 = {'execute.return_value': '''
        For address family: VPNv4 Unicast
        BGP router identifier 4.4.4.4, local AS number 100
        BGP table version is 56, main routing table version 56
        30 network entries using 4560 bytes of memory
        45 path entries using 3600 bytes of memory
        6/4 BGP path/bestpath attribute entries using 960 bytes of memory
        2 BGP rrinfo entries using 48 bytes of memory
        3 BGP AS-PATH entries using 120 bytes of memory
        4 BGP extended community entries using 96 bytes of memory
        0 BGP route-map cache entries using 0 bytes of memory
        0 BGP filter-list cache entries using 0 bytes of memory
        BGP using 9384 total bytes of memory
        BGP activity 85/25 prefixes, 120/30 paths, scan interval 60 secs

        Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        2.2.2.2         4          100      82      88       56    0    0 01:12:00       10
        3.3.3.3         4          100      82      89       56    0    0 01:12:06       10
        10.4.6.6        4          300      68      75       56    0    0 01:03:23        5
        20.4.6.6        4          400      67      72       56    0    0 01:03:14        5

        For address family: VPNv6 Unicast
        BGP router identifier 4.4.4.4, local AS number 100
        BGP table version is 66, main routing table version 66
        30 network entries using 5280 bytes of memory
        45 path entries using 4860 bytes of memory
        6/4 BGP path/bestpath attribute entries using 960 bytes of memory
        2 BGP rrinfo entries using 48 bytes of memory
        3 BGP AS-PATH entries using 120 bytes of memory
        4 BGP extended community entries using 96 bytes of memory
        0 BGP route-map cache entries using 0 bytes of memory
        0 BGP filter-list cache entries using 0 bytes of memory
        BGP using 11364 total bytes of memory
        BGP activity 85/25 prefixes, 120/30 paths, scan interval 60 secs

        Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        2.2.2.2         4          100      82      88       66    0    0 01:12:00       10
        3.3.3.3         4          100      82      89       66    0    0 01:12:06       10
        2001:DB8:4:6::6 4          300      67      75       66    0    0 01:03:19        5
        2001:DB8:20:4:6::6
                4          400      67      73       66    0    0 01:03:11        5


            '''}
    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        bgp_summary_obj = ShowBgpAllSummary(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = bgp_summary_obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowBgpAllSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowBgpAllSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)


class test_show_bgp_all_cluster_ids(unittest.TestCase):
    '''
        unit test for  show bgp all cluster_ids
    '''
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        'vrf':
            {'default':
                {
                    'cluster_id': '4.4.4.4',
                    'configured_id': '0.0.0.0',
                    'reflection_all_configured': 'enabled',
                    'reflection_intra_cluster_configured': 'enabled',
                    'reflection_intra_cluster_used': 'enabled',
                },
                'vrf1':
                {
                    'cluster_id': '4.4.4.4',
                    'configured_id': '0.0.0.0',
                    'reflection_all_configured': 'enabled',
                    'reflection_intra_cluster_configured': 'enabled',
                    'reflection_intra_cluster_used': 'enabled',

                },
                'vrf2':
                    {
                    'cluster_id': '4.4.4.4',
                    'configured_id': '0.0.0.0',
                    'reflection_all_configured': 'enabled',
                    'reflection_intra_cluster_configured': 'enabled',
                    'reflection_intra_cluster_used': 'enabled',

                    }
            }
    }

    golden_output = {'execute.return_value': '''
        R4_iosv#show vrf detail | inc \(VRF
        VRF VRF1 (VRF Id = 1); default RD 300:1; default VPNID <not set>
        VRF VRF2 (VRF Id = 2); default RD 400:1; default VPNID <not set>

        R4_iosv#show bgp all cluster-ids
        Global cluster-id: 4.4.4.4 (configured: 0.0.0.0)
        BGP client-to-client reflection:         Configured    Used
         all (inter-cluster and intra-cluster): ENABLED
         intra-cluster:                         ENABLED       ENABLED

        List of cluster-ids:
        Cluster-id     #-neighbors C2C-rfl-CFG C2C-rfl-USE
        '''}

    golden_parsed_output_1 = {
        'vrf':
            {'default':
                {
                    'cluster_id': '4.4.4.4',
                    'configured_id': '0.0.0.0',
                    'reflection_all_configured': 'enabled',
                    'reflection_intra_cluster_configured': 'enabled',
                    'reflection_intra_cluster_used': 'enabled',
                }
            }
    }

    golden_output_1 = {'execute.return_value': '''
           R4_iosv#show vrf detail | inc \(VRF
           % unmatched ()
           % Failed to compile regular expression.

           R4_iosv#show bgp all cluster-ids
           Global cluster-id: 4.4.4.4 (configured: 0.0.0.0)
           BGP client-to-client reflection:         Configured    Used
            all (inter-cluster and intra-cluster): ENABLED
            intra-cluster:                         ENABLED       ENABLED

           List of cluster-ids:
           Cluster-id     #-neighbors C2C-rfl-CFG C2C-rfl-USE
           '''}

    golden_parsed_output_2 = {
        'vrf':
            {'default':
                {
                    'cluster_id': '4.4.4.4',
                    'configured_id': '0.0.0.0',
                    'reflection_all_configured': 'enabled',
                    'reflection_intra_cluster_configured': 'enabled',
                    'reflection_intra_cluster_used': 'enabled',
                    'list_of_cluster_ids':
                        {
                           '192.168.1.1':
                               {
                                   'num_neighbors': 2,
                                   'client_to_client_reflection_configured': 'disabled',
                                   'client_to_client_reflection_used': 'disabled',
                               },
                            '192.168.2.2':
                                {
                                    'num_neighbors': 2,
                                    'client_to_client_reflection_configured': 'disabled',
                                    'client_to_client_reflection_used': 'disabled',
                                },

                        }
                },
                'vrf1':
                    {
                        'cluster_id': '4.4.4.4',
                        'configured_id': '0.0.0.0',
                        'reflection_all_configured': 'enabled',
                        'reflection_intra_cluster_configured': 'enabled',
                        'reflection_intra_cluster_used': 'enabled',
                        'list_of_cluster_ids':
                            {
                                '192.168.1.1':
                                    {
                                        'num_neighbors': 2,
                                        'client_to_client_reflection_configured': 'disabled',
                                        'client_to_client_reflection_used': 'disabled',
                                    },
                                '192.168.2.2':
                                    {
                                        'num_neighbors': 2,
                                        'client_to_client_reflection_configured': 'disabled',
                                        'client_to_client_reflection_used': 'disabled',
                                    },

                            }
                    },
                'vrf2':
                    {
                        'cluster_id': '4.4.4.4',
                        'configured_id': '0.0.0.0',
                        'reflection_all_configured': 'enabled',
                        'reflection_intra_cluster_configured': 'enabled',
                        'reflection_intra_cluster_used': 'enabled',
                        'list_of_cluster_ids':
                            {
                                '192.168.1.1':
                                    {
                                        'num_neighbors': 2,
                                        'client_to_client_reflection_configured': 'disabled',
                                        'client_to_client_reflection_used': 'disabled',
                                    },
                                '192.168.2.2':
                                    {
                                        'num_neighbors': 2,
                                        'client_to_client_reflection_configured': 'disabled',
                                        'client_to_client_reflection_used': 'disabled',
                                    },

                            }
                    }
            }
    }

    golden_output_2 = {'execute.return_value': '''
               R4_iosv#show vrf detail | inc \(VRF
               VRF VRF1 (VRF Id = 1); default RD 300:1; default VPNID <not set>
               VRF VRF2 (VRF Id = 2); default RD 400:1; default VPNID <not set>

               R4_iosv#show bgp all cluster-ids
               Global cluster-id: 4.4.4.4 (configured: 0.0.0.0)
               BGP client-to-client reflection:         Configured    Used
                all (inter-cluster and intra-cluster): ENABLED
                intra-cluster:                         ENABLED       ENABLED

               List of cluster-ids:
               Cluster-id     #-neighbors C2C-rfl-CFG C2C-rfl-USE
               192.168.1.1                2 DISABLED    DISABLED
               192.168.2.2                2 DISABLED    DISABLED
               '''}


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpAllClusterIds(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowBgpAllClusterIds(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowBgpAllClusterIds(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowBgpAllClusterIds(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

"""
class test_show_bgp_all_neighbores(unittest.TestCase):
    '''
        unit test for  show bgp all neighbors
    '''
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vrf':
            {'default':
                 {
                 'neighbor':
                      {'2.2.2.2':
                         {'remote_as': 100,
                          'link': 'internal',
                          'bgp_version':4,
                          'router_id': '2.2.2.2',
                          'session_state':'established' ,
                          'shutdown': False,

                          'bgp_negotiated_keepalive_timers':
                              {
                               'keepalive_interval': 60,
                               'hold_time': 180,
                               },
                          'bgp_session_transport':
                              {'connection':
                                   {
                                    'last_reset': 'never',
                                    'established': 1,
                                    'dropped': 0,
                                    },
                               'transport':
                                   {'local_host': '4.4.4.4',
                                    'local_port': '35281',
                                    'foreign_host': '2.2.2.2',
                                    'foreign_port': '179',
                                    },
                               },
                          'bgp_neighbor_counters':
                              {'messages':
                                   {
                                    'sent':
                                        {
                                            'opens': 1,
                                            'updates': 11,
                                            'notifications': 0,
                                            'keepalives': 75,
                                            'route_refresh': 0,
                                            'total': 87,
                                         },
                                    'received':
                                        {
                                            'opens': 1,
                                            'updates': 6,
                                            'notifications': 0,
                                            'keepalives': 74,
                                            'route_refresh': 0,
                                            'total':81,
                                         },
                                       'input_queue': 0,
                                       'output_queue': 0,
                                    },

                               },
                          'bgp_negotiated_capabilities':
                              {'route_refresh': 'advertised and received(new)',
                               'vpnv4_unicast': 'advertised and received',
                               'vpnv6_unicast': 'advertised and received',
                               'graceful_restart': 'received',
                               'enhanced_refresh': 'advertised',
                               'four_octets_asn': 'advertised and received',
                               'stateful_switchover': 'enabled',
                               },
                          'bgp_event_timer':
                               {
                                'starts':
                                   {
                                       'retrans': 86,
                                       'timewait': 0,
                                       'ackhold': 80,
                                       'sendwnd': 0,
                                       'keepalive': 0,
                                       'giveup': 0,
                                       'pmtuager': 1,
                                       'deadwait': 0,
                                       'linger': 0,
                                       'processq': 0,
                                   },
                                'wakeups':
                                   {
                                       'retrans': 0,
                                       'timewait': 0,
                                       'ackhold': 72,
                                       'sendwnd': 0,
                                       'keepalive': 0,
                                       'giveup': 0,
                                       'pmtuager': 1,
                                       'deadwait': 0,
                                       'linger': 0,
                                       'processq': 0,
                                   },
                                'next':
                                   {
                                       'retrans': '0x0',
                                       'timewait': '0x0',
                                       'ackhold': '0x0',
                                       'sendwnd': '0x0',
                                       'keepalive': '0x0',
                                       'giveup': '0x0',
                                       'pmtuager': '0x0',
                                       'deadwait': '0x0',
                                       'linger': '0x0',
                                       'processq': '0x0',
                                   },
                               },
                          'address_family':
                              {'vpnv4 unicast':
                                   {
                                       'last_read': '00:00:04',
                                       'last_written': '00:00:09',
                                       'up_time': '01:10:35',
                               },
                          },
                     },
                 },
            },
        },
    }

    golden_output = {'execute.return_value': '''
        For address family: IPv4 Unicast

        For address family: IPv6 Unicast

        For address family: VPNv4 Unicast
        BGP neighbor is 2.2.2.2,  remote AS 100, internal link
          BGP version 4, remote router ID 2.2.2.2
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

          Address tracking is enabled, the RIB does have a route to 2.2.2.2
          Connections established 1; dropped 0
          Last reset never
          Transport(tcp) path-mtu-discovery is enabled
          Graceful-Restart is disabled
        Connection state is ESTAB, I/O status: 1, unread input bytes: 0
        Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 255
        Local host: 4.4.4.4, Local port: 35281
        Foreign host: 2.2.2.2, Foreign port: 179
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
        '''}
    golden_parsed_output_1 = {
        'vrf':
            {'default':
                {
                    'neighbor':
                        {'2.2.2.2':
                             {'remote_as': 100,
                              'link': 'internal',
                              'bgp_version': 4,
                              'router_id': '2.2.2.2',
                              'session_state': 'established',
                              'shutdown': False,
                              'bgp_negotiated_keepalive_timers':
                                  {
                                   'keepalive_interval': 60,
                                   'hold_time': 180,
                                   },
                              'bgp_session_transport':
                                  {'connection':
                                      {
                                          'last_reset': 'never',
                                          # 'reset_reason': str,
                                          'established': 1,
                                          'dropped': 0,
                                      },
                                      'transport':
                                          {'local_host': '4.4.4.4',
                                           'local_port': '35281',
                                           'foreign_host': '2.2.2.2',
                                           'foreign_port': '179',
                                           },
                                  },
                              'bgp_neighbor_counters':
                                  {'messages':
                                      {
                                          'sent':
                                              {
                                                  'opens': 1,
                                                  'updates': 11,
                                                  'notifications': 0,
                                                  'keepalives': 75,
                                                  'route_refresh': 0,
                                                  'total': 87,
                                              },
                                          'received':
                                              {
                                                  'opens': 1,
                                                  'updates': 6,
                                                  'notifications': 0,
                                                  'keepalives': 74,
                                                  'route_refresh': 0,
                                                  'total': 81,
                                              },
                                          'input_queue': 0,
                                          'output_queue': 0,
                                      },

                                  },
                              'bgp_negotiated_capabilities':
                                  {'route_refresh': 'advertised and received(new)',
                                   'vpnv4_unicast': 'advertised and received',
                                   'vpnv6_unicast': 'advertised and received',
                                   'graceful_restart': 'received',
                                   'enhanced_refresh': 'advertised',
                                   'four_octets_asn': 'advertised and received',
                                   'stateful_switchover': 'enabled',
                                   },
                              'bgp_event_timer':
                                  {
                                      'starts':
                                          {
                                              'retrans': 86,
                                              'timewait': 0,
                                              'ackhold': 80,
                                              'sendwnd': 0,
                                              'keepalive': 0,
                                              'giveup': 0,
                                              'pmtuager': 1,
                                              'deadwait': 0,
                                              'linger': 0,
                                              'processq': 0,
                                          },
                                      'wakeups':
                                          {
                                              'retrans': 0,
                                              'timewait': 0,
                                              'ackhold': 72,
                                              'sendwnd': 0,
                                              'keepalive': 0,
                                              'giveup': 0,
                                              'pmtuager': 1,
                                              'deadwait': 0,
                                              'linger': 0,
                                              'processq': 0,
                                          },
                                      'next':
                                          {
                                              'retrans': '0x0',
                                              'timewait': '0x0',
                                              'ackhold': '0x0',
                                              'sendwnd': '0x0',
                                              'keepalive': '0x0',
                                              'giveup': '0x0',
                                              'pmtuager': '0x0',
                                              'deadwait': '0x0',
                                              'linger': '0x0',
                                              'processq': '0x0',
                                          },
                                  },
                              'address_family':
                                  {'vpnv4 unicast':
                                      {
                                          'last_read': '00:00:04',
                                          'last_written': '00:00:09',
                                          'up_time': '01:10:35',
                                      },
                                  'vpnv6 unicast':
                                      {
                                          'last_read': '00:00:07',
                                          'last_written': '00:00:12',
                                          'up_time': '01:10:38',
                                      },

                                  },
                              },
                        '3.3.3.3':
                             {'remote_as': 100,
                              'link': 'internal',
                              'bgp_version': 4,
                              'router_id': '3.3.3.3',
                              'session_state': 'established',
                              'shutdown': False,

                              'bgp_negotiated_keepalive_timers':
                                  {
                                   #'last_read': '00:00:04',
                                   'keepalive_interval': 60,
                                   'hold_time': 180,
                                   #'last_written': '00:00:43',
                                   },
                              'bgp_session_transport':
                                  {'connection':
                                      {
                                          'last_reset': 'never',
                                          # 'reset_reason': str,
                                          'established': 1,
                                          'dropped': 0,
                                      },
                                      'transport':
                                          {'local_host': '4.4.4.4',
                                           'local_port': '56031',
                                           'foreign_host': '3.3.3.3',
                                           'foreign_port': '179',
                                           },
                                  },
                              'bgp_neighbor_counters':
                                  {'messages':
                                      {
                                          'sent':
                                              {
                                                  'opens': 1,
                                                  'updates': 11,
                                                  'notifications': 0,
                                                  'keepalives': 75,
                                                  'route_refresh': 0,
                                                  'total': 87,
                                              },
                                          'received':
                                              {
                                                  'opens': 1,
                                                  'updates': 6,
                                                  'notifications': 0,
                                                  'keepalives': 74,
                                                  'route_refresh': 0,
                                                  'total': 81,
                                              },
                                          'input_queue': 0,
                                          'output_queue': 0,
                                      },

                                  },
                              'bgp_negotiated_capabilities':
                                  {'route_refresh': 'advertised and received(new)',
                                   'vpnv4_unicast': 'advertised and received',
                                   'vpnv6_unicast': 'advertised and received',
                                   'graceful_restart': 'received',
                                   'enhanced_refresh': 'advertised',
                                   # 'multisession': '',
                                   'four_octets_asn': 'advertised and received',
                                   'stateful_switchover': 'enabled',
                                   },
                              'bgp_event_timer':
                                  {
                                      'starts':
                                          {
                                              'retrans': 86,
                                              'timewait': 0,
                                              'ackhold': 80,
                                              'sendwnd': 0,
                                              'keepalive': 0,
                                              'giveup': 0,
                                              'pmtuager': 1,
                                              'deadwait': 0,
                                              'linger': 0,
                                              'processq': 0,
                                          },
                                      'wakeups':
                                          {
                                              'retrans': 0,
                                              'timewait': 0,
                                              'ackhold': 73,
                                              'sendwnd': 0,
                                              'keepalive': 0,
                                              'giveup': 0,
                                              'pmtuager': 1,
                                              'deadwait': 0,
                                              'linger': 0,
                                              'processq': 0,
                                          },
                                      'next':
                                          {
                                              'retrans': '0x0',
                                              'timewait': '0x0',
                                              'ackhold': '0x0',
                                              'sendwnd': '0x0',
                                              'keepalive': '0x0',
                                              'giveup': '0x0',
                                              'pmtuager': '0x0',
                                              'deadwait': '0x0',
                                              'linger': '0x0',
                                              'processq': '0x0',
                                          },
                                  },
                              'address_family':
                                  {'vpnv4 unicast':
                                      {
                                          'last_read': '00:00:04',
                                          'last_written': '00:00:43',
                                          'up_time': '01:10:41',
                                      },
                                  'vpnv6 unicast':
                                      {
                                          'last_read': '00:00:08',
                                          'last_written': '00:00:47',
                                          'up_time': '01:10:44',
                                      },
                                  },
                              },
                        },
                },
            'vrf1':
                {
                    'neighbor':
                        {'10.4.6.6':
                             {'remote_as': 300,
                              'link': 'external',
                              'bgp_version': 4,
                              'router_id': '10.4.6.6',
                              'session_state': 'established',
                              'shutdown': False,
                              'bgp_negotiated_keepalive_timers':
                                  {
                                      'keepalive_interval': 60,
                                      'hold_time': 180,

                                  },
                              'bgp_session_transport':
                                  {
                                      'connection':
                                          {
                                              'last_reset': '01:02:11',
                                              'reset_reason': 'Peer closed the session of session 1',
                                              'established': 2,
                                              'dropped': 1,
                                          },
                                      'transport':
                                          {
                                              'local_host': '10.4.6.4',
                                              'local_port': '179',
                                              'foreign_host': '10.4.6.6',
                                              'foreign_port': '11010',
                                          },
                                  },
                              'bgp_neighbor_counters':
                                  {'messages':
                                      {
                                          'sent':
                                              {
                                                  'opens': 1,
                                                  'updates': 3,
                                                  'notifications': 0,
                                                  'keepalives': 69,
                                                  'route_refresh': 0,
                                                  'total': 73,
                                              },
                                          'received':
                                              {
                                                  'opens': 1,
                                                  'updates': 1,
                                                  'notifications': 0,
                                                  'keepalives': 64,
                                                  'route_refresh': 0,
                                                  'total': 66,
                                              },
                                          'input_queue': 0,
                                          'output_queue': 0,
                                      },

                                  },
                              'bgp_negotiated_capabilities':
                                  {'route_refresh': 'advertised',
                                   'ipv4_unicast': 'advertised and received',
                                   'enhanced_refresh': 'advertised',
                                   'four_octets_asn': 'advertised',
                                   'stateful_switchover': 'enabled',
                                   },
                              'bgp_event_timer':
                                  {
                                      'starts':
                                          {
                                              'retrans': 71,
                                              'timewait': 0,
                                              'ackhold': 66,
                                              'sendwnd': 0,
                                              'keepalive': 0,
                                              'giveup': 0,
                                              'pmtuager': 0,
                                              'deadwait': 0,
                                              'linger': 0,
                                              'processq': 0,
                                          },
                                      'wakeups':
                                          {
                                              'retrans': 0,
                                              'timewait': 0,
                                              'ackhold': 64,
                                              'sendwnd': 0,
                                              'keepalive': 0,
                                              'giveup': 0,
                                              'pmtuager': 0,
                                              'deadwait': 0,
                                              'linger': 0,
                                              'processq': 0,
                                          },
                                      'next':
                                          {
                                              'retrans': '0x0',
                                              'timewait': '0x0',
                                              'ackhold': '0x0',
                                              'sendwnd': '0x0',
                                              'keepalive': '0x0',
                                              'giveup': '0x0',
                                              'pmtuager': '0x0',
                                              'deadwait': '0x0',
                                              'linger': '0x0',
                                              'processq': '0x0',
                                          },
                                  },
                              'address_family':
                                  {'vpnv4 unicast':
                                      {
                                          'last_read': '00:00:33',
                                          'last_written': '00:00:30',
                                          'up_time': '01:01:59',
                                      },
                                  },
                              },
                         '2001:DB8:4:6::6':
                             {'remote_as': 300,
                              'link': 'external',
                              'bgp_version': 4,
                              'router_id': '10.4.6.6',
                              'session_state': 'established',
                              'shutdown': False,
                              'bgp_negotiated_keepalive_timers':
                                  {
                                      'keepalive_interval': 60,
                                      'hold_time': 180,
                                  },
                              'bgp_session_transport':
                                  {
                                      'connection':
                                          {
                                              'last_reset': '01:05:12',
                                              'reset_reason': 'Active open failed',
                                              'established': 2,
                                              'dropped': 1,
                                          },
                                      'transport':
                                          {
                                              'local_host': '2001:DB8:4:6::4',
                                              'local_port': '179',
                                              'foreign_host': '2001:DB8:4:6::6',
                                              'foreign_port': '11003',
                                          },
                                  },
                              'bgp_neighbor_counters':
                                  {'messages':
                                      {
                                          'sent':
                                              {
                                                  'opens': 1,
                                                  'updates': 3,
                                                  'notifications': 0,
                                                  'keepalives': 70,
                                                  'route_refresh': 0,
                                                  'total': 74,
                                              },
                                          'received':
                                              {
                                                  'opens': 1,
                                                  'updates': 1,
                                                  'notifications': 0,
                                                  'keepalives': 64,
                                                  'route_refresh': 0,
                                                  'total': 66,
                                              },
                                          'input_queue': 0,
                                          'output_queue': 0,
                                      },

                                  },
                              'bgp_negotiated_capabilities':
                                  {'route_refresh': 'advertised',
                                   'ipv6_unicast': 'advertised and received',
                                   'enhanced_refresh': 'advertised',
                                   'four_octets_asn': 'advertised',
                                   'stateful_switchover': 'enabled',
                                   },
                              'bgp_event_timer':
                                  {
                                      'starts':
                                          {
                                              'retrans': 72,
                                              'timewait': 0,
                                              'ackhold': 66,
                                              'sendwnd': 0,
                                              'keepalive': 0,
                                              'giveup': 0,
                                              'pmtuager': 0,
                                              'deadwait': 0,
                                              'linger': 0,
                                              'processq': 0,
                                          },
                                      'wakeups':
                                          {
                                              'retrans': 0,
                                              'timewait': 0,
                                              'ackhold': 64,
                                              'sendwnd': 0,
                                              'keepalive': 0,
                                              'giveup': 0,
                                              'pmtuager': 0,
                                              'deadwait': 0,
                                              'linger': 0,
                                              'processq': 0,
                                          },
                                      'next':
                                          {
                                              'retrans': '0x0',
                                              'timewait': '0x0',
                                              'ackhold': '0x0',
                                              'sendwnd': '0x0',
                                              'keepalive': '0x0',
                                              'giveup': '0x0',
                                              'pmtuager': '0x0',
                                              'deadwait': '0x0',
                                              'linger': '0x0',
                                              'processq': '0x0',
                                          },
                                  },
                              'address_family':
                                  {'vpnv6 unicast':
                                      {
                                          'last_read': '00:00:32',
                                          'last_written': '00:00:06',
                                          'up_time': '01:01:58',
                                      },
                                  },
                              },
                         },
                },
            'vrf2':
                {
                    'neighbor':
                        {'20.4.6.6':
                             {'remote_as': 400,
                              'link': 'external',
                              'bgp_version': 4,
                              'router_id': '20.4.6.6',
                              'session_state': 'established',
                              'shutdown': False,
                              'bgp_negotiated_keepalive_timers':
                                  {
                                      'keepalive_interval': 60,
                                      'hold_time': 180,
                                  },
                              'bgp_session_transport':
                                  {
                                      'connection':
                                          {
                                              'last_reset': '01:05:09',
                                              'reset_reason': 'Active open failed',
                                              'established': 2,
                                              'dropped': 1,
                                          },
                                      'transport':
                                          {
                                              'local_host': '20.4.6.4',
                                              'local_port': '179',
                                              'foreign_host': '20.4.6.6',
                                              'foreign_port': '11003',
                                          },
                                  },
                              'bgp_neighbor_counters':
                                  {'messages':
                                      {
                                          'sent':
                                              {
                                                  'opens': 1,
                                                  'updates': 1,
                                                  'notifications': 0,
                                                  'keepalives': 69,
                                                  'route_refresh': 0,
                                                  'total': 71,
                                              },
                                          'received':
                                              {
                                                  'opens': 1,
                                                  'updates': 1,
                                                  'notifications': 0,
                                                  'keepalives': 64,
                                                  'route_refresh': 0,
                                                  'total': 66,
                                              },
                                          'input_queue': 0,
                                          'output_queue': 0,
                                      },

                                  },
                              'bgp_negotiated_capabilities':
                                  {'route_refresh': 'advertised',
                                   'ipv4_unicast': 'advertised and received',
                                   'enhanced_refresh': 'advertised',
                                   'four_octets_asn': 'advertised',
                                   'stateful_switchover': 'enabled',
                                   },
                              'bgp_event_timer':
                                  {
                                      'starts':
                                          {
                                              'retrans': 70,
                                              'timewait': 0,
                                              'ackhold': 66,
                                              'sendwnd': 0,
                                              'keepalive': 0,
                                              'giveup': 0,
                                              'pmtuager': 0,
                                              'deadwait': 0,
                                              'linger': 0,
                                              'processq': 0,
                                          },
                                      'wakeups':
                                          {
                                              'retrans': 0,
                                              'timewait': 0,
                                              'ackhold': 64,
                                              'sendwnd': 0,
                                              'keepalive': 0,
                                              'giveup': 0,
                                              'pmtuager': 0,
                                              'deadwait': 0,
                                              'linger': 0,
                                              'processq': 0,
                                          },
                                      'next':
                                          {
                                              'retrans': '0x0',
                                              'timewait': '0x0',
                                              'ackhold': '0x0',
                                              'sendwnd': '0x0',
                                              'keepalive': '0x0',
                                              'giveup': '0x0',
                                              'pmtuager': '0x0',
                                              'deadwait': '0x0',
                                              'linger': '0x0',
                                              'processq': '0x0',
                                          },
                                  },
                              'address_family':
                                  {'vpnv4 unicast':
                                      {
                                          'last_read': '00:00:24',
                                          'last_written': '00:00:21',
                                          'up_time': '01:01:51',
                                      },
                                  },
                              },
                         '2001:DB8:20:4:6::6':
                             {'remote_as': 400,
                              'link': 'external',
                              'bgp_version': 4,
                              'router_id': '20.4.6.6',
                              'session_state': 'established',
                              'shutdown': False,
                              'bgp_negotiated_keepalive_timers':
                                  {
                                      'keepalive_interval': 60,
                                      'hold_time': 180,
                                  },
                              'bgp_session_transport':
                                  {
                                      'connection':
                                          {
                                              'last_reset': '01:05:13',
                                              'reset_reason': 'Active open failed',
                                              'established': 2,
                                              'dropped': 1,
                                          },
                                      'transport':
                                          {
                                              'local_host': '2001:DB8:20:4:6::4',
                                              'local_port': '179',
                                              'foreign_host': '2001:DB8:20:4:6::6',
                                              'foreign_port': '11003',
                                          },
                                  },
                              'bgp_neighbor_counters':
                                  {'messages':
                                      {
                                          'sent':
                                              {
                                                  'opens': 1,
                                                  'updates': 1,
                                                  'notifications': 0,
                                                  'keepalives': 70,
                                                  'route_refresh': 0,
                                                  'total': 72,
                                              },
                                          'received':
                                              {
                                                  'opens': 1,
                                                  'updates': 1,
                                                  'notifications': 0,
                                                  'keepalives': 64,
                                                  'route_refresh': 0,
                                                  'total': 66,
                                              },
                                          'input_queue': 0,
                                          'output_queue': 0,
                                      },

                                  },
                              'bgp_negotiated_capabilities':
                                  {'route_refresh': 'advertised',
                                   'ipv6_unicast': 'advertised and received',
                                   'enhanced_refresh': 'advertised',
                                   'four_octets_asn': 'advertised',
                                   'stateful_switchover': 'enabled',
                                   },
                              'bgp_event_timer':
                                  {
                                      'starts':
                                          {
                                              'retrans': 71,
                                              'timewait': 0,
                                              'ackhold': 66,
                                              'sendwnd': 0,
                                              'keepalive': 0,
                                              'giveup': 0,
                                              'pmtuager': 0,
                                              'deadwait': 0,
                                              'linger': 0,
                                              'processq': 0,
                                          },
                                      'wakeups':
                                          {
                                              'retrans': 0,
                                              'timewait': 0,
                                              'ackhold': 64,
                                              'sendwnd': 0,
                                              'keepalive': 0,
                                              'giveup': 0,
                                              'pmtuager': 0,
                                              'deadwait': 0,
                                              'linger': 0,
                                              'processq': 0,
                                          },
                                      'next':
                                          {
                                              'retrans': '0x0',
                                              'timewait': '0x0',
                                              'ackhold': '0x0',
                                              'sendwnd': '0x0',
                                              'keepalive': '0x0',
                                              'giveup': '0x0',
                                              'pmtuager': '0x0',
                                              'deadwait': '0x0',
                                              'linger': '0x0',
                                              'processq': '0x0',
                                          },
                                  },
                              'address_family':
                                  {'vpnv6 unicast':
                                      {
                                          'last_read': '00:00:22',
                                          'last_written': '00:00:01',
                                          'up_time': '01:01:51',
                                      },
                                  },
                              },
                         },
                },

            },
    }
    golden_output_1 = {'execute.return_value': '''
            For address family: IPv4 Unicast

            For address family: IPv6 Unicast

            For address family: VPNv4 Unicast
            BGP neighbor is 2.2.2.2,  remote AS 100, internal link
              BGP version 4, remote router ID 2.2.2.2
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

              Address tracking is enabled, the RIB does have a route to 2.2.2.2
              Connections established 1; dropped 0
              Last reset never
              Transport(tcp) path-mtu-discovery is enabled
              Graceful-Restart is disabled
            Connection state is ESTAB, I/O status: 1, unread input bytes: 0
            Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 255
            Local host: 4.4.4.4, Local port: 35281
            Foreign host: 2.2.2.2, Foreign port: 179
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

            BGP neighbor is 3.3.3.3,  remote AS 100, internal link
              BGP version 4, remote router ID 3.3.3.3
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

              Address tracking is enabled, the RIB does have a route to 3.3.3.3
              Connections established 1; dropped 0
              Last reset never
              Transport(tcp) path-mtu-discovery is enabled
              Graceful-Restart is disabled
            Connection state is ESTAB, I/O status: 1, unread input bytes: 0
            Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 255
            Local host: 4.4.4.4, Local port: 56031
            Foreign host: 3.3.3.3, Foreign port: 179
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

            BGP neighbor is 20.4.6.6,  vrf VRF2,  remote AS 400, external link
              BGP version 4, remote router ID 20.4.6.6
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

              Address tracking is enabled, the RIB does have a route to 20.4.6.6
              Connections established 2; dropped 1
              Last reset 01:05:09, due to Active open failed
              Transport(tcp) path-mtu-discovery is enabled
              Graceful-Restart is disabled
            Connection state is ESTAB, I/O status: 1, unread input bytes: 0
            Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 1
            Local host: 20.4.6.4, Local port: 179
            Foreign host: 20.4.6.6, Foreign port: 11003
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
            BGP neighbor is 2.2.2.2,  remote AS 100, internal link
              BGP version 4, remote router ID 2.2.2.2
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

              Address tracking is enabled, the RIB does have a route to 2.2.2.2
              Connections established 1; dropped 0
              Last reset never
              Transport(tcp) path-mtu-discovery is enabled
              Graceful-Restart is disabled
            Connection state is ESTAB, I/O status: 1, unread input bytes: 0
            Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 255
            Local host: 4.4.4.4, Local port: 35281
            Foreign host: 2.2.2.2, Foreign port: 179
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

            BGP neighbor is 3.3.3.3,  remote AS 100, internal link
              BGP version 4, remote router ID 3.3.3.3
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

              Address tracking is enabled, the RIB does have a route to 3.3.3.3
              Connections established 1; dropped 0
              Last reset never
              Transport(tcp) path-mtu-discovery is enabled
              Graceful-Restart is disabled
            Connection state is ESTAB, I/O status: 1, unread input bytes: 0
            Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 255
            Local host: 4.4.4.4, Local port: 56031
            Foreign host: 3.3.3.3, Foreign port: 179
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
              BGP version 4, remote router ID 20.4.6.6
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

    golden_parsed_output_default = {
        'vrf':
            {'default':
                {
                    'neighbor':
                        {'2.2.2.2':
                             {'remote_as': 100,
                              'link': 'internal',
                              'bgp_version': 4,
                              'router_id': '2.2.2.2',
                              'session_state': 'established',
                              'shutdown': False,
                              'bgp_negotiated_keepalive_timers':
                                  {
                                      'keepalive_interval': 60,
                                      'hold_time': 180,
                                  },
                              'bgp_session_transport':
                                  {'connection':
                                      {
                                          'last_reset': 'never',
                                          # 'reset_reason': str,
                                          'established': 1,
                                          'dropped': 0,
                                      },
                                      'transport':
                                          {'local_host': '4.4.4.4',
                                           'local_port': '35281',
                                           'foreign_host': '2.2.2.2',
                                           'foreign_port': '179',
                                           },
                                  },
                              'bgp_neighbor_counters':
                                  {'messages':
                                      {
                                          'sent':
                                              {
                                                  'opens': 1,
                                                  'updates': 11,
                                                  'notifications': 0,
                                                  'keepalives': 75,
                                                  'route_refresh': 0,
                                                  'total': 87,
                                              },
                                          'received':
                                              {
                                                  'opens': 1,
                                                  'updates': 6,
                                                  'notifications': 0,
                                                  'keepalives': 74,
                                                  'route_refresh': 0,
                                                  'total': 81,
                                              },
                                          'input_queue': 0,
                                          'output_queue': 0,
                                      },

                                  },
                              'bgp_negotiated_capabilities':
                                  {'route_refresh': 'advertised and received(new)',
                                   'vpnv4_unicast': 'advertised and received',
                                   'vpnv6_unicast': 'advertised and received',
                                   'graceful_restart': 'received',
                                   'enhanced_refresh': 'advertised',
                                   # 'multisession': '',
                                   'four_octets_asn': 'advertised and received',
                                   'stateful_switchover': 'enabled',
                                   },
                              'bgp_event_timer':
                                  {
                                      'starts':
                                          {
                                              'retrans': 86,
                                              'timewait': 0,
                                              'ackhold': 80,
                                              'sendwnd': 0,
                                              'keepalive': 0,
                                              'giveup': 0,
                                              'pmtuager': 1,
                                              'deadwait': 0,
                                              'linger': 0,
                                              'processq': 0,
                                          },
                                      'wakeups':
                                          {
                                              'retrans': 0,
                                              'timewait': 0,
                                              'ackhold': 72,
                                              'sendwnd': 0,
                                              'keepalive': 0,
                                              'giveup': 0,
                                              'pmtuager': 1,
                                              'deadwait': 0,
                                              'linger': 0,
                                              'processq': 0,
                                          },
                                      'next':
                                          {
                                              'retrans': '0x0',
                                              'timewait': '0x0',
                                              'ackhold': '0x0',
                                              'sendwnd': '0x0',
                                              'keepalive': '0x0',
                                              'giveup': '0x0',
                                              'pmtuager': '0x0',
                                              'deadwait': '0x0',
                                              'linger': '0x0',
                                              'processq': '0x0',
                                          },
                                  },
                              'address_family':
                                  {'vpnv4 unicast':
                                      {
                                          'last_read': '00:00:04',
                                          'last_written': '00:00:09',
                                          'up_time': '01:10:35',
                                      },
                                      'vpnv6 unicast':
                                          {
                                              'last_read': '00:00:07',
                                              'last_written': '00:00:12',
                                              'up_time': '01:10:38',
                                          },

                                  },
                              },
                         '3.3.3.3':
                             {'remote_as': 100,
                              'link': 'internal',
                              'bgp_version': 4,
                              'router_id': '3.3.3.3',
                              'session_state': 'established',
                              'shutdown': False,
                              'bgp_negotiated_keepalive_timers':
                                  {
                                      # 'last_read': '00:00:04',
                                      'keepalive_interval': 60,
                                      'hold_time': 180,
                                      # 'last_written': '00:00:43',
                                  },
                              'bgp_session_transport':
                                  {'connection':
                                      {
                                          'last_reset': 'never',
                                          # 'reset_reason': str,
                                          'established': 1,
                                          'dropped': 0,
                                      },
                                      'transport':
                                          {'local_host': '4.4.4.4',
                                           'local_port': '56031',
                                           'foreign_host': '3.3.3.3',
                                           'foreign_port': '179',
                                           },
                                  },
                              'bgp_neighbor_counters':
                                  {'messages':
                                      {
                                          'sent':
                                              {
                                                  'opens': 1,
                                                  'updates': 11,
                                                  'notifications': 0,
                                                  'keepalives': 75,
                                                  'route_refresh': 0,
                                                  'total': 87,
                                              },
                                          'received':
                                              {
                                                  'opens': 1,
                                                  'updates': 6,
                                                  'notifications': 0,
                                                  'keepalives': 74,
                                                  'route_refresh': 0,
                                                  'total': 81,
                                              },
                                          'input_queue': 0,
                                          'output_queue': 0,
                                      },

                                  },
                              'bgp_negotiated_capabilities':
                                  {'route_refresh': 'advertised and received(new)',
                                   'vpnv4_unicast': 'advertised and received',
                                   'vpnv6_unicast': 'advertised and received',
                                   'graceful_restart': 'received',
                                   'enhanced_refresh': 'advertised',
                                   # 'multisession': '',
                                   'four_octets_asn': 'advertised and received',
                                   'stateful_switchover': 'enabled',
                                   },
                              'bgp_event_timer':
                                  {
                                      'starts':
                                          {
                                              'retrans': 86,
                                              'timewait': 0,
                                              'ackhold': 80,
                                              'sendwnd': 0,
                                              'keepalive': 0,
                                              'giveup': 0,
                                              'pmtuager': 1,
                                              'deadwait': 0,
                                              'linger': 0,
                                              'processq': 0,
                                          },
                                      'wakeups':
                                          {
                                              'retrans': 0,
                                              'timewait': 0,
                                              'ackhold': 73,
                                              'sendwnd': 0,
                                              'keepalive': 0,
                                              'giveup': 0,
                                              'pmtuager': 1,
                                              'deadwait': 0,
                                              'linger': 0,
                                              'processq': 0,
                                          },
                                      'next':
                                          {
                                              'retrans': '0x0',
                                              'timewait': '0x0',
                                              'ackhold': '0x0',
                                              'sendwnd': '0x0',
                                              'keepalive': '0x0',
                                              'giveup': '0x0',
                                              'pmtuager': '0x0',
                                              'deadwait': '0x0',
                                              'linger': '0x0',
                                              'processq': '0x0',
                                          },
                                  },
                              'address_family':
                                  {'vpnv4 unicast':
                                      {
                                          'last_read': '00:00:04',
                                          'last_written': '00:00:43',
                                          'up_time': '01:10:41',
                                      },
                                      'vpnv6 unicast':
                                          {
                                              'last_read': '00:00:08',
                                              'last_written': '00:00:47',
                                              'up_time': '01:10:44',
                                          },
                                  },
                              },
                         },
                },

            },
    }
    golden_output_default = {'execute.return_value': '''
                For address family: IPv4 Unicast

                For address family: IPv6 Unicast

                For address family: VPNv4 Unicast
                BGP neighbor is 2.2.2.2,  remote AS 100, internal link
                  BGP version 4, remote router ID 2.2.2.2
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

                  Address tracking is enabled, the RIB does have a route to 2.2.2.2
                  Connections established 1; dropped 0
                  Last reset never
                  Transport(tcp) path-mtu-discovery is enabled
                  Graceful-Restart is disabled
                Connection state is ESTAB, I/O status: 1, unread input bytes: 0
                Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 255
                Local host: 4.4.4.4, Local port: 35281
                Foreign host: 2.2.2.2, Foreign port: 179
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

                BGP neighbor is 3.3.3.3,  remote AS 100, internal link
                  BGP version 4, remote router ID 3.3.3.3
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

                  Address tracking is enabled, the RIB does have a route to 3.3.3.3
                  Connections established 1; dropped 0
                  Last reset never
                  Transport(tcp) path-mtu-discovery is enabled
                  Graceful-Restart is disabled
                Connection state is ESTAB, I/O status: 1, unread input bytes: 0
                Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 255
                Local host: 4.4.4.4, Local port: 56031
                Foreign host: 3.3.3.3, Foreign port: 179
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

                For address family: VPNv6 Unicast
                BGP neighbor is 2.2.2.2,  remote AS 100, internal link
                  BGP version 4, remote router ID 2.2.2.2
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

                  Address tracking is enabled, the RIB does have a route to 2.2.2.2
                  Connections established 1; dropped 0
                  Last reset never
                  Transport(tcp) path-mtu-discovery is enabled
                  Graceful-Restart is disabled
                Connection state is ESTAB, I/O status: 1, unread input bytes: 0
                Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 255
                Local host: 4.4.4.4, Local port: 35281
                Foreign host: 2.2.2.2, Foreign port: 179
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

                BGP neighbor is 3.3.3.3,  remote AS 100, internal link
                  BGP version 4, remote router ID 3.3.3.3
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

                  Address tracking is enabled, the RIB does have a route to 3.3.3.3
                  Connections established 1; dropped 0
                  Last reset never
                  Transport(tcp) path-mtu-discovery is enabled
                  Graceful-Restart is disabled
                Connection state is ESTAB, I/O status: 1, unread input bytes: 0
                Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 255
                Local host: 4.4.4.4, Local port: 56031
                Foreign host: 3.3.3.3, Foreign port: 179
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



                For address family: IPv4 Multicast

                For address family: L2VPN E-VPN

                For address family: VPNv4 Multicast

                For address family: MVPNv4 Unicast

                For address family: MVPNv6 Unicast

                For address family: VPNv6 Multicast

                '''}
    golden_parsed_output_vrf = {
        'vrf':
            {'vrf1':
                    {
                        'neighbor':
                            {'10.4.6.6':
                                 {'remote_as': 300,
                                  'link': 'external',
                                  'bgp_version': 4,
                                  'router_id': '10.4.6.6',
                                  'session_state': 'established',
                                  'shutdown': False,
                                  'bgp_negotiated_keepalive_timers':
                                      {
                                          'keepalive_interval': 60,
                                          'hold_time': 180,

                                      },
                                  'bgp_session_transport':
                                      {
                                          'connection':
                                              {
                                                  'last_reset': '01:02:11',
                                                  'reset_reason': 'Peer closed the session of session 1',
                                                  'established': 2,
                                                  'dropped': 1,
                                              },
                                          'transport':
                                              {
                                                  'local_host': '10.4.6.4',
                                                  'local_port': '179',
                                                  'foreign_host': '10.4.6.6',
                                                  'foreign_port': '11010',
                                              },
                                      },
                                  'bgp_neighbor_counters':
                                      {'messages':
                                          {
                                              'sent':
                                                  {
                                                      'opens': 1,
                                                      'updates': 3,
                                                      'notifications': 0,
                                                      'keepalives': 69,
                                                      'route_refresh': 0,
                                                      'total': 73,
                                                  },
                                              'received':
                                                  {
                                                      'opens': 1,
                                                      'updates': 1,
                                                      'notifications': 0,
                                                      'keepalives': 64,
                                                      'route_refresh': 0,
                                                      'total': 66,
                                                  },
                                              'input_queue': 0,
                                              'output_queue': 0,
                                          },

                                      },
                                  'bgp_negotiated_capabilities':
                                      {'route_refresh': 'advertised',
                                       'ipv4_unicast': 'advertised and received',
                                       'enhanced_refresh': 'advertised',
                                       'four_octets_asn': 'advertised',
                                       'stateful_switchover': 'enabled',
                                       },
                                  'bgp_event_timer':
                                      {
                                          'starts':
                                              {
                                                  'retrans': 71,
                                                  'timewait': 0,
                                                  'ackhold': 66,
                                                  'sendwnd': 0,
                                                  'keepalive': 0,
                                                  'giveup': 0,
                                                  'pmtuager': 0,
                                                  'deadwait': 0,
                                                  'linger': 0,
                                                  'processq': 0,
                                              },
                                          'wakeups':
                                              {
                                                  'retrans': 0,
                                                  'timewait': 0,
                                                  'ackhold': 64,
                                                  'sendwnd': 0,
                                                  'keepalive': 0,
                                                  'giveup': 0,
                                                  'pmtuager': 0,
                                                  'deadwait': 0,
                                                  'linger': 0,
                                                  'processq': 0,
                                              },
                                          'next':
                                              {
                                                  'retrans': '0x0',
                                                  'timewait': '0x0',
                                                  'ackhold': '0x0',
                                                  'sendwnd': '0x0',
                                                  'keepalive': '0x0',
                                                  'giveup': '0x0',
                                                  'pmtuager': '0x0',
                                                  'deadwait': '0x0',
                                                  'linger': '0x0',
                                                  'processq': '0x0',
                                              },
                                      },
                                  'address_family':
                                      {'vpnv4 unicast':
                                          {
                                              'last_read': '00:00:33',
                                              'last_written': '00:00:30',
                                              'up_time': '01:01:59',
                                          },
                                      },
                                  },
                             '2001:DB8:4:6::6':
                                 {'remote_as': 300,
                                  'link': 'external',
                                  'bgp_version': 4,
                                  'router_id': '10.4.6.6',
                                  'session_state': 'established',
                                  'shutdown': False,
                                  'bgp_negotiated_keepalive_timers':
                                      {
                                          'keepalive_interval': 60,
                                          'hold_time': 180,
                                      },
                                  'bgp_session_transport':
                                      {
                                          'connection':
                                              {
                                                  'last_reset': '01:05:12',
                                                  'reset_reason': 'Active open failed',
                                                  'established': 2,
                                                  'dropped': 1,
                                              },
                                          'transport':
                                              {
                                                  'local_host': '2001:DB8:4:6::4',
                                                  'local_port': '179',
                                                  'foreign_host': '2001:DB8:4:6::6',
                                                  'foreign_port': '11003',
                                              },
                                      },
                                  'bgp_neighbor_counters':
                                      {'messages':
                                          {
                                              'sent':
                                                  {
                                                      'opens': 1,
                                                      'updates': 3,
                                                      'notifications': 0,
                                                      'keepalives': 70,
                                                      'route_refresh': 0,
                                                      'total': 74,
                                                  },
                                              'received':
                                                  {
                                                      'opens': 1,
                                                      'updates': 1,
                                                      'notifications': 0,
                                                      'keepalives': 64,
                                                      'route_refresh': 0,
                                                      'total': 66,
                                                  },
                                              'input_queue': 0,
                                              'output_queue': 0,
                                          },

                                      },
                                  'bgp_negotiated_capabilities':
                                      {'route_refresh': 'advertised',
                                       'ipv6_unicast': 'advertised and received',
                                       'enhanced_refresh': 'advertised',
                                       'four_octets_asn': 'advertised',
                                       'stateful_switchover': 'enabled',
                                       },
                                  'bgp_event_timer':
                                      {
                                          'starts':
                                              {
                                                  'retrans': 72,
                                                  'timewait': 0,
                                                  'ackhold': 66,
                                                  'sendwnd': 0,
                                                  'keepalive': 0,
                                                  'giveup': 0,
                                                  'pmtuager': 0,
                                                  'deadwait': 0,
                                                  'linger': 0,
                                                  'processq': 0,
                                              },
                                          'wakeups':
                                              {
                                                  'retrans': 0,
                                                  'timewait': 0,
                                                  'ackhold': 64,
                                                  'sendwnd': 0,
                                                  'keepalive': 0,
                                                  'giveup': 0,
                                                  'pmtuager': 0,
                                                  'deadwait': 0,
                                                  'linger': 0,
                                                  'processq': 0,
                                              },
                                          'next':
                                              {
                                                  'retrans': '0x0',
                                                  'timewait': '0x0',
                                                  'ackhold': '0x0',
                                                  'sendwnd': '0x0',
                                                  'keepalive': '0x0',
                                                  'giveup': '0x0',
                                                  'pmtuager': '0x0',
                                                  'deadwait': '0x0',
                                                  'linger': '0x0',
                                                  'processq': '0x0',
                                              },
                                      },
                                  'address_family':
                                      {'vpnv6 unicast':
                                          {
                                              'last_read': '00:00:32',
                                              'last_written': '00:00:06',
                                              'up_time': '01:01:58',
                                          },
                                      },
                                  },
                             },
                    },
                'vrf2':
                    {
                        'neighbor':
                            {'20.4.6.6':
                                 {'remote_as': 400,
                                  'link': 'external',
                                  'bgp_version': 4,
                                  'router_id': '20.4.6.6',
                                  'session_state': 'established',
                                  'shutdown': False,
                                  'bgp_negotiated_keepalive_timers':
                                      {
                                          'keepalive_interval': 60,
                                          'hold_time': 180,
                                      },
                                  'bgp_session_transport':
                                      {
                                          'connection':
                                              {
                                                  'last_reset': '01:05:09',
                                                  'reset_reason': 'Active open failed',
                                                  'established': 2,
                                                  'dropped': 1,
                                              },
                                          'transport':
                                              {
                                                  'local_host': '20.4.6.4',
                                                  'local_port': '179',
                                                  'foreign_host': '20.4.6.6',
                                                  'foreign_port': '11003',
                                              },
                                      },
                                  'bgp_neighbor_counters':
                                      {'messages':
                                          {
                                              'sent':
                                                  {
                                                      'opens': 1,
                                                      'updates': 1,
                                                      'notifications': 0,
                                                      'keepalives': 69,
                                                      'route_refresh': 0,
                                                      'total': 71,
                                                  },
                                              'received':
                                                  {
                                                      'opens': 1,
                                                      'updates': 1,
                                                      'notifications': 0,
                                                      'keepalives': 64,
                                                      'route_refresh': 0,
                                                      'total': 66,
                                                  },
                                              'input_queue': 0,
                                              'output_queue': 0,
                                          },

                                      },
                                  'bgp_negotiated_capabilities':
                                      {'route_refresh': 'advertised',
                                       'ipv4_unicast': 'advertised and received',
                                       'enhanced_refresh': 'advertised',
                                       'four_octets_asn': 'advertised',
                                       'stateful_switchover': 'enabled',
                                       },
                                  'bgp_event_timer':
                                      {
                                          'starts':
                                              {
                                                  'retrans': 70,
                                                  'timewait': 0,
                                                  'ackhold': 66,
                                                  'sendwnd': 0,
                                                  'keepalive': 0,
                                                  'giveup': 0,
                                                  'pmtuager': 0,
                                                  'deadwait': 0,
                                                  'linger': 0,
                                                  'processq': 0,
                                              },
                                          'wakeups':
                                              {
                                                  'retrans': 0,
                                                  'timewait': 0,
                                                  'ackhold': 64,
                                                  'sendwnd': 0,
                                                  'keepalive': 0,
                                                  'giveup': 0,
                                                  'pmtuager': 0,
                                                  'deadwait': 0,
                                                  'linger': 0,
                                                  'processq': 0,
                                              },
                                          'next':
                                              {
                                                  'retrans': '0x0',
                                                  'timewait': '0x0',
                                                  'ackhold': '0x0',
                                                  'sendwnd': '0x0',
                                                  'keepalive': '0x0',
                                                  'giveup': '0x0',
                                                  'pmtuager': '0x0',
                                                  'deadwait': '0x0',
                                                  'linger': '0x0',
                                                  'processq': '0x0',
                                              },
                                      },
                                  'address_family':
                                      {'vpnv4 unicast':
                                          {
                                              'last_read': '00:00:24',
                                              'last_written': '00:00:21',
                                              'up_time': '01:01:51',
                                          },
                                      },
                                  },
                             '2001:DB8:20:4:6::6':
                                 {'remote_as': 400,
                                  'link': 'external',
                                  'bgp_version': 4,
                                  'router_id': '20.4.6.6',
                                  'session_state': 'established',
                                  'shutdown': False,
                                  'bgp_negotiated_keepalive_timers':
                                      {
                                          'keepalive_interval': 60,
                                          'hold_time': 180,
                                      },
                                  'bgp_session_transport':
                                      {
                                          'connection':
                                              {
                                                  'last_reset': '01:05:13',
                                                  'reset_reason': 'Active open failed',
                                                  'established': 2,
                                                  'dropped': 1,
                                              },
                                          'transport':
                                              {
                                                  'local_host': '2001:DB8:20:4:6::4',
                                                  'local_port': '179',
                                                  'foreign_host': '2001:DB8:20:4:6::6',
                                                  'foreign_port': '11003',
                                              },
                                      },
                                  'bgp_neighbor_counters':
                                      {'messages':
                                          {
                                              'sent':
                                                  {
                                                      'opens': 1,
                                                      'updates': 1,
                                                      'notifications': 0,
                                                      'keepalives': 70,
                                                      'route_refresh': 0,
                                                      'total': 72,
                                                  },
                                              'received':
                                                  {
                                                      'opens': 1,
                                                      'updates': 1,
                                                      'notifications': 0,
                                                      'keepalives': 64,
                                                      'route_refresh': 0,
                                                      'total': 66,
                                                  },
                                              'input_queue': 0,
                                              'output_queue': 0,
                                          },

                                      },
                                  'bgp_negotiated_capabilities':
                                      {'route_refresh': 'advertised',
                                       'ipv6_unicast': 'advertised and received',
                                       'enhanced_refresh': 'advertised',
                                       'four_octets_asn': 'advertised',
                                       'stateful_switchover': 'enabled',
                                       },
                                  'bgp_event_timer':
                                      {
                                          'starts':
                                              {
                                                  'retrans': 71,
                                                  'timewait': 0,
                                                  'ackhold': 66,
                                                  'sendwnd': 0,
                                                  'keepalive': 0,
                                                  'giveup': 0,
                                                  'pmtuager': 0,
                                                  'deadwait': 0,
                                                  'linger': 0,
                                                  'processq': 0,
                                              },
                                          'wakeups':
                                              {
                                                  'retrans': 0,
                                                  'timewait': 0,
                                                  'ackhold': 64,
                                                  'sendwnd': 0,
                                                  'keepalive': 0,
                                                  'giveup': 0,
                                                  'pmtuager': 0,
                                                  'deadwait': 0,
                                                  'linger': 0,
                                                  'processq': 0,
                                              },
                                          'next':
                                              {
                                                  'retrans': '0x0',
                                                  'timewait': '0x0',
                                                  'ackhold': '0x0',
                                                  'sendwnd': '0x0',
                                                  'keepalive': '0x0',
                                                  'giveup': '0x0',
                                                  'pmtuager': '0x0',
                                                  'deadwait': '0x0',
                                                  'linger': '0x0',
                                                  'processq': '0x0',
                                              },
                                      },
                                  'address_family':
                                      {'vpnv6 unicast':
                                          {
                                              'last_read': '00:00:22',
                                              'last_written': '00:00:01',
                                              'up_time': '01:01:51',
                                          },
                                      },
                                  },
                             },
                    },

            },
    }
    golden_output_vrf = {'execute.return_value': '''
                For address family: IPv4 Unicast

                For address family: IPv6 Unicast

                For address family: VPNv4 Unicast
                BGP neighbor is 10.4.6.6,  vrf VRF1,  remote AS 300, external link
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

                BGP neighbor is 20.4.6.6,  vrf VRF2,  remote AS 400, external link
                  BGP version 4, remote router ID 20.4.6.6
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

                  Address tracking is enabled, the RIB does have a route to 20.4.6.6
                  Connections established 2; dropped 1
                  Last reset 01:05:09, due to Active open failed
                  Transport(tcp) path-mtu-discovery is enabled
                  Graceful-Restart is disabled
                Connection state is ESTAB, I/O status: 1, unread input bytes: 0
                Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 1
                Local host: 20.4.6.4, Local port: 179
                Foreign host: 20.4.6.6, Foreign port: 11003
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
                  BGP version 4, remote router ID 20.4.6.6
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


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpAllNeighbors(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowBgpAllNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_default(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_default)
        obj = ShowBgpAllNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_default)


    def test_golden_vrf(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_vrf)
        obj = ShowBgpAllNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_vrf)


    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowBgpAllNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)



if __name__ == '__main__':
    unittest.main()
