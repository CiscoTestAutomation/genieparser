expected_output = {
    "1": {
        "aces": {
            "30": {
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "ip",
                            "source_network": {
                                "172.16.154.23/32": {
                                    "source_network": "172.16.154.23/32"
                                }
                            },
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                        }
                    }
                },
                "name": "30",
                "actions": {"forwarding": "permit"},
            },
            "20": {
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "ip",
                            "source_network": {
                                "10.1.1.39/32": {"source_network": "10.1.1.39/32"}
                            },
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                        }
                    }
                },
                "name": "20",
                "actions": {"forwarding": "permit"},
            },
        },
        "type": "ipv4-acl-type",
        "name": "1",
    }
}
