expected_output = {
    "ipv6_add": {
        "2001:10:10:1::/64": {
            "ipv6route_id": "0x574a415e0958",
            "obj_name": "LOOKUP",
            "obj_id": "0x30",
            "table_id": 0,
            "da": 0,
            "last_act": 0,
            "last_rc": 0,
            "state": "success",
            "flags": "0x800",
            "device": 0,
            "lspa_rec": 0,
            "api_type": 3,
            "sdk": {
                "is_host": 0,
                "l3_dest": "0x787c938fc190",
                "l3_dest_type": "la_next_hop_base",
                "l3_dest_oid": 3995,
                "vrf_gid": 0,
                "vrf_oid": "0x3b2",
            },
            "sdk_object": {
                "sdk_oid": "0xf9b",
                "devid": 1,
                "asic": 0,
                "nexthop_oid": "0xf9b",
                "nexthop_dev": 1,
                "nexthop_gid": 12,
                "macaddr": "4e41.5000.0114",
                "nh_type": "normal(0)",
                "sdk_outgoing_port_oid": "0xdab",
                "porttype": "l3ac(70)",
            },
            "lookup": {
                "obj_id": 48,
                "table_id": 2,
                "proto": 1,
                "state": "success",
            },
        }
    }
}
