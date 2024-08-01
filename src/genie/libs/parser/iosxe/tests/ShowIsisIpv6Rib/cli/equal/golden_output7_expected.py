expected_output = {
    "tag": {
        "1": {
            "rib_root": "local RIB",
            "flex_algo": {
                132: {
                    "prefix": {
                        "FCCC:F132:C1::/48": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "local_router": True,
                            "pfx_algo": 132,
                            'src_rtr_id': '333::333',
                            "via": {
                                "FE80::A8BB:CCFF:FE01:4721": {
                                    "type": {
                                        "L1": {
                                            "metric": 10,
                                            "tag": "0",
                                            "interface": "Ethernet1/2",
                                            "filtered_out": False,
                                            'installed': True,
                                            "repair_path": {
                                                "attributes": {
                                                    "DS": True,
                                                    "LC": True,
                                                    "NP": False,
                                                    "PP": False,
                                                    "SR": True
                                                },
                                                "nh_addr": "FE80::A8BB:CCFF:FE01:AF10",
                                                "interface": "Ethernet0/0",
                                                "metric": 30,
                                                "lfa_type": "TI-LFA link-protecting",
                                                "srv6_fwid": 25165871,
                                                "nodes": {
                                                    "iolR5": {
                                                        "pq_node": "P",
                                                        "sid": "FCCC:F132:E1::",
                                                        'srv6_sid_behavior': 'uN (PSP/USD)'
                                                    }
                                                },
                                                "repair_source": "iolR3",
                                                "metric_to_prefix": 40
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
}
