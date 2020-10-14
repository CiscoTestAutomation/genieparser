expected_output = {
    "interfaces": {
        "Port-channel1": {
            "name": "Port-channel1",
            "protocol": "pagp",
            "members": {
                "GigabitEthernet0/1": {
                    "interface": "GigabitEthernet0/1",
                    "counters": {
                        "information_in_pkts": 52,
                        "information_out_pkts": 60,
                        "pagp_errors": 0,
                        "flush_in_pkts": 0,
                        "flush_out_pkts": 0,
                    },
                },
                "GigabitEthernet0/2": {
                    "interface": "GigabitEthernet0/2",
                    "counters": {
                        "information_in_pkts": 52,
                        "information_out_pkts": 59,
                        "pagp_errors": 0,
                        "flush_in_pkts": 0,
                        "flush_out_pkts": 0,
                    },
                },
            },
        },
        "Port-channel2": {
            "name": "Port-channel2",
            "protocol": "pagp",
            "members": {
                "GigabitEthernet0/3": {
                    "interface": "GigabitEthernet0/3",
                    "counters": {
                        "information_in_pkts": 11,
                        "information_out_pkts": 21,
                        "pagp_errors": 0,
                        "flush_in_pkts": 0,
                        "flush_out_pkts": 0,
                    },
                },
                "GigabitEthernet1/0": {
                    "interface": "GigabitEthernet1/0",
                    "counters": {
                        "information_in_pkts": 11,
                        "information_out_pkts": 19,
                        "pagp_errors": 0,
                        "flush_in_pkts": 0,
                        "flush_out_pkts": 0,
                    },
                },
                "GigabitEthernet1/1": {
                    "interface": "GigabitEthernet1/1",
                    "counters": {
                        "information_in_pkts": 10,
                        "information_out_pkts": 19,
                        "pagp_errors": 0,
                        "flush_in_pkts": 0,
                        "flush_out_pkts": 0,
                    },
                },
            },
        },
    }
}
