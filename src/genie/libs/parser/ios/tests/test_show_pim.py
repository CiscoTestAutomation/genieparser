# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from genie.libs.parser.ios.show_pim import ShowIpv6PimInterface,\
                                  ShowIpPimInterfaceDetail,\
                                  ShowIpPimInterface, \
                                  ShowIpv6PimBsrCandidateRp, \
                                  ShowIpPimRpMapping, \
                                  ShowIpv6PimBsrElection, \
                                  ShowIpPimBsrRouter, \
                                  ShowIpPimNeighbor, \
                                  ShowIpv6PimNeighbor, \
                                  ShowIpv6PimNeighborDetail, \
                                  ShowIpPimInterfaceDf

from genie.libs.parser.iosxe.tests.test_show_pim import test_show_ipv6_pim_interface as test_show_ipv6_pim_interface_iosxe,\
                                                        test_show_ip_pim_interface as test_show_ip_pim_interface_iosxe,\
                                                        test_show_ipv6_pim_bsr_election as test_show_ipv6_pim_bsr_election_iosxe,\
                                                        test_show_ipv6_pim_bsr_candidate_rp as test_show_ipv6_pim_bsr_candidate_rp_iosxe,\
                                                        test_show_ip_pim_rp_mapping as test_show_ip_pim_rp_mapping_iosxe,\
                                                        test_show_ip_pim_bsr_router as test_show_ip_pim_bsr_router_iosxe,\
                                                        test_show_ip_pim_interface_detail as test_show_ip_pim_interface_detail_iosxe,\
                                                        test_show_ip_pim_neighbor as test_show_ip_pim_neighbor_iosxe,\
                                                        test_show_ipv6_pim_neighbor_detail as test_show_ipv6_pim_neighbor_detail_iosxe,\
                                                        test_show_ipv6_pim_neighbor as test_show_ipv6_pim_neighbor_iosxe,\
                                                        test_show_ip_pim_interface_df as test_show_ip_pim_interface_df_iosxe
# ============================================
# Parser for 'show ipv6 pim interface'
# Parser for 'show ipv6 pim vrf xxx interface'
# ============================================
class test_show_ipv6_pim_interface(test_show_ipv6_pim_interface_iosxe):

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpv6PimInterface(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_vrf_default(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6PimInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_vrf_non_default(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowIpv6PimInterface(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output,self.golden_parsed_output2)

# ============================================
# Parser for 'show ip pim interface'
# Parser for 'show ip pim vrf xxx interface'
# ============================================
class test_show_ip_pim_interface(test_show_ip_pim_interface_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpPimInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_mapping_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_interface_1)
        obj = ShowIpPimInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_interface_1)

    def test_golden_mapping_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_interface_2)
        obj = ShowIpPimInterface(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output_interface_2)

# ============================================
# Parser for 'show ipv6 pim bsr election'
# Parser for 'show ipv6 pim vrf xxx bsr election'
# ============================================
class test_show_ipv6_pim_bsr_election(test_show_ipv6_pim_bsr_election_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6PimBsrElection(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_mapping_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_bsr_elec_1)
        obj = ShowIpv6PimBsrElection(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output_bsr_elec_1)

    def test_golden_mapping_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_bsr_elec_2)
        obj = ShowIpv6PimBsrElection(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_elec_2)

# ============================================
# Parser for 'show ipv6 pim candidate-rp'
# Parser for 'show ipv6 pim vrf xxx candidate-rp'
# ============================================
class test_show_ipv6_pim_bsr_candidate_rp(test_show_ipv6_pim_bsr_candidate_rp_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6PimBsrCandidateRp(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_candidate_rp_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_bsr_candidate_1)
        obj = ShowIpv6PimBsrCandidateRp(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output_bsr_candidate_1)

    def test_golden_candidate_rp_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_bsr_candidate_2)
        obj = ShowIpv6PimBsrCandidateRp(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_candidate_2)

    def test_golden_candidate_rp_3(self):
        self.device = Mock(**self.golden_output_bsr_candidate_3)
        obj = ShowIpv6PimBsrCandidateRp(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

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


# ============================================
# Parser for 'show ip pim bsr-router'
# Parser for 'show ip pim vrf xxx bsr-router'
# ============================================
class test_show_ip_pim_bsr_router(test_show_ip_pim_bsr_router_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpPimBsrRouter(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_bsr_router_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_bsr_1)
        obj = ShowIpPimBsrRouter(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output_bsr_1)

    def test_golden_bsr_router_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_bsr_2)
        obj = ShowIpPimBsrRouter(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_bsr_2)

    def test_golden_bsr_router_3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_bsr_3)
        obj = ShowIpPimBsrRouter(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_bsr_3)

    def test_golden_bsr_router_4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_bsr_4)
        obj = ShowIpPimBsrRouter(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output_bsr_4)

# ============================================
# unit test for 'show ip pim mapping'
# unit test for 'show ip pim vrf xxx mapping'
# ============================================
class test_show_ip_pim_rp_mapping(test_show_ip_pim_rp_mapping_iosxe):

    def test_empty_1(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpPimRpMapping(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_mapping_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_mapping_1)
        obj = ShowIpPimRpMapping(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_mapping_1)

    def test_golden_mapping_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_mapping_2)
        obj = ShowIpPimRpMapping(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output,self.golden_parsed_output_mapping_2)

# =============================================================
# parser for : show ip pim interface detail
# parser for : show ip pim vrf <vrf_name> interface detail
# =============================================================

class test_show_ip_pim_interface_detail(test_show_ip_pim_interface_detail_iosxe):

    def test_empty_detail(self):
        self.device = Mock(**self.empty_output_detail)
        obj = ShowIpPimInterfaceDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


    def test_golden_detail_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_intf_detail_1)
        obj = ShowIpPimInterfaceDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_intf_detail_1)

    def test_golden_intf_detail_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_intf_detail_2)
        obj = ShowIpPimInterfaceDetail(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output,self.golden_parsed_output_intf_detail_2)


# ============================================
# Parser for 'show ip pim neighbor'
# Parser for 'show ip pim vrf xxx neighborrrr'
# ============================================
class test_show_ip_pim_neighbor(test_show_ip_pim_neighbor_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpPimNeighbor(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_default_vrf(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpPimNeighbor(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.parsed_output)


# ============================================
# Parser for 'show ipv6 pim neighbor'
# Parser for 'show ipv6 pim vrf xxx neighbor'
# ============================================
class test_show_ipv6_pim_neighbor(test_show_ipv6_pim_neighbor_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6PimNeighbor(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_default_vrf(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6PimNeighbor(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.parsed_output)


# ===================================================
# Parser for 'show ipv6 pim neighbor detail'
# Parser for 'show ipv6 pim vrf xxx neighbor detail'
# ====================================================
class test_show_ipv6_pim_neighbor_detail(test_show_ipv6_pim_neighbor_detail_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6PimNeighborDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_default_vrf(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6PimNeighborDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.parsed_output)


# ============================================
# Parser for 'show ip pim interface df'
# Parser for 'show ip pim vrf xxx interface df'
# ============================================
class test_show_ip_pim_interface_df(test_show_ip_pim_interface_df_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpPimInterfaceDf(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_default_vrf(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpPimInterfaceDf(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.parsed_output)

    def test_golden_vrf(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpPimInterfaceDf(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.parsed_output_1)

if __name__ == '__main__':
    unittest.main()