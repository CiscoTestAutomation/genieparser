# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_pva_traffic
from genie.libs.parser.bigip.get_sys_pva_traffic import SysPvatraffic

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/pva-traffic'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:pva-traffic:pva-trafficstats",
            "selfLink": "https://localhost/mgmt/tm/sys/pva-traffic?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/pva-traffic/0.0": {
                    "nestedStats": {
                        "entries": {
                            "currPvaAssistConn": {"value": 0},
                            "hardwareSyncookiesDetected": {"value": 0},
                            "hardwareSyncookiesGenerated": {"value": 0},
                            "pvaClientSideTraffic.bitsIn": {"value": 0},
                            "pvaClientSideTraffic.bitsOut": {"value": 0},
                            "pvaClientSideTraffic.curConns": {"value": 0},
                            "pvaClientSideTraffic.maxConns": {"value": 0},
                            "pvaClientSideTraffic.pktsIn": {"value": 0},
                            "pvaClientSideTraffic.pktsOut": {"value": 0},
                            "pvaClientSideTraffic.totConns": {"value": 0},
                            "pvaId": {"description": "0.0"},
                            "pvaServerSideTraffic.bitsIn": {"value": 0},
                            "pvaServerSideTraffic.bitsOut": {"value": 0},
                            "pvaServerSideTraffic.curConns": {"value": 0},
                            "pvaServerSideTraffic.maxConns": {"value": 0},
                            "pvaServerSideTraffic.pktsIn": {"value": 0},
                            "pvaServerSideTraffic.pktsOut": {"value": 0},
                            "pvaServerSideTraffic.totConns": {"value": 0},
                            "totPvaAssistConn": {"value": 0},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/pva-traffic/0.1": {
                    "nestedStats": {
                        "entries": {
                            "currPvaAssistConn": {"value": 0},
                            "hardwareSyncookiesDetected": {"value": 0},
                            "hardwareSyncookiesGenerated": {"value": 0},
                            "pvaClientSideTraffic.bitsIn": {"value": 0},
                            "pvaClientSideTraffic.bitsOut": {"value": 0},
                            "pvaClientSideTraffic.curConns": {"value": 0},
                            "pvaClientSideTraffic.maxConns": {"value": 0},
                            "pvaClientSideTraffic.pktsIn": {"value": 0},
                            "pvaClientSideTraffic.pktsOut": {"value": 0},
                            "pvaClientSideTraffic.totConns": {"value": 0},
                            "pvaId": {"description": "0.1"},
                            "pvaServerSideTraffic.bitsIn": {"value": 0},
                            "pvaServerSideTraffic.bitsOut": {"value": 0},
                            "pvaServerSideTraffic.curConns": {"value": 0},
                            "pvaServerSideTraffic.maxConns": {"value": 0},
                            "pvaServerSideTraffic.pktsIn": {"value": 0},
                            "pvaServerSideTraffic.pktsOut": {"value": 0},
                            "pvaServerSideTraffic.totConns": {"value": 0},
                            "totPvaAssistConn": {"value": 0},
                        }
                    }
                },
            },
        }


class test_get_sys_pva_traffic(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "entries": {
            "https://localhost/mgmt/tm/sys/pva-traffic/0.0": {
                "nestedStats": {
                    "entries": {
                        "currPvaAssistConn": {"value": 0},
                        "hardwareSyncookiesDetected": {"value": 0},
                        "hardwareSyncookiesGenerated": {"value": 0},
                        "pvaClientSideTraffic.bitsIn": {"value": 0},
                        "pvaClientSideTraffic.bitsOut": {"value": 0},
                        "pvaClientSideTraffic.curConns": {"value": 0},
                        "pvaClientSideTraffic.maxConns": {"value": 0},
                        "pvaClientSideTraffic.pktsIn": {"value": 0},
                        "pvaClientSideTraffic.pktsOut": {"value": 0},
                        "pvaClientSideTraffic.totConns": {"value": 0},
                        "pvaId": {"description": "0.0"},
                        "pvaServerSideTraffic.bitsIn": {"value": 0},
                        "pvaServerSideTraffic.bitsOut": {"value": 0},
                        "pvaServerSideTraffic.curConns": {"value": 0},
                        "pvaServerSideTraffic.maxConns": {"value": 0},
                        "pvaServerSideTraffic.pktsIn": {"value": 0},
                        "pvaServerSideTraffic.pktsOut": {"value": 0},
                        "pvaServerSideTraffic.totConns": {"value": 0},
                        "totPvaAssistConn": {"value": 0},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/pva-traffic/0.1": {
                "nestedStats": {
                    "entries": {
                        "currPvaAssistConn": {"value": 0},
                        "hardwareSyncookiesDetected": {"value": 0},
                        "hardwareSyncookiesGenerated": {"value": 0},
                        "pvaClientSideTraffic.bitsIn": {"value": 0},
                        "pvaClientSideTraffic.bitsOut": {"value": 0},
                        "pvaClientSideTraffic.curConns": {"value": 0},
                        "pvaClientSideTraffic.maxConns": {"value": 0},
                        "pvaClientSideTraffic.pktsIn": {"value": 0},
                        "pvaClientSideTraffic.pktsOut": {"value": 0},
                        "pvaClientSideTraffic.totConns": {"value": 0},
                        "pvaId": {"description": "0.1"},
                        "pvaServerSideTraffic.bitsIn": {"value": 0},
                        "pvaServerSideTraffic.bitsOut": {"value": 0},
                        "pvaServerSideTraffic.curConns": {"value": 0},
                        "pvaServerSideTraffic.maxConns": {"value": 0},
                        "pvaServerSideTraffic.pktsIn": {"value": 0},
                        "pvaServerSideTraffic.pktsOut": {"value": 0},
                        "pvaServerSideTraffic.totConns": {"value": 0},
                        "totPvaAssistConn": {"value": 0},
                    }
                }
            },
        },
        "kind": "tm:sys:pva-traffic:pva-trafficstats",
        "selfLink": "https://localhost/mgmt/tm/sys/pva-traffic?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysPvatraffic(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysPvatraffic(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
