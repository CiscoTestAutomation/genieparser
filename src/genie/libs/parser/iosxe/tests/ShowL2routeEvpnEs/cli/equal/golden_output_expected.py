expected_output = {
    "esi": {
        "0010.1010.1010.1010.1010": {
            "orig_rtr": {
                "10.0.0.12": {
                    "producer": "BGP",
                    "next_hop": "10.0.0.12",
                    "nfn_bitmap": "0",
                    "l2vni_id": 0
                },
                "10.0.0.11": {
                    "producer": "L2VPN",
                    "next_hop": "Port-channel2",
                    "nfn_bitmap": "0"
                }
            }
        },
        "0100.451D.E5B3.8000.0100": {
            "orig_rtr": {
                "10.0.0.12": {
                    "producer": "BGP",
                    "next_hop": "10.0.0.12",
                    "nfn_bitmap": "0",
                    "l2vni_id": 0
                },
                "10.0.0.11": {
                    "producer": "L2VPN",
                    "next_hop": "Port-channel1",
                    "nfn_bitmap": "0"
                }
            }
        },
        "012C.4F52.057D.C000.0300": {
            "orig_rtr": {
                "10.0.0.12": {
                    "producer": "BGP",
                    "next_hop": "10.0.0.12",
                    "nfn_bitmap": "0",
                    "l2vni_id": 0
                },
                "10.0.0.11": {
                    "producer": "L2VPN",
                    "next_hop": "Port-channel3",
                    "nfn_bitmap": "0"
                }
            }
        }
    }
}
