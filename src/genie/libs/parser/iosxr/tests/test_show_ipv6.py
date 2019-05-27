import re
import unittest
from unittest.mock import Mock

from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

from genie.libs.parser.iosxr.show_ipv6 import ShowIpv6NeighborsDetail


#############################################################################
# unitest For show ipv6 neighbors detail
#############################################################################

class test_show_ipv6_neighbors_detail(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'interfaces': {
            'GigabitEthernet0/0/0/0': {
                'interface': 'Gi0/0/0/0',
                'neighbors': {
                    '2010:1:2::1': {
                        'age': '82',
                        'dynamic': 'Y',
                        'ip': '2010:1:2::1',
                        'link_layer_address': 'fa16.3e19.abba',
                        'location': '0/0/CPU0',
                        'neighbor_state': 'REACH',
                        'serg_flags': 'ff',
                        'static': '-',
                        'sync': '-'},
                    '2010:1:2::22': {
                        'age': '-',
                        'dynamic': '-',
                        'ip': '2010:1:2::22',
                        'link_layer_address': 'aaaa.beaf.bbbb',
                        'location': '0/0/CPU0',
                        'neighbor_state': 'REACH',
                        'serg_flags': 'ff',
                        'static': 'Y',
                        'sync': '-'},
                    'Mcast adjacency': {
                        'age': '-',
                        'dynamic': '-',
                        'ip': 'Mcast adjacency',
                        'link_layer_address': '0000.0000.0000',
                        'location': '0/0/CPU0',
                        'neighbor_state': 'REACH',
                        'serg_flags': 'ff',
                        'static': '-',
                        'sync': '-'},
                    'fe80::f816:3eff:fe19:abba': {
                        'age': '158',
                        'dynamic': 'Y',
                        'ip': 'fe80::f816:3eff:fe19:abba',
                        'link_layer_address': 'fa16.3e19.abba',
                        'location': '0/0/CPU0',
                        'neighbor_state': 'REACH',
                        'serg_flags': 'ff',
                        'static': '-',
                        'sync': '-'}}},
            'GigabitEthernet0/0/0/1': {
                'interface': 'Gi0/0/0/1',
                'neighbors': {
                    '2020:1:2::1': {
                        'age': '4',
                        'dynamic': 'Y',
                        'ip': '2020:1:2::1',
                        'link_layer_address': 'fa16.3e72.8407',
                        'location': '0/0/CPU0',
                        'neighbor_state': 'REACH',
                        'serg_flags': 'ff',
                        'static': '-',
                        'sync': '-'},
                    '2020:1:2::22': {
                        'age': '-',
                        'dynamic': '-',
                        'ip': '2020:1:2::22',
                        'link_layer_address': 'dddd.beef.aaaa',
                        'location': '0/0/CPU0',
                        'neighbor_state': 'REACH',
                        'serg_flags': 'ff',
                        'static': 'Y',
                        'sync': '-'},
                    'Mcast adjacency': {
                        'age': '-',
                        'dynamic': '-',
                        'ip': 'Mcast adjacency',
                        'link_layer_address': '0000.0000.0000',
                        'location': '0/0/CPU0',
                        'neighbor_state': 'REACH',
                        'serg_flags': 'ff',
                        'static': '-',
                        'sync': '-'},
                    'fe80::f816:3eff:fe72:8407': {
                        'age': '37',
                        'dynamic': 'Y',
                        'ip': 'fe80::f816:3eff:fe72:8407',
                        'link_layer_address': 'fa16.3e72.8407',
                        'location': '0/0/CPU0',
                        'neighbor_state': 'REACH',
                        'serg_flags': 'ff',
                        'static': '-',
                        'sync': '-'}}},
            'GigabitEthernet0/0/0/2': {
                'interface': 'Gi0/0/0/2',
                'neighbors': {
                    '2010:2:3::3': {
                        'age': '1',
                        'dynamic': 'Y',
                        'ip': '2010:2:3::3',
                        'link_layer_address': '5e01.c002.0007',
                        'location': '0/0/CPU0',
                        'neighbor_state': 'REACH',
                        'serg_flags': 'ff',
                        'static': '-',
                        'sync': '-'},
                    'Mcast adjacency': {
                        'age': '-',
                        'dynamic': '-',
                        'ip': 'Mcast adjacency',
                        'link_layer_address': '0000.0000.0000',
                        'location': '0/0/CPU0',
                        'neighbor_state': 'REACH',
                        'serg_flags': 'ff',
                        'static': '-',
                        'sync': '-'},
                    'fe80::5c01:c0ff:fe02:7': {
                        'age': '12',
                        'dynamic': 'Y',
                        'ip': 'fe80::5c01:c0ff:fe02:7',
                        'link_layer_address': '5e01.c002.0007',
                        'location': '0/0/CPU0',
                        'neighbor_state': 'REACH',
                        'serg_flags': 'ff',
                        'static': '-',
                        'sync': '-'}}},
            'GigabitEthernet0/0/0/3': {
                'interface': 'Gi0/0/0/3',
                'neighbors': {
                    '2020:2:3::3': {
                        'age': '114',
                        'dynamic': 'Y',
                        'ip': '2020:2:3::3',
                        'link_layer_address': '5e01.c002.0007',
                        'location': '0/0/CPU0',
                        'neighbor_state': 'REACH',
                        'serg_flags': 'ff',
                        'static': '-',
                        'sync': '-'},
                    'Mcast adjacency': {
                        'age': '-',
                        'dynamic': '-',
                        'ip': 'Mcast adjacency',
                        'link_layer_address': '0000.0000.0000',
                        'location': '0/0/CPU0',
                        'neighbor_state': 'REACH',
                        'serg_flags': 'ff',
                        'static': '-',
                        'sync': '-'},
                    'fe80::5c01:c0ff:fe02:7': {
                        'age': '12',
                        'dynamic': 'Y',
                        'ip': 'fe80::5c01:c0ff:fe02:7',
                        'link_layer_address': '5e01.c002.0007',
                        'location': '0/0/CPU0',
                        'neighbor_state': 'REACH',
                        'serg_flags': 'ff',
                        'static': '-',
                        'sync': '-'}}}}}

    golden_output = {'execute.return_value': '''
        RP/0/RP0/CPU0:xr9kv-2#show ipv6 neighbors detail
        Thu Apr 26 13:09:53.379 UTC
        IPv6 Address                             Age  Link-layer Add State Interface            Location      Static Dynamic Sync       Serg-Flags 
        2010:1:2::1                              82   fa16.3e19.abba REACH Gi0/0/0/0            0/0/CPU0        -      Y       -            ff
        2010:1:2::22                                - aaaa.beaf.bbbb REACH Gi0/0/0/0            0/0/CPU0        Y      -       -            ff
        fe80::f816:3eff:fe19:abba                158  fa16.3e19.abba REACH Gi0/0/0/0            0/0/CPU0        -      Y       -            ff
        [Mcast adjacency]                           - 0000.0000.0000 REACH Gi0/0/0/0            0/0/CPU0        -      -       -            ff
        2020:2:3::3                              114  5e01.c002.0007 REACH Gi0/0/0/3            0/0/CPU0        -      Y       -            ff
        fe80::5c01:c0ff:fe02:7                   12   5e01.c002.0007 REACH Gi0/0/0/3            0/0/CPU0        -      Y       -            ff
        [Mcast adjacency]                           - 0000.0000.0000 REACH Gi0/0/0/3            0/0/CPU0        -      -       -            ff
        2010:2:3::3                              1    5e01.c002.0007 REACH Gi0/0/0/2            0/0/CPU0        -      Y       -            ff
        fe80::5c01:c0ff:fe02:7                   12   5e01.c002.0007 REACH Gi0/0/0/2            0/0/CPU0        -      Y       -            ff
        [Mcast adjacency]                           - 0000.0000.0000 REACH Gi0/0/0/2            0/0/CPU0        -      -       -            ff
        2020:1:2::1                              4    fa16.3e72.8407 REACH Gi0/0/0/1            0/0/CPU0        -      Y       -            ff
        2020:1:2::22                                - dddd.beef.aaaa REACH Gi0/0/0/1            0/0/CPU0        Y      -       -            ff
        fe80::f816:3eff:fe72:8407                37   fa16.3e72.8407 REACH Gi0/0/0/1            0/0/CPU0        -      Y       -            ff
        [Mcast adjacency]                           - 0000.0000.0000 REACH Gi0/0/0/1            0/0/CPU0        -      -       -            ff
    '''}

    def test_show_ipv6_neighbors_detail_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6NeighborsDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ipv6_neighbors_detail_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6NeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()