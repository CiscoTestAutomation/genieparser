expected_output = {
    "tag": {
        "VRF1": {
            "hostname_db": {
                "hostname": {
                    "7777.77ff.eeee": {"hostname": "R7", "level": 2},
                    "2222.22ff.4444": {"hostname": "R2", "local_router": True},
                }
            }
        },
        "test": {
            "hostname_db": {
                "hostname": {
                    "9999.99ff.3333": {"hostname": "R9", "level": 2},
                    "8888.88ff.1111": {"hostname": "R8", "level": 2},
                    "7777.77ff.eeee": {"hostname": "R7", "level": 2},
                    "5555.55ff.aaaa": {"hostname": "R5", "level": 2},
                    "3333.33ff.6666": {"hostname": "R3", "level": 2},
                    "1111.11ff.2222": {"hostname": "R1", "level": 1},
                    "2222.22ff.4444": {"hostname": "R2", "local_router": True},
                }
            }
        },
    }
}
