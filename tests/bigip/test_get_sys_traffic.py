# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_traffic
from genie.libs.parser.bigip.get_sys_traffic import SysTraffic

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/traffic'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:traffic:trafficstats",
            "selfLink": "https://localhost/mgmt/tm/sys/traffic?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/traffic/0": {
                    "nestedStats": {
                        "entries": {
                            "clientSideTraffic.bitsIn": {"value": 1673280},
                            "clientSideTraffic.bitsOut": {"value": 6400},
                            "clientSideTraffic.curConns": {"value": 10},
                            "clientSideTraffic.evictedConns": {"value": 0},
                            "clientSideTraffic.maxConns": {"value": 12},
                            "clientSideTraffic.pktsIn": {"value": 3980},
                            "clientSideTraffic.pktsOut": {"value": 20},
                            "clientSideTraffic.slowKilled": {"value": 0},
                            "clientSideTraffic.totConns": {"value": 3915},
                            "connectionMemoryErrors": {"value": 0},
                            "droppedPackets": {"value": 0},
                            "fiveMinAvgClientSideTraffic.bitsIn": {"value": 336},
                            "fiveMinAvgClientSideTraffic.bitsOut": {"value": 0},
                            "fiveMinAvgClientSideTraffic.pktsIn": {"value": 1},
                            "fiveMinAvgClientSideTraffic.pktsOut": {"value": 0},
                            "fiveMinAvgClientSideTraffic.totConns": {"value": 1},
                            "fiveMinAvgServerSideTraffic.bitsIn": {"value": 328},
                            "fiveMinAvgServerSideTraffic.bitsOut": {"value": 0},
                            "fiveMinAvgServerSideTraffic.pktsIn": {"value": 1},
                            "fiveMinAvgServerSideTraffic.pktsOut": {"value": 0},
                            "fiveMinAvgServerSideTraffic.totConns": {"value": 1},
                            "fiveSecAvgClientSideTraffic.bitsIn": {"value": 168},
                            "fiveSecAvgClientSideTraffic.bitsOut": {"value": 0},
                            "fiveSecAvgClientSideTraffic.pktsIn": {"value": 0},
                            "fiveSecAvgClientSideTraffic.pktsOut": {"value": 0},
                            "fiveSecAvgClientSideTraffic.totConns": {"value": 1},
                            "fiveSecAvgServerSideTraffic.bitsIn": {"value": 416},
                            "fiveSecAvgServerSideTraffic.bitsOut": {"value": 0},
                            "fiveSecAvgServerSideTraffic.pktsIn": {"value": 1},
                            "fiveSecAvgServerSideTraffic.pktsOut": {"value": 0},
                            "fiveSecAvgServerSideTraffic.totConns": {"value": 1},
                            "hardwareSyncookiesDetected": {"value": 0},
                            "hardwareSyncookiesGenerated": {"value": 0},
                            "httpRequests": {"value": 0},
                            "incomingPacketErrors": {"value": 0},
                            "licenseDeny": {"value": 0},
                            "maintenanceModeDeny": {"value": 0},
                            "maxConnVirtualAddressDeny": {"value": 0},
                            "maxConnVirtualPathDeny": {"value": 0},
                            "noHandlerDeny": {"value": 0},
                            "noStagedHandlerDeny": {"value": 0},
                            "oneMinAvgClientSideTraffic.bitsIn": {"value": 312},
                            "oneMinAvgClientSideTraffic.bitsOut": {"value": 0},
                            "oneMinAvgClientSideTraffic.pktsIn": {"value": 1},
                            "oneMinAvgClientSideTraffic.pktsOut": {"value": 0},
                            "oneMinAvgClientSideTraffic.totConns": {"value": 1},
                            "oneMinAvgServerSideTraffic.bitsIn": {"value": 336},
                            "oneMinAvgServerSideTraffic.bitsOut": {"value": 0},
                            "oneMinAvgServerSideTraffic.pktsIn": {"value": 1},
                            "oneMinAvgServerSideTraffic.pktsOut": {"value": 0},
                            "oneMinAvgServerSideTraffic.totConns": {"value": 1},
                            "outgoingPacketErrors": {"value": 0},
                            "serverSideTraffic.bitsIn": {"value": 1679296},
                            "serverSideTraffic.bitsOut": {"value": 0},
                            "serverSideTraffic.curConns": {"value": 10},
                            "serverSideTraffic.evictedConns": {"value": 0},
                            "serverSideTraffic.maxConns": {"value": 12},
                            "serverSideTraffic.pktsIn": {"value": 4000},
                            "serverSideTraffic.pktsOut": {"value": 0},
                            "serverSideTraffic.slowKilled": {"value": 0},
                            "serverSideTraffic.totConns": {"value": 3915},
                            "tmauth.curSessions": {"value": 0},
                            "tmauth.errorResults": {"value": 0},
                            "tmauth.failureResults": {"value": 0},
                            "tmauth.maxSessions": {"value": 0},
                            "tmauth.successResults": {"value": 0},
                            "tmauth.totSessions": {"value": 0},
                            "tmauth.wantcredentialResults": {"value": 0},
                            "virtualServerNonSynDeny": {"value": 0},
                        }
                    }
                }
            },
        }


class test_get_sys_traffic(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "kind": "tm:sys:traffic:trafficstats",
        "selfLink": "https://localhost/mgmt/tm/sys/traffic?ver=14.1.2.1",
        "entries": {
            "https://localhost/mgmt/tm/sys/traffic/0": {
                "nestedStats": {
                    "entries": {
                        "clientSideTraffic.bitsIn": {"value": 1673280},
                        "clientSideTraffic.bitsOut": {"value": 6400},
                        "clientSideTraffic.curConns": {"value": 10},
                        "clientSideTraffic.evictedConns": {"value": 0},
                        "clientSideTraffic.maxConns": {"value": 12},
                        "clientSideTraffic.pktsIn": {"value": 3980},
                        "clientSideTraffic.pktsOut": {"value": 20},
                        "clientSideTraffic.slowKilled": {"value": 0},
                        "clientSideTraffic.totConns": {"value": 3915},
                        "connectionMemoryErrors": {"value": 0},
                        "droppedPackets": {"value": 0},
                        "fiveMinAvgClientSideTraffic.bitsIn": {"value": 336},
                        "fiveMinAvgClientSideTraffic.bitsOut": {"value": 0},
                        "fiveMinAvgClientSideTraffic.pktsIn": {"value": 1},
                        "fiveMinAvgClientSideTraffic.pktsOut": {"value": 0},
                        "fiveMinAvgClientSideTraffic.totConns": {"value": 1},
                        "fiveMinAvgServerSideTraffic.bitsIn": {"value": 328},
                        "fiveMinAvgServerSideTraffic.bitsOut": {"value": 0},
                        "fiveMinAvgServerSideTraffic.pktsIn": {"value": 1},
                        "fiveMinAvgServerSideTraffic.pktsOut": {"value": 0},
                        "fiveMinAvgServerSideTraffic.totConns": {"value": 1},
                        "fiveSecAvgClientSideTraffic.bitsIn": {"value": 168},
                        "fiveSecAvgClientSideTraffic.bitsOut": {"value": 0},
                        "fiveSecAvgClientSideTraffic.pktsIn": {"value": 0},
                        "fiveSecAvgClientSideTraffic.pktsOut": {"value": 0},
                        "fiveSecAvgClientSideTraffic.totConns": {"value": 1},
                        "fiveSecAvgServerSideTraffic.bitsIn": {"value": 416},
                        "fiveSecAvgServerSideTraffic.bitsOut": {"value": 0},
                        "fiveSecAvgServerSideTraffic.pktsIn": {"value": 1},
                        "fiveSecAvgServerSideTraffic.pktsOut": {"value": 0},
                        "fiveSecAvgServerSideTraffic.totConns": {"value": 1},
                        "hardwareSyncookiesDetected": {"value": 0},
                        "hardwareSyncookiesGenerated": {"value": 0},
                        "httpRequests": {"value": 0},
                        "incomingPacketErrors": {"value": 0},
                        "licenseDeny": {"value": 0},
                        "maintenanceModeDeny": {"value": 0},
                        "maxConnVirtualAddressDeny": {"value": 0},
                        "maxConnVirtualPathDeny": {"value": 0},
                        "noHandlerDeny": {"value": 0},
                        "noStagedHandlerDeny": {"value": 0},
                        "oneMinAvgClientSideTraffic.bitsIn": {"value": 312},
                        "oneMinAvgClientSideTraffic.bitsOut": {"value": 0},
                        "oneMinAvgClientSideTraffic.pktsIn": {"value": 1},
                        "oneMinAvgClientSideTraffic.pktsOut": {"value": 0},
                        "oneMinAvgClientSideTraffic.totConns": {"value": 1},
                        "oneMinAvgServerSideTraffic.bitsIn": {"value": 336},
                        "oneMinAvgServerSideTraffic.bitsOut": {"value": 0},
                        "oneMinAvgServerSideTraffic.pktsIn": {"value": 1},
                        "oneMinAvgServerSideTraffic.pktsOut": {"value": 0},
                        "oneMinAvgServerSideTraffic.totConns": {"value": 1},
                        "outgoingPacketErrors": {"value": 0},
                        "serverSideTraffic.bitsIn": {"value": 1679296},
                        "serverSideTraffic.bitsOut": {"value": 0},
                        "serverSideTraffic.curConns": {"value": 10},
                        "serverSideTraffic.evictedConns": {"value": 0},
                        "serverSideTraffic.maxConns": {"value": 12},
                        "serverSideTraffic.pktsIn": {"value": 4000},
                        "serverSideTraffic.pktsOut": {"value": 0},
                        "serverSideTraffic.slowKilled": {"value": 0},
                        "serverSideTraffic.totConns": {"value": 3915},
                        "tmauth.curSessions": {"value": 0},
                        "tmauth.errorResults": {"value": 0},
                        "tmauth.failureResults": {"value": 0},
                        "tmauth.maxSessions": {"value": 0},
                        "tmauth.successResults": {"value": 0},
                        "tmauth.totSessions": {"value": 0},
                        "tmauth.wantcredentialResults": {"value": 0},
                        "virtualServerNonSynDeny": {"value": 0},
                    }
                }
            }
        },
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysTraffic(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysTraffic(device=self.device, alias="rest", via="rest", context="rest")
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
