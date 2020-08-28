expected_output = {
    "bpdu_filter": False,
    "extended_system_id": True,
    "etherchannel_misconfig_guard": False,
    "total_statistics": {
        "forwardings": 10,
        "listenings": 0,
        "num_of_msts": 2,
        "stp_actives": 16,
        "learnings": 0,
        "blockings": 6,
    },
    "root_bridge_for": "MST0, MST100",
    "bpdu_guard": False,
    "mode": {
        "mst": {
            "MST100": {
                "blocking": 3,
                "forwarding": 1,
                "listening": 0,
                "stp_active": 4,
                "learning": 0,
            },
            "MST0": {
                "blocking": 3,
                "forwarding": 9,
                "listening": 0,
                "stp_active": 12,
                "learning": 0,
            },
        }
    },
    "uplink_fast": False,
    "backbone_fast": False,
    "portfast_default": False,
    "loop_guard": False,
    "configured_pathcost": {"method": "short", "operational_value": "long"},
}
