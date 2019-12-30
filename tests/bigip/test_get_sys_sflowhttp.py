# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_sflowhttp
from genie.libs.parser.bigip.get_sys_sflowhttp import SysSflowHttp

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/sflow/data-source/http'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:sflow:data-source:http:httpstats",
            "selfLink": "https://localhost/mgmt/tm/sys/sflow/data-source/http?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/sflow/data-source/http/~Common~vs_tcp_80_abc01.xyz.net_172.16.100.141": {
                    "nestedStats": {
                        "entries": {
                            "isActive": {"description": "no"},
                            "pollInterval": {"value": 10},
                            "profileName": {
                                "description": "/Common/http_1001"
                            },
                            "samplingRate": {"description": "1024"},
                            "vsName": {
                                "description": "/Common/vs_tcp_80_abc01.xyz.net_172.16.100.141"
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/sflow/data-source/http/~Common~vs_tcp_80_abc01.xyz.net_172.16.220.141": {
                    "nestedStats": {
                        "entries": {
                            "isActive": {"description": "no"},
                            "pollInterval": {"value": 10},
                            "profileName": {
                                "description": "/Common/http_2001"
                            },
                            "samplingRate": {"description": "1024"},
                            "vsName": {
                                "description": "/Common/vs_tcp_80_abc01.xyz.net_172.16.220.141"
                            },
                        }
                    }
                },
            },
        }


class test_get_sys_sflowhttp(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "entries": {
            "https://localhost/mgmt/tm/sys/sflow/data-source/http/~Common~vs_tcp_80_abc01.xyz.net_172.16.100.141": {
                "nestedStats": {
                    "entries": {
                        "isActive": {"description": "no"},
                        "pollInterval": {"value": 10},
                        "profileName": {"description": "/Common/http_1001"},
                        "samplingRate": {"description": "1024"},
                        "vsName": {
                            "description": "/Common/vs_tcp_80_abc01.xyz.net_172.16.100.141"
                        },
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/sflow/data-source/http/~Common~vs_tcp_80_abc01.xyz.net_172.16.220.141": {
                "nestedStats": {
                    "entries": {
                        "isActive": {"description": "no"},
                        "pollInterval": {"value": 10},
                        "profileName": {"description": "/Common/http_2001"},
                        "samplingRate": {"description": "1024"},
                        "vsName": {
                            "description": "/Common/vs_tcp_80_abc01.xyz.net_172.16.220.141"
                        },
                    }
                }
            },
        },
        "kind": "tm:sys:sflow:data-source:http:httpstats",
        "selfLink": "https://localhost/mgmt/tm/sys/sflow/data-source/http?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysSflowHttp(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysSflowHttp(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
