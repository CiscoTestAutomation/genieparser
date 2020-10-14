expected_output = {
    "test": {
        "statements": {
            "10": {
                "actions": {
                    "route_disposition": "permit",
                    "set_next_hop_self": False,
                    "set_next_hop_v6": ["2001:DB8:1::1", "2001:DB8:2::1"],
                    "set_tag": "10",
                },
                "conditions": {
                    "match_interface": "GigabitEthernet1",
                    "match_nexthop_in_v6": ["test"],
                },
            }
        }
    },
    "test2": {
        "statements": {
            "10": {
                "actions": {
                    "route_disposition": "permit",
                    "set_community": "6553700",
                    "set_community_delete": "test",
                    "set_ext_community_rt": ["100:10", "100:100", "200:200"],
                    "set_ext_community_rt_additive": True,
                    "set_ext_community_soo": "100:10",
                    "set_ext_community_vpn": "100:100",
                    "set_local_pref": 111,
                    "set_metric_type": "external",
                    "set_metric": 100,
                    "set_next_hop_self": True,
                    "set_next_hop": ["10.4.1.1", "10.16.2.2"],
                    "set_next_hop_v6": ["2001:DB8:1::1", "2001:DB8:2::1"],
                    "set_route_origin": "incomplete",
                    "set_tag": "10",
                },
                "conditions": {"match_med_eq": 100},
            },
            "20": {
                "actions": {
                    "route_disposition": "permit",
                    "set_metric": -20,
                    "set_ospf_metric_type": "type-1",
                    "set_next_hop": ["10.36.3.3"],
                    "set_next_hop_self": False,
                    "set_next_hop_v6": ["2001:DB8:3::1"],
                    "set_route_origin": "igp",
                },
                "conditions": {
                    "match_as_path_list": "100",
                    "match_community_list": "test",
                    "match_ext_community_list": "test",
                    "match_prefix_list": "test test2",
                    "match_level_eq": "level-1-2",
                    "match_interface": "GigabitEthernet1 GigabitEthernet2",
                },
            },
        }
    },
}
