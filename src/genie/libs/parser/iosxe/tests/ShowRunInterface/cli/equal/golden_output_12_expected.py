expected_output = {
    "interfaces": {
        "Port-channel20": {
            "description": "distacc Te1/1/1, Te2/1/1",
            "switchport_trunk_vlans": "9,51",
            "switchport_mode": "trunk",
            "ip_arp_inspection_trust": True,
            "ip_dhcp_snooping_trust": True,
        },
        "GigabitEthernet0/0": {
            "vrf": "Mgmt-vrf",
            "shutdown": True,
            "negotiation_auto": True,
        },
        "GigabitEthernet1/0/1": {
            "description": "unknown DA",
            "switchport_access_vlan": "51",
            "switchport_mode": "access",
            "spanning_tree_portfast": True,
            "ip_dhcp_snooping_limit_rate": "10",
        },
        "GigabitEthernet1/0/2": {
            "description": "DA1202B_21_13 ap-100",
            "switchport_access_vlan": "51",
            "switchport_mode": "access",
            "spanning_tree_portfast": True,
            "ip_dhcp_snooping_limit_rate": "10",
        },
    }
}
