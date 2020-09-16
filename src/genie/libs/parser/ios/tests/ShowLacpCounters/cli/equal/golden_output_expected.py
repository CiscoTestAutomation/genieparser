expected_output = {
    "interfaces": {
        "Port-channel1": {
            "name": "Port-channel1",
            "protocol": "lacp",
            "members": {
                "FastEthernet4/1": {
                    "interface": "FastEthernet4/1",
                    "counters": {
                        "lacp_in_pkts": 15,
                        "lacp_out_pkts": 8,
                        "marker_in_pkts": 0,
                        "marker_out_pkts": 0,
                        "lacp_pkts": 3,
                        "lacp_errors": 0,
                    },
                },
                "FastEthernet4/2": {
                    "interface": "FastEthernet4/2",
                    "counters": {
                        "lacp_in_pkts": 18,
                        "lacp_out_pkts": 14,
                        "marker_in_pkts": 0,
                        "marker_out_pkts": 0,
                        "lacp_pkts": 3,
                        "lacp_errors": 0,
                    },
                },
                "FastEthernet4/3": {
                    "interface": "FastEthernet4/3",
                    "counters": {
                        "lacp_in_pkts": 18,
                        "lacp_out_pkts": 14,
                        "marker_in_pkts": 0,
                        "marker_out_pkts": 0,
                        "lacp_pkts": 0,
                    },
                },
                "FastEthernet4/4": {
                    "interface": "FastEthernet4/4",
                    "counters": {
                        "lacp_in_pkts": 18,
                        "lacp_out_pkts": 13,
                        "marker_in_pkts": 0,
                        "marker_out_pkts": 0,
                        "lacp_pkts": 0,
                    },
                },
            },
        }
    }
}
