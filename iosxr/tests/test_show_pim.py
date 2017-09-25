
# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_pim
from parser.iosxr.show_pim import ShowPimVrfMstatic


# ===================================================
#  Unit test for 'show pim vrf <WORD> <WORD> mstatic'
# ===================================================

class test_show_pim_vrf_mstatic(unittest.TestCase):

    '''Unit test for 'show pim vrf <WORD> <WORD> mstatic'''
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv4': 
                        {'mroute': 
                            {'10.10.10.10/32': 
                                {'path': 
                                    {'192.168.1.0 GigabitEthernet0/0/0/0 10': 
                                        {'admin_distance': 10,
                                        'interface_name': 'GigabitEthernet0/0/0/0',
                                        'neighbor_address': '192.168.1.0'}}},
                            '10.10.10.11/32': 
                                {'path': 
                                    {'192.168.1.1 GigabitEthernet0/0/0/1 11': 
                                        {'admin_distance': 11,
                                        'interface_name': 'GigabitEthernet0/0/0/1',
                                        'neighbor_address': '192.168.1.1'}}},
                            '10.10.10.12/32': 
                                {'path': 
                                    {'192.168.1.2 GigabitEthernet0/0/0/2 12': 
                                        {'admin_distance': 12,
                                        'interface_name': 'GigabitEthernet0/0/0/2',
                                        'neighbor_address': '192.168.1.2'}}},
                            '10.10.10.13/32': 
                                {'path': 
                                    {'192.168.1.3 GigabitEthernet0/0/0/3 13': 
                                        {'admin_distance': 13,
                                        'interface_name': 'GigabitEthernet0/0/0/3',
                                        'neighbor_address': '192.168.1.3'}}},
                            '10.10.10.14/32': 
                                {'path': 
                                    {'192.168.1.4 GigabitEthernet0/0/0/4 14': 
                                        {'admin_distance': 14,
                                        'interface_name': 'GigabitEthernet0/0/0/4',
                                        'neighbor_address': '192.168.1.4'}}},
                            '10.10.10.15/32': 
                                {'path': 
                                    {'192.168.1.5 GigabitEthernet0/0/0/5 15': 
                                        {'admin_distance': 15,
                                        'interface_name': 'GigabitEthernet0/0/0/5',
                                        'neighbor_address': '192.168.1.5'}}},
                            '10.10.10.16/32': 
                                {'path': 
                                    {'192.168.1.6 GigabitEthernet0/0/0/6 16': 
                                        {'admin_distance': 16,
                                        'interface_name': 'GigabitEthernet0/0/0/6',
                                        'neighbor_address': '192.168.1.6'}}},
                            '10.10.10.17/32': 
                                {'path': 
                                    {'192.168.1.7 GigabitEthernet0/0/0/7 17': 
                                        {'admin_distance': 17,
                                        'interface_name': 'GigabitEthernet0/0/0/7',
                                        'neighbor_address': '192.168.1.7'}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        RP/0/0/CPU0:R2# show pim vrf default ipv4 mstatic
        Mon May 29 14:37:05.732 UTC
        IP Multicast Static Routes Information

        * 10.10.10.10/32 via GigabitEthernet0/0/0/0 with nexthop 192.168.1.0 and distance 10
        * 10.10.10.11/32 via GigabitEthernet0/0/0/1 with nexthop 192.168.1.1 and distance 11
        * 10.10.10.12/32 via GigabitEthernet0/0/0/2 with nexthop 192.168.1.2 and distance 12
        * 10.10.10.13/32 via GigabitEthernet0/0/0/3 with nexthop 192.168.1.3 and distance 13
        * 10.10.10.14/32 via GigabitEthernet0/0/0/4 with nexthop 192.168.1.4 and distance 14
        * 10.10.10.15/32 via GigabitEthernet0/0/0/5 with nexthop 192.168.1.5 and distance 15
        * 10.10.10.16/32 via GigabitEthernet0/0/0/6 with nexthop 192.168.1.6 and distance 16
        * 10.10.10.17/32 via GigabitEthernet0/0/0/7 with nexthop 192.168.1.7 and distance 17
        '''}

    golden_parsed_output2 = {
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv6': 
                        {'mroute': 
                            {'2001:10:10::10/128': 
                                {'path': 
                                    {'2001:11:11::10 GigabitEthernet0/0/0/0 10': 
                                        {'admin_distance': 10,
                                        'interface_name': 'GigabitEthernet0/0/0/0',
                                        'neighbor_address': '2001:11:11::10'}}},
                                    '2001:10:10::11/128': 
                                        {'path': 
                                            {'2001:11:11::11 GigabitEthernet0/0/0/1 11': 
                                                {'admin_distance': 11,
                                                'interface_name': 'GigabitEthernet0/0/0/1',
                                                'neighbor_address': '2001:11:11::11'}}},
                                    '2001:10:10::12/128': 
                                        {'path': 
                                            {'2001:11:11::12 GigabitEthernet0/0/0/2 12': 
                                                {'admin_distance': 12,
                                                'interface_name': 'GigabitEthernet0/0/0/2',
                                                'neighbor_address': '2001:11:11::12'}}},
                                    '2001:10:10::13/128': 
                                        {'path': 
                                            {'2001:11:11::13 GigabitEthernet0/0/0/3 13': 
                                                {'admin_distance': 13,
                                                'interface_name': 'GigabitEthernet0/0/0/3',
                                                'neighbor_address': '2001:11:11::13'}}},
                                    '2001:10:10::14/128': 
                                        {'path': 
                                            {'2001:11:11::14 GigabitEthernet0/0/0/4 14': 
                                                {'admin_distance': 14,
                                                'interface_name': 'GigabitEthernet0/0/0/4',
                                                'neighbor_address': '2001:11:11::14'}}},
                                    '2001:10:10::15/128': 
                                        {'path': 
                                            {'2001:11:11::15 GigabitEthernet0/0/0/5 15': 
                                                {'admin_distance': 15,
                                                'interface_name': 'GigabitEthernet0/0/0/5',
                                                'neighbor_address': '2001:11:11::15'}}}}}}}}}

    golden_output2 = {'execute.return_value': '''
        RP/0/0/CPU0:R2# show pim vrf default ipv6 mstatic
        Mon May 29 14:37:26.421 UTC
        IP Multicast Static Routes Information

         * 2001:10:10::10/128 via GigabitEthernet0/0/0/0 with nexthop 2001:11:11::10 and distance 10 
         * 2001:10:10::11/128 via GigabitEthernet0/0/0/1 with nexthop 2001:11:11::11 and distance 11 
         * 2001:10:10::12/128 via GigabitEthernet0/0/0/2 with nexthop 2001:11:11::12 and distance 12
         * 2001:10:10::13/128 via GigabitEthernet0/0/0/3 with nexthop 2001:11:11::13 and distance 13
         * 2001:10:10::14/128 via GigabitEthernet0/0/0/4 with nexthop 2001:11:11::14 and distance 14
         * 2001:10:10::15/128 via GigabitEthernet0/0/0/5 with nexthop 2001:11:11::15 and distance 15
        '''}

    def test_show_pim_vrf_mstatic_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowPimVrfMstatic(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_pim_vrf_default_ipv4_mstatic_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowPimVrfMstatic(device=self.device)
        parsed_output = obj.parse(vrf='default', af='ipv4')
        self.assertEqual(parsed_output,self.golden_parsed_output1)

    def test_show_pim_vrf_default_ipv6_mstatic_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowPimVrfMstatic(device=self.device)
        parsed_output = obj.parse(vrf='default', af='ipv6')
        self.assertEqual(parsed_output,self.golden_parsed_output2)


if __name__ == '__main__':
    unittest.main()