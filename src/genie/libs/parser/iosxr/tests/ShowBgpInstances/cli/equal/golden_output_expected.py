expected_output = {
    "instance": {
        "test": {
            "instance_id": 0,
            "bgp_id": 333,
            "num_vrfs": 0,
            "placed_grp": "v4_routing"
        },
        "test1": {
            "instance_id": 1,
            "bgp_id": 333,
            "num_vrfs": 0,
            "placed_grp": "bgp2_1"
        },
        "test2": {
            "instance_id": 2,
            "bgp_id": 333,
            "num_vrfs": 0,
            "placed_grp": "bgp3_1"
        },
        "default": {
            "instance_id": 3,
            "bgp_id": 100,
            "num_vrfs": 2,
            "address_families": [
                "ipv4 unicast",
                "vpnv4 unicast"
            ],
            "placed_grp": "bgp4_1"
        }
    }
}
