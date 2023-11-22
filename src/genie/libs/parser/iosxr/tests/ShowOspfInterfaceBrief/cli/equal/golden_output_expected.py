expected_output = {
    "instance": {
        "mpls1": {
            "areas": {
                "0": {
                    "interfaces": {
                        "Lo0": {
                            "name": "Lo0",
                            "process_id": "mpls1",
                            "area": "0",
                            "ip_address": "17.17.17.17/32",
                            "state": "LOOP",
                            "cost": 1,
                            "nbrs_f": 0,
                            "nbrs_count": 0
                        },
                        "Lo10": {
                            "name": "Lo10",
                            "process_id": "mpls1",
                            "area": "0",
                            "ip_address": "10.10.10.10/32",
                            "state": "LOOP",
                            "cost": 1,
                            "nbrs_f": 0,
                            "nbrs_count": 0
                        },
                        "Hu0/0/0/0": {
                            "name": "Hu0/0/0/0",
                            "process_id": "mpls1",
                            "area": "0",
                            "ip_address": "21.0.0.1/24",
                            "state": "P2P",
                            "cost": 1,
                            "nbrs_f": 1,
                            "nbrs_count": 1
                        },
                        "Te0/2/0/0": {
                            "name": "Te0/2/0/0",
                            "process_id": "mpls1",
                            "area": "0",
                            "ip_address": "100.20.0.1/30",
                            "state": "P2P",
                            "cost": 10,
                            "nbrs_f": 1,
                            "nbrs_count": 1
                        },
                        "Te0/2/0/3": {
                            "name": "Te0/2/0/3",
                            "process_id": "mpls1",
                            "area": "0",
                            "ip_address": "100.10.0.1/30",
                            "state": "P2P",
                            "cost": 10,
                            "nbrs_f": 1,
                            "nbrs_count": 1
                        }
                    }
                }
            }
        }
    }
}
