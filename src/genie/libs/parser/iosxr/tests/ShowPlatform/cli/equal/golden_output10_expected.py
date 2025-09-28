expected_output = {
    "slot": {
        "rp": {
            "0/RP0": {
                "name": "A99-RP-F",
                "full_slot": "0/RP0/CPU0",
                "state": "IOS XR RUN",
                "config_state": "NSHUT",
                "redundancy_state": "Active",
            },
            "0/RP1": {
                "name": "A99-RP-F",
                "full_slot": "0/RP1/CPU0",
                "state": "IOS XR RUN",
                "config_state": "NSHUT",
                "redundancy_state": "Standby",
            },
        },
        "oc": {
            "0/FT0": {
                "name": "ASR-9903-FAN",
                "full_slot": "0/FT0",
                "state": "OPERATIONAL",
                "config_state": "NSHUT",
            },
            "0/FT1": {
                "name": "ASR-9903-FAN",
                "full_slot": "0/FT1",
                "state": "OPERATIONAL",
                "config_state": "NSHUT",
            },
            "0/FT2": {
                "name": "ASR-9903-FAN",
                "full_slot": "0/FT2",
                "state": "OPERATIONAL",
                "config_state": "NSHUT",
            },
            "0/FT3": {
                "name": "ASR-9903-FAN",
                "full_slot": "0/FT3",
                "state": "OPERATIONAL",
                "config_state": "NSHUT",
            },
            "0/PT0": {
                "name": "ASR-9900-DC-PEM",
                "full_slot": "0/PT0",
                "state": "OPERATIONAL",
                "config_state": "NSHUT",
            },
        },
        "lc": {
            "0/0": {
                "name": "ASR-9903-LC",
                "full_slot": "0/0/CPU0",
                "state": "IOS XR RUN",
                "config_state": "NSHUT",
                "subslot": {
                    "1": {
                        "name": "A9903-20HG-PEC",
                        "state": "OK",
                        "config_state": "None",
                        "redundancy_state": "None",
                    }
                },
            }
        },
    }
}
