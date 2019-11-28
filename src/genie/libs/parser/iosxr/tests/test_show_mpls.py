# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_mpls
from genie.libs.parser.iosxr.show_mpls import (ShowMplsLdpNeighborBrief, 
                                                ShowMplsLabelTableDetail,
                                                ShowMplsInterfaces)


# ==================================================
#  Unit test for 'show mpls ldp neighbor brief'
# ==================================================

class test_show_mpls_ldp_neighbor_brief(unittest.TestCase):
    '''Unit test for 'show mpls ldp neighbor brief'''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'peer': {
            '10.16.2.2:0': {
                'addresses': {
                    'address': 5},
                'discovery': {
                        'discovery': 2},
                'gr': 'N',
                'up_time': '00:01:02'},
            '10.36.3.3:0': {
                'addresses': {
                    'address': 8},
                'discovery': {
                    'discovery': 3},
                'gr': 'Y',
                'up_time': '00:01:04'},
            '10.64.4.4:0': {
                'addresses': {
                    'ipv4': 3,
                    'ipv6': 0},
                'discovery': {
                    'ipv4': 1,
                    'ipv6': 0},
                'gr': 'Y',
                'labels': {
                    'ipv4': 5,
                    'ipv6': 0},
                'nsr': 'N',
                'up_time': '1d00h'},
            '10.49.46.2:0': {
                'addresses': {
                    'ipv4': 3,
                    'ipv6': 3},
                'discovery': {
                    'ipv4': 1,
                    'ipv6': 1},
                'gr': 'N',
                'labels': {
                    'ipv4': 5,
                    'ipv6': 5},
                'nsr': 'N',
                'up_time': '1d00h'},
            '10.49.46.46:0': {
                'addresses': {
                    'ipv4': 4,
                    'ipv6': 4},
                'discovery': {
                    'ipv4': 2,
                    'ipv6': 2},
                'gr': 'Y',
                'labels': {
                    'ipv4': 5,
                    'ipv6': 5},
                'nsr': 'N',
                'up_time': '1d00h'},
            '10.144.6.1:0': {
                'addresses': {
                    'ipv4': 0,
                    'ipv6': 2},
                'discovery': {
                    'ipv4': 0,
                    'ipv6': 1},
                    'gr': 'Y',
                'labels': {
                    'ipv4': 0,
                    'ipv6': 5},
                'nsr': 'N',
                'up_time': '23:25:50'}}}

    golden_output1 = {'execute.return_value': '''
        RP/0/0/CPU0:router# show mpls ldp neighbor brief

            Peer              GR Up Time         Discovery Address
            ----------------- -- --------------- --------- -------
            10.36.3.3:0         Y  00:01:04                3       8
            10.16.2.2:0         N  00:01:02                2       5


            Peer               GR  NSR  Up Time     Discovery   Addresses     Labels
                                                    ipv4  ipv6  ipv4  ipv6  ipv4   ipv6
            -----------------  --  ---  ----------  ----------  ----------  ------------
            10.64.4.4:0          Y   N    1d00h       1     0     3     0     5      0
            10.49.46.2:0       N   N    1d00h       1     1     3     3     5      5
            10.49.46.46:0      Y   N    1d00h       2     2     4     4     5      5
            10.144.6.1:0          Y   N    23:25:50    0     1     0     2     0      5
        '''}

    golden_parsed_output2 = {
        'peer': {
            '10.36.3.3:0': {
                'gr': 'Y',
                'up_time': '00:01:04',
                'discovery': {
                    'discovery': 3},
                'addresses': {
                    'address': 8}},
            '10.16.2.2:0': {
                'gr': 'N',
                'up_time': '00:01:02',
                'discovery': {'discovery': 2},
                'addresses': {'address': 5}}}}

    golden_output2 = {'execute.return_value': '''
        RP/0/RP0/CPU0:router# show mpls ldp neighbor brief
  
        Peer              GR Up Time         Discovery Address
        ----------------- -- --------------- --------- -------
        10.36.3.3:0         Y  00:01:04                3       8
        10.16.2.2:0         N  00:01:02                2       5
    '''}

    golden_parsed_output3 = {
        'peer': {
            '10.4.1.1:0': {
                'addresses': {
                    'ipv4': 9,
                    'ipv6': 0},
                'discovery': {
                    'ipv4': 1,
                    'ipv6': 0},
                'gr': 'N',
                'labels': {
                    'ipv4': 15,
                    'ipv6': 0},
                'nsr': 'N',
                'up_time': '00:08:57'}}}

    golden_output3 = {'execute.return_value': '''
         +++ R2_xr: executing command 'show mpls ldp neighbor brief' +++
         show mpls ldp neighbor brief
         Wed Apr 17 16:45:04.410 UTC
         
         Peer               GR  NSR  Up Time     Discovery   Addresses     Labels
                                                 ipv4  ipv6  ipv4  ipv6  ipv4   ipv6
         -----------------  --  ---  ----------  ----------  ----------  ------------
         10.4.1.1:0          N   N    00:08:57    1     0     9     0     15     0
    '''}

    def test_show_mpls_ldp_neighbor_brief_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowMplsLdpNeighborBrief(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_mpls_ldp_neighbor_brief_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowMplsLdpNeighborBrief(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_mpls_ldp_neighbor_brief_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowMplsLdpNeighborBrief(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_mpls_ldp_neighbor_brief_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowMplsLdpNeighborBrief(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output3)


# ==================================================
#  Unit test for 'show mpls label table detail'
# ==================================================

class test_show_mpls_ldp_neighbor_brief(unittest.TestCase):
    '''Unit test for 'show mpls ldp neighbor brief'''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'table': {
            0: {
                'label': {
                    0: {
                        'owner': 'LSD(A)',
                        'rewrite': 'Yes',
                        'state': 'InUse'},
                    1: {
                        'owner': 'LSD(A)',
                        'rewrite': 'Yes',
                        'state': 'InUse'},
                    2: {
                        'owner': 'LSD(A)',
                        'rewrite': 'Yes',
                        'state': 'InUse'},
                    13: {
                        'owner': 'LSD(A)',
                        'rewrite': 'Yes',
                        'state': 'InUse'},
                    16000: {
                        'label_type': {
                            'Lbl-blk SRGB': {
                                'size': 8000,
                                'start_label': 16000,
                                'vers': 0}
                        },
                        'owner': 'ISIS(A):SR',
                        'rewrite': 'No',
                        'state': 'InUse'},
                    24000: {
                        'label_type': {
                            'SR Adj Segment IPv4': {
                                'index': 0,
                                'interface': 'Gi0/0/0/1',
                                'nh': '10.1.2.2',
                                'type': 0,
                                'vers': 0}
                        },
                        'owner': 'ISIS(A):SR',
                        'rewrite': 'Yes',
                        'state': 'InUse'},
                    24001: {
                        'label_type': {
                            'SR Adj Segment IPv4': {
                                'index': 2,
                                'interface': 'Gi0/0/0/1',
                                'nh': '10.1.2.2',
                                'type': 0,
                                'vers': 0}
                        },
                        'owner': 'ISIS(A):SR',
                        'rewrite': 'Yes',
                        'state': 'InUse'},
                    24002: {
                        'label_type': {
                            'SR Adj Segment IPv4': {
                                'index': 1,
                                'interface': 'Gi0/0/0/1',
                                'nh': '10.1.2.2',
                                'type': 0,
                                'vers': 0}
                        },
                        'owner': 'ISIS(A):SR',
                        'rewrite': 'Yes',
                        'state': 'InUse'},
                    24003: {
                        'label_type': {
                            'SR Adj Segment IPv4': {
                                'index': 3,
                                'interface': 'Gi0/0/0/1',
                                'nh': '10.1.2.2',
                                'type': 0,
                                'vers': 0}
                        },
                        'owner': 'ISIS(A):SR',
                        'rewrite': 'Yes',
                        'state': 'InUse'}
                }
            }
        }
    }

    golden_output1 = {'execute.return_value': '''
        RP/0/RP0/CPU0:iosxrv9000-1#show mpls label table detail 
        Mon Sep 30 13:26:56.133 EDT
        Table Label   Owner                           State  Rewrite
        ----- ------- ------------------------------- ------ -------
        0     0       LSD(A)                          InUse  Yes
        0     1       LSD(A)                          InUse  Yes
        0     2       LSD(A)                          InUse  Yes
        0     13      LSD(A)                          InUse  Yes
        0     16000   ISIS(A):SR                      InUse  No
          (Lbl-blk SRGB, vers:0, (start_label=16000, size=8000)
        0     24000   ISIS(A):SR                      InUse  Yes
          (SR Adj Segment IPv4, vers:0, index=0, type=0, intf=Gi0/0/0/1, nh=10.1.2.2)
        0     24001   ISIS(A):SR                      InUse  Yes
          (SR Adj Segment IPv4, vers:0, index=2, type=0, intf=Gi0/0/0/1, nh=10.1.2.2)
        0     24002   ISIS(A):SR                      InUse  Yes
          (SR Adj Segment IPv4, vers:0, index=1, type=0, intf=Gi0/0/0/1, nh=10.1.2.2)
        0     24003   ISIS(A):SR                      InUse  Yes
          (SR Adj Segment IPv4, vers:0, index=3, type=0, intf=Gi0/0/0/1, nh=10.1.2.2)
        '''}

    golden_parsed_output2 = {
        'table': {
            0: {
                'label': {
                    0: {
                        'owner': 'LSD(A)',
                        'rewrite': 'Yes',
                        'state': 'InUse'},
                    1: {
                        'owner': 'LSD(A)',
                        'rewrite': 'Yes',
                        'state': 'InUse'},
                    2: {
                        'owner': 'LSD(A)',
                        'rewrite': 'Yes',
                        'state': 'InUse'},
                    13: {
                        'owner': 'LSD(A)',
                        'rewrite': 'Yes',
                        'state': 'InUse'},
                    15000: {
                        'label_type': {
                            'Lbl-blk SRLB': {
                                'size': 1000,
                                'start_label': 15000,
                                'vers': 0,
                                'app_notify': 0}
                        },
                        'owner': 'LSD(A)',
                        'rewrite': 'No',
                        'state': 'InUse'},
                    16000: {
                        'label_type': {
                            'Lbl-blk SRGB': {
                                'size': 7000,
                                'start_label': 16000,
                                'vers': 0}
                        },
                        'owner': 'ISIS(A):SR',
                        'rewrite': 'No',
                        'state': 'InUse'},
                    24000: {
                        'label_type': {
                            'SR Adj Segment IPv4': {
                                'index': 0,
                                'interface': 'Gi0/0/0/0',
                                'nh': '10.1.3.1',
                                'type': 0,
                                'vers': 0}
                        },
                        'owner': 'ISIS(A):SR',
                        'rewrite': 'Yes',
                        'state': 'InUse'},
                    24001: {
                        'label_type': {
                            'SR Adj Segment IPv4': {
                                'index': 2,
                                'interface': 'Gi0/0/0/0',
                                'nh': '10.1.3.1',
                                'type': 0,
                                'vers': 0}
                        },
                        'owner': 'ISIS(A):SR',
                        'rewrite': 'Yes',
                        'state': 'InUse'},
                    24002: {
                        'label_type': {
                            'SR Adj Segment IPv4': {
                                'index': 1,
                                'interface': 'Gi0/0/0/0',
                                'nh': '10.1.3.1',
                                'type': 0,
                                'vers': 0}
                        },
                        'owner': 'ISIS(A):SR',
                        'rewrite': 'Yes',
                        'state': 'InUse'},
                    24003: {
                        'label_type': {
                            'SR Adj Segment IPv4': {
                                'index': 3,
                                'interface': 'Gi0/0/0/0',
                                'nh': '10.1.3.1',
                                'type': 0,
                                'vers': 0}
                        },
                        'owner': 'ISIS(A):SR',
                        'rewrite': 'Yes',
                        'state': 'InUse'},
                    24004: {
                        'label_type': {
                            'SR Adj Segment IPv4': {
                                'index': 0,
                                'interface': 'Gi0/0/0/1',
                                'nh': '10.3.4.4',
                                'type': 0,
                                'vers': 0}
                        },
                        'owner': 'ISIS(A):SR',
                        'rewrite': 'Yes',
                        'state': 'InUse'},
                    24005: {
                        'label_type': {
                            'SR Adj Segment IPv4': {
                                'index': 2,
                                'interface': 'Gi0/0/0/1',
                                'nh': '10.3.4.4',
                                'type': 0,
                                'vers': 0}
                        },
                        'owner': 'ISIS(A):SR',
                        'rewrite': 'Yes',
                        'state': 'InUse'},
                    24006: {
                        'label_type': {
                            'SR Adj Segment IPv4': {
                                'index': 1,
                                'interface': 'Gi0/0/0/1',
                                'nh': '10.3.4.4',
                                'type': 0,
                                'vers': 0}
                        },
                        'owner': 'ISIS(A):SR',
                        'rewrite': 'Yes',
                        'state': 'InUse'},
                    24007: {
                        'label_type': {
                            'SR Adj Segment IPv4': {
                                'index': 3,
                                'interface': 'Gi0/0/0/1',
                                'nh': '10.3.4.4',
                                'type': 0,
                                'vers': 0}
                        },
                        'owner': 'ISIS(A):SR',
                        'rewrite': 'Yes',
                        'state': 'InUse'}
                }
            }
        }
    }

    golden_output2 = {'execute.return_value': '''
        RP/0/RP0/CPU0:R3#show mpls label table detail 
        Thu Aug 29 15:33:47.761 UTC
        Table Label   Owner                           State  Rewrite
        ----- ------- ------------------------------- ------ -------
        0     0       LSD(A)                          InUse  Yes
        0     1       LSD(A)                          InUse  Yes
        0     2       LSD(A)                          InUse  Yes
        0     13      LSD(A)                          InUse  Yes
        0     15000   LSD(A)                          InUse  No
          (Lbl-blk SRLB, vers:0, (start_label=15000, size=1000, app_notify=0)
        0     16000   ISIS(A):SR                      InUse  No
          (Lbl-blk SRGB, vers:0, (start_label=16000, size=7000)
        0     24000   ISIS(A):SR                      InUse  Yes
          (SR Adj Segment IPv4, vers:0, index=0, type=0, intf=Gi0/0/0/0, nh=10.1.3.1)
        0     24001   ISIS(A):SR                      InUse  Yes
          (SR Adj Segment IPv4, vers:0, index=2, type=0, intf=Gi0/0/0/0, nh=10.1.3.1)
        0     24002   ISIS(A):SR                      InUse  Yes
          (SR Adj Segment IPv4, vers:0, index=1, type=0, intf=Gi0/0/0/0, nh=10.1.3.1)
        0     24003   ISIS(A):SR                      InUse  Yes
          (SR Adj Segment IPv4, vers:0, index=3, type=0, intf=Gi0/0/0/0, nh=10.1.3.1)
        0     24004   ISIS(A):SR                      InUse  Yes
          (SR Adj Segment IPv4, vers:0, index=0, type=0, intf=Gi0/0/0/1, nh=10.3.4.4)
        0     24005   ISIS(A):SR                      InUse  Yes
          (SR Adj Segment IPv4, vers:0, index=2, type=0, intf=Gi0/0/0/1, nh=10.3.4.4)
        0     24006   ISIS(A):SR                      InUse  Yes
          (SR Adj Segment IPv4, vers:0, index=1, type=0, intf=Gi0/0/0/1, nh=10.3.4.4)
        0     24007   ISIS(A):SR                      InUse  Yes
          (SR Adj Segment IPv4, vers:0, index=3, type=0, intf=Gi0/0/0/1, nh=10.3.4.4)
    '''}

    def test_show_mpls_label_table_detail_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowMplsLabelTableDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_mpls_label_table_detail_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowMplsLabelTableDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_mpls_label_table_detail_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowMplsLabelTableDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

# ==================================================
#  Unit test for 'show mpls interfaces'
# ==================================================
class TestShowMplsInterfaces(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output1 = {
        'interfaces': {
            'GigabitEthernet0/0/0/0': {
                'enabled': 'Yes',
                'ldp': 'No',
                'static': 'No',
                'tunnel': 'No',
            },
            'GigabitEthernet0/0/0/1': {
                'enabled': 'Yes',
                'ldp': 'No',
                'static': 'No',
                'tunnel': 'No',
            },
        },
        'local_label': {
            '16001': {
                'outgoing_label': {
                    'Pop': {
                        'bytes_switched': 0,
                        'next_hop': '10.1.3.1',
                        'outgoing_interface': 'Gi0/0/0/0',
                        'prefix_or_id': 'SR Pfx (idx 1)',
                    },
                },
            },
            '16002': {
                'outgoing_label': {
                    '16002': {
                        'bytes_switched': 0,
                        'next_hop': '10.1.3.1',
                        'outgoing_interface': 'Gi0/0/0/0',
                        'prefix_or_id': 'SR Pfx (idx 2)',
                    },
                },
            },
            '16004': {
                'outgoing_label': {
                    'Pop': {
                        'bytes_switched': 0,
                        'next_hop': '10.3.4.4',
                        'outgoing_interface': 'Gi0/0/0/1',
                        'prefix_or_id': 'SR Pfx (idx 4)',
                    },
                },
            },
            '16005': {
                'outgoing_label': {
                    '16005': {
                        'bytes_switched': 0,
                        'next_hop': '10.1.3.1',
                        'outgoing_interface': 'Gi0/0/0/0',
                        'prefix_or_id': 'SR Pfx (idx 5)',
                    },
                },
            },
            '24000': {
                'outgoing_label': {
                    'Pop': {
                        'bytes_switched': 0,
                        'next_hop': '10.1.3.1',
                        'outgoing_interface': 'Gi0/0/0/0',
                        'prefix_or_id': 'SR Adj (idx 0)',
                    },
                },
            },
            '24001': {
                'outgoing_label': {
                    'Pop': {
                        'bytes_switched': 0,
                        'next_hop': '10.1.3.1',
                        'outgoing_interface': 'Gi0/0/0/0',
                        'prefix_or_id': 'SR Adj (idx 2)',
                    },
                },
            },
            '24002': {
                'outgoing_label': {
                    'Pop': {
                        'bytes_switched': 0,
                        'next_hop': '10.1.3.1',
                        'outgoing_interface': 'Gi0/0/0/0',
                        'prefix_or_id': 'SR Adj (idx 1)',
                    },
                },
            },
            '24003': {
                'outgoing_label': {
                    'Pop': {
                        'bytes_switched': 0,
                        'next_hop': '10.1.3.1',
                        'outgoing_interface': 'Gi0/0/0/0',
                        'prefix_or_id': 'SR Adj (idx 3)',
                    },
                },
            },
            '24004': {
                'outgoing_label': {
                    'Pop': {
                        'bytes_switched': 0,
                        'next_hop': '10.3.4.4',
                        'outgoing_interface': 'Gi0/0/0/1',
                        'prefix_or_id': 'SR Adj (idx 0)',
                    },
                },
            },
            '24005': {
                'outgoing_label': {
                    'Pop': {
                        'bytes_switched': 0,
                        'next_hop': '10.3.4.4',
                        'outgoing_interface': 'Gi0/0/0/1',
                        'prefix_or_id': 'SR Adj (idx 2)',
                    },
                },
            },
            '24006': {
                'outgoing_label': {
                    'Pop': {
                        'bytes_switched': 0,
                        'next_hop': '10.3.4.4',
                        'outgoing_interface': 'Gi0/0/0/1',
                        'prefix_or_id': 'SR Adj (idx 1)',
                    },
                },
            },
            '24007': {
                'outgoing_label': {
                    'Pop': {
                        'bytes_switched': 0,
                        'next_hop': '10.3.4.4',
                        'outgoing_interface': 'Gi0/0/0/1',
                        'prefix_or_id': 'SR Adj (idx 3)',
                    },
                },
            },
        },
    }
    
    golden_output1 = {'execute.return_value': '''
        RP/0/RP0/CPU0:R3#show mpls interfaces 
        Thu Aug 29 15:32:55.170 UTC
        Interface                  LDP      Tunnel   Static   Enabled 
        -------------------------- -------- -------- -------- --------
        GigabitEthernet0/0/0/0     No       No       No       Yes
        GigabitEthernet0/0/0/1     No       No       No       Yes

        RP/0/RP0/CPU0:R3#show mpls forwarding 
        Thu Aug 29 15:29:39.411 UTC
        Local  Outgoing    Prefix             Outgoing     Next Hop        Bytes       
        Label  Label       or ID              Interface                    Switched    
        ------ ----------- ------------------ ------------ --------------- ------------
        16001  Pop         SR Pfx (idx 1)     Gi0/0/0/0    10.1.3.1        0           
        16002  16002       SR Pfx (idx 2)     Gi0/0/0/0    10.1.3.1        0           
        16004  Pop         SR Pfx (idx 4)     Gi0/0/0/1    10.3.4.4        0           
        16005  16005       SR Pfx (idx 5)     Gi0/0/0/0    10.1.3.1        0           
        24000  Pop         SR Adj (idx 0)     Gi0/0/0/0    10.1.3.1        0           
        24001  Pop         SR Adj (idx 2)     Gi0/0/0/0    10.1.3.1        0           
        24002  Pop         SR Adj (idx 1)     Gi0/0/0/0    10.1.3.1        0           
        24003  Pop         SR Adj (idx 3)     Gi0/0/0/0    10.1.3.1        0           
        24004  Pop         SR Adj (idx 0)     Gi0/0/0/1    10.3.4.4        0           
        24005  Pop         SR Adj (idx 2)     Gi0/0/0/1    10.3.4.4        0           
        24006  Pop         SR Adj (idx 1)     Gi0/0/0/1    10.3.4.4        0           
        24007  Pop         SR Adj (idx 3)     Gi0/0/0/1    10.3.4.4        0
    '''}

    def test__empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowMplsInterfaces(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowMplsInterfaces(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

if __name__ == '__main__':
    unittest.main()