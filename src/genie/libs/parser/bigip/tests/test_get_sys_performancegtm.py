# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_performancegtm
from genie.libs.parser.bigip.get_sys_performancegtm import SysPerformanceGtm

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/performance/gtm'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:performance:gtm:gtmstats",
            "selfLink": "https://localhost/mgmt/tm/sys/performance/gtm?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/performance/gtm/Persisted": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Performance": {"description": "Persisted"},
                            "Max(since 2019_12_30T13:45:44Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/gtm/Requests": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Performance": {"description": "Requests"},
                            "Max(since 2019_12_30T13:45:44Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/gtm/Resolutions": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Performance": {"description": "Resolutions"},
                            "Max(since 2019_12_30T13:45:44Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/gtm/Return%20to%20DNS": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Performance": {
                                "description": "Return to DNS"
                            },
                            "Max(since 2019_12_30T13:45:44Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/gtm/Type%20A": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Request Breakdown ": {
                                "description": "Type A"
                            },
                            "Max(since 2019_12_30T13:45:44Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/gtm/Type%20AAAA": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Request Breakdown ": {
                                "description": "Type AAAA"
                            },
                            "Max(since 2019_12_30T13:45:44Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/gtm/Type%20CNAME": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Request Breakdown ": {
                                "description": "Type CNAME"
                            },
                            "Max(since 2019_12_30T13:45:44Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/gtm/Type%20MX": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Request Breakdown ": {
                                "description": "Type MX"
                            },
                            "Max(since 2019_12_30T13:45:44Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/gtm/Type%20NAPTR": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Request Breakdown ": {
                                "description": "Type NAPTR"
                            },
                            "Max(since 2019_12_30T13:45:44Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/gtm/Type%20SRV": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Request Breakdown ": {
                                "description": "Type SRV"
                            },
                            "Max(since 2019_12_30T13:45:44Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
            },
        }


class test_get_sys_performancegtm(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
            "kind": "tm:sys:performance:gtm:gtmstats",
            "selfLink": "https://localhost/mgmt/tm/sys/performance/gtm?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/performance/gtm/Persisted": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Performance": {"description": "Persisted"},
                            "Max(since 2019_12_30T13:45:44Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/gtm/Requests": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Performance": {"description": "Requests"},
                            "Max(since 2019_12_30T13:45:44Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/gtm/Resolutions": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Performance": {"description": "Resolutions"},
                            "Max(since 2019_12_30T13:45:44Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/gtm/Return%20to%20DNS": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Performance": {
                                "description": "Return to DNS"
                            },
                            "Max(since 2019_12_30T13:45:44Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/gtm/Type%20A": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Request Breakdown ": {
                                "description": "Type A"
                            },
                            "Max(since 2019_12_30T13:45:44Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/gtm/Type%20AAAA": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Request Breakdown ": {
                                "description": "Type AAAA"
                            },
                            "Max(since 2019_12_30T13:45:44Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/gtm/Type%20CNAME": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Request Breakdown ": {
                                "description": "Type CNAME"
                            },
                            "Max(since 2019_12_30T13:45:44Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/gtm/Type%20MX": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Request Breakdown ": {
                                "description": "Type MX"
                            },
                            "Max(since 2019_12_30T13:45:44Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/gtm/Type%20NAPTR": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Request Breakdown ": {
                                "description": "Type NAPTR"
                            },
                            "Max(since 2019_12_30T13:45:44Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/gtm/Type%20SRV": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "0"},
                            "Current": {"description": "0"},
                            "GSLB Request Breakdown ": {
                                "description": "Type SRV"
                            },
                            "Max(since 2019_12_30T13:45:44Z)": {
                                "description": "0"
                            },
                        }
                    }
                },
            },
        }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysPerformanceGtm(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysPerformanceGtm(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
