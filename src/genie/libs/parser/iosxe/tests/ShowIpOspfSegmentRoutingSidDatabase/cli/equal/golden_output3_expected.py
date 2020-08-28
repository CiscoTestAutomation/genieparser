expected_output = {
    "process_id": {
        65109: {
            "router_id": "10.4.1.1",
            "sids": {
                "total_entries": 4,
                1: {
                    "index": {
                        1: {
                            "prefix": "10.4.1.1/32",
                            "codes": "L",
                            "adv_rtr_id": "10.4.1.1",
                            "area_id": "0.0.0.8",
                            "type": "Intra",
                            "algo": 0,
                        },
                        2: {
                            "prefix": "10.4.1.2/32",
                            "adv_rtr_id": "10.4.1.2",
                            "area_id": "0.0.0.8",
                            "type": "Intra",
                            "algo": 0,
                        },
                    }
                },
                11: {
                    "index": {
                        1: {
                            "prefix": "10.4.1.2/32",
                            "adv_rtr_id": "10.4.1.2",
                            "area_id": "0.0.0.8",
                            "type": "Intra",
                            "algo": 0,
                        }
                    }
                },
                45: {
                    "index": {
                        1: {
                            "prefix": "10.4.1.3/32",
                            "codes": "M",
                            "type": "Unknown",
                            "algo": 0,
                        }
                    }
                },
            },
        }
    }
}
