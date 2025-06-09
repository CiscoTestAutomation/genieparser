expected_output = {
    "session": {
        "10": {
            "type": "ERSPAN Source Session",
            "status": "Admin Enabled",
            "source_ports": {
                "both": "Gi0/0/1"
            },
            "destination_ip_address": "10.1.1.1",
            "mtu": 1464,
            "destination_erspan_id": "10",
            "origin_ip_address": "100.1.1.1"
        },
        "20": {
            "type": "ERSPAN Destination Session",
            "status": "Admin Enabled",
            "destination_ports": "Gi0/1/3",
            "source_ip_address": "10.1.1.1",
            "source_erspan_id": "10"
        }
    }
}
