expected_output = {
    "process": "1",
    "vrfs": {
        "default": {
            "neighbors": {
                "10.4.1.1": {
                    "priority": "1",
                    "state": "FULL/DR",
                    "dead_time": "00:00:34",
                    "address": "22",
                    "interface": "GigabitEthernet0/0/0/0.110",
                    "up_time": "2d20h"
                },
                "10.36.3.3": {
                    "priority": "1",
                    "state": "FULL/BDR",
                    "dead_time": "00:00:33",
                    "address": "136",
                    "interface": "GigabitEthernet0/0/0/1.110",
                    "up_time": "2d20h"
                }
            },
            "total_neighbor_count": 2
        },
        "VRF1": {
            "neighbors": {
                "10.36.3.3": {
                    "priority": "1",
                    "state": "FULL/BDR",
                    "dead_time": "00:00:36",
                    "address": "140",
                    "interface": "GigabitEthernet0/0/0/1.410",
                    "up_time": "2d20h"
                }
            },
            "total_neighbor_count": 1
        }
    }
}
