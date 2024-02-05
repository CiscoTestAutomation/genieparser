expected_output = {
    "instance": {
        "default": {
            "vrf": {
                "default": {
                    "address_family": {
                        "vpnv4 unicast": {
                            "router_id": "10.4.1.1",
                            "local_as": 100,
                            "generic_scan_interval": 60,
                            "non_stop_routing": "enabled",
                            "table_state": "active",
                            "table_id": "0x0",
                            "rd_version": 0,
                            "bgp_table_version": 43,
                            "nsr_initial_initsync_version": 11,
                            "nsr_initial_init_ver_status": "reached",
                            "nsr_issu_sync_group_versions": "0/0",
                            "scan_interval": 60,
                            "operation_mode": "standalone",
                            "process": {
                                "Speaker": {
                                    "rcvtblver": 43,
                                    "brib_rib": 43,
                                    "labelver": 43,
                                    "importver": 43,
                                    "sendtblver": 43,
                                    "standbyver": 0,
                                }
                            },
                        },
                        "vpnv6 unicast": {
                            "router_id": "10.4.1.1",
                            "local_as": 100,
                            "generic_scan_interval": 60,
                            "non_stop_routing": "enabled",
                            "table_state": "active",
                            "table_id": "0x0",
                            "rd_version": 0,
                            "bgp_table_version": 43,
                            "nsr_initial_initsync_version": 11,
                            "nsr_initial_init_ver_status": "reached",
                            "nsr_issu_sync_group_versions": "0/0",
                            "scan_interval": 60,
                            "operation_mode": "standalone",
                            "process": {
                                "Speaker": {
                                    "rcvtblver": 43,
                                    "brib_rib": 43,
                                    "labelver": 43,
                                    "importver": 43,
                                    "sendtblver": 43,
                                    "standbyver": 0,
                                }
                            },
                        },
                    },
                    "neighbor": {
                        "10.16.2.2": {
                            "address_family": {
                                "vpnv4 unicast": {
                                    "spk": 0,
                                    "msg_rcvd": 59,
                                    "msg_sent": 56,
                                    "tbl_ver": 43,
                                    "input_queue": 0,
                                    "output_queue": 0,
                                    "up_down": "00:50:38",
                                    "state_pfxrcd": "10",
                                },
                            },
                            "remote_as": 100,
                        },
                        "10.36.3.3": {
                            "address_family": {
                                "vpnv4 unicast": {
                                    "spk": 0,
                                    "msg_rcvd": 68,
                                    "msg_sent": 58,
                                    "tbl_ver": 43,
                                    "input_queue": 0,
                                    "output_queue": 0,
                                    "up_down": "00:47:11",
                                    "state_pfxrcd": "10",
                                },
                            },
                            "remote_as": "60000.60001",
                        },
                        "2001:db8:20:1:5::5": {
                            "address_family": {
                                "vpnv6 unicast": {
                                    "input_queue": 0,
                                    "msg_rcvd": 68,
                                    "msg_sent": 58,
                                    "output_queue": 0,
                                    "spk": 0,
                                    "state_pfxrcd": "10",
                                    "tbl_ver": 43,
                                    "up_down": "00:47:11",
                                },
                            },
                            "remote_as": "60000.60002",
                        },                        
                    },
                }
            }
        }
    }
}
