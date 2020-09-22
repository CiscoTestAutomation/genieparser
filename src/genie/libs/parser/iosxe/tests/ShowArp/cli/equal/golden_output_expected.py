expected_output = {
    "interfaces": {
        "Vlan100": {
            "ipv4": {
                "neighbors": {
                    "192.168.234.1": {
                        "age": "-",
                        "ip": "192.168.234.1",
                        "link_layer_address": "58bf.eaff.e508",
                        "origin": "static",
                        "protocol": "Internet",
                        "type": "ARPA",
                    },
                    "192.168.234.2": {
                        "age": "29",
                        "ip": "192.168.234.2",
                        "link_layer_address": "3820.56ff.6fc3",
                        "origin": "dynamic",
                        "protocol": "Internet",
                        "type": "ARPA",
                    },
                }
            }
        },
        "Vlan200": {
            "ipv4": {
                "neighbors": {
                    "192.168.70.1": {
                        "age": "-",
                        "ip": "192.168.70.1",
                        "link_layer_address": "58bf.eaff.e519",
                        "origin": "static",
                        "protocol": "Internet",
                        "type": "ARPA",
                    }
                }
            }
        },
    }
}
