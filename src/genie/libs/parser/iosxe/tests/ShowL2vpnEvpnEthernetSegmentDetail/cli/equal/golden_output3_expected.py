expected_output = {
    "00CA.FE00.0000.0000.0001": {
        "interface": ["Ethernet0/0"],
        "redundancy_mode": "single-active",
        "df_wait_time": 3,
        "split_horizon_label": 0,
        "state": "Ready",
        "encap_type": "vxlan",
        "ordinal": 1,
        "core_isolation": "No",
        "rd": {
            "2.2.2.3:1" : {
                "export_rt": ["1:1", "1:2", "1:5", "1:6", "1:11",
                              "1:12", "1:13", "1:14", "1:21", "1:22",
                              "1:23", "1:24"],
                        }
               },
        "forwarder_list": [
            "1.1.1.2",
            "2.2.2.2"
        ],
    },
    "00CA.FE00.0000.0000.0002": {
        "interface": ["Ethernet0/1"],
        "redundancy_mode": "single-active",
        "df_wait_time": 3,
        "split_horizon_label": 0,
        "state": "Ready",
        "encap_type": "vxlan",
        "ordinal": 1,
        "core_isolation": "No",
        "rd": {
            "2.2.2.3:3" : {
                "export_rt": ["1:1", "1:2", "1:5", "1:6", "1:11",
                              "1:12", "1:13", "1:14", "1:21", "1:22",
                              "1:23", "1:24"],
                        }
               },
        "forwarder_list": [
            "1.1.1.2",
            "2.2.2.2"
        ],
    },
    "00CA.FE00.0000.0000.0003": {
        "interface": ["pseudowire100002", "pseudowire100003",
                      "pseudowire100005", "pseudowire100006"],
        "redundancy_mode": "single-active",
        "df_wait_time": 3,
        "split_horizon_label": 0,
        "state": "Port Down",
        "encap_type": "vxlan",
        "ordinal": "Not available",
        "core_isolation": "No",
        "rd": {
            "2.2.2.3:2" : {
                "export_rt": ["1:11", "1:12"],
                        }
               },
        "forwarder_list": [],
    },
}
