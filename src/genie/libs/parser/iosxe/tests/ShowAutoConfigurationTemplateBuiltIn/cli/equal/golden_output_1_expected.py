expected_output = {
    'template': {
        'IP_CAMERA_INTERFACE_TEMPLATE': {
            'definition': [
                "switchport mode access",
                "switchport block unicast",
                "spanning-tree portfast",
                "switchport port-security",
                "spanning-tree bpduguard enable", 
                "service-policy input AutoConf-4.0-Trust-Dscp-Input-Policy",
                "service-policy output AutoConf-4.0-Output-Policy"
            ]
        },
        'DMP_INTERFACE_TEMPLATE': {
            'definition': [
                "switchport mode access",
                "switchport block unicast",
                "spanning-tree portfast",
                "switchport port-security",
                "spanning-tree bpduguard enable",
                "service-policy input AutoConf-4.0-Trust-Dscp-Input-Policy",
                "service-policy output AutoConf-4.0-Output-Policy"
            ]
        },
        'LAP_INTERFACE_TEMPLATE': {
            'definition': [
                "switchport mode access",
                "switchport block unicast",
                "switchport port-security",
                "switchport port-security aging time 2",
                "switchport port-security violation protect", 
                "switchport port-security aging type inactivity",
                "load-interval 30",
                "storm-control broadcast level pps 1k",
                "storm-control multicast level pps 2k",
                "storm-control action trap",
                "spanning-tree portfast",
                "spanning-tree bpduguard enable",
                "ip dhcp snooping limit rate 15"
            ]
        },
        'TP_INTERFACE_TEMPLATE': {
            'definition': [
                "switchport port-security maximum 3",
                "switchport mode access",
                "switchport port-security maximum 2 vlan access",
                "switchport port-security",
                "switchport port-security aging time 2",
                "switchport port-security violation restrict",
                "switchport port-security aging type inactivity",
                "load-interval 30",
                "storm-control broadcast level pps 1k",
                "storm-control multicast level pps 2k",
                "storm-control action trap",
                "spanning-tree portfast",
                "spanning-tree bpduguard enable",
                "ip dhcp snooping limit rate 15",
                "service-policy input AutoConf-4.0-Trust-Dscp-Input-Policy",
                "service-policy output AutoConf-4.0-Output-Policy"
            ]
        }
    }
}