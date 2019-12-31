# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_httpd
from genie.libs.parser.bigip.get_sys_httpd import SysHttpd

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/httpd'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:httpd:httpdstate",
            "selfLink": "https://localhost/mgmt/tm/sys/httpd?ver=14.1.2.1",
            "allow": ["All"],
            "authName": "BIG-IP",
            "authPamDashboardTimeout": "off",
            "authPamIdleTimeout": 1200,
            "authPamValidateIp": "on",
            "fastcgiTimeout": 300,
            "fipsCipherVersion": 0,
            "hostnameLookup": "off",
            "logLevel": "warn",
            "maxClients": 10,
            "redirectHttpToHttps": "disabled",
            "requestBodyMaxTimeout": 0,
            "requestBodyMinRate": 500,
            "requestBodyTimeout": 60,
            "requestHeaderMaxTimeout": 40,
            "requestHeaderMinRate": 500,
            "requestHeaderTimeout": 20,
            "sslCertfile": "/etc/httpd/conf/ssl.crt/server.crt",
            "sslCertkeyfile": "/etc/httpd/conf/ssl.key/server.key",
            "sslCiphersuite": "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-SHA:ECDHE-RSA-AES256-SHA:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-SHA:ECDHE-ECDSA-AES256-SHA:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA384:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA:AES256-SHA:AES128-SHA256:AES256-SHA256",
            "sslOcspDefaultResponder": "http://127.0.0.1",
            "sslOcspEnable": "off",
            "sslOcspOverrideResponder": "off",
            "sslOcspResponderTimeout": 300,
            "sslOcspResponseMaxAge": -1,
            "sslOcspResponseTimeSkew": 300,
            "sslPort": 443,
            "sslProtocol": "all -SSLv2 -SSLv3 -TLSv1",
            "sslVerifyClient": "no",
            "sslVerifyDepth": 10,
        }


class test_get_sys_httpd(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "allow": ["All"],
        "authName": "BIG-IP",
        "authPamDashboardTimeout": "off",
        "authPamIdleTimeout": 1200,
        "authPamValidateIp": "on",
        "fastcgiTimeout": 300,
        "fipsCipherVersion": 0,
        "hostnameLookup": "off",
        "kind": "tm:sys:httpd:httpdstate",
        "logLevel": "warn",
        "maxClients": 10,
        "redirectHttpToHttps": "disabled",
        "requestBodyMaxTimeout": 0,
        "requestBodyMinRate": 500,
        "requestBodyTimeout": 60,
        "requestHeaderMaxTimeout": 40,
        "requestHeaderMinRate": 500,
        "requestHeaderTimeout": 20,
        "selfLink": "https://localhost/mgmt/tm/sys/httpd?ver=14.1.2.1",
        "sslCertfile": "/etc/httpd/conf/ssl.crt/server.crt",
        "sslCertkeyfile": "/etc/httpd/conf/ssl.key/server.key",
        "sslCiphersuite": "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-SHA:ECDHE-RSA-AES256-SHA:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-SHA:ECDHE-ECDSA-AES256-SHA:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA384:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA:AES256-SHA:AES128-SHA256:AES256-SHA256",
        "sslOcspDefaultResponder": "http://127.0.0.1",
        "sslOcspEnable": "off",
        "sslOcspOverrideResponder": "off",
        "sslOcspResponderTimeout": 300,
        "sslOcspResponseMaxAge": -1,
        "sslOcspResponseTimeSkew": 300,
        "sslPort": 443,
        "sslProtocol": "all -SSLv2 -SSLv3 -TLSv1",
        "sslVerifyClient": "no",
        "sslVerifyDepth": 10,
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysHttpd(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysHttpd(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
