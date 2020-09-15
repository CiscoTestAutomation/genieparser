expected_output = {
    "instance": {
        "default": {
            "vrf": {
                "EVPN-BGP-Table": {
                    "address_family": {
                        "vpnv4 unicast RD 65535:1": {
                            "default_vrf": "evpn1",
                            "prefixes": {
                                "10.1.1.0/17": {
                                    "available_path": "1",
                                    "best_path": "1",
                                    "index": {
                                        1: {
                                            "evpn": {
                                                "encap": "8",
                                                "evpn_esi": "00000000000000000000",
                                                "ext_community": "RT:65535:1",
                                                "gateway_address": "0.0.0.0",
                                                "label": 30000,
                                                "local_vtep": "10.21.33.33",
                                                "router_mac": "MAC:001E.7AFF.FCD2",
                                            },
                                            "gateway": "0.0.0.0",
                                            "inaccessible": False,
                                            "localpref": 100,
                                            "metric": 0,
                                            "next_hop": "0.0.0.0",
                                            "next_hop_via": "vrf evpn1",
                                            "origin_codes": "?",
                                            "originator": "10.21.33.33",
                                            "recipient_pathid": "0",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "imported_path_from": "base",
                                            "status_codes": "*>",
                                            "transfer_pathid": "0x0",
                                            "weight": "32768",
                                        }
                                    },
                                    "paths": "1 available, best #1, table EVPN-BGP-Table",
                                    "table_version": "4",
                                },
                                "10.36.3.0/17": {
                                    "available_path": "2",
                                    "best_path": "1",
                                    "index": {
                                        1: {
                                            "evpn": {
                                                "encap": "8",
                                                "evpn_esi": "00000000000000000000",
                                                "ext_community": "RT:65535:1",
                                                "gateway_address": "0.0.0.0",
                                                "label": 30000,
                                                "local_vtep": "10.21.33.33",
                                                "router_mac": "MAC:001E.7AFF.FCD2",
                                            },
                                            "gateway": "0.0.0.0",
                                            "inaccessible": False,
                                            "localpref": 100,
                                            "metric": 0,
                                            "next_hop": "0.0.0.0",
                                            "next_hop_via": "vrf evpn1",
                                            "origin_codes": "?",
                                            "originator": "10.21.33.33",
                                            "recipient_pathid": "0",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "imported_path_from": "base",
                                            "status_codes": "*>",
                                            "transfer_pathid": "0x0",
                                            "weight": "32768",
                                        },
                                        2: {
                                            "evpn": {
                                                "encap": "8",
                                                "evpn_esi": "00000000000000000000",
                                                "ext_community": "RT:65535:1",
                                                "gateway_address": "0.0.0.0",
                                                "label": 30000,
                                                "local_vtep": "10.21.33.33",
                                                "router_mac": "MAC:001E.7AFF.FCD2",
                                            },
                                            "gateway": "10.36.3.254",
                                            "inaccessible": False,
                                            "localpref": 100,
                                            "metric": 0,
                                            "next_hop": "10.36.3.254",
                                            "next_hop_via": "vrf evpn1",
                                            "origin_codes": "?",
                                            "originator": "10.21.33.22",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0",
                                            "refresh_epoch": 1,
                                            "route_info": "65530",
                                            "imported_path_from": "base",
                                            "status_codes": "* ",
                                        },
                                    },
                                    "paths": "2 available, best #1, table EVPN-BGP-Table",
                                    "table_version": "3",
                                },
                            },
                            "route_distinguisher": "65535:1",
                        }
                    }
                },
                "evpn1": {
                    "address_family": {
                        "vpnv4 unicast RD 65535:1": {
                            "default_vrf": "evpn1",
                            "prefixes": {
                                "10.1.1.0/24": {
                                    "available_path": "1",
                                    "best_path": "1",
                                    "index": {
                                        1: {
                                            "gateway": "0.0.0.0",
                                            "inaccessible": False,
                                            "local_vxlan_vtep": {
                                                "bdi": "BDI200",
                                                "encap": "8",
                                                "local_router_mac": "001E.7AFF.FCD2",
                                                "vni": "30000",
                                                "vrf": "evpn1",
                                                "vtep_ip": "10.21.33.33",
                                            },
                                            "localpref": 100,
                                            "metric": 0,
                                            "next_hop": "0.0.0.0",
                                            "next_hop_via": "vrf evpn1",
                                            "origin_codes": "?",
                                            "originator": "10.21.33.33",
                                            "recipient_pathid": "0",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "status_codes": "*>",
                                            "transfer_pathid": "0x0",
                                            "update_group": 1,
                                            "weight": "32768",
                                        }
                                    },
                                    "paths": "1 available, best #1, table evpn1",
                                    "table_version": "5",
                                },
                                "10.36.3.0/24": {
                                    "available_path": "2",
                                    "best_path": "2",
                                    "index": {
                                        1: {
                                            "gateway": "10.36.3.254",
                                            "inaccessible": False,
                                            "local_vxlan_vtep": {
                                                "bdi": "BDI200",
                                                "encap": "8",
                                                "local_router_mac": "001E.7AFF.FCD2",
                                                "vni": "30000",
                                                "vrf": "evpn1",
                                                "vtep_ip": "10.21.33.33",
                                            },
                                            "localpref": 100,
                                            "metric": 0,
                                            "next_hop": "10.36.3.254",
                                            "next_hop_via": "vrf evpn1",
                                            "origin_codes": "?",
                                            "originator": "10.21.33.22",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0",
                                            "refresh_epoch": 1,
                                            "route_info": "65530",
                                            "status_codes": "* ",
                                            "update_group": 1,
                                        },
                                        2: {
                                            "gateway": "0.0.0.0",
                                            "inaccessible": False,
                                            "local_vxlan_vtep": {
                                                "bdi": "BDI200",
                                                "encap": "8",
                                                "local_router_mac": "001E.7AFF.FCD2",
                                                "vni": "30000",
                                                "vrf": "evpn1",
                                                "vtep_ip": "10.21.33.33",
                                            },
                                            "localpref": 100,
                                            "metric": 0,
                                            "next_hop": "0.0.0.0",
                                            "next_hop_via": "vrf evpn1",
                                            "origin_codes": "?",
                                            "originator": "10.21.33.33",
                                            "recipient_pathid": "0",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "status_codes": "*>",
                                            "transfer_pathid": "0x0",
                                            "update_group": 1,
                                            "weight": "32768",
                                        },
                                    },
                                    "paths": "2 available, best #2, table evpn1",
                                    "table_version": "4",
                                },
                            },
                            "route_distinguisher": "65535:1",
                        }
                    }
                },
            }
        }
    }
}
