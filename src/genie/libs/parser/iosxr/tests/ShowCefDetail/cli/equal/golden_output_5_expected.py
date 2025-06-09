expected_output = {
    "vrf":{
        "default":{
            "address_family":{
                "ipv4":{
                    "prefix":{
                        "10.0.88.65/32":{
                            "LW-LDI-TS":{
                                "datetime":"Aug  5 15:15:08.465",
                                "load_distribution":{
                                    "distribution":"0",
                                    "refcount":115
                                },
                                "via_entries":{
                                    "0":{
                                        "dependencies":8,
                                        "path":{
                                            "nhid":"0x0",
                                            "nhid_hex":"0x5ad9dd40 0x0",
                                            "path_idx":0
                                        },
                                        "via_address":"10.10.32.141/32",
                                        "via_class":0,
                                        "via_interface":"TenGigE0/1/0/30.4",
                                        "weight":0
                                    }
                                }
                            },
                            "gateway_array":{
                                "LW-LDI":{
                                    "ptr":"0x5a3d0424",
                                    "refc":1,
                                    "sh_ldi":"0x5a7a24cc",
                                    "type":1
                                },
                                "backups":1,
                                "flags":{
                                    "flag_count":115,
                                    "flag_internal":"0x108401 (0x5a7a24cc) ext 0x0 (0x0)]",
                                    "flag_type":4
                                },
                                "reference_count":114,
                                "source_lsd":5,
                                "update":{
                                    "type_time":1,
                                    "updated_at":"Jul 31 08:57:27.801"
                                }
                            },
                            "internal":"0x1000001 0x0 (ptr 0x63f4ccd0) [1], 0x0 (0x5a3d0424), 0xa20 (0x5a76b9f4)",
                            "ldi_update_time":"Aug  5 15:15:08.465",
                            "length":32,
                            "precedence":"n/a",
                            "priority":3,
                            "traffic_index":0,
                            "updated":"Dec 23 10:08:20.329",
                            "version":2403689
                        }
                    }
                }
            }
        }
    }
}