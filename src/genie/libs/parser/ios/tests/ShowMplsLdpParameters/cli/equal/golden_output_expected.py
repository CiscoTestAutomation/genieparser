expected_output = {
    "ldp_featureset_manager": {
        "State Initialized": {
            "ldp_features": [
                "Auto-Configuration",
                "Basic",
                "ICPM",
                "IP-over-MPLS",
                "IGP-Sync",
                "LLAF",
                "TCP-MD5-Rollover",
                "TDP",
                "NSR",
            ]
        }
    },
    "ldp_backoff": {"initial": 15, "maximum": 120},
    "ldp_loop_detection": "off",
    "ldp_nsr": "disabled",
    "ldp_for_targeted_sessions": True,
    "version": 1,
    "session_hold_time": 180,
    "keep_alive_interval": 60,
    "discovery_targeted_hello": {"holdtime": 90, "interval": 10},
    "discovery_hello": {"holdtime": 15, "interval": 5},
    "downstream_on_demand_max_hop_count": 255,
}
