expected_output = {
    "instance":{
        "default":{
            "vrf":{
                "default":{
                    "address_family":{
                        "":{
                            "prefixes":{
                                "1.1.1.1/32":{
                                    "table_version":"162",
                                    "available_path":"4",
                                    "best_path":"4",
                                    "paths":"4 available, best #4, table default",
                                    "index":{
                                        1:{
                                            "next_hop":"10.10.10.1",
                                            "gateway":"10.10.10.1",
                                            "originator":"192.168.1.1",
                                            "multipath":"multipath",
                                            "localpref":100,
                                            "origin_codes":"i",
                                            "status_codes":"* ",
                                            "refresh_epoch":2,
                                            "route_info":"65000 65001",
                                            "route_status":"received & used",
                                            "community":"1:1",
                                            "recipient_pathid":"0",
                                            "transfer_pathid":"0"
                                        },
                                        2:{
                                            "next_hop":"10.10.20.1",
                                            "gateway":"10.10.20.1",
                                            "originator":"192.168.1.2",
                                            "multipath":"multipath",
                                            "localpref":100,
                                            "origin_codes":"i",
                                            "status_codes":"* ",
                                            "refresh_epoch":2,
                                            "route_info":"65000 65001",
                                            "route_status":"received & used",
                                            "community":"1:1",
                                            "recipient_pathid":"0",
                                            "transfer_pathid":"0"
                                        },
                                        3:{
                                            "next_hop":"10.10.30.1",
                                            "gateway":"10.10.30.1",
                                            "originator":"192.168.1.3",
                                            "multipath":"multipath(oldest)",
                                            "localpref":100,
                                            "origin_codes":"i",
                                            "status_codes":"* ",
                                            "refresh_epoch":2,
                                            "route_info":"65000 65001",
                                            "route_status":"received & used",
                                            "community":"1:1",
                                            "recipient_pathid":"0",
                                            "transfer_pathid":"0"
                                        },
                                        4:{
                                            "next_hop":"10.10.40.1",
                                            "gateway":"10.10.40.1",
                                            "originator":"192.168.1.4",
                                            "multipath":"multipath",
                                            "localpref":100,
                                            "origin_codes":"i",
                                            "status_codes":"*>",
                                            "refresh_epoch":2,
                                            "route_info":"65000 65001",
                                            "route_status":"received & used",
                                            "community":"1:1",
                                            "recipient_pathid":"0",
                                            "transfer_pathid":"0x0"
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