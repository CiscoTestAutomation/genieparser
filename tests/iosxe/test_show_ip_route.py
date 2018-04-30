import unittest
from unittest.mock import Mock

from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.iosxe.show_ip_route import ShowIpRoute, ShowIpv6Route


# =========================================
#  Unit test for 'show ip route bgp'
#                'show ip route vrf <WORD> bgp'
#                'show ipv6 route bgp'
#                'show ipv6 route vrf <WORD> bgp'
# =========================================
class test_show_ip_route(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {'vrf':
      {'default':
        {'address_family':
          {'ipv4 unicast':
            {'ip':
              {'15.1.1.0/24':
                {'nexthop':
                  {'1.1.1.1':
                    {'protocol':
                      {'bgp':
                        {'metric': '2219',
                         'preference': '200',
                         'uptime': '01:40:40'}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
      R1#show ip route bgp
      IPv6 Routing Table - default - 5 entries
      Codes: C - Connected, L - Local, S - Static, U - Per-user Static route
             B - BGP, R - RIP, H - NHRP, I1 - ISIS L1
             I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary, D - EIGRP
             EX - EIGRP external, ND - ND Default, NDp - ND Prefix, DCE - Destination
             NDr - Redirect, RL - RPL, O - OSPF Intra, OI - OSPF Inter
             OE1 - OSPF ext 1, OE2 - OSPF ext 2, ON1 - OSPF NSSA ext 1
             ON2 - OSPF NSSA ext 2, la - LISP alt, lr - LISP site-registrations
             ld - LISP dyn-eid, a - Application
            15.0.0.0/24 is subnetted, 5 subnets
      B        15.1.1.0 [200/2219] via 1.1.1.1, 01:40:40
      '''}

    golden_parsed_output2 = {'vrf':
      {'VRF1':
        {'address_family':
          {'vpnv4 unicast':
            {'ip':
              {'15.1.1.0/24':
                {'nexthop':
                  {'1.1.1.1':
                    {'protocol':
                      {'bgp':
                        {'metric': '2219',
                         'preference': '200',
                         'uptime': '01:40:40'}}}}},
              '15.1.2.0/24':
                {'nexthop':
                  {'1.1.1.1':
                    {'protocol':
                      {'bgp':
                        {'metric': '2219',
                         'preference': '200',
                         'uptime': '01:40:40'}}}}},
              '15.1.3.0/24':
                {'nexthop':
                  {'1.1.1.1':
                    {'protocol':
                      {'bgp':
                        {'metric': '2219',
                         'preference': '200',
                         'uptime': '01:40:40'}}}}},
              '15.1.4.0/24':
                {'nexthop':
                  {'1.1.1.1':
                    {'protocol':
                      {'bgp':
                        {'metric': '2219',
                         'preference': '200',
                         'uptime': '01:40:40'}}}}},
              '15.1.5.0/24':
                {'nexthop':
                  {'1.1.1.1':
                    {'protocol':
                      {'bgp':
                        {'metric': '2219',
                         'preference': '200',
                         'uptime': '01:40:40'}}}}},
              '46.1.1.0/24':
                {'nexthop':
                  {'10.4.6.6':
                    {'protocol':
                      {'bgp':
                        {'metric': '2219',
                         'preference': '20',
                         'uptime': '01:36:35'}}}}},
              '46.1.2.0/24':
                {'nexthop':
                  {'10.4.6.6':
                    {'protocol':
                      {'bgp':
                        {'metric': '2219',
                         'preference': '20',
                         'uptime': '01:36:35'}}}}},
              '46.1.3.0/24':
                {'nexthop':
                  {'10.4.6.6':
                    {'protocol':
                      {'bgp':
                        {'metric': '2219',
                         'preference': '20',
                         'uptime': '01:36:35'}}}}},
              '46.1.4.0/24':
                {'nexthop':
                  {'10.4.6.6':
                    {'protocol':
                      {'bgp':
                        {'metric': '2219',
                         'preference': '20',
                         'uptime': '01:36:35'}}}}},
              '46.1.5.0/24':
                {'nexthop':
                  {'10.4.6.6':
                    {'protocol':
                      {'bgp':
                        {'metric': '2219',
                         'preference': '20',
                         'uptime': '01:36:35'}}}}},
              '46.2.2.0/24':
                {'nexthop':
                  {'20.4.6.6':
                    {'protocol':
                      {'bgp':
                        {'metric': '2219',
                         'preference': '20',
                         'route_table': 'VRF2',
                         'uptime': '01:36:26'}}}}},
              '46.2.3.0/24':
                {'nexthop':
                  {'20.4.6.6':
                    {'protocol':
                      {'bgp':
                        {'metric': '2219',
                         'preference': '20',
                         'route_table': 'VRF2',
                         'uptime': '01:36:26'}}}}},
              '46.2.4.0/24':
                {'nexthop':
                  {'20.4.6.6':
                    {'protocol':
                      {'bgp':
                        {'metric': '2219',
                         'preference': '20',
                         'route_table': 'VRF2',
                         'uptime': '01:36:26'}}}}},
              '46.2.5.0/24':
                {'nexthop':
                  {'20.4.6.6':
                    {'protocol':
                      {'bgp':
                        {'metric': '2219',
                         'preference': '20',
                         'route_table': 'VRF2',
                         'uptime': '01:36:26'}}}}},
              '46.2.6.0/24':
                {'nexthop':
                  {'20.4.6.6':
                    {'protocol':
                      {'bgp':
                        {'metric': '2219',
                         'preference': '20',
                         'route_table': 'VRF2',
                         'uptime': '01:36:26'}}}}}}}}}}}

    golden_output2 = {'execute.return_value': '''
      R4_iosv#show ip route vrf VRF1 bgp
      Routing Table: VRF1
      Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
             D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
             N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
             E1 - OSPF external type 1, E2 - OSPF external type 2
             i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
             ia - IS-IS inter area, * - candidate default, U - per-user static route
             o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP
             a - application route
             + - replicated route, % - next hop override

      Gateway of last resort is not set

            15.0.0.0/24 is subnetted, 5 subnets
      B        15.1.1.0 [200/2219] via 1.1.1.1, 01:40:40
      B        15.1.2.0 [200/2219] via 1.1.1.1, 01:40:40
      B        15.1.3.0 [200/2219] via 1.1.1.1, 01:40:40
      B        15.1.4.0 [200/2219] via 1.1.1.1, 01:40:40
      B        15.1.5.0 [200/2219] via 1.1.1.1, 01:40:40
            46.0.0.0/24 is subnetted, 10 subnets
      B        46.1.1.0 [20/2219] via 10.4.6.6, 01:36:35
      B        46.1.2.0 [20/2219] via 10.4.6.6, 01:36:35
      B        46.1.3.0 [20/2219] via 10.4.6.6, 01:36:35
      B        46.1.4.0 [20/2219] via 10.4.6.6, 01:36:35
      B        46.1.5.0 [20/2219] via 10.4.6.6, 01:36:35
      B        46.2.2.0 [20/2219] via 20.4.6.6 (VRF2), 01:36:26
      B        46.2.3.0 [20/2219] via 20.4.6.6 (VRF2), 01:36:26
      B        46.2.4.0 [20/2219] via 20.4.6.6 (VRF2), 01:36:26
      B        46.2.5.0 [20/2219] via 20.4.6.6 (VRF2), 01:36:26
      B        46.2.6.0 [20/2219] via 20.4.6.6 (VRF2), 01:36:26
      '''}

    golden_parsed_output3 = {'vrf':
      {'default':
        {'address_family':
          {'ipv6 unicast':
            {'ip':
              {'2001:2:2:2::2/128':
                {'nexthop':
                  {'2001:DB8:1:1::2':
                    {'protocol':
                      {'bgp': {'metric': '0',
                       'preference': '200'}
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }

    golden_output3 = {'execute.return_value': '''
      R1#show ipv6 route bgp
      IPv6 Routing Table - default - 5 entries
      Codes: C - Connected, L - Local, S - Static, U - Per-user Static route
             B - BGP, R - RIP, H - NHRP, I1 - ISIS L1
             I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary, D - EIGRP
             EX - EIGRP external, ND - ND Default, NDp - ND Prefix, DCE - Destination
             NDr - Redirect, RL - RPL, O - OSPF Intra, OI - OSPF Inter
             OE1 - OSPF ext 1, OE2 - OSPF ext 2, ON1 - OSPF NSSA ext 1
             ON2 - OSPF NSSA ext 2, la - LISP alt, lr - LISP site-registrations
             ld - LISP dyn-eid, a - Application
      B   2001:2:2:2::2/128 [200/0]
           via 2001:DB8:1:1::2
      '''}

    golden_parsed_output4 = {'vrf':
      {'VRF1':
        {'address_family':
          {'vpnv6 unicast':
            {'ip':
              {'615:11:11:1::/64':
                {'nexthop':
                  {'1.1.1.1':
                    {'protocol':
                      {'bgp':
                        {'attribute': 'indirectly connected',
                         'metric': '2219',
                         'preference': '200',
                         'route_table': 'default'}}}}},
              '615:11:11:2::/64':
                {'nexthop':
                  {'1.1.1.1':
                    {'protocol':
                      {'bgp':
                        {'attribute': 'indirectly connected',
                         'metric': '2219',
                         'preference': '200',
                         'route_table': 'default'}}}}},
              '615:11:11:3::/64':
                {'nexthop':
                  {'1.1.1.1':
                    {'protocol':
                      {'bgp':
                        {'attribute': 'indirectly connected',
                         'metric': '2219',
                         'preference': '200',
                         'route_table': 'default'}}}}},
              '615:11:11:4::/64':
                {'nexthop':
                  {'1.1.1.1':
                    {'protocol':
                      {'bgp':
                        {'attribute': 'indirectly connected',
                         'metric': '2219',
                         'preference': '200',
                         'route_table': 'default'}}}}},
              '615:11:11::/64':
                {'nexthop':
                  {'1.1.1.1':
                    {'protocol':
                      {'bgp':
                        {'attribute': 'indirectly connected',
                         'metric': '2219',
                         'preference': '200',
                         'route_table': 'default'}}}}},
              '646:11:11:1::/64':
                {'nexthop':
                  {'2001:DB8:4:6::6':
                    {'protocol':
                      {'bgp':
                        {'metric': '2219',
                         'preference': '20'}}}}},
              '646:11:11:2::/64':
                {'nexthop':
                  {'2001:DB8:4:6::6':
                    {'protocol':
                      {'bgp':
                        {'metric': '2219',
                         'preference': '20'}}}}},
              '646:11:11:3::/64':
                {'nexthop':
                  {'2001:DB8:4:6::6':
                    {'protocol':
                      {'bgp':
                        {'metric': '2219',
                         'preference': '20'}}}}},
              '646:11:11:4::/64':
                {'nexthop':
                  {'2001:DB8:4:6::6':
                    {'protocol':
                      {'bgp':
                        {'metric': '2219',
                         'preference': '20'}}}}},
              '646:11:11::/64':
                {'nexthop':
                  {'2001:DB8:4:6::6':
                    {'protocol':
                      {'bgp':
                        {'metric': '2219',
                         'preference': '20'}}}}},
              '646:22:22:1::/64':
                {'nexthop':
                  {'2001:DB8:20:4:6::6':
                    {'protocol':
                      {'bgp':
                        {'metric': '2219',
                         'preference': '20',
                         'route_table': 'VRF2'}}}}},
              '646:22:22:2::/64':
                {'nexthop':
                  {'2001:DB8:20:4:6::6':
                    {'protocol':
                      {'bgp':
                        {'metric': '2219',
                         'preference': '20',
                         'route_table': 'VRF2'}}}}},
              '646:22:22:3::/64':
                {'nexthop':
                  {'2001:DB8:20:4:6::6':
                    {'protocol':
                      {'bgp':
                        {'metric': '2219',
                         'preference': '20',
                         'route_table': 'VRF2'}}}}},
              '646:22:22:4::/64':
                {'nexthop':
                  {'2001:DB8:20:4:6::6':
                    {'protocol':
                      {'bgp':
                        {'metric': '2219',
                         'preference': '20',
                         'route_table': 'VRF2'}}}}},
              '646:22:22::/64':
                {'nexthop':
                  {'2001:DB8:20:4:6::6':
                    {'protocol':
                      {'bgp':
                        {'metric': '2219',
                         'preference': '20',
                         'route_table': 'VRF2'}}}}}}}}}}}


    golden_output4 = {'execute.return_value': '''
      R4_iosv#show ipv6 route vrf VRF1 bgp
      IPv6 Routing Table - VRF1 - 18 entries
      Codes: C - Connected, L - Local, S - Static, U - Per-user Static route
             B - BGP, HA - Home Agent, MR - Mobile Router, R - RIP
             H - NHRP, I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea
             IS - ISIS summary, D - EIGRP, EX - EIGRP external, NM - NEMO
             ND - ND Default, NDp - ND Prefix, DCE - Destination, NDr - Redirect
             O - OSPF Intra, OI - OSPF Inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2
             ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2, la - LISP alt
             lr - LISP site-registrations, ld - LISP dyn-eid, a - Application
      B   615:11:11::/64 [200/2219]
           via 1.1.1.1%default, indirectly connected
      B   615:11:11:1::/64 [200/2219]
           via 1.1.1.1%default, indirectly connected
      B   615:11:11:2::/64 [200/2219]
           via 1.1.1.1%default, indirectly connected
      B   615:11:11:3::/64 [200/2219]
           via 1.1.1.1%default, indirectly connected
      B   615:11:11:4::/64 [200/2219]
           via 1.1.1.1%default, indirectly connected
      B   646:11:11::/64 [20/2219]
           via 2001:DB8:4:6::6
      B   646:11:11:1::/64 [20/2219]
           via 2001:DB8:4:6::6
      B   646:11:11:2::/64 [20/2219]
           via 2001:DB8:4:6::6
      B   646:11:11:3::/64 [20/2219]
           via 2001:DB8:4:6::6
      B   646:11:11:4::/64 [20/2219]
           via 2001:DB8:4:6::6
      B   646:22:22::/64 [20/2219]
           via 2001:DB8:20:4:6::6%VRF2
      B   646:22:22:1::/64 [20/2219]
           via 2001:DB8:20:4:6::6%VRF2
      B   646:22:22:2::/64 [20/2219]
           via 2001:DB8:20:4:6::6%VRF2
      B   646:22:22:3::/64 [20/2219]
           via 2001:DB8:20:4:6::6%VRF2
      B   646:22:22:4::/64 [20/2219]
           via 2001:DB8:20:4:6::6%VRF2
      '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        route_map_obj = ShowIpRoute(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = route_map_obj.parse(protocol='bgp', ip='ip')

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        route_map_obj = ShowIpRoute(device=self.device)
        parsed_output = route_map_obj.parse(protocol='bgp', ip='ip')
        self.assertEqual(parsed_output,self.golden_parsed_output1)

    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        route_map_obj = ShowIpRoute(device=self.device)
        parsed_output = route_map_obj.parse(protocol='bgp', vrf='VRF1', ip='ip')
        self.assertEqual(parsed_output,self.golden_parsed_output2)

    def test_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        route_map_obj = ShowIpv6Route(device=self.device)
        parsed_output = route_map_obj.parse(protocol='bgp', ip='ipv6')
        self.assertEqual(parsed_output,self.golden_parsed_output3)

    def test_golden4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output4)
        route_map_obj = ShowIpv6Route(device=self.device)
        parsed_output = route_map_obj.parse(protocol='bgp', vrf='VRF1', ip='ipv6')
        self.assertEqual(parsed_output,self.golden_parsed_output4)

if __name__ == '__main__':
    unittest.main()
