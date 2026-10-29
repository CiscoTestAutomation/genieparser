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
                    },
                    "80.244.17.144/29": {
                    "index": {
                        1: {
                        "metric": "120",
                        "locprf": "100",
                        "next_hop": "80.244.17.126",
                        "origin_codes": "?",
                        "path": "(64622)",
                        "status_codes": "*>",
                        "weight": "0"
                        },
                        2: {
                        "metric": "100",
                        "locprf": "100",
                        "next_hop": "213.140.196.36",
                        "origin_codes": "?",
                        "path": "(64630 64615 64622)",
                        "status_codes": "*",
                        "weight": "0"
                        }
                    }
                    },
                    "80.244.96.160/27": {
                    "index": {
                        1: {
                        "locprf": "100",
                        "next_hop": "213.140.196.20",
                        "origin_codes": "?",
                        "path": "(64630 64609) 6762 4445 3209 21334",
                        "status_codes": "*>",
                        "weight": "0"
                        },
                        2: {
                        "locprf": "100",
                        "next_hop": "213.140.196.20",
                        "origin_codes": "?",
                        "path": "(64629 64601 64630 64609) 6762 4445 3209 21334",
                        "status_codes": "*",
                        "weight": "0"
                        }
                    }
                    }
                },
                "processed_paths": 10,
                "processed_prefix": 6,
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
                    },
                    "2400:cb00:203::/48": {
                    "index": {
                        1: {
                        "locprf": "120",
                        "next_hop": "2a02:540:5::1",
                        "origin_codes": "i",
                        "path": "(64605 64628 64630) 13335",
                        "status_codes": "*",
                        "weight": "0"
                        },
                        2: {
                        "locprf": "120",
                        "next_hop": "2a02:540:13::1",
                        "origin_codes": "i",
                        "path": "(64630) 13335",
                        "status_codes": "*>",
                        "weight": "500"
                        }
                    }
                    },
                    "2a02:540::/32": {
                    "index": {
                        1: {
                        "metric": "0",
                        "locprf": "120",
                        "next_hop": "2a02:540:13::1",
                        "origin_codes": "i",
                        "path": "(64630)",
                        "status_codes": "*>",
                        "weight": "500"
                        }
                    }
                    },
                    "2a0c:5cc0::/29": {
                    "index": {
                        1: {
                        "metric": "0",
                        "locprf": "120",
                        "next_hop": "2a02:540:5::1",
                        "origin_codes": "i",
                        "path": "(64605 64628 64603) 197648",
                        "status_codes": "*",
                        "weight": "0"
                        },
                        2: {
                        "metric": "0",
                        "locprf": "120",
                        "next_hop": "2a02:540:13::1",
                        "origin_codes": "i",
                        "path": "(64630 64601 64629 64628 64603) 197648",
                        "status_codes": "*>",
                        "weight": "500"
                        }
                    }
                    }
                },
                "processed_paths": 12,
                "processed_prefix": 9,
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