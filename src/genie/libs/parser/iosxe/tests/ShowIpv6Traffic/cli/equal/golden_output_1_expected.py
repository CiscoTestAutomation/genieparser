expected_output = {
    "ipv6_statistics": {
        "received": {
            "total": 2,
            "total_bytes": 112,
            "local_destination": 2,
            "source_routed": 0,
            "truncated": 0,
            "no_route": 0,
            "format_errors": 0,
            "hop_count_exceeded": 0,
            "bad_header": 0,
            "unknown_option": 0,
            "bad_source": 0,
            "unknown_protocol": 0,
            "not_a_router": 0,
            "fragments": 0,
            "total_reassembled": 0,
            "reassembly_timeouts": 0,
            "reassembly_failures": 0
        },
        "sent": {
            "total": 161,
            "total_bytes": 18670,
            "generated": 162,
            "forwarded": 161,
            "fragmented": 0,
            "fragments": 0,
            "failed": 0,
            "encapsulation_failed": 0,
            "no_route": 0,
            "too_big": 0,
            "rpf_drops": 0,
            "rpf_suppressed_drops": 0
        },
        "multicast": {
            "received": 2,
            "received_bytes": 112,
            "sent": 0,
            "sent_bytes": 0
        }
    },
    "icmp_statistics": {
        "received": {
            "input": 2,
            "checksum_errors": 0,
            "too_short": 0,
            "unknown_info_type": 0,
            "unknown_error_type": 0,
            "unreachable": {
                "routing": 0,
                "admin": 0,
                "neighbor": 0,
                "address": 0,
                "port": 0,
                "sa_policy": 0,
                "reject_route": 0
            },
            "parameter": {
                "error": 0,
                "header": 0,
                "option": 0
            },
            "hopcount_expired": 0,
            "reassembly_timeout": 0,
            "too_big": 0,
            "bad_embedded_ipv6": 0,
            "echo_request": 0,
            "echo_reply": 0,
            "group_query": 0,
            "group_report": 0,
            "group_reduce": 0,
            "router_solicit": 2,
            "router_advert": 0,
            "redirects": 0,
            "neighbor_solicit": 0,
            "neighbor_advert": 0
        },
        "sent": {
            "output": 162,
            "rate_limited": 0,
            "unreachable": {
                "routing": 0,
                "admin": 0,
                "neighbor": 0,
                "address": 0,
                "port": 0,
                "sa_policy": 0,
                "reject_route": 0
            },
            "parameter": {
                "error": 0,
                "header": 0,
                "option": 0
            },
            "hopcount_expired": 0,
            "reassembly_timeout": 0,
            "too_big": 0,
            "echo_request": 0,
            "echo_reply": 0,
            "group_query": 0,
            "group_report": 0,
            "group_reduce": 0,
            "router_solicit": 0,
            "router_advert": 162,
            "redirects": 0,
            "neighbor_solicit": 0,
            "neighbor_advert": 0
        }
    },
    "udp_statistics": {
        "received": {
            "input": 0,
            "checksum_errors": 0,
            "length_errors": 0,
            "no_port": 0,
            "dropped": 0
        },
        "sent": {
            "output": 0
        }
    },
    "tcp_statistics": {
        "received": {
            "input": 0,
            "checksum_errors": 0
        },
        "sent": {
            "output": 0,
            "retransmitted": 0
        }
    }
}