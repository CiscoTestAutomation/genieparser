expected_output = {
    "cluster_ip": "cluster1",
    "encryption": "Enabled",
    "failover": "n/a",
    "peers": {
        1: {
            "load_balancing_version": 4,
            "model": "ASA-VASA",
            "pri": 5,
            "public_ip": "10.246.0.1*",
            "role": "Master",
        },
        2: {
            "load_balancing_version": 4,
            "model": "ASA-VASA",
            "pri": 5,
            "public_ip": "10.246.0.2",
            "role": "Backup",
        },
    },
    "peers_count": 1,
    "role": "Master",
    "status": "Enabled",
    "total_license_load": {
        1: {
            "anyconnect_premium_essentials": {"limit": 250, "load": 0, "used": 0},
            "other_vpn": {"limit": 250, "load": 1, "used": 2},
            "public_ip": "10.246.0.1*",
        },
        2: {
            "anyconnect_premium_essentials": {"limit": 0, "load": 0, "used": 0},
            "other_vpn": {"limit": 0, "load": 0, "used": 0},
            "public_ip": "10.246.0.2",
        },
    },
}
