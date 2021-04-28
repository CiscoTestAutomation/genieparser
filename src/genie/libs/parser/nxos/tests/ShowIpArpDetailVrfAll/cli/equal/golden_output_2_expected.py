expected_output = {
    "interfaces": {
        "Vlan392": {
            "ipv4": {
                "neighbors": {
                    "172.16.8.178": {
                        "age": "00:00:04",
                        "ip": "172.16.8.178",
                        "link_layer_address": "INCOMPLETE",
                        "origin": "dynamic",
                        "physical_interface": "Vlan392",
                    },
                    "172.16.8.183": {
                        "age": "00:13:47",
                        "ip": "172.16.8.183",
                        "link_layer_address": "0050.56ff.ece6",
                        "origin": "dynamic",
                        "physical_interface": "port-channel105",
                    },
                    "172.16.8.185": {
                        "age": "00:08:55",
                        "flag": "Adjacencies synced via CFSoE",
                        "ip": "172.16.8.185",
                        "link_layer_address": "0050.56ff.c11c",
                        "origin": "dynamic",
                        "physical_interface": "port-channel110",
                    },
                }
            }
        },
        "Vlan393": {
            "ipv4": {
                "neighbors": {
                    "172.16.10.1": {
                        "age": "-",
                        "ip": "172.16.10.1",
                        "link_layer_address": "0000.0cff.9129",
                        "origin": "static",
                        "physical_interface": "-",
                    }
                }
            }
        },
    }
}
