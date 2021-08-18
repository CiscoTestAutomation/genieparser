expected_output = {
    "instance": {
        "default": {
        "vrf": {
            "default": {
            "address_family": {
                "ipv4 unicast": {
                "bgp_table_version": 16,
                "generic_scan_interval": "60",
                "instance_number": "0",
                "local_as": "65108.65108",
                "non_stop_routing": True,
                "nsr_initial_init_ver_status": "reached",
                "nsr_initial_initsync_version": "3",
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
                        "metric": "0",
                        "next_hop": "10.10.10.107",
                        "origin_codes": "?",
                        "path": "65107.65107",
                        "status_codes": "*",
                        "weight": "0"
                        }
                    }
                    },
                    "10.7.7.7/32": {
                    "index": {
                        1: {
                        "metric": "0",
                        "next_hop": "10.10.10.107",
                        "origin_codes": "?",
                        "path": "65107.65107",
                        "status_codes": "*>",
                        "weight": "0"
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
                        "metric": "0",
                        "next_hop": "10.10.10.107",
                        "origin_codes": "?",
                        "path": "65107.65107",
                        "status_codes": "*",
                        "weight": "0"
                        }
                    }
                    }
                },
                "processed_paths": 6,
                "processed_prefix": 4,
                "rd_version": 16,
                "router_identifier": "10.10.10.108",
                "scan_interval": 60,
                "table_id": "0xe0000000",
                "table_state": "active"
                },
                "ipv6 unicast": {
                "bgp_table_version": 15,
                "generic_scan_interval": "60",
                "instance_number": "0",
                "local_as": "65108.65108",
                "non_stop_routing": True,
                "nsr_initial_init_ver_status": "reached",
                "nsr_initial_initsync_version": "1",
                "nsr_issu_sync_group_versions": "0/0",
                "prefix": {
                    "10:10:10:7::/128": {
                    "index": {
                        1: {
                        "metric": "0",
                        "next_hop": "2001:2001:2001:2001:2001::7",
                        "origin_codes": "?",
                        "path": "65107.65107",
                        "status_codes": "*>",
                        "weight": "0"
                        }
                    }
                    },
                    "10:10:10:8::/128": {
                    "index": {
                        1: {
                        "locprf": "0",
                        "next_hop": "::",
                        "origin_codes": "?",
                        "status_codes": "*>",
                        "weight": "32768"
                        }
                    }
                    },
                    "2000:2000:2000:7777::/64": {
                    "index": {
                        1: {
                        "metric": "0",
                        "origin_codes": "?",
                        "path": "65107.65107",
                        "status_codes": "*>",
                        "weight": "0"
                        }
                    }
                    },
                    "2000:2000:2000:8888::/64": {
                    "index": {
                        1: {
                        "metric": "0",
                        "next_hop": "::",
                        "origin_codes": "?",
                        "status_codes": "*>",
                        "weight": "32768"
                        }
                    }
                    },
                    "2001:2001:2001:2001:2001::/124": {
                    "index": {
                        1: {
                        "metric": "0",
                        "next_hop": "::",
                        "origin_codes": "?",
                        "path": "65107.65107",
                        "status_codes": "*>",
                        "weight": "0"
                        }
                    }
                    },
                    "2001:2001:2001:2001:2001::7/128": {
                    "index": {
                        1: {
                        "metric": "0",
                        "next_hop": "::",
                        "origin_codes": "?",
                        "status_codes": "*>",
                        "weight": "32768"
                        }
                    }
                    }
                },
                "processed_paths": 7,
                "processed_prefix": 6,
                "rd_version": 15,
                "router_identifier": "10.10.10.108",
                "scan_interval": 60,
                "table_id": "0xe0800000",
                "table_state": "active"
                }
            }
            }
        }
        }
    }
}