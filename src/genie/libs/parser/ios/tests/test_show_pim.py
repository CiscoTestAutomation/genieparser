# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from genie.libs.parser.ios.show_pim import ShowIpv6PimBsrCandidateRp


class test_show_ipv6_pim_bsr_candidate_rp(unittest.TestCase):
    golden_output_ios = {'execute.return_value': '''
            Device# show ipv6 pim bsr candidate-rp
            PIMv2 C-RP information
                Candidate RP: 2001:db8:100::1:1:3
                  All Learnt Scoped Zones, Priority 192, Holdtime 150
                  Advertisement interval 60 seconds
                  Next advertisement in 00:00:33
            '''}

    golden_parsed_output_candidate_ios = {
        "vrf": {
            "default": {
                "address_family": {
                    "ipv6": {
                        "rp": {
                            "bsr": {
                                "rp_candidate_next_advertisement": "00:00:33",
                                "2001:db8:100::1:1:3": {
                                    "holdtime": 150,
                                    "priority": 192,
                                    "interval": 60,
                                    "scope": "All Learnt Scoped Zones",
                                    "address": "2001:db8:100::1:1:3"
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    def test_golden_candidate_rp_4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_ios)
        obj = ShowIpv6PimBsrCandidateRp(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_candidate_ios)


if __name__ == '__main__':
    unittest.main()