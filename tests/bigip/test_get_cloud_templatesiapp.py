# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_cloud_templatesiapp
from genie.libs.parser.bigip.get_cloud_templatesiapp import CloudTemplatesIapp

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/cloud/templates/iapp'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "items": [
                "f5.bea_weblogic",
                "f5.cifs",
                "f5.citrix_presentation_server",
                "f5.citrix_xen_app",
                "f5.diameter",
                "f5.dns",
                "f5.ftp",
                "f5.http",
                "f5.ip_forwarding",
                "f5.ldap",
                "f5.microsoft_exchange_2010",
                "f5.microsoft_exchange_owa_2007",
                "f5.microsoft_iis",
                "f5.microsoft_lync_server_2010",
                "f5.microsoft_ocs_2007_r2",
                "f5.microsoft_sharepoint_2007",
                "f5.microsoft_sharepoint_2010",
                "f5.npath",
                "f5.oracle_as_10g",
                "f5.oracle_ebs",
                "f5.peoplesoft_9",
                "f5.radius",
                "f5.replication",
                "f5.sap_enterprise_portal",
                "f5.sap_erp",
                "f5.vmware_view",
                "f5.vmware_vmotion",
            ],
            "generation": 0,
            "lastUpdateMicros": 0,
        }


class test_get_cloud_templatesiapp(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "generation": 0,
        "items": [
            "f5.bea_weblogic",
            "f5.cifs",
            "f5.citrix_presentation_server",
            "f5.citrix_xen_app",
            "f5.diameter",
            "f5.dns",
            "f5.ftp",
            "f5.http",
            "f5.ip_forwarding",
            "f5.ldap",
            "f5.microsoft_exchange_2010",
            "f5.microsoft_exchange_owa_2007",
            "f5.microsoft_iis",
            "f5.microsoft_lync_server_2010",
            "f5.microsoft_ocs_2007_r2",
            "f5.microsoft_sharepoint_2007",
            "f5.microsoft_sharepoint_2010",
            "f5.npath",
            "f5.oracle_as_10g",
            "f5.oracle_ebs",
            "f5.peoplesoft_9",
            "f5.radius",
            "f5.replication",
            "f5.sap_enterprise_portal",
            "f5.sap_erp",
            "f5.vmware_view",
            "f5.vmware_vmotion",
        ],
        "lastUpdateMicros": 0,
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = CloudTemplatesIapp(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = CloudTemplatesIapp(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
