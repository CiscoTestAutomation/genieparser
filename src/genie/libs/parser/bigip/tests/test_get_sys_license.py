# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_license
from genie.libs.parser.bigip.get_sys_license import SysLicense

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/license'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:license:licensestats",
            "selfLink": "https://localhost/mgmt/tm/sys/license?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/license/0": {
                    "nestedStats": {
                        "entries": {
                            "licensedOnDate": {"description": "2019/10/10"},
                            "licensedVersion": {"description": "14.1.2"},
                            "platformId": {"description": "Z100"},
                            "registrationKey": {
                                "description": "IYMGF-MMRUK-NDXCX-CWRKR-AAMNTPS"
                            },
                            "serviceCheckDate": {"description": "2019/09/25"},
                            "https://localhost/mgmt/tm/sys/license/0/active-modules": {
                                "nestedStats": {
                                    "entries": {
                                        "https://localhost/mgmt/tm/sys/license/0/active-modules/%22BIG-IP,%20VE,%20LAB%22": {
                                            "nestedStats": {
                                                "entries": {
                                                    "featureModules": {
                                                        "description": '{ "Rate Shaping" "External Interface and Network HSM, VE" "BIG-IP VE, Multicast Routing" "Routing Bundle, VE" "ASM, VE" "SSL, VE" "DNS VE Lab  (10K QPS)" "Max Compression, VE" "Advanced Protocols, VE" "SSL Orchestrator, VE" "Advanced Web Application Firewall, VE Lab" "APM, Lab, VE" "AFM, VE (LAB ONLY - NO ROUTING)" "DNSSEC" "VE, Carrier Grade NAT (AFM ONLY)" "PSM, VE" }'
                                                    },
                                                    "key": {
                                                        "description": "GSMORBH-FRIQHYL"
                                                    },
                                                }
                                            }
                                        }
                                    }
                                }
                            },
                        }
                    }
                }
            },
        }


class test_get_sys_license(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "entries": {
            "https://localhost/mgmt/tm/sys/license/0": {
                "nestedStats": {
                    "entries": {
                        "https://localhost/mgmt/tm/sys/license/0/active-modules": {
                            "nestedStats": {
                                "entries": {
                                    "https://localhost/mgmt/tm/sys/license/0/active-modules/%22BIG-IP,%20VE,%20LAB%22": {
                                        "nestedStats": {
                                            "entries": {
                                                "featureModules": {
                                                    "description": "{ "
                                                    '"Rate '
                                                    'Shaping" '
                                                    '"External '
                                                    "Interface "
                                                    "and "
                                                    "Network "
                                                    "HSM, "
                                                    'VE" '
                                                    '"BIG-IP '
                                                    "VE, "
                                                    "Multicast "
                                                    'Routing" '
                                                    '"Routing '
                                                    "Bundle, "
                                                    'VE" '
                                                    '"ASM, '
                                                    'VE" '
                                                    '"SSL, '
                                                    'VE" '
                                                    '"DNS '
                                                    "VE "
                                                    "Lab  "
                                                    "(10K "
                                                    'QPS)" '
                                                    '"Max '
                                                    "Compression, "
                                                    'VE" '
                                                    '"Advanced '
                                                    "Protocols, "
                                                    'VE" '
                                                    '"SSL '
                                                    "Orchestrator, "
                                                    'VE" '
                                                    '"Advanced '
                                                    "Web "
                                                    "Application "
                                                    "Firewall, "
                                                    "VE "
                                                    'Lab" '
                                                    '"APM, '
                                                    "Lab, "
                                                    'VE" '
                                                    '"AFM, '
                                                    "VE "
                                                    "(LAB "
                                                    "ONLY "
                                                    "- "
                                                    "NO "
                                                    'ROUTING)" '
                                                    '"DNSSEC" '
                                                    '"VE, '
                                                    "Carrier "
                                                    "Grade "
                                                    "NAT "
                                                    "(AFM "
                                                    'ONLY)" '
                                                    '"PSM, '
                                                    'VE" '
                                                    "}"
                                                },
                                                "key": {
                                                    "description": "GSMORBH-FRIQHYL"
                                                },
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "licensedOnDate": {"description": "2019/10/10"},
                        "licensedVersion": {"description": "14.1.2"},
                        "platformId": {"description": "Z100"},
                        "registrationKey": {
                            "description": "IYMGF-MMRUK-NDXCX-CWRKR-AAMNTPS"
                        },
                        "serviceCheckDate": {"description": "2019/09/25"},
                    }
                }
            }
        },
        "kind": "tm:sys:license:licensestats",
        "selfLink": "https://localhost/mgmt/tm/sys/license?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysLicense(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysLicense(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
