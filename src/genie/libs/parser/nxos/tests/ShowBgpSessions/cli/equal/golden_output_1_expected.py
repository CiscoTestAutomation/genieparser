

expected_output = {
    "total_peers": 3,
    "total_established_peers": 2,
    "local_as": 333,
    "vrf": {
      "default": {
           "router_id": "10.106.0.6",
           "neighbor": {
                "10.106.102.4": {
                     "last_flap": "01:03:35",
                     "last_write": "00:00:09",
                     "last_read": "00:00:41",
                     "remote_port": 36462,
                     "notifications_sent": 0,
                     "local_port": 179,
                     "notifications_received": 0,
                     "connections_dropped": 0,
                     "state": "established",
                     "remote_as": 333
                },
                "10.106.101.1": {
                     "last_flap": "01:03:35",
                     "last_write": "00:00:09",
                     "last_read": "00:00:41",
                     "remote_port": 48392,
                     "notifications_sent": 0,
                     "local_port": 179,
                     "notifications_received": 0,
                     "connections_dropped": 0,
                     "state": "established",
                     "remote_as": 333
                },
                "10.106.102.3": {
                     "last_flap": "01:03:39",
                     "last_write": "never",
                     "last_read": "never",
                     "remote_port": 0,
                     "notifications_sent": 0,
                     "local_port": 0,
                     "notifications_received": 0,
                     "connections_dropped": 0,
                     "state": "idle",
                     "remote_as": 888
                }
           },
           "vrf_peers": 3,
           "vrf_established_peers": 2,
           "local_as": 333
        },
        "vpn1": {
           "router_id": "10.229.11.11",
           "vrf_peers": 0,
           "vrf_established_peers": 0,
           "local_as": 333
        }
    }
}
