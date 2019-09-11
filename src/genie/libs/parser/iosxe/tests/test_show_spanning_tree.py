#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from genie.libs.parser.iosxe.show_spanning_tree import ShowSpanningTreeDetail, \
                                    ShowSpanningTreeMstDetail, \
                                    ShowSpanningTreeSummary, \
                                    ShowErrdisableRecovery, \
                                    ShowSpanningTree, \
                                    ShowSpanningTreeMstConfiguration



class test_show_spanning_tree_summary(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output_mstp = {
        "bpdu_filter": False,
        "extended_system_id": True,
        "etherchannel_misconfig_guard": False,
        "total_statistics": {
          "forwardings": 10,
          "listenings": 0,
          "num_of_msts": 2,
          "stp_actives": 16,
          "learnings": 0,
          "blockings": 6
        },
        "root_bridge_for": "MST0, MST100",
        "bpdu_guard": False,
        "mode": {
          "mst": {
               "MST100": {
                    "blocking": 3,
                    "forwarding": 1,
                    "listening": 0,
                    "stp_active": 4,
                    "learning": 0
               },
               "MST0": {
                    "blocking": 3,
                    "forwarding": 9,
                    "listening": 0,
                    "stp_active": 12,
                    "learning": 0
               }
          }
        },
        "uplink_fast": False,
        "backbone_fast": False,
        "portfast_default": False,
        "loop_guard": False,
        "configured_pathcost": {
            'method': 'short',
            'operational_value': 'long',
        }
    }

    golden_parsed_output_mstp_single_mst = {
        "backbone_fast": False,
        "bpdu_filter": False,
        "bpdu_guard": False,
        "bridge_assurance": True,
        "configured_pathcost": {
            "method": "short",
            "operational_value": "long"
        },
        "etherchannel_misconfig_guard": True,
        "extended_system_id": True,
        "loop_guard": False,
        "mode": {
            "mst": {
                "MST0": {
                    "blocking": 3,
                    "forwarding": 0,
                    "learning": 0,
                    "listening": 0,
                    "stp_active": 3
                }
            }
        },
        "portfast_default": False,
        "pvst_simulation": True,
        "root_bridge_for": "MST0",
        "total_statistics": {
            "blockings": 3,
            "forwardings": 0,
            "learnings": 0,
            "listenings": 0,
            "num_of_msts": 1,
            "stp_actives": 3
        },
        "uplink_fast": False
    }

    golden_parsed_output_pvst = {
        "etherchannel_misconfig_guard": True,
        "mode": {
          "pvst": {
                "VLAN0101": {
                    "stp_active": 1,
                    "forwarding": 0,
                    "blocking": 0,
                    "listening": 1,
                    "learning": 0
                },
                "VLAN0406": {
                    "stp_active": 1,
                    "forwarding": 0,
                    "blocking": 0,
                    "listening": 1,
                    "learning": 0
                },
                "VLAN0405": {
                    "stp_active": 1,
                    "forwarding": 0,
                    "blocking": 0,
                    "listening": 1,
                    "learning": 0
                },
                "VLAN0407": {
                    "stp_active": 1,
                    "forwarding": 0,
                    "blocking": 0,
                    "listening": 1,
                    "learning": 0
                },
                "VLAN0100": {
                    "stp_active": 1,
                    "forwarding": 0,
                    "blocking": 0,
                    "listening": 1,
                    "learning": 0
                }
            }
        },
        "portfast_default": False,
        "backbone_fast": False,
        "extended_system_id": True,
        "bpdu_filter": False,
        "bpdu_guard": False,
        "total_statistics": {
          "stp_actives": 5,
          "forwardings": 0,
          "blockings": 0,
          "num_of_vlans": 5,
          "learnings": 0,
          "listenings": 5
        },
        "loop_guard": False,
        "uplink_fast": False,
        "root_bridge_for": "VLAN0100-VLAN0101, VLAN0405-VLAN0407",
        "configured_pathcost": {
            'method': 'short'
        }
    }

    golden_parsed_output_rpvst = {
        "backbone_fast": False,
        "bpdu_filter": False,
        "bpdu_guard": False,
        "bridge_assurance": True,
        "pvst_simulation": True,
        "pvst_simulation_status": "inactive",
        "configured_pathcost": {
            "method": "short"
        },
        "etherchannel_misconfig_guard": True,
        "extended_system_id": True,
        "loop_guard": False,
        "mode": {
            "rapid_pvst": {
                "VLAN0001": {
                    "blocking": 0,
                    "forwarding": 1,
                    "learning": 0,
                    "listening": 0,
                    "stp_active": 1
                }
            }
        },
        "portfast_default": False,
        "root_bridge_for": "VLAN0001",
        "total_statistics": {
            "blockings": 0,
            "forwardings": 1,
            "learnings": 0,
            "listenings": 0,
            "num_of_vlans": 1,
            "stp_actives": 1
        },
        "uplink_fast": False
    }

    golden_output_mstp = {'execute.return_value': '''\
        Switch is in mst mode (IEEE Standard)
        Root bridge for: MST0, MST100
        EtherChannel misconfig guard is disabled
        Extended system ID           is enabled
        Portfast Default             is disabled
        PortFast BPDU Guard Default  is disabled
        Portfast BPDU Filter Default is disabled
        Loopguard Default            is disabled
        UplinkFast                   is disabled
        BackboneFast                 is disabled
        Configured Pathcost method used is short (Operational value is long)

        Name                   Blocking Listening Learning Forwarding STP Active
        ---------------------- -------- --------- -------- ---------- ----------
        MST0                         3         0        0          9         12
        MST100                       3         0        0          1          4
        ---------------------- -------- --------- -------- ---------- ----------
        2 msts                       6         0        0         10         16
    '''
    }

    golden_output_mstp_single_mst = {'execute.return_value': '''\
        Switch is in mst mode (IEEE Standard)
        Root bridge for: MST0
        Extended system ID                      is enabled
        Portfast Default                        is disabled
        Portfast Edge BPDU Guard Default        is disabled
        Portfast Edge BPDU Filter Default       is disabled
        Loopguard Default                       is disabled
        PVST Simulation                         is enabled
        Bridge Assurance                        is enabled
        EtherChannel misconfig guard            is enabled
        UplinkFast                              is disabled
        BackboneFast                            is disabled
        Configured Pathcost method used is short (Operational value is long)

        Name                   Blocking Listening Learning Forwarding STP Active
        ---------------------- -------- --------- -------- ---------- ----------
        MST0                         3         0        0          0          3
        ---------------------- -------- --------- -------- ---------- ----------
        1 mst                        3         0        0          0          3
    '''
    }

    golden_output_pvst = {'execute.return_value': '''\
        Switch is in pvst mode
        Root bridge for: VLAN0100-VLAN0101, VLAN0405-VLAN0407
        EtherChannel misconfig guard            is enabled
        Extended system ID                      is enabled
        Portfast Default                        is disabled
        PortFast BPDU Guard Default            is disabled
        Portfast BPDU Filter Default           is disabled
        Loopguard Default                      is disabled
        UplinkFast                              is disabled
        BackboneFast                            is disabled
        Configured Pathcost method used is short

        Name                   Blocking Listening Learning Forwarding STP Active
        ---------------------- -------- --------- -------- ---------- ----------
        VLAN0100                     0         1        0          0          1
        VLAN0101                     0         1        0          0          1
                  
        Name                   Blocking Listening Learning Forwarding STP Active
        ---------------------- -------- --------- -------- ---------- ----------
        VLAN0405                     0         1        0          0          1
        VLAN0406                     0         1        0          0          1
                  
        Name                   Blocking Listening Learning Forwarding STP Active
        ---------------------- -------- --------- -------- ---------- ----------
        VLAN0407                     0         1        0          0          1
        ---------------------- -------- --------- -------- ---------- ----------
        5 vlans                      0         5        0          0          5

    '''
   }

    golden_output_rpvst = {'execute.return_value': '''\
        Switch is in rapid-pvst mode
        Root bridge for: VLAN0001
        Extended system ID                      is enabled
        Portfast Default                        is disabled
        Portfast Edge BPDU Guard Default        is disabled
        Portfast Edge BPDU Filter Default       is disabled
        Loopguard Default                       is disabled
        PVST Simulation Default                 is enabled but inactive in rapid-pvst mode
        Bridge Assurance                        is enabled
        EtherChannel misconfig guard            is enabled
        UplinkFast                              is disabled
        BackboneFast                            is disabled
        Configured Pathcost method used is short

        Name                   Blocking Listening Learning Forwarding STP Active
        ---------------------- -------- --------- -------- ---------- ----------
        VLAN0001                     0         0        0          1          1
        ---------------------- -------- --------- -------- ---------- ----------
        1 vlan                       0         0        0          1          1

     '''
    }
    
    golden_output_1 = {'execute.return_value': '''\
        show spanning-tree summary
        Switch is in rapid-pvst mode
        Root bridge for: VLAN0001, VLAN0115-VLAN0116, VLAN0118-VLAN0119, VLAN0121
          VLAN0180, VLAN0501-VLAN0503, VLAN0506, VLAN0508-VLAN0518, VLAN0521-VLAN0522
          VLAN0540, VLAN0601-VLAN0604, VLAN0606, VLAN0701, VLAN0801-VLAN0806
          VLAN1111-VLAN1116, VLAN1506, VLAN1509, VLAN1601
        EtherChannel misconfig guard            is enabled
        Extended system ID                      is enabled
        Portfast Default                        is disabled
        Portfast Edge BPDU Guard Default        is disabled
        Portfast Edge BPDU Filter Default       is disabled
        Loopguard Default                       is disabled
        PVST Simulation Default                 is enabled but inactive in rapid-pvst mode
        Bridge Assurance                        is enabled
        UplinkFast                              is disabled
        BackboneFast                            is disabled
        Pathcost method used                    is short

        Name                   Blocking Listening Learning Forwarding STP Active
        ---------------------- -------- --------- -------- ---------- ----------
        VLAN0001                     0         0        0          2          2
        VLAN0115                     0         0        0          1          1
        VLAN0116                     0         0        0          1          1
        VLAN0118                     0         0        0          1          1
        VLAN0119                     0         0        0          1          1
        VLAN0121                     0         0        0          1          1
        VLAN0180                     0         0        0          1          1
        VLAN0501                     0         0        0          1          1
        VLAN0502                     0         0        0          1          1
        VLAN0503                     0         0        0          3          3
        VLAN0506                     0         0        0          1          1
        VLAN0508                     0         0        0          1          1
        VLAN0509                     0         0        0          1          1
        VLAN0510                     0         0        0          1          1
        VLAN0511                     0         0        0          1          1
        VLAN0512                     0         0        0          1          1
        VLAN0513                     0         0        0          1          1
        VLAN0514                     0         0        0          1          1
        VLAN0515                     0         0        0          1          1
        VLAN0516                     0         0        0          1          1
        VLAN0517                     0         0        0          1          1
        VLAN0518                     0         0        0          1          1
        VLAN0521                     0         0        0          1          1
        VLAN0522                     0         0        0          1          1
        VLAN0540                     0         0        0          3          3
        VLAN0601                     0         0        0          1          1
        VLAN0602                     0         0        0          1          1
        VLAN0603                     0         0        0          2          2
        VLAN0604                     0         0        0          1          1
        VLAN0606                     0         0        0          2          2
        VLAN0701                     0         0        0          1          1
        VLAN0801                     0         0        0          1          1
        VLAN0802                     0         0        0          1          1
        VLAN0803                     0         0        0          1          1
        VLAN0804                     0         0        0          1          1
        VLAN0805                     0         0        0          1          1
        VLAN0806                     0         0        0          1          1
        VLAN0916                     0         0        0          2          2
        VLAN1111                     0         0        0          2          2
        VLAN1112                     0         0        0          2          2
        VLAN1113                     0         0        0          2          2
        VLAN1114                     0         0        0          2          2
        VLAN1115                     0         0        0          2          2
        VLAN1116                     0         0        0          2          2
        VLAN1125                     0         0        0          1          1
        VLAN1506                     0         0        0          1          1
        VLAN1509                     0         0        0          1          1
        VLAN1601                     0         0        0          1          1
        ---------------------- -------- --------- -------- ---------- ----------
        48 vlans                     0         0        0         62         62
     '''
    }

    golden_parsed_output_1 = {
        'backbone_fast': False,
        'bpdu_filter': False,
        'bpdu_guard': False,
        'bridge_assurance': True,
        'configured_pathcost': {'method': 'short'},
        'etherchannel_misconfig_guard': True,
        'extended_system_id': True,
        'loop_guard': False,
        'mode': {'rapid_pvst': {'VLAN0001': {'blocking': 0,
                                              'forwarding': 2,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 2},
                                'VLAN0115': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0116': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0118': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0119': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0121': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0180': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0501': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0502': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0503': {'blocking': 0,
                                              'forwarding': 3,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 3},
                                'VLAN0506': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0508': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0509': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0510': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0511': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0512': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0513': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0514': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0515': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0516': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0517': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0518': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0521': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0522': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0540': {'blocking': 0,
                                             'forwarding': 3,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 3},
                                'VLAN0601': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0602': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0603': {'blocking': 0,
                                              'forwarding': 2,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 2},
                                'VLAN0604': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0606': {'blocking': 0,
                                              'forwarding': 2,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 2},
                                'VLAN0701': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0801': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0802': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0803': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0804': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0805': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0806': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN0916': {'blocking': 0,
                                              'forwarding': 2,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 2},
                                'VLAN1111': {'blocking': 0,
                                              'forwarding': 2,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 2},
                                'VLAN1112': {'blocking': 0,
                                              'forwarding': 2,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 2},
                                'VLAN1113': {'blocking': 0,
                                              'forwarding': 2,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 2},
                                'VLAN1114': {'blocking': 0,
                                              'forwarding': 2,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 2},
                                'VLAN1115': {'blocking': 0,
                                              'forwarding': 2,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 2},
                                'VLAN1116': {'blocking': 0,
                                              'forwarding': 2,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 2},
                                'VLAN1125': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN1506': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN1509': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1},
                                'VLAN1601': {'blocking': 0,
                                              'forwarding': 1,
                                              'learning': 0,
                                              'listening': 0,
                                              'stp_active': 1}}},
            'portfast_default': False,
            'pvst_simulation': True,
            'pvst_simulation_status': 'inactive',
            'root_bridge_for': 'VLAN0001, VLAN0115-VLAN0116, VLAN0118-VLAN0119, VLAN0121, '
                                'VLAN0180, VLAN0501-VLAN0503, VLAN0506, VLAN0508-VLAN0518, '
                                'VLAN0521-VLAN0522, VLAN0540, VLAN0601-VLAN0604, VLAN0606, '
                                'VLAN0701, VLAN0801-VLAN0806, VLAN1111-VLAN1116, VLAN1506, '
                                'VLAN1509, VLAN1601',
            'total_statistics': {'blockings': 0,
                              'forwardings': 62,
                              'learnings': 0,
                              'listenings': 0,
                              'num_of_vlans': 48,
                              'stp_actives': 62},
            'uplink_fast': False
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowSpanningTreeSummary(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_mst(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_mstp)
        obj = ShowSpanningTreeSummary(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_mstp)

    def test_golden_single_mst(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_mstp_single_mst)
        obj = ShowSpanningTreeSummary(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_mstp_single_mst)

    def test_golden_pvst(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_pvst)
        obj = ShowSpanningTreeSummary(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_pvst)

    def test_golden_rpvst(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_rpvst)
        obj = ShowSpanningTreeSummary(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_rpvst)

    def test_golden_1(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_1)
        obj = ShowSpanningTreeSummary(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_1)

class test_show_spanning_tree_detail(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output_mstp = {
        "mstp": {
              "mst_instances": {
                   0: {
                        "hello_timer": 0,
                        "notification_timer": 0,
                        "bridge_sysid": 0,
                        "forwarding_delay": 30,
                        "hello_time": 10,
                        "topology_change_timer": 0,
                        "time_since_topology_change": "03:09:48",
                        "notification_times": 10,
                        "mst_id": 0,
                        "topology_change_flag": False,
                        "root_of_spanning_tree": True,
                        "hold_time": 1,
                        "topology_changes": 3,
                        "bridge_address": "d8b1.9009.bf80",
                        "interfaces": {
                             "Port-channel24": {
                                  "number_of_forward_transitions": 1,
                                  "designated_port_id": "128.2400",
                                  "status": "designated forwarding",
                                  "designated_bridge_priority": 32768,
                                  "forward_delay": 0,
                                  "designated_bridge_address": "d8b1.9009.bf80",
                                  "designated_path_cost": 0,
                                  "designated_root_priority": 32768,
                                  "port_identifier": "128.2400.",
                                  "cost": 6660,
                                  "counters": {
                                       "bpdu_sent": 1099019,
                                       "bpdu_received": 2191582
                                  },
                                  "designated_root_address": "d8b1.9009.bf80",
                                  "boundary": "PVST",
                                  "port_num": 2400,
                                  "port_priority": 128,
                                  "name": "Port-channel24",
                                  "hold": 0,
                                  "message_age": 0,
                                  "link_type": "point-to-point",
                                  "loop_guard": True
                             },
                             "Port-channel14": {
                                  "number_of_forward_transitions": 0,
                                  "designated_port_id": "128.2390",
                                  "status": "broken  (PVST Sim. Inconsistent)",
                                  "designated_bridge_priority": 32768,
                                  "forward_delay": 0,
                                  "designated_bridge_address": "d8b1.9009.bf80",
                                  "designated_path_cost": 0,
                                  "designated_root_priority": 32768,
                                  "port_identifier": "128.2390.",
                                  "cost": 6660,
                                  "counters": {
                                       "bpdu_sent": 138231,
                                       "bpdu_received": 167393
                                  },
                                  "designated_root_address": "d8b1.9009.bf80",
                                  "boundary": "PVST",
                                  "port_num": 2390,
                                  "port_priority": 128,
                                  "name": "Port-channel14",
                                  "hold": 0,
                                  "message_age": 0,
                                  "link_type": "point-to-point",
                                  "loop_guard": True
                             }
                        },
                        "topology_change_times": 70,
                        "topology_from_port": "Port-channel24",
                        "bridge_priority": 32768,
                        "topology_detected_flag": False,
                        "max_age": 40,
                        "hold_count": 20
                   }
              },
              "forwarding_delay": 30,
              "hello_time": 10,
              "max_age": 40,
              "hold_count": 20
        }
    }
    golden_parsed_output_pvst = {
        "pvst": {
              "vlans": {
                   100: {
                        "topology_from_port": "Port-channel12",
                        "topology_detected_flag": False,
                        "topology_change_flag": False,
                        "bridge_address": "3820.565b.1b80",
                        "forwarding_delay": 15,
                        "topology_change_times": 35,
                        "hello_timer": 0,
                        "hello_time": 2,
                        "bridge_sysid": 100,
                        "aging_timer": 300,
                        "hold_time": 1,
                        "bridge_priority": 24576,
                        "notification_times": 2,
                        "topology_changes": 1,
                        "notification_timer": 0,
                        "root_of_spanning_tree": True,
                        "interfaces": {
                             "Port-channel12": {
                                  "designated_bridge_priority": 24676,
                                  "link_type": "point-to-point",
                                  "hold": 0,
                                  "counters": {
                                       "bpdu_sent": 183,
                                       "bpdu_received": 0
                                  },
                                  "port_num": 2388,
                                  "message_age": 0,
                                  "number_of_forward_transitions": 1,
                                  "designated_path_cost": 0,
                                  "forward_delay": 0,
                                  "name": "Port-channel12",
                                  "designated_root_priority": 24676,
                                  "designated_bridge_address": "3820.565b.1b80",
                                  "status": "designated forwarding",
                                  "port_identifier": "128.2388.",
                                  "designated_root_address": "3820.565b.1b80",
                                  "cost": 3,
                                  "port_priority": 128,
                                  "designated_port_id": "128.2388"
                             }
                        },
                        "vlan_id": 100,
                        "max_age": 20,
                        "topology_change_timer": 0,
                        "time_since_topology_change": "00:05:37"
                   }
              },
              "hello_time": 2,
              "max_age": 20,
              "forwarding_delay": 15
         }
    }

    golden_parsed_output_rapid_pvst = {
        "rapid_pvst": {
              "forwarding_delay": 15,
              "vlans": {
                   201: {
                        "forwarding_delay": 15,
                        "hello_timer": 0,
                        "bridge_sysid": 201,
                        "hold_time": 1,
                        "time_since_topology_change": "00:00:14",
                        "notification_timer": 0,
                        "topology_change_flag": True,
                        "topology_changes": 1,
                        "topology_change_times": 35,
                        "aging_timer": 300,
                        "topology_from_port": "Port-channel14",
                        "topology_change_timer": 21,
                        "bridge_address": "ecbd.1d09.5680",
                        "notification_times": 2,
                        "bridge_priority": 28672,
                        "topology_detected_flag": False,
                        "hello_time": 2,
                        "interfaces": {
                             "GigabitEthernet1/0/5": {
                                  "designated_bridge_address": "ecbd.1d09.5680",
                                  "number_of_forward_transitions": 1,
                                  "port_identifier": "128.5.",
                                  "counters": {
                                       "bpdu_received": 4,
                                       "bpdu_sent": 20
                                  },
                                  "cost": 4,
                                  "designated_port_id": "128.5",
                                  "designated_root_priority": 24777,
                                  "designated_root_address": "58bf.eab6.2f00",
                                  "port_num": 5,
                                  "status": "designated forwarding",
                                  "port_priority": 128,
                                  "forward_delay": 0,
                                  "hold": 0,
                                  "message_age": 0,
                                  "peer": "STP",
                                  "link_type": "point-to-point",
                                  "designated_bridge_priority": 28873,
                                  "designated_path_cost": 3,
                                  "name": "GigabitEthernet1/0/5"
                             }
                        },
                        "max_age": 20,
                        "hold_count": 6,
                        "vlan_id": 201
                   },
                   100: {
                        "forwarding_delay": 15,
                        "hello_timer": 0,
                        "bridge_sysid": 100,
                        "hold_time": 1,
                        "time_since_topology_change": "00:00:34",
                        "notification_timer": 0,
                        "hello_time": 2,
                        "topology_change_flag": True,
                        "topology_changes": 1,
                        "notification_times": 2,
                        "aging_timer": 300,
                        "topology_from_port": "Port-channel12",
                        "topology_change_timer": 0,
                        "bridge_address": "3820.565b.1b80",
                        "topology_change_times": 35,
                        "bridge_priority": 24576,
                        "topology_detected_flag": False,
                        "root_of_spanning_tree": True,
                        "interfaces": {
                             "Port-channel12": {
                                  "designated_bridge_address": "3820.565b.1b80",
                                  "number_of_forward_transitions": 1,
                                  "port_identifier": "128.2388.",
                                  "counters": {
                                       "bpdu_received": 0,
                                       "bpdu_sent": 34
                                  },
                                  "cost": 3,
                                  "designated_port_id": "128.2388",
                                  "designated_root_priority": 24676,
                                  "designated_root_address": "3820.565b.1b80",
                                  "port_num": 2388,
                                  "status": "designated forwarding",
                                  "port_priority": 128,
                                  "forward_delay": 0,
                                  "hold": 0,
                                  "message_age": 0,
                                  "link_type": "point-to-point",
                                  "designated_bridge_priority": 24676,
                                  "designated_path_cost": 0,
                                  "name": "Port-channel12"
                             }
                        },
                        "max_age": 20,
                        "hold_count": 6,
                        "vlan_id": 100
                   }
              },
              "max_age": 20,
              "hold_count": 6,
              "hello_time": 2
         }
    }

    golden_output_mstp = {'execute.return_value': '''\
        MST0 is executing the mstp compatible Spanning Tree protocol
          Bridge Identifier has priority 32768, sysid 0, address d8b1.9009.bf80
          Configured hello time 10, max age 40, forward delay 30, transmit hold-count 20
          We are the root of the spanning tree
          Topology change flag not set, detected flag not set
          Number of topology changes 3 last change occurred 03:09:48 ago
                  from Port-channel24
          Times:  hold 1, topology change 70, notification 10
                  hello 10, max age 40, forward delay 30 
          Timers: hello 0, topology change 0, notification 0

         Port 2390 (Port-channel14) of MST0 is broken  (PVST Sim. Inconsistent)
           Port path cost 6660, Port priority 128, Port Identifier 128.2390.
           Designated root has priority 32768, address d8b1.9009.bf80
           Designated bridge has priority 32768, address d8b1.9009.bf80
           Designated port id is 128.2390, designated path cost 0
           Timers: message age 0, forward delay 0, hold 0
           Number of transitions to forwarding state: 0
           Link type is point-to-point by default, Boundary PVST
           Loop guard is enabled by default on the port
           BPDU: sent 138231, received 167393

         Port 2400 (Port-channel24) of MST0 is designated forwarding 
           Port path cost 6660, Port priority 128, Port Identifier 128.2400.
           Designated root has priority 32768, address d8b1.9009.bf80
           Designated bridge has priority 32768, address d8b1.9009.bf80
           Designated port id is 128.2400, designated path cost 0
           Timers: message age 0, forward delay 0, hold 0
           Number of transitions to forwarding state: 1
           Link type is point-to-point by default, Boundary PVST
           Loop guard is enabled by default on the port
           BPDU: sent 1099019, received 2191582
    '''
    }

    golden_output_pvst = {'execute.return_value': '''\
        VLAN0100 is executing the ieee compatible Spanning Tree protocol
          Bridge Identifier has priority 24576, sysid 100, address 3820.565b.1b80
          Configured hello time 2, max age 20, forward delay 15
          We are the root of the spanning tree
          Topology change flag not set, detected flag not set
          Number of topology changes 1 last change occurred 00:05:37 ago
                  from Port-channel12
          Times:  hold 1, topology change 35, notification 2
                  hello 2, max age 20, forward delay 15 
          Timers: hello 0, topology change 0, notification 0, aging 300

         Port 2388 (Port-channel12) of VLAN0100 is designated forwarding 
           Port path cost 3, Port priority 128, Port Identifier 128.2388.
           Designated root has priority 24676, address 3820.565b.1b80
           Designated bridge has priority 24676, address 3820.565b.1b80
           Designated port id is 128.2388, designated path cost 0
           Timers: message age 0, forward delay 0, hold 0
           Number of transitions to forwarding state: 1
           Link type is point-to-point by default
           BPDU: sent 183, received 0

    '''
    }

    golden_output_rapid_pvst = {'execute.return_value': '''\
        VLAN0100 is executing the rstp compatible Spanning Tree protocol
          Bridge Identifier has priority 24576, sysid 100, address 3820.565b.1b80
          Configured hello time 2, max age 20, forward delay 15, transmit hold-count 6
          We are the root of the spanning tree
          Topology change flag set, detected flag not set
          Number of topology changes 1 last change occurred 00:00:34 ago
                  from Port-channel12
          Times:  hold 1, topology change 35, notification 2
                  hello 2, max age 20, forward delay 15 
          Timers: hello 0, topology change 0, notification 0, aging 300

         Port 2388 (Port-channel12) of VLAN0100 is designated forwarding 
           Port path cost 3, Port priority 128, Port Identifier 128.2388.
           Designated root has priority 24676, address 3820.565b.1b80
           Designated bridge has priority 24676, address 3820.565b.1b80
           Designated port id is 128.2388, designated path cost 0
           Timers: message age 0, forward delay 0, hold 0
           Number of transitions to forwarding state: 1
           Link type is point-to-point by default
           BPDU: sent 34, received 0

        VLAN0201 is executing the rstp compatible Spanning Tree protocol
          Bridge Identifier has priority 28672, sysid 201, address ecbd.1d09.5680
          Configured hello time 2, max age 20, forward delay 15, transmit hold-count 6
          Current root has priority 24777, address 58bf.eab6.2f00
          Root port is 2390 (Port-channel14), cost of root path is 3
          Topology change flag set, detected flag not set
          Number of topology changes 1 last change occurred 00:00:14 ago
                  from Port-channel14
          Times:  hold 1, topology change 35, notification 2
                  hello 2, max age 20, forward delay 15 
          Timers: hello 0, topology change 21, notification 0, aging 300

         Port 5 (GigabitEthernet1/0/5) of VLAN0201 is designated forwarding 
           Port path cost 4, Port priority 128, Port Identifier 128.5.
           Designated root has priority 24777, address 58bf.eab6.2f00
           Designated bridge has priority 28873, address ecbd.1d09.5680
           Designated port id is 128.5, designated path cost 3
           Timers: message age 0, forward delay 0, hold 0
           Number of transitions to forwarding state: 1
           Link type is point-to-point by default, Peer is STP
           BPDU: sent 20, received 4

    '''
    }
    golden_output_1 = {'execute.return_value': '''\
        VLAN0001 is executing the rstp compatible Spanning Tree protocol
          Bridge Identifier has priority 24576, sysid 1, address 000e.3962.0f40
          Configured hello time 2, max age 20, forward delay 15, tranmsit hold-count 6
          We are the root of the spanning tree
          Topology change flag not set, detected flag not set
          Number of topology changes 10 last change occurred 38w1d ago
                  from GigabitEthernet8/10
          Times:  hold 1, topology change 35, notification 2
                  hello 2, max age 20, forward delay 15 
          Timers: hello 0, topology change 0, notification 0, aging 480

         Port 1671 (Port-channel220) of VLAN0001 is designated forwarding 
           Port path cost 1, Port priority 128, Port Identifier 128.1671.
           Designated root has priority 24577, address 000e.3962.0f40
           Designated bridge has priority 24577, address 000e.3962.0f40
           Designated port id is 128.1671, designated path cost 0
           Timers: message age 0, forward delay 0, hold 0
           Number of transitions to forwarding state: 1
           Link type is point-to-point by default
           BPDU: sent 20120147, received 0

         Port 1673 (Port-channel265) of VLAN0001 is designated forwarding 
           Port path cost 3, Port priority 128, Port Identifier 128.1673.
           Designated root has priority 24577, address 000e.3962.0f40
           Designated bridge has priority 24577, address 000e.3962.0f40
           Designated port id is 128.1673, designated path cost 0
           Timers: message age 0, forward delay 0, hold 0
           Number of transitions to forwarding state: 1
           The port is in the portfast edge trunk mode
           Link type is point-to-point by default
           BPDU: sent 21320048, received 0

                  
        VLAN0115 is executing the rstp compatible Spanning Tree protocol
          Bridge Identifier has priority 24576, sysid 115, address 000e.3962.0f40
          Configured hello time 2, max age 20, forward delay 15, tranmsit hold-count 6
          We are the root of the spanning tree
          Topology change flag not set, detected flag not set
          Number of topology changes 2 last change occurred 33w6d ago
                  from Port-channel210
          Times:  hold 1, topology change 35, notification 2
                  hello 2, max age 20, forward delay 15 
          Timers: hello 0, topology change 0, notification 0, aging 480

         Port 1670 (Port-channel210) of VLAN0115 is designated forwarding 
           Port path cost 2, Port priority 128, Port Identifier 128.1670.
           Designated root has priority 24691, address 000e.3962.0f40
           Designated bridge has priority 24691, address 000e.3962.0f40
           Designated port id is 128.1670, designated path cost 0
           Timers: message age 0, forward delay 0, hold 0
           Number of transitions to forwarding state: 1
           Link type is point-to-point by default
           BPDU: sent 10172865, received 4

                  
        VLAN0116 is executing the rstp compatible Spanning Tree protocol
          Bridge Identifier has priority 24576, sysid 116, address 000e.3962.0f40
          Configured hello time 2, max age 20, forward delay 15, tranmsit hold-count 6
          We are the root of the spanning tree
          Topology change flag not set, detected flag not set
          Number of topology changes 2 last change occurred 33w6d ago
                  from Port-channel210
          Times:  hold 1, topology change 35, notification 2
                  hello 2, max age 20, forward delay 15 
          Timers: hello 0, topology change 0, notification 0, aging 480

         Port 1670 (Port-channel210) of VLAN0116 is designated forwarding 
           Port path cost 2, Port priority 128, Port Identifier 128.1670.
           Designated root has priority 24692, address 000e.3962.0f40
           Designated bridge has priority 24692, address 000e.3962.0f40
           Designated port id is 128.1670, designated path cost 0
           Timers: message age 0, forward delay 0, hold 0
           Number of transitions to forwarding state: 1
           Link type is point-to-point by default
           BPDU: sent 10172829, received 4

                  
        VLAN0118 is executing the rstp compatible Spanning Tree protocol
          Bridge Identifier has priority 24576, sysid 118, address 000e.3962.0f40
          Configured hello time 2, max age 20, forward delay 15, tranmsit hold-count 6
          We are the root of the spanning tree
          Topology change flag not set, detected flag not set
          Number of topology changes 2 last change occurred 33w6d ago
                  from Port-channel210
          Times:  hold 1, topology change 35, notification 2
                  hello 2, max age 20, forward delay 15 
          Timers: hello 0, topology change 0, notification 0, aging 480

         Port 1670 (Port-channel210) of VLAN0118 is designated forwarding 
           Port path cost 2, Port priority 128, Port Identifier 128.1670.
           Designated root has priority 24694, address 000e.3962.0f40
           Designated bridge has priority 24694, address 000e.3962.0f40
           Designated port id is 128.1670, designated path cost 0
           Timers: message age 0, forward delay 0, hold 0
           Number of transitions to forwarding state: 1
           Link type is point-to-point by default
           BPDU: sent 10172791, received 4
        '''
    }

    golden_parsed_output_1 = {
        'rapid_pvst': {
            'forwarding_delay': 15,
            'hello_time': 2,
            'hold_count': 6,
            'max_age': 20,
            'vlans': {
                1: {
                    'aging_timer': 480,
                    'bridge_address': '000e.3962.0f40',
                    'bridge_priority': 24576,
                    'bridge_sysid': 1,
                    'forwarding_delay': 15,
                    'hello_time': 2,
                    'hello_timer': 0,
                    'hold_count': 6,
                    'hold_time': 1,
                    'interfaces': {
                        'Port-channel220': {
                            'cost': 1,
                            'counters': {
                                'bpdu_received': 0,
                                'bpdu_sent': 20120147
                            },
                            'designated_bridge_address': '000e.3962.0f40',
                            'designated_bridge_priority': 24577,
                            'designated_path_cost': 0,
                            'designated_port_id': '128.1671',
                            'designated_root_address': '000e.3962.0f40',
                            'designated_root_priority': 24577,
                            'forward_delay': 0,
                            'hold': 0,
                            'link_type': 'point-to-point',
                            'message_age': 0,
                            'name': 'Port-channel220',
                            'number_of_forward_transitions': 1,
                            'port_identifier': '128.1671.',
                            'port_num': 1671,
                            'port_priority': 128,
                            'status': 
                                'designated '
                                'forwarding'
                        },
                        'Port-channel265': {
                            'cost': 3,
                            'counters': {
                                'bpdu_received': 0,
                                'bpdu_sent': 21320048
                            },
                            'designated_bridge_address': '000e.3962.0f40',
                            'designated_bridge_priority': 24577,
                            'designated_path_cost': 0,
                            'designated_port_id': '128.1673',
                            'designated_root_address': '000e.3962.0f40',
                            'designated_root_priority': 24577,
                            'forward_delay': 0,
                            'hold': 0,
                            'link_type': 'point-to-point',
                            'message_age': 0,
                            'name': 'Port-channel265',
                            'number_of_forward_transitions': 1,
                            'port_identifier': '128.1673.',
                            'port_num': 1673,
                            'port_priority': 128,
                            'status': 
                                'designated '
                                'forwarding'
                            }
                        },
                        'max_age': 20,
                        'notification_timer': 0,
                        'notification_times': 2,
                        'root_of_spanning_tree': True,
                        'time_since_topology_change': '38w1d',
                        'topology_change_flag': False,
                        'topology_change_timer': 0,
                        'topology_change_times': 35,
                        'topology_changes': 10,
                        'topology_detected_flag': False,
                        'topology_from_port': 'GigabitEthernet8/10',
                        'vlan_id': 1
                },
                115: {
                    'aging_timer': 480,
                    'bridge_address': '000e.3962.0f40',
                    'bridge_priority': 24576,
                    'bridge_sysid': 115,
                    'forwarding_delay': 15,
                    'hello_time': 2,
                    'hello_timer': 0,
                    'hold_count': 6,
                    'hold_time': 1,
                    'interfaces': {
                        'Port-channel210': {
                            'cost': 2,
                            'counters': {
                                'bpdu_received': 4,
                                'bpdu_sent': 10172865
                            },
                           'designated_bridge_address': '000e.3962.0f40',
                           'designated_bridge_priority': 24691,
                           'designated_path_cost': 0,
                           'designated_port_id': '128.1670',
                           'designated_root_address': '000e.3962.0f40',
                           'designated_root_priority': 24691,
                           'forward_delay': 0,
                           'hold': 0,
                           'link_type': 'point-to-point',
                           'message_age': 0,
                           'name': 'Port-channel210',
                           'number_of_forward_transitions': 1,
                           'port_identifier': '128.1670.',
                           'port_num': 1670,
                           'port_priority': 128,
                           'status':
                                'designated '
                                'forwarding'
                        }
                    },
                    'max_age': 20,
                    'notification_timer': 0,
                    'notification_times': 2,
                    'root_of_spanning_tree': True,
                    'time_since_topology_change': '33w6d',
                    'topology_change_flag': False,
                    'topology_change_timer': 0,
                    'topology_change_times': 35,
                    'topology_changes': 2,
                    'topology_detected_flag': False,
                    'topology_from_port': 'Port-channel210',
                    'vlan_id': 115
                },
                116: {
                    'aging_timer': 480,
                    'bridge_address': '000e.3962.0f40',
                    'bridge_priority': 24576,
                    'bridge_sysid': 116,
                    'forwarding_delay': 15,
                    'hello_time': 2,
                    'hello_timer': 0,
                    'hold_count': 6,
                    'hold_time': 1,
                    'interfaces': {
                        'Port-channel210': {
                            'cost': 2,
                            'counters': {
                                'bpdu_received': 4,
                                'bpdu_sent': 10172829
                            },
                           'designated_bridge_address': '000e.3962.0f40',
                           'designated_bridge_priority': 24692,
                           'designated_path_cost': 0,
                           'designated_port_id': '128.1670',
                           'designated_root_address': '000e.3962.0f40',
                           'designated_root_priority': 24692,
                           'forward_delay': 0,
                           'hold': 0,
                           'link_type': 'point-to-point',
                           'message_age': 0,
                           'name': 'Port-channel210',
                           'number_of_forward_transitions': 1,
                           'port_identifier': '128.1670.',
                           'port_num': 1670,
                           'port_priority': 128,
                           'status': 'designated '
                                     'forwarding'
                            }
                        },
                        'max_age': 20,
                        'notification_timer': 0,
                        'notification_times': 2,
                        'root_of_spanning_tree': True,
                        'time_since_topology_change': '33w6d',
                        'topology_change_flag': False,
                        'topology_change_timer': 0,
                        'topology_change_times': 35,
                        'topology_changes': 2,
                        'topology_detected_flag': False,
                        'topology_from_port': 'Port-channel210',
                        'vlan_id': 116
                    },
                    118: {
                        'aging_timer': 480,
                        'bridge_address': '000e.3962.0f40',
                        'bridge_priority': 24576,
                        'bridge_sysid': 118,
                        'forwarding_delay': 15,
                        'hello_time': 2,
                        'hello_timer': 0,
                        'hold_count': 6,
                        'hold_time': 1,
                        'interfaces': {
                            'Port-channel210': {
                                'cost': 2,
                                'counters': {
                                    'bpdu_received': 4,
                                    'bpdu_sent': 10172791
                                },
                               'designated_bridge_address': '000e.3962.0f40',
                               'designated_bridge_priority': 24694,
                               'designated_path_cost': 0,
                               'designated_port_id': '128.1670',
                               'designated_root_address': '000e.3962.0f40',
                               'designated_root_priority': 24694,
                               'forward_delay': 0,
                               'hold': 0,
                               'link_type': 'point-to-point',
                               'message_age': 0,
                               'name': 'Port-channel210',
                               'number_of_forward_transitions': 1,
                               'port_identifier': '128.1670.',
                               'port_num': 1670,
                               'port_priority': 128,
                               'status': 'designated '
                                         'forwarding'
                            }
                        },
                        'max_age': 20,
                        'notification_timer': 0,
                        'notification_times': 2,
                        'root_of_spanning_tree': True,
                        'time_since_topology_change': '33w6d',
                        'topology_change_flag': False,
                        'topology_change_timer': 0,
                        'topology_change_times': 35,
                        'topology_changes': 2,
                        'topology_detected_flag': False,
                        'topology_from_port': 'Port-channel210',
                        'vlan_id': 118
                    }
                }
            }
        }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowSpanningTreeDetail(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()    

    def test_golden_mstp(self):
        self.dev_c3850 = Mock(**self.golden_output_mstp)
        obj = ShowSpanningTreeDetail(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_mstp)    

    def test_golden_pvst(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_pvst)
        obj = ShowSpanningTreeDetail(device=self.dev_c3850)
        parsed_output = obj.parse()

        self.assertEqual(parsed_output,self.golden_parsed_output_pvst)    

    def test_golden_rapid_pvst(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_rapid_pvst)
        obj = ShowSpanningTreeDetail(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_rapid_pvst)

    def test_golden_1(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_1)
        obj = ShowSpanningTreeDetail(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_1)

class test_show_spanning_tree_mst_detail(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        "mst_instances": {
            0: {
               "bridge_priority": 32768,
               "interfaces": {
                    "GigabitEthernet1/0/23": {
                         "designated_regional_root_cost": 0,
                         "port_priority": 128,
                         "designated_root_priority": 32768,
                         "designated_bridge_port_id": "128.23",
                         "designated_bridge_priority": 32768,
                         "forward_delay": 0,
                         "port_id": "128.23",
                         "name": "GigabitEthernet1/0/23",
                         "designated_regional_root_priority": 32768,
                         "forward_transitions": 1,
                         "counters": {
                              "bpdu_sent": 493,
                              "bpdu_received": 0
                         },
                         "designated_regional_root_address": "3820.565b.8600",
                         "status": "designated forwarding",
                         "designated_root_cost": 0,
                         "designated_bridge_address": "3820.565b.8600",
                         "designated_root_address": "3820.565b.8600",
                         "cost": 20000,
                         "message_expires": 0
                    }
               },
               "operational": {
                    "max_age": 35,
                    "tx_hold_count": 20,
                    "hello_time": 10,
                    "forward_delay": 30
               },
               "sysid": 0,
               "root": "CIST",
               "bridge_address": "3820.565b.8600",
               "configured": {
                    "max_age": 35,
                    "forward_delay": 30,
                    "hello_time": 10,
                    "max_hops": 10
               },
               "mst_id": 0,
               "vlan": "1-99,201-4094"
            },
            10: {
               "bridge_priority": 61450,
               "interfaces": {
                    "GigabitEthernet1/0/23": {
                         "port_priority": 128,
                         "designated_root_priority": 61450,
                         "designated_bridge_port_id": "128.23",
                         "designated_bridge_priority": 61450,
                         "forward_delay": 0,
                         "port_id": "128.23",
                         "name": "GigabitEthernet1/0/23",
                         "forward_transitions": 1,
                         "counters": {
                              "bpdu_sent": 493,
                              "bpdu_received": 0
                         },
                         "message_expires": 0,
                         "status": "designated forwarding",
                         "designated_root_cost": 0,
                         "designated_bridge_address": "3820.565b.8600",
                         "designated_root_address": "3820.565b.8600",
                         "cost": 20000
                    }
               },
               "sysid": 10,
               "root": "MST10",
               "bridge_address": "3820.565b.8600",
               "mst_id": 10,
               "vlan": "100-200"
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        ##### MST0    vlans mapped:   1-99,201-4094
        Bridge        address 3820.565b.8600  priority      32768 (32768 sysid 0)
        Root          this switch for the CIST
        Operational   hello time 10, forward delay 30, max age 35, txholdcount 20
        Configured    hello time 10, forward delay 30, max age 35, max hops    10

        GigabitEthernet1/0/23 of MST0 is designated forwarding 
        Port info             port id         128.23  priority    128  cost       20000
        Designated root       address 3820.565b.8600  priority  32768  cost           0
        Design. regional root address 3820.565b.8600  priority  32768  cost           0
        Designated bridge     address 3820.565b.8600  priority  32768  port id   128.23
        Timers: message expires in 0 sec, forward delay 0, forward transitions 1
        Bpdus sent 493, received 0

        ##### MST10   vlans mapped:   100-200
        Bridge        address 3820.565b.8600  priority      61450 (61440 sysid 10)
        Root          this switch for MST10

        GigabitEthernet1/0/23 of MST10 is designated forwarding 
        Port info             port id         128.23  priority    128  cost       20000
        Designated root       address 3820.565b.8600  priority  61450  cost           0
        Designated bridge     address 3820.565b.8600  priority  61450  port id   128.23
        Timers: message expires in 0 sec, forward delay 0, forward transitions 1
        Bpdus (MRecords) sent 493, received 0
    '''
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowSpanningTreeMstDetail(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()    

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowSpanningTreeMstDetail(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


class test_show_errdisable_recovery(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        "bpduguard_timeout_recovery": 333,
        "timer_status": {
          "gbic-invalid": False,
          "oam-remote-failure": False,
          "arp-inspection": False,
          "dtp-flap": False,
          "port-mode-failure": False,
          "loopback": False,
          "mac-limit": False,
          "psp": False,
          "channel-misconfig (STP)": False,
          "l2ptguard": False,
          "Recovery command: \"clear": False,
          "link-monitor-failure": False,
          "vmps": False,
          "bpduguard": False,
          "sfp-config-mismatch": False,
          "dual-active-recovery": False,
          "pagp-flap": False,
          "security-violation": False,
          "storm-control": False,
          "psecure-violation": False,
          "udld": False,
          "inline-power": False,
          "link-flap": False,
          "evc-lite input mapping fa": False,
          "pppoe-ia-rate-limit": False,
          "dhcp-rate-limit": False
        },
        "interfaces": {
            "FastEthernet2/4": {
                'interface': "FastEthernet2/4",
                'errdisable_reason': 'bpduguard',
                'time_left': 273,
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        ErrDisable Reason            Timer Status
        -----------------            --------------
        arp-inspection               Disabled
        bpduguard                    Disabled
        channel-misconfig (STP)      Disabled
        dhcp-rate-limit              Disabled
        dtp-flap                     Disabled
        gbic-invalid                 Disabled
        inline-power                 Disabled
        l2ptguard                    Disabled
        link-flap                    Disabled
        mac-limit                    Disabled
        link-monitor-failure         Disabled
        loopback                     Disabled
        oam-remote-failure           Disabled
        pagp-flap                    Disabled
        port-mode-failure            Disabled
        pppoe-ia-rate-limit          Disabled
        psecure-violation            Disabled
        security-violation           Disabled
        sfp-config-mismatch          Disabled
        storm-control                Disabled
        udld                         Disabled
        vmps                         Disabled
        psp                          Disabled
        dual-active-recovery         Disabled
        evc-lite input mapping fa    Disabled
        Recovery command: "clear     Disabled

        Timer interval: 333 seconds

        Interfaces that will be enabled at the next timeout:

        Interface      Errdisable reason      Time left(sec)
        ---------    ---------------------    --------------
          Fa2/4                bpduguard          273
    '''
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowErrdisableRecovery(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()    

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowErrdisableRecovery(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


class test_show_spanning_tree(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output_mstp = {
        "mstp": {
          "mst_instances": {
               0: {
                    "bridge": {
                         "hello_time": 7,
                         "priority": 32768,
                         "forward_delay": 15,
                         "address": "ecbd.1d09.5680",
                         "max_age": 12,
                         "configured_bridge_priority": 32768,
                         "sys_id_ext": 0,
                    },
                    "interfaces": {
                         "GigabitEthernet1/0/5": {
                              "port_state": "forwarding",
                              "bound": "RSTP",
                              "port_num": 5,
                              "port_priority": 128,
                              "type": "P2p",
                              "cost": 20000,
                              "role": "root"
                         },
                         "Port-channel14": {
                              "port_state": "broken",
                              "bound": "PVST",
                              "port_num": 2390,
                              "port_priority": 128,
                              "type": "P2p",
                              "cost": 6660,
                              "role": "designated"
                         },
                         "Port-channel24": {
                              "port_state": "forwarding",
                              "bound": "PVST",
                              "port_num": 2400,
                              "port_priority": 128,
                              "type": "P2p",
                              "cost": 6660,
                              "role": "designated"
                         }
                    },
                    "root": {
                         "hello_time": 10,
                         "priority": 32768,
                         "forward_delay": 30,
                         "max_age": 35,
                         "cost": 20000,
                         "address": "3820.565b.8600",
                         "interface": "GigabitEthernet1/0/5",
                         "port": 5
                    }
               },
               10: {
                    "bridge": {
                         "hello_time": 7,
                         "priority": 61450,
                         "forward_delay": 15,
                         "address": "ecbd.1d09.5680",
                         "max_age": 12,
                         "configured_bridge_priority": 61440,
                         "sys_id_ext": 10,
                    },
                    "interfaces": {
                         "GigabitEthernet1/0/5": {
                              "port_state": "forwarding",
                              "bound": "RSTP",
                              "port_num": 5,
                              "port_priority": 128,
                              "type": "P2p",
                              "cost": 20000,
                              "role": "master "
                         },
                         "Port-channel14": {
                              "port_state": "broken",
                              "bound": "PVST",
                              "port_num": 2390,
                              "port_priority": 128,
                              "type": "P2p",
                              "cost": 6660,
                              "role": "designated"
                         }
                    },
                    "root": {
                         "hello_time": 10,
                         "priority": 61450,
                         "forward_delay": 30,
                         "address": "ecbd.1d09.5680",
                         "max_age": 35
                    }
               }
            }
        }
    }

    golden_parsed_output_rstp = {
        "rapid_pvst": {
          "vlans": {
               200: {
                    "bridge": {
                         "hello_time": 2,
                         "priority": 28872,
                         "forward_delay": 15,
                         "max_age": 20,
                         "aging_time": 300,
                         "address": "ecbd.1d09.5680",
                         "configured_bridge_priority": 28672,
                         "sys_id_ext": 200,
                    },
                    "interfaces": {
                         "GigabitEthernet1/0/5": {
                              "peer": "STP",
                              "port_state": "forwarding",
                              "port_num": 5,
                              "port_priority": 128,
                              "type": "P2p",
                              "cost": 4,
                              "role": "designated"
                         },
                         "Port-channel14": {
                              "port_state": "forwarding",
                              "port_num": 2390,
                              "port_priority": 128,
                              "type": "P2p",
                              "cost": 3,
                              "role": "root"
                         }
                    },
                    "root": {
                         "hello_time": 2,
                         "priority": 24776,
                         "forward_delay": 15,
                         "max_age": 20,
                         "cost": 3,
                         "address": "58bf.eab6.2f00",
                         "interface": "Port-channel14",
                         "port": 2390
                    }
               },
               201: {
                    "bridge": {
                         "hello_time": 2,
                         "priority": 28873,
                         "forward_delay": 15,
                         "max_age": 20,
                         "aging_time": 300,
                         "address": "ecbd.1d09.5680",
                         "configured_bridge_priority": 28672,
                         "sys_id_ext": 201,
                    },
                    "interfaces": {
                         "GigabitEthernet1/0/5": {
                              "peer": "STP",
                              "port_state": "forwarding",
                              "port_num": 5,
                              "port_priority": 128,
                              "type": "P2p",
                              "cost": 4,
                              "role": "designated"
                         },
                         "Port-channel14": {
                              "port_state": "forwarding",
                              "port_num": 2390,
                              "port_priority": 128,
                              "type": "P2p",
                              "cost": 3,
                              "role": "root"
                         }
                    },
                    "root": {
                         "hello_time": 2,
                         "priority": 24777,
                         "forward_delay": 15,
                         "max_age": 20,
                         "cost": 3,
                         "address": "58bf.eab6.2f00",
                         "interface": "Port-channel14",
                         "port": 2390
                    }
               }
            }
        }
    }

    golden_output_mstp = {'execute.return_value': '''\
        MST0
          Spanning tree enabled protocol mstp
          Root ID    Priority    32768
                     Address     3820.565b.8600
                     Cost        20000
                     Port        5 (GigabitEthernet1/0/5)
                     Hello Time  10 sec  Max Age 35 sec  Forward Delay 30 sec

          Bridge ID  Priority    32768  (priority 32768 sys-id-ext 0)
                     Address     ecbd.1d09.5680
                     Hello Time   7 sec  Max Age 12 sec  Forward Delay 15 sec

        Interface           Role Sts Cost      Prio.Nbr Type
        ------------------- ---- --- --------- -------- --------------------------------
        Gi1/0/5             Root FWD 20000     128.5    P2p Bound(RSTP) 
        Po14                Desg BKN*6660      128.2390 P2p Bound(PVST) *PVST_Inc 
        Po24                Desg FWD 6660      128.2400 P2p Bound(PVST) 


                  
        MST10     
          Spanning tree enabled protocol mstp
          Root ID    Priority    61450
                     Address     ecbd.1d09.5680
                     This bridge is the root
                     Hello Time  10 sec  Max Age 35 sec  Forward Delay 30 sec
                  
          Bridge ID  Priority    61450  (priority 61440 sys-id-ext 10)
                     Address     ecbd.1d09.5680
                     Hello Time   7 sec  Max Age 12 sec  Forward Delay 15 sec
                  
        Interface           Role Sts Cost      Prio.Nbr Type
        ------------------- ---- --- --------- -------- --------------------------------
        Gi1/0/5             Mstr FWD 20000     128.5    P2p Bound(RSTP) 
        Po14                Desg BKN*6660      128.2390 P2p Bound(PVST) *PVST_Inc 
    '''
    }

    golden_output_rstp = {'execute.return_value': '''\
        VLAN0200
          Spanning tree enabled protocol rstp
          Root ID    Priority    24776
                     Address     58bf.eab6.2f00
                     Cost        3
                     Port        2390 (Port-channel14)
                     Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

          Bridge ID  Priority    28872  (priority 28672 sys-id-ext 200)
                     Address     ecbd.1d09.5680
                     Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
                     Aging Time  300 sec

        Interface           Role Sts Cost      Prio.Nbr Type
        ------------------- ---- --- --------- -------- --------------------------------
        Gi1/0/5             Desg FWD 4         128.5    P2p Peer(STP) 
        Po14                Root FWD 3         128.2390 P2p 


                  
        VLAN0201
          Spanning tree enabled protocol rstp
          Root ID    Priority    24777
                     Address     58bf.eab6.2f00
                     Cost        3
                     Port        2390 (Port-channel14)
                     Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

          Bridge ID  Priority    28873  (priority 28672 sys-id-ext 201)
                     Address     ecbd.1d09.5680
                     Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
                     Aging Time  300 sec

        Interface           Role Sts Cost      Prio.Nbr Type
        ------------------- ---- --- --------- -------- --------------------------------
        Gi1/0/5             Desg FWD 4         128.5    P2p Peer(STP) 
        Po14                Root FWD 3         128.2390 P2p 
    '''
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowSpanningTree(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()    

    def test_golden_mst(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_mstp)
        obj = ShowSpanningTree(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_mstp)  

    def test_golden_rstp(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_rstp)
        obj = ShowSpanningTree(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_rstp)


class test_show_spanning_tree_mst_configuration(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        "mstp": {
            "revision": 111,
            "name": "mst",
            "instances_configured": 2,
            "mst_instances": {
               10: {
                    "vlan_mapped": "100-200"
               },
               0: {
                    "vlan_mapped": "1-99,201-4094"
               }
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        Name      [mst]
        Revision  111   Instances configured 2

        Instance  Vlans mapped
        --------  ---------------------------------------------------------------------
        0         1-99,201-4094
        10        100-200
        -------------------------------------------------------------------------------
    '''
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowSpanningTreeMstConfiguration(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()    

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowSpanningTreeMstConfiguration(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()

