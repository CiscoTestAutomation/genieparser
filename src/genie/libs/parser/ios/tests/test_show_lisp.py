
# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# ios show_lisp
from genie.libs.parser.ios.show_lisp import ShowLispSession,\
                                            ShowLispPlatform,\
                                            ShowLispExtranet,\
                                            ShowLispDynamicEidDetail,\
                                            ShowLispService,\
                                            ShowLispServiceMapCache,\
                                            ShowLispServiceRlocMembers,\
                                            ShowLispServiceSmr,\
                                            ShowLispServiceSummary,\
                                            ShowLispServiceDatabase,\
                                            ShowLispServiceServerSummary,\
                                            ShowLispServiceServerDetailInternal,\
                                            ShowLispServiceStatistics

# iosxe tests/test_show_lisp
from genie.libs.parser.iosxe.tests.test_show_lisp import \
            test_show_lisp_session as test_show_lisp_session_iosxe,\
            test_show_lisp_platform as test_show_lisp_platform_iosxe,\
            test_show_lisp_extranet as test_show_lisp_extranet_iosxe,\
            test_show_lisp_dynamic_eid_detail as test_show_lisp_dynamic_eid_detail_iosxe,\
            test_show_lisp_service as test_show_lisp_service_iosxe,\
            test_show_lisp_service_map_cache as test_show_lisp_service_map_cache_iosxe,\
            test_show_lisp_service_rloc_members as test_show_lisp_service_rloc_members_iosxe,\
            test_show_lisp_service_smr as test_show_lisp_service_smr_iosxe,\
            test_show_lisp_service_summary as test_show_lisp_service_summary_iosxe,\
            test_show_lisp_service_database as test_show_lisp_service_database_iosxe,\
            test_show_lisp_service_server_summary as test_show_lisp_service_server_summary_iosxe,\
            test_show_lisp_service_server_detail_internal as test_show_lisp_service_server_detail_internal_iosxe,\
            test_show_lisp_service_statistics as test_show_lisp_service_statistics_iosxe

# =================================
# Unit test for 'show lisp session'
# =================================
class test_show_lisp_session(test_show_lisp_session_iosxe):

    def test_show_lisp_session_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispSession(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_session_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispSession(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ==================================
# Unit test for 'show lisp platform'
# ==================================
class test_show_lisp_platform(test_show_lisp_platform_iosxe):

    def test_show_lisp_platform_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispPlatform(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_platform_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispPlatform(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ===========================================================================
# Unit test for 'show lisp all extranet <extranet> instance-id <instance_id>'
# ===========================================================================
class test_show_lisp_extranet(test_show_lisp_extranet_iosxe):

    def test_show_lisp_extranet_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispExtranet(device=self.device)
        parsed_output = obj.parse(extranet='ext1', instance_id='103')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_extranet_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispExtranet(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(extranet='ext1', instance_id='103')


# ==========================================================================
# Unit test for 'show lisp all instance-id <instance_id> dynamic-eid detail'
# ==========================================================================
class test_show_lisp_dynamic_eid_detail(test_show_lisp_dynamic_eid_detail_iosxe):

    def test_show_lisp_dynamic_eid_detail_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispDynamicEidDetail(device=self.device)
        parsed_output = obj.parse(instance_id=101)
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_dynamic_eid_detail_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowLispDynamicEidDetail(device=self.device)
        parsed_output = obj.parse(instance_id=101)
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_lisp_dynamic_eid_detail_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowLispDynamicEidDetail(device=self.device)
        parsed_output = obj.parse(instance_id=101)
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_lisp_dynamic_eid_detail_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispDynamicEidDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(instance_id=101)


# =================================================================
# Unit test for 'show lisp all instance-id <instance_id> <service>'
# =================================================================
class test_show_lisp_service(test_show_lisp_service_iosxe):

    def test_show_lisp_service_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispService(device=self.device)
        parsed_output = obj.parse(instance_id=101, service='ipv4')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_service_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowLispService(device=self.device)
        parsed_output = obj.parse(instance_id=101, service='ipv6')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_lisp_service_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowLispService(device=self.device)
        parsed_output = obj.parse(instance_id='*', service='ethernet')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_lisp_service_full4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output4)
        obj = ShowLispService(device=self.device)
        parsed_output = obj.parse(instance_id='*', service='ipv4')
        self.assertEqual(parsed_output, self.golden_parsed_output4)

    def test_show_lisp_service_full5(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output5)
        obj = ShowLispService(device=self.device)
        parsed_output = obj.parse(instance_id='*', service='ipv6')
        self.assertEqual(parsed_output, self.golden_parsed_output5)

    def test_show_lisp_service_full6(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output6)
        obj = ShowLispService(device=self.device)
        parsed_output = obj.parse(instance_id='*', service='ethernet')
        self.assertEqual(parsed_output, self.golden_parsed_output6)

    def test_show_lisp_service_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispService(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(instance_id='*', service='ipv4')


# ===========================================================================
# Unit test for 'show lisp all instance-id <instance_id> <service> map-cache'
# ===========================================================================
class test_show_lisp_service_map_cache(test_show_lisp_service_map_cache_iosxe):

    def test_show_lisp_service_map_cache_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispServiceMapCache(device=self.device)
        parsed_output = obj.parse(instance_id=101, service='ipv4')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_service_map_cache_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowLispServiceMapCache(device=self.device)
        parsed_output = obj.parse(instance_id=101, service='ipv6')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_lisp_service_map_cache_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowLispServiceMapCache(device=self.device)
        parsed_output = obj.parse(instance_id='*', service='ethernet')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_lisp_service_map_cache_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispServiceMapCache(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(instance_id='*', service='ipv4')


# ==============================================================================
# Unit test for 'show lisp all instance-id <instance_id> <service> rloc members'
# ==============================================================================
class test_show_lisp_service_rloc_members(test_show_lisp_service_rloc_members_iosxe):

    def test_show_lisp_service_rloc_members_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispServiceRlocMembers(device=self.device)
        parsed_output = obj.parse(instance_id=101, service='ipv4')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_service_rloc_members_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowLispServiceRlocMembers(device=self.device)
        parsed_output = obj.parse(instance_id=101, service='ipv6')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_lisp_service_rloc_members_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowLispServiceRlocMembers(device=self.device)
        parsed_output = obj.parse(instance_id='*', service='ethernet')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_lisp_service_rloc_members_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispServiceRlocMembers(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(instance_id='*', service='ipv4')


# =====================================================================
# Unit test for 'show lisp all instance-id <instance_id> <service> smr'
# =====================================================================
class test_show_lisp_service_smr(test_show_lisp_service_smr_iosxe):

    def test_show_lisp_service_smr_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispServiceSmr(device=self.device)
        parsed_output = obj.parse(instance_id=101, service='ipv4')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_service_smr_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowLispServiceSmr(device=self.device)
        parsed_output = obj.parse(instance_id=101, service='ipv6')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_lisp_service_smr_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispServiceSmr(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(instance_id='*', service='ipv4')


# =======================================================
# Unit test for 'show lisp all service <service> summary'
# =======================================================
class test_show_lisp_service_summary(test_show_lisp_service_summary_iosxe):

    def test_show_lisp_service_summary_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispServiceSummary(device=self.device)
        parsed_output = obj.parse(service='ipv4')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_service_summary_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowLispServiceSummary(device=self.device)
        parsed_output = obj.parse(service='ipv6')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_lisp_service_summary_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowLispServiceSummary(device=self.device)
        parsed_output = obj.parse(service='ethernet')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_lisp_service_summary_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispServiceSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(service='ipv4')


# ==========================================================================
# Unit test for 'show lisp all instance-id <instance_id> <service> dabatase'
# ==========================================================================
class test_show_lisp_service_database(test_show_lisp_service_database_iosxe):

    def test_show_lisp_service_database_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispServiceDatabase(device=self.device)
        parsed_output = obj.parse(service='ipv4', instance_id='101')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_service_database_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowLispServiceDatabase(device=self.device)
        parsed_output = obj.parse(service='ipv6', instance_id='101')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_lisp_service_database_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowLispServiceDatabase(device=self.device)
        parsed_output = obj.parse(service='ethernet', instance_id='*')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_lisp_service_database_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispServiceDatabase(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(service='ipv4', instance_id='*')


# ================================================================================
# Unit test for 'show lisp all instance-id <instance_id> <service> server summary'
# ================================================================================
class test_show_lisp_service_server_summary(test_show_lisp_service_server_summary_iosxe):

    def test_show_lisp_service_server_summary_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispServiceServerSummary(device=self.device)
        parsed_output = obj.parse(service='ipv4', instance_id='101')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_service_server_summary_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowLispServiceServerSummary(device=self.device)
        parsed_output = obj.parse(service='ipv6', instance_id='101')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_lisp_service_server_summary_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowLispServiceServerSummary(device=self.device)
        parsed_output = obj.parse(service='ethernet', instance_id='*')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_lisp_service_server_summary_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispServiceServerSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(service='ipv4', instance_id='*')


# ========================================================================================
# Unit test for 'show lisp all instance-id <instance_id> <service> server detail internal'
# ========================================================================================
class test_show_lisp_service_server_detail_internal(test_show_lisp_service_server_detail_internal_iosxe):

    def test_show_lisp_service_server_detail_internal_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispServiceServerDetailInternal(device=self.device)
        parsed_output = obj.parse(service='ipv4', instance_id='101')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_service_server_detail_internal_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowLispServiceServerDetailInternal(device=self.device)
        parsed_output = obj.parse(service='ipv6', instance_id='101')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_lisp_service_server_detail_internal_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowLispServiceServerDetailInternal(device=self.device)
        parsed_output = obj.parse(service='ethernet', instance_id='*')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_lisp_service_server_detail_internal_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispServiceServerDetailInternal(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(service='ipv4', instance_id='*')


# ============================================================================
# Unit test for 'show lisp all instance-id <instance_id> <service> statistics'
# ============================================================================
class test_show_lisp_service_statistics(test_show_lisp_service_statistics_iosxe):

    def test_show_lisp_service_statistics_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispServiceStatistics(device=self.device)
        parsed_output = obj.parse(service='ipv4', instance_id='101')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_service_statistics_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowLispServiceStatistics(device=self.device)
        parsed_output = obj.parse(service='ipv6', instance_id='101')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_lisp_service_statistics_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowLispServiceStatistics(device=self.device)
        parsed_output = obj.parse(service='ethernet', instance_id='*')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_lisp_service_statistics_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispServiceStatistics(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(service='ipv4', instance_id='*')


if __name__ == '__main__':
    unittest.main()
