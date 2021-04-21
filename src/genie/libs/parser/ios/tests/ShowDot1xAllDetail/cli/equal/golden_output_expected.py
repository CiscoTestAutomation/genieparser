expected_output = {
    "version": 3,
    "interfaces": {
        "GigabitEthernet1/0/9": {
            "interface": "GigabitEthernet1/0/9",
            "max_start": 3,
            "pae": "supplicant",
            "credentials": "switch4",
            "supplicant": {"eap": {"profile": "EAP-METH"}},
            "timeout": {"held_period": 60, "start_period": 30, "auth_period": 30},
        }
    },
    "system_auth_control": True,
}
