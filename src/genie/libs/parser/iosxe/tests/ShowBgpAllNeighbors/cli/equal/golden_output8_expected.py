expected_output = {
    "list_of_neighbors": [
        "100.64.0.1"
    ],
    "vrf": {
        "default": {
            "neighbor": {
                "100.64.0.1": {
                    "remote_as": "1.101",
                    "link": "external",
                    "shutdown": False,
                    "address_family": {
                        "ipv4 unicast": {
                            "session_state": "Idle",
                            "down_time": "06:06:59"
                        },
                        "ipv6 unicast": {},
                        "ipv4 multicast": {},
                        "l2vpn evpn": {},
                        "mvpnv4 unicast": {},
                        "mvpnv6 unicast": {},
                        "ipv4 labelunicast": {},
                        "ipv6 labelunicast": {}
                    },
                    "description": "svs-fc-agg-t1-a-1",
                    "peer_group": "T1-ASN1.101",
                    "bgp_version": 4,
                    "router_id": "0.0.0.0",
                    "session_state": "Idle",
                    "bgp_negotiated_keepalive_timers": {
                        "hold_time": 15,
                        "keepalive_interval": 5,
                        "min_holdtime": 0
                    },
                    "bgp_neighbor_session": {
                        "sessions": 0,
                        "stateful_switchover": "NO"
                    },
                    "bgp_session_transport": {
                        "min_time_between_advertisement_runs": 30,
                        "address_tracking_status": "enabled",
                        "rib_route_ip": "100.64.0.1",
                        "connection": {
                            "established": 1,
                            "dropped": 1,
                            "last_reset": "06:06:59",
                            "reset_reason": "Active open failed"
                        },
                        "tcp_path_mtu_discovery": "enabled",
                        "graceful_restart": "enabled",
                        "gr_restart_time": 120,
                        "gr_stalepath_time": 360,
                        "sso": False,
                        "tcp_connection": False
                    }
                }
            }
        }
    }
} 
