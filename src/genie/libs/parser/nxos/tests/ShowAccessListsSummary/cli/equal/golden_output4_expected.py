expected_output = {
    "acl": {
        "199": {
            "total_aces_configured": 5
        },
        "98": {
            "total_aces_configured": 9
        },
        "99": {
            "total_aces_configured": 2
        },
        "COMMENT09": {
            "total_aces_configured": 1
        },
        "COMMENT10": {
            "total_aces_configured": 1
        },
                "COMMENT11": {
            "total_aces_configured": 1
        }
    },
    "attachment_points": {
        "VTY": {
            "interface_id": "VTY",
            "ingress": {
                "199": {
                    "total_aces_configured": 5,
                    "active": True,
                    "name": "199"
                }
            }
        },
        "Ethernetxx/x.xxx": {
            "interface_id": "Ethernetxx/x.xxx",
            "egress": {
                "COMMENT09": {
                    "total_aces_configured": 1,
                    "active": True,
                    "name": "COMMENT09",
                    "type": "Router ACL"
                }
            }
        }
    }

}

