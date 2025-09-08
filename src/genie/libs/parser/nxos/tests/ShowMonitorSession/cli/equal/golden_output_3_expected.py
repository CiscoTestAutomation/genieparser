expected_output = {
    "session": {
        "session_number": 1,
        "type": "local",
        "mode": "extended",
        "ssn_direction": "both",
        "state": "up",
        "src_intf_all": "both",
        "filter_vlans": 100,
        "feature": {
            "mtu_trunc": {
                "enabled": "No"
            },
            "rate_limit_rx": {
                "enabled": "No"
            },
            "rate_limit_tx": {
                "enabled": "No"
            },
            "sampling": {
                "enabled": "No"
            },
            "mcbe": {
                "enabled": "No"
            },
            "l3_tx": {
                "enabled": "-",
                "modules_supported": [
                    1,
                    3,
                    4,
                    9
                ]
            },
            "simpl rb span": {
                "enabled": "No"
            },
            "extended_ssn": {
                "enabled": "Yes",
                "modules_supported": [
                    1,
                    3,
                    4,
                    9
                ]
            }
        },
        "legend": {
            "mcbe": "Multicast Best Effort",
            "l3_tx": "L3 Multicast Egress SPAN",
            "exsp_x": "L3, FP, or misc"
        }
    }
}
