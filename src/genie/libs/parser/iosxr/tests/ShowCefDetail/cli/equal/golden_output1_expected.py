expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "prefix": {
                        "10.255.255.224/32": {
                            "version": 31880810,
                            "internal": "0x1000001 0x30 (ptr 0x79189280) [1], 0x0 (0x0), 0x0 (0x0)",
                            "drop": "adjacency",
                            "updated": "Mar 20 11:11:27.890",
                            "length": 32,
                            "traffic_index": 0,
                            "precedence": "n/a",
                            "priority": 3,
                            "gateway_array": {
                                "reference_count": 1,
                                "source_rib": 7,
                                "backups": 0,
                                "flags": {
                                    "flag_count": 1,
                                    "flag_type": 3,
                                    "flag_internal": "0xc8401 (0x78399948) ext 0x0 (0x0)]",
                                },
                                "LW-LDI": {
                                    "type": 0,
                                    "refc": 0,
                                    "ptr": "0x0",
                                    "sh_ldi": "0x0",
                                },
                                "update": {
                                    "type_time": 3,
                                    "updated_at": "Mar 20 14:47:43.154",
                                },
                            },
                            "ldi_update_time": "Mar 20 11:11:27.890",
                            "LW-LDI-TS": {
                                "datetime": "Mar 20 11:11:27.890",
                                "via_entries": {
                                    "0": {
                                        "via_address": "1.3.2.1/32",
                                        "dependencies": 0,
                                        "via_flags": "recursive",
                                        "path": {"path_idx": 0, "nhid": "0x0", "nhid_hex": "0x781b57c8 0x0"},
                                    }
                                },
                                "load_distribution": {
                                    "distribution": '0',
                                    "refcount": 1,
                                    "0": {
                                        "hash": 0,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "drop",
                                    }
                                },
                            },
                        }
                    }
                }
            }
        }
    }
}
