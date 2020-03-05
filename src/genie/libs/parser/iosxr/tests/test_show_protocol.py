
# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_ospf
from genie.libs.parser.iosxr.show_protocol import ShowProtocolsAfiAllAll


# ===========================================
#  Unit test for 'show protocols afi-all all'
# ===========================================
class test_show_protocols_afi_all_all(unittest.TestCase):

    '''Unit test for "show protocols afi-all all" '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'protocols': 
            {'bgp': 
                {'address_family': 
                    {'vpnv4 unicast': 
                        {'distance': 
                            {'external': 20,
                            'internal': 200,
                            'local': 200},
                        'neighbors': 
                            {'10.64.4.4': 
                                {'gr_enable': 'No',
                                'last_update': '00:01:28',
                                'nsr_state': 'None'}}},
                    'vpnv6 unicast': 
                        {'distance': 
                            {'external': 20,
                            'internal': 200,
                            'local': 200},
                        'neighbors': 
                            {'10.64.4.4': 
                                {'gr_enable': 'No',
                                'last_update': '00:01:28',
                                'nsr_state': 'None'}}}},
                'bgp_pid': 100,
                'graceful_restart': 
                    {'enable': False},
                'nsr': 
                    {'current_state': 'active ready',
                    'enable': True}},
            'ospf': 
                {'vrf': 
                    {'default': 
                        {'address_family': 
                            {'ipv4': 
                                {'instance': 
                                    {'1': 
                                        {'areas': 
                                            {'0.0.0.0': 
                                                {'interfaces': ['Loopback0', 'GigabitEthernet0/0/0/0', 'GigabitEthernet0/0/0/2'],
                                                'mpls': 
                                                    {'te': 
                                                        {'enable': True}}}},
                                                'nsf': False,
                                        'preference': 
                                            {'multi_values': 
                                                {'external': 114,
                                                'granularity': 
                                                    {'detail': 
                                                        {'inter_area': 113,
                                                        'intra_area': 112}}},
                                            'single_value': 
                                                {'all': 110}},
                                        'redistribution': 
                                            {'bgp': 
                                                {'bgp_id': 100,
                                                'metric': 111},
                                            'connected': 
                                                {'enabled': True},
                                            'isis': 
                                                {'isis_pid': '10',
                                                'metric': 3333},
                                            'static': 
                                                {'enabled': True,
                                                'metric': 10}},
                                        'router_id': '10.36.3.3'}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        RP/0/0/CPU0:R3_ospf_xr#show protocols afi-all all
        Mon Jan  8 17:45:17.553 UTC

        Routing Protocol "BGP 100"
        Non-stop routing is enabled
        Graceful restart is not enabled
        Current BGP NSR state - Active Ready
        BGP NSR state not ready: Wait for standby ready msg

        Address Family VPNv4 Unicast:
          Distance: external 20 internal 200 local 200
          Routing Information Sources:
            Neighbor          State/Last update received  NSR-State  GR-Enabled
            10.64.4.4           00:01:28                    None         No

        Address Family VPNv6 Unicast:
          Distance: external 20 internal 200 local 200
          Routing Information Sources:
            Neighbor          State/Last update received  NSR-State  GR-Enabled
            10.64.4.4           00:01:28                    None         No

        Routing Protocol OSPF 1
          Router Id: 10.36.3.3
          Distance: 110
          Distance: IntraArea 112 InterArea 113 External/NSSA 114
          Non-Stop Forwarding: Disabled
          Redistribution:
            connected
            static with metric 10
            bgp 100 with metric 111
            isis 10 with metric 3333
          Area 0
            MPLS/TE enabled
            Loopback0
            GigabitEthernet0/0/0/0
            GigabitEthernet0/0/0/2
        '''}

    golden_parsed_output2 = {
        "protocols": {
              "ospf": {
                   "vrf": {
                        "default": {
                             "address_family": {
                                  "ipv4": {
                                       "instance": {
                                            "1": {
                                                 "preference": {
                                                      "single_value": {
                                                           "all": 110
                                                      }
                                                 },
                                                 "router_id": "192.168.205.1",
                                                 "nsf": True,
                                                 "areas": {
                                                      "0.0.0.1": {
                                                           "mpls": {
                                                                "te": {
                                                                     "enable": True
                                                                }
                                                           },
                                                           "interfaces": [
                                                                "Loopback5"
                                                           ]
                                                      },
                                                      "0.0.0.0": {
                                                           "interfaces": [
                                                                "Loopback0"
                                                           ]
                                                      }
                                                 }
                                            }
                                       }
                                  }
                             }
                        }
                   }
              },
              "ospfv3": {
                   "vrf": {
                        "default": {
                             "address_family": {
                                  "ipv4": {
                                       "instance": {
                                            "1": {
                                                 "preference": {
                                                      "single_value": {
                                                           "all": 110
                                                      }
                                                 },
                                                 "router_id": "0.0.0.0"
                                            }
                                       }
                                  }
                             }
                        }
                   }
              },
              "bgp": {
                   "bgp_pid": 100,
                   "nsr": {
                        "enable": True,
                        "current_state": "tcp initial sync"
                   },
                   "address_family": {
                        "vpnv6 unicast": {
                             "distance": {
                                  "internal": 200,
                                  "local": 200,
                                  "external": 20
                             }
                        },
                        "vpnv4 unicast": {
                             "distance": {
                                  "internal": 200,
                                  "local": 200,
                                  "external": 20
                             }
                        }
                   }
              }
         }
    }
    golden_output2 = {'execute.return_value': '''
        Routing Protocol "BGP 100"
        Non-stop routing is enabled
        Graceful restart is enabled
        Current BGP NSR state - TCP Initial Sync
        BGP NSR state not ready: TCP Initsync in progress

        Address Family VPNv4 Unicast:
          Distance: external 20 internal 200 local 200

        Address Family VPNv6 Unicast:
          Distance: external 20 internal 200 local 200


        IS-IS Router: 1
          System Id: 1c53.00ff.0102 
          Instance Id: 0
          IS Levels: level-2-only
          Manual area address(es):
            49.0001
          Routing for area address(es):
            49.0001
          Non-stop forwarding: Disabled
          Most recent startup mode: Cold Restart
          TE connection status: Up
          Topologies supported by IS-IS:
            IPv4 Unicast
              Level-2
                Metric style (generate/accept): Narrow/Narrow
                Metric: 10
                ISPF status: Disabled
              No protocols redistributed
              Distance: 115
              Advertise Passive Interface Prefixes Only: No
            IPv6 Unicast
              Level-2
                Metric: 10
                ISPF status: Disabled
              No protocols redistributed
              Distance: 115
              Advertise Passive Interface Prefixes Only: No
          SRLB allocated: 0 - 0
          SRGB not allocated
          Interfaces supported by IS-IS:
            GigabitEthernet0/0/0/0.104 is disabled (active in configuration)
            GigabitEthernet0/0/0/1.104 is disabled (active in configuration)

        Routing Protocol OSPF 1
          Router Id: 192.168.205.1
          Distance: 110
          Non-Stop Forwarding: Enabled
          Redistribution:
            None
          Area 0
            Loopback0
          Area 1
            MPLS/TE enabled
            Loopback5

        Routing Protocol OSPFv3 1
          Router Id: 0.0.0.0
          Distance: 110
          Graceful Restart: Disabled
          Redistribution:
            None
    '''}

    def test_show_protocols_afi_all_all_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowProtocolsAfiAllAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_protocols_afi_all_all_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowProtocolsAfiAllAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_protocols_afi_all_all_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowProtocolsAfiAllAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
