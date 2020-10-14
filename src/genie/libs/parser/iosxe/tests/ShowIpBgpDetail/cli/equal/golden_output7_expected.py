expected_output = {
    "instance": {
        "default": {
            "vrf": {
                "sample_vrf": {
                    "address_family": {
                        "vpnv4": {
                            "prefixes": {
                                "111.222.333.0/24": {
                                    "available_path": "3",
                                    "best_path": "3",
                                    "index": {
                                        1: {
                                            "atomic_aggregate": True,
                                            "aggregated_by_as": "65251",
                                            "aggregated_by_address": "10.160.0.61",
                                            "community": "1:1 65100:101 65100:175 65100:500 65100:601 65151:65000 65351:1",
                                            "gateway": "10.105.6.80",
                                            "localpref": 100,
                                            "next_hop": "10.105.6.80",
                                            "next_hop_via": "vrf sample_vrf",
                                            "origin_codes": "i",
                                            "originator": "10.105.5.16",
                                            "recipient_pathid": "0",
                                            "refresh_epoch": 1,
                                            "route_info": "4210105002 4210105502 4210105001 4210105507 4210105007 4210105220 65000 65151 65501",
                                            "route_status": "received & used",
                                            "status_codes": "* ",
                                            "transfer_pathid": "0",
                                            "update_group": [1, 29, 35],
                                        },
                                        2: {
                                            "atomic_aggregate": True,
                                            "aggregated_by_as": "65251",
                                            "aggregated_by_address": "2001:db8:4::1",
                                            "community": "1:1 65100:101 65100:175 65100:500 65100:601 65151:65000 65351:1",
                                            "gateway": "10.105.5.1",
                                            "localpref": 100,
                                            "metric": 0,
                                            "next_hop": "10.105.5.1",
                                            "next_hop_igp_metric": "2",
                                            "next_hop_via": "vrf sample_vrf",
                                            "origin_codes": "i",
                                            "originator": "10.105.5.1",
                                            "recipient_pathid": "0",
                                            "refresh_epoch": 3,
                                            "route_info": "4210105002 4210105502 4210105001 4210105507 4210105007 4210105220 65000 65151 65501",
                                            "route_status": "received & used",
                                            "status_codes": "* ",
                                            "transfer_pathid": "0",
                                            "update_group": [1, 29, 35],
                                        },
                                        3: {
                                            "atomic_aggregate": True,
                                            "aggregated_by_as": "65251",
                                            "aggregated_by_address": "FE80:CD00:0:CDE:1257:0:211E:729C",
                                            "community": "1:1 65100:101 65100:175 65100:500 65100:601 65151:65000 65351:1",
                                            "gateway": "10.105.6.84",
                                            "localpref": 100,
                                            "next_hop": "10.105.6.84",
                                            "next_hop_via": "vrf sample_vrf",
                                            "origin_codes": "i",
                                            "originator": "10.105.5.17",
                                            "recipient_pathid": "0",
                                            "refresh_epoch": 1,
                                            "route_info": "4210105002 4210105502 4210105001 4210105507 4210105007 4210105220 65000 65151 65501",
                                            "route_status": "received & used",
                                            "status_codes": "*>",
                                            "transfer_pathid": "0x0",
                                            "update_group": [1, 29, 35],
                                        },
                                    },
                                    "paths": "3 available, best #3, table sample_vrf",
                                    "table_version": "1606506",
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
