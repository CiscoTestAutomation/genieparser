expected_output = {
    "list_of_neighbors": [
        "34.0.0.1"
    ],
    "vrf": {
        "default": {
            "neighbor": {
                "34.0.0.1": {
                    "remote_as": 200,
                    "link": "external",
                    "shutdown": False,
                    "bgp_version": 4,
                    "router_id": "100.3.1.1",
                    "bgp_negotiated_keepalive_timers": {
                        "hold_time": 180,
                        "keepalive_interval": 60
                    },
                    "bgp_neighbor_session": {
                        "sessions": 1
                    },
                    "bgp_negotiated_capabilities": {
                        "route_refresh": "advertised and received(new)",
                        "four_octets_asn": "advertised and received",
                        "ipv4_unicast": "advertised and received",
                        "enhanced_refresh": "advertised and received",
                        "stateful_switchover": "NO for session 1"
                    },
                    "bgp_neighbor_counters": {
                        "messages": {
                            "sent": {
                                "opens": 1,
                                "notifications": 0,
                                "updates": 1,
                                "keepalives": 2,
                                "route_refresh": 0,
                                "total": 4
                            },
                            "received": {
                                "opens": 1,
                                "notifications": 0,
                                "updates": 1,
                                "keepalives": 2,
                                "route_refresh": 0,
                                "total": 4
                            },
                            "in_queue_depth": 0,
                            "out_queue_depth": 0
                        }
                    },
                    "bgp_session_transport": {
                        "min_time_between_advertisement_runs": 30,
                        "address_tracking_status": "enabled",
                        "rib_route_ip": "34.0.0.1",
                        "connection": {
                            "established": 1,
                            "dropped": 0,
                            "last_reset": "never"
                        },
                        "tcp_path_mtu_discovery": "enabled",
                        "graceful_restart": "disabled",
                        "sso": False,
                        "connection_state": "estab",
                        "io_status": 1,
                        "unread_input_bytes": 0,
                        "ecn_connection": "disabled",
                        "minimum_incoming_ttl": 0,
                        "outgoing_ttl": 1,
                        "transport": {
                            "local_host": "34.0.0.2",
                            "local_port": "34825",
                            "foreign_host": "34.0.0.1",
                            "foreign_port": "179",
                            "mss": 1460
                        },
                        "connection_tableid": 0,
                        "maximum_output_segment_queue_size": 50,
                        "enqueued_packets": {
                            "retransmit_packet": 0,
                            "input_packet": 0,
                            "mis_ordered_packet": 0
                        },
                        "iss": 714064615,
                        "snduna": 714064734,
                        "sndnxt": 714064734,
                        "irs": 1403370884,
                        "rcvnxt": 1403371003,
                        "sndwnd": 16266,
                        "snd_scale": 0,
                        "maxrcvwnd": 16384,
                        "rcvwnd": 16266,
                        "rcv_scale": 0,
                        "delrcvwnd": 118,
                        "srtt": 413,
                        "rtto": 3205,
                        "rtv": 2792,
                        "krtt": 0,
                        "min_rtt": 1,
                        "max_rtt": 1000,
                        "ack_hold": 120,
                        "uptime": 26070,
                        "sent_idletime": 25046,
                        "receive_idletime": 24925,
                        "status_flags": "active open",
                        "option_flags": "nagle, path mtu capable, SACK option permitted",
                        "ip_precedence_value": 6,
                        "datagram": {
                            "datagram_received": {
                                "value": 7,
                                "out_of_order": 0,
                                "with_data": 4,
                                "total_data": 118
                            },
                            "datagram_sent": {
                                "value": 8,
                                "retransmit": 0,
                                "fastretransmit": 0,
                                "partialack": 0,
                                "second_congestion": 0,
                                "with_data": 4,
                                "total_data": 118
                            }
                        },
                        "packet_fast_path": 0,
                        "packet_fast_processed": 0,
                        "packet_slow_path": 0,
                        "fast_lock_acquisition_failures": 0,
                        "lock_slow_path": 0,
                        "tcp_semaphore": "0x7CF66F80A318",
                        "tcp_semaphore_status": "FREE",
                        "tcp_ao_key_chain": {
                            "keychain_name": "test1",
                            "current_key": {
                                "id": 1,
                                "send_id": 1,
                                "recv_id": 1,
                                "include_tcp_options": True,
                                "accept_ao_mismatch": False
                            },
                            "next_key": {
                                "id": 1,
                                "send_id": 1,
                                "recv_id": 1,
                                "include_tcp_options": True,
                                "accept_ao_mismatch": False
                            }
                        }
                    },
                    "address_family": {
                        "ipv4 unicast": {
                            "bgp_table_version": 1,
                            "neighbor_version": "1/0",
                            "output_queue_size": 0,
                            "index": 1,
                            "advertise_bit": 0,
                            "update_group_member": 1,
                            "slow_peer_detection": False,
                            "slow_peer_split_update_group_dynamic": False,
                            "prefix_activity_counters": {
                                "sent": {
                                    "prefixes_current": 0,
                                    "prefixes_total": 0,
                                    "implicit_withdraw": 0,
                                    "explicit_withdraw": 0,
                                    "used_as_bestpath": "n/a",
                                    "used_as_multipath": "n/a",
                                    "used_as_secondary": "n/a"
                                },
                                "received": {
                                    "prefixes_current": 0,
                                    "prefixes_total": 0,
                                    "implicit_withdraw": 0,
                                    "explicit_withdraw": 0,
                                    "used_as_bestpath": 0,
                                    "used_as_multipath": 0,
                                    "used_as_secondary": 0
                                }
                            },
                            "local_policy_denied_prefixes_counters": {
                                "outbound": {
                                    "total": 0
                                },
                                "inbound": {
                                    "total": 0
                                }
                            },
                            "max_nlri": 0,
                            "min_nlri": 0,
                            "last_detected_dynamic_slow_peer": "never",
                            "dynamic_slow_peer_recovered": "never",
                            "refresh_epoch": 1,
                            "last_sent_refresh_start_of_rib": "never",
                            "last_sent_refresh_end_of_rib": "never",
                            "last_received_refresh_start_of_rib": "never",
                            "last_received_refresh_end_of_rib": "never",
                            "refresh_activity_counters": {
                                "sent": {
                                    "refresh_start_of_rib": 0,
                                    "refresh_end_of_rib": 0
                                },
                                "received": {
                                    "refresh_start_of_rib": 0,
                                    "refresh_end_of_rib": 0
                                }
                            },
                            "current_time": "0x616B9631"
                        }
                    },
                    "bgp_event_timer": {
                        "starts": {
                            "retrans": 4,
                            "timewait": 0,
                            "ackhold": 4,
                            "sendwnd": 0,
                            "keepalive": 0,
                            "giveup": 0,
                            "deadwait": 0,
                            "linger": 0,
                            "processq": 0
                        },
                        "wakeups": {
                            "retrans": 0,
                            "timewait": 0,
                            "ackhold": 1,
                            "sendwnd": 0,
                            "keepalive": 0,
                            "giveup": 0,
                            "deadwait": 0,
                            "linger": 0,
                            "processq": 0
                        },
                        "next": {
                            "retrans": "0x0",
                            "timewait": "0x0",
                            "ackhold": "0x0",
                            "sendwnd": "0x0",
                            "keepalive": "0x0",
                            "giveup": "0x0",
                            "deadwait": "0x0",
                            "linger": "0x0",
                            "processq": "0x0"
                        }
                    }
                }
            }
        }
    }
}