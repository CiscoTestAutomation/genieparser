

expected_output = {
    "vrf": {
        "VRF1": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "1": {
                            "areas": {
                                "0.0.0.1": {
                                    "sham_links": {
                                        "10.21.33.33 10.151.22.22": {
                                            "cost": 111,
                                            "dcbitless_lsa_count": 1,
                                            "donotage_lsa": "not allowed",
                                            "dead_interval": 13,
                                            "demand_circuit": True,
                                            "hello_interval": 3,
                                            "hello_timer": "00:00:00:772",
                                            "if_index": 2,
                                            "local_id": "10.21.33.33",
                                            "name": "SL0",
                                            "link_state": "up",
                                            "remote_id": "10.151.22.22",
                                            "retransmit_interval": 5,
                                            "state": "point-to-point,",
                                            "transit_area_id": "0.0.0.1",
                                            "transmit_delay": 7,
                                            "wait_interval": 13,
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
