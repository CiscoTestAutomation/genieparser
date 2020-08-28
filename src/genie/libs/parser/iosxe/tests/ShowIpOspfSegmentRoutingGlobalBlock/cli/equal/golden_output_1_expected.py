expected_output = {
    "process_id": {
        1234: {
            "router_id": "10.4.1.1",
            "area": 3,
            "routers": {
                "10.4.1.1": {
                    "router_id": "10.4.1.1",
                    "sr_capable": "Yes",
                    "sr_algorithm": "SPF,StrictSPF",
                    "srgb_base": 16000,
                    "srgb_range": 8000,
                    "sid_label": "Label",
                },
                "10.16.2.2": {
                    "router_id": "10.16.2.2",
                    "sr_capable": "Yes",
                    "sr_algorithm": "SPF,StrictSPF",
                    "srgb_base": 16000,
                    "srgb_range": 8000,
                    "sid_label": "Label",
                },
            },
        }
    }
}
