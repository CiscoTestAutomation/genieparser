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

        RxVersion = 1   LastRxSrcMAC = 9ceb.e83d.24a4

        Dot1x Authenticator Port Statistics for GigabitEthernet2/2
        --------------------------------------------
        RxStart = 124   RxLogoff = 71   RxResp = 2307   RxRespID = 220
        RxInvalid = 0   RxLenErr = 0    RxTotal = 2742

        TxReq = 2480    TxReqID = 525   TxTotal = 3148

        RxVersion = 1   LastRxSrcMAC = 1866.dafd.44a3

        Dot1x Authenticator Port Statistics for GigabitEthernet2/3
        --------------------------------------------
        RxStart = 111   RxLogoff = 87   RxResp = 2290   RxRespID = 222
        RxInvalid = 0   RxLenErr = 0    RxTotal = 2746

        TxReq = 2471    TxReqID = 449   TxTotal = 3057

        RxVersion = 1   LastRxSrcMAC = 34e6.d73d.103a

        Dot1x Authenticator Port Statistics for GigabitEthernet2/4
        --------------------------------------------
        RxStart = 125   RxLogoff = 0    RxResp = 2972   RxRespID = 298
        RxInvalid = 0   RxLenErr = 0    RxTotal = 3441

        TxReq = 3214    TxReqID = 902   TxTotal = 4304

        RxVersion = 1   LastRxSrcMAC = f8ca.b859.0d01

        Dot1x Authenticator Port Statistics for GigabitEthernet2/5
        --------------------------------------------
        RxStart = 50    RxLogoff = 0    RxResp = 1708   RxRespID = 151
        RxInvalid = 0   RxLenErr = 0    RxTotal = 1928

        TxReq = 1850    TxReqID = 457   TxTotal = 2408

        RxVersion = 1   LastRxSrcMAC = d481.d763.b569

        Dot1x Authenticator Port Statistics for GigabitEthernet2/6
        --------------------------------------------
        RxStart = 174   RxLogoff = 176  RxResp = 2427   RxRespID = 238
        RxInvalid = 0   RxLenErr = 0    RxTotal = 3035

        TxReq = 2617    TxReqID = 747   TxTotal = 3654

        RxVersion = 1   LastRxSrcMAC = 9ceb.e83d.240d

        Dot1x Authenticator Port Statistics for GigabitEthernet2/7
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet2/8
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet2/9
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet2/10
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 2     TxTotal = 3

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet2/11
        --------------------------------------------
        RxStart = 2     RxLogoff = 0    RxResp = 139    RxRespID = 12
        RxInvalid = 0   RxLenErr = 0    RxTotal = 157

        TxReq = 148     TxReqID = 23    TxTotal = 175

        RxVersion = 1   LastRxSrcMAC = b8ca.3abf.6955

        Dot1x Authenticator Port Statistics for GigabitEthernet2/12
        --------------------------------------------
        RxStart = 88    RxLogoff = 103  RxResp = 1595   RxRespID = 169
        RxInvalid = 0   RxLenErr = 0    RxTotal = 1971

        TxReq = 1718    TxReqID = 268   TxTotal = 2101

        RxVersion = 1   LastRxSrcMAC = 9840.bb2f.e2f5

        Dot1x Authenticator Port Statistics for GigabitEthernet2/13
        --------------------------------------------
        RxStart = 107   RxLogoff = 0    RxResp = 2642   RxRespID = 238
        RxInvalid = 0   RxLenErr = 0    RxTotal = 3027

        TxReq = 2856    TxReqID = 637   TxTotal = 3610

        RxVersion = 1   LastRxSrcMAC = 1418.77c3.da25

        Dot1x Authenticator Port Statistics for GigabitEthernet2/14
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 21    TxTotal = 28

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet2/15
        --------------------------------------------
        RxStart = 111   RxLogoff = 0    RxResp = 1899   RxRespID = 234
        RxInvalid = 0   RxLenErr = 0    RxTotal = 2273

        TxReq = 2048    TxReqID = 362   TxTotal = 2430

        RxVersion = 1   LastRxSrcMAC = b8ca.3aff.9e0c

        Dot1x Authenticator Port Statistics for GigabitEthernet2/16
        --------------------------------------------
        RxStart = 32    RxLogoff = 0    RxResp = 1612   RxRespID = 141
        RxInvalid = 0   RxLenErr = 0    RxTotal = 1804

        TxReq = 1736    TxReqID = 223   TxTotal = 1985

        RxVersion = 1   LastRxSrcMAC = d481.d7d8.8422

        Dot1x Authenticator Port Statistics for GigabitEthernet2/17
        --------------------------------------------
        RxStart = 56    RxLogoff = 0    RxResp = 2080   RxRespID = 188
        RxInvalid = 0   RxLenErr = 0    RxTotal = 2352

        TxReq = 2240    TxReqID = 265   TxTotal = 2533

        RxVersion = 1   LastRxSrcMAC = f8ca.b859.0dbc

        Dot1x Authenticator Port Statistics for GigabitEthernet2/18
        --------------------------------------------
        RxStart = 19    RxLogoff = 20   RxResp = 260    RxRespID = 24
        RxInvalid = 0   RxLenErr = 0    RxTotal = 324

        TxReq = 280     TxReqID = 49    TxTotal = 351

        RxVersion = 1   LastRxSrcMAC = f8ca.b859.07fc

        Dot1x Authenticator Port Statistics for GigabitEthernet2/19
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet2/20
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet2/21
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 1545  TxTotal = 2060

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet2/22
        --------------------------------------------
        RxStart = 5619  RxLogoff = 60   RxResp = 5774   RxRespID = 5956
        RxInvalid = 0   RxLenErr = 0    RxTotal = 17606

        TxReq = 5924    TxReqID = 6669  TxTotal = 12886

        RxVersion = 1   LastRxSrcMAC = e04f.439f.cf2e

        Dot1x Authenticator Port Statistics for GigabitEthernet2/23
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 26     RxRespID = 2
        RxInvalid = 0   RxLenErr = 0    RxTotal = 28

        TxReq = 28  TxReqID = 2     TxTotal = 30

        RxVersion = 1   LastRxSrcMAC = 34e6.d758.c0b1

        Dot1x Authenticator Port Statistics for GigabitEthernet2/24
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet2/25
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 519   TxTotal = 692

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet2/26
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 489   TxTotal = 652

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet2/27
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 1797  TxTotal = 2396

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet2/28
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet2/29
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet2/30
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet2/31
        --------------------------------------------
        RxStart = 1     RxLogoff = 0    RxResp = 13     RxRespID = 1
        RxInvalid = 0   RxLenErr = 0    RxTotal = 15

        TxReq = 14  TxReqID = 2     TxTotal = 16

        RxVersion = 1   LastRxSrcMAC = f8ca.b859.0b96

        Dot1x Authenticator Port Statistics for GigabitEthernet2/32
        --------------------------------------------
        RxStart = 64    RxLogoff = 0    RxResp = 1482   RxRespID = 240
        RxInvalid = 0   RxLenErr = 0    RxTotal = 1835

        TxReq = 1596    TxReqID = 434   TxTotal = 2100

        RxVersion = 1   LastRxSrcMAC = f8ca.b859.0eca

        Dot1x Authenticator Port Statistics for GigabitEthernet2/34
        --------------------------------------------
        RxStart = 65    RxLogoff = 0    RxResp = 2491   RxRespID = 227
        RxInvalid = 0   RxLenErr = 0    RxTotal = 2809

        TxReq = 2685    TxReqID = 312   TxTotal = 3018

        RxVersion = 1   LastRxSrcMAC = f8ca.b85a.7614

        Dot1x Authenticator Port Statistics for GigabitEthernet2/35
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet2/36
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet2/37
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet2/38
        --------------------------------------------
        RxStart = 91    RxLogoff = 0    RxResp = 2042   RxRespID = 242
        RxInvalid = 0   RxLenErr = 0    RxTotal = 2423

        TxReq = 2199    TxReqID = 478   TxTotal = 2748

        RxVersion = 1   LastRxSrcMAC = f8ca.b859.0be7

        Dot1x Authenticator Port Statistics for GigabitEthernet2/39
        --------------------------------------------
        RxStart = 65    RxLogoff = 0    RxResp = 2126   RxRespID = 219
        RxInvalid = 0   RxLenErr = 0    RxTotal = 2462

        TxReq = 2290    TxReqID = 527   TxTotal = 2927

        RxVersion = 1   LastRxSrcMAC = f8ca.b859.0dc1

        Dot1x Authenticator Port Statistics for GigabitEthernet2/40
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet2/41
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet2/42
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet2/43
        --------------------------------------------
        RxStart = 41    RxLogoff = 0    RxResp = 2275   RxRespID = 196
        RxInvalid = 0   RxLenErr = 0    RxTotal = 2533

        TxReq = 2450    TxReqID = 228   TxTotal = 2680

        RxVersion = 1   LastRxSrcMAC = 8cec.4bfd.d4dd

        Dot1x Authenticator Port Statistics for GigabitEthernet2/44
        --------------------------------------------
        RxStart = 17    RxLogoff = 0    RxResp = 689    RxRespID = 62
        RxInvalid = 0   RxLenErr = 0    RxTotal = 783

        TxReq = 742     TxReqID = 208   TxTotal = 999

        RxVersion = 1   LastRxSrcMAC = f8ca.b813.c68c

        Dot1x Authenticator Port Statistics for GigabitEthernet2/45
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet2/46
        --------------------------------------------
        RxStart = 2     RxLogoff = 0    RxResp = 104    RxRespID = 9
        RxInvalid = 0   RxLenErr = 0    RxTotal = 116

        TxReq = 112     TxReqID = 22    TxTotal = 138

        RxVersion = 1   LastRxSrcMAC = 4c76.25fd.471d

        Dot1x Authenticator Port Statistics for GigabitEthernet2/47
        --------------------------------------------
        RxStart = 33    RxLogoff = 44   RxResp = 611    RxRespID = 65
        RxInvalid = 0   RxLenErr = 0    RxTotal = 772

        TxReq = 658     TxReqID = 295   TxTotal = 1063

        RxVersion = 1   LastRxSrcMAC = 9840.bb2f.e3bf

        Dot1x Authenticator Port Statistics for GigabitEthernet2/48
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet3/1
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 364

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 1   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet3/2
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet3/3
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet3/4
        --------------------------------------------
        RxStart = 1     RxLogoff = 0    RxResp = 13     RxRespID = 1
        RxInvalid = 0   RxLenErr = 0    RxTotal = 15

        TxReq = 14  TxReqID = 2     TxTotal = 16

        RxVersion = 1   LastRxSrcMAC = 3c2c.30fa.2f52

        Dot1x Authenticator Port Statistics for GigabitEthernet3/5
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 333   TxTotal = 444

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet3/6
        --------------------------------------------
        RxStart = 10    RxLogoff = 0    RxResp = 4368   RxRespID = 344
        RxInvalid = 0   RxLenErr = 0    RxTotal = 4729

        TxReq = 4704    TxReqID = 352   TxTotal = 5062

        RxVersion = 1   LastRxSrcMAC = 484d.7ed7.4954

        Dot1x Authenticator Port Statistics for GigabitEthernet3/7
        --------------------------------------------
        RxStart = 6     RxLogoff = 74   RxResp = 6190   RxRespID = 491
        RxInvalid = 0   RxLenErr = 0    RxTotal = 6837

        TxReq = 6667    TxReqID = 721   TxTotal = 7540

        RxVersion = 1   LastRxSrcMAC = 1803.73dc.8581

        Dot1x Authenticator Port Statistics for GigabitEthernet3/8
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet3/9
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet3/10
        --------------------------------------------
        RxStart = 95    RxLogoff = 0    RxResp = 3000   RxRespID = 348
        RxInvalid = 0   RxLenErr = 0    RxTotal = 3538

        TxReq = 3238    TxReqID = 658   TxTotal = 3983

        RxVersion = 1   LastRxSrcMAC = 34e6.d758.c344

        Dot1x Authenticator Port Statistics for GigabitEthernet3/11
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet3/12
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 333   TxTotal = 444

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet3/13
        --------------------------------------------
        RxStart = 48    RxLogoff = 0    RxResp = 2509   RxRespID = 269
        RxInvalid = 0   RxLenErr = 0    RxTotal = 2939

        TxReq = 2710    TxReqID = 647   TxTotal = 3505

        RxVersion = 1   LastRxSrcMAC = f8ca.b859.0aa6

        Dot1x Authenticator Port Statistics for GigabitEthernet3/14
        --------------------------------------------
        RxStart = 1     RxLogoff = 0    RxResp = 26     RxRespID = 2
        RxInvalid = 0   RxLenErr = 0    RxTotal = 29

        TxReq = 28  TxReqID = 3     TxTotal = 31

        RxVersion = 1   LastRxSrcMAC = 3c2c.30ab.bbec

        Dot1x Authenticator Port Statistics for GigabitEthernet3/15
        --------------------------------------------
        RxStart = 209   RxLogoff = 249  RxResp = 3418   RxRespID = 329
        RxInvalid = 0   RxLenErr = 0    RxTotal = 4270

        TxReq = 3684    TxReqID = 778   TxTotal = 4777

        RxVersion = 1   LastRxSrcMAC = 34e6.d758.cafe

        Dot1x Authenticator Port Statistics for GigabitEthernet3/16
        --------------------------------------------
        RxStart = 160   RxLogoff = 296  RxResp = 3919   RxRespID = 507
        RxInvalid = 0   RxLenErr = 0    RxTotal = 5048

        TxReq = 4227    TxReqID = 1250  TxTotal = 5983

        RxVersion = 1   LastRxSrcMAC = c8f7.5048.42cf

        Dot1x Authenticator Port Statistics for GigabitEthernet3/17
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet3/18
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet3/19
        --------------------------------------------
        RxStart = 2     RxLogoff = 0    RxResp = 52     RxRespID = 4
        RxInvalid = 0   RxLenErr = 0    RxTotal = 59

        TxReq = 56  TxReqID = 6     TxTotal = 62

        RxVersion = 1   LastRxSrcMAC = f8ca.b859.08ef

        Dot1x Authenticator Port Statistics for GigabitEthernet3/20
        --------------------------------------------
        RxStart = 193   RxLogoff = 265  RxResp = 3498   RxRespID = 333
        RxInvalid = 0   RxLenErr = 0    RxTotal = 4351

        TxReq = 3767    TxReqID = 1021  TxTotal = 5204

        RxVersion = 1   LastRxSrcMAC = a44c.c82b.391a

        Dot1x Authenticator Port Statistics for GigabitEthernet3/21
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet3/22
        --------------------------------------------
        RxStart = 1     RxLogoff = 0    RxResp = 52     RxRespID = 4
        RxInvalid = 0   RxLenErr = 0    RxTotal = 59

        TxReq = 56  TxReqID = 14    TxTotal = 73

        RxVersion = 1   LastRxSrcMAC = 1418.779b.8a76

        Dot1x Authenticator Port Statistics for GigabitEthernet3/23
        --------------------------------------------
        RxStart = 129   RxLogoff = 117  RxResp = 2951   RxRespID = 364
        RxInvalid = 0   RxLenErr = 0    RxTotal = 3661

        TxReq = 3181    TxReqID = 919   TxTotal = 4370

        RxVersion = 1   LastRxSrcMAC = f8ca.b859.0dbb

        Dot1x Authenticator Port Statistics for GigabitEthernet3/24
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 69    TxTotal = 92

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet3/25
        --------------------------------------------
        RxStart = 46    RxLogoff = 0    RxResp = 1456   RxRespID = 141
        RxInvalid = 0   RxLenErr = 0    RxTotal = 1667

        TxReq = 1568    TxReqID = 210   TxTotal = 1792

        RxVersion = 1   LastRxSrcMAC = 34e6.d758.c306

        Dot1x Authenticator Port Statistics for GigabitEthernet3/26
        --------------------------------------------
        RxStart = 25    RxLogoff = 0    RxResp = 477    RxRespID = 42
        RxInvalid = 0   RxLenErr = 0    RxTotal = 551

        TxReq = 522     TxReqID = 54    TxTotal = 583

        RxVersion = 1   LastRxSrcMAC = 3c2c.30fa.31c8

        Dot1x Authenticator Port Statistics for GigabitEthernet3/27
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet3/28
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet3/29
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet3/30
        --------------------------------------------
        RxStart = 1     RxLogoff = 0    RxResp = 13     RxRespID = 1
        RxInvalid = 0   RxLenErr = 0    RxTotal = 15

        TxReq = 14  TxReqID = 2     TxTotal = 16

        RxVersion = 1   LastRxSrcMAC = 9840.bb2f.e2f5

        Dot1x Authenticator Port Statistics for GigabitEthernet3/31
        --------------------------------------------
        RxStart = 6     RxLogoff = 0    RxResp = 312    RxRespID = 27
        RxInvalid = 0   RxLenErr = 0    RxTotal = 350

        TxReq = 336     TxReqID = 1136  TxTotal = 1841

        RxVersion = 1   LastRxSrcMAC = 58fc.db41.29c8

        Dot1x Authenticator Port Statistics for GigabitEthernet3/32
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet3/33
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 894   TxTotal = 1192

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet3/34
        --------------------------------------------
        RxStart = 21    RxLogoff = 0    RxResp = 819    RxRespID = 72
        RxInvalid = 0   RxLenErr = 0    RxTotal = 922

        TxReq = 882     TxReqID = 118   TxTotal = 1015

        RxVersion = 1   LastRxSrcMAC = d481.d772.df18

        Dot1x Authenticator Port Statistics for GigabitEthernet3/35
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet3/36
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet3/37
        --------------------------------------------
        RxStart = 1     RxLogoff = 0    RxResp = 13     RxRespID = 2
        RxInvalid = 0   RxLenErr = 0    RxTotal = 16

        TxReq = 14  TxReqID = 3     TxTotal = 17

        RxVersion = 1   LastRxSrcMAC = 54bf.640e.7e10

        Dot1x Authenticator Port Statistics for GigabitEthernet3/38
        --------------------------------------------
        RxStart = 199   RxLogoff = 0    RxResp = 4488   RxRespID = 501
        RxInvalid = 0   RxLenErr = 0    RxTotal = 5266

        TxReq = 4838    TxReqID = 704   TxTotal = 5574

        RxVersion = 1   LastRxSrcMAC = f8ca.b80d.f63c

        Dot1x Authenticator Port Statistics for GigabitEthernet3/39
        --------------------------------------------
        RxStart = 3     RxLogoff = 0    RxResp = 68     RxRespID = 7
        RxInvalid = 0   RxLenErr = 0    RxTotal = 79

        TxReq = 76  TxReqID = 11    TxTotal = 90

        RxVersion = 1   LastRxSrcMAC = f8ca.b802.3863

        Dot1x Authenticator Port Statistics for GigabitEthernet3/40
        --------------------------------------------
        RxStart = 108   RxLogoff = 0    RxResp = 2535   RxRespID = 261
        RxInvalid = 0   RxLenErr = 0    RxTotal = 2937

        TxReq = 2734    TxReqID = 420   TxTotal = 3182

        RxVersion = 1   LastRxSrcMAC = 34e6.d758.c344

        Dot1x Authenticator Port Statistics for GigabitEthernet3/41
        --------------------------------------------
        RxStart = 171   RxLogoff = 0    RxResp = 2459   RxRespID = 216
        RxInvalid = 0   RxLenErr = 0    RxTotal = 2849

        TxReq = 2648    TxReqID = 387   TxTotal = 3035

        RxVersion = 1   LastRxSrcMAC = 34e6.d758.c899

        Dot1x Authenticator Port Statistics for GigabitEthernet3/42
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet3/43
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet3/44
        --------------------------------------------
        RxStart = 90    RxLogoff = 0    RxResp = 2366   RxRespID = 257
        RxInvalid = 0   RxLenErr = 0    RxTotal = 2757

        TxReq = 2548    TxReqID = 407   TxTotal = 2983

        RxVersion = 1   LastRxSrcMAC = c8f7.5068.2c10

        Dot1x Authenticator Port Statistics for GigabitEthernet3/45
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 39     RxRespID = 3
        RxInvalid = 0   RxLenErr = 0    RxTotal = 43

        TxReq = 42  TxReqID = 10    TxTotal = 54

        RxVersion = 1   LastRxSrcMAC = 847b.eb39.f721

        Dot1x Authenticator Port Statistics for GigabitEthernet3/46
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet3/47
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 6     TxTotal = 8

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet3/48
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet4/1
        --------------------------------------------
        RxStart = 1     RxLogoff = 0    RxResp = 13     RxRespID = 1
        RxInvalid = 0   RxLenErr = 0    RxTotal = 15

        TxReq = 14  TxReqID = 2     TxTotal = 16

        RxVersion = 1   LastRxSrcMAC = c8f7.5021.63b5

        Dot1x Authenticator Port Statistics for GigabitEthernet4/2
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet4/3
        --------------------------------------------
        RxStart = 131   RxLogoff = 0    RxResp = 2666   RxRespID = 342
        RxInvalid = 0   RxLenErr = 0    RxTotal = 3204

        TxReq = 2871    TxReqID = 573   TxTotal = 3485

        RxVersion = 1   LastRxSrcMAC = c8f7.50a3.f104

        Dot1x Authenticator Port Statistics for GigabitEthernet4/4
        --------------------------------------------
        RxStart = 18    RxLogoff = 0    RxResp = 1378   RxRespID = 118
        RxInvalid = 0   RxLenErr = 0    RxTotal = 1539

        TxReq = 1484    TxReqID = 149   TxTotal = 1640

        RxVersion = 1   LastRxSrcMAC = c8f7.5021.6551

        Dot1x Authenticator Port Statistics for GigabitEthernet4/5
        --------------------------------------------
        RxStart = 37    RxLogoff = 0    RxResp = 2756   RxRespID = 242
        RxInvalid = 0   RxLenErr = 0    RxTotal = 3072

        TxReq = 2969    TxReqID = 290   TxTotal = 3268

        RxVersion = 1   LastRxSrcMAC = c8f7.5049.4a8f

        Dot1x Authenticator Port Statistics for GigabitEthernet4/6
        --------------------------------------------
        RxStart = 8     RxLogoff = 12   RxResp = 2424   RxRespID = 189
        RxInvalid = 0   RxLenErr = 0    RxTotal = 2644

        TxReq = 2606    TxReqID = 225   TxTotal = 2854

        RxVersion = 1   LastRxSrcMAC = 3417.ebae.b881

        Dot1x Authenticator Port Statistics for GigabitEthernet4/7
        --------------------------------------------
        RxStart = 254   RxLogoff = 288  RxResp = 3957   RxRespID = 372
        RxInvalid = 0   RxLenErr = 0    RxTotal = 4920

        TxReq = 4266    TxReqID = 952   TxTotal = 5603

        RxVersion = 1   LastRxSrcMAC = 3c2c.30ab.be49

        Dot1x Authenticator Port Statistics for GigabitEthernet4/8
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet4/9
        --------------------------------------------
        RxStart = 50    RxLogoff = 0    RxResp = 1729   RxRespID = 176
        RxInvalid = 0   RxLenErr = 0    RxTotal = 2013

        TxReq = 1863    TxReqID = 263   TxTotal = 2149

        RxVersion = 1   LastRxSrcMAC = 2047.47ea.b8ae

        Dot1x Authenticator Port Statistics for GigabitEthernet4/10
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet4/11
        --------------------------------------------
        RxStart = 17    RxLogoff = 0    RxResp = 468    RxRespID = 48
        RxInvalid = 0   RxLenErr = 0    RxTotal = 543

        TxReq = 504     TxReqID = 146   TxTotal = 680

        RxVersion = 1   LastRxSrcMAC = 54bf.6433.f842

        Dot1x Authenticator Port Statistics for GigabitEthernet4/12
        --------------------------------------------
        RxStart = 1     RxLogoff = 0    RxResp = 1014   RxRespID = 84
        RxInvalid = 0   RxLenErr = 0    RxTotal = 1111

        TxReq = 1092    TxReqID = 102   TxTotal = 1205

        RxVersion = 1   LastRxSrcMAC = 1803.73db.d296

        Dot1x Authenticator Port Statistics for GigabitEthernet4/13
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet4/14
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet4/15
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet4/16
        --------------------------------------------
        RxStart = 32    RxLogoff = 0    RxResp = 1222   RxRespID = 114
        RxInvalid = 0   RxLenErr = 0    RxTotal = 1386

        TxReq = 1316    TxReqID = 286   TxTotal = 1658

        RxVersion = 1   LastRxSrcMAC = d4be.d911.f0de

        Dot1x Authenticator Port Statistics for GigabitEthernet4/17
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet4/18
        --------------------------------------------
        RxStart = 9     RxLogoff = 15   RxResp = 273    RxRespID = 28
        RxInvalid = 0   RxLenErr = 0    RxTotal = 333

        TxReq = 296     TxReqID = 54    TxTotal = 372

        RxVersion = 1   LastRxSrcMAC = d481.d75d.ee27

        Dot1x Authenticator Port Statistics for GigabitEthernet4/19
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet4/20
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet4/21
        --------------------------------------------
        RxStart = 100   RxLogoff = 0    RxResp = 2678   RxRespID = 227
        RxInvalid = 0   RxLenErr = 0    RxTotal = 3046

        TxReq = 2884    TxReqID = 506   TxTotal = 3419

        RxVersion = 1   LastRxSrcMAC = 3c2c.30e5.ee8c

        Dot1x Authenticator Port Statistics for GigabitEthernet4/22
        --------------------------------------------
        RxStart = 92    RxLogoff = 0    RxResp = 1864   RxRespID = 305
        RxInvalid = 0   RxLenErr = 0    RxTotal = 2319

        TxReq = 2013    TxReqID = 500   TxTotal = 2571

        RxVersion = 1   LastRxSrcMAC = 34e6.d759.1b8c

        Dot1x Authenticator Port Statistics for GigabitEthernet4/23
        --------------------------------------------
        RxStart = 141   RxLogoff = 0    RxResp = 3307   RxRespID = 368
        RxInvalid = 0   RxLenErr = 0    RxTotal = 3850

        TxReq = 3561    TxReqID = 474   TxTotal = 4049

        RxVersion = 1   LastRxSrcMAC = 34e6.d758.c8c3

        Dot1x Authenticator Port Statistics for GigabitEthernet4/24
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet4/25
        --------------------------------------------
        RxStart = 1     RxLogoff = 3    RxResp = 39     RxRespID = 4
        RxInvalid = 0   RxLenErr = 0    RxTotal = 48

        TxReq = 42  TxReqID = 7     TxTotal = 53

        RxVersion = 1   LastRxSrcMAC = f8ca.b80d.f6d0

        Dot1x Authenticator Port Statistics for GigabitEthernet4/26
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet4/27
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet4/28
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet4/29
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet4/30
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet4/31
        --------------------------------------------
        RxStart = 16    RxLogoff = 0    RxResp = 923    RxRespID = 71
        RxInvalid = 0   RxLenErr = 0    RxTotal = 1017

        TxReq = 994     TxReqID = 92    TxTotal = 1088

        RxVersion = 1   LastRxSrcMAC = f8ca.b80d.f74b

        Dot1x Authenticator Port Statistics for GigabitEthernet4/32
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet4/33
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet4/34
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet4/35
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet4/36
        --------------------------------------------
        RxStart = 105   RxLogoff = 0    RxResp = 1963   RxRespID = 286
        RxInvalid = 0   RxLenErr = 0    RxTotal = 2397

        TxReq = 2114    TxReqID = 494   TxTotal = 2649

        RxVersion = 1   LastRxSrcMAC = 34e6.d758.c2bc

        Dot1x Authenticator Port Statistics for GigabitEthernet4/37
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 165   TxTotal = 220

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet4/38
        --------------------------------------------
        RxStart = 96    RxLogoff = 0    RxResp = 2213   RxRespID = 297
        RxInvalid = 0   RxLenErr = 0    RxTotal = 2679

        TxReq = 2494    TxReqID = 10516     TxTotal = 18465

        RxVersion = 1   LastRxSrcMAC = c8f7.50c3.e4a9

        Dot1x Authenticator Port Statistics for GigabitEthernet4/39
        --------------------------------------------
        RxStart = 33    RxLogoff = 0    RxResp = 845    RxRespID = 81
        RxInvalid = 0   RxLenErr = 0    RxTotal = 975

        TxReq = 910     TxReqID = 624   TxTotal = 1704

        RxVersion = 1   LastRxSrcMAC = f8ca.b859.08ef

        Dot1x Authenticator Port Statistics for GigabitEthernet4/40
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet4/41
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 443

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 1   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet4/42
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet4/43
        --------------------------------------------
        RxStart = 111   RxLogoff = 0    RxResp = 1834   RxRespID = 256
        RxInvalid = 0   RxLenErr = 0    RxTotal = 2230

        TxReq = 1975    TxReqID = 444   TxTotal = 2451

        RxVersion = 1   LastRxSrcMAC = 34e6.d758.c106

        Dot1x Authenticator Port Statistics for GigabitEthernet4/44
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet4/45
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 61    TxTotal = 82

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet4/46
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet4/47
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet4/48
        --------------------------------------------
        RxStart = 1     RxLogoff = 0    RxResp = 6721   RxRespID = 524
        RxInvalid = 0   RxLenErr = 0    RxTotal = 7307

        TxReq = 7240    TxReqID = 641   TxTotal = 7925

        RxVersion = 1   LastRxSrcMAC = 3417.ebae.a363

        Dot1x Authenticator Port Statistics for GigabitEthernet5/1
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet5/2
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet5/3
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet5/4
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet5/5
        --------------------------------------------
        RxStart = 13    RxLogoff = 0    RxResp = 1469   RxRespID = 129
        RxInvalid = 0   RxLenErr = 0    RxTotal = 1640

        TxReq = 1582    TxReqID = 220   TxTotal = 1831

        RxVersion = 1   LastRxSrcMAC = f8ca.b859.0a15

        Dot1x Authenticator Port Statistics for GigabitEthernet5/6
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 13     RxRespID = 4
        RxInvalid = 0   RxLenErr = 0    RxTotal = 18

        TxReq = 14  TxReqID = 6     TxTotal = 21

        RxVersion = 1   LastRxSrcMAC = d481.d766.506e

        Dot1x Authenticator Port Statistics for GigabitEthernet5/7
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 3517   RxRespID = 581
        RxInvalid = 0   RxLenErr = 0    RxTotal = 4101

        TxReq = 4097    TxReqID = 587   TxTotal = 4687

        RxVersion = 3   LastRxSrcMAC = 442b.03a9.5ff5

        Dot1x Authenticator Port Statistics for GigabitEthernet5/8
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet5/9
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet5/10
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 1790  TxTotal = 2387

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet5/11
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet5/12
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 6     TxTotal = 8

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet5/13
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 6

        TxReq = 0   TxReqID = 570   TxTotal = 760

        RxVersion = 1   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet5/14
        --------------------------------------------
        RxStart = 225   RxLogoff = 170  RxResp = 4705   RxRespID = 587
        RxInvalid = 0   RxLenErr = 0    RxTotal = 5768

        TxReq = 5289    TxReqID = 1514  TxTotal = 7420

        RxVersion = 1   LastRxSrcMAC = f8ca.b800.67fa

        Dot1x Authenticator Port Statistics for GigabitEthernet5/15
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet5/16
        --------------------------------------------
        RxStart = 3     RxLogoff = 0    RxResp = 3393   RxRespID = 270
        RxInvalid = 0   RxLenErr = 0    RxTotal = 3687

        TxReq = 3654    TxReqID = 397   TxTotal = 4098

        RxVersion = 1   LastRxSrcMAC = 1866.da49.b7ab

        Dot1x Authenticator Port Statistics for GigabitEthernet5/17
        --------------------------------------------
        RxStart = 109   RxLogoff = 0    RxResp = 3315   RxRespID = 485
        RxInvalid = 0   RxLenErr = 0    RxTotal = 3998

        TxReq = 3581    TxReqID = 700   TxTotal = 4357

        RxVersion = 1   LastRxSrcMAC = 34e6.d758.cb14

        Dot1x Authenticator Port Statistics for GigabitEthernet5/18
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet5/19
        --------------------------------------------
        RxStart = 3     RxLogoff = 0    RxResp = 390    RxRespID = 33
        RxInvalid = 0   RxLenErr = 0    RxTotal = 429

        TxReq = 420     TxReqID = 123   TxTotal = 573

        RxVersion = 1   LastRxSrcMAC = d481.d7cb.460e

        Dot1x Authenticator Port Statistics for GigabitEthernet5/20
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 3517   RxRespID = 580
        RxInvalid = 0   RxLenErr = 0    RxTotal = 4099

        TxReq = 4097    TxReqID = 586   TxTotal = 4685

        RxVersion = 3   LastRxSrcMAC = 442b.03a9.614f

        Dot1x Authenticator Port Statistics for GigabitEthernet5/21
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 3523   RxRespID = 581
        RxInvalid = 0   RxLenErr = 0    RxTotal = 4107

        TxReq = 4103    TxReqID = 587   TxTotal = 4693

        RxVersion = 3   LastRxSrcMAC = 442b.03a9.6a73

        Dot1x Authenticator Port Statistics for GigabitEthernet5/22
        --------------------------------------------
        RxStart = 122   RxLogoff = 169  RxResp = 2197   RxRespID = 235
        RxInvalid = 0   RxLenErr = 0    RxTotal = 2768

        TxReq = 2366    TxReqID = 523   TxTotal = 3103

        RxVersion = 1   LastRxSrcMAC = 9840.bb2f.e329

        Dot1x Authenticator Port Statistics for GigabitEthernet5/23
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet5/24
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 3517   RxRespID = 581
        RxInvalid = 0   RxLenErr = 0    RxTotal = 4101

        TxReq = 4097    TxReqID = 587   TxTotal = 4687

        RxVersion = 3   LastRxSrcMAC = 442b.03a9.6662

        Dot1x Authenticator Port Statistics for GigabitEthernet5/25
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet5/26
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet5/27
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet5/28
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet5/29
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 1824  TxTotal = 2432

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet5/30
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet5/31
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet5/32
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet5/33
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet5/34
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 1884  TxTotal = 2512

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet5/35
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet5/36
        --------------------------------------------
        RxStart = 165   RxLogoff = 193  RxResp = 2904   RxRespID = 251
        RxInvalid = 0   RxLenErr = 0    RxTotal = 3552

        TxReq = 3130    TxReqID = 636   TxTotal = 3998

        RxVersion = 1   LastRxSrcMAC = 3c2c.30ab.be77

        Dot1x Authenticator Port Statistics for GigabitEthernet5/37
        --------------------------------------------
        RxStart = 50    RxLogoff = 0    RxResp = 2843   RxRespID = 254
        RxInvalid = 0   RxLenErr = 0    RxTotal = 3179

        TxReq = 3064    TxReqID = 334   TxTotal = 3416

        RxVersion = 1   LastRxSrcMAC = d481.d75d.f026

        Dot1x Authenticator Port Statistics for GigabitEthernet5/38
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet5/39
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet5/40
        --------------------------------------------
        RxStart = 7     RxLogoff = 0    RxResp = 1482   RxRespID = 125
        RxInvalid = 0   RxLenErr = 0    RxTotal = 1626

        TxReq = 1602    TxReqID = 132   TxTotal = 1739

        RxVersion = 1   LastRxSrcMAC = e4b9.7aa3.8fc9

        Dot1x Authenticator Port Statistics for GigabitEthernet5/41
        --------------------------------------------
        RxStart = 19612     RxLogoff = 0    RxResp = 235570     RxRespID = 19643
        RxInvalid = 0   RxLenErr = 0    RxTotal = 274843

        TxReq = 235582  TxReqID = 19658     TxTotal = 255255

        RxVersion = 1   LastRxSrcMAC = 3417.ebad.fc88

        Dot1x Authenticator Port Statistics for GigabitEthernet5/42
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet5/43
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet5/44
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 91     RxRespID = 7
        RxInvalid = 0   RxLenErr = 0    RxTotal = 99

        TxReq = 98  TxReqID = 10    TxTotal = 109

        RxVersion = 1   LastRxSrcMAC = f8ca.b80d.f8d9

        Dot1x Authenticator Port Statistics for GigabitEthernet5/45
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet5/46
        --------------------------------------------
        RxStart = 0     RxLogoff = 0    RxResp = 0  RxRespID = 0
        RxInvalid = 0   RxLenErr = 0    RxTotal = 0

        TxReq = 0   TxReqID = 0     TxTotal = 0

        RxVersion = 0   LastRxSrcMAC = 0000.0000.0000

        Dot1x Authenticator Port Statistics for GigabitEthernet5/47
        --------------------------------------------
        RxStart = 72    RxLogoff = 75   RxResp = 988    RxRespID = 84
        RxInvalid = 0   RxLenErr = 0    RxTotal = 1220

        TxReq = 1064    TxReqID = 187   TxTotal = 1326

        RxVersion = 1   LastRxSrcMAC = 3c2c.30ab.be49

        Dot1x Authenticator Port Statistics for GigabitEthernet5/48
        --------------------------------------------
        RxStart = 5     RxLogoff = 16   RxResp = 275    RxRespID = 33
        RxInvalid = 0   RxLenErr = 0    RxTotal = 341

        TxReq = 296     TxReqID = 71    TxTotal = 394

        RxVersion = 1   LastRxSrcMAC = d481.d766.506e

    '''
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
        #self.assertEqual(parsed_output,self.golden_parsed_output_1)

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

