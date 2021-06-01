expected_output = {
    "interfaces": {
        "Ethernet1/1": {
            "ipv4": {
                "neighbors": {
                    "10.2.4.4": {
                        "ip": "10.2.4.4",
                        "link_layer_address": "5e00.00ff.030a",
                        "physical_interface": "Ethernet1/1",
                        "origin": "dynamic",
                        "age": "00:13:42",
                    },
                    "10.2.4.5": {
                        "ip": "10.2.4.5",
                        "link_layer_address": "aaaa.bbff.8888",
                        "physical_interface": "Ethernet1/1",
                        "origin": "static",
                        "age": "-",
                    },
                }
            }
        },
        "Ethernet1/2": {
            "ipv4": {
                "neighbors": {
                    "10.2.5.5": {
                        "ip": "10.2.5.5",
                        "link_layer_address": "5e00.00ff.040b",
                        "physical_interface": "Ethernet1/2",
                        "origin": "dynamic",
                        "age": "00:00:04",
                    }
                }
            }
        },
    },
    "statistics": {"entries_total": 2},
}
