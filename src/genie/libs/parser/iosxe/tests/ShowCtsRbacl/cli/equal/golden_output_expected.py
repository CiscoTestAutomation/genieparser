expected_output = {
    "cts_rbacl": {
        "ip_ver_support": "IPv4 & IPv6",
        "name": {
            "TCP_51005-01": {
                "aces": {
                    1: {
                        "action": "permit",
                        "protocol": "tcp",
                        "direction": "dst",
                        "port": 51005
                    }
                },
                "ip_protocol_version": "IPV4",
                "refcnt": 2,
                "flag": "0x41000000",
                "stale": False
            },
            "TCP_51060-02": {
                "aces": {
                    1: {
                        "action": "permit",
                        "protocol": "tcp",
                        "direction": "dst",
                        "port": 51060
                    }
                },
                "ip_protocol_version": "IPV4",
                "refcnt": 4,
                "flag": "0x41000000",
                "stale": False
            },
            "TCP_51144-01": {
                "aces": {
                    1: {
                        "action": "permit",
                        "protocol": "tcp",
                        "direction": "dst",
                        "port": 51144
                    }
                },
                "ip_protocol_version": "IPV4",
                "refcnt": 10,
                "flag": "0x41000000",
                "stale": False
            },
            "TCP_51009-01": {
                "aces": {
                    1: {
                        "action": "permit",
                        "protocol": "tcp",
                        "direction": "dst",
                        "port": 51009
                    }
                },
                "ip_protocol_version": "IPV4",
                "refcnt": 2,
                "flag": "0x41000000",
                "stale": False
            }
        }
    }
}

