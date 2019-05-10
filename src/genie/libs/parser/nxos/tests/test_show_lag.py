# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
    SchemaMissingKeyError

# iosxe show_lisp
from genie.libs.parser.nxos.show_lag import ShowFeature, ShowLacpSystemIdentifier, \
    ShowLacpCounters


# =================================
# Unit test for 'show feature'
# =================================
class test_show_feature(unittest.TestCase):
    """unit test for show feature"""
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        Feature Name          Instance  State
    --------------------  --------  --------
    bash-shell             1          disabled
    eigrp                  1          disabled
    eigrp                  2          disabled
    lacp                   1          enabled
    '''
                     }
    golden_parsed_output = {'features': {
        'bash-shell': {
            'instances': {
                '1': False
            }
        },
        'eigrp': {
            'instances': {
                '1': False,
                '2': False
            }
        },
        'lacp': {
            'instances': {
                '1': True
            }
        }
    }
    }

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowFeature(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowFeature(device=self.device)
        parsed_output = obj.parse()

        self.assertEqual(parsed_output, self.golden_parsed_output)


# =================================
# Unit test for 'show system-identifier'
# =================================
class test_show_system_identifier(unittest.TestCase):
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
    32768,5e-2-0-1-0-7
    '''}
    golden_parsed_output = {
        'system_id_mac': '5e-2-0-1-0-7',
        'system_priority': 32768,
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLacpSystemIdentifier(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowLacpSystemIdentifier(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

# =================================
# Unit test for 'show lacp counters'
# =================================
class test_show_lacp_counters(unittest.TestCase):
    """unit test for show lacp counters """

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        NOTE: Clear lacp counters to get accurate statistics
    
        ------------------------------------------------------------------------------
                                     LACPDUs                      Markers/Resp LACPDUs
        Port              Sent                Recv                  Recv Sent  Pkts Err
        ------------------------------------------------------------------------------
        port-channel1
        Ethernet1/1        92                   85                     0      0    0      
        Ethernet1/2        79                   87                     0      0    0      
        
        port-channel2
        Ethernet1/3        136                  112                    0      0    0      
        Ethernet1/4        95                   90                     0      0    0      
        Ethernet1/5        118                  146                    0      0    0  
    '''}

    golden_parsed_output = {
        "interfaces": {
            "port-channel1": {
                "members": {
                    "Ethernet1/1": {
                        "interface": "Ethernet1/1",
                        "counters": {
                            "lacp_in_pkts": 85,
                            "lacp_out_pkts": 92,
                            "marker_in_pkts": 0,
                            "marker_out_pkts": 0,
                            "lacp_errors": 0
                        }
                    },
                    "Ethernet1/2": {
                        "interface": "Ethernet1/2",
                        "counters": {
                            "lacp_in_pkts": 87,
                            "lacp_out_pkts": 79,
                            "marker_in_pkts": 0,
                            "marker_out_pkts": 0,
                            "lacp_errors": 0,
                        }
                    }
                }
            },
            "port-channel2": {
                "members": {
                    "Ethernet1/3": {
                        "interface": "Ethernet1/3",
                        "counters": {
                            "lacp_in_pkts": 112,
                            "lacp_out_pkts": 136,
                            "marker_in_pkts": 0,
                            "marker_out_pkts": 0,
                            "lacp_errors": 0,
                        }
                    },
                    "Ethernet1/4": {
                        "interface": "Ethernet1/4",
                        "counters": {
                            "lacp_in_pkts": 90,
                            "lacp_out_pkts": 95,
                            "marker_in_pkts": 0,
                            "marker_out_pkts": 0,
                            "lacp_errors": 0,
                        }
                    },
                    "Ethernet1/5": {
                        "interface": "Ethernet1/5",
                        "counters": {
                            "lacp_in_pkts": 146,
                            "lacp_out_pkts": 118,
                            "marker_in_pkts": 0,
                            "marker_out_pkts": 0,
                            "lacp_errors": 0,
                        }
                    }
                }
            }
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLacpCounters(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowLacpCounters(device=self.device)
        parsed_output = obj.parse()
        self.assertDictEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()
