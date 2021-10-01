expected_output = {
    "TenGigabitEthernet5/0/1": {
        "interface_templates": {
            "source_template": {
                 "method": "static",
                 "source": "user",
             }
        },
        "service_templates": {
            "DefaultCriticalAuthVlan_SRV_TEMPLATE": {
                "mac": "40-f0-78-ca-d1-1a",
                "source": "user",
            },
            "DefaultCriticalVoice_SRV_TEMPLATE": {
                "mac": "40-f0-78-ca-d1-1a",
                "source": "user",
            },
        },
    },
}
