expected_output = {
    "list_of_neighbors": [
        "10.4.11.2"
    ],
    "vrf": {
        "default": {
            "neighbor": {
                "10.4.11.2": {
                    "remote_as": "101.101",
                    "link": "external",
                    "shutdown": False,
                    "address_family": {
                        "ipv4 unicast": {
                            "session_state": "Established",
                            "up_time": "07:58:19",
                            "last_read": "00:00:07",
                            "last_write": "00:00:54",
                            "current_time": "0x1B8B90A"
                        }
                    },
                    "bgp_version": 4,
                    "router_id": "20.1.101.11",
                    "session_state": "Established",
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
                        "graceful_restart": "advertised and received",
                        "remote_restart_timer": 120,
                        "enhanced_refresh": "advertised and received",
                        "stateful_switchover": "NO for session 1"
                    },
                    "bgp_neighbor_counters": {
                        "messages": {
                            "sent": {
                                "opens": 1,
                                "notifications": 0,
                                "updates": 17,
                                "keepalives": 520,
                                "route_refresh": 0,
                                "total": 538
                            },
                            "received": {
                                "opens": 1,
                                "notifications": 0,
                                "updates": 25,
                                "keepalives": 520,
                                "route_refresh": 0,
                                "total": 548
                            },
                            "in_queue_depth": 0,
                            "out_queue_depth": 0
                        }
                    },
                    "bgp_session_transport": {
                        "min_time_between_advertisement_runs": 30,
                        "address_tracking_status": "enabled",
                        "rib_route_ip": "10.4.11.2",
                        "connection": {
                            "established": 1,
                            "dropped": 0,
                            "last_reset": "never"
                        },
                        "tcp_path_mtu_discovery": "enabled",
                        "graceful_restart": "enabled",
                        "gr_restart_time": 120,
                        "gr_stalepath_time": 360,
                        "sso": False,
                        "connection_state": "estab",
                        "io_status": 1,
                        "unread_input_bytes": 0,
                        "ecn_connection": "disabled",
                        "minimum_incoming_ttl": 0,
                        "outgoing_ttl": 1,
                        "transport": {
                            "local_host": "10.4.11.1",
                            "local_port": "179",
                            "foreign_host": "10.4.11.2",
                            "foreign_port": "33934",
                            "mss": 9060
                        },
                        "connection_tableid": 0,
                        "maximum_output_segment_queue_size": 50,
                        "enqueued_packets": {
                            "retransmit_packet": 0,
                            "input_packet": 0,
                            "mis_ordered_packet": 0
                        },
                        "iss": 2384224398,
                        "snduna": 2384235317,
                        "sndnxt": 2384235317,
                        "irs": 2754786057,
                        "rcvnxt": 2754797455,
                        "sndwnd": 13667,
                        "snd_scale": 0,
                        "maxrcvwnd": 16384,
                        "rcvwnd": 13192,
                        "rcv_scale": 0,
                        "delrcvwnd": 3192,
                        "srtt": 1000,
                        "rtto": 1003,
                        "rtv": 3,
                        "krtt": 0,
                        "min_rtt": 0,
                        "max_rtt": 1000,
                        "ack_hold": 200,
                        "uptime": 28699915,
                        "sent_idletime": 7314,
                        "receive_idletime": 7514,
                        "status_flags": "passive open, gen tcbs",
                        "option_flags": "nagle, path mtu capable",
                        "ip_precedence_value": 6,
                        "datagram": {
                            "datagram_received": {
                                "value": 1066,
                                "out_of_order": 0,
                                "with_data": 536,
                                "total_data": 11397
                            },
                            "datagram_sent": {
                                "value": 1070,
                                "retransmit": 0,
                                "fastretransmit": 0,
                                "partialack": 0,
                                "second_congestion": 0,
                                "with_data": 535,
                                "total_data": 10918
                            }
                        },
                        "packet_fast_path": 0,
                        "packet_fast_processed": 0,
                        "packet_slow_path": 0,
                        "fast_lock_acquisition_failures": 0,
                        "lock_slow_path": 0,
                        "tcp_semaphore": "0x7F844F05D020",
                        "tcp_semaphore_status": "FREE"
                    },
                    "bgp_event_timer": {
                        "starts": {
                            "retrans": 534,
                            "timewait": 0,
                            "ackhold": 534,
                            "sendwnd": 0,
                            "keepalive": 0,
                            "giveup": 0,
                            "pmtuager": 0,
                            "deadwait": 0,
                            "linger": 0,
                            "processq": 0
                        },
                        "wakeups": {
                            "retrans": 0,
                            "timewait": 0,
                            "ackhold": 530,
                            "sendwnd": 0,
                            "keepalive": 0,
                            "giveup": 0,
                            "pmtuager": 0,
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
                            "pmtuager": "0x0",
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