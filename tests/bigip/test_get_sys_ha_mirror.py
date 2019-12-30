# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_ha_mirror
from genie.libs.parser.bigip.get_sys_ha_mirror import SysHamirror

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/ha-mirror'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:ha-mirror:ha-mirrorstats",
            "selfLink": "https://localhost/mgmt/tm/sys/ha-mirror?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/ha-mirror/0": {
                    "nestedStats": {
                        "entries": {
                            "aborts": {"value": 0},
                            "buffered": {"value": 0},
                            "errors": {"value": 0},
                            "l4Mirrorable": {"value": 0},
                            "l7Failed": {"value": 0},
                            "l7Mirrorable": {"value": 0},
                            "overflows": {"value": 0},
                            "primaryStatus": {"description": "closed"},
                            "secondaryStatus": {"description": "closed"},
                            "tmid": {"description": "[0.0]"},
                            "trafficGroup": {
                                "description": "/Common/traffic-group-1"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-mirror/1": {
                    "nestedStats": {
                        "entries": {
                            "aborts": {"value": 0},
                            "buffered": {"value": 0},
                            "errors": {"value": 0},
                            "l4Mirrorable": {"value": 0},
                            "l7Failed": {"value": 0},
                            "l7Mirrorable": {"value": 0},
                            "overflows": {"value": 0},
                            "primaryStatus": {"description": "closed"},
                            "secondaryStatus": {"description": "closed"},
                            "tmid": {"description": "[0.1]"},
                            "trafficGroup": {
                                "description": "/Common/traffic-group-1"
                            },
                        }
                    }
                },
            },
        }


class test_get_sys_ha_mirror(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "entries": {
            "https://localhost/mgmt/tm/sys/ha-mirror/0": {
                "nestedStats": {
                    "entries": {
                        "aborts": {"value": 0},
                        "buffered": {"value": 0},
                        "errors": {"value": 0},
                        "l4Mirrorable": {"value": 0},
                        "l7Failed": {"value": 0},
                        "l7Mirrorable": {"value": 0},
                        "overflows": {"value": 0},
                        "primaryStatus": {"description": "closed"},
                        "secondaryStatus": {"description": "closed"},
                        "tmid": {"description": "[0.0]"},
                        "trafficGroup": {
                            "description": "/Common/traffic-group-1"
                        },
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-mirror/1": {
                "nestedStats": {
                    "entries": {
                        "aborts": {"value": 0},
                        "buffered": {"value": 0},
                        "errors": {"value": 0},
                        "l4Mirrorable": {"value": 0},
                        "l7Failed": {"value": 0},
                        "l7Mirrorable": {"value": 0},
                        "overflows": {"value": 0},
                        "primaryStatus": {"description": "closed"},
                        "secondaryStatus": {"description": "closed"},
                        "tmid": {"description": "[0.1]"},
                        "trafficGroup": {
                            "description": "/Common/traffic-group-1"
                        },
                    }
                }
            },
        },
        "kind": "tm:sys:ha-mirror:ha-mirrorstats",
        "selfLink": "https://localhost/mgmt/tm/sys/ha-mirror?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysHamirror(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysHamirror(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
