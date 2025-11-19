expected_output = {
    "parameter_maps": {
        "global": {
            "parameter_map_type": "Parameter-Map",
            "global_parameter_map": True,
            "alerts": "On",
            "audits": "Off",
            "drop_log": "On",
            "log_flow": "Off",
            "hsl_mode": "Disabled",
            "host": ":0",
            "port": 0,
            "template": "300 sec",
            "session_rate": {
                "high": 2147483647,
                "low": 2147483647,
                "time_duration": "60 sec"
            },
            "half_open": {
                "high": 2147483647,
                "low": 2147483647,
                "host": 4294967295,
                "host_block_time": 0
            },
            "inactivity_times": {
                "dns": 5,
                "icmp": 10,
                "tcp": 3600,
                "udp": 30
            },
            "inactivity_age_out_times": {
                "icmp": 10,
                "tcp": 3600,
                "udp": 30
            },
            "tcp_timeouts": {
                "syn_wait_time": 30,
                "fin_wait_time": 1
            },
            "tcp_ageout_timeouts": {
                "syn_wait_time": 30,
                "fin_wait_time": 1
            },
            "tcp_rst_pkt_control": {
                "half_open": "On",
                "half_close": "On",
                "idle": "On"
            },
            "udp_timeout": {
                "udp_half_open_time": 30000
            },
            "udp_ageout_timeout": {
                "udp_half_open_time": 30000
            },
            "max_sessions": "Unlimited",
            "number_of_simultaneous_packet_per_sessions": 0,
            "syn_cookie_and_resource_management": {
                "global_syn_flood_limit": 4294967295,
                "global_total_session": 4294967295,
            },
            "global_total_session_aggressive_aging": "Disabled",
            "global_alert": "Off",
            "global_max_incomplete": 4294967295,
            "global_max_incomplete_tcp": 4294967295,
            "global_max_incomplete_udp": 4294967295,
            "global_max_incomplete_icmp": 4294967295,
            "global_max_incomplete_aggressive_aging": "Disabled",
            "per_box_configuration": {
                "syn_flood_limit": 4294967295,
                "total_session_aggressive_aging": "Disabled",
                "max_incomplete": 4294967295,
                "max_incomplete_tcp": 4294967295,
                "max_incomplete_udp": 4294967295,
                "max_incomplete_icmp": 4294967295,
                "max_incomplete_aggressive_aging": "Disabled"
            }
        },
        "log_param": {
            "parameter_map_type": "Parameter-Map",
            "alerts": "On",
            "audits": "Off",
            "drop_log": "On",
            "log_flow": "Off",
            "zone_mismatch_drop": "Off",
            "multi_tenancy": "Off",
            "icmp_ureachable_allowed": "No",
            "session_rate": {
                "high": 2147483647,
                "low": 2147483647,
                "time_duration": "60 sec"
            },
            "half_open": {
                "high": 2147483647,
                "low": 2147483647,
                "host": 4294967295,
                "host_block_time": 0
            },
            "inactivity_times": {
                "dns": 5,
                "icmp": 10,
                "tcp": 3600,
                "udp": 30
            },
            "inactivity_age_out_times": {
                "icmp": 10,
                "tcp": 3600,
                "udp": 30
            },
            "tcp_timeouts": {
                "syn_wait_time": 30,
                "fin_wait_time": 1
            },
            "tcp_ageout_timeouts": {
                "syn_wait_time": 30,
                "fin_wait_time": 1
            },
            "tcp_rst_pkt_control": {
                "half_open": "On",
                "half_close": "On",
                "idle": "On"
            },
            "udp_timeout": {
                "udp_half_open_time": 30000
            },
            "udp_ageout_timeout": {
                "udp_half_open_time": 30000
            },
            "max_sessions": "Unlimited",
            "number_of_simultaneous_packet_per_sessions": 0,
            "syn_cookie_and_resource_management": {
                "global_syn_flood_limit": 4294967295,
                "global_total_session": 4294967295,
            },
            "application_protocol_control": {
                "protocol_1": {
                    "protocol": "dns",
                    "status": "on"
                },
                "protocol_2": {
                    "protocol": "ftp",
                    "status": "on"
                },
                "protocol_3": {
                    "protocol": "gtp",
                    "status": "on"
                },
                "protocol_4": {
                    "protocol": "H323",
                    "status": "on"
                },
                "protocol_5": {
                    "protocol": "http",
                    "status": "on"
                },
                "protocol_6": {
                    "protocol": "imap",
                    "status": "on"
                },
                "protocol_7": {
                    "protocol": "msrpc",
                    "status": "on"
                },
                "protocol_8": {
                    "protocol": "netbios",
                    "status": "on"
                },
                "protocol_9": {
                    "protocol": "pop3",
                    "status": "on"
                },
                "protocol_10": {
                    "protocol": "exec",
                    "status": "on"
                },
                "protocol_11": {
                    "protocol": "rlogin",
                    "status": "on"
                },
                "protocol_12": {
                    "protocol": "shell",
                    "status": "on"
                },
                "protocol_13": {
                    "protocol": "rtsp",
                    "status": "on"
                },
                "protocol_14": {
                    "protocol": "sip",
                    "status": "on"
                },
                "protocol_15": {
                    "protocol": "skinny",
                    "status": "on"
                },
                "protocol_16": {
                    "protocol": "smtp",
                    "status": "on"
                },
                "protocol_17": {
                    "protocol": "sunrpc",
                    "status": "on"
                },
                "protocol_18": {
                    "protocol": "tftp",
                    "status": "on"
                }
            }
        },
        "vrf-default": {
            "parameter_map_type": "VRF-Parameter-Map",
            "vrf_pmap_syn_flood_limit": 4294967295,
            "vrf_pmap_total_session": 4294967295,
            "vrf_pmap_total_session_aggressive_aging": "Disabled",
            "vrf_pmap_alert": "Off",
            "vrf_pmap_max_incomplete": 4294967295,
            "vrf_pmap_max_incomplete_tcp": 4294967295,
            "vrf_pmap_max_incomplete_udp": 4294967295,
            "vrf_pmap_max_incomplete_icmp": 4294967295,
            "vrf_pmap_max_incomplete_aggressive_aging": "Disabled"
        },
        "pmap_sessions": {
            "parameter_map_type": "Parameter-Map",
            "alerts": "On",
            "audits": "Off",
            "drop_log": "Off",
            "log_flow": "Off",
            "zone_mismatch_drop": "Off",
            "multi_tenancy": "Off",
            "icmp_ureachable_allowed": "No",
            "session_rate": {
                "high": 2147483647,
                "low": 2147483647,
                "time_duration": "60 sec"
            },
            "half_open": {
                "high": 2147483647,
                "low": 2147483647,
                "host": 4294967295,
                "host_block_time": 0
            },
            "inactivity_times": {
                "dns": 5,
                "icmp": 10,
                "tcp": 3600,
                "udp": 30
            },
            "inactivity_age_out_times": {
                "icmp": 10,
                "tcp": 3600,
                "udp": 30
            },
            "tcp_timeouts": {
                "syn_wait_time": 30,
                "fin_wait_time": 1
            },
            "tcp_ageout_timeouts": {
                "syn_wait_time": 30,
                "fin_wait_time": 1
            },
            "tcp_rst_pkt_control": {
                "half_open": "On",
                "half_close": "On",
                "idle": "On"
            },
            "udp_timeout": {
                "udp_half_open_time": 30000
            },
            "udp_ageout_timeout": {
                "udp_half_open_time": 30000
            },
            "max_sessions": "100",
            "number_of_simultaneous_packet_per_sessions": 0,
            "syn_cookie_and_resource_management": {
                "global_syn_flood_limit": 4294967295,
                "global_total_session": 4294967295,
            },
            "application_protocol_control": {
                "protocol_1": {
                    "protocol": "dns",
                    "status": "on"
                },
                "protocol_2": {
                    "protocol": "ftp",
                    "status": "on"
                },
                "protocol_3": {
                    "protocol": "gtp",
                    "status": "on"
                },
                "protocol_4": {
                    "protocol": "H323",
                    "status": "on"
                },
                "protocol_5": {
                    "protocol": "http",
                    "status": "on"
                },
                "protocol_6": {
                    "protocol": "imap",
                    "status": "on"
                },
                "protocol_7": {
                    "protocol": "msrpc",
                    "status": "on"
                },
                "protocol_8": {
                    "protocol": "netbios",
                    "status": "on"
                },
                "protocol_9": {
                    "protocol": "pop3",
                    "status": "on"
                },
                "protocol_10": {
                    "protocol": "exec",
                    "status": "on"
                },
                "protocol_11": {
                    "protocol": "rlogin",
                    "status": "on"
                },
                "protocol_12": {
                    "protocol": "shell",
                    "status": "on"
                },
                "protocol_13": {
                    "protocol": "rtsp",
                    "status": "on"
                },
                "protocol_14": {
                    "protocol": "sip",
                    "status": "on"
                },
                "protocol_15": {
                    "protocol": "skinny",
                    "status": "on"
                },
                "protocol_16": {
                    "protocol": "smtp",
                    "status": "on"
                },
                "protocol_17": {
                    "protocol": "sunrpc",
                    "status": "on"
                },
                "protocol_18": {
                    "protocol": "tftp",
                    "status": "on"
                }
            }
        }
    }
}
