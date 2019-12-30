# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_cm_failover_status
from genie.libs.parser.bigip.get_cm_failover_status import CmFailoverstatus

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/cm/failover-status'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:cm:failover-status:failover-statusstats",
            "selfLink": "https://localhost/mgmt/tm/cm/failover-status?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/cm/failover-status/0": {
                    "nestedStats": {
                        "entries": {
                            "color": {"description": "green"},
                            "https://localhost/mgmt/tm/cm/failoverStatus/0/details": {
                                "nestedStats": {
                                    "entries": {
                                        "https://localhost/mgmt/tm/cm/failoverStatus/0/details/0": {
                                            "nestedStats": {
                                                "entries": {
                                                    "details": {
                                                        "description": "active for /Common/traffic-group-1"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            },
                            "status": {"description": "ACTIVE"},
                            "summary": {"description": "1/1 active"},
                        }
                    }
                }
            },
        }


class test_get_cm_failover_status(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "entries": {
            "https://localhost/mgmt/tm/cm/failover-status/0": {
                "nestedStats": {
                    "entries": {
                        "color": {"description": "green"},
                        "https://localhost/mgmt/tm/cm/failoverStatus/0/details": {
                            "nestedStats": {
                                "entries": {
                                    "https://localhost/mgmt/tm/cm/failoverStatus/0/details/0": {
                                        "nestedStats": {
                                            "entries": {
                                                "details": {
                                                    "description": "active "
                                                    "for "
                                                    "/Common/traffic-group-1"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "status": {"description": "ACTIVE"},
                        "summary": {"description": "1/1 " "active"},
                    }
                }
            }
        },
        "kind": "tm:cm:failover-status:failover-statusstats",
        "selfLink": "https://localhost/mgmt/tm/cm/failover-status?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = CmFailoverstatus(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = CmFailoverstatus(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
