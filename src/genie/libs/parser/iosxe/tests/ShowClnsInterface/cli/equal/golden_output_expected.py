expected_output = {
    "interfaces": {
        "GigabitEthernet1": {
            "status": "up",
            "line_protocol": "up",
            "clns_protocol_processing": False,
        },
        "GigabitEthernet2": {
            "status": "up",
            "line_protocol": "up",
            "checksum_enabled": True,
            "mtu": 1497,
            "encapsulation": "SAP",
            "erpdus_enabled": True,
            "min_interval_msec": 10,
            "clns_fast_switching": True,
            "clns_sse_switching": False,
            "dec_compatibility_mode": "OFF",
            "next_esh_ish_in": 20,
            "routing_protocol": {
                "IS-IS": {
                    "process_id": {
                        "test": {
                            "level_type": "level-1-2",
                            "interface_number": "0x1",
                            "local_circuit_id": "0x1",
                            "neighbor_extended_local_circuit_id": "0x0",
                            "hello_interval": {
                                "level-1": {"next_is_is_lan_hello_in": 1},
                                "level-2": {"next_is_is_lan_hello_in_ms": 645},
                            },
                            "level-1": {
                                "metric": 10,
                                "dr_id": "R2.01",
                                "circuit_id": "R2.01",
                                "ipv6_metric": 10,
                            },
                            "level-2": {
                                "metric": 10,
                                "dr_id": "0000.0000.0000.00",
                                "circuit_id": "R2.01",
                                "ipv6_metric": 10,
                            },
                            "priority": {
                                "level-1": {"priority": 64},
                                "level-2": {"priority": 64},
                            },
                            "adjacencies": {
                                "level-1": {"number_of_active_adjancies": 1},
                                "level-2": {"number_of_active_adjancies": 0},
                            },
                        }
                    }
                }
            },
        },
    }
}
