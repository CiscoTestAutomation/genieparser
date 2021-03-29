expected_output = {
    "vrf": {
        "default": {
            "vrf_index": "0x60000000",
            "interfaces": {
                "TenGigE0/3/0/0": {
                    "interface_index": "0xa0004c0",
                    "enabled": {
                        "LDP interface": { "via": "config"}
                    },
                },
                "HundredGigE0/5/0/0": {
                    "interface_index": "0xe0000c0",
                    "disabled": {},
                },
                "HundredGigE0/5/0/0.100": {
                    "interface_index": "0xe0001c0",
                    "disabled": {},
                },
                "TenGigE0/3/0/1.100": {
                    "interface_index": "0xa001940",
                    "disabled": {},
                },
            },
        }
    }
}