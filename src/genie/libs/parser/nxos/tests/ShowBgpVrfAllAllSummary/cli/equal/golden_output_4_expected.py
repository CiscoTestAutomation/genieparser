

expected_output = {
    "vrf": {
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
                "10.10.80.1": {
                     "address_family": {
                          "ipv4 unicast": {
                               "msg_rcvd": 578124,
                               "path": {
                                    "memory_usage": 0,
                                    "total_entries": 0
                               },
                               "tbl_ver": 3272,
                               "clusterlist_entries": "[1/4]",
                               "as_path_entries": "[0/0]",
                               "up_down": "9w3d",
                               "dampening": True,
                               "community_entries": "[0/0]",
                               "state_pfxrcd": "297",
                               "state": "established",
                               "history_paths": 0,
                               "prefixes": {
                                    "memory_usage": 0,
                                    "total_entries": 0
                               },
                               "prefix_received": "297",
                               "local_as": 100,
                               "msg_sent": 577455,
                               "dampened_paths": 0,
                               "neighbor_table_version": 4,
                               "as": 4210410100,
                               "capable_peers": 0,
                               "outq": 0,
                               "attribute_entries": "[0/0]",
                               "route_identifier": "10.4.1.1",
                               "inq": 0,
                               "bgp_table_version": 2,
                               "config_peers": 1
                          }
                     }
                }
           }
        }
    }
}
