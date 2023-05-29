expected_output = {
    "instance":{
        "default":{
            "vrf":{
                "green":{
                    "address_family":{
                        "vpnv4 unicast":{
                            "prefixes":{
                                "192.1.0.40/32":{
                                    "table_version":"12640",
                                    "available_path":"1",
                                    "best_path":"1",
                                    "paths":"1 available, best #1, table green",
                                    "index":{
                                        1:{
                                            "next_hop":"6:6:10::6",
                                            "gateway":"6::6",
                                            "originator":"6.6.6.6",
                                            "next_hop_igp_metric":"1",
                                            "next_hop_via":"default",
                                            "localpref":100,
                                            "metric":0,
                                            "origin_codes":"?",
                                            "status_codes":"*>",
                                            "refresh_epoch":1,
                                            "route_info":"Local",
                                            "imported_path_from":"[2][6.6.10.6:101][0][48][001094000030][32][192.1.0.40]/24 (global)",
                                            "ext_community":"RT:1:1 RT:100:101 MVPN AS:100:0.0.0.0 RTEP 6:6:10::6",
                                            "local_vxlan_vtep":{
                                                "vrf":"green",
                                                "vni":"50901",
                                                "local_router_mac":"A0B4.39CD.70FF",
                                                "encap":"8",
                                                "vtep_ip":"1:1:10::1"
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
