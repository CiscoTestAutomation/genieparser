expected_output = {
    "vtp": {
        "version_capable": [1, 2, 3],
        "version": "3",
        "feature": {
            "vlan": {
                "operating_mode": "client",
                "enabled": True,
                "existing_vlans": 47,
                "existing_extended_vlans": 0,
                "maximum_vlans": 2048,
                "configuration_revision": 15,
                "primary_id": "501c.bfff.a91e",
                "primary_description": "sw001",
                "md5_digest": "0x1D 0x23 0x33 0x42 0x62 0x7A 0xA0 0xA7 0xAA 0xB1 0xB3 0xBE 0xD6 0xD7 0xD9 0xE8",
            },
            "mst": {"operating_mode": "transparent", "enabled": False},
        },
        "domain_name": "GENIE",
        "pruning_mode": False,
        "traps_generation": False,
        "device_id": "885a.92ff.7c92",
    }
}
