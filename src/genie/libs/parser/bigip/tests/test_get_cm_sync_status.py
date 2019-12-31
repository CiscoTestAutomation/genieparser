# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_cm_sync_status
from genie.libs.parser.bigip.get_cm_sync_status import CmSyncstatus

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/cm/sync-status'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:cm:sync-status:sync-statusstats",
            "selfLink": "https://localhost/mgmt/tm/cm/sync-status?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/cm/sync-status/0": {
                    "nestedStats": {
                        "entries": {
                            "color": {"description": "green"},
                            "https://localhost/mgmt/tm/cm/syncStatus/0/details": {
                                "nestedStats": {
                                    "entries": {
                                        "https://localhost/mgmt/tm/cm/syncStatus/0/details/0": {
                                            "nestedStats": {
                                                "entries": {
                                                    "details": {
                                                        "description": "Optional action: Add a device to the trust domain"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            },
                            "mode": {"description": "standalone"},
                            "status": {"description": "Standalone"},
                            "summary": {"description": " "},
                        }
                    }
                }
            },
        }


class test_get_cm_sync_status(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "entries": {
            "https://localhost/mgmt/tm/cm/sync-status/0": {
                "nestedStats": {
                    "entries": {
                        "color": {"description": "green"},
                        "https://localhost/mgmt/tm/cm/syncStatus/0/details": {
                            "nestedStats": {
                                "entries": {
                                    "https://localhost/mgmt/tm/cm/syncStatus/0/details/0": {
                                        "nestedStats": {
                                            "entries": {
                                                "details": {
                                                    "description": "Optional "
                                                    "action: "
                                                    "Add "
                                                    "a "
                                                    "device "
                                                    "to "
                                                    "the "
                                                    "trust "
                                                    "domain"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "mode": {"description": "standalone"},
                        "status": {"description": "Standalone"},
                        "summary": {"description": " "},
                    }
                }
            }
        },
        "kind": "tm:cm:sync-status:sync-statusstats",
        "selfLink": "https://localhost/mgmt/tm/cm/sync-status?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = CmSyncstatus(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = CmSyncstatus(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
