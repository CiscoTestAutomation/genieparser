expected_output = {
    "source": "*",
    "group": "*",
    "reference_count": 1,
    "epoch": 0,
    "source_port": "Null",
    "flags": "Age Out",
    "adjacency": {"output_list_id": 45, "ports": 1},
    "receiver_ports": {
        "[SMC]20121:239.2.1.121": {
            "is_pathlist": True,
            "description": {
                "path_list_id": 85,
                "path_list_count": 1,
                "path_list_type": "VXLAN_REP",
                "path_list_description": {
                    "type": "SMC",
                    "port": 20121,
                    "address": "239.2.1.121",
                },
            },
            "epoch": 0,
            "producer": "EVPN",
        }
    },
}
