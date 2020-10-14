expected_output = {
    "vrf": {
        "default": {
            "interfaces": {
                "GigabitEthernet6/0": {
                    "ip": "yes",
                    "tunnel": "no",
                    "session": "ldp",
                    "operational": "yes",
                }
            }
        },
        "vpn1": {
            "interfaces": {
                "Ethernet3/1": {"ip": "no", "tunnel": "no", "operational": "yes"}
            }
        },
    }
}
