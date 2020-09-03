expected_output = {
    "summary": {
        "Tunnels": {
            "session": {
                "AnyConnect-Parent": {
                    "active": 127,
                    "cumulative": 432,
                    "peak_concurrent": 205,
                },
                "Clientless": {"active": 0, "cumulative": 1, "peak_concurrent": 1},
                "DTLS-Tunnel": {
                    "active": 124,
                    "cumulative": 1508,
                    "peak_concurrent": 202,
                },
                "SSL-Tunnel": {
                    "active": 125,
                    "cumulative": 1577,
                    "peak_concurrent": 204,
                },
            },
            "totals": {"active": 376, "cumulative": 3518},
        },
        "VPN Session": {
            "session": {
                "AnyConnect Client": {
                    "active": 127,
                    "cumulative": 432,
                    "inactive": 0,
                    "peak_concurrent": 205,
                    "type": {
                        "SSL/TLS/DTLS": {
                            "active": 127,
                            "cumulative": 432,
                            "inactive": 0,
                            "peak_concurrent": 205,
                        },
                        "IKEv2 IPsec": {
                            "active": 8,
                            "cumulative": 17,
                            "inactive": 0,
                            "peak_concurrent": 8,
                        },
                    },
                },
                "Clientless VPN": {
                    "active": 0,
                    "type": {
                        "Browser": {"active": 0, "cumulative": 1, "peak_concurrent": 1}
                    },
                    "cumulative": 1,
                    "peak_concurrent": 1,
                },
                "Site-to-Site VPN": {
                    "active": 29,
                    "cumulative": 59,
                    "type": {
                        "IKEv2 IPsec": {
                            "active": 29,
                            "cumulative": 59,
                            "peak_concurrent": 29,
                        }
                    },
                    "peak_concurrent": 29,
                },
            },
            "device_load": 0.0,
            "device_total_vpn_capacity": 5000,
            "total_active_and_inactive": 127,
            "total_cumulative": 432,
        },
    }
}
