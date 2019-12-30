# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_log_configpublisher
from genie.libs.parser.bigip.get_sys_log_configpublisher import (
    SysLogconfigPublisher,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/log-config/publisher'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:log-config:publisher:publishercollectionstate",
            "selfLink": "https://localhost/mgmt/tm/sys/log-config/publisher?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:sys:log-config:publisher:publisherstate",
                    "name": "default-ipsec-log-publisher",
                    "partition": "Common",
                    "fullPath": "/Common/default-ipsec-log-publisher",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/log-config/publisher/~Common~default-ipsec-log-publisher?ver=14.1.2.1",
                    "destinations": [
                        {
                            "name": "local-syslog",
                            "partition": "Common",
                            "nameReference": {
                                "link": "https://localhost/mgmt/tm/sys/log-config/destination/local-syslog/~Common~local-syslog?ver=14.1.2.1"
                            },
                        }
                    ],
                },
                {
                    "kind": "tm:sys:log-config:publisher:publisherstate",
                    "name": "default-mgmt-acl-log-publisher",
                    "partition": "Common",
                    "fullPath": "/Common/default-mgmt-acl-log-publisher",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/log-config/publisher/~Common~default-mgmt-acl-log-publisher?ver=14.1.2.1",
                },
                {
                    "kind": "tm:sys:log-config:publisher:publisherstate",
                    "name": "local-db-publisher",
                    "partition": "Common",
                    "fullPath": "/Common/local-db-publisher",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/log-config/publisher/~Common~local-db-publisher?ver=14.1.2.1",
                    "destinations": [
                        {
                            "name": "local-db",
                            "partition": "Common",
                            "nameReference": {
                                "link": "https://localhost/mgmt/tm/sys/log-config/destination/local-database/~Common~local-db?ver=14.1.2.1"
                            },
                        }
                    ],
                },
                {
                    "kind": "tm:sys:log-config:publisher:publisherstate",
                    "name": "sys-db-access-publisher",
                    "partition": "Common",
                    "fullPath": "/Common/sys-db-access-publisher",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/log-config/publisher/~Common~sys-db-access-publisher?ver=14.1.2.1",
                    "destinations": [
                        {
                            "name": "local-db",
                            "partition": "Common",
                            "nameReference": {
                                "link": "https://localhost/mgmt/tm/sys/log-config/destination/local-database/~Common~local-db?ver=14.1.2.1"
                            },
                        },
                        {
                            "name": "local-syslog",
                            "partition": "Common",
                            "nameReference": {
                                "link": "https://localhost/mgmt/tm/sys/log-config/destination/local-syslog/~Common~local-syslog?ver=14.1.2.1"
                            },
                        },
                    ],
                },
                {
                    "kind": "tm:sys:log-config:publisher:publisherstate",
                    "name": "sys-sslo-publisher",
                    "partition": "Common",
                    "fullPath": "/Common/sys-sslo-publisher",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/log-config/publisher/~Common~sys-sslo-publisher?ver=14.1.2.1",
                    "destinations": [
                        {
                            "name": "local-syslog",
                            "partition": "Common",
                            "nameReference": {
                                "link": "https://localhost/mgmt/tm/sys/log-config/destination/local-syslog/~Common~local-syslog?ver=14.1.2.1"
                            },
                        }
                    ],
                },
                {
                    "kind": "tm:sys:log-config:publisher:publisherstate",
                    "name": "sys-sso-access-publisher",
                    "partition": "Common",
                    "fullPath": "/Common/sys-sso-access-publisher",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/log-config/publisher/~Common~sys-sso-access-publisher?ver=14.1.2.1",
                    "destinations": [
                        {
                            "name": "local-syslog",
                            "partition": "Common",
                            "nameReference": {
                                "link": "https://localhost/mgmt/tm/sys/log-config/destination/local-syslog/~Common~local-syslog?ver=14.1.2.1"
                            },
                        }
                    ],
                },
            ],
        }


class test_get_sys_log_configpublisher(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "destinations": [
                    {
                        "name": "local-syslog",
                        "nameReference": {
                            "link": "https://localhost/mgmt/tm/sys/log-config/destination/local-syslog/~Common~local-syslog?ver=14.1.2.1"
                        },
                        "partition": "Common",
                    }
                ],
                "fullPath": "/Common/default-ipsec-log-publisher",
                "generation": 1,
                "kind": "tm:sys:log-config:publisher:publisherstate",
                "name": "default-ipsec-log-publisher",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/sys/log-config/publisher/~Common~default-ipsec-log-publisher?ver=14.1.2.1",
            },
            {
                "fullPath": "/Common/default-mgmt-acl-log-publisher",
                "generation": 1,
                "kind": "tm:sys:log-config:publisher:publisherstate",
                "name": "default-mgmt-acl-log-publisher",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/sys/log-config/publisher/~Common~default-mgmt-acl-log-publisher?ver=14.1.2.1",
            },
            {
                "destinations": [
                    {
                        "name": "local-db",
                        "nameReference": {
                            "link": "https://localhost/mgmt/tm/sys/log-config/destination/local-database/~Common~local-db?ver=14.1.2.1"
                        },
                        "partition": "Common",
                    }
                ],
                "fullPath": "/Common/local-db-publisher",
                "generation": 1,
                "kind": "tm:sys:log-config:publisher:publisherstate",
                "name": "local-db-publisher",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/sys/log-config/publisher/~Common~local-db-publisher?ver=14.1.2.1",
            },
            {
                "destinations": [
                    {
                        "name": "local-db",
                        "nameReference": {
                            "link": "https://localhost/mgmt/tm/sys/log-config/destination/local-database/~Common~local-db?ver=14.1.2.1"
                        },
                        "partition": "Common",
                    },
                    {
                        "name": "local-syslog",
                        "nameReference": {
                            "link": "https://localhost/mgmt/tm/sys/log-config/destination/local-syslog/~Common~local-syslog?ver=14.1.2.1"
                        },
                        "partition": "Common",
                    },
                ],
                "fullPath": "/Common/sys-db-access-publisher",
                "generation": 1,
                "kind": "tm:sys:log-config:publisher:publisherstate",
                "name": "sys-db-access-publisher",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/sys/log-config/publisher/~Common~sys-db-access-publisher?ver=14.1.2.1",
            },
            {
                "destinations": [
                    {
                        "name": "local-syslog",
                        "nameReference": {
                            "link": "https://localhost/mgmt/tm/sys/log-config/destination/local-syslog/~Common~local-syslog?ver=14.1.2.1"
                        },
                        "partition": "Common",
                    }
                ],
                "fullPath": "/Common/sys-sslo-publisher",
                "generation": 1,
                "kind": "tm:sys:log-config:publisher:publisherstate",
                "name": "sys-sslo-publisher",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/sys/log-config/publisher/~Common~sys-sslo-publisher?ver=14.1.2.1",
            },
            {
                "destinations": [
                    {
                        "name": "local-syslog",
                        "nameReference": {
                            "link": "https://localhost/mgmt/tm/sys/log-config/destination/local-syslog/~Common~local-syslog?ver=14.1.2.1"
                        },
                        "partition": "Common",
                    }
                ],
                "fullPath": "/Common/sys-sso-access-publisher",
                "generation": 1,
                "kind": "tm:sys:log-config:publisher:publisherstate",
                "name": "sys-sso-access-publisher",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/sys/log-config/publisher/~Common~sys-sso-access-publisher?ver=14.1.2.1",
            },
        ],
        "kind": "tm:sys:log-config:publisher:publishercollectionstate",
        "selfLink": "https://localhost/mgmt/tm/sys/log-config/publisher?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysLogconfigPublisher(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysLogconfigPublisher(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
