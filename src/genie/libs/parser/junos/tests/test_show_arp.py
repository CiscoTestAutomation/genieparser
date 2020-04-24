# Python
import unittest
from unittest.mock import Mock

# PyATS
from pyats.topology import (Device, loader)

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# junos show_arp
from genie.libs.parser.junos.show_arp import ShowArp,\
                                             ShowArpNoResolve


class TestShowArp(unittest.TestCase):
    """ Unit tests for:
            * show arp
    """

    device = Device(name='aDevice')
    maxDiff = None
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show arp
        MAC Address       Address         Name                      Interface               Flags
        00:50:56:ff:ba:6f 10.1.0.1         10.1.0.1                   fxp0.0                  none
        00:50:56:ff:8b:e0 10.1.0.201       10.1.0.201                 fxp0.0                  none
        50:3d:e5:ff:2f:06 10.19.198.26    10.19.198.26              ge-0/0/2.0              none
        00:50:56:ff:92:04 10.55.0.1       10.55.0.1                 ge-0/0/3.0              none
        00:50:56:ff:00:4b 10.169.14.121  10.169.14.121            ge-0/0/1.0              none
        00:50:56:ff:e0:4e 10.189.5.94     10.189.5.94               ge-0/0/0.0              none
        00:50:56:ff:c5:c3 172.16.64.16      fpc0                      em1.0                   none
        Total entries: 7
    '''}
    
    golden_parsed_output = {
        "arp-table-information": {
            "arp-entry-count": "7",
            "arp-table-entry": [
                {
                    "arp-table-entry-flags": "none",
                    "hostname": "10.1.0.1",
                    "interface-name": "fxp0.0",
                    "ip-address": "10.1.0.1",
                    "mac-address": "00:50:56:ff:ba:6f"
                },
                {
                    "arp-table-entry-flags": "none",
                    "hostname": "10.1.0.201",
                    "interface-name": "fxp0.0",
                    "ip-address": "10.1.0.201",
                    "mac-address": "00:50:56:ff:8b:e0"
                },
                {
                    "arp-table-entry-flags": "none",
                    "hostname": "10.19.198.26",
                    "interface-name": "ge-0/0/2.0",
                    "ip-address": "10.19.198.26",
                    "mac-address": "50:3d:e5:ff:2f:06"
                },
                {
                    "arp-table-entry-flags": "none",
                    "hostname": "10.55.0.1",
                    "interface-name": "ge-0/0/3.0",
                    "ip-address": "10.55.0.1",
                    "mac-address": "00:50:56:ff:92:04"
                },
                {
                    "arp-table-entry-flags": "none",
                    "hostname": "10.169.14.121",
                    "interface-name": "ge-0/0/1.0",
                    "ip-address": "10.169.14.121",
                    "mac-address": "00:50:56:ff:00:4b"
                },
                {
                    "arp-table-entry-flags": "none",
                    "hostname": "10.189.5.94",
                    "interface-name": "ge-0/0/0.0",
                    "ip-address": "10.189.5.94",
                    "mac-address": "00:50:56:ff:e0:4e"
                },
                {
                    "arp-table-entry-flags": "none",
                    "hostname": "fpc0",
                    "interface-name": "em1.0",
                    "ip-address": "172.16.64.16",
                    "mac-address": "00:50:56:ff:c5:c3"
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

class TestShowArpNoResolve(unittest.TestCase):
    """ Unit tests for:
            * show arp no-resolve
    """

    device = Device(name='aDevice')
    maxDiff = None
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show arp no-resolve
        MAC Address       Address         Interface                Flags
        00:50:56:ff:ba:6f 10.1.0.1         fxp0.0                   none
        00:50:56:ff:8b:e0 10.1.0.201       fxp0.0                   none
        50:3d:e5:ff:2f:06 10.19.198.26    ge-0/0/2.0               none
        00:50:56:ff:92:04 10.55.0.1       ge-0/0/3.0               none
        00:50:56:ff:00:4b 10.169.14.121  ge-0/0/1.0               none
        00:50:56:ff:e0:4e 10.189.5.94     ge-0/0/0.0               none
        00:50:56:ff:c5:c3 172.16.64.16      em1.0                    none
        Total entries: 7
    '''}
    
    golden_parsed_output = {
        "arp-table-information": {
            "arp-entry-count": "7",
            "arp-table-entry": [
                {
                    "arp-table-entry-flags": "none",
                    "interface-name": "fxp0.0",
                    "ip-address": "10.1.0.1",
                    "mac-address": "00:50:56:ff:ba:6f"
                },
                {
                    "arp-table-entry-flags": "none",
                    "interface-name": "fxp0.0",
                    "ip-address": "10.1.0.201",
                    "mac-address": "00:50:56:ff:8b:e0"
                },
                {
                    "arp-table-entry-flags": "none",
                    "interface-name": "ge-0/0/2.0",
                    "ip-address": "10.19.198.26",
                    "mac-address": "50:3d:e5:ff:2f:06"
                },
                {
                    "arp-table-entry-flags": "none",
                    "interface-name": "ge-0/0/3.0",
                    "ip-address": "10.55.0.1",
                    "mac-address": "00:50:56:ff:92:04"
                },
                {
                    "arp-table-entry-flags": "none",
                    "interface-name": "ge-0/0/1.0",
                    "ip-address": "10.169.14.121",
                    "mac-address": "00:50:56:ff:00:4b"
                },
                {
                    "arp-table-entry-flags": "none",
                    "interface-name": "ge-0/0/0.0",
                    "ip-address": "10.189.5.94",
                    "mac-address": "00:50:56:ff:e0:4e"
                },
                {
                    "arp-table-entry-flags": "none",
                    "interface-name": "em1.0",
                    "ip-address": "172.16.64.16",
                    "mac-address": "00:50:56:ff:c5:c3"
                }
            ]
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowArpNoResolve(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowArpNoResolve(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()