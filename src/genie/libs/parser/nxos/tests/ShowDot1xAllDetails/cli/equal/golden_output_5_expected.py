expected_output = {
    "system_auth_control": False,
    "version": 3,
    "interfaces": {
        "Ethernet1/2": {
            "interface": "Ethernet1/2",
            "pae": "authenticator",
            "port_control": "not auto",
            "host_mode": "double host",
            "re_authentication": False,
            "timeout": {
                "quiet_period": 59,
                "server_timeout": 29,
                "supp_timeout": 29,
                "tx_period": 29,
                "ratelimit_period": 1,
                "re_auth_period": 59,
                "time_to_next_reauth": 16,
            },
            "re_auth_max": 1,
            "max_req": 2,
            "mac-auth-bypass": True,
            "clients": {
                "53:ab:de:ff:e5:e5": {
                    "client": "53:ab:de:ff:e5:e5",
                    "session": {
                        "auth_sm_state": "authenticated",
                        "auth_bend_sm_state": "idle",
                        "auth_by": "remote",
                        "reauth_action": "reauthenticate",
                    },
                    "auth_method": "eap",
                }
            },
            "port_status": "authorized",
        }
    },
}
