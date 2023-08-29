expected_output = {
    "interfaces": {
        "TenGigabitEthernet1/0/2.154": {
            "mode": "client",
            "prefix_state": "OPEN",
            "address_state": "OPEN",
            "known_servers": {
                "FE80::20C:29FF:FE22:1DA5": {
                    "duid": "00030001001EE59BE700",
                    "preference": 0,
                    "IA PD": {
                        "iaid": "0x00200001",
                        "t1": 302400,
                        "t2": 483840,
                        "prefix": "8882:0:0:100::/56",
                        "preferred_lifetime": 604800,
                        "valid_lifetime": 2592000,
                    },
                    "IA NA": {
                        "iaid": "0x00200001",
                        "t1": 43200,
                        "t2": 69120,
                        "address": "7772::41EF:B5D6:B50:38B7/128",
                        "preferred_lifetime": 86400,
                        "valid_lifetime": 172800,
                    },
                    "dns_server": "11::11",
                    "domain_name": "cisco.com",
                    "information_refresh_time": 0,
                },
                "FE80::20C:29FF:FEF7:D6A4": {
                    "duid": "00030001001EBD9A6800",
                    "preference": 0,
                    "IA PD": {
                        "iaid": "0x00200001",
                        "t1": 302400,
                        "t2": 483840,
                        "prefix": "8881:0:0:100::/56",
                        "preferred_lifetime": 604800,
                        "valid_lifetime": 2592000,
                    },
                    "IA NA": {
                        "iaid": "0x00200001",
                        "t1": 43200,
                        "t2": 69120,
                        "address": "7771::399D:20AD:29FB:771B/128",
                        "preferred_lifetime": 86400,
                        "valid_lifetime": 172800,
                    },
                    "dns_server": "11::11",
                    "domain_name": "cisco.com",
                    "information_refresh_time": 0,
                },
            },
            "prefix_name": "TEST123",
            "prefix_rapid_commit": "disabled",
            "address_rapid_commit": "disabled",
        }
    }
}