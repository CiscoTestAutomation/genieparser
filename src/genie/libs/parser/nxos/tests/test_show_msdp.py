# Python

import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Parser
from genie.libs.parser.nxos.show_msdp import ShowIpMsdpSaCacheDetailVrf,\
                                             ShowIpMsdpPeerVrf

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError


# ===========================================================
#  Unit test for 'show ip msdp sa-cache detail vrf <vrf>'
# ===========================================================

class test_show_ip_msdp_sa_cache_detail_vrf(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vrfs': {
            'default':{
                'sa_cache': {
                    "228.1.1.1 173.1.1.2": {
                        'group': "228.1.1.1",
                        'source_addr': "173.1.1.2",
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
    173.1.1.2       228.1.1.1        10.106.106.106   100         00:02:43
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
            "vrfs": {
                "VRF1": {
                    "peer": {
                        "44.44.44.44": {
                            "sa_limit": 44,
                            "description": "R4",
                            "elapsed_time": "01:03:22",
                            "local_address": "33.33.33.34",
                            "sa_filter": {
                                "in": "none",
                                "out": "none"
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
                                "sent": {
                                    "notification": 0,
                                    "data_message": 0,
                                    "sa_response": 0,
                                    "sa_request": 0,
                                    "keepalive": 0,
                                    "total": 0,
                                    "ctrl_message": 0
                                },
                                "cache_lifetime": "00:03:30",
                                "received": {
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
                        "1.1.1.1": {
                            "sa_limit": 111,
                            "description": "R1",
                            "elapsed_time": "01:27:25",
                            "local_address": "3.3.3.3",
                            "sa_filter": {
                                "in": "none",
                                "out": "none"
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
                                "sent": {
                                    "notification": 0,
                                    "data_message": 0,
                                    "sa_response": 0,
                                    "sa_request": 0,
                                    "keepalive": 92,
                                    "total": 0,
                                    "ctrl_message": 0
                                },
                                "cache_lifetime": "00:03:30",
                                "received": {
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
    MSDP peer 1.1.1.1 for VRF "default"
    AS 100, local address: 3.3.3.3 (loopback0)
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

    MSDP peer 44.44.44.44 for VRF "VRF1"
    AS 200, local address: 33.33.33.34 (loopback3)
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
if __name__ == '__main__':
    unittest.main()