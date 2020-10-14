expected_output = {
    "vtp": {
        "device_id": "3820.56ff.c7a2",
        "feature": {
            "mst": {
                "configuration_revision": 0,
                "enabled": True,
                "operating_mode": "server",
                "primary_id": "0000.0000.0000",
            },
            "unknown": {"enabled": False, "operating_mode": "transparent"},
            "vlan": {
                "configuration_revision": 2,
                "enabled": True,
                "existing_extended_vlans": 0,
                "existing_vlans": 100,
                "maximum_vlans": 4096,
                "md5_digest": "0x15 0x17 0x1A 0x1C 0x25 0x2C 0x3C 0x48 0x6B 0x70 0x7D 0x87 0x92 0xC2 0xC7 0xFC",
                "operating_mode": "primary server",
                "primary_description": "SW1",
                "primary_id": "3820.56ff.c7a2",
            },
        },
        "pruning_mode": False,
        "traps_generation": False,
        "version": "3",
        "version_capable": [1, 2, 3],
    }
}
