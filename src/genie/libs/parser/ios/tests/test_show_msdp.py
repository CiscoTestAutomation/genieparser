# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# ios show msdp
from genie.libs.parser.ios.show_msdp import ShowIpMsdpPeer, ShowIpMsdpSaCache


class test_show_msdp_peer(unittest.TestCase):
    """
        Commands:
        show ip msdp peer
        show ip msdp vrf {vrf} peer
    """

    device = Device(name="aDevice")

    expected_parsed_output_1 = {
        "vrf": {
            "default": {
                "peer": {
                    "10.16.2.2": {
                        "peer_as": 65000,
                        "session_state": "Up",
                        "resets": "0",
                        "connect_source": "Loopback0",
                        "connect_source_address": "10.4.1.1",
                        "elapsed_time": "00:13:18",
                        "statistics": {
                            "sent": {
                                "data_message": 15,
                                "sa_message": 14,
                                "sa_response": 0,
                                "data_packets": 0,
                            },
                            "received": {
                                "data_message": 28,
                                "sa_message": 0,
                                "sa_request": 0,
                                "data_packets": 0,
                            },
                            "output_msg_discarded": 0,
                            "established_transitions": 1,
                            "queue": {"size_in": 0, "size_out": 0},
                            "error": {"rpf_failure": 0},
                        },
                        "conn_count_cleared": "00:22:05",
                        "sa_filter": {
                            "in": {
                                "(S,G)": {"filter": "none", "route_map": "none"},
                                "RP": {"filter": "none", "route_map": "none"},
                            },
                            "out": {
                                "(S,G)": {"filter": "none", "route_map": "none"},
                                "RP": {"filter": "none", "route_map": "none"},
                            },
                        },
                        "sa_request": {"input_filter": "none"},
                        "ttl_threshold": 0,
                        "sa_learned_from": 0,
                        "signature_protection": False,
                    },
                    "10.36.3.3": {
                        "peer_as": 65000,
                        "session_state": "Up",
                        "resets": "0",
                        "connect_source": "Loopback0",
                        "connect_source_address": "10.4.1.1",
                        "elapsed_time": "00:16:57",
                        "statistics": {
                            "sent": {
                                "data_message": 20,
                                "sa_message": 19,
                                "sa_response": 0,
                                "data_packets": 0,
                            },
                            "received": {
                                "data_message": 19,
                                "sa_message": 0,
                                "sa_request": 0,
                                "data_packets": 0,
                            },
                            "output_msg_discarded": 0,
                            "established_transitions": 1,
                            "queue": {"size_in": 0, "size_out": 0},
                            "error": {"rpf_failure": 0},
                        },
                        "conn_count_cleared": "00:22:14",
                        "sa_filter": {
                            "in": {
                                "(S,G)": {"filter": "none", "route_map": "none"},
                                "RP": {"filter": "none", "route_map": "none"},
                            },
                            "out": {
                                "(S,G)": {"filter": "none", "route_map": "none"},
                                "RP": {"filter": "none", "route_map": "none"},
                            },
                        },
                        "sa_request": {"input_filter": "none"},
                        "ttl_threshold": 0,
                        "sa_learned_from": 0,
                        "signature_protection": False,
                    },
                }
            }
        }
    }

    device_output_1 = {"execute.return_value": """
    show ip msdp peer
    MSDP Peer 10.16.2.2 (?), AS 65000
      Connection status:
        State: Up, Resets: 0, Connection source: Loopback0 (10.4.1.1)
        Uptime(Downtime): 00:13:18, Messages sent/received: 15/28
        Output messages discarded: 0
        Connection and counters cleared 00:22:05 ago
      SA Filtering:
        Input (S,G) filter: none, route-map: none
        Input RP filter: none, route-map: none
        Output (S,G) filter: none, route-map: none
        Output RP filter: none, route-map: none
      SA-Requests:
        Input filter: none
      Peer ttl threshold: 0
      SAs learned from this peer: 0
      Number of connection transitions to Established state: 1
        Input queue size: 0, Output queue size: 0
      MD5 signature protection on MSDP TCP connection: not enabled
      Message counters:
        RPF Failure count: 0
        SA Messages in/out: 0/14
        SA Requests in: 0
        SA Responses out: 0
        Data Packets in/out: 0/0
    MSDP Peer 10.36.3.3 (?), AS 65000
      Connection status:
        State: Up, Resets: 0, Connection source: Loopback0 (10.4.1.1)
        Uptime(Downtime): 00:16:57, Messages sent/received: 20/19
        Output messages discarded: 0
        Connection and counters cleared 00:22:14 ago
      SA Filtering:
        Input (S,G) filter: none, route-map: none
        Input RP filter: none, route-map: none
        Output (S,G) filter: none, route-map: none
        Output RP filter: none, route-map: none
      SA-Requests:
        Input filter: none
      Peer ttl threshold: 0
      SAs learned from this peer: 0
      Number of connection transitions to Established state: 1
        Input queue size: 0, Output queue size: 0
      MD5 signature protection on MSDP TCP connection: not enabled
      Message counters:
        RPF Failure count: 0
        SA Messages in/out: 0/19
        SA Requests in: 0
        SA Responses out: 0
        Data Packets in/out: 0/0
    """
    }

    expected_parsed_output_2 = {
        "vrf": {
            "VRF1": {
                "peer": {
                    "10.16.2.2": {
                        "peer_as": 65000,
                        "session_state": "Up",
                        "resets": "0",
                        "connect_source": "Loopback300",
                        "connect_source_address": "10.4.1.1",
                        "elapsed_time": "00:19:00",
                        "statistics": {
                            "sent": {
                                "data_message": 22,
                                "sa_message": 21,
                                "sa_response": 0,
                                "data_packets": 0,
                            },
                            "received": {
                                "data_message": 40,
                                "sa_message": 0,
                                "sa_request": 0,
                                "data_packets": 0,
                            },
                            "output_msg_discarded": 0,
                            "established_transitions": 1,
                            "queue": {"size_in": 0, "size_out": 0},
                            "error": {"rpf_failure": 0},
                        },
                        "conn_count_cleared": "00:27:47",
                        "sa_filter": {
                            "in": {
                                "(S,G)": {"filter": "none", "route_map": "none"},
                                "RP": {"filter": "none", "route_map": "none"},
                            },
                            "out": {
                                "(S,G)": {"filter": "none", "route_map": "none"},
                                "RP": {"filter": "none", "route_map": "none"},
                            },
                        },
                        "sa_request": {"input_filter": "none"},
                        "ttl_threshold": 0,
                        "sa_learned_from": 0,
                        "signature_protection": False,
                    },
                    "10.36.3.3": {
                        "peer_as": 65000,
                        "session_state": "Down",
                        "resets": "31",
                        "connect_source": "Loopback300",
                        "connect_source_address": "10.4.1.1",
                        "elapsed_time": "00:00:23",
                        "statistics": {
                            "sent": {
                                "data_message": 0,
                                "sa_message": 0,
                                "sa_response": 0,
                                "data_packets": 0,
                            },
                            "received": {
                                "data_message": 0,
                                "sa_message": 0,
                                "sa_request": 0,
                                "data_packets": 0,
                            },
                            "output_msg_discarded": 0,
                            "established_transitions": 31,
                            "queue": {"size_in": 0, "size_out": 0},
                            "error": {"rpf_failure": 0},
                        },
                        "conn_count_cleared": "00:27:56",
                        "sa_filter": {
                            "in": {
                                "(S,G)": {"filter": "none", "route_map": "none"},
                                "RP": {"filter": "none", "route_map": "none"},
                            },
                            "out": {
                                "(S,G)": {"filter": "none", "route_map": "none"},
                                "RP": {"filter": "none", "route_map": "none"},
                            },
                        },
                        "sa_request": {"input_filter": "none"},
                        "ttl_threshold": 0,
                        "sa_learned_from": 0,
                        "signature_protection": False,
                    },
                }
            }
        }
    }

    device_output_2 = {"execute.return_value": """
    Router# show ip msdp vrf VRF1 peer
    MSDP Peer 10.16.2.2 (?), AS 65000
      Connection status:
        State: Up, Resets: 0, Connection source: Loopback300 (10.4.1.1)
        Uptime(Downtime): 00:19:00, Messages sent/received: 22/40
        Output messages discarded: 0
        Connection and counters cleared 00:27:47 ago
      SA Filtering:
        Input (S,G) filter: none, route-map: none
        Input RP filter: none, route-map: none
        Output (S,G) filter: none, route-map: none
        Output RP filter: none, route-map: none
      SA-Requests:
        Input filter: none
      Peer ttl threshold: 0
      SAs learned from this peer: 0
      Number of connection transitions to Established state: 1
        Input queue size: 0, Output queue size: 0
      MD5 signature protection on MSDP TCP connection: not enabled
      Message counters:
        RPF Failure count: 0
        SA Messages in/out: 0/21
        SA Requests in: 0
        SA Responses out: 0
        Data Packets in/out: 0/0
    MSDP Peer 10.36.3.3 (?), AS 65000
      Connection status:
        State: Down, Resets: 31, Connection source: Loopback300 (10.4.1.1)
        Uptime(Downtime): 00:00:23, Messages sent/received: 0/0
        Output messages discarded: 0
        Connection and counters cleared 00:27:56 ago
      SA Filtering:
        Input (S,G) filter: none, route-map: none
        Input RP filter: none, route-map: none
        Output (S,G) filter: none, route-map: none
        Output RP filter: none, route-map: none
      SA-Requests:
        Input filter: none
      Peer ttl threshold: 0
      SAs learned from this peer: 0
      Number of connection transitions to Established state: 31
        Input queue size: 0, Output queue size: 0
      MD5 signature protection on MSDP TCP connection: not enabled
      Message counters:
        RPF Failure count: 0
        SA Messages in/out: 0/0
        SA Requests in: 0
        SA Responses out: 0
        Data Packets in/out: 0/0
    """
    }

    device_output_empty = {"execute.return_value": ""}

    def test_test_show_msdp_peer_1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_1)
        obj = ShowIpMsdpPeer(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_1)

    def test_test_show_msdp_peer_2(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_2)
        obj = ShowIpMsdpPeer(device=self.device)
        parsed_output = obj.parse(vrf="VRF1")
        self.assertEqual(parsed_output, self.expected_parsed_output_2)

    def test_test_show_msdp_peer_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_empty)
        obj = ShowIpMsdpPeer(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


class test_show_msdp_sa_cache(unittest.TestCase):

    """
        show ip msdp sa-cache
        show ip msdb vrf <vrf> sa-cache
    """

    device = Device(name="aDevice")

    expected_parsed_output_1 = {
        "vrf": {
            "default": {
                "num_of_sa_cache": 1,
                "sa_cache": {
                    "225.1.1.1 10.3.3.18": {
                        "group": "225.1.1.1",
                        "source_addr": "10.3.3.18",
                        "up_time": "00:00:10",
                        "expire": "00:05:49",
                        "peer_as": 3,
                        "peer": "10.1.100.4",
                        "origin_rp": {"10.3.100.8": {"rp_address": "10.3.100.8"}},
                        "peer_learned_from": "10.1.100.4",
                        "rpf_peer": "10.1.100.4",
                        "statistics": {
                            "received": {"sa": 1, "encapsulated_data_received": 1}
                        },
                    }
                },
            }
        }
    }

    device_output_1 = {"execute.return_value": """
        Router# show ip msdp sa-cache
        MSDP Source-Active Cache - 1 entries
        (10.3.3.18, 225.1.1.1), RP 10.3.100.8, BGP/AS 3, 00:00:10/00:05:49, Peer 10.1.100.4
        Learned from peer 10.1.100.4, RPF peer 10.1.100.4, 
        SAs received: 1, Encapsulated data received: 1
    """
    }

    expected_parsed_output_2 = {
        "vrf": {
            "default": {
                "num_of_sa_cache": 1,
                "sa_cache": {
                    "225.1.1.1 10.1.4.15": {
                        "group": "225.1.1.1",
                        "source_addr": "10.1.4.15",
                        "up_time": "00:19:29",
                        "expire": "00:05:14",
                        "peer": "10.1.100.1",
                        "origin_rp": {"10.1.100.1": {"rp_address": "10.1.100.1"}},
                        "peer_learned_from": "10.1.100.1",
                        "rpf_peer": "10.1.100.1",
                        "statistics": {
                            "received": {"sa": 14, "encapsulated_data_received": 0}
                        },
                    }
                },
            }
        }
    }

    device_output_2 = {"execute.return_value": """
        P2#show ip msdp vrf VRF1 sa-cache
        MSDP Source-Active Cache - 1 entries
        (10.1.4.15, 225.1.1.1), RP 10.1.100.1, AS ?,00:19:29/00:05:14, Peer 10.1.100.1
        Learned from peer 10.1.100.1, RPF peer 10.1.100.1, 
        SAs received: 14, Encapsulated data received: 0
    """
    }

    expected_parsed_output_3 = {
        "vrf": {
            "default": {
                "num_of_sa_cache": 8,
                "sa_cache": {
                    "239.232.1.0 10.44.44.5": {
                        "group": "239.232.1.0",
                        "source_addr": "10.44.44.5",
                        "up_time": "00:01:20",
                        "expire": "00:05:32",
                        "peer_as": 64512,
                        "peer": "192.168.4.4",
                        "origin_rp": {"192.168.4.4": {"rp_address": "192.168.4.4"}},
                    },
                    "239.232.1.1 10.44.44.5": {
                        "group": "239.232.1.1",
                        "source_addr": "10.44.44.5",
                        "up_time": "00:01:20",
                        "expire": "00:05:32",
                        "peer_as": 64512,
                        "peer": "192.168.4.4",
                        "origin_rp": {"192.168.4.4": {"rp_address": "192.168.4.4"}},
                    },
                    "239.232.1.2 10.44.44.5": {
                        "group": "239.232.1.2",
                        "source_addr": "10.44.44.5",
                        "up_time": "00:01:19",
                        "expire": "00:05:32",
                        "peer": "192.168.4.4",
                        "peer_as": 64512,
                        "origin_rp": {"192.168.4.4": {"rp_address": "192.168.4.4"}},
                    },
                    "239.232.1.3 10.44.44.5": {
                        "group": "239.232.1.3",
                        "source_addr": "10.44.44.5",
                        "up_time": "00:01:19",
                        "expire": "00:05:32",
                        "peer": "192.168.4.4",
                        "peer_as": 64512,
                        "origin_rp": {"192.168.4.4": {"rp_address": "192.168.4.4"}},
                    },
                    "239.232.1.4 10.44.44.5": {
                        "group": "239.232.1.4",
                        "source_addr": "10.44.44.5",
                        "up_time": "00:01:19",
                        "expire": "00:05:32",
                        "peer_as": 64512,
                        "peer": "192.168.4.4",
                        "origin_rp": {"192.168.4.4": {"rp_address": "192.168.4.4"}},
                    },
                    "239.232.1.5 10.44.44.5": {
                        "group": "239.232.1.5",
                        "source_addr": "10.44.44.5",
                        "up_time": "00:01:19",
                        "expire": "00:05:32",
                        "peer_as": 64512,
                        "peer": "192.168.4.4",
                        "origin_rp": {"192.168.4.4": {"rp_address": "192.168.4.4"}},
                    },
                    "239.232.1.6 10.44.44.5": {
                        "group": "239.232.1.6",
                        "source_addr": "10.44.44.5",
                        "up_time": "00:01:19",
                        "expire": "00:05:32",
                        "peer_as": 64512,
                        "peer": "192.168.4.4",
                        "origin_rp": {"192.168.4.4": {"rp_address": "192.168.4.4"}},
                    },
                    "239.232.1.7 10.44.44.5": {
                        "group": "239.232.1.7",
                        "source_addr": "10.44.44.5",
                        "up_time": "00:01:19",
                        "expire": "00:05:32",
                        "peer_as": 64512,
                        "peer": "192.168.4.4",
                        "origin_rp": {"192.168.4.4": {"rp_address": "192.168.4.4"}},
                    },
                },
            }
        }
    }

    device_output_3 = {"execute.return_value": """
        Device# show ip msdp sa-cache
        MSDP Source-Active Cache - 8 entries
        (10.44.44.5, 239.232.1.0), RP 192.168.4.4, BGP/AS 64512, 00:01:20/00:05:32, Peer 192.168.4.4
        (10.44.44.5, 239.232.1.1), RP 192.168.4.4, BGP/AS 64512, 00:01:20/00:05:32, Peer 192.168.4.4
        (10.44.44.5, 239.232.1.2), RP 192.168.4.4, BGP/AS 64512, 00:01:19/00:05:32, Peer 192.168.4.4
        (10.44.44.5, 239.232.1.3), RP 192.168.4.4, BGP/AS 64512, 00:01:19/00:05:32, Peer 192.168.4.4
        (10.44.44.5, 239.232.1.4), RP 192.168.4.4, BGP/AS 64512, 00:01:19/00:05:32, Peer 192.168.4.4
        (10.44.44.5, 239.232.1.5), RP 192.168.4.4, BGP/AS 64512, 00:01:19/00:05:32, Peer 192.168.4.4
        (10.44.44.5, 239.232.1.6), RP 192.168.4.4, BGP/AS 64512, 00:01:19/00:05:32, Peer 192.168.4.4
        (10.44.44.5, 239.232.1.7), RP 192.168.4.4, BGP/AS 64512, 00:01:19/00:05:32, Peer 192.168.4.4
    """
    }

    device_output_empty = {"execute.return_value": ""}

    def test_show_msdp_sa_cache_1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_1)
        obj = ShowIpMsdpSaCache(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_1)

    def test_show_msdp_sa_cache_2(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_2)
        obj = ShowIpMsdpSaCache(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_2)

    def test_show_msdp_sa_cache_3(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_3)
        obj = ShowIpMsdpSaCache(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_3)

    def test_show_msdp_sa_cache_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_empty)
        obj = ShowIpMsdpSaCache(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == "__main__":
    unittest.main()
