expected_output = {
    "backbone_fast": False,
    "bpdu_filter": False,
    "bpdu_guard": False,
    "bridge_assurance": True,
    "configured_pathcost": {"method": "short", "operational_value": "long"},
    "etherchannel_misconfig_guard": True,
    "extended_system_id": True,
    "loop_guard": False,
    "mode": {
        "mst": {
            "MST0": {
                "blocking": 3,
                "forwarding": 0,
                "learning": 0,
                "listening": 0,
                "stp_active": 3,
            }
        }
    },
    "portfast_default": False,
    "pvst_simulation": True,
    "root_bridge_for": "MST0",
    "total_statistics": {
        "blockings": 3,
        "forwardings": 0,
        "learnings": 0,
        "listenings": 0,
        "num_of_msts": 1,
        "stp_actives": 3,
    },
    "uplink_fast": False,
}
