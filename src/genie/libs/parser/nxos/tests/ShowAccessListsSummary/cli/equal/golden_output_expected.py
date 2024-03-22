expected_output = {
    "acl": {
        "acl_name": {
            "total_aces_configured": 1
        },
        "ipv4_acl": {
            "total_aces_configured": 3
        },
        "ipv4_ext": {
            "total_aces_configured": 0
        },
        "ipv6_acl": {
            "total_aces_configured": 3
        },
        "ipv6_acl2": {
            "total_aces_configured": 1
        },
        "mac_acl": {
            "total_aces_configured": 5
        },
        "sl_def_acl": {
            "Statistics": "enabled",
            "total_aces_configured": 4
        },
        "test22": {
            "total_aces_configured": 3
        }
    },
    "attachment_points": {
        "Ethernet1/1": {
            "interface_id": "Ethernet1/1",
            "egress": {
                "ipv4_acl": {
                    "total_aces_configured": 3,
                    "active": True,
                    "name": "ipv4_acl",
                    "type": "Router ACL"
                },
                "ipv6_acl2": {
                    "total_aces_configured": 1,
                    "active": True,
                    "name": "ipv6_acl2",
                    "type": "Router ACL"
                }
            },
            "ingress": {
                "ipv6_acl": {
                    "total_aces_configured": 3,
                    "active": True,
                    "name": "ipv6_acl",
                    "type": "Router ACL"
                },
                "mac_acl": {
                    "total_aces_configured": 5,
                    "active": True,
                    "name": "mac_acl",
                    "type": "Port ACL"
                },
                "test22": {
                    "total_aces_configured": 3,
                    "active": True,
                    "name": "test22",
                    "type": "Router ACL"
                }
            }
        }
    }
}