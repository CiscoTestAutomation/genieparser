# Python
import unittest
from unittest.mock import Mock

# pyATS
from pyats.topology import (Device, loader)

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# junos show_arp
from genie.libs.parser.junos.show_ddos import ShowDdosProtectionStatistics


class TestShowDdosProtectionStatistics(unittest.TestCase):
    """ Unit tests for:
            * show ddos-protection statistics
    """

    device = Device(name='aDevice')
    maxDiff = None
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value':'''
            show ddos-protection statistics 
            DDOS protection global statistics:
            Policing on routing engine:         Yes
            Policing on FPC:                    Yes
            Flow detection:                     No
            Logging:                            Yes
            Policer violation report rate:      100
            Flow report rate:                   100
            Default flow detection mode         Automatic
            Default flow level detection mode   Automatic
            Default flow level control mode     Drop
            Currently violated packet types:    0
            Packet types have seen violations:  0
            Total violation counts:             0
            Currently tracked flows:            0
            Total detected flows:               0
    '''}

    golden_parsed_output =  {
            "ddos-statistics-information": {
                "aggr-level-control-mode": "Drop",
                "aggr-level-detection-mode": "Automatic",
                "ddos-flow-detection-enabled": "No",
                "ddos-logging-enabled": "Yes",
                "ddos-policing-fpc-enabled": "Yes",
                "ddos-policing-re-enabled": "Yes",
                "detection-mode": "Automatic",
                "flow-report-rate": "100",
                "flows-cumulative": "0",
                "flows-current": "0",
                "packet-types-in-violation": "0",
                "packet-types-seen-violation": "0",
                "total-violations": "0",
                "violation-report-rate": "100"
            }
        }


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowDdosProtectionStatistics(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowDdosProtectionStatistics(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)    

if __name__ == '__main__':
    unittest.main()        