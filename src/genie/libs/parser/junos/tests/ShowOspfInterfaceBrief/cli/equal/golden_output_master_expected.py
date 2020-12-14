expected_output = {
    "instance": {
        "master": {
            "areas": {
                "0.0.0.4": {
                    "interfaces": {
                        "ge-0/0/4.0": {
                            "state": "BDR",
                            "dr_id": "10.64.4.4",
                            "bdr_id": "192.168.10.22",
                            "nbrs_count": 2,
                        },
                        "ge-0/0/5.0": {
                            "state": "BDR",
                            "dr_id": "10.16.2.2",
                            "bdr_id": "10.16.2.2",
                            "nbrs_count": 3,
                        },
                        "ge-0/0/6.0": {
                            "state": "DR",
                            "dr_id": "10.64.4.4",
                            "bdr_id": "192.168.10.22",
                            "nbrs_count": 4,
                        },
                        "lo1.0": {
                            "state": "DR",
                            "dr_id": "10.16.2.2",
                            "bdr_id": "0.0.0.0",
                            "nbrs_count": 0,
                        },
                    }
                }
            }
        }
    }
}
