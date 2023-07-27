expected_output = {
    "interfaces": {
        "TenGigabitEthernet0/1/3": {
            "mtu": 1468,
            "load_interval": "30",
            "mka_policy": "MKAPolicy",
            "mka_primary_keychain": "KCP256",
            "macsec_access_control": "should-secure",
            "macsec_enabled": True,
            "channel_group": {
                "chg": 1,
                "mode": "active"
            }
        }
    }
}
