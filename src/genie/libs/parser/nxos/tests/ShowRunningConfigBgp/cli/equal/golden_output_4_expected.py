expected_output = {
   "bgp": {
      "instance": {
         "default": {
            "bgp_id": 65000,
            "protocol_shutdown": False,
            "vrf": {
               "bgptesting": {
                  "graceful_restart": True,
                  "log_neighbor_changes": True,
                  "router_id": "192.168.1.1",
                  "enforce_first_as": True,
                  "fast_external_fallover": True,
                  "flush_routes": False,
                  "isolate": False,
                  "af_name": {
                     "ipv4 unicast": {
                        "af_client_to_client_reflection": True,
                        "af_network_number": [
                           "192.168.1.1",
                           "192.168.3.0"
                        ],
                        "af_network_mask": [
                           32,
                           24
                        ]
                     }
                  },
                  "neighbor_id": {
                     "192.168.3.2": {
                        "nbr_fall_over_bfd": False,
                        "nbr_suppress_four_byte_as_capability": False,
                        "nbr_disable_connected_check": False,
                        "nbr_ebgp_multihop": False,
                        "nbr_local_as_no_prepend": False,
                        "nbr_local_as_replace_as": False,
                        "nbr_local_as_dual_as": False,
                        "nbr_remote_as": 65001,
                        "nbr_remove_private_as": False,
                        "nbr_shutdown": False,
                        "nbr_af_name": {
                           "ipv4 unicast": {}
                        }
                     }
                  }
               }
            }
         }
      }
   }
}