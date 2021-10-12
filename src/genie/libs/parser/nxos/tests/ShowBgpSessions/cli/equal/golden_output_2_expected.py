

expected_output = {
    "local_as": 100,
    "total_established_peers": 3,
    "total_peers": 4,
    "vrf": {
      "default": {
           "router_id": "10.1.1.1",
           "vrf_peers": 4,
           "vrf_established_peers": 3,
           "local_as": 100,
           "neighbor": {
                "10.51.1.101": {
                     "last_write": "never",
                     "state": "idle",
                     "notifications_received": 0,
                     "last_flap": "00:30:22",
                     "notifications_sent": 2,
                     "remote_port": 0,
                     "local_port": 0,
                     "last_read": "never",
                     "remote_as": 300,
                     "connections_dropped": 2
                },
                "2001:db8:4:1::1:1": {
                     "last_write": "00:00:04",
                     "state": "established",
                     "notifications_received": 0,
                     "last_flap": "12:11:57",
                     "notifications_sent": 0,
                     "remote_port": 179,
                     "local_port": 30942,
                     "last_read": "0.599405",
                     "remote_as": 100,
                     "connections_dropped": 1
                },
                "2001:db8:1900:1::1:101": {
                     "last_write": "00:00:13",
                     "state": "established",
                     "notifications_received": 0,
                     "last_flap": "02:29:16",
                     "notifications_sent": 5,
                     "remote_port": 32874,
                     "local_port": 179,
                     "last_read": "00:00:15",
                     "remote_as": 300,
                     "connections_dropped": 5
                },
                "192.168.4.1": {
                     "last_write": "00:00:20",
                     "state": "established",
                     "notifications_received": 0,
                     "last_flap": "12:12:01",
                     "notifications_sent": 0,
                     "remote_port": 37583,
                     "local_port": 179,
                     "last_read": "00:00:04",
                     "remote_as": 100,
                     "connections_dropped": 1
                }
            }
        }
    }
}
