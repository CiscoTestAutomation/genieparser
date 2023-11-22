expected_output = {
    "total_established_peers": 4, 
    "local_as": 1, 
    "vrf": {
        "default": {
            "router_id": "1.1.1.1", 
            "vrf_established_peers": 4, 
            "local_as": 1, 
            "vrf_peers": 4, 
            "neighbor": {
                "99.99.99.99": {
                    "state": "established", 
                    "notifications_sent": 0, 
                    "notifications_received": 0, 
                    "last_write": "00:00:19", 
                    "last_read": "00:00:19", 
                    "local_port": 50938, 
                    "remote_as": 1, 
                    "last_flap": "01:05:37", 
                    "remote_port": 179, 
                    "connections_dropped": 0
                }, 
                "fe80::a111:2222:3333:e11": {
                    "last_read": "00:00:50", 
                    "notifications_sent": 0, 
                    "remote_as": 1, 
                    "local_port": 27490, 
                    "remote_port": 179, 
                    "state": "established", 
                    "notifications_received": 0, 
                    "connections_dropped": 0, 
                    "last_write": "00:00:50", 
                    "last_flap": "01:05:51", 
                    "linklocal_interfaceport": "Ethernet1/1"
                }, 
                "fe80::b111:2222:3333:e11": {
                    "last_read": "00:00:49", 
                    "notifications_sent": 0, 
                    "remote_as": 1, 
                    "local_port": 48598, 
                    "remote_port": 179, 
                    "state": "established", 
                    "notifications_received": 0, 
                    "connections_dropped": 0, 
                    "last_write": "00:00:50", 
                    "last_flap": "01:05:50", 
                    "linklocal_interfaceport": "Ethernet1/2"
                }, 
                "98.98.98.98": {
                    "state": "established", 
                    "notifications_sent": 0, 
                    "notifications_received": 0, 
                    "last_write": "00:00:19", 
                    "last_read": "00:00:19", 
                    "local_port": 26550, 
                    "remote_as": 1, 
                    "last_flap": "01:05:37", 
                    "remote_port": 179, 
                    "connections_dropped": 0
                }
            }
        }
    }, 
    "total_peers": 4
}
