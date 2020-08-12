expected_output = {
    "pod1": {
        "context_created": True,
        "id": 2,
        "flags": "0x00000112",
        "class": "default",
        "url": "disk0:/pod-context/pod1",
        "interfaces": {
            "real_interfaces": ["Vlan100", "Vlan200"],
            "mapped_interfaces": ["Vlan100", "Vlan200"],
        },
    },
    "null": {
        "context_created": False,
        "id": 4,
        "flags": "0x00000114",
        "class": "default",
        "url": "... null ...",
    },
    "admin": {
        "context_created": True,
        "id": 1,
        "flags": "0x00000111",
        "class": "default",
        "url": "disk0:/pod-context/admin.cfg",
        "interfaces": {
            "real_interfaces": [
                "Vlan1000",
                "Vlan1001",
                "Vlan1030",
                "Vlan1031",
                "Vlan1032",
                "Vlan993",
                "Vlan994",
                "Vlan995",
                "Vlan996",
                "Vlan997",
                "Vlan998",
                "Vlan999",
            ]
        },
    },
    "pod3": {
        "context_created": True,
        "id": 3,
        "flags": "0x00000113",
        "class": "default",
        "url": "disk0:/pod-context/pod3",
        "interfaces": {
            "real_interfaces": ["Vlan303", "Vlan603"],
            "mapped_interfaces": ["Vlan303", "Vlan603"],
        },
    },
}
