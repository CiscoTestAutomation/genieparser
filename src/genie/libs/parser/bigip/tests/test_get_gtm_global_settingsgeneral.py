# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_gtm_global_settingsgeneral
from genie.libs.parser.bigip.get_gtm_global_settingsgeneral import (
    GtmGlobalsettingsGeneral,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/gtm/global-settings/general'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:gtm:global-settings:general:generalstate",
            "selfLink": "https://localhost/mgmt/tm/gtm/global-settings/general?ver=14.1.2.1",
            "autoDiscovery": "yes",
            "autoDiscoveryInterval": 30,
            "automaticConfigurationSaveTimeout": 15,
            "cacheLdnsServers": "yes",
            "domainNameCheck": "allow-underscore",
            "drainPersistentRequests": "yes",
            "forwardStatus": "disabled",
            "gtmSetsRecursion": "no",
            "heartbeatInterval": 10,
            "iqueryCipherList": "AESGCM:AES:!ADH:!AECDH:!PSK:!aECDH:!DSS:!ECDSA:!AES128:-SHA1:AES256-SHA",
            "iqueryMinimumTlsVersion": "TLSv1",
            "monitorDisabledObjects": "no",
            "nethsmTimeout": 20,
            "nsec3TypesBitmapStrict": "disabled",
            "sendWildcardRrs": "disabled",
            "staticPersistCidrIpv4": 32,
            "staticPersistCidrIpv6": 128,
            "synchronization": "no",
            "synchronizationGroupName": "default",
            "synchronizationTimeTolerance": 10,
            "synchronizationTimeout": 180,
            "synchronizeZoneFiles": "no",
            "synchronizeZoneFilesTimeout": 300,
            "virtualsDependOnServerState": "yes",
            "wideipZoneNameserver": "this.name.is.invalid.",
        }


class test_get_gtm_global_settingsgeneral(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "autoDiscovery": "yes",
        "autoDiscoveryInterval": 30,
        "automaticConfigurationSaveTimeout": 15,
        "cacheLdnsServers": "yes",
        "domainNameCheck": "allow-underscore",
        "drainPersistentRequests": "yes",
        "forwardStatus": "disabled",
        "gtmSetsRecursion": "no",
        "heartbeatInterval": 10,
        "iqueryCipherList": "AESGCM:AES:!ADH:!AECDH:!PSK:!aECDH:!DSS:!ECDSA:!AES128:-SHA1:AES256-SHA",
        "iqueryMinimumTlsVersion": "TLSv1",
        "kind": "tm:gtm:global-settings:general:generalstate",
        "monitorDisabledObjects": "no",
        "nethsmTimeout": 20,
        "nsec3TypesBitmapStrict": "disabled",
        "selfLink": "https://localhost/mgmt/tm/gtm/global-settings/general?ver=14.1.2.1",
        "sendWildcardRrs": "disabled",
        "staticPersistCidrIpv4": 32,
        "staticPersistCidrIpv6": 128,
        "synchronization": "no",
        "synchronizationGroupName": "default",
        "synchronizationTimeTolerance": 10,
        "synchronizationTimeout": 180,
        "synchronizeZoneFiles": "no",
        "synchronizeZoneFilesTimeout": 300,
        "virtualsDependOnServerState": "yes",
        "wideipZoneNameserver": "this.name.is.invalid.",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = GtmGlobalsettingsGeneral(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = GtmGlobalsettingsGeneral(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
