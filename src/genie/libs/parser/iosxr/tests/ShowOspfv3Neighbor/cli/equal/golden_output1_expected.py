expected_output = {
    "process": "1",
    "vrfs": {
        "default": {
            "neighbors": {
                "10.4.1.1": {
                    "priority": "1",
                    "state": "FULL/DR",
                    "dead_time": "00:00:39",
                    "address": "22",
                    "interface": "GigabitEthernet0/0/0/0.110",
                    "up_time": "02:02:04"
                },
                "10.36.3.3": {
                    "priority": "1",
                    "state": "FULL/BDR",
                    "dead_time": "00:00:39",
                    "address": "136",
                    "interface": "GigabitEthernet0/0/0/1.110",
                    "up_time": "01:59:28"
                }
            },
            "total_neighbor_count": 2
        }
    }
}