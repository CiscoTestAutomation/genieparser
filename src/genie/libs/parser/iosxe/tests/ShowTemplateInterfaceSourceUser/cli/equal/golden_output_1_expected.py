expected_output = {
    'template': {
        "Child": {
            'definition': [
                "switchport access vlan 60",
                "switchport mode access",
                "load-interval 60",
                "description Sourcing from interface template Child"
            ]
        },
        "Parent": {
            'definition': [
                "switchport mode access",
                "source template Child",
                "load-interval 30",
                "description Sourcing from interface template Parent"
            ]
        },
        "alpha": {
            'definition': [
                "storm-control broadcast level pps 3k",
                "storm-control multicast level pps 3k",
                "storm-control action trap",
                "spanning-tree portfast",
                "spanning-tree bpduguard enable",
                "switchport mode access",
                "switchport block unicast",
                "switchport port-security maximum 3",
                "switchport port-security maximum 3 vlan access",
                "switchport port-security aging time 3",
                "switchport port-security aging type inactivity",
                "switchport port-security",
                "load-interval 30",
                "description Sourcing interface template alpha",
                "ip dhcp snooping limit rate 30"
            ]
        },
        "beta": {
            'definition': [
                "switchport trunk allowed vlan 3",
                "switchport mode trunk",
                "description Sourcing interface template beta"
            ]
        }
    }
}