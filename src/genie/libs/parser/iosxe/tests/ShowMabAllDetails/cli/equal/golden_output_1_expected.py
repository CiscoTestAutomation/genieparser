expected_output = {
    "interfaces": {
        "GigabitEthernet2/0/1": {
            "client_mac": {
                "0000.0001.0003": {
                    "authen_status": "SUCCESS",
                    "mab_sm_state": "TERMINATE",
                    "session_id": "000000000000000C82FA130E",
                },
                "0000.0001.0004": {
                    "authen_status": "SUCCESS",
                    "mab_sm_state": "TERMINATE",
                    "session_id": "000000000000000C82FA130F",
                },
            },
            "mac_auth_bypass": "Enabled",
        },
        "GigabitEthernet2/0/2": {
            "client_mac": {
                "0000.0001.0003": {
                    "authen_status": "SUCCESS",
                    "mab_sm_state": "TERMINATE",
                    "session_id": "000000000000000C82FA130E",
                }
            },
            "mac_auth_bypass": "Enabled",
        },
        "GigabitEthernet2/0/3": {
            "client_mac": {}, 
            "mac_auth_bypass": "Enabled"
            },
    }
}
