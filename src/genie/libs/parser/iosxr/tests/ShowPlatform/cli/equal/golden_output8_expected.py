expected_output = {
    "slot": {
        "rp": {
            "0/RSP0": {
                "name": "A9K-RSP-4G",
                "full_slot": "0/RSP0/CPU0",
                "state": "IOS XR RUN",
                "config_state": "PWR,NSHUT,MON",
                "redundancy_state": "Active",
            },
            "0/RSP1": {
                "name": "A9K-RSP-4G",
                "full_slot": "0/RSP1/CPU0",
                "state": "IOS XR RUN",
                "config_state": "PWR,NSHUT,MON",
                "redundancy_state": "Standby",
            },
        },
        "lc": {
            "0/0": {
                "name": "A9K-8T/4-B",
                "full_slot": "0/0/CPU0",
                "state": "IOS XR RUN",
                "config_state": "PWR,NSHUT,MON",
            },
            "0/1": {
                "name": "A9K-8T/4-B",
                "full_slot": "0/1/CPU0",
                "state": "IOS XR RUN",
                "config_state": "PWR,NSHUT,MON",
            },
            "0/4": {
                "name": "A9K-2T20GE-B",
                "full_slot": "0/4/CPU0",
                "state": "IOS XR RUN",
                "config_state": "PWR,NSHUT,MON",
            },
            "0/5": {
                "name": "A9K-2T20GE-B",
                "full_slot": "0/5/CPU0",
                "state": "IOS XR RUN",
                "config_state": "PWR,NSHUT,MON",
            },
            "0/6": {
                "name": "A9K-MOD80-TR",
                "full_slot": "0/6/CPU0",
                "state": "IOS XR RUN",
                "config_state": "PWR,NSHUT,MON",
                "subslot": {
                    "0": {
                        "name": "A9K-MPA-20X1GE",
                        "state": "OK",
                        "config_state": "PWR,NSHUT,MON",
                        "redundancy_state": "None",
                    },
                    "1": {
                        "name": "A9K-MPA-4X10GE",
                        "state": "OK",
                        "config_state": "PWR,NSHUT,MON",
                        "redundancy_state": "None",
                    },
                },
            },
            "0/7": {
                "name": "A9K-MOD80-TR",
                "full_slot": "0/7/CPU0",
                "state": "IOS XR RUN",
                "config_state": "PWR,NSHUT,MON",
                "subslot": {
                    "0": {
                        "name": "A9K-MPA-20X1GE",
                        "state": "OK",
                        "config_state": "PWR,NSHUT,MON",
                        "redundancy_state": "None",
                    },
                    "1": {
                        "name": "A9K-MPA-4X10GE",
                        "state": "OK",
                        "config_state": "PWR,NSHUT,MON",
                        "redundancy_state": "None",
                    },
                },
            },
        },
        "oc": {
            "0/PM0": {
                "name": "A9K-3KW-AC",
                "full_slot": "0/PM0/SP",
                "state": "READY",
                "config_state": "PWR,NSHUT,MON",
            },
            "0/PM1": {
                "name": "A9K-3KW-AC",
                "full_slot": "0/PM1/SP",
                "state": "READY",
                "config_state": "PWR,NSHUT,MON",
            },
            "0/PM3": {
                "name": "A9K-3KW-AC",
                "full_slot": "0/PM3/SP",
                "state": "READY",
                "config_state": "PWR,NSHUT,MON",
            },
            "0/PM4": {
                "name": "A9K-3KW-AC",
                "full_slot": "0/PM4/SP",
                "state": "READY",
                "config_state": "PWR,NSHUT,MON",
            },
            "0/FT0": {
                "name": "FAN TRAY",
                "full_slot": "0/FT0/SP",
                "state": "READY",
                "config_state": "None",
            },
            "0/FT1": {
                "name": "FAN TRAY",
                "full_slot": "0/FT1/SP",
                "state": "READY",
                "config_state": "None",
            },
        },
    }
}