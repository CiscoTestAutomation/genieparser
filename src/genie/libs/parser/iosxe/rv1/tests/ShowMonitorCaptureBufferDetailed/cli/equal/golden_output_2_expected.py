expected_output = {
    "framenumber": {
        1: {
            "interface_id": "0 (/tmp/epc_ws/wif_to_ts_pipe)",
            "interface_name": "/tmp/epc_ws/wif_to_ts_pipe",
            "encapsulation_type": "Ethernet (1)",
            "arrival_time": "Jul  4, 2024 23:33:59.661634000 IST",
            "time_shift_for_this_packet": "0.000000000 seconds",
            "epoch_time": "1720116239.661634000 seconds",
            "time_delta_from_previous_captured_frame": "0.000000000 seconds",
            "time_delta_from_previous_displayed_frame": "0.000000000 seconds",
            "time_since_reference_or_first_frame": "0.000000000 seconds",
            "frame_number": 1,
            "frame_length": "1490 bytes (11920 bits)",
            "capture_length": "1490 bytes (11920 bits)",
            "frame_is_marked": "False",
            "frame_is_ignored": "False",
            "protocols_in_frame": "eth:ethertype:ip:udp:cflow",
            "source_eth": "0c:d0:f8:87:ee:46 (0c:d0:f8:87:ee:46)",
            "destination_eth": "00:27:90:bf:c9:46 (00:27:90:bf:c9:46)",
            "destination": "00:27:90:bf:c9:46 (00:27:90:bf:c9:46)",
            "address": "0c:d0:f8:87:ee:46 (0c:d0:f8:87:ee:46)",
            "source": "0c:d0:f8:87:ee:46 (0c:d0:f8:87:ee:46)",
            "type": "IPv4 (0x0800)",
            "source_ipv4": "132.132.132.1",
            "destination_ipv4": "132.132.132.2",
            "dscp_value": 0,
            "total_length": 1476,
            "identification": "0x100f (4111)",
            "flags": "0x00",
            "fragment_offset": 0,
            "time_to_live": 254,
            "protocol": "UDP (17)",
            "header_checksum": "0x960d validation disabled",
            "header_checksum_status": "Unverified",
            "source_address": "132.132.132.1",
            "destination_address": "132.132.132.2",
            "udp_source_port": 54574,
            "udp_destination_port": 2055,
            "source_port": 54574,
            "destination_port": 2055,
            "length": 1456,
            "checksum": "0xfa25 unverified",
            "checksum_status": "Unverified",
            "stream_index": 0,
            "time_since_first_frame": "0.000000000 seconds",
            "time_since_previous_frame": "0.000000000 seconds",
            "cisco_netflow_ipfix": {
                "version": 9,
                "count": 47,
                "sys_uptime": "220138.000000000 seconds",
                "timestamp": "Jul  4, 2024 23:33:59.000000000 IST",
                "current_secs": 1720116239,
                "flow_sequence": 15,
                "source_id": 16777217,
                "1": {
                    "id": 0,
                    "flowset_id": "Data Template (V9) (0)",
                    "flowset_length": 44,
                    "template": {
                        "template_id": 257,
                        "field_count": 9,
                        "fields": {
                            "1": {
                                "type": "IP_SRC_ADDR (8)",
                                "length": 4
                            },
                            "2": {
                                "type": "IP_DST_ADDR (12)",
                                "length": 4
                            },
                            "3": {
                                "type": "L4_DST_PORT (11)",
                                "length": 2
                            },
                            "4": {
                                "type": "TCP_FLAGS (6)",
                                "length": 1
                            },
                            "5": {
                                "type": "BYTES (1)",
                                "length": 8
                            },
                            "6": {
                                "type": "PKTS (2)",
                                "length": 8
                            },
                            "7": {
                                "type": "IP_PROTOCOL_VERSION (60)",
                                "length": 1
                            },
                            "8": {
                                "type": "IP_TOS (5)",
                                "length": 1
                            },
                            "9": {
                                "type": "PROTOCOL (4)",
                                "length": 1
                            }
                        }
                    }
                },
                "2": {
                    "id": 257,
                    "flowset_id": "(Data) (257)",
                    "flowset_length": 1384,
                    "template_frame": 1,
                    "flows": {
                        "1": {
                            "src_addr": "6.6.6.133",
                            "dst_addr": "15.15.15.133",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 1482,
                            "packets": 3,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "2": {
                            "src_addr": "6.6.6.101",
                            "dst_addr": "15.15.15.101",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 988,
                            "packets": 2,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "3": {
                            "src_addr": "6.6.6.189",
                            "dst_addr": "15.15.15.189",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 988,
                            "packets": 2,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "4": {
                            "src_addr": "6.6.6.20",
                            "dst_addr": "15.15.15.20",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 1976,
                            "packets": 4,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "5": {
                            "src_addr": "6.6.6.59",
                            "dst_addr": "15.15.15.59",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 988,
                            "packets": 2,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "6": {
                            "src_addr": "6.6.6.227",
                            "dst_addr": "15.15.15.227",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 494,
                            "packets": 1,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "7": {
                            "src_addr": "6.6.6.216",
                            "dst_addr": "15.15.15.216",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 988,
                            "packets": 2,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "8": {
                            "src_addr": "6.6.6.207",
                            "dst_addr": "15.15.15.207",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 988,
                            "packets": 2,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "9": {
                            "src_addr": "6.6.6.224",
                            "dst_addr": "15.15.15.224",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 2964,
                            "packets": 6,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "10": {
                            "src_addr": "6.6.6.145",
                            "dst_addr": "15.15.15.145",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 988,
                            "packets": 2,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "11": {
                            "src_addr": "6.6.6.169",
                            "dst_addr": "15.15.15.169",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 2470,
                            "packets": 5,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "12": {
                            "src_addr": "6.6.6.113",
                            "dst_addr": "15.15.15.113",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 494,
                            "packets": 1,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "13": {
                            "src_addr": "6.6.6.41",
                            "dst_addr": "15.15.15.41",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 988,
                            "packets": 2,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "14": {
                            "src_addr": "6.6.6.17",
                            "dst_addr": "15.15.15.17",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 988,
                            "packets": 2,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "15": {
                            "src_addr": "6.6.6.222",
                            "dst_addr": "15.15.15.222",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 494,
                            "packets": 1,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "16": {
                            "src_addr": "6.6.6.96",
                            "dst_addr": "15.15.15.96",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 988,
                            "packets": 2,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "17": {
                            "src_addr": "6.6.6.184",
                            "dst_addr": "15.15.15.184",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 1482,
                            "packets": 3,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "18": {
                            "src_addr": "6.6.6.187",
                            "dst_addr": "15.15.15.187",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 988,
                            "packets": 2,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "19": {
                            "src_addr": "6.6.6.131",
                            "dst_addr": "15.15.15.131",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 988,
                            "packets": 2,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "20": {
                            "src_addr": "6.6.6.148",
                            "dst_addr": "15.15.15.148",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 1976,
                            "packets": 4,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "21": {
                            "src_addr": "6.6.6.229",
                            "dst_addr": "15.15.15.229",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 988,
                            "packets": 2,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "22": {
                            "src_addr": "6.6.6.242",
                            "dst_addr": "15.15.15.242",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 2470,
                            "packets": 5,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "23": {
                            "src_addr": "6.6.6.5",
                            "dst_addr": "15.15.15.5",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 494,
                            "packets": 1,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "24": {
                            "src_addr": "6.6.6.181",
                            "dst_addr": "15.15.15.181",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 988,
                            "packets": 2,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "25": {
                            "src_addr": "6.6.6.122",
                            "dst_addr": "15.15.15.122",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 494,
                            "packets": 1,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "26": {
                            "src_addr": "6.6.6.141",
                            "dst_addr": "15.15.15.141",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 988,
                            "packets": 2,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "27": {
                            "src_addr": "6.6.6.154",
                            "dst_addr": "15.15.15.154",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 1482,
                            "packets": 3,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "28": {
                            "src_addr": "6.6.6.85",
                            "dst_addr": "15.15.15.85",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 988,
                            "packets": 2,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "29": {
                            "src_addr": "6.6.6.51",
                            "dst_addr": "15.15.15.51",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 494,
                            "packets": 1,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "30": {
                            "src_addr": "6.6.6.211",
                            "dst_addr": "15.15.15.211",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 988,
                            "packets": 2,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "31": {
                            "src_addr": "6.6.6.196",
                            "dst_addr": "15.15.15.196",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 988,
                            "packets": 2,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "32": {
                            "src_addr": "6.6.6.39",
                            "dst_addr": "15.15.15.39",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 988,
                            "packets": 2,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "33": {
                            "src_addr": "6.6.6.48",
                            "dst_addr": "15.15.15.48",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 494,
                            "packets": 1,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "34": {
                            "src_addr": "6.6.6.232",
                            "dst_addr": "15.15.15.232",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 494,
                            "packets": 1,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "35": {
                            "src_addr": "6.6.6.8",
                            "dst_addr": "15.15.15.8",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 1482,
                            "packets": 3,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "36": {
                            "src_addr": "6.6.6.110",
                            "dst_addr": "15.15.15.110",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 1482,
                            "packets": 3,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "37": {
                            "src_addr": "6.6.6.161",
                            "dst_addr": "15.15.15.161",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 988,
                            "packets": 2,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "38": {
                            "src_addr": "6.6.6.65",
                            "dst_addr": "15.15.15.65",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 1482,
                            "packets": 3,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "39": {
                            "src_addr": "6.6.6.193",
                            "dst_addr": "15.15.15.193",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 988,
                            "packets": 2,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "40": {
                            "src_addr": "6.6.6.80",
                            "dst_addr": "15.15.15.80",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 988,
                            "packets": 2,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "41": {
                            "src_addr": "6.6.6.71",
                            "dst_addr": "15.15.15.71",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 988,
                            "packets": 2,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "42": {
                            "src_addr": "6.6.6.176",
                            "dst_addr": "15.15.15.176",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 988,
                            "packets": 2,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "43": {
                            "src_addr": "6.6.6.167",
                            "dst_addr": "15.15.15.167",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 494,
                            "packets": 1,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "44": {
                            "src_addr": "6.6.6.104",
                            "dst_addr": "15.15.15.104",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 2964,
                            "packets": 6,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "45": {
                            "src_addr": "6.6.6.127",
                            "dst_addr": "15.15.15.127",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 1482,
                            "packets": 3,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        },
                        "46": {
                            "src_addr": "6.6.6.83",
                            "dst_addr": "15.15.15.83",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 988,
                            "packets": 2,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        }
                    }
                }
            }
        }
    }
}
