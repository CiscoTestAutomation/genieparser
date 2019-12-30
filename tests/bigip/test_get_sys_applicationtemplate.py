# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_applicationtemplate
from genie.libs.parser.bigip.get_sys_applicationtemplate import (
    SysApplicationTemplate,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/application/template'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:application:template:templatecollectionstate",
            "selfLink": "https://localhost/mgmt/tm/sys/application/template?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:sys:application:template:templatestate",
                    "name": "f5.bea_weblogic",
                    "partition": "Common",
                    "fullPath": "/Common/f5.bea_weblogic",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.bea_weblogic?ver=14.1.2.1",
                    "ignoreVerification": "false",
                    "requiresBigipVersionMax": "13.1.0",
                    "requiresBigipVersionMin": "11.5.0",
                    "signingKey": "/Common/f5-irule",
                    "signingKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                    },
                    "tmplSignature": "XVoL9U9hNt0GaNU+IgFcxg6GkC3rF2b7A8EMMF6vthOPRKxWOmzD74rff4D+mRfJ57FFwTtEzOP27MVPouhzcQP4qPgSrB4G4S2/nicUDt863/yQ+lbXOLipPOA2SP4blqw3OmuqSH/+sHfeooywg3gRDhopYuBSZWHL3CXapOgGz0aVrb+drRghfU+rAPiRSbU3L4JKfeHkbCxMACKOtLsugnhYnU5865PigH+fGbEe8yabLhtmVC7a4NRGeNTV08Vnyh9p6vRPZG+t3rcHYClUE1SB/YTU7g/lbCqjSnPpR3JOjs0DaSFd+vdwxwtX3o2bw7wV1CTP5AdVnSX4TQ==",
                    "totalSigningStatus": "one-cert-signed",
                    "verificationStatus": "signature-verified",
                    "actionsReference": {
                        "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.bea_weblogic/actions?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:application:template:templatestate",
                    "name": "f5.cifs",
                    "partition": "Common",
                    "fullPath": "/Common/f5.cifs",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.cifs?ver=14.1.2.1",
                    "ignoreVerification": "false",
                    "prerequisiteErrors": "Error: am is not provisioned/enabled.",
                    "requiresBigipVersionMax": "13.1.0",
                    "requiresBigipVersionMin": "11.4.0",
                    "requiresModules": ["am"],
                    "signingKey": "/Common/f5-irule",
                    "signingKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                    },
                    "tmplSignature": "HLdCmhshGGjHjTCtSddRVUcC9ABN1vwwzOk3K8XHvlihSctkNSdoALqwYniJ5Esw437qPwuklEkLahjc8DjkB9bNdxJVRiUP6nHVyvUc/IaAiL4Gd1VxKqx/qullicB8oGrDsY6YPM9c7/l4Wf2fBsG3q1boeoARvxY0y+j6K315dltIyQOAkqyD0NkA47jCp5yMg0c+pM8HKCnY1DphrSDPp0Lt2pML3wFmiqq2ZE+3DfXWo4VE1SX3fG15OQDFLJFOtwI+MnXJErRF4J94piuKe/0t4InXWe2wmhN7iAr/tIYlq0dn5/fTRHUg524/u7TFMNVexbJcuoN/Ui+8RQ==",
                    "totalSigningStatus": "one-cert-signed",
                    "verificationStatus": "signature-verified",
                    "actionsReference": {
                        "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.cifs/actions?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:application:template:templatestate",
                    "name": "f5.citrix_presentation_server",
                    "partition": "Common",
                    "fullPath": "/Common/f5.citrix_presentation_server",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.citrix_presentation_server?ver=14.1.2.1",
                    "ignoreVerification": "false",
                    "requiresBigipVersionMax": "12.1.0",
                    "requiresBigipVersionMin": "11.4.0",
                    "requiresModules": ["ltm"],
                    "signingKey": "/Common/f5-irule",
                    "signingKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                    },
                    "tmplSignature": "Sr5m6PWobUngFFr4F/2NUxkb4KIc7d//TSGcPm202MukaLY7SO2pPas17yVA8ew3GwrL7zS9Sf6s0YGa+DE8ES+wzp47M0UuNkSlY/QLt5ah3Tfcz2fdchMbo+Lmorbj17rXa29IIoM/NQYIwPNEiwZuismuKvxCRSOROvVtEdWZINNdBjxhMSEMEhx8inGJmsrkDHEhfK+yuWYFhbRwtM6jSqFbkIpiWPK8dJ3wJNqpt2Y/Tky7q8YuuaWZrOlMS4Oy2neqA/YEL5Nlxm3YcbZug3ZdesODJqOTVTeFXgzBP4m3RX4AAUDEM3OM0eKzQiY+lC5EVESVpNWMo5mlCg==",
                    "totalSigningStatus": "one-cert-signed",
                    "verificationStatus": "signature-verified",
                    "actionsReference": {
                        "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.citrix_presentation_server/actions?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:application:template:templatestate",
                    "name": "f5.citrix_xen_app",
                    "partition": "Common",
                    "fullPath": "/Common/f5.citrix_xen_app",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.citrix_xen_app?ver=14.1.2.1",
                    "ignoreVerification": "false",
                    "requiresBigipVersionMax": "12.1.0",
                    "requiresBigipVersionMin": "11.4.0",
                    "requiresModules": ["ltm"],
                    "signingKey": "/Common/f5-irule",
                    "signingKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                    },
                    "tmplSignature": "XmavFlMkeaYbZD4C9UH9A5RG7F/3UCr22bdv9b+Vie38EqpDBMagxEOoTIlRDIBL4dLChC6uFKP48DPVS9PHMYWYb/DHh1odpIUClidjeAD5ofWBaRvFB7Wv9DgkPtyrK0zQ4Uxt+O5J5iQuyBvWlu6W0aBZ158cJ+pbKORUSMvgFpDJ+yyPZHdnKYwxx+fRhUMrU7RWCgQbLhpjH3o/4A4uXWBiYqVmYWi0pxVUE5Mj1ij2JU4OfMNr1BWXg7giLedU8PaRsSz8KsJ95WjphiWtxHT2cAoM8WgPx+FXqzryhxnWvMTtYBhXGWALwgFrwDOTBa5ShuswQcUMLzse0w==",
                    "totalSigningStatus": "one-cert-signed",
                    "verificationStatus": "signature-verified",
                    "actionsReference": {
                        "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.citrix_xen_app/actions?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:application:template:templatestate",
                    "name": "f5.diameter",
                    "partition": "Common",
                    "fullPath": "/Common/f5.diameter",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.diameter?ver=14.1.2.1",
                    "ignoreVerification": "false",
                    "requiresBigipVersionMin": "11.4.0",
                    "requiresModules": ["ltm"],
                    "signingKey": "/Common/f5-irule",
                    "signingKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                    },
                    "tmplSignature": "IYabgZmKAPZw4Ditr4kZrmvQ60F0zWlekz3U+5ezMmfIiAyDynErrBdiDjCB9bUE1ZEIXyr2w5+PPUH4iWwTBHa2YB/Cem3BehpG5ZpMS2n4EOg9vEyrwlVvCv8Oc9nd0UwwzGn0oHyJDAe+rR7bHxuSJK34hbbhX9MaSK0lZgNCv2dLSn4JVYrWJUe9H1AQHO7GJMqpcQSP/W4HQdCU8iCBfhV4SH4mZ4T9nvE9mQyWKh/qW/mPMuUPc6vfVanHNecscTys/Re49bDEnA3bUdB6S5QGkL2Jc6tahYiOGGNUDd8pjBUwz8ZEtKt1KW2aYsfwx64ugzkAD2unKCWdpw==",
                    "totalSigningStatus": "one-cert-signed",
                    "verificationStatus": "signature-verified",
                    "actionsReference": {
                        "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.diameter/actions?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:application:template:templatestate",
                    "name": "f5.dns",
                    "partition": "Common",
                    "fullPath": "/Common/f5.dns",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.dns?ver=14.1.2.1",
                    "ignoreVerification": "false",
                    "requiresBigipVersionMin": "11.4.0",
                    "requiresModules": ["ltm"],
                    "signingKey": "/Common/f5-irule",
                    "signingKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                    },
                    "tmplSignature": "GeuZpeVXExovXfOBwTxM1wyOkq/lkycNCEcc9l67kbvkbzOho8bRLng9m0IzePp+FGwL4U4QIV2tpKuN5HnEBRlSTKa4vncdZRMSNs8wA7Ax0TsTNQjUpeoXN1rDe7TCgJg+F2eGv1xOxSSB3cq99QsRDRpQoCY5Hk5m2CRLkPmjgtfHUg48PgZLJ97sUIL41jrOIUeUOnMvZxHC2nm17sYJ0zXj5xity74PX9dgvUYKfPcbYu6soRvgBHDGVQ+cycZc/5XiqsYs53UGE5/0K3Q1BFHZ6j3NuaE9RGQD8RPUQpn58VkTrCv1BURBVcjl0VV8prDNfQjCUHwKI8iwOA==",
                    "totalSigningStatus": "one-cert-signed",
                    "verificationStatus": "signature-verified",
                    "actionsReference": {
                        "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.dns/actions?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:application:template:templatestate",
                    "name": "f5.ftp",
                    "partition": "Common",
                    "fullPath": "/Common/f5.ftp",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.ftp?ver=14.1.2.1",
                    "ignoreVerification": "false",
                    "prerequisiteErrors": "Error: am is not provisioned/enabled.",
                    "requiresBigipVersionMax": "13.1.0",
                    "requiresBigipVersionMin": "11.4.0",
                    "requiresModules": ["am"],
                    "signingKey": "/Common/f5-irule",
                    "signingKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                    },
                    "tmplSignature": "lx4OxjLgbxfhE6SOE9Xlp2ZOwsotIEgD+OKWkSTrcaAanSQjkjIMEFmEepchc69S6uvuuiqW21mRtLMl8PzvQJ//Z4OXHCEba+GJNpsZy+OE7Y7lWqx+CxGNAoNuiwKvbWjG7UNfkCVs4v5w2hnyAp/fHsu0rimP6svc7QyNSZp6SczVDPxpeQy3japSKlkX7IOBBH9rmuj1kiF3nIALa2OnvdyYseJ+py3QBnSruQK3oZ+yxCOqFOKo2Fru2hrGItaHq5707Zzc0nQzdKOtWR/fz0zGzgymr3BctYxXrMu6fPahOrmhQcaD2fd1yGbgmqokCGJ+XonHqeSQd7Aq+g==",
                    "totalSigningStatus": "one-cert-signed",
                    "verificationStatus": "signature-verified",
                    "actionsReference": {
                        "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.ftp/actions?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:application:template:templatestate",
                    "name": "f5.http",
                    "partition": "Common",
                    "fullPath": "/Common/f5.http",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.http?ver=14.1.2.1",
                    "ignoreVerification": "false",
                    "requiresBigipVersionMin": "11.5.0",
                    "signingKey": "/Common/f5-irule",
                    "signingKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                    },
                    "tmplSignature": "IKgu72P0wc64JUma2QKuFSQ/vPMy3IxGAX4cOi6eRRfO8HFZJ7I6W1lK1qbKMOkkZ3sEE6fcEArqlIt0swqX7YnMX2ph0+v2iZXkNTk6MCVQekRIoi999hIFX+Rhd151efvULgemEV59XUoU+6HAL6YcfE9dZXg17Kf/g0O0oDE8VI+93ubTzE6QR4ZS8V4KwpzVy761DYxgqBs5Vu0tBYDPrJNO5j+IkQiW+/4o3Kzpj6ZgTrV39sXhLEYuulIuVRqJPZTCAVmY/GeBY2OM3q+urKjtQyu3sIDyBgP0vkY6I1pqvmcumPp0A+yJdXFZPF4HlO1ag7z3bL1lPOcPfw==",
                    "totalSigningStatus": "one-cert-signed",
                    "verificationStatus": "signature-verified",
                    "actionsReference": {
                        "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.http/actions?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:application:template:templatestate",
                    "name": "f5.ip_forwarding",
                    "partition": "Common",
                    "fullPath": "/Common/f5.ip_forwarding",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.ip_forwarding?ver=14.1.2.1",
                    "ignoreVerification": "false",
                    "requiresBigipVersionMin": "11.4.0",
                    "requiresModules": ["ltm"],
                    "signingKey": "/Common/f5-irule",
                    "signingKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                    },
                    "tmplSignature": "Zl9j3jJh6MJp23kBFHMZk6qzkuAMdkg3+Pn7nkB9T7TC4pUmodRBQwAJo7gk/wvgNaUnDfCy/IUKbFaGjzT9L+y6oPssqTG8YP+lJ/EYdTIK2w5XDKGmsaOkRyify4737FsGdqjyz99ChuywL+CX5BTV9WyeKfVO+wSxS6QeZlLVJUrgL8JhwjLixdGltrJtzHd7T7nhW86v5nObXMdTPW77eXmjV6+Ii3FOP8G/bMETHwoW7k2gUIShFqnmOqjyvZLH8QzMLU6b4iUioD39HqiZwCQ/oOIjbUrPPwB0r/WhiYE0b3piSLa6UoK5bopbcTYqlgLAowzAEfRlkwKiAg==",
                    "totalSigningStatus": "one-cert-signed",
                    "verificationStatus": "signature-verified",
                    "actionsReference": {
                        "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.ip_forwarding/actions?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:application:template:templatestate",
                    "name": "f5.ldap",
                    "partition": "Common",
                    "fullPath": "/Common/f5.ldap",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.ldap?ver=14.1.2.1",
                    "ignoreVerification": "false",
                    "requiresBigipVersionMin": "11.4.0",
                    "requiresModules": ["ltm"],
                    "signingKey": "/Common/f5-irule",
                    "signingKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                    },
                    "tmplSignature": "e4PtV0m3Lsn14J82Zjna55MO+TBTufzT2or7Th5lgWGpuYSFc8XhRg6aW3iHpCqCJKcKQ6YWy1YzcFjsrWJ4e+trQ74nqa8CqLXLs6uzaqmxkaRQgdUClUACjXIOx9GHOJGaRhvldlilfjWb20h/ogME8v0t36ZA3oykeAnZ6HmZzx0L/hm1Q8bkwN6RTRFh7uPkH2TRyjUUqC1bDTbl3Cf738hhh9pjRgyc9iOO+jBb2zm1QSyJ8q4MD2f+dGi45Uc90Cj0yOMfpWg73AQLKsvHPzGxrH4SFoeYMUArJuRCFE42WpiCREvnEVgob7lFmAGlIlDToHS0Jyca2wZ4Uw==",
                    "totalSigningStatus": "one-cert-signed",
                    "verificationStatus": "signature-verified",
                    "actionsReference": {
                        "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.ldap/actions?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:application:template:templatestate",
                    "name": "f5.microsoft_exchange_2010",
                    "partition": "Common",
                    "fullPath": "/Common/f5.microsoft_exchange_2010",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.microsoft_exchange_2010?ver=14.1.2.1",
                    "ignoreVerification": "false",
                    "requiresBigipVersionMax": "12.1.0",
                    "requiresBigipVersionMin": "11.4.0",
                    "requiresModules": ["ltm"],
                    "signingKey": "/Common/f5-irule",
                    "signingKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                    },
                    "tmplSignature": "D/3qwsglMZRpuePJecPX2OALA0p2ISkosUtWZ6q/zo6LDjpCZ0rImIPIABPnfnXrGRxrGO6McAH/ZNGwrOop9GSDIB9lUTbUgT/NJvMwq+XRymC+jfOYgxfwkmwZdJDTzEcNt10QoqHWvoq/Li7ARMRle9VskLqi+isQ4fwJl7MyZofOtJRBWeHwRJEoL23ZRRzSZAoDqa/XBCrtAkZ/1VQZx0+HuE4JBkfpoJYC/QUwU8SL8QU/IBDTm/9fJNbbC7HJo6wetdzUj8qluusPQk4CQzL3iQwqFdqrHMta017BP42K7az8XbCA9rWAr+buckOt5w0f2VdBLIR1ZC8vyA==",
                    "totalSigningStatus": "one-cert-signed",
                    "verificationStatus": "signature-verified",
                    "actionsReference": {
                        "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.microsoft_exchange_2010/actions?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:application:template:templatestate",
                    "name": "f5.microsoft_exchange_owa_2007",
                    "partition": "Common",
                    "fullPath": "/Common/f5.microsoft_exchange_owa_2007",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.microsoft_exchange_owa_2007?ver=14.1.2.1",
                    "ignoreVerification": "false",
                    "requiresBigipVersionMax": "12.1.0",
                    "requiresBigipVersionMin": "11.4.0",
                    "signingKey": "/Common/f5-irule",
                    "signingKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                    },
                    "tmplSignature": "DDfeduX/WmkBpdWZvipn5Dv4vLA6YtUFc7FHy4a6uGR/J802UhG7lsezOKnFKUiJBQaGEEfbDrzn2uTUA9ZLZCNEbD2OzzmbaryetK+ms48mJULDD4FzmJI4gHJYNXDlYFNk5Yw7n0ZTmoqegWt2tM3h3uTaWmz6di1ZgTL+PIzosMTdf6OtAiCbY3hMRihC9NuhIk61i5VK0S6n/JXU5iVVtcHUUIgZBxjsoBEQlR8IZu7jCx62bj39uE5CAO+FndFPpLDVf7fA38cU8o+/3tMDNSz+5dnzDDCqizWHjQxRlku0TcSdMQC9q1VOAXrPYCk/LtmCR/Ku315ONDRw5A==",
                    "totalSigningStatus": "one-cert-signed",
                    "verificationStatus": "signature-verified",
                    "actionsReference": {
                        "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.microsoft_exchange_owa_2007/actions?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:application:template:templatestate",
                    "name": "f5.microsoft_iis",
                    "partition": "Common",
                    "fullPath": "/Common/f5.microsoft_iis",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.microsoft_iis?ver=14.1.2.1",
                    "ignoreVerification": "false",
                    "requiresBigipVersionMin": "11.5.0",
                    "signingKey": "/Common/f5-irule",
                    "signingKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                    },
                    "tmplSignature": "ggb00Ed3FsVxfoNpxQo47sIcag79+vSQ7e2mUaVZIJzN0pbItuFvXwWaE9lRY8sCmC9lhvVx+tOwTT9qzw4DRKSvRG/69YEtT7F6GhL+8ZdwUiR3KtyAz9+lvFBXW5uAehhFLeW3ofZPDEzUKVhwRJK2DnOz5JyrcyinOczs4echPNhtm7B10PuoOGhTCiEkVnoMpz9f03qOXTjRs0tavQ4+ug+iRVjcCMaDmzS1B/tgfSKbCfrJA+UwCSuEqg+J6ciiRl9al8a3418T90Eg7W2O1qSTwl50E1h81/DbdOIK5pHgJQSYYZ9UoRwM/ppr+JJdUmTFVSgcLv8yjEYh6A==",
                    "totalSigningStatus": "one-cert-signed",
                    "verificationStatus": "signature-verified",
                    "actionsReference": {
                        "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.microsoft_iis/actions?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:application:template:templatestate",
                    "name": "f5.microsoft_lync_server_2010",
                    "partition": "Common",
                    "fullPath": "/Common/f5.microsoft_lync_server_2010",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.microsoft_lync_server_2010?ver=14.1.2.1",
                    "ignoreVerification": "false",
                    "requiresBigipVersionMax": "12.1.0",
                    "requiresBigipVersionMin": "11.4.0",
                    "requiresModules": ["ltm"],
                    "signingKey": "/Common/f5-irule",
                    "signingKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                    },
                    "tmplSignature": "OtOpRF3gnlvMuE0vah7rc/cZqr0+9igQqC99ekqjB2qGwFBMYUGIZ/6eTLPvXJf2GAWD+TO0zC6sGGhJOYdoKxff1M74Bp26IF1aSxQaweX+9xqsKMwNJi5X8Ks1yyyi+s7GLBc33Rv5xucMzMw/lIOqqoN+e227A2289VsVNIs1TEfZ5XIcb7AGWq9U9cGgdui283ekyczYks63Ltw/PzEqX/3AJR/f5xQH/IzjHS+W0XdMHl6fZdlK2FB0xgv9EguU+XaGXTUtd6oKFbSN3wDhNPgk8rFFKot8T4BtYwbM5rYLeSRPXMXAjhHZ0FPxWl9l5fRHHB5fISR5f2Lb4A==",
                    "totalSigningStatus": "one-cert-signed",
                    "verificationStatus": "signature-verified",
                    "actionsReference": {
                        "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.microsoft_lync_server_2010/actions?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:application:template:templatestate",
                    "name": "f5.microsoft_ocs_2007_r2",
                    "partition": "Common",
                    "fullPath": "/Common/f5.microsoft_ocs_2007_r2",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.microsoft_ocs_2007_r2?ver=14.1.2.1",
                    "ignoreVerification": "false",
                    "requiresBigipVersionMax": "12.1.0",
                    "requiresBigipVersionMin": "11.4.0",
                    "requiresModules": ["ltm"],
                    "signingKey": "/Common/f5-irule",
                    "signingKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                    },
                    "tmplSignature": "cdUTaR/Mud6PPlYTdztpz0tUbTo5PrcBMrx3jIhBvWaI7prJpYhDnQn9RMrZwz7ffRQq59NPblQMiYQEKvVJew5dx1Hkc0gFkRaxqlNtg9lF/wfweO9+Omxwj9oPyoEvAa8soLJQNnUP0CtH3jMXYw1U9tT9ExmFzE8ZuxNQgWywu6dRxZO9mDUcqoPjViROl/tZT7NQsUyVWRgPNXvhvJMPG7KJN5oSH2MU/t9EXxl64t3EECBLyQsG0EZHmeXm7atu+DQD8NyygioR9QiO3qe7esX4GhnLWxYNceRyeQg74EDPghanJQ8OZHMcdboHHHWsOnZ9pKHuLmQgZnJqcw==",
                    "totalSigningStatus": "one-cert-signed",
                    "verificationStatus": "signature-verified",
                    "actionsReference": {
                        "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.microsoft_ocs_2007_r2/actions?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:application:template:templatestate",
                    "name": "f5.microsoft_sharepoint_2007",
                    "partition": "Common",
                    "fullPath": "/Common/f5.microsoft_sharepoint_2007",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.microsoft_sharepoint_2007?ver=14.1.2.1",
                    "ignoreVerification": "false",
                    "requiresBigipVersionMax": "12.1.0",
                    "requiresBigipVersionMin": "11.4.0",
                    "signingKey": "/Common/f5-irule",
                    "signingKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                    },
                    "tmplSignature": "EVlp5nX4Tfa4OwXcmbazbcAsn+UNioe9pJGa92PwE2h4rk+Yj7j9hMmNxDTCgkVu7aBXNU+fERxuOeW92mK2BbdkEos0/HMNOF5cgvjoPxJvoOgKQInCYumH6OQ/0SQCkL46bT0Deullh1/n8VC5RIj+qoqIkvgACLl2syTz0cjfKrCHC5LJXR0Ja6yYhLraPX5+TmoJNoeZhqDGiYAmphkkvG2vT08wl9Kyz0XtgnBbmGPu6VqIpi7I7hthqHbAk8+kDY0khd/sg34kFbki5NtVrudQ9MXLq3c0kmqLoO2gBLCyND8KyHjz8idQSdOxO5Ga/gRTZcil60AufJNG8w==",
                    "totalSigningStatus": "one-cert-signed",
                    "verificationStatus": "signature-verified",
                    "actionsReference": {
                        "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.microsoft_sharepoint_2007/actions?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:application:template:templatestate",
                    "name": "f5.microsoft_sharepoint_2010",
                    "partition": "Common",
                    "fullPath": "/Common/f5.microsoft_sharepoint_2010",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.microsoft_sharepoint_2010?ver=14.1.2.1",
                    "ignoreVerification": "false",
                    "requiresBigipVersionMin": "11.5.0",
                    "signingKey": "/Common/f5-irule",
                    "signingKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                    },
                    "tmplSignature": "X3vPcUbwznluKUh++34sC/iOE4SExn58VOgPRw29IWRAJdhwxbVaxZ3dHd0LMMcQ0y32ZwvFML2kl9rW0KflrJ7CkRXBYKM3d8S20E4h1sG6Yk6u+M5eXG+iRJPLUI8fm3TA40xIIKLMrFEOHpVyxvL5em3EY/2QJetfdpjdn/sa1KymE8UZGfEn0PT+kYYatxiiCClDhd4L4aYyml6jhGCx1fauTb1nQo5BDgHx3OMr0LinZkM1y0aKpPnODLty6f/VkMKMylViwhNDLWmuaYpGXFzyuPKCVR8LwRPtgFi+kSlKXnKhoL5S0TSOB1YP4yzdmNX7/PUaVnHek5U+8Q==",
                    "totalSigningStatus": "one-cert-signed",
                    "verificationStatus": "signature-verified",
                    "actionsReference": {
                        "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.microsoft_sharepoint_2010/actions?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:application:template:templatestate",
                    "name": "f5.npath",
                    "partition": "Common",
                    "fullPath": "/Common/f5.npath",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.npath?ver=14.1.2.1",
                    "ignoreVerification": "false",
                    "requiresBigipVersionMin": "11.4.0",
                    "requiresModules": ["ltm"],
                    "signingKey": "/Common/f5-irule",
                    "signingKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                    },
                    "tmplSignature": "AXg5YAQ3g1MQumSAyCLZyDrb1WsLV1y1pbNNZBea7m/D7wtnFPyHpltlJlnsIl3/cUqxMcXzEqC5X3RfMdE/RKGFnV4SBDzKUbxIk4+t9jtgTw7PzS2rKkFkA5VIypZ9a2ts5ZqUnAYY2adBDzbVn7fAoqg0MBnVuMn2u6uWt/feR+mkNIraKf+NUkaS27v4YTtDMC11s6Z238uau29upK0QmKgnpj6rgC1iC74W4JkiPrSH4A3AW4b0H1bzBn/GSrRj2nO1mPmIYkmXu9FweStg3yprfbOLaY9nHuVymbDi375ESD+AH+Bq1TmyxYnGCiaWTb+lgRmYIH2Zbzyxiw==",
                    "totalSigningStatus": "one-cert-signed",
                    "verificationStatus": "signature-verified",
                    "actionsReference": {
                        "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.npath/actions?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:application:template:templatestate",
                    "name": "f5.oracle_as_10g",
                    "partition": "Common",
                    "fullPath": "/Common/f5.oracle_as_10g",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.oracle_as_10g?ver=14.1.2.1",
                    "ignoreVerification": "false",
                    "requiresBigipVersionMax": "13.1.0",
                    "requiresBigipVersionMin": "11.4.0",
                    "signingKey": "/Common/f5-irule",
                    "signingKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                    },
                    "tmplSignature": "grKFltviMvdeUsPg6UCANDSC20YxUZzzg3phYBMjrcZtOTcg+tcsRJVQ0wq94w2twhoj/0DNppm3Qz2+wj8ClROiclWvrtWV/DjxBeUd0LFMRf7p/6vJtgx8+4IHe/O+AaE3On0JdMLBCfdFp3g7cUhGZAAmr8M6DdKAm7SComHsZs4WhS5kCmNgJWTZvkmk2PgzDdxLE5D6iGQ8QAW+6IHpVhQ9S46oqHpHGnNQye1x7Zb968UcPCEQDB1l+II99VHyBp1B9Lrxr4CbI7z45HtHsvfDtDyCXF55ccqIXQ2lOrGlAYfWedDSwDria45w3ZxQ3+Ndd5bhQhBkVWEbqg==",
                    "totalSigningStatus": "one-cert-signed",
                    "verificationStatus": "signature-verified",
                    "actionsReference": {
                        "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.oracle_as_10g/actions?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:application:template:templatestate",
                    "name": "f5.oracle_ebs",
                    "partition": "Common",
                    "fullPath": "/Common/f5.oracle_ebs",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.oracle_ebs?ver=14.1.2.1",
                    "ignoreVerification": "false",
                    "requiresBigipVersionMax": "13.1.0",
                    "requiresBigipVersionMin": "11.5.0",
                    "signingKey": "/Common/f5-irule",
                    "signingKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                    },
                    "tmplSignature": "BL+tWDogX6+vLfyganxKylpAzDipUSsNHpFCLrnKkSnmUSMiThUWVq2/EmQN8zwRrip66o8PW8ooIfdNz3P8jOa5MOwsGK7FPpgjCFBcALWkvqSKJB1A2yt+QNJbRp7BCAz7Uf4wUae9BXoIcg5Il3xBj82QDlpswZtEzfQcI32uuIpLTy0UtqEtQlVV5zRdT16IaBpMEl6w237zx2Jd170JTTjFmez4IHH/gG1HFeSvfHkFSRvnKIag9EUC26FU4O8KurLE/VK/wMNE+hjrbuzE6aiy5DfLsKEdp48UrNnY0x2ORgjJkE0XBKSQattkWafbU6Ce64XqDzgtN9QGCg==",
                    "totalSigningStatus": "one-cert-signed",
                    "verificationStatus": "signature-verified",
                    "actionsReference": {
                        "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.oracle_ebs/actions?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:application:template:templatestate",
                    "name": "f5.peoplesoft_9",
                    "partition": "Common",
                    "fullPath": "/Common/f5.peoplesoft_9",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.peoplesoft_9?ver=14.1.2.1",
                    "ignoreVerification": "false",
                    "requiresBigipVersionMax": "13.1.0",
                    "requiresBigipVersionMin": "11.5.0",
                    "signingKey": "/Common/f5-irule",
                    "signingKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                    },
                    "tmplSignature": "aELtdJPG5rJS1ONgWVE6+x+FWbkw5WoaDU3f8LF0j9a0XXXZDEgHbvKLaQrueeBv3bhZ0xQiNdEcmiUC5f1sBZ7CdtQpxd7PKegIpIRXZlWZZHykjjzuh2D8zhQP0lQQkO6t/FOtAXirSs+0Ob93qnKe8in3mue/dK6XeuhRl28Ov6BprXbQhUK3W76Ommt1hINDSXY1vC4x7viIfK/yyTIPSWNd7jMk83LPwkQop5iCczdh3IbQ5d8L998epwCmvwuWFCS1d3yBCp3SIYOR0rQNk5naWSOE7M6L0wQtFbrZsn1+LxUqj3Df/gQoSa5Ahl6JUjfUriUy4H/QfRgfPg==",
                    "totalSigningStatus": "one-cert-signed",
                    "verificationStatus": "signature-verified",
                    "actionsReference": {
                        "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.peoplesoft_9/actions?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:application:template:templatestate",
                    "name": "f5.radius",
                    "partition": "Common",
                    "fullPath": "/Common/f5.radius",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.radius?ver=14.1.2.1",
                    "ignoreVerification": "false",
                    "requiresBigipVersionMin": "11.4.0",
                    "requiresModules": ["ltm"],
                    "signingKey": "/Common/f5-irule",
                    "signingKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                    },
                    "tmplSignature": "AvmOJD8Vh1r/jujEgusCmxNRcYFwfvaS1uO0MMlFqwtFCxl6Mpd+NUdtPGI7BYON5HKFr8e64MVMlxhfXNh1SyFK3fJueZ6hqPc1OOHMx1AiU+/VsozwciayF2nG0A5KUHEslY52MMQf9xiUvuDRVZTHrOU025E+QxtObDTlbrp03mW00dUflDP0W1qyvAruL73DXeSADMZLpo9Cm7r2mYA/RgKT8DVXfItwYSFBMyd1YR5AJHYIxoOc1WFZIyZ//AdktHRE5eaEozIQZ3bB4Re2qU8aoabhQB0SexDvaYOrY7AznxQN4MY4QAFY/XqyO/1RuY+svnWE/lbrqkMZWw==",
                    "totalSigningStatus": "one-cert-signed",
                    "verificationStatus": "signature-verified",
                    "actionsReference": {
                        "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.radius/actions?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:application:template:templatestate",
                    "name": "f5.replication",
                    "partition": "Common",
                    "fullPath": "/Common/f5.replication",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.replication?ver=14.1.2.1",
                    "ignoreVerification": "false",
                    "prerequisiteErrors": "Error: am is not provisioned/enabled.",
                    "requiresBigipVersionMax": "13.1.0",
                    "requiresBigipVersionMin": "11.4.0",
                    "requiresModules": ["am"],
                    "signingKey": "/Common/f5-irule",
                    "signingKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                    },
                    "tmplSignature": "TNzZ2xvZTm3Jqu+1+ZuCWq0wlg3awZ7BkKhR9n+RV7DzE3yfJ1A66QPt64AoJ1fXsSS2tqMOceuOG8+odpH/1MVTU23EABE+6F75xDdi4rbzNE2oaG5ntU2+EUkqmz2hf4SKrIwaM0oU7JCMZBLYMj1nyxmikVWhpVIWF7f3MaYVYXpTGWDhv+yFk8VvuxYTQQSgWhMuqZAqqq0fBgSAd+lLxTB+8YyQMPpHQ2ZC31vKus63u0Pj3HIftmt9zKTBuh0KReHF4g4ZIQJ1VUrojI0UKR/D8+7L3zkBA2aGdWUeJu1mcxqPn8xzITRDffkWQLIc0C0wjNCgqS9uELM+xg==",
                    "totalSigningStatus": "one-cert-signed",
                    "verificationStatus": "signature-verified",
                    "actionsReference": {
                        "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.replication/actions?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:application:template:templatestate",
                    "name": "f5.sap_enterprise_portal",
                    "partition": "Common",
                    "fullPath": "/Common/f5.sap_enterprise_portal",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.sap_enterprise_portal?ver=14.1.2.1",
                    "ignoreVerification": "false",
                    "requiresBigipVersionMax": "13.1.0",
                    "requiresBigipVersionMin": "11.5.0",
                    "signingKey": "/Common/f5-irule",
                    "signingKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                    },
                    "tmplSignature": "EdbiChNEy0qmOq1cgic+TXNP0C/X4kQw/qXqQ+pKBudxQxVjakkl+uD2yp4vYx9H0+Qw7bD9LIyt6c9X1Cd2ZZVBuEZx/mmidYuN9gRroU5G6HxwaHkVBmI1/EGxC1/iotlaStxpzitq81znkXTDjosAvY8W4xL8Dl55una9GjmuZX8yMTfKfwEm+qc4zbp88i5+Wnp19Khem3E2sIQChNiZDfR7DjKotPuDDr7nmN1dr2bBJhPGRtv8WZwzfrgghwNxIYzIw8y3zrIQpeJAkmCBjA+KhxQYKxaAHzXx3EUrjNZlcxi8RRdliD+cZtWCjCHCl/Nx6xRJIMyUJZTUsw==",
                    "totalSigningStatus": "one-cert-signed",
                    "verificationStatus": "signature-verified",
                    "actionsReference": {
                        "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.sap_enterprise_portal/actions?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:application:template:templatestate",
                    "name": "f5.sap_erp",
                    "partition": "Common",
                    "fullPath": "/Common/f5.sap_erp",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.sap_erp?ver=14.1.2.1",
                    "ignoreVerification": "false",
                    "requiresBigipVersionMax": "13.1.0",
                    "requiresBigipVersionMin": "11.5.0",
                    "signingKey": "/Common/f5-irule",
                    "signingKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                    },
                    "tmplSignature": "a+268FXW1grdVcND6t6wqI5WpY7KW0iasypriPWOrEYsnJQ96g1n1K6ynxUoBs0/P23881tMVefUK4jyf4wFXlgE8OzGnjQCmqMuRoRkQ0U6JWPKMbQIFAasCkJCR8kBBKcmnUmA59vw8brMR7MRaUITMWuyrmAZtri5EMK5ljcHSWvbE7hdLPK3K+rZAI5xpzT3e30oQvAd0T3g/D9pPzhE4VqInXHbiTh0wvM2Nxh8SqepNTSGkkyr99xn21xklRtkiCHH1QAB8oPvvWJ7Tm76AyvtK7RGBwwc3dYDDD/4K+BH8nzN3nZk55cjAKZP7HZ1Bh+A9ijzjZ67vTjwHg==",
                    "totalSigningStatus": "one-cert-signed",
                    "verificationStatus": "signature-verified",
                    "actionsReference": {
                        "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.sap_erp/actions?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:application:template:templatestate",
                    "name": "f5.vmware_view",
                    "partition": "Common",
                    "fullPath": "/Common/f5.vmware_view",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.vmware_view?ver=14.1.2.1",
                    "ignoreVerification": "false",
                    "requiresBigipVersionMax": "12.1.0",
                    "requiresBigipVersionMin": "11.4.0",
                    "requiresModules": ["ltm"],
                    "signingKey": "/Common/f5-irule",
                    "signingKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                    },
                    "tmplSignature": "Vgj7OLs9HdTygNJAb0eZKVSRyPaoWnclZXeBTEttpix806cW0rCu0bnJ8P1wjI3SBweQ3ButZvpz7pfp76DJvVg6aeLCaYbPrVWwAUyH8EyH4+J7PWpc08a+38+s1u9F5IUHU4uMiwxmXUaS4ao3XkB0AmA4nkwKvqyHC2s2BSHm9viqO58dglfrAClYNUvnP9FDVcDHiOw/5lNOhYU78Z1d56bhwcl3GdpbPpnT+6i7A+253kZ4Vj0xDqCpxTR47hcLVZO89yVdHdx7C/VuaNhHWLyTluVRohIIrG7PN3i5b+M+n91e/9ageQX1Z7DVlDQlpjS63DzUdPQVK+jjAQ==",
                    "totalSigningStatus": "one-cert-signed",
                    "verificationStatus": "signature-verified",
                    "actionsReference": {
                        "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.vmware_view/actions?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:application:template:templatestate",
                    "name": "f5.vmware_vmotion",
                    "partition": "Common",
                    "fullPath": "/Common/f5.vmware_vmotion",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.vmware_vmotion?ver=14.1.2.1",
                    "ignoreVerification": "false",
                    "prerequisiteErrors": "Error: am is not provisioned/enabled.",
                    "requiresBigipVersionMax": "13.1.0",
                    "requiresBigipVersionMin": "11.4.0",
                    "requiresModules": ["am"],
                    "signingKey": "/Common/f5-irule",
                    "signingKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                    },
                    "tmplSignature": "QxUEiGk06+t867VXiWmORxaqIXzz4+B5CAcpKe0pjwcDpRuYUBmwLojHznYaEvz1pout67LyX9OOKNLenrB5Fky3ZyFZbuBBLElgKPWDgzOfUTncRQFIH4o+NARGKVcSA+F2mBjWBqJ8oqOt1XbqPTIq31ciDDA5bXsH9J7V3wqvTqg+oHcPhDpFMXNi/BHE5EBFcfD2Y4fH1zBFT/KtCIYku7hIp0lBaNaMNRM568REgHLIasKMoHlloJxr2TFBhbMR71QMqT5G/T8L2BDBcHV/57EMsrwJFPgmR2h29kv6E6cOxrYV4l1cisFQXkJwOZtfcoGFjYzR5oToW+YRtg==",
                    "totalSigningStatus": "one-cert-signed",
                    "verificationStatus": "signature-verified",
                    "actionsReference": {
                        "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.vmware_vmotion/actions?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
            ],
        }


class test_get_sys_applicationtemplate(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "actionsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.bea_weblogic/actions?ver=14.1.2.1",
                },
                "fullPath": "/Common/f5.bea_weblogic",
                "generation": 1,
                "ignoreVerification": "false",
                "kind": "tm:sys:application:template:templatestate",
                "name": "f5.bea_weblogic",
                "partition": "Common",
                "requiresBigipVersionMax": "13.1.0",
                "requiresBigipVersionMin": "11.5.0",
                "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.bea_weblogic?ver=14.1.2.1",
                "signingKey": "/Common/f5-irule",
                "signingKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                },
                "tmplSignature": "XVoL9U9hNt0GaNU+IgFcxg6GkC3rF2b7A8EMMF6vthOPRKxWOmzD74rff4D+mRfJ57FFwTtEzOP27MVPouhzcQP4qPgSrB4G4S2/nicUDt863/yQ+lbXOLipPOA2SP4blqw3OmuqSH/+sHfeooywg3gRDhopYuBSZWHL3CXapOgGz0aVrb+drRghfU+rAPiRSbU3L4JKfeHkbCxMACKOtLsugnhYnU5865PigH+fGbEe8yabLhtmVC7a4NRGeNTV08Vnyh9p6vRPZG+t3rcHYClUE1SB/YTU7g/lbCqjSnPpR3JOjs0DaSFd+vdwxwtX3o2bw7wV1CTP5AdVnSX4TQ==",
                "totalSigningStatus": "one-cert-signed",
                "verificationStatus": "signature-verified",
            },
            {
                "actionsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.cifs/actions?ver=14.1.2.1",
                },
                "fullPath": "/Common/f5.cifs",
                "generation": 1,
                "ignoreVerification": "false",
                "kind": "tm:sys:application:template:templatestate",
                "name": "f5.cifs",
                "partition": "Common",
                "prerequisiteErrors": "Error: am is not provisioned/enabled.",
                "requiresBigipVersionMax": "13.1.0",
                "requiresBigipVersionMin": "11.4.0",
                "requiresModules": ["am"],
                "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.cifs?ver=14.1.2.1",
                "signingKey": "/Common/f5-irule",
                "signingKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                },
                "tmplSignature": "HLdCmhshGGjHjTCtSddRVUcC9ABN1vwwzOk3K8XHvlihSctkNSdoALqwYniJ5Esw437qPwuklEkLahjc8DjkB9bNdxJVRiUP6nHVyvUc/IaAiL4Gd1VxKqx/qullicB8oGrDsY6YPM9c7/l4Wf2fBsG3q1boeoARvxY0y+j6K315dltIyQOAkqyD0NkA47jCp5yMg0c+pM8HKCnY1DphrSDPp0Lt2pML3wFmiqq2ZE+3DfXWo4VE1SX3fG15OQDFLJFOtwI+MnXJErRF4J94piuKe/0t4InXWe2wmhN7iAr/tIYlq0dn5/fTRHUg524/u7TFMNVexbJcuoN/Ui+8RQ==",
                "totalSigningStatus": "one-cert-signed",
                "verificationStatus": "signature-verified",
            },
            {
                "actionsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.citrix_presentation_server/actions?ver=14.1.2.1",
                },
                "fullPath": "/Common/f5.citrix_presentation_server",
                "generation": 1,
                "ignoreVerification": "false",
                "kind": "tm:sys:application:template:templatestate",
                "name": "f5.citrix_presentation_server",
                "partition": "Common",
                "requiresBigipVersionMax": "12.1.0",
                "requiresBigipVersionMin": "11.4.0",
                "requiresModules": ["ltm"],
                "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.citrix_presentation_server?ver=14.1.2.1",
                "signingKey": "/Common/f5-irule",
                "signingKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                },
                "tmplSignature": "Sr5m6PWobUngFFr4F/2NUxkb4KIc7d//TSGcPm202MukaLY7SO2pPas17yVA8ew3GwrL7zS9Sf6s0YGa+DE8ES+wzp47M0UuNkSlY/QLt5ah3Tfcz2fdchMbo+Lmorbj17rXa29IIoM/NQYIwPNEiwZuismuKvxCRSOROvVtEdWZINNdBjxhMSEMEhx8inGJmsrkDHEhfK+yuWYFhbRwtM6jSqFbkIpiWPK8dJ3wJNqpt2Y/Tky7q8YuuaWZrOlMS4Oy2neqA/YEL5Nlxm3YcbZug3ZdesODJqOTVTeFXgzBP4m3RX4AAUDEM3OM0eKzQiY+lC5EVESVpNWMo5mlCg==",
                "totalSigningStatus": "one-cert-signed",
                "verificationStatus": "signature-verified",
            },
            {
                "actionsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.citrix_xen_app/actions?ver=14.1.2.1",
                },
                "fullPath": "/Common/f5.citrix_xen_app",
                "generation": 1,
                "ignoreVerification": "false",
                "kind": "tm:sys:application:template:templatestate",
                "name": "f5.citrix_xen_app",
                "partition": "Common",
                "requiresBigipVersionMax": "12.1.0",
                "requiresBigipVersionMin": "11.4.0",
                "requiresModules": ["ltm"],
                "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.citrix_xen_app?ver=14.1.2.1",
                "signingKey": "/Common/f5-irule",
                "signingKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                },
                "tmplSignature": "XmavFlMkeaYbZD4C9UH9A5RG7F/3UCr22bdv9b+Vie38EqpDBMagxEOoTIlRDIBL4dLChC6uFKP48DPVS9PHMYWYb/DHh1odpIUClidjeAD5ofWBaRvFB7Wv9DgkPtyrK0zQ4Uxt+O5J5iQuyBvWlu6W0aBZ158cJ+pbKORUSMvgFpDJ+yyPZHdnKYwxx+fRhUMrU7RWCgQbLhpjH3o/4A4uXWBiYqVmYWi0pxVUE5Mj1ij2JU4OfMNr1BWXg7giLedU8PaRsSz8KsJ95WjphiWtxHT2cAoM8WgPx+FXqzryhxnWvMTtYBhXGWALwgFrwDOTBa5ShuswQcUMLzse0w==",
                "totalSigningStatus": "one-cert-signed",
                "verificationStatus": "signature-verified",
            },
            {
                "actionsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.diameter/actions?ver=14.1.2.1",
                },
                "fullPath": "/Common/f5.diameter",
                "generation": 1,
                "ignoreVerification": "false",
                "kind": "tm:sys:application:template:templatestate",
                "name": "f5.diameter",
                "partition": "Common",
                "requiresBigipVersionMin": "11.4.0",
                "requiresModules": ["ltm"],
                "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.diameter?ver=14.1.2.1",
                "signingKey": "/Common/f5-irule",
                "signingKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                },
                "tmplSignature": "IYabgZmKAPZw4Ditr4kZrmvQ60F0zWlekz3U+5ezMmfIiAyDynErrBdiDjCB9bUE1ZEIXyr2w5+PPUH4iWwTBHa2YB/Cem3BehpG5ZpMS2n4EOg9vEyrwlVvCv8Oc9nd0UwwzGn0oHyJDAe+rR7bHxuSJK34hbbhX9MaSK0lZgNCv2dLSn4JVYrWJUe9H1AQHO7GJMqpcQSP/W4HQdCU8iCBfhV4SH4mZ4T9nvE9mQyWKh/qW/mPMuUPc6vfVanHNecscTys/Re49bDEnA3bUdB6S5QGkL2Jc6tahYiOGGNUDd8pjBUwz8ZEtKt1KW2aYsfwx64ugzkAD2unKCWdpw==",
                "totalSigningStatus": "one-cert-signed",
                "verificationStatus": "signature-verified",
            },
            {
                "actionsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.dns/actions?ver=14.1.2.1",
                },
                "fullPath": "/Common/f5.dns",
                "generation": 1,
                "ignoreVerification": "false",
                "kind": "tm:sys:application:template:templatestate",
                "name": "f5.dns",
                "partition": "Common",
                "requiresBigipVersionMin": "11.4.0",
                "requiresModules": ["ltm"],
                "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.dns?ver=14.1.2.1",
                "signingKey": "/Common/f5-irule",
                "signingKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                },
                "tmplSignature": "GeuZpeVXExovXfOBwTxM1wyOkq/lkycNCEcc9l67kbvkbzOho8bRLng9m0IzePp+FGwL4U4QIV2tpKuN5HnEBRlSTKa4vncdZRMSNs8wA7Ax0TsTNQjUpeoXN1rDe7TCgJg+F2eGv1xOxSSB3cq99QsRDRpQoCY5Hk5m2CRLkPmjgtfHUg48PgZLJ97sUIL41jrOIUeUOnMvZxHC2nm17sYJ0zXj5xity74PX9dgvUYKfPcbYu6soRvgBHDGVQ+cycZc/5XiqsYs53UGE5/0K3Q1BFHZ6j3NuaE9RGQD8RPUQpn58VkTrCv1BURBVcjl0VV8prDNfQjCUHwKI8iwOA==",
                "totalSigningStatus": "one-cert-signed",
                "verificationStatus": "signature-verified",
            },
            {
                "actionsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.ftp/actions?ver=14.1.2.1",
                },
                "fullPath": "/Common/f5.ftp",
                "generation": 1,
                "ignoreVerification": "false",
                "kind": "tm:sys:application:template:templatestate",
                "name": "f5.ftp",
                "partition": "Common",
                "prerequisiteErrors": "Error: am is not provisioned/enabled.",
                "requiresBigipVersionMax": "13.1.0",
                "requiresBigipVersionMin": "11.4.0",
                "requiresModules": ["am"],
                "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.ftp?ver=14.1.2.1",
                "signingKey": "/Common/f5-irule",
                "signingKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                },
                "tmplSignature": "lx4OxjLgbxfhE6SOE9Xlp2ZOwsotIEgD+OKWkSTrcaAanSQjkjIMEFmEepchc69S6uvuuiqW21mRtLMl8PzvQJ//Z4OXHCEba+GJNpsZy+OE7Y7lWqx+CxGNAoNuiwKvbWjG7UNfkCVs4v5w2hnyAp/fHsu0rimP6svc7QyNSZp6SczVDPxpeQy3japSKlkX7IOBBH9rmuj1kiF3nIALa2OnvdyYseJ+py3QBnSruQK3oZ+yxCOqFOKo2Fru2hrGItaHq5707Zzc0nQzdKOtWR/fz0zGzgymr3BctYxXrMu6fPahOrmhQcaD2fd1yGbgmqokCGJ+XonHqeSQd7Aq+g==",
                "totalSigningStatus": "one-cert-signed",
                "verificationStatus": "signature-verified",
            },
            {
                "actionsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.http/actions?ver=14.1.2.1",
                },
                "fullPath": "/Common/f5.http",
                "generation": 1,
                "ignoreVerification": "false",
                "kind": "tm:sys:application:template:templatestate",
                "name": "f5.http",
                "partition": "Common",
                "requiresBigipVersionMin": "11.5.0",
                "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.http?ver=14.1.2.1",
                "signingKey": "/Common/f5-irule",
                "signingKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                },
                "tmplSignature": "IKgu72P0wc64JUma2QKuFSQ/vPMy3IxGAX4cOi6eRRfO8HFZJ7I6W1lK1qbKMOkkZ3sEE6fcEArqlIt0swqX7YnMX2ph0+v2iZXkNTk6MCVQekRIoi999hIFX+Rhd151efvULgemEV59XUoU+6HAL6YcfE9dZXg17Kf/g0O0oDE8VI+93ubTzE6QR4ZS8V4KwpzVy761DYxgqBs5Vu0tBYDPrJNO5j+IkQiW+/4o3Kzpj6ZgTrV39sXhLEYuulIuVRqJPZTCAVmY/GeBY2OM3q+urKjtQyu3sIDyBgP0vkY6I1pqvmcumPp0A+yJdXFZPF4HlO1ag7z3bL1lPOcPfw==",
                "totalSigningStatus": "one-cert-signed",
                "verificationStatus": "signature-verified",
            },
            {
                "actionsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.ip_forwarding/actions?ver=14.1.2.1",
                },
                "fullPath": "/Common/f5.ip_forwarding",
                "generation": 1,
                "ignoreVerification": "false",
                "kind": "tm:sys:application:template:templatestate",
                "name": "f5.ip_forwarding",
                "partition": "Common",
                "requiresBigipVersionMin": "11.4.0",
                "requiresModules": ["ltm"],
                "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.ip_forwarding?ver=14.1.2.1",
                "signingKey": "/Common/f5-irule",
                "signingKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                },
                "tmplSignature": "Zl9j3jJh6MJp23kBFHMZk6qzkuAMdkg3+Pn7nkB9T7TC4pUmodRBQwAJo7gk/wvgNaUnDfCy/IUKbFaGjzT9L+y6oPssqTG8YP+lJ/EYdTIK2w5XDKGmsaOkRyify4737FsGdqjyz99ChuywL+CX5BTV9WyeKfVO+wSxS6QeZlLVJUrgL8JhwjLixdGltrJtzHd7T7nhW86v5nObXMdTPW77eXmjV6+Ii3FOP8G/bMETHwoW7k2gUIShFqnmOqjyvZLH8QzMLU6b4iUioD39HqiZwCQ/oOIjbUrPPwB0r/WhiYE0b3piSLa6UoK5bopbcTYqlgLAowzAEfRlkwKiAg==",
                "totalSigningStatus": "one-cert-signed",
                "verificationStatus": "signature-verified",
            },
            {
                "actionsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.ldap/actions?ver=14.1.2.1",
                },
                "fullPath": "/Common/f5.ldap",
                "generation": 1,
                "ignoreVerification": "false",
                "kind": "tm:sys:application:template:templatestate",
                "name": "f5.ldap",
                "partition": "Common",
                "requiresBigipVersionMin": "11.4.0",
                "requiresModules": ["ltm"],
                "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.ldap?ver=14.1.2.1",
                "signingKey": "/Common/f5-irule",
                "signingKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                },
                "tmplSignature": "e4PtV0m3Lsn14J82Zjna55MO+TBTufzT2or7Th5lgWGpuYSFc8XhRg6aW3iHpCqCJKcKQ6YWy1YzcFjsrWJ4e+trQ74nqa8CqLXLs6uzaqmxkaRQgdUClUACjXIOx9GHOJGaRhvldlilfjWb20h/ogME8v0t36ZA3oykeAnZ6HmZzx0L/hm1Q8bkwN6RTRFh7uPkH2TRyjUUqC1bDTbl3Cf738hhh9pjRgyc9iOO+jBb2zm1QSyJ8q4MD2f+dGi45Uc90Cj0yOMfpWg73AQLKsvHPzGxrH4SFoeYMUArJuRCFE42WpiCREvnEVgob7lFmAGlIlDToHS0Jyca2wZ4Uw==",
                "totalSigningStatus": "one-cert-signed",
                "verificationStatus": "signature-verified",
            },
            {
                "actionsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.microsoft_exchange_2010/actions?ver=14.1.2.1",
                },
                "fullPath": "/Common/f5.microsoft_exchange_2010",
                "generation": 1,
                "ignoreVerification": "false",
                "kind": "tm:sys:application:template:templatestate",
                "name": "f5.microsoft_exchange_2010",
                "partition": "Common",
                "requiresBigipVersionMax": "12.1.0",
                "requiresBigipVersionMin": "11.4.0",
                "requiresModules": ["ltm"],
                "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.microsoft_exchange_2010?ver=14.1.2.1",
                "signingKey": "/Common/f5-irule",
                "signingKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                },
                "tmplSignature": "D/3qwsglMZRpuePJecPX2OALA0p2ISkosUtWZ6q/zo6LDjpCZ0rImIPIABPnfnXrGRxrGO6McAH/ZNGwrOop9GSDIB9lUTbUgT/NJvMwq+XRymC+jfOYgxfwkmwZdJDTzEcNt10QoqHWvoq/Li7ARMRle9VskLqi+isQ4fwJl7MyZofOtJRBWeHwRJEoL23ZRRzSZAoDqa/XBCrtAkZ/1VQZx0+HuE4JBkfpoJYC/QUwU8SL8QU/IBDTm/9fJNbbC7HJo6wetdzUj8qluusPQk4CQzL3iQwqFdqrHMta017BP42K7az8XbCA9rWAr+buckOt5w0f2VdBLIR1ZC8vyA==",
                "totalSigningStatus": "one-cert-signed",
                "verificationStatus": "signature-verified",
            },
            {
                "actionsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.microsoft_exchange_owa_2007/actions?ver=14.1.2.1",
                },
                "fullPath": "/Common/f5.microsoft_exchange_owa_2007",
                "generation": 1,
                "ignoreVerification": "false",
                "kind": "tm:sys:application:template:templatestate",
                "name": "f5.microsoft_exchange_owa_2007",
                "partition": "Common",
                "requiresBigipVersionMax": "12.1.0",
                "requiresBigipVersionMin": "11.4.0",
                "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.microsoft_exchange_owa_2007?ver=14.1.2.1",
                "signingKey": "/Common/f5-irule",
                "signingKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                },
                "tmplSignature": "DDfeduX/WmkBpdWZvipn5Dv4vLA6YtUFc7FHy4a6uGR/J802UhG7lsezOKnFKUiJBQaGEEfbDrzn2uTUA9ZLZCNEbD2OzzmbaryetK+ms48mJULDD4FzmJI4gHJYNXDlYFNk5Yw7n0ZTmoqegWt2tM3h3uTaWmz6di1ZgTL+PIzosMTdf6OtAiCbY3hMRihC9NuhIk61i5VK0S6n/JXU5iVVtcHUUIgZBxjsoBEQlR8IZu7jCx62bj39uE5CAO+FndFPpLDVf7fA38cU8o+/3tMDNSz+5dnzDDCqizWHjQxRlku0TcSdMQC9q1VOAXrPYCk/LtmCR/Ku315ONDRw5A==",
                "totalSigningStatus": "one-cert-signed",
                "verificationStatus": "signature-verified",
            },
            {
                "actionsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.microsoft_iis/actions?ver=14.1.2.1",
                },
                "fullPath": "/Common/f5.microsoft_iis",
                "generation": 1,
                "ignoreVerification": "false",
                "kind": "tm:sys:application:template:templatestate",
                "name": "f5.microsoft_iis",
                "partition": "Common",
                "requiresBigipVersionMin": "11.5.0",
                "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.microsoft_iis?ver=14.1.2.1",
                "signingKey": "/Common/f5-irule",
                "signingKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                },
                "tmplSignature": "ggb00Ed3FsVxfoNpxQo47sIcag79+vSQ7e2mUaVZIJzN0pbItuFvXwWaE9lRY8sCmC9lhvVx+tOwTT9qzw4DRKSvRG/69YEtT7F6GhL+8ZdwUiR3KtyAz9+lvFBXW5uAehhFLeW3ofZPDEzUKVhwRJK2DnOz5JyrcyinOczs4echPNhtm7B10PuoOGhTCiEkVnoMpz9f03qOXTjRs0tavQ4+ug+iRVjcCMaDmzS1B/tgfSKbCfrJA+UwCSuEqg+J6ciiRl9al8a3418T90Eg7W2O1qSTwl50E1h81/DbdOIK5pHgJQSYYZ9UoRwM/ppr+JJdUmTFVSgcLv8yjEYh6A==",
                "totalSigningStatus": "one-cert-signed",
                "verificationStatus": "signature-verified",
            },
            {
                "actionsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.microsoft_lync_server_2010/actions?ver=14.1.2.1",
                },
                "fullPath": "/Common/f5.microsoft_lync_server_2010",
                "generation": 1,
                "ignoreVerification": "false",
                "kind": "tm:sys:application:template:templatestate",
                "name": "f5.microsoft_lync_server_2010",
                "partition": "Common",
                "requiresBigipVersionMax": "12.1.0",
                "requiresBigipVersionMin": "11.4.0",
                "requiresModules": ["ltm"],
                "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.microsoft_lync_server_2010?ver=14.1.2.1",
                "signingKey": "/Common/f5-irule",
                "signingKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                },
                "tmplSignature": "OtOpRF3gnlvMuE0vah7rc/cZqr0+9igQqC99ekqjB2qGwFBMYUGIZ/6eTLPvXJf2GAWD+TO0zC6sGGhJOYdoKxff1M74Bp26IF1aSxQaweX+9xqsKMwNJi5X8Ks1yyyi+s7GLBc33Rv5xucMzMw/lIOqqoN+e227A2289VsVNIs1TEfZ5XIcb7AGWq9U9cGgdui283ekyczYks63Ltw/PzEqX/3AJR/f5xQH/IzjHS+W0XdMHl6fZdlK2FB0xgv9EguU+XaGXTUtd6oKFbSN3wDhNPgk8rFFKot8T4BtYwbM5rYLeSRPXMXAjhHZ0FPxWl9l5fRHHB5fISR5f2Lb4A==",
                "totalSigningStatus": "one-cert-signed",
                "verificationStatus": "signature-verified",
            },
            {
                "actionsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.microsoft_ocs_2007_r2/actions?ver=14.1.2.1",
                },
                "fullPath": "/Common/f5.microsoft_ocs_2007_r2",
                "generation": 1,
                "ignoreVerification": "false",
                "kind": "tm:sys:application:template:templatestate",
                "name": "f5.microsoft_ocs_2007_r2",
                "partition": "Common",
                "requiresBigipVersionMax": "12.1.0",
                "requiresBigipVersionMin": "11.4.0",
                "requiresModules": ["ltm"],
                "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.microsoft_ocs_2007_r2?ver=14.1.2.1",
                "signingKey": "/Common/f5-irule",
                "signingKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                },
                "tmplSignature": "cdUTaR/Mud6PPlYTdztpz0tUbTo5PrcBMrx3jIhBvWaI7prJpYhDnQn9RMrZwz7ffRQq59NPblQMiYQEKvVJew5dx1Hkc0gFkRaxqlNtg9lF/wfweO9+Omxwj9oPyoEvAa8soLJQNnUP0CtH3jMXYw1U9tT9ExmFzE8ZuxNQgWywu6dRxZO9mDUcqoPjViROl/tZT7NQsUyVWRgPNXvhvJMPG7KJN5oSH2MU/t9EXxl64t3EECBLyQsG0EZHmeXm7atu+DQD8NyygioR9QiO3qe7esX4GhnLWxYNceRyeQg74EDPghanJQ8OZHMcdboHHHWsOnZ9pKHuLmQgZnJqcw==",
                "totalSigningStatus": "one-cert-signed",
                "verificationStatus": "signature-verified",
            },
            {
                "actionsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.microsoft_sharepoint_2007/actions?ver=14.1.2.1",
                },
                "fullPath": "/Common/f5.microsoft_sharepoint_2007",
                "generation": 1,
                "ignoreVerification": "false",
                "kind": "tm:sys:application:template:templatestate",
                "name": "f5.microsoft_sharepoint_2007",
                "partition": "Common",
                "requiresBigipVersionMax": "12.1.0",
                "requiresBigipVersionMin": "11.4.0",
                "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.microsoft_sharepoint_2007?ver=14.1.2.1",
                "signingKey": "/Common/f5-irule",
                "signingKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                },
                "tmplSignature": "EVlp5nX4Tfa4OwXcmbazbcAsn+UNioe9pJGa92PwE2h4rk+Yj7j9hMmNxDTCgkVu7aBXNU+fERxuOeW92mK2BbdkEos0/HMNOF5cgvjoPxJvoOgKQInCYumH6OQ/0SQCkL46bT0Deullh1/n8VC5RIj+qoqIkvgACLl2syTz0cjfKrCHC5LJXR0Ja6yYhLraPX5+TmoJNoeZhqDGiYAmphkkvG2vT08wl9Kyz0XtgnBbmGPu6VqIpi7I7hthqHbAk8+kDY0khd/sg34kFbki5NtVrudQ9MXLq3c0kmqLoO2gBLCyND8KyHjz8idQSdOxO5Ga/gRTZcil60AufJNG8w==",
                "totalSigningStatus": "one-cert-signed",
                "verificationStatus": "signature-verified",
            },
            {
                "actionsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.microsoft_sharepoint_2010/actions?ver=14.1.2.1",
                },
                "fullPath": "/Common/f5.microsoft_sharepoint_2010",
                "generation": 1,
                "ignoreVerification": "false",
                "kind": "tm:sys:application:template:templatestate",
                "name": "f5.microsoft_sharepoint_2010",
                "partition": "Common",
                "requiresBigipVersionMin": "11.5.0",
                "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.microsoft_sharepoint_2010?ver=14.1.2.1",
                "signingKey": "/Common/f5-irule",
                "signingKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                },
                "tmplSignature": "X3vPcUbwznluKUh++34sC/iOE4SExn58VOgPRw29IWRAJdhwxbVaxZ3dHd0LMMcQ0y32ZwvFML2kl9rW0KflrJ7CkRXBYKM3d8S20E4h1sG6Yk6u+M5eXG+iRJPLUI8fm3TA40xIIKLMrFEOHpVyxvL5em3EY/2QJetfdpjdn/sa1KymE8UZGfEn0PT+kYYatxiiCClDhd4L4aYyml6jhGCx1fauTb1nQo5BDgHx3OMr0LinZkM1y0aKpPnODLty6f/VkMKMylViwhNDLWmuaYpGXFzyuPKCVR8LwRPtgFi+kSlKXnKhoL5S0TSOB1YP4yzdmNX7/PUaVnHek5U+8Q==",
                "totalSigningStatus": "one-cert-signed",
                "verificationStatus": "signature-verified",
            },
            {
                "actionsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.npath/actions?ver=14.1.2.1",
                },
                "fullPath": "/Common/f5.npath",
                "generation": 1,
                "ignoreVerification": "false",
                "kind": "tm:sys:application:template:templatestate",
                "name": "f5.npath",
                "partition": "Common",
                "requiresBigipVersionMin": "11.4.0",
                "requiresModules": ["ltm"],
                "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.npath?ver=14.1.2.1",
                "signingKey": "/Common/f5-irule",
                "signingKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                },
                "tmplSignature": "AXg5YAQ3g1MQumSAyCLZyDrb1WsLV1y1pbNNZBea7m/D7wtnFPyHpltlJlnsIl3/cUqxMcXzEqC5X3RfMdE/RKGFnV4SBDzKUbxIk4+t9jtgTw7PzS2rKkFkA5VIypZ9a2ts5ZqUnAYY2adBDzbVn7fAoqg0MBnVuMn2u6uWt/feR+mkNIraKf+NUkaS27v4YTtDMC11s6Z238uau29upK0QmKgnpj6rgC1iC74W4JkiPrSH4A3AW4b0H1bzBn/GSrRj2nO1mPmIYkmXu9FweStg3yprfbOLaY9nHuVymbDi375ESD+AH+Bq1TmyxYnGCiaWTb+lgRmYIH2Zbzyxiw==",
                "totalSigningStatus": "one-cert-signed",
                "verificationStatus": "signature-verified",
            },
            {
                "actionsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.oracle_as_10g/actions?ver=14.1.2.1",
                },
                "fullPath": "/Common/f5.oracle_as_10g",
                "generation": 1,
                "ignoreVerification": "false",
                "kind": "tm:sys:application:template:templatestate",
                "name": "f5.oracle_as_10g",
                "partition": "Common",
                "requiresBigipVersionMax": "13.1.0",
                "requiresBigipVersionMin": "11.4.0",
                "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.oracle_as_10g?ver=14.1.2.1",
                "signingKey": "/Common/f5-irule",
                "signingKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                },
                "tmplSignature": "grKFltviMvdeUsPg6UCANDSC20YxUZzzg3phYBMjrcZtOTcg+tcsRJVQ0wq94w2twhoj/0DNppm3Qz2+wj8ClROiclWvrtWV/DjxBeUd0LFMRf7p/6vJtgx8+4IHe/O+AaE3On0JdMLBCfdFp3g7cUhGZAAmr8M6DdKAm7SComHsZs4WhS5kCmNgJWTZvkmk2PgzDdxLE5D6iGQ8QAW+6IHpVhQ9S46oqHpHGnNQye1x7Zb968UcPCEQDB1l+II99VHyBp1B9Lrxr4CbI7z45HtHsvfDtDyCXF55ccqIXQ2lOrGlAYfWedDSwDria45w3ZxQ3+Ndd5bhQhBkVWEbqg==",
                "totalSigningStatus": "one-cert-signed",
                "verificationStatus": "signature-verified",
            },
            {
                "actionsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.oracle_ebs/actions?ver=14.1.2.1",
                },
                "fullPath": "/Common/f5.oracle_ebs",
                "generation": 1,
                "ignoreVerification": "false",
                "kind": "tm:sys:application:template:templatestate",
                "name": "f5.oracle_ebs",
                "partition": "Common",
                "requiresBigipVersionMax": "13.1.0",
                "requiresBigipVersionMin": "11.5.0",
                "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.oracle_ebs?ver=14.1.2.1",
                "signingKey": "/Common/f5-irule",
                "signingKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                },
                "tmplSignature": "BL+tWDogX6+vLfyganxKylpAzDipUSsNHpFCLrnKkSnmUSMiThUWVq2/EmQN8zwRrip66o8PW8ooIfdNz3P8jOa5MOwsGK7FPpgjCFBcALWkvqSKJB1A2yt+QNJbRp7BCAz7Uf4wUae9BXoIcg5Il3xBj82QDlpswZtEzfQcI32uuIpLTy0UtqEtQlVV5zRdT16IaBpMEl6w237zx2Jd170JTTjFmez4IHH/gG1HFeSvfHkFSRvnKIag9EUC26FU4O8KurLE/VK/wMNE+hjrbuzE6aiy5DfLsKEdp48UrNnY0x2ORgjJkE0XBKSQattkWafbU6Ce64XqDzgtN9QGCg==",
                "totalSigningStatus": "one-cert-signed",
                "verificationStatus": "signature-verified",
            },
            {
                "actionsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.peoplesoft_9/actions?ver=14.1.2.1",
                },
                "fullPath": "/Common/f5.peoplesoft_9",
                "generation": 1,
                "ignoreVerification": "false",
                "kind": "tm:sys:application:template:templatestate",
                "name": "f5.peoplesoft_9",
                "partition": "Common",
                "requiresBigipVersionMax": "13.1.0",
                "requiresBigipVersionMin": "11.5.0",
                "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.peoplesoft_9?ver=14.1.2.1",
                "signingKey": "/Common/f5-irule",
                "signingKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                },
                "tmplSignature": "aELtdJPG5rJS1ONgWVE6+x+FWbkw5WoaDU3f8LF0j9a0XXXZDEgHbvKLaQrueeBv3bhZ0xQiNdEcmiUC5f1sBZ7CdtQpxd7PKegIpIRXZlWZZHykjjzuh2D8zhQP0lQQkO6t/FOtAXirSs+0Ob93qnKe8in3mue/dK6XeuhRl28Ov6BprXbQhUK3W76Ommt1hINDSXY1vC4x7viIfK/yyTIPSWNd7jMk83LPwkQop5iCczdh3IbQ5d8L998epwCmvwuWFCS1d3yBCp3SIYOR0rQNk5naWSOE7M6L0wQtFbrZsn1+LxUqj3Df/gQoSa5Ahl6JUjfUriUy4H/QfRgfPg==",
                "totalSigningStatus": "one-cert-signed",
                "verificationStatus": "signature-verified",
            },
            {
                "actionsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.radius/actions?ver=14.1.2.1",
                },
                "fullPath": "/Common/f5.radius",
                "generation": 1,
                "ignoreVerification": "false",
                "kind": "tm:sys:application:template:templatestate",
                "name": "f5.radius",
                "partition": "Common",
                "requiresBigipVersionMin": "11.4.0",
                "requiresModules": ["ltm"],
                "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.radius?ver=14.1.2.1",
                "signingKey": "/Common/f5-irule",
                "signingKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                },
                "tmplSignature": "AvmOJD8Vh1r/jujEgusCmxNRcYFwfvaS1uO0MMlFqwtFCxl6Mpd+NUdtPGI7BYON5HKFr8e64MVMlxhfXNh1SyFK3fJueZ6hqPc1OOHMx1AiU+/VsozwciayF2nG0A5KUHEslY52MMQf9xiUvuDRVZTHrOU025E+QxtObDTlbrp03mW00dUflDP0W1qyvAruL73DXeSADMZLpo9Cm7r2mYA/RgKT8DVXfItwYSFBMyd1YR5AJHYIxoOc1WFZIyZ//AdktHRE5eaEozIQZ3bB4Re2qU8aoabhQB0SexDvaYOrY7AznxQN4MY4QAFY/XqyO/1RuY+svnWE/lbrqkMZWw==",
                "totalSigningStatus": "one-cert-signed",
                "verificationStatus": "signature-verified",
            },
            {
                "actionsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.replication/actions?ver=14.1.2.1",
                },
                "fullPath": "/Common/f5.replication",
                "generation": 1,
                "ignoreVerification": "false",
                "kind": "tm:sys:application:template:templatestate",
                "name": "f5.replication",
                "partition": "Common",
                "prerequisiteErrors": "Error: am is not provisioned/enabled.",
                "requiresBigipVersionMax": "13.1.0",
                "requiresBigipVersionMin": "11.4.0",
                "requiresModules": ["am"],
                "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.replication?ver=14.1.2.1",
                "signingKey": "/Common/f5-irule",
                "signingKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                },
                "tmplSignature": "TNzZ2xvZTm3Jqu+1+ZuCWq0wlg3awZ7BkKhR9n+RV7DzE3yfJ1A66QPt64AoJ1fXsSS2tqMOceuOG8+odpH/1MVTU23EABE+6F75xDdi4rbzNE2oaG5ntU2+EUkqmz2hf4SKrIwaM0oU7JCMZBLYMj1nyxmikVWhpVIWF7f3MaYVYXpTGWDhv+yFk8VvuxYTQQSgWhMuqZAqqq0fBgSAd+lLxTB+8YyQMPpHQ2ZC31vKus63u0Pj3HIftmt9zKTBuh0KReHF4g4ZIQJ1VUrojI0UKR/D8+7L3zkBA2aGdWUeJu1mcxqPn8xzITRDffkWQLIc0C0wjNCgqS9uELM+xg==",
                "totalSigningStatus": "one-cert-signed",
                "verificationStatus": "signature-verified",
            },
            {
                "actionsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.sap_enterprise_portal/actions?ver=14.1.2.1",
                },
                "fullPath": "/Common/f5.sap_enterprise_portal",
                "generation": 1,
                "ignoreVerification": "false",
                "kind": "tm:sys:application:template:templatestate",
                "name": "f5.sap_enterprise_portal",
                "partition": "Common",
                "requiresBigipVersionMax": "13.1.0",
                "requiresBigipVersionMin": "11.5.0",
                "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.sap_enterprise_portal?ver=14.1.2.1",
                "signingKey": "/Common/f5-irule",
                "signingKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                },
                "tmplSignature": "EdbiChNEy0qmOq1cgic+TXNP0C/X4kQw/qXqQ+pKBudxQxVjakkl+uD2yp4vYx9H0+Qw7bD9LIyt6c9X1Cd2ZZVBuEZx/mmidYuN9gRroU5G6HxwaHkVBmI1/EGxC1/iotlaStxpzitq81znkXTDjosAvY8W4xL8Dl55una9GjmuZX8yMTfKfwEm+qc4zbp88i5+Wnp19Khem3E2sIQChNiZDfR7DjKotPuDDr7nmN1dr2bBJhPGRtv8WZwzfrgghwNxIYzIw8y3zrIQpeJAkmCBjA+KhxQYKxaAHzXx3EUrjNZlcxi8RRdliD+cZtWCjCHCl/Nx6xRJIMyUJZTUsw==",
                "totalSigningStatus": "one-cert-signed",
                "verificationStatus": "signature-verified",
            },
            {
                "actionsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.sap_erp/actions?ver=14.1.2.1",
                },
                "fullPath": "/Common/f5.sap_erp",
                "generation": 1,
                "ignoreVerification": "false",
                "kind": "tm:sys:application:template:templatestate",
                "name": "f5.sap_erp",
                "partition": "Common",
                "requiresBigipVersionMax": "13.1.0",
                "requiresBigipVersionMin": "11.5.0",
                "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.sap_erp?ver=14.1.2.1",
                "signingKey": "/Common/f5-irule",
                "signingKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                },
                "tmplSignature": "a+268FXW1grdVcND6t6wqI5WpY7KW0iasypriPWOrEYsnJQ96g1n1K6ynxUoBs0/P23881tMVefUK4jyf4wFXlgE8OzGnjQCmqMuRoRkQ0U6JWPKMbQIFAasCkJCR8kBBKcmnUmA59vw8brMR7MRaUITMWuyrmAZtri5EMK5ljcHSWvbE7hdLPK3K+rZAI5xpzT3e30oQvAd0T3g/D9pPzhE4VqInXHbiTh0wvM2Nxh8SqepNTSGkkyr99xn21xklRtkiCHH1QAB8oPvvWJ7Tm76AyvtK7RGBwwc3dYDDD/4K+BH8nzN3nZk55cjAKZP7HZ1Bh+A9ijzjZ67vTjwHg==",
                "totalSigningStatus": "one-cert-signed",
                "verificationStatus": "signature-verified",
            },
            {
                "actionsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.vmware_view/actions?ver=14.1.2.1",
                },
                "fullPath": "/Common/f5.vmware_view",
                "generation": 1,
                "ignoreVerification": "false",
                "kind": "tm:sys:application:template:templatestate",
                "name": "f5.vmware_view",
                "partition": "Common",
                "requiresBigipVersionMax": "12.1.0",
                "requiresBigipVersionMin": "11.4.0",
                "requiresModules": ["ltm"],
                "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.vmware_view?ver=14.1.2.1",
                "signingKey": "/Common/f5-irule",
                "signingKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                },
                "tmplSignature": "Vgj7OLs9HdTygNJAb0eZKVSRyPaoWnclZXeBTEttpix806cW0rCu0bnJ8P1wjI3SBweQ3ButZvpz7pfp76DJvVg6aeLCaYbPrVWwAUyH8EyH4+J7PWpc08a+38+s1u9F5IUHU4uMiwxmXUaS4ao3XkB0AmA4nkwKvqyHC2s2BSHm9viqO58dglfrAClYNUvnP9FDVcDHiOw/5lNOhYU78Z1d56bhwcl3GdpbPpnT+6i7A+253kZ4Vj0xDqCpxTR47hcLVZO89yVdHdx7C/VuaNhHWLyTluVRohIIrG7PN3i5b+M+n91e/9ageQX1Z7DVlDQlpjS63DzUdPQVK+jjAQ==",
                "totalSigningStatus": "one-cert-signed",
                "verificationStatus": "signature-verified",
            },
            {
                "actionsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.vmware_vmotion/actions?ver=14.1.2.1",
                },
                "fullPath": "/Common/f5.vmware_vmotion",
                "generation": 1,
                "ignoreVerification": "false",
                "kind": "tm:sys:application:template:templatestate",
                "name": "f5.vmware_vmotion",
                "partition": "Common",
                "prerequisiteErrors": "Error: am is not provisioned/enabled.",
                "requiresBigipVersionMax": "13.1.0",
                "requiresBigipVersionMin": "11.4.0",
                "requiresModules": ["am"],
                "selfLink": "https://localhost/mgmt/tm/sys/application/template/~Common~f5.vmware_vmotion?ver=14.1.2.1",
                "signingKey": "/Common/f5-irule",
                "signingKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                },
                "tmplSignature": "QxUEiGk06+t867VXiWmORxaqIXzz4+B5CAcpKe0pjwcDpRuYUBmwLojHznYaEvz1pout67LyX9OOKNLenrB5Fky3ZyFZbuBBLElgKPWDgzOfUTncRQFIH4o+NARGKVcSA+F2mBjWBqJ8oqOt1XbqPTIq31ciDDA5bXsH9J7V3wqvTqg+oHcPhDpFMXNi/BHE5EBFcfD2Y4fH1zBFT/KtCIYku7hIp0lBaNaMNRM568REgHLIasKMoHlloJxr2TFBhbMR71QMqT5G/T8L2BDBcHV/57EMsrwJFPgmR2h29kv6E6cOxrYV4l1cisFQXkJwOZtfcoGFjYzR5oToW+YRtg==",
                "totalSigningStatus": "one-cert-signed",
                "verificationStatus": "signature-verified",
            },
        ],
        "kind": "tm:sys:application:template:templatecollectionstate",
        "selfLink": "https://localhost/mgmt/tm/sys/application/template?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysApplicationTemplate(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysApplicationTemplate(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
