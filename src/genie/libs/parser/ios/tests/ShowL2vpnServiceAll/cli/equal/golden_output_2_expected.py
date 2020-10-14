expected_output = {
    "vpls_name": {
        "Gi1/1/1-1001": {
            "interface": {
                "pw100001": {
                    "encapsulation": "10.9.1.2:1234000(MPLS)",
                    "priority": 0,
                    "state_in_l2vpn_service": "UP",
                    "state": "UP",
                    "group": "right",
                },
                "Gi1/1/1": {
                    "encapsulation": "Gi1/1/1:1001(Gi VLAN)",
                    "priority": 0,
                    "state_in_l2vpn_service": "UP",
                    "state": "UP",
                    "group": "left",
                },
            },
            "state": "UP",
        }
    }
}
