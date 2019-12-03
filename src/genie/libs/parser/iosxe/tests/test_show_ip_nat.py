#!/bin/env python
import unittest

from unittest.mock import Mock
# ATS
from ats.topology import Device

from genie.metaparser.util.exceptions import (SchemaEmptyParserError,
                                              SchemaMissingKeyError)

from genie.libs.parser.iosxe.show_ip_nat import (ShowIpNatTranslations,
                                                ShowIpNatStatistics)

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
        'vrf': {
            'default': {
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
                }
            },
            'number_of_translations': 3
        }
    }

    golden_output_1 = {'execute.return_value': '''\
        Router#show ip nat translations
        Pro Inside global      Inside local       Outside local      Outside global
        --- 10.1.7.2     192.168.1.95       ---                ---
        --- 10.1.7.200     192.168.1.89       ---                --
        Total number of translations: 2
    '''
    }

    golden_parsed_output_1 = {
        'vrf': {
            'default': { 
                'index': {
                    1: {
                        'inside_global': '10.1.7.2',
                        'inside_local': '192.168.1.95',
                        'outside_global': '---',
                        'outside_local': '---',
                        'protocol': '---'
                    },
                    2: {
                        'inside_global': '10.1.7.200',
                        'inside_local': '192.168.1.89',
                        'outside_global': '--',
                        'outside_local': '---',
                        'protocol': '---'
                    }
                }
            },
            'number_of_translations': 2
        }
    }
    golden_output_2 = {'execute.return_value': '''\
        Router#show ip nat translations
        Pro Inside global        Inside local       Outside local      Outside global
        udp 10.1.7.2:1220  192.168.1.95:1220  10.100.20.100:53    10.100.20.100:53
        tcp 10.1.7.2:11012 192.168.1.89:11012 10.26.102.100:23    10.26.102.100:23
        tcp 10.1.7.2:1067  192.168.1.95:1067  10.220.2.25:23    10.220.2.25:23
        Total number of translations: 3
    '''
    }

    golden_parsed_output_2 = {
        'vrf': {
            'default': {
                'index': {
                    1: {
                        'inside_global': '10.1.7.2:1220',
                        'inside_local': '192.168.1.95:1220',
                        'outside_global': '10.100.20.100:53',
                        'outside_local': '10.100.20.100:53',
                        'protocol': 'udp'
                    },
                    2: {
                        'inside_global': '10.1.7.2:11012',
                        'inside_local': '192.168.1.89:11012',
                        'outside_global': '10.26.102.100:23',
                        'outside_local': '10.26.102.100:23',
                        'protocol': 'tcp'
                    },
                    3: {
                        'inside_global': '10.1.7.2:1067',
                        'inside_local': '192.168.1.95:1067',
                        'outside_global': '10.220.2.25:23',
                        'outside_local': '10.220.2.25:23',
                        'protocol': 'tcp'
                    }
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
        'vrf': {
            'default': {
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
                }
            },
            'number_of_translations': 3
        }
    }

    golden_output_vrf = {'execute.return_value': '''
        Router# show ip nat translations vrf abc
        Pro Inside global Inside local Outside local Outside global
        --- 10.16.2.1 192.168.121.113 --- ---
        --- 10.16.2.2 192.168.122.49 --- ---
        --- 10.16.2.11 192.168.11.1 --- ---
        --- 10.16.2.12 192.168.11.3 --- ---
        --- 10.16.2.13 172.16.19.20 --- ---

        Pro Inside global Inside local Outside local Outside global
        --- 10.16.2.3 192.168.121.113 --- ---
        --- 10.16.2.4 192.168.22.49 --- ---
    '''
    }

    golden_parsed_output_vrf = {
        'vrf': {
            'default': {
                'index': {
                    1: {
                        'inside_global': '10.16.2.1',
                        'inside_local': '192.168.121.113',
                        'outside_global': '---',
                        'outside_local': '---',
                        'protocol': '---'
                    },
                    2: {
                        'inside_global': '10.16.2.2',
                        'inside_local': '192.168.122.49',
                        'outside_global': '---',
                        'outside_local': '---',
                        'protocol': '---'
                    },
                    3: {
                        'inside_global': '10.16.2.11',
                        'inside_local': '192.168.11.1',
                        'outside_global': '---',
                        'outside_local': '---',
                        'protocol': '---'
                    },
                    4: {
                        'inside_global': '10.16.2.12',
                        'inside_local': '192.168.11.3',
                        'outside_global': '---',
                        'outside_local': '---',
                        'protocol': '---'
                    },
                    5: {
                        'inside_global': '10.16.2.13',
                        'inside_local': '172.16.19.20',
                        'outside_global': '---',
                        'outside_local': '---',
                        'protocol': '---'
                    },
                    6: {
                        'inside_global': '10.16.2.3',
                        'inside_local': '192.168.121.113',
                        'outside_global': '---',
                        'outside_local': '---',
                        'protocol': '---'
                    },
                    7: {
                        'inside_global': '10.16.2.4',
                        'inside_local': '192.168.22.49',
                        'outside_global': '---',
                        'outside_local': '---',
                        'protocol': '---'
                    }
                }
            }
        }
    }

    golden_output_vrf_1 = {'execute.return_value': '''
        ISRG2#show ip nat translations vrf T172
        Pro Inside global      Inside local       Outside local      Outside global
        icmp 192.168.33.28:228 172.25.0.1:228     192.168.33.1:228   192.168.33.1:228
        icmp 192.168.33.28:229 172.25.0.1:229     192.168.33.28:229  192.168.33.28:229
        icmp 192.168.33.28:230 172.25.0.1:230     10.1.8.8:230        10.1.8.8:230
        icmp 192.168.33.28:231 172.25.0.1:231     192.168.219.1:231    192.168.219.1:231
        icmp 192.168.33.28:27432 172.25.0.2:27432 10.1.8.8:27432      10.1.8.8:27432
    '''
    }

    golden_parsed_output_vrf_1 = {
        'vrf': {
            'default': {
                'index': {
                    1: {
                        'inside_global': '192.168.33.28:228',
                        'inside_local': '172.25.0.1:228',
                        'outside_global': '192.168.33.1:228',
                        'outside_local': '192.168.33.1:228',
                        'protocol': 'icmp'
                    },
                    2: {
                        'inside_global': '192.168.33.28:229',
                        'inside_local': '172.25.0.1:229',
                        'outside_global': '192.168.33.28:229',
                        'outside_local': '192.168.33.28:229',
                        'protocol': 'icmp'
                    },
                    3: {
                        'inside_global': '192.168.33.28:230',
                        'inside_local': '172.25.0.1:230',
                        'outside_global': '10.1.8.8:230',
                        'outside_local': '10.1.8.8:230',
                        'protocol': 'icmp'
                    },
                    4: {
                        'inside_global': '192.168.33.28:231',
                        'inside_local': '172.25.0.1:231',
                        'outside_global': '192.168.219.1:231',
                        'outside_local': '192.168.219.1:231',
                        'protocol': 'icmp'
                    },
                    5: {
                        'inside_global': '192.168.33.28:27432',
                        'inside_local': '172.25.0.2:27432',
                        'outside_global': '10.1.8.8:27432',
                        'outside_local': '10.1.8.8:27432',
                        'protocol': 'icmp'
                    }
                }
            }
        }
    }

    golden_output_vrf_verbose = {'execute.return_value': '''
        GENIE-1(config)# show ip nat translations vrf genie verbose
        Pro Inside global      Inside local       Outside local      Outside global
        any ---                ---                10.1.0.2          10.144.0.2
            Group_id:0   vrf: genie
            Format(H:M:S) Time-left :0:0:-1
        any ---                ---                10.1.2.21          120.1.211
            Group_id:0   vrf: genie
            Format(H:M:S) Time-left :0:1:38
        any ---                ---                10.1.2.22          120.1.212
            Group_id:0   vrf: genie
            Format(H:M:S) Time-left :0:1:56
        any ---                ---                10.1.2.23          120.1.213
            Group_id:0   vrf: genie
            Format(H:M:S) Time-left :0:1:30
        any ---                ---                10.1.2.24          120.1.214
            Group_id:0   vrf: genie
            Format(H:M:S) Time-left :0:1:54
        any ---                ---                10.1.2.25          120.1.215
            Group_id:0   vrf: genie
            Format(H:M:S) Time-left :0:1:58
        any ---                ---                10.1.2.26          120.1.216
            Group_id:0   vrf: genie
            Format(H:M:S) Time-left :0:1:30
    '''
    }

    golden_parsed_output_vrf_verbose = {
        'vrf': {
            'genie': {
                'index': {
                    1: {
                        'group_id': 0,
                        'inside_global': '---',
                        'inside_local': '---',
                        'outside_global': '10.144.0.2',
                        'outside_local': '10.1.0.2',
                        'protocol': 'any',
                        'time_left': '0:0:-1'
                    },
                    2: {
                        'group_id': 0,
                        'inside_global': '---',
                        'inside_local': '---',
                        'outside_global': '120.1.211',
                        'outside_local': '10.1.2.21',
                        'protocol': 'any',
                        'time_left': '0:1:38'
                    },
                    3: {
                        'group_id': 0,
                        'inside_global': '---',
                        'inside_local': '---',
                        'outside_global': '120.1.212',
                        'outside_local': '10.1.2.22',
                        'protocol': 'any',
                        'time_left': '0:1:56'
                    },
                    4: {
                        'group_id': 0,
                        'inside_global': '---',
                        'inside_local': '---',
                        'outside_global': '120.1.213',
                        'outside_local': '10.1.2.23',
                        'protocol': 'any',
                        'time_left': '0:1:30'
                    },
                    5: {
                        'group_id': 0,
                        'inside_global': '---',
                        'inside_local': '---',
                        'outside_global': '120.1.214',
                        'outside_local': '10.1.2.24',
                        'protocol': 'any',
                        'time_left': '0:1:54'
                    },
                    6: {
                        'group_id': 0,
                        'inside_global': '---',
                        'inside_local': '---',
                        'outside_global': '120.1.215',
                        'outside_local': '10.1.2.25',
                        'protocol': 'any',
                        'time_left': '0:1:58'
                    },
                    7: {
                        'group_id': 0,
                        'inside_global': '---',
                        'inside_local': '---',
                        'outside_global': '120.1.216',
                        'outside_local': '10.1.2.26',
                        'protocol': 'any',
                        'time_left': '0:1:30'
                    }
                }
            }
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
    
    def test_golden_vrf(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_vrf)
        obj = ShowIpNatTranslations(device=self.device)
        parsed_output = obj.parse(vrf='abc')
        self.assertEqual(parsed_output, self.golden_parsed_output_vrf)

    def test_golden_vrf_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_vrf_1)
        obj = ShowIpNatTranslations(device=self.device)
        parsed_output = obj.parse(vrf='T172')
        self.assertEqual(parsed_output, self.golden_parsed_output_vrf_1)
    
    def test_golden_vrf_verbose(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_vrf_verbose)
        obj = ShowIpNatTranslations(device=self.device)
        parsed_output = obj.parse(vrf='genie', option='verbose')
        self.assertEqual(parsed_output, self.golden_parsed_output_vrf_verbose)

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
                        'access_list': '102',
                        'match': 'access-list 102 pool mypool',
                        'pool': {
                            'mypool': {
                                'allocated': 1,
                                'allocated_percentage': 20,
                                'end': '10.5.5.5',
                                'misses': 0,
                                'netmask': '255.255.255.0',
                                'start': '10.5.5.1',
                                'total_addresses': 5,
                                'type': 'generic'
                            }
                        },
                        'refcount': 3
                    }
                }
            }
        },
        'expired_translations': 0,
        'hits': 59230465,
        'interfaces': {
            'inside': ['TenGigabitEthernet1/0/0,',
                        'TenGigabitEthernet1/1/0,',
                        'TenGigabitEthernet1/2/0',
                        'TenGigabitEthernet1/3/0'],
            'outside': ['TenGigabitEthernet2/0/0,',
                        'TenGigabitEthernet2/1/0,',
                        'TenGigabitEthernet2/2/0',
                        'TenGigabitEthernet2/3/0']
        },
        'ip_alias_add_fail': 0,
        'limit_entry_add_fail': 0,
        'mapping_stats_drop': 0,
        'misses': 3,
        'nat_limit_statistics': {
            'max_entry': {
                'max_allowed': 2147483647,
                'missed': 0,
                'used': 3
            }
        },
        'pool_stats_drop': 0,
        'port_block_alloc_fail': 0
    }
    golden_output_1 = {'execute.return_value': '''
        asr1000#sh ip nat statistics 
        Total active translations: 0 (0 static, 0 dynamic; 0 extended)
        Outside interfaces:
        TenGigabitEthernet0/2/0
        Inside interfaces: 
        TenGigabitEthernet0/1/0
        Hits: 3358708  Misses: 11050
        CEF Translated packets: 0, CEF Punted packets: 0
        Expired translations: 11013
        Dynamic mappings:
        -- Inside Source
        [Id: 1] access-list test-robot pool test-robot refcount 0
        pool test-robot: netmask 255.255.255.252
            start 10.1.1.1 end 10.1.1.1
            type generic, total addresses 1, allocated 0 (0%), misses 0
        Pool stats drop: 0  Mapping stats drop: 0
        Port block alloc fail: 0
        IP alias add fail: 0
        Limit entry add fail: 0
    '''
    }

    golden_parsed_output_1 = {
        'active_translations': {
            'dynamic': 0, 
            'extended': 0, 
            'static': 0, 
            'total': 0
        },
        'cef_punted_pkts': 0,
        'cef_translated_pkts': 0,
        'dynamic_mappings': {
            'inside_source': {
                'id': {
                    1: {
                        'access_list': 'test-robot',
                        'match': 'access-list test-robot pool test-robot',
                        'pool': {
                            'test-robot': {
                                'allocated': 0,
                                'allocated_percentage': 0,
                                'end': '10.1.1.1',
                                'misses': 0,
                                'netmask': '255.255.255.252',
                                'start': '10.1.1.1',
                                'total_addresses': 1,
                                'type': 'generic'
                            }
                        },
                        'refcount': 0
                    }
                }
            }
        },
        'expired_translations': 11013,
        'hits': 3358708,
        'interfaces': {
            'inside': ['TenGigabitEthernet0/1/0'],
            'outside': ['TenGigabitEthernet0/2/0']
        },
        'ip_alias_add_fail': 0,
        'limit_entry_add_fail': 0,
        'mapping_stats_drop': 0,
        'misses': 11050,
        'pool_stats_drop': 0,
        'port_block_alloc_fail': 0
    }

    golden_output_2 = {'execute.return_value': '''
        C1841#sh ip nat statistics 
        Total active translations: 3339 (0 static, 3339 dynamic; 3339 extended)
        Peak translations: 8114, occurred 18:35:17 ago
        Outside interfaces:
        FastEthernet0/0
        Inside interfaces: 
        FastEthernet0/1
        Hits: 28658670  Misses: 0
    '''
    }

    golden_parsed_output_2 = {
        'active_translations': {
            'dynamic': 3339,
            'extended': 3339,
            'static': 0,
            'total': 3339
        },
        'hits': 28658670,
        'interfaces': {
            'inside': ['FastEthernet0/1'], 
            'outside': ['FastEthernet0/0']
        },
        'misses': 0,
        'occurred': '18:35:17',
        'peak_translations': 8114
    }

    golden_output_3 = {'execute.return_value': '''
        r1#sh ip nat stat
        Total active translations: 1 (0 static, 1 dynamic; 1 extended)
        Outside interfaces:
          Serial0/0
        Inside interfaces:
          FastEthernet0/0
        Hits: 3  Misses: 1
        CEF Translated packets: 4, CEF Punted packets: 0
        Expired translations: 0
        Dynamic mappings:
        -- Inside Source
        [Id: 3] access-list 99 interface Serial0/0 refcount 1
        Queued Packets: 0
    '''}

    golden_parsed_output_3 = {
        'active_translations': {
            'dynamic': 1, 
            'extended': 1, 
            'static': 0, 
            'total': 1
        },
        'cef_punted_pkts': 0,
        'cef_translated_pkts': 4,
        'dynamic_mappings': {
            'inside_source': {
                'id': {
                    3: {
                        'access_list': '99',
                        'interface': 'Serial0/0',
                        'match': 'access-list 99 '
                        'interface '
                        'Serial0/0',
                        'refcount': 1
                    }
                }
            }
        },
        'expired_translations': 0,
        'hits': 3,
        'interfaces': {
            'inside': ['FastEthernet0/0'], 
            'outside': ['Serial0/0']
        },
        'misses': 1,
        'queued_pkts': 0
    }

    golden_output_4 = {'execute.return_value': '''
        Total active translations: 0 (0 static, 0 dynamic; 0 extended)
        Peak translations: 0
        Outside interfaces:
        Inside interfaces: 
        Hits: 0  Misses: 0
        CEF Translated packets: 0, CEF Punted packets: 0
        Expired translations: 0
        Dynamic mappings:

        Total doors: 0
        Appl doors: 0
        Normal doors: 0
        Queued Packets: 0
    '''
    }

    golden_parsed_output_4 = {
        'active_translations': {
            'dynamic': 0, 
            'extended': 0, 
            'static': 0, 
            'total': 0
        },
        'appl_doors': 0,
        'cef_punted_pkts': 0,
        'cef_translated_pkts': 0,
        'dynamic_mappings': {},
        'expired_translations': 0,
        'hits': 0,
        'interfaces': {},
        'misses': 0,
        'normal_doors': 0,
        'peak_translations': 0,
        'queued_pkts': 0,
        'total_doors': 0
    }

    golden_output_5 = {'execute.return_value': '''
        show ip nat statistics
        Total active translations: 5 (0 static, 5 dynamic; 5 extended)
        Outside interfaces:
        GigabitEthernet0/0/1
        Inside interfaces: 
        GigabitEthernet0/0/0
        Hits: 11178  Misses: 8
        Expired translations: 0
        Dynamic mappings:
        -- Inside Source
        [Id: 1] route-map NAT-MAP pool inside-pool refcount 6
        pool inside-pool: id 1, netmask 255.255.255.0
            start 10.49.1.1 end 10.49.1.1
            type generic, total addresses 1, allocated 1 (100%), misses 0
        nat-limit statistics:
        max entry: max allowed 0, used 0, missed 0
        In-to-out drops: 0  Out-to-in drops: 0
        Pool stats drop: 0  Mapping stats drop: 0
        Port block alloc fail: 0
        IP alias add fail: 0
        Limit entry add fail: 0
    '''
    }

    golden_parsed_output_5 = {
        'active_translations': {
            'dynamic': 5, 
            'extended': 5, 
            'static': 0, 
            'total': 5
        },
        'dynamic_mappings': {
            'inside_source': {
                'id': {
                    1: {
                        'match': 'route-map NAT-MAP pool inside-pool',
                        'pool': {
                            'inside-pool': {
                                'allocated': 1,
                                'allocated_percentage': 100,
                                'end': '10.49.1.1',
                                'id': 1,
                                'misses': 0,
                                'netmask': '255.255.255.0',
                                'start': '10.49.1.1',
                                'total_addresses': 1,
                                'type': 'generic'
                            }
                        },
                        'refcount': 6,
                        'route_map': 'NAT-MAP'
                    }
                }
            }
        },
        'expired_translations': 0,
        'hits': 11178,
        'in_to_out_drops': 0,
        'interfaces': {
            'inside': ['GigabitEthernet0/0/0'],
            'outside': ['GigabitEthernet0/0/1']
        },
        'ip_alias_add_fail': 0,
        'limit_entry_add_fail': 0,
        'mapping_stats_drop': 0,
        'misses': 8,
        'nat_limit_statistics': {
            'max_entry': {
                'max_allowed': 0,
                'missed': 0,
                'used': 0
            }
        },
        'out_to_in_drops': 0,
        'pool_stats_drop': 0,
        'port_block_alloc_fail': 0
    }

    golden_output_6 = {'execute.return_value': '''
        show ip nat statistics
        Total active translations: 6 (1 static, 5 dynamic; 5 extended)
        Outside interfaces:
        GigabitEthernet0/0/1
        Inside interfaces: 
        GigabitEthernet0/0/0
        Hits: 78230  Misses: 56
        Expired translations: 0
        Dynamic mappings:
        -- Inside Source
        [Id: 1] route-map NAT-MAP pool inside-pool refcount 6
        pool inside-pool: id 6, netmask 255.255.255.0
            start 10.49.1.1 end 10.49.1.1
            type generic, total addresses 1, allocated 1 (100%), misses 0
        [Id: 0] route-map STATIC-MAP pool genie-pool refcount 5
        pool genie-pool: id 5, netmask 255.255.255.0
            start 10.49.1.1 end 10.49.1.1
            type generic, total addresses 1, allocated 1 (100%), misses 0
        [Id: 4] route-map GENIE-MAP
        [Id: 3] access-list 99 interface Serial0/0 refcount 1
        nat-limit statistics:
        max entry: max allowed 0, used 0, missed 0
        In-to-out drops: 0  Out-to-in drops: 0
        Pool stats drop: 0  Mapping stats drop: 0
        Port block alloc fail: 0
        IP alias add fail: 0
        Limit entry add fail: 0
    '''
    }

    golden_parsed_output_6 = {
        'active_translations': {
            'dynamic': 5, 
            'extended': 5, 
            'static': 1, 
            'total': 6
        },
        'dynamic_mappings': {
            'inside_source': {
                'id': {
                    0: {
                        'match': 'route-map STATIC-MAP pool genie-pool',
                        'pool': {
                            'genie-pool': {
                                'allocated': 1,
                                'allocated_percentage': 100,
                                'end': '10.49.1.1',
                                'id': 5,
                                'misses': 0,
                                'netmask': '255.255.255.0',
                                'start': '10.49.1.1',
                                'total_addresses': 1,
                                'type': 'generic'
                            }
                        },
                        'refcount': 5,
                        'route_map': 'STATIC-MAP'
                    },
                    1: {
                        'match': 'route-map NAT-MAP pool inside-pool',
                        'pool': {
                            'inside-pool': {
                                'allocated': 1,
                                'allocated_percentage': 100,
                                'end': '10.49.1.1',
                                'id': 6,
                                'misses': 0,
                                'netmask': '255.255.255.0',
                                'start': '10.49.1.1',
                                'total_addresses': 1,
                                'type': 'generic'
                            }
                        },
                        'refcount': 6,
                        'route_map': 'NAT-MAP'
                    },
                    3: {
                        'access_list': '99',
                        'interface': 'Serial0/0',
                        'match': 'access-list 99 '
                        'interface Serial0/0',
                        'refcount': 1
                    },
                    4: {
                        'match': 'route-map GENIE-MAP',
                        'route_map': 'GENIE-MAP'
                    }
                }
            }
        },
        'expired_translations': 0,
        'hits': 78230,
        'in_to_out_drops': 0,
        'interfaces': {
            'inside': ['GigabitEthernet0/0/0'],
            'outside': ['GigabitEthernet0/0/1']
        },
        'ip_alias_add_fail': 0,
        'limit_entry_add_fail': 0,
        'mapping_stats_drop': 0,
        'misses': 56,
        'nat_limit_statistics': {
            'max_entry': {
                'max_allowed': 0,
                'missed': 0,
                'used': 0
            }
        },
        'out_to_in_drops': 0,
        'pool_stats_drop': 0,
        'port_block_alloc_fail': 0
    }

    golden_output_7 = {'execute.return_value': '''
        Genie#show ip nat statistics 
        Total active translations: 3001 (1 static, 3000 dynamic; 1500 extended)
        Outside interfaces:
        Vlan89
        Inside interfaces: 
        Vlan88
        Hits: 45392  Misses: 0
        CEF Translated packets: 0, CEF Punted packets: 0
        Expired translations: 1
        Dynamic mappings:
        -- Inside Source
        [Id: 1] access-list test pool net-208 refcount 3000
        pool net-208: id 1, netmask 255.255.0.0
            start 10.55.0.1 end 10.55.100.254
            type generic, total addresses 25854, allocated 1500 (5%), misses 0
        longest chain in pool: net-208's addr-hash: 6, average len 5,chains 256/256
    '''
    }

    golden_parsed_output_7 = {
        'active_translations': {
            'dynamic': 3000,
            'extended': 1500,
            'static': 1,
            'total': 3001
        },
        'cef_punted_pkts': 0,
        'cef_translated_pkts': 0,
        'dynamic_mappings': {
            'inside_source': {
                'id': {
                    1: {
                        'access_list': 'test',
                        'match': 'access-list test pool net-208',
                        'pool': {
                            'net-208': {
                                'addr_hash': 6,
                                'allocated': 1500,
                                'allocated_percentage': 5,
                                'average_len': 5,
                                'chains': '256/256',
                                'end': '10.55.100.254',
                                'id': 1,
                                'misses': 0,
                                'netmask': '255.255.0.0',
                                'start': '10.55.0.1',
                                'total_addresses': 25854,
                                'type': 'generic'
                            }
                        },
                        'refcount': 3000
                    }
                }
            }
        },
        'expired_translations': 1,
        'hits': 45392,
        'interfaces': {
            'inside': ['Vlan88'], 
            'outside': ['Vlan89']
        },
        'misses': 0
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

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpNatStatistics(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_3)
        obj = ShowIpNatStatistics(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_3)
    
    def test_golden_4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_4)
        obj = ShowIpNatStatistics(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_4)
    
    def test_golden_5(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_5)
        obj = ShowIpNatStatistics(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_5)
    
    def test_golden_6(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_6)
        obj = ShowIpNatStatistics(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_6)

    def test_golden_7(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_7)
        obj = ShowIpNatStatistics(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_7)
 
    
if __name__ == '__main__':
    unittest.main()
