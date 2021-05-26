import logging
import unittest
import re

from genie.libs.parser.utils import common

class TestFuzzyRegexSearchCommand(unittest.TestCase):
    
    def setUp(self):
        try:
            del common.parser_data
        except AttributeError as err:
            logging.warning(err)
    
    def test_search_normal_arguments(self):
        
        with self.assertRaises(AttributeError):
            getattr(common, "parser_data")
        
        common._load_parser_json()
        getattr(common, "parser_data")
        
        for command in common.parser_data.keys():
            wildcard = re.sub('{.*?}', '---', command)
            search = re.sub('{.*?}', 'argument', command)
            results = common._fuzzy_search_command(search, False)
            self.assertEqual(len(results), 1)
            found_command, _, _ = results[0]
            self.assertEqual(re.sub('{.*?}', '---', found_command), wildcard)

    def test_search_normal_arguments_with_regex(self):
        
        with self.assertRaises(AttributeError):
            getattr(common, "parser_data")
        
        common._load_parser_json()
        getattr(common, "parser_data")
        
        for command, expected_source in common.parser_data.items(): 
            arguments = re.findall('{(.*?)}', command)
            search = re.escape(re.sub('{.*?}', 'argument', command))
            expected_kwargs = {argument:'argument' for argument in arguments}            
            results = common._fuzzy_search_command(search, True)
            is_found = False
            
            for result in results:
                found_command, source, kwargs = result
                if source == expected_source and command == found_command:
                    is_found = True
                    self.assertDictEqual(kwargs, expected_kwargs, search)
                    break
                
            self.assertTrue(is_found, search)

    def test_special_command(self):
        results = common._fuzzy_search_command('/dna/intent/api/v1/interface', False)
        self.assertTrue(len(results), 1)
        self.assertEqual(results[0][0], '/dna/intent/api/v1/interface')

        results = common._fuzzy_search_command('/dna/intent/api/v1/interface/argument',
                                                                        False)
        self.assertTrue(len(results), 1)
        self.assertEqual(results[0][0], 
                                    '/dna/intent/api/v1/interface/{interface}')
        self.assertEqual(results[0][2], {'interface': 'argument'})

        results = common._fuzzy_search_command(
                        r'\/dna\/intent\/api\/v1\/interface\/argument', True)
        self.assertTrue(len(results), 1)
        self.assertEqual(results[0][0], 
                                    '/dna/intent/api/v1/interface/{interface}')
        self.assertEqual(results[0][2], {'interface': 'argument'})

        results = common._fuzzy_search_command(
                                    r'\/dna\/intent\/api\/v1\/interface', True)
        self.assertTrue(len(results), 1)
        self.assertEqual(results[0][0], '/dna/intent/api/v1/interface')

    def test_matching_simple(self):
        self.assertIsNotNone(common._matches_fuzzy(0, 0, 's v'.split(), 
                                                    'show version', {}, False))
        self.assertIsNotNone(common._matches_fuzzy(0, 0, 'sh ver'.split(), 
                                                    'show version', {}, False))
        self.assertIsNotNone(common._matches_fuzzy(0, 0, 'show vers'.split(), 
                                                    'show version', {}, False))
        self.assertIsNotNone(common._matches_fuzzy(0, 0, 'sh version'.split(), 
                                                    'show version', {}, False))

        self.assertIsNotNone(common._matches_fuzzy(0, 0, 's v'.split(), 
                                                    'show version', {}, True))
        self.assertIsNotNone(common._matches_fuzzy(0, 0, 'sh ver'.split(), 
                                                    'show version', {}, True))
        self.assertIsNotNone(common._matches_fuzzy(0, 0, 'show vers'.split(), 
                                                    'show version', {}, True))
        self.assertIsNotNone(common._matches_fuzzy(0, 0, 'sh version'.split(), 
                                                    'show version', {}, True))

    def test_matching_arguments(self):
        self.assertEqual(common._matches_fuzzy(0, 0, 'sh ver blue'.split(),
                        'show version {arg}', {}, False)[0], {'arg': 'blue'})
        self.assertEqual(common._matches_fuzzy(0, 0, 'sh red blue'.split(),
            'show {one} {arg}', {}, False)[0], {'arg': 'blue', 'one': 'red'})
        self.assertEqual(common._matches_fuzzy(0, 0, 'sh red blu'.split(), 
                        'show {one} blue', {}, False)[0], {'one': 'red'})

        self.assertEqual(common._matches_fuzzy(0, 0, 'sh ver blue'.split(), 
                            'show version {arg}', {}, True)[0], {'arg': 'blue'})
        self.assertEqual(common._matches_fuzzy(0, 0, 'sh red blue'.split(), 
                'show {one} {arg}', {}, True)[0], {'arg': 'blue', 'one': 'red'})
        self.assertEqual(common._matches_fuzzy(0, 0, 'sh red blu'.split(), 
                                'show {one} blue', {}, True)[0], {'one': 'red'})

        self.assertEqual(common._matches_fuzzy(0, 0, 
                                         'sh red blu abc arg bg w w'.split(), 
                        'show {one} blue abc {arg} bgp {a} {b}', {}, False)[0], 
                            {'one': 'red', 'arg': 'arg', 'a': 'w', 'b': 'w'})
        self.assertEqual(common._matches_fuzzy(0, 0, 
                                            'sh red blu abc arg bg w w'.split(), 
                        'show {one} blue abc {arg} bgp {a} {b}', {}, True)[0], 
                            {'one': 'red', 'arg': 'arg', 'a': 'w', 'b': 'w'})

    def test_matching_negative(self): 
        self.assertIsNone(common._matches_fuzzy(0, 0, 'sh ver blue'.split(), 
                                        'show version {arg} {b}', {}, False))
        self.assertIsNone(common._matches_fuzzy(0, 0, 'sh ver blue'.split(), 
                                        'show version {arg} {b}', {}, True))

        self.assertIsNone(common._matches_fuzzy(0, 0, 'show xyz'.split(), 
                                                    'show version', {}, False))
        self.assertIsNone(common._matches_fuzzy(0, 0, 'show xyz'.split(), 
                                                    'show version', {}, True))

        self.assertIsNone(common._matches_fuzzy(0, 0, 'show www xyz'.split(), 
                                                'show {b} version', {}, False))
        self.assertIsNone(common._matches_fuzzy(0, 0, 'show www xyz'.split(), 
                                                'show {b} version', {}, True))

        self.assertIsNone(common._matches_fuzzy(0, 0, 
                                            'sh bgp ixia inst all all'.split(), 
                    'show bgp instance {instance} all all summary', {}, False))
        self.assertIsNone(common._matches_fuzzy(0, 0, 
                                        'sh bgp inst all all summary'.split(), 
                    'show bgp instance {instance} all all summary', {}, True))

        self.assertIsNone(common._matches_fuzzy(0, 0, 'sh .*'.split(), 
                    'show bgp instance {instance} all all summary', {}, False))
        self.assertIsNone(common._matches_fuzzy(0, 0, 'sh .*'.split(), 
                    'show bgp instance {instance} all all summary', {}, True))

        self.assertIsNone(common._matches_fuzzy(0, 0, '.*'.split(), 
                                'show bgp instance all all summary', {}, False))
        self.assertIsNone(common._matches_fuzzy(0, 0, 
                                    'show bgp instance .* all all .*'.split(),
                                'show bgp instance all all summary', {}, False))
        
        self.assertIsNone(common._matches_fuzzy(0, 0, 
                            'show abb ab'.split(), 'show abc ab', {}, False))
        self.assertIsNone(common._matches_fuzzy(0, 0, 
                                'ow abc ab'.split(), 'show abc ab', {}, False))

        self.assertIsNone(common._matches_fuzzy(0, 0, 
                            'show abb ab xd'.split(), 'show {ww}', {}, False))
        self.assertIsNone(common._matches_fuzzy(0, 0, 
                    'show show x abb ab xd'.split(), '{x} abb {wx}', {}, False))

    def test_matching_negative_regex(self):
        self.assertIsNone(common._matches_fuzzy(0, 0, 
                            'show a b .*'.split(), 'show a b c d', {}, False))
        self.assertIsNone(common._matches_fuzzy(0, 0, 
                'show a b [a-z] [a-z] [a-z]'.split(), 'show a b c d', {}, True))
        self.assertIsNone(common._matches_fuzzy(0, 0, 
                        'show a b .* .* .*'.split(), 'show a b c d', {}, True))
        self.assertIsNone(common._matches_fuzzy(0, 0, 
                        'show a b .* f .*'.split(), 'show a b c d', {}, True))
        self.assertIsNone(common._matches_fuzzy(0, 0, 
                        'show a b .* .* f'.split(), 'show a b c d', {}, True))
        self.assertIsNone(common._matches_fuzzy(0, 0, 
                            'show a b .* m'.split(), 'show a b c d', {}, True))
        self.assertIsNone(common._matches_fuzzy(0, 0, 
                    'show a b .* [a-z]'.split(), 'show a b c {ww}', {}, True))
        self.assertIsNone(common._matches_fuzzy(0, 0, 
                                'show .*'.split(), 'show a {a} c', {}, True))
        self.assertIsNone(common._matches_fuzzy(0, 0, 'show .* a f'.split(), 
                                                    'show a {a} c', {}, True))
        self.assertIsNone(common._matches_fuzzy(0, 0, 'show .* a f .*'.split(), 
                                                'show a {vrf} {vrf}', {}, True))
        self.assertIsNone(common._matches_fuzzy(0, 0, 'show .* a.* c'.split(), 
                                                    'show a {a} c', {}, True))
        self.assertIsNone(common._matches_fuzzy(0, 0, 'show .* a b c'.split(), 
                                                     'show a b c', {}, True))
        self.assertIsNone(common._matches_fuzzy(0, 0, 'a? b c'.split(), 
                                                             'b c', {}, True))
        self.assertIsNone(common._matches_fuzzy(0, 0, 'sh .* inst al [ab]*'.split(), 
                                    'show bgp instance all sessions', {}, True))
        self.assertIsNone(common._matches_fuzzy(0, 0, 'sh .* inst x [a-z]*'.split(), 
                                    'show bgp instance all sessions', {}, True))
        self.assertIsNone(common._matches_fuzzy(0, 0, 'show [a-z]*'.split(), 
                                                    'show a b c d c', {}, True))
        self.assertIsNone(common._matches_fuzzy(0, 0, 'show [ab]* ab'.split(), 
                                                        'show ab', {}, True))
        self.assertIsNone(common._matches_fuzzy(0, 0, 'show ac ab .*'.split(), 
                                                    'show abc ab c', {}, True))

    def test_matching_regex(self):
        self.assertIsNotNone(common._matches_fuzzy(0, 0, 'show a b .* c'.split(), 
                                                    'show a b c d c', {}, True))
        self.assertIsNotNone(common._matches_fuzzy(0, 0, 'show .* .* .* .*'.split(), 
                                                    'show a b c d c', {}, True))
        self.assertIsNotNone(common._matches_fuzzy(0, 0, 
            'show a b .* .* .* .*'.split(), 'show a b c d c abcdef', {}, True))
        self.assertIsNotNone(common._matches_fuzzy(0, 0, 'show a.*'.split(), 
                                                    'show a b c d c', {}, True))
        self.assertIsNotNone(common._matches_fuzzy(0, 0, 'show a .* d .*'.split(), 
                                                    'show a b c d c', {}, True))
        self.assertIsNotNone(common._matches_fuzzy(0, 0, 'show a .* d.* c'.split(), 
                                                    'show a b c d c', {}, True))
        self.assertIsNotNone(common._matches_fuzzy(0, 0, '.*'.split(), 
                                                    'show a b c d c', {}, True))
        self.assertIsNotNone(common._matches_fuzzy(0, 0, 'show (a|b) (b|c) .*'.split(), 
                                                    'show a b c d c', {}, True))
        self.assertIsNotNone(common._matches_fuzzy(0, 0, 'show .* d'.split(), 
                                                'show a b c d c d', {}, True))
        self.assertIsNotNone(common._matches_fuzzy(0, 0, 
                                                'show .* a b c d e f g'.split(), 
                                    'show a b c d c d a b c d e f g', {}, True))
        self.assertIsNotNone(common._matches_fuzzy(0, 0, 'show [ab]* ab'.split(), 
                                                        'show ab ab', {}, True))
        self.assertIsNotNone(common._matches_fuzzy(0, 0, 'show [ab]* ab .* cd'.split(),    
                                            'show abababab ab oo cd', {}, True))
        self.assertIsNotNone(common._matches_fuzzy(0, 0, 'a? b c'.split(), 
                                                            'a b c', {}, True))
        self.assertIsNotNone(common._matches_fuzzy(0, 0, 'a b [a-z] d'.split(), 
                                                        'a b c d', {}, True))

        self.assertIsNotNone(common._matches_fuzzy(0, 0, 'sh ver .*'.split(), 
                                            'show version abc def', {}, True))
        self.assertIsNotNone(common._matches_fuzzy(0, 0, 'sh ver .* int'.split(), 
                                    'show version abc def interface', {}, True))
        self.assertIsNotNone(common._matches_fuzzy(0, 0, 
                                            'sh ver .* int b .* wwx'.split(), 
                        'show version abc def interface bgp mb wwx', {}, True))
        self.assertIsNotNone(common._matches_fuzzy(0, 0, 'sh .* inst al sess'.split(), 
                                    'show bgp instance all sessions', {}, True))
        self.assertIsNotNone(common._matches_fuzzy(0, 0, 
                                                'sh .* inst al [a-z]*'.split(), 
                                    'show bgp instance all sessions', {}, True))
        self.assertIsNotNone(common._matches_fuzzy(0, 0, 'sh .* inst.*'.split(), 
                                    'show bgp instance all sessions', {}, True))

        self.assertIsNotNone(common._matches_fuzzy(0, 0, 'sh .* inst.*'.split(), 
                                    'show bgp instance all sessions', {}, True))
        self.assertIsNotNone(common._matches_fuzzy(0, 0, 'sh .* inst.*'.split(), 
                                    'show bgp instance all sessions', {}, True))

    def test_matching_regex_arguments(self):
        self.assertEqual(common._matches_fuzzy(0, 0, 'sh ver .* blue'.split(), 
                    'show version wx abc {arg}', {}, True)[0], {'arg': 'blue'})
        self.assertEqual(common._matches_fuzzy(0, 0, 'sh a .* b .*c c'.split(), 
                                        'show {a} wx {b} abc {c}', {}, True)[0],
                                                {'a': 'a', 'b': 'b', 'c': 'c'})
        self.assertEqual(common._matches_fuzzy(0, 0, 'sh .* a b c'.split(), 
        'show version wx abc {a} {b} {c}', {}, True)[0], 
                                                {'a': 'a', 'b': 'b', 'c': 'c'})
        self.assertEqual(common._matches_fuzzy(0, 0, 'sh .* a b c c'.split(), 
                            'show version wx abc {a} {b} {c} c', {}, True)[0], 
                                                {'a': 'a', 'b': 'b', 'c': 'c'})
        self.assertEqual(common._matches_fuzzy(0, 0, 'sh .* a b c c.* f'.split(), 
                    'show version wx abc {a} {b} {c} c d {f}', {}, True)[0], 
                                    {'a': 'a', 'b': 'b', 'c': 'c', 'f': 'f'})

    def test_extra_spaces(self):
        self.assertIsNotNone(common._matches_fuzzy(0, 0, 
            '   show    show  show     '.split(), 'show show show', {}, False))
        self.assertIsNotNone(common._matches_fuzzy(0, 0, 
                '   show    .*  show     '.split(), 'show a show', {}, True))
        self.assertEqual(common._fuzzy_search_command(
                                            ' s  e ipv6   n  d', False)[0][0], 
                                            'show eigrp ipv6 neighbors detail')

    def test_simple_fuzzy_search(self):
        self.assertEqual([i[0] for i in 
                    common._fuzzy_search_command('sh ver', False)], ['show version'])
        self.assertEqual([i[0] for i in 
                            common._fuzzy_search_command('p -ef', False)], ['ps -ef'])
        self.assertEqual([i[0] for i in 
                        common._fuzzy_search_command('sh mp int', False)], 
                                                    ['show mpls interfaces'])
        self.assertEqual([i[0] for i in common._fuzzy_search_command(
                                                        'sh run int x', False)], 
                                ['show running-config interface {interface}'])
        self.assertEqual([i[0] for i in common._fuzzy_search_command(
            's b i w x y a sum', False)], 
            ['show bgp instance {instance} {vrf_type} {vrf} {address_family}' +
                                                                    ' summary'])
        self.assertEqual([i[0] for i in common._fuzzy_search_command(
            'sh l2v for bridge-domain r mac loc x', False)], 
            ['show l2vpn forwarding bridge-domain {bridge_domain} mac-address' +
                                                        ' location {location}'])
        self.assertEqual([i[0] for i in common._fuzzy_search_command(
                                        's bundle', False)], ['show bundle'])
        self.assertEqual([i[0] for i in common._fuzzy_search_command(
                                                'sh e int det loc x', False)], 
                        ['show evpn internal-label detail location {location}'])
        self.assertEqual([i[0] for i in common._fuzzy_search_command(
                                'sh l2 mac-learning type al loc wee', False)], 
                ['show l2vpn mac-learning {mac_type} all location {location}'])
        self.assertEqual([i[0] for i in common._fuzzy_search_command(
                            '/dna', False)], ['/dna/intent/api/v1/interface'])
        self.assertEqual([i[0] for i in common._fuzzy_search_command(
                                'sh l ent *', False)], ['show lldp entry *'])
        self.assertEqual([i[0] for i in common._fuzzy_search_command(
            'sh run f | i af-group', False)], ['show run formal | i af-group'])
        self.assertEqual([i[0] for i in common._fuzzy_search_command(
                    'sh r ipv4 abc', False)], ['show route ipv4 {protocol}'])

    def test_simple_fuzzy_search_regex(self):
        self.assertEqual([i[0] for i in common._fuzzy_search_command('sh r ipv4 abc', 
            True)], ['show route ipv4 {protocol}', 'show route ipv4 {route}'])
        self.assertEqual([i[0] for i in common._fuzzy_search_command('sh run x .*', 
                            True)], ["show running-config {pim} | sec '^i'"])
        self.assertEqual([i[0] for i in common._fuzzy_search_command(
            'sh .* inst w ser c .* m', True)], 
            ["show lisp all instance-id {instance_id} service" + 
             " {service} rloc members"])
        self.assertEqual([i[0] for i in common._fuzzy_search_command('sh run int x', 
                        True)], ['show running-config interface {interface}'])
        self.assertEqual([i[0] for i in common._fuzzy_search_command(
            's b i w x y a sum', True)], [
                'show bgp instance {instance}' +
                ' {vrf_type} {vrf} {address_family} summary'])
        self.assertEqual([i[0] for i in common._fuzzy_search_command(
            'sh l2v for bridge-domain r mac loc x', True)], 
            ['show l2vpn forwarding bridge-domain ' + 
             '{bridge_domain} mac-address location {location}'])
        self.assertEqual([i[0] for i in common._fuzzy_search_command('s bundle',
                                                     True)], ['show bundle'])
        self.assertEqual([i[0] for i in common._fuzzy_search_command(
            'sh e int det loc x', True)], 
            ['show evpn internal-label detail location {location}'])
        self.assertEqual([i[0] for i in common._fuzzy_search_command(
            'sh l2 mac-learning type al loc wee', True)], 
            ['show l2vpn mac-learning {mac_type} all location {location}'])
        self.assertEqual([i[0] for i in common._fuzzy_search_command('\/dna', True)],
                                            ['/dna/intent/api/v1/interface'])
    
    def test_prefix_single_character_search(self):
        self.assertEqual(common._fuzzy_search_command('s e ipv6 n d', False)[0][0], 
                                            'show eigrp ipv6 neighbors detail')
        self.assertEqual(common._fuzzy_search_command('s e e p', False)[0][0], 
                                        'show evpn ethernet-segment private')

    def test_prefix_single_character_search_regex(self):
        self.assertEqual(common._fuzzy_search_command('s e ipv6 n d', True)[0][0], 
                                            'show eigrp ipv6 neighbors detail')
        self.assertEqual(common._fuzzy_search_command('s e e p', True)[0][0], 
                                        'show evpn ethernet-segment private')
        self.assertEqual(len(common._fuzzy_search_command('s e (ipv4|ipv6) n d',
                                                                    True)), 2)
        self.assertEqual(len(common._fuzzy_search_command('s e \| .* p', True)), 1)

    def test_negative_prefix_search(self):
        self.assertEqual(common._fuzzy_search_command('s e e x w p', True), [])
        self.assertEqual(common._fuzzy_search_command('s e e x w p .*', True), [])
        self.assertEqual(common._fuzzy_search_command('swp .* wx ww abc adc b', True), 
                                                                            [])
        self.assertEqual(common._fuzzy_search_command('s e e x w p', False), [])
        self.assertEqual(common._fuzzy_search_command('s e e x w p .*', False), [])
        self.assertEqual(common._fuzzy_search_command('swp .* wx', False), [])

    def test_regex_escaped_arguments(self):
        result = common._fuzzy_search_command('sh bridge-domain 1.1.1.1.1', False)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], 'show bridge-domain {bd_id}')
        self.assertEqual(result[0][2], {'bd_id': '1.1.1.1.1'})

        result = common._fuzzy_search_command(r'sh bridge\-domain 1\.1\.1\.1\.1', True)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], 'show bridge-domain {bd_id}')
        self.assertEqual(result[0][2], {'bd_id': '1.1.1.1.1'})

        result = common._fuzzy_search_command(r'sh b.*-.*n 1\.1\.1\.1\.1', True)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], 'show bridge-domain {bd_id}')
        self.assertEqual(result[0][2], {'bd_id': '1.1.1.1.1'})

    def test_escaped_characters(self):
        result = common._fuzzy_search_command(r'sh ll en \*', True)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], 'show lldp entry *')

        result = common._fuzzy_search_command('p \\-ef', True)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], 'ps -ef')

        result = common._fuzzy_search_command(re.escape('/dna'), True)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], '/dna/intent/api/v1/interface')

        result = common._fuzzy_search_command(r'sh plat s proc slot switch act R' +
                                        ' monitor \| inc Mem :\|Swap:', True)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], 'show platform software process slot ' +
                                'switch active R0 monitor | inc Mem :|Swap:')
        
        result = common._fuzzy_search_command(re.escape('vs -c "show plat internal' + 
                    ' hal policy red group_id id id src_ip 10.4.1.1 dst_ip ' + 
                    'dst protocol prt"'), True)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], 'vsh_lc -c "show platform internal hal' +
                    ' policy redirdst group_id {group_id} {address_family}' +
                    ' src_ip {src_ip} dst_ip {dst_ip} protocol {protocol}"')
        self.assertEqual(result[0][2], {'group_id': 'id', 'address_family': 
                'id', 'src_ip': '10.4.1.1', 'dst_ip': 'dst', 'protocol': 'prt'})

    def test_ambiguous_search(self):
        with self.assertRaises(Exception):
            common._fuzzy_search_command('s p', False)

        with self.assertRaises(Exception):
            common._fuzzy_search_command('sh c', False)

        with self.assertRaises(Exception):
            common._fuzzy_search_command('s i r', False)

    def test_single_argument(self):
        self.assertEqual(common._matches_fuzzy(0, 0, 'a b c d'.split(), 
                                    'a b c {vrf}', {}, True)[0], {'vrf': 'd'})
        self.assertEqual(common._matches_fuzzy(0, 0, 'a b c d'.split(), 
                                    'a {vrf} c d', {}, True)[0], {'vrf': 'b'})
        self.assertEqual(common._matches_fuzzy(0, 0, 'a b c d'.split(), 
                                    '{vrf} b {rd} {instance}', {}, True)[0], 
                                    {'vrf': 'a', 'rd': 'c', 'instance': 'd'})
        self.assertEqual(common._matches_fuzzy(0, 0, 'abc .* bdc ef'.split(), 
                        'abcd www www {vrf} ef', {}, True)[0], {'vrf': 'bdc'})
        self.assertEqual(common._matches_fuzzy(0, 0, 'a .* w .* p .* v'.split(), 
                            'a b c {vrf} e f {instance} h v', {}, True)[0], 
                                                {'vrf': 'w', 'instance': 'p'})
        self.assertEqual(common._matches_fuzzy(0, 0, 'abc fileA fileB'.split(), 
                            'abcdef {fileA} {fileB}', {}, True)[0], 
                                        {'fileA': 'fileA', 'fileB': 'fileB'})

    def test_double_argument(self):
        self.assertEqual(common._matches_fuzzy(0, 0, 'a b c d'.split(), 
                                    'a b c {w}', {}, True)[0], {'w': 'd'})
        self.assertEqual(common._matches_fuzzy(0, 0, 'a b c d e'.split(), 
                                    'a b c {w}', {}, True)[0], {'w': 'd e'})
        self.assertEqual(common._matches_fuzzy(0, 0, 's b vpnv4 unicast a s'.split(), 
                            'show bgp {stuff} all summary', {}, True)[0], 
                                        {'stuff': 'vpnv4 unicast'})
        self.assertEqual(common._matches_fuzzy(0, 0, 'a a b b'.split(), 
                            '{a} {b}', {}, True)[0], {'a': 'a a', 'b': 'b b'})
        self.assertEqual(common._matches_fuzzy(0, 0, 'w x y z z'.split(), 
                    'w x y {a} {vrf}', {}, True)[0], {'a': 'z', 'vrf': 'z'})
        self.assertEqual(common._matches_fuzzy(0, 0, 'w x y z z z'.split(), 
                    'w x y {a} {vrf}', {}, True)[0], {'a': 'z z', 'vrf': 'z'})
        self.assertEqual(common._matches_fuzzy(0, 0, 'w x y a b c'.split(), 
                    'w x y {a} {b} {c}', {}, True)[0], 
                                                {'a': 'a', 'b': 'b', 'c': 'c'})
    
    def test_resolve_argument(self):
        result = common._fuzzy_search_command('show ip prefix-list detail', False)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], 'show {af} prefix-list detail')
    
        result = common._fuzzy_search_command('show ipv6 prefix-list detail', True)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], 'show ipv6 prefix-list detail')

if __name__ == '__main__':
    unittest.main()
