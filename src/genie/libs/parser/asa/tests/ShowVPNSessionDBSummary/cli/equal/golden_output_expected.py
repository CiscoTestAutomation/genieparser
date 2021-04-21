expected_output = {
    "summary": {
        "VPN Session": {
            "device_load": 0.01,
            "device_total_vpn_capacity": 250,
            "session": {
                "IKEv1 IPsec/L2TP IPsec": {
                    "active": 2,
                    "cumulative": 2,
                    "peak_concurrent": 2,
                },
                "Load Balancing(Encryption)": {
                    "active": 0,
                    "cumulative": 6,
                    "peak_concurrent": 1,
                },
            },
            "total_active_and_inactive": 2,
            "total_cumulative": 8,
        }
    }
}
