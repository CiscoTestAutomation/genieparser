expected_output = {
    "list_of_neighbors": ["192.168.10.254"],
    "vrf": {
        "default": {
            "neighbor": {
                "192.168.10.254": {
                    "remote_as": 65109,
                    "link": "external",
                    "shutdown": False,
                    "bgp_version": 4,
                    "router_id": "0.0.0.0",
                    "session_state": "Idle",
                    "bgp_negotiated_keepalive_timers": {
                        "hold_time": 90,
                        "keepalive_interval": 30,
                        "min_holdtime": 15,
                    },
                    "bgp_neighbor_counters": {
                        "messages": {
                            "sent": {
                                "opens": 0,
                                "notifications": 0,
                                "updates": 0,
                                "keepalives": 0,
                                "route_refresh": 0,
                                "total": 0,
                            },
                            "received": {
                                "opens": 0,
                                "notifications": 0,
                                "updates": 0,
                                "keepalives": 0,
                                "route_refresh": 0,
                                "total": 0,
                            },
                            "in_queue_depth": 0,
                            "out_queue_depth": 0,
                        }
                    },
                    "bgp_session_transport": {
                        "min_time_between_advertisement_runs": 30,
                        "connection": {
                            "established": 0,
                            "dropped": 0,
                            "last_reset": "never",
                        },
                        "tcp_connection": False,
                    },
                    "address_family": {
                        "ipv4 unicast": {
                            "bgp_table_version": 1,
                            "neighbor_version": "0/0",
                            "output_queue_size": 0,
                            "update_group_member": 0,
                            "community_attribute_sent": True,
                            "prefix_activity_counters": {
                                "sent": {
                                    "prefixes_current": 0,
                                    "prefixes_total": 0,
                                    "implicit_withdraw": 0,
                                    "explicit_withdraw": 0,
                                    "used_as_bestpath": "n/a",
                                    "used_as_multipath": "n/a",
                                },
                                "received": {
                                    "prefixes_current": 0,
                                    "prefixes_total": 0,
                                    "implicit_withdraw": 0,
                                    "explicit_withdraw": 0,
                                    "used_as_bestpath": 0,
                                    "used_as_multipath": 0,
                                },
                            },
                            "local_policy_denied_prefixes_counters": {
                                "outbound": {"total": 0},
                                "inbound": {"total": 0},
                            },
                            "max_nlri": 0,
                            "min_nlri": 0,
                        }
                    },
                }
            }
        }
    },
}
