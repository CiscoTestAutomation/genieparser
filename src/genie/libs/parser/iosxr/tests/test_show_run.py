# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_run
from genie.libs.parser.iosxr.show_run import ShowRunKeyChain,ShowRunRouterIsis


# ======================================================
#  Unit test for 'show run key chain'
# ======================================================
class test_show_run_key_chain(unittest.TestCase):
    '''Unit test for "show run key chain" '''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'key_chain': {
            'ISIS-HELLO-CORE': {
                'keys': {
                    '1': {
                        'accept_lifetime': '00:01:00 january 01 2013 infinite',
                        'key_string': 'password 020F175218',
                        'cryptographic_algorithm': 'HMAC-MD5'}},
                'accept_tolerance': 'infinite'}}}

    golden_output1 = {'execute.return_value': '''
        show run key chain
        Wed Mar 27 22:31:22.533 UTC
        key chain ISIS-HELLO-CORE
            key 1
                accept-lifetime 00:01:00 january 01 2013 infinite
                key-string password 020F175218
                cryptographic-algorithm HMAC-MD5
                !
            accept-tolerance infinite !
    '''}

    def test_show_run_key_chain(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowRunKeyChain(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_run_key_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowRunKeyChain(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ============================================================
#  Unit test for 'show run router isis'
# ============================================================
class test_show_run_router_isis(unittest.TestCase):
    '''Unit test for "show run router isis" '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'isis': {
            'test': {
                'address_family': {
                    'ipv4_unicast': {
                        'fast_reroute': {
                            'per_prefix': {
                                'tiebreaker': {
                                    'srlg_disjoint': 'index 255'}}},
                        'mpls': {
                            'traffic_eng': ['level-2-only spf-interval maximum-wait 8000 initial-wait 300 secondary-wait 500']},
                        'segment_routing': {
                            'mpls': 'sr-prefer'},
                        'spf_prefix_priority': {
                            'critical_tag': '1000'}}},
                'segment_routing': {
                    'global_block': '160000 167999'},
                'interfaces': {
                    'Bundle-Ether2': {
                        'other': ['passive']}},
                'lsp_gen_interval': {
                    'maximum_wait': '8000',
                    'initial_wait': '1',
                    'secondary_wait': '250'}}}}

    golden_output1 = {'execute.return_value': '''
        RP/0/RP0/CPU0:R2#sh run router isis
        Wed Apr 10 15:11:45.748 UTC
        router isis test
            segment-routing global-block 160000 167999
            lsp-gen-interval maximum-wait 8000 initial-wait 1 secondary-wait 250
            address-family ipv4 unicast
                fast-reroute per-prefix tiebreaker srlg-disjoint index 255
                mpls traffic-eng level-2-only spf-interval maximum-wait 8000 initial-wait 300 secondary-wait 500
                segment-routing mpls sr-prefer
                spf prefix-priority critical tag 1000
            !
            interface Bundle-Ether2
                passive
            !
        !
    '''}

    golden_parsed_output2 = {
        'isis': {
            'test2': {
                'address_family': {
                    'ipv4_unicast': {
                        'advertise': 'passive_only',
                        'metric': '100000',
                        'metric_style': 'wide',
                        'redistribute': 'static '
                                        'level_2 '
                                        'metric '
                                        '10',
                        'router_id': '10.25.5.6',
                        'segment_routing': {'mpls': 'sr-prefer'},
                        'spf': 'prefix_priority '
                               'medium '
                               'ISIS_PREFIX_PRIORITY_MEDIUM',
                        'spf_interval': {'initial_wait': '50',
                                         'maximum_wait': '5000',
                                         'secondary_wait': '150'}}},
                    'interfaces': {
                        'Bundle-Ether15': {
                            'address_family': {
                                'ipv4_unicast': {
                                    'fast_reroute': 'per_prefix '
                                                    'ti_lfa',
                                    'metric': '10'}
                            },
                            'other': ['point-to-point']},
                        'HundredGigE0/0/0/100': {
                            'address_family': {
                                'ipv4_unicast': {
                                    'fast_reroute': 'per_prefix '
                                                    'ti_lfa',
                                    'metric': '10'}
                            },
                            'bfd': {
                                'fast_detect': 'ipv4',
                                'minimum_interval': '250',
                                'multiplier': '3'},
                            'other': ['point-to-point']},
                        'HundredGigE0/0/0/101': {
                            'address_family': {
                                'ipv4_unicast': {
                                    'fast_reroute': 'per_prefix '
                                                    'ti_lfa',
                                    'metric': '10'}},
                            'bfd': {
                                'fast_detect': 'ipv4',
                                'minimum_interval': '250',
                                'multiplier': '3'},
                            'other': ['point-to-point']},
                        'HundredGigE0/0/0/102': {
                            'address_family': {
                                'ipv4_unicast': {
                                    'metric': '10'}},
                            'bfd': {
                                'fast_detect': 'ipv4',
                                'minimum_interval': '250',
                                'multiplier': '3'},
                            'other': ['point-to-point']},
                        'HundredGigE0/0/0/103': {
                            'address_family': {
                                'ipv4_unicast': {
                                    'fast_reroute': 'per_prefix '
                                                    'ti_lfa',
                                    'metric': '10'}},
                            'bfd': {'fast_detect': 'ipv4',
                                    'minimum_interval': '250',
                                    'multiplier': '3'},
                            'other': ['point-to-point']},
                        'HundredGigE0/0/0/104': {
                            'address_family': {
                                'ipv4_unicast': {
                                    'metric': '100'}
                            },
                            'bfd': {
                                'fast_detect': 'ipv4',
                                'minimum_interval': '250',
                                'multiplier': '3'},
                            'other': ['point-to-point']},
                        'HundredGigE0/0/0/105': {
                            'address_family': {
                                'ipv4_unicast': {
                                    'metric': '100'}
                            },
                            'bfd': {
                                'fast_detect': 'ipv4',
                                'minimum_interval': '250',
                                'multiplier': '3'},
                            'other': ['point-to-point']},
                        'HundredGigE0/0/0/106': {
                            'address_family': {
                                'ipv4_unicast': {
                                    'metric': '100'}
                                },
                            'bfd': {'fast_detect': 'ipv4',
                                    'minimum_interval': '250',
                                    'multiplier': '3'},
                            'other': ['point-to-point']},
                        'HundredGigE0/0/0/107': {
                            'address_family': {
                                'ipv4_unicast': {
                                    'metric': '100'}},
                            'bfd': {
                                'fast_detect': 'ipv4',
                                'minimum_interval': '250',
                                'multiplier': '3'},
                            'other': ['point-to-point']},
                        'HundredGigE0/0/0/108': {
                            'address_family': {
                                'ipv4_unicast': {
                                    'metric': '200000'}},
                                    'bfd': {
                                        'fast_detect': 'ipv4',
                                        'minimum_interval': '250',
                                        'multiplier': '3'},
                                    'other': ['point-to-point']},
                        'HundredGigE0/0/0/109': {
                            'address_family': {
                                'ipv4_unicast': {
                                    'metric': '200000'}
                            },
                            'bfd': {
                                'fast_detect': 'ipv4',
                                'minimum_interval': '250',
                                'multiplier': '3'},
                            'other': ['point-to-point',
                                      'RP/0/RP0/CPU0:spine1-tatooine#']},
                        'Loopback0': {
                            'address_family': {
                                'ipv4_unicast': {
                                    'metric': '10',
                                    'prefix_sid': 'index '
                                                  '288'}
                            },
                            'other': ['passive']},
                        'TenGigE0/0/0/0/200': {},
                        'TenGigE0/0/0/0/201': {
                            'address_family': {
                                'ipv4_unicast': {
                                    'metric': '10'}
                            },
                            'bfd': {
                                'fast_detect': 'ipv4',
                                'minimum_interval': '250',
                                'multiplier': '3'},
                            'other': ['point-to-point']},
                        'TenGigE0/0/0/0/202': {
                            'address_family': {
                                'ipv4_unicast': {
                                    'metric': '10'}
                            },
                            'bfd': {'fast_detect': 'ipv4',
                                  'minimum_interval': '250',
                                  'multiplier': '3'},
                            'other': ['point-to-point']}
                        },
            'is_type': 'level-2-only',
            'log': 'adjacency changes',
            'lsp_gen_interval': {
                'initial_wait': '20',
                'maximum_wait': '5000',
                'secondary_wait': '100'},
            'lsp_refresh_interval': '35000',
            'max_lsp_lifetime': '65535',
            'net': '10.9.3.4.5.6',
            'segment_routing': {},
            'set_overload_bit': 'on-startup 300'}
        }
    }

    golden_output2 = {'execute.return_value': '''
        show run router isis

        Fri Sep 27 17:02:48.279 EDT
        router isis test2
         set-overload-bit on-startup 300
         is-type level-2-only
         net 10.9.3.4.5.6
         nsr
         log adjacency changes
         lsp-gen-interval maximum-wait 5000 initial-wait 20 secondary-wait 100
         lsp-refresh-interval 35000
         max-lsp-lifetime 65535
         address-family ipv4 unicast
          metric-style wide
          metric 100000
          advertise passive-only
          spf-interval maximum-wait 5000 initial-wait 50 secondary-wait 150
          router-id 10.25.5.6
          redistribute static level-2 metric 10
          segment-routing mpls sr-prefer
          spf prefix-priority high ISIS-PREFIX-PRIORITY-HIGH
          spf prefix-priority medium ISIS-PREFIX-PRIORITY-MEDIUM
         !
         interface Bundle-Ether15
          point-to-point
          address-family ipv4 unicast
          fast-reroute per-prefix
           fast-reroute per-prefix tiebreaker node-protecting index 100
           fast-reroute per-prefix ti-lfa
           metric 10
          !
         !
         interface Loopback0
          passive
          address-family ipv4 unicast
           metric 10
           prefix-sid index 288
          !
         !
         interface TenGigE0/0/0/0/200
         !
         interface TenGigE0/0/0/0/201
          bfd minimum-interval 250
          bfd multiplier 3
          bfd fast-detect ipv4
          point-to-point
          address-family ipv4 unicast
           metric 10
          !
         !
         interface TenGigE0/0/0/0/202
          bfd minimum-interval 250
          bfd multiplier 3
          bfd fast-detect ipv4
          point-to-point
          address-family ipv4 unicast
           metric 10
          !
         !
         interface HundredGigE0/0/0/100
          bfd minimum-interval 250
          bfd multiplier 3
          bfd fast-detect ipv4
          point-to-point
          address-family ipv4 unicast
           fast-reroute per-prefix
           fast-reroute per-prefix tiebreaker node-protecting index 100
           fast-reroute per-prefix ti-lfa
           metric 10
          !
         !
         interface HundredGigE0/0/0/101
          bfd minimum-interval 250
          bfd multiplier 3
          bfd fast-detect ipv4
          point-to-point
          address-family ipv4 unicast
           fast-reroute per-prefix
           fast-reroute per-prefix tiebreaker node-protecting index 100
           fast-reroute per-prefix ti-lfa
           metric 10
          !
         !
         interface HundredGigE0/0/0/102
          bfd minimum-interval 250
          bfd multiplier 3
          bfd fast-detect ipv4
          point-to-point
          address-family ipv4 unicast
           metric 10
          !
         !
         interface HundredGigE0/0/0/103
          bfd minimum-interval 250
          bfd multiplier 3
          bfd fast-detect ipv4
          point-to-point
          address-family ipv4 unicast
           fast-reroute per-prefix
           fast-reroute per-prefix tiebreaker node-protecting index 100
           fast-reroute per-prefix ti-lfa
           metric 10
          !
         !
         interface HundredGigE0/0/0/104
          bfd minimum-interval 250
          bfd multiplier 3
          bfd fast-detect ipv4
          point-to-point
          address-family ipv4 unicast
           metric 100
          !
         !
         interface HundredGigE0/0/0/105
          bfd minimum-interval 250
          bfd multiplier 3
          bfd fast-detect ipv4
          point-to-point
          address-family ipv4 unicast
           metric 100
          !
         !
         interface HundredGigE0/0/0/106
          bfd minimum-interval 250
          bfd multiplier 3
          bfd fast-detect ipv4
          point-to-point
          address-family ipv4 unicast
           metric 100
          !
         !
         interface HundredGigE0/0/0/107
          bfd minimum-interval 250
          bfd multiplier 3
          bfd fast-detect ipv4
          point-to-point
          address-family ipv4 unicast
           metric 100
          !
         !
         interface HundredGigE0/0/0/108
          bfd minimum-interval 250
          bfd multiplier 3
          bfd fast-detect ipv4
          point-to-point
          address-family ipv4 unicast
           metric 200000
          !
         !
         interface HundredGigE0/0/0/109
          bfd minimum-interval 250
          bfd multiplier 3
          bfd fast-detect ipv4
          point-to-point
          address-family ipv4 unicast
           metric 200000
          !
         !
        !

        RP/0/RP0/CPU0:spine1-tatooine#
    '''}

    def test_show_run_router_isis_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowRunRouterIsis(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_run_router_isis_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowRunRouterIsis(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_run_router_isis_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowRunRouterIsis(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
