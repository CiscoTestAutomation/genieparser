expected_output = {
    "session": {
        "10": {
            "type": "Local Session",
            "source_ports": {},
            "destination_ports": "Gi4/0/2",
        },
        "20": {
            "type": "Local Session",
            "source_ports": {},
            "destination_ports": "Gi3/0/28",
        },
        "30": {
            "type": "Local Session",
            "source_ports": {},
            "destination_ports": "Gi1/0/1",
        },
        "40": {
            "type": "Remote Source Session",
            "source_ports": {},
            "dest_rspan_vlan": 300,
        },
        "52": {
            "type": "ERSPAN Source Session",
            "status": "Admin Enabled",
            "source_ports": {},
            "destination_ip_address": "1.1.1.20",
            "mtu": 1500,
            "destination_erspan_id": "12",
            "origin_ip_address": "1.1.1.2",
        },
    }
}

