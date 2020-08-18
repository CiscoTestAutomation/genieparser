expected_output = {
    "summary": {
        "Tunnels": {
            "session": {
                "Clientless": {"active": 0, "cumulative": 1, "peak_concurrent": 1}
            },
            "totals": {"active": 0, "cumulative": 1},
        },
        "VPN Session": {
            "device_load": 0.0,
            "device_total_vpn_capacity": 250,
            "session": {
                "Clientless VPN": {
                    "active": 0,
                    "cumulative": 1,
                    "peak_concurrent": 1,
                    "type": {
                        "Browser": {"active": 0, "cumulative": 1, "peak_concurrent": 1}
                    },
                }
            },
            "total_active_and_inactive": 0,
            "total_cumulative": 1,
        },
    }
}
