expected_output = {
    "interfaces":{
        "TenGigabitEthernet1/0/13":{
            "description":"EEDGE-MD",
            "switchport_access_vlan":"881",
            "switchport_mode":"access",
            "authentication_periodic":True,
            "mab":True,
            "trust_device":"cisco-phone",
            "dot1x_pae_authenticator":True,
            "ipv6_destination_guard_attach_policy":"Univ-v6-IPDG-Policy1",
            "ipv6_source_guard_attach_policy":"Univ-v6-IPSG-Policy2",
            "keepalive":False,
            "spanning_tree_portfast":True,
            "input_policy":"AutoQos-4.0-CiscoPhone-Input-Policy",
            "output_policy":"AutoQos-4.0-Output-Policy",
            "access_session": "closed",
            "access_session_host_mode": "multi-domain",
            "access_session_port_control": "auto"
        }
    }
}
