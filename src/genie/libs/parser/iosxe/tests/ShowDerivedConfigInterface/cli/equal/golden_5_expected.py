expected_output = {
    "derived_config": {
        "nve1": {
            "source_interface": "Loopback0",
            "host_reachability_protocol": "bgp",
            "vxlan_encapsulation": {
                "encapsulation_type": "dual-stack",
                "dual_stack_ip": "prefer-ipv6"
            },
            "member_vni": {
                "20010": {
                    "mcast_group_ipv6": "FF0E::A"
                },
                "2000201": {
                    "ingress_replication": {
                        "ir_enabled": True
                    }
                },
                "2000401": {
                    "mcast_group_ip": "239.4.0.145",
                    "mcast_group_ipv6": "FF1E::91"
                },
                "30010": {
                    "vrf": "GETCONFIG"
                }
            }
        }
    }   
}
