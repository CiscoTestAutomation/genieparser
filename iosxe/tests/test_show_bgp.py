import re
import unittest
from unittest.mock import Mock

from ats.topology import Device

from metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from parser.iosxe.show_bgp import ShowBgpAllSummary, ShowBgpAllClusterIds, \
                                  ShowBgpAllNeighborsAdvertisedRoutes, \
                                  ShowBgpAllNeighborsReceivedRoutes, \
                                  ShowIpBgpTemplatePeerPolicy, \
                                  ShowBgpAllNeighbors, \
                                  ShowIpBgpAllDampeningParameters, \
                                  ShowIpBgpTemplatePeerSession, \
                                  ShowBgpAllNeighborsRoutes, \
                                  ShowBgpAllNeighborsPolicy, \
                                  ShowBgpAll, \
                                  ShowBgpAllDetail

# ===================================
# Unit test for 'show bgp all detail'
# ===================================

class test_show_bgp_all_detail(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
      'instance':
        {'default':
          {'vrf':
            {'VRF1':
              {'address_family':
                {'vpnv4 unicast RD 100:100':
                  {'default_vrf': 'VRF1',
                   'prefixes':
                    {'11.11.11.11/32':
                      {'available_path': '1',
                       'best_path': '1',
                       'index':
                        {1:
                          {'gateway': '0.0.0.0',
                           'localpref': 100,
                           'metric': 0,
                           'next_hop': '0.0.0.0',
                           'next_hop_via': 'vrf '
                                           'VRF1',
                           'origin_codes': '?',
                           'originator': '10.1.1.1',
                           'recipient_pathid': 0,
                           'refresh_epoch': 1,
                           'route_info': 'Local',
                           'status_codes': '*>',
                           'transfer_pathid': '0x0',
                           'weight': '32768'}},
                       'paths': '(1 '
                                'available, '
                                'best '
                                '#1, '
                                'table '
                                'VRF1)',
                       'table_version': '2'}},
                    'route_distinguisher': '100:100'},
                'vpnv6 unicast RD 100:100':
                  {'default_vrf': 'VRF1',
                   'prefixes':
                    {'2001:11:11::11/128':
                      {'available_path': '1',
                       'best_path': '1',
                       'index':
                        {1:
                          {'gateway': '0.0.0.0',
                           'localpref': 100,
                           'metric': 0,
                           'next_hop': '::',
                           'next_hop_via': 'vrf '
                                           'VRF1',
                           'origin_codes': '?',
                           'originator': '10.1.1.1',
                           'recipient_pathid': 0,
                           'refresh_epoch': 1,
                           'route_info': 'Local',
                           'status_codes': '*>',
                           'transfer_pathid': '0x0',
                           'weight': '32768'}},
                       'paths': '(1 '
                                'available, '
                                'best '
                                '#1, '
                                'table '
                                'VRF1)',
                       'table_version': '2'}},
                    'route_distinguisher': '100:100'}}},
            'default':
              {'address_family':
                {'ipv4 unicast':
                  {'prefixes':
                    {'1.1.1.1/32':
                      {'available_path': '1',
                       'best_path': '1',
                       'index':
                        {1:
                          {'gateway': '0.0.0.0',
                           'localpref': 100,
                           'metric': 0,
                           'next_hop': '0.0.0.0',
                           'origin_codes': '?',
                           'originator': '10.1.1.1',
                           'recipient_pathid': 0,
                           'refresh_epoch': 1,
                           'route_info': 'Local',
                           'status_codes': '*>',
                           'transfer_pathid': '0x0',
                           'update_group': 3,
                           'weight': '32768'}},
                       'paths': '(1 '
                                'available, '
                                'best '
                                '#1, '
                                'table '
                                'default)',
                       'table_version': '4'},
                    '10.1.1.0/24':
                      {'available_path': '2',
                       'best_path': '1',
                       'index':
                        {1:
                          {'gateway': '0.0.0.0',
                           'localpref': 100,
                           'metric': 0,
                           'next_hop': '0.0.0.0',
                           'origin_codes': '?',
                           'originator': '10.1.1.1',
                           'recipient_pathid': 0,
                           'refresh_epoch': 1,
                           'route_info': 'Local',
                           'status_codes': '*>',
                           'transfer_pathid': '0x0',
                           'update_group': 3,
                           'weight': '32768'},
                        2:
                          {'gateway': '10.1.1.2',
                           'localpref': 100,
                           'metric': 0,
                           'next_hop': '10.1.1.2',
                           'origin_codes': '?',
                           'originator': '10.1.1.2',
                           'refresh_epoch': 1,
                           'route_info': 'Local',
                           'status_codes': '* '
                                           'i',
                           'update_group': 3}},
                       'paths': '(2 '
                                'available, '
                                'best '
                                '#1, '
                                'table '
                                'default)',
                       'table_version': '5'},
                    '2.2.2.2/32':
                      {'available_path': '1',
                       'best_path': '1',
                       'index':
                        {1:
                          {'gateway': '10.1.1.2',
                           'localpref': 100,
                           'metric': 0,
                           'next_hop': '10.1.1.2',
                           'origin_codes': '?',
                           'originator': '10.1.1.2',
                           'recipient_pathid': 0,
                           'refresh_epoch': 1,
                           'route_info': 'Local',
                           'status_codes': '*>',
                           'transfer_pathid': '0x0'}},
                       'paths': '(1 '
                                'available, '
                                'best '
                                '#1, '
                                'table '
                                'default)',
                       'table_version': '2'}}},
                'ipv6 unicast':
                  {'prefixes':
                    {'2001:1:1:1::1/128':
                      {'available_path': '1',
                       'best_path': '1',
                       'index':
                        {1:
                          {'gateway': '0.0.0.0',
                           'localpref': 100,
                           'metric': 0,
                           'next_hop': '::',
                           'origin_codes': '?',
                           'originator': '10.1.1.1',
                           'recipient_pathid': 0,
                           'refresh_epoch': 1,
                           'route_info': 'Local',
                           'status_codes': '*>',
                           'transfer_pathid': '0x0',
                           'update_group': 1,
                           'weight': '32768'}},
                       'paths': '(1 '
                                'available, '
                                'best '
                                '#1, '
                                'table '
                                'default)',
                       'table_version': '4'},
                    '2001:2:2:2::2/128':
                      {'available_path': '2',
                       'best_path': '1',
                       'index':
                        {1:
                          {'gateway': '2001:DB8:1:1::2',
                           'localpref': 100,
                           'metric': 0,
                           'next_hop': '2001:DB8:1:1::2',
                           'origin_codes': '?',
                           'originator': '10.1.1.2',
                           'recipient_pathid': 0,
                           'refresh_epoch': 1,
                           'route_info': 'Local',
                           'status_codes': '* '
                                           'i',
                           'transfer_pathid': '0x0'}},
                       'paths': '(2 '
                                'available, '
                                'best '
                                '#1, '
                                'table '
                                'default)',
                       'table_version': '2'},
                    '2001:DB8:1:1::/64':
                      {'available_path': '3',
                       'best_path': '1',
                       'index':
                        {1:
                          {'gateway': '0.0.0.0',
                           'localpref': 100,
                           'metric': 0,
                           'next_hop': '::',
                           'origin_codes': '?',
                           'originator': '10.1.1.1',
                           'recipient_pathid': 0,
                           'refresh_epoch': 1,
                           'route_info': 'Local',
                           'status_codes': '*>',
                           'transfer_pathid': '0x0',
                           'update_group': 1,
                           'weight': '32768'},
                        2: {'gateway': '2001:DB8:1:1::2',
                            'localpref': 100,
                            'metric': 0,
                            'next_hop': '2001:DB8:1:1::2',
                            'origin_codes': '?',
                            'originator': '10.1.1.2',
                            'refresh_epoch': 1,
                            'route_info': 'Local',
                            'status_codes': '* '
                                            'i',
                            'update_group': 1}},
                       'paths': '(3 '
                                'available, '
                                'best '
                                '#1, '
                                'table '
                                'default)',
                       'table_version': '5'}}}}}}}}}

    golden_output = {'execute.return_value': '''
      R1#show bgp all detail 
      For address family: IPv4 Unicast

      BGP routing table entry for 1.1.1.1/32, version 4
        Paths: (1 available, best #1, table default)
        Advertised to update-groups:
           3         
        Refresh Epoch 1
        Local
          0.0.0.0 from 0.0.0.0 (10.1.1.1)
            Origin incomplete, metric 0, localpref 100, weight 32768, valid, sourced, best
            rx pathid: 0, tx pathid: 0x0
      BGP routing table entry for 2.2.2.2/32, version 2
        Paths: (1 available, best #1, table default)
        Not advertised to any peer
        Refresh Epoch 1
        Local
          10.1.1.2 from 10.1.1.2 (10.1.1.2)
            Origin incomplete, metric 0, localpref 100, valid, internal, best
            rx pathid: 0, tx pathid: 0x0
      BGP routing table entry for 10.1.1.0/24, version 5
        Paths: (2 available, best #1, table default)
        Advertised to update-groups:
           3         
        Refresh Epoch 1
        Local
          0.0.0.0 from 0.0.0.0 (10.1.1.1)
            Origin incomplete, metric 0, localpref 100, weight 32768, valid, sourced, best
            rx pathid: 0, tx pathid: 0x0
        Refresh Epoch 1
        Local
          10.1.1.2 from 10.1.1.2 (10.1.1.2)
            Origin incomplete, metric 0, localpref 100, valid, internal
            rx pathid: 0, tx pathid: 0

      For address family: IPv6 Unicast

      BGP routing table entry for 2001:1:1:1::1/128, version 4
        Paths: (1 available, best #1, table default)
        Advertised to update-groups:
           1         
        Refresh Epoch 1
        Local
          :: from 0.0.0.0 (10.1.1.1)
            Origin incomplete, metric 0, localpref 100, weight 32768, valid, sourced, best
            rx pathid: 0, tx pathid: 0x0
      BGP routing table entry for 2001:2:2:2::2/128, version 2
        Paths: (2 available, best #1, table default)
        Not advertised to any peer
        Refresh Epoch 1
        Local
          2001:DB8:1:1::2 from 2001:DB8:1:1::2 (10.1.1.2)
            Origin incomplete, metric 0, localpref 100, valid, internal, best
            rx pathid: 0, tx pathid: 0x0
        Refresh Epoch 1
        Local
          ::FFFF:10.1.1.2 (inaccessible) from 10.1.1.2 (10.1.1.2)
            Origin incomplete, metric 0, localpref 100, valid, internal
            rx pathid: 0, tx pathid: 0
      BGP routing table entry for 2001:DB8:1:1::/64, version 5
        Paths: (3 available, best #1, table default)
        Advertised to update-groups:
           1         
        Refresh Epoch 1
        Local
          :: from 0.0.0.0 (10.1.1.1)
            Origin incomplete, metric 0, localpref 100, weight 32768, valid, sourced, best
            rx pathid: 0, tx pathid: 0x0
        Refresh Epoch 1
        Local
          2001:DB8:1:1::2 from 2001:DB8:1:1::2 (10.1.1.2)
            Origin incomplete, metric 0, localpref 100, valid, internal
            rx pathid: 0, tx pathid: 0
        Refresh Epoch 1
        Local
          ::FFFF:10.1.1.2 (inaccessible) from 10.1.1.2 (10.1.1.2)
            Origin incomplete, metric 0, localpref 100, valid, internal
            rx pathid: 0, tx pathid: 0

      For address family: VPNv4 Unicast


      Route Distinguisher: 100:100 (default for vrf VRF1)
      BGP routing table entry for 100:100:11.11.11.11/32, version 2
        Paths: (1 available, best #1, table VRF1)
        Not advertised to any peer
        Refresh Epoch 1
        Local
          0.0.0.0 (via vrf VRF1) from 0.0.0.0 (10.1.1.1)
            Origin incomplete, metric 0, localpref 100, weight 32768, valid, sourced, best
            rx pathid: 0, tx pathid: 0x0

      For address family: VPNv6 Unicast


      Route Distinguisher: 100:100 (default for vrf VRF1)
      BGP routing table entry for [100:100]2001:11:11::11/128, version 2
        Paths: (1 available, best #1, table VRF1)
        Not advertised to any peer
        Refresh Epoch 1
        Local
          :: (via vrf VRF1) from 0.0.0.0 (10.1.1.1)
            Origin incomplete, metric 0, localpref 100, weight 32768, valid, sourced, best
            rx pathid: 0, tx pathid: 0x0

      For address family: IPv4 Multicast


      For address family: L2VPN E-VPN


      For address family: VPNv4 Multicast
                

      For address family: MVPNv4 Unicast


      For address family: MVPNv6 Unicast


      For address family: VPNv6 Multicast


      For address family: VPNv4 Flowspec


      For address family: VPNv6 Flowspec
        '''}

    golden_parsed_output2 = {
      'instance':
        {'default':
          {'vrf':
            {'EVPN-BGP-Table':
              {'address_family':
                {'vpnv4 unicast RD 65535:1':
                  {'default_vrf': 'evpn1',
                   'prefixes':
                    {'100.1.1.0/17':
                      {'available_path': '1',
                       'best_path': '1',
                       'index':
                        {1:
                          {'evpn':
                            {'encap': ':8',
                             'evpn_esi': '00000000000000000000',
                             'ext_community': 'RT:65535:1',
                             'gateway_address': '0.0.0.0',
                             'label': 30000,
                             'local_vtep': '33.33.33.33',
                             'router_mac': 'MAC:001E.7A13.E9BF'},
                          'gateway': '0.0.0.0',
                          'localpref': 100,
                          'metric': 0,
                          'next_hop': '0.0.0.0',
                          'next_hop_via': 'vrf '
                                          'evpn1',
                          'origin_codes': '?',
                          'originator': '33.33.33.33',
                          'recipient_pathid': 0,
                          'refresh_epoch': 1,
                          'route_info': 'Local, '
                                        'imported '
                                        'path '
                                        'from '
                                        'base',
                          'status_codes': '*>',
                          'transfer_pathid': '0x0',
                          'weight': '32768'}},
                       'paths': '(1 '
                                'available, '
                                'best '
                                '#1, '
                                'table '
                                'EVPN-BGP-Table)',
                       'table_version': '4'},
                    '3.3.3.0/17':
                      {'available_path': '2',
                       'best_path': '1',
                       'index':
                        {1:
                          {'evpn':
                            {'encap': ':8',
                             'evpn_esi': '00000000000000000000',
                             'ext_community': 'RT:65535:1',
                             'gateway_address': '0.0.0.0',
                             'label': 30000,
                             'local_vtep': '33.33.33.33',
                             'router_mac': 'MAC:001E.7A13.E9BF'},
                          'gateway': '0.0.0.0',
                          'localpref': 100,
                          'metric': 0,
                          'next_hop': '0.0.0.0',
                          'next_hop_via': 'vrf '
                                          'evpn1',
                          'origin_codes': '?',
                          'originator': '33.33.33.33',
                          'recipient_pathid': 0,
                          'refresh_epoch': 1,
                          'route_info': 'Local, '
                                        'imported '
                                        'path '
                                        'from '
                                        'base',
                          'status_codes': '*>',
                          'transfer_pathid': '0x0',
                          'weight': '32768'},
                        2:
                          {'evpn':
                            {'encap': ':8',
                             'evpn_esi': '00000000000000000000',
                             'ext_community': 'RT:65535:1',
                             'gateway_address': '0.0.0.0',
                             'label': 30000,
                             'local_vtep': '33.33.33.33',
                             'router_mac': 'MAC:001E.7A13.E9BF'},
                          'gateway': '3.3.3.254',
                          'localpref': 100,
                          'metric': 0,
                          'next_hop': '3.3.3.254',
                          'next_hop_via': 'vrf '
                                          'evpn1',
                          'origin_codes': '?',
                          'originator': '33.33.33.22',
                          'refresh_epoch': 1,
                          'route_info': '65530, '
                                        'imported '
                                        'path '
                                        'from '
                                        'base',
                          'status_codes': '* '}},
                       'paths': '(2 '
                                'available, '
                                'best '
                                '#1, '
                                'table '
                                'EVPN-BGP-Table)',
                       'table_version': '3'}},
                    'route_distinguisher': '65535:1'}}},
                'evpn1':
                  {'address_family':
                    {'vpnv4 unicast RD 65535:1':
                      {'default_vrf': 'evpn1',
                       'prefixes':
                        {'100.1.1.0/24':
                          {'available_path': '1',
                           'best_path': '1',
                           'index':
                            {1:
                              {'gateway': '0.0.0.0',
                               'local_vxlan_vtep':
                                {'bdi': 'BDI200',
                                 'encap': '8',
                                 'local_router_mac': '001E.7A13.E9BF',
                                 'vni': '30000',
                                 'vrf': 'evpn1',
                                 'vtep_ip': '33.33.33.33'},
                               'localpref': 100,
                               'metric': 0,
                               'next_hop': '0.0.0.0',
                               'next_hop_via': 'vrf '
                                               'evpn1',
                               'origin_codes': '?',
                               'originator': '33.33.33.33',
                               'recipient_pathid': 0,
                               'refresh_epoch': 1,
                               'route_info': 'Local',
                               'status_codes': '*>',
                               'transfer_pathid': '0x0',
                               'update_group': 1,
                               'weight': '32768'}},
                       'paths': '(1 '
                                'available, '
                                'best '
                                '#1, '
                                'table '
                                'evpn1)',
                       'table_version': '5'},
                        '3.3.3.0/24':
                          {'available_path': '2',
                           'best_path': '2',
                           'index':
                            {1:
                              {'gateway': '3.3.3.254',
                               'local_vxlan_vtep':
                                {'bdi': 'BDI200',
                                 'encap': '8',
                                 'local_router_mac': '001E.7A13.E9BF',
                                 'vni': '30000',
                                 'vrf': 'evpn1',
                                 'vtep_ip': '33.33.33.33'},
                               'localpref': 100,
                               'metric': 0,
                               'next_hop': '3.3.3.254',
                               'next_hop_via': 'vrf '
                                               'evpn1',
                               'origin_codes': '?',
                               'originator': '33.33.33.22',
                               'refresh_epoch': 1,
                               'route_info': '65530',
                               'status_codes': '* ',
                               'update_group': 1},
                            2:
                              {'gateway': '0.0.0.0',
                               'local_vxlan_vtep':
                                {'bdi': 'BDI200',
                                 'encap': '8',
                                 'local_router_mac': '001E.7A13.E9BF',
                                 'vni': '30000',
                                 'vrf': 'evpn1',
                                 'vtep_ip': '33.33.33.33'},
                               'localpref': 100,
                               'metric': 0,
                               'next_hop': '0.0.0.0',
                               'next_hop_via': 'vrf '
                                               'evpn1',
                               'origin_codes': '?',
                               'originator': '33.33.33.33',
                               'recipient_pathid': 0,
                               'refresh_epoch': 1,
                               'route_info': 'Local',
                               'status_codes': '*>',
                               'transfer_pathid': '0x0',
                               'update_group': 1,
                               'weight': '32768'}},
                       'paths': '(2 '
                                'available, '
                                'best '
                                '#2, '
                                'table '
                                'evpn1)',
                       'table_version': '4'}},
                    'route_distinguisher': '65535:1'}}}}}}}

    golden_output2 = {'execute.return_value': '''
      R1_CE#show bgp all detail 
      For address family: IPv4 Unicast


      For address family: IPv6 Unicast


      For address family: VPNv4 Unicast


      Route Distinguisher: 65535:1 (default for vrf evpn1)
      BGP routing table entry for 65535:1:3.3.3.0/24, version 4
        Paths: (2 available, best #2, table evpn1)
        Advertised to update-groups:
           1         
        Refresh Epoch 1
        65530
          3.3.3.254 (via vrf evpn1) from 3.3.3.254 (33.33.33.22)
            Origin incomplete, metric 0, localpref 100, valid, external
            Local vxlan vtep:
              vrf:evpn1, vni:30000
              local router mac:001E.7A13.E9BF
              encap:8
              vtep-ip:33.33.33.33
              bdi:BDI200
            rx pathid: 0, tx pathid: 0
        Refresh Epoch 1
        Local
          0.0.0.0 (via vrf evpn1) from 0.0.0.0 (33.33.33.33)
            Origin incomplete, metric 0, localpref 100, weight 32768, valid, sourced, best
            Local vxlan vtep:
              vrf:evpn1, vni:30000
              local router mac:001E.7A13.E9BF
              encap:8
              vtep-ip:33.33.33.33
              bdi:BDI200
            rx pathid: 0, tx pathid: 0x0
      BGP routing table entry for 65535:1:100.1.1.0/24, version 5
        Paths: (1 available, best #1, table evpn1)
        Advertised to update-groups:
           1         
        Refresh Epoch 1
        Local
          0.0.0.0 (via vrf evpn1) from 0.0.0.0 (33.33.33.33)
            Origin incomplete, metric 0, localpref 100, weight 32768, valid, sourced, best
            Local vxlan vtep:
              vrf:evpn1, vni:30000
              local router mac:001E.7A13.E9BF
              encap:8
              vtep-ip:33.33.33.33
              bdi:BDI200
            rx pathid: 0, tx pathid: 0x0

      For address family: IPv4 Multicast


      For address family: L2VPN E-VPN


      Route Distinguisher: 65535:1 (default for vrf evpn1)
      BGP routing table entry for [5][65535:1][0][24][3.3.3.0]/17, version 3
        Paths: (2 available, best #1, table EVPN-BGP-Table)
        Not advertised to any peer
        Refresh Epoch 1
        Local, imported path from base
          0.0.0.0 (via vrf evpn1) from 0.0.0.0 (33.33.33.33)
            Origin incomplete, metric 0, localpref 100, weight 32768, valid, external, best
            EVPN ESI: 00000000000000000000, Gateway Address: 0.0.0.0, local vtep: 33.33.33.33, Label 30000
            Extended Community: RT:65535:1 ENCAP:8 Router MAC:001E.7A13.E9BF
            rx pathid: 0, tx pathid: 0x0
        Refresh Epoch 1
        65530, imported path from base
          3.3.3.254 (via vrf evpn1) from 3.3.3.254 (33.33.33.22)
            Origin incomplete, metric 0, localpref 100, valid, external
            EVPN ESI: 00000000000000000000, Gateway Address: 0.0.0.0, local vtep: 33.33.33.33, Label 30000
            Extended Community: RT:65535:1 ENCAP:8 Router MAC:001E.7A13.E9BF
            rx pathid: 0, tx pathid: 0
      BGP routing table entry for [5][65535:1][0][24][100.1.1.0]/17, version 4
        Paths: (1 available, best #1, table EVPN-BGP-Table)
        Not advertised to any peer
        Refresh Epoch 1
        Local, imported path from base
          0.0.0.0 (via vrf evpn1) from 0.0.0.0 (33.33.33.33)
            Origin incomplete, metric 0, localpref 100, weight 32768, valid, external, best
            EVPN ESI: 00000000000000000000, Gateway Address: 0.0.0.0, local vtep: 33.33.33.33, Label 30000
            Extended Community: RT:65535:1 ENCAP:8 Router MAC:001E.7A13.E9BF
            rx pathid: 0, tx pathid: 0x0

      For address family: VPNv4 Multicast


      For address family: MVPNv4 Unicast


      For address family: MVPNv6 Unicast


      For address family: VPNv4 Flowspec
        '''}

    def test_show_bgp_all_detail_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowBgpAllDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_bgp_all_detail_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowBgpAllDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output2)

    def test_show_bgp_all_detail_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpAllDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ====================================================
# Unit test for 'show bgp all neighbors <WORD> policy'
# ====================================================

class test_show_bgp_all_neighbors_policy(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {'vrf':
      {'VRF1':
        {'neighbor':
          {'21.0.0.2':
            {'address_family':
              {'vpnv4 unicast':
                {'nbr_af_route_map_name_in': 'test',
                 'nbr_af_route_map_name_out': 'test'}}}}}}}

    golden_output = {'execute.return_value': '''
        R4_iosv#show bgp all neighbors 21.0.0.2 policy
         Neighbor: 21.0.0.2, Address-Family: VPNv4 Unicast (VRF1)
         Locally configured policies:
          route-map test in
          route-map test out
        '''}

    golden_parsed_output2 = {}

    golden_output2 = {'execute.return_value': '''
        R4_iosv#show bgp all neighbors 19.0.102.3 policy 
         Neighbor: 19.0.102.3, Address-Family: VPNv4 Unicast

         Neighbor: 19.0.102.3, Address-Family: VPNv6 Unicast

        '''}

    golden_parsed_output3 = {'vrf':
      {'default':
        {'neighbor':
          {'10.4.6.6':
            {'address_family':
              {'vpnv4 unicast':
                {'nbr_af_route_map_name_in': 'rmap1'}}}}}}}

    golden_output3 = {'execute.return_value': '''
        R4_iosv#show bgp all neighbors 10.4.6.6 policy 
         Neighbor: 10.4.6.6, Address-Family: VPNv4 Unicast
         Locally configured policies:
          route-map rmap1 in
         Neighbor: 10.4.6.6, Address-Family: VPNv6 Unicast

        '''}

    def test_show_bgp_all_neighbors_policy_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowBgpAllNeighborsPolicy(device=self.device)
        parsed_output = obj.parse(neighbor='21.0.0.2')
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_bgp_vrf_all_neighbors_policy_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowBgpAllNeighborsPolicy(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
          parsed_output = obj.parse(neighbor='19.0.102.3')

    def test_show_bgp_all_neighbors_policy_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowBgpAllNeighborsPolicy(device=self.device)
        parsed_output = obj.parse(neighbor='10.4.6.6')
        self.assertEqual(parsed_output,self.golden_parsed_output3)

    def test_show_bgp_all_neighbors_policy_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpAllNeighborsPolicy(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(neighbor='10.4.6.6')

# ===============================================================
# Unit test for 'show bgp all neighbors <WORD> advertised-routes'
# ===============================================================

class test_show_bgp_all_neighbors_advertised_routes(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = \
      {'vrf':
        {'default':
          {'neighbor':
            {'21.0.0.2':
              {'address_family':
                {'vpnv4 unicast':
                  {'advertised': {},
                   'bgp_table_version': 56,
                   'local_router_id': '4.4.4.4'},
                'vpnv4 unicast RD 300:1':
                  {'advertised':
                    {'46.1.1.0/24':
                      {'index':
                        {1:
                          {'metric': 2219,
                           'next_hop': '10.4.6.6',
                           'origin_codes': 'e',
                           'path': '300 '
                                   '33299 '
                                   '51178 '
                                   '47751 '
                                   '{27016}',
                           'status_codes': '*>',
                           'weight': 0}}},
                    '46.1.2.0/24':
                      {'index':
                        {1:
                          {'metric': 2219,
                           'next_hop': '10.4.6.6',
                           'origin_codes': 'e',
                           'path': '300 '
                                   '33299 '
                                   '51178 '
                                   '47751 '
                                   '{27016}',
                           'status_codes': '*>',
                           'weight': 0}}},
                    '46.1.3.0/24':
                      {'index':
                        {1:
                          {'metric': 2219,
                           'next_hop': '10.4.6.6',
                           'origin_codes': 'e',
                           'path': '300 '
                                   '33299 '
                                   '51178 '
                                   '47751 '
                                   '{27016}',
                           'status_codes': '*>',
                           'weight': 0}}},
                    '46.1.4.0/24':
                      {'index':
                        {1:
                          {'metric': 2219,
                           'next_hop': '10.4.6.6',
                           'origin_codes': 'e',
                           'path': '300 '
                                   '33299 '
                                   '51178 '
                                   '47751 '
                                   '{27016}',
                           'status_codes': '*>',
                           'weight': 0}}},
                    '46.1.5.0/24':
                      {'index':
                        {1:
                          {'metric': 2219,
                           'next_hop': '10.4.6.6',
                           'origin_codes': 'e',
                           'path': '300 '
                                   '33299 '
                                   '51178 '
                                   '47751 '
                                   '{27016}',
                           'status_codes': '*>',
                           'weight': 0}}}},
                   'bgp_table_version': 56,
                   'default_vrf': 'VRF1',
                   'local_router_id': '4.4.4.4',
                   'route_distinguisher': '300:1'},
                'vpnv4 unicast RD 400:1':
                  {'advertised':
                    {'46.2.2.0/24':
                      {'index':
                        {1:
                          {'metric': 2219,
                           'next_hop': '20.4.6.6',
                           'origin_codes': 'e',
                           'path': '400 '
                                   '33299 '
                                   '51178 '
                                   '47751 '
                                   '{27016}',
                           'status_codes': '*>',
                           'weight': 0}}},
                    '46.2.3.0/24':
                      {'index':
                        {1:
                          {'metric': 2219,
                           'next_hop': '20.4.6.6',
                           'origin_codes': 'e',
                           'path': '400 '
                                   '33299 '
                                   '51178 '
                                   '47751 '
                                   '{27016}',
                           'status_codes': '*>',
                           'weight': 0}}},
                    '46.2.4.0/24':
                      {'index':
                        {1:
                          {'metric': 2219,
                           'next_hop': '20.4.6.6',
                           'origin_codes': 'e',
                           'path': '400 '
                                   '33299 '
                                   '51178 '
                                   '47751 '
                                   '{27016}',
                           'status_codes': '*>',
                           'weight': 0}}},
                    '46.2.5.0/24':
                      {'index':
                        {1:
                          {'metric': 2219,
                           'next_hop': '20.4.6.6',
                           'origin_codes': 'e',
                           'path': '400 '
                                   '33299 '
                                   '51178 '
                                   '47751 '
                                   '{27016}',
                           'status_codes': '*>',
                           'weight': 0}}},
                    '46.2.6.0/24':
                      {'index':
                        {1:
                          {'metric': 2219,
                           'next_hop': '20.4.6.6',
                           'origin_codes': 'e',
                           'path': '400 '
                                   '33299 '
                                   '51178 '
                                   '47751 '
                                   '{27016}',
                           'status_codes': '*>',
                           'weight': 0}}}},
                   'bgp_table_version': 56,
                   'default_vrf': 'VRF2',
                   'local_router_id': '4.4.4.4',
                   'route_distinguisher': '400:1'},
                'vpnv6 unicast':
                  {'advertised': {},
                   'bgp_table_version': 66,
                   'local_router_id': '4.4.4.4'},
                'vpnv6 unicast RD 300:1':
                  {'advertised':
                    {'646:11:11:1::/64':
                      {'index':
                        {1:
                          {'metric': 2219,
                           'next_hop': '2001:DB8:4:6::6',
                           'origin_codes': 'e',
                           'path': '300 '
                                   '33299 '
                                   '51178 '
                                   '47751 '
                                   '{27016}',
                           'status_codes': '*>',
                           'weight': 0}}},
                    '646:11:11:2::/64':
                      {'index':
                        {1:
                          {'metric': 2219,
                           'next_hop': '2001:DB8:4:6::6',
                           'origin_codes': 'e',
                           'path': '300 '
                                   '33299 '
                                   '51178 '
                                   '47751 '
                                   '{27016}',
                           'status_codes': '*>',
                           'weight': 0}}},
                    '646:11:11:3::/64':
                      {'index':
                        {1:
                          {'metric': 2219,
                           'next_hop': '2001:DB8:4:6::6',
                           'origin_codes': 'e',
                           'path': '300 '
                                   '33299 '
                                   '51178 '
                                   '47751 '
                                   '{27016}',
                           'status_codes': '*>',
                           'weight': 0}}},
                    '646:11:11:4::/64':
                      {'index':
                        {1:
                          {'metric': 2219,
                           'next_hop': '2001:DB8:4:6::6',
                           'origin_codes': 'e',
                           'path': '300 '
                                   '33299 '
                                   '51178 '
                                   '47751 '
                                   '{27016}',
                           'status_codes': '*>',
                           'weight': 0}}},
                    '646:11:11::/64':
                      {'index':
                        {1:
                          {'metric': 2219,
                           'next_hop': '2001:DB8:4:6::6',
                           'origin_codes': 'e',
                           'path': '300 '
                                   '33299 '
                                   '51178 '
                                   '47751 '
                                   '{27016}',
                           'status_codes': '*>',
                           'weight': 0}}}},
                 'bgp_table_version': 66,
                 'default_vrf': 'VRF1',
                 'local_router_id': '4.4.4.4',
                 'route_distinguisher': '300:1'},
                'vpnv6 unicast RD 400:1':
                  {'advertised':
                    {'646:22:22:1::/64':
                      {'index':
                        {1:
                          {'metric': 2219,
                           'next_hop': '2001:DB8:20:4:6::6',
                           'origin_codes': 'e',
                           'path': '400 '
                                   '33299 '
                                   '51178 '
                                   '47751 '
                                   '{27016}',
                           'status_codes': '*>',
                           'weight': 0}}},
                    '646:22:22:2::/64':
                      {'index':
                        {1:
                          {'metric': 2219,
                           'next_hop': '2001:DB8:20:4:6::6',
                           'origin_codes': 'e',
                           'path': '400 '
                                   '33299 '
                                   '51178 '
                                   '47751 '
                                   '{27016}',
                           'status_codes': '*>',
                           'weight': 0}}},
                    '646:22:22:3::/64':
                      {'index':
                        {1:
                          {'metric': 2219,
                           'next_hop': '2001:DB8:20:4:6::6',
                           'origin_codes': 'e',
                           'path': '400 '
                                   '33299 '
                                   '51178 '
                                   '47751 '
                                   '{27016}',
                           'status_codes': '*>',
                           'weight': 0}}},
                    '646:22:22:4::/64':
                      {'index':
                        {1:
                          {'metric': 2219,
                           'next_hop': '2001:DB8:20:4:6::6',
                           'origin_codes': 'e',
                           'path': '400 '
                                   '33299 '
                                   '51178 '
                                   '47751 '
                                   '{27016}',
                           'status_codes': '*>',
                           'weight': 0}}},
                    '646:22:22::/64':
                      {'index':
                        {1:
                          {'metric': 2219,
                           'next_hop': '2001:DB8:20:4:6::6',
                           'origin_codes': 'e',
                           'path': '400 '
                                   '33299 '
                                   '51178 '
                                   '47751 '
                                   '{27016}',
                           'status_codes': '*>',
                           'weight': 0}}}},
                 'bgp_table_version': 66,
                 'default_vrf': 'VRF2',
                 'local_router_id': '4.4.4.4',
                 'route_distinguisher': '400:1'}}}}}}}

    golden_output = {'execute.return_value': '''
        For address family: VPNv4 Unicast
        BGP table version is 56, local router ID is 4.4.4.4
        Status codes: s suppressed, d damped, h history, * valid, > best, i - internal, 
                      r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter, 
                      x best-external, a additional-path, c RIB-compressed, 
        Origin codes: i - IGP, e - EGP, ? - incomplete
        RPKI validation codes: V valid, I invalid, N Not found

             Network          Next Hop            Metric LocPrf Weight Path
        Route Distinguisher: 300:1 (default for vrf VRF1) VRF Router ID 44.44.44.44
         *>  46.1.1.0/24      10.4.6.6              2219             0 300 33299 51178 47751 {27016} e
         *>  46.1.2.0/24      10.4.6.6              2219             0 300 33299 51178 47751 {27016} e
         *>  46.1.3.0/24      10.4.6.6              2219             0 300 33299 51178 47751 {27016} e
         *>  46.1.4.0/24      10.4.6.6              2219             0 300 33299 51178 47751 {27016} e
         *>  46.1.5.0/24      10.4.6.6              2219             0 300 33299 51178 47751 {27016} e
        Route Distinguisher: 400:1 (default for vrf VRF2) VRF Router ID 44.44.44.44
         *>  46.2.2.0/24      20.4.6.6              2219             0 400 33299 51178 47751 {27016} e
         *>  46.2.3.0/24      20.4.6.6              2219             0 400 33299 51178 47751 {27016} e
         *>  46.2.4.0/24      20.4.6.6              2219             0 400 33299 51178 47751 {27016} e
         *>  46.2.5.0/24      20.4.6.6              2219             0 400 33299 51178 47751 {27016} e
         *>  46.2.6.0/24      20.4.6.6              2219             0 400 33299 51178 47751 {27016} e

        Total number of prefixes 10 

        For address family: VPNv6 Unicast
        BGP table version is 66, local router ID is 4.4.4.4
        Status codes: s suppressed, d damped, h history, * valid, > best, i - internal, 
                      r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter, 
                      x best-external, a additional-path, c RIB-compressed, 
        Origin codes: i - IGP, e - EGP, ? - incomplete
        RPKI validation codes: V valid, I invalid, N Not found

             Network          Next Hop            Metric LocPrf Weight Path
        Route Distinguisher: 300:1 (default for vrf VRF1) VRF Router ID 44.44.44.44
         *>  646:11:11::/64   2001:DB8:4:6::6       2219             0 300 33299 51178 47751 {27016} e
         *>  646:11:11:1::/64 2001:DB8:4:6::6       2219             0 300 33299 51178 47751 {27016} e
         *>  646:11:11:2::/64 2001:DB8:4:6::6       2219             0 300 33299 51178 47751 {27016} e
         *>  646:11:11:3::/64 2001:DB8:4:6::6       2219             0 300 33299 51178 47751 {27016} e
         *>  646:11:11:4::/64 2001:DB8:4:6::6       2219             0 300 33299 51178 47751 {27016} e
        Route Distinguisher: 400:1 (default for vrf VRF2) VRF Router ID 44.44.44.44
         *>  646:22:22::/64   2001:DB8:20:4:6::6
                                                     2219             0 400 33299 51178 47751 {27016} e
         *>  646:22:22:1::/64 2001:DB8:20:4:6::6
                                                     2219             0 400 33299 51178 47751 {27016} e
         *>  646:22:22:2::/64 2001:DB8:20:4:6::6
                                                     2219             0 400 33299 51178 47751 {27016} e
         *>  646:22:22:3::/64 2001:DB8:20:4:6::6
                                                     2219             0 400 33299 51178 47751 {27016} e
         *>  646:22:22:4::/64 2001:DB8:20:4:6::6
                                                     2219             0 400 33299 51178 47751 {27016} e

        Total number of prefixes 10
        '''}

    golden_parsed_output2 = {
        'vrf': 
            {'default': 
                {'neighbor': 
                    {'19.0.102.3': 
                        {'address_family': 
                            {'ipv4 multicast': 
                                {'advertised': 
                                    {'1.2.1.0/24': {'index': {1: {'localprf': 100,
                                                               'next_hop': '19.0.101.1',
                                                               'origin_codes': 'i',
                                                               'path': '2 '
                                                                       '3 '
                                                                       '4',
                                                               'path_type': 'i',
                                                               'status_codes': '*>',
                                                               'weight': 0}}},
                                    '1.2.2.0/24': {'index': {1: {'localprf': 100,
                                                               'next_hop': '19.0.101.1',
                                                               'origin_codes': 'i',
                                                               'path': '2 '
                                                                       '3 '
                                                                       '4',
                                                               'path_type': 'i',
                                                               'status_codes': '*>',
                                                               'weight': 0}}},
                                    '1.4.1.0/24': {'index': {1: {'localprf': 100,
                                                               'next_hop': '19.0.102.4',
                                                               'origin_codes': 'i',
                                                               'path': '2 '
                                                                       '3 '
                                                                       '4',
                                                               'path_type': 'i',
                                                               'status_codes': '*>',
                                                               'weight': 0}}},
                                    '1.4.2.0/24': {'index': {1: {'localprf': 100,
                                                               'next_hop': '19.0.102.4',
                                                               'origin_codes': 'i',
                                                               'path': '2 '
                                                                       '3 '
                                                                       '4',
                                                               'path_type': 'i',
                                                               'status_codes': '*>',
                                                               'weight': 0}}},
                                    '1.5.2.0/24': {'index': {1: {'localprf': 500,
                                                               'metric': 5555,
                                                               'next_hop': '19.0.102.4',
                                                               'origin_codes': 'i',
                                                               'path': '2 '
                                                                       '3 '
                                                                       '4 '
                                                                       '5 '
                                                                       '6 '
                                                                       '7 '
                                                                       '8 '
                                                                       '9 '
                                                                       '10 '
                                                                       '11 '
                                                                       '12',
                                                               'path_type': 'i',
                                                               'status_codes': '*>',
                                                               'weight': 32788}}}},
                                'bgp_table_version': 175,
                                'local_router_id': '20.0.0.6'},
                            'ipv4 unicast': 
                                {'advertised': 
                                    {'1.1.1.0/24': {'index': {1: {'localprf': 100,
                                                                 'next_hop': '19.0.102.4',
                                                                 'origin_codes': 'i',
                                                                 'path': '{62112 '
                                                                         '33492 '
                                                                         '4872 '
                                                                         '41787 '
                                                                         '13166 '
                                                                         '50081 '
                                                                         '21461 '
                                                                         '58376 '
                                                                         '29755 '
                                                                         '1135}',
                                                                 'path_type': 'i',
                                                                 'status_codes': '*>',
                                                                 'weight': 0}}},
                                    '1.1.2.0/24': {'index': {1: {'localprf': 100,
                                                                 'next_hop': '19.0.102.4',
                                                                 'origin_codes': 'i',
                                                                 'path': '{62112 '
                                                                         '33492 '
                                                                         '4872 '
                                                                         '41787 '
                                                                         '13166 '
                                                                         '50081 '
                                                                         '21461 '
                                                                         '58376 '
                                                                         '29755 '
                                                                         '1135}',
                                                                 'path_type': 'i',
                                                                 'status_codes': '*>',
                                                                 'weight': 0}}},
                                    '1.5.0.0/24': {'index': {1: {'metric': 100,
                                                                 'next_hop': '19.0.102.3',
                                                                 'origin_codes': 'i',
                                                                 'path': '10 '
                                                                         '20 '
                                                                         '30 '
                                                                         '40 '
                                                                         '50 '
                                                                         '60 '
                                                                         '70 '
                                                                         '80 '
                                                                         '90',
                                                                 'path_type': 'i',
                                                                 'status_codes': '*>',
                                                                 'weight': 0}}},
                                    '1.6.0.0/16': {'index': {1: {'localprf': 100,
                                                                 'next_hop': '19.0.101.1',
                                                                 'origin_codes': 'i',
                                                                 'path': '10 '
                                                                         '20 '
                                                                         '30 '
                                                                         '40 '
                                                                         '50 '
                                                                         '60 '
                                                                         '70 '
                                                                         '80 '
                                                                         '90',
                                                                 'path_type': 'i',
                                                                 'status_codes': '*>',
                                                                 'weight': 0}}}},
                                'bgp_table_version': 174,
                                'local_router_id': '20.0.0.6'},
                            'ipv6 multicast': 
                                {'bgp_table_version': 6,
                                'local_router_id': '20.0.0.6',
                                'advertised': {}},
                            'ipv6 unicast': 
                                {'bgp_table_version': 173,
                                'local_router_id': '20.0.0.6',
                                'advertised': {}},
                            'link-state': 
                                {'advertised': 
                                    {'[2]:[77][7,0][9.9.9.9,1,151587081][29.1.1.1,22][19.0.101.1,29.0.1.30]/616': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 4444,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '3 '
                                                        '10 '
                                                        '20 '
                                                        '30 '
                                                        '40 '
                                                        '50 '
                                                        '60 '
                                                        '70 '
                                                        '80 '
                                                        '90',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0},
                                            2: 
                                                {'localprf': 100,
                                                'metric': 4444,
                                                'next_hop': '19.0.102.3',
                                                'origin_codes': 'i',
                                                'path': '3 '
                                                        '10 '
                                                        '20 '
                                                        '30 '
                                                        '40 '
                                                        '50 '
                                                        '60 '
                                                        '70 '
                                                        '80 '
                                                        '90',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    '[2]:[77][7,0][9.9.9.9,2,151587081][29.1.1.1,22][19.0.101.1,29.0.1.31]/616': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 200,
                                                'metric': 555,
                                                'next_hop': '19.0.103.2',
                                                'origin_codes': 'i',
                                                'path': '3 '
                                                        '10 '
                                                        '20 '
                                                        '30 '
                                                        '40 '
                                                        '50 '
                                                        '60 '
                                                        '70 '
                                                        '80 '
                                                        '90',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}}},
                                'bgp_table_version': 173,
                                'local_router_id': '20.0.0.6'},
                            'vpnv4 unicast': 
                                {'bgp_table_version': 183,
                                'local_router_id': '20.0.0.6',
                                'advertised': {}},
                            'vpnv4 unicast RD 0:0': 
                                {'bgp_table_version': 183,
                                'local_router_id': '20.0.0.6',
                                'route_distinguisher': '0:0',
                                'advertised': {}},
                            'vpnv4 unicast RD 101:100': 
                                {'bgp_table_version': 183,
                                'local_router_id': '20.0.0.6',
                                'route_distinguisher': '101:100',
                                'advertised': {}},
                            'vpnv4 unicast RD 102:100': 
                                {'bgp_table_version': 183,
                                'local_router_id': '20.0.0.6',
                                'route_distinguisher': '102:100',
                                'advertised': {}},
                            'vpnv6 unicast': 
                                {'bgp_table_version': 13,
                                'local_router_id': '20.0.0.6',
                                'advertised': {}},
                            'vpnv6 unicast RD 0xbb00010000000000': 
                                {'bgp_table_version': 13,
                                'local_router_id': '20.0.0.6',
                                'route_distinguisher': '0xbb00010000000000',
                                'advertised': {}},
                            'vpnv6 unicast RD 100:200': 
                                {'bgp_table_version': 13,
                                'local_router_id': '20.0.0.6',
                                'route_distinguisher': '100:200',
                                'advertised': {}}}}}}}}

    golden_output2 = {'execute.return_value': '''
        show bgp all neighbors 19.0.102.3 advertised-routes


        For address family: IPv4 Unicast
        BGP table version is 174, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>i1.1.1.0/24         19.0.102.4                        100          0 {62112 33492 4872 41787 13166 50081 21461 58376 29755 1135} i
        *>i1.1.2.0/24         19.0.102.4                        100          0 {62112 33492 4872 41787 13166 50081 21461 58376 29755 1135} i
        *>i1.6.0.0/16         19.0.101.1                        100          0 10 20 30 40 50 60 70 80 90 i
        *>i1.5.0.0/24         19.0.102.3             100                     0 10 20 30 40 50 60 70 80 90 i


        For address family: IPv4 Multicast
        BGP table version is 175, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>i1.2.1.0/24         19.0.101.1                        100          0 2 3 4 i
        *>i1.2.2.0/24         19.0.101.1                        100          0 2 3 4 i
        *>i1.4.1.0/24         19.0.102.4                        100          0 2 3 4 i
        *>i1.4.2.0/24         19.0.102.4                        100          0 2 3 4 i
        *>i1.5.2.0/24         19.0.102.4            5555        500      32788 2 3 4 5 6 7 8 9 10 11 12 i


        For address family: IPv6 Unicast
        BGP table version is 173, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path


        For address family: IPv6 Multicast
        BGP table version is 6, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path


        For address family: VPNv4 Unicast
        BGP table version is 183, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        Route Distinguisher: 0:0

        Route Distinguisher: 101:100

        Route Distinguisher: 102:100


        For address family: VPNv6 Unicast
        BGP table version is 13, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        Route Distinguisher: 100:200

        Route Distinguisher: 0xbb00010000000000


        For address family: Link-State
        BGP table version is 173, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>i[2]:[77][7,0][9.9.9.9,1,151587081][29.1.1.1,22][19.0.101.1,29.0.1.30]/616
                              19.0.101.1            4444        100          0 3 10 20 30 40 50 60 70 80 90 i
                              19.0.102.3            4444        100          0 3 10 20 30 40 50 60 70 80 90 i
        *>i[2]:[77][7,0][9.9.9.9,2,151587081][29.1.1.1,22][19.0.101.1,29.0.1.31]/616
                              19.0.103.2            555        200          0 3 10 20 30 40 50 60 70 80 90 i
        '''}

    golden_parsed_output3 = {
        'vrf': 
            {'default': 
                {'neighbor': 
                    {'10.4.6.6': 
                        {'address_family': 
                            {'ipv4 unicast': 
                                {'advertised': 
                                    {'15.1.1.0/24': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 2219,
                                                'next_hop': '1.1.1.1',
                                                'origin_codes': 'e',
                                                'path': '200 '
                                                        '33299 '
                                                        '51178 '
                                                        '47751 '
                                                        '{27016}',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    '15.1.2.0/24': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 2219,
                                                'next_hop': '1.1.1.1',
                                                'origin_codes': 'e',
                                                'path': '200 '
                                                        '33299 '
                                                        '51178 '
                                                        '47751 '
                                                        '{27016}',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    '15.1.3.0/24': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 2219,
                                                'next_hop': '1.1.1.1',
                                                'origin_codes': 'e',
                                                'path': '200 '
                                                        '33299 '
                                                        '51178 '
                                                        '47751 '
                                                        '{27016}',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    '15.1.4.0/24': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 2219,
                                                'next_hop': '1.1.1.1',
                                                'origin_codes': 'e',
                                                'path': '200 '
                                                        '33299 '
                                                        '51178 '
                                                        '47751 '
                                                        '{27016}',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    '15.1.5.0/24': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 2219,
                                                'next_hop': '1.1.1.1',
                                                'origin_codes': 'e',
                                                'path': '200 '
                                                        '33299 '
                                                        '51178 '
                                                        '47751 '
                                                        '{27016}',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    '46.2.2.0/24': 
                                        {'index': 
                                            {1: 
                                                {'metric': 100,
                                                'next_hop': '20.4.6.6',
                                                'origin_codes': 'e',
                                                'path': '400 '
                                                        '33299 '
                                                        '51178 '
                                                        '{47751}',
                                                'path_type': 'e',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    '46.2.3.0/24': 
                                        {'index': 
                                            {1: 
                                                {'metric': 100,
                                                'next_hop': '20.4.6.6',
                                                'origin_codes': 'e',
                                                'path': '400 '
                                                        '33299 '
                                                        '51178 '
                                                        '{47751}',
                                                'path_type': 'e',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    '46.2.4.0/24': 
                                        {'index': 
                                            {1: 
                                                {'metric': 100,
                                                'next_hop': '20.4.6.6',
                                                'origin_codes': 'e',
                                                'path': '400 '
                                                        '33299 '
                                                        '51178 '
                                                        '{47751}',
                                                'path_type': 'e',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    '46.2.5.0/24': 
                                        {'index': 
                                            {1: 
                                                {'metric': 100,
                                                'next_hop': '20.4.6.6',
                                                'origin_codes': 'e',
                                                'path': '400 '
                                                        '33299 '
                                                        '51178 '
                                                        '{47751}',
                                                'path_type': 'e',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    '46.2.6.0/24': 
                                        {'index': 
                                            {1: 
                                                {'metric': 100,
                                                'next_hop': '20.4.6.6',
                                                'origin_codes': 'e',
                                                'path': '400 '
                                                        '33299 '
                                                        '51178 '
                                                        '{47751}',
                                                'path_type': 'e',
                                                'status_codes': '*>',
                                                'weight': 0}}}},
                                'bgp_table_version': 648438,
                                'local_router_id': '44.44.44.44'},
                            'ipv6 unicast': 
                                {'advertised': {},
                                'bgp_table_version': 256028,
                                'local_router_id': '44.44.44.44'}}}}}}}

    golden_output3 = {'execute.return_value': '''\
        R4# show bgp all neighbors 10.4.6.6 advertised-routes

        For address family: IPv4 Unicast
        BGP table version is 648438, local router ID is 44.44.44.44
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>i15.1.1.0/24        1.1.1.1               2219        100          0 200 33299 51178 47751 {27016} e
        *>i15.1.2.0/24        1.1.1.1               2219        100          0 200 33299 51178 47751 {27016} e
        *>i15.1.3.0/24        1.1.1.1               2219        100          0 200 33299 51178 47751 {27016} e
        *>i15.1.4.0/24        1.1.1.1               2219        100          0 200 33299 51178 47751 {27016} e
        *>i15.1.5.0/24        1.1.1.1               2219        100          0 200 33299 51178 47751 {27016} e
        *>e46.2.2.0/24        20.4.6.6               100                     0 400 33299 51178 {47751} e
        *>e46.2.3.0/24        20.4.6.6               100                     0 400 33299 51178 {47751} e
        *>e46.2.4.0/24        20.4.6.6               100                     0 400 33299 51178 {47751} e
        *>e46.2.5.0/24        20.4.6.6               100                     0 400 33299 51178 {47751} e
        *>e46.2.6.0/24        20.4.6.6               100                     0 400 33299 51178 {47751} e

        For address family: IPv4 Multicast

        For address family: IPv6 Unicast
        BGP table version is 256028, local router ID is 44.44.44.44
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path

        For address family: IPv6 Multicast

        For address family: VPNv4 Unicast

        For address family: VPNv6 Unicast

        For address family: IPv4 MDT

        For address family: IPv6 Label Unicast

        For address family: L2VPN VPLS

        For address family: IPv4 MVPN

        For address family: IPv6 MVPN

        For address family: IPv4 Label Unicast
        '''}

    def test_show_bgp_all_neighbors_advertised_routes_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowBgpAllNeighborsAdvertisedRoutes(device=self.device)
        parsed_output = obj.parse(neighbor='21.0.0.2')
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_bgp_vrf_all_neighbors_advertised_routes_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowBgpAllNeighborsAdvertisedRoutes(device=self.device)
        parsed_output = obj.parse(neighbor='19.0.102.3')
        self.assertEqual(parsed_output,self.golden_parsed_output2)

    def test_show_bgp_vrf_all_neighbors_advertised_routes_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowBgpAllNeighborsAdvertisedRoutes(device=self.device)
        parsed_output = obj.parse(neighbor='10.4.6.6')
        self.assertEqual(parsed_output,self.golden_parsed_output3)

    def test_show_bgp_all_neighbors_advertised_routes_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpAllNeighborsAdvertisedRoutes(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(neighbor='10.4.6.6')


class test_show_bgp_all_summary(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        'bgp_id': 100,
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
        'bgp_id': 100,
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


class test_show_bgp_all_neighbores(unittest.TestCase):
    '''
        unit test for  show bgp all neighbors
    '''
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output_1 = {
        'list_of_neighbors': ['2.2.2.2',
                        '3.3.3.3',
                        '10.4.6.6',
                        '20.4.6.6',
                        '2.2.2.2',
                        '3.3.3.3',
                        '2001:DB8:4:6::6',
                        '2001:DB8:20:4:6::6'],
        'vrf':
            {'default':
                {
                    'neighbor':
                        {'2.2.2.2':
                             {'remote_as': 100,
                              'link': 'internal',
                              'bgp_version': 4,
                              'router_id': '2.2.2.2',
                              'description': 'router2222222',
                              'session_state': 'established',
                              'bgp_negotiated_keepalive_timers':
                                  {
                                   'keepalive_interval': 60,
                                   'hold_time': 180,
                                   },
                              'bgp_session_transport':
                                  {
                                      'connection':
                                      {
                                          'last_reset': 'never',
                                          'established': 1,
                                          'dropped': 0,
                                      },
                                      'transport':
                                      {
                                           'local_host': '4.4.4.4',
                                           'local_port': '35281',
                                           'foreign_host': '2.2.2.2',
                                           'foreign_port': '179',
                                           'mss':536,
                                      },
                                      'min_time_between_advertisement_runs': 0,
                                      'address_tracking_status': 'enabled' ,
                                      'rib_route_ip': '2.2.2.2',
                                      'tcp_path_mtu_discovery': 'enabled',
                                      'graceful_restart': 'disabled',
                                      'connection_state': 'estab',
                                      'io_status': 1,
                                      'unread_input_bytes': 0,
                                      'ecn_connection': 'disabled',
                                      'minimum_incoming_ttl': 0,
                                      'outgoing_ttl': 255,
                                      'connection_tableid': 0,
                                      'maximum_output_segment_queue_size': 50,
                                      'enqueued_packets':
                                          {
                                              'retransmit_packet': 0,
                                              'input_packet': 0,
                                              'mis_ordered_packet': 0,
                                          },

                                      'iss': 55023811,
                                      'snduna': 55027115,
                                      'sndnxt': 55027115,
                                      'irs': 109992783,
                                      'rcvnxt':109995158,
                                      'sndwnd': 16616,
                                      'snd_scale': 0,
                                      'maxrcvwnd': 16384,
                                      'rcvwnd': 16327,
                                      'rcv_scale':0 ,
                                      'delrcvwnd': 57,
                                      'srtt': 1000 ,
                                      'rtto': 1003,
                                      'rtv': 3,
                                      'krtt': 0,
                                      'min_rtt': 4 ,
                                      'max_rtt': 1000,
                                      'ack_hold': 200,
                                      'uptime': 4239741  ,
                                      'sent_idletime': 7832 ,
                                      'receive_idletime': 8032  ,
                                      'status_flags': 'active open',
                                      'option_flags': 'nagle, path mtu capable',
                                      'ip_precedence_value': 6,
                                      'datagram':
                                          {
                                              'datagram_sent':
                                                  {
                                                      'value': 166,
                                                      'retransmit':0 ,
                                                      'fastretransmit':0 ,
                                                      'partialack': 0,
                                                      'second_congestion':0 ,
                                                      'with_data':87 ,
                                                      'total_data': 3303,
                                                  },
                                              'datagram_received':
                                                  {
                                                      'value':164 ,
                                                      'out_of_order':0,
                                                      'with_data': 80,
                                                      'total_data': 2374,
                                                  },

                                          },
                                      'packet_fast_path': 0,
                                      'packet_fast_processed': 0,
                                      'packet_slow_path':0 ,
                                      'fast_lock_acquisition_failures':0,
                                      'lock_slow_path': 0,
                                      'tcp_semaphore': '0x1286E7EC',
                                      'tcp_semaphore_status': 'FREE',

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
                                          'in_queue_depth': 0,
                                          'out_queue_depth': 0,
                                      },

                                  },
                              'bgp_negotiated_capabilities':
                                  {'route_refresh': 'advertised and received(new)',
                                   'vpnv4_unicast': 'advertised and received',
                                   'vpnv6_unicast': 'advertised and received',
                                   'graceful_restart': 'received',
                                   'enhanced_refresh': 'advertised',
                                   'four_octets_asn': 'advertised and received',
                                   'stateful_switchover': 'NO for session 1',
                                   'graceful_restart_af_advertised_by_peer':
                                       'VPNv4 Unicast (was not preserved, VPNv6 Unicast (was not preserved',
                                   'graceful_remote_restart_timer':120,
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
                                          'last_write': '00:00:09',
                                          'session_state': 'established',
                                          'up_time': '01:10:35',
                                          'current_time': '0x530449',
                                      },
                                  'vpnv6 unicast':
                                      {
                                          'last_read': '00:00:07',
                                          'last_write': '00:00:12',
                                          'session_state': 'established',
                                          'up_time': '01:10:38',
                                          'current_time': '0x530FF5',
                                      },

                                  },
                              },
                        '3.3.3.3':
                             {'remote_as': 100,
                              'link': 'internal',
                              'bgp_version': 4,
                              'router_id': '3.3.3.3',
                              'session_state': 'established',
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
                                           'local_port': '56031',
                                           'foreign_host': '3.3.3.3',
                                           'foreign_port': '179',
                                           'mss': 536,
                                           },
                                      'min_time_between_advertisement_runs': 0,
                                      'address_tracking_status': 'enabled',
                                      'rib_route_ip': '3.3.3.3',
                                      'tcp_path_mtu_discovery': 'enabled',
                                      'graceful_restart': 'disabled',
                                      'connection_state': 'estab',
                                      'io_status': 1,
                                      'unread_input_bytes': 0,
                                      'ecn_connection': 'disabled',
                                      'minimum_incoming_ttl': 0,
                                      'outgoing_ttl': 255,
                                      'connection_tableid': 0,
                                      'maximum_output_segment_queue_size': 50,
                                      'enqueued_packets':
                                          {
                                              'retransmit_packet': 0,
                                              'input_packet': 0,
                                              'mis_ordered_packet': 0,
                                          },
                                      'iss': 2116369173,
                                      'snduna': 2116372477,
                                      'sndnxt': 2116372477,
                                      'irs': 4033842748,
                                      'rcvnxt': 4033845123,
                                      'sndwnd': 16616,
                                      'snd_scale':0,
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
                                      'datagram':
                                          {
                                              'datagram_sent':
                                                  {
                                                      'value': 167,
                                                      'retransmit': 0,
                                                      'fastretransmit': 0,
                                                      'partialack': 0,
                                                      'second_congestion': 0,
                                                      'with_data': 87,
                                                      'total_data': 3303,
                                                  },
                                              'datagram_received':
                                                  {
                                                      'value': 165,
                                                      'out_of_order': 0,
                                                      'with_data': 80,
                                                      'total_data': 2374,
                                                  },

                                          },
                                      'packet_fast_path': 0,
                                      'packet_fast_processed': 0,
                                      'packet_slow_path': 0,
                                      'fast_lock_acquisition_failures': 0,
                                      'lock_slow_path': 0,
                                      'tcp_semaphore': '0x1286E85C',
                                      'tcp_semaphore_status': 'FREE',
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
                                          'in_queue_depth': 0,
                                          'out_queue_depth': 0,
                                      },

                                  },
                              'bgp_negotiated_capabilities':
                                  {'route_refresh': 'advertised and received(new)',
                                   'vpnv4_unicast': 'advertised and received',
                                   'vpnv6_unicast': 'advertised and received',
                                   'graceful_restart': 'received',
                                   'enhanced_refresh': 'advertised',
                                   'four_octets_asn': 'advertised and received',
                                   'stateful_switchover': 'NO for session 1',
                                   'graceful_restart_af_advertised_by_peer':
                                       'VPNv4 Unicast (was not preserved, VPNv6 Unicast (was not preserved',
                                   'graceful_remote_restart_timer': 120,
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
                                          'last_write': '00:00:43',
                                          'session_state': 'established',
                                          'up_time': '01:10:41',
                                          'current_time': '0x530638',
                                      },
                                  'vpnv6 unicast':
                                      {
                                          'last_read': '00:00:08',
                                          'last_write': '00:00:47',
                                          'session_state': 'established',
                                          'up_time': '01:10:44',
                                          'current_time': '0x5313D8',
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
                              'shutdown': True,
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
                                              'mss': 1460,
                                          },
                                      'min_time_between_advertisement_runs': 0,
                                      'address_tracking_status': 'enabled',
                                      'rib_route_ip': '10.4.6.6',
                                      'tcp_path_mtu_discovery': 'enabled',
                                      'graceful_restart': 'disabled',
                                      'connection_state': 'estab',
                                      'io_status': 1,
                                      'unread_input_bytes': 0,
                                      'ecn_connection': 'disabled',
                                      'minimum_incoming_ttl': 0,
                                      'outgoing_ttl': 1,
                                      'connection_tableid': 1,
                                      'maximum_output_segment_queue_size': 50,
                                      'enqueued_packets':
                                          {
                                              'retransmit_packet': 0,
                                              'input_packet': 0,
                                              'mis_ordered_packet': 0,
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
                                      'datagram':
                                          {
                                              'datagram_sent':
                                                  {
                                                      'value': 138,
                                                      'retransmit': 0,
                                                      'fastretransmit': 0,
                                                      'partialack': 0,
                                                      'second_congestion': 0,
                                                      'with_data': 72,
                                                      'total_data': 1537,
                                                  },
                                              'datagram_received':
                                                  {
                                                      'value': 137,
                                                      'out_of_order': 0,
                                                      'with_data': 66,
                                                      'total_data': 1330,
                                                  },

                                          },
                                      'packet_fast_path': 0,
                                      'packet_fast_processed': 0,
                                      'packet_slow_path': 0,
                                      'fast_lock_acquisition_failures': 0,
                                      'lock_slow_path': 0,
                                      'tcp_semaphore': '0x1286E62C',
                                      'tcp_semaphore_status': 'FREE',
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
                                          'in_queue_depth': 0,
                                          'out_queue_depth': 0,
                                      },

                                  },
                              'bgp_negotiated_capabilities':
                                  {'route_refresh': 'advertised',
                                   'ipv4_unicast': 'advertised and received',
                                   'enhanced_refresh': 'advertised',
                                   'four_octets_asn': 'advertised',
                                   'stateful_switchover': 'NO for session 1',
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
                                          'last_write': '00:00:30',
                                          'session_state': 'established',
                                          'up_time': '01:01:59',
                                          'current_time': '0x530A19'
                                      },
                                  },
                              },
                         '2001:DB8:4:6::6':
                             {'remote_as': 300,
                              'link': 'external',
                              'bgp_version': 4,
                              'router_id': '10.4.6.6',
                              'session_state': 'established',
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
                                              'mss': 1440,
                                          },
                                      'min_time_between_advertisement_runs': 0,
                                      'address_tracking_status': 'enabled',
                                      'rib_route_ip': '2001:DB8:4:6::6',
                                      'tcp_path_mtu_discovery': 'enabled',
                                      'graceful_restart': 'disabled',
                                      'connection_state': 'estab',
                                      'io_status': 1,
                                      'unread_input_bytes': 0,
                                      'ecn_connection': 'disabled',
                                      'minimum_incoming_ttl': 0,
                                      'outgoing_ttl': 1,
                                      'connection_tableid': 503316481,
                                      'maximum_output_segment_queue_size': 50,
                                      'enqueued_packets':
                                          {
                                              'retransmit_packet': 0,
                                              'input_packet': 0,
                                              'mis_ordered_packet': 0,
                                          },
                                      'iss': 164676617,
                                      'snduna': 164678296,
                                      'sndnxt': 164678296,
                                      'irs': 1797203329,
                                      'rcvnxt':1797204710,
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
                                      'datagram':
                                          {
                                              'datagram_sent':
                                                  {
                                                      'value': 139,
                                                      'retransmit': 0,
                                                      'fastretransmit': 0,
                                                      'partialack': 0,
                                                      'second_congestion': 0,
                                                      'with_data': 139,
                                                      'total_data': 7246,
                                                  },
                                              'datagram_received':
                                                  {
                                                      'value': 138,
                                                      'out_of_order': 0,
                                                      'with_data': 66,
                                                      'total_data': 1380,
                                                  },

                                          },
                                      'packet_fast_path': 0,
                                      'packet_fast_processed': 0,
                                      'packet_slow_path': 0,
                                      'fast_lock_acquisition_failures': 0,
                                      'lock_slow_path': 0,
                                      'tcp_semaphore': '0x1286E9AC',
                                      'tcp_semaphore_status': 'FREE',

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
                                          'in_queue_depth': 0,
                                          'out_queue_depth': 0,
                                      },

                                  },
                              'bgp_negotiated_capabilities':
                                  {'route_refresh': 'advertised',
                                   'ipv6_unicast': 'advertised and received',
                                   'enhanced_refresh': 'advertised',
                                   'four_octets_asn': 'advertised',
                                   'stateful_switchover': 'NO for session 1',
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
                                          'last_write': '00:00:06',
                                          'session_state': 'established',
                                          'up_time': '01:01:58',
                                          'current_time': '0x5315CE'
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
                                              'mss': 1460,
                                          },
                                      'min_time_between_advertisement_runs': 0,
                                      'address_tracking_status': 'enabled',
                                      'rib_route_ip': '20.4.6.6',
                                      'tcp_path_mtu_discovery': 'enabled',
                                      'graceful_restart': 'disabled',
                                      'connection_state': 'estab',
                                      'io_status': 1,
                                      'unread_input_bytes': 0,
                                      'ecn_connection': 'disabled',
                                      'minimum_incoming_ttl': 0,
                                      'outgoing_ttl': 1,
                                      'connection_tableid': 2,
                                      'maximum_output_segment_queue_size': 50,
                                      'enqueued_packets':
                                          {
                                              'retransmit_packet': 0,
                                              'input_packet': 0,
                                              'mis_ordered_packet': 0,
                                          },
                                      'iss': 2048397580,
                                      'snduna': 2048398972,
                                      'sndnxt':2048398972 ,
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
                                      'datagram':
                                          {
                                              'datagram_sent':
                                                  {
                                                      'value': 137,
                                                      'retransmit': 0,
                                                      'fastretransmit': 0,
                                                      'partialack': 0,
                                                      'second_congestion': 0,
                                                      'with_data': 71,
                                                      'total_data': 1391,
                                                  },
                                              'datagram_received':
                                                  {
                                                      'value': 135,
                                                      'out_of_order': 0,
                                                      'with_data': 66,
                                                      'total_data': 1330,
                                                  },

                                          },
                                      'packet_fast_path': 0,
                                      'packet_fast_processed': 0,
                                      'packet_slow_path': 0,
                                      'fast_lock_acquisition_failures': 0,
                                      'lock_slow_path': 0,
                                      'tcp_semaphore': '0x1286E8CC',
                                      'tcp_semaphore_status': 'FREE',
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
                                          'in_queue_depth': 0,
                                          'out_queue_depth': 0,
                                      },

                                  },
                              'bgp_negotiated_capabilities':
                                  {'route_refresh': 'advertised',
                                   'ipv4_unicast': 'advertised and received',
                                   'enhanced_refresh': 'advertised',
                                   'four_octets_asn': 'advertised',
                                   'stateful_switchover': 'NO for session 1',
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
                                          'last_write': '00:00:21',
                                          'session_state': 'established',
                                          'up_time': '01:01:51',
                                          'current_time': '0x530C0D',
                                      },
                                  },
                              },
                         '2001:DB8:20:4:6::6':
                             {'remote_as': 400,
                              'link': 'external',
                              'bgp_version': 4,
                              'router_id': '20.4.6.6',
                              'session_state': 'established',
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
                                              'mss': 1440,
                                          },
                                      'min_time_between_advertisement_runs': 0,
                                      'address_tracking_status': 'enabled',
                                      'rib_route_ip': '2001:DB8:20:4:6::6',
                                      'tcp_path_mtu_discovery': 'enabled',
                                      'graceful_restart': 'disabled',
                                      'connection_state': 'estab',
                                      'io_status': 1,
                                      'unread_input_bytes': 0,
                                      'ecn_connection': 'disabled',
                                      'minimum_incoming_ttl': 0,
                                      'outgoing_ttl': 1,
                                      'connection_tableid': 503316482,
                                      'maximum_output_segment_queue_size': 50,
                                      'enqueued_packets':
                                          {
                                              'retransmit_packet': 0,
                                              'input_packet': 0,
                                              'mis_ordered_packet': 0,
                                          },
                                      'iss': 3178074389,
                                      'snduna':3178075806,
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
                                      'datagram':
                                          {
                                              'datagram_sent':
                                                  {
                                                      'value': 138,
                                                      'retransmit': 0,
                                                      'fastretransmit': 0,
                                                      'partialack': 0,
                                                      'second_congestion': 0,
                                                      'with_data': 138,
                                                      'total_data': 6944,
                                                  },
                                              'datagram_received':
                                                  {
                                                      'value': 137,
                                                      'out_of_order': 0,
                                                      'with_data': 66,
                                                      'total_data': 1380,
                                                  },

                                          },
                                      'packet_fast_path': 0,
                                      'packet_fast_processed': 0,
                                      'packet_slow_path': 0,
                                      'fast_lock_acquisition_failures': 0,
                                      'lock_slow_path': 0,
                                      'tcp_semaphore': '0x1286E93C',
                                      'tcp_semaphore_status': 'FREE',
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
                                          'in_queue_depth': 0,
                                          'out_queue_depth': 0,
                                      },

                                  },
                              'bgp_negotiated_capabilities':
                                  {'route_refresh': 'advertised',
                                   'ipv6_unicast': 'advertised and received',
                                   'enhanced_refresh': 'advertised',
                                   'four_octets_asn': 'advertised',
                                   'stateful_switchover': 'NO for session 1',
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
                                          'last_write': '00:00:01',
                                          'session_state': 'established',
                                          'up_time': '01:01:51',
                                          'current_time': '0x5319B5',
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
  Description: router2222222
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

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpAllNeighbors(device=self.device)
        with self.assertRaises(SchemaMissingKeyError):
            parsed_output = obj.parse()
    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowBgpAllNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

# =============================================================
# Unit test for 'show bgp all neighbors <WORD> received-routes'
# =============================================================

class test_show_bgp_neighbors_received_routes(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {'vrf':
                            {'default':
                              {'neighbor':
                                {'21.0.0.2':
                                  {'address_family':
                                    {'vpnv4 unicast':
                                      {'bgp_table_version': 66,
                                       'local_router_id': '4.4.4.4',
                                       'received_routes': {}},
                                     'vpnv4 unicast RD 300:1':
                                      {'bgp_table_version': 66,
                                       'default_vrf': 'VRF1',
                                       'local_router_id': '4.4.4.4',
                                       'received_routes':
                                        {'46.1.1.0/24':
                                          {'index':
                                            {1:
                                              {'metric': 2219,
                                               'next_hop': '10.4.6.6',
                                               'origin_codes': 'e',
                                               'path': '300 '
                                                       '33299 '
                                                       '51178 '
                                                       '47751 '
                                                       '{27016}',
                                               'status_codes': '*',
                                               'weight': 0}}},
                                         '46.1.2.0/24':
                                          {'index':
                                            {1:
                                              {'metric': 2219,
                                               'next_hop': '10.4.6.6',
                                               'origin_codes': 'e',
                                               'path': '300 '
                                                       '33299 '
                                                       '51178 '
                                                       '47751 '
                                                       '{27016}',
                                               'status_codes': '*',
                                               'weight': 0}}},
                                         '46.1.3.0/24':
                                          {'index':
                                            {1:
                                              {'metric': 2219,
                                               'next_hop': '10.4.6.6',
                                               'origin_codes': 'e',
                                               'path': '300 '
                                                       '33299 '
                                                       '51178 '
                                                       '47751 '
                                                       '{27016}',
                                               'status_codes': '*',
                                               'weight': 0}}},
                                         '46.1.4.0/24':
                                          {'index':
                                            {1:
                                              {'metric': 2219,
                                               'next_hop': '10.4.6.6',
                                               'origin_codes': 'e',
                                               'path': '300 '
                                                       '33299 '
                                                       '51178 '
                                                       '47751 '
                                                       '{27016}',
                                               'status_codes': '*',
                                               'weight': 0}}},
                                         '46.1.5.0/24':
                                          {'index':
                                            {1:
                                              {'metric': 2219,
                                               'next_hop': '10.4.6.6',
                                               'origin_codes': 'e',
                                               'path': '300 '
                                                       '33299 '
                                                       '51178 '
                                                       '47751 '
                                                       '{27016}',
                                               'status_codes': '*',
                                               'weight': 0}
                                            }
                                          }
                                        },
                                       'route_distinguisher': '300:1'}}}}}}}


    golden_output = {'execute.return_value': '''
        R4_iosv#show bgp all neighbors 10.4.6.6 received-routes 
        For address family: VPNv4 Unicast
        BGP table version is 66, local router ID is 4.4.4.4
        Status codes: s suppressed, d damped, h history, * valid, > best, i - internal, 
                      r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter, 
                      x best-external, a additional-path, c RIB-compressed, 
        Origin codes: i - IGP, e - EGP, ? - incomplete
        RPKI validation codes: V valid, I invalid, N Not found

             Network          Next Hop            Metric LocPrf Weight Path
        Route Distinguisher: 300:1 (default for vrf VRF1) VRF Router ID 44.44.44.44
         *   46.1.1.0/24      10.4.6.6              2219             0 300 33299 51178 47751 {27016} e
         *   46.1.2.0/24      10.4.6.6              2219             0 300 33299 51178 47751 {27016} e
         *   46.1.3.0/24      10.4.6.6              2219             0 300 33299 51178 47751 {27016} e
         *   46.1.4.0/24      10.4.6.6              2219             0 300 33299 51178 47751 {27016} e
         *   46.1.5.0/24      10.4.6.6              2219             0 300 33299 51178 47751 {27016} e

        Total number of prefixes 5
        '''}

    golden_parsed_output2 = {
        'vrf': 
            {'default': 
                {'neighbor': 
                    {'19.0.101.1': 
                        {'address_family': 
                            {'ipv4 multicast': 
                                {'bgp_table_version': 175,
                                'local_router_id': '20.0.0.6',
                                'received_routes': 
                                    {'1.2.1.0/24': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '2 '
                                                        '3 '
                                                        '4',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    '1.2.2.0/24': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '2 '
                                                        '3 '
                                                        '4',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}}}},
                            'ipv4 unicast': 
                                {'bgp_table_version': 174,
                                'local_router_id': '20.0.0.6',
                                'received_routes': 
                                    {'1.1.1.0/24': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 2222,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '1 '
                                                        '2 '
                                                        '3 '
                                                        '65000 '
                                                        '23',
                                                'path_type': 'i',
                                                'status_codes': '*',
                                                'weight': 0}}},
                                    '1.1.2.0/24': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 2222,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '1 '
                                                        '2 '
                                                        '3 '
                                                        '65000 '
                                                        '23',
                                                'path_type': 'i',
                                                'status_codes': '*',
                                                'weight': 0}}},
                                    '1.6.0.0/16': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '10 '
                                                        '20 '
                                                        '30 '
                                                        '40 '
                                                        '50 '
                                                        '60 '
                                                        '70 '
                                                        '80 '
                                                        '90',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}}}},
                            'ipv6 multicast': 
                                {'bgp_table_version': 6,
                                'local_router_id': '20.0.0.6',
                                'received_routes': {}},
                            'ipv6 unicast': 
                                {'bgp_table_version': 173,
                                'local_router_id': '20.0.0.6',
                                'received_routes': {}},
                            'link-state': 
                                {'bgp_table_version': 173,
                                'local_router_id': '20.0.0.6',
                                'received_routes': 
                                    {'[2]:[77][7,0][9.9.9.9,1,151587081][29.1.1.1,22][19.0.101.1,29.0.1.30]/616': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 4444,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '3 '
                                                      '10 '
                                                      '20 '
                                                      '30 '
                                                      '40 '
                                                      '50 '
                                                      '60 '
                                                      '70 '
                                                      '80 '
                                                      '90',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    '[2]:[77][7,0][9.9.9.9,2,151587081][29.1.1.1,22][19.0.101.1,29.0.1.31]/616': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 4444,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '3 '
                                                      '10 '
                                                      '20 '
                                                      '30 '
                                                      '40 '
                                                      '50 '
                                                      '60 '
                                                      '70 '
                                                      '80 '
                                                      '90',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}}}},
                            'vpnv4 unicast': 
                                {'bgp_table_version': 183,
                                'local_router_id': '20.0.0.6',
                                'received_routes': {}},
                            'vpnv4 unicast RD 0:0': 
                                {'bgp_table_version': 183,
                                'local_router_id': '20.0.0.6',
                                'route_distinguisher': '0:0',
                                'received_routes': {}},
                            'vpnv4 unicast RD 101:100': 
                                {'bgp_table_version': 183,
                                'local_router_id': '20.0.0.6',
                                'route_distinguisher': '101:100',
                                'received_routes': 
                                    {'1.3.1.0/24': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 4444,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '3 '
                                                        '10 '
                                                        '20 '
                                                        '4 '
                                                        '5 '
                                                        '6 '
                                                        '3 '
                                                        '10 '
                                                        '20 '
                                                        '4 '
                                                        '5 '
                                                        '6',
                                                'path_type': 'i',
                                                'status_codes': '*',
                                                'weight': 0}}},
                                    '1.3.2.0/24': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 4444,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '3 '
                                                     '10 '
                                                     '20 '
                                                     '4 '
                                                     '5 '
                                                     '6 '
                                                     '3 '
                                                     '10 '
                                                     '20 '
                                                     '4 '
                                                     '5 '
                                                     '6',
                                                'path_type': 'i',
                                                'status_codes': '*',
                                                'weight': 0}}}}},
                            'vpnv4 unicast RD 102:100': 
                                {'bgp_table_version': 183,
                                'local_router_id': '20.0.0.6',
                                'route_distinguisher': '102:100',
                                'received_routes': {}},
                            'vpnv6 unicast': 
                                {'bgp_table_version': 13,
                                'local_router_id': '20.0.0.6',
                                'received_routes': {}},
                            'vpnv6 unicast RD 0xbb00010000000000': 
                                {'bgp_table_version': 13,
                                'local_router_id': '20.0.0.6',
                                'route_distinguisher': '0xbb00010000000000',
                                'received_routes': {}},
                            'vpnv6 unicast RD 100:200': 
                                {'bgp_table_version': 13,
                                'local_router_id': '20.0.0.6',
                                'route_distinguisher': '100:200',
                                'received_routes': 
                                    {'aaaa:1::/113': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'next_hop': '4444',
                                                'origin_codes': 'i',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    'aaaa:1::8000/113': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'next_hop': '4444',
                                                'origin_codes': 'i',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}}}}}}}}}}

    golden_output2 = {'execute.return_value': '''
        For address family: IPv4 Unicast
        BGP table version is 174, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        * i1.1.1.0/24         19.0.101.1            2222        100          0 1 2 3 65000 23 i
        * i1.1.2.0/24         19.0.101.1            2222        100          0 1 2 3 65000 23 i
        *>i1.6.0.0/16         19.0.101.1                        100          0 10 20 30 40 50 60 70 80 90 i


        For address family: IPv4 Multicast
        BGP table version is 175, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>i1.2.1.0/24         19.0.101.1                        100          0 2 3 4 i
        *>i1.2.2.0/24         19.0.101.1                        100          0 2 3 4 i


        For address family: IPv6 Unicast
        BGP table version is 173, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path


        For address family: IPv6 Multicast
        BGP table version is 6, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path


        For address family: VPNv4 Unicast
        BGP table version is 183, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        Route Distinguisher: 0:0

        Route Distinguisher: 101:100
        * i1.3.1.0/24         19.0.101.1            4444        100          0 3 10 20 4 5 6 3 10 20 4 5 6 i
        * i1.3.2.0/24         19.0.101.1            4444        100          0 3 10 20 4 5 6 3 10 20 4 5 6 i

        Route Distinguisher: 102:100


        For address family: VPNv6 Unicast
        BGP table version is 13, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        Route Distinguisher: 100:200
        *>iaaaa:1::/113       ::ffff:19.0.101.1
                                                    4444        100          0 i
        *>iaaaa:1::8000/113   ::ffff:19.0.101.1
                                                    4444        100          0 i

        Route Distinguisher: 0xbb00010000000000


        For address family: Link-State
        BGP table version is 173, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>i[2]:[77][7,0][9.9.9.9,1,151587081][29.1.1.1,22][19.0.101.1,29.0.1.30]/616
                              19.0.101.1            4444        100          0 3 10 20 30 40 50 60 70 80 90 i
        *>i[2]:[77][7,0][9.9.9.9,2,151587081][29.1.1.1,22][19.0.101.1,29.0.1.31]/616
                              19.0.101.1            4444        100          0 3 10 20 30 40 50 60 70 80 90 i
        '''}

    def test_show_bgp_vrf_all_neighbors_received_routes_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowBgpAllNeighborsReceivedRoutes(device=self.device)
        parsed_output = obj.parse(neighbor='21.0.0.2')
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_bgp_vrf_all_neighbors_received_routes_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowBgpAllNeighborsReceivedRoutes(device=self.device)
        parsed_output = obj.parse(neighbor='19.0.101.1')
        self.assertEqual(parsed_output,self.golden_parsed_output2)

    def test_show_bgp_vrf_all_neighbors_received_routes_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpAllNeighborsReceivedRoutes(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(neighbor='21.0.0.2')



class test_show_ip_bgp_template_peer_session(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'peer_session':
            {'PEER-SESSION':
                {
                    'local_policies' : '0x5025FD',
                    'inherited_polices' : '0x0',
                    'fall_over_bfd': True,
                    'suppress_four_byte_as_capability': True,
                    'description': 'desc1!',
                    'disable_connected_check': True,
                    'ebgp_multihop_enable': True,
                    'ebgp_multihop_max_hop': 254,
                    'local_as_as_no': 255,
                    'password_text': 'is configured',
                    'remote_as': 321,
                    'shutdown': True,
                    'keepalive_interval': 10,
                    'holdtime': 30,
                    'transport_connection_mode': 'passive',
                    'update_source': 'Loopback0',
                    'index': 1,
                },
            'PEER-SESSION2':
                {
                    'local_policies' : '0x100000',
                    'inherited_polices' : '0x0',
                    'fall_over_bfd': True,
                    'index': 2,
                }

            },
    }

    golden_output = {'execute.return_value':'''
            R4_iosv#show ip bgp template peer-session
            Template:PEER-SESSION, index:1
            Local policies:0x5025FD, Inherited polices:0x0
            Locally configured session commands:
             remote-as 321
             password is configured
             shutdown
             ebgp-multihop 254
             update-source Loopback0
             transport connection-mode passive
             description desc1!
             dont-capability-negotiate four-octets-as
             timers 10 30
             local-as 255
             disable-connected-check
             fall-over bfd
            Inherited session commands:

            Template:PEER-SESSION2, index:2
            Local policies:0x100000, Inherited polices:0x0
            Locally configured session commands:
             fall-over bfd
            Inherited session commands:
    '''}
    golden_parsed_output_1 = {
        'peer_session':
            {'PEER-SESSION':
                {
                    'local_policies': '0x5025FD',
                    'inherited_polices': '0x0',
                    'fall_over_bfd': True,
                    'suppress_four_byte_as_capability': True,
                    'description': 'desc1!',
                    'disable_connected_check': True,
                    'ebgp_multihop_enable': True,
                    'ebgp_multihop_max_hop': 254,
                    'local_as_as_no': 255,
                    'password_text': 'is configured',
                    'remote_as': 321,
                    'shutdown': True,
                    'transport_connection_mode': 'passive',
                    'update_source': 'Loopback0',
                    'index': 1,
                    'inherited_session_commands':
                        {
                            'keepalive_interval': 10,
                            'holdtime': 30,
                        },
                },
                'PEER-SESSION2':
                    {
                        'local_policies': '0x100000',
                        'inherited_polices': '0x0',
                        'fall_over_bfd': True,
                        'index': 2,
                    }

            },
    }

    golden_output_1 = {'execute.return_value': '''
                R4_iosv#show ip bgp template peer-session
                Template:PEER-SESSION, index:1
                Local policies:0x5025FD, Inherited polices:0x0
                Locally configured session commands:
                 remote-as 321
                 password is configured
                 shutdown
                 ebgp-multihop 254
                 update-source Loopback0
                 transport connection-mode passive
                 description desc1!
                 dont-capability-negotiate four-octets-as
                 local-as 255
                 disable-connected-check
                 fall-over bfd
                Inherited session commands:
                timers 10 30

                Template:PEER-SESSION2, index:2
                Local policies:0x100000, Inherited polices:0x0
                Locally configured session commands:
                 fall-over bfd
                Inherited session commands:
        '''}

    golden_parsed_output_2 = {
        'peer_session':
            {'PEER-SESSION':
                {
                    'local_policies': '0x5025FD',
                    'inherited_polices': '0x0',
                    'fall_over_bfd': True,
                    'suppress_four_byte_as_capability': True,
                    'description': 'desc1!',
                    'disable_connected_check': True,
                    'ebgp_multihop_enable': True,
                    'ebgp_multihop_max_hop': 254,
                    'local_as_as_no': 255,
                    'password_text': 'is configured',
                    'remote_as': 321,
                    'shutdown': True,
                    'transport_connection_mode': 'passive',
                    'update_source': 'Loopback0',
                    'index': 1,
                    'inherited_session_commands':
                        {
                            'keepalive_interval': 10,
                            'holdtime': 30,
                        },
                }
            },
    }

    golden_output_2 = {'execute.return_value': '''
                    R4_iosv#show ip bgp template peer-session PEER-SESSION
                    Template:PEER-SESSION, index:1
                    Local policies:0x5025FD, Inherited polices:0x0
                    Locally configured session commands:
                     remote-as 321
                     password is configured
                     shutdown
                     ebgp-multihop 254
                     update-source Loopback0
                     transport connection-mode passive
                     description desc1!
                     dont-capability-negotiate four-octets-as
                     local-as 255
                     disable-connected-check
                     fall-over bfd
                    Inherited session commands:
                    timers 10 30
            '''}
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpBgpTemplatePeerSession(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpBgpTemplatePeerSession(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpBgpTemplatePeerSession(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpBgpTemplatePeerSession(device=self.device)
        parsed_output = obj.parse(template_name='PEER-SESSION')
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

# ====================================================
# Unit test for 'show bgp all neighbors <WORD> routes'
# ====================================================

class test_show_bgp_all_neighbors_routes(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = \
      {'vrf':
        {'default':
          {'neighbor':
            {'21.0.0.2':
              {'address_family':
                {'vpnv4 unicast':
                  {'bgp_table_version': 56,
                   'local_router_id': '4.4.4.4',
                   'routes': {}},
                'vpnv4 unicast RD 200:1':
                  {'bgp_table_version': 56,
                   'local_router_id': '4.4.4.4',
                   'route_distinguisher': '200:1',
                   'routes': {'15.1.1.0/24': {'index': {1: {'localprf': 100,
                                                            'metric': 2219,
                                                            'next_hop': '1.1.1.1',
                                                            'origin_codes': 'e',
                                                            'path': '200 '
                                                                    '33299 '
                                                                    '51178 '
                                                                    '47751 '
                                                                    '{27016}',
                                                            'path_type': 'i',
                                                            'status_codes': '*>',
                                                            'weight': 0}}},
                              '15.1.2.0/24': {'index': {1: {'localprf': 100,
                                                            'metric': 2219,
                                                            'next_hop': '1.1.1.1',
                                                            'origin_codes': 'e',
                                                            'path': '200 '
                                                                    '33299 '
                                                                    '51178 '
                                                                    '47751 '
                                                                    '{27016}',
                                                            'path_type': 'i',
                                                            'status_codes': '*>',
                                                            'weight': 0}}},
                              '15.1.3.0/24': {'index': {1: {'localprf': 100,
                                                            'metric': 2219,
                                                            'next_hop': '1.1.1.1',
                                                            'origin_codes': 'e',
                                                            'path': '200 '
                                                                    '33299 '
                                                                    '51178 '
                                                                    '47751 '
                                                                    '{27016}',
                                                            'path_type': 'i',
                                                            'status_codes': '*>',
                                                            'weight': 0}}},
                              '15.1.4.0/24': {'index': {1: {'localprf': 100,
                                                            'metric': 2219,
                                                            'next_hop': '1.1.1.1',
                                                            'origin_codes': 'e',
                                                            'path': '200 '
                                                                    '33299 '
                                                                    '51178 '
                                                                    '47751 '
                                                                    '{27016}',
                                                            'path_type': 'i',
                                                            'status_codes': '*>',
                                                            'weight': 0}}},
                              '15.1.5.0/24': {'index': {1: {'localprf': 100,
                                                            'metric': 2219,
                                                            'next_hop': '1.1.1.1',
                                                            'origin_codes': 'e',
                                                            'path': '200 '
                                                                    '33299 '
                                                                    '51178 '
                                                                    '47751 '
                                                                    '{27016}',
                                                            'path_type': 'i',
                                                            'status_codes': '*>',
                                                            'weight': 0}}}}},
                'vpnv4 unicast RD 200:2':
                  {'bgp_table_version': 56,
                   'local_router_id': '4.4.4.4',
                   'route_distinguisher': '200:2',
                   'routes': {'15.1.1.0/24': {'index': {1: {'localprf': 100,
                                                            'metric': 2219,
                                                            'next_hop': '1.1.1.1',
                                                            'origin_codes': 'e',
                                                            'path': '200 '
                                                                    '33299 '
                                                                    '51178 '
                                                                    '47751 '
                                                                    '{27016}',
                                                            'path_type': 'i',
                                                            'status_codes': '*>',
                                                            'weight': 0}}},
                              '15.1.2.0/24': {'index': {1: {'localprf': 100,
                                                            'metric': 2219,
                                                            'next_hop': '1.1.1.1',
                                                            'origin_codes': 'e',
                                                            'path': '200 '
                                                                    '33299 '
                                                                    '51178 '
                                                                    '47751 '
                                                                    '{27016}',
                                                            'path_type': 'i',
                                                            'status_codes': '*>',
                                                            'weight': 0}}},
                              '15.1.3.0/24': {'index': {1: {'localprf': 100,
                                                            'metric': 2219,
                                                            'next_hop': '1.1.1.1',
                                                            'origin_codes': 'e',
                                                            'path': '200 '
                                                                    '33299 '
                                                                    '51178 '
                                                                    '47751 '
                                                                    '{27016}',
                                                            'path_type': 'i',
                                                            'status_codes': '*>',
                                                            'weight': 0}}},
                              '15.1.4.0/24': {'index': {1: {'localprf': 100,
                                                            'metric': 2219,
                                                            'next_hop': '1.1.1.1',
                                                            'origin_codes': 'e',
                                                            'path': '200 '
                                                                    '33299 '
                                                                    '51178 '
                                                                    '47751 '
                                                                    '{27016}',
                                                            'path_type': 'i',
                                                            'status_codes': '*>',
                                                            'weight': 0}}},
                              '15.1.5.0/24': {'index': {1: {'localprf': 100,
                                                            'metric': 2219,
                                                            'next_hop': '1.1.1.1',
                                                            'origin_codes': 'e',
                                                            'path': '200 '
                                                                    '33299 '
                                                                    '51178 '
                                                                    '47751 '
                                                                    '{27016}',
                                                            'path_type': 'i',
                                                            'status_codes': '*>',
                                                            'weight': 0}}}}},
            'vpnv4 unicast RD 300:1':
              {'bgp_table_version': 56,
               'default_vrf': 'VRF1',
               'local_router_id': '4.4.4.4',
               'route_distinguisher': '300:1',
               'routes': {'15.1.1.0/24': {'index': {1: {'localprf': 100,
                                                        'metric': 2219,
                                                        'next_hop': '1.1.1.1',
                                                        'origin_codes': 'e',
                                                        'path': '200 '
                                                                '33299 '
                                                                '51178 '
                                                                '47751 '
                                                                '{27016}',
                                                        'path_type': 'i',
                                                        'status_codes': '*',
                                                        'weight': 0},
                                                    2: {'localprf': 100,
                                                        'metric': 2219,
                                                        'next_hop': '1.1.1.1',
                                                        'origin_codes': 'e',
                                                        'path': '200 '
                                                                '33299 '
                                                                '51178 '
                                                                '47751 '
                                                                '{27016}',
                                                        'path_type': 'i',
                                                        'status_codes': '*',
                                                        'weight': 0}}},
                          '15.1.2.0/24': {'index': {1: {'localprf': 100,
                                                        'metric': 2219,
                                                        'next_hop': '1.1.1.1',
                                                        'origin_codes': 'e',
                                                        'path': '200 '
                                                                '33299 '
                                                                '51178 '
                                                                '47751 '
                                                                '{27016}',
                                                        'path_type': 'i',
                                                        'status_codes': '*',
                                                        'weight': 0},
                                                    2: {'localprf': 100,
                                                        'metric': 2219,
                                                        'next_hop': '1.1.1.1',
                                                        'origin_codes': 'e',
                                                        'path': '200 '
                                                                '33299 '
                                                                '51178 '
                                                                '47751 '
                                                                '{27016}',
                                                        'path_type': 'i',
                                                        'status_codes': '*',
                                                        'weight': 0}}},
                          '15.1.3.0/24': {'index': {1: {'localprf': 100,
                                                        'metric': 2219,
                                                        'next_hop': '1.1.1.1',
                                                        'origin_codes': 'e',
                                                        'path': '200 '
                                                                '33299 '
                                                                '51178 '
                                                                '47751 '
                                                                '{27016}',
                                                        'path_type': 'i',
                                                        'status_codes': '*',
                                                        'weight': 0},
                                                    2: {'localprf': 100,
                                                        'metric': 2219,
                                                        'next_hop': '1.1.1.1',
                                                        'origin_codes': 'e',
                                                        'path': '200 '
                                                                '33299 '
                                                                '51178 '
                                                                '47751 '
                                                                '{27016}',
                                                        'path_type': 'i',
                                                        'status_codes': '*',
                                                        'weight': 0}}},
                          '15.1.4.0/24': {'index': {1: {'localprf': 100,
                                                        'metric': 2219,
                                                        'next_hop': '1.1.1.1',
                                                        'origin_codes': 'e',
                                                        'path': '200 '
                                                                '33299 '
                                                                '51178 '
                                                                '47751 '
                                                                '{27016}',
                                                        'path_type': 'i',
                                                        'status_codes': '*',
                                                        'weight': 0},
                                                    2: {'localprf': 100,
                                                        'metric': 2219,
                                                        'next_hop': '1.1.1.1',
                                                        'origin_codes': 'e',
                                                        'path': '200 '
                                                                '33299 '
                                                                '51178 '
                                                                '47751 '
                                                                '{27016}',
                                                        'path_type': 'i',
                                                        'status_codes': '*',
                                                        'weight': 0}}},
                          '15.1.5.0/24': {'index': {1: {'localprf': 100,
                                                        'metric': 2219,
                                                        'next_hop': '1.1.1.1',
                                                        'origin_codes': 'e',
                                                        'path': '200 '
                                                                '33299 '
                                                                '51178 '
                                                                '47751 '
                                                                '{27016}',
                                                        'path_type': 'i',
                                                        'status_codes': '*',
                                                        'weight': 0},
                                                    2: {'localprf': 100,
                                                        'metric': 2219,
                                                        'next_hop': '1.1.1.1',
                                                        'origin_codes': 'e',
                                                        'path': '200 '
                                                                '33299 '
                                                                '51178 '
                                                                '47751 '
                                                                '{27016}',
                                                        'path_type': 'i',
                                                        'status_codes': '*',
                                                        'weight': 0}}}}},
            'vpnv6 unicast': {'bgp_table_version': 66,
                              'local_router_id': '4.4.4.4',
                              'routes': {}},
            'vpnv6 unicast RD 200:1':
              {'bgp_table_version': 66,
               'local_router_id': '4.4.4.4',
               'route_distinguisher': '200:1',
               'routes': {'615:11:11:1::/64': {'index': {1: {'localprf': 100,
                                                             'metric': 2219,
                                                             'next_hop': '::FFFF:1.1.1.1',
                                                             'origin_codes': 'e',
                                                             'path': '200 '
                                                                     '33299 '
                                                                     '51178 '
                                                                     '47751 '
                                                                     '{27016}',
                                                             'path_type': 'i',
                                                             'status_codes': '*>',
                                                             'weight': 0}}},
                          '615:11:11:2::/64': {'index': {1: {'localprf': 100,
                                                             'metric': 2219,
                                                             'next_hop': '::FFFF:1.1.1.1',
                                                             'origin_codes': 'e',
                                                             'path': '200 '
                                                                     '33299 '
                                                                     '51178 '
                                                                     '47751 '
                                                                     '{27016}',
                                                             'path_type': 'i',
                                                             'status_codes': '*>',
                                                             'weight': 0}}},
                          '615:11:11:3::/64': {'index': {1: {'localprf': 100,
                                                             'metric': 2219,
                                                             'next_hop': '::FFFF:1.1.1.1',
                                                             'origin_codes': 'e',
                                                             'path': '200 '
                                                                     '33299 '
                                                                     '51178 '
                                                                     '47751 '
                                                                     '{27016}',
                                                             'path_type': 'i',
                                                             'status_codes': '*>',
                                                             'weight': 0}}},
                          '615:11:11:4::/64': {'index': {1: {'localprf': 100,
                                                             'metric': 2219,
                                                             'next_hop': '::FFFF:1.1.1.1',
                                                             'origin_codes': 'e',
                                                             'path': '200 '
                                                                     '33299 '
                                                                     '51178 '
                                                                     '47751 '
                                                                     '{27016}',
                                                             'path_type': 'i',
                                                             'status_codes': '*>',
                                                             'weight': 0}}},
                          '615:11:11::/64': {'index': {1: {'localprf': 100,
                                                           'metric': 2219,
                                                           'next_hop': '::FFFF:1.1.1.1',
                                                           'origin_codes': 'e',
                                                           'path': '200 '
                                                                   '33299 '
                                                                   '51178 '
                                                                   '47751 '
                                                                   '{27016}',
                                                           'path_type': 'i',
                                                           'status_codes': '*>',
                                                           'weight': 0}}}}},
            'vpnv6 unicast RD 200:2':
              {'bgp_table_version': 66,
               'local_router_id': '4.4.4.4',
               'route_distinguisher': '200:2',
               'routes': {'615:11:11:1::/64': {'index': {1: {'localprf': 100,
                                                             'metric': 2219,
                                                             'next_hop': '::FFFF:1.1.1.1',
                                                             'origin_codes': 'e',
                                                             'path': '200 '
                                                                     '33299 '
                                                                     '51178 '
                                                                     '47751 '
                                                                     '{27016}',
                                                             'path_type': 'i',
                                                             'status_codes': '*>',
                                                             'weight': 0}}},
                          '615:11:11:2::/64': {'index': {1: {'localprf': 100,
                                                             'metric': 2219,
                                                             'next_hop': '::FFFF:1.1.1.1',
                                                             'origin_codes': 'e',
                                                             'path': '200 '
                                                                     '33299 '
                                                                     '51178 '
                                                                     '47751 '
                                                                     '{27016}',
                                                             'path_type': 'i',
                                                             'status_codes': '*>',
                                                             'weight': 0}}},
                          '615:11:11:3::/64': {'index': {1: {'localprf': 100,
                                                             'metric': 2219,
                                                             'next_hop': '::FFFF:1.1.1.1',
                                                             'origin_codes': 'e',
                                                             'path': '200 '
                                                                     '33299 '
                                                                     '51178 '
                                                                     '47751 '
                                                                     '{27016}',
                                                             'path_type': 'i',
                                                             'status_codes': '*>',
                                                             'weight': 0}}},
                          '615:11:11:4::/64': {'index': {1: {'localprf': 100,
                                                             'metric': 2219,
                                                             'next_hop': '::FFFF:1.1.1.1',
                                                             'origin_codes': 'e',
                                                             'path': '200 '
                                                                     '33299 '
                                                                     '51178 '
                                                                     '47751 '
                                                                     '{27016}',
                                                             'path_type': 'i',
                                                             'status_codes': '*>',
                                                             'weight': 0}}},
                          '615:11:11::/64': {'index': {1: {'localprf': 100,
                                                           'metric': 2219,
                                                           'next_hop': '::FFFF:1.1.1.1',
                                                           'origin_codes': 'e',
                                                           'path': '200 '
                                                                   '33299 '
                                                                   '51178 '
                                                                   '47751 '
                                                                   '{27016}',
                                                           'path_type': 'i',
                                                           'status_codes': '*>',
                                                           'weight': 0}}}}},
            'vpnv6 unicast RD 300:1':
              {'bgp_table_version': 66,
               'default_vrf': 'VRF1',
               'local_router_id': '4.4.4.4',
               'route_distinguisher': '300:1',
               'routes': {'615:11:11:1::/64': {'index': {1: {'localprf': 100,
                                                             'metric': 2219,
                                                             'next_hop': '::FFFF:1.1.1.1',
                                                             'origin_codes': 'e',
                                                             'path': '200 '
                                                                     '33299 '
                                                                     '51178 '
                                                                     '47751 '
                                                                     '{27016}',
                                                             'path_type': 'i',
                                                             'status_codes': '*',
                                                             'weight': 0},
                                                         2: {'localprf': 100,
                                                             'metric': 2219,
                                                             'next_hop': '::FFFF:1.1.1.1',
                                                             'origin_codes': 'e',
                                                             'path': '200 '
                                                                     '33299 '
                                                                     '51178 '
                                                                     '47751 '
                                                                     '{27016}',
                                                             'path_type': 'i',
                                                             'status_codes': '*',
                                                             'weight': 0}}},
                          '615:11:11:2::/64': {'index': {1: {'localprf': 100,
                                                             'metric': 2219,
                                                             'next_hop': '::FFFF:1.1.1.1',
                                                             'origin_codes': 'e',
                                                             'path': '200 '
                                                                     '33299 '
                                                                     '51178 '
                                                                     '47751 '
                                                                     '{27016}',
                                                             'path_type': 'i',
                                                             'status_codes': '*',
                                                             'weight': 0},
                                                         2: {'localprf': 100,
                                                             'metric': 2219,
                                                             'next_hop': '::FFFF:1.1.1.1',
                                                             'origin_codes': 'e',
                                                             'path': '200 '
                                                                     '33299 '
                                                                     '51178 '
                                                                     '47751 '
                                                                     '{27016}',
                                                             'path_type': 'i',
                                                             'status_codes': '*',
                                                             'weight': 0}}},
                          '615:11:11:3::/64': {'index': {1: {'localprf': 100,
                                                             'metric': 2219,
                                                             'next_hop': '::FFFF:1.1.1.1',
                                                             'origin_codes': 'e',
                                                             'path': '200 '
                                                                     '33299 '
                                                                     '51178 '
                                                                     '47751 '
                                                                     '{27016}',
                                                             'path_type': 'i',
                                                             'status_codes': '*',
                                                             'weight': 0},
                                                         2: {'localprf': 100,
                                                             'metric': 2219,
                                                             'next_hop': '::FFFF:1.1.1.1',
                                                             'origin_codes': 'e',
                                                             'path': '200 '
                                                                     '33299 '
                                                                     '51178 '
                                                                     '47751 '
                                                                     '{27016}',
                                                             'path_type': 'i',
                                                             'status_codes': '*',
                                                             'weight': 0}}},
                          '615:11:11:4::/64': {'index': {1: {'localprf': 100,
                                                             'metric': 2219,
                                                             'next_hop': '::FFFF:1.1.1.1',
                                                             'origin_codes': 'e',
                                                             'path': '200 '
                                                                     '33299 '
                                                                     '51178 '
                                                                     '47751 '
                                                                     '{27016}',
                                                             'path_type': 'i',
                                                             'status_codes': '*',
                                                             'weight': 0},
                                                         2: {'localprf': 100,
                                                             'metric': 2219,
                                                             'next_hop': '::FFFF:1.1.1.1',
                                                             'origin_codes': 'e',
                                                             'path': '200 '
                                                                     '33299 '
                                                                     '51178 '
                                                                     '47751 '
                                                                     '{27016}',
                                                             'path_type': 'i',
                                                             'status_codes': '*',
                                                             'weight': 0}}},
                          '615:11:11::/64': {'index': {1: {'localprf': 100,
                                                           'metric': 2219,
                                                           'next_hop': '::FFFF:1.1.1.1',
                                                           'origin_codes': 'e',
                                                           'path': '200 '
                                                                   '33299 '
                                                                   '51178 '
                                                                   '47751 '
                                                                   '{27016}',
                                                           'path_type': 'i',
                                                           'status_codes': '*',
                                                           'weight': 0},
                                                       2: {'localprf': 100,
                                                           'metric': 2219,
                                                           'next_hop': '::FFFF:1.1.1.1',
                                                           'origin_codes': 'e',
                                                           'path': '200 '
                                                                   '33299 '
                                                                   '51178 '
                                                                   '47751 '
                                                                   '{27016}',
                                                           'path_type': 'i',
                                                           'status_codes': '*',
                                                           'weight': 0}}}}}}}}}}}

    golden_output = {'execute.return_value': '''
        For address family: VPNv4 Unicast
        BGP table version is 56, local router ID is 4.4.4.4
        Status codes: s suppressed, d damped, h history, * valid, > best, i - internal, 
                      r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter, 
                      x best-external, a additional-path, c RIB-compressed, 
        Origin codes: i - IGP, e - EGP, ? - incomplete
        RPKI validation codes: V valid, I invalid, N Not found

             Network          Next Hop            Metric LocPrf Weight Path
        Route Distinguisher: 200:1
         *>i 15.1.1.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
         *>i 15.1.2.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
         *>i 15.1.3.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
         *>i 15.1.4.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
         *>i 15.1.5.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
        Route Distinguisher: 200:2
         *>i 15.1.1.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
         *>i 15.1.2.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
         *>i 15.1.3.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
         *>i 15.1.4.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
         *>i 15.1.5.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
        Route Distinguisher: 300:1 (default for vrf VRF1) VRF Router ID 44.44.44.44
         * i 15.1.1.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
         *>i                  1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
         * i 15.1.2.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
         *>i                  1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
         * i 15.1.3.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
         *>i                  1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
         * i 15.1.4.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
         *>i                  1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
         * i 15.1.5.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
         *>i                  1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e

        Total number of prefixes 20 

        For address family: VPNv6 Unicast
        BGP table version is 66, local router ID is 4.4.4.4
        Status codes: s suppressed, d damped, h history, * valid, > best, i - internal, 
                      r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter, 
                      x best-external, a additional-path, c RIB-compressed, 
        Origin codes: i - IGP, e - EGP, ? - incomplete
        RPKI validation codes: V valid, I invalid, N Not found

             Network          Next Hop            Metric LocPrf Weight Path
        Route Distinguisher: 200:1
         *>i 615:11:11::/64   ::FFFF:1.1.1.1        2219    100      0 200 33299 51178 47751 {27016} e
         *>i 615:11:11:1::/64 ::FFFF:1.1.1.1        2219    100      0 200 33299 51178 47751 {27016} e
         *>i 615:11:11:2::/64 ::FFFF:1.1.1.1        2219    100      0 200 33299 51178 47751 {27016} e
         *>i 615:11:11:3::/64 ::FFFF:1.1.1.1        2219    100      0 200 33299 51178 47751 {27016} e
         *>i 615:11:11:4::/64 ::FFFF:1.1.1.1        2219    100      0 200 33299 51178 47751 {27016} e
        Route Distinguisher: 200:2
         *>i 615:11:11::/64   ::FFFF:1.1.1.1        2219    100      0 200 33299 51178 47751 {27016} e
         *>i 615:11:11:1::/64 ::FFFF:1.1.1.1        2219    100      0 200 33299 51178 47751 {27016} e
         *>i 615:11:11:2::/64 ::FFFF:1.1.1.1        2219    100      0 200 33299 51178 47751 {27016} e
         *>i 615:11:11:3::/64 ::FFFF:1.1.1.1        2219    100      0 200 33299 51178 47751 {27016} e
         *>i 615:11:11:4::/64 ::FFFF:1.1.1.1        2219    100      0 200 33299 51178 47751 {27016} e
        Route Distinguisher: 300:1 (default for vrf VRF1) VRF Router ID 44.44.44.44
         * i 615:11:11::/64   ::FFFF:1.1.1.1        2219    100      0 200 33299 51178 47751 {27016} e
         *>i                  ::FFFF:1.1.1.1        2219    100      0 200 33299 51178 47751 {27016} e
         * i 615:11:11:1::/64 ::FFFF:1.1.1.1        2219    100      0 200 33299 51178 47751 {27016} e
         *>i                  ::FFFF:1.1.1.1        2219    100      0 200 33299 51178 47751 {27016} e
         * i 615:11:11:2::/64 ::FFFF:1.1.1.1        2219    100      0 200 33299 51178 47751 {27016} e
         *>i                  ::FFFF:1.1.1.1        2219    100      0 200 33299 51178 47751 {27016} e
         * i 615:11:11:3::/64 ::FFFF:1.1.1.1        2219    100      0 200 33299 51178 47751 {27016} e
         *>i                  ::FFFF:1.1.1.1        2219    100      0 200 33299 51178 47751 {27016} e
         * i 615:11:11:4::/64 ::FFFF:1.1.1.1        2219    100      0 200 33299 51178 47751 {27016} e
         *>i                  ::FFFF:1.1.1.1        2219    100      0 200 33299 51178 47751 {27016} e

        Total number of prefixes 20
        '''}

    golden_parsed_output2 = {
        'vrf': 
            {'default': 
                {'neighbor': 
                    {'19.0.101.1': 
                        {'address_family': 
                            {'ipv4 multicast': 
                                {'bgp_table_version': 175,
                                'local_router_id': '20.0.0.6',
                                'routes': 
                                    {'1.2.1.0/24': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '2 '
                                                        '3 '
                                                        '4',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    '1.2.2.0/24': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '2 '
                                                        '3 '
                                                        '4',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}}}},
                            'ipv4 unicast': 
                                {'bgp_table_version': 174,
                                'local_router_id': '20.0.0.6',
                                'routes': 
                                    {'1.1.1.0/24': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 2222,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '1 '
                                                        '2 '
                                                        '3 '
                                                        '65000 '
                                                        '23',
                                                'path_type': 'i',
                                                'status_codes': '*',
                                                'weight': 0}}},
                                    '1.1.2.0/24': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 2222,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '1 '
                                                        '2 '
                                                        '3 '
                                                        '65000 '
                                                        '23',
                                                'path_type': 'i',
                                                'status_codes': '*',
                                                'weight': 0}}},
                                    '1.6.0.0/16': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '10 '
                                                        '20 '
                                                        '30 '
                                                        '40 '
                                                        '50 '
                                                        '60 '
                                                        '70 '
                                                        '80 '
                                                        '90',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}}}},
                            'ipv6 multicast': 
                                {'bgp_table_version': 6,
                                'local_router_id': '20.0.0.6',
                                'routes': {}},
                            'ipv6 unicast': 
                                {'bgp_table_version': 173,
                                'local_router_id': '20.0.0.6',
                                'routes': {}},
                            'link-state': 
                                {'bgp_table_version': 173,
                                'local_router_id': '20.0.0.6',
                                'routes': 
                                    {'[2]:[77][7,0][9.9.9.9,1,151587081][29.1.1.1,22][19.0.101.1,29.0.1.30]/616': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 4444,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '3 '
                                                      '10 '
                                                      '20 '
                                                      '30 '
                                                      '40 '
                                                      '50 '
                                                      '60 '
                                                      '70 '
                                                      '80 '
                                                      '90',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    '[2]:[77][7,0][9.9.9.9,2,151587081][29.1.1.1,22][19.0.101.1,29.0.1.31]/616': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 4444,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '3 '
                                                      '10 '
                                                      '20 '
                                                      '30 '
                                                      '40 '
                                                      '50 '
                                                      '60 '
                                                      '70 '
                                                      '80 '
                                                      '90',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}}}},
                            'vpnv4 unicast': 
                                {'bgp_table_version': 183,
                                'local_router_id': '20.0.0.6',
                                'routes': {}},
                            'vpnv4 unicast RD 0:0': 
                                {'bgp_table_version': 183,
                                'local_router_id': '20.0.0.6',
                                'route_distinguisher': '0:0',
                                'routes': {}},
                            'vpnv4 unicast RD 101:100': 
                                {'bgp_table_version': 183,
                                'local_router_id': '20.0.0.6',
                                'route_distinguisher': '101:100',
                                'routes': 
                                    {'1.3.1.0/24': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 4444,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '3 '
                                                        '10 '
                                                        '20 '
                                                        '4 '
                                                        '5 '
                                                        '6 '
                                                        '3 '
                                                        '10 '
                                                        '20 '
                                                        '4 '
                                                        '5 '
                                                        '6',
                                                'path_type': 'i',
                                                'status_codes': '*',
                                                'weight': 0}}},
                                    '1.3.2.0/24': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 4444,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '3 '
                                                     '10 '
                                                     '20 '
                                                     '4 '
                                                     '5 '
                                                     '6 '
                                                     '3 '
                                                     '10 '
                                                     '20 '
                                                     '4 '
                                                     '5 '
                                                     '6',
                                                'path_type': 'i',
                                                'status_codes': '*',
                                                'weight': 0}}}}},
                            'vpnv4 unicast RD 102:100': 
                                {'bgp_table_version': 183,
                                'local_router_id': '20.0.0.6',
                                'route_distinguisher': '102:100',
                                'routes': {}},
                            'vpnv6 unicast': 
                                {'bgp_table_version': 13,
                                'local_router_id': '20.0.0.6',
                                'routes': {}},
                            'vpnv6 unicast RD 0xbb00010000000000': 
                                {'bgp_table_version': 13,
                                'local_router_id': '20.0.0.6',
                                'route_distinguisher': '0xbb00010000000000',
                                'routes': {}},
                            'vpnv6 unicast RD 100:200': 
                                {'bgp_table_version': 13,
                                'local_router_id': '20.0.0.6',
                                'route_distinguisher': '100:200',
                                'routes': 
                                    {'aaaa:1::/113': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'next_hop': '4444',
                                                'origin_codes': 'i',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    'aaaa:1::8000/113': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'next_hop': '4444',
                                                'origin_codes': 'i',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}}}}}}}}}}

    golden_output2 = {'execute.return_value': '''

        For address family: IPv4 Unicast
        BGP table version is 174, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        * i1.1.1.0/24         19.0.101.1            2222        100          0 1 2 3 65000 23 i
        * i1.1.2.0/24         19.0.101.1            2222        100          0 1 2 3 65000 23 i
        *>i1.6.0.0/16         19.0.101.1                        100          0 10 20 30 40 50 60 70 80 90 i


        For address family: IPv4 Multicast
        BGP table version is 175, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>i1.2.1.0/24         19.0.101.1                        100          0 2 3 4 i
        *>i1.2.2.0/24         19.0.101.1                        100          0 2 3 4 i


        For address family: IPv6 Unicast
        BGP table version is 173, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path


        For address family: IPv6 Multicast
        BGP table version is 6, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path


        For address family: VPNv4 Unicast
        BGP table version is 183, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        Route Distinguisher: 0:0

        Route Distinguisher: 101:100
        * i1.3.1.0/24         19.0.101.1            4444        100          0 3 10 20 4 5 6 3 10 20 4 5 6 i
        * i1.3.2.0/24         19.0.101.1            4444        100          0 3 10 20 4 5 6 3 10 20 4 5 6 i

        Route Distinguisher: 102:100


        For address family: VPNv6 Unicast
        BGP table version is 13, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        Route Distinguisher: 100:200
        *>iaaaa:1::/113       ::ffff:19.0.101.1
                                                    4444        100          0 i
        *>iaaaa:1::8000/113   ::ffff:19.0.101.1
                                                    4444        100          0 i

        Route Distinguisher: 0xbb00010000000000


        For address family: Link-State
        BGP table version is 173, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>i[2]:[77][7,0][9.9.9.9,1,151587081][29.1.1.1,22][19.0.101.1,29.0.1.30]/616
                              19.0.101.1            4444        100          0 3 10 20 30 40 50 60 70 80 90 i
        *>i[2]:[77][7,0][9.9.9.9,2,151587081][29.1.1.1,22][19.0.101.1,29.0.1.31]/616
                              19.0.101.1            4444        100          0 3 10 20 30 40 50 60 70 80 90 i
        '''}

    golden_parsed_output3 = {
        'vrf': 
            {'default': 
                {'neighbor': 
                    {'10.4.6.6': 
                        {'address_family': 
                            {'ipv4 unicast': 
                                {'bgp_table_version': 773961,
                                'local_router_id': '44.44.44.44',
                                'routes': 
                                    {'46.1.1.0/24': 
                                        {'index': 
                                            {1: 
                                                {'metric': 2219,
                                                'next_hop': '10.4.6.6',
                                                'origin_codes': 'e',
                                                'path': '300 '
                                                        '33299 '
                                                        '51178 '
                                                        '47751 '
                                                        '{27016}',
                                                'path_type': 'e',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    '46.1.2.0/24': 
                                        {'index': 
                                            {1: 
                                                {'metric': 2219,
                                                'next_hop': '10.4.6.6',
                                                'origin_codes': 'e',
                                                'path': '300 '
                                                        '33299 '
                                                        '51178 '
                                                        '47751 '
                                                        '{27016}',
                                                'path_type': 'e',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    '46.1.3.0/24': 
                                        {'index': 
                                            {1: 
                                                {'metric': 2219,
                                                'next_hop': '10.4.6.6',
                                                'origin_codes': 'e',
                                                'path': '300 '
                                                        '33299 '
                                                        '51178 '
                                                        '47751 '
                                                        '{27016}',
                                                'path_type': 'e',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    '46.1.4.0/24': 
                                        {'index': 
                                            {1: 
                                                {'metric': 2219,
                                                'next_hop': '10.4.6.6',
                                                'origin_codes': 'e',
                                                'path': '300 '
                                                        '33299 '
                                                        '51178 '
                                                        '47751 '
                                                        '{27016}',
                                                'path_type': 'e',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    '46.1.5.0/24': 
                                        {'index': 
                                            {1: 
                                                {'metric': 2219,
                                                'next_hop': '10.4.6.6',
                                                'origin_codes': 'e',
                                                'path': '300 '
                                                        '33299 '
                                                        '51178 '
                                                        '47751 '
                                                        '{27016}',
                                                'path_type': 'e',
                                                'status_codes': '*>',
                                                'weight': 0}}}}},
                            'ipv6 unicast': 
                                {'bgp_table_version': 256033,
                                'local_router_id': '44.44.44.44',
                                'routes': {}}}}}}}}

    golden_output3 = {'execute.return_value': '''
        R4# show bgp all neighbors 10.4.6.6 routes 

        For address family: IPv4 Unicast
        BGP table version is 773961, local router ID is 44.44.44.44
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>e46.1.1.0/24        10.4.6.6              2219                     0 300 33299 51178 47751 {27016} e
        *>e46.1.2.0/24        10.4.6.6              2219                     0 300 33299 51178 47751 {27016} e
        *>e46.1.3.0/24        10.4.6.6              2219                     0 300 33299 51178 47751 {27016} e
        *>e46.1.4.0/24        10.4.6.6              2219                     0 300 33299 51178 47751 {27016} e
        *>e46.1.5.0/24        10.4.6.6              2219                     0 300 33299 51178 47751 {27016} e

        For address family: IPv4 Multicast

        For address family: IPv6 Unicast
        BGP table version is 256033, local router ID is 44.44.44.44
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path

        For address family: IPv6 Multicast

        For address family: VPNv4 Unicast

        For address family: VPNv6 Unicast

        For address family: IPv4 MDT

        For address family: IPv6 Label Unicast

        For address family: L2VPN VPLS

        For address family: IPv4 MVPN

        For address family: IPv6 MVPN

        For address family: IPv4 Label Unicast
        '''}

    def test_show_bgp_vrf_all_neighbors_routes_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowBgpAllNeighborsRoutes(device=self.device)
        parsed_output = obj.parse(neighbor='21.0.0.2')
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_bgp_vrf_all_neighbors_routes_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowBgpAllNeighborsRoutes(device=self.device)
        parsed_output = obj.parse(neighbor='19.0.101.1')
        self.assertEqual(parsed_output,self.golden_parsed_output2)

    def test_show_bgp_vrf_all_neighbors_routes_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowBgpAllNeighborsRoutes(device=self.device)
        parsed_output = obj.parse(neighbor='10.4.6.6')
        self.assertEqual(parsed_output,self.golden_parsed_output3)

    def test_show_bgp_vrf_all_neighbors_routes_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpAllNeighborsRoutes(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(neighbor='21.0.0.2')


class test_show_ip_bgp_template_peer_policy(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'peer_policy':
            {'PEER-POLICY':
                {
                    'local_policies' : '0x8002069C603',
                    'inherited_polices' : '0x0',
                    'local_disable_policies': '0x0',
                    'inherited_disable_polices': '0x0',
                    'allowas_in':True ,
                    'allowas_in_as_number': 9,
                    'as_override': True,
                    'default_originate': True,
                    'default_originate_route_map': 'test',
                    'route_map_name_in': 'test',
                    'route_map_name_out': 'test2',
                    'maximum_prefix_max_prefix_no': 5555,
                    'maximum_prefix_threshold': 70,
                    'maximum_prefix_restart': 300,
                    'next_hop_self': True,
                    'route_reflector_client': True,
                    'send_community': 'both',
                    'soft_reconfiguration': True,
                    'soo': 'SoO:100:100',
                    'index': 1,
                },
            'PEER-POLICY2':
                {
                    'local_policies': '0x200000',
                    'inherited_polices': '0x0',
                    'local_disable_policies': '0x0',
                    'inherited_disable_polices': '0x0',
                    'allowas_in': True,
                    'allowas_in_as_number': 10,
                    'index': 2,
                }

            },
    }

    golden_output = {'execute.return_value':'''
            R4_iosv#show ip bgp template peer-policy
            Template:PEER-POLICY, index:1.
            Local policies:0x8002069C603, Inherited polices:0x0
            Local disable policies:0x0, Inherited disable policies:0x0
            Locally configured policies:
              route-map test in
              route-map test2 out
              default-originate route-map test
              soft-reconfiguration inbound
              maximum-prefix 5555 70 restart 300
              as-override
              allowas-in 9
              route-reflector-client
              next-hop-self
              send-community both
              soo SoO:100:100
            Inherited policies:

            Template:PEER-POLICY2, index:2.
            Local policies:0x200000, Inherited polices:0x0
            Local disable policies:0x0, Inherited disable policies:0x0
            Locally configured policies:
              allowas-in 10
            Inherited policies:
    '''}

    golden_parsed_output_1 = {
        'peer_policy':
            {'PEER-POLICY':
                {
                    'local_policies': '0x8002069C603',
                    'inherited_polices': '0x0',
                    'local_disable_policies': '0x0',
                    'inherited_disable_polices': '0x0',
                    'default_originate': True,
                    'allowas_in': True,
                    'allowas_in_as_number': 9,
                    'default_originate_route_map': 'test',
                    'route_map_name_in': 'test',
                    'route_map_name_out': 'test2',
                    'maximum_prefix_max_prefix_no': 5555,
                    'maximum_prefix_restart': 300,
                    'next_hop_self': True,
                    'route_reflector_client': True,
                    'send_community': 'both',
                    'soft_reconfiguration': True,
                    'index': 1,
                    'inherited_policies':
                        {
                            'as_override': True,
                            'soo': 'SoO:100:100',
                        },
                },
                'PEER-POLICY2':
                    {
                        'local_policies': '0x200000',
                        'inherited_polices': '0x0',
                        'local_disable_policies': '0x0',
                        'inherited_disable_polices': '0x0',
                        'allowas_in': True,
                        'allowas_in_as_number': 10,
                        'index': 2,
                    }

            },
    }

    golden_output_1 = {'execute.return_value': '''
               R4_iosv#show ip bgp template peer-policy
               Template:PEER-POLICY, index:1.
               Local policies:0x8002069C603, Inherited polices:0x0
               Local disable policies:0x0, Inherited disable policies:0x0
               Locally configured policies:
                 allowas-in 9
                 route-map test in
                 route-map test2 out
                 default-originate route-map test
                 soft-reconfiguration inbound
                 maximum-prefix 5555 restart 300
                 route-reflector-client
                 next-hop-self
                 send-community both
               Inherited policies:
                 as-override
                 soo SoO:100:100


               Template:PEER-POLICY2, index:2.
               Local policies:0x200000, Inherited polices:0x0
               Local disable policies:0x0, Inherited disable policies:0x0
               Locally configured policies:
                 allowas-in 10
               Inherited policies:
       '''}

    golden_parsed_output_2 = {
        'peer_policy':
            {'PEER-POLICY2':
                    {
                        'local_policies': '0x200000',
                        'inherited_polices': '0x0',
                        'local_disable_policies': '0x0',
                        'inherited_disable_polices': '0x0',
                        'allowas_in': True,
                        'allowas_in_as_number': 10,
                        'index': 2,
                    }

            },
    }

    golden_output_2 = {'execute.return_value': '''
                   R4_iosv#show ip bgp template peer-policy PEER-POLICY2

                   Template:PEER-POLICY2, index:2.
                   Local policies:0x200000, Inherited polices:0x0
                   Local disable policies:0x0, Inherited disable policies:0x0
                   Locally configured policies:
                     allowas-in 10
                   Inherited policies:
           '''}
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpBgpTemplatePeerPolicy(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpBgpTemplatePeerPolicy(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpBgpTemplatePeerPolicy(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpBgpTemplatePeerPolicy(device=self.device)
        parsed_output = obj.parse(template_name='PEER-POLICY2')
        self.assertEqual(parsed_output, self.golden_parsed_output_2)


class test_show_ip_bgp_all_dampening_parameters(unittest.TestCase):
    '''
        unit test for show ip bgp all dampening parameters
    '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        'vrf':
            {'default':
                {
                    'address_family':
                        {
                            'ipv4 unicast':
                                {
                                   'dampening': True,
                                   'dampening_decay_time': 4200,
                                   'dampening_half_life_time': 2100,
                                   'dampening_reuse_time': 200,
                                   'dampening_max_suppress_time': 4200,
                                   'dampening_suppress_time': 200,
                                   'dampening_max_suppress_penalty': 800,
                                },
                            'ipv6 unicast':
                                {
                                    'dampening': True,
                                    'dampening_decay_time': 4235,
                                    'dampening_half_life_time': 2160,
                                    'dampening_reuse_time': 201,
                                    'dampening_max_suppress_time': 4260,
                                    'dampening_suppress_time': 201,
                                    'dampening_max_suppress_penalty': 788,
                                },
                        },
                },
            },
    }
    golden_output = {'execute.return_value': '''
    R4_iosv#show ip bgp all dampening parameters
    For address family: IPv4 Unicast

     dampening 35 200 200 70
      Half-life time      : 35 mins       Decay Time       : 4200 secs
      Max suppress penalty:   800         Max suppress time: 70 mins
      Suppress penalty    :   200         Reuse penalty    : 200


    For address family: IPv6 Unicast

     dampening 36 201 201 71
      Half-life time      : 36 mins       Decay Time       : 4235 secs
      Max suppress penalty:   788         Max suppress time: 71 mins
      Suppress penalty    :   201         Reuse penalty    : 201


    For address family: VPNv4 Unicast

    % dampening not enabled for base

    For vrf: VRF1

    % dampening not enabled for vrf VRF1

    For vrf: VRF2

    % dampening not enabled for vrf VRF2

    For address family: VPNv6 Unicast

    % dampening not enabled for base

    For vrf: VRF1

    % dampening not enabled for vrf VRF1

    For vrf: VRF2

    % dampening not enabled for vrf VRF2

    For address family: IPv4 Multicast

    % dampening not enabled for base

    For address family: L2VPN E-VPN

    % dampening not enabled for base

    For address family: VPNv4 Multicast

    % dampening not enabled for base

    For vrf: VRF1

    % dampening not enabled for vrf VRF1

    For vrf: VRF2

    % dampening not enabled for vrf VRF2

    For address family: MVPNv4 Unicast

    % dampening not enabled for base

    For vrf: VRF1

    % dampening not enabled for vrf VRF1

    For vrf: VRF2

    % dampening not enabled for vrf VRF2

    For address family: MVPNv6 Unicast

    % dampening not enabled for base

    For vrf: VRF1

    % dampening not enabled for vrf VRF1

    For vrf: VRF2

    % dampening not enabled for vrf VRF2

    For address family: VPNv6 Multicast

    % dampening not enabled for base

    For vrf: VRF1

    % dampening not enabled for vrf VRF1

    For vrf: VRF2

    % dampening not enabled for vrf VRF2
                    '''}

    golden_parsed_output_2 = {
        'vrf':
            {'default':
                {
                    'address_family':
                        {
                            'ipv4 unicast':
                                {
                                    'dampening': True,
                                    'dampening_decay_time': 2320,
                                    'dampening_half_life_time': 900,
                                    'dampening_reuse_time': 750,
                                    'dampening_max_suppress_time': 3600,
                                    'dampening_suppress_time': 2000,
                                    'dampening_max_suppress_penalty': 12000,
                                },
                            'vpnv4 unicast':
                                {
                                    'dampening': True,
                                    'dampening_decay_time': 2320,
                                    'dampening_half_life_time': 900,
                                    'dampening_reuse_time': 750,
                                    'dampening_max_suppress_time': 3600,
                                    'dampening_suppress_time': 2000,
                                    'dampening_max_suppress_penalty': 12000,
                                },
                        },
                },
                'VRF1':
                    {
                        'address_family':
                            {
                                'vpnv4 unicast':
                                    {
                                        'dampening': True,
                                        'dampening_decay_time': 2320,
                                        'dampening_half_life_time': 900,
                                        'dampening_reuse_time': 750,
                                        'dampening_max_suppress_time': 3600,
                                        'dampening_suppress_time': 2000,
                                        'dampening_max_suppress_penalty': 12000,
                                    },
                            },
                    },
            },
    }

    golden_output_2 = {'execute.return_value': '''
          R4_iosv#sh ip bgp all dampening parameters
            For address family: IPv4 Unicast

             dampening 15 750 2000 60 (DEFAULT)
              Half-life time      : 15 mins       Decay Time       : 2320 secs
              Max suppress penalty: 12000         Max suppress time: 60 mins
              Suppress penalty    :  2000         Reuse penalty    : 750


            For address family: IPv6 Unicast

            % dampening not enabled for base

            For address family: VPNv4 Unicast

             dampening 15 750 2000 60 (DEFAULT)
              Half-life time      : 15 mins       Decay Time       : 2320 secs
              Max suppress penalty: 12000         Max suppress time: 60 mins
              Suppress penalty    :  2000         Reuse penalty    : 750


            For vrf: VRF1

             dampening 15 750 2000 60 (DEFAULT)
              Half-life time      : 15 mins       Decay Time       : 2320 secs
              Max suppress penalty: 12000         Max suppress time: 60 mins
              Suppress penalty    :  2000         Reuse penalty    : 750


            For vrf: VRF2

            % dampening not enabled for vrf VRF2
                          '''}

    golden_parsed_output_3 = {
        'vrf':
            {'default':
                {
                    'address_family':
                        {
                            'ipv4 unicast':
                                {
                                    'dampening': True,
                                    'dampening_decay_time': 4200,
                                    'dampening_half_life_time': 2100,
                                    'dampening_reuse_time': 200,
                                    'dampening_max_suppress_time': 4200,
                                    'dampening_suppress_time': 200,
                                    'dampening_max_suppress_penalty': 800,
                                },
                        },
                },
                'VRF1':
                    {
                        'address_family':
                            {
                                'vpnv4 unicast':
                                    {
                                        'dampening': True,
                                        'dampening_decay_time': 4240,
                                        'dampening_half_life_time': 2160,
                                        'dampening_reuse_time': 2001,
                                        'dampening_max_suppress_time': 4260,
                                        'dampening_suppress_time': 2001,
                                        'dampening_max_suppress_penalty': 7850,
                                    },
                            },
                    },
            },
    }
    golden_output_3 = {'execute.return_value':'''
        R4_iosv#show ip bgp all dampening parameters
        For address family: IPv4 Unicast

         dampening 35 200 200 70
          Half-life time      : 35 mins       Decay Time       : 4200 secs
          Max suppress penalty:   800         Max suppress time: 70 mins
          Suppress penalty    :   200         Reuse penalty    : 200


        For address family: IPv6 Unicast

        % dampening not enabled for base

        For address family: VPNv4 Unicast

        % dampening not enabled for base

        For vrf: VRF1

         dampening 36 2001 2001 71
          Half-life time      : 36 mins       Decay Time       : 4240 secs
          Max suppress penalty:  7850         Max suppress time: 71 mins
          Suppress penalty    :  2001         Reuse penalty    : 2001


        For vrf: VRF2

        % dampening not enabled for vrf VRF2
    '''}

    golden_parsed_output_4 = {
        'vrf':
            {'default':
                {
                    'address_family':
                        {
                            'ipv4 unicast':
                                {
                                    'dampening': True,
                                    'dampening_decay_time': 4200,
                                    'dampening_half_life_time': 2100,
                                    'dampening_reuse_time': 200,
                                    'dampening_max_suppress_time': 4200,
                                    'dampening_suppress_time': 200,
                                    'dampening_max_suppress_penalty': 800,
                                },
                        },
                },
                'VRF1':
                    {
                        'address_family':
                            {
                                'vpnv4 unicast':
                                    {
                                        'dampening': True,
                                        'dampening_decay_time': 4240,
                                        'dampening_half_life_time': 2160,
                                        'dampening_reuse_time': 2001,
                                        'dampening_max_suppress_time': 4260,
                                        'dampening_suppress_time': 2001,
                                        'dampening_max_suppress_penalty': 7850,
                                    },
                            },
                    },
            },
    }
    golden_output_4 = {'execute.return_value': '''
    R4_iosv#show ip bgp all dampening parameters
        For address family: IPv4 Unicast

         dampening 35 200 200 70
          Half-life time      : 35 mins       Decay Time       : 4200 secs
          Max suppress penalty:   800         Max suppress time: 70 mins
          Suppress penalty    :   200         Reuse penalty    : 200


        For address family: IPv6 Unicast

        % dampening not enabled for base

        For address family: VPNv4 Unicast

        % dampening not enabled for base

        For vrf: VRF1

         dampening 36 2001 2001 71
          Half-life time      : 36 mins       Decay Time       : 4240 secs
          Max suppress penalty:  7850         Max suppress time: 71 mins
          Suppress penalty    :  2001         Reuse penalty    : 2001


        For vrf: VRF2

        % dampening not enabled for vrf VRF2

        For address family: VPNv6 Unicast

        % dampening not enabled for base

        For vrf: VRF1

        % dampening not enabled for vrf VRF1

        For vrf: VRF2

        % dampening not enabled for vrf VRF2

        For address family: IPv4 Multicast

        % dampening not enabled for base

        For address family: L2VPN E-VPN

        % dampening not enabled for base

        For address family: VPNv4 Multicast

        % dampening not enabled for base

        For vrf: VRF1

        % dampening not enabled for vrf VRF1

        For vrf: VRF2

        % dampening not enabled for vrf VRF2

        For address family: MVPNv4 Unicast

        % dampening not enabled for base

        For vrf: VRF1

        % dampening not enabled for vrf VRF1

        For vrf: VRF2

        % dampening not enabled for vrf VRF2

        For address family: MVPNv6 Unicast

        % dampening not enabled for base

        For vrf: VRF1

        % dampening not enabled for vrf VRF1

        For vrf: VRF2

        % dampening not enabled for vrf VRF2

        For address family: VPNv6 Multicast

        % dampening not enabled for base

        For vrf: VRF1

        % dampening not enabled for vrf VRF1

        For vrf: VRF2

        % dampening not enabled for vrf VRF2
       '''}

    golden_parsed_output_5 = {}

    golden_output_5 = {'execute.return_value': '''
        R4_iosv#show ip bgp all dampening parameters
        For address family: IPv4 Unicast

        % dampening not enabled for base

        For address family: IPv6 Unicast

        % dampening not enabled for base

        For address family: VPNv4 Unicast

        % dampening not enabled for base

        For vrf: VRF1

        % dampening not enabled for vrf VRF1

        For vrf: VRF2

        % dampening not enabled for vrf VRF2

        For address family: VPNv6 Unicast

        % dampening not enabled for base

        For vrf: VRF1

        % dampening not enabled for vrf VRF1

        For vrf: VRF2

        % dampening not enabled for vrf VRF2

        For address family: IPv4 Multicast

        % dampening not enabled for base

        For address family: L2VPN E-VPN

        % dampening not enabled for base

        For address family: VPNv4 Multicast

        % dampening not enabled for base

        For vrf: VRF1

        % dampening not enabled for vrf VRF1

        For vrf: VRF2

        % dampening not enabled for vrf VRF2

        For address family: MVPNv4 Unicast

        % dampening not enabled for base

        For vrf: VRF1

        % dampening not enabled for vrf VRF1

        For vrf: VRF2

        % dampening not enabled for vrf VRF2

        For address family: MVPNv6 Unicast

        % dampening not enabled for base

        For vrf: VRF1

        % dampening not enabled for vrf VRF1

        For vrf: VRF2

        % dampening not enabled for vrf VRF2

        For address family: VPNv6 Multicast

        % dampening not enabled for base

        For vrf: VRF1

        % dampening not enabled for vrf VRF1

        For vrf: VRF2

        % dampening not enabled for vrf VRF2
        '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpBgpAllDampeningParameters(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpBgpAllDampeningParameters(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpBgpAllDampeningParameters(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_3)
        obj = ShowIpBgpAllDampeningParameters(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_3)

    def test_golden_4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_4)
        obj = ShowIpBgpAllDampeningParameters(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_4)


    def test_golden_5(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_5)
        obj = ShowIpBgpAllDampeningParameters(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()



class test_show_bgp_all(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_1 = {
        'vrf':
            {'evpn1':
                 {'address_family':
                      {'vpnv4 unicast RD 65535:1':
                           {'bgp_table_version': 5,
                            'default_vrf': 'evpn1',
                            'route_distinguisher': '65535:1',
                            'route_identifier': '33.33.33.33',
                            'af_private_import_to_address_family': 'L2VPN E-VPN',
                            'pfx_count': 2,
                            'pfx_limit': 1000,
                            'routes':
                                {'3.3.3.0/24':
                                     {'index':
                                          {1:
                                               {'metric': 0,
                                                'next_hop': '3.3.3.254',
                                                'origin_codes': '?',
                                                'path': '65530',
                                                'status_codes': '*',
                                                'weight': 0,
                                                },
                                           2:
                                               {
                                                'next_hop': '0.0.0.0',
                                                'origin_codes': '?',
                                                'weight': 32768,
                                                'status_codes': '*>',
                                                'metric':0,
                                                },
                                           },
                                      },
                                 '100.1.1.0/24':
                                     {'index':
                                          {1:
                                               {'metric': 0,
                                                'next_hop': '0.0.0.0',
                                                'origin_codes': '?',
                                                'weight': 32768,
                                                'status_codes': '*>',
                                                },
                                           },
                                      },
                                 },
                            },
                      'l2vpn e-vpn RD 65535:1':
                           {'bgp_table_version': 4,
                            'default_vrf': 'evpn1',
                            'route_distinguisher': '65535:1',
                            'route_identifier': '33.33.33.33',
                            'routes':
                                {'[5][65535:1][0][24][3.3.3.0]/17':
                                     {'index':
                                          {1:
                                               {'metric': 0,
                                                'next_hop': '0.0.0.0',
                                                'origin_codes': '?',
                                                'weight': 32768,
                                                'status_codes': '*>',
                                                },
                                           2:
                                               {'metric': 0,
                                                'next_hop': '3.3.3.254',
                                                'origin_codes': '?',
                                                'path': '65530',
                                                'status_codes': '*',
                                                'weight': 0,
                                                },
                                           },
                                      },
                                 '[5][65535:1][0][24][100.1.1.0]/17':
                                     {'index':
                                          {1:
                                               {'metric': 0,
                                                'next_hop': '0.0.0.0',
                                                'origin_codes': '?',
                                                'weight': 32768,
                                                'status_codes': '*>',
                                                },
                                           },
                                      },
                                 },
                            },
                       },
                  },
             },
    }

    golden_output_1 = {'execute.return_value': '''
            R1_CE#show bgp all
            For address family: IPv4 Unicast


            For address family: IPv6 Unicast


            For address family: VPNv4 Unicast

            BGP table version is 5, local router ID is 33.33.33.33
            Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,
                          r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter,
                          x best-external, a additional-path, c RIB-compressed,
                          t secondary path,
            Origin codes: i - IGP, e - EGP, ? - incomplete
            RPKI validation codes: V valid, I invalid, N Not found

                 Network          Next Hop            Metric LocPrf Weight Path
            Route Distinguisher: 65535:1 (default for vrf evpn1)
            AF-Private Import to Address-Family: L2VPN E-VPN, Pfx Count/Limit: 2/1000
             *    3.3.3.0/24       3.3.3.254                0             0 65530 ?
             *>                    0.0.0.0                  0         32768 ?
             *>   100.1.1.0/24     0.0.0.0                  0         32768 ?

            For address family: IPv4 Multicast

            For address family: L2VPN E-VPN

            BGP table version is 4, local router ID is 33.33.33.33
            Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,
                          r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter,
                          x best-external, a additional-path, c RIB-compressed,
                          t secondary path,
            Origin codes: i - IGP, e - EGP, ? - incomplete
            RPKI validation codes: V valid, I invalid, N Not found

                 Network          Next Hop            Metric LocPrf Weight Path
            Route Distinguisher: 65535:1 (default for vrf evpn1)
             *>   [5][65535:1][0][24][3.3.3.0]/17
                                  0.0.0.0                  0         32768 ?
             *                     3.3.3.254                0             0 65530 ?
             *>   [5][65535:1][0][24][100.1.1.0]/17
                                  0.0.0.0                  0         32768 ?


            For address family: VPNv4 Multicast


            For address family: MVPNv4 Unicast


            For address family: MVPNv6 Unicast


            For address family: VPNv4 Flowspec

        '''
                     }

    golden_parsed_output_2 = {
        'vrf':
            {'default':
                 {'address_family':
                      {'vpnv4 unicast RD 200:1':
                           {'bgp_table_version': 56,
                            'default_vrf': 'default',
                            'route_distinguisher': '200:1',
                            'route_identifier': '4.4.4.4',
                            'routes':
                                {'15.1.1.0/24':
                                     {'index':
                                          {1:
                                               {'metric': 2219,
                                                'next_hop': '1.1.1.1',
                                                'localpref': 100,
                                                'origin_codes': 'e',
                                                'path': '200 33299 51178 47751 {27016}',
                                                'status_codes': '* i',
                                                'weight': 0,
                                                },
                                          2:
                                               {'metric': 2219,
                                                'next_hop': '1.1.1.1',
                                                'localpref': 100,
                                                'origin_codes': 'e',
                                                'path': '200 33299 51178 47751 {27016}',
                                                'status_codes': '*>i',
                                                'weight': 0,
                                                },

                                          },
                                     },
                                '15.1.2.0/24':
                                     {'index':
                                          {1:
                                               {'metric': 2219,
                                                'next_hop': '1.1.1.1',
                                                'localpref': 100,
                                                'origin_codes': 'e',
                                                'path': '200 33299 51178 47751 {27016}',
                                                'status_codes': '* i',
                                                'weight': 0,
                                                },
                                          2:
                                               {'metric': 2219,
                                                'next_hop': '1.1.1.1',
                                                'localpref': 100,
                                                'origin_codes': 'e',
                                                'path': '200 33299 51178 47751 {27016}',
                                                'status_codes': '*>i',
                                                'weight': 0,
                                                },

                                          },
                                      },
                                },
                            },
                       'vpnv4 unicast RD 200:2':
                           {'bgp_table_version': 56,
                            'default_vrf': 'default',
                            'route_distinguisher': '200:2',
                            'route_identifier': '4.4.4.4',
                            'routes':
                                {'15.1.1.0/24':
                                     {'index':
                                          {1:
                                               {'metric': 2219,
                                                'next_hop': '1.1.1.1',
                                                'localpref': 100,
                                                'origin_codes': 'e',
                                                'path': '200 33299 51178 47751 {27016}',
                                                'status_codes': '*>i',
                                                'weight': 0,
                                                },
                                           2:
                                               {'metric': 2219,
                                                'next_hop': '1.1.1.1',
                                                'localpref': 100,
                                                'origin_codes': 'e',
                                                'path': '200 33299 51178 47751 {27016}',
                                                'status_codes': '* i',
                                                'weight': 0,
                                                },

                                           },
                                      },
                                 '15.1.2.0/24':
                                     {'index':
                                          {1:
                                               {'metric': 2219,
                                                'next_hop': '1.1.1.1',
                                                'localpref': 100,
                                                'origin_codes': 'e',
                                                'path': '200 33299 51178 47751 {27016}',
                                                'status_codes': '*>i',
                                                'weight': 0,
                                                },
                                          2:
                                               {'metric': 2219,
                                                'next_hop': '1.1.1.1',
                                                'localpref': 100,
                                                'origin_codes': 'e',
                                                'path': '200 33299 51178 47751 {27016}',
                                                'status_codes': '* i',
                                                'weight': 0,
                                                },


                                          },
                                      },
                                 '15.1.3.0/24':
                                     {'index':
                                          {1:
                                               {'metric': 2219,
                                                'next_hop': '1.1.1.1',
                                                'localpref': 100,
                                                'origin_codes': 'e',
                                                'path': '200 33299 51178 47751 {27016}',
                                                'status_codes': '*>i',
                                                'weight': 0,
                                                },
                                           2:
                                               {'metric': 2219,
                                                'next_hop': '1.1.1.1',
                                                'localpref': 100,
                                                'origin_codes': 'e',
                                                'path': '200 33299 51178 47751 {27016}',
                                                'status_codes': '* i',
                                                'weight': 0,
                                                },

                                           },
                                      },
                                 },
                            },
                       },
                  },
             },
    }

    golden_output_2 = {'execute.return_value': '''
        R4_iosv#show bgp all
        For address family: IPv4 Unicast


        For address family: IPv6 Unicast


        For address family: VPNv4 Unicast

        BGP table version is 56, local router ID is 4.4.4.4
        Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,
                      r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter,
                      x best-external, a additional-path, c RIB-compressed,
        Origin codes: i - IGP, e - EGP, ? - incomplete
        RPKI validation codes: V valid, I invalid, N Not found

             Network          Next Hop            Metric LocPrf Weight Path
        Route Distinguisher: 200:1
         * i 15.1.1.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
         *>i                  1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
         * i 15.1.2.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
         *>i                  1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
        Route Distinguisher: 200:2
         *>i 15.1.1.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
         * i                  1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
         *>i 15.1.2.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
         * i                  1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
         *>i 15.1.3.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
         * i                  1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e



        For address family: L2VPN E-VPN


        For address family: VPNv4 Multicast


        For address family: MVPNv4 Unicast


        For address family: MVPNv6 Unicast


        For address family: VPNv6 Multicast
           ''' }

    golden_parsed_output_3 = {
        'vrf':
            {'default':
                 {'address_family':
                      {'vpnv4 unicast RD 200:1':
                           {'bgp_table_version': 56,
                            'default_vrf': 'default',
                            'route_distinguisher': '200:1',
                            'route_identifier': '4.4.4.4',
                            'routes':
                                {'15.1.1.0/24':
                                     {'index':
                                          {1:
                                               {'metric': 2219,
                                                'next_hop': '1.1.1.1',
                                                'localpref': 100,
                                                'origin_codes': 'e',
                                                'path': '200 33299 51178 47751 {27016}',
                                                'status_codes': '* i',
                                                'weight': 0,
                                                },
                                           2:
                                               {'metric': 2219,
                                                'next_hop': '1.1.1.1',
                                                'localpref': 100,
                                                'origin_codes': 'e',
                                                'path': '200 33299 51178 47751 {27016}',
                                                'status_codes': '*>i',
                                                'weight': 0,
                                                },

                                           },
                                      },
                                 '15.1.2.0/24':
                                     {'index':
                                          {1:
                                               {'metric': 2219,
                                                'next_hop': '1.1.1.1',
                                                'localpref': 100,
                                                'origin_codes': 'e',
                                                'path': '200 33299 51178 47751 {27016}',
                                                'status_codes': '* i',
                                                'weight': 0,
                                                },
                                           2:
                                               {'metric': 2219,
                                                'next_hop': '1.1.1.1',
                                                'localpref': 100,
                                                'origin_codes': 'e',
                                                'path': '200 33299 51178 47751 {27016}',
                                                'status_codes': '*>i',
                                                'weight': 0,
                                                },

                                           },
                                      },
                                 },
                            },
                       'vpnv4 unicast RD 200:2':
                           {'bgp_table_version': 56,
                            'default_vrf': 'default',
                            'route_distinguisher': '200:2',
                            'route_identifier': '4.4.4.4',
                            'routes':
                                {'15.1.1.0/24':
                                     {'index':
                                          {1:
                                               {'metric': 2219,
                                                'next_hop': '1.1.1.1',
                                                'localpref': 100,
                                                'origin_codes': 'e',
                                                'path': '200 33299 51178 47751 {27016}',
                                                'status_codes': '*>i',
                                                'weight': 0,
                                                },
                                           2:
                                               {'metric': 2219,
                                                'next_hop': '1.1.1.1',
                                                'localpref': 100,
                                                'origin_codes': 'e',
                                                'path': '200 33299 51178 47751 {27016}',
                                                'status_codes': '* i',
                                                'weight': 0,
                                                },

                                           },
                                      },
                                 '15.1.2.0/24':
                                     {'index':
                                          {1:
                                               {'metric': 2219,
                                                'next_hop': '1.1.1.1',
                                                'localpref': 100,
                                                'origin_codes': 'e',
                                                'path': '200 33299 51178 47751 {27016}',
                                                'status_codes': '*>i',
                                                'weight': 0,
                                                },
                                           2:
                                               {'metric': 2219,
                                                'next_hop': '1.1.1.1',
                                                'localpref': 100,
                                                'origin_codes': 'e',
                                                'path': '200 33299 51178 47751 {27016}',
                                                'status_codes': '* i',
                                                'weight': 0,
                                                },

                                           },
                                      },
                                 '15.1.3.0/24':
                                     {'index':
                                          {1:
                                               {'metric': 2219,
                                                'next_hop': '1.1.1.1',
                                                'localpref': 100,
                                                'origin_codes': 'e',
                                                'path': '200 33299 51178 47751 {27016}',
                                                'status_codes': '*>i',
                                                'weight': 0,
                                                },
                                           2:
                                               {'metric': 2219,
                                                'next_hop': '1.1.1.1',
                                                'localpref': 100,
                                                'origin_codes': 'e',
                                                'path': '200 33299 51178 47751 {27016}',
                                                'status_codes': '* i',
                                                'weight': 0,
                                                },

                                           },
                                      },
                                 },
                            },
                       },
                  },
             'VRF1':
                 {'address_family':
                     {
                         'vpnv4 unicast RD 300:1':
                             {'bgp_table_version': 56,
                              'default_vrf': 'VRF1',
                              'route_distinguisher': '300:1',
                              'route_identifier': '4.4.4.4',
                              'vrf_route_identifier': '44.44.44.44',
                              'routes':
                                  {'15.1.1.0/24':
                                       {'index':
                                            {1:
                                                 {'metric': 2219,
                                                  'next_hop': '1.1.1.1',
                                                  'localpref': 100,
                                                  'origin_codes': 'e',
                                                  'path': '200 33299 51178 47751 {27016}',
                                                  'status_codes': '* i',
                                                  'weight': 0,
                                                  },
                                             2:
                                                 {'metric': 2219,
                                                  'next_hop': '1.1.1.1',
                                                  'localpref': 100,
                                                  'origin_codes': 'e',
                                                  'path': '200 33299 51178 47751 {27016}',
                                                  'status_codes': '*>i',
                                                  'weight': 0,
                                                  },

                                             },
                                        },
                                   '15.1.2.0/24':
                                       {'index':
                                            {1:
                                                 {'metric': 2219,
                                                  'next_hop': '1.1.1.1',
                                                  'localpref': 100,
                                                  'origin_codes': 'e',
                                                  'path': '200 33299 51178 47751 {27016}',
                                                  'status_codes': '* i',
                                                  'weight': 0,
                                                  },
                                             2:
                                                 {'metric': 2219,
                                                  'next_hop': '1.1.1.1',
                                                  'localpref': 100,
                                                  'origin_codes': 'e',
                                                  'path': '200 33299 51178 47751 {27016}',
                                                  'status_codes': '*>i',
                                                  'weight': 0,
                                                  },

                                             },
                                        },
                                   '46.1.1.0/24':
                                       {'index':
                                            {1:
                                                 {'metric': 2219,
                                                  'next_hop': '10.4.6.6',
                                                  'origin_codes': 'e',
                                                  'path': '300 33299 51178 47751 {27016}',
                                                  'status_codes': '*>',
                                                  'weight': 0,
                                                  },

                                             },
                                        },
                                   '46.1.2.0/24':
                                       {'index':
                                            {1:
                                                 {'metric': 2219,
                                                  'next_hop': '10.4.6.6',
                                                  'origin_codes': 'e',
                                                  'path': '300 33299 51178 47751 {27016}',
                                                  'status_codes': '*>',
                                                  'weight': 0,
                                                  },

                                             },
                                        },
                                   '46.1.3.0/24':
                                       {'index':
                                            {1:
                                                 {'metric': 2219,
                                                  'next_hop': '10.4.6.6',
                                                  'origin_codes': 'e',
                                                  'path': '300 33299 51178 47751 {27016}',
                                                  'status_codes': '*>',
                                                  'weight': 0,
                                                  },

                                             },
                                        },
                                   '46.1.4.0/24':
                                       {'index':
                                            {1:
                                                 {'metric': 2219,
                                                  'next_hop': '10.4.6.6',
                                                  'origin_codes': 'e',
                                                  'path': '300 33299 51178 47751 {27016}',
                                                  'status_codes': '*>',
                                                  'weight': 0,
                                                  },

                                             },
                                        },
                                   '46.1.5.0/24':
                                       {'index':
                                            {1:
                                                 {'metric': 2219,
                                                  'next_hop': '10.4.6.6',
                                                  'origin_codes': 'e',
                                                  'path': '300 33299 51178 47751 {27016}',
                                                  'status_codes': '*>',
                                                  'weight': 0,
                                                  },

                                             },
                                        },
                                   '46.2.2.0/24':
                                       {'index':
                                            {1:
                                                 {'metric': 2219,
                                                  'next_hop': '20.4.6.6',
                                                  'origin_codes': 'e',
                                                  'path': '400 33299 51178 47751 {27016}',
                                                  'status_codes': '*>',
                                                  'weight': 0,
                                                  },

                                             },
                                        },
                                   },
                              },
                     },
                 },
             'VRF2':
                 {'address_family':
                     {
                         'vpnv4 unicast RD 400:1':
                             {'bgp_table_version': 56,
                              'default_vrf': 'VRF2',
                              'route_distinguisher': '400:1',
                              'route_identifier': '4.4.4.4',
                              'vrf_route_identifier': '44.44.44.44',
                              'routes':
                                  {'46.2.2.0/24':
                                       {'index':
                                            {1:
                                                 {'metric': 2219,
                                                  'next_hop': '20.4.6.6',
                                                  'origin_codes': 'e',
                                                  'path': '400 33299 51178 47751 {27016}',
                                                  'status_codes': '*>',
                                                  'weight': 0,
                                                  },
                                             },
                                        },
                                   '46.2.3.0/24':
                                       {'index':
                                            {1:
                                                 {'metric': 2219,
                                                  'next_hop': '20.4.6.6',
                                                  'origin_codes': 'e',
                                                  'path': '400 33299 51178 47751 {27016}',
                                                  'status_codes': '*>',
                                                  'weight': 0,
                                                  },
                                             },
                                        },
                                   '46.2.4.0/24':
                                       {'index':
                                            {1:
                                                 {'metric': 2219,
                                                  'next_hop': '20.4.6.6',
                                                  'origin_codes': 'e',
                                                  'path': '400 33299 51178 47751 {27016}',
                                                  'status_codes': '*>',
                                                  'weight': 0,
                                                  },
                                             },
                                        },
                                   '46.2.5.0/24':
                                       {'index':
                                            {1:
                                                 {'metric': 2219,
                                                  'next_hop': '20.4.6.6',
                                                  'origin_codes': 'e',
                                                  'path': '400 33299 51178 47751 {27016}',
                                                  'status_codes': '*>',
                                                  'weight': 0,
                                                  },
                                             },
                                        },
                                   '46.2.6.0/24':
                                       {'index':
                                            {1:
                                                 {'metric': 2219,
                                                  'next_hop': '20.4.6.6',
                                                  'origin_codes': 'e',
                                                  'path': '400 33299 51178 47751 {27016}',
                                                  'status_codes': '*>',
                                                  'weight': 0,
                                                  },
                                             },
                                        },
                                   '615:11:11::/64':
                                       {'index':
                                            {1:
                                                 {'metric': 2219,
                                                  'localpref': 100,
                                                  'next_hop': '::FFFF:1.1.1.1',
                                                  'origin_codes': 'e',
                                                  'path': '400 33299 51178 47751 {27016}',
                                                  'status_codes': '* i',
                                                  'weight': 0,
                                                  },
                                             2:
                                                 {'metric': 2219,
                                                  'localpref': 100,
                                                  'next_hop': '::FFFF:1.1.1.1',
                                                  'origin_codes': 'e',
                                                  'path': '400 33299 51178 47751 {27016}',
                                                  'status_codes': '*>i',
                                                  'weight': 0,
                                                  },
                                             },
                                        },
                                   '615:11:11:1::/64':
                                       {'index':
                                            {1:
                                                 {'metric': 2219,
                                                  'localpref': 100,
                                                  'next_hop': '::FFFF:1.1.1.1',
                                                  'origin_codes': 'e',
                                                  'path': '400 33299 51178 47751 {27016}',
                                                  'status_codes': '* i',
                                                  'weight': 0,
                                                  },
                                             2:
                                                 {'metric': 2219,
                                                  'localpref': 100,
                                                  'next_hop': '::FFFF:1.1.1.1',
                                                  'origin_codes': 'e',
                                                  'path': '400 33299 51178 47751 {27016}',
                                                  'status_codes': '*>i',
                                                  'weight': 0,
                                                  },
                                             },
                                        },

                                   },
                              },
                     },
                 },
             },
    }

    golden_output_3 = {'execute.return_value': '''
           R4_iosv#show bgp all
           For address family: IPv4 Unicast


           For address family: IPv6 Unicast


           For address family: VPNv4 Unicast

           BGP table version is 56, local router ID is 4.4.4.4
           Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,
                         r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter,
                         x best-external, a additional-path, c RIB-compressed,
           Origin codes: i - IGP, e - EGP, ? - incomplete
           RPKI validation codes: V valid, I invalid, N Not found

                Network          Next Hop            Metric LocPrf Weight Path
           Route Distinguisher: 200:1
            * i 15.1.1.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
            *>i                  1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
            * i 15.1.2.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
            *>i                  1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
           Route Distinguisher: 200:2
            *>i 15.1.1.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
            * i                  1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
            *>i 15.1.2.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
            * i                  1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
            *>i 15.1.3.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
            * i                  1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
           Route Distinguisher: 300:1 (default for vrf VRF1) VRF Router ID 44.44.44.44
            * i 15.1.1.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
            *>i                  1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
            * i 15.1.2.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
            *>i                  1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
            *>  46.1.1.0/24      10.4.6.6              2219             0 300 33299 51178 47751 {27016} e
            *>  46.1.2.0/24      10.4.6.6              2219             0 300 33299 51178 47751 {27016} e
            *>  46.1.3.0/24      10.4.6.6              2219             0 300 33299 51178 47751 {27016} e
            *>  46.1.4.0/24      10.4.6.6              2219             0 300 33299 51178 47751 {27016} e
            *>  46.1.5.0/24      10.4.6.6              2219             0 300 33299 51178 47751 {27016} e
            *>  46.2.2.0/24      20.4.6.6              2219             0 400 33299 51178 47751 {27016} e
           Route Distinguisher: 400:1 (default for vrf VRF2) VRF Router ID 44.44.44.44
            *>  46.2.2.0/24      20.4.6.6              2219             0 400 33299 51178 47751 {27016} e
            *>  46.2.3.0/24      20.4.6.6              2219             0 400 33299 51178 47751 {27016} e
            *>  46.2.4.0/24      20.4.6.6              2219             0 400 33299 51178 47751 {27016} e
            *>  46.2.5.0/24      20.4.6.6              2219             0 400 33299 51178 47751 {27016} e
            *>  46.2.6.0/24      20.4.6.6              2219             0 400 33299 51178 47751 {27016} e
            * i 615:11:11::/64   ::FFFF:1.1.1.1        2219    100      0 400 33299 51178 47751 {27016} e
            *>i                  ::FFFF:1.1.1.1        2219    100      0 400 33299 51178 47751 {27016} e
            * i 615:11:11:1::/64 ::FFFF:1.1.1.1        2219    100      0 400 33299 51178 47751 {27016} e
            *>i                  ::FFFF:1.1.1.1        2219    100      0 400 33299 51178 47751 {27016} e



           For address family: L2VPN E-VPN


           For address family: VPNv4 Multicast


           For address family: MVPNv4 Unicast


           For address family: MVPNv6 Unicast


           For address family: VPNv6 Multicast
              '''}


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowBgpAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowBgpAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_3)
        obj = ShowBgpAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_3)

if __name__ == '__main__':
    unittest.main()
