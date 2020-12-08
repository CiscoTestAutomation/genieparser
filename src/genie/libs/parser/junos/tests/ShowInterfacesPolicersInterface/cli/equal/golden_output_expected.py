expected_output = {
    "interface-policer-information": {
        "physical-interface": [
            {
                "admin-status": "up",
                "logical-interface": [
                    {
                        "admin-status": "up",
                        "name": "ge-0/0/2.0",
                        "oper-status": "up",
                        "policer-information": [
                            {
                                "policer-family": "inet",
                                "policer-input": "GE_1M-ge-0/0/2.0-log_int-i",
                                "policer-output": "GE_1M-ge-0/0/2.0-log_int-o",
                            },
                            {
                                "policer-family": "inet6",
                                "policer-input": "GE_1M-ge-0/0/2.0-log_int-i",
                                "policer-output": "GE_1M-ge-0/0/2.0-log_int-o",
                            },
                            {
                                "policer-family": "multiservice",
                                "policer-input": "__default_arp_policer__",
                            },
                        ],
                    }
                ],
                "name": "ge-0/0/2",
                "oper-status": "up",
            }
        ]
    }
}
