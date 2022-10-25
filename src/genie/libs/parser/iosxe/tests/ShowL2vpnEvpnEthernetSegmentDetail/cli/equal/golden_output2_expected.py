expected_output = {
    "03AA.BB00.0000.0200.0001": {
        "interface": ["Port-channel1"],
        "redundancy_mode": "all-active",
        "df_wait_time": 3,
        "split_horizon_label": 16,
        "state": "Ready",
        "encap_type": "mpls",
        "ordinal": 1,
        "core_isolation": "No",
        "rd": { 
            "4.4.4.3:1" : { 
                "export_rt": ["100:2"],
                        }
               },
        "forwarder_list": [
            "3.3.3.3",
            "4.4.4.3"
        ],
    },
}
