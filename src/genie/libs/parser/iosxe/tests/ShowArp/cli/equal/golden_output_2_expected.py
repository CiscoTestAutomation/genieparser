expected_output = {
    "global_static_table": {
        "10.169.197.93": {
            "ip_address": "10.169.197.93",
            "mac_address": "fa16.3eff.b7ad",
            "encap_type": "ARPA",
            "age": "-",
            "protocol": "Internet",
        }
    },
    "interfaces": {
        "GigabitEthernet2": {
            "ipv4": {
                "neighbors": {
                    "10.169.197.94": {
                        "ip": "10.169.197.94",
                        "link_layer_address": "fa16.3eff.aae1",
                        "type": "ARPA",
                        "origin": "static",
                        "age": "-",
                        "protocol": "Internet",
                    }
                }
            }
        },
        "GigabitEthernet4": {
            "ipv4": {
                "neighbors": {
                    "10.169.197.97": {
                        "ip": "10.169.197.97",
                        "link_layer_address": "fa16.3eff.45a8",
                        "type": "ARPA",
                        "origin": "dynamic",
                        "age": "18",
                        "protocol": "Internet",
                    },
                    "10.169.197.98": {
                        "ip": "10.169.197.98",
                        "link_layer_address": "fa16.3eff.9dca",
                        "type": "ARPA",
                        "origin": "static",
                        "age": "-",
                        "protocol": "Internet",
                    },
                }
            }
        },
    },
}
