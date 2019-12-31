# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_applicationapl_script
from genie.libs.parser.bigip.get_sys_applicationapl_script import (
    SysApplicationAplscript,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/application/apl-script'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:application:apl-script:apl-scriptcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/sys/application/apl-script?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:sys:application:apl-script:apl-scriptstate",
                    "name": "f5.apl_common",
                    "partition": "Common",
                    "fullPath": "/Common/f5.apl_common",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/application/apl-script/~Common~f5.apl_common?ver=14.1.2.1",
                    "apiAnonymous": 'script {\ndefine choice yesno default "Yes" display "small" {\n        "Yes" => "Yes",\n        "No" => "No"\n    }\n    define choice noyes default "No" display "small" {\n        "No" => "No",\n        "Yes" => "Yes"\n    }\n\n    define section ssl_section {\n        noyes offload_ssl\n        optional ( offload_ssl == "Yes" ) {\n            choice cert default "/Common/default.crt" display "xxlarge" tcl { tmsh::run_proc f5.app_utils:get_ssl_certs }\n            choice key default "/Common/default.key" display "xxlarge" tcl { tmsh::run_proc f5.app_utils:get_ssl_keys }\n        }\n    }\n\n    define choice lb_method display "xxlarge" tcl {\n        if { [string first ltm_lb_least_conn [tmsh::show sys license detail]] != -1 } {\n            set choices "Least Connections (member)\\tleast-connections-member\\nLeast Connections (node)\\tleast-connections-node\\nLeast Sessions\\tleast-sessions\\nDynamic Ratio (member)\\tdynamic-ratio-member\\nDynamic Ratio (node)\\tdynamic-ratio-node\\nFastest (application)\\tfastest-app-response\\nFastest (node)\\tfastest-node\\nObserved (member)\\tobserved-member\\nObserved (node)\\tobserved-node\\nPredictive (member)\\tpredictive-member\\nPredictive (node)\\tpredictive-node\\nRound Robin\\tround-robin\\nRatio (member)\\tratio-member\\nRatio (node)\\tratio-node\\nRatio (session)\\tratio-session\\nRatio Least Connections (member)\\tratio-least-connections-member\\nRatio Least Connections (node)\\tratio-least-connections-node\\nWeighted Least Connections (member)\\tweighted-least-connections-member"\n        } else {\n            set choices "Round Robin\\tround-robin\\nRatio (member)\\tratio-member\\nRatio (node)\\tratio-node"\n        }\n        return $choices\n    }\n\n    define choice language_choice default "utf-8" display "xxlarge" {\n        "Arabic (iso-8859-6)" => "iso-8859-6",\n        "Baltic (iso-8859-4)" => "iso-8859-4",\n        "Baltic (iso-8859-13)" => "iso-8859-13",\n        "Baltic (windows-1257)" => "windows-1257",\n        "Central European (iso-8859-2)" => "iso-8859-2",\n        "Central European (windows-1250)" => "windows-1250",\n        "Chinese (big5)" => "big5",\n        "Chinese (gb2312)" => "gb2312",\n        "Chinese (gbk)" => "gbk",\n        "Chinese (gb18030)" => "gb18030",\n        "Cyrillic (iso-8859-5)" => "iso-8859-5",\n        "Cyrillic (koi8-r)" => "koi8-r",\n        "Cyrillic (windows-1251)" => "windows-1251",\n        "Greek (iso-8859-7)" => "iso-8859-7",\n        "Greek (windows-1253)" => "windows-1253",\n        "Hebrew (iso-8859-8)" => "iso-8859-8",\n        "Hebrew (windows-1255)" => "windows-1255",\n        "Japanese (euc-jp)" => "euc-jp",\n        "Japanese (shift_jis)" => "shift_jis",\n        "Korean (euc-kr)" => "euc-kr",\n        "Nordic (iso-8859-10)" => "iso-8859-10",\n        "Romanian (iso-8859-16)" => "iso-8859-16",\n        "South European (iso-8859-3)" => "iso-8859-3",\n        "Thai (windows-874)" => "windows-874",\n        "Turkish (iso-8859-9)" => "iso-8859-9",\n        "Unicode (utf-8)" => "utf-8",\n        "Western European (iso-8859-1)" => "iso-8859-1",\n        "Western European (iso-8859-15)" => "iso-8859-15",\n        "Western European (windows-1252)" => "windows-1252"\n    }\n}\n',
                    "aplSignature": "WuZzpmWHZZgUf6ZHmqUoDPoqkjnx9nXjMQxfeLDsgrt0aD0sd07kVIUY5YF26RyzEnCABzqqffEoBEJnvFk9bXDzg+vMLRTML5TqqwX1AYWb2bZryGwgPoti4eimCqlJKNp7UxTrvY2s1yf8YTzQI0wlAAEUaN0Nh+gNTovphVPmxwe9HKfoVpxHMKcJzxIjvdyMATnfoCJ0vJR74lN8dnyr5WJdjAZnLK+kAZJIaJSzJ6CUavLsftnBdmTifuMkEgkzaebnFzxhyBn4nr74ktqppO8/FEtXXGu2GaI6Cmpa3bWGTnZpBfuiPGfAO+3QR9mlCFEhE0atd8bAu6XF0Q==",
                    "ignoreVerification": "false",
                    "signingKey": "/Common/f5-irule",
                    "signingKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                    },
                    "totalSigningStatus": "one-cert-signed",
                    "verificationStatus": "signature-verified",
                }
            ],
        }


class test_get_sys_applicationapl_script(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "apiAnonymous": "script {\n"
                'define choice yesno default "Yes" display "small" '
                "{\n"
                '        "Yes" => "Yes",\n'
                '        "No" => "No"\n'
                "    }\n"
                '    define choice noyes default "No" display '
                '"small" {\n'
                '        "No" => "No",\n'
                '        "Yes" => "Yes"\n'
                "    }\n"
                "\n"
                "    define section ssl_section {\n"
                "        noyes offload_ssl\n"
                '        optional ( offload_ssl == "Yes" ) {\n'
                "            choice cert default "
                '"/Common/default.crt" display "xxlarge" tcl { '
                "tmsh::run_proc f5.app_utils:get_ssl_certs }\n"
                "            choice key default "
                '"/Common/default.key" display "xxlarge" tcl { '
                "tmsh::run_proc f5.app_utils:get_ssl_keys }\n"
                "        }\n"
                "    }\n"
                "\n"
                '    define choice lb_method display "xxlarge" tcl '
                "{\n"
                "        if { [string first ltm_lb_least_conn "
                "[tmsh::show sys license detail]] != -1 } {\n"
                '            set choices "Least Connections '
                "(member)\\tleast-connections-member\\nLeast "
                "Connections "
                "(node)\\tleast-connections-node\\nLeast "
                "Sessions\\tleast-sessions\\nDynamic Ratio "
                "(member)\\tdynamic-ratio-member\\nDynamic Ratio "
                "(node)\\tdynamic-ratio-node\\nFastest "
                "(application)\\tfastest-app-response\\nFastest "
                "(node)\\tfastest-node\\nObserved "
                "(member)\\tobserved-member\\nObserved "
                "(node)\\tobserved-node\\nPredictive "
                "(member)\\tpredictive-member\\nPredictive "
                "(node)\\tpredictive-node\\nRound "
                "Robin\\tround-robin\\nRatio "
                "(member)\\tratio-member\\nRatio "
                "(node)\\tratio-node\\nRatio "
                "(session)\\tratio-session\\nRatio Least "
                "Connections "
                "(member)\\tratio-least-connections-member\\nRatio "
                "Least Connections "
                "(node)\\tratio-least-connections-node\\nWeighted "
                "Least Connections "
                '(member)\\tweighted-least-connections-member"\n'
                "        } else {\n"
                '            set choices "Round '
                "Robin\\tround-robin\\nRatio "
                "(member)\\tratio-member\\nRatio "
                '(node)\\tratio-node"\n'
                "        }\n"
                "        return $choices\n"
                "    }\n"
                "\n"
                '    define choice language_choice default "utf-8" '
                'display "xxlarge" {\n'
                '        "Arabic (iso-8859-6)" => "iso-8859-6",\n'
                '        "Baltic (iso-8859-4)" => "iso-8859-4",\n'
                '        "Baltic (iso-8859-13)" => "iso-8859-13",\n'
                '        "Baltic (windows-1257)" => '
                '"windows-1257",\n'
                '        "Central European (iso-8859-2)" => '
                '"iso-8859-2",\n'
                '        "Central European (windows-1250)" => '
                '"windows-1250",\n'
                '        "Chinese (big5)" => "big5",\n'
                '        "Chinese (gb2312)" => "gb2312",\n'
                '        "Chinese (gbk)" => "gbk",\n'
                '        "Chinese (gb18030)" => "gb18030",\n'
                '        "Cyrillic (iso-8859-5)" => "iso-8859-5",\n'
                '        "Cyrillic (koi8-r)" => "koi8-r",\n'
                '        "Cyrillic (windows-1251)" => '
                '"windows-1251",\n'
                '        "Greek (iso-8859-7)" => "iso-8859-7",\n'
                '        "Greek (windows-1253)" => '
                '"windows-1253",\n'
                '        "Hebrew (iso-8859-8)" => "iso-8859-8",\n'
                '        "Hebrew (windows-1255)" => '
                '"windows-1255",\n'
                '        "Japanese (euc-jp)" => "euc-jp",\n'
                '        "Japanese (shift_jis)" => "shift_jis",\n'
                '        "Korean (euc-kr)" => "euc-kr",\n'
                '        "Nordic (iso-8859-10)" => "iso-8859-10",\n'
                '        "Romanian (iso-8859-16)" => '
                '"iso-8859-16",\n'
                '        "South European (iso-8859-3)" => '
                '"iso-8859-3",\n'
                '        "Thai (windows-874)" => "windows-874",\n'
                '        "Turkish (iso-8859-9)" => "iso-8859-9",\n'
                '        "Unicode (utf-8)" => "utf-8",\n'
                '        "Western European (iso-8859-1)" => '
                '"iso-8859-1",\n'
                '        "Western European (iso-8859-15)" => '
                '"iso-8859-15",\n'
                '        "Western European (windows-1252)" => '
                '"windows-1252"\n'
                "    }\n"
                "}\n",
                "aplSignature": "WuZzpmWHZZgUf6ZHmqUoDPoqkjnx9nXjMQxfeLDsgrt0aD0sd07kVIUY5YF26RyzEnCABzqqffEoBEJnvFk9bXDzg+vMLRTML5TqqwX1AYWb2bZryGwgPoti4eimCqlJKNp7UxTrvY2s1yf8YTzQI0wlAAEUaN0Nh+gNTovphVPmxwe9HKfoVpxHMKcJzxIjvdyMATnfoCJ0vJR74lN8dnyr5WJdjAZnLK+kAZJIaJSzJ6CUavLsftnBdmTifuMkEgkzaebnFzxhyBn4nr74ktqppO8/FEtXXGu2GaI6Cmpa3bWGTnZpBfuiPGfAO+3QR9mlCFEhE0atd8bAu6XF0Q==",
                "fullPath": "/Common/f5.apl_common",
                "generation": 1,
                "ignoreVerification": "false",
                "kind": "tm:sys:application:apl-script:apl-scriptstate",
                "name": "f5.apl_common",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/sys/application/apl-script/~Common~f5.apl_common?ver=14.1.2.1",
                "signingKey": "/Common/f5-irule",
                "signingKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5-irule?ver=14.1.2.1"
                },
                "totalSigningStatus": "one-cert-signed",
                "verificationStatus": "signature-verified",
            }
        ],
        "kind": "tm:sys:application:apl-script:apl-scriptcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/sys/application/apl-script?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysApplicationAplscript(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysApplicationAplscript(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
