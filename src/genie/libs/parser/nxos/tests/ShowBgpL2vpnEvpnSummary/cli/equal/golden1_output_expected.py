expected_output = {
    "instance": {
        "default": {
            "vrf": {
                "default": {
                    "vrf_name_out": "default",
                    "address_family": {
                        "l2vpn evpn": {
                            "tableversion": 5549,
                            "configuredpeers": 2,
                            "capablepeers": 2,
                            "totalnetworks": 293,
                            "totalpaths": 442,
                            "memoryused": 72332,
                            "dampening": "disabled",
                            "numberattrs": 110,
                            "bytesattrs": 18920,
                            "numberpaths": 5,
                            "bytespaths": 54,
                            "numbercommunities": 0,
                            "bytescommunities": 0,
                            "numberclusterlist": 8,
                            "bytesclusterlist": 32,
                            "neighbor": {
                                "1.1.1.1": {
                                    "neighbor": "1.1.1.1",
                                    "remoteas": 4444444444,
                                    "version": 4,
                                    "msgrecvd": 121842,
                                    "msgsent": 120925,
                                    "neighbortableversion": 5549,
                                    "inq": 0,
                                    "outq": 0,
                                    "time": "11w6d",
                                    "prefixreceived": 142,
                                    "state": "established"
                                },
                                "1.1.1.2": {
                                    "neighbor": "1.1.1.2",
                                    "remoteas": 4444444444,
                                    "version": 4,
                                    "msgrecvd": 118316,
                                    "msgsent": 117369,
                                    "neighbortableversion": 5549,
                                    "inq": 0,
                                    "outq": 0,
                                    "time": "3w4d",
                                    "prefixreceived": 142,
                                    "state": "established"
                                }
                            }
                        }
                    },
                    "vrf_router_id": "4.4.4.4",
                    "vrf_local_as": 4444444444
                }
            }
        }
    }
}