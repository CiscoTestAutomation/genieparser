

expected_output = {
    "vrf": {
      "default": {
           "neighbor": {
                "10.106.101.1": {
                     "address_family": {
                          "ipv6 unicast": {
                               "config_peers": 5,
                               "msg_sent": 31,
                               "state": "established",
                               "attribute_entries": "[3/480]",
                               "outq": 0,
                               "path": {
                                    "memory_usage": 1220,
                                    "total_entries": 5
                               },
                               "dampening": True,
                               "tbl_ver": 0,
                               "prefix_received": "0",
                               "local_as": 333,
                               "state_pfxrcd": "0 (no cap)",
                               "community_entries": "[2/96]",
                               "clusterlist_entries": "[7/28]",
                               "history_paths": 0,
                               "dampened_paths": 2,
                               "capable_peers": 2,
                               "up_down": "00:20:33",
                               "msg_rcvd": 29,
                               "bgp_table_version": 173,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "route_identifier": "10.145.0.6",
                               "as": 333,
                               "prefixes": {
                                    "memory_usage": 1220,
                                    "total_entries": 5
                               },
                               "as_path_entries": "[3/106]"
                          },
                          "ipv6 multicast": {
                               "config_peers": 5,
                               "msg_sent": 31,
                               "state": "established",
                               "attribute_entries": "[1/160]",
                               "outq": 0,
                               "path": {
                                    "memory_usage": 488,
                                    "total_entries": 2
                               },
                               "dampening": True,
                               "tbl_ver": 0,
                               "prefix_received": "0",
                               "local_as": 333,
                               "state_pfxrcd": "0 (no cap)",
                               "community_entries": "[2/96]",
                               "clusterlist_entries": "[7/28]",
                               "history_paths": 0,
                               "dampened_paths": 0,
                               "capable_peers": 2,
                               "up_down": "00:20:33",
                               "msg_rcvd": 29,
                               "bgp_table_version": 6,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "route_identifier": "10.145.0.6",
                               "as": 333,
                               "prefixes": {
                                    "memory_usage": 488,
                                    "total_entries": 2
                               },
                               "as_path_entries": "[0/0]"
                          },
                          "vpnv6 unicast": {
                               "config_peers": 3,
                               "msg_sent": 31,
                               "state": "established",
                               "attribute_entries": "[2/320]",
                               "outq": 0,
                               "path": {
                                    "memory_usage": 976,
                                    "total_entries": 4
                               },
                               "dampening": True,
                               "tbl_ver": 13,
                               "prefix_received": "2",
                               "local_as": 333,
                               "state_pfxrcd": "2",
                               "community_entries": "[2/96]",
                               "clusterlist_entries": "[7/28]",
                               "history_paths": 0,
                               "dampened_paths": 0,
                               "capable_peers": 3,
                               "up_down": "00:20:33",
                               "msg_rcvd": 29,
                               "bgp_table_version": 13,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "route_identifier": "10.145.0.6",
                               "as": 333,
                               "prefixes": {
                                    "memory_usage": 976,
                                    "total_entries": 4
                               },
                               "as_path_entries": "[1/42]"
                          },
                          "ipv4 unicast": {
                               "config_peers": 3,
                               "msg_sent": 31,
                               "state": "established",
                               "attribute_entries": "[4/640]",
                               "outq": 0,
                               "path": {
                                    "memory_usage": 1424,
                                    "total_entries": 7
                               },
                               "dampening": True,
                               "tbl_ver": 174,
                               "prefix_received": "3",
                               "local_as": 333,
                               "state_pfxrcd": "3",
                               "community_entries": "[2/96]",
                               "clusterlist_entries": "[7/28]",
                               "history_paths": 0,
                               "dampened_paths": 2,
                               "capable_peers": 3,
                               "up_down": "00:20:33",
                               "msg_rcvd": 29,
                               "bgp_table_version": 174,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "route_identifier": "10.145.0.6",
                               "as": 333,
                               "prefixes": {
                                    "memory_usage": 1424,
                                    "total_entries": 5
                               },
                               "as_path_entries": "[4/144]"
                          },
                          "ipv4 multicast": {
                               "config_peers": 3,
                               "msg_sent": 31,
                               "state": "established",
                               "attribute_entries": "[3/480]",
                               "outq": 0,
                               "path": {
                                    "memory_usage": 1392,
                                    "total_entries": 6
                               },
                               "dampening": True,
                               "tbl_ver": 175,
                               "prefix_received": "2",
                               "local_as": 333,
                               "state_pfxrcd": "2",
                               "community_entries": "[2/96]",
                               "clusterlist_entries": "[7/28]",
                               "history_paths": 0,
                               "dampened_paths": 2,
                               "capable_peers": 3,
                               "up_down": "00:20:33",
                               "msg_rcvd": 29,
                               "bgp_table_version": 175,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "route_identifier": "10.145.0.6",
                               "as": 333,
                               "prefixes": {
                                    "memory_usage": 1392,
                                    "total_entries": 6
                               },
                               "as_path_entries": "[2/56]"
                          },
                          "vpnv4 unicast": {
                               "config_peers": 3,
                               "msg_sent": 31,
                               "state": "established",
                               "attribute_entries": "[4/640]",
                               "outq": 0,
                               "path": {
                                    "memory_usage": 1656,
                                    "total_entries": 8
                               },
                               "dampening": True,
                               "tbl_ver": 183,
                               "prefix_received": "2",
                               "local_as": 333,
                               "state_pfxrcd": "2",
                               "community_entries": "[2/96]",
                               "clusterlist_entries": "[7/28]",
                               "history_paths": 0,
                               "dampened_paths": 2,
                               "capable_peers": 3,
                               "up_down": "00:20:33",
                               "msg_rcvd": 29,
                               "bgp_table_version": 183,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "route_identifier": "10.145.0.6",
                               "as": 333,
                               "prefixes": {
                                    "memory_usage": 1656,
                                    "total_entries": 6
                               },
                               "as_path_entries": "[4/140]"
                          },
                          "link-state": {
                               "config_peers": 5,
                               "msg_sent": 31,
                               "state": "established",
                               "attribute_entries": "[2/320]",
                               "outq": 0,
                               "path": {
                                    "memory_usage": 928,
                                    "total_entries": 4
                               },
                               "dampening": True,
                               "tbl_ver": 173,
                               "prefix_received": "2",
                               "local_as": 333,
                               "state_pfxrcd": "2",
                               "community_entries": "[2/96]",
                               "clusterlist_entries": "[7/28]",
                               "history_paths": 0,
                               "dampened_paths": 2,
                               "capable_peers": 3,
                               "up_down": "00:20:33",
                               "msg_rcvd": 29,
                               "bgp_table_version": 173,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "route_identifier": "10.145.0.6",
                               "as": 333,
                               "prefixes": {
                                    "memory_usage": 928,
                                    "total_entries": 4
                               },
                               "as_path_entries": "[2/84]"
                          }
                     }
                },
                "10.106.102.4": {
                     "address_family": {
                          "ipv6 unicast": {
                               "config_peers": 5,
                               "msg_sent": 31,
                               "state": "established",
                               "attribute_entries": "[3/480]",
                               "outq": 0,
                               "path": {
                                    "memory_usage": 1220,
                                    "total_entries": 5
                               },
                               "dampening": True,
                               "tbl_ver": 0,
                               "prefix_received": "0",
                               "local_as": 333,
                               "state_pfxrcd": "0 (no cap)",
                               "community_entries": "[2/96]",
                               "clusterlist_entries": "[7/28]",
                               "history_paths": 0,
                               "dampened_paths": 2,
                               "capable_peers": 2,
                               "up_down": "00:20:33",
                               "msg_rcvd": 27,
                               "bgp_table_version": 173,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "route_identifier": "10.145.0.6",
                               "as": 333,
                               "prefixes": {
                                    "memory_usage": 1220,
                                    "total_entries": 5
                               },
                               "as_path_entries": "[3/106]"
                          },
                          "ipv6 multicast": {
                               "config_peers": 5,
                               "msg_sent": 31,
                               "state": "established",
                               "attribute_entries": "[1/160]",
                               "outq": 0,
                               "path": {
                                    "memory_usage": 488,
                                    "total_entries": 2
                               },
                               "dampening": True,
                               "tbl_ver": 0,
                               "prefix_received": "0",
                               "local_as": 333,
                               "state_pfxrcd": "0 (no cap)",
                               "community_entries": "[2/96]",
                               "clusterlist_entries": "[7/28]",
                               "history_paths": 0,
                               "dampened_paths": 0,
                               "capable_peers": 2,
                               "up_down": "00:20:33",
                               "msg_rcvd": 27,
                               "bgp_table_version": 6,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "route_identifier": "10.145.0.6",
                               "as": 333,
                               "prefixes": {
                                    "memory_usage": 488,
                                    "total_entries": 2
                               },
                               "as_path_entries": "[0/0]"
                          },
                          "vpnv6 unicast": {
                               "config_peers": 3,
                               "msg_sent": 31,
                               "state": "established",
                               "attribute_entries": "[2/320]",
                               "outq": 0,
                               "path": {
                                    "memory_usage": 976,
                                    "total_entries": 4
                               },
                               "dampening": True,
                               "tbl_ver": 13,
                               "prefix_received": "0",
                               "local_as": 333,
                               "state_pfxrcd": "0",
                               "community_entries": "[2/96]",
                               "clusterlist_entries": "[7/28]",
                               "history_paths": 0,
                               "dampened_paths": 0,
                               "capable_peers": 3,
                               "up_down": "00:20:33",
                               "msg_rcvd": 27,
                               "bgp_table_version": 13,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "route_identifier": "10.145.0.6",
                               "as": 333,
                               "prefixes": {
                                    "memory_usage": 976,
                                    "total_entries": 4
                               },
                               "as_path_entries": "[1/42]"
                          },
                          "ipv4 unicast": {
                               "config_peers": 3,
                               "msg_sent": 31,
                               "state": "established",
                               "attribute_entries": "[4/640]",
                               "outq": 0,
                               "path": {
                                    "memory_usage": 1424,
                                    "total_entries": 7
                               },
                               "dampening": True,
                               "tbl_ver": 174,
                               "prefix_received": "2",
                               "local_as": 333,
                               "state_pfxrcd": "2",
                               "community_entries": "[2/96]",
                               "clusterlist_entries": "[7/28]",
                               "history_paths": 0,
                               "dampened_paths": 2,
                               "capable_peers": 3,
                               "up_down": "00:20:33",
                               "msg_rcvd": 27,
                               "bgp_table_version": 174,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "route_identifier": "10.145.0.6",
                               "as": 333,
                               "prefixes": {
                                    "memory_usage": 1424,
                                    "total_entries": 5
                               },
                               "as_path_entries": "[4/144]"
                          },
                          "ipv4 multicast": {
                               "config_peers": 3,
                               "msg_sent": 31,
                               "state": "established",
                               "attribute_entries": "[3/480]",
                               "outq": 0,
                               "path": {
                                    "memory_usage": 1392,
                                    "total_entries": 6
                               },
                               "dampening": True,
                               "tbl_ver": 175,
                               "prefix_received": "2",
                               "local_as": 333,
                               "state_pfxrcd": "2",
                               "community_entries": "[2/96]",
                               "clusterlist_entries": "[7/28]",
                               "history_paths": 0,
                               "dampened_paths": 2,
                               "capable_peers": 3,
                               "up_down": "00:20:33",
                               "msg_rcvd": 27,
                               "bgp_table_version": 175,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "route_identifier": "10.145.0.6",
                               "as": 333,
                               "prefixes": {
                                    "memory_usage": 1392,
                                    "total_entries": 6
                               },
                               "as_path_entries": "[2/56]"
                          },
                          "vpnv4 unicast": {
                               "config_peers": 3,
                               "msg_sent": 31,
                               "state": "established",
                               "attribute_entries": "[4/640]",
                               "outq": 0,
                               "path": {
                                    "memory_usage": 1656,
                                    "total_entries": 8
                               },
                               "dampening": True,
                               "tbl_ver": 183,
                               "prefix_received": "4",
                               "local_as": 333,
                               "state_pfxrcd": "4",
                               "community_entries": "[2/96]",
                               "clusterlist_entries": "[7/28]",
                               "history_paths": 0,
                               "dampened_paths": 2,
                               "capable_peers": 3,
                               "up_down": "00:20:33",
                               "msg_rcvd": 27,
                               "bgp_table_version": 183,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "route_identifier": "10.145.0.6",
                               "as": 333,
                               "prefixes": {
                                    "memory_usage": 1656,
                                    "total_entries": 6
                               },
                               "as_path_entries": "[4/140]"
                          },
                          "link-state": {
                               "config_peers": 5,
                               "msg_sent": 31,
                               "state": "established",
                               "attribute_entries": "[2/320]",
                               "outq": 0,
                               "path": {
                                    "memory_usage": 928,
                                    "total_entries": 4
                               },
                               "dampening": True,
                               "tbl_ver": 173,
                               "prefix_received": "0",
                               "local_as": 333,
                               "state_pfxrcd": "0",
                               "community_entries": "[2/96]",
                               "clusterlist_entries": "[7/28]",
                               "history_paths": 0,
                               "dampened_paths": 2,
                               "capable_peers": 3,
                               "up_down": "00:20:33",
                               "msg_rcvd": 27,
                               "bgp_table_version": 173,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "route_identifier": "10.145.0.6",
                               "as": 333,
                               "prefixes": {
                                    "memory_usage": 928,
                                    "total_entries": 4
                               },
                               "as_path_entries": "[2/84]"
                          }
                     }
                },
                "2001:db8:8d82::1002": {
                     "address_family": {
                          "ipv6 unicast": {
                               "config_peers": 5,
                               "msg_sent": 26,
                               "state": "established",
                               "attribute_entries": "[3/480]",
                               "outq": 0,
                               "path": {
                                    "memory_usage": 1220,
                                    "total_entries": 5
                               },
                               "dampening": True,
                               "tbl_ver": 173,
                               "prefix_received": "3",
                               "local_as": 333,
                               "state_pfxrcd": "3",
                               "community_entries": "[2/96]",
                               "clusterlist_entries": "[7/28]",
                               "history_paths": 0,
                               "dampened_paths": 2,
                               "capable_peers": 2,
                               "up_down": "00:20:33",
                               "msg_rcvd": 26,
                               "bgp_table_version": 173,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "route_identifier": "10.145.0.6",
                               "as": 333,
                               "prefixes": {
                                    "memory_usage": 1220,
                                    "total_entries": 5
                               },
                               "as_path_entries": "[3/106]"
                          },
                          "ipv6 multicast": {
                               "config_peers": 5,
                               "msg_sent": 26,
                               "state": "established",
                               "attribute_entries": "[1/160]",
                               "outq": 0,
                               "path": {
                                    "memory_usage": 488,
                                    "total_entries": 2
                               },
                               "dampening": True,
                               "tbl_ver": 6,
                               "prefix_received": "2",
                               "local_as": 333,
                               "state_pfxrcd": "2",
                               "community_entries": "[2/96]",
                               "clusterlist_entries": "[7/28]",
                               "history_paths": 0,
                               "dampened_paths": 0,
                               "capable_peers": 2,
                               "up_down": "00:20:33",
                               "msg_rcvd": 26,
                               "bgp_table_version": 6,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "route_identifier": "10.145.0.6",
                               "as": 333,
                               "prefixes": {
                                    "memory_usage": 488,
                                    "total_entries": 2
                               },
                               "as_path_entries": "[0/0]"
                          },
                          "link-state": {
                               "config_peers": 5,
                               "msg_sent": 26,
                               "state": "established",
                               "attribute_entries": "[2/320]",
                               "outq": 0,
                               "path": {
                                    "memory_usage": 928,
                                    "total_entries": 4
                               },
                               "dampening": True,
                               "tbl_ver": 0,
                               "prefix_received": "0",
                               "local_as": 333,
                               "state_pfxrcd": "0 (no cap)",
                               "community_entries": "[2/96]",
                               "clusterlist_entries": "[7/28]",
                               "history_paths": 0,
                               "dampened_paths": 2,
                               "capable_peers": 3,
                               "up_down": "00:20:33",
                               "msg_rcvd": 26,
                               "bgp_table_version": 173,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "route_identifier": "10.145.0.6",
                               "as": 333,
                               "prefixes": {
                                    "memory_usage": 928,
                                    "total_entries": 4
                               },
                               "as_path_entries": "[2/84]"
                          }
                     }
                },
                "2001:db8:8d82::2002": {
                     "address_family": {
                          "ipv6 unicast": {
                               "config_peers": 5,
                               "msg_sent": 25,
                               "state": "established",
                               "attribute_entries": "[3/480]",
                               "outq": 0,
                               "path": {
                                    "memory_usage": 1220,
                                    "total_entries": 5
                               },
                               "dampening": True,
                               "tbl_ver": 173,
                               "prefix_received": "2",
                               "local_as": 333,
                               "state_pfxrcd": "2",
                               "community_entries": "[2/96]",
                               "clusterlist_entries": "[7/28]",
                               "history_paths": 0,
                               "dampened_paths": 2,
                               "capable_peers": 2,
                               "up_down": "00:20:33",
                               "msg_rcvd": 187,
                               "bgp_table_version": 173,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "route_identifier": "10.145.0.6",
                               "as": 888,
                               "prefixes": {
                                    "memory_usage": 1220,
                                    "total_entries": 5
                               },
                               "as_path_entries": "[3/106]"
                          },
                          "ipv6 multicast": {
                               "config_peers": 5,
                               "msg_sent": 25,
                               "state": "established",
                               "attribute_entries": "[1/160]",
                               "outq": 0,
                               "path": {
                                    "memory_usage": 488,
                                    "total_entries": 2
                               },
                               "dampening": True,
                               "tbl_ver": 6,
                               "prefix_received": "0",
                               "local_as": 333,
                               "state_pfxrcd": "0",
                               "community_entries": "[2/96]",
                               "clusterlist_entries": "[7/28]",
                               "history_paths": 0,
                               "dampened_paths": 0,
                               "capable_peers": 2,
                               "up_down": "00:20:33",
                               "msg_rcvd": 187,
                               "bgp_table_version": 6,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "route_identifier": "10.145.0.6",
                               "as": 888,
                               "prefixes": {
                                    "memory_usage": 488,
                                    "total_entries": 2
                               },
                               "as_path_entries": "[0/0]"
                          },
                          "link-state": {
                               "config_peers": 5,
                               "msg_sent": 25,
                               "state": "established",
                               "attribute_entries": "[2/320]",
                               "outq": 0,
                               "path": {
                                    "memory_usage": 928,
                                    "total_entries": 4
                               },
                               "dampening": True,
                               "tbl_ver": 0,
                               "prefix_received": "0",
                               "local_as": 333,
                               "state_pfxrcd": "0 (no cap)",
                               "community_entries": "[2/96]",
                               "clusterlist_entries": "[7/28]",
                               "history_paths": 0,
                               "dampened_paths": 2,
                               "capable_peers": 3,
                               "up_down": "00:20:33",
                               "msg_rcvd": 187,
                               "bgp_table_version": 173,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "route_identifier": "10.145.0.6",
                               "as": 888,
                               "prefixes": {
                                    "memory_usage": 928,
                                    "total_entries": 4
                               },
                               "as_path_entries": "[2/84]"
                          }
                     }
                },
                "10.106.102.3": {
                     "address_family": {
                          "ipv6 unicast": {
                               "config_peers": 5,
                               "msg_sent": 28,
                               "state": "established",
                               "attribute_entries": "[3/480]",
                               "outq": 0,
                               "path": {
                                    "memory_usage": 1220,
                                    "total_entries": 5
                               },
                               "dampening": True,
                               "tbl_ver": 0,
                               "prefix_received": "0",
                               "local_as": 333,
                               "state_pfxrcd": "0 (no cap)",
                               "community_entries": "[2/96]",
                               "clusterlist_entries": "[7/28]",
                               "history_paths": 0,
                               "dampened_paths": 2,
                               "capable_peers": 2,
                               "up_down": "00:20:33",
                               "msg_rcvd": 841,
                               "bgp_table_version": 173,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "route_identifier": "10.145.0.6",
                               "as": 888,
                               "prefixes": {
                                    "memory_usage": 1220,
                                    "total_entries": 5
                               },
                               "as_path_entries": "[3/106]"
                          },
                          "ipv6 multicast": {
                               "config_peers": 5,
                               "msg_sent": 28,
                               "state": "established",
                               "attribute_entries": "[1/160]",
                               "outq": 0,
                               "path": {
                                    "memory_usage": 488,
                                    "total_entries": 2
                               },
                               "dampening": True,
                               "tbl_ver": 0,
                               "prefix_received": "0",
                               "local_as": 333,
                               "state_pfxrcd": "0 (no cap)",
                               "community_entries": "[2/96]",
                               "clusterlist_entries": "[7/28]",
                               "history_paths": 0,
                               "dampened_paths": 0,
                               "capable_peers": 2,
                               "up_down": "00:20:33",
                               "msg_rcvd": 841,
                               "bgp_table_version": 6,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "route_identifier": "10.145.0.6",
                               "as": 888,
                               "prefixes": {
                                    "memory_usage": 488,
                                    "total_entries": 2
                               },
                               "as_path_entries": "[0/0]"
                          },
                          "vpnv6 unicast": {
                               "config_peers": 3,
                               "msg_sent": 28,
                               "state": "established",
                               "attribute_entries": "[2/320]",
                               "outq": 0,
                               "path": {
                                    "memory_usage": 976,
                                    "total_entries": 4
                               },
                               "dampening": True,
                               "tbl_ver": 13,
                               "prefix_received": "2",
                               "local_as": 333,
                               "state_pfxrcd": "2",
                               "community_entries": "[2/96]",
                               "clusterlist_entries": "[7/28]",
                               "history_paths": 0,
                               "dampened_paths": 0,
                               "capable_peers": 3,
                               "up_down": "00:20:33",
                               "msg_rcvd": 841,
                               "bgp_table_version": 13,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "route_identifier": "10.145.0.6",
                               "as": 888,
                               "prefixes": {
                                    "memory_usage": 976,
                                    "total_entries": 4
                               },
                               "as_path_entries": "[1/42]"
                          },
                          "ipv4 unicast": {
                               "config_peers": 3,
                               "msg_sent": 28,
                               "state": "established",
                               "attribute_entries": "[4/640]",
                               "outq": 0,
                               "path": {
                                    "memory_usage": 1424,
                                    "total_entries": 7
                               },
                               "dampening": True,
                               "tbl_ver": 174,
                               "prefix_received": "2",
                               "local_as": 333,
                               "state_pfxrcd": "2",
                               "community_entries": "[2/96]",
                               "clusterlist_entries": "[7/28]",
                               "history_paths": 0,
                               "dampened_paths": 2,
                               "capable_peers": 3,
                               "up_down": "00:20:33",
                               "msg_rcvd": 841,
                               "bgp_table_version": 174,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "route_identifier": "10.145.0.6",
                               "as": 888,
                               "prefixes": {
                                    "memory_usage": 1424,
                                    "total_entries": 5
                               },
                               "as_path_entries": "[4/144]"
                          },
                          "ipv4 multicast": {
                               "config_peers": 3,
                               "msg_sent": 28,
                               "state": "established",
                               "attribute_entries": "[3/480]",
                               "outq": 0,
                               "path": {
                                    "memory_usage": 1392,
                                    "total_entries": 6
                               },
                               "dampening": True,
                               "tbl_ver": 175,
                               "prefix_received": "2",
                               "local_as": 333,
                               "state_pfxrcd": "2",
                               "community_entries": "[2/96]",
                               "clusterlist_entries": "[7/28]",
                               "history_paths": 0,
                               "dampened_paths": 2,
                               "capable_peers": 3,
                               "up_down": "00:20:33",
                               "msg_rcvd": 841,
                               "bgp_table_version": 175,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "route_identifier": "10.145.0.6",
                               "as": 888,
                               "prefixes": {
                                    "memory_usage": 1392,
                                    "total_entries": 6
                               },
                               "as_path_entries": "[2/56]"
                          },
                          "vpnv4 unicast": {
                               "config_peers": 3,
                               "msg_sent": 28,
                               "state": "established",
                               "attribute_entries": "[4/640]",
                               "outq": 0,
                               "path": {
                                    "memory_usage": 1656,
                                    "total_entries": 8
                               },
                               "dampening": True,
                               "tbl_ver": 183,
                               "prefix_received": "2",
                               "local_as": 333,
                               "state_pfxrcd": "2",
                               "community_entries": "[2/96]",
                               "clusterlist_entries": "[7/28]",
                               "history_paths": 0,
                               "dampened_paths": 2,
                               "capable_peers": 3,
                               "up_down": "00:20:33",
                               "msg_rcvd": 841,
                               "bgp_table_version": 183,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "route_identifier": "10.145.0.6",
                               "as": 888,
                               "prefixes": {
                                    "memory_usage": 1656,
                                    "total_entries": 6
                               },
                               "as_path_entries": "[4/140]"
                          },
                          "link-state": {
                               "config_peers": 5,
                               "msg_sent": 28,
                               "state": "established",
                               "attribute_entries": "[2/320]",
                               "outq": 0,
                               "path": {
                                    "memory_usage": 928,
                                    "total_entries": 4
                               },
                               "dampening": True,
                               "tbl_ver": 173,
                               "prefix_received": "2",
                               "local_as": 333,
                               "state_pfxrcd": "2",
                               "community_entries": "[2/96]",
                               "clusterlist_entries": "[7/28]",
                               "history_paths": 0,
                               "dampened_paths": 2,
                               "capable_peers": 3,
                               "up_down": "00:20:33",
                               "msg_rcvd": 841,
                               "bgp_table_version": 173,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "route_identifier": "10.145.0.6",
                               "as": 888,
                               "prefixes": {
                                    "memory_usage": 928,
                                    "total_entries": 4
                               },
                               "as_path_entries": "[2/84]"
                          }
                     }
                }
           }
      },
      "vpn1": {
           "neighbor": {
                "10.106.103.1": {
                     "address_family": {
                          "ipv6 unicast": {
                               "clusterlist_entries": "[7/28]",
                               "state_pfxrcd": "idle",
                               "config_peers": 1,
                               "msg_sent": 0,
                               "msg_rcvd": 0,
                               "capable_peers": 0,
                               "state": "idle",
                               "attribute_entries": "[0/0]",
                               "up_down": "00:20:35",
                               "path": {
                                    "memory_usage": 0,
                                    "total_entries": 0
                               },
                               "outq": 0,
                               "bgp_table_version": 2,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "tbl_ver": 0,
                               "route_identifier": "0.0.0.0",
                               "local_as": 333,
                               "as": 333,
                               "prefixes": {
                                    "memory_usage": 0,
                                    "total_entries": 0
                               },
                               "community_entries": "[2/96]",
                               "as_path_entries": "[0/0]"
                          },
                          "ipv4 multicast": {
                               "clusterlist_entries": "[7/28]",
                               "state_pfxrcd": "idle",
                               "config_peers": 1,
                               "msg_sent": 0,
                               "msg_rcvd": 0,
                               "capable_peers": 0,
                               "state": "idle",
                               "attribute_entries": "[0/0]",
                               "up_down": "00:20:35",
                               "path": {
                                    "memory_usage": 0,
                                    "total_entries": 0
                               },
                               "outq": 0,
                               "bgp_table_version": 2,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "tbl_ver": 0,
                               "route_identifier": "0.0.0.0",
                               "local_as": 333,
                               "as": 333,
                               "prefixes": {
                                    "memory_usage": 0,
                                    "total_entries": 0
                               },
                               "community_entries": "[2/96]",
                               "as_path_entries": "[0/0]"
                          },
                          "ipv4 unicast": {
                               "clusterlist_entries": "[7/28]",
                               "state_pfxrcd": "idle",
                               "config_peers": 1,
                               "msg_sent": 0,
                               "msg_rcvd": 0,
                               "capable_peers": 0,
                               "state": "idle",
                               "attribute_entries": "[2/320]",
                               "up_down": "00:20:35",
                               "path": {
                                    "memory_usage": 300,
                                    "total_entries": 3
                               },
                               "outq": 0,
                               "bgp_table_version": 9,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "tbl_ver": 0,
                               "route_identifier": "0.0.0.0",
                               "local_as": 333,
                               "as": 333,
                               "prefixes": {
                                    "memory_usage": 300,
                                    "total_entries": 3
                               },
                               "community_entries": "[2/96]",
                               "as_path_entries": "[2/80]"
                          },
                          "ipv6 multicast": {
                               "clusterlist_entries": "[7/28]",
                               "state_pfxrcd": "idle",
                               "config_peers": 1,
                               "msg_sent": 0,
                               "msg_rcvd": 0,
                               "capable_peers": 0,
                               "state": "idle",
                               "attribute_entries": "[0/0]",
                               "up_down": "00:20:35",
                               "path": {
                                    "memory_usage": 0,
                                    "total_entries": 0
                               },
                               "outq": 0,
                               "bgp_table_version": 2,
                               "neighbor_table_version": 4,
                               "inq": 0,
                               "tbl_ver": 0,
                               "route_identifier": "0.0.0.0",
                               "local_as": 333,
                               "as": 333,
                               "prefixes": {
                                    "memory_usage": 0,
                                    "total_entries": 0
                               },
                               "community_entries": "[2/96]",
                               "as_path_entries": "[0/0]"
                          }
                     }
                }
           }
        }
    }
}
