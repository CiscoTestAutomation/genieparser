expected_output = {
    "segment_routing": {
        "bindings": {
            "mapping_server": {
                "policy": {
                    "prefix_sid_remote_export_map": {
                        "ipv4": {
                            "mapping_entry": {
                                "192.168.111.1/32": {
                                    "algorithm": {
                                        "ALGO_0": {
                                            "prefix": "192.168.111.1/32",
                                            "algorithm": "ALGO_0",
                                            "value_type": "Indx",
                                            "sid": 5001,
                                            "range": "1",
                                            "srgb": "Y",
                                            "source": "OSPF Area 8 10.229.11.11",
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
