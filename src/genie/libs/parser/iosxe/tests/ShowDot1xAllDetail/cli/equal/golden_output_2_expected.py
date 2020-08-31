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
            "max_reauth_req": 2,
            "max_req": 1,
            "clients": {
                "6451.06ff.565e": {
                    "client": "6451.06ff.565e",
                    "eap_method": "(13)",
                    "session": {
                        "0A90740B0000A7FD44A5F6A8": {
                            "session_id": "0A90740B0000A7FD44A5F6A8",
                            "auth_sm_state": "authenticated",
                            "auth_bend_sm_state": "idle",
                        }
                    },
                }
            },
        }
    }
}
