expected_output = {
    "tag": {
        "VRF1": {
            "lsp_log": {
                "level": {
                    1: {
                        "index": {
                            1: {
                                "when": "01:13:52",
                                "count": 5,
                                "triggers": "CONFIG OTVINFOCHG",
                            },
                            2: {
                                "when": "00:25:46",
                                "count": 1,
                                "triggers": "ATTACHFLAG",
                            },
                            3: {
                                "when": "00:25:44",
                                "count": 2,
                                "triggers": "ATTACHFLAG IPV6IA",
                            },
                        }
                    },
                    2: {
                        "index": {
                            1: {
                                "when": "01:13:52",
                                "count": 5,
                                "triggers": "CONFIG OTVINFOCHG",
                            },
                            2: {
                                "when": "00:25:46",
                                "count": 2,
                                "triggers": "NEWADJ DIS",
                                "interface": "GigabitEthernet4",
                            },
                            3: {
                                "when": "00:25:45",
                                "count": 1,
                                "triggers": "ADJMTIDCHG",
                                "interface": "GigabitEthernet4",
                            },
                        }
                    },
                }
            }
        }
    }
}
