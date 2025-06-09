expected_output = {
    "slot": {
        "rp": {
            "0/RSP0": {
                "name": "A9K-RSP440-SE",
                "full_slot": "0/RSP0/CPU0",
                "state": "IOS XR RUN",
                "config_state": "PWR,NSHUT,MON",
                "redundancy_state": "Active",
            },
            "0/RSP1": {
                "name": "A9K-RSP440-SE",
                "full_slot": "0/RSP1/CPU0",
                "state": "IOS XR RUN",
                "config_state": "PWR,NSHUT,MON",
                "redundancy_state": "Standby",
            },
        },
        "lc": {
            "0/0": {
                "name": "A9K-24x10GE-TR",
                "full_slot": "0/0/CPU0",
                "state": "IOS XR RUN",
                "config_state": "PWR,NSHUT,MON",
            },
            "0/1": {
                "name": "A9K-2T20GE-L",
                "full_slot": "0/1/CPU0",
                "state": "IN-RESET",
                "config_state": "PWR,NSHUT,MON",
            },
            "0/2": {
                "name": "A9K-24x10GE-TR",
                "full_slot": "0/2/CPU0",
                "state": "IOS XR RUN",
                "config_state": "PWR,NSHUT,MON",
            },
            "0/3": {
                "name": "A9K-2x100GE-TR",
                "full_slot": "0/3/CPU0",
                "state": "IOS XR RUN",
                "config_state": "PWR,NSHUT,MON",
            },
        },
    }
}
