
# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_pim
from genie.libs.parser.iosxr.show_pim import ShowPimVrfMstatic, ShowPimVrfRpfSummary,\
                                  ShowPimVrfInterfaceDetail


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

    def test_show_pim_vrf_default_ipv6_mstatic_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowPimVrfMstatic(device=self.device)
        parsed_output = obj.parse(vrf='default', af='ipv6')
        self.assertEqual(parsed_output,self.golden_parsed_output2)


# ============================================================
#  Unit test for 'show pim vrf <WORD> <WORD> interface detail'
# ============================================================

class test_show_pim_vrf_interface_detail(unittest.TestCase):

    '''Unit test for 'show pim vrf <WORD> <WORD> interface detail'''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf':
            {'default':
                {'interfaces':
                    {'GigabitEthernet0/0/0/0':
                        {'address_family':
                            {'ipv4':
                                {'address': ['10.2.3.2'],
                                'bfd':
                                    {'enable': False,
                                    'interval': 0.150,
                                    'detection_multiplier': 3,
                                    },
                                'dr': 'this system',
                                'dr_priority': 1,
                                'flags': 'B P',
                                'hello_interval': 30,
                                'hello_expiration': '00:00:01',
                                'nbr_count': 1,
                                'neighbor_filter': '-',
                                'override_interval': 2500,
                                'oper_status': 'on',
                                'primary_address': '10.2.3.2',
                                'propagation_delay': 500}}},
                    'GigabitEthernet0/0/0/1':
                        {'address_family':
                            {'ipv4':
                                {'address': ['10.1.2.2'],
                                'bfd':
                                    {'enable': False,
                                    'interval': 0.150,
                                    'detection_multiplier': 3,
                                    },
                                'dr': '10.1.2.3',
                                'dr_priority': 1,
                                'flags': 'NB P',
                                'hello_interval': 30,
                                'hello_expiration': '00:00:07',
                                'nbr_count': 2,
                                'neighbor_filter': '-',
                                'override_interval': 2500,
                                'oper_status': 'on',
                                'primary_address': '10.1.2.2',
                                'propagation_delay': 500}}},
                    'Loopback0':
                        {'address_family':
                            {'ipv4':
                                {'address': ['10.16.2.2'],
                                'bfd':
                                    {'enable': False,
                                    'interval': 0.150,
                                    'detection_multiplier': 3,
                                    },
                                'dr': 'this system',
                                'dr_priority': 1,
                                'flags': 'B P V',
                                'hello_interval': 30,
                                'hello_expiration': '00:00:15',
                                'nbr_count': 1,
                                'neighbor_filter': '-',
                                'override_interval': 2500,
                                'oper_status': 'on',
                                'primary_address': '10.16.2.2',
                                'propagation_delay': 500}}}}}}}

    golden_output1 = {'execute.return_value': '''
        RP/0/0/CPU0:R2#show pim vrf default ipv4 interface detail
        Mon May 29 14:41:28.444 UTC

        PIM interfaces in VRF default
        IP PIM Multicast Interface State
        Flag: B - Bidir enabled, NB - Bidir disabled
              P - PIM Proxy enabled, NP - PIM Proxy disabled
              V - Virtual Interface
        BFD State - State/Interval/Multiplier

        Interface                  PIM  Nbr   Hello  DR
                                        Count Intvl  Prior

        Loopback0                   on   1     30     1
            Primary Address : 10.16.2.2
                      Flags : B P V
                        BFD : Off/150 ms/3
                         DR : this system
          Propagation delay : 500
          Override Interval : 2500
                Hello Timer : 00:00:15
            Neighbor Filter : -

        GigabitEthernet0/0/0/0      on   1     30     1
            Primary Address : 10.2.3.2
                      Flags : B P
                        BFD : Off/150 ms/3
                         DR : this system
          Propagation delay : 500
          Override Interval : 2500
                Hello Timer : 00:00:01
            Neighbor Filter : -

        GigabitEthernet0/0/0/1      on   2     30     1
            Primary Address : 10.1.2.2
                      Flags : NB P
                        BFD : Off/150 ms/3
                         DR : 10.1.2.3
          Propagation delay : 500
          Override Interval : 2500
                Hello Timer : 00:00:07
            Neighbor Filter : -
        '''}

    golden_parsed_output2 = {
        'vrf':
            {'default':
                {'interfaces':
                    {'GigabitEthernet0/0/0/0':
                        {'address_family':
                            {'ipv6':
                                {'address': ['fe80::5054:ff:fee4:f669', '2001:db8:2:3::2'],
                                'bfd':
                                    {'enable': False,
                                    'interval': 0.150,
                                    'detection_multiplier': 3,
                                    },
                                'dr': 'this system',
                                'dr_priority': 1,
                                'flags': 'B P NA',
                                'hello_interval': 30,
                                'hello_expiration': '00:00:22',
                                'nbr_count': 1,
                                'neighbor_filter': '-',
                                'override_interval': 2500,
                                'oper_status': 'on',
                                'primary_address': 'fe80::5054:ff:fee4:f669',
                                'propagation_delay': 500}}},
                    'GigabitEthernet0/0/0/1':
                        {'address_family':
                            {'ipv6':
                                {'address': ['fe80::5054:ff:feac:64b3', '2001:db8:1:2::2'],
                                'bfd':
                                    {'enable': False,
                                    'interval': 0.150,
                                    'detection_multiplier': 3,
                                    },
                                'dr': 'this system',
                                'dr_priority': 1,
                                'flags': 'B P NA',
                                'hello_interval': 30,
                                'hello_expiration': '00:00:02',
                                'nbr_count': 1,
                                'neighbor_filter': '-',
                                'override_interval': 2500,
                                'oper_status': 'off',
                                'primary_address': 'fe80::5054:ff:feac:64b3',
                                'propagation_delay': 500}}},
                    'Loopback0':
                        {'address_family':
                            {'ipv6':
                                {'address': ['fe80::85c6:bdff:fe62:61e', '2001:db8:2:2::2'],
                                'bfd':
                                    {'enable': False,
                                    'interval': 0.150,
                                    'detection_multiplier': 3,
                                    },
                                'dr': 'this system',
                                'dr_priority': 1,
                                'flags': 'B P NA V',
                                'hello_interval': 30,
                                'hello_expiration': '00:00:19',
                                'nbr_count': 1,
                                'neighbor_filter': '-',
                                'override_interval': 2500,
                                'oper_status': 'on',
                                'primary_address': 'fe80::85c6:bdff:fe62:61e',
                                'propagation_delay': 500}}}}}}}

    golden_output2 = {'execute.return_value': '''
        RP/0/0/CPU0:R2#show pim vrf default ipv6 interface detail
        Mon May 29 14:41:52.972 UTC

        PIM interfaces in VRF default
        IP PIM Multicast Interface State
        Flag: B - Bidir enabled, NB - Bidir disabled
              P - PIM Proxy enabled, NP - PIM Proxy disabled
              A - PIM Assert batching capable, NA - PIM Assert batching incapable
              V - Virtual Interface

        Interface                  PIM  Nbr   Hello  DR
                                        Count Intvl  Prior

        Loopback0                   on   1     30     1
            Primary Address : fe80::85c6:bdff:fe62:61e
                    Address : 2001:db8:2:2::2
                      Flags : B P NA V
                        BFD : Off/150 ms/3
                         DR : this system

          Propagation delay : 500
          Override Interval : 2500
                Hello Timer : 00:00:19
            Neighbor Filter : -

        GigabitEthernet0/0/0/0      on   1     30     1
            Primary Address : fe80::5054:ff:fee4:f669
                    Address : 2001:db8:2:3::2
                      Flags : B P NA
                        BFD : Off/150 ms/3
                         DR : this system

          Propagation delay : 500
          Override Interval : 2500
                Hello Timer : 00:00:22
            Neighbor Filter : -

        GigabitEthernet0/0/0/1off         1     30     1
            Primary Address : fe80::5054:ff:feac:64b3
                    Address : 2001:db8:1:2::2
                      Flags : B P NA
                        BFD : Off/150 ms/3
                         DR : this system

          Propagation delay : 500
          Override Interval : 2500
                Hello Timer : 00:00:02
            Neighbor Filter : -
        '''}

    def test_show_pim_vrf_interface_detail_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowPimVrfInterfaceDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_pim_vrf_default_ipv4_interface_detail_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowPimVrfInterfaceDetail(device=self.device)
        parsed_output = obj.parse(vrf='default', af='ipv4')
        self.assertEqual(parsed_output,self.golden_parsed_output1)

    def test_show_pim_vrf_default_ipv6_interface_detail_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowPimVrfInterfaceDetail(device=self.device)
        parsed_output = obj.parse(vrf='default', af='ipv6')
        self.assertEqual(parsed_output,self.golden_parsed_output2)


# =======================================================
#  Unit test for 'show pim vrf <WORD> <WORD> rpf summary'
# =======================================================

class test_show_pim_vrf_rpf_summary(unittest.TestCase):

    '''Unit test for 'show pim vrf <WORD> <WORD> rpf summary'''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf':
            {'default':
                {'address_family':
                    {'ipv4':
                        {'default_rpf_table': 'IPv4-Unicast-default',
                        'isis_mcast_topology': False,
                        'mo_frr_flow_based': False,
                        'mo_frr_rib': False,
                        'multipath': True,
                        'pim_rpfs_registered': 'Unicast RIB table',
                        'rib_convergence_time_left': '00:00:00',
                        'rib_convergence_timeout': '00:30:00',
                        'rump_mu_rib': False,
                        'table':
                            {'IPv4-Unicast-default':
                                {'pim_rpf_registrations': 1,
                                'rib_table_converged': True}}}}}}}

    golden_output1 = {'execute.return_value': '''
        RP/0/0/CPU0:R2#show pim vrf default ipv4 rpf summary
        Mon May 29 14:42:47.569 UTC
            ISIS Mcast Topology Not configured
            MoFRR Flow-based    Not configured
            MoFRR RIB           Not configured
            RUMP MuRIB          Not enabled

        PIM RPFs registered with Unicast RIB table

        Default RPF Table: IPv4-Unicast-default
        RIB Convergence Timeout Value: 00:30:00
        RIB Convergence Time Left:     00:00:00
        Multipath RPF Selection is Enabled

        Table: IPv4-Unicast-default
            PIM RPF Registrations = 1
            RIB Table converged
        '''}

    golden_parsed_output2 = {
        'vrf':
            {'default':
                {'address_family':
                    {'ipv6':
                        {'default_rpf_table': 'IPv6-Unicast-default',
                        'isis_mcast_topology': False,
                        'mo_frr_flow_based': False,
                        'mo_frr_rib': False,
                        'multipath': True,
                        'pim_rpfs_registered': 'Unicast RIB table',
                        'rib_convergence_time_left': '00:00:00',
                        'rib_convergence_timeout': '00:30:00',
                        'rump_mu_rib': False,
                        'table':
                            {'IPv6-Unicast-default':
                                {'pim_rpf_registrations': 0,
                                'rib_table_converged': True}}}}}}}

    golden_output2 = {'execute.return_value': '''
        RP/0/0/CPU0:R2#show pim vrf default ipv6 rpf summary
        Mon May 29 14:42:53.538 UTC
            ISIS Mcast Topology Not configured
            MoFRR Flow-based    Not configured
            MoFRR RIB           Not configured
            RUMP MuRIB          Not enabled

        PIM RPFs registered with Unicast RIB table

        Default RPF Table: IPv6-Unicast-default
        RIB Convergence Timeout Value: 00:30:00
        RIB Convergence Time Left:     00:00:00
        Multipath RPF Selection is Enabled

        Table: IPv6-Unicast-default
            PIM RPF Registrations = 0
            RIB Table converged
        '''}

    def test_show_pim_vrf_rpf_summary_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowPimVrfRpfSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_pim_vrf_default_ipv4_rpf_summary_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowPimVrfRpfSummary(device=self.device)
        parsed_output = obj.parse(vrf='default', af='ipv4')
        self.assertEqual(parsed_output,self.golden_parsed_output1)

    def test_show_pim_vrf_default_ipv6_rpf_summary_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowPimVrfRpfSummary(device=self.device)
        parsed_output = obj.parse(vrf='default', af='ipv6')
        self.assertEqual(parsed_output,self.golden_parsed_output2)


if __name__ == '__main__':
    unittest.main()
