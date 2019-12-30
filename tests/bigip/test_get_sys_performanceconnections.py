# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_performanceconnections
from genie.libs.parser.bigip.get_sys_performanceconnections import (
    SysPerformanceConnections,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/performance/connections'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:performance:connections:connectionsstats",
            "selfLink": "https://localhost/mgmt/tm/sys/performance/connections?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/performance/connections/Client%20Connections": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "1"},
                            "Current": {"description": "1"},
                            "Max(since 2019_12_30T13:45:54Z)": {
                                "description": "1"
                            },
                            "Total New Connections": {
                                "description": "Client Connections"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/connections/Connections": {
                    "nestedStats": {
                        "entries": {
                            "Active Connections": {
                                "description": "Connections"
                            },
                            "Average": {"description": "10"},
                            "Current": {"description": "9"},
                            "Max(since 2019_12_30T13:45:54Z)": {
                                "description": "14"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/connections/HTTP%20Requests": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "HTTP Requests": {"description": "HTTP Requests"},
                            "Max(since 2019_12_30T13:45:54Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/connections/Server%20Connections": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "1"},
                            "Current": {"description": "1"},
                            "Max(since 2019_12_30T13:45:54Z)": {
                                "description": "1"
                            },
                            "Total New Connections": {
                                "description": "Server Connections"
                            },
                        }
                    }
                },
            },
        }


class test_get_sys_performanceconnections(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
            "kind": "tm:sys:performance:connections:connectionsstats",
            "selfLink": "https://localhost/mgmt/tm/sys/performance/connections?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/performance/connections/Client%20Connections": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "1"},
                            "Current": {"description": "1"},
                            "Max(since 2019_12_30T13:45:54Z)": {
                                "description": "1"
                            },
                            "Total New Connections": {
                                "description": "Client Connections"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/connections/Connections": {
                    "nestedStats": {
                        "entries": {
                            "Active Connections": {
                                "description": "Connections"
                            },
                            "Average": {"description": "10"},
                            "Current": {"description": "9"},
                            "Max(since 2019_12_30T13:45:54Z)": {
                                "description": "14"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/connections/HTTP%20Requests": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "HTTP Requests": {"description": "HTTP Requests"},
                            "Max(since 2019_12_30T13:45:54Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/connections/Server%20Connections": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "1"},
                            "Current": {"description": "1"},
                            "Max(since 2019_12_30T13:45:54Z)": {
                                "description": "1"
                            },
                            "Total New Connections": {
                                "description": "Server Connections"
                            },
                        }
                    }
                },
            },
        }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysPerformanceConnections(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysPerformanceConnections(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
