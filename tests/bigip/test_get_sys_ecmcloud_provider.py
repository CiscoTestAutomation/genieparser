# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_ecmcloud_provider
from genie.libs.parser.bigip.get_sys_ecmcloud_provider import (
    SysEcmCloudprovider,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/ecm/cloud-provider'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:ecm:cloud-provider:cloud-providercollectionstate",
            "selfLink": "https://localhost/mgmt/tm/sys/ecm/cloud-provider?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:sys:ecm:cloud-provider:cloud-providerstate",
                    "name": "aws-ec2",
                    "partition": "Common",
                    "fullPath": "/Common/aws-ec2",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/ecm/cloud-provider/~Common~aws-ec2?ver=14.1.2.1",
                    "description": "The aws-ec2 parameters",
                    "propertyTemplate": [
                        {"name": "account"},
                        {
                            "name": "availability-zone",
                            "validValues": ["a", "b", "c", "d"],
                        },
                        {
                            "name": "instance-type",
                            "validValues": [
                                "t2.micro",
                                "t2.small",
                                "t2.medium",
                                "m3.medium",
                                "m3.large",
                                "m3.xlarge",
                                "m3.2xlarge",
                                "c3.large",
                                "c3.xlarge",
                                "c3.2xlarge",
                                "c3.4xlarge",
                                "c3.8xlarge",
                                "r3.large",
                                "r3.xlarge",
                                "r3.2xlarge",
                                "r3.4xlarge",
                                "r3.8xlarge",
                            ],
                        },
                        {
                            "name": "region",
                            "validValues": [
                                "us-east-1",
                                "us-west-1",
                                "us-west-2",
                                "sa-east-1",
                                "eu-west-1",
                                "eu-central-1",
                                "ap-southeast-2",
                                "ap-southeast-1",
                                "ap-northeast-1",
                            ],
                        },
                    ],
                },
                {
                    "kind": "tm:sys:ecm:cloud-provider:cloud-providerstate",
                    "name": "dnet",
                    "partition": "Common",
                    "fullPath": "/Common/dnet",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/ecm/cloud-provider/~Common~dnet?ver=14.1.2.1",
                    "description": "The dnet parameters",
                },
                {
                    "kind": "tm:sys:ecm:cloud-provider:cloud-providerstate",
                    "name": "vsphere",
                    "partition": "Common",
                    "fullPath": "/Common/vsphere",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/ecm/cloud-provider/~Common~vsphere?ver=14.1.2.1",
                    "description": "The vsphere parameters",
                    "propertyTemplate": [
                        {"name": "cloud-host-ip"},
                        {"name": "dhcp-network-name"},
                        {"name": "end-point-url"},
                        {"name": "node-name"},
                    ],
                },
            ],
        }


class test_get_sys_ecmcloud_provider(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "description": "The aws-ec2 parameters",
                "fullPath": "/Common/aws-ec2",
                "generation": 1,
                "kind": "tm:sys:ecm:cloud-provider:cloud-providerstate",
                "name": "aws-ec2",
                "partition": "Common",
                "propertyTemplate": [
                    {"name": "account"},
                    {
                        "name": "availability-zone",
                        "validValues": ["a", "b", "c", "d"],
                    },
                    {
                        "name": "instance-type",
                        "validValues": [
                            "t2.micro",
                            "t2.small",
                            "t2.medium",
                            "m3.medium",
                            "m3.large",
                            "m3.xlarge",
                            "m3.2xlarge",
                            "c3.large",
                            "c3.xlarge",
                            "c3.2xlarge",
                            "c3.4xlarge",
                            "c3.8xlarge",
                            "r3.large",
                            "r3.xlarge",
                            "r3.2xlarge",
                            "r3.4xlarge",
                            "r3.8xlarge",
                        ],
                    },
                    {
                        "name": "region",
                        "validValues": [
                            "us-east-1",
                            "us-west-1",
                            "us-west-2",
                            "sa-east-1",
                            "eu-west-1",
                            "eu-central-1",
                            "ap-southeast-2",
                            "ap-southeast-1",
                            "ap-northeast-1",
                        ],
                    },
                ],
                "selfLink": "https://localhost/mgmt/tm/sys/ecm/cloud-provider/~Common~aws-ec2?ver=14.1.2.1",
            },
            {
                "description": "The dnet parameters",
                "fullPath": "/Common/dnet",
                "generation": 1,
                "kind": "tm:sys:ecm:cloud-provider:cloud-providerstate",
                "name": "dnet",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/sys/ecm/cloud-provider/~Common~dnet?ver=14.1.2.1",
            },
            {
                "description": "The vsphere parameters",
                "fullPath": "/Common/vsphere",
                "generation": 1,
                "kind": "tm:sys:ecm:cloud-provider:cloud-providerstate",
                "name": "vsphere",
                "partition": "Common",
                "propertyTemplate": [
                    {"name": "cloud-host-ip"},
                    {"name": "dhcp-network-name"},
                    {"name": "end-point-url"},
                    {"name": "node-name"},
                ],
                "selfLink": "https://localhost/mgmt/tm/sys/ecm/cloud-provider/~Common~vsphere?ver=14.1.2.1",
            },
        ],
        "kind": "tm:sys:ecm:cloud-provider:cloud-providercollectionstate",
        "selfLink": "https://localhost/mgmt/tm/sys/ecm/cloud-provider?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysEcmCloudprovider(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysEcmCloudprovider(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
