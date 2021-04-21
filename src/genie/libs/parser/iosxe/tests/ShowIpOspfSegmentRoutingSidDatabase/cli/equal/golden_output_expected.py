expected_output = {
    "process_id": {
        1234: {
            "router_id": "10.4.1.1",
            "sids": {
                "total_entries": 2,
                1: {
                    "index": {
                        1: {
                            "prefix": "10.4.1.1/32",
                            "codes": "L",
                            "adv_rtr_id": "10.4.1.1",
                            "area_id": "0.0.0.8",
                            "type": "Intra",
                            "algo": 0,
                        }
                    }
                },
                2: {
                    "index": {
                        1: {
                            "prefix": "10.16.2.2/32",
                            "adv_rtr_id": "10.16.2.2",
                            "area_id": "0.0.0.8",
                            "type": "Intra",
                            "algo": 0,
                        }
                    }
                },
            },
        }
    }
}
