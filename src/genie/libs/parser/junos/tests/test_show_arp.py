# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# junos show_arp
from genie.libs.parser.junos.show_arp import (ShowArp)


class TestShowArp(unittest.TestCase):
    """ Unit tests for:
            * show arp
    """

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show arp | no-more
        MAC Address       Address         Name                      Interface               Flags
        00:50:56:8d:2d:e1 1.0.0.1         1.0.0.1                   fxp0.0                  none
        00:50:56:8d:fd:53 1.0.0.201       1.0.0.201                 fxp0.0                  none
        50:3d:e5:cf:5f:36 27.86.198.26    27.86.198.26              ge-0/0/2.0              none
        00:50:56:8d:05:76 100.0.0.1       100.0.0.1                 ge-0/0/3.0              none
        00:50:56:8d:72:bd 106.187.14.121  106.187.14.121            ge-0/0/1.0              none
        00:50:56:8d:53:c0 111.87.5.94     111.87.5.94               ge-0/0/0.0              none
        00:50:56:8d:38:36 128.0.0.16      fpc0                      em1.0                   none
        Total entries: 7
    '''}
    
    golden_parsed_output = {
        "arp-table-information": {
            "arp-entry-count": "7",
            "arp-table-entry": [
                {
                    "arp-table-entry-flags": "none",
                    "hostname": "1.0.0.1",
                    "interface-name": "fxp0.0",
                    "ip-address": "1.0.0.1",
                    "mac-address": "00:50:56:8d:2d:e1"
                },
                {
                    "arp-table-entry-flags": "none",
                    "hostname": "1.0.0.201",
                    "interface-name": "fxp0.0",
                    "ip-address": "1.0.0.201",
                    "mac-address": "00:50:56:8d:fd:53"
                },
                {
                    "arp-table-entry-flags": "none",
                    "hostname": "27.86.198.26",
                    "interface-name": "ge-0/0/2.0",
                    "ip-address": "27.86.198.26",
                    "mac-address": "50:3d:e5:cf:5f:36"
                },
                {
                    "arp-table-entry-flags": "none",
                    "hostname": "100.0.0.1",
                    "interface-name": "ge-0/0/3.0",
                    "ip-address": "100.0.0.1",
                    "mac-address": "00:50:56:8d:05:76"
                },
                {
                    "arp-table-entry-flags": "none",
                    "hostname": "106.187.14.121",
                    "interface-name": "ge-0/0/1.0",
                    "ip-address": "106.187.14.121",
                    "mac-address": "00:50:56:8d:72:bd"
                },
                {
                    "arp-table-entry-flags": "none",
                    "hostname": "111.87.5.94",
                    "interface-name": "ge-0/0/0.0",
                    "ip-address": "111.87.5.94",
                    "mac-address": "00:50:56:8d:53:c0"
                },
                {
                    "arp-table-entry-flags": "none",
                    "hostname": "fpc0",
                    "interface-name": "em1.0",
                    "ip-address": "128.0.0.16",
                    "mac-address": "00:50:56:8d:38:36"
                }
            ]
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowArp(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowArp(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()