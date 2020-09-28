expected_output = {
    "vtp": {
        "version_capable": [1, 2, 3],
        "version": "3",
        "feature": {
            "vlan": {
                "operating_mode": "client",
                "enabled": True,
                "existing_vlans": 40,
                "existing_extended_vlans": 2,
                "configuration_revision": 13,
                "primary_id": "3333.11ff.3333",
                "primary_description": "description",
            },
            "mst": {"operating_mode": "transparent", "enabled": False},
            "unknown": {"operating_mode": "transparent", "enabled": False},
        },
        "domain_name": "Domain-Name",
        "pruning_mode": True,
        "traps_generation": True,
        "device_id": "ffff.aaff.aaaa",
    }
}
