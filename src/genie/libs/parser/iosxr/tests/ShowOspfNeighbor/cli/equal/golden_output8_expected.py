expected_output = {
    "process_name": "1",
    "vrfs": {
        "default": {
            "neighbors": {
                "10.0.0.4": {
                    "priority": "1",
                    "state": "FULL/BDR",
                    "dead_time": "00:00:38",
                    "address": "10.4.14.1",
                    "interface": "Bundle-Ether414",
                    "up_time": "2d01h"
                },
                "10.0.0.13": [
                    {
                        "priority": "1",
                        "state": "EXSTART/BDR",
                        "dead_time": "00:00:39",
                        "address": "10.13.14.1",
                        "interface": "Bundle-Ether1314.511",
                        "up_time": "00:00:38"
                    },
                    {
                        "priority": "1",
                        "state": "FULL/BDR",
                        "dead_time": "00:00:34",
                        "address": "10.13.14.5",
                        "interface": "Bundle-Ether1314.510",
                        "up_time": "17w1d"
                    }
                ]
            },
            "total_neighbor_count": 3
        }
    }
}