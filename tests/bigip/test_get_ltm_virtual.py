# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_virtual
from genie.libs.parser.bigip.get_ltm_virtual import LtmVirtual

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/virtual'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:virtual:virtualcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/virtual?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:virtual:virtualstate",
                    "name": "vip1",
                    "partition": "Common",
                    "fullPath": "/Common/vip1",
                    "generation": 1342,
                    "selfLink": "https://localhost/mgmt/tm/ltm/virtual/~Common~vip1?ver=14.1.2.1",
                    "addressStatus": "yes",
                    "autoLasthop": "default",
                    "cmpEnabled": "yes",
                    "connectionLimit": 0,
                    "creationTime": "2019-11-13T19:29:49Z",
                    "destination": "/Common/1.1.1.2:80",
                    "enabled": True,
                    "gtmScore": 0,
                    "ipProtocol": "tcp",
                    "lastModifiedTime": "2019-11-13T19:29:49Z",
                    "mask": "255.255.255.255",
                    "mirror": "disabled",
                    "mobileAppTunnel": "disabled",
                    "nat64": "disabled",
                    "pool": "/Common/pool1",
                    "poolReference": {
                        "link": "https://localhost/mgmt/tm/ltm/pool/~Common~pool1?ver=14.1.2.1"
                    },
                    "rateLimit": "disabled",
                    "rateLimitDstMask": 0,
                    "rateLimitMode": "object",
                    "rateLimitSrcMask": 0,
                    "serviceDownImmediateAction": "none",
                    "source": "0.0.0.0/0",
                    "sourceAddressTranslation": {"type": "none"},
                    "sourcePort": "preserve",
                    "synCookieStatus": "not-activated",
                    "translateAddress": "enabled",
                    "translatePort": "enabled",
                    "vlansDisabled": True,
                    "vsIndex": 27,
                    "policiesReference": {
                        "link": "https://localhost/mgmt/tm/ltm/virtual/~Common~vip1/policies?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                    "profilesReference": {
                        "link": "https://localhost/mgmt/tm/ltm/virtual/~Common~vip1/profiles?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:ltm:virtual:virtualstate",
                    "name": "vs-tcp-8191.CG2ABSV2MPG.lbsrvc-out-mainperf.local.net-out-10.10.34.250",
                    "partition": "Common",
                    "fullPath": "/Common/vs-tcp-8191.CG2ABSV2MPG.lbsrvc-out-mainperf.local.net-out-10.10.34.250",
                    "generation": 1446,
                    "selfLink": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs-tcp-8191.CG2ABSV2MPG.lbsrvc-out-mainperf.local.net-out-10.10.34.250?ver=14.1.2.1",
                    "addressStatus": "yes",
                    "autoLasthop": "default",
                    "cmpEnabled": "yes",
                    "connectionLimit": 0,
                    "creationTime": "2019-11-13T22:00:04Z",
                    "description": "CG2ABSV2MPG.lbsrvc-out-mainperf.local.net-out-10.10.34.250-8191",
                    "destination": "/Common/10.10.34.250:8191",
                    "enabled": True,
                    "gtmScore": 0,
                    "ipProtocol": "tcp",
                    "lastModifiedTime": "2019-11-13T22:00:04Z",
                    "mask": "255.255.255.255",
                    "mirror": "disabled",
                    "mobileAppTunnel": "disabled",
                    "nat64": "disabled",
                    "pool": "/Common/pool-tcp-8191.CG2ABSV2MPG.lbsrvc-out-mainperf.local.net-out-10.10.34.250",
                    "poolReference": {
                        "link": "https://localhost/mgmt/tm/ltm/pool/~Common~pool-tcp-8191.CG2ABSV2MPG.lbsrvc-out-mainperf.local.net-out-10.10.34.250?ver=14.1.2.1"
                    },
                    "rateLimit": "disabled",
                    "rateLimitDstMask": 0,
                    "rateLimitMode": "object",
                    "rateLimitSrcMask": 0,
                    "serviceDownImmediateAction": "none",
                    "source": "0.0.0.0/0",
                    "sourceAddressTranslation": {"type": "automap"},
                    "sourcePort": "preserve",
                    "synCookieStatus": "not-activated",
                    "translateAddress": "enabled",
                    "translatePort": "enabled",
                    "vlansEnabled": True,
                    "vsIndex": 35,
                    "rules": ["/Common/SNAT-39"],
                    "rulesReference": [
                        {
                            "link": "https://localhost/mgmt/tm/ltm/rule/~Common~SNAT-39?ver=14.1.2.1"
                        }
                    ],
                    "vlans": ["/Common/Internal"],
                    "vlansReference": [
                        {
                            "link": "https://localhost/mgmt/tm/net/vlan/~Common~Internal?ver=14.1.2.1"
                        }
                    ],
                    "metadata": [
                        {
                            "name": "f5-ansible.last_modified",
                            "persist": "true",
                            "value": "2019-11-14 15:23:15.845689",
                        },
                        {
                            "name": "f5-ansible.version",
                            "persist": "true",
                            "value": "2.9.0",
                        },
                    ],
                    "policiesReference": {
                        "link": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs-tcp-8191.CG2ABSV2MPG.lbsrvc-out-mainperf.local.net-out-10.10.34.250/policies?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                    "profilesReference": {
                        "link": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs-tcp-8191.CG2ABSV2MPG.lbsrvc-out-mainperf.local.net-out-10.10.34.250/profiles?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:ltm:virtual:virtualstate",
                    "name": "vs-tcp-9003-Test-Project-3-Test-LOB-3-10.1.1.3",
                    "partition": "Common",
                    "fullPath": "/Common/vs-tcp-9003-Test-Project-3-Test-LOB-3-10.1.1.3",
                    "generation": 1580,
                    "selfLink": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs-tcp-9003-Test-Project-3-Test-LOB-3-10.1.1.3?ver=14.1.2.1",
                    "addressStatus": "yes",
                    "autoLasthop": "default",
                    "cmpEnabled": "yes",
                    "connectionLimit": 0,
                    "creationTime": "2019-11-21T04:53:44Z",
                    "destination": "/Common/10.1.1.3:80",
                    "enabled": True,
                    "gtmScore": 0,
                    "ipProtocol": "tcp",
                    "lastModifiedTime": "2019-11-21T04:53:44Z",
                    "mask": "255.255.255.255",
                    "mirror": "disabled",
                    "mobileAppTunnel": "disabled",
                    "nat64": "disabled",
                    "pool": "/Common/pool-tcp-9003-Test-Project-3-Test-LOB-3-10.1.1.3",
                    "poolReference": {
                        "link": "https://localhost/mgmt/tm/ltm/pool/~Common~pool-tcp-9003-Test-Project-3-Test-LOB-3-10.1.1.3?ver=14.1.2.1"
                    },
                    "rateLimit": "disabled",
                    "rateLimitDstMask": 0,
                    "rateLimitMode": "object",
                    "rateLimitSrcMask": 0,
                    "serviceDownImmediateAction": "none",
                    "source": "0.0.0.0/0",
                    "sourceAddressTranslation": {"type": "none"},
                    "sourcePort": "preserve",
                    "synCookieStatus": "not-activated",
                    "translateAddress": "enabled",
                    "translatePort": "enabled",
                    "vlansDisabled": True,
                    "vsIndex": 39,
                    "policiesReference": {
                        "link": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs-tcp-9003-Test-Project-3-Test-LOB-3-10.1.1.3/policies?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                    "profilesReference": {
                        "link": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs-tcp-9003-Test-Project-3-Test-LOB-3-10.1.1.3/profiles?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:ltm:virtual:virtualstate",
                    "name": "vs-tcp-9007-Test-Project-7-Test-LOB-7-10.1.1.7",
                    "partition": "Common",
                    "fullPath": "/Common/vs-tcp-9007-Test-Project-7-Test-LOB-7-10.1.1.7",
                    "generation": 1458,
                    "selfLink": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs-tcp-9007-Test-Project-7-Test-LOB-7-10.1.1.7?ver=14.1.2.1",
                    "addressStatus": "yes",
                    "autoLasthop": "default",
                    "cmpEnabled": "yes",
                    "connectionLimit": 0,
                    "creationTime": "2019-11-13T22:15:29Z",
                    "description": "vs-tcp-9007-Test-Project-7-Test-LOB-7-10.1.1.7",
                    "destination": "/Common/10.1.1.7:9007",
                    "disabled": True,
                    "gtmScore": 0,
                    "ipProtocol": "tcp",
                    "lastModifiedTime": "2019-11-13T22:15:29Z",
                    "mask": "255.255.255.255",
                    "mirror": "disabled",
                    "mobileAppTunnel": "disabled",
                    "nat64": "disabled",
                    "pool": "/Common/pool-tcp-9007-Test-Project-7-Test-LOB-7-10.1.1.7",
                    "poolReference": {
                        "link": "https://localhost/mgmt/tm/ltm/pool/~Common~pool-tcp-9007-Test-Project-7-Test-LOB-7-10.1.1.7?ver=14.1.2.1"
                    },
                    "rateLimit": "disabled",
                    "rateLimitDstMask": 0,
                    "rateLimitMode": "object",
                    "rateLimitSrcMask": 0,
                    "serviceDownImmediateAction": "none",
                    "source": "0.0.0.0/0",
                    "sourceAddressTranslation": {"type": "automap"},
                    "sourcePort": "preserve",
                    "synCookieStatus": "not-activated",
                    "translateAddress": "enabled",
                    "translatePort": "enabled",
                    "vlansEnabled": True,
                    "vsIndex": 37,
                    "rules": ["/Common/SNAT-10-197-225.tcl"],
                    "rulesReference": [
                        {
                            "link": "https://localhost/mgmt/tm/ltm/rule/~Common~SNAT-10-197-225.tcl?ver=14.1.2.1"
                        }
                    ],
                    "vlans": ["/Common/Internal"],
                    "vlansReference": [
                        {
                            "link": "https://localhost/mgmt/tm/net/vlan/~Common~Internal?ver=14.1.2.1"
                        }
                    ],
                    "metadata": [
                        {
                            "name": "f5-ansible.last_modified",
                            "persist": "true",
                            "value": "2019-11-14 15:38:40.393209",
                        },
                        {
                            "name": "f5-ansible.version",
                            "persist": "true",
                            "value": "2.8.6",
                        },
                    ],
                    "policiesReference": {
                        "link": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs-tcp-9007-Test-Project-7-Test-LOB-7-10.1.1.7/policies?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                    "profilesReference": {
                        "link": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs-tcp-9007-Test-Project-7-Test-LOB-7-10.1.1.7/profiles?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:ltm:virtual:virtualstate",
                    "name": "vs-tcp-9406-IAC-2-IAC-2-101.11.11.139",
                    "partition": "Common",
                    "fullPath": "/Common/vs-tcp-9406-IAC-2-IAC-2-101.11.11.139",
                    "generation": 1440,
                    "selfLink": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs-tcp-9406-IAC-2-IAC-2-101.11.11.139?ver=14.1.2.1",
                    "addressStatus": "yes",
                    "autoLasthop": "default",
                    "cmpEnabled": "yes",
                    "connectionLimit": 0,
                    "creationTime": "2019-11-13T21:52:22Z",
                    "description": "vs-tcp-9406-IAC-2-IAC-2-101.11.11.139",
                    "destination": "/Common/101.11.11.139:9406",
                    "enabled": True,
                    "gtmScore": 0,
                    "ipProtocol": "tcp",
                    "lastModifiedTime": "2019-11-13T21:52:22Z",
                    "mask": "255.255.255.255",
                    "mirror": "disabled",
                    "mobileAppTunnel": "disabled",
                    "nat64": "disabled",
                    "pool": "/Common/pool-tcp-9406-IAC-2-IAC-2-101.11.11.139",
                    "poolReference": {
                        "link": "https://localhost/mgmt/tm/ltm/pool/~Common~pool-tcp-9406-IAC-2-IAC-2-101.11.11.139?ver=14.1.2.1"
                    },
                    "rateLimit": "disabled",
                    "rateLimitDstMask": 0,
                    "rateLimitMode": "object",
                    "rateLimitSrcMask": 0,
                    "serviceDownImmediateAction": "none",
                    "source": "0.0.0.0/0",
                    "sourceAddressTranslation": {"type": "automap"},
                    "sourcePort": "preserve",
                    "synCookieStatus": "not-activated",
                    "translateAddress": "enabled",
                    "translatePort": "enabled",
                    "vlansEnabled": True,
                    "vsIndex": 34,
                    "rules": ["/Common/SNAT-10-197-225.tcl"],
                    "rulesReference": [
                        {
                            "link": "https://localhost/mgmt/tm/ltm/rule/~Common~SNAT-10-197-225.tcl?ver=14.1.2.1"
                        }
                    ],
                    "vlans": ["/Common/Internal"],
                    "vlansReference": [
                        {
                            "link": "https://localhost/mgmt/tm/net/vlan/~Common~Internal?ver=14.1.2.1"
                        }
                    ],
                    "metadata": [
                        {
                            "name": "f5-ansible.last_modified",
                            "persist": "true",
                            "value": "2019-11-14 15:15:33.529332",
                        },
                        {
                            "name": "f5-ansible.version",
                            "persist": "true",
                            "value": "2.8.6",
                        },
                    ],
                    "policiesReference": {
                        "link": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs-tcp-9406-IAC-2-IAC-2-101.11.11.139/policies?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                    "profilesReference": {
                        "link": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs-tcp-9406-IAC-2-IAC-2-101.11.11.139/profiles?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:ltm:virtual:virtualstate",
                    "name": "vs_tcp_80_abc01.xyz.net_172.16.100.141",
                    "partition": "Common",
                    "fullPath": "/Common/vs_tcp_80_abc01.xyz.net_172.16.100.141",
                    "generation": 1430,
                    "selfLink": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs_tcp_80_abc01.xyz.net_172.16.100.141?ver=14.1.2.1",
                    "addressStatus": "yes",
                    "autoLasthop": "default",
                    "cmpEnabled": "yes",
                    "connectionLimit": 0,
                    "creationTime": "2019-11-13T21:44:16Z",
                    "description": "vs_tcp_80_abc01.xyz.net_172.16.0.141",
                    "destination": "/Common/172.16.100.141:80",
                    "enabled": True,
                    "gtmScore": 0,
                    "ipProtocol": "tcp",
                    "lastModifiedTime": "2019-11-13T21:46:05Z",
                    "mask": "255.255.255.255",
                    "mirror": "disabled",
                    "mobileAppTunnel": "disabled",
                    "nat64": "disabled",
                    "pool": "/Common/pl_web-pool101",
                    "poolReference": {
                        "link": "https://localhost/mgmt/tm/ltm/pool/~Common~pl_web-pool101?ver=14.1.2.1"
                    },
                    "rateLimit": "disabled",
                    "rateLimitDstMask": 0,
                    "rateLimitMode": "object",
                    "rateLimitSrcMask": 0,
                    "serviceDownImmediateAction": "none",
                    "source": "0.0.0.0/0",
                    "sourceAddressTranslation": {"type": "automap"},
                    "sourcePort": "preserve",
                    "synCookieStatus": "not-activated",
                    "translateAddress": "enabled",
                    "translatePort": "enabled",
                    "vlansDisabled": True,
                    "vsIndex": 33,
                    "policiesReference": {
                        "link": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs_tcp_80_abc01.xyz.net_172.16.100.141/policies?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                    "profilesReference": {
                        "link": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs_tcp_80_abc01.xyz.net_172.16.100.141/profiles?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:ltm:virtual:virtualstate",
                    "name": "vs_tcp_80_abc01.xyz.net_172.16.220.141",
                    "partition": "Common",
                    "fullPath": "/Common/vs_tcp_80_abc01.xyz.net_172.16.220.141",
                    "generation": 1431,
                    "selfLink": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs_tcp_80_abc01.xyz.net_172.16.220.141?ver=14.1.2.1",
                    "addressStatus": "yes",
                    "autoLasthop": "default",
                    "cmpEnabled": "yes",
                    "connectionLimit": 0,
                    "creationTime": "2019-11-13T21:44:15Z",
                    "description": "vs_tcp_80_abc01.xyz.net_172.16.0.141",
                    "destination": "/Common/172.16.220.141:8220",
                    "enabled": True,
                    "gtmScore": 0,
                    "ipProtocol": "tcp",
                    "lastModifiedTime": "2019-11-13T21:46:05Z",
                    "mask": "255.255.255.255",
                    "mirror": "disabled",
                    "mobileAppTunnel": "disabled",
                    "nat64": "disabled",
                    "pool": "/Common/pl_web-pool221",
                    "poolReference": {
                        "link": "https://localhost/mgmt/tm/ltm/pool/~Common~pl_web-pool221?ver=14.1.2.1"
                    },
                    "rateLimit": "disabled",
                    "rateLimitDstMask": 0,
                    "rateLimitMode": "object",
                    "rateLimitSrcMask": 0,
                    "serviceDownImmediateAction": "none",
                    "source": "0.0.0.0/0",
                    "sourceAddressTranslation": {"type": "automap"},
                    "sourcePort": "preserve",
                    "synCookieStatus": "not-activated",
                    "translateAddress": "enabled",
                    "translatePort": "enabled",
                    "vlansDisabled": True,
                    "vsIndex": 32,
                    "policiesReference": {
                        "link": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs_tcp_80_abc01.xyz.net_172.16.220.141/policies?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                    "profilesReference": {
                        "link": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs_tcp_80_abc01.xyz.net_172.16.220.141/profiles?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
            ],
        }


class test_get_ltm_virtual(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "addressStatus": "yes",
                "autoLasthop": "default",
                "cmpEnabled": "yes",
                "connectionLimit": 0,
                "creationTime": "2019-11-13T19:29:49Z",
                "destination": "/Common/1.1.1.2:80",
                "enabled": True,
                "fullPath": "/Common/vip1",
                "generation": 1342,
                "gtmScore": 0,
                "ipProtocol": "tcp",
                "kind": "tm:ltm:virtual:virtualstate",
                "lastModifiedTime": "2019-11-13T19:29:49Z",
                "mask": "255.255.255.255",
                "mirror": "disabled",
                "mobileAppTunnel": "disabled",
                "name": "vip1",
                "nat64": "disabled",
                "partition": "Common",
                "policiesReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/ltm/virtual/~Common~vip1/policies?ver=14.1.2.1",
                },
                "pool": "/Common/pool1",
                "poolReference": {
                    "link": "https://localhost/mgmt/tm/ltm/pool/~Common~pool1?ver=14.1.2.1"
                },
                "profilesReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/ltm/virtual/~Common~vip1/profiles?ver=14.1.2.1",
                },
                "rateLimit": "disabled",
                "rateLimitDstMask": 0,
                "rateLimitMode": "object",
                "rateLimitSrcMask": 0,
                "selfLink": "https://localhost/mgmt/tm/ltm/virtual/~Common~vip1?ver=14.1.2.1",
                "serviceDownImmediateAction": "none",
                "source": "0.0.0.0/0",
                "sourceAddressTranslation": {"type": "none"},
                "sourcePort": "preserve",
                "synCookieStatus": "not-activated",
                "translateAddress": "enabled",
                "translatePort": "enabled",
                "vlansDisabled": True,
                "vsIndex": 27,
            },
            {
                "addressStatus": "yes",
                "autoLasthop": "default",
                "cmpEnabled": "yes",
                "connectionLimit": 0,
                "creationTime": "2019-11-13T22:00:04Z",
                "description": "CG2ABSV2MPG.lbsrvc-out-mainperf.local.net-out-10.10.34.250-8191",
                "destination": "/Common/10.10.34.250:8191",
                "enabled": True,
                "fullPath": "/Common/vs-tcp-8191.CG2ABSV2MPG.lbsrvc-out-mainperf.local.net-out-10.10.34.250",
                "generation": 1446,
                "gtmScore": 0,
                "ipProtocol": "tcp",
                "kind": "tm:ltm:virtual:virtualstate",
                "lastModifiedTime": "2019-11-13T22:00:04Z",
                "mask": "255.255.255.255",
                "metadata": [
                    {
                        "name": "f5-ansible.last_modified",
                        "persist": "true",
                        "value": "2019-11-14 15:23:15.845689",
                    },
                    {
                        "name": "f5-ansible.version",
                        "persist": "true",
                        "value": "2.9.0",
                    },
                ],
                "mirror": "disabled",
                "mobileAppTunnel": "disabled",
                "name": "vs-tcp-8191.CG2ABSV2MPG.lbsrvc-out-mainperf.local.net-out-10.10.34.250",
                "nat64": "disabled",
                "partition": "Common",
                "policiesReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs-tcp-8191.CG2ABSV2MPG.lbsrvc-out-mainperf.local.net-out-10.10.34.250/policies?ver=14.1.2.1",
                },
                "pool": "/Common/pool-tcp-8191.CG2ABSV2MPG.lbsrvc-out-mainperf.local.net-out-10.10.34.250",
                "poolReference": {
                    "link": "https://localhost/mgmt/tm/ltm/pool/~Common~pool-tcp-8191.CG2ABSV2MPG.lbsrvc-out-mainperf.local.net-out-10.10.34.250?ver=14.1.2.1"
                },
                "profilesReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs-tcp-8191.CG2ABSV2MPG.lbsrvc-out-mainperf.local.net-out-10.10.34.250/profiles?ver=14.1.2.1",
                },
                "rateLimit": "disabled",
                "rateLimitDstMask": 0,
                "rateLimitMode": "object",
                "rateLimitSrcMask": 0,
                "rules": ["/Common/SNAT-39"],
                "rulesReference": [
                    {
                        "link": "https://localhost/mgmt/tm/ltm/rule/~Common~SNAT-39?ver=14.1.2.1"
                    }
                ],
                "selfLink": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs-tcp-8191.CG2ABSV2MPG.lbsrvc-out-mainperf.local.net-out-10.10.34.250?ver=14.1.2.1",
                "serviceDownImmediateAction": "none",
                "source": "0.0.0.0/0",
                "sourceAddressTranslation": {"type": "automap"},
                "sourcePort": "preserve",
                "synCookieStatus": "not-activated",
                "translateAddress": "enabled",
                "translatePort": "enabled",
                "vlans": ["/Common/Internal"],
                "vlansEnabled": True,
                "vlansReference": [
                    {
                        "link": "https://localhost/mgmt/tm/net/vlan/~Common~Internal?ver=14.1.2.1"
                    }
                ],
                "vsIndex": 35,
            },
            {
                "addressStatus": "yes",
                "autoLasthop": "default",
                "cmpEnabled": "yes",
                "connectionLimit": 0,
                "creationTime": "2019-11-21T04:53:44Z",
                "destination": "/Common/10.1.1.3:80",
                "enabled": True,
                "fullPath": "/Common/vs-tcp-9003-Test-Project-3-Test-LOB-3-10.1.1.3",
                "generation": 1580,
                "gtmScore": 0,
                "ipProtocol": "tcp",
                "kind": "tm:ltm:virtual:virtualstate",
                "lastModifiedTime": "2019-11-21T04:53:44Z",
                "mask": "255.255.255.255",
                "mirror": "disabled",
                "mobileAppTunnel": "disabled",
                "name": "vs-tcp-9003-Test-Project-3-Test-LOB-3-10.1.1.3",
                "nat64": "disabled",
                "partition": "Common",
                "policiesReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs-tcp-9003-Test-Project-3-Test-LOB-3-10.1.1.3/policies?ver=14.1.2.1",
                },
                "pool": "/Common/pool-tcp-9003-Test-Project-3-Test-LOB-3-10.1.1.3",
                "poolReference": {
                    "link": "https://localhost/mgmt/tm/ltm/pool/~Common~pool-tcp-9003-Test-Project-3-Test-LOB-3-10.1.1.3?ver=14.1.2.1"
                },
                "profilesReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs-tcp-9003-Test-Project-3-Test-LOB-3-10.1.1.3/profiles?ver=14.1.2.1",
                },
                "rateLimit": "disabled",
                "rateLimitDstMask": 0,
                "rateLimitMode": "object",
                "rateLimitSrcMask": 0,
                "selfLink": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs-tcp-9003-Test-Project-3-Test-LOB-3-10.1.1.3?ver=14.1.2.1",
                "serviceDownImmediateAction": "none",
                "source": "0.0.0.0/0",
                "sourceAddressTranslation": {"type": "none"},
                "sourcePort": "preserve",
                "synCookieStatus": "not-activated",
                "translateAddress": "enabled",
                "translatePort": "enabled",
                "vlansDisabled": True,
                "vsIndex": 39,
            },
            {
                "addressStatus": "yes",
                "autoLasthop": "default",
                "cmpEnabled": "yes",
                "connectionLimit": 0,
                "creationTime": "2019-11-13T22:15:29Z",
                "description": "vs-tcp-9007-Test-Project-7-Test-LOB-7-10.1.1.7",
                "destination": "/Common/10.1.1.7:9007",
                "disabled": True,
                "fullPath": "/Common/vs-tcp-9007-Test-Project-7-Test-LOB-7-10.1.1.7",
                "generation": 1458,
                "gtmScore": 0,
                "ipProtocol": "tcp",
                "kind": "tm:ltm:virtual:virtualstate",
                "lastModifiedTime": "2019-11-13T22:15:29Z",
                "mask": "255.255.255.255",
                "metadata": [
                    {
                        "name": "f5-ansible.last_modified",
                        "persist": "true",
                        "value": "2019-11-14 15:38:40.393209",
                    },
                    {
                        "name": "f5-ansible.version",
                        "persist": "true",
                        "value": "2.8.6",
                    },
                ],
                "mirror": "disabled",
                "mobileAppTunnel": "disabled",
                "name": "vs-tcp-9007-Test-Project-7-Test-LOB-7-10.1.1.7",
                "nat64": "disabled",
                "partition": "Common",
                "policiesReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs-tcp-9007-Test-Project-7-Test-LOB-7-10.1.1.7/policies?ver=14.1.2.1",
                },
                "pool": "/Common/pool-tcp-9007-Test-Project-7-Test-LOB-7-10.1.1.7",
                "poolReference": {
                    "link": "https://localhost/mgmt/tm/ltm/pool/~Common~pool-tcp-9007-Test-Project-7-Test-LOB-7-10.1.1.7?ver=14.1.2.1"
                },
                "profilesReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs-tcp-9007-Test-Project-7-Test-LOB-7-10.1.1.7/profiles?ver=14.1.2.1",
                },
                "rateLimit": "disabled",
                "rateLimitDstMask": 0,
                "rateLimitMode": "object",
                "rateLimitSrcMask": 0,
                "rules": ["/Common/SNAT-10-197-225.tcl"],
                "rulesReference": [
                    {
                        "link": "https://localhost/mgmt/tm/ltm/rule/~Common~SNAT-10-197-225.tcl?ver=14.1.2.1"
                    }
                ],
                "selfLink": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs-tcp-9007-Test-Project-7-Test-LOB-7-10.1.1.7?ver=14.1.2.1",
                "serviceDownImmediateAction": "none",
                "source": "0.0.0.0/0",
                "sourceAddressTranslation": {"type": "automap"},
                "sourcePort": "preserve",
                "synCookieStatus": "not-activated",
                "translateAddress": "enabled",
                "translatePort": "enabled",
                "vlans": ["/Common/Internal"],
                "vlansEnabled": True,
                "vlansReference": [
                    {
                        "link": "https://localhost/mgmt/tm/net/vlan/~Common~Internal?ver=14.1.2.1"
                    }
                ],
                "vsIndex": 37,
            },
            {
                "addressStatus": "yes",
                "autoLasthop": "default",
                "cmpEnabled": "yes",
                "connectionLimit": 0,
                "creationTime": "2019-11-13T21:52:22Z",
                "description": "vs-tcp-9406-IAC-2-IAC-2-101.11.11.139",
                "destination": "/Common/101.11.11.139:9406",
                "enabled": True,
                "fullPath": "/Common/vs-tcp-9406-IAC-2-IAC-2-101.11.11.139",
                "generation": 1440,
                "gtmScore": 0,
                "ipProtocol": "tcp",
                "kind": "tm:ltm:virtual:virtualstate",
                "lastModifiedTime": "2019-11-13T21:52:22Z",
                "mask": "255.255.255.255",
                "metadata": [
                    {
                        "name": "f5-ansible.last_modified",
                        "persist": "true",
                        "value": "2019-11-14 15:15:33.529332",
                    },
                    {
                        "name": "f5-ansible.version",
                        "persist": "true",
                        "value": "2.8.6",
                    },
                ],
                "mirror": "disabled",
                "mobileAppTunnel": "disabled",
                "name": "vs-tcp-9406-IAC-2-IAC-2-101.11.11.139",
                "nat64": "disabled",
                "partition": "Common",
                "policiesReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs-tcp-9406-IAC-2-IAC-2-101.11.11.139/policies?ver=14.1.2.1",
                },
                "pool": "/Common/pool-tcp-9406-IAC-2-IAC-2-101.11.11.139",
                "poolReference": {
                    "link": "https://localhost/mgmt/tm/ltm/pool/~Common~pool-tcp-9406-IAC-2-IAC-2-101.11.11.139?ver=14.1.2.1"
                },
                "profilesReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs-tcp-9406-IAC-2-IAC-2-101.11.11.139/profiles?ver=14.1.2.1",
                },
                "rateLimit": "disabled",
                "rateLimitDstMask": 0,
                "rateLimitMode": "object",
                "rateLimitSrcMask": 0,
                "rules": ["/Common/SNAT-10-197-225.tcl"],
                "rulesReference": [
                    {
                        "link": "https://localhost/mgmt/tm/ltm/rule/~Common~SNAT-10-197-225.tcl?ver=14.1.2.1"
                    }
                ],
                "selfLink": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs-tcp-9406-IAC-2-IAC-2-101.11.11.139?ver=14.1.2.1",
                "serviceDownImmediateAction": "none",
                "source": "0.0.0.0/0",
                "sourceAddressTranslation": {"type": "automap"},
                "sourcePort": "preserve",
                "synCookieStatus": "not-activated",
                "translateAddress": "enabled",
                "translatePort": "enabled",
                "vlans": ["/Common/Internal"],
                "vlansEnabled": True,
                "vlansReference": [
                    {
                        "link": "https://localhost/mgmt/tm/net/vlan/~Common~Internal?ver=14.1.2.1"
                    }
                ],
                "vsIndex": 34,
            },
            {
                "addressStatus": "yes",
                "autoLasthop": "default",
                "cmpEnabled": "yes",
                "connectionLimit": 0,
                "creationTime": "2019-11-13T21:44:16Z",
                "description": "vs_tcp_80_abc01.xyz.net_172.16.0.141",
                "destination": "/Common/172.16.100.141:80",
                "enabled": True,
                "fullPath": "/Common/vs_tcp_80_abc01.xyz.net_172.16.100.141",
                "generation": 1430,
                "gtmScore": 0,
                "ipProtocol": "tcp",
                "kind": "tm:ltm:virtual:virtualstate",
                "lastModifiedTime": "2019-11-13T21:46:05Z",
                "mask": "255.255.255.255",
                "mirror": "disabled",
                "mobileAppTunnel": "disabled",
                "name": "vs_tcp_80_abc01.xyz.net_172.16.100.141",
                "nat64": "disabled",
                "partition": "Common",
                "policiesReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs_tcp_80_abc01.xyz.net_172.16.100.141/policies?ver=14.1.2.1",
                },
                "pool": "/Common/pl_web-pool101",
                "poolReference": {
                    "link": "https://localhost/mgmt/tm/ltm/pool/~Common~pl_web-pool101?ver=14.1.2.1"
                },
                "profilesReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs_tcp_80_abc01.xyz.net_172.16.100.141/profiles?ver=14.1.2.1",
                },
                "rateLimit": "disabled",
                "rateLimitDstMask": 0,
                "rateLimitMode": "object",
                "rateLimitSrcMask": 0,
                "selfLink": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs_tcp_80_abc01.xyz.net_172.16.100.141?ver=14.1.2.1",
                "serviceDownImmediateAction": "none",
                "source": "0.0.0.0/0",
                "sourceAddressTranslation": {"type": "automap"},
                "sourcePort": "preserve",
                "synCookieStatus": "not-activated",
                "translateAddress": "enabled",
                "translatePort": "enabled",
                "vlansDisabled": True,
                "vsIndex": 33,
            },
            {
                "addressStatus": "yes",
                "autoLasthop": "default",
                "cmpEnabled": "yes",
                "connectionLimit": 0,
                "creationTime": "2019-11-13T21:44:15Z",
                "description": "vs_tcp_80_abc01.xyz.net_172.16.0.141",
                "destination": "/Common/172.16.220.141:8220",
                "enabled": True,
                "fullPath": "/Common/vs_tcp_80_abc01.xyz.net_172.16.220.141",
                "generation": 1431,
                "gtmScore": 0,
                "ipProtocol": "tcp",
                "kind": "tm:ltm:virtual:virtualstate",
                "lastModifiedTime": "2019-11-13T21:46:05Z",
                "mask": "255.255.255.255",
                "mirror": "disabled",
                "mobileAppTunnel": "disabled",
                "name": "vs_tcp_80_abc01.xyz.net_172.16.220.141",
                "nat64": "disabled",
                "partition": "Common",
                "policiesReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs_tcp_80_abc01.xyz.net_172.16.220.141/policies?ver=14.1.2.1",
                },
                "pool": "/Common/pl_web-pool221",
                "poolReference": {
                    "link": "https://localhost/mgmt/tm/ltm/pool/~Common~pl_web-pool221?ver=14.1.2.1"
                },
                "profilesReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs_tcp_80_abc01.xyz.net_172.16.220.141/profiles?ver=14.1.2.1",
                },
                "rateLimit": "disabled",
                "rateLimitDstMask": 0,
                "rateLimitMode": "object",
                "rateLimitSrcMask": 0,
                "selfLink": "https://localhost/mgmt/tm/ltm/virtual/~Common~vs_tcp_80_abc01.xyz.net_172.16.220.141?ver=14.1.2.1",
                "serviceDownImmediateAction": "none",
                "source": "0.0.0.0/0",
                "sourceAddressTranslation": {"type": "automap"},
                "sourcePort": "preserve",
                "synCookieStatus": "not-activated",
                "translateAddress": "enabled",
                "translatePort": "enabled",
                "vlansDisabled": True,
                "vsIndex": 32,
            },
        ],
        "kind": "tm:ltm:virtual:virtualcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/virtual?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmVirtual(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmVirtual(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
