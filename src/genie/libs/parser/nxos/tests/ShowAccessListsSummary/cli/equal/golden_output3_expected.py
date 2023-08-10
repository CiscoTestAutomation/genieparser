expected_output = {
    "acl": {
        "ALLOW-MGT": {
            "total_aces_configured": 14
        },
        "CORP-CCRPRIV-INOUT": {
            "total_aces_configured": 8
        },
        "L3-UPG-MEDIUM-TRUST": {
            "Statistics": "enabled",
            "Fragments": "permit-all",
            "total_aces_configured": 10
        },
        "L3-UPG-UPG-HIGH-TRUST": {
            "Statistics": "enabled",
            "Fragments": "permit-all",
            "total_aces_configured": 10
        }
    },
    "attachment_points": {
        "VTY": {
            "interface_id": "VTY",
            "ingress": {
                "ALLOW-MGT": {
                    "total_aces_configured": 14,
                    "active": True,
                    "name": "ALLOW-MGT"
                }
            }
        },
        "Vlan2007": {
            "interface_id": "Vlan2007",
            "ingress": {
                "CORP-CCRPRIV-INOUT": {
                    "total_aces_configured": 8,
                    "active": True,
                    "name": "CORP-CCRPRIV-INOUT",
                    "type": "Router ACL"
                }
            },
            "egress": {
                "CORP-CCRPRIV-INOUT": {
                    "total_aces_configured": 8,
                    "active": True,
                    "name": "CORP-CCRPRIV-INOUT",
                    "type": "Router ACL"
                }
            }
        },
        "Vlan2102": {
            "interface_id": "Vlan2102",
            "ingress": {
                "CORP-CCRPRIV-INOUT": {
                    "total_aces_configured": 8,
                    "active": True,
                    "name": "CORP-CCRPRIV-INOUT",
                    "type": "Router ACL"
                }
            },
            "egress": {
                "CORP-CCRPRIV-INOUT": {
                    "total_aces_configured": 8,
                    "active": True,
                    "name": "CORP-CCRPRIV-INOUT",
                    "type": "Router ACL"
                }
            }
        },
        "Vlan2471": {
            "interface_id": "Vlan2471",
            "egress": {
                "L3-UPG-MEDIUM-TRUST": {
                    "total_aces_configured": 10,
                    "active": True,
                    "name": "L3-UPG-MEDIUM-TRUST",
                    "type": "Router ACL"
                }
            }
        },
        "Vlan2473": {
            "interface_id": "Vlan2473",
            "egress": {
                "L3-UPG-MEDIUM-TRUST": {
                    "total_aces_configured": 10,
                    "active": True,
                    "name": "L3-UPG-MEDIUM-TRUST",
                    "type": "Router ACL"
                }
            }
        },
        "Vlan2472": {
            "interface_id": "Vlan2472",
            "egress": {
                "L3-UPG-UPG-HIGH-TRUST": {
                    "total_aces_configured": 10,
                    "active": True,
                    "name": "L3-UPG-UPG-HIGH-TRUST",
                    "type": "Router ACL"
                }
            }
        },
        "Vlan2474": {
            "interface_id": "Vlan2474",
            "egress": {
                "L3-UPG-UPG-HIGH-TRUST": {
                    "total_aces_configured": 10,
                    "active": True,
                    "name": "L3-UPG-UPG-HIGH-TRUST",
                    "type": "Router ACL"
                }
            }
        }
    }
}