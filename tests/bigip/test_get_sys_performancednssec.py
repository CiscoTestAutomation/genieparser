# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_performancednssec
from genie.libs.parser.bigip.get_sys_performancednssec import (
    SysPerformanceDnssec,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/performance/dnssec'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:performance:dnssec:dnssecstats",
            "selfLink": "https://localhost/mgmt/tm/sys/performance/dnssec?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/performance/dnssec/AXFR%20Queries": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSSEC Queries": {"description": "AXFR Queries"},
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/dnssec/CDNSKEY%20Queries": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSSEC Queries": {
                                "description": "CDNSKEY Queries"
                            },
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/dnssec/CDS%20Queries": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSSEC Queries": {"description": "CDS Queries"},
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/dnssec/DNSKEY%20Queries": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSSEC Queries": {
                                "description": "DNSKEY Queries"
                            },
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/dnssec/DS%20Queries": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSSEC Queries": {"description": "DS Queries"},
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/dnssec/IXFR%20Queries": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSSEC Queries": {"description": "IXFR Queries"},
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/dnssec/NSEC3%20Param%20Queries": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSSEC Queries": {
                                "description": "NSEC3 Param Queries"
                            },
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/dnssec/Responses": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSSEC Responses and Sig Info": {
                                "description": "Responses"
                            },
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/dnssec/Sig%20Crypto%20Failed": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSSEC Responses and Sig Info": {
                                "description": "Sig Crypto Failed"
                            },
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/dnssec/Sig%20RRset%20Failed": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSSEC Responses and Sig Info": {
                                "description": "Sig RRset Failed"
                            },
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/dnssec/Sig%20Success": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSSEC Responses and Sig Info": {
                                "description": "Sig Success"
                            },
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/dnssec/Total": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSSEC Queries": {"description": "Total"},
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
            },
        }


class test_get_sys_performancednssec(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
            "kind": "tm:sys:performance:dnssec:dnssecstats",
            "selfLink": "https://localhost/mgmt/tm/sys/performance/dnssec?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/performance/dnssec/AXFR%20Queries": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSSEC Queries": {"description": "AXFR Queries"},
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/dnssec/CDNSKEY%20Queries": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSSEC Queries": {
                                "description": "CDNSKEY Queries"
                            },
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/dnssec/CDS%20Queries": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSSEC Queries": {"description": "CDS Queries"},
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/dnssec/DNSKEY%20Queries": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSSEC Queries": {
                                "description": "DNSKEY Queries"
                            },
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/dnssec/DS%20Queries": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSSEC Queries": {"description": "DS Queries"},
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/dnssec/IXFR%20Queries": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSSEC Queries": {"description": "IXFR Queries"},
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/dnssec/NSEC3%20Param%20Queries": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSSEC Queries": {
                                "description": "NSEC3 Param Queries"
                            },
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/dnssec/Responses": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSSEC Responses and Sig Info": {
                                "description": "Responses"
                            },
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/dnssec/Sig%20Crypto%20Failed": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSSEC Responses and Sig Info": {
                                "description": "Sig Crypto Failed"
                            },
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/dnssec/Sig%20RRset%20Failed": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSSEC Responses and Sig Info": {
                                "description": "Sig RRset Failed"
                            },
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/dnssec/Sig%20Success": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSSEC Responses and Sig Info": {
                                "description": "Sig Success"
                            },
                            "Max(since 2019_12_30T13:45:43Z)": {
                                "description": "-nan"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/performance/dnssec/Total": {
                    "nestedStats": {
                        "entries": {
                            "Average": {"description": "-nan"},
                            "Current": {"description": "-nan"},
                            "DNSSEC Queries": {"description": "Total"},
                            "Max(since 2019_12_30T13:45:43Z)": {
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
    #     obj = SysPerformanceDnssec(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysPerformanceDnssec(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
