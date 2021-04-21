expected_output = {
    "session": {
        "1": {
            "destination_erspan_id": "1",
            "destination_ip_address": "172.18.197.254",
            "mtu": 1464,
            "origin_ip_address": "172.18.197.254",
            "source_ports": {"tx_only": "Gi0/1/4"},
            "status": "Admin Enabled",
            "type": "ERSPAN Source Session",
        },
        "2": {
            "destination_ports": "Gi0/1/6",
            "mtu": 1464,
            "source_erspan_id": "1",
            "source_ip_address": "172.18.197.254",
            "status": "Admin Enabled",
            "type": "ERSPAN Destination Session",
        },
    }
}
