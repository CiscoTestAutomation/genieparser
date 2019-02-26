#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from genie.libs.parser.ios.show_dot1x import ShowDot1xAllDetail, \
                                    ShowDot1xAllSummary, \
                                    ShowDot1xAllCount


class test_show_dot1x_all_details(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        "version": 3,
        "interfaces": {
          "GigabitEthernet1/0/9": {
               "interface": "GigabitEthernet1/0/9",
               "max_start": 3,
               "pae": "supplicant",
               "credentials": 'switch4',
               'supplicant': {
                    'eap': {
                        'profile': 'EAP-METH'
                    }
                },
               "timeout": {
                    "held_period": 60,
                    "start_period": 30,
                    "auth_period": 30
               }
            }
        },
        "system_auth_control": True
    }

    golden_output = {'execute.return_value': '''\
        Sysauthcontrol                 Enabled
        Dot1x Protocol Version               3
        Dot1x Info for GigabitEthernet1/0/9
        --------------------------------------------
        PAE                       = SUPPLICANT
        StartPeriod               = 30
        AuthPeriod                = 30
        HeldPeriod                = 60
        MaxStart                  = 3
        Credentials profile       = switch4
        EAP profile               = EAP-METH
        Dot1x Supplicant Client List Empty
    '''
    }

    golden_parsed_output_1 = {
        "interfaces": {
            "FastEthernet7/1": {
               "interface": "FastEthernet7/1",
               "pae": "authenticator",
               "clients": {
                    "fa16.3e0b.b5b8": {
                         "session": {
                              "000000000000000E00110F79": {
                                   "session_id": "000000000000000E00110F79",
                                   "auth_bend_sm_state": "idle",
                                   "auth_sm_state": "held"
                              }
                         },
                         "eap_method": "md5",
                         "client": "fa16.3e0b.b5b8"
                    },
                    "fa16.3e42.fd85": {
                         "session": {
                              "000000000000000C00108250": {
                                   "session_id": "000000000000000C00108250",
                                   "auth_bend_sm_state": "idle",
                                   "auth_sm_state": "authenticated"
                              }
                         },
                         "eap_method": "md5",
                         "client": "fa16.3e42.fd85"
                    }
               },
               "host_mode": "single_host",
               "port_control": "auto",
               "max_reauth_req": 2,
               "re_authentication": False,
               "control_direction": "both",
               "max_req": 2,
               "timeout": {
                    "tx_period": 30,
                    "quiet_period": 60,
                    "auth_period": 3600,
                    "ratelimit_period": 0,
                    "server_timeout": 30,
                    "supp_timeout": 30
               }
            }
        },
         "system_auth_control": True,
         "version": 3
    }

    golden_output_1 = {'execute.return_value': '''\
        Sysauthcontrol                 Enabled
        Dot1x Protocol Version               3

        Dot1x Info for FastEthernet7/1
        -----------------------------------
        PAE                       = AUTHENTICATOR
        PortControl               = AUTO
        ControlDirection          = Both 
        HostMode                  = SINGLE_HOST
        ReAuthentication          = Disabled
        QuietPeriod               = 60
        ServerTimeout             = 30
        SuppTimeout               = 30
        ReAuthPeriod              = 3600 (Locally configured)
        ReAuthMax                 = 2
        MaxReq                    = 2
        TxPeriod                  = 30
        RateLimitPeriod           = 0
        Dot1x Authenticator Client List
        -------------------------------
        EAP Method                = MD5
        Supplicant                = fa16.3e0b.b5b8
        Session ID                = 000000000000000E00110F79
            Auth SM State         = HELD
            Auth BEND SM State    = IDLE

        EAP Method                = MD5
        Supplicant                = fa16.3e42.fd85
        Session ID                = 000000000000000C00108250
            Auth SM State         = AUTHENTICATED
            Auth BEND SM State    = IDLE
    '''
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowDot1xAllDetail(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowDot1xAllDetail(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_1(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_1)
        obj = ShowDot1xAllDetail(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_1)

class test_show_dot1x_all_summary(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        "interfaces": {
            "FastEthernet1": {
                "interface": "FastEthernet1",
                "clients": {
                    "000d.bcef.bfdc": {
                        "client": "000d.bcef.bfdc",
                        "status": "authorized",
                        "pae": "authenticator",
                    }
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        Interface             PAE             Client                         Status 
        ------------------------------------------------------------------------------------------
        Fa1                   AUTH             000d.bcef.bfdc           AUTHORIZED
    '''
    }

    golden_parsed_output_1 = {
        "interfaces": {
            "GigabitEthernet0/1": {
               "clients": {
                    "fa16.3ede.7048": {
                         "pae": "authenticator",
                         "status": "unauthorized",
                         "client": "fa16.3ede.7048"
                    },
                    "fa16.3ea5.663a": {
                         "pae": "authenticator",
                         "status": "authorized",
                         "client": "fa16.3ea5.663a"
                    },
                    "fa16.3ea5.663b": {
                         "pae": "supplicant",
                         "status": "authorized",
                         "client": "fa16.3ea5.663b"
                    },
                    "fa16.3ede.7049": {
                         "pae": "supplicant",
                         "status": "unauthorized",
                         "client": "fa16.3ede.7049"
                    }
               },
               "interface": "GigabitEthernet0/1"
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''\
        Interface       PAE     Client          Status          
        --------------------------------------------------------
        Gi0/1           AUTH    fa16.3ede.7048  UNAUTHORIZED
                                fa16.3ea5.663a  AUTHORIZED
                        SUPP    fa16.3ede.7049  UNAUTHORIZED
                                fa16.3ea5.663b  AUTHORIZED

    '''
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowDot1xAllSummary(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowDot1xAllSummary(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_1(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_1)
        obj = ShowDot1xAllSummary(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_1)


class test_show_dot1x_all_count(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        'sessions': {
            'authorized_clients': 0,
            'unauthorized_clients': 0,
            'total': 0,
        }
    }

    golden_output = {'execute.return_value': '''\
        Number of Dot1x sessions
        -------------------------------
        Authorized Clients        = 0
        UnAuthorized Clients      = 0
        Total No of Client        = 0
    '''
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowDot1xAllCount(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowDot1xAllCount(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()

