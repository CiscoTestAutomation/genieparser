# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_performancesystem
from genie.libs.parser.bigip.get_sys_performancesystem import (
    SysPerformanceSystem,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/performance/system'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:performance:system:systemstats",
            "selfLink": "https://localhost/mgmt/tm/sys/performance/system?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/performance/system/Other%20Memory%20Used": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "82"},
                            "Current": {"description": "84"},
                            "Max(since 2019_12_30T13:45:38Z)": {
                                "description": "88"
                            },
                            "Memory Used": {
                                "description": "Other Memory Used"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/system/Swap%20Used": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "7"},
                            "Current": {"description": "12"},
                            "Max(since 2019_12_30T13:45:38Z)": {
                                "description": "12"
                            },
                            "Memory Used": {"description": "Swap Used"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/system/TMM%20Memory%20Used": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "11"},
                            "Current": {"description": "11"},
                            "Max(since 2019_12_30T13:45:38Z)": {
                                "description": "11"
                            },
                            "Memory Used": {"description": "TMM Memory Used"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/system/Utilization": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "14"},
                            "Current": {"description": "9"},
                            "Max(since 2019_12_30T13:45:38Z)": {
                                "description": "100"
                            },
                            "System CPU Usage": {"description": "Utilization"},
                        }
                    }
                },
            },
        }


class test_get_sys_performancesystem(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
            "kind": "tm:sys:performance:system:systemstats",
            "selfLink": "https://localhost/mgmt/tm/sys/performance/system?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/performance/system/Other%20Memory%20Used": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "82"},
                            "Current": {"description": "84"},
                            "Max(since 2019_12_30T13:45:38Z)": {
                                "description": "88"
                            },
                            "Memory Used": {
                                "description": "Other Memory Used"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/system/Swap%20Used": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "7"},
                            "Current": {"description": "12"},
                            "Max(since 2019_12_30T13:45:38Z)": {
                                "description": "12"
                            },
                            "Memory Used": {"description": "Swap Used"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/system/TMM%20Memory%20Used": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "11"},
                            "Current": {"description": "11"},
                            "Max(since 2019_12_30T13:45:38Z)": {
                                "description": "11"
                            },
                            "Memory Used": {"description": "TMM Memory Used"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/system/Utilization": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "14"},
                            "Current": {"description": "9"},
                            "Max(since 2019_12_30T13:45:38Z)": {
                                "description": "100"
                            },
                            "System CPU Usage": {"description": "Utilization"},
                        }
                    }
                },
            },
        }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysPerformanceSystem(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysPerformanceSystem(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
