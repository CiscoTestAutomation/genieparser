expected_output = {
    "etherchannel_misconfig_guard": True,
    "mode": {
        "pvst": {
            "VLAN0101": {
                "stp_active": 1,
                "forwarding": 0,
                "blocking": 0,
                "listening": 1,
                "learning": 0,
            },
            "VLAN0406": {
                "stp_active": 1,
                "forwarding": 0,
                "blocking": 0,
                "listening": 1,
                "learning": 0,
            },
            "VLAN0405": {
                "stp_active": 1,
                "forwarding": 0,
                "blocking": 0,
                "listening": 1,
                "learning": 0,
            },
            "VLAN0407": {
                "stp_active": 1,
                "forwarding": 0,
                "blocking": 0,
                "listening": 1,
                "learning": 0,
            },
            "VLAN0100": {
                "stp_active": 1,
                "forwarding": 0,
                "blocking": 0,
                "listening": 1,
                "learning": 0,
            },
        }
    },
    "portfast_default": False,
    "backbone_fast": False,
    "extended_system_id": True,
    "bpdu_filter": False,
    "bpdu_guard": False,
    "total_statistics": {
        "stp_actives": 5,
        "forwardings": 0,
        "blockings": 0,
        "num_of_vlans": 5,
        "learnings": 0,
        "listenings": 5,
    },
    "loop_guard": False,
    "uplink_fast": False,
    "root_bridge_for": "VLAN0100-VLAN0101, VLAN0405-VLAN0407",
    "configured_pathcost": {"method": "short"},
}
