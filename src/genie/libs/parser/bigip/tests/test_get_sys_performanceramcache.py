# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_performanceramcache
from genie.libs.parser.bigip.get_sys_performanceramcache import (
    SysPerformanceRamcache,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/performance/ramcache'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:performance:ramcache:ramcachestats",
            "selfLink": "https://localhost/mgmt/tm/sys/performance/ramcache?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/performance/ramcache/Byte%20Rate": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "Max(since 2019_12_30T13:45:58Z)": {
                                "description": "0"
                            },
                            "RAM Cache Utilization": {
                                "description": "Byte Rate"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/ramcache/Eviction%20Rate": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "Max(since 2019_12_30T13:45:58Z)": {
                                "description": "0"
                            },
                            "RAM Cache Utilization": {
                                "description": "Eviction Rate"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/ramcache/Hit%20Rate": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "Max(since 2019_12_30T13:45:58Z)": {
                                "description": "0"
                            },
                            "RAM Cache Utilization": {
                                "description": "Hit Rate"
                            },
                        }
                    }
                },
            },
        }


class test_get_sys_performanceramcache(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
            "kind": "tm:sys:performance:ramcache:ramcachestats",
            "selfLink": "https://localhost/mgmt/tm/sys/performance/ramcache?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/performance/ramcache/Byte%20Rate": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "Max(since 2019_12_30T13:45:58Z)": {
                                "description": "0"
                            },
                            "RAM Cache Utilization": {
                                "description": "Byte Rate"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/ramcache/Eviction%20Rate": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "Max(since 2019_12_30T13:45:58Z)": {
                                "description": "0"
                            },
                            "RAM Cache Utilization": {
                                "description": "Eviction Rate"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/ramcache/Hit%20Rate": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "Max(since 2019_12_30T13:45:58Z)": {
                                "description": "0"
                            },
                            "RAM Cache Utilization": {
                                "description": "Hit Rate"
                            },
                        }
                    }
                },
            },
        }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysPerformanceRamcache(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysPerformanceRamcache(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
