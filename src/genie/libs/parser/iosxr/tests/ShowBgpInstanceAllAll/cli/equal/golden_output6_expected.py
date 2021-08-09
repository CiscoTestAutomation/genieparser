expected_output = {
        "instance": {
            "default": {
            "vrf": {
                "default": {
                "address_family": {
                    "ipv4 unicast": {
                    "bgp_table_version": 12,
                    "generic_scan_interval": "60",
                    "instance_number": "0",
                    "local_as": "65108.65108",
                    "non_stop_routing": True,
                    "nsr_initial_init_ver_status": "reached",
                    "nsr_initial_initsync_version": "2",
                    "nsr_issu_sync_group_versions": "0/0",
                    "prefix": {
                        "10.10.10.0/24": {
                        "index": {
                            1: {
                            "locprf": "0",
                            "next_hop": "0.0.0.0",
                            "origin_codes": "?",
                            "status_codes": "*>",
                            "weight": "32768"
                            },
                            2: {
                            "next_hop": "10.10.10.107",
                            "origin_codes": "?",
                            "status_codes": "*"
                            }
                        }
                        },
                        "10.7.7.7/32": {
                        "index": {
                            1: {
                            "next_hop": "10.10.10.107",
                            "origin_codes": "?",
                            "status_codes": "*>"
                            }
                        }
                        },
                        "10.8.8.8/32": {
                        "index": {
                            1: {
                            "locprf": "0",
                            "next_hop": "0.0.0.0",
                            "origin_codes": "?",
                            "status_codes": "*>",
                            "weight": "32768"
                            }
                        }
                        },
                        "192.168.52.0/24": {
                        "index": {
                            1: {
                            "locprf": "0",
                            "next_hop": "0.0.0.0",
                            "origin_codes": "?",
                            "status_codes": "*>",
                            "weight": "32768"
                            },
                            2: {
                            "next_hop": "10.10.10.107",
                            "origin_codes": "?",
                            "status_codes": "*"
                            }
                        }
                        }
                    },
                    "processed_paths": 6,
                    "processed_prefix": 4,
                    "rd_version": 12,
                    "router_identifier": "10.10.10.108",
                    "scan_interval": 60,
                    "table_id": "0xe0000000",
                    "table_state": "active"
                    }
                }
                }
            }
          }
      }
    }