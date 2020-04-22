
import unittest
import re

from genie.libs.parser.utils.common import (
    _matches_fuzzy_regex, 
    _fuzzy_search_command,
    parser_data
)

class TestFuzzyRegexSearchCommand(unittest.TestCase):
    def test_search_normal_arguments(self):
        for command in parser_data.keys():
            wildcard = re.sub('{.*?}', '---', command)
            search = re.sub('{.*?}', 'argument', command)
            results = _fuzzy_search_command(search, False)
            self.assertEqual(len(results), 1)
            found_command, _, _ = results[0]
            self.assertEqual(re.sub('{.*?}', '---', found_command), wildcard)

    def test_search_normal_arguments_with_regex(self):
        for command, expected_source in parser_data.items(): 
            arguments = re.findall('{(.*?)}', command)
            search = re.escape(re.sub('{.*?}', 'argument', command))
            expected_kwargs = {argument:'argument' for argument in arguments}
            results = _fuzzy_search_command(search, True)
            is_found = False
            for result in results:
                found_command, source, kwargs = result
                if source == expected_source and command == found_command:
                    is_found = True
                    self.assertDictEqual(kwargs, expected_kwargs, search)
                    break
            self.assertTrue(is_found, search)

    def test_special_command(self):
        results = _fuzzy_search_command('/dna/intent/api/v1/interface', False)
        self.assertTrue(len(results), 1)
        self.assertEqual(results[0][0], '/dna/intent/api/v1/interface')

        results = _fuzzy_search_command('/dna/intent/api/v1/interface/argument', False)
        self.assertTrue(len(results), 1)
        self.assertEqual(results[0][0], '/dna/intent/api/v1/interface/{interface}')
        self.assertEqual(results[0][2], {'interface': 'argument'})

        results = _fuzzy_search_command(r'\/dna\/intent\/api\/v1\/interface\/argument', True)
        self.assertTrue(len(results), 1)
        self.assertEqual(results[0][0], '/dna/intent/api/v1/interface/{interface}')
        self.assertEqual(results[0][2], {'interface': 'argument'})

        results = _fuzzy_search_command(r'\/dna\/intent\/api\/v1\/interface', True)
        self.assertTrue(len(results), 1)
        self.assertEqual(results[0][0], '/dna/intent/api/v1/interface')

    def test_matching_simple(self):
        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, 's v'.split(), 'show version', {}, False))
        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, 'sh ver'.split(), 'show version', {}, False))
        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, 'sh ver'.split(), 'show version', {}, False))
        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, 'sh vison'.split(), 'show version', {}, False))

        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, 's v'.split(), 'show version', {}, True))
        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, 'sh ver'.split(), 'show version', {}, True))
        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, 'sh ver'.split(), 'show version', {}, True))
        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, 'sh vison'.split(), 'show version', {}, True))

    def test_matching_arguments(self):
        self.assertEqual(_matches_fuzzy_regex(0, 0, 'sh ver blue'.split(), 'show version {arg}', {}, False)[0], {'arg': 'blue'})
        self.assertEqual(_matches_fuzzy_regex(0, 0, 'sh red blue'.split(), 'show {one} {arg}', {}, False)[0], {'arg': 'blue', 'one': 'red'})
        self.assertEqual(_matches_fuzzy_regex(0, 0, 'sh red blu'.split(), 'show {one} blue', {}, False)[0], {'one': 'red'})

        self.assertEqual(_matches_fuzzy_regex(0, 0, 'sh ver blue'.split(), 'show version {arg}', {}, True)[0], {'arg': 'blue'})
        self.assertEqual(_matches_fuzzy_regex(0, 0, 'sh red blue'.split(), 'show {one} {arg}', {}, True)[0], {'arg': 'blue', 'one': 'red'})
        self.assertEqual(_matches_fuzzy_regex(0, 0, 'sh red blu'.split(), 'show {one} blue', {}, True)[0], {'one': 'red'})

        self.assertEqual(_matches_fuzzy_regex(0, 0, 'sh red blu abc arg bg w w'.split(), 'show {one} blue abc {arg} bgp {a} {b}', {}, False)[0], {'one': 'red', 'arg': 'arg', 'a': 'w', 'b': 'w'})
        self.assertEqual(_matches_fuzzy_regex(0, 0, 'sh red blu abc arg bg w w'.split(), 'show {one} blue abc {arg} bgp {a} {b}', {}, True)[0], {'one': 'red', 'arg': 'arg', 'a': 'w', 'b': 'w'})

    def test_matching_negative(self): 
        self.assertIsNone(_matches_fuzzy_regex(0, 0, 'sh ver blue'.split(), 'show version {arg} {b}', {}, False))
        self.assertIsNone(_matches_fuzzy_regex(0, 0, 'sh ver blue'.split(), 'show version {arg} {b}', {}, True))

        self.assertIsNone(_matches_fuzzy_regex(0, 0, 'show xyz'.split(), 'show version', {}, False))
        self.assertIsNone(_matches_fuzzy_regex(0, 0, 'show xyz'.split(), 'show version', {}, True))

        self.assertIsNone(_matches_fuzzy_regex(0, 0, 'show www xyz'.split(), 'show {b} version', {}, False))
        self.assertIsNone(_matches_fuzzy_regex(0, 0, 'show www xyz'.split(), 'show {b} version', {}, True))

        self.assertIsNone(_matches_fuzzy_regex(0, 0, 'sh bgp ixia inst all all'.split(), 'show bgp instance {instance} all all summary', {}, False))
        self.assertIsNone(_matches_fuzzy_regex(0, 0, 'sh bgp inst all all summary'.split(), 'show bgp instance {instance} all all summary', {}, True))

        self.assertIsNone(_matches_fuzzy_regex(0, 0, 'sh .*'.split(), 'show bgp instance {instance} all all summary', {}, False))
        self.assertIsNone(_matches_fuzzy_regex(0, 0, 'sh .*'.split(), 'show bgp instance {instance} all all summary', {}, True))

        self.assertIsNone(_matches_fuzzy_regex(0, 0, '.*'.split(), 'show bgp instance all all summary', {}, False))
        self.assertIsNone(_matches_fuzzy_regex(0, 0, 'show bgp instance .* all all .*'.split(), 'show bgp instance all all summary', {}, False))

    def test_matching_negative_regex(self):
        self.assertIsNone(_matches_fuzzy_regex(0, 0, 'show a b .*'.split(), 'show a b c d', {}, False))
        self.assertIsNone(_matches_fuzzy_regex(0, 0, 'show a b [a-z] [a-z] [a-z]'.split(), 'show a b c d', {}, True))
        self.assertIsNone(_matches_fuzzy_regex(0, 0, 'show a b .* .* .*'.split(), 'show a b c d', {}, True))
        self.assertIsNone(_matches_fuzzy_regex(0, 0, 'show a b .* f .*'.split(), 'show a b c d', {}, True))
        self.assertIsNone(_matches_fuzzy_regex(0, 0, 'show a b .* .* f'.split(), 'show a b c d', {}, True))
        self.assertIsNone(_matches_fuzzy_regex(0, 0, 'show a b .* m'.split(), 'show a b c d', {}, True))
        self.assertIsNone(_matches_fuzzy_regex(0, 0, 'show a b .* [a-z]'.split(), 'show a b c {ww}', {}, True))
        self.assertIsNone(_matches_fuzzy_regex(0, 0, 'show .*'.split(), 'show a {a} c', {}, True))
        self.assertIsNone(_matches_fuzzy_regex(0, 0, 'show .* a f'.split(), 'show a {a} c', {}, True))
        self.assertIsNone(_matches_fuzzy_regex(0, 0, 'show .* a f .*'.split(), 'show a {a} {d}', {}, True))
        self.assertIsNone(_matches_fuzzy_regex(0, 0, 'show .* a.* c'.split(), 'show a {a} c', {}, True))
        self.assertIsNone(_matches_fuzzy_regex(0, 0, 'show .* a b c'.split(), 'show a b c', {}, True))
        self.assertIsNone(_matches_fuzzy_regex(0, 0, 'a? b c'.split(), 'b c', {}, True))
        self.assertIsNone(_matches_fuzzy_regex(0, 0, 'sh .* inst al [ab]*'.split(), 'show bgp instance all sessions', {}, True))
        self.assertIsNone(_matches_fuzzy_regex(0, 0, 'sh .* inst x [a-z]*'.split(), 'show bgp instance all sessions', {}, True))
        self.assertIsNone(_matches_fuzzy_regex(0, 0, 'show [a-z]*'.split(), 'show a b c d c', {}, True))
        self.assertIsNone(_matches_fuzzy_regex(0, 0, 'show [ab]* ab'.split(), 'show ab', {}, True))

    def test_matching_regex(self):
        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, 'show a b .* c'.split(), 'show a b c d c', {}, True))
        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, 'show .* .* .* .*'.split(), 'show a b c d c', {}, True))
        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, 'show a b .* .* .* .*'.split(), 'show a b c d c abcdef', {}, True))
        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, 'show a.*'.split(), 'show a b c d c', {}, True))
        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, 'show a .* d .*'.split(), 'show a b c d c', {}, True))
        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, 'show a .* d.* c'.split(), 'show a b c d c', {}, True))
        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, '.*'.split(), 'show a b c d c', {}, True))
        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, 'show (a|b) (b|c) .*'.split(), 'show a b c d c', {}, True))
        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, 'show .* d'.split(), 'show a b c d c d', {}, True))
        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, 'show .* a b c d e f g'.split(), 'show a b c d c d a b c d e f g', {}, True))
        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, 'show [ab]* ab'.split(), 'show ab ab', {}, True))
        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, 'show [ab]* ab .* cd'.split(), 'show abababab ab oo cd', {}, True))
        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, 'a? b c'.split(), 'a b c', {}, True))
        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, 'a b [a-z] d'.split(), 'a b c d', {}, True))

        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, 'sh ver .*'.split(), 'show version abc def', {}, True))
        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, 'sh ver .* int'.split(), 'show version abc def interface', {}, True))
        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, 'sh ver .* int b .* wwx'.split(), 'show version abc def interface bgp mb wwx', {}, True))
        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, 'sh .* inst al sess'.split(), 'show bgp instance all sessions', {}, True))
        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, 'sh .* inst al [a-z]*'.split(), 'show bgp instance all sessions', {}, True))
        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, 'sh .* inst.*'.split(), 'show bgp instance all sessions', {}, True))

        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, 'sh .* inst.*'.split(), 'show bgp instance all sessions', {}, True))
        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, 'sh .* inst.*'.split(), 'show bgp instance all sessions', {}, True))

    def test_matching_regex_arguments(self):
        self.assertEqual(_matches_fuzzy_regex(0, 0, 'sh ver .* blue'.split(), 'show version wx abc {arg}', {}, True)[0], {'arg': 'blue'})
        self.assertEqual(_matches_fuzzy_regex(0, 0, 'sh a .* b .*c c'.split(), 'show {a} wx {b} abc {c}', {}, True)[0], {'a': 'a', 'b': 'b', 'c': 'c'})
        self.assertEqual(_matches_fuzzy_regex(0, 0, 'sh .* a b c'.split(), 'show version wx abc {a} {b} {c}', {}, True)[0], {'a': 'a', 'b': 'b', 'c': 'c'})
        self.assertEqual(_matches_fuzzy_regex(0, 0, 'sh .* a b c c'.split(), 'show version wx abc {a} {b} {c} c', {}, True)[0], {'a': 'a', 'b': 'b', 'c': 'c'})
        self.assertEqual(_matches_fuzzy_regex(0, 0, 'sh .* a b c c.* f'.split(), 'show version wx abc {a} {b} {c} c d {f}', {}, True)[0], {'a': 'a', 'b': 'b', 'c': 'c', 'f': 'f'})

    def test_extra_spaces(self):
        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, '   show    show  show     '.split(), 'show show show', {}, False))
        self.assertIsNotNone(_matches_fuzzy_regex(0, 0, '   show    .*  show     '.split(), 'show a show', {}, True))
        self.assertEqual(_fuzzy_search_command(' s  e ipv6   n  d', False)[0][0], 'show eigrp ipv6 neighbors detail')

    def test_simple_fuzzy_search(self):
        self.assertEqual([i[0] for i in _fuzzy_search_command('sh ver', False)], ['show version'])
        self.assertEqual([i[0] for i in _fuzzy_search_command('ps -', False)], ['ps -ef']) #BUG should be p -
        self.assertEqual([i[0] for i in _fuzzy_search_command('sh ms int', False)], ['show mpls interfaces'])
        self.assertEqual([i[0] for i in _fuzzy_search_command('sh run int x', False)], ['show running-config interface {interface}'])
        self.assertEqual([i[0] for i in _fuzzy_search_command('s b i w x y a sum', False)], ['show bgp instance {instance} {vrf_type} {vrf} {address_family} summary'])
        self.assertEqual([i[0] for i in _fuzzy_search_command('sh l2vn for bridge-domain r address loc x', False)], ['show l2vpn forwarding bridge-domain {bridge_domain} mac-address location {location}'])
        self.assertEqual([i[0] for i in _fuzzy_search_command('s bundle', False)], ['show bundle'])
        self.assertEqual([i[0] for i in _fuzzy_search_command('sh en int-label det loc x', False)], ['show evpn internal-label detail location {location}'])
        self.assertEqual([i[0] for i in _fuzzy_search_command('sh l2 mac-learning type al loc wee', False)], ['show l2vpn mac-learning {mac_type} all location {location}'])
        self.assertEqual([i[0] for i in _fuzzy_search_command('/dna', False)], ['/dna/intent/api/v1/interface'])
        self.assertEqual([i[0] for i in _fuzzy_search_command('sh l ent *', False)], ['show lldp entry *'])
        self.assertEqual([i[0] for i in _fuzzy_search_command('sh run f | i af-group', False)], ['show run formal | i af-group'])
        self.assertEqual([i[0] for i in _fuzzy_search_command('sh r ip4 abc', False)], ['show route ipv4 {protocol}'])

    def test_simple_fuzzy_search_regex(self):
        self.assertEqual([i[0] for i in _fuzzy_search_command('sh r ip4 abc', True)], ['show route ipv4 {protocol}', 'show route ipv4 {route}'])
        self.assertEqual([i[0] for i in _fuzzy_search_command('sh run x .*', True)], ["show running-config {pim} | sec '^i'"])
        self.assertEqual([i[0] for i in _fuzzy_search_command('sh .* inst w ser c .* m', True)], ["show lisp all instance-id {instance_id} service {service} rloc members"])
    
    def test_prefix_single_character_search(self):
        self.assertEqual(_fuzzy_search_command('s e ipv6 n d', False)[0][0], 'show eigrp ipv6 neighbors detail')
        self.assertEqual(_fuzzy_search_command('s e e p', False)[0][0], 'show evpn ethernet-segment private')

    def test_prefix_single_character_search_regex(self):
        self.assertEqual(_fuzzy_search_command('s e ipv6 n d', True)[0][0], 'show eigrp ipv6 neighbors detail')
        self.assertEqual(_fuzzy_search_command('s e e p', True)[0][0], 'show evpn ethernet-segment private')
        self.assertEqual(len(_fuzzy_search_command('s e (ipv4|ipv6) n d', True)), 2)
        self.assertEqual(len(_fuzzy_search_command('s e .* p', True)), 2)

    def test_negative_prefix_search(self):
        self.assertEqual(_fuzzy_search_command('s e e x w p', True), [])
        self.assertEqual(_fuzzy_search_command('s e e x w p .*', True), [])
        self.assertEqual(_fuzzy_search_command('swp .* wx ww abc adc b', True), [])
        self.assertEqual(_fuzzy_search_command('s e e x w p', False), [])
        self.assertEqual(_fuzzy_search_command('s e e x w p .*', False), [])
        self.assertEqual(_fuzzy_search_command('swp .* wx', False), [])

    def test_regex_escaped_arguments(self):
        result = _fuzzy_search_command('sh bridge-domain 1.1.1.1.1', False)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], 'show bridge-domain {bd_id}')
        self.assertEqual(result[0][2], {'bd_id': '1.1.1.1.1'})

        result = _fuzzy_search_command(r'sh bridge\-domain 1\.1\.1\.1\.1', True)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], 'show bridge-domain {bd_id}')
        self.assertEqual(result[0][2], {'bd_id': '1.1.1.1.1'})

        result = _fuzzy_search_command(r'sh b.*-.*n 1\.1\.1\.1\.1', True)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], 'show bridge-domain {bd_id}')
        self.assertEqual(result[0][2], {'bd_id': '1.1.1.1.1'})

    def test_escaped_characters(self):
        result = _fuzzy_search_command(r'sh ll en \*', True)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], 'show lldp entry *')

        result = _fuzzy_search_command('p \\-', True)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], 'ps -ef')

        result = _fuzzy_search_command(re.escape('/dna'), True)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], '/dna/intent/api/v1/interface')

        result = _fuzzy_search_command(r'sh form s proc slot switch act R monitor \| inc Mem :\|Swap:', True)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], 'show platform software process slot switch active R0 monitor | inc Mem :|Swap:')
        
        result = _fuzzy_search_command(re.escape('vs -c "show plat internal hal policy red group_id id id src_ip 1.1.1.1 dst_ip dst protocol prt"'), True)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], 'vsh_lc -c "show platform internal hal policy redirdst group_id {group_id} {address_family} src_ip {src_ip} dst_ip {dst_ip} protocol {protocol}"')
        self.assertEqual(result[0][2], {'group_id': 'id', 'address_family': 'id', 'src_ip': '1.1.1.1', 'dst_ip': 'dst', 'protocol': 'prt'})

    def test_ambiguous_search(self):
        with self.assertRaises(Exception):
            _fuzzy_search_command('s p', False)

        with self.assertRaises(Exception):
            _fuzzy_search_command('sh c', False)

if __name__ == '__main__':
    unittest.main()
