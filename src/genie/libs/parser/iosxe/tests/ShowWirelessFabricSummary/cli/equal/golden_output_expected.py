expected_output = {
    "fabric_status": "Enabled",
    "control_plane": {
        "ip_address": {
            "10.10.90.16": {
                "name": "default-control-plane",
                "key": "099fff",
                "status": "Up"
            },
            "10.10.90.22": {
                "name": "default-control-plane",
                "key": "099fff",
                "status": "Up"
            }
        }
    },
    "fabric_vnid_mapping": {
        "l2_vnid": {
            8192: {
                "name": "Data",
                "l3_vnid": 0,
                "control_plane_name": "Data"
            },
            8189: {
                "name": "Guest",
                "l3_vnid": 0,
                "control_plane_name": "Guest"
            },
            8191: {
                "name": "Voice",
                "l3_vnid": 0,
                "control_plane_name": "Voice"
            },
            8188: {
                "name": "Fabric_B_INFRA_VN",
                "l3_vnid": 4097,
                "ip_address": "10.10.40.0",
                "subnet": "255.255.254.0",
                "control_plane_name": "default-control-plane"
            },
            8190: {
                "name": "Physical_Security",
                "l3_vnid": 0,
                "control_plane_name": "Physical_Security"
            }
        }
    }
}
