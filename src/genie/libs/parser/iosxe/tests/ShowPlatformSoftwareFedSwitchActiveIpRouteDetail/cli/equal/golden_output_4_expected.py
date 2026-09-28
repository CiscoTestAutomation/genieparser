expected_output = {
    "ipv4_add": {
        "10.10.1.0/24": {
            "ipv4route_id": "0x574a415e21e8",
            "obj_name": "LOOKUP",
            "obj_id": "0x3a",
            "tblid": 0,
            "da": 0,
            "state": "success",
            "flags": "0x800",
            "device": 0,
            "lspa_rec": 0,
            "api_type": 3,
            "sdk": {
                "is_host": 0,
                "l3_dest": "0x787c93851a40",
                "l3_dest_type": "la_next_hop_base",
                "l3_dest_oid": 3989,
                "vrf_gid": 0,
                "vrf_oid": "0x3b2",
            },
            "sdk_object": {
                "sdk_oid": "0xf95",
                "devid": 1,
                "asic": 0,
                "nexthop_oid": "0xf95",
                "nexthop_dev": 1,
                "nexthop_gid": 11,
                "macaddr": "4e41.5000.0114",
                "nh_type": "normal(0)",
                "sdk_outgoing_port_oid": "0xdad",
                "porttype": "l3ac(70)",
            },
            "lookup": {
                "obj_id": 58,
                "table_id": 4,
                "proto": 0,
                "state": "success",
            },
        }
    }
}
