expected_output = {
    "vpls_name": {
        "serviceStit3": {
            "state": "UP",
            "interface": {
                "Pw4": {
                    "encapsulation": "MPLS 10.1.8.8:300",
                    "state": "UP",
                    "priority": 0,
                    "group": "right",
                    "state_in_l2vpn_service": "UP",
                },
                "Pw3": {
                    "encapsulation": "MPLS 10.196.7.7:300",
                    "state": "UP",
                    "priority": 0,
                    "group": "left",
                    "state_in_l2vpn_service": "UP",
                },
            },
        },
        "serviceWire1": {
            "state": "UP",
            "interface": {
                "Eth3/1:20": {
                    "encapsulation": "EVC 55",
                    "state": "DN",
                    "priority": 0,
                    "group": "core_conn",
                    "state_in_l2vpn_service": "IA",
                },
                "Pw2": {
                    "encapsulation": "MPLS 10.144.6.6:200",
                    "state": "SB",
                    "priority": 1,
                    "group": "core",
                    "state_in_l2vpn_service": "IA",
                },
                "Pw1": {
                    "encapsulation": "MPLS 10.100.5.5:100",
                    "state": "UP",
                    "priority": 0,
                    "group": "core",
                    "state_in_l2vpn_service": "UP",
                },
                "Eth1/1:10": {
                    "encapsulation": "EVC 45",
                    "state": "UP",
                    "priority": 0,
                    "group": "access",
                    "state_in_l2vpn_service": "UP",
                },
                "Eth2/1:20": {
                    "encapsulation": "EVC 55",
                    "state": "UP",
                    "priority": 0,
                    "group": "access_conn",
                    "state_in_l2vpn_service": "UP",
                },
                "Eth4/1:20": {
                    "encapsulation": "EVC 55",
                    "state": "UP",
                    "priority": 1,
                    "group": "core_conn",
                    "state_in_l2vpn_service": "UP",
                },
            },
        },
    }
}
