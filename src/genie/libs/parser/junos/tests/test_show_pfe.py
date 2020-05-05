# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import (
    SchemaEmptyParserError,
    SchemaMissingKeyError,
)

# Parser
from genie.libs.parser.junos.show_pfe import (
    ShowPfeStatisticsTraffic,
    ShowPfeRouteSummary,
    ShowPfeStatisticsIpIcmp,
)


# =========================================================
# Unit test for show pfe statistics traffic
# =========================================================
class test_show_pfe_statistics_traffic(unittest.TestCase):

    device = Device(name="aDevice")
    empty_output = {"execute.return_value": ""}
    maxDiff = None

    golden_parsed_output_1 = {
        "pfe-statistics": {
            "pfe-chip-statistics": {
                "input-checksum": "0",
                "output-mtu": "0"
            },
            "pfe-hardware-discard-statistics": {
                "bad-route-discard": "962415",
                "bits-to-test-discard": "0",
                "data-error-discard": "0",
                "fabric-discard": "0",
                "info-cell-discard": "0",
                "invalid-iif-discard": "0",
                "nexthop-discard": "0",
                "stack-overflow-discard": "0",
                "stack-underflow-discard": "0",
                "tcp-header-error-discard": "0",
                "timeout-discard": "0",
                "truncated-key-discard": "0",
            },
            "pfe-local-protocol-statistics": {
                "arp-count": "56818",
                "atm-oam-count": "0",
                "bfd-count": "82347033",
                "ether-oam-count": "0",
                "fr-lmi-count": "0",
                "hdlc-keepalive-count": "0",
                "isis-iih-count": "0",
                "lacp-count": "0",
                "ldp-hello-count": "3462026",
                "ospf-hello-count": "5732336",
                "ospf3-hello-count": "4146329",
                "ppp-lcp-ncp-count": "0",
                "rsvp-hello-count": "7040269",
                "unknown-count": "0",
            },
            "pfe-local-traffic-statistics": {
                "hardware-input-drops": "0",
                "pfe-input-packets": "184259247",
                "pfe-output-packets": "370506284",
                "software-input-control-drops": "0",
                "software-input-high-drops": "0",
                "software-input-low-drops": "0",
                "software-input-medium-drops": "0",
                "software-output-low-drops": "0",
            },
            "pfe-traffic-statistics": {
                "input-pps": "14",
                "output-pps": "16",
                "pfe-fabric-input": "0",
                "pfe-fabric-input-pps": "0",
                "pfe-fabric-output": "0",
                "pfe-fabric-output-pps": "0",
                "pfe-input-packets": "763584752",
                "pfe-output-packets": "728623201",
            },
        }
    }

    golden_output_1 = {
        "execute.return_value":
        """
                show pfe statistics traffic
        Packet Forwarding Engine traffic statistics:
            Input  packets:            763584752                   14 pps
            Output packets:            728623201                   16 pps
            Fabric Input  :                    0                    0 pps
            Fabric Output :                    0                    0 pps
        Packet Forwarding Engine local traffic statistics:
            Local packets input                 :            184259247
            Local packets output                :            370506284
            Software input control plane drops  :                    0
            Software input high drops           :                    0
            Software input medium drops         :                    0
            Software input low drops            :                    0
            Software output drops               :                    0
            Hardware input drops                :                    0
        Packet Forwarding Engine local protocol statistics:
            HDLC keepalives            :                    0
            ATM OAM                    :                    0
            Frame Relay LMI            :                    0
            PPP LCP/NCP                :                    0
            OSPF hello                 :              5732336
            OSPF3 hello                :              4146329
            RSVP hello                 :              7040269
            LDP hello                  :              3462026
            BFD                        :             82347033
            IS-IS IIH                  :                    0
            LACP                       :                    0
            ARP                        :                56818
            ETHER OAM                  :                    0
            Unknown                    :                    0
        Packet Forwarding Engine hardware discard statistics:
            Timeout                    :                    0
            Truncated key              :                    0
            Bits to test               :                    0
            Data error                 :                    0
            TCP header length error    :                    0
            Stack underflow            :                    0
            Stack overflow             :                    0
            Normal discard             :               962415
            Extended discard           :                    0
            Invalid interface          :                    0
            Info cell drops            :                    0
            Fabric drops               :                    0
        Packet Forwarding Engine Input IPv4 Header Checksum Error and Output MTU Error statistics:
            Input Checksum             :                    0
            Output MTU                 :                    0

    """
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowPfeStatisticsTraffic(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowPfeStatisticsTraffic(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


# =========================================================
# Unit test for show pfe statistics ip icmp
# =========================================================
class TestShowPfeStatisticsIpIcmp(unittest.TestCase):

    device = Device(name="aDevice")
    empty_output = {"execute.return_value": ""}
    maxDiff = None

    golden_parsed_output_1 = {
        "pfe-statistics": {
            "icmp-discards": {
                "bad-dest-addresses": "0",
                "bad-source-addresses": "0",
                "icmp-errors": "0",
                "ip-fragments": "0",
                "multicasts": "0",
            },
            "icmp-errors": {
                "bad-input-interface": "0",
                "invalid-icmp-type": "0",
                "invalid-protocol": "0",
                "runts": "0",
                "throttled-icmps": "575",
                "unknown-unreachables": "0",
                "unprocessed-redirects": "0",
                "unsupported-icmp-type": "0",
            },
            "icmp-statistics": {
                "icmp-option-handoffs": "0",
                "mtu-exceeded": "0",
                "network-unreachables": "311",
                "redirects": "0",
                "requests": "246259",
                "ttl-captured": "0",
                "ttl-expired": "245373",
            },
        }
    }

    golden_output_1 = {
        "execute.return_value":
        """
                show pfe statistics ip icmp
            ICMP Statistics:
                246259 requests
                    311 network unreachables
                245373 ttl expired
                    0 ttl captured
                    0 redirects
                    0 mtu exceeded
                    0 icmp/option handoffs

            ICMP Errors:
                    0 unknown unreachables
                    0 unsupported ICMP type
                    0 unprocessed redirects
                    0 invalid ICMP type
                    0 invalid protocol
                    0 bad input interface
                    575 throttled icmps
                    0 runts

            ICMP Discards:
                    0 multicasts
                    0 bad source addresses
                    0 bad dest addresses
                    0 IP fragments
                    0 ICMP errors

    """
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowPfeStatisticsIpIcmp(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowPfeStatisticsIpIcmp(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


# =========================================================
# Unit test for show pfe route summary
# =========================================================
class TestShowPfeRouteSummary(unittest.TestCase):

    device = Device(name="aDevice")
    empty_output = {"execute.return_value": ""}
    maxDiff = None

    golden_parsed_output_1 = {
        "slot": {
            "0": {
                "route-tables": {
                    "CLNP": [
                        {
                            "index": "Default",
                            "routes": "1",
                            "size": "136"
                        },
                        {
                            "index": "5",
                            "routes": "1",
                            "size": "136"
                        },
                    ],
                    "DHCP-Snooping": [{
                        "index": "Default",
                        "routes": "1",
                        "size": "136"
                    }],
                    "IPv4": [
                        {
                            "index": "Default",
                            "routes": "944",
                            "size": "132156"
                        },
                        {
                            "index": "1",
                            "routes": "9",
                            "size": "1256"
                        },
                        {
                            "index": "2",
                            "routes": "8",
                            "size": "1116"
                        },
                        {
                            "index": "3",
                            "routes": "5",
                            "size": "696"
                        },
                        {
                            "index": "4",
                            "routes": "9",
                            "size": "1256"
                        },
                        {
                            "index": "5",
                            "routes": "5",
                            "size": "696"
                        },
                        {
                            "index": "36736",
                            "routes": "5",
                            "size": "696"
                        },
                    ],
                    "IPv6": [
                        {
                            "index": "Default",
                            "routes": "39",
                            "size": "5824"
                        },
                        {
                            "index": "1",
                            "routes": "6",
                            "size": "872"
                        },
                        {
                            "index": "5",
                            "routes": "6",
                            "size": "872"
                        },
                    ],
                    "MPLS": [
                        {
                            "index": "Default",
                            "routes": "45",
                            "size": "6296"
                        },
                        {
                            "index": "6",
                            "routes": "1",
                            "size": "136"
                        },
                    ],
                }
            }
        }
    }

    golden_output_1 = {
        "execute.return_value":
        """
            show pfe route summary

            Slot 0


            IPv4 Route Tables:
            Index         Routes     Size(b)
            --------  ----------  ----------
            Default          944      132156
            1                  9        1256
            2                  8        1116
            3                  5         696
            4                  9        1256
            5                  5         696
            36736              5         696

            MPLS Route Tables:
            Index         Routes     Size(b)
            --------  ----------  ----------
            Default           45        6296
            6                  1         136

            IPv6 Route Tables:
            Index         Routes     Size(b)
            --------  ----------  ----------
            Default           39        5824
            1                  6         872
            5                  6         872

            CLNP Route Tables:
            Index         Routes     Size(b)
            --------  ----------  ----------
            Default            1         136
            5                  1         136

            DHCP-Snooping Route Tables:
            Index         Routes     Size(b)
            --------  ----------  ----------
            Default            1         136
    """
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowPfeRouteSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowPfeRouteSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


if __name__ == "__main__":
    unittest.main()
