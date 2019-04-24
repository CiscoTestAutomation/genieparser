# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

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

    def test_show_run_router_isis_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowRunRouterIsis(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_run_router_isis_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowRunRouterIsis(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
