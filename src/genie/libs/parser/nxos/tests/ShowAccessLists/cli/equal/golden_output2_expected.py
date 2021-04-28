expected_output = {
    "NTP-ACL": {
        "aces": {
            "10": {
                "actions": {"forwarding": "permit"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "protocol": "ip",
                            "source_network": {
                                "10.1.50.64/32": {"source_network": "10.1.50.64/32"}
                            },
                        }
                    }
                },
                "name": "10",
                "statistics": {"matched_packets": 0},
            },
            "20": {
                "actions": {"forwarding": "permit"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "protocol": "ip",
                            "source_network": {
                                "172.18.106.1/32": {"source_network": "172.18.106.1/32"}
                            },
                        }
                    }
                },
                "name": "20",
                "statistics": {"matched_packets": 4},
            },
            "40": {
                "actions": {"forwarding": "permit"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "protocol": "ip",
                            "source_network": {"any": {"source_network": "any"}},
                        }
                    }
                },
                "name": "40",
                "statistics": {"matched_packets": 4},
            },
        },
        "name": "NTP-ACL",
        "type": "ipv4-acl-type",
    }
}
