expected_output = {
    "framenumber": {
        7291: {
            "interface_id": "0 (/tmp/epc_ws/wif_to_ts_pipe)",
            "interface_name": "/tmp/epc_ws/wif_to_ts_pipe",
            "encapsulation_type": "Ethernet (1)",
            "arrival_time": "Jul  9, 2024 06:14:47.195934000 IST",
            "time_shift_for_this_packet": "0.000000000 seconds",
            "epoch_time": "1720485887.195934000 seconds",
            "time_delta_from_previous_captured_frame": "0.000602000 seconds",
            "time_delta_from_previous_displayed_frame": "0.000000000 seconds",
            "time_since_reference_or_first_frame": "75.186930000 seconds",
            "frame_number": 7291,
            "frame_length": "142 bytes (1136 bits)",
            "capture_length": "142 bytes (1136 bits)",
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
            "total_length": 128,
            "identification": "0x1018 (4120)",
            "flags": "0x00",
            "fragment_offset": 0,
            "time_to_live": 254,
            "protocol": "UDP (17)",
            "header_checksum": "0x9b48 validation disabled",
            "header_checksum_status": "Unverified",
            "source_address": "132.132.132.1",
            "destination_address": "132.132.132.2",
            "udp_source_port": 54960,
            "udp_destination_port": 2055,
            "source_port": 54960,
            "destination_port": 2055,
            "length": 108,
            "checksum": "0xbc78 unverified",
            "checksum_status": "Unverified",
            "stream_index": 0,
            "time_since_first_frame": "0.000000000 seconds",
            "time_since_previous_frame": "0.000000000 seconds",
            "cisco_netflow_ipfix": {
                "version": 9,
                "count": 2,
                "sys_uptime": "589785.000000000 seconds",
                "timestamp": "Jul  9, 2024 06:14:46.000000000 IST",
                "current_secs": 1720485886,
                "flow_sequence": 24,
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
                    "flowset_length": 36,
                    "template_frame": 7291,
                    "flows": {
                        "1": {
                            "src_addr": "6.6.6.8",
                            "dst_addr": "15.15.15.8",
                            "dst_port": 60,
                            "tcp_flags": "0x00",
                            "octets": 2470,
                            "packets": 5,
                            "ipversion": 4,
                            "ip_tos": "0x00",
                            "protocol": "TCP (6)"
                        }
                    },
                    "padding": 0000
                }
            }
        }
    }
}
