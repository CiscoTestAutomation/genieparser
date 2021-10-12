

expected_output = {
    "vrf": {
      "VRF1": {
           "neighbor": {
                "10.16.2.10": {
                     "address_family": {
                          "ipv4 unicast": {
                               "msg_rcvd": 0,
                               "path": {
                                    "memory_usage": 620,
                                    "total_entries": 5
                               },
                               "tbl_ver": 0,
                               "clusterlist_entries": "[1/4]",
                               "as_path_entries": "[0/0]",
                               "up_down": "5w6d",
                               "dampening": True,
                               "community_entries": "[0/0]",
                               "state_pfxrcd": "idle",
                               "state": "idle",
                               "history_paths": 0,
                               "prefixes": {
                                    "memory_usage": 620,
                                    "total_entries": 5
                               },
                               "local_as": 100,
                               "msg_sent": 0,
                               "dampened_paths": 0,
                               "neighbor_table_version": 4,
                               "as": 0,
                               "capable_peers": 0,
                               "outq": 0,
                               "attribute_entries": "[3/384]",
                               "route_identifier": "10.64.4.4",
                               "inq": 0,
                               "bgp_table_version": 40,
                               "config_peers": 1
                          }
                     }
                }
           }
      },
      "default": {
           "neighbor": {
                "10.16.2.5": {
                     "address_family": {
                          "ipv4 unicast": {
                               "msg_rcvd": 0,
                               "path": {
                                    "memory_usage": 0,
                                    "total_entries": 0
                               },
                               "tbl_ver": 0,
                               "clusterlist_entries": "[1/4]",
                               "as_path_entries": "[0/0]",
                               "up_down": "5w6d",
                               "dampening": True,
                               "community_entries": "[0/0]",
                               "state_pfxrcd": "shut (admin)",
                               "state": "shut (admin)",
                               "history_paths": 0,
                               "prefixes": {
                                    "memory_usage": 0,
                                    "total_entries": 0
                               },
                               "local_as": 100,
                               "msg_sent": 0,
                               "dampened_paths": 0,
                               "neighbor_table_version": 4,
                               "as": 200,
                               "capable_peers": 0,
                               "outq": 0,
                               "attribute_entries": "[0/0]",
                               "route_identifier": "10.4.1.1",
                               "inq": 0,
                               "bgp_table_version": 2,
                               "config_peers": 1
                          }
                     }
                },
                "2001:db8:8191:506d:5::5": {
                     "address_family": {
                          "ipv4 unicast": {
                               "msg_rcvd": 0,
                               "path": {
                                    "memory_usage": 0,
                                    "total_entries": 0
                               },
                               "tbl_ver": 0,
                               "clusterlist_entries": "[1/4]",
                               "as_path_entries": "[0/0]",
                               "up_down": "5w5d",
                               "dampening": True,
                               "community_entries": "[0/0]",
                               "state_pfxrcd": "shut (admin)",
                               "state": "shut (admin)",
                               "history_paths": 0,
                               "prefixes": {
                                    "memory_usage": 0,
                                    "total_entries": 0
                               },
                               "local_as": 100,
                               "msg_sent": 0,
                               "dampened_paths": 0,
                               "neighbor_table_version": 3,
                               "as": 200,
                               "capable_peers": 0,
                               "outq": 0,
                               "attribute_entries": "[0/0]",
                               "route_identifier": "10.4.1.1",
                               "inq": 0,
                               "bgp_table_version": 2,
                               "config_peers": 1
                          }
                     }
                },
                "10.16.2.2": {
                     "address_family": {
                          "vpnv6 unicast": {
                               "msg_rcvd": 108554,
                               "path": {
                                    "memory_usage": 544,
                                    "total_entries": 4
                               },
                               "tbl_ver": 45,
                               "clusterlist_entries": "[1/4]",
                               "as_path_entries": "[0/0]",
                               "up_down": "5w6d",
                               "community_entries": "[0/0]",
                               "state_pfxrcd": "1",
                               "state": "established",
                               "prefix_received": '1',
                               "prefixes": {
                                    "memory_usage": 544,
                                    "total_entries": 4
                               },
                               "local_as": 100,
                               "msg_sent": 108566,
                               "neighbor_table_version": 4,
                               "as": 100,
                               "capable_peers": 1,
                               "outq": 0,
                               "attribute_entries": "[1/128]",
                               "route_identifier": "10.4.1.1",
                               "inq": 0,
                               "bgp_table_version": 45,
                               "config_peers": 1
                          },
                          "vpnv4 unicast": {
                               "msg_rcvd": 108554,
                               "path": {
                                    "memory_usage": 620,
                                    "total_entries": 5
                               },
                               "tbl_ver": 53,
                               "clusterlist_entries": "[1/4]",
                               "as_path_entries": "[0/0]",
                               "up_down": "5w6d",
                               "community_entries": "[0/0]",
                               "state_pfxrcd": "1",
                               "state": "established",
                               "prefix_received": '1',
                               "prefixes": {
                                    "memory_usage": 620,
                                    "total_entries": 5
                               },
                               "local_as": 100,
                               "msg_sent": 108566,
                               "neighbor_table_version": 4,
                               "as": 100,
                               "capable_peers": 1,
                               "outq": 0,
                               "attribute_entries": "[1/128]",
                               "route_identifier": "10.4.1.1",
                               "inq": 0,
                               "bgp_table_version": 53,
                               "config_peers": 1
                          }
                     }
                }
           }
        }
    }
}
