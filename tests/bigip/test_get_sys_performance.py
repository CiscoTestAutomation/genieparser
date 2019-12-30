# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_performance
from genie.libs.parser.bigip.get_sys_performance import SysPerformance

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/performance'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:performance:performancecollectionstats",
            "selfLink": "https://localhost/mgmt/tm/sys/performance?ver=14.1.2.1",
            "items": [
                {
                    "reference": {
                        "link": "https://localhost/mgmt/tm/sys/performance/all-stats?ver=14.1.2.1"
                    }
                },
                {
                    "reference": {
                        "link": "https://localhost/mgmt/tm/sys/performance/connections?ver=14.1.2.1"
                    }
                },
                {
                    "reference": {
                        "link": "https://localhost/mgmt/tm/sys/performance/dnsexpress?ver=14.1.2.1"
                    }
                },
                {
                    "reference": {
                        "link": "https://localhost/mgmt/tm/sys/performance/dnssec?ver=14.1.2.1"
                    }
                },
                {
                    "reference": {
                        "link": "https://localhost/mgmt/tm/sys/performance/gtm?ver=14.1.2.1"
                    }
                },
                {
                    "reference": {
                        "link": "https://localhost/mgmt/tm/sys/performance/ramcache?ver=14.1.2.1"
                    }
                },
                {
                    "reference": {
                        "link": "https://localhost/mgmt/tm/sys/performance/system?ver=14.1.2.1"
                    }
                },
                {
                    "reference": {
                        "link": "https://localhost/mgmt/tm/sys/performance/throughput?ver=14.1.2.1"
                    }
                },
            ],
        }


class test_get_sys_performance(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "reference": {
                    "link": "https://localhost/mgmt/tm/sys/performance/all-stats?ver=14.1.2.1"
                }
            },
            {
                "reference": {
                    "link": "https://localhost/mgmt/tm/sys/performance/connections?ver=14.1.2.1"
                }
            },
            {
                "reference": {
                    "link": "https://localhost/mgmt/tm/sys/performance/dnsexpress?ver=14.1.2.1"
                }
            },
            {
                "reference": {
                    "link": "https://localhost/mgmt/tm/sys/performance/dnssec?ver=14.1.2.1"
                }
            },
            {
                "reference": {
                    "link": "https://localhost/mgmt/tm/sys/performance/gtm?ver=14.1.2.1"
                }
            },
            {
                "reference": {
                    "link": "https://localhost/mgmt/tm/sys/performance/ramcache?ver=14.1.2.1"
                }
            },
            {
                "reference": {
                    "link": "https://localhost/mgmt/tm/sys/performance/system?ver=14.1.2.1"
                }
            },
            {
                "reference": {
                    "link": "https://localhost/mgmt/tm/sys/performance/throughput?ver=14.1.2.1"
                }
            },
        ],
        "kind": "tm:sys:performance:performancecollectionstats",
        "selfLink": "https://localhost/mgmt/tm/sys/performance?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysPerformance(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysPerformance(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
