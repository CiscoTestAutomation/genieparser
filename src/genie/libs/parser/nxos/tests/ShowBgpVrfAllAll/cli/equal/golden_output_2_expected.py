

expected_output = {
    "vrf": {
        "default": {
           "address_family": {
                "l2vpn evpn RD 10.4.1.2:32868": {
                     "route_distinguisher": "10.4.1.2:32868",
                     "local_router_id": "10.4.1.2",
                     "prefixes": {
                          "[2]:[0]:[0]:[48]:[0000.19ff.f320]:[0]:[0.0.0.0]/216": {
                               "index": {
                                    1: {
                                         "weight": 32768,
                                         "next_hop": "10.9.1.1",
                                         "localprf": 100,
                                         "status_codes": "*>",
                                         "path_type": "l",
                                         "origin_codes": "i"
                                    }
                               }
                          },
                          "[2]:[0]:[0]:[48]:[0000.19ff.f320]:[32]:[10.220.20.44]/272": {
                               "index": {
                                    1: {
                                         "weight": 32768,
                                         "next_hop": "10.9.1.1",
                                         "localprf": 100,
                                         "status_codes": "*>",
                                         "path_type": "l",
                                         "origin_codes": "i"
                                    }
                               }
                          },
                          "[2]:[0]:[0]:[48]:[0000.19ff.f320]:[128]:[2001:db8:183c:4005::44]/368": {
                               "index": {
                                    1: {
                                         "weight": 32768,
                                         "next_hop": "10.9.1.1",
                                         "localprf": 100,
                                         "status_codes": "*>",
                                         "path_type": "l",
                                         "origin_codes": "i"
                                    }
                               }
                          }
                     },
                     "default_vrf": "L2",
                     "bgp_table_version": 381
                },
                "l2vpn evpn": {
                     "local_router_id": "10.4.1.2",
                     "bgp_table_version": 381
                }
           }
        }
    }
}
