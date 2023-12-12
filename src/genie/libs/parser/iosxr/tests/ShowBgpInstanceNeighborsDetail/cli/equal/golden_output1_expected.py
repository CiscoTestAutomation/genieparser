expected_output = {
    "instance": {
        "all": {
            "vrf": {
                "default": {
                    "neighbor": {
                        "10.4.1.1": {
                            "remote_as": 65000,
                            "link_state": "internal link",
                            "local_as_as_no": 65000,
                            "local_as_no_prepend": True,
                            "local_as_replace_as": True,
                            "local_as_dual_as": True,
                            "router_id": "10.4.1.1",
                            "session_state": "established",
                            "up_time": "1w1d",
                            "nsr_state": "None",
                            "holdtime": 180,
                            "keepalive_interval": 60,
                            "min_acceptable_hold_time": 3,
                            "last_write": "00:00:03",
                            "attempted": 19,
                            "written": 19,
                            "second_last_write": "00:01:03",
                            "second_attempted": 19,
                            "second_written": 19,
                            "last_write_pulse_rcvd": "Nov  1 21:31:48.334 ",
                            "last_full_not_set_pulse_count": 85322,
                            "last_ka_error_before_reset": "00:00:00",
                            "last_ka_error_ka_not_sent": "00:00:00",
                            "precedence": "internet",
                            "non_stop_routing": True,
                            "multiprotocol_capability": "received",
                            "minimum_time_between_adv_runs": 0,
                            "inbound_message": "3",
                            "outbound_message": "3",
                            "configured_holdtime": 180,
                            "configured_keepalive_interval": 60,
                            "messages": {
                                "received": {
                                    "messages_count": 44766,
                                    "notifications": 0,
                                    "queue": 0,
                                },
                                "sent": {
                                    "messages_count": 40667,
                                    "notifications": 1,
                                    "queue": 0,
                                },
                            },
                            "address_family": {
                                "ipv4 unicast": {
                                    "neighbor_version": 7,
                                    "update_group": "0.2",
                                    "filter_group": "0.1",
                                    "refresh_request_status": "No Refresh request being processed",
                                    "route_refresh_request_received": 0,
                                    "route_refresh_request_sent": 0,
                                    "accepted_prefixes": 1,
                                    "best_paths": 1,
                                    "exact_no_prefixes_denied": 0,
                                    "cummulative_no_prefixes_denied": 0,
                                    "prefix_advertised": 1,
                                    "prefix_suppressed": 0,
                                    "prefix_withdrawn": 0,
                                    "maximum_prefix_max_prefix_no": 1048576,
                                    "maximum_prefix_warning_only": True,
                                    "maximum_prefix_threshold": "75%",
                                    "maximum_prefix_restart": 0,
                                    "eor_status": "was received during read-only mode",
                                    "last_synced_ack_version": 0,
                                    "last_ack_version": 7,
                                    "additional_paths_operation": "None",
                                    "send_multicast_attributes": True,
                                    "additional_routes_local_label": "Unicast SAFI",
                                }
                            },
                            "bgp_negotiated_capabilities": {
                                "four_octets_asn": "advertised received",
                                "ipv4_unicast": "advertised received",
                                "route_refresh": "advertised received",
                            },
                            "bgp_session_transport": {
                                "connection": {
                                    "state": "established",
                                    "connections_established": 2,
                                    "connections_dropped": 1,
                                },
                                "transport": {
                                    "local_host": "10.16.2.2",
                                    "local_port": "179",
                                    "if_handle": "0x00000000",
                                    "foreign_host": "10.4.1.1",
                                    "foreign_port": "27104",
                                },
                            },
                        }
                    }
                }
            }
        }
    }
}
