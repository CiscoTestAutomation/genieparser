# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_performancethroughput
from genie.libs.parser.bigip.get_sys_performancethroughput import (
    SysPerformanceThroughput,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/performance/throughput'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:performance:throughput:throughputstats",
            "selfLink": "https://localhost/mgmt/tm/sys/performance/throughput?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/performance/throughput/In": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "2"},
                            "Current": {"description": "2"},
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "20"
                            },
                            "Throughput(packets)": {"description": "In"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/throughput/Out": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "1"},
                            "Current": {"description": "1"},
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "10"
                            },
                            "Throughput(packets)": {"description": "Out"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/throughput/SSL%20TPS": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "0"
                            },
                            "SSL Transactions": {"description": "SSL TPS"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/throughput/Service": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "1"},
                            "Current": {"description": "1"},
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "2"
                            },
                            "Throughput(packets)": {"description": "Service"},
                        }
                    }
                },
            },
        }


class test_get_sys_performancethroughput(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
            "kind": "tm:sys:performance:throughput:throughputstats",
            "selfLink": "https://localhost/mgmt/tm/sys/performance/throughput?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/performance/throughput/In": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "2"},
                            "Current": {"description": "2"},
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "20"
                            },
                            "Throughput(packets)": {"description": "In"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/throughput/Out": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "1"},
                            "Current": {"description": "1"},
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "10"
                            },
                            "Throughput(packets)": {"description": "Out"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/throughput/SSL%20TPS": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "0"
                            },
                            "SSL Transactions": {"description": "SSL TPS"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/throughput/Service": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "1"},
                            "Current": {"description": "1"},
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "2"
                            },
                            "Throughput(packets)": {"description": "Service"},
                        }
                    }
                },
            },
        }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysPerformanceThroughput(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysPerformanceThroughput(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
