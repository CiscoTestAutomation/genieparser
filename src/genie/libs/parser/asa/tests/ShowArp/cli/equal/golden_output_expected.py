expected_output = {
    "outside": {
        "ipv4": {
            "neighbors": {
                "10.10.1.1": {
                    "ip": "10.10.1.1",
                    "link_layer_address": "aa11.bbff.ee55",
                    "age": "alias",
                },
                "10.10.1.1/1": {
                    "ip": "10.10.1.1",
                    "prefix_length": "1",
                    "link_layer_address": "aa11.bbff.ee55",
                    "age": "-",
                },
            }
        }
    },
    "pod100": {
        "ipv4": {
            "neighbors": {
                "10.10.1.1": {
                    "ip": "10.10.1.1",
                    "link_layer_address": "aa11.bbff.ee55",
                    "age": "2222",
                }
            }
        }
    },
}
