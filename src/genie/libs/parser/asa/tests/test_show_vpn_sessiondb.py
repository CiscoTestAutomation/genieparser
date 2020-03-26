import unittest
from unittest.mock import Mock

# pyATS
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from genie.libs.parser.asa.show_vpn_sessiondb import ShowVPNSessionDBSummary,\
                                                     ShowVpnSessiondbAnyconnect, \
                                                     ShowVpnSessiondbWebvpn


# ============================================
# unit test for
#       * show vpn-sessiondb summary
#       * show vpn-sessiondb
# =============================================
class TestShowVpnSessionDBSummary(unittest.TestCase):
    """
    unit test for
            * show vpn-sessiondb summary
            * show vpn-sessiondb
    """

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    maxDiff = None

    # show vpn-sessiondb summary
    golden_output = {'execute.return_value': '''
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

    golden_parsed_output = {
        'summary': {
            'VPN Session': {
                'device_load': 0.01,
                'device_total_vpn_capacity': 250,
                'session': {
                    'IKEv1 IPsec/L2TP IPsec': {
                        'active': 2,
                        'cumulative': 2,
                        'peak_concurrent': 2,
                    },
                    'Load Balancing(Encryption)': {
                        'active': 0,
                        'cumulative': 6,
                        'peak_concurrent': 1,
                    },
                },
                'total_active_and_inactive': 2,
                'total_cumulative': 8,
            },
        },
    }

    # show vpn-sessiondb
    golden_output_2 = {'execute.return_value': ''' 
    ---------------------------------------------------------------------------
    VPN Session Summary
    ---------------------------------------------------------------------------
                                   Active : Cumulative : Peak Concur : Inactive
                                 ----------------------------------------------
    AnyConnect Client            :    127 :        432 :         205 :        0
      SSL/TLS/DTLS               :    127 :        432 :         205 :        0
      IKEv2 IPsec                :      8 :         17 :           8 :        0
    Clientless VPN               :      0 :          1 :           1
      Browser                    :      0 :          1 :           1
    Site-to-Site VPN             :     29 :         59 :          29
      IKEv2 IPsec                :     29 :         59 :          29
    ---------------------------------------------------------------------------
    Total Active and Inactive    :    127             Total Cumulative :    432
    Device Total VPN Capacity    :   5000
    Device Load                  :     0%
    ---------------------------------------------------------------------------

    ---------------------------------------------------------------------------
    Tunnels Summary
    ---------------------------------------------------------------------------
                                   Active : Cumulative : Peak Concurrent   
                                 ----------------------------------------------
    Clientless                   :      0 :          1 :               1                                 
    AnyConnect-Parent            :    127 :        432 :             205
    SSL-Tunnel                   :    125 :       1577 :             204
    DTLS-Tunnel                  :    124 :       1508 :             202
    ---------------------------------------------------------------------------
    Totals                       :    376 :       3518
    ---------------------------------------------------------------------------
    '''}

    golden_parsed_output_2 = {
        'summary': {
            'Tunnels': {
                'session': {
                    'AnyConnect-Parent': {
                        'active': 127,
                        'cumulative': 432,
                        'peak_concurrent': 205,
                    },
                    'Clientless': {
                        'active': 0,
                        'cumulative': 1,
                        'peak_concurrent': 1
                    },
                    'DTLS-Tunnel': {
                        'active': 124,
                        'cumulative': 1508,
                        'peak_concurrent': 202,
                    },
                    'SSL-Tunnel': {
                        'active': 125,
                        'cumulative': 1577,
                        'peak_concurrent': 204,
                    },
                },
                'totals': {
                    'active': 376,
                    'cumulative': 3518,
                },
            },
            'VPN Session': {
                'session': {
                    'AnyConnect Client': {
                        'active': 127,
                        'cumulative': 432,
                        'inactive': 0,
                        'peak_concurrent': 205,
                        'type': {
                            'SSL/TLS/DTLS': {
                                'active': 127,
                                'cumulative': 432,
                                'inactive': 0,
                                'peak_concurrent': 205,
                            },
                            'IKEv2 IPsec': {
                                'active': 8,
                                'cumulative': 17,
                                'inactive': 0,
                                'peak_concurrent': 8
                            },
                        },
                    },
                    'Clientless VPN': {
                        'active': 0,
                        'type': {
                            'Browser': {
                                'active': 0,
                                'cumulative': 1,
                                'peak_concurrent': 1,
                            },
                        },
                        'cumulative': 1,
                        'peak_concurrent': 1,
                    },
                    'Site-to-Site VPN': {
                        'active': 29,
                        'cumulative': 59,
                        'type': {
                            'IKEv2 IPsec': {
                                'active': 29,
                                'cumulative': 59,
                                'peak_concurrent': 29
                            },
                        },
                        'peak_concurrent': 29
                    },
                },
                'device_load': 0.0,
                'device_total_vpn_capacity': 5000,
                'total_active_and_inactive': 127,
                'total_cumulative': 432,
            },
        },
    }

    # show vpn-sessiondb summary
    golden_output_3 = {'execute.return_value': ''' 
    ---------------------------------------------------------------------------
    VPN Session Summary
    ---------------------------------------------------------------------------
                                   Active : Cumulative : Peak Concur : Inactive
                                 ----------------------------------------------
    AnyConnect Client            :   1672 :     140011 :        2219 :        355
      SSL/TLS/DTLS               :   1672 :     140011 :        2219 :        355
    Clientless VPN               :   2    :     125    :            6
      Browser                    :   2    :     125    :            6
    ---------------------------------------------------------------------------
    Total Active and Inactive    :    2029             Total Cumulative :    1140136
    Device Total VPN Capacity    :    5000
    Device Load                  :    41%
    ---------------------------------------------------------------------------
    '''}

    golden_parsed_output_3 = {
        'summary': {
            'VPN Session': {
                'session': {
                    'AnyConnect Client': {
                        'active': 1672,
                        'cumulative': 140011,
                        'inactive': 355,
                        'peak_concurrent': 2219,
                        'type': {
                            'SSL/TLS/DTLS': {
                                'active': 1672,
                                'cumulative': 140011,
                                'inactive': 355,
                                'peak_concurrent': 2219,
                            },
                        },
                    },
                    'Clientless VPN': {
                        'active': 2,
                        'type': {
                            'Browser': {
                                'active': 2,
                                'cumulative': 125,
                                'peak_concurrent': 6,
                            },
                        },
                        'cumulative': 125,
                        'peak_concurrent': 6,
                    },
                },
                'device_load': 0.41,
                'device_total_vpn_capacity': 5000,
                'total_active_and_inactive': 2029,
                'total_cumulative': 1140136,
            },
        },
    }

    # show vpn-sessiondb
    golden_output_4 = {'execute.return_value': '''
    show vpn-sessiondb

    ---------------------------------------------------------------------------
    
    VPN Session Summary                                                        
    
    ---------------------------------------------------------------------------
    
                                   Active : Cumulative : Peak Concur : Inactive
    
                                 ----------------------------------------------
    
    Clientless VPN               :      0 :          1 :           1
    
      Browser                    :      0 :          1 :           1
    
    ---------------------------------------------------------------------------
    
    Total Active and Inactive    :      0             Total Cumulative :      1
    
    Device Total VPN Capacity    :    250
    
    Device Load                  :     0%
    
    ---------------------------------------------------------------------------
    
     
    
    ---------------------------------------------------------------------------
    
    Tunnels Summary
    
    ---------------------------------------------------------------------------
    
                                   Active : Cumulative : Peak Concurrent   
    
                                 ----------------------------------------------
    
    Clientless                   :      0 :          1 :               1
    
    ---------------------------------------------------------------------------
    
    Totals                       :      0 :          1
    
    ---------------------------------------------------------------------------
    '''}

    golden_parsed_output_4 = {
        'summary': {
            'Tunnels': {
                'session': {
                    'Clientless': {
                        'active': 0,
                        'cumulative': 1,
                        'peak_concurrent': 1,
                    },
                },
                'totals': {
                    'active': 0,
                    'cumulative': 1,
                },
            },
            'VPN Session': {
                'device_load': 0.0,
                'device_total_vpn_capacity': 250,
                'session': {
                    'Clientless VPN': {
                        'active': 0,
                        'cumulative': 1,
                        'peak_concurrent': 1,
                        'type': {
                            'Browser': {
                                'active': 0,
                                'cumulative': 1,
                                'peak_concurrent': 1,
                            },
                        },
                    },
                },
                'total_active_and_inactive': 0,
                'total_cumulative': 1,
            },
        },
    }

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

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        route_obj = ShowVPNSessionDBSummary(device=self.device)
        parsed_output = route_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_3(self):
        self.device = Mock(**self.golden_output_3)
        route_obj = ShowVPNSessionDBSummary(device=self.device)
        parsed_output = route_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_3)

    def test_golden_4(self):
        self.device = Mock(**self.golden_output_4)
        route_obj = ShowVPNSessionDBSummary(device=self.device)
        parsed_output = route_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_4)


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
    maxDiff = None

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
        Assigned IP : 10.10.10.80 Public IP : 10.66.2.2
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
        Assigned IP : 10.10.10.213 Public IP : 10.4.1.1
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
                                'public_ip': '10.66.2.2',
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
                                'public_ip': '10.4.1.1',
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

    # show vpn-sessiondb anyconnect
    golden_output_4 = {'execute.return_value': '''
    Session Type: AnyConnect
    
     
    
    Username     : xxxxxxxx               Index        : 1917
    
    Assigned IP  : x.x.x.x            Public IP    : x.x.x.x
    
    Protocol     : AnyConnect-Parent SSL-Tunnel
    
    License      : AnyConnect Premium, AnyConnect for Mobile
    
    Encryption   : AnyConnect-Parent: (1)none  SSL-Tunnel: (1)AES256
    
    Hashing      : AnyConnect-Parent: (1)none  SSL-Tunnel: (1)SHA1
    
    Bytes Tx     : 8360206                Bytes Rx     : 7533909
    
    Group Policy : GroupPolicy_Employee
    
    Tunnel Group : Employee
    
    Login Time   : 13:50:15 CDT Thu Mar 19 2020
    
    Duration     : 2h:26m:41s
    
    Inactivity   : 0h:00m:00s
    
    VLAN Mapping : N/A                    VLAN         : none
    
    Audt Sess ID : 0af034360077d0005e73bee7
    
    Security Grp : none                  
    
     
    
    Username     : xxxxxxxx               Index        : 18594
    
    Assigned IP  : x.x.x.x            Public IP    : x.x.x.x
    
    Protocol     : AnyConnect-Parent SSL-Tunnel DTLS-Tunnel
    
    License      : AnyConnect Premium
    
    Encryption   : AnyConnect-Parent: (1)none  SSL-Tunnel: (1)AES256  DTLS-Tunnel: (1)AES256
    
    Hashing      : AnyConnect-Parent: (1)none  SSL-Tunnel: (1)SHA1  DTLS-Tunnel: (1)SHA1
    
    Bytes Tx     : 26059343               Bytes Rx     : 12795265
    
    Group Policy : GroupPolicy_Employee
    
    Tunnel Group : Employee
    
    Login Time   : 09:48:37 CDT Thu Mar 19 2020
    
    Duration     : 6h:28m:19s
    
    Inactivity   : 0h:00m:00s
    
    VLAN Mapping : N/A                    VLAN         : none
    
    Audt Sess ID : 0af03436048a20005e738645
    
    Security Grp : none                  
           
    '''}

    golden_parsed_output_4 = {
    'session_type': {
        'AnyConnect': {
            'username': {
                'xxxxxxxx': {
                    'index': {
                        1917: {
                            'assigned_ip': 'x.x.x.x',
                            'audt_sess_id': '0af034360077d0005e73bee7',
                            'bytes': {
                                'rx': 7533909,
                                'tx': 8360206,
                            },
                            'duration': '2h:26m:41s',
                            'encryption': '(1)none',
                            'group_policy': 'GroupPolicy_Employee',
                            'hashing': '(1)none',
                            'inactivity': '0h:00m:00s',
                            'license': 'AnyConnect Premium, AnyConnect for Mobile',
                            'login_time': '13:50:15 CDT Thu Mar 19 2020',
                            'protocol': 'AnyConnect-Parent SSL-Tunnel',
                            'public_ip': 'x.x.x.x',
                            'security_group': 'none',
                            'ssl_tunnel': '(1)SHA1',
                            'tunnel_group': 'Employee',
                            'vlan': 'none',
                            'vlan_mapping': 'N/A',
                        },
                        18594: {
                            'assigned_ip': 'x.x.x.x',
                            'audt_sess_id': '0af03436048a20005e738645',
                            'bytes': {
                                'rx': 12795265,
                                'tx': 26059343,
                            },
                            'dtls_tunnel': '(1)SHA1',
                            'duration': '6h:28m:19s',
                            'encryption': '(1)none',
                            'group_policy': 'GroupPolicy_Employee',
                            'hashing': '(1)none',
                            'inactivity': '0h:00m:00s',
                            'license': 'AnyConnect Premium',
                            'login_time': '09:48:37 CDT Thu Mar 19 2020',
                            'protocol': 'AnyConnect-Parent SSL-Tunnel DTLS-Tunnel',
                            'public_ip': 'x.x.x.x',
                            'security_group': 'none',
                            'ssl_tunnel': '(1)SHA1',
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

    # show vpn-sessiondb anyconnect
    golden_output_5 = {'execute.return_value': '''
        Session Type: AnyConnect
        Username     : tpet2195               Index        : 5097
        Assigned IP  : 10.97.140.229          Public IP    : 172.16.4.118
        Protocol     : AnyConnect-Parent DTLS-Tunnel
        License      : AnyConnect Premium
        Encryption   : AnyConnect-Parent: (1)none  DTLS-Tunnel: (1)AES256
        Hashing      : AnyConnect-Parent: (1)none  DTLS-Tunnel: (1)SHA1
        Bytes Tx     : 694074707              Bytes Rx     : 257924006
        Group Policy : GroupPolicy_Employee_US_Z
        Tunnel Group : Employee_US_Z
        Login Time   : 13:45:06 CDT Tue Mar 17 2020
        Duration     : 6d 21h:39m:09s
        Inactivity   : 0h:09m:00s
        VLAN Mapping : N/A                    VLAN         : none
        Audt Sess ID : 0afd8115013e90005e711ab2
        Security Grp : none
        '''}

    golden_parsed_output_5 = {
        'session_type': {
            'AnyConnect': {
                'username': {
                    'tpet2195': {
                        'index': {
                            5097: {
                                'assigned_ip': '10.97.140.229',
                                'audt_sess_id': '0afd8115013e90005e711ab2',
                                'bytes': {
                                    'rx': 257924006,
                                    'tx': 694074707,
                                },
                                'dtls_tunnel': '(1)SHA1',
                                'duration': '6d 21h:39m:09s',
                                'encryption': '(1)none',
                                'group_policy': 'GroupPolicy_Employee_US_Z',
                                'hashing': '(1)none',
                                'inactivity': '0h:09m:00s',
                                'license': 'AnyConnect Premium',
                                'login_time': '13:45:06 CDT Tue Mar 17 2020',
                                'protocol': 'AnyConnect-Parent DTLS-Tunnel',
                                'public_ip': '172.16.4.118',
                                'security_group': 'none',
                                'tunnel_group': 'Employee_US_Z',
                                'vlan': 'none',
                                'vlan_mapping': 'N/A',
                            },
                        },
                    },
                },
            },
        },
    }

    # show vpn-sessiondb anyconnect
    golden_output_6 = {'execute.return_value': '''
    Session Type: AnyConnect

    Username : XXX
    Index : 62535
    Assigned IP : 10.25.112.2 Public IP : 10.69.27.37
    Protocol : AnyConnect-Parent SSL-Tunnel DTLS-Tunnel
    License : AnyConnect Premium
    Encryption : AnyConnect-Parent: (1)none SSL-Tunnel: (1)AES256 DTLS-Tunnel: (1)AES256
    Hashing : AnyConnect-Parent: (1)none SSL-Tunnel: (1)SHA1 DTLS-Tunnel: (1)SHA1
    Bytes Tx : 355483199 Bytes Rx : 187465614
    Group Policy : GroupPolicy_RSM_Auto_VPN_UserCert
    Tunnel Group : RSM_Auto_VPN_UserCert
    Login Time : 13:47:22 UTC Wed Mar 25 2020
    Duration : 1d 1h:36m:09s
    Inactivity : 0h:00m:00s
    VLAN Mapping : N/A VLAN : none
    Audt Sess ID : 42626e2b0f4470005e7b60ea
    Security Grp : none
    '''}

    golden_parsed_output_6 = {
        'session_type': {
            'AnyConnect': {
                'username': {
                    'XXX': {
                        'index': {
                            62535: {
                                'assigned_ip': '10.25.112.2',
                                'audt_sess_id': '42626e2b0f4470005e7b60ea',
                                'bytes': {
                                    'rx': 187465614,
                                    'tx': 355483199,
                                },
                                'dtls_tunnel': '(1)SHA1',
                                'duration': '1d 1h:36m:09s',
                                'encryption': '(1)none',
                                'group_policy': 'GroupPolicy_RSM_Auto_VPN_UserCert',
                                'hashing': '(1)none',
                                'inactivity': '0h:00m:00s',
                                'license': 'AnyConnect Premium',
                                'login_time': '13:47:22 UTC Wed Mar 25 2020',
                                'protocol': 'AnyConnect-Parent SSL-Tunnel DTLS-Tunnel',
                                'public_ip': '10.69.27.37',
                                'security_group': 'none',
                                'ssl_tunnel': '(1)SHA1',
                                'tunnel_group': 'RSM_Auto_VPN_UserCert',
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
        self.device = Mock(**self.golden_output_2)
        route_obj = ShowVpnSessiondbAnyconnect(device=self.device)
        parsed_output = route_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_3(self):
        self.device = Mock(**self.golden_output_3)
        route_obj = ShowVpnSessiondbAnyconnect(device=self.device)
        parsed_output = route_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_3)

    def test_golden_4(self):
        self.device = Mock(**self.golden_output_4)
        route_obj = ShowVpnSessiondbAnyconnect(device=self.device)
        parsed_output = route_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_4)

    def test_golden_5(self):
        self.device = Mock(**self.golden_output_5)
        route_obj = ShowVpnSessiondbAnyconnect(device=self.device)
        parsed_output = route_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_5)

    def test_golden_6(self):
        self.device = Mock(**self.golden_output_6)
        route_obj = ShowVpnSessiondbAnyconnect(device=self.device)
        parsed_output = route_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_6)


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
    maxDiff = None
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
        obj = ShowVpnSessiondbWebvpn(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output_4)
        route_obj = ShowVpnSessiondbWebvpn(device=self.device)
        parsed_output = route_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_4)


if __name__ == '__main__':
    unittest.main()