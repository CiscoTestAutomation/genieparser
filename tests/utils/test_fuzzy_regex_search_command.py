
import unittest
import re

from genie.libs.parser.utils.common import (
    _matches_fuzzy_regex, 
    _fuzzy_search_command,
    parser_data
)

class TestFuzzyRegexSearchCommand(unittest.TestCase):
    def test_search_normal_arguments(self):
        for command, expected_source in parser_data.items(): 
            arguments = re.findall('{(.*?)}', command)
            search = re.sub('{.*?}', 'argument', command)
            expected_kwargs = {argument:'argument' for argument in arguments}
            results = _fuzzy_search_command(search, False)
            is_found = False
            for result in results:
                found_command, source, kwargs = result
                if source == expected_source and command == found_command:
                    is_found = True
                    self.assertDictEqual(kwargs, expected_kwargs, search)
            self.assertTrue(is_found)

    def test_search_normal_arguments_with_regex(self):
        for command, expected_source in parser_data.items(): 
            arguments = re.findall('{(.*?)}', command)
            search = re.sub('{.*?}', 'argument', command)
            expected_kwargs = {argument:'argument' for argument in arguments}
            results = _fuzzy_search_command(search, True)
            is_found = False
            for result in results:
                found_command, source, kwargs = result
                if source == expected_source and command == found_command:
                    is_found = True
                    self.assertDictEqual(kwargs, expected_kwargs, search)
            self.assertTrue(is_found)

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

if __name__ == '__main__':
    #print(_fuzzy_search_command('/dna/intent/api/v1/interface', False))

    #results = _fuzzy_search_command('\/dna\/intent\/api\/v1\/interface\/argument', True)
    #exit()
    # unittest.main() 
    # exit()
    # print(_fuzzy_search_command('\/dna\/intent\/api\/v1\/interface\/apcd', True)[0][0])
    # exit()

    print([[*x] for x in _fuzzy_search_command(re.escape("show route ipv4 abc"), True)])

    exit()
    for command, expected_source in parser_data.items(): 
        if command.startswith('/mgmt'):
            continue
        print('running command: ' + command)
        arguments = re.findall('{(.*?)}', command)
        search = re.escape(re.sub('{.*?}', 'argument', command))
        expected_kwargs = {argument:'argument' for argument in arguments}
        #results = _fuzzy_search_command(search)
        try:
            results = _fuzzy_search_command(search, True)
        except SystemExit:
            print(command)
            exit()
        # cmd, _, _ = results
        # if cmd != command:
        #     raise Exception(cmd + '|' + command)
        if len(results) > 1:
            print()
            print()
            print("Searching For: " + command)
            print("====================")
            print("Found:")
            for s, _, _ in results:
                print(s)
            print('====================')
        
        if not command in set(result for result, _, _ in results):
            print('search: ' + search)
            print('---------------')
            for s, _, _ in results:
                print(s)
            raise Exception(command)
    #_fuzzy_search_command('show access-lists wjosf', False)
    
    # print("started")
    # count = 0

    # for command in parser_data.keys(): 
    #     arguments = re.findall('{(.*?)}', command)
    #     command = re.sub('{.*?}', 'argument', command)
    #     expected_kwargs = {argument:'argument' for argument in arguments}
    #     results = _fuzzy_search_command(command, False)
    #     if len(results) != 1:
    #         print("ERROR ", command)
    #         count += 1
    #         break

    # print(count)
    # print(len(parser_data))


    #print(_fuzzy_search_command('/mgmt/tm/auth/radius', False))

    # self.assertTrue(result)

    # command, source, kwargs = result

    # self.assertDictEqual(kwargs, expected_kwargs)
    #print(_matches_fuzzy_regex(0,0, 's v'.split(), 'show version'.split(), {} ))
    #print(_matches_fuzzy_regex(0,0, 'sh ver blue'.split(), 'show version {arg}'.split(), {} ))
    #print(_matches_fuzzy_regex(0,0, 'sh ver blue blue green'.split(), 'show version {arg} {ww}'.split(), {} ))
    #print(_matches_fuzzy_regex(0,0, 'sh ver (vs|ww) ww'.split(), 'show version vs ww'.split(), {} ))
    #print(_matches_fuzzy_regex(0,0, 'sh ver .* az blue .* .* ajs .* x x'.split(), 'show version a az {int} abc d ajs bjos {x} x'.split(), {} ))
    #sh ver .* az {int}
    # print(_matches_fuzzy_regex(0,0, 'sh ver .* blue'.split(), 'show version wx abc {arg}'.split(), {} ))

    #argument as 1\.3\.4\.5 etc
    #print(_matches_fuzzy_regex(0,0, 'sh v.* .*'.split(), 'ps -ef'.split(), {} ))
    # buggg 'sh b .* blue .* n|p d'
    # # OR operator
    # for w in _fuzzy_search_command('sh b .* blue .* [n|p] d'):
    #     print(w[0])
    #     print(w[2])
    #     print('========')

