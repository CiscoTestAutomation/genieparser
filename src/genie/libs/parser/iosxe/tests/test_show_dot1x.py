#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from genie.libs.parser.iosxe.show_dot1x import ShowDot1xAllDetail, \
                                    ShowDot1xAllStatistics, \
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


class test_show_dot1x_all_statistics(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        "interfaces": {
            "GigabitEthernet1/0/9": {
               "interface": "GigabitEthernet1/0/9",
               "statistics": {
                    "txtotal": 3,
                    "rxreq": 0,
                    "txstart": 3,
                    "rxversion": 0,
                    "txlogoff": 0,
                    "rxinvalid": 0,
                    "rxlenerr": 0,
                    "lastrxsrcmac": "0000.0000.0000",
                    "rxtotal": 0,
                    "txresp": 0
               }
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        Dot1x Supplicant Port Statistics for GigabitEthernet1/0/9
        --------------------------------------------
        RxReq = 0       RxInvalid = 0    RxLenErr = 0    RxTotal = 0

        TxStart = 3     TxLogoff = 0      TxResp = 0      TxTotal = 3

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000
    '''
    }

    golden_parsed_output_1 = {
        "interfaces": {
            "GigabitEthernet0/1": {
               "statistics": {
                    "lastrxsrcmac": "fa16.3ede.7048",
                    "txtotal": 2650,
                    "rxinvalid": 0,
                    "txreqid": 890,
                    "rxtotal": 2349,
                    "rxlogoff": 0,
                    "rxrespid": 887,
                    "rxversion": 3,
                    "rxresp": 880,
                    "txreq": 1760,
                    "rxstart": 580,
                    "rxlenerr": 0
               },
               "interface": "GigabitEthernet0/1"
            }
        }
    }


    golden_output_1 = {'execute.return_value': '''\
        Dot1x Authenticator Port Statistics for GigabitEthernet0/1
        --------------------------------------------
        RxStart = 580   RxLogoff = 0    RxResp = 880    RxRespID = 887
        RxInvalid = 0   RxLenErr = 0    RxTotal = 2349

        TxReq = 1760    TxReqID = 890   TxTotal = 2650

        RxVersion = 3   LastRxSrcMAC = fa16.3ede.7048
    '''
    }

    golden_output_2 = {'execute.return_value': '''\
        Load for five secs: 24%/5%; one minute: 20%; five minutes: 20%
        Time source is NTP, 07:26:59.359 EDT Tue Aug 27 2019

        Dot1x Authenticator Port Statistics for GigabitEthernet2/1
        --------------------------------------------
        RxStart = 212   RxLogoff = 237  RxResp = 3147   RxRespID = 287
        RxInvalid = 0   RxLenErr = 0    RxTotal = 3918

        TxReq = 3391    TxReqID = 1018  TxTotal = 4821

        RxVersion = 1   LastRxSrcMAC = d481.d75d.f026

        Dot1x Authenticator Port Statistics for GigabitEthernet2/2
        --------------------------------------------
        RxStart = 124   RxLogoff = 71   RxResp = 2307   RxRespID = 220
        RxInvalid = 0   RxLenErr = 0    RxTotal = 2742

        TxReq = 2480    TxReqID = 525   TxTotal = 3148

        RxVersion = 1   LastRxSrcMAC = 2899.fadd.f021

        Dot1x Authenticator Port Statistics for GigabitEthernet2/3
        --------------------------------------------
        RxStart = 111   RxLogoff = 87   RxResp = 2290   RxRespID = 222
        RxInvalid = 0   RxLenErr = 0    RxTotal = 2746

        TxReq = 2471    TxReqID = 449   TxTotal = 3057

        RxVersion = 1   LastRxSrcMAC = 103a.34e6.d73d

        Dot1x Authenticator Port Statistics for GigabitEthernet2/4
        --------------------------------------------
        RxStart = 125   RxLogoff = 0    RxResp = 2972   RxRespID = 298
        RxInvalid = 0   RxLenErr = 0    RxTotal = 3441

        TxReq = 3214    TxReqID = 902   TxTotal = 4304

        RxVersion = 1   LastRxSrcMAC = 0d01.f8ca.b859

    '''
    }

    golden_parsed_output_2 = {
        "interfaces": {
            "GigabitEthernet2/1": {
               "statistics": {
                    "lastrxsrcmac": "d481.d75d.f026",
                    "txtotal": 4821,
                    "rxinvalid": 0,
                    "txreqid": 1018,
                    "rxtotal": 3918,
                    "rxlogoff": 237,
                    "rxrespid": 287,
                    "rxversion": 1,
                    "rxresp": 3147,
                    "txreq": 3391,
                    "rxstart": 212,
                    "rxlenerr": 0
                },
                "interface": "GigabitEthernet2/1"
            },
            "GigabitEthernet2/2": {
                "statistics": {
                    "lastrxsrcmac": "2899.fadd.f021",
                    "txtotal": 3148,
                    "rxinvalid": 0,
                    "txreqid": 525,
                    "rxtotal": 2742,
                    "rxlogoff": 71,
                    "rxrespid": 220,
                    "rxversion": 1,
                    "rxresp": 2307,
                    "txreq": 2480,
                    "rxstart": 124,
                    "rxlenerr": 0
                },
                "interface": "GigabitEthernet2/2"
            },
            "GigabitEthernet2/3": {
                "statistics": {
                    "lastrxsrcmac": "103a.34e6.d73d",
                    "txtotal": 3057,
                    "rxinvalid": 0,
                    "txreqid": 449,
                    "rxtotal": 2746,
                    "rxlogoff": 87,
                    "rxrespid": 222,
                    "rxversion": 1,
                    "rxresp": 2290,
                    "txreq": 2471,
                    "rxstart": 111,
                    "rxlenerr": 0
                },
                "interface": "GigabitEthernet2/3"
            },
            "GigabitEthernet2/4": {
                "statistics": {
                    "lastrxsrcmac": "0d01.f8ca.b859",
                    "txtotal": 4304,
                    "rxinvalid": 0,
                    "txreqid": 902,
                    "rxtotal": 3441,
                    "rxlogoff": 0,
                    "rxrespid": 298,
                    "rxversion": 1,
                    "rxresp": 2972,
                    "txreq": 3214,
                    "rxstart": 125,
                    "rxlenerr": 0
                },
                "interface": "GigabitEthernet2/4"
            },
        }
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowDot1xAllStatistics(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowDot1xAllStatistics(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_1(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_1)
        obj = ShowDot1xAllStatistics(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_1)

    def test_golden_2(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_2)
        obj = ShowDot1xAllStatistics(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_2)

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

