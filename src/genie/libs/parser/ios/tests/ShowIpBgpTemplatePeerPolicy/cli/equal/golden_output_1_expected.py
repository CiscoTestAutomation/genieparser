expected_output = {
    "peer_policy": {
        "PEER-POLICY": {
            "local_policies": "0x8002069C603",
            "inherited_polices": "0x0",
            "local_disable_policies": "0x0",
            "inherited_disable_polices": "0x0",
            "default_originate": True,
            "allowas_in": True,
            "allowas_in_as_number": 9,
            "default_originate_route_map": "test",
            "route_map_name_in": "test",
            "route_map_name_out": "test2",
            "maximum_prefix_max_prefix_no": 5555,
            "maximum_prefix_restart": 300,
            "next_hop_self": True,
            "route_reflector_client": True,
            "send_community": "both",
            "soft_reconfiguration": True,
            "index": 1,
            "inherited_policies": {"as_override": True, "soo": "SoO:100:100"},
        },
        "PEER-POLICY2": {
            "local_policies": "0x200000",
            "inherited_polices": "0x0",
            "local_disable_policies": "0x0",
            "inherited_disable_polices": "0x0",
            "allowas_in": True,
            "allowas_in_as_number": 10,
            "index": 2,
        },
    }
}
