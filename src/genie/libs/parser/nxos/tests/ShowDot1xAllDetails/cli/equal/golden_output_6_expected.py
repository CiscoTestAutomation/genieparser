expected_output = {
    "interfaces": {
        "GigabitEthernet1/6": {
            "interface": "GigabitEthernet1/6",
            "pae": "authenticator",
            "timeout": {
                "quiet_period": 3,
                "server_timeout": 0,
                "supp_timeout": 15,
                "tx_period": 1,
            },
            "re_auth_max": 2,
            "max_req": 1,
            "clients": {
                "6451.06ff.565e": {
                    "client": "6451.06ff.565e",
                    "eap_method": "(13)",
                    "session": {
                        "session_id": "0a90740b0000a7fd44a5f6a8",
                        "auth_sm_state": "authenticated",
                        "auth_bend_sm_state": "idle",
                    },
                }
            },
        }
    }
}
