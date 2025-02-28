expected_output = {
    "slots": {
        "2": {
            "tables": {
                "default/base": {
                    "prefixes": {}
                },
                "vxlan-3001/base": {
                    "prefixes": {
                        "100.10.1.30/32": {
                            "next_hop": "100.10.1.30",
                            "interface": "port-channel11",
                            "labels": "",
                            "partial_install": ""
                        },
                        "100.10.1.31/32": {
                            "next_hop": "100.10.1.31",
                            "interface": "port-channel11",
                            "labels": "",
                            "partial_install": ""
                        },
                        "100.10.1.32/32": {
                            "next_hop": "100.10.1.32",
                            "interface": "port-channel11",
                            "labels": "",
                            "partial_install": ""
                        },
                        "100.10.1.33/32": {
                            "next_hop": "100.10.1.33",
                            "interface": "port-channel11",
                            "labels": "",
                            "partial_install": ""
                        },
                        "100.10.1.104/32": {
                            "next_hop": "100.10.1.104",
                            "interface": "Ethernet1/15/1",
                            "labels": "",
                            "partial_install": ""
                        }
                    }
                },
                "0xfffe": {
                    "prefixes": {}
                }
            }
        }
    }
}