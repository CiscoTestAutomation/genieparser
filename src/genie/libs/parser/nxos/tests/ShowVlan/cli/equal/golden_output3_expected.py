expected_output = {
    "vlans": {
        "10": {
            "interfaces": [
                "Ethernet1/1",
                "Ethernet1/2"
            ],
            "mode": "ce",
            "name": "STD-VLAN10",
            "shutdown": True,
            "state": "suspend",
            "type": "enet",
            "vlan_id": "10"
        },
        "20": {
            "interfaces": [
                "Ethernet1/11",
                "Ethernet1/12"
            ],
            "mode": "ce",
            "name": "PV-VLAN20-PRIMARY",
            "shutdown": True,
            "state": "active",
            "type": "enet",
            "vlan_id": "20",
            "private_vlan":{
                "primary": True,
                "association": ['25'],
            },
        },
        "25": {
            "interfaces": [
                "Ethernet1/21",
                "Ethernet1/22"
            ],
            "mode": "ce",
            "name": "PV-VLAN25-SEC-ISO",
            "shutdown": True,
            "state": "suspend",
            "type": "enet",
            "vlan_id": "25",
            "private_vlan":{
                "primary": False,
                "type": "isolated",
            },
        },
        "30": {
            "interfaces": [
                "Ethernet1/31",
                "Ethernet1/32"
            ],
            "mode": "ce",
            "name": "PV-VLAN30-SEC-ISO",
            "shutdown": True,
            "state": "active",
            "type": "enet",
            "vlan_id": "30",
        }
    }
}