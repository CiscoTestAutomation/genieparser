expected_output = {
    "backbone_fast": False,
    "bpdu_filter": False,
    "bpdu_guard": False,
    "bridge_assurance": True,
    "pvst_simulation": True,
    "pvst_simulation_status": "inactive",
    "configured_pathcost": {"method": "short"},
    "etherchannel_misconfig_guard": True,
    "extended_system_id": True,
    "loop_guard": False,
    "mode": {
        "rapid_pvst": {
            "VLAN0001": {
                "blocking": 0,
                "forwarding": 1,
                "learning": 0,
                "listening": 0,
                "stp_active": 1,
            }
        }
    },
    "portfast_default": False,
    "root_bridge_for": "VLAN0001",
    "total_statistics": {
        "blockings": 0,
        "forwardings": 1,
        "learnings": 0,
        "listenings": 0,
        "num_of_vlans": 1,
        "stp_actives": 1,
    },
    "uplink_fast": False,
}
