# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_performancednsexpress
from genie.libs.parser.bigip.get_sys_performancednsexpress import (
    SysPerformanceDnsexpress,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/performance/dnsexpress'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:performance:dnsexpress:dnsexpressstats",
            "selfLink": "https://localhost/mgmt/tm/sys/performance/dnsexpress?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/performance/dnsexpress/Notifies%20Received": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSX General Info": {
                                "description": "Notifies Received"
                            },
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/dnsexpress/Queries": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSX General Info": {"description": "Queries"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/dnsexpress/Responses": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSX General Info": {"description": "Responses"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/dnsexpress/XFR%20Messages": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSX General Info": {
                                "description": "XFR Messages"
                            },
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
            },
        }


class test_get_sys_performancednsexpress(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
            "kind": "tm:sys:performance:dnsexpress:dnsexpressstats",
            "selfLink": "https://localhost/mgmt/tm/sys/performance/dnsexpress?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/performance/dnsexpress/Notifies%20Received": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSX General Info": {
                                "description": "Notifies Received"
                            },
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/dnsexpress/Queries": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSX General Info": {"description": "Queries"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/dnsexpress/Responses": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSX General Info": {"description": "Responses"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/dnsexpress/XFR%20Messages": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSX General Info": {
                                "description": "XFR Messages"
                            },
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
            },
        }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysPerformanceDnsexpress(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysPerformanceDnsexpress(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
