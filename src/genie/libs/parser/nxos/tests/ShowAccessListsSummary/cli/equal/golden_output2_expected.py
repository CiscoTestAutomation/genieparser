expected_output = {
    "acl": {
        "23": {
            "total_aces_configured": 13
        },
        "Deny-any": {
            "total_aces_configured": 1
        },
        "FROM_AD_LAB_ESX": {
            "total_aces_configured": 17
        },
        "TO_AD_LAB_ESX": {
            "total_aces_configured": 17
        },
        "__urpf_v4_acl__": {
            "total_aces_configured": 1
        },
        "__urpf_v6_acl__": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-bgp": {
            "total_aces_configured": 2
        },
        "copp-system-p-acl-bgp6": {
            "total_aces_configured": 2
        },
        "copp-system-p-acl-cts": {
            "total_aces_configured": 2
        },
        "copp-system-p-acl-dhcp": {
            "total_aces_configured": 2
        },
        "copp-system-p-acl-dhcp-relay-response": {
            "total_aces_configured": 2
        },
        "copp-system-p-acl-dhcp6": {
            "total_aces_configured": 2
        },
        "copp-system-p-acl-dhcp6-relay-response": {
            "total_aces_configured": 2
        },
        "copp-system-p-acl-eigrp": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-eigrp6": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-ftp": {
            "total_aces_configured": 4
        },
        "copp-system-p-acl-glbp": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-hsrp": {
            "total_aces_configured": 2
        },
        "copp-system-p-acl-hsrp6": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-http-response": {
            "total_aces_configured": 2
        },
        "copp-system-p-acl-http6-response": {
            "total_aces_configured": 2
        },
        "copp-system-p-acl-icmp": {
            "total_aces_configured": 2
        },
        "copp-system-p-acl-icmp6": {
            "total_aces_configured": 2
        },
        "copp-system-p-acl-igmp": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-lisp": {
            "total_aces_configured": 2
        },
        "copp-system-p-acl-lisp6": {
            "total_aces_configured": 2
        },
        "copp-system-p-acl-mac-cdp-udld-vtp": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-mac-cfsoe": {
            "total_aces_configured": 2
        },
        "copp-system-p-acl-mac-dot1x": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-mac-fabricpath-isis": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-mac-fcoe": {
            "total_aces_configured": 2
        },
        "copp-system-p-acl-mac-flow-control": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-mac-l2-tunnel": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-mac-l2pt": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-mac-l3-isis": {
            "total_aces_configured": 3
        },
        "copp-system-p-acl-mac-lacp": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-mac-lldp": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-mac-mvrp": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-mac-otv-isis": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-mac-sdp-srp": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-mac-stp": {
            "total_aces_configured": 2
        },
        "copp-system-p-acl-mac-undesirable": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-mld": {
            "total_aces_configured": 4
        },
        "copp-system-p-acl-mpls-ldp": {
            "total_aces_configured": 3
        },
        "copp-system-p-acl-mpls-oam": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-mpls-rsvp": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-msdp": {
            "total_aces_configured": 2
        },
        "copp-system-p-acl-ndp": {
            "total_aces_configured": 5
        },
        "copp-system-p-acl-ntp": {
            "total_aces_configured": 2
        },
        "copp-system-p-acl-ntp6": {
            "total_aces_configured": 2
        },
        "copp-system-p-acl-ospf": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-ospf6": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-otv-as": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-pim": {
            "total_aces_configured": 3
        },
        "copp-system-p-acl-pim-mdt-join": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-pim-reg": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-pim6": {
            "total_aces_configured": 2
        },
        "copp-system-p-acl-pim6-reg": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-radius": {
            "total_aces_configured": 8
        },
        "copp-system-p-acl-radius6": {
            "total_aces_configured": 8
        },
        "copp-system-p-acl-rip": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-rip6": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-rise": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-rise6": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-sftp": {
            "total_aces_configured": 2
        },
        "copp-system-p-acl-smtp-response": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-smtp6-response": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-snmp": {
            "total_aces_configured": 2
        },
        "copp-system-p-acl-ssh": {
            "total_aces_configured": 2
        },
        "copp-system-p-acl-ssh6": {
            "total_aces_configured": 2
        },
        "copp-system-p-acl-tacacs": {
            "total_aces_configured": 2
        },
        "copp-system-p-acl-tacacs6": {
            "total_aces_configured": 2
        },
        "copp-system-p-acl-telnet": {
            "total_aces_configured": 4
        },
        "copp-system-p-acl-telnet6": {
            "total_aces_configured": 4
        },
        "copp-system-p-acl-tftp": {
            "total_aces_configured": 4
        },
        "copp-system-p-acl-tftp6": {
            "total_aces_configured": 4
        },
        "copp-system-p-acl-traceroute": {
            "total_aces_configured": 3
        },
        "copp-system-p-acl-undesirable": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-vpc": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-vrrp": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-vrrp6": {
            "total_aces_configured": 1
        },
        "copp-system-p-acl-wccp": {
            "total_aces_configured": 1
        },
        "ctrlNet": {
            "total_aces_configured": 1
        },
        "jtienm": {
            "total_aces_configured": 3
        },
        "jtinms": {
            "total_aces_configured": 0
        },
        "jtisnmp": {
            "total_aces_configured": 11
        },
        "sl_def_acl": {
            "Statistics": "enabled",
            "total_aces_configured": 4
        }
    },
    "attachment_points": {
        "VTY": {
            "interface_id": "VTY",
            "ingress": {
                "23": {
                    "total_aces_configured": 13,
                    "active": True,
                    "name": "23"
                }
            }
        },
        "Vlan125": {
            "interface_id": "Vlan125",
            "ingress": {
                "FROM_AD_LAB_ESX": {
                    "total_aces_configured": 17,
                    "active": True,
                    "name": "FROM_AD_LAB_ESX",
                    "type": "Router ACL"
                }
            },
            "egress": {
                "TO_AD_LAB_ESX": {
                    "total_aces_configured": 17,
                    "active": True,
                    "name": "TO_AD_LAB_ESX",
                    "type": "Router ACL"
                }
            }
        }
    }
}