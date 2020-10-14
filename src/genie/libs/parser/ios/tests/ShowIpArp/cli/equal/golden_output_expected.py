expected_output = {
    "interfaces": {
        "FastEthernet0": {
            "ipv4": {
                "neighbors": {
                    "10.1.8.1": {
                        "age": "79",
                        "ip": "10.1.8.1",
                        "link_layer_address": "0012.7fff.04d7",
                        "origin": "dynamic",
                        "protocol": "Internet",
                        "type": "ARPA",
                    },
                    "10.1.8.146": {
                        "age": "-",
                        "ip": "10.1.8.146",
                        "link_layer_address": "843d.c6ff.f1ef",
                        "origin": "static",
                        "protocol": "Internet",
                        "type": "ARPA",
                    },
                }
            }
        },
        "Port-channel10": {
            "ipv4": {
                "neighbors": {
                    "10.9.1.1": {
                        "age": "-",
                        "ip": "10.9.1.1",
                        "link_layer_address": "843d.c6ff.f1fe",
                        "origin": "static",
                        "protocol": "Internet",
                        "type": "ARPA",
                    }
                }
            }
        },
        "Vlan99": {
            "ipv4": {
                "neighbors": {
                    "10.69.1.2": {
                        "age": "-",
                        "ip": "10.69.1.2",
                        "link_layer_address": "843d.c6ff.f1f9",
                        "origin": "static",
                        "protocol": "Internet",
                        "type": "ARPA",
                    }
                }
            }
        },
    }
}
