#!/bin/env python
import unittest
from unittest.mock import Mock
from pyats.topology import Device

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
class test_show_lacp_counters(unittest.TestCase):
    """unit test for show lacp counters """

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        Device# show lacp 1 counters
                      LACPDUs         Marker       LACPDUs
        Port       Sent   Recv     Sent   Recv     Pkts Err
        ---------------------------------------------------
        Channel group: 1
          Fa4/1    8      15       0      0         3    0
          Fa4/2    14     18       0      0         3    0
          Fa4/3    14     18       0      0         0
          Fa4/4    13     18       0      0         0
    '''}

    golden_parsed_output = {
        "interfaces": {
            "Port-channel1": {
                "name": "Port-channel1",
                "protocol": "lacp",
                "members": {
                    "FastEthernet4/1": {
                        "interface": "FastEthernet4/1",
                        "counters": {
                            "lacp_in_pkts": 15,
                            "lacp_out_pkts": 8,
                            "marker_in_pkts": 0,
                            "marker_out_pkts": 0,
                            "lacp_pkts": 3,
                            "lacp_errors": 0
                        }
                    },
                    "FastEthernet4/2": {
                        "interface": "FastEthernet4/2",
                        "counters": {
                            "lacp_in_pkts": 18,
                            "lacp_out_pkts": 14,
                            "marker_in_pkts": 0,
                            "marker_out_pkts": 0,
                            "lacp_pkts": 3,
                            "lacp_errors": 0
                        }
                    },
                    "FastEthernet4/3": {
                        "interface": "FastEthernet4/3",
                        "counters": {
                            "lacp_in_pkts": 18,
                            "lacp_out_pkts": 14,
                            "marker_in_pkts": 0,
                            "marker_out_pkts": 0,
                            "lacp_pkts": 0
                        }
                    },
                    "FastEthernet4/4": {
                        "interface": "FastEthernet4/4",
                        "counters": {
                            "lacp_in_pkts": 18,
                            "lacp_out_pkts": 13,
                            "marker_in_pkts": 0,
                            "marker_out_pkts": 0,
                            "lacp_pkts": 0
                        }
                    }
                }
            }
        }
    }

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
class test_show_lacp_internal(unittest.TestCase):
    """unit test for show lacp internal """

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        Device# show lacp 1 internal
        Channel group 1
                                    LACPDUs     LACP Port    Admin   Oper    Port     Port
        Port      Flags    State    Interval    Priority     Key     Key     Number   State
        Fa4/1     saC      bndl     30s         32768        100     100     0xc1     0x75
        Fa4/2     saC      bndl     30s         32768        100     100     0xc2     0x75
    '''}

    golden_parsed_output = {
        "interfaces": {
            "Port-channel1": {
                "name": "Port-channel1",
                "protocol": "lacp",
                "members": {
                    "FastEthernet4/1": {
                        "interface": "FastEthernet4/1",
                        "activity": "auto",
                        "flags": "saC",
                        "state": "bndl",
                        "bundled": True,
                        "lacp_port_priority": 32768,
                        "admin_key": 100,
                        "oper_key": 100,
                        "port_num": 193,
                        "port_state": 117,
                        "lacp_interval": "30s"
                    },
                    "FastEthernet4/2": {
                        "interface": "FastEthernet4/2",
                        "activity": "auto",
                        "flags": "saC",
                        "state": "bndl",
                        "bundled": True,
                        "lacp_port_priority": 32768,
                        "admin_key": 100,
                        "oper_key": 100,
                        "port_num": 194,
                        "port_state": 117,
                        "lacp_interval": "30s"
                    }
                }
            }
        }
    }

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