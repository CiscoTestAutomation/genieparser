import unittest
from unittest.mock import Mock

# pyATS
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from genie.libs.parser.asa.show_vpn_sessiondb import ShowVPNSessionDBSummary,\
                                                     ShowVpnSessiondb, \
                                                     ShowVpnSessiondbAnyconnect, \
                                                     ShowVpnSessiondbWebvpn


# ============================================
# unit test for 'show vpn-sessiondb summary'
# =============================================
class TestShowVpnSessionDBSummary(unittest.TestCase):
    '''
       unit test for show vpn-sessiondb summary
    '''
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    maxDiff = None
    golden_parsed_output = {
        'device_load': 1,
        'device_total_vpn_capacity': 250,
        'ikev1_ipsec_l2tp_ip_sec': {
            'active': 2,
            'cumulative': 2,
            'peak_concurrent': 2,
        },
        'load_balancing_encryption': {
            'active': 0,
            'cumulative': 6,
            'peak_concurrent': 1,
        },
        'total_active_and_inactive': 2,
        'total_cumulative': 8,
    }

    golden_output = {'execute.return_value': '''
        vASA-VPN-20#show vpn-sessiondb summary 

        show vpn-sessiondb summary
        ---------------------------------------------------------------------------
        VPN Session Summary                                                        
        ---------------------------------------------------------------------------
                                    Active : Cumulative : Peak Concur : Inactive
                                    ----------------------------------------------
        IKEv1 IPsec/L2TP IPsec       :      2 :          2 :           2
        Load Balancing(Encryption)   :      0 :          6 :           1
        ---------------------------------------------------------------------------
        Total Active and Inactive    :      2             Total Cumulative :      8
        Device Total VPN Capacity    :    250
        Device Load                  :     1%
          '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowVPNSessionDBSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        route_obj = ShowVPNSessionDBSummary(device=self.device)
        parsed_output = route_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


# ============================================
# unit test for 'show vpn-sessiondb'
# =============================================
class TestShowVpnSessiondb(unittest.TestCase):
    """
    Unit test for
        * show vpn-sessiondb
    """
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    # show vpn-sessiondb
    golden_output = {'execute.return_value': ''' 
    Session Type: SSL VPN Client
     
    Username : lee
    Index : 1 IP Addr : 192.168.16.232
    Protocol : SSL VPN Client Encryption : 3DES
    Hashing : SHA1 Auth Mode : userPassword
    TCP Dst Port : 443 TCP Src Port : 54230
    Bytes Tx : 20178 Bytes Rx : 8662
    Pkts Tx : 27 Pkts Rx : 19
    Client Ver : Cisco STC 10.4.0.117
    Client Type : Internet Explorer
    Group : DfltGrpPolicy
    Login Time : 14:32:03 UTC Wed Mar 20 2007
    Duration : 0h:00m:04s
    Inactivity : 0h:00m:04s
    Filter Name :
    '''}

    golden_parsed_output = {
    'session_type': {
        'SSL VPN Client': {
            'username': {
                'lee': {
                    'index': {
                        1: {
                            'auth_mode': 'userPassword',
                            'bytes': {
                                'rx': 8662,
                                'tx': 20178,
                            },
                            'client_type': 'Internet Explorer',
                            'client_version': 'Cisco STC 10.4.0.117',
                            'duration': '0h:00m:04s',
                            'group': 'DfltGrpPolicy',
                            'hashing': 'SHA1',
                            'inactivity': '0h:00m:04s',
                            'ip_addr': '192.168.16.232',
                            'login_time': '14:32:03 UTC Wed Mar 20 2007',
                            'pkts': {
                                'rx': 19,
                                'tx': 27,
                            },
                            'protocol': 'SSL',
                            'tcp': {
                                'dst_port': 443,
                                'src_port': 54230,
                            },
                            'vpn_client_encryption': '3DES',
                        },
                    },
                },
            },
        },
    },
}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowVpnSessiondb(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        route_obj = ShowVpnSessiondb(device=self.device)
        parsed_output = route_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


# ============================================
# unit test for
#         * show vpn-sessiondb anyconnect
#         * show vpn-sessiondb anyconnect sort inactivity
# =============================================
class TestShowVpnSessiondbAnyconnect(unittest.TestCase):
    """
    Unit test for
         * show vpn-sessiondb anyconnect
         * show vpn-sessiondb anyconnect sort inactivity
    """
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    # show vpn-sessiondb anyconnect
    golden_output_2 = {'execute.return_value': '''     
        Session Type: AnyConnect

        Username : lee Index : 1
        Assigned IP : 192.168.246.1 Public IP : 10.139.1.2
        Protocol : AnyConnect-Parent SSL-Tunnel DTLS-Tunnel
        License : AnyConnect Premium
        Encryption : RC4 AES128 Hashing : SHA1
        Bytes Tx : 11079 Bytes Rx : 4942
        Group Policy : EngPolicy Tunnel Group : EngGroup
        Login Time : 15:25:13 EST Fri Jan 28 2011
        Duration : 0h:00m:15s
        Inactivity : 0h:00m:00s
        NAC Result : Unknown
        VLAN Mapping : N/A VLAN : none

        Username : yumi Index : 2
        Assigned IP : 192.168.246.2 Public IP : 10.139.1.3
        Protocol : AnyConnect-Parent SSL-Tunnel DTLS-Tunnel
        License : AnyConnect Premium
        Encryption : RC4 AES128 Hashing : SHA1
        Bytes Tx : 11055 Bytes Rx : 6942
        Group Policy : EngPolicy Tunnel Group : EngGroup
        Login Time : 15:25:13 EST Fri Jan 29 2011
        Duration : 0h:05m:15s
        Inactivity : 0h:00m:00s
        NAC Result : Unknown
        VLAN Mapping : N/A VLAN : none
        '''}

    golden_parsed_output_2 = {
        'session_type': {
            'AnyConnect': {
                'username': {
                    'lee': {
                        'index': {
                            1: {
                                'assigned_ip': '192.168.246.1',
                                'bytes': {
                                    'rx': 4942,
                                    'tx': 11079,
                                },
                                'duration': '0h:00m:15s',
                                'encryption': 'RC4 AES128',
                                'group_policy': 'EngPolicy',
                                'hashing': 'SHA1',
                                'inactivity': '0h:00m:00s',
                                'license': 'AnyConnect Premium',
                                'login_time': '15:25:13 EST Fri Jan 28 2011',
                                'nac_result': 'Unknown',
                                'protocol': 'AnyConnect-Parent SSL-Tunnel DTLS-Tunnel',
                                'public_ip': '10.139.1.2',
                                'tunnel_group': 'EngGroup',
                                'vlan': 'none',
                                'vlan_mapping': 'N/A',
                            },
                        },
                    },
                    'yumi': {
                        'index': {
                            2: {
                                'assigned_ip': '192.168.246.2',
                                'bytes': {
                                    'rx': 6942,
                                    'tx': 11055,
                                },
                                'duration': '0h:05m:15s',
                                'encryption': 'RC4 AES128',
                                'group_policy': 'EngPolicy',
                                'hashing': 'SHA1',
                                'inactivity': '0h:00m:00s',
                                'license': 'AnyConnect Premium',
                                'login_time': '15:25:13 EST Fri Jan 29 2011',
                                'nac_result': 'Unknown',
                                'protocol': 'AnyConnect-Parent SSL-Tunnel DTLS-Tunnel',
                                'public_ip': '10.139.1.3',
                                'tunnel_group': 'EngGroup',
                                'vlan': 'none',
                                'vlan_mapping': 'N/A',
                            },
                        },
                    },
                },
            },
        },
    }

    # show vpn-sessiondb anyconnect sort inactivity
    golden_output_3 = {'execute.return_value': '''
        Session Type: AnyConnect

        Username : user1 Index : 37670
        Assigned IP : 10.10.10.80 Public IP : 2.22.2.2
        Protocol : AnyConnect-Parent
        License : AnyConnect Premium
        Encryption : AnyConnect-Parent: (1)none
        Hashing : AnyConnect-Parent: (1)none
        Bytes Tx : 92531620 Bytes Rx : 38126521
        Group Policy : GroupPolicy_Employee
        Tunnel Group : Employee
        Login Time : 15:56:33 CDT Fri Mar 13 2020
        Duration : 2d 4h:21m:44s
        Inactivity : 1d 9h:13m:24s
        VLAN Mapping : N/A VLAN : none
        Audt Sess ID : 0adc27fd093260005381
        Security Grp : none

        Username : user1 Index : 56867
        Assigned IP : 10.10.10.213 Public IP : 1.1.1.1
        Protocol : AnyConnect-Parent
        License : AnyConnect Premium
        Encryption : AnyConnect-Parent: (1)none
        Hashing : AnyConnect-Parent: (1)none
        Bytes Tx : 18318907 Bytes Rx : 5297986
        Group Policy : GroupPolicy_Employee
        Tunnel Group : Employee
        Login Time : 08:36:57 CDT Sat Mar 14 2020
        Duration : 1d 11h:41m:20s
        Inactivity : 1d 9h:04m:29s
        VLAN Mapping : N/A VLAN : none
        Audt Sess ID : 0adc27fd0de230005e6f9
        Security Grp : none
        '''}

    golden_parsed_output_3 = {
        'session_type': {
            'AnyConnect': {
                'username': {
                    'user1': {
                        'index': {
                            37670: {
                                'assigned_ip': '10.10.10.80',
                                'audt_sess_id': '0adc27fd093260005381',
                                'bytes': {
                                    'rx': 38126521,
                                    'tx': 92531620,
                                },
                                'duration': '2d 4h:21m:44s',
                                'encryption': '(1)none',
                                'group_policy': 'GroupPolicy_Employee',
                                'hashing': '(1)none',
                                'inactivity': '1d 9h:13m:24s',
                                'license': 'AnyConnect Premium',
                                'login_time': '15:56:33 CDT Fri Mar 13 2020',
                                'protocol': 'AnyConnect-Parent',
                                'public_ip': '2.22.2.2',
                                'security_group': 'none',
                                'tunnel_group': 'Employee',
                                'vlan': 'none',
                                'vlan_mapping': 'N/A',
                            },
                            56867: {
                                'assigned_ip': '10.10.10.213',
                                'audt_sess_id': '0adc27fd0de230005e6f9',
                                'bytes': {
                                    'rx': 5297986,
                                    'tx': 18318907,
                                },
                                'duration': '1d 11h:41m:20s',
                                'encryption': '(1)none',
                                'group_policy': 'GroupPolicy_Employee',
                                'hashing': '(1)none',
                                'inactivity': '1d 9h:04m:29s',
                                'license': 'AnyConnect Premium',
                                'login_time': '08:36:57 CDT Sat Mar 14 2020',
                                'protocol': 'AnyConnect-Parent',
                                'public_ip': '1.1.1.1',
                                'security_group': 'none',
                                'tunnel_group': 'Employee',
                                'vlan': 'none',
                                'vlan_mapping': 'N/A',
                            },
                        },
                    },
                },
            },
        },
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowVpnSessiondbAnyconnect(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        route_obj = ShowVpnSessiondbAnyconnect(device=self.device)
        parsed_output = route_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_3)
        route_obj = ShowVpnSessiondbAnyconnect(device=self.device)
        parsed_output = route_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_3)


# =============================================
# Unit test for
#     * show vpn-sessiondb webvpn
# =============================================
class TestShowVpnSessiondbWebvpn(unittest.TestCase):
    """
    Unit test for
         * show vpn-sessiondb webvpn
    """
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    # show vpn-sessiondb webvpn
    golden_output_4 = {'execute.return_value': '''
        Session Type: WebVPN

        Username     : admin                  Index        : 3
        Public IP    : 10.229.20.77
        Protocol     : Clientless
        License      : AnyConnect Premium
        Encryption   : Clientless: (1)AES128  Hashing      : Clientless: (1)SHA256
        Bytes Tx     : 72214                  Bytes Rx     : 270241
        Group Policy : WEBVPN_Group_Policy    Tunnel Group : DefaultWEBVPNGroup
        Login Time   : 10:40:04 UTC Tue May 26 2015
        Duration     : 0h:05m:21s
        Inactivity   : 0h:00m:00s
        VLAN Mapping : N/A                    VLAN         : none
        Audt Sess ID : 0a1516010000300055644d84
        Security Grp : none
        '''}

    golden_parsed_output_4 = {
        'session_type': {
            'WebVPN': {
                'username': {
                    'admin': {
                        'index': {
                            3: {
                                'audt_sess_id': '0a1516010000300055644d84',
                                'bytes': {
                                    'rx': 270241,
                                    'tx': 72214,
                                },
                                'duration': '0h:05m:21s',
                                'encryption': '(1)AES128',
                                'group_policy': 'WEBVPN_Group_Policy',
                                'hashing': '(1)SHA256',
                                'inactivity': '0h:00m:00s',
                                'license': 'AnyConnect Premium',
                                'login_time': '10:40:04 UTC Tue May 26 2015',
                                'protocol': 'Clientless',
                                'public_ip': '10.229.20.77',
                                'security_group': 'none',
                                'tunnel_group': 'DefaultWEBVPNGroup',
                                'vlan': 'none',
                                'vlan_mapping': 'N/A',
                            },
                        },
                    },
                },
            },
        },
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowVpnSessiondbAnyconnect(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_4)
        route_obj = ShowVpnSessiondb(device=self.device)
        parsed_output = route_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_4)


if __name__ == '__main__':
    unittest.main()