import unittest

from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from genie.libs.parser.sros.show_system_ntp_all import ShowSystemNtpAll


class TestShowSystemNtpAll(unittest.TestCase):
    maxDiff = None
    dev = Device(name='device')
    empty_output = {'execute.return_value': ''}

    sample_output = {'execute.return_value': '''
    A:admin@GENIE01XR1#  show system ntp all
    ===============================================================================
    NTP Status
    ===============================================================================
    Configured         : Yes                Stratum              : 3
    Admin Status       : up                 Oper Status          : up
    Server Enabled     : No                 Server Authenticate  : No
    Clock Source       : 192.168.132.170
    Auth Check         : No                 
    Current Date & Time: 2020/01/17 17:24:12 UTC
    ===============================================================================
    ===============================================================================
    NTP Active Associations
    ===============================================================================
    State                     Reference ID    St Type  A  Poll Reach     Offset(ms)
        Router         Remote                                            
    -------------------------------------------------------------------------------
    reject                    STEP            -  srvr  -  64   ........  0.000
        Base           172.16.189.64
    reject                    STEP            -  srvr  -  64   ........  0.000
        Base           172.16.189.74
    candidate                 172.16.25.201  4  srvr  -  64   YYYYYYYY  -0.541
        Base           172.16.25.140
    candidate                 172.16.25.201  4  srvr  -  64   YYYYYYYY  -0.335
        Base           172.16.25.141
    reject                    STEP            -  srvr  -  64   ........  0.000
        Base           172.16.186.22
    reject                    STEP            -  srvr  -  64   ........  0.000
        Base           172.24.107.142
    chosen                    172.16.85.97   2  srvr  -  64   YYYYYYYY  0.259
        Base           192.168.132.170
    ===============================================================================
    ===============================================================================
    NTP Clients
    ===============================================================================
    vRouter                                                    Time Last Request Rx
        Address                                                
    -------------------------------------------------------------------------------
    ===============================================================================
    '''}

    sample_parsed_output = {
    'clock_state': {
        'system_status': {
            'admin_status': 'up',
            'auth_check': 'No',
            'clock_source': '192.168.132.170',
            'configured': 'Yes',
            'current_date_time': '2020/01/17 17:24:12 UTC',
            'oper_status': 'up',
            'server_authenticate': 'No',
            'server_enabled': 'No',
            'stratum': 3,
        },
    },
    'peer': {
        '172.16.189.64': {
            'local_mode': {
                'client': {
                    'a': '-',
                    'offset': 0.0,
                    'poll': 64,
                    'reach': '........',
                    'refid': 'STEP',
                    'remote': '172.16.189.64',
                    'router': 'Base',
                    'state': 'reject',
                    'stratum': '-',
                    'type': 'srvr',
                },
            },
        },
        '172.16.189.74': {
            'local_mode': {
                'client': {
                    'a': '-',
                    'offset': 0.0,
                    'poll': 64,
                    'reach': '........',
                    'refid': 'STEP',
                    'remote': '172.16.189.74',
                    'router': 'Base',
                    'state': 'reject',
                    'stratum': '-',
                    'type': 'srvr',
                },
            },
        },
        '172.16.25.140': {
            'local_mode': {
                'client': {
                    'a': '-',
                    'offset': -0.541,
                    'poll': 64,
                    'reach': 'YYYYYYYY',
                    'refid': '172.16.25.201',
                    'remote': '172.16.25.140',
                    'router': 'Base',
                    'state': 'candidate',
                    'stratum': '4',
                    'type': 'srvr',
                },
            },
        },
        '172.16.25.141': {
            'local_mode': {
                'client': {
                    'a': '-',
                    'offset': -0.335,
                    'poll': 64,
                    'reach': 'YYYYYYYY',
                    'refid': '172.16.25.201',
                    'remote': '172.16.25.141',
                    'router': 'Base',
                    'state': 'candidate',
                    'stratum': '4',
                    'type': 'srvr',
                },
            },
        },
        '172.16.186.22': {
            'local_mode': {
                'client': {
                    'a': '-',
                    'offset': 0.0,
                    'poll': 64,
                    'reach': '........',
                    'refid': 'STEP',
                    'remote': '172.16.186.22',
                    'router': 'Base',
                    'state': 'reject',
                    'stratum': '-',
                    'type': 'srvr',
                },
            },
        },
        '172.24.107.142': {
            'local_mode': {
                'client': {
                    'a': '-',
                    'offset': 0.0,
                    'poll': 64,
                    'reach': '........',
                    'refid': 'STEP',
                    'remote': '172.24.107.142',
                    'router': 'Base',
                    'state': 'reject',
                    'stratum': '-',
                    'type': 'srvr',
                },
            },
        },
        '192.168.132.170': {
            'local_mode': {
                'client': {
                    'a': '-',
                    'offset': 0.259,
                    'poll': 64,
                    'reach': 'YYYYYYYY',
                    'refid': '172.16.85.97',
                    'remote': '192.168.132.170',
                    'router': 'Base',
                    'state': 'chosen',
                    'stratum': '2',
                    'type': 'srvr',
                },
            },
        },
    },
}

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowSystemNtpAll(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.dev = Mock(**self.sample_output)
        obj = ShowSystemNtpAll(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.sample_parsed_output)