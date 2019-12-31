# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_global_settings
from genie.libs.parser.bigip.get_sys_global_settings import SysGlobalsettings

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/global-settings'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:global-settings:global-settingsstate",
            "selfLink": "https://localhost/mgmt/tm/sys/global-settings?ver=14.1.2.1",
            "awsApiMaxConcurrency": 1,
            "consoleInactivityTimeout": 0,
            "customAddr": "none",
            "failsafeAction": "go-offline-restart-tm",
            "fileBlacklistPathPrefix": "{/shared/3dns/} {/shared/bin/} {/shared/core/} {/appdata/core/} {/shared/datasync/} {/shared/em/} {/shared/GeoIP/} {/shared/images/} {/shared/lib/} {/shared/lib64/} {/shared/log/} {/shared/lost+found/} {/shared/mgmt/} {/shared/nfb/} {/shared/ssh/} {/shared/statsd/} {/shared/tmstat/} {/shared/vadc/} {/config/aaa/} {/config/big3d/} {/config/bigip/} {/config/filestore/} {/config/gtm/} {/config/httpd/} {/config/ntp.conf} {/config/rndc.key} {/config/ssh/} {/config/ssl/}",
            "fileBlacklistReadOnlyPathPrefix": "{/etc/shadow}",
            "fileLocalPathPrefix": "{/shared/} {/tmp/}",
            "fileWhitelistPathPrefix": "{/var/local/scf} {/tmp/} {/shared/} {/config/} {/usr/share/aws/}",
            "guiAudit": "disabled",
            "guiSecurityBanner": "enabled",
            "guiSecurityBannerText": "Welcome to the BIG-IP Configuration Utility.\n\nLog in with your username and password using the fields on the left.",
            "guiSetup": "disabled",
            "hostAddrMode": "management",
            "hostname": "bigip01.lab.local",
            "lcdDisplay": "enabled",
            "ledLocator": "disabled",
            "mgmtDhcp": "disabled",
            "netReboot": "disabled",
            "passwordPrompt": "Password",
            "quietBoot": "enabled",
            "usernamePrompt": "Username",
        }


class test_get_sys_global_settings(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "awsApiMaxConcurrency": 1,
        "consoleInactivityTimeout": 0,
        "customAddr": "none",
        "failsafeAction": "go-offline-restart-tm",
        "fileBlacklistPathPrefix": "{/shared/3dns/} {/shared/bin/} {/shared/core/} "
        "{/appdata/core/} {/shared/datasync/} "
        "{/shared/em/} {/shared/GeoIP/} {/shared/images/} "
        "{/shared/lib/} {/shared/lib64/} {/shared/log/} "
        "{/shared/lost+found/} {/shared/mgmt/} "
        "{/shared/nfb/} {/shared/ssh/} {/shared/statsd/} "
        "{/shared/tmstat/} {/shared/vadc/} {/config/aaa/} "
        "{/config/big3d/} {/config/bigip/} "
        "{/config/filestore/} {/config/gtm/} "
        "{/config/httpd/} {/config/ntp.conf} "
        "{/config/rndc.key} {/config/ssh/} {/config/ssl/}",
        "fileBlacklistReadOnlyPathPrefix": "{/etc/shadow}",
        "fileLocalPathPrefix": "{/shared/} {/tmp/}",
        "fileWhitelistPathPrefix": "{/var/local/scf} {/tmp/} {/shared/} {/config/} "
        "{/usr/share/aws/}",
        "guiAudit": "disabled",
        "guiSecurityBanner": "enabled",
        "guiSecurityBannerText": "Welcome to the BIG-IP Configuration Utility.\n"
        "\n"
        "Log in with your username and password using the "
        "fields on the left.",
        "guiSetup": "disabled",
        "hostAddrMode": "management",
        "hostname": "bigip01.lab.local",
        "kind": "tm:sys:global-settings:global-settingsstate",
        "lcdDisplay": "enabled",
        "ledLocator": "disabled",
        "mgmtDhcp": "disabled",
        "netReboot": "disabled",
        "passwordPrompt": "Password",
        "quietBoot": "enabled",
        "selfLink": "https://localhost/mgmt/tm/sys/global-settings?ver=14.1.2.1",
        "usernamePrompt": "Username",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysGlobalsettings(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysGlobalsettings(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
