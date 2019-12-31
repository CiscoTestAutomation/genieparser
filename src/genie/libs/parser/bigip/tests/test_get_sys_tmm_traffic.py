# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_tmm_traffic
from genie.libs.parser.bigip.get_sys_tmm_traffic import SysTmmtraffic

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/tmm-traffic'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:tmm-traffic:tmm-trafficstats",
            "selfLink": "https://localhost/mgmt/tm/sys/tmm-traffic?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/tmm-traffic/0.0": {
                    "nestedStats": {
                        "entries": {
                            "clientSideTraffic.bitsIn": {"value": 870912},
                            "clientSideTraffic.bitsOut": {"value": 6400},
                            "clientSideTraffic.curConns": {"value": 4},
                            "clientSideTraffic.evictedConns": {"value": 0},
                            "clientSideTraffic.maxConns": {"value": 12},
                            "clientSideTraffic.pktsIn": {"value": 2057},
                            "clientSideTraffic.pktsOut": {"value": 20},
                            "clientSideTraffic.slowKilled": {"value": 0},
                            "clientSideTraffic.totConns": {"value": 1992},
                            "cmpConnRedirected": {"value": 0},
                            "connectionMemoryErrors": {"value": 0},
                            "droppedPackets": {"value": 0},
                            "httpRequests": {"value": 0},
                            "incomingPacketErrors": {"value": 0},
                            "licenseDeny": {"value": 0},
                            "maintenanceModeDeny": {"value": 0},
                            "maxConnVirtualAddressDeny": {"value": 0},
                            "maxConnVirtualPathDeny": {"value": 0},
                            "noHandlerDeny": {"value": 0},
                            "noStagedHandlerDeny": {"value": 0},
                            "outgoingPacketErrors": {"value": 0},
                            "serverSideTraffic.bitsIn": {"value": 876288},
                            "serverSideTraffic.bitsOut": {"value": 0},
                            "serverSideTraffic.curConns": {"value": 4},
                            "serverSideTraffic.evictedConns": {"value": 0},
                            "serverSideTraffic.maxConns": {"value": 12},
                            "serverSideTraffic.pktsIn": {"value": 2075},
                            "serverSideTraffic.pktsOut": {"value": 0},
                            "serverSideTraffic.slowKilled": {"value": 0},
                            "serverSideTraffic.totConns": {"value": 1992},
                            "tmmId": {"description": "0.0"},
                            "virtualServerNonSynDeny": {"value": 0},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/tmm-traffic/0.1": {
                    "nestedStats": {
                        "entries": {
                            "clientSideTraffic.bitsIn": {"value": 808608},
                            "clientSideTraffic.bitsOut": {"value": 0},
                            "clientSideTraffic.curConns": {"value": 5},
                            "clientSideTraffic.evictedConns": {"value": 0},
                            "clientSideTraffic.maxConns": {"value": 7},
                            "clientSideTraffic.pktsIn": {"value": 1938},
                            "clientSideTraffic.pktsOut": {"value": 0},
                            "clientSideTraffic.slowKilled": {"value": 0},
                            "clientSideTraffic.totConns": {"value": 1933},
                            "cmpConnRedirected": {"value": 0},
                            "connectionMemoryErrors": {"value": 0},
                            "droppedPackets": {"value": 0},
                            "httpRequests": {"value": 0},
                            "incomingPacketErrors": {"value": 0},
                            "licenseDeny": {"value": 0},
                            "maintenanceModeDeny": {"value": 0},
                            "maxConnVirtualAddressDeny": {"value": 0},
                            "maxConnVirtualPathDeny": {"value": 0},
                            "noHandlerDeny": {"value": 0},
                            "noStagedHandlerDeny": {"value": 0},
                            "outgoingPacketErrors": {"value": 0},
                            "serverSideTraffic.bitsIn": {"value": 807168},
                            "serverSideTraffic.bitsOut": {"value": 0},
                            "serverSideTraffic.curConns": {"value": 5},
                            "serverSideTraffic.evictedConns": {"value": 0},
                            "serverSideTraffic.maxConns": {"value": 7},
                            "serverSideTraffic.pktsIn": {"value": 1935},
                            "serverSideTraffic.pktsOut": {"value": 0},
                            "serverSideTraffic.slowKilled": {"value": 0},
                            "serverSideTraffic.totConns": {"value": 1933},
                            "tmmId": {"description": "0.1"},
                            "virtualServerNonSynDeny": {"value": 0},
                        }
                    }
                },
            },
        }


class test_get_sys_tmm_traffic(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
            "kind": "tm:sys:tmm-traffic:tmm-trafficstats",
            "selfLink": "https://localhost/mgmt/tm/sys/tmm-traffic?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/tmm-traffic/0.0": {
                    "nestedStats": {
                        "entries": {
                            "clientSideTraffic.bitsIn": {"value": 870912},
                            "clientSideTraffic.bitsOut": {"value": 6400},
                            "clientSideTraffic.curConns": {"value": 4},
                            "clientSideTraffic.evictedConns": {"value": 0},
                            "clientSideTraffic.maxConns": {"value": 12},
                            "clientSideTraffic.pktsIn": {"value": 2057},
                            "clientSideTraffic.pktsOut": {"value": 20},
                            "clientSideTraffic.slowKilled": {"value": 0},
                            "clientSideTraffic.totConns": {"value": 1992},
                            "cmpConnRedirected": {"value": 0},
                            "connectionMemoryErrors": {"value": 0},
                            "droppedPackets": {"value": 0},
                            "httpRequests": {"value": 0},
                            "incomingPacketErrors": {"value": 0},
                            "licenseDeny": {"value": 0},
                            "maintenanceModeDeny": {"value": 0},
                            "maxConnVirtualAddressDeny": {"value": 0},
                            "maxConnVirtualPathDeny": {"value": 0},
                            "noHandlerDeny": {"value": 0},
                            "noStagedHandlerDeny": {"value": 0},
                            "outgoingPacketErrors": {"value": 0},
                            "serverSideTraffic.bitsIn": {"value": 876288},
                            "serverSideTraffic.bitsOut": {"value": 0},
                            "serverSideTraffic.curConns": {"value": 4},
                            "serverSideTraffic.evictedConns": {"value": 0},
                            "serverSideTraffic.maxConns": {"value": 12},
                            "serverSideTraffic.pktsIn": {"value": 2075},
                            "serverSideTraffic.pktsOut": {"value": 0},
                            "serverSideTraffic.slowKilled": {"value": 0},
                            "serverSideTraffic.totConns": {"value": 1992},
                            "tmmId": {"description": "0.0"},
                            "virtualServerNonSynDeny": {"value": 0},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/tmm-traffic/0.1": {
                    "nestedStats": {
                        "entries": {
                            "clientSideTraffic.bitsIn": {"value": 808608},
                            "clientSideTraffic.bitsOut": {"value": 0},
                            "clientSideTraffic.curConns": {"value": 5},
                            "clientSideTraffic.evictedConns": {"value": 0},
                            "clientSideTraffic.maxConns": {"value": 7},
                            "clientSideTraffic.pktsIn": {"value": 1938},
                            "clientSideTraffic.pktsOut": {"value": 0},
                            "clientSideTraffic.slowKilled": {"value": 0},
                            "clientSideTraffic.totConns": {"value": 1933},
                            "cmpConnRedirected": {"value": 0},
                            "connectionMemoryErrors": {"value": 0},
                            "droppedPackets": {"value": 0},
                            "httpRequests": {"value": 0},
                            "incomingPacketErrors": {"value": 0},
                            "licenseDeny": {"value": 0},
                            "maintenanceModeDeny": {"value": 0},
                            "maxConnVirtualAddressDeny": {"value": 0},
                            "maxConnVirtualPathDeny": {"value": 0},
                            "noHandlerDeny": {"value": 0},
                            "noStagedHandlerDeny": {"value": 0},
                            "outgoingPacketErrors": {"value": 0},
                            "serverSideTraffic.bitsIn": {"value": 807168},
                            "serverSideTraffic.bitsOut": {"value": 0},
                            "serverSideTraffic.curConns": {"value": 5},
                            "serverSideTraffic.evictedConns": {"value": 0},
                            "serverSideTraffic.maxConns": {"value": 7},
                            "serverSideTraffic.pktsIn": {"value": 1935},
                            "serverSideTraffic.pktsOut": {"value": 0},
                            "serverSideTraffic.slowKilled": {"value": 0},
                            "serverSideTraffic.totConns": {"value": 1933},
                            "tmmId": {"description": "0.1"},
                            "virtualServerNonSynDeny": {"value": 0},
                        }
                    }
                },
            },
        }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysTmmtraffic(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysTmmtraffic(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
