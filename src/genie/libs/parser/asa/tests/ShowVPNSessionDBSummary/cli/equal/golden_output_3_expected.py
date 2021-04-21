expected_output = {
    "summary": {
        "VPN Session": {
            "session": {
                "AnyConnect Client": {
                    "active": 1672,
                    "cumulative": 140011,
                    "inactive": 355,
                    "peak_concurrent": 2219,
                    "type": {
                        "SSL/TLS/DTLS": {
                            "active": 1672,
                            "cumulative": 140011,
                            "inactive": 355,
                            "peak_concurrent": 2219,
                        }
                    },
                },
                "Clientless VPN": {
                    "active": 2,
                    "type": {
                        "Browser": {
                            "active": 2,
                            "cumulative": 125,
                            "peak_concurrent": 6,
                        }
                    },
                    "cumulative": 125,
                    "peak_concurrent": 6,
                },
            },
            "device_load": 0.41,
            "device_total_vpn_capacity": 5000,
            "total_active_and_inactive": 2029,
            "total_cumulative": 1140136,
        }
    }
}
