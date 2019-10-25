
# Python
import unittest
from unittest.mock import Mock

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

# ios show_bgp
from genie.libs.parser.ios.show_bgp import ShowBgpAllSummary,\
                                           ShowBgpAllClusterIds,\
                                           ShowBgpAllNeighborsAdvertisedRoutes,\
                                           ShowBgpAllNeighborsReceivedRoutes,\
                                           ShowIpBgpTemplatePeerPolicy,\
                                           ShowBgpAllNeighbors,\
                                           ShowIpBgpAllDampeningParameters,\
                                           ShowIpBgpTemplatePeerSession,\
                                           ShowBgpAllNeighborsRoutes,\
                                           ShowBgpAllNeighborsPolicy,\
                                           ShowBgpAll,\
                                           ShowBgpAllDetail, \
                                           ShowBgpSummary, \
                                           ShowIpBgp

# iosxe tests/test_show_bgp
from genie.libs.parser.iosxe.tests.test_show_bgp import \
                                test_show_bgp_all_detail as test_show_bgp_all_detail_iosxe,\
                                test_show_bgp_all_neighbors_policy as test_show_bgp_all_neighbors_policy_iosxe,\
                                test_show_bgp_all_neighbors_advertised_routes as test_show_bgp_all_neighbors_advertised_routes_iosxe,\
                                test_show_bgp_all_summary as test_show_bgp_all_summary_iosxe,\
                                test_show_bgp_all_cluster_ids as test_show_bgp_all_cluster_ids_iosxe,\
                                test_show_bgp_all_neighbors as test_show_bgp_all_neighbors_iosxe,\
                                test_show_bgp_neighbors_received_routes as test_show_bgp_neighbors_received_routes_iosxe,\
                                test_show_ip_bgp_template_peer_session as test_show_ip_bgp_template_peer_session_iosxe,\
                                test_show_bgp_all_neighbors_routes as test_show_bgp_all_neighbors_routes_iosxe,\
                                test_show_ip_bgp_template_peer_policy as test_show_ip_bgp_template_peer_policy_iosxe,\
                                test_show_ip_bgp_all_dampening_parameters as test_show_ip_bgp_all_dampening_parameters_iosxe,\
                                test_show_bgp_all as test_show_bgp_all_iosxe, \
                                test_show_bgp_summary as test_show_bgp_summary_iosxe, \
                                test_show_ip_bgp as test_show_bgp_iosxe

# ===================================
# Unit test for 'show bgp all detail'
# ===================================
class test_show_ip_bgp(test_show_bgp_iosxe):

    def test_show_ip_bgp(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpBgp(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


# ===================================
# Unit test for 'show bgp all detail'
# ===================================
class test_show_bgp_all_detail(test_show_bgp_all_detail_iosxe):

    def test_show_bgp_all_detail_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowBgpAllDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_bgp_all_detail_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowBgpAllDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_bgp_all_detail_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpAllDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

# ====================================================
# Unit test for 'show bgp all neighbors <WORD> policy'
# ====================================================
class test_show_bgp_all_neighbors_policy(test_show_bgp_all_neighbors_policy_iosxe):

    def test_show_bgp_all_neighbors_policy_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowBgpAllNeighborsPolicy(device=self.device)
        parsed_output = obj.parse(neighbor='10.186.0.2')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_bgp_vrf_all_neighbors_policy_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowBgpAllNeighborsPolicy(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(neighbor='10.106.102.3')

    def test_show_bgp_all_neighbors_policy_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowBgpAllNeighborsPolicy(device=self.device)
        parsed_output = obj.parse(neighbor='10.4.6.6')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_bgp_all_neighbors_policy_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpAllNeighborsPolicy(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(neighbor='10.4.6.6')

# ===============================================================
# Unit test for 'show bgp all neighbors <WORD> advertised-routes'
# ===============================================================
class test_show_bgp_all_neighbors_advertised_routes(test_show_bgp_all_neighbors_advertised_routes_iosxe):

    def test_show_bgp_all_neighbors_advertised_routes_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowBgpAllNeighborsAdvertisedRoutes(device=self.device)
        parsed_output = obj.parse(neighbor='10.186.0.2')
        self.assertEqual(parsed_output,self.golden_parsed_output1)

    def test_show_bgp_vrf_all_neighbors_advertised_routes_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowBgpAllNeighborsAdvertisedRoutes(device=self.device)
        parsed_output = obj.parse(neighbor='10.106.102.3')
        self.assertEqual(parsed_output,self.golden_parsed_output2)

    def test_show_bgp_vrf_all_neighbors_advertised_routes_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowBgpAllNeighborsAdvertisedRoutes(device=self.device)
        parsed_output = obj.parse(neighbor='10.4.6.6')
        self.assertEqual(parsed_output,self.golden_parsed_output3)

    def test_show_bgp_all_neighbors_advertised_routes_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpAllNeighborsAdvertisedRoutes(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(neighbor='10.4.6.6')

# ===============================================================
# Unit test for 'show bgp all summary'
# ===============================================================

class test_show_bgp_all_summary(test_show_bgp_all_summary_iosxe):

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowBgpAllSummary(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowBgpAllSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowBgpAllSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

# ===============================================================
# Unit test for 'show bgp all cluster-ids'
# ===============================================================
class test_show_bgp_all_cluster_ids(test_show_bgp_all_cluster_ids_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpAllClusterIds(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowBgpAllClusterIds(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowBgpAllClusterIds(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowBgpAllClusterIds(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

# =============================================================
# Unit test for 'show bgp all neighbors'
# =============================================================
class test_show_bgp_all_neighbors(test_show_bgp_all_neighbors_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpAllNeighbors(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowBgpAllNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

# =============================================================
# Unit test for 'show bgp all neighbors <WORD> received-routes'
# =============================================================
class test_show_bgp_neighbors_received_routes(test_show_bgp_neighbors_received_routes_iosxe):

    def test_show_bgp_vrf_all_neighbors_received_routes_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowBgpAllNeighborsReceivedRoutes(device=self.device)
        parsed_output = obj.parse(neighbor='10.186.0.2')
        self.assertEqual(parsed_output,self.golden_parsed_output1)

    def test_show_bgp_vrf_all_neighbors_received_routes_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowBgpAllNeighborsReceivedRoutes(device=self.device)
        parsed_output = obj.parse(neighbor='10.106.101.1')
        self.assertEqual(parsed_output,self.golden_parsed_output2)

    def test_show_bgp_vrf_all_neighbors_received_routes_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpAllNeighborsReceivedRoutes(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(neighbor='10.186.0.2')

# ================================================================
#  unit test for show ip bgp template peer-session <WORD>"""
# =================================================================
class test_show_ip_bgp_template_peer_session(test_show_ip_bgp_template_peer_session_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpBgpTemplatePeerSession(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowIpBgpTemplatePeerSession(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_golden2(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowIpBgpTemplatePeerSession(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_golden3(self):
        self.device = Mock(**self.golden_output3)
        obj = ShowIpBgpTemplatePeerSession(device=self.device)
        parsed_output = obj.parse(template_name='PEER-SESSION')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

# ====================================================
# Unit test for 'show bgp all neighbors <WORD> routes'
# ====================================================
class test_show_bgp_all_neighbors_routes(test_show_bgp_all_neighbors_routes_iosxe):

    def test_show_bgp_vrf_all_neighbors_routes_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowBgpAllNeighborsRoutes(device=self.device)
        parsed_output = obj.parse(neighbor='10.186.0.2')
        self.assertEqual(parsed_output,self.golden_parsed_output1)

    def test_show_bgp_vrf_all_neighbors_routes_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowBgpAllNeighborsRoutes(device=self.device)
        parsed_output = obj.parse(neighbor='10.106.101.1')
        self.assertEqual(parsed_output,self.golden_parsed_output2)

    def test_show_bgp_vrf_all_neighbors_routes_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowBgpAllNeighborsRoutes(device=self.device)
        parsed_output = obj.parse(neighbor='10.4.6.6')
        self.assertEqual(parsed_output,self.golden_parsed_output3)

    def test_show_bgp_vrf_all_neighbors_routes_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpAllNeighborsRoutes(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(neighbor='10.186.0.2')

# ================================================================
#  unit test for show ip bgp template peer-policy <WORD>"""
# =================================================================
class test_show_ip_bgp_template_peer_policy(test_show_ip_bgp_template_peer_policy_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpBgpTemplatePeerPolicy(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpBgpTemplatePeerPolicy(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpBgpTemplatePeerPolicy(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpBgpTemplatePeerPolicy(device=self.device)
        parsed_output = obj.parse(template_name='PEER-POLICY2')
        self.assertEqual(parsed_output, self.golden_parsed_output_2)


# ===================================================================
#   unit test for show ip bgp all dampening parameters
# ===================================================================
class test_show_ip_bgp_all_dampening_parameters(test_show_ip_bgp_all_dampening_parameters_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpBgpAllDampeningParameters(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpBgpAllDampeningParameters(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpBgpAllDampeningParameters(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_3)
        obj = ShowIpBgpAllDampeningParameters(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_3)

    def test_golden_4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_4)
        obj = ShowIpBgpAllDampeningParameters(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_4)

    def test_golden_5(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_5)
        obj = ShowIpBgpAllDampeningParameters(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

# ===================================================================
#   unit test for show bgp all
# ===================================================================
class test_show_bgp_all(test_show_bgp_all_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowBgpAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowBgpAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_golden_3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowBgpAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output3)

# ===============================================================
# Unit test for 'show bgp summary'
# ===============================================================

class test_show_bgp_summary(test_show_bgp_summary_iosxe):

    def test_show_bgp_summary_empty(self):
        self.device1 = Mock(**self.empty_output)
        bgp_summary_obj = ShowBgpSummary(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = bgp_summary_obj.parse()

    def test_show_bgp_summary_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowBgpSummary(device=self.device)
        parsed_output = obj.parse(address_family='vpnv4 unicast', rd='5918:51')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_bgp_summary_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowBgpSummary(device=self.device)
        parsed_output = obj.parse(address_family='vpnv4 unicast', vrf='L3VPN-0051')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

if __name__ == '__main__':
    unittest.main()
