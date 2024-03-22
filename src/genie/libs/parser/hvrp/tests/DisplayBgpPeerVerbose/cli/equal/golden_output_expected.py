expected_output = {
    "vrf": {
        "default": {
            "peer": {
                "10.10.10.10": {
                    "remote_as": "65000",
                    "peer_type": "EBGP link",
                    "description": "TEST",
                    "bgp_version": 4,
                    "remote_router_id": "1.1.1.1",
                    "update_group_id": 2,
                    "current_state": "Established",
                    "up_time": "00h11m41s",
                    "last_state": "OpenConfirm",
                    "peer_up_count": 1,
                    "prefixes_counters": {
                        "received": 40,
                        "active": 24,
                        "advertised": 16
                    },
                    "transport": {
                        "local_port": 57164,
                        "remote_port": 179
                    },
                    "capabilities": {
                        "multi-protocol extension": "",
                        "route refresh capability": "",
                        "4-byte-as capability": "",
                        "VPNv4 Unicast": "advertised and received",
                        "VPNv6 Unicast": "advertised and received"
                    },
                    "messages_counters": {
                        "received": {
                            "total": 143,
                            "update": 66,
                            "open": 1,
                            "keepalive": 76,
                            "notification": 0,
                            "refresh": 0
                        },
                        "sent": {
                            "total": 93,
                            "update": 7,
                            "open": 1,
                            "keepalive": 85,
                            "notification": 0,
                            "refresh": 0
                        }
                    },
                    "route_update_interval": "30",
                    "route_policies": {
                        "import": "FROM_RRVPN",
                        "export": "KEEP_MED"
                    }
                }
            }
        }
    }
}
