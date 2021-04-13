expected_output = {
    "vlans": {
        "10": {
            "interfaces": [
                "Ethernet1/1",
                "Ethernet1/2"
            ],
            "mode": "ce",
            "name": "STD-VLAN10",
            "shutdown": False,
            "state": "active",
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
            "shutdown": False,
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
                "Ethernet1/11",
                "Ethernet1/12"
            ],
            "mode": "ce",
            "name": "PV-VLAN25-SEC-ISO",
            "shutdown": False,
            "state": "active",
            "type": "enet",
            "vlan_id": "25",
            "private_vlan":{
                "primary": False,
                "type": "isolated",
            },
        }
    }
}