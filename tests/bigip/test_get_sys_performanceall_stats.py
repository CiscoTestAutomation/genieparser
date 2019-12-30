# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_performanceall_stats
from genie.libs.parser.bigip.get_sys_performanceall_stats import (
    SysPerformanceAllstats,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/performance/all-stats'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:performance:all-stats:all-statsstats",
            "selfLink": "https://localhost/mgmt/tm/sys/performance/all-stats?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/performance/all-stats/Byte%20Rate": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "0"
                            },
                            "RAM Cache Utilization": {
                                "description": "Byte Rate"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Client%20Connections": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "1"},
                            "Current": {"description": "1"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "1"
                            },
                            "Total New Connections": {
                                "description": "Client Connections"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Connections": {
                    "nestedStats": {
                        "entries": {
                            "Active Connections": {
                                "description": "Connections"
                            },
                            "Average": {"description": "10"},
                            "Current": {"description": "9"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "14"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Eviction%20Rate": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "0"
                            },
                            "RAM Cache Utilization": {
                                "description": "Eviction Rate"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/HTTP%20Requests": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "HTTP Requests": {"description": "HTTP Requests"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Hit%20Rate": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "0"
                            },
                            "RAM Cache Utilization": {
                                "description": "Hit Rate"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/In": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "2"},
                            "Current": {"description": "2"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "20"
                            },
                            "Throughput(packets)": {"description": "In"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Other%20Memory%20Used": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "82"},
                            "Current": {"description": "84"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "88"
                            },
                            "Memory Used": {
                                "description": "Other Memory Used"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Out": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "1"},
                            "Current": {"description": "1"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "10"
                            },
                            "Throughput(packets)": {"description": "Out"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Persisted": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Performance": {"description": "Persisted"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Requests": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Performance": {"description": "Requests"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Resolutions": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Performance": {"description": "Resolutions"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Return%20to%20DNS": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Performance": {
                                "description": "Return to DNS"
                            },
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/SSL%20TPS": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "0"
                            },
                            "SSL Transactions": {"description": "SSL TPS"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Server%20Connections": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "1"},
                            "Current": {"description": "1"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "1"
                            },
                            "Total New Connections": {
                                "description": "Server Connections"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Service": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "1"},
                            "Current": {"description": "1"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "2"
                            },
                            "Throughput(packets)": {"description": "Service"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Swap%20Used": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "7"},
                            "Current": {"description": "12"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "12"
                            },
                            "Memory Used": {"description": "Swap Used"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/TMM%20Memory%20Used": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "11"},
                            "Current": {"description": "11"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "11"
                            },
                            "Memory Used": {"description": "TMM Memory Used"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Type%20A": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Request Breakdown ": {
                                "description": "Type A"
                            },
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Type%20AAAA": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Request Breakdown ": {
                                "description": "Type AAAA"
                            },
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Type%20CNAME": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Request Breakdown ": {
                                "description": "Type CNAME"
                            },
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Type%20MX": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Request Breakdown ": {
                                "description": "Type MX"
                            },
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Type%20NAPTR": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Request Breakdown ": {
                                "description": "Type NAPTR"
                            },
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Type%20SRV": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Request Breakdown ": {
                                "description": "Type SRV"
                            },
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Utilization": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "14"},
                            "Current": {"description": "36"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "100"
                            },
                            "System CPU Usage": {"description": "Utilization"},
                        }
                    }
                },
            },
        }


class test_get_sys_performanceall_stats(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
            "kind": "tm:sys:performance:all-stats:all-statsstats",
            "selfLink": "https://localhost/mgmt/tm/sys/performance/all-stats?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/performance/all-stats/Byte%20Rate": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "0"
                            },
                            "RAM Cache Utilization": {
                                "description": "Byte Rate"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Client%20Connections": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "1"},
                            "Current": {"description": "1"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "1"
                            },
                            "Total New Connections": {
                                "description": "Client Connections"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Connections": {
                    "nestedStats": {
                        "entries": {
                            "Active Connections": {
                                "description": "Connections"
                            },
                            "Average": {"description": "10"},
                            "Current": {"description": "9"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "14"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Eviction%20Rate": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "0"
                            },
                            "RAM Cache Utilization": {
                                "description": "Eviction Rate"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/HTTP%20Requests": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "HTTP Requests": {"description": "HTTP Requests"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Hit%20Rate": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "0"
                            },
                            "RAM Cache Utilization": {
                                "description": "Hit Rate"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/In": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "2"},
                            "Current": {"description": "2"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "20"
                            },
                            "Throughput(packets)": {"description": "In"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Other%20Memory%20Used": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "82"},
                            "Current": {"description": "84"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "88"
                            },
                            "Memory Used": {
                                "description": "Other Memory Used"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Out": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "1"},
                            "Current": {"description": "1"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "10"
                            },
                            "Throughput(packets)": {"description": "Out"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Persisted": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Performance": {"description": "Persisted"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Requests": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Performance": {"description": "Requests"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Resolutions": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Performance": {"description": "Resolutions"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Return%20to%20DNS": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Performance": {
                                "description": "Return to DNS"
                            },
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/SSL%20TPS": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "0"
                            },
                            "SSL Transactions": {"description": "SSL TPS"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Server%20Connections": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "1"},
                            "Current": {"description": "1"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "1"
                            },
                            "Total New Connections": {
                                "description": "Server Connections"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Service": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "1"},
                            "Current": {"description": "1"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "2"
                            },
                            "Throughput(packets)": {"description": "Service"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Swap%20Used": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "7"},
                            "Current": {"description": "12"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "12"
                            },
                            "Memory Used": {"description": "Swap Used"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/TMM%20Memory%20Used": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "11"},
                            "Current": {"description": "11"},
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "11"
                            },
                            "Memory Used": {"description": "TMM Memory Used"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Type%20A": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Request Breakdown ": {
                                "description": "Type A"
                            },
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Type%20AAAA": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Request Breakdown ": {
                                "description": "Type AAAA"
                            },
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Type%20CNAME": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Request Breakdown ": {
                                "description": "Type CNAME"
                            },
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Type%20MX": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Request Breakdown ": {
                                "description": "Type MX"
                            },
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Type%20NAPTR": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Request Breakdown ": {
                                "description": "Type NAPTR"
                            },
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Type%20SRV": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Request Breakdown ": {
                                "description": "Type SRV"
                            },
                            "Max(since 2019_12_30T13:46:00Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/all-stats/Utilization": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "14"},
                            "Current": {"description": "36"},
                            "Max(since 2019_12_30T13:46:00Z)": {
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
    #     obj = SysPerformanceAllstats(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysPerformanceAllstats(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
