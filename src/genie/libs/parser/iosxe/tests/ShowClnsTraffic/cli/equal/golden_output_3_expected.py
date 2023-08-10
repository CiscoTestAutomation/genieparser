expected_output = {
    "clns": {
        "last_clear": "never",
        "input": 934369,
        "output": 26509,
        "dropped_protocol": 0,
        "local": 0,
        "forward": 0,
        "discards": {
            "hdr_syntax": 0,
            "checksum": 0,
            "lifetime": 0,
            "output_cngstn": 0,
            "no_route": 0,
            "discard_route": 0,
            "dst_unreachable": 0,
            "encaps_failed": 0,
            "nlp_unknown": 0,
            "not_an_is": 0,
        },
        "options": {"packets": 0, "total": 0, "bad": 0, "gqos": 0, "cngstn_exprncd": 0},
        "segments": {"segmented": 0, "failed": 0},
        "broadcasts": {"sent": 0, "rcvd": 0},
    },
    "echos": {
        "rcvd": {"requests": 0, "replied": 0},
        "sent": {"requests": 0, "replied": 0},
    },
    "packet_counters": {
        "level": {
            "level-all": {
                "esh": {"rcvd": 0, "sent": 0},
                "ish": {"rcvd": 0, "sent": 26509},
                "rd": {"sent": 0, "rcvd": 0},
                "qcf": {"rcvd": 0, "sent": 0},
            }
        }
    },
    "tunneling": {
        "ip": {"rcvd": 0, "sent": 0, "rcvd_dropped": 0},
        "ipv6": {"rcvd": 0, "sent": 0, "rcvd_dropped": 0},
    },
    "iso-igrp": {
        "query": {"rcvd": 0, "sent": 0},
        "update": {"rcvd": 0, "sent": 0},
        "router_hello": {"rcvd": 0, "sent": 0},
        "syntax_errors": 0,
    },
    "tag": {
        "null": {
            "IS-IS": {
                "last_clear": "never",
                "hello": {
                    "level-1": {"sent": 1093921, "rcvd": 758008},
                    "ptp": {"sent": 0, "rcvd": 0},
                },
                "lsp_sourced": {"level-1": {"new": 15, "refresh": 5195}},
                "lsp_flooded": {"level-1": {"sent": 19736, "rcvd": 26484}},
                "lsp_retransmissions": 0,
                "csnp": {"level-1": {"sent": 308588, "rcvd": 149877}},
                "psnp": {"level-1": {"sent": 0, "rcvd": 0}},
                "dr_election": {"level-1": 9, "level-2": 7},
                "spf_calculation": {"level-1": 1565, "level-2": 1324},
                "partial_route_calculation": {"level-1": 4, "level-2": 6},
                "lsp_checksum_errors_received": 0,
                "update_process_queue_depth": "0/200",
                "update_process_packets_dropped": 0,
            }
        },
        "default": {
            "IS-IS": {
                "last_clear": "never",
                "hello": {
                    "level-1": {"sent": 0, "rcvd": 0},
                    "level-2": {"sent": 0, "rcvd": 0},
                    "ptp": {"sent": 0, "rcvd": 0},
                },
                "lsp_sourced": {
                    "level-1": {"new": 0, "refresh": 0},
                    "level-2": {"new": 0, "refresh": 0},
                },
                "lsp_flooded": {
                    "level-1": {"sent": 0, "rcvd": 0},
                    "level-2": {"sent": 0, "rcvd": 0},
                },
                "lsp_retransmissions": 0,
                "csnp": {
                    "level-1": {"sent": 0, "rcvd": 0},
                    "level-2": {"sent": 0, "rcvd": 0},
                },
                "psnp": {
                    "level-1": {"sent": 0, "rcvd": 0},
                    "level-2": {"sent": 0, "rcvd": 0},
                },
                "dr_election": {"level-1": 0, "level-2": 0},
                "spf_calculation": {"level-1": 0, "level-2": 0},
                "partial_route_calculation": {"level-1": 0, "level-2": 0},
                "lsp_checksum_errors_received": 0,
                "update_process_queue_depth": "0/200",
                "update_process_packets_dropped": 0,
            }
        },
    },
}
