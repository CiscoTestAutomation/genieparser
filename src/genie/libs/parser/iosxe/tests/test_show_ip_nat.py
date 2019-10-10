#!/bin/env python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

from genie.libs.parser.iosxe.show_ip_nat import ShowIpNatTranslations, \
                                                ShowIpNatStatistics


####################################################
# Unit test for:
#   * 'show ip nat translations'
#   * 'show ip nat translations verbose'
####################################################

class TestShowIpNatTranslations(unittest.TestCase):

    golden_output = {'execute.return_value': '''\
        Device# show ip nat translations

		Pro  Inside global         Inside local          Outside local         Outside global
		udp  10.5.5.1:1025          192.0.2.1:4000        ---                   ---
		udp  10.5.5.1:1024          192.0.2.3:4000        ---                   ---
        udp  10.5.5.1:1026          192.0.2.2:4000        ---                   ---
        Total number of translations: 3
    '''
    }

    golden_parsed_output = {
        'nat_translations': {
            'index': {
                1: {
                    'inside_global': '10.5.5.1:1025',
                    'inside_local': '192.0.2.1:4000',
                    'outside_global': '---',
                    'outside_local': '---',
                    'protocol': 'udp'
                },
                2: {
                    'inside_global': '10.5.5.1:1024',
                    'inside_local': '192.0.2.3:4000',
                    'outside_global': '---',
                    'outside_local': '---',
                    'protocol': 'udp'
                },
                3: {
                    'inside_global': '10.5.5.1:1026',
                    'inside_local': '192.0.2.2:4000',
                    'outside_global': '---',
                    'outside_local': '---',
                    'protocol': 'udp'
                }
            },
            'number_of_translations': 3
        }
    }

    golden_output_1 = {'execute.return_value': '''\
        Router#show ip nat translations
        Pro Inside global      Inside local       Outside local      Outside global
        --- 171.69.233.209     192.168.1.95       ---                ---
        --- 171.69.233.210     192.168.1.89       ---                --
        Total number of translations: 2
    '''
    }

    golden_parsed_output_1 = {
        'nat_translations': {
            'index': {
                1: {
                    'inside_global': '171.69.233.209',
                    'inside_local': '192.168.1.95',
                    'outside_global': '---',
                    'outside_local': '---',
                    'protocol': '---'
                },
                2: {
                    'inside_global': '171.69.233.210',
                    'inside_local': '192.168.1.89',
                    'outside_global': '--',
                    'outside_local': '---',
                    'protocol': '---'
                }
            },
            'number_of_translations': 2
        }
    }
    golden_output_2 = {'execute.return_value': '''\
        Router#show ip nat translations
        Pro Inside global        Inside local       Outside local      Outside global
        udp 171.69.233.209:1220  192.168.1.95:1220  171.69.2.132:53    171.69.2.132:53
        tcp 171.69.233.209:11012 192.168.1.89:11012 171.69.1.220:23    171.69.1.220:23
        tcp 171.69.233.209:1067  192.168.1.95:1067  171.69.1.161:23    171.69.1.161:23
        Total number of translations: 3
    '''
    }

    golden_parsed_output_2 = {
        'nat_translations': {
            'index': {
                1: {
                    'inside_global': '171.69.233.209:1220',
                    'inside_local': '192.168.1.95:1220',
                    'outside_global': '171.69.2.132:53',
                    'outside_local': '171.69.2.132:53',
                    'protocol': 'udp'
                },
                2: {
                    'inside_global': '171.69.233.209:11012',
                    'inside_local': '192.168.1.89:11012',
                    'outside_global': '171.69.1.220:23',
                    'outside_local': '171.69.1.220:23',
                    'protocol': 'tcp'
                },
                3: {
                    'inside_global': '171.69.233.209:1067',
                    'inside_local': '192.168.1.95:1067',
                    'outside_global': '171.69.1.161:23',
                    'outside_local': '171.69.1.161:23',
                    'protocol': 'tcp'
                }
            },
            'number_of_translations': 3
        }
    }

    golden_output_3 = {'execute.return_value': '''\
        Device# show ip nat translations verbose

        Pro  Inside global         Inside local          Outside local         Outside global
        udp  10.5.5.1:1025          192.0.2.1:4000        ---                   ---
        create: 02/15/12 11:38:01, use: 02/15/12 11:39:02, timeout: 00:00:00
        Map-Id(In): 1
        Mac-Address: 0000.0000.0000    Input-IDB: TenGigabitEthernet1/1/0
        entry-id: 0x0, use_count:1

        udp  10.5.5.1:1024          192.0.2.3:4000        ---                   ---
        create: 02/15/12 11:38:00, use: 02/15/12 11:39:02, timeout: 00:00:00
        Map-Id(In): 1
        Mac-Address: 0000.0000.0000    Input-IDB: TenGigabitEthernet1/1/0
        entry-id: 0x0, use_count:1

        udp  10.5.5.1:1026          192.0.2.2:4000        ---                   ---
        create: 02/15/12 11:38:00, use: 02/15/12 11:39:02, timeout: 00:00:00
        Map-Id(In): 1
        Mac-Address: 0000.0000.0000    Input-IDB: TenGigabitEthernet1/1/0
        entry-id: 0x0, use_count:1

        Total number of translations: 3
    '''    
    }

    golden_parsed_output_3 = {
        'nat_translations': {
            'index': {
                1: {
                    'details': {
                        'create': '02/15/12 11:38:01',
                        'entry_id': '0x0',
                        'input_idb': 'TenGigabitEthernet1/1/0',
                        'mac_address': '0000.0000.0000',
                        'map_id_in': 1,
                        'timeout': '00:00:00',
                        'use': '02/15/12 11:39:02',
                        'use_count': 1
                    },
                    'inside_global': '10.5.5.1:1025',
                    'inside_local': '192.0.2.1:4000',
                    'outside_global': '---',
                    'outside_local': '---',
                    'protocol': 'udp'
                },
                2: {
                    'details': {
                        'create': '02/15/12 11:38:00',
                        'entry_id': '0x0',
                        'input_idb': 'TenGigabitEthernet1/1/0',
                        'mac_address': '0000.0000.0000',
                        'map_id_in': 1,
                        'timeout': '00:00:00',
                        'use': '02/15/12 11:39:02',
                        'use_count': 1
                    },
                    'inside_global': '10.5.5.1:1024',
                    'inside_local': '192.0.2.3:4000',
                    'outside_global': '---',
                    'outside_local': '---',
                    'protocol': 'udp'
                },
                3: {
                    'details': {
                        'create': '02/15/12 11:38:00',
                        'entry_id': '0x0',
                        'input_idb': 'TenGigabitEthernet1/1/0',
                        'mac_address': '0000.0000.0000',
                        'map_id_in': 1,
                        'timeout': '00:00:00',
                        'use': '02/15/12 11:39:02',
                        'use_count': 1
                    },
                    'inside_global': '10.5.5.1:1026',
                    'inside_local': '192.0.2.2:4000',
                    'outside_global': '---',
                    'outside_local': '---',
                    'protocol': 'udp'
                }
            },
            'number_of_translations': 3
        }
    }

    device = Device(name='c3850')
    dev_empty = Device(name='empty')
    empty_output = {'execute.return_value': '  '}

    def test_empty(self):
        self.dev_empty = Mock(**self.empty_output)
        obj = ShowIpNatTranslations(device=self.dev_empty)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()
    
    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpNatTranslations(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpNatTranslations(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpNatTranslations(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_3)
        obj = ShowIpNatTranslations(device=self.device)
        parsed_output = obj.parse(option='verbose')
        self.assertEqual(parsed_output, self.golden_parsed_output_3)

class TestShowIpNatStatistics(unittest.TestCase):

    device = Device(name='c3850')
    dev_empty = Device(name='empty')
    empty_output = {'execute.return_value': '  '}

    golden_output = {'execute.return_value': '''
        Device# show ip nat statistics

        Total active translations: 3 (0 static, 3 dynamic; 3 extended)
        Outside interfaces:
        TenGigabitEthernet2/0/0, TenGigabitEthernet2/1/0, TenGigabitEthernet2/2/0
        TenGigabitEthernet2/3/0
        Inside interfaces: 
        TenGigabitEthernet1/0/0, TenGigabitEthernet1/1/0, TenGigabitEthernet1/2/0
        TenGigabitEthernet1/3/0
        Hits: 59230465  Misses: 3
        CEF Translated packets: 0, CEF Punted packets: 0
        Expired translations: 0
        Dynamic mappings:
        -- Inside Source
        [Id: 1] access-list 102 pool mypool refcount 3
        pool mypool: netmask 255.255.255.0
                start 10.5.5.1 end 10.5.5.5
                type generic, total addresses 5, allocated 1 (20%), misses 0
        nat-limit statistics:
        max entry: max allowed 2147483647, used 3, missed 0
        Pool stats drop: 0  Mapping stats drop: 0
        Port block alloc fail: 0
        IP alias add fail: 0
        Limit entry add fail: 0
    '''
    }

    def test_empty(self):
        self.dev_empty = Mock(**self.empty_output)
        obj = ShowIpNatStatistics(device=self.dev_empty)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpNatStatistics(device=self.device)
        parsed_output = obj.parse()
        import pprint
        pprint.pprint(parsed_output)
        #self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()
