expected_output = {
    "pod1": {
        "candidate_default": False,
        "class": "default",
        "mode": "Routed",
        "url": "disk0:/pod-context/pod1",
        "interfaces": ["Vlan100", "Vlan200"],
    },
    "pod2": {
        "candidate_default": False,
        "class": "111",
        "mode": "Routed",
        "url": "disk0:/pod-context/pod2",
        "interfaces": ["Vlan300", "Vlan400"],
    },
    "admin": {
        "candidate_default": True,
        "class": "default",
        "mode": "Routed",
        "url": "disk0:/pod-context/admin.cfg",
        "interfaces": [
            "Vlan1000",
            "Vlan1001",
            "Vlan1030",
            "Vlan1031",
            "Vlan1050",
            "Vlan1051",
            "Vlan1082",
            "Vlan1083",
        ],
    },
}
