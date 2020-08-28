expected_output = {
    "1": {
        "aces": {
            "10": {
                "actions": {"forwarding": "deny", "logging": "log-syslog"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "ipv4",
                            "source_network": {
                                "10.9.3.4 0.0.0.0": {
                                    "source_network": "10.9.3.4 0.0.0.0"
                                }
                            },
                        }
                    }
                },
                "name": "10",
                "statistics": {"matched_packets": 18},
            },
            "20": {
                "actions": {"forwarding": "permit"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "ipv4",
                            "source_network": {"any": {"source_network": "any"}},
                        }
                    }
                },
                "name": "20",
                "statistics": {"matched_packets": 58},
            },
        },
        "name": "1",
        "type": "ipv4-acl-type",
    },
    "meraki-fqdn-dns": {"name": "meraki-fqdn-dns", "type": "ipv4-acl-type"},
}
