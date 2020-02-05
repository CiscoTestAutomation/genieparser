# Python

import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Parser
from genie.libs.parser.nxos.show_msdp import ShowIpMsdpSaCacheDetailVrf,\
                                             ShowIpMsdpPeerVrf,\
                                             ShowIpMsdpPolicyStatisticsSaPolicyIn, \
                                             ShowIpMsdpPolicyStatisticsSaPolicyOut, \
                                             ShowIpMsdpSummary, ShowRunningConfigMsdp

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError


# ===========================================================
#  Unit test for 'show ip msdp sa-cache detail vrf <vrf>'
# ===========================================================

class test_show_ip_msdp_sa_cache_detail_vrf(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vrf': {
            'default':{
                'sa_cache': {
                    "228.1.1.1 172.16.25.2": {
                        'group': "228.1.1.1",
                        'source_addr': "172.16.25.2",
                        'up_time': "00:02:43",
                        'expire': "00:02:32",
                        'asn': 100,
                        'peer_learned_from': "10.106.106.106",
                        'origin_rp': {
                            "10.106.106.106": {
                                'rp_address': "10.106.106.106",
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output = {'execute.return_value': '''
    nexus# show ip msdp sa-cache detail vrf all
    MSDP SA Route Cache for VRF "default" - 1 entries
    Source          Group            RP               ASN         Uptime
    172.16.25.2       228.1.1.1        10.106.106.106   100         00:02:43
        Peer: 10.106.106.106, Expires: 00:02:32
    '''}

    def test_show_ip_msdp_sa_cache_detail_vrf_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpMsdpSaCacheDetailVrf(device=self.device)
        parsed_output = obj.parse(vrf="all")
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_ip_msdp_sa_cache_detail_vrf_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpMsdpSaCacheDetailVrf(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ===========================================================
#  Unit test for 'show ip msdp peer vrf <vrf>'
# ===========================================================

class test_show_ip_msdp_peer_vrf(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
            "vrf": {
                "VRF1": {
                    "peer": {
                        "10.94.44.44": {
                            "sa_limit": "44",
                            "description": "R4",
                            "elapsed_time": "01:03:22",
                            "connect_source_address": "10.21.33.34",
                            "authentication": {
                                "password": {
                                    "set": False
                                },
                            },
                            "connect_source": "loopback3",
                            "peer_as": "200",
                            "mesh_group": "2",
                            "session_state": "inactive",
                            "statistics": {
                                "established_transitions": 0,
                                "last_message_received": "never",
                                "discontinuity_time": "00:00:20",
                                "port": {
                                    "remote": 0,
                                    "local": 0
                                },
                                "received": {
                                    "notification": 0,
                                    "data_message": 0,
                                    "sa_response": 0,
                                    "sa_request": 0,
                                    "keepalive": 0,
                                    "total": 0,
                                    "ctrl_message": 0
                                },
                                "cache_lifetime": "00:03:30",
                                "sent": {
                                    "notification": 0,
                                    "data_message": 0,
                                    "sa_response": 0,
                                    "sa_request": 0,
                                    "keepalive": 0,
                                    "total": 0,
                                    "ctrl_message": 0
                                },
                                "connection_attempts": 88,
                                "error": {
                                    "rpf_failure": "0"
                                }
                            },
                            "enable": False,
                            "timer": {
                                "keepalive_interval": 60,
                                "connect_retry_interval": 44,
                                "holdtime_interval": 90
                            }
                        }
                    }
                },
                "default": {
                    "peer": {
                        "10.4.1.1": {
                            "sa_limit": "111",
                            "description": "R1",
                            "elapsed_time": "01:27:25",
                            "connect_source_address": "10.36.3.3",
                            "reset_reason": 'Keepalive timer expired',
                            "authentication": {
                                "password": {
                                    "set": False
                                },
                            },
                            "connect_source": "loopback0",
                            "peer_as": "100",
                            "mesh_group": "1",
                            "session_state": "established",
                            "statistics": {
                                "established_transitions": 6,
                                "last_message_received": "00:00:22",
                                "discontinuity_time": "01:27:25",
                                "port": {
                                    "remote": 26743,
                                    "local": 639
                                },
                                "received": {
                                    "notification": 0,
                                    "data_message": 0,
                                    "sa_response": 0,
                                    "sa_request": 0,
                                    "keepalive": 92,
                                    "total": 0,
                                    "ctrl_message": 0
                                },
                                "cache_lifetime": "00:03:30",
                                "sent": {
                                    "notification": 6,
                                    "data_message": 0,
                                    "sa_response": 0,
                                    "sa_request": 0,
                                    "keepalive": 119,
                                    "total": 0,
                                    "ctrl_message": 0
                                },
                                "connection_attempts": 0,
                                "error": {
                                    "rpf_failure": "0"
                                }
                            },
                            "enable": True,
                            "timer": {
                                "keepalive_interval": 60,
                                "connect_retry_interval": 33,
                                "holdtime_interval": 90
                            }
                        }
                    }
                }
            }
        }

    golden_output = {'execute.return_value': '''
    R3_titatnium# show ip msdp peer vrf all
    MSDP peer 10.4.1.1 for VRF "default"
    AS 100, local address: 10.36.3.3 (loopback0)
      Description: R1
      Connection status: Established
        Uptime(Downtime): 01:27:25
        Last reset reason: Keepalive timer expired
        Password: not set
      Keepalive Interval: 60 sec
      Keepalive Timeout: 90 sec
      Reconnection Interval: 33 sec
      Policies:
        SA in: none, SA out: none
        SA limit: 111
      Member of mesh-group: 1
      Statistics (in/out):
        Last messaged received: 00:00:22
        SAs: 0/0, SA-Requests: 0/0, SA-Responses: 0/0
        In/Out Ctrl Msgs: 0/0, In/Out Data Msgs: 0/0
        Remote/Local Port 26743/639
        Keepalives: 92/119, Notifications: 0/6
        RPF check failures: 0
        Cache Lifetime: 00:03:30
        Established Transitions: 6
        Connection Attempts: 0
        Discontinuity Time: 01:27:25

    MSDP peer 10.94.44.44 for VRF "VRF1"
    AS 200, local address: 10.21.33.34 (loopback3)
      Description: R4
      Connection status: Inactive, Connecting in: 00:00:23
        Uptime(Downtime): 01:03:22
        Password: not set
      Keepalive Interval: 60 sec
      Keepalive Timeout: 90 sec
      Reconnection Interval: 44 sec
      Policies:
        SA in: none, SA out: none
        SA limit: 44
      Member of mesh-group: 2
      Statistics (in/out):
        Last messaged received: never
        SAs: 0/0, SA-Requests: 0/0, SA-Responses: 0/0
        In/Out Ctrl Msgs: 0/0, In/Out Data Msgs: 0/0
        Remote/Local Port 0/0
        Keepalives: 0/0, Notifications: 0/0
        RPF check failures: 0
        Cache Lifetime: 00:03:30
        Established Transitions: 0
        Connection Attempts: 88
        Discontinuity Time: 00:00:20
    '''}

    def test_show_ip_msdp_peer_vrf_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpMsdpPeerVrf(device=self.device)
        parsed_output = obj.parse(vrf="all")
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_ip_msdp_sa_cache_detail_vrf_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpMsdpPeerVrf(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# =============================================================================
#  Unit test for 'show ip msdp policy statistics sa-policy <address> in|out'
# =============================================================================

class test_show_ip_msdp_policy_statistics_sa_policy(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': '''No SA input policy set for this peer'''}

    golden_parsed_output_in_1 = {
        "vrf": {
            "default": {
               "peer": {
                    "10.144.6.6": {
                         "in": {
                             "total_accept_count": 0,
                             "total_reject_count": 0,
                              "filtera": {
                                   "route-map filtera permit 10 match ip address mcast-all-groups": {
                                        "match": "route-map filtera permit 10 match ip address mcast-all-groups",
                                        "num_of_matches": 0,
                                        "num_of_comparison": 0
                                   },
                                   "route-map filtera permit 20 match ip address mcast-all-groups2": {
                                        "match": "route-map filtera permit 20 match ip address mcast-all-groups2",
                                        "num_of_matches": 0,
                                        "num_of_comparison": 0
                                   }
                              }
                         },
                    }
               }
            }
        }
    }

    golden_parsed_output_in_2 = {
        "vrf": {
            "default": {
               "peer": {
                    "10.144.6.6": {
                         "in": {
                             "total_accept_count": 0,
                             "total_reject_count": 1,
                              "pfxlista": {
                                   "ip prefix-list pfxlista seq 10 permit 224.0.0.0/4 le 32": {
                                        "num_of_matches": 0,
                                        "match": "ip prefix-list pfxlista seq 10 permit 224.0.0.0/4 le 32"
                                   },
                                   "ip prefix-list pfxlista seq 5 permit 224.0.0.0/4": {
                                        "num_of_matches": 0,
                                        "match": "ip prefix-list pfxlista seq 5 permit 224.0.0.0/4",
                                   }
                              }
                         },
                    }
               }
            }
        }
    }

    golden_parsed_output_out_1 = {
       "vrf": {
            "default": {
               "peer": {
                    "10.144.6.6": {
                         "out": {
                             "total_accept_count": 0,
                             "total_reject_count": 0,
                              "filtera": {
                                   "route-map filtera permit 10 match ip address mcast-all-groups": {
                                        "match": "route-map filtera permit 10 match ip address mcast-all-groups",
                                        "num_of_matches": 0,
                                        "num_of_comparison": 0
                                   },
                                   "route-map filtera permit 20 match ip address mcast-all-groups2": {
                                        "match": "route-map filtera permit 20 match ip address mcast-all-groups2",
                                        "num_of_matches": 0,
                                        "num_of_comparison": 0
                                   }
                              }
                         },
                    }
               }
            }
        }
    }

    golden_output_in_1 = {'execute.return_value': '''
    N95_2_R2# show ip msdp policy statistics sa-policy 10.144.6.6 in 
    C: No. of comparisions, M: No. of matches

    route-map filtera permit 10
      match ip address mcast-all-groups                          C: 0      M: 0     
    route-map filtera permit 20
      match ip address mcast-all-groups2                         C: 0      M: 0     

    Total accept count for policy: 0     
    Total reject count for policy: 0  
    '''}

    golden_output_in_2 = {'execute.return_value': '''
    N95_2_R2# show ip msdp policy statistics sa-policy 10.144.6.6 in
    C: No. of comparisions, M: No. of matches

    ip prefix-list pfxlista seq 5 permit 224.0.0.0/4             M: 0     
    ip prefix-list pfxlista seq 10 permit 224.0.0.0/4 le 32      M: 0     

    Total accept count for policy: 0     
    Total reject count for policy: 1 
    '''}

    golden_output_out_1 = {'execute.return_value': '''
    N95_2_R2# show ip msdp policy statistics sa-policy 10.144.6.6 out
    C: No. of comparisions, M: No. of matches

    route-map filtera permit 10
      match ip address mcast-all-groups                          C: 0      M: 0     
    route-map filtera permit 20
      match ip address mcast-all-groups2                         C: 0      M: 0     

    Total accept count for policy: 0     
    Total reject count for policy: 0
    '''}

    def test_golden_in_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_in_1)
        obj = ShowIpMsdpPolicyStatisticsSaPolicyIn(device=self.device)
        parsed_output = obj.parse(peer='10.144.6.6')
        self.assertEqual(parsed_output, self.golden_parsed_output_in_1)

    def test_golden_in_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_in_2)
        obj = ShowIpMsdpPolicyStatisticsSaPolicyIn(device=self.device)
        parsed_output = obj.parse(peer='10.144.6.6')
        self.assertEqual(parsed_output, self.golden_parsed_output_in_2)

    def test_golden_out_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_out_1)
        obj = ShowIpMsdpPolicyStatisticsSaPolicyOut(device=self.device)
        parsed_output = obj.parse(peer='10.144.6.6')
        self.assertEqual(parsed_output, self.golden_parsed_output_out_1)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpMsdpPolicyStatisticsSaPolicyIn(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(peer='10.144.6.6')
        obj = ShowIpMsdpPolicyStatisticsSaPolicyOut(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(peer='10.144.6.6')


# =============================================================================
#  Unit test for 'show ip msdp summary [vrf <vrf>]'
# =============================================================================

class test_show_ip_msdp_summary(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''' '''}

    golden_parsed_output = {
        "vrf": {
            "default": {
               "local_as": 0,
               "originator_id": "10.16.2.2",
               "statistics": {
                    "num_of_configured_peers": 1,
                    "num_of_established_peers": 1,
                    "num_of_shutdown_peers": 0
               },
               "peer": {
                    "10.144.6.6": {
                         "elapsed_time": "05:46:19",
                         "statistics": {
                              "num_of_sg_received": 1,
                              "last_message_received": "00:00:51"
                         },
                         "session_state": "established",
                         "address": "10.144.6.6",
                         "peer_as": 0
                    }
                }
            },
            "VRF1": {
               "local_as": 0,
               "originator_id": "10.16.2.2",
               "statistics": {
                    "num_of_configured_peers": 1,
                    "num_of_established_peers": 1,
                    "num_of_shutdown_peers": 0
               },
               "peer": {
                    "10.144.6.6": {
                         "elapsed_time": "05:46:18",
                         "statistics": {
                              "num_of_sg_received": 0,
                              "last_message_received": "00:00:55"
                         },
                         "session_state": "established",
                         "address": "10.144.6.6",
                         "peer_as": 0
                    }
                }
            }
        }
    }

    golden_parsed_output_vrf_default = {
        "vrf": {
            "default": {
               "local_as": 0,
               "originator_id": "10.16.2.2",
               "statistics": {
                    "num_of_configured_peers": 1,
                    "num_of_established_peers": 1,
                    "num_of_shutdown_peers": 0
               },
               "peer": {
                    "10.144.6.6": {
                         "elapsed_time": "06:15:59",
                         "statistics": {
                              "num_of_sg_received": 1,
                              "last_message_received": "00:00:48"
                         },
                         "session_state": "established",
                         "address": "10.144.6.6",
                         "peer_as": 0
                    }
                }
            },
        }
    }

    golden_output = {'execute.return_value': '''
    N95_2_R2# show ip msdp summary vrf all
    MSDP Peer Status Summary for VRF "default"
    Local ASN: 0, originator-id: 10.16.2.2

    Number of configured peers:  1
    Number of established peers: 1
    Number of shutdown peers:    0

    Peer            Peer        Connection      Uptime/   Last msg  (S,G)s
    Address         ASN         State           Downtime  Received  Received
    10.144.6.6         0           Established     05:46:19  00:00:51  1

    MSDP Peer Status Summary for VRF "VRF1"
    Local ASN: 0, originator-id: 10.16.2.2

    Number of configured peers:  1
    Number of established peers: 1
    Number of shutdown peers:    0

    Peer            Peer        Connection      Uptime/   Last msg  (S,G)s
    Address         ASN         State           Downtime  Received  Received
    10.144.6.6         0           Established     05:46:18  00:00:55  0
 
    '''}

    golden_output_vrf_default = {'execute.return_value': '''
    N95_2_R2# show ip msdp summary 
    MSDP Peer Status Summary for VRF "default"
    Local ASN: 0, originator-id: 10.16.2.2

    Number of configured peers:  1
    Number of established peers: 1
    Number of shutdown peers:    0

    Peer            Peer        Connection      Uptime/   Last msg  (S,G)s
    Address         ASN         State           Downtime  Received  Received
    10.144.6.6         0           Established     06:15:59  00:00:48  1

    '''}

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpMsdpSummary(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_vrf_default(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_vrf_default)
        obj = ShowIpMsdpSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_vrf_default)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpMsdpSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# =============================================================================
#  Unit test for 'show running-config msdp [| sec <vrf> | inc <str>]'
# =============================================================================

class test_show_run_msdp(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''' '''}

    golden_parsed_output = {
        "vrf": {
            "default": {
               "global": {
                    "timer": {
                         "connect_retry_interval": 15
                    }
               },
               "peer": {
                    "10.144.6.6": {
                         "description": "test description",
                         "timer": {
                              "keepalive_interval": 50,
                              "holdtime_interval": 60
                         },
                         "connect_source": "loopback0",
                    }
               }
            },
            "VRF1": {
               "peer": {
                    "10.144.6.6": {
                         "description": "test description on VRF1",
                         "connect_source": "loopback11",
                         "peer_as": "234",
                    }
               }
            }
        }
    }

    golden_parsed_output_default_vrf = {
        "vrf": {
            "default": {
               "global": {
                    "timer": {
                         "connect_retry_interval": 15
                    }
               },
               "peer": {
                    "10.144.6.6": {
                         "description": "test description",
                         "timer": {
                              "keepalive_interval": 50,
                              "holdtime_interval": 60
                         }
                    }
               }
            },
        }
    }


    golden_parsed_output_vrf_pip = {
        "vrf": {
            "VRF1": {
               "peer": {
                    "10.144.6.6": {
                         "description": "test description on VRF1"
                    }
               }
            }
        }
    }

    golden_output = {'execute.return_value': '''
        N95_2_R2# show run msdp
!Command: show running-config msdp
!Time: Mon Aug 27 20:17:11 2018

version 7.0(3)I7(3)
feature msdp

ip msdp description 10.144.6.6 test description
ip msdp keepalive 10.144.6.6 50 60
ip msdp reconnect-interval 15
ip msdp peer 10.144.6.6 connect-source loopback0

vrf context VRF1
  ip msdp description 10.144.6.6 test description on VRF1
  ip msdp peer 10.144.6.6 connect-source loopback11 remote-as 234
 
    '''}


    golden_output_vrf_default = {'execute.return_value': '''
        N95_2_R2# show run msdp | sec '^i'
ip msdp description 10.144.6.6 test description
ip msdp keepalive 10.144.6.6 50 60
ip msdp reconnect-interval 15
 
    '''}


    golden_output_vrf_VRF1_pip = {'execute.return_value': '''
        N95_2_R2# show run msdp | sec VRF1 | inc description
  ip msdp description 10.144.6.6 test description on VRF1 
    '''}

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowRunningConfigMsdp(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_vrf_default(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_vrf_default)
        obj = ShowRunningConfigMsdp(device=self.device)
        parsed_output = obj.parse(vrf='default')
        self.assertEqual(parsed_output, self.golden_parsed_output_default_vrf)

    def test_golden_vrf_pip(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_vrf_VRF1_pip)
        obj = ShowRunningConfigMsdp(device=self.device)
        parsed_output = obj.parse(vrf='VRF1', pip_str='description')
        self.assertEqual(parsed_output, self.golden_parsed_output_vrf_pip)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowRunningConfigMsdp(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()