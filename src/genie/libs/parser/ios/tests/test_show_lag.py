#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError

from genie.libs.parser.ios.show_lag import ShowLacpSysId,\
                                    ShowEtherchannelSummary,\
                                    ShowLacpCounters,\
                                    ShowLacpInternal,\
                                    ShowLacpNeighbor,\
                                    ShowPagpCounters, \
                                    ShowPagpNeighbor,\
                                    ShowPagpInternal,\
                                    ShowEtherChannelLoadBalancing,\
                                    ShowLacpNeighborDetail

# iosxe tests/test_show_lag
from genie.libs.parser.iosxe.tests.test_show_lag import \
            test_show_lacp_sysid as test_show_lacp_sysid_iosxe,\
            test_show_lacp_counters as test_show_lacp_counters_iosxe,\
            test_show_lacp_internal as test_show_lacp_internal_iosxe,\
            test_show_lacp_neighbor as test_show_lacp_neighbor_iosxe,\
            test_show_lacp_neighbor_detail as test_show_lacp_neighbor_detail_iosxe,\
            test_show_pagp_neighbor as test_show_pagp_neighbor_iosxe,\
            test_show_pagp_counters as test_show_pagp_counters_iosxe,\
            test_show_pagp_internal as test_show_pagp_internal_iosxe,\
            test_show_etherchannel_summary as test_show_etherchannel_summary_iosxe,\
            test_show_etherchannel_loadbalancing as test_show_etherchannel_loadbalancing_iosxe


###################################################
# unit test for show lacp sys-id
####################################################
class test_show_lacp_sysid(test_show_lacp_sysid_iosxe):
    """unit test for show lacp sysid"""

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLacpSysId(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowLacpSysId(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


###################################################
# unit test for show lacp counter
####################################################
class test_show_lacp_counters(test_show_lacp_counters_iosxe):
    """unit test for show lacp counters """

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLacpCounters(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowLacpCounters(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


###################################################
# unit test for show lacp internal
####################################################
class test_show_lacp_internal(test_show_lacp_internal_iosxe):
    """unit test for show lacp internal """

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLacpInternal(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowLacpInternal(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


###################################################
# unit test for show lacp neighbor
####################################################
class test_show_lacp_neighbor(test_show_lacp_neighbor_iosxe):
    """unit test for show lacp neighbor """

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLacpNeighbor(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowLacpNeighbor(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


###################################################
# unit test for show pagp neighbor
####################################################
class test_show_pagp_neighbor(test_show_pagp_neighbor_iosxe):
    """unit test for show pagp neighbor """

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowPagpNeighbor(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowPagpNeighbor(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


###################################################
# unit test for show pagp counters
####################################################
class test_show_pagp_counters(test_show_pagp_counters_iosxe):
    """unit test for show pagp counters"""

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowPagpCounters(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowPagpCounters(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


###################################################
# unit test for show pagp internal
####################################################
class test_show_pagp_internal(test_show_pagp_internal_iosxe):
    """unit test for show pagp internal"""

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowPagpInternal(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowPagpInternal(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


###################################################
# unit test for show etherchannel summary
####################################################
class test_show_etherchannel_summary(test_show_etherchannel_summary_iosxe):
    """unit test for show etherchannel summary """

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowEtherchannelSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowEtherchannelSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowEtherchannelSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_1)


###################################################
# unit test for show etherchannel load-balancing
####################################################
class test_show_etherchannel_loadbalancing(test_show_etherchannel_loadbalancing_iosxe):
    """unit test for show etherchannel load-balancing """

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowEtherChannelLoadBalancing(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowEtherChannelLoadBalancing(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


###################################################
# unit test for show lacp neighbor detail
####################################################
class test_show_lacp_neighbor_detail(test_show_lacp_neighbor_detail_iosxe):
    """unit test for show lacp neighbor detail"""

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLacpNeighborDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowLacpNeighborDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()