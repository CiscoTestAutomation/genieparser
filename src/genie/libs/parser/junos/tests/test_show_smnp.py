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

from genie.libs.parser.junos.show_smnp import ShowSnmpMibWalkSystem, ShowSnmpConfiguration, ShowSnmpStatistics


# =========================================================
# Unit test for show snmp mib walk system
# =========================================================
class TestShowSnmpMibWalkSystem(unittest.TestCase):

    device = Device(name="aDevice")

    maxDiff = None

    empty_output = {"execute.return_value": ""}

    golden_parsed_output_1 = {
        "snmp-object-information": {
            "snmp-object": [
                {
                    "name": "sysDescr.0",
                    "object-value": "Juniper "
                    "Networks, Inc. "
                    "vmx internet "
                    "router, kernel "
                    "JUNOS 19.2R1.8, "
                    "Build date: "
                    "2019-06-21 "
                    "21:03:26 UTC "
                    "Copyright (c) "
                    "1996-2019 "
                    "Juniper "
                    "Networks, Inc.",
                },
                {"name": "sysObjectID.0", "object-value": "jnxProductNameVMX"},
                {"name": "sysUpTime.0", "object-value": "1805867174"},
                {"name": "sysContact.0", "object-value": "KHK"},
                {"name": "sysName.0", "object-value": "sr_hktGDS201"},
                {
                    "name": "sysLocation.0",
                    "object-value": "TH-HK2/floor_1B-002/rack_KHK1104",
                },
                {"name": "sysServices.0", "object-value": "6"},
            ]
        }
    }

    golden_output_1 = {
        "execute.return_value": """
            show snmp mib walk system
        sysDescr.0    = Juniper Networks, Inc. vmx internet router, kernel JUNOS 19.2R1.8, Build date: 2019-06-21 21:03:26 UTC Copyright (c) 1996-2019 Juniper Networks, Inc.
        sysObjectID.0 = jnxProductNameVMX
        sysUpTime.0   = 1805867174
        sysContact.0  = KHK
        sysName.0     = sr_hktGDS201
        sysLocation.0 = TH-HK2/floor_1B-002/rack_KHK1104
        sysServices.0 = 6
    """
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSnmpMibWalkSystem(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowSnmpMibWalkSystem(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


class TestShowSnmpConfiguration(unittest.TestCase):

    device = Device(name="aDevice")

    maxDiff = None

    empty_output = {"execute.return_value": ""}

    golden_parsed_output_1 = {
        "configuration": {
            "snmp": {
                "location": "TH-HK2/floor_1B-002/rack_KHK1104",
                "contact": "KHK",
                "community": [
                    {
                        "name": "safaripub",
                        "authorization": "read-only",
                        "clients": [
                            {
                                "name": "106.187.5.0/25"
                            },
                            {
                                "name": "124.211.32.0/24"
                            },
                            {
                                "name": "210.132.90.128/27"
                            },
                            {
                                "name": "210.132.91.0/24"
                            },
                            {
                                "name": "210.224.143.0/24"
                            },
                            {
                                "name": "0.0.0.0/0",
                                "restrict": True
                            },
                            {
                                "name": "2001:268:fd06:1::/64"
                            },
                            {
                                "name": "2001:268:fd06:2::/64"
                            },
                            {
                                "name": "27.85.164.48/28"
                            },
                            {
                                "name": "210.234.255.0/24"
                            },
                            {
                                "name": "125.53.97.0/24"
                            }
                        ]
                    },
                    {
                        "name": "SpiderSDC",
                        "authorization": "read-only",
                        "clients": [
                            {
                                "name": "125.53.99.0/26"
                            }
                        ]
                    },
                    {
                        "name": "kitsune",
                        "authorization": "read-only",
                        "clients": [
                            {
                                "name": "203.141.183.0/24"
                            }
                        ]
                    }
                ],
                "trap-options": {
                    "source-address": "lo0"
                },
                "trap-group": {
                    "name": "safaripub",
                    "version": "v1",
                    "categories": [
                        {
                            "name": "chassis"
                        },
                        {
                            "name": "link"
                        },
                        {
                            "name": "routing"
                        },
                    ],
                    "targets": [
                        {
                            "name": "125.53.99.32"
                        },
                        {
                            "name": "106.162.249.67"
                        }
                    ]
                }
            }
        }
    }

    golden_output_1 = {
        "execute.return_value": """
            show configuration snmp
        location TH-HK2/floor_1B-002/rack_KHK1104;
        contact KHK;
        community safaripub {
            authorization read-only;
            clients {
                106.187.5.0/25;
                124.211.32.0/24;
                210.132.90.128/27;
                210.132.91.0/24;
                210.224.143.0/24;
                0.0.0.0/0 restrict;
                2001:268:fd06:1::/64;
                2001:268:fd06:2::/64;
                27.85.164.48/28;
                210.234.255.0/24;
                125.53.97.0/24;
            }
        }
        community SpiderSDC {
            authorization read-only;
            clients {
                125.53.99.0/26;
            }
        }
        community kitsune {
            authorization read-only;
            clients {
                203.141.183.0/24;
            }
        }
        trap-options {
            source-address lo0;
        }
        trap-group safaripub {
            version v1;
            categories {
                chassis;
                link;
                routing;
            }
            targets {
                125.53.99.32;                   
                106.162.249.67;
            }
        }
    """
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSnmpConfiguration(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowSnmpConfiguration(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


class TestShowSnmpStatistics(unittest.TestCase):

    device = Device(name="aDevice")

    maxDiff = None

    empty_output = {"execute.return_value": ""}

    golden_parsed_output_1 = {
        "snmp-statistics": {
            "snmp-input-statistics": {
                "packets": "8",
                "bad-versions": "0",
                "bad-community-names": "0",
                "bad-community-uses": "0",
                "asn-parse-errors": "0",
                "too-bigs": "0",
                "no-such-names": "0",
                "bad-values": "0",
                "read-onlys": "0",
                "general-errors": "0",
                "total-request-varbinds": "8",
                "total-set-varbinds": "0",
                "get-requests": "0",
                "get-nexts": "8",
                "set-requests": "0",
                "get-responses": "0",
                "traps": "0",
                "silent-drops": "0",
                "proxy-drops": "0",
                "commit-pending-drops": "0",
                "throttle-drops": "0",
                "duplicate-request-drops": "0"
            },
            "snmp-v3-input-statistics": {
                "unknown-secmodels": "0",
                "invalid-msgs": "0",
                "unknown-pduhandlers": "0",
                "unavail-contexts": "0",
                "unknown-contexts": "0",
                "unsupported-seclevels": "0",
                "not-in-timewindows": "0",
                "unknown-usernames": "0",
                "unknown-eids": "0",
                "wrong-digests": "0",
                "decrypt-errors": "0"
            },
            "snmp-output-statistics": {
                "packets": "8",
                "too-bigs": "0",
                "no-such-names": "0",
                "bad-values": "0",
                "general-errors": "0",
                "get-requests": "0",
                "get-nexts": "0",
                "set-requests": "0",
                "get-responses": "8",
                "traps": "0"
            },
            "snmp-performance-statistics": {
                "average-response-time": "10.91",
                "one-minute-request-throughput": "0",
                "five-minute-request-throughput": "0",
                "fifteen-minute-request-throughput": "0",
                "one-minute-response-throughput": "0",
                "five-minute-response-throughput": "0",
                "fifteen-minute-response-throughput": "0"
            }
        }
    }

    golden_output_1 = {
        "execute.return_value": """
            show snmp statistics
        SNMP statistics:
            Input:
                Packets: 8, Bad versions: 0, Bad community names: 0,
                Bad community uses: 0, ASN parse errors: 0,
                Too bigs: 0, No such names: 0, Bad values: 0,
                Read onlys: 0, General errors: 0,
                Total request varbinds: 8, Total set varbinds: 0,
                Get requests: 0, Get nexts: 8, Set requests: 0,
                Get responses: 0, Traps: 0,
                Silent drops: 0, Proxy drops: 0, Commit pending drops: 0,
                Throttle drops: 0, Duplicate request drops: 0
            V3 Input:
                Unknown security models: 0, Invalid messages: 0
                Unknown pdu handlers: 0, Unavailable contexts: 0
                Unknown contexts: 0, Unsupported security levels: 0
                Not in time windows: 0, Unknown user names: 0
                Unknown engine ids: 0, Wrong digests: 0, Decryption errors: 0
            Output:
                Packets: 8, Too bigs: 0, No such names: 0,
                Bad values: 0, General errors: 0,
                    Get requests: 0, Get nexts: 0, Set requests: 0,
                Get responses: 8, Traps: 0
            Performance:
                Average response time(ms): 10.91
            Number of requests dispatched to subagents in last:
                1 minute:0, 5 minutes:0, 15 minutes:0
            Number of responses dispatched to NMS in last:
                1 minute:0, 5 minutes:0, 15 minutes:0
    """
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSnmpStatistics(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowSnmpStatistics(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

if __name__ == "__main__":
    unittest.main()