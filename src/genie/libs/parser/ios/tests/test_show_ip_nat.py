import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

from genie.metaparser.util.exceptions import (SchemaEmptyParserError,
                                              SchemaMissingKeyError)

from genie.libs.parser.ios.show_ip_nat import (ShowIpNatTranslations,
                                               ShowIpNatStatistics)

from genie.libs.parser.iosxe.tests.test_show_ip_nat import \
    (TestShowIpNatTranslations as TestShowIpNatTranslationsIosxe,
    TestShowIpNatStatistics as TestShowIpNatStatisticsIosxe)


class TestShowIpNatTranslations(TestShowIpNatStatisticsIosxe):
    device = Device(name='c3850')
    dev_empty = Device(name='empty')
    empty_output = {'execute.return_value': '  '}


    golden_output = {'execute.return_value': '''
        Device# show ip nat translations
        Pro Inside global Inside local Outside local Outside global
        tcp 192.168.1.1:514 192.168.2.3:53 192.168.2.22:256 192.168.2.22:256
        tcp 192.168.1.1:513 192.168.2.2:53 192.168.2.22:256 192.168.2.22:256
        tcp 192.168.1.1:512 192.168.2.4:53 192.168.2.22:256 192.168.2.22:256
        Total number of translations: 3
    '''
    }

    golden_parsed_output = {
        'vrf': {
            'default': {
                'index': {
                    1: {
                        'inside_global': '192.168.1.1:514',
                        'inside_local': '192.168.2.3:53',
                        'outside_global': '192.168.2.22:256',
                        'outside_local': '192.168.2.22:256',
                        'protocol': 'tcp'
                    },
                    2: {
                        'inside_global': '192.168.1.1:513',
                        'inside_local': '192.168.2.2:53',
                        'outside_global': '192.168.2.22:256',
                        'outside_local': '192.168.2.22:256',
                        'protocol': 'tcp'
                    },
                    3: {
                        'inside_global': '192.168.1.1:512',
                        'inside_local': '192.168.2.4:53',
                        'outside_global': '192.168.2.22:256',
                        'outside_local': '192.168.2.22:256',
                        'protocol': 'tcp'
                    }
                }
            },
            'number_of_translations': 3
        }
    }

    golden_output_verbose = {'execute.return_value': '''
        Device# show ip nat translations verbose
        Pro Inside global Inside local Outside local Outside global
        tcp 192.168.1.1:514 192.168.2.3:53 192.168.2.22:256 192.168.2.22:256
        create 04/09/11 10:51:48, use 04/09/11 10:52:31, timeout: 00:01:00
        Map-Id(In):1, Mac-Address: 0000.0000.0000 Input-IDB: GigabitEthernet0/3/1
        entry-id: 0x8ef80350, use_count:1
        tcp 192.168.1.1:513 192.168.2.2:53 192.168.2.22:256 192.168.2.22:256
        create 04/09/11 10:51:48, use 04/09/11 10:52:31, timeout: 00:01:00
        Map-Id(In):1, Mac-Address: 0000.0000.0000 Input-IDB: GigabitEthernet0/3/1
        entry-id: 0x8ef801b0, use_count:1
        tcp 192.168.1.1:512 192.168.2.4:53 192.168.2.22:256 192.168.2.22:256
        create 04/09/11 10:51:48, use 04/09/11 10:52:31, timeout: 00:01:00
        Map-Id(In):1, Mac-Address: 0000.0000.0000 Input-IDB: GigabitEthernet0/3/1
        entry-id: 0x8ef80280, use_count:1
        Total number of translations: 3
    '''
    }

    golden_parsed_output_verbose = {
        'vrf': {
            'default': {
                'index': {
                    1: {
                        'details': {
                            'create': '04/09/11 10:51:48',
                            'entry_id': '0x8ef80350',
                            'input_idb': 'GigabitEthernet0/3/1',
                            'mac_address': '0000.0000.0000',
                            'map_id_in': 1,
                            'timeout': '00:01:00',
                            'use': '04/09/11 10:52:31',
                            'use_count': 1
                        },
                        'inside_global': '192.168.1.1:514',
                        'inside_local': '192.168.2.3:53',
                        'outside_global': '192.168.2.22:256',
                        'outside_local': '192.168.2.22:256',
                        'protocol': 'tcp'
                    },
                    2: {
                        'details': {
                            'create': '04/09/11 10:51:48',
                            'entry_id': '0x8ef801b0',
                            'input_idb': 'GigabitEthernet0/3/1',
                            'mac_address': '0000.0000.0000',
                            'map_id_in': 1,
                            'timeout': '00:01:00',
                            'use': '04/09/11 10:52:31',
                            'use_count': 1
                        },
                        'inside_global': '192.168.1.1:513',
                        'inside_local': '192.168.2.2:53',
                        'outside_global': '192.168.2.22:256',
                        'outside_local': '192.168.2.22:256',
                        'protocol': 'tcp'
                    },
                    3: {
                        'details': {
                            'create': '04/09/11 10:51:48',
                            'entry_id': '0x8ef80280',
                            'input_idb': 'GigabitEthernet0/3/1',
                            'mac_address': '0000.0000.0000',
                            'map_id_in': 1,
                            'timeout': '00:01:00',
                            'use': '04/09/11 10:52:31',
                            'use_count': 1
                        },
                        'inside_global': '192.168.1.1:512',
                        'inside_local': '192.168.2.4:53',
                        'outside_global': '192.168.2.22:256',
                        'outside_local': '192.168.2.22:256',
                        'protocol': 'tcp'
                    }
                }
            },
            'number_of_translations': 3
        }
    }


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

    def test_golden_verbose(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_verbose)
        obj = ShowIpNatTranslations(device=self.device)
        parsed_output = obj.parse(option='verbose')
        self.assertEqual(parsed_output, self.golden_parsed_output_verbose)


class TestShowIpNatStatistics(TestShowIpNatStatisticsIosxe):

    device = Device(name='c3850')
    dev_empty = Device(name='empty')
    empty_output = {'execute.return_value': '  '}

    golden_output = {'execute.return_value': '''
        Device# show ip nat statistics

        Total active translations: 3 (0 static, 3 dynamic; 3 extended) 
        Outside interfaces: 
        GigabitEthernet0/3/0 
        Inside interfaces: 
        GigabitEthernet0/3/1 
        Hits: 3228980 Misses: 3 
        CEF Translated packets: 0, CEF Punted packets: 0 
        Expired translations: 0 
        Dynamic mappings: 
        -- Inside Source 
        [Id: 1] access-list 1 pool pool1 refcount 3 
        pool pool1: netmask 255.255.255.0 
        start 192.168.49.1 end 192.168.115.254 
        type generic, total addresses 254, allocated 0 (0%), misses 0 
        longest chain in pool: pool1's addr-hash: 0, average len 0,chains 0/256 
        Pool stats drop: 0 Mapping stats drop: 0 
        Port block alloc fail: 0 
        IP alias add fail: 0 
        Limit entry add fail: 0 
    '''
    }

    golden_parsed_output = {
        'active_translations': {
            'dynamic': 3, 
            'extended': 3, 
            'static': 0, 
            'total': 3
        },
        'cef_punted_pkts': 0,
        'cef_translated_pkts': 0,
        'dynamic_mappings': {
            'inside_source': {
                'id': {
                    1: {
                        'access_list': '1',
                        'match': 'access-list 1 '
                        'pool pool1',
                        'pool': {
                            'pool1': {
                                'addr_hash': 0,
                                'allocated': 0,
                                'allocated_percentage': 0,
                                'average_len': 0,
                                'chains': '0/256',
                                'end': '192.168.115.254',
                                'misses': 0,
                                'netmask': '255.255.255.0',
                                'start': '192.168.49.1',
                                'total_addresses': 254,
                                'type': 'generic'
                            }
                        },
                        'refcount': 3
                    }
                }
            }
        },
        'expired_translations': 0,
        'hits': 3228980,
        'interfaces': {
            'inside': ['GigabitEthernet0/3/1'],
            'outside': ['GigabitEthernet0/3/0']
        },
        'ip_alias_add_fail': 0,
        'limit_entry_add_fail': 0,
        'mapping_stats_drop': 0,
        'misses': 3,
        'pool_stats_drop': 0,
        'port_block_alloc_fail': 0
    }

    golden_output_1 = {'execute.return_value': '''
        Router# show ip nat statistics
        Total translations: 2 (0 static, 2 dynamic; 0 extended)
        Outside interfaces: Serial0
        Inside interfaces: Ethernet1
        Hits: 135  Misses: 5
        Expired translations: 2
        Dynamic mappings:
        -- Inside Source
        access-list 1 pool net-208 refcount 2
        pool net-208: netmask 255.255.255.240
                start 172.16.233.208 end 172.16.233.221
                type generic, total addresses 14, allocated 2 (14%), misses 0
    '''
    }

    golden_parsed_output_1 = {
        'active_translations': {
            'dynamic': 2, 
            'extended': 0, 
            'static': 0, 
            'total': 2
        },
        'dynamic_mappings': {
            'inside_source': {
                'id': {
                    1: {
                        'access_list': '1',
                        'match': 'access-list 1 pool net-208',
                        'pool': {
                            'net-208': {
                                'allocated': 2,
                                'allocated_percentage': 14,
                                'end': '172.16.233.221',
                                'misses': 0,
                                'netmask': '255.255.255.240',
                                'start': '172.16.233.208',
                                'total_addresses': 14,
                                'type': 'generic'
                            }
                        },
                        'refcount': 2
                    }
                }
            }
        },
        'expired_translations': 2,
        'hits': 135,
        'interfaces': {
            'inside': ['Ethernet1'],
            'outside': ['Serial0']
        },
        'misses': 5
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
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpNatStatistics(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


if __name__ == '__main__':
    unittest.main()
