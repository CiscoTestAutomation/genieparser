expected_output = {
    "clns": {
        "last_clear": "never",
        "output": 168,
        "input": 4021,
        "local": 0,
        "forward": 0,
        "dropped_protocol": 0,
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
                "ish": {"rcvd": 0, "sent": 168},
                "rd": {"rcvd": 0, "sent": 0},
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
        "VRF1": {
            "IS-IS": {
                "last_clear": "never",
                "hello": {
                    "level-1": {"rcvd": 533, "sent": 497},
                    "level-2": {"rcvd": 611, "sent": 843},
                    "ptp": {"rcvd": 0, "sent": 0},
                },
                "lsp_sourced": {
                    "level-1": {"new": 3, "refresh": 4},
                    "level-2": {"new": 4, "refresh": 5},
                },
                "lsp_flooded": {
                    "level-1": {"sent": 0, "rcvd": 0},
                    "level-2": {"sent": 5, "rcvd": 5},
                },
                "lsp_retransmissions": 0,
                "csnp": {
                    "level-1": {"rcvd": 0, "sent": 0},
                    "level-2": {"rcvd": 0, "sent": 170},
                },
                "psnp": {
                    "level-1": {"rcvd": 0, "sent": 0},
                    "level-2": {"rcvd": 0, "sent": 0},
                },
                "dr_election": {"level-1": 1, "level-2": 2},
                "spf_calculation": {"level-1": 14, "level-2": 17},
                "partial_route_calculation": {"level-1": 0, "level-2": 1},
                "lsp_checksum_errors_received": 0,
                "update_process_queue_depth": "0/200",
                "update_process_packets_dropped": 0,
            }
        }
    },
}
