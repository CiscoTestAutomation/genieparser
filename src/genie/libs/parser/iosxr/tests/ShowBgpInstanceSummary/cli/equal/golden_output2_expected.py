expected_output = {
    "instance": {
        "default": {
            "vrf": {
                "HI-TST": {
                    "address_family": {
                        "vpnv4 unicast": {
                            "route_distinguisher": "10.16.2.2:0",
                            "vrf_id": "0x60000001",
                            "router_id": "10.4.1.1",
                            "local_as": 64577,
                            "non_stop_routing": "enabled",
                            "table_state": "active",
                            "table_id": "0xe0011110",
                            "rd_version": 19,
                            "bgp_table_version": 1,
                            "nsr_initial_initsync_version": 18,
                            "nsr_initial_init_ver_status": "reached",
                            "nsr_issu_sync_group_versions": "0/0",
                            "operation_mode": "standalone",
                            "process": {
                                "Speaker": {
                                    "rcvtblver": 1,
                                    "brib_rib": 1,
                                    "labelver": 1,
                                    "importver": 1,
                                    "sendtblver": 1,
                                    "standbyver": 0,
                                }
                            },
                        }
                    }
                },
                "CTV-BG-JYI": {
                    "address_family": {
                        "vpnv4 unicast": {
                            "route_distinguisher": "10.25.4.5:1",
                            "vrf_id": "0x60000004",
                            "router_id": "10.4.1.1",
                            "local_as": 12345,
                            "non_stop_routing": "enabled",
                            "table_state": "active",
                            "table_id": "0xe0011114",
                            "rd_version": 1,
                            "bgp_table_version": 1,
                            "nsr_initial_initsync_version": 18,
                            "nsr_initial_init_ver_status": "reached",
                            "nsr_issu_sync_group_versions": "0/0",
                            "operation_mode": "standalone",
                            "process": {
                                "Speaker": {
                                    "rcvtblver": 1,
                                    "brib_rib": 1,
                                    "labelver": 1,
                                    "importver": 1,
                                    "sendtblver": 1,
                                    "standbyver": 0,
                                }
                            },
                        }
                    }
                },
            }
        }
    }
}
